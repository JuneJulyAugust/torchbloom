from __future__ import annotations

import json
from pathlib import Path

from torchbloom.udl_paddle_structure import (
    main,
    page_markdown_path,
    page_output_dir,
    pipeline_kwargs,
    save_layout_result,
    save_page_result,
)
from torchbloom.udl_fusion_pilot import Chapter, PageSpec


class FakeResult:
    def __init__(self, markdown: str) -> None:
        self.markdown = markdown
        self.saved_json_path: Path | None = None

    def save_to_json(self, save_path: str) -> None:
        dest = Path(save_path)
        dest.mkdir(parents=True, exist_ok=True)
        self.saved_json_path = dest / "result.json"
        self.saved_json_path.write_text('{"ok": true}\n', encoding="utf-8")


class FakePipeline:
    def concatenate_markdown_pages(self, pages: list[str]) -> str:
        return "\n\n".join(page.strip() for page in pages)


def _spec() -> PageSpec:
    return PageSpec(
        chapter=Chapter(
            number=4,
            title="Deep neural networks",
            slug="ch04-deep-neural-networks",
            pdf_start=55,
            pdf_end=55,
        ),
        page=55,
    )


def _write_chapter_map(raw_root: Path) -> None:
    raw_root.mkdir(parents=True)
    (raw_root / "chapter_map.json").write_text(
        json.dumps(
            [
                {
                    "number": 4,
                    "title": "Deep neural networks",
                    "slug": "ch04-deep-neural-networks",
                    "pdf_start": 55,
                    "pdf_end": 56,
                }
            ]
        )
        + "\n",
        encoding="utf-8",
    )


def test_save_page_result_writes_nested_combined_markdown_and_json(tmp_path):
    spec = _spec()
    output_dir = tmp_path / "paddle"
    result = [FakeResult("# Page 55\n"), FakeResult("second page fragment")]

    written = save_page_result(FakePipeline(), result, output_dir, spec)

    assert written == page_markdown_path(output_dir, spec)
    assert written == output_dir / "pages" / "page_0055" / "page_0055.combined.md"
    assert written.read_text(encoding="utf-8") == "# Page 55\n\nsecond page fragment\n"
    assert page_output_dir(output_dir, spec).joinpath("json", "result.json").exists()


def test_status_reports_nested_combined_markdown_completion(tmp_path, capsys):
    raw_root = tmp_path / "raw" / "udl" / "textbook"
    output_dir = tmp_path / "output" / "paddle"
    _write_chapter_map(raw_root)
    page_markdown_path(output_dir, _spec()).parent.mkdir(parents=True)
    page_markdown_path(output_dir, _spec()).write_text("done\n", encoding="utf-8")

    result = main(
        [
            "--chapters",
            "4",
            "--raw-root",
            str(raw_root),
            "--output-dir",
            str(output_dir),
            "--status",
        ]
    )

    assert result == 0
    out = capsys.readouterr().out
    assert "1/2 pages done" in out
    assert "ch04: 1/2" in out


def test_pipeline_kwargs_disable_heavy_recognizers_by_default(tmp_path):
    class Args:
        paddlex_cache = tmp_path / "cache"
        lang = "en"
        device = "cpu"
        engine = "paddle"
        use_table_recognition = False
        use_formula_recognition = False
        use_chart_recognition = False
        use_region_detection = False

    kwargs = pipeline_kwargs(Args())

    assert kwargs["use_table_recognition"] is False
    assert kwargs["use_formula_recognition"] is False
    assert kwargs["use_chart_recognition"] is False
    assert kwargs["use_region_detection"] is False


def test_save_layout_result_writes_fusion_ready_markdown_json_and_crops(tmp_path):
    from PIL import Image

    spec = _spec()
    output_dir = tmp_path / "paddle"
    image_path = tmp_path / "page_0055.png"
    Image.new("RGB", (2000, 2600), (255, 255, 255)).save(image_path)
    result = [
        {
            "boxes": [
                {"label": "image", "score": 0.91, "coordinate": [200, 260, 1200, 1560]},
                {"label": "formula", "score": 0.87, "coordinate": [1000, 2000, 1500, 2100]},
            ]
        }
    ]

    written = save_layout_result(result, output_dir, spec, image_path)

    assert written == output_dir / "pages" / "page_0055" / "page_0055.combined.md"
    text = written.read_text(encoding="utf-8")
    assert "LayoutDetection page_0055" in text
    assert "image score=0.910 bbox=[100, 130, 600, 780]" in text
    layout_json = json.loads(
        (output_dir / "pages" / "page_0055" / "json" / "page_0055.layout.json").read_text(encoding="utf-8")
    )
    assert layout_json["boxes"][0]["layout_bbox"] == [100, 130, 600, 780]
    assert (output_dir / "pages" / "page_0055" / "imgs" / "img_in_image_box_100_130_600_780.jpg").exists()
    assert (output_dir / "pages" / "page_0055" / "imgs" / "img_in_formula_box_500_1000_750_1050.jpg").exists()


def test_save_layout_result_merges_panels_above_figure_title(tmp_path):
    from PIL import Image

    spec = _spec()
    output_dir = tmp_path / "paddle"
    image_path = tmp_path / "page_0055.png"
    Image.new("RGB", (2000, 2600), (255, 255, 255)).save(image_path)
    result = [
        {
            "boxes": [
                {"label": "chart", "score": 0.91, "coordinate": [200, 260, 800, 1000]},
                {"label": "chart", "score": 0.88, "coordinate": [900, 260, 1600, 1000]},
                {"label": "figure_title", "score": 0.95, "coordinate": [200, 1100, 1800, 1400]},
            ]
        }
    ]
    stale_dir = output_dir / "pages" / "page_0055" / "imgs"
    stale_dir.mkdir(parents=True)
    (stale_dir / "img_in_chart_box_1_2_3_4.jpg").write_text("stale", encoding="utf-8")

    save_layout_result(result, output_dir, spec, image_path)

    imgs_dir = output_dir / "pages" / "page_0055" / "imgs"
    names = sorted(path.name for path in imgs_dir.iterdir())
    assert names == ["img_in_image_box_100_130_800_500.jpg"]
    layout_json = json.loads((output_dir / "pages" / "page_0055" / "json" / "page_0055.layout.json").read_text())
    assert layout_json["visual_groups"][0]["layout_bbox"] == [100, 130, 800, 500]
    assert layout_json["visual_groups"][0]["source_box_indexes"] == [1, 2]


def test_run_skips_done_page_in_resume_mode(tmp_path, monkeypatch):
    from PIL import Image

    raw_root = tmp_path / "raw" / "udl" / "textbook"
    image_root = raw_root / "images"
    output_dir = tmp_path / "output" / "paddle"
    _write_chapter_map(raw_root)
    image_root.mkdir(parents=True)
    Image.new("RGB", (200, 260), (255, 255, 255)).save(image_root / "page_0055.png")
    Image.new("RGB", (200, 260), (255, 255, 255)).save(image_root / "page_0056.png")
    page_markdown_path(output_dir, _spec()).parent.mkdir(parents=True)
    page_markdown_path(output_dir, _spec()).write_text("done\n", encoding="utf-8")

    called_images: list[Path] = []

    class LayoutDetector:
        def predict(self, image_path: str):
            called_images.append(Path(image_path))
            return [{"boxes": [{"label": "text", "score": 0.9, "coordinate": [10, 10, 100, 100]}]}]

    monkeypatch.setattr("torchbloom.udl_paddle_structure.build_layout_detector", lambda args: LayoutDetector())

    result = main(
        [
            "--chapters",
            "4",
            "--raw-root",
            str(raw_root),
            "--image-root",
            str(image_root),
            "--output-dir",
            str(output_dir),
            "--backend",
            "layout-detection",
            "--resume",
        ]
    )

    assert result == 0
    assert called_images == [image_root / "page_0056.png"]
    assert (output_dir / "pages" / "page_0056" / "page_0056.combined.md").exists()
