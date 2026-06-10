from torchbloom.udl_answer_extract import (
    answer_page_markdown,
    build_answer_chapter_spans,
    chapter_answer_heading,
    chapter_for_page,
)


def test_chapter_answer_heading():
    assert chapter_answer_heading(1) == "Chapter 1"
    assert chapter_answer_heading(3) == "Chapter 3"


def test_build_answer_chapter_spans_from_toc():
    toc = [
        (1, "Supervised learning", 5),
        (1, "Shallow neural networks", 7),
        (1, "Deep neural networks", 13),
    ]

    spans = build_answer_chapter_spans(toc, page_count=20)

    assert spans[0].number == 2
    assert spans[0].title == "Supervised learning"
    assert spans[0].pdf_start == 5
    assert spans[0].pdf_end == 6
    assert spans[1].number == 3
    assert spans[1].pdf_start == 7
    assert spans[1].pdf_end == 12


def test_chapter_for_page_returns_none_for_frontmatter():
    spans = build_answer_chapter_spans(
        [(1, "Supervised learning", 5), (1, "Shallow neural networks", 7)],
        page_count=10,
    )

    assert chapter_for_page(4, spans) is None
    assert chapter_for_page(5, spans).number == 2
    assert chapter_for_page(8, spans).number == 3


def test_answer_page_markdown_includes_source_metadata():
    spans = build_answer_chapter_spans([(1, "Supervised learning", 5)], page_count=6)

    text = answer_page_markdown(
        pdf_page=5,
        source_name="UDL_Answer_Booklet_Students.pdf",
        page_text="Chapter 2\nSupervised learning\nProblem 2.1 ...",
        spans=spans,
    )

    assert "source: UDL_Answer_Booklet_Students.pdf" in text
    assert "page_key: 5" in text
    assert "answer_page: 5" in text
    assert "pdf_page: 5" in text
    assert "chapter: 2 - Supervised learning" in text
    assert "chapter_slug: ch02-supervised-learning" in text
    assert "extraction_method: pymupdf-text" in text
    assert "fusion_status: text-extract" in text
    assert "Problem 2.1" in text
