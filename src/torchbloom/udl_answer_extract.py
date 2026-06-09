from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import re

from torchbloom.udl_chapter_map import slugify_title


SOURCE_ID = "udlbook-answer-booklet-students"

UDL_CHAPTERS_BY_TITLE = {
    "supervised learning": 2,
    "shallow neural networks": 3,
    "deep neural networks": 4,
    "loss functions": 5,
    "fitting models": 6,
    "gradients and initialization": 7,
    "measuring performance": 8,
    "regularization": 9,
    "convolutional networks": 10,
    "residual networks": 11,
    "transformers": 12,
    "graph neural networks": 13,
    "unsupervised learning": 14,
    "generative adversarial networks": 15,
    "normalizing flows": 16,
    "variational autoencoders": 17,
    "diffusion models": 18,
    "reinforcement learning": 19,
    "why does deep learning work": 20,
    "deep learning and ethics": 21,
}


@dataclass(frozen=True)
class AnswerChapterSpan:
    number: int
    title: str
    slug: str
    pdf_start: int
    pdf_end: int


def chapter_answer_heading(chapter: int) -> str:
    return f"Chapter {chapter}"


def build_answer_chapter_spans(
    toc: list[tuple[int, str, int]],
    page_count: int,
) -> list[AnswerChapterSpan]:
    starts: list[tuple[int, str, int]] = []
    for level, title, page in toc:
        if level != 1:
            continue
        chapter_number = UDL_CHAPTERS_BY_TITLE.get(_normalize_title(title))
        if chapter_number is None:
            continue
        starts.append((chapter_number, title.strip(), page))

    spans: list[AnswerChapterSpan] = []
    for index, (number, title, pdf_start) in enumerate(starts):
        pdf_end = starts[index + 1][2] - 1 if index + 1 < len(starts) else page_count
        spans.append(
            AnswerChapterSpan(
                number=number,
                title=title,
                slug=f"ch{number:02d}-{slugify_title(title)}",
                pdf_start=pdf_start,
                pdf_end=pdf_end,
            )
        )
    return spans


def chapter_for_page(pdf_page: int, spans: list[AnswerChapterSpan]) -> AnswerChapterSpan | None:
    for span in spans:
        if span.pdf_start <= pdf_page <= span.pdf_end:
            return span
    return None


def answer_page_markdown(
    pdf_page: int,
    source_name: str,
    page_text: str,
    spans: list[AnswerChapterSpan],
) -> str:
    chapter = chapter_for_page(pdf_page, spans)
    if chapter is None:
        chapter_value = "null"
        chapter_slug = "null"
    else:
        chapter_value = f"{chapter.number} - {chapter.title}"
        chapter_slug = chapter.slug

    clean_text = page_text.strip()
    return (
        "---\n"
        f"source: {source_name}\n"
        f"source_id: {SOURCE_ID}\n"
        f"page_key: {pdf_page}\n"
        f"answer_page: {pdf_page}\n"
        f"pdf_page: {pdf_page}\n"
        f"chapter: {chapter_value}\n"
        f"chapter_slug: {chapter_slug}\n"
        "extraction_method: pymupdf-text\n"
        "fusion_status: text-extract\n"
        "restricted: true\n"
        "---\n\n"
        f"{clean_text}\n"
    )


def extract_answer_pages(pdf_path: Path, output_dir: Path) -> list[AnswerChapterSpan]:
    import fitz

    output_dir.mkdir(parents=True, exist_ok=True)
    source_name = pdf_path.name

    with fitz.open(pdf_path) as doc:
        spans = build_answer_chapter_spans(doc.get_toc(), page_count=doc.page_count)
        for page_index, page in enumerate(doc, start=1):
            text = page.get_text("text")
            page_path = output_dir / f"page_{page_index:04d}.md"
            page_path.write_text(
                answer_page_markdown(page_index, source_name, text, spans),
                encoding="utf-8",
            )

    _write_index(output_dir.parent / "index.md", source_name, spans)
    return spans


def _write_index(index_path: Path, source_name: str, spans: list[AnswerChapterSpan]) -> None:
    lines = [
        "# UDL Student Answer Booklet Extract",
        "",
        f"Source: `{source_name}`.",
        "",
        "Restricted private raw evidence. Use these pages only to check practice-card correctness.",
        "",
        "## Pilot Coverage",
        "",
    ]

    by_number = {span.number: span for span in spans}
    for chapter in [1, 2, 3]:
        span = by_number.get(chapter)
        if span is None:
            lines.append(f"- Chapter {chapter}: no selected-answer section in this booklet.")
        else:
            lines.append(
                f"- Chapter {chapter}: `{span.slug}`, booklet pages "
                f"{span.pdf_start}-{span.pdf_end}."
            )

    lines.extend(["", "## Chapter Sections", ""])
    for span in spans:
        lines.append(
            f"- Chapter {span.number}: {span.title} "
            f"([page_{span.pdf_start:04d}.md](pages/page_{span.pdf_start:04d}.md)"
            f" - [page_{span.pdf_end:04d}.md](pages/page_{span.pdf_end:04d}.md))"
        )

    index_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _normalize_title(title: str) -> str:
    text = title.strip().lower().rstrip("?")
    text = re.sub(r"\s+", " ", text)
    return text


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Extract UDL answer booklet pages to Markdown.")
    parser.add_argument("--pdf-path", default="raw/udl/source/UDL_Answer_Booklet_Students.pdf")
    parser.add_argument("--output-dir", default="raw/udl/answers/pages")
    args = parser.parse_args(argv)

    spans = extract_answer_pages(Path(args.pdf_path), Path(args.output_dir))
    print(f"extracted {len(spans)} chapter sections to {Path(args.output_dir).parent}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
