"""Prepare and validate UDL hybrid OCR fusion pilot artifacts."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import json
import re
import shutil
import sys
from pathlib import Path
from typing import Any

import yaml


DEFAULT_RAW_ROOT = Path("raw/udl/textbook")
DEFAULT_PADDLE_PAGES_DIR = Path("output/udl-ocr-comparison/paddleocr-structure/pages")
DEFAULT_OUTPUT_DIR = Path("output/udl-fusion-pilot")
DEFAULT_PDF_PATH = Path("raw/udl/source/UnderstandingDeepLearning_02_09_26_C.pdf")
DEFAULT_BOOK_PAGE_OFFSET = 14
FINAL_VISUAL_CROP_KINDS = {"chart", "image", "table"}
FIGURE_RE = re.compile(
    r"img_in_(?P<kind>[a-z]+)_box_(?P<x1>\d+)_(?P<y1>\d+)_(?P<x2>\d+)_(?P<y2>\d+)",
    re.IGNORECASE,
)
IMAGE_LINK_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
HTML_IMG_RE = re.compile(r"<img\b[^>]*\bsrc=[\"']([^\"']+)[\"'][^>]*>", re.IGNORECASE)
CENTERED_HTML_IMG_RE = re.compile(
    r"<p\s+align=[\"']center[\"']>\s*<img\b[^>]*\bsrc=[\"']([^\"']+)[\"'][^>]*>\s*</p>",
    re.IGNORECASE | re.DOTALL,
)
DISPLAY_MATH_BRACKET_RE = re.compile(r"\\\[|\\\]")
INLINE_MATH_PAREN_RE = re.compile(r"\\\(|\\\)")
GITHUB_BLOCKED_MATH_MACRO_RE = re.compile(r"\\operatorname\b")
INLINE_ESCAPED_BRACE_RE = re.compile(r"\$[^\n$]*\\[{}][^\n$]*\$")
DISPLAY_MATH_BLOCK_RE = re.compile(r"(?ms)^\$\$\n(?P<body>.*?)\n\$\$")
INLINE_SUPERSCRIPT_FOOTNOTE_RE = re.compile(r"\$\^\d+\$")
FIGURE_CAPTION_START_RE = re.compile(r"(?m)^Figure\s+\d+\.\d+\b")
FIGURE_CAPTION_BLOCK_RE = re.compile(r"^Figure\s+\d+\.\d+\b", re.DOTALL)
CENTERED_FIGURE_CAPTION_RE = re.compile(
    r"^<p\s+align=[\"']center[\"']>\s*<strong>Figure\s+\d+\.\d+</strong>.*</p>$",
    re.IGNORECASE | re.DOTALL,
)
REVIEW_NOTE_TEXT_RE = re.compile(r"(?im)^\s*>?\s*review note\b")
REQUIRED_FRONTMATTER = {
    "source",
    "page_key",
    "book_page",
    "pdf_page",
    "chapter",
    "chapter_slug",
    "ocr_sources",
    "fusion_status",
    "confidence",
    "figure_count",
}
REQUIRED_BLOCK_KEYS = {"id", "page_key", "order", "type", "source", "confidence"}
SUPPORTED_BLOCK_TYPES = {
    "heading",
    "paragraph",
    "equation",
    "figure",
    "caption",
    "table",
    "list",
    "exercise",
    "review_note",
}


@dataclass(frozen=True)
class Chapter:
    number: int
    title: str
    slug: str
    pdf_start: int
    pdf_end: int

    @property
    def label(self) -> str:
        return f"{self.number} - {self.title}"

    @property
    def short_slug(self) -> str:
        return f"ch{self.number:02d}"

    @property
    def pages(self) -> range:
        return range(self.pdf_start, self.pdf_end + 1)


@dataclass(frozen=True)
class PageSpec:
    chapter: Chapter
    page: int
    book_page_offset: int = DEFAULT_BOOK_PAGE_OFFSET

    @property
    def pdf_page(self) -> int:
        return self.page

    @property
    def book_page(self) -> int:
        return self.page - self.book_page_offset

    @property
    def source_key(self) -> str:
        return f"page_{self.page:04d}"

    @property
    def key(self) -> str:
        return f"page_{self.book_page:04d}"


def load_chapters(chapter_map_path: Path) -> list[Chapter]:
    data = json.loads(chapter_map_path.read_text(encoding="utf-8"))
    return [Chapter(**item) for item in data]


def select_pages(chapters: list[Chapter], chapter_text: str, book_page_offset: int = DEFAULT_BOOK_PAGE_OFFSET) -> list[PageSpec]:
    wanted = {int(value) for value in chapter_text.split(",") if value.strip()}
    by_number = {chapter.number: chapter for chapter in chapters}
    missing = sorted(wanted - set(by_number))
    if missing:
        raise ValueError(f"chapter(s) not found in map: {missing}")

    specs: list[PageSpec] = []
    for number in sorted(wanted):
        chapter = by_number[number]
        specs.extend(PageSpec(chapter=chapter, page=page, book_page_offset=book_page_offset) for page in chapter.pages)
    return specs


def deepseek_page_path(raw_root: Path, spec: PageSpec) -> Path:
    return raw_root / "pages" / spec.chapter.slug / f"{spec.source_key}.md"


def deepseek_raw_path(raw_root: Path, spec: PageSpec) -> Path:
    return raw_root / "raw_ocr" / f"{spec.source_key}.txt"


def page_image_path(raw_root: Path, spec: PageSpec) -> Path:
    return raw_root / "images" / f"{spec.source_key}.png"


def paddle_page_dir(paddle_pages_dir: Path, spec: PageSpec) -> Path:
    return paddle_pages_dir / spec.source_key


def paddle_markdown_path(paddle_pages_dir: Path, spec: PageSpec) -> Path:
    page_dir = paddle_page_dir(paddle_pages_dir, spec)
    combined = page_dir / f"{spec.source_key}.combined.md"
    if combined.exists():
        return combined
    return page_dir / f"{spec.source_key}.md"


def fused_markdown_path(output_dir: Path, spec: PageSpec) -> Path:
    return output_dir / "fused" / spec.chapter.short_slug / f"{spec.key}.md"


def blocks_json_path(output_dir: Path, spec: PageSpec) -> Path:
    return output_dir / "blocks" / spec.chapter.short_slug / f"{spec.key}.blocks.json"


def published_markdown_path(dest_root: Path, spec: PageSpec) -> Path:
    return dest_root / "pages" / spec.chapter.slug / f"{spec.key}.md"


def published_blocks_path(dest_root: Path, spec: PageSpec) -> Path:
    return dest_root / "blocks" / spec.chapter.short_slug / f"{spec.key}.blocks.json"


def _copy_file(src: Path, dest: Path) -> None:
    if not src.exists():
        raise FileNotFoundError(src)
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)


def _layout_size_for_image(width: int, height: int, layout_width: int) -> tuple[int, int]:
    return layout_width, round(height * layout_width / width)


def _scale_bbox(
    bbox: list[int],
    image_size: tuple[int, int],
    layout_width: int,
    pad_layout: int = 0,
    pad_left: int | None = None,
    pad_top: int | None = None,
    pad_right: int | None = None,
    pad_bottom: int | None = None,
) -> tuple[int, int, int, int]:
    image_width, image_height = image_size
    layout_w, layout_h = _layout_size_for_image(image_width, image_height, layout_width)
    x_scale = image_width / layout_w
    y_scale = image_height / layout_h
    pad_left = pad_layout if pad_left is None else pad_left
    pad_top = pad_layout if pad_top is None else pad_top
    pad_right = pad_layout if pad_right is None else pad_right
    pad_bottom = pad_layout if pad_bottom is None else pad_bottom
    x1, y1, x2, y2 = bbox
    x1, x2 = sorted((x1 - pad_left, x2 + pad_right))
    y1, y2 = sorted((y1 - pad_top, y2 + pad_bottom))
    left = max(0, round(x1 * x_scale))
    top = max(0, round(y1 * y_scale))
    right = min(image_width, round(x2 * x_scale))
    bottom = min(image_height, round(y2 * y_scale))
    right = max(right, left + 1)
    bottom = max(bottom, top + 1)
    return left, top, right, bottom


def _figure_meta(path: Path, spec: PageSpec, index: int) -> dict[str, Any]:
    match = FIGURE_RE.search(path.stem)
    kind = _crop_kind(path)
    bbox = None
    if match:
        bbox = [int(match.group(name)) for name in ("x1", "y1", "x2", "y2")]

    stable_name = f"{spec.key}_fig_{index}{path.suffix.lower()}"
    return {
        "index": index,
        "kind": kind,
        "bbox": bbox,
        "source_name": path.name,
        "input_path": f"inputs/{spec.source_key}/paddle_figures/{path.name}",
        "stable_path": f"figures/{stable_name}",
    }


def _crop_kind(path: Path) -> str:
    match = FIGURE_RE.search(path.stem)
    return match.group("kind") if match else "image"


def page_figure_paths(paddle_pages_dir: Path, spec: PageSpec) -> list[Path]:
    imgs = paddle_page_dir(paddle_pages_dir, spec) / "imgs"
    if not imgs.exists():
        return []
    return sorted(
        (path for path in imgs.iterdir() if path.is_file()),
        key=lambda path: (_crop_kind(path) not in FINAL_VISUAL_CROP_KINDS, path.name),
    )


def build_manifest(
    output_dir: Path,
    raw_root: Path,
    paddle_pages_dir: Path,
    spec: PageSpec,
    figures: list[dict[str, Any]],
) -> dict[str, Any]:
    return {
        "page_key": spec.book_page,
        "page_name": spec.key,
        "book_page": spec.book_page,
        "pdf_page": spec.pdf_page,
        "source_pdf_page_name": spec.source_key,
        "chapter_number": spec.chapter.number,
        "chapter_title": spec.chapter.title,
        "chapter_slug": spec.chapter.slug,
        "chapter_short_slug": spec.chapter.short_slug,
        "inputs": {
            "deepseek_markdown": f"inputs/{spec.source_key}/deepseek.md",
            "deepseek_raw": f"inputs/{spec.source_key}/deepseek_raw.txt",
            "paddle_markdown": f"inputs/{spec.source_key}/paddle.md",
            "original_page_image": f"inputs/{spec.source_key}/original_page.png",
        },
        "source_paths": {
            "deepseek_markdown": str(deepseek_page_path(raw_root, spec)),
            "deepseek_raw": str(deepseek_raw_path(raw_root, spec)),
            "paddle_markdown": str(paddle_markdown_path(paddle_pages_dir, spec)),
            "original_page_image": str(page_image_path(raw_root, spec)),
        },
        "figures": figures,
        "expected_outputs": {
            "fused_markdown": str(fused_markdown_path(output_dir, spec)),
            "blocks_json": str(blocks_json_path(output_dir, spec)),
        },
    }


def prompt_text(manifest: dict[str, Any]) -> str:
    page_name = manifest["page_name"]
    visual_figures = [
        fig for fig in manifest["figures"] if fig["kind"] in FINAL_VISUAL_CROP_KINDS
    ]
    evidence_only_figures = [
        fig for fig in manifest["figures"] if fig["kind"] not in FINAL_VISUAL_CROP_KINDS
    ]
    visual_lines = "\n".join(
        f"- {fig['stable_path']} ({fig['kind']}, bbox={fig['bbox']})" for fig in visual_figures
    )
    if not visual_lines:
        visual_lines = "- No final visual crops for this page."
    evidence_lines = "\n".join(
        f"- {fig['stable_path']} ({fig['kind']}, bbox={fig['bbox']})" for fig in evidence_only_figures
    )
    if not evidence_lines:
        evidence_lines = "- No evidence-only formula/table crops for this page."

    return f"""# Fusion Prompt: {page_name}

You are producing a private source-derived OCR fusion page for TorchBloom.
Do not call external APIs. Use the evidence files already prepared for this page.

## Page

- Book page: {manifest["book_page"]}
- PDF page: {manifest["pdf_page"]}
- Chapter: {manifest["chapter_number"]} - {manifest["chapter_title"]}
- DeepSeek Markdown: `{manifest["inputs"]["deepseek_markdown"]}`
- DeepSeek raw OCR: `{manifest["inputs"]["deepseek_raw"]}`
- PPStructureV3 Markdown: `{manifest["inputs"]["paddle_markdown"]}`
- Original page image: `{manifest["inputs"]["original_page_image"]}`
- Output Markdown: `{manifest["expected_outputs"]["fused_markdown"]}`
- Output blocks JSON: `{manifest["expected_outputs"]["blocks_json"]}`

## PPStructureV3 Final Visual Crops

These are the only crop paths that may appear as final centered HTML image blocks or JSON `figure.image_path` values. In Markdown files under `fused/chXX/`, link them as `../../figures/...`, not `figures/...`.

Use this exact centered image form for final visual crops:

```html
<p align="center">
  <img src="../../figures/{page_name}_fig_1.jpg" alt="Figure caption or short label" />
</p>
```

Place the figure caption immediately after the image as centered HTML and bold only the figure label:

```html
<p align="center">
  <strong>Figure 3.14</strong> Processing in network...
</p>
```

{visual_lines}

## PPStructureV3 Evidence-Only Crops

Use these to check transcription, especially equations, but do not include them as final Markdown images or JSON figure blocks. If a formula crop is readable, transcribe it as LaTeX in an `equation` block. If it is not readable, add a `review_note` block.

{evidence_lines}

## Fusion Rules

1. Use PPStructureV3 for page layout and figure crop boundaries.
2. Use DeepSeek as the first candidate for prose and LaTeX-style math.
3. Preserve stable PPStructureV3 visual crop paths in figure blocks and centered HTML image blocks.
4. Never include `formula` crops as final images or JSON figure blocks; keep only LaTeX equations in final output.
5. If Paddle has an equation only as an image and DeepSeek does not have trustworthy LaTeX, leave the content as normal prose/math only when it can be grounded in the page evidence.
6. Do not invent content not supported by the two OCR sources.
7. Do not include review-note text in final Markdown frontmatter or body.
8. Center figure caption text and bold the `Figure X.Y` label.
9. Use GitHub-compatible display math delimiters: `$$` on a line before and after display equations. Do not use `\\[` and `\\]` for display math.
10. Use GitHub-compatible inline math delimiters: `$...$`. Do not use `\\(...\\)` inline math.
11. Avoid GitHub-blocked math macros. Use `\\mathrm{{ReLU}}`, `\\mathrm{{argmin}}`, or `\\mathrm{{HardSwish}}` instead of `\\operatorname{{...}}`.
12. In inline math, write literal set braces as `\\lbrace ...\\rbrace`, not `\\{{...\\}}`, so GitHub does not consume the escaping before MathJax sees it.
13. Wrap every numbered display equation that uses `\\tag{{...}}` in a `\\begin{{aligned}} ... \\end{{aligned}}` environment, even if it has only one line. GitHub renders unwrapped tagged equations poorly.
14. Use Markdown footnotes such as `[^1]` and `[^1]: ...`; do not use `$^1$` as a footnote marker.

## Required Markdown Frontmatter

```yaml
source: UnderstandingDeepLearning_02_09_26_C.pdf
page_key: {manifest["page_key"]}
book_page: {manifest["book_page"]}
pdf_page: {manifest["pdf_page"]}
chapter: "{manifest["chapter_number"]} - {manifest["chapter_title"]}"
chapter_slug: {manifest["chapter_slug"]}
ocr_sources:
  - deepseek-ocr-2
  - ppstructurev3
fusion_status: fused
confidence: medium
figure_count: {len(visual_figures)}
```

## Blocks JSON Contract

Write a JSON array. Each block must include:

- `id`: `{page_name}-b001`, `{page_name}-b002`, and so on
- `page_key`: {manifest["page_key"]}
- `order`: integer reading order
- `type`: heading, paragraph, equation, figure, caption, table, list, exercise, or review_note
- `source`: deepseek, paddle, deepseek+paddle, or codex-fusion
- `confidence`: high, medium, or low

For figure blocks, include `image_path`, using the output-root stable path such as `figures/{page_name}_fig_1.jpg`. Do not put `image_path` on equation blocks.

Prefer readable Markdown and compact JSON over verbose commentary.
"""


def prepare_page(output_dir: Path, raw_root: Path, paddle_pages_dir: Path, spec: PageSpec) -> dict[str, Any]:
    input_dir = output_dir / "inputs" / spec.source_key
    _copy_file(deepseek_page_path(raw_root, spec), input_dir / "deepseek.md")
    raw_path = deepseek_raw_path(raw_root, spec)
    if raw_path.exists():
        _copy_file(raw_path, input_dir / "deepseek_raw.txt")
    else:
        (input_dir / "deepseek_raw.txt").write_text("", encoding="utf-8")
    _copy_file(paddle_markdown_path(paddle_pages_dir, spec), input_dir / "paddle.md")
    _copy_file(page_image_path(raw_root, spec), input_dir / "original_page.png")

    figure_metas: list[dict[str, Any]] = []
    for index, src in enumerate(page_figure_paths(paddle_pages_dir, spec), start=1):
        meta = _figure_meta(src, spec, index)
        _copy_file(src, output_dir / meta["input_path"])
        _copy_file(src, output_dir / meta["stable_path"])
        figure_metas.append(meta)

    manifest = build_manifest(output_dir, raw_root, paddle_pages_dir, spec, figure_metas)
    (input_dir / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    prompt_dir = output_dir / "prompts"
    prompt_dir.mkdir(parents=True, exist_ok=True)
    (prompt_dir / f"{spec.key}.md").write_text(prompt_text(manifest), encoding="utf-8")
    return manifest


def write_prepare_summary(output_dir: Path, manifests: list[dict[str, Any]]) -> None:
    output_dir.joinpath("reports").mkdir(parents=True, exist_ok=True)
    chapters: dict[str, int] = {}
    figure_count = 0
    for manifest in manifests:
        key = manifest["chapter_short_slug"]
        chapters[key] = chapters.get(key, 0) + 1
        figure_count += len(manifest["figures"])

    lines = [
        "# UDL Fusion Pilot Summary",
        "",
        "Prepared evidence for Codex-session fusion. No external LLM API is used by this utility.",
        "",
        f"- Pages prepared: {len(manifests)}",
        f"- PPStructureV3 figure crops copied: {figure_count}",
        "- Evidence inputs: `inputs/page_XXXX/`",
        "- Per-page prompts: `prompts/page_XXXX.md`",
        "- Fused Markdown target: `fused/chXX/page_XXXX.md`",
        "- Blocks JSON target: `blocks/chXX/page_XXXX.blocks.json`",
        "",
        "## Chapter Counts",
        "",
    ]
    for chapter, count in sorted(chapters.items()):
        lines.append(f"- {chapter}: {count} pages")
    lines.extend(
        [
            "",
            "## Next Step",
            "",
            "Assign Codex subagents by chapter to read the prepared prompts and write the fused outputs.",
            "",
        ]
    )
    (output_dir / "reports" / "summary.md").write_text("\n".join(lines), encoding="utf-8")


def prepare(args: argparse.Namespace) -> int:
    raw_root = Path(args.raw_root)
    paddle_pages_dir = Path(args.paddle_pages_dir)
    output_dir = Path(args.output_dir)
    chapters = load_chapters(raw_root / "chapter_map.json")
    specs = select_pages(chapters, args.chapters, args.book_page_offset)

    manifests = [prepare_page(output_dir, raw_root, paddle_pages_dir, spec) for spec in specs]
    write_prepare_summary(output_dir, manifests)
    print(f"prepared {len(manifests)} pages in {output_dir}")
    return 0


def refresh_prompts(args: argparse.Namespace) -> int:
    output_dir = Path(args.output_dir)
    raw_root = Path(args.raw_root)
    chapters = load_chapters(raw_root / "chapter_map.json")
    specs = select_pages(chapters, args.chapters, args.book_page_offset)

    prompt_dir = output_dir / "prompts"
    prompt_dir.mkdir(parents=True, exist_ok=True)
    written = 0
    for spec in specs:
        manifest_path = _manifest_path(output_dir, spec)
        if not manifest_path.exists():
            raise FileNotFoundError(manifest_path)
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        (prompt_dir / f"{spec.key}.md").write_text(prompt_text(manifest), encoding="utf-8")
        written += 1

    print(f"refreshed {written} prompts in {prompt_dir}")
    return 0


def _open_image(path: Path):
    from PIL import Image

    image = Image.open(path)
    return image.convert("RGB")


def _render_pdf_page(pdf_path: Path, page_number: int, dpi: int):
    from PIL import Image
    import fitz

    with fitz.open(pdf_path) as doc:
        page = doc.load_page(page_number - 1)
        pix = page.get_pixmap(matrix=fitz.Matrix(dpi / 72.0, dpi / 72.0), alpha=False)
    return Image.frombytes("RGB", (pix.width, pix.height), pix.samples)


def _save_crop(
    image,
    bbox: list[int],
    dest: Path,
    layout_width: int,
    pad_layout: int,
    quality: int,
    pad_left: int | None = None,
    pad_top: int | None = None,
    pad_right: int | None = None,
    pad_bottom: int | None = None,
) -> dict[str, Any]:
    dest.parent.mkdir(parents=True, exist_ok=True)
    crop_box = _scale_bbox(
        bbox,
        image.size,
        layout_width=layout_width,
        pad_layout=pad_layout,
        pad_left=pad_left,
        pad_top=pad_top,
        pad_right=pad_right,
        pad_bottom=pad_bottom,
    )
    crop = image.crop(crop_box)
    save_kwargs: dict[str, Any] = {}
    if dest.suffix.lower() in {".jpg", ".jpeg"}:
        save_kwargs = {"quality": quality, "subsampling": 0, "optimize": True}
    crop.save(dest, **save_kwargs)
    return {"crop_box": list(crop_box), "size": list(crop.size)}


def recrop_figures(args: argparse.Namespace) -> int:
    output_dir = Path(args.output_dir)
    raw_root = Path(args.raw_root)
    page_image_root = Path(args.page_image_root) if args.page_image_root else None
    pdf_path = Path(args.pdf_path)
    chapters = load_chapters(raw_root / "chapter_map.json")
    specs = select_pages(chapters, args.chapters, args.book_page_offset)
    report_entries: list[dict[str, Any]] = []
    if args.pad_layout is None:
        pad_layout = 0
        pad_left = args.pad_layout_x
        pad_right = args.pad_layout_x
        pad_top = args.pad_layout_top
        pad_bottom = args.pad_layout_bottom
    else:
        pad_layout = args.pad_layout
        pad_left = pad_right = pad_top = pad_bottom = None

    for spec in specs:
        manifest_path = _manifest_path(output_dir, spec)
        if not manifest_path.exists():
            raise FileNotFoundError(manifest_path)
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if page_image_root:
            page_image = _open_image(page_image_root / f"{spec.source_key}.png")
            source = str(page_image_root / f"{spec.source_key}.png")
            source_dpi = None
        else:
            page_image = _render_pdf_page(pdf_path, spec.page, args.dpi)
            source = str(pdf_path)
            source_dpi = args.dpi
        try:
            for figure in manifest.get("figures", []):
                bbox = figure.get("bbox")
                if not bbox:
                    continue
                stable_path = output_dir / figure["stable_path"]
                input_path = output_dir / figure["input_path"]
                before_size = None
                if stable_path.exists():
                    try:
                        with _open_image(stable_path) as before:
                            before_size = list(before.size)
                    except Exception:
                        before_size = None
                result = _save_crop(
                    page_image,
                    bbox,
                    stable_path,
                    layout_width=args.layout_width,
                    pad_layout=pad_layout,
                    quality=args.quality,
                    pad_left=pad_left,
                    pad_top=pad_top,
                    pad_right=pad_right,
                    pad_bottom=pad_bottom,
                )
                _save_crop(
                    page_image,
                    bbox,
                    input_path,
                    layout_width=args.layout_width,
                    pad_layout=pad_layout,
                    quality=args.quality,
                    pad_left=pad_left,
                    pad_top=pad_top,
                    pad_right=pad_right,
                    pad_bottom=pad_bottom,
                )
                report_entries.append(
                    {
                        "page_key": spec.book_page,
                        "book_page": spec.book_page,
                        "pdf_page": spec.pdf_page,
                        "stable_path": figure["stable_path"],
                        "input_path": figure["input_path"],
                        "kind": figure["kind"],
                        "bbox": bbox,
                        "source": source,
                        "source_dpi": source_dpi,
                        "layout_width": args.layout_width,
                        "pad_left": pad_layout if pad_left is None else pad_left,
                        "pad_top": pad_layout if pad_top is None else pad_top,
                        "pad_right": pad_layout if pad_right is None else pad_right,
                        "pad_bottom": pad_layout if pad_bottom is None else pad_bottom,
                        "before_size": before_size,
                        "after_size": result["size"],
                        "crop_box": result["crop_box"],
                    }
                )
        finally:
            page_image.close()

    reports_dir = output_dir / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    report = {
        "chapters": args.chapters,
        "dpi": args.dpi if not page_image_root else None,
        "layout_width": args.layout_width,
        "pad_layout": args.pad_layout,
        "pad_layout_x": args.pad_layout_x,
        "pad_layout_top": args.pad_layout_top,
        "pad_layout_bottom": args.pad_layout_bottom,
        "quality": args.quality,
        "crop_count": len(report_entries),
        "entries": report_entries,
    }
    (reports_dir / "high-res-figures.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"recropped {len(report_entries)} figure crops into {output_dir / 'figures'}")
    return 0


def _split_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter")
    _, rest = text.split("---\n", 1)
    frontmatter_text, sep, body = rest.partition("\n---")
    if not sep:
        raise ValueError("frontmatter is not closed")
    data = yaml.safe_load(frontmatter_text) or {}
    if not isinstance(data, dict):
        raise ValueError("frontmatter is not a mapping")
    return data, body


def _resolve_output_path(output_dir: Path, base: Path, link: str) -> Path:
    clean = link.split("#", 1)[0].split("?", 1)[0]
    if not clean:
        return output_dir
    path = Path(clean)
    if path.is_absolute():
        return path
    if clean.startswith("figures/"):
        return output_dir / clean
    return base / clean


def _resolve_markdown_link(base: Path, link: str) -> Path:
    clean = link.split("#", 1)[0].split("?", 1)[0]
    if not clean:
        return base
    path = Path(clean)
    if path.is_absolute():
        return path
    return base / path


def _relative_to(path: Path, root: Path) -> Path:
    return path.resolve().relative_to(root.resolve())


def _manifest_path(output_dir: Path, spec: PageSpec) -> Path:
    return output_dir / "inputs" / spec.source_key / "manifest.json"


def _crop_kind_by_resolved_path(output_dir: Path, spec: PageSpec) -> dict[Path, str]:
    path = _manifest_path(output_dir, spec)
    if not path.exists():
        return {}
    manifest = json.loads(path.read_text(encoding="utf-8"))
    kinds: dict[Path, str] = {}
    for figure in manifest.get("figures", []):
        stable_path = figure.get("stable_path")
        kind = figure.get("kind")
        if stable_path and kind:
            kinds[(output_dir / stable_path).resolve()] = str(kind)
    return kinds


def _is_formula_crop(path: Path, crop_kinds: dict[Path, str]) -> bool:
    return crop_kinds.get(path.resolve()) == "formula"


def _is_known_nonvisual_crop(path: Path, crop_kinds: dict[Path, str]) -> bool:
    kind = crop_kinds.get(path.resolve())
    return kind is not None and kind not in FINAL_VISUAL_CROP_KINDS


def _leading_figure_caption_count(body: str) -> int:
    body_without_images = CENTERED_HTML_IMG_RE.sub("", body).strip()
    if not body_without_images:
        return 0

    count = 0
    for block in re.split(r"\n\s*\n", body_without_images):
        stripped = block.strip()
        if not stripped:
            continue
        if stripped.startswith(("##", "$$", "\\[", ">", "<")):
            break
        if FIGURE_CAPTION_START_RE.match(stripped):
            count += 1
            continue
        break
    return count


def _validate_centered_figure_captions(md_path: Path, body: str, errors: list[str]) -> None:
    blocks = [block.strip() for block in re.split(r"\n\s*\n", body) if block.strip()]
    for index, block in enumerate(blocks[:-1]):
        if not HTML_IMG_RE.search(block):
            continue
        following = blocks[index + 1]
        if HTML_IMG_RE.search(following):
            continue
        if FIGURE_CAPTION_BLOCK_RE.match(following) or (
            following.startswith("<p") and "Figure " in following and not CENTERED_FIGURE_CAPTION_RE.match(following)
        ):
            errors.append(
                f"{md_path}: figure caption after image must be centered and bold the Figure label"
            )


def _validate_github_math_blocks(md_path: Path, body: str, errors: list[str]) -> None:
    for match in DISPLAY_MATH_BLOCK_RE.finditer(body):
        block = match.group("body")
        if "\\tag{" in block and "\\begin{aligned}" not in block:
            errors.append(
                f"{md_path}: tagged display equations must use an aligned environment for GitHub rendering"
            )


def _validate_markdown(output_dir: Path, spec: PageSpec, errors: list[str]) -> dict[str, Any] | None:
    md_path = fused_markdown_path(output_dir, spec)
    if not md_path.exists():
        errors.append(f"missing fused Markdown: {md_path}")
        return None

    text = md_path.read_text(encoding="utf-8")
    try:
        frontmatter, body = _split_frontmatter(text)
    except ValueError as exc:
        errors.append(f"{md_path}: {exc}")
        return None

    missing = sorted(REQUIRED_FRONTMATTER - set(frontmatter))
    if missing:
        errors.append(f"{md_path}: missing frontmatter keys {missing}")
    if "review_notes" in frontmatter:
        errors.append(f"{md_path}: remove review_notes from final Markdown frontmatter")
    if REVIEW_NOTE_TEXT_RE.search(body):
        errors.append(f"{md_path}: remove review-note text from final Markdown body")
    if DISPLAY_MATH_BRACKET_RE.search(body):
        errors.append(f"{md_path}: use $$ display math delimiters for GitHub rendering, not \\[ or \\]")
    if INLINE_MATH_PAREN_RE.search(body):
        errors.append(f"{md_path}: use $...$ inline math delimiters for GitHub rendering, not \\(...\\)")
    if GITHUB_BLOCKED_MATH_MACRO_RE.search(body):
        errors.append(f"{md_path}: replace GitHub-blocked math macro \\operatorname with \\mathrm or plain LaTeX")
    if INLINE_ESCAPED_BRACE_RE.search(body):
        errors.append(f"{md_path}: use \\lbrace and \\rbrace for literal braces in inline math")
    if INLINE_SUPERSCRIPT_FOOTNOTE_RE.search(body):
        errors.append(f"{md_path}: use Markdown footnotes like [^1], not $^1$ math markers")
    _validate_github_math_blocks(md_path, body, errors)
    if frontmatter.get("page_key") != spec.book_page:
        errors.append(f"{md_path}: page_key should be book page {spec.book_page}")
    if frontmatter.get("book_page") != spec.book_page:
        errors.append(f"{md_path}: book_page should be {spec.book_page}")
    if frontmatter.get("pdf_page") != spec.pdf_page:
        errors.append(f"{md_path}: pdf_page should be {spec.pdf_page}")
    if frontmatter.get("chapter_slug") != spec.chapter.slug:
        errors.append(f"{md_path}: chapter_slug should be {spec.chapter.slug}")

    crop_kinds = _crop_kind_by_resolved_path(output_dir, spec)
    markdown_links = IMAGE_LINK_RE.findall(text)
    for link in markdown_links:
        errors.append(f"{md_path}: use centered HTML image block instead of Markdown image syntax: {link}")

    image_links = HTML_IMG_RE.findall(text)
    centered_links = set(CENTERED_HTML_IMG_RE.findall(text))
    for link in image_links:
        if link not in centered_links:
            errors.append(f"{md_path}: image is not centered with <p align=\"center\">: {link}")
        image_path = _resolve_markdown_link(md_path.parent, link)
        if not image_path.exists():
            errors.append(f"{md_path}: image link does not exist: {link}")
            if link.startswith("figures/"):
                errors.append(f"{md_path}: image link must be relative from fused/chXX, usually ../../{link}")
            continue
        if _is_known_nonvisual_crop(image_path, crop_kinds):
            errors.append(f"{md_path}: final Markdown image links to nonvisual PPStructure crop: {link}")

    expected_figure_count = sum(
        1
        for link in image_links
        if _resolve_markdown_link(md_path.parent, link).exists()
        and not _is_known_nonvisual_crop(_resolve_markdown_link(md_path.parent, link), crop_kinds)
    )
    if frontmatter.get("figure_count") != expected_figure_count:
        errors.append(f"{md_path}: figure_count should be {expected_figure_count}")

    figure_caption_count = _leading_figure_caption_count(body)
    if expected_figure_count < figure_caption_count:
        errors.append(
            f"{md_path}: found {figure_caption_count} leading figure caption(s) but only "
            f"{expected_figure_count} final visual figure image(s)"
        )
    _validate_centered_figure_captions(md_path, body, errors)

    return frontmatter


def _validate_blocks(output_dir: Path, spec: PageSpec, errors: list[str]) -> int:
    block_path = blocks_json_path(output_dir, spec)
    if not block_path.exists():
        errors.append(f"missing blocks JSON: {block_path}")
        return 0

    try:
        data = json.loads(block_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"{block_path}: invalid JSON: {exc}")
        return 0

    if not isinstance(data, list):
        errors.append(f"{block_path}: top-level JSON must be a list")
        return 0

    crop_kinds = _crop_kind_by_resolved_path(output_dir, spec)
    expected_figures = 0
    for idx, block in enumerate(data, start=1):
        if not isinstance(block, dict):
            errors.append(f"{block_path}: block {idx} is not an object")
            continue
        missing = sorted(REQUIRED_BLOCK_KEYS - set(block))
        if missing:
            errors.append(f"{block_path}: block {idx} missing keys {missing}")
        if block.get("page_key") != spec.book_page:
            errors.append(f"{block_path}: block {idx} page_key should be book page {spec.book_page}")
        block_type = block.get("type")
        if block_type not in SUPPORTED_BLOCK_TYPES:
            errors.append(f"{block_path}: block {idx} unsupported type {block_type!r}")
        for key in ("text", "latex", "caption"):
            value = block.get(key)
            if isinstance(value, str) and GITHUB_BLOCKED_MATH_MACRO_RE.search(value):
                errors.append(
                    f"{block_path}: block {idx} field {key!r} uses GitHub-blocked math macro \\operatorname"
                )
        if block_type == "equation" and block.get("image_path"):
            errors.append(f"{block_path}: equation block {idx} must use LaTeX, not image_path")
        if block_type == "figure":
            image_path = block.get("image_path")
            if not image_path:
                errors.append(f"{block_path}: figure block {idx} missing image_path")
            else:
                resolved = _resolve_output_path(output_dir, block_path.parent, str(image_path))
                if not resolved.exists():
                    errors.append(f"{block_path}: figure block {idx} image_path does not exist: {image_path}")
                elif _is_known_nonvisual_crop(resolved, crop_kinds):
                    errors.append(
                        f"{block_path}: figure block {idx} points to nonvisual PPStructure crop: {image_path}"
                    )
                else:
                    expected_figures += 1

    markdown = fused_markdown_path(output_dir, spec)
    if markdown.exists():
        try:
            frontmatter, _ = _split_frontmatter(markdown.read_text(encoding="utf-8"))
        except ValueError:
            frontmatter = {}
        if frontmatter.get("figure_count") != expected_figures:
            errors.append(f"{block_path}: figure blocks should match frontmatter figure_count {frontmatter.get('figure_count')}")

    return len(data)


def _validate_specs(output_dir: Path, specs: list[PageSpec]) -> tuple[list[str], int]:
    errors: list[str] = []
    block_count = 0
    for spec in specs:
        _validate_markdown(output_dir, spec, errors)
        block_count += _validate_blocks(output_dir, spec, errors)
    return errors, block_count


def _write_validation_report(output_dir: Path, specs: list[PageSpec], block_count: int, errors: list[str]) -> None:
    report = {
        "pages_expected": len(specs),
        "blocks_seen": block_count,
        "error_count": len(errors),
        "errors": errors,
    }
    reports_dir = output_dir / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    (reports_dir / "validation.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")


def validate(args: argparse.Namespace) -> int:
    output_dir = Path(args.output_dir)
    raw_root = Path(args.raw_root)
    chapters = load_chapters(raw_root / "chapter_map.json")
    specs = select_pages(chapters, args.chapters, args.book_page_offset)

    errors, block_count = _validate_specs(output_dir, specs)
    _write_validation_report(output_dir, specs, block_count, errors)

    if errors:
        print(f"validation failed: {len(errors)} error(s)")
        for error in errors[:20]:
            print(f"- {error}")
        if len(errors) > 20:
            print(f"- ... {len(errors) - 20} more")
        return 1

    print(f"validation passed: {len(specs)} pages, {block_count} blocks")
    return 0


def _referenced_figure_sources(output_dir: Path, spec: PageSpec) -> list[Path]:
    sources: set[Path] = set()
    md_path = fused_markdown_path(output_dir, spec)
    block_path = blocks_json_path(output_dir, spec)

    text = md_path.read_text(encoding="utf-8")
    for link in HTML_IMG_RE.findall(text):
        resolved = _resolve_markdown_link(md_path.parent, link)
        if resolved.exists():
            sources.add(resolved.resolve())

    blocks = json.loads(block_path.read_text(encoding="utf-8"))
    for block in blocks:
        if not isinstance(block, dict) or block.get("type") != "figure":
            continue
        image_path = block.get("image_path")
        if not image_path:
            continue
        resolved = _resolve_output_path(output_dir, block_path.parent, str(image_path))
        if resolved.exists():
            sources.add(resolved.resolve())

    return sorted(sources)


def _remove_file(path: Path, cleaned: list[str]) -> None:
    if path.exists() and path.is_file():
        path.unlink()
        cleaned.append(str(path))


def _remove_empty_dir(path: Path) -> None:
    try:
        path.rmdir()
    except OSError:
        pass


def _clean_legacy_for_spec(dest_root: Path, spec: PageSpec, cleaned: list[str]) -> None:
    _remove_file(dest_root / "pages" / spec.chapter.slug / f"{spec.source_key}.md", cleaned)
    _remove_empty_dir(dest_root / "pages" / spec.chapter.slug)

    _remove_file(dest_root / "raw_ocr" / f"{spec.source_key}.txt", cleaned)
    _remove_empty_dir(dest_root / "raw_ocr")

    _remove_file(dest_root / "images" / f"{spec.source_key}.png", cleaned)
    _remove_empty_dir(dest_root / "images")

    figures_dir = dest_root / "figures"
    for figure in sorted(figures_dir.glob(f"{spec.source_key}_fig_*")):
        _remove_file(figure, cleaned)
    _remove_empty_dir(figures_dir)


def _write_publish_index(dest_root: Path, specs: list[PageSpec], copied_figures: list[str]) -> None:
    chapters: dict[int, Chapter] = {}
    for spec in specs:
        chapters[spec.chapter.number] = spec.chapter

    lines = [
        "# UDL Textbook Fused Source Layer",
        "",
        "This directory stores validated private, source-derived UDL fused OCR pages.",
        "Final Markdown filenames use printed book page numbers; each page keeps `pdf_page` provenance in frontmatter.",
        "",
        "## Published Scope",
        "",
    ]
    for chapter in sorted(chapters.values(), key=lambda item: item.number):
        chapter_specs = [spec for spec in specs if spec.chapter.number == chapter.number]
        first = chapter_specs[0].key
        last = chapter_specs[-1].key
        lines.append(
            f"- Chapter {chapter.number}: {chapter.title} "
            f"(`pages/{chapter.slug}/{first}.md` through `{last}.md`)"
        )

    lines.extend(
        [
            "",
            "## Assets",
            "",
            f"- Referenced figure files: {len(copied_figures)}",
            "- Block sidecars: `blocks/chXX/page_XXXX.blocks.json`",
            "",
            "## Cleanup Policy",
            "",
            "Legacy DeepSeek-only raw text, old rendered page images, and old PDF-page-key Markdown are removed only for pages that have a validated fused replacement.",
            "",
        ]
    )
    (dest_root / "index.md").write_text("\n".join(lines), encoding="utf-8")


def _write_publish_log(
    dest_root: Path,
    chapters_text: str,
    specs: list[PageSpec],
    block_count: int,
    copied_pages: list[str],
    copied_blocks: list[str],
    copied_figures: list[str],
    cleaned: list[str],
) -> None:
    chapters: dict[int, Chapter] = {}
    for spec in specs:
        chapters[spec.chapter.number] = spec.chapter

    lines = [
        "# UDL Textbook Fusion Publish Log",
        "",
        "Latest publish was produced by `torchbloom-udl-fusion-pilot publish` after validation.",
        "",
        "## Summary",
        "",
        f"- Chapters: {chapters_text}",
        f"- Pages validated: {len(specs)}",
        f"- Blocks validated: {block_count}",
        f"- Markdown pages copied: {len(copied_pages)}",
        f"- Block sidecars copied: {len(copied_blocks)}",
        f"- Referenced figures copied: {len(copied_figures)}",
        f"- Legacy files cleaned: {len(cleaned)}",
        "",
        "## Published Chapters",
        "",
    ]
    for chapter in sorted(chapters.values(), key=lambda item: item.number):
        chapter_specs = [spec for spec in specs if spec.chapter.number == chapter.number]
        lines.append(
            f"- Chapter {chapter.number}: {chapter.title} "
            f"(`{chapter_specs[0].key}.md` through `{chapter_specs[-1].key}.md`)"
        )
    lines.extend(
        [
            "",
            "## Cleanup Policy",
            "",
            "Legacy DeepSeek-only files are removed only for pages with validated fused replacements.",
            "The cleaned-file count is retained as provenance; individual cleaned paths are intentionally omitted to keep this log readable.",
        ]
    )
    lines.append("")
    (dest_root / "log.md").write_text("\n".join(lines), encoding="utf-8")


def publish(args: argparse.Namespace) -> int:
    output_dir = Path(args.output_dir)
    raw_root = Path(args.raw_root)
    dest_root = Path(args.dest_root) if args.dest_root else raw_root
    chapters = load_chapters(raw_root / "chapter_map.json")
    specs = select_pages(chapters, args.chapters, args.book_page_offset)

    errors, block_count = _validate_specs(output_dir, specs)
    _write_validation_report(output_dir, specs, block_count, errors)
    if errors:
        print(f"publish stopped: validation failed with {len(errors)} error(s)")
        for error in errors[:20]:
            print(f"- {error}")
        if len(errors) > 20:
            print(f"- ... {len(errors) - 20} more")
        return 1

    staging_root = dest_root / ".publish-staging"
    if staging_root.exists():
        shutil.rmtree(staging_root)
    staging_root.mkdir(parents=True)

    copied_pages: list[str] = []
    copied_blocks: list[str] = []
    copied_figures: list[str] = []
    cleaned: list[str] = []
    figure_sources: set[Path] = set()

    try:
        for spec in specs:
            page_dest = published_markdown_path(staging_root, spec)
            block_dest = published_blocks_path(staging_root, spec)
            _copy_file(fused_markdown_path(output_dir, spec), page_dest)
            _copy_file(blocks_json_path(output_dir, spec), block_dest)
            copied_pages.append(str(published_markdown_path(dest_root, spec)))
            copied_blocks.append(str(published_blocks_path(dest_root, spec)))
            figure_sources.update(_referenced_figure_sources(output_dir, spec))

        for src in sorted(figure_sources):
            rel = _relative_to(src, output_dir)
            dest = staging_root / rel
            _copy_file(src, dest)
            copied_figures.append(str(dest_root / rel))

        if args.clean_legacy:
            for spec in specs:
                _clean_legacy_for_spec(dest_root, spec, cleaned)

        shutil.copytree(staging_root, dest_root, dirs_exist_ok=True)
    finally:
        if staging_root.exists():
            shutil.rmtree(staging_root)

    _write_publish_index(dest_root, specs, copied_figures)
    _write_publish_log(
        dest_root,
        args.chapters,
        specs,
        block_count,
        copied_pages,
        copied_blocks,
        copied_figures,
        cleaned,
    )
    print(
        "published "
        f"{len(copied_pages)} pages, {len(copied_blocks)} block sidecars, "
        f"{len(copied_figures)} figures to {dest_root}"
    )
    if args.clean_legacy:
        print(f"cleaned {len(cleaned)} legacy file(s)")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    prepare_parser = subparsers.add_parser("prepare", help="prepare evidence and prompts")
    prepare_parser.add_argument("--chapters", default="1,2,3")
    prepare_parser.add_argument("--raw-root", default=str(DEFAULT_RAW_ROOT))
    prepare_parser.add_argument("--paddle-pages-dir", default=str(DEFAULT_PADDLE_PAGES_DIR))
    prepare_parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR))
    prepare_parser.add_argument("--book-page-offset", type=int, default=DEFAULT_BOOK_PAGE_OFFSET)
    prepare_parser.set_defaults(func=prepare)

    refresh_parser = subparsers.add_parser("refresh-prompts", help="refresh prompts from prepared manifests")
    refresh_parser.add_argument("--chapters", default="1,2,3")
    refresh_parser.add_argument("--raw-root", default=str(DEFAULT_RAW_ROOT))
    refresh_parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR))
    refresh_parser.add_argument("--book-page-offset", type=int, default=DEFAULT_BOOK_PAGE_OFFSET)
    refresh_parser.set_defaults(func=refresh_prompts)

    recrop_parser = subparsers.add_parser("recrop-figures", help="recrop PPStructure boxes from high-resolution pages")
    recrop_parser.add_argument("--chapters", default="1,2,3")
    recrop_parser.add_argument("--raw-root", default=str(DEFAULT_RAW_ROOT))
    recrop_parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR))
    recrop_parser.add_argument("--book-page-offset", type=int, default=DEFAULT_BOOK_PAGE_OFFSET)
    recrop_parser.add_argument("--pdf-path", default=str(DEFAULT_PDF_PATH))
    recrop_parser.add_argument("--page-image-root", default=None)
    recrop_parser.add_argument("--dpi", type=int, default=600)
    recrop_parser.add_argument("--layout-width", type=int, default=1000)
    recrop_parser.add_argument("--pad-layout", type=int, default=None)
    recrop_parser.add_argument("--pad-layout-x", type=int, default=8)
    recrop_parser.add_argument("--pad-layout-top", type=int, default=8)
    recrop_parser.add_argument("--pad-layout-bottom", type=int, default=24)
    recrop_parser.add_argument("--quality", type=int, default=95)
    recrop_parser.set_defaults(func=recrop_figures)

    validate_parser = subparsers.add_parser("validate", help="validate fused outputs")
    validate_parser.add_argument("--chapters", default="1,2,3")
    validate_parser.add_argument("--raw-root", default=str(DEFAULT_RAW_ROOT))
    validate_parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR))
    validate_parser.add_argument("--book-page-offset", type=int, default=DEFAULT_BOOK_PAGE_OFFSET)
    validate_parser.set_defaults(func=validate)

    publish_parser = subparsers.add_parser("publish", help="publish validated fused outputs into raw/udl/textbook")
    publish_parser.add_argument("--chapters", default="1,2,3")
    publish_parser.add_argument("--raw-root", default=str(DEFAULT_RAW_ROOT))
    publish_parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR))
    publish_parser.add_argument("--dest-root", default=None)
    publish_parser.add_argument("--book-page-offset", type=int, default=DEFAULT_BOOK_PAGE_OFFSET)
    publish_parser.add_argument("--clean-legacy", action="store_true")
    publish_parser.set_defaults(func=publish)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except (FileNotFoundError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
