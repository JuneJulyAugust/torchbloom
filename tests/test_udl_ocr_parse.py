# tests/test_udl_ocr_parse.py
from torchbloom.udl_ocr_parse import parse_elements, _clean_inline

SAMPLE = (
    "<|ref|>title<|/ref|><|det|>[[100, 80, 900, 130]]<|/det|>"
    "# A Tour of the Cell\n"
    "<|ref|>text<|/ref|><|det|>[[100, 200, 480, 600]]<|/det|>"
    "Cells are the basic unit of life.\n"
    "<|ref|>image<|/ref|><|det|>[[520, 200, 900, 560]]<|/det|>"
)


def test_parse_elements_counts_and_types():
    els = parse_elements(SAMPLE)
    assert [e["type"] for e in els] == ["title", "text", "image"]


def test_parse_elements_coords():
    els = parse_elements(SAMPLE)
    assert els[2]["coords"] == [[520, 200, 900, 560]]


def test_parse_elements_content_text():
    els = parse_elements(SAMPLE)
    assert "basic unit of life" in els[1]["content"]


def test_clean_inline_strips_tags():
    assert _clean_inline("<|ref|>text<|/ref|><|det|>[[1,2,3,4]]<|/det|>hi") == "hi"


# append to tests/test_udl_ocr_parse.py
from torchbloom.udl_ocr_parse import merge_figures


def test_merge_unions_touching_image_fragments():
    els = [
        {"type": "image", "coords": [[100, 100, 300, 300]]},
        {"type": "image", "coords": [[295, 100, 500, 300]]},  # touches the first
        {"type": "text", "coords": [[100, 700, 900, 780]]},
    ]
    crops, absorbed = merge_figures(els)
    assert absorbed == set()
    assert len(crops) == 1          # two fragments merged into one figure
    _, box = crops[0]
    assert box == [100, 100, 500, 300]


def test_merge_keeps_separate_distant_images():
    els = [
        {"type": "image", "coords": [[100, 100, 300, 300]]},
        {"type": "image", "coords": [[600, 600, 800, 800]]},
    ]
    crops, _ = merge_figures(els)
    assert len(crops) == 2


# append to tests/test_udl_ocr_parse.py
from torchbloom.udl_ocr_parse import detect_uncovered_figure


def test_no_uncovered_figure_on_plain_text_page():
    els = [
        {"type": "text", "coords": [[100, 100, 900, 200]]},
        {"type": "text", "coords": [[100, 220, 900, 320]]},
    ]
    assert detect_uncovered_figure(els) is None


def test_uncovered_figure_returns_box_when_central_void_flanked():
    # Label content on the far left and far right with a large empty middle band.
    els = [
        {"type": "text", "coords": [[10, 200, 60, 800]]},    # left labels
        {"type": "text", "coords": [[940, 200, 990, 800]]},  # right labels
        {"type": "image", "coords": [[0, 850, 1000, 980]]},  # bottom panel row
    ]
    box = detect_uncovered_figure(els)
    assert box is not None
    assert box[0] >= 0 and box[2] <= 1000 and box[3] > box[1]


# append to tests/test_udl_ocr_parse.py
from torchbloom.udl_ocr_parse import build_caption, reconstruct_markdown


def test_build_caption_picks_nearby_formal_figure_label():
    els = [
        {"type": "image", "coords": [[100, 100, 400, 400]]},
        {"type": "text", "coords": [[100, 410, 400, 450]],
         "content": "Figure 6.6 The endomembrane system. Details follow."},
    ]
    cap = build_caption([100, 100, 400, 400], els)
    assert cap.startswith("Figure 6.6")


def test_reconstruct_markdown_inserts_figure_block_and_dedups():
    els = [
        {"type": "text", "coords": [[0, 0, 10, 10]], "content": "Intro line."},
        {"type": "text", "coords": [[0, 0, 10, 10]], "content": "Intro line."},  # dup
        {"type": "image", "coords": [[0, 0, 10, 10]], "content": ""},
    ]
    md = reconstruct_markdown(els, {2: (1, "Caption")}, 51)
    assert md.count("Intro line.") == 1
    assert "![Figure 1](../../figures/page_0051_fig_1.png)" in md
    assert "**Figure 1** — Caption" in md
from torchbloom.udl_ocr_parse import (
    parse_grounding_to_crops, build_frontmatter, parse_figure_title,
)


def test_parse_grounding_to_crops_basic():
    raw = (
        "<|ref|>sub_title<|/ref|><|det|>[[100, 80, 900, 130]]<|/det|>"
        "## The Cell\n"
        "<|ref|>text<|/ref|><|det|>[[100, 200, 900, 600]]<|/det|>"
        "Body text about cells.\n"
        "<|ref|>image<|/ref|><|det|>[[100, 650, 500, 950]]<|/det|>"
        "<|ref|>text<|/ref|><|det|>[[100, 955, 500, 985]]<|/det|>"
        "Figure 6.1 A cell."
    )
    md, crops, meta = parse_grounding_to_crops(raw, page_num=93)
    assert "## The Cell" in md
    assert "Body text about cells." in md
    assert len(crops) == 1                     # (fig_idx, per-mille box)
    assert crops[0][0] == 1
    assert "![Figure 1](../../figures/page_0093_fig_1.png)" in md
    assert "The Cell" in meta["headings"]


def test_build_frontmatter_shape():
    fm = build_frontmatter(
        source="UnderstandingDeepLearning_02_09_26_C.pdf", page_key=93, pdf_page=142,
        title="A Tour of the Cell", chapter="6 — A Tour of the Cell",
        chapter_slug="ch03-shallow-neural-networks",
        figures=["page_0093_fig_1.png"], headings=["The Cell"],
    )
    assert fm.startswith("---")
    assert "page_key: 93" in fm
    assert "pdf_page: 142" in fm
    assert fm.index("page_key: 93") < fm.index("pdf_page: 142")
    assert "chapter_slug: ch03-shallow-neural-networks" in fm
    assert "figure_count: 1" in fm


def test_parse_figure_title_only_with_figure_pattern():
    assert parse_figure_title("Figure 6.8 Exploring Eukaryotic Cells\n", "") \
        == "Figure 6.8 Exploring Eukaryotic Cells"
    assert parse_figure_title("random banner text\n", "") is None
    # skipped when body already references the figure
    assert parse_figure_title("Figure 6.8 X\n", "see Figure 6.8 here") is None
