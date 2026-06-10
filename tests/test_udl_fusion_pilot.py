from __future__ import annotations

import json
from pathlib import Path

from torchbloom.udl_fusion_pilot import main


def _write_fake_chapter_map(raw_root: Path) -> None:
    raw_root.mkdir(parents=True)
    (raw_root / "chapter_map.json").write_text(
        json.dumps(
            [
                {
                    "number": 1,
                    "title": "Introduction",
                    "slug": "ch01-introduction",
                    "pdf_start": 15,
                    "pdf_end": 15,
                }
            ]
        )
        + "\n",
        encoding="utf-8",
    )


def _write_fake_inputs(tmp_path: Path) -> tuple[Path, Path, Path]:
    from PIL import Image

    raw_root = tmp_path / "raw" / "udl" / "textbook"
    paddle_dir = tmp_path / "output" / "comparison" / "paddle-pages"
    output_dir = tmp_path / "output" / "fusion"
    _write_fake_chapter_map(raw_root)

    (raw_root / "pages" / "ch01-introduction").mkdir(parents=True)
    (raw_root / "pages" / "ch01-introduction" / "page_0015.md").write_text(
        "---\npage_key: 15\n---\n\n## DeepSeek page\n",
        encoding="utf-8",
    )
    (raw_root / "raw_ocr").mkdir()
    (raw_root / "raw_ocr" / "page_0015.txt").write_text("raw grounding", encoding="utf-8")
    (raw_root / "images").mkdir()
    Image.new("RGB", (2000, 2600), (255, 255, 255)).save(raw_root / "images" / "page_0015.png")

    page_dir = paddle_dir / "page_0015"
    (page_dir / "imgs").mkdir(parents=True)
    (page_dir / "page_0015.combined.md").write_text("## Paddle page\n", encoding="utf-8")
    (page_dir / "imgs" / "img_in_image_box_10_20_30_40.jpg").write_bytes(b"fake crop")
    (page_dir / "imgs" / "img_in_formula_box_50_60_70_80.jpg").write_bytes(b"fake formula crop")
    return raw_root, paddle_dir, output_dir


def test_prepare_writes_manifest_prompt_and_stable_figure(tmp_path):
    raw_root, paddle_dir, output_dir = _write_fake_inputs(tmp_path)

    result = main(
        [
            "prepare",
            "--chapters",
            "1",
            "--raw-root",
            str(raw_root),
            "--paddle-pages-dir",
            str(paddle_dir),
            "--output-dir",
            str(output_dir),
        ]
    )

    assert result == 0
    manifest_path = output_dir / "inputs" / "page_0015" / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert manifest["page_key"] == 1
    assert manifest["book_page"] == 1
    assert manifest["pdf_page"] == 15
    assert manifest["source_pdf_page_name"] == "page_0015"
    assert manifest["page_name"] == "page_0001"
    assert manifest["figures"][0]["kind"] == "image"
    assert manifest["figures"][0]["bbox"] == [10, 20, 30, 40]
    assert manifest["figures"][1]["kind"] == "formula"
    assert (output_dir / "prompts" / "page_0001.md").exists()
    prompt = (output_dir / "prompts" / "page_0001.md").read_text(encoding="utf-8")
    assert "book_page: 1" in prompt
    assert "pdf_page: 15" in prompt
    assert "review_notes" not in prompt
    assert "figure_count: 1" in prompt
    assert "Evidence-Only Crops" in prompt
    assert (output_dir / "figures" / "page_0001_fig_1.jpg").exists()
    assert (output_dir / "figures" / "page_0001_fig_2.jpg").exists()
    assert (output_dir / "inputs" / "page_0015" / "paddle_figures" / "img_in_image_box_10_20_30_40.jpg").exists()


def test_refresh_prompts_rewrites_from_existing_manifest(tmp_path):
    raw_root, paddle_dir, output_dir = _write_fake_inputs(tmp_path)
    assert (
        main(
            [
                "prepare",
                "--chapters",
                "1",
                "--raw-root",
                str(raw_root),
                "--paddle-pages-dir",
                str(paddle_dir),
                "--output-dir",
                str(output_dir),
            ]
        )
        == 0
    )
    prompt_path = output_dir / "prompts" / "page_0001.md"
    prompt_path.write_text("stale", encoding="utf-8")

    result = main(["refresh-prompts", "--chapters", "1", "--raw-root", str(raw_root), "--output-dir", str(output_dir)])

    assert result == 0
    assert "Evidence-Only Crops" in prompt_path.read_text(encoding="utf-8")


def test_recrop_figures_uses_layout_boxes_on_high_resolution_page(tmp_path):
    from PIL import Image

    raw_root, paddle_dir, output_dir = _write_fake_inputs(tmp_path)
    assert (
        main(
            [
                "prepare",
                "--chapters",
                "1",
                "--raw-root",
                str(raw_root),
                "--paddle-pages-dir",
                str(paddle_dir),
                "--output-dir",
                str(output_dir),
            ]
        )
        == 0
    )

    result = main(
        [
            "recrop-figures",
            "--chapters",
            "1",
            "--raw-root",
            str(raw_root),
            "--output-dir",
            str(output_dir),
            "--page-image-root",
            str(raw_root / "images"),
            "--layout-width",
            "1000",
            "--pad-layout",
            "0",
        ]
    )

    assert result == 0
    with Image.open(output_dir / "figures" / "page_0001_fig_1.jpg") as image:
        assert image.size == (40, 40)
    report = json.loads((output_dir / "reports" / "high-res-figures.json").read_text(encoding="utf-8"))
    assert report["crop_count"] == 2
    assert report["entries"][0]["after_size"] == [40, 40]


def test_validate_accepts_minimal_fused_page_and_blocks(tmp_path):
    raw_root, paddle_dir, output_dir = _write_fake_inputs(tmp_path)
    assert (
        main(
            [
                "prepare",
                "--chapters",
                "1",
                "--raw-root",
                str(raw_root),
                "--paddle-pages-dir",
                str(paddle_dir),
                "--output-dir",
                str(output_dir),
            ]
        )
        == 0
    )

    fused_dir = output_dir / "fused" / "ch01"
    blocks_dir = output_dir / "blocks" / "ch01"
    fused_dir.mkdir(parents=True)
    blocks_dir.mkdir(parents=True)
    (fused_dir / "page_0001.md").write_text(
        r"""---
source: UnderstandingDeepLearning_02_09_26_C.pdf
page_key: 1
book_page: 1
pdf_page: 15
chapter: "1 - Introduction"
chapter_slug: ch01-introduction
ocr_sources:
  - deepseek-ocr-2
  - ppstructurev3
fusion_status: fused
confidence: medium
figure_count: 1
---

## Introduction

<p align="center">
  <img src="../../figures/page_0001_fig_1.jpg" alt="Figure" />
</p>
""",
        encoding="utf-8",
    )
    (blocks_dir / "page_0001.blocks.json").write_text(
        json.dumps(
            [
                {
                    "id": "page_0001-b001",
                    "page_key": 1,
                    "order": 1,
                    "type": "heading",
                    "text": "Introduction",
                    "source": "deepseek+paddle",
                    "confidence": "high",
                },
                {
                    "id": "page_0001-b002",
                    "page_key": 1,
                    "order": 2,
                    "type": "figure",
                    "image_path": "figures/page_0001_fig_1.jpg",
                    "source": "paddle",
                    "confidence": "high",
                },
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    result = main(["validate", "--chapters", "1", "--raw-root", str(raw_root), "--output-dir", str(output_dir)])

    assert result == 0


def test_publish_stops_when_validation_fails(tmp_path):
    raw_root, _, output_dir = _write_fake_inputs(tmp_path)
    fused_dir = output_dir / "fused" / "ch01"
    fused_dir.mkdir(parents=True)
    (fused_dir / "page_0001.md").write_text("not valid frontmatter\n", encoding="utf-8")

    result = main(["publish", "--chapters", "1", "--raw-root", str(raw_root), "--output-dir", str(output_dir)])

    assert result == 1
    assert not (raw_root / "pages" / "ch01-introduction" / "page_0001.md").exists()


def test_publish_copies_validated_outputs_and_cleans_legacy_scope(tmp_path):
    raw_root, paddle_dir, output_dir = _write_fake_inputs(tmp_path)
    assert (
        main(
            [
                "prepare",
                "--chapters",
                "1",
                "--raw-root",
                str(raw_root),
                "--paddle-pages-dir",
                str(paddle_dir),
                "--output-dir",
                str(output_dir),
            ]
        )
        == 0
    )

    legacy_page = raw_root / "pages" / "ch01-introduction" / "page_0015.md"
    assert legacy_page.exists()
    assert (raw_root / "raw_ocr" / "page_0015.txt").exists()
    assert (raw_root / "images" / "page_0015.png").exists()
    legacy_figure = raw_root / "figures" / "page_0015_fig_1.png"
    legacy_figure.parent.mkdir(parents=True)
    legacy_figure.write_bytes(b"legacy figure")

    fused_dir = output_dir / "fused" / "ch01"
    blocks_dir = output_dir / "blocks" / "ch01"
    fused_dir.mkdir(parents=True)
    blocks_dir.mkdir(parents=True)
    (fused_dir / "page_0001.md").write_text(
        r"""---
source: UnderstandingDeepLearning_02_09_26_C.pdf
page_key: 1
book_page: 1
pdf_page: 15
chapter: "1 - Introduction"
chapter_slug: ch01-introduction
ocr_sources:
  - deepseek-ocr-2
  - ppstructurev3
fusion_status: fused
confidence: medium
figure_count: 1
---

## Introduction

<p align="center">
  <img src="../../figures/page_0001_fig_1.jpg" alt="Figure" />
</p>
""",
        encoding="utf-8",
    )
    (blocks_dir / "page_0001.blocks.json").write_text(
        json.dumps(
            [
                {
                    "id": "page_0001-b001",
                    "page_key": 1,
                    "order": 1,
                    "type": "heading",
                    "text": "Introduction",
                    "source": "deepseek+paddle",
                    "confidence": "high",
                },
                {
                    "id": "page_0001-b002",
                    "page_key": 1,
                    "order": 2,
                    "type": "figure",
                    "image_path": "figures/page_0001_fig_1.jpg",
                    "source": "paddle",
                    "confidence": "high",
                },
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    result = main(
        [
            "publish",
            "--chapters",
            "1",
            "--raw-root",
            str(raw_root),
            "--output-dir",
            str(output_dir),
            "--clean-legacy",
        ]
    )

    assert result == 0
    assert (raw_root / "pages" / "ch01-introduction" / "page_0001.md").exists()
    assert not legacy_page.exists()
    assert not (raw_root / "raw_ocr" / "page_0015.txt").exists()
    assert not (raw_root / "images" / "page_0015.png").exists()
    assert not legacy_figure.exists()
    assert (raw_root / "blocks" / "ch01" / "page_0001.blocks.json").exists()
    assert (raw_root / "figures" / "page_0001_fig_1.jpg").exists()
    assert not (raw_root / "figures" / "page_0001_fig_2.jpg").exists()
    assert "Markdown pages copied: 1" in (raw_root / "log.md").read_text(encoding="utf-8")


def test_validate_reports_missing_figure_reference(tmp_path):
    raw_root, _, output_dir = _write_fake_inputs(tmp_path)
    fused_dir = output_dir / "fused" / "ch01"
    blocks_dir = output_dir / "blocks" / "ch01"
    fused_dir.mkdir(parents=True)
    blocks_dir.mkdir(parents=True)
    (fused_dir / "page_0001.md").write_text(
        r"""---
source: UnderstandingDeepLearning_02_09_26_C.pdf
page_key: 1
book_page: 1
pdf_page: 15
chapter: "1 - Introduction"
chapter_slug: ch01-introduction
ocr_sources:
  - deepseek-ocr-2
  - ppstructurev3
fusion_status: fused
confidence: medium
figure_count: 1
---

<p align="center">
  <img src="../../figures/missing.jpg" alt="Missing" />
</p>
""",
        encoding="utf-8",
    )
    (blocks_dir / "page_0001.blocks.json").write_text(
        json.dumps(
            [
                {
                    "id": "page_0001-b001",
                    "page_key": 1,
                    "order": 1,
                    "type": "figure",
                    "image_path": "figures/missing.jpg",
                    "source": "paddle",
                    "confidence": "low",
                }
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    result = main(["validate", "--chapters", "1", "--raw-root", str(raw_root), "--output-dir", str(output_dir)])

    assert result == 1
    validation = json.loads((output_dir / "reports" / "validation.json").read_text(encoding="utf-8"))
    assert validation["error_count"] >= 1
    assert any("does not exist" in error for error in validation["errors"])


def test_validate_rejects_figure_captions_without_visual_images(tmp_path):
    raw_root, _, output_dir = _write_fake_inputs(tmp_path)
    fused_dir = output_dir / "fused" / "ch01"
    blocks_dir = output_dir / "blocks" / "ch01"
    fused_dir.mkdir(parents=True)
    blocks_dir.mkdir(parents=True)
    (fused_dir / "page_0001.md").write_text(
        """---
source: UnderstandingDeepLearning_02_09_26_C.pdf
page_key: 1
book_page: 1
pdf_page: 15
chapter: "1 - Introduction"
chapter_slug: ch01-introduction
ocr_sources:
  - deepseek-ocr-2
  - ppstructurev3
fusion_status: fused
confidence: medium
figure_count: 0
---

Figure 1.1 A caption with no final visual image.
""",
        encoding="utf-8",
    )
    (blocks_dir / "page_0001.blocks.json").write_text(
        json.dumps(
            [
                {
                    "id": "page_0001-b001",
                    "page_key": 1,
                    "order": 1,
                    "type": "caption",
                    "source": "deepseek+paddle",
                    "confidence": "low",
                    "text": "Figure 1.1 A caption with no final visual image.",
                }
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    result = main(["validate", "--chapters", "1", "--raw-root", str(raw_root), "--output-dir", str(output_dir)])

    assert result == 1
    validation = json.loads((output_dir / "reports" / "validation.json").read_text(encoding="utf-8"))
    assert any("figure caption(s)" in error for error in validation["errors"])


def test_validate_rejects_review_notes_in_final_markdown(tmp_path):
    raw_root, _, output_dir = _write_fake_inputs(tmp_path)
    fused_dir = output_dir / "fused" / "ch01"
    blocks_dir = output_dir / "blocks" / "ch01"
    fused_dir.mkdir(parents=True)
    blocks_dir.mkdir(parents=True)
    (fused_dir / "page_0001.md").write_text(
        """---
source: UnderstandingDeepLearning_02_09_26_C.pdf
page_key: 1
book_page: 1
pdf_page: 15
chapter: "1 - Introduction"
chapter_slug: ch01-introduction
ocr_sources:
  - deepseek-ocr-2
  - ppstructurev3
fusion_status: fused
confidence: medium
figure_count: 0
review_notes: []
---

> Review note: This should stay out of final Markdown.
""",
        encoding="utf-8",
    )
    (blocks_dir / "page_0001.blocks.json").write_text(
        json.dumps(
            [
                {
                    "id": "page_0001-b001",
                    "page_key": 1,
                    "order": 1,
                    "type": "paragraph",
                    "source": "deepseek+paddle",
                    "confidence": "low",
                    "text": "Placeholder.",
                }
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    result = main(["validate", "--chapters", "1", "--raw-root", str(raw_root), "--output-dir", str(output_dir)])

    assert result == 1
    validation = json.loads((output_dir / "reports" / "validation.json").read_text(encoding="utf-8"))
    assert any("review_notes" in error for error in validation["errors"])
    assert any("review-note text" in error for error in validation["errors"])


def test_validate_rejects_bracket_display_math_for_github_rendering(tmp_path):
    raw_root, _, output_dir = _write_fake_inputs(tmp_path)
    fused_dir = output_dir / "fused" / "ch01"
    blocks_dir = output_dir / "blocks" / "ch01"
    fused_dir.mkdir(parents=True)
    blocks_dir.mkdir(parents=True)
    (fused_dir / "page_0001.md").write_text(
        """---
source: UnderstandingDeepLearning_02_09_26_C.pdf
page_key: 1
book_page: 1
pdf_page: 15
chapter: "1 - Introduction"
chapter_slug: ch01-introduction
ocr_sources:
  - deepseek-ocr-2
  - ppstructurev3
fusion_status: fused
confidence: medium
figure_count: 0
---

\\[
x = y
\\]
""",
        encoding="utf-8",
    )
    (blocks_dir / "page_0001.blocks.json").write_text(
        json.dumps(
            [
                {
                    "id": "page_0001-b001",
                    "page_key": 1,
                    "order": 1,
                    "type": "equation",
                    "source": "deepseek+paddle",
                    "confidence": "high",
                    "latex": "x = y",
                }
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    result = main(["validate", "--chapters", "1", "--raw-root", str(raw_root), "--output-dir", str(output_dir)])

    assert result == 1
    validation = json.loads((output_dir / "reports" / "validation.json").read_text(encoding="utf-8"))
    assert any("GitHub rendering" in error for error in validation["errors"])


def test_validate_rejects_single_line_bracket_display_math_for_github_rendering(tmp_path):
    raw_root, _, output_dir = _write_fake_inputs(tmp_path)
    fused_dir = output_dir / "fused" / "ch01"
    blocks_dir = output_dir / "blocks" / "ch01"
    fused_dir.mkdir(parents=True)
    blocks_dir.mkdir(parents=True)
    (fused_dir / "page_0001.md").write_text(
        """---
source: UnderstandingDeepLearning_02_09_26_C.pdf
page_key: 1
book_page: 1
pdf_page: 15
chapter: "1 - Introduction"
chapter_slug: ch01-introduction
ocr_sources:
  - deepseek-ocr-2
  - ppstructurev3
fusion_status: fused
confidence: medium
figure_count: 0
---

\\[ x = y \\]
""",
        encoding="utf-8",
    )
    (blocks_dir / "page_0001.blocks.json").write_text(
        json.dumps(
            [
                {
                    "id": "page_0001-b001",
                    "page_key": 1,
                    "order": 1,
                    "type": "equation",
                    "source": "deepseek+paddle",
                    "confidence": "high",
                    "latex": "x = y",
                }
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    result = main(["validate", "--chapters", "1", "--raw-root", str(raw_root), "--output-dir", str(output_dir)])

    assert result == 1
    validation = json.loads((output_dir / "reports" / "validation.json").read_text(encoding="utf-8"))
    assert any("GitHub rendering" in error for error in validation["errors"])


def test_validate_rejects_paren_inline_math_for_github_rendering(tmp_path):
    raw_root, _, output_dir = _write_fake_inputs(tmp_path)
    fused_dir = output_dir / "fused" / "ch01"
    blocks_dir = output_dir / "blocks" / "ch01"
    fused_dir.mkdir(parents=True)
    blocks_dir.mkdir(parents=True)
    (fused_dir / "page_0001.md").write_text(
        """---
source: UnderstandingDeepLearning_02_09_26_C.pdf
page_key: 1
book_page: 1
pdf_page: 15
chapter: "1 - Introduction"
chapter_slug: ch01-introduction
ocr_sources:
  - deepseek-ocr-2
  - ppstructurev3
fusion_status: fused
confidence: medium
figure_count: 0
---

This still uses \\(x_i\\) as inline math.
""",
        encoding="utf-8",
    )
    (blocks_dir / "page_0001.blocks.json").write_text(
        json.dumps(
            [
                {
                    "id": "page_0001-b001",
                    "page_key": 1,
                    "order": 1,
                    "type": "paragraph",
                    "source": "deepseek+paddle",
                    "confidence": "high",
                    "text": "This still uses x_i as inline math.",
                }
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    result = main(["validate", "--chapters", "1", "--raw-root", str(raw_root), "--output-dir", str(output_dir)])

    assert result == 1
    validation = json.loads((output_dir / "reports" / "validation.json").read_text(encoding="utf-8"))
    assert any("inline math" in error for error in validation["errors"])


def test_validate_rejects_operatorname_for_github_rendering(tmp_path):
    raw_root, _, output_dir = _write_fake_inputs(tmp_path)
    fused_dir = output_dir / "fused" / "ch01"
    blocks_dir = output_dir / "blocks" / "ch01"
    fused_dir.mkdir(parents=True)
    blocks_dir.mkdir(parents=True)
    (fused_dir / "page_0001.md").write_text(
        """---
source: UnderstandingDeepLearning_02_09_26_C.pdf
page_key: 1
book_page: 1
pdf_page: 15
chapter: "1 - Introduction"
chapter_slug: ch01-introduction
ocr_sources:
  - deepseek-ocr-2
  - ppstructurev3
fusion_status: fused
confidence: medium
figure_count: 0
---

$$
\\operatorname{ReLU}[z]
$$
""",
        encoding="utf-8",
    )
    (blocks_dir / "page_0001.blocks.json").write_text(
        json.dumps(
            [
                {
                    "id": "page_0001-b001",
                    "page_key": 1,
                    "order": 1,
                    "type": "equation",
                    "source": "deepseek+paddle",
                    "confidence": "high",
                    "latex": "\\operatorname{ReLU}[z]",
                }
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    result = main(["validate", "--chapters", "1", "--raw-root", str(raw_root), "--output-dir", str(output_dir)])

    assert result == 1
    validation = json.loads((output_dir / "reports" / "validation.json").read_text(encoding="utf-8"))
    assert any("operatorname" in error for error in validation["errors"])


def test_validate_rejects_escaped_inline_set_braces_for_github_rendering(tmp_path):
    raw_root, _, output_dir = _write_fake_inputs(tmp_path)
    fused_dir = output_dir / "fused" / "ch01"
    blocks_dir = output_dir / "blocks" / "ch01"
    fused_dir.mkdir(parents=True)
    blocks_dir.mkdir(parents=True)
    (fused_dir / "page_0001.md").write_text(
        """---
source: UnderstandingDeepLearning_02_09_26_C.pdf
page_key: 1
book_page: 1
pdf_page: 15
chapter: "1 - Introduction"
chapter_slug: ch01-introduction
ocr_sources:
  - deepseek-ocr-2
  - ppstructurev3
fusion_status: fused
confidence: medium
figure_count: 0
---

This set notation uses $\\{x_i,y_i\\}$ inline.
""",
        encoding="utf-8",
    )
    (blocks_dir / "page_0001.blocks.json").write_text(
        json.dumps(
            [
                {
                    "id": "page_0001-b001",
                    "page_key": 1,
                    "order": 1,
                    "type": "paragraph",
                    "source": "deepseek+paddle",
                    "confidence": "high",
                    "text": "This set notation uses x_i,y_i inline.",
                }
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    result = main(["validate", "--chapters", "1", "--raw-root", str(raw_root), "--output-dir", str(output_dir)])

    assert result == 1
    validation = json.loads((output_dir / "reports" / "validation.json").read_text(encoding="utf-8"))
    assert any("lbrace" in error for error in validation["errors"])


def test_validate_rejects_glued_inline_set_braces_for_github_rendering(tmp_path):
    raw_root, _, output_dir = _write_fake_inputs(tmp_path)
    fused_dir = output_dir / "fused" / "ch01"
    blocks_dir = output_dir / "blocks" / "ch01"
    fused_dir.mkdir(parents=True)
    blocks_dir.mkdir(parents=True)
    (fused_dir / "page_0001.md").write_text(
        """---
source: UnderstandingDeepLearning_02_09_26_C.pdf
page_key: 1
book_page: 1
pdf_page: 15
chapter: "1 - Introduction"
chapter_slug: ch01-introduction
ocr_sources:
  - deepseek-ocr-2
  - ppstructurev3
fusion_status: fused
confidence: medium
figure_count: 0
---

This set notation has a glued macro $\\lbracex_{i}\\rbrace$ inline.
""",
        encoding="utf-8",
    )
    (blocks_dir / "page_0001.blocks.json").write_text(
        json.dumps(
            [
                {
                    "id": "page_0001-b001",
                    "page_key": 1,
                    "order": 1,
                    "type": "paragraph",
                    "source": "deepseek+paddle",
                    "confidence": "high",
                    "text": "This set notation has a glued macro $\\lbracex_{i}\\rbrace$ inline.",
                }
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    result = main(["validate", "--chapters", "1", "--raw-root", str(raw_root), "--output-dir", str(output_dir)])

    assert result == 1
    validation = json.loads((output_dir / "reports" / "validation.json").read_text(encoding="utf-8"))
    assert any("glued inline" in error or "space after inline" in error for error in validation["errors"])


def test_validate_rejects_tagged_display_equations_for_github_rendering(tmp_path):
    raw_root, _, output_dir = _write_fake_inputs(tmp_path)
    fused_dir = output_dir / "fused" / "ch01"
    blocks_dir = output_dir / "blocks" / "ch01"
    fused_dir.mkdir(parents=True)
    blocks_dir.mkdir(parents=True)
    (fused_dir / "page_0001.md").write_text(
        """---
source: UnderstandingDeepLearning_02_09_26_C.pdf
page_key: 1
book_page: 1
pdf_page: 15
chapter: "1 - Introduction"
chapter_slug: ch01-introduction
ocr_sources:
  - deepseek-ocr-2
  - ppstructurev3
fusion_status: fused
confidence: medium
figure_count: 0
---

$$
y=\\phi_0+\\phi_1h_1.
\\tag{3.4}
$$
""",
        encoding="utf-8",
    )
    (blocks_dir / "page_0001.blocks.json").write_text(
        json.dumps(
            [
                {
                    "id": "page_0001-b001",
                    "page_key": 1,
                    "order": 1,
                    "type": "equation",
                    "source": "deepseek+paddle",
                    "confidence": "high",
                    "latex": "y=\\phi_0+\\phi_1h_1. \\tag{3.4}",
                }
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    result = main(["validate", "--chapters", "1", "--raw-root", str(raw_root), "--output-dir", str(output_dir)])

    assert result == 1
    validation = json.loads((output_dir / "reports" / "validation.json").read_text(encoding="utf-8"))
    assert any("not \\tag" in error or "uses \\tag" in error for error in validation["errors"])


def test_validate_rejects_tag_inside_aligned_environment_for_github_rendering(tmp_path):
    raw_root, _, output_dir = _write_fake_inputs(tmp_path)
    fused_dir = output_dir / "fused" / "ch01"
    blocks_dir = output_dir / "blocks" / "ch01"
    fused_dir.mkdir(parents=True)
    blocks_dir.mkdir(parents=True)
    (fused_dir / "page_0001.md").write_text(
        """---
source: UnderstandingDeepLearning_02_09_26_C.pdf
page_key: 1
book_page: 1
pdf_page: 15
chapter: "1 - Introduction"
chapter_slug: ch01-introduction
ocr_sources:
  - deepseek-ocr-2
  - ppstructurev3
fusion_status: fused
confidence: medium
figure_count: 0
---

$$
\\begin{aligned}
y&=\\phi_0+\\phi_1h_1. \\\\
\\tag{3.4}
\\end{aligned}
$$
""",
        encoding="utf-8",
    )
    (blocks_dir / "page_0001.blocks.json").write_text(
        json.dumps(
            [
                {
                    "id": "page_0001-b001",
                    "page_key": 1,
                    "order": 1,
                    "type": "equation",
                    "source": "deepseek+paddle",
                    "confidence": "high",
                    "latex": "\\begin{aligned}\ny&=\\phi_0+\\phi_1h_1. \\\\\n\\tag{3.4}\n\\end{aligned}",
                }
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    result = main(["validate", "--chapters", "1", "--raw-root", str(raw_root), "--output-dir", str(output_dir)])

    assert result == 1
    validation = json.loads((output_dir / "reports" / "validation.json").read_text(encoding="utf-8"))
    assert any("not \\tag" in error or "uses \\tag" in error for error in validation["errors"])


def test_validate_rejects_inline_math_in_markdown_headings_for_github_rendering(tmp_path):
    raw_root, _, output_dir = _write_fake_inputs(tmp_path)
    fused_dir = output_dir / "fused" / "ch01"
    blocks_dir = output_dir / "blocks" / "ch01"
    fused_dir.mkdir(parents=True)
    blocks_dir.mkdir(parents=True)
    (fused_dir / "page_0001.md").write_text(
        """---
source: UnderstandingDeepLearning_02_09_26_C.pdf
page_key: 1
book_page: 1
pdf_page: 15
chapter: "1 - Introduction"
chapter_slug: ch01-introduction
ocr_sources:
  - deepseek-ocr-2
  - ppstructurev3
fusion_status: fused
confidence: medium
figure_count: 0
---
## Conditional distribution $q(z_t)$

The heading math renders literally on GitHub.
""",
        encoding="utf-8",
    )
    (blocks_dir / "page_0001.blocks.json").write_text(
        json.dumps(
            [
                {
                    "id": "page_0001-b001",
                    "page_key": 1,
                    "order": 1,
                    "type": "heading",
                    "source": "deepseek+paddle",
                    "confidence": "high",
                    "text": "Conditional distribution q(z_t)",
                }
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    result = main(["validate", "--chapters", "1", "--raw-root", str(raw_root), "--output-dir", str(output_dir)])

    assert result == 1
    validation = json.loads((output_dir / "reports" / "validation.json").read_text(encoding="utf-8"))
    assert any("heading math" in error for error in validation["errors"])


def test_validate_rejects_ocr_spaced_math_words_for_github_rendering(tmp_path):
    raw_root, _, output_dir = _write_fake_inputs(tmp_path)
    fused_dir = output_dir / "fused" / "ch01"
    blocks_dir = output_dir / "blocks" / "ch01"
    fused_dir.mkdir(parents=True)
    blocks_dir.mkdir(parents=True)
    (fused_dir / "page_0001.md").write_text(
        """---
source: UnderstandingDeepLearning_02_09_26_C.pdf
page_key: 1
book_page: 1
pdf_page: 15
chapter: "1 - Introduction"
chapter_slug: ch01-introduction
ocr_sources:
  - deepseek-ocr-2
  - ppstructurev3
fusion_status: fused
confidence: medium
figure_count: 0
---

$$
P r(x)=N o r m_x[0, 1].
$$
""",
        encoding="utf-8",
    )
    (blocks_dir / "page_0001.blocks.json").write_text(
        json.dumps(
            [
                {
                    "id": "page_0001-b001",
                    "page_key": 1,
                    "order": 1,
                    "type": "equation",
                    "source": "deepseek+paddle",
                    "confidence": "high",
                    "text": "P r(x)=N o r m_x[0, 1].",
                }
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    result = main(["validate", "--chapters", "1", "--raw-root", str(raw_root), "--output-dir", str(output_dir)])

    assert result == 1
    validation = json.loads((output_dir / "reports" / "validation.json").read_text(encoding="utf-8"))
    assert any("OCR-spaced math token" in error for error in validation["errors"])


def test_validate_rejects_double_escaped_math_macros_for_github_rendering(tmp_path):
    raw_root, _, output_dir = _write_fake_inputs(tmp_path)
    fused_dir = output_dir / "fused" / "ch01"
    blocks_dir = output_dir / "blocks" / "ch01"
    fused_dir.mkdir(parents=True)
    blocks_dir.mkdir(parents=True)
    (fused_dir / "page_0001.md").write_text(
        """---
source: UnderstandingDeepLearning_02_09_26_C.pdf
page_key: 1
book_page: 1
pdf_page: 15
chapter: "1 - Introduction"
chapter_slug: ch01-introduction
ocr_sources:
  - deepseek-ocr-2
  - ppstructurev3
fusion_status: fused
confidence: medium
figure_count: 0
---

$$
\\\\mathrm{softmax}[z]
$$
""",
        encoding="utf-8",
    )
    (blocks_dir / "page_0001.blocks.json").write_text(
        json.dumps(
            [
                {
                    "id": "page_0001-b001",
                    "page_key": 1,
                    "order": 1,
                    "type": "equation",
                    "source": "deepseek+paddle",
                    "confidence": "high",
                    "text": "\\\\mathrm{softmax}[z]",
                }
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    result = main(["validate", "--chapters", "1", "--raw-root", str(raw_root), "--output-dir", str(output_dir)])

    assert result == 1
    validation = json.loads((output_dir / "reports" / "validation.json").read_text(encoding="utf-8"))
    assert any("double-escaped math macro" in error for error in validation["errors"])


def test_validate_rejects_single_backslash_rowbreak_math_macro_for_github_rendering(tmp_path):
    raw_root, _, output_dir = _write_fake_inputs(tmp_path)
    fused_dir = output_dir / "fused" / "ch01"
    blocks_dir = output_dir / "blocks" / "ch01"
    fused_dir.mkdir(parents=True)
    blocks_dir.mkdir(parents=True)
    (fused_dir / "page_0001.md").write_text(
        """---
source: UnderstandingDeepLearning_02_09_26_C.pdf
page_key: 1
book_page: 1
pdf_page: 15
chapter: "1 - Introduction"
chapter_slug: ch01-introduction
ocr_sources:
  - deepseek-ocr-2
  - ppstructurev3
fusion_status: fused
confidence: medium
figure_count: 0
---

$$
x = y\\ \\frac{a}{b}
$$
""",
        encoding="utf-8",
    )
    (blocks_dir / "page_0001.blocks.json").write_text(
        json.dumps(
            [
                {
                    "id": "page_0001-b001",
                    "page_key": 1,
                    "order": 1,
                    "type": "equation",
                    "source": "deepseek+paddle",
                    "confidence": "high",
                    "text": "x = y\\ \\frac{a}{b}",
                }
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    result = main(["validate", "--chapters", "1", "--raw-root", str(raw_root), "--output-dir", str(output_dir)])

    assert result == 1
    validation = json.loads((output_dir / "reports" / "validation.json").read_text(encoding="utf-8"))
    assert any("malformed row-break math macro" in error for error in validation["errors"])


def test_validate_rejects_missing_math_command_subscripts_for_github_rendering(tmp_path):
    raw_root, _, output_dir = _write_fake_inputs(tmp_path)
    fused_dir = output_dir / "fused" / "ch01"
    blocks_dir = output_dir / "blocks" / "ch01"
    fused_dir.mkdir(parents=True)
    blocks_dir.mkdir(parents=True)
    (fused_dir / "page_0001.md").write_text(
        """---
source: UnderstandingDeepLearning_02_09_26_C.pdf
page_key: 1
book_page: 1
pdf_page: 15
chapter: "1 - Introduction"
chapter_slug: ch01-introduction
ocr_sources:
  - deepseek-ocr-2
  - ppstructurev3
fusion_status: fused
confidence: medium
figure_count: 0
---

This OCR dropped the subscript marker: $q(\\mathbf{z}{t}|\\mathbf{x})$.
""",
        encoding="utf-8",
    )
    (blocks_dir / "page_0001.blocks.json").write_text(
        json.dumps(
            [
                {
                    "id": "page_0001-b001",
                    "page_key": 1,
                    "order": 1,
                    "type": "paragraph",
                    "source": "deepseek+paddle",
                    "confidence": "high",
                    "text": "This OCR dropped $q(\\mathbf{z}{t}|\\mathbf{x})$.",
                }
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    result = main(["validate", "--chapters", "1", "--raw-root", str(raw_root), "--output-dir", str(output_dir)])

    assert result == 1
    validation = json.loads((output_dir / "reports" / "validation.json").read_text(encoding="utf-8"))
    assert any("missing math subscript" in error for error in validation["errors"])


def test_validate_rejects_aligned_rowbreak_before_operator_for_github_rendering(tmp_path):
    raw_root, _, output_dir = _write_fake_inputs(tmp_path)
    fused_dir = output_dir / "fused" / "ch01"
    blocks_dir = output_dir / "blocks" / "ch01"
    fused_dir.mkdir(parents=True)
    blocks_dir.mkdir(parents=True)
    (fused_dir / "page_0001.md").write_text(
        """---
source: UnderstandingDeepLearning_02_09_26_C.pdf
page_key: 1
book_page: 1
pdf_page: 15
chapter: "1 - Introduction"
chapter_slug: ch01-introduction
ocr_sources:
  - deepseek-ocr-2
  - ppstructurev3
fusion_status: fused
confidence: medium
figure_count: 0
---

$$
\\begin{aligned}
x&\\\\=y
\\end{aligned}
$$
""",
        encoding="utf-8",
    )
    (blocks_dir / "page_0001.blocks.json").write_text(
        json.dumps(
            [
                {
                    "id": "page_0001-b001",
                    "page_key": 1,
                    "order": 1,
                    "type": "equation",
                    "source": "deepseek+paddle",
                    "confidence": "high",
                    "text": "\\begin{aligned}\nx&\\\\=y\n\\end{aligned}",
                }
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    result = main(["validate", "--chapters", "1", "--raw-root", str(raw_root), "--output-dir", str(output_dir)])

    assert result == 1
    validation = json.loads((output_dir / "reports" / "validation.json").read_text(encoding="utf-8"))
    assert any("row break before math operator" in error for error in validation["errors"])


def test_validate_rejects_bare_log_in_display_math_for_github_rendering(tmp_path):
    raw_root, _, output_dir = _write_fake_inputs(tmp_path)
    fused_dir = output_dir / "fused" / "ch01"
    blocks_dir = output_dir / "blocks" / "ch01"
    fused_dir.mkdir(parents=True)
    blocks_dir.mkdir(parents=True)
    (fused_dir / "page_0001.md").write_text(
        """---
source: UnderstandingDeepLearning_02_09_26_C.pdf
page_key: 1
book_page: 1
pdf_page: 15
chapter: "1 - Introduction"
chapter_slug: ch01-introduction
ocr_sources:
  - deepseek-ocr-2
  - ppstructurev3
fusion_status: fused
confidence: medium
figure_count: 0
---

$$
x = log\\left[y\\right]
$$
""",
        encoding="utf-8",
    )
    (blocks_dir / "page_0001.blocks.json").write_text(
        json.dumps(
            [
                {
                    "id": "page_0001-b001",
                    "page_key": 1,
                    "order": 1,
                    "type": "equation",
                    "source": "deepseek+paddle",
                    "confidence": "high",
                    "text": "x = log\\left[y\\right]",
                }
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    result = main(["validate", "--chapters", "1", "--raw-root", str(raw_root), "--output-dir", str(output_dir)])

    assert result == 1
    validation = json.loads((output_dir / "reports" / "validation.json").read_text(encoding="utf-8"))
    assert any("bare log" in error for error in validation["errors"])


def test_validate_rejects_nested_display_math_environment_for_github_rendering(tmp_path):
    raw_root, _, output_dir = _write_fake_inputs(tmp_path)
    fused_dir = output_dir / "fused" / "ch01"
    blocks_dir = output_dir / "blocks" / "ch01"
    fused_dir.mkdir(parents=True)
    blocks_dir.mkdir(parents=True)
    (fused_dir / "page_0001.md").write_text(
        """---
source: UnderstandingDeepLearning_02_09_26_C.pdf
page_key: 1
book_page: 1
pdf_page: 15
chapter: "1 - Introduction"
chapter_slug: ch01-introduction
ocr_sources:
  - deepseek-ocr-2
  - ppstructurev3
fusion_status: fused
confidence: medium
figure_count: 0
---

$$
\\begin{align*}
x &= y
\\end{align*}
$$
""",
        encoding="utf-8",
    )
    (blocks_dir / "page_0001.blocks.json").write_text(
        json.dumps(
            [
                {
                    "id": "page_0001-b001",
                    "page_key": 1,
                    "order": 1,
                    "type": "equation",
                    "source": "deepseek+paddle",
                    "confidence": "high",
                    "text": "\\begin{align*}\nx &= y\n\\end{align*}",
                }
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    result = main(["validate", "--chapters", "1", "--raw-root", str(raw_root), "--output-dir", str(output_dir)])

    assert result == 1
    validation = json.loads((output_dir / "reports" / "validation.json").read_text(encoding="utf-8"))
    assert any("nested display math environment" in error for error in validation["errors"])


def test_validate_rejects_blank_lines_inside_display_math_for_github_rendering(tmp_path):
    raw_root, _, output_dir = _write_fake_inputs(tmp_path)
    fused_dir = output_dir / "fused" / "ch01"
    blocks_dir = output_dir / "blocks" / "ch01"
    fused_dir.mkdir(parents=True)
    blocks_dir.mkdir(parents=True)
    (fused_dir / "page_0001.md").write_text(
        """---
source: UnderstandingDeepLearning_02_09_26_C.pdf
page_key: 1
book_page: 1
pdf_page: 15
chapter: "1 - Introduction"
chapter_slug: ch01-introduction
ocr_sources:
  - deepseek-ocr-2
  - ppstructurev3
fusion_status: fused
confidence: medium
figure_count: 0
---

$$
\\begin{aligned}

x &= y
\\end{aligned}
$$
""",
        encoding="utf-8",
    )
    (blocks_dir / "page_0001.blocks.json").write_text(
        json.dumps(
            [
                {
                    "id": "page_0001-b001",
                    "page_key": 1,
                    "order": 1,
                    "type": "equation",
                    "source": "deepseek+paddle",
                    "confidence": "high",
                    "text": "\\begin{aligned}\n\nx &= y\n\\end{aligned}",
                }
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    result = main(["validate", "--chapters", "1", "--raw-root", str(raw_root), "--output-dir", str(output_dir)])

    assert result == 1
    validation = json.loads((output_dir / "reports" / "validation.json").read_text(encoding="utf-8"))
    assert any("blank line inside display math" in error for error in validation["errors"])


def test_validate_rejects_stray_dollar_inside_display_math_for_github_rendering(tmp_path):
    raw_root, _, output_dir = _write_fake_inputs(tmp_path)
    fused_dir = output_dir / "fused" / "ch01"
    blocks_dir = output_dir / "blocks" / "ch01"
    fused_dir.mkdir(parents=True)
    blocks_dir.mkdir(parents=True)
    (fused_dir / "page_0001.md").write_text(
        """---
source: UnderstandingDeepLearning_02_09_26_C.pdf
page_key: 1
book_page: 1
pdf_page: 15
chapter: "1 - Introduction"
chapter_slug: ch01-introduction
ocr_sources:
  - deepseek-ocr-2
  - ppstructurev3
fusion_status: fused
confidence: medium
figure_count: 0
---

$$
\\phi]$:
$$
""",
        encoding="utf-8",
    )
    (blocks_dir / "page_0001.blocks.json").write_text(
        json.dumps(
            [
                {
                    "id": "page_0001-b001",
                    "page_key": 1,
                    "order": 1,
                    "type": "equation",
                    "source": "deepseek+paddle",
                    "confidence": "high",
                    "text": "\\phi]$:",
                }
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    result = main(["validate", "--chapters", "1", "--raw-root", str(raw_root), "--output-dir", str(output_dir)])

    assert result == 1
    validation = json.loads((output_dir / "reports" / "validation.json").read_text(encoding="utf-8"))
    assert any("stray dollar sign inside display math" in error for error in validation["errors"])


def test_validate_rejects_mismatched_probability_delimiters_for_github_rendering(tmp_path):
    raw_root, _, output_dir = _write_fake_inputs(tmp_path)
    fused_dir = output_dir / "fused" / "ch01"
    blocks_dir = output_dir / "blocks" / "ch01"
    fused_dir.mkdir(parents=True)
    blocks_dir.mkdir(parents=True)
    (fused_dir / "page_0001.md").write_text(
        """---
source: UnderstandingDeepLearning_02_09_26_C.pdf
page_key: 1
book_page: 1
pdf_page: 15
chapter: "1 - Introduction"
chapter_slug: ch01-introduction
ocr_sources:
  - deepseek-ocr-2
  - ppstructurev3
fusion_status: fused
confidence: medium
figure_count: 0
---

$$
\\Pr\\left(y_i|\\mathbf{x}_i)\\right]
$$
""",
        encoding="utf-8",
    )
    (blocks_dir / "page_0001.blocks.json").write_text(
        json.dumps(
            [
                {
                    "id": "page_0001-b001",
                    "page_key": 1,
                    "order": 1,
                    "type": "equation",
                    "source": "deepseek+paddle",
                    "confidence": "high",
                    "text": "\\Pr\\left(y_i|\\mathbf{x}_i)\\right]",
                }
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    result = main(["validate", "--chapters", "1", "--raw-root", str(raw_root), "--output-dir", str(output_dir)])

    assert result == 1
    validation = json.loads((output_dir / "reports" / "validation.json").read_text(encoding="utf-8"))
    assert any("mismatched probability delimiter" in error for error in validation["errors"])


def test_validate_rejects_one_line_multirow_aligned_equation_for_github_rendering(tmp_path):
    raw_root, _, output_dir = _write_fake_inputs(tmp_path)
    fused_dir = output_dir / "fused" / "ch01"
    blocks_dir = output_dir / "blocks" / "ch01"
    fused_dir.mkdir(parents=True)
    blocks_dir.mkdir(parents=True)
    (fused_dir / "page_0001.md").write_text(
        """---
source: UnderstandingDeepLearning_02_09_26_C.pdf
page_key: 1
book_page: 1
pdf_page: 15
chapter: "1 - Introduction"
chapter_slug: ch01-introduction
ocr_sources:
  - deepseek-ocr-2
  - ppstructurev3
fusion_status: fused
confidence: medium
figure_count: 0
---

$$
\\begin{aligned}x &= y \\\\ z &= w\\end{aligned}
$$
""",
        encoding="utf-8",
    )
    (blocks_dir / "page_0001.blocks.json").write_text(
        json.dumps(
            [
                {
                    "id": "page_0001-b001",
                    "page_key": 1,
                    "order": 1,
                    "type": "equation",
                    "source": "deepseek+paddle",
                    "confidence": "high",
                    "text": "\\begin{aligned}x &= y \\\\ z &= w\\end{aligned}",
                }
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    result = main(["validate", "--chapters", "1", "--raw-root", str(raw_root), "--output-dir", str(output_dir)])

    assert result == 1
    validation = json.loads((output_dir / "reports" / "validation.json").read_text(encoding="utf-8"))
    assert any("one-line multi-row aligned equation" in error for error in validation["errors"])


def test_validate_rejects_bare_ocr_math_tokens_in_display_math(tmp_path):
    raw_root, _, output_dir = _write_fake_inputs(tmp_path)
    fused_dir = output_dir / "fused" / "ch01"
    blocks_dir = output_dir / "blocks" / "ch01"
    fused_dir.mkdir(parents=True)
    blocks_dir.mkdir(parents=True)
    (fused_dir / "page_0001.md").write_text(
        """---
source: UnderstandingDeepLearning_02_09_26_C.pdf
page_key: 1
book_page: 1
pdf_page: 15
chapter: "1 - Introduction"
chapter_slug: ch01-introduction
ocr_sources:
  - deepseek-ocr-2
  - ppstructurev3
fusion_status: fused
confidence: medium
figure_count: 0
---

$$
\\hat{\\phi}=argmin_{\\phi}\\left[-\\sum_i log[Pr(x_i)]\\right]+Norm(0,1)
$$
""",
        encoding="utf-8",
    )
    (blocks_dir / "page_0001.blocks.json").write_text(
        json.dumps(
            [
                {
                    "id": "page_0001-b001",
                    "page_key": 1,
                    "order": 1,
                    "type": "equation",
                    "source": "deepseek+paddle",
                    "confidence": "high",
                    "text": "\\hat{\\phi}=argmin_{\\phi}\\left[-\\sum_i log[Pr(x_i)]\\right]+Norm(0,1)",
                }
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    result = main(["validate", "--chapters", "1", "--raw-root", str(raw_root), "--output-dir", str(output_dir)])

    assert result == 1
    validation = json.loads((output_dir / "reports" / "validation.json").read_text(encoding="utf-8"))
    assert any("bare OCR math token" in error for error in validation["errors"])


def test_validate_rejects_prose_wrapped_as_display_equation(tmp_path):
    raw_root, _, output_dir = _write_fake_inputs(tmp_path)
    fused_dir = output_dir / "fused" / "ch01"
    blocks_dir = output_dir / "blocks" / "ch01"
    fused_dir.mkdir(parents=True)
    blocks_dir.mkdir(parents=True)
    (fused_dir / "page_0001.md").write_text(
        """---
source: UnderstandingDeepLearning_02_09_26_C.pdf
page_key: 1
book_page: 1
pdf_page: 15
chapter: "1 - Introduction"
chapter_slug: ch01-introduction
ocr_sources:
  - deepseek-ocr-2
  - ppstructurev3
fusion_status: fused
confidence: medium
figure_count: 0
---

$$
\\begin{aligned}
&where we have multiplied both sides by \\sqrt{x}
\\end{aligned}
$$
""",
        encoding="utf-8",
    )
    (blocks_dir / "page_0001.blocks.json").write_text(
        json.dumps(
            [
                {
                    "id": "page_0001-b001",
                    "page_key": 1,
                    "order": 1,
                    "type": "equation",
                    "source": "deepseek+paddle",
                    "confidence": "high",
                    "text": "\\begin{aligned}\n&where we have multiplied both sides by \\sqrt{x}\n\\end{aligned}",
                }
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    result = main(["validate", "--chapters", "1", "--raw-root", str(raw_root), "--output-dir", str(output_dir)])

    assert result == 1
    validation = json.loads((output_dir / "reports" / "validation.json").read_text(encoding="utf-8"))
    assert any("prose inside display math" in error for error in validation["errors"])


def test_validate_rejects_dollar_superscript_footnote_markers(tmp_path):
    raw_root, _, output_dir = _write_fake_inputs(tmp_path)
    fused_dir = output_dir / "fused" / "ch01"
    blocks_dir = output_dir / "blocks" / "ch01"
    fused_dir.mkdir(parents=True)
    blocks_dir.mkdir(parents=True)
    (fused_dir / "page_0001.md").write_text(
        """---
source: UnderstandingDeepLearning_02_09_26_C.pdf
page_key: 1
book_page: 1
pdf_page: 15
chapter: "1 - Introduction"
chapter_slug: ch01-introduction
ocr_sources:
  - deepseek-ocr-2
  - ppstructurev3
fusion_status: fused
confidence: medium
figure_count: 0
---

This prose uses a literal math footnote marker:$^1$

$^1$ Footnote text.
""",
        encoding="utf-8",
    )
    (blocks_dir / "page_0001.blocks.json").write_text(
        json.dumps(
            [
                {
                    "id": "page_0001-b001",
                    "page_key": 1,
                    "order": 1,
                    "type": "paragraph",
                    "source": "deepseek+paddle",
                    "confidence": "high",
                    "text": "This prose uses a literal math footnote marker.",
                }
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    result = main(["validate", "--chapters", "1", "--raw-root", str(raw_root), "--output-dir", str(output_dir)])

    assert result == 1
    validation = json.loads((output_dir / "reports" / "validation.json").read_text(encoding="utf-8"))
    assert any("Markdown footnotes" in error for error in validation["errors"])


def test_validate_rejects_markdown_links_that_are_not_relative_to_fused_page(tmp_path):
    raw_root, paddle_dir, output_dir = _write_fake_inputs(tmp_path)
    assert (
        main(
            [
                "prepare",
                "--chapters",
                "1",
                "--raw-root",
                str(raw_root),
                "--paddle-pages-dir",
                str(paddle_dir),
                "--output-dir",
                str(output_dir),
            ]
        )
        == 0
    )

    fused_dir = output_dir / "fused" / "ch01"
    blocks_dir = output_dir / "blocks" / "ch01"
    fused_dir.mkdir(parents=True)
    blocks_dir.mkdir(parents=True)
    (fused_dir / "page_0001.md").write_text(
        """---
source: UnderstandingDeepLearning_02_09_26_C.pdf
page_key: 1
book_page: 1
pdf_page: 15
chapter: "1 - Introduction"
chapter_slug: ch01-introduction
ocr_sources:
  - deepseek-ocr-2
  - ppstructurev3
fusion_status: fused
confidence: medium
figure_count: 1
---

<p align="center">
  <img src="figures/page_0001_fig_1.jpg" alt="Figure" />
</p>
""",
        encoding="utf-8",
    )
    (blocks_dir / "page_0001.blocks.json").write_text(
        json.dumps(
            [
                {
                    "id": "page_0001-b001",
                    "page_key": 1,
                    "order": 1,
                    "type": "figure",
                    "image_path": "figures/page_0001_fig_1.jpg",
                    "source": "paddle",
                    "confidence": "high",
                }
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    result = main(["validate", "--chapters", "1", "--raw-root", str(raw_root), "--output-dir", str(output_dir)])

    assert result == 1
    validation = json.loads((output_dir / "reports" / "validation.json").read_text(encoding="utf-8"))
    assert any("usually ../../figures/page_0001_fig_1.jpg" in error for error in validation["errors"])


def test_validate_rejects_plain_markdown_figure_syntax(tmp_path):
    raw_root, paddle_dir, output_dir = _write_fake_inputs(tmp_path)
    assert (
        main(
            [
                "prepare",
                "--chapters",
                "1",
                "--raw-root",
                str(raw_root),
                "--paddle-pages-dir",
                str(paddle_dir),
                "--output-dir",
                str(output_dir),
            ]
        )
        == 0
    )

    fused_dir = output_dir / "fused" / "ch01"
    blocks_dir = output_dir / "blocks" / "ch01"
    fused_dir.mkdir(parents=True)
    blocks_dir.mkdir(parents=True)
    (fused_dir / "page_0001.md").write_text(
        """---
source: UnderstandingDeepLearning_02_09_26_C.pdf
page_key: 1
book_page: 1
pdf_page: 15
chapter: "1 - Introduction"
chapter_slug: ch01-introduction
ocr_sources:
  - deepseek-ocr-2
  - ppstructurev3
fusion_status: fused
confidence: medium
figure_count: 1
---

![Figure](../../figures/page_0001_fig_1.jpg)
""",
        encoding="utf-8",
    )
    (blocks_dir / "page_0001.blocks.json").write_text(
        json.dumps(
            [
                {
                    "id": "page_0001-b001",
                    "page_key": 1,
                    "order": 1,
                    "type": "figure",
                    "image_path": "figures/page_0001_fig_1.jpg",
                    "source": "paddle",
                    "confidence": "high",
                }
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    result = main(["validate", "--chapters", "1", "--raw-root", str(raw_root), "--output-dir", str(output_dir)])

    assert result == 1
    validation = json.loads((output_dir / "reports" / "validation.json").read_text(encoding="utf-8"))
    assert any("centered HTML image block" in error for error in validation["errors"])


def test_validate_rejects_uncentered_figure_caption_after_image(tmp_path):
    raw_root, paddle_dir, output_dir = _write_fake_inputs(tmp_path)
    assert (
        main(
            [
                "prepare",
                "--chapters",
                "1",
                "--raw-root",
                str(raw_root),
                "--paddle-pages-dir",
                str(paddle_dir),
                "--output-dir",
                str(output_dir),
            ]
        )
        == 0
    )

    fused_dir = output_dir / "fused" / "ch01"
    blocks_dir = output_dir / "blocks" / "ch01"
    fused_dir.mkdir(parents=True)
    blocks_dir.mkdir(parents=True)
    (fused_dir / "page_0001.md").write_text(
        """---
source: UnderstandingDeepLearning_02_09_26_C.pdf
page_key: 1
book_page: 1
pdf_page: 15
chapter: "1 - Introduction"
chapter_slug: ch01-introduction
ocr_sources:
  - deepseek-ocr-2
  - ppstructurev3
fusion_status: fused
confidence: medium
figure_count: 1
---

<p align="center">
  <img src="../../figures/page_0001_fig_1.jpg" alt="Figure" />
</p>

Figure 1.1 Plain caption text.
""",
        encoding="utf-8",
    )
    (blocks_dir / "page_0001.blocks.json").write_text(
        json.dumps(
            [
                {
                    "id": "page_0001-b001",
                    "page_key": 1,
                    "order": 1,
                    "type": "figure",
                    "image_path": "figures/page_0001_fig_1.jpg",
                    "source": "paddle",
                    "confidence": "high",
                }
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    result = main(["validate", "--chapters", "1", "--raw-root", str(raw_root), "--output-dir", str(output_dir)])

    assert result == 1
    validation = json.loads((output_dir / "reports" / "validation.json").read_text(encoding="utf-8"))
    assert any("centered and bold" in error for error in validation["errors"])


def test_validate_rejects_uncentered_html_image(tmp_path):
    raw_root, paddle_dir, output_dir = _write_fake_inputs(tmp_path)
    assert (
        main(
            [
                "prepare",
                "--chapters",
                "1",
                "--raw-root",
                str(raw_root),
                "--paddle-pages-dir",
                str(paddle_dir),
                "--output-dir",
                str(output_dir),
            ]
        )
        == 0
    )

    fused_dir = output_dir / "fused" / "ch01"
    blocks_dir = output_dir / "blocks" / "ch01"
    fused_dir.mkdir(parents=True)
    blocks_dir.mkdir(parents=True)
    (fused_dir / "page_0001.md").write_text(
        """---
source: UnderstandingDeepLearning_02_09_26_C.pdf
page_key: 1
book_page: 1
pdf_page: 15
chapter: "1 - Introduction"
chapter_slug: ch01-introduction
ocr_sources:
  - deepseek-ocr-2
  - ppstructurev3
fusion_status: fused
confidence: medium
figure_count: 1
---

<img src="../../figures/page_0001_fig_1.jpg" alt="Figure" />
""",
        encoding="utf-8",
    )
    (blocks_dir / "page_0001.blocks.json").write_text(
        json.dumps(
            [
                {
                    "id": "page_0001-b001",
                    "page_key": 1,
                    "order": 1,
                    "type": "figure",
                    "image_path": "figures/page_0001_fig_1.jpg",
                    "source": "paddle",
                    "confidence": "high",
                }
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    result = main(["validate", "--chapters", "1", "--raw-root", str(raw_root), "--output-dir", str(output_dir)])

    assert result == 1
    validation = json.loads((output_dir / "reports" / "validation.json").read_text(encoding="utf-8"))
    assert any("image is not centered" in error for error in validation["errors"])


def test_validate_rejects_formula_crops_in_final_markdown_and_blocks(tmp_path):
    raw_root, paddle_dir, output_dir = _write_fake_inputs(tmp_path)
    assert (
        main(
            [
                "prepare",
                "--chapters",
                "1",
                "--raw-root",
                str(raw_root),
                "--paddle-pages-dir",
                str(paddle_dir),
                "--output-dir",
                str(output_dir),
            ]
        )
        == 0
    )

    fused_dir = output_dir / "fused" / "ch01"
    blocks_dir = output_dir / "blocks" / "ch01"
    fused_dir.mkdir(parents=True)
    blocks_dir.mkdir(parents=True)
    (fused_dir / "page_0001.md").write_text(
        """---
source: UnderstandingDeepLearning_02_09_26_C.pdf
page_key: 1
book_page: 1
pdf_page: 15
chapter: "1 - Introduction"
chapter_slug: ch01-introduction
ocr_sources:
  - deepseek-ocr-2
  - ppstructurev3
fusion_status: fused
confidence: medium
figure_count: 1
---

$$
x = y
$$

<p align="center">
  <img src="../../figures/page_0001_fig_2.jpg" alt="Equation crop" />
</p>
""",
        encoding="utf-8",
    )
    (blocks_dir / "page_0001.blocks.json").write_text(
        json.dumps(
            [
                {
                    "id": "page_0001-b001",
                    "page_key": 1,
                    "order": 1,
                    "type": "figure",
                    "image_path": "figures/page_0001_fig_2.jpg",
                    "source": "paddle",
                    "confidence": "low",
                }
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    result = main(["validate", "--chapters", "1", "--raw-root", str(raw_root), "--output-dir", str(output_dir)])

    assert result == 1
    validation = json.loads((output_dir / "reports" / "validation.json").read_text(encoding="utf-8"))
    assert any("nonvisual PPStructure crop" in error for error in validation["errors"])


def test_validate_rejects_semantic_ocr_math_residue(tmp_path):
    raw_root, _, output_dir = _write_fake_inputs(tmp_path)
    fused_dir = output_dir / "fused" / "ch01"
    blocks_dir = output_dir / "blocks" / "ch01"
    fused_dir.mkdir(parents=True)
    blocks_dir.mkdir(parents=True)
    (fused_dir / "page_0001.md").write_text(
        r"""---
source: UnderstandingDeepLearning_02_09_26_C.pdf
page_key: 1
book_page: 1
pdf_page: 15
chapter: "1 - Introduction"
chapter_slug: ch01-introduction
ocr_sources:
  - deepseek-ocr-2
  - ppstructurev3
fusion_status: fused
confidence: medium
figure_count: 0
---

The joint distribution of the latent variables {z_{t}} is:

(18.17)

This inline probability still uses an OCR token: $Pr(y|x)$.

This caption-like text has glued commands $\lambdaK$ and $y_d\inR$.

$$
\mathbf{z}_{t}=\sqrt{1-\beta_{t}}\cdot\mathbf{z}_{t-1}
\quad\forall t\in\lbrace 2,\cdots,T
$$

$$
\left\
|\mathbf{x}-\mathbf{y}\right\
|^2
$$
""",
        encoding="utf-8",
    )
    (blocks_dir / "page_0001.blocks.json").write_text(
        json.dumps(
            [
                {
                    "id": "page_0001-b001",
                    "page_key": 1,
                    "order": 1,
                    "type": "paragraph",
                    "source": "deepseek",
                    "confidence": "medium",
                    "text": "The joint distribution of the latent variables {z_{t}} is:",
                },
                {
                    "id": "page_0001-b002",
                    "page_key": 1,
                    "order": 2,
                    "type": "paragraph",
                    "source": "deepseek",
                    "confidence": "medium",
                    "text": "(18.17)",
                },
                {
                    "id": "page_0001-b003",
                    "page_key": 1,
                    "order": 3,
                    "type": "equation",
                    "source": "deepseek",
                    "confidence": "medium",
                    "text": "$$\n\\left\\\n|\\mathbf{x}-\\mathbf{y}\\right\\\n|^2\n$$",
                },
                {
                    "id": "page_0001-b004",
                    "page_key": 1,
                    "order": 4,
                    "type": "figure",
                    "source": "paddle",
                    "confidence": "medium",
                    "image_path": "figures/page_0001_fig_1.jpg",
                    "alt": "Figure alt has a truncated OCR macro \\par",
                },
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    result = main(["validate", "--chapters", "1", "--raw-root", str(raw_root), "--output-dir", str(output_dir)])

    assert result == 1
    validation = json.loads((output_dir / "reports" / "validation.json").read_text(encoding="utf-8"))
    errors = "\n".join(validation["errors"])
    assert "raw OCR math braces" in errors
    assert "standalone equation number" in errors
    assert "bare OCR math token inside inline math" in errors
    assert "glued math command" in errors
    assert "missing closing \\rbrace" in errors
    assert "broken sized delimiter before norm bar" in errors
