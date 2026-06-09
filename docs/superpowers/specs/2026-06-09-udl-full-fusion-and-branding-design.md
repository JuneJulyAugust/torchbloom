# UDL Full Fusion And Branding Design

**Date:** 2026-06-09
**Status:** Approved for low-risk implementation
**Scope:** UDL source cleanup, full-book fusion workflow, answer booklet normalization, and TorchBloom brand assets

## Purpose

Move the successful UDL chapters 1-3 fusion pilot toward a durable source layer without deleting evidence before a validated replacement exists. Also add a small TorchBloom visual identity so the repository README better reflects the project.

## Key Constraint

The repository currently has validated hybrid OCR fusion output only for UDL chapters 1-3. The rest of the textbook has not yet been run through the full PPStructureV3 plus Codex fusion workflow. Cleanup must therefore be staged:

1. Publish and clean only the validated fused scope.
2. Keep source PDFs and manifests.
3. Do not delete un-replaced source-derived Markdown for a future full-book scope until that scope validates.

## Source Layout

`raw/udl/source/` remains the immutable source area and must keep:

- `UnderstandingDeepLearning_02_09_26_C.pdf`
- `UDL_Answer_Booklet_Students.pdf`
- `SHA256SUMS`

`raw/udl/textbook/` becomes the curated fused OCR source layer for generated Markdown that has passed validation.

```text
raw/udl/textbook/
  chapter_map.json
  index.md
  log.md
  pages/
    ch01-introduction/
      page_0001.md
  blocks/
    ch01/
      page_0001.blocks.json
  figures/
    page_0002_fig_1.jpg
```

Final page filenames use printed book page numbers. PDF page numbers remain in Markdown frontmatter as provenance.

Display equations use `$$` delimiters so they render in GitHub Markdown and local previews. Do not publish pages with `\[` and `\]` display delimiters.

## Cleanup Rules

Legacy DeepSeek-only artifacts are removable only when a validated replacement covers the same page:

- old PDF-page-key Markdown under `raw/udl/textbook/pages/<chapter>/page_00XX.md`,
- DeepSeek raw text under `raw/udl/textbook/raw_ocr/page_00XX.txt`,
- rendered page images under `raw/udl/textbook/images/page_00XX.png`,
- old DeepSeek crop files under `raw/udl/textbook/figures/page_00XX_fig_*`.

The cleanup stage must be implemented as a deterministic publish command, not manual deletion. It must validate the fused output first, copy the replacement Markdown, block JSON, and referenced final figures, then remove only the legacy files for that validated page range.

## Answer Booklet

The current answer booklet pages are extracted from embedded PDF text, not DeepSeek OCR. They should not be deleted as DeepSeek-only output. The full-book follow-up should normalize answer pages into the same source-friendly contract:

- `page_key` and `answer_page` metadata,
- `pdf_page` provenance,
- `chapter` and `chapter_slug`,
- `extraction_method: pymupdf-text`,
- optional future block sidecars if answers need LLM parsing.

This is lower risk than OCR fusion because the PDF exposes selectable text, but it should still be regenerated through code and tested.

## Branding

Add versionable SVG assets under `assets/brand/`:

- `torchbloom-icon.svg`: square icon for project identity.
- `torchbloom-logo.svg`: compact logo lockup.
- `torchbloom-title-banner-v2.svg`: README banner, versioned so GitHub refreshes the rendered image instead of serving a cached draft.

The visual direction is a warm torch flame joined with a sprout and small learning-path nodes. It should feel rigorous, kind, and curriculum-first rather than flashy.

## README Update

Place the title banner at the top of `README.md`, above the existing project title. Keep the current bilingual project name and mission text.

## Validation

Before publishing or cleanup:

- `python -m torchbloom.udl_fusion_pilot validate --chapters 1,2,3` must pass for the current publish scope.
- `python -m pytest` must pass.
- The publish command must produce a report recording copied pages, copied figures, copied block sidecars, and cleaned legacy files.

## Full-Book Follow-Up

The whole textbook and answer booklet should be completed in a later pass with these gates:

1. Generate PPStructureV3 page evidence for the full PDF at high resolution.
2. Prepare Codex fusion prompts for each chapter.
3. Fuse chapter batches.
4. Recrop final figures from high-resolution PDF renders.
5. Validate all generated Markdown, block JSON, figure paths, figure counts, centered figures, centered captions, and absence of review notes.
6. Publish only after validation passes for the requested scope.
7. Clean legacy artifacts only for pages that were published.
