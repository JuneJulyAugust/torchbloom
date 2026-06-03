from __future__ import annotations

from dataclasses import asdict, dataclass
import json
import re
from pathlib import Path


CHAPTER_RE = re.compile(r"^(?:Chapter\s+)?(\d{1,2})[\s.:—-]+(.+)$", re.IGNORECASE)
FRONTMATTER_TITLES = {"preface", "acknowledgements", "acknowledgments"}
BACKMATTER_START_TITLES = {"notation", "mathematics", "probability", "bibliography", "index"}


@dataclass(frozen=True)
class ChapterRange:
    number: int
    title: str
    slug: str
    pdf_start: int
    pdf_end: int


def slugify_title(title: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return re.sub(r"-+", "-", slug)


def build_chapter_map(outline: list[tuple[int, str, int]], page_count: int) -> list[ChapterRange]:
    top_level = [(title.strip(), page) for level, title, page in outline if level == 1]
    starts = _numbered_chapter_starts(top_level)
    if not starts:
        starts = _unnumbered_chapter_starts(top_level)

    first_post_chapter_page = _first_post_chapter_page(top_level, starts, page_count)
    return _ranges_from_starts(starts, first_post_chapter_page)


def _numbered_chapter_starts(top_level: list[tuple[str, int]]) -> list[tuple[int, str, int]]:
    starts: list[tuple[int, str, int]] = []
    for title, page in top_level:
        match = CHAPTER_RE.match(title)
        if match:
            starts.append((int(match.group(1)), match.group(2).strip(), page))
    return starts


def _unnumbered_chapter_starts(top_level: list[tuple[str, int]]) -> list[tuple[int, str, int]]:
    starts: list[tuple[int, str, int]] = []
    started = False

    for title, page in top_level:
        normalized = _normalize_title(title)
        if not started and normalized in FRONTMATTER_TITLES:
            continue
        if started and normalized in BACKMATTER_START_TITLES:
            break
        started = True
        starts.append((len(starts) + 1, title, page))

    return starts


def _first_post_chapter_page(
    top_level: list[tuple[str, int]],
    starts: list[tuple[int, str, int]],
    page_count: int,
) -> int:
    first_post_chapter_page = page_count + 1
    start_pages = {page for _, _, page in starts}

    for title, page in top_level:
        if page in start_pages:
            continue
        if starts and page > starts[-1][2]:
            first_post_chapter_page = page
            break

    return first_post_chapter_page


def _ranges_from_starts(
    starts: list[tuple[int, str, int]],
    first_post_chapter_page: int,
) -> list[ChapterRange]:
    chapters: list[ChapterRange] = []
    for index, (number, title, pdf_start) in enumerate(starts):
        if index + 1 < len(starts):
            pdf_end = starts[index + 1][2] - 1
        else:
            pdf_end = first_post_chapter_page - 1
        chapters.append(
            ChapterRange(
                number=number,
                title=title,
                slug=f"ch{number:02d}-{slugify_title(title)}",
                pdf_start=pdf_start,
                pdf_end=pdf_end,
            )
        )
    return chapters


def _normalize_title(title: str) -> str:
    return re.sub(r"\s+", " ", title.strip().lower())


def load_chapter_map(pdf_path: Path) -> list[ChapterRange]:
    import fitz

    with fitz.open(pdf_path) as doc:
        return build_chapter_map(doc.get_toc(), page_count=doc.page_count)


def write_chapter_map(pdf_path: Path, output_path: Path) -> list[ChapterRange]:
    chapters = load_chapter_map(pdf_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps([asdict(chapter) for chapter in chapters], indent=2) + "\n",
        encoding="utf-8",
    )
    return chapters
