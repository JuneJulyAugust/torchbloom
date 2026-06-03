# src/torchbloom/udl_ocr_parse.py
"""Pure parsing of DeepSeek-OCR-2 grounding output into Markdown + figure boxes.

Ported from Mac-M5-Deepseek-OCR-2/mlx/pdf_ocr.py. No MLX/model/Pillow imports —
this module is unit-testable on raw-text fixtures. The shell crops figures.
"""

from __future__ import annotations

import re

_TAG_RE = re.compile(
    r"<\|ref\|>(?P<type>.*?)<\|/ref\|><\|det\|>\[(?P<coords>.*?)\]<\|/det\|>"
)
_BOX_RE = re.compile(r"\[?(\d+),\s*(\d+),\s*(\d+),\s*(\d+)\]?")


def parse_elements(raw_text: str) -> list[dict]:
    matches = list(_TAG_RE.finditer(raw_text))
    elements: list[dict] = []
    for idx, match in enumerate(matches):
        coords = [
            [int(b.group(1)), int(b.group(2)), int(b.group(3)), int(b.group(4))]
            for b in _BOX_RE.finditer(match.group("coords"))
        ]
        start_idx = match.end()
        end_idx = matches[idx + 1].start() if idx + 1 < len(matches) else len(raw_text)
        elements.append(
            {
                "type": match.group("type"),
                "coords": coords,
                "content": raw_text[start_idx:end_idx].strip(),
            }
        )
    return elements


def _clean_inline(text: str) -> str:
    text = re.sub(r"<\|ref\|>.*?<\|/ref\|>", "", text)
    text = re.sub(r"<\|det\|>.*?<\|/det\|>", "", text)
    return text.strip()


def _element_bbox(coords: list[list[int]]) -> list[int] | None:
    if not coords:
        return None
    return [
        min(c[0] for c in coords),
        min(c[1] for c in coords),
        max(c[2] for c in coords),
        max(c[3] for c in coords),
    ]


# append to src/torchbloom/udl_ocr_parse.py
def merge_figures(elements: list[dict]):
    """Union touching/overlapping *image* fragments into figure crop boxes.
    Text is never absorbed (avoids the multi-column gutter-jump bug). Returns
    (fig_crops, absorbed_idxs) where fig_crops is [(rep_element_idx, box)] and
    absorbed_idxs is always empty.
    """
    boxes = {}
    for idx, el in enumerate(elements):
        if el["type"] == "image":
            b = _element_bbox(el["coords"])
            if b:
                boxes[idx] = b

    def overlap(a, b):
        ox = min(a[2], b[2]) - max(a[0], b[0])
        oy = min(a[3], b[3]) - max(a[1], b[1])
        return ox > -10 and oy > -10

    idxs = list(boxes)
    parent = {i: i for i in idxs}

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    for a in range(len(idxs)):
        for b in range(a + 1, len(idxs)):
            ia, ib = idxs[a], idxs[b]
            if overlap(boxes[ia], boxes[ib]):
                parent[find(ia)] = find(ib)

    groups: dict[int, list[int]] = {}
    for i in idxs:
        groups.setdefault(find(i), []).append(i)

    fig_crops = []
    for members in groups.values():
        rep = min(members)
        x1 = min(boxes[m][0] for m in members)
        y1 = min(boxes[m][1] for m in members)
        x2 = max(boxes[m][2] for m in members)
        y2 = max(boxes[m][3] for m in members)
        fig_crops.append((rep, [x1, y1, x2, y2]))
    return fig_crops, set()


# append to src/torchbloom/udl_ocr_parse.py
def _largest_empty_rect(grid):
    """Largest all-False rectangle in a boolean grid (histogram method)."""
    n = len(grid)
    best = (0, None)
    heights = [0] * n
    for r in range(n):
        for c in range(n):
            heights[c] = 0 if grid[r][c] else heights[c] + 1
        stack = []
        for c in range(n + 1):
            cur = heights[c] if c < n else 0
            start = c
            while stack and stack[-1][1] > cur:
                s, h = stack.pop()
                area = h * (c - s)
                if area > best[0]:
                    best = (area, (s, r - h + 1, c - 1, r))
                start = s
            stack.append((start, cur))
    return best


def detect_uncovered_figure(elements):
    """Recover a large central diagram the model failed to emit as an image.
    Returns a per-mille crop box [x1,y1,x2,y2] or None. (Verbatim port.)"""
    boxes = [b for b in (_element_bbox(e["coords"]) for e in elements) if b]
    if not boxes:
        return None
    img_boxes = [
        b for b in (_element_bbox(e["coords"]) for e in elements if e["type"] == "image") if b
    ]
    prose_boxes = [
        b for b in (
            _element_bbox(e["coords"]) for e in elements
            if e["type"] in ("text", "sub_title")
        )
        if b and (b[2] - b[0]) >= 300 and (b[3] - b[1]) >= 120
    ]

    N = 50
    grid = [[False] * N for _ in range(N)]
    for x1, y1, x2, y2 in boxes:
        for gy in range(max(0, y1 * N // 1000), min(N, y2 * N // 1000 + 1)):
            for gx in range(max(0, x1 * N // 1000), min(N, x2 * N // 1000 + 1)):
                grid[gy][gx] = True

    area, rect = _largest_empty_rect(grid)
    if not rect:
        return None
    gx1, gy1, gx2, gy2 = rect
    px1, py1 = gx1 * 1000 // N, gy1 * 1000 // N
    px2, py2 = (gx2 + 1) * 1000 // N, (gy2 + 1) * 1000 // N

    width_pct, height_pct = px2 - px1, py2 - py1
    area_pct = area * 100 // (N * N)
    if area_pct < 8 or height_pct < 25 or width_pct < 18:
        return None
    if px1 < 50 or px2 > 950:
        return None

    def overlaps_y(b):
        return min(b[3], py2) - max(b[1], py1) > 0

    has_left = any(b[2] <= px1 + 20 and overlaps_y(b) for b in boxes)
    has_right = any(b[0] >= px2 - 20 and overlaps_y(b) for b in boxes)
    if not (has_left and has_right):
        return None

    bottom_band_top = min((b[1] for b in img_boxes if b[1] > 720), default=985)
    upper = [b for b in boxes if b[1] < bottom_band_top]
    crop_y1 = max(0, min(b[1] for b in upper) - 10)
    crop_y2 = min(bottom_band_top - 8, 990)
    if crop_y2 - crop_y1 < 30:
        return None

    def y_overlaps_crop(b):
        return min(b[3], crop_y2) - max(b[1], crop_y1) > 0

    left_x, right_x = 0, 1000
    right_prose = [b for b in prose_boxes if (b[0] + b[2]) / 2 > px2 and y_overlaps_crop(b)]
    if right_prose:
        right_x = max(px2, min(b[0] for b in right_prose) - 15)
    left_prose = [b for b in prose_boxes if (b[0] + b[2]) / 2 < px1 and y_overlaps_crop(b)]
    if left_prose:
        left_x = min(px1, max(b[2] for b in left_prose) + 15)
    if right_x - left_x < 150:
        return None
    return [left_x, crop_y1, right_x, crop_y2]


# append to src/torchbloom/udl_ocr_parse.py
def build_caption(fig_box, elements) -> str:
    """Formal 'Figure N.N ...' caption near the figure + short overlay labels.
    Verbatim port from pdf_ocr.py build_caption."""
    fx1, fy1, fx2, fy2 = fig_box
    formal = None
    labels: list[str] = []
    for el in elements:
        if el["type"] == "image":
            continue
        b = _element_bbox(el["coords"])
        if not b:
            continue
        content = re.sub(r"^#+\s*", "", _clean_inline(el["content"])).strip()
        if not content:
            continue
        bcx, bcy = (b[0] + b[2]) / 2, (b[1] + b[3]) / 2

        m = re.match(r"^[\W]*Figure\s+\d+\.\d+\b[.\s:–-]*(.*)", content, re.IGNORECASE)
        if m and formal is None:
            near = (fx1 - 120 <= bcx <= fx2 + 120) and (fy1 - 120 <= bcy <= fy2 + 120)
            if near:
                formal = re.split(r"(?<=[.])\s", content)[0][:200]
                continue

        inside = (fx1 <= bcx <= fx2) and (fy1 <= bcy <= fy2)
        below = (fx1 - 30 <= bcx <= fx2 + 30) and (fy2 <= bcy <= fy2 + 45)
        if not (inside or below):
            continue
        for line in content.split("\n"):
            head = line.split(":")[0].strip()
            if ":" in line and 0 < len(head) <= 40:
                labels.append(head)
            elif 0 < len(line.strip()) <= 50:
                labels.append(line.strip())

    parts = []
    if formal:
        parts.append(formal)
    if labels:
        uniq = list(dict.fromkeys(labels))[:12]
        parts.append("Labels: " + ", ".join(uniq))
    return " — ".join(parts)[:300]


def _figure_block(fig_idx: int, caption: str, page_num: int) -> str:
    ref = f"![Figure {fig_idx}](../../figures/page_{page_num:04d}_fig_{fig_idx}.png)"
    if caption:
        return f"**Figure {fig_idx}** — {caption}\n\n{ref}"
    return f"**Figure {fig_idx}**\n\n{ref}"


def reconstruct_markdown(elements, fig_info: dict, page_num: int) -> str:
    """fig_info maps an image element index -> (fig_idx, caption)."""
    parts = []
    for idx, el in enumerate(elements):
        if el["type"] == "image":
            info = fig_info.get(idx)
            if info:
                parts.append(_figure_block(info[0], info[1], page_num))
        else:
            parts.append(_clean_inline(el["content"]))

    raw_md = "\n\n".join(p for p in parts if p.strip())
    raw_md = re.sub(r"\n{3,}", "\n\n", raw_md)

    def norm(s):
        return re.sub(r"^\W+", "", s.strip())

    blocks = raw_md.split("\n\n")
    deduped: list[str] = []
    for b in blocks:
        if deduped and norm(b) and norm(b) == norm(deduped[-1]):
            continue
        deduped.append(b)
    return "\n\n".join(deduped).strip()


def _yaml_str(s) -> str:
    return '"' + str(s).replace("\\", "\\\\").replace('"', "'") + '"'


def parse_grounding_to_crops(raw_text: str, page_num: int):
    """Parse grounding output. Returns (clean_markdown, crops, meta) where
    crops = [(fig_idx, [x1,y1,x2,y2] per-mille)] in reading order (the recovered
    central diagram, if any, is fig 1). The shell crops the image from these boxes.
    """
    elements = parse_elements(raw_text)
    if not elements:
        return _clean_inline(raw_text), [], {"headings": [], "chapter": None}

    fig_crops, _ = merge_figures(elements)
    fig_crops_dict = dict(fig_crops)

    crops: list[tuple[int, list[int]]] = []
    fig_info: dict[int, tuple[int, str]] = {}
    fig_idx = 1
    main_fig_block = None

    main_box = detect_uncovered_figure(elements)
    if main_box:
        crops.append((fig_idx, main_box))
        main_fig_block = _figure_block(fig_idx, build_caption(main_box, elements), page_num)
        fig_idx += 1

    for idx, el in enumerate(elements):
        if el["type"] == "image" and idx in fig_crops_dict:
            box = fig_crops_dict[idx]
            crops.append((fig_idx, box))
            fig_info[idx] = (fig_idx, build_caption(box, elements))
            fig_idx += 1

    clean_md = reconstruct_markdown(elements, fig_info, page_num)
    if main_fig_block:
        clean_md = f"{main_fig_block}\n\n{clean_md}"

    headings = [
        re.sub(r"^#+\s*", "", _clean_inline(el["content"])).strip()
        for el in elements if el["type"] == "sub_title"
    ]
    headings = [h for h in headings if h]
    chap = re.search(r"CHAPTER\s+(\d+)\s+([A-Z][^\n]{2,45})", raw_text)
    chapter = f"{chap.group(1)} — {chap.group(2).strip()}" if chap else None
    return clean_md, crops, {"headings": headings, "chapter": chapter}


def build_frontmatter(source, page_key, pdf_page, title, chapter, chapter_slug, figures, headings) -> str:
    lines = ["---", f"source: {source}", f"page_key: {page_key}", f"pdf_page: {pdf_page}", f"title: {_yaml_str(title)}"]
    if chapter:
        lines.append(f"chapter: {_yaml_str(chapter)}")
    if chapter_slug:
        lines.append(f"chapter_slug: {chapter_slug}")
    lines.append(f"figure_count: {len(figures)}")
    if figures:
        lines.append("figures:")
        lines += [f"  - {f}" for f in figures]
    uniq = list(dict.fromkeys(headings))[:12]
    if uniq:
        lines.append("headings:")
        lines += [f"  - {_yaml_str(h)}" for h in uniq]
    lines.append("---")
    return "\n".join(lines)


_FIGURE_TITLE_RE = re.compile(r"^[\s\W]*?(Figure\s+\d+(?:\.\d+)?\b.*)", re.IGNORECASE)


def parse_figure_title(strip_ocr_text: str, clean_md: str):
    """Pure half of figure-title-banner recovery. Input is the free-OCR text of the
    page's top strip; output is the title string or None. Verbatim port of the
    text-parsing portion of pdf_ocr.py extract_figure_title (lines 448–477)."""
    lines = [ln.strip() for ln in strip_ocr_text.splitlines()]
    start = next((i for i, ln in enumerate(lines) if ln and _FIGURE_TITLE_RE.match(ln)), None)
    if start is None:
        return None
    m = _FIGURE_TITLE_RE.match(lines[start])
    parts = [m.group(1).strip()]
    for ln in lines[start + 1:]:
        if not ln:
            break
        if ln.startswith("---") or _FIGURE_TITLE_RE.match(ln):
            break
        if not re.search(r"\w", ln):
            break
        parts.append(ln)
        if sum(len(p) for p in parts) > 90:
            break
    title = re.sub(r"[*_`]", "", " ".join(parts))
    title = re.sub(r"\s{2,}", " ", title).strip().rstrip(".").strip()
    if len(title) > 90:
        return None
    fig_id = re.match(r"Figure\s+\d+(?:\.\d+)?", title, re.IGNORECASE)
    if fig_id and fig_id.group(0).lower() in clean_md.lower():
        return None
    return title
