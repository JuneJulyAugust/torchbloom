# UDL Hybrid OCR Fusion Pilot Design

**Date:** 2026-06-09
**Status:** Pilot successful
**Scope:** *Understanding Deep Learning* chapters 1, 2, and 3

## Purpose

Create a private fusion pilot that combines the strongest parts of the two OCR paths already tested on UDL chapters 1-3:

- **PPStructureV3:** better page parsing, visual region detection, and figure cropping.
- **DeepSeek-OCR-2:** better current Markdown prose and LaTeX-style math transcription.

The pilot should produce an LLM-friendly page layer that is more organized than either raw output alone, while keeping the original OCR evidence visible enough for review.

## Core Decision

Do not call OpenAI through `OPENAI_API_KEY` or any external API in this pilot. The meaning-aware merge is performed inside the Codex session, with subagents assigned to chapter-sized batches.

Python code is allowed only for deterministic work:

- collect inputs,
- copy figure crops,
- write per-page fusion prompts,
- validate output paths and schemas,
- summarize status.

Python must not decide which OCR text is semantically correct when the sources conflict.

## Source Inputs

Read-only evidence:

- DeepSeek parsed pages: `raw/udl/textbook/pages/`
- DeepSeek raw OCR: `raw/udl/textbook/raw_ocr/`
- Original rendered page images: `raw/udl/textbook/images/`
- Chapter ranges: `raw/udl/textbook/chapter_map.json`
- PPStructureV3 page Markdown and figure crops: `output/udl-ocr-comparison/paddleocr-structure/pages/`

The PPStructureV3 comparison output is temporary. The fusion pilot copies the needed crops and Markdown into its own ignored workspace before the old comparison output is cleaned.

## Output Contract

All generated pilot artifacts live under ignored `output/udl-fusion-pilot/`.

```text
output/udl-fusion-pilot/
  inputs/
    page_0015/  # source PDF page key
      manifest.json
      deepseek.md
      paddle.md
      paddle_figures/
      original_page.png
  prompts/
    page_0001.md  # printed book page key
  figures/
    page_0001_fig_1.png
  fused/
    ch01/
      page_0001.md
  blocks/
    ch01/
      page_0001.blocks.json
  reports/
    summary.md
    ch01.md
    ch02.md
    ch03.md
```

### Fused Markdown

Each fused page has YAML frontmatter:

- `source`
- `page_key` (printed book page number)
- `book_page`
- `pdf_page`
- `chapter`
- `chapter_slug`
- `ocr_sources`
- `fusion_status`
- `confidence`
- `figure_count`

The body should preserve normal reading order, section headings, equations in LaTeX when available, figure references, and captions. Review notes are useful during fusion, but they must not remain in final Markdown frontmatter or body text.

Markdown math must use GitHub-compatible syntax:

- Display equations use `$$` delimiters rather than `\[` and `\]`.
- Inline equations use `$...$` rather than `\(...\)`.
- Named functions use GitHub-accepted forms such as `\mathrm{ReLU}` and `\mathrm{argmin}` rather than `\operatorname{...}`.
- Inline literal set braces use `\lbrace ...\rbrace` rather than `\{...\}`, because Markdown may consume the backslash escapes before MathJax receives the expression.
- Numbered display equations do not use `\tag{...}`. GitHub may reject or vertically stack tagged equations, so visible numbers are written inside the display as plain math text, for example `\quad (3.4)`.
- Footnotes use Markdown footnote syntax such as `[^1]` and `[^1]: ...`, not math superscript markers such as `$^1$`.

GitHub renders `$$` math blocks and `$...$` inline math in Markdown files, while the bracket and parenthesis delimiters may render in local previews but appear as plain text on GitHub. GitHub's math sanitizer may reject some LaTeX macros, including `\operatorname`.

### Blocks JSON

Each page also has a lightweight block sidecar for future LLM parsing:

```json
[
  {
    "id": "page_0001-b001",
    "page_key": 1,
    "order": 1,
    "type": "heading",
    "text": "Chapter 1",
    "source": "deepseek+paddle",
    "confidence": "high"
  }
]
```

Supported block types are `heading`, `paragraph`, `equation`, `figure`, `caption`, `table`, `list`, `exercise`, and `review_note`.

For figure blocks, the sidecar records the stable crop path under `output/udl-fusion-pilot/figures/`. PPStructureV3 visual crops are the visual source of truth unless a crop is visibly wrong. PPStructureV3 formula crops are evidence only and must not appear as final Markdown images or JSON figure blocks.

Final visual crops must be centered in fused Markdown using this HTML form:

```html
<p align="center">
  <img src="../../figures/page_0028_fig_1.jpg" alt="Figure 3.3" />
</p>
```

Figure captions immediately below visual crops must also be centered and should bold the figure label:

```html
<p align="center">
  <strong>Figure 3.14</strong> Processing in network...
</p>
```

Final visual crop files should be regenerated from the original PDF at high resolution after fusion preparation. The pilot uses PPStructureV3's layout boxes as the source of truth, then crops from a 600-DPI PDF render with small side/top padding and larger bottom padding so labels are not clipped. This preserves Paddle's page parsing while avoiding low-resolution model-output crops.

When PPStructureV3 misses a figure or detects only part of a multi-panel figure, the reviewer may add an explicit manual override under `output/udl-fusion-pilot/manual-figure-overrides.json`. Overrides must include the page key, reason, stable output path, and layout-space bounding box, and the resulting crop must still be generated from the 600-DPI source PDF.

## Fusion Rules

1. Use PPStructureV3 as the page-layout and figure-cropping backbone.
2. Use DeepSeek Markdown as the first candidate for prose and math.
3. Prefer DeepSeek LaTeX for equations when it matches the surrounding context.
4. Preserve PPStructureV3 visual crops for figures, charts, and tables.
5. Do not preserve PPStructureV3 formula crops in final pages when LaTeX is available; use them only to verify or repair the LaTeX transcription.
6. If a displayed equation exists only as a PPStructureV3 image and cannot be transcribed confidently, add a `review_note` block instead of linking the crop.
7. Fused Markdown must use centered HTML image blocks, not plain Markdown image syntax.
8. Image paths inside `fused/chXX/` must be real relative paths such as `../../figures/page_0028_fig_1.jpg`.
9. `figure_count` counts final non-formula visual crops, not all PPStructureV3 crops.
10. Keep uncertainty out of final Markdown; use reports or JSON sidecars for audit notes.
11. Use printed book page numbers for fused Markdown, block JSON, prompt, and final figure filenames. Keep PDF page numbers in metadata and source/evidence paths.
12. Do not create public-facing curriculum pages from this layer yet; this remains source-derived OCR working output.
13. Use GitHub-compatible math: `$$` for display math, `$...$` for inline math, `\mathrm{...}` for named functions instead of `\operatorname{...}`, `\lbrace ...\rbrace` for inline set braces, and plain visible equation numbers like `\quad (3.4)` instead of `\tag{...}`.
14. Use Markdown footnotes such as `[^1]`; do not encode footnote markers as `$^1$`.

## Subagent Split

Use three subagents with disjoint write areas:

- Chapter 1: pages 15-30, writes `fused/ch01/`, `blocks/ch01/`, `reports/ch01.md`
- Chapter 2: pages 31-38, writes `fused/ch02/`, `blocks/ch02/`, `reports/ch02.md`
- Chapter 3: pages 39-54, writes `fused/ch03/`, `blocks/ch03/`, `reports/ch03.md`

The main Codex session owns the design docs, utility code, cleanup, validation, and final summary.

## Quality Bar

The pilot is useful when:

- every Ch1-3 page has a fused Markdown page and block JSON sidecar,
- every referenced figure path exists,
- no final page links to PPStructureV3 formula crops,
- every final visual crop is centered with `<p align="center">`,
- every figure caption under a visual crop is centered and bolds the `Figure X.Y` label,
- no final Markdown file contains `review_notes` frontmatter or `Review note` body text,
- figure paths resolve from their actual `fused/chXX/` location,
- stable figure files are regenerated from high-resolution PDF renders using the PPStructureV3 boxes,
- manual figure overrides are recorded when PPStructureV3 misses or under-crops a required visual,
- leading figure captions have enough final visual image blocks to match them,
- display equations avoid `\tag{...}` and footnotes use Markdown footnote syntax,
- per-page frontmatter is parseable,
- uncertainty is explicit in reports or sidecars rather than final Markdown,
- the report explains where PPStructureV3 was better, where DeepSeek was better, and where human review is still needed.

## Pilot Outcome

The three-chapter pilot completed successfully. The final generated layer lives in ignored `output/udl-fusion-pilot/`, uses printed book page numbers for reader-facing filenames, records PDF page numbers as provenance, centers all figure visuals and captions, and excludes review notes from final Markdown. The validation gate passed for all 40 pages and 306 JSON blocks after the final migration.
