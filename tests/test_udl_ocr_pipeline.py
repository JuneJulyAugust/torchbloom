from pathlib import Path

import pytest

from torchbloom.udl_chapter_map import ChapterRange
from torchbloom.udl_ocr_pipeline import (
    ERROR_MARKER,
    _crop_and_save,
    is_page_done,
    page_md_dest,
    raw_ocr_path,
    status_report,
    write_page_from_raw,
)

PIL = pytest.importorskip("PIL.Image")


def _make_page_png(path: Path, w: int = 1000, h: int = 1000) -> None:
    from PIL import Image

    Image.new("RGB", (w, h), (255, 255, 255)).save(path)


def test_raw_ocr_path_is_4_digit(tmp_path):
    assert raw_ocr_path(tmp_path, 15).name == "page_0015.txt"


def test_is_page_done_false_when_missing(tmp_path):
    assert is_page_done(tmp_path, 15) is False


def test_is_page_done_true_when_present_and_clean(tmp_path):
    (tmp_path / "raw_ocr").mkdir()
    raw_ocr_path(tmp_path, 15).write_text("some grounding text", encoding="utf-8")
    assert is_page_done(tmp_path, 15) is True


def test_is_page_done_false_when_error_marker(tmp_path):
    (tmp_path / "raw_ocr").mkdir()
    raw_ocr_path(tmp_path, 15).write_text(ERROR_MARKER + " boom", encoding="utf-8")
    assert is_page_done(tmp_path, 15) is False


def test_page_md_dest_groups_by_chapter_slug(tmp_path):
    dest = page_md_dest(tmp_path, 39, "ch03-shallow-neural-networks")
    assert dest == tmp_path / "pages" / "ch03-shallow-neural-networks" / "page_0039.md"


def test_write_page_from_raw_emits_md_and_figure(tmp_path):
    out = tmp_path
    (out / "raw_ocr").mkdir()
    raw = (
        "<|ref|>sub_title<|/ref|><|det|>[[100, 80, 900, 130]]<|/det|>## Shallow networks\n"
        "<|ref|>image<|/ref|><|det|>[[100, 200, 500, 600]]<|/det|>"
    )
    raw_ocr_path(out, 39).write_text(raw, encoding="utf-8")
    page_png = tmp_path / "page_0039.png"
    _make_page_png(page_png)

    ranges = [ChapterRange(3, "Shallow neural networks", "ch03-shallow-neural-networks", 39, 54)]
    md_path = write_page_from_raw(
        output_dir=out,
        pdf_page=39,
        ranges=ranges,
        page_image_path=page_png,
        source_name="UnderstandingDeepLearning_02_09_26_C.pdf",
        title_banner=None,
    )

    assert md_path.exists()
    text = md_path.read_text(encoding="utf-8")
    assert "page_key: 39" in text
    assert "pdf_page: 39" in text
    assert "chapter_slug: ch03-shallow-neural-networks" in text
    assert "## Shallow networks" in text
    assert (out / "figures" / "page_0039_fig_1.png").exists()


def test_status_report_counts_done_and_error_pages(tmp_path):
    (tmp_path / "raw_ocr").mkdir()
    ranges = [ChapterRange(1, "Introduction", "ch01-introduction", 15, 17)]
    raw_ocr_path(tmp_path, 15).write_text("ok", encoding="utf-8")
    raw_ocr_path(tmp_path, 16).write_text(ERROR_MARKER + " failed", encoding="utf-8")

    rep = status_report(tmp_path, ranges, [1])

    assert rep["total"] == 3
    assert rep["done"] == 1
    assert rep["complete"] is False
    assert rep["error_pages"] == [16]
    assert rep["per_chapter"][1] == {"done": 1, "total": 3}


def test_crop_and_save_handles_inverted_box(tmp_path):
    from PIL import Image

    img = Image.new("RGB", (1000, 1000), (255, 255, 255))
    out = tmp_path / "fig.png"
    _crop_and_save(img, 1000, 1000, [800, 600, 200, 100], out)
    assert out.exists()
