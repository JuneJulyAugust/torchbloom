# UDL Full Textbook Fusion Rollout Plan

## Goal

Publish the full *Understanding Deep Learning* textbook extraction under `raw/udl/textbook` using the validated hybrid fusion method from chapters 1-3.

The finished corpus should keep the pilot contract:

- Markdown filenames use printed book page numbers.
- Frontmatter records both `book_page` and `pdf_page`.
- Figures are high-resolution PDF recrops from Paddle layout boxes.
- Figures and figure captions are centered.
- Figure labels such as `Figure 3.14` are bold.
- Equation crops are removed when a LaTeX equation is present.
- Markdown is GitHub-safe: display math uses `$$`, inline math uses `$...$`, and fragile tagged equations avoid unsupported macros.
- Final pages contain no review notes.

## Scope

- Keep the existing reviewed chapters 1-3 as the quality baseline.
- Generate and fuse chapters 4-21 from the source PDF.
- Publish the complete validated corpus back to `raw/udl/textbook`.
- Keep the source PDF and durable docs.
- Clean DeepSeek-only intermediate markdown only after the fused corpus validates.

## Execution

1. Baseline the current state.
   - Confirm git is clean.
   - Confirm chapters 1-3 validate with the current fusion validator.
   - Confirm `chapter_map.json` covers chapters 1-21 and PDF pages 15-450.

2. Generate source evidence for chapters 4-21.
   - Run DeepSeek OCR2 with retained page images for the remaining chapter pages.
   - Run Paddle LayoutDetection over those page images for stable layout and figure boxes.
   - Store Paddle layout markdown, JSON, and cropped image evidence under `output/udl-ocr-comparison/paddleocr-structure`.
   - Resume by chapter/page so partial failures do not require restarting the whole book.

3. Prepare fusion inputs.
   - Use the existing fusion preparer to combine DeepSeek text, Paddle layout markdown, source page image, and chapter metadata.
   - Preserve chapter/page mapping from the printed book page convention.

4. Fuse chapters 4-21.
   - Fuse chapter batches with the same rules proven by chapters 1-3.
   - Prefer LaTeX equations over equation crops.
   - Prefer Paddle figure boxes for visual crops.
   - Treat multi-panel figures as one figure when the printed page shows one complete figure.
   - Keep captions with the figure and avoid repeating caption text as ordinary prose.

5. Recrop and normalize figures.
   - Recrop final referenced figures from the source PDF at high resolution.
   - Center image blocks and figure-note/caption text.
   - Bold figure identifiers.
   - Verify every referenced figure path exists.

6. Validate before publish.
   - Run the fusion validator across chapters 1-21.
   - Run unit tests.
   - Run wiki/content validation.
   - Spot-check known fragile patterns: unsupported GitHub math macros, duplicated equation crops, missing figures, broken relative figure paths, and lingering review notes.

7. Publish and clean.
   - Publish all validated chapters to `raw/udl/textbook`.
   - Remove legacy DeepSeek-only markdown and raw intermediates only after publish validation passes.
   - Keep the source PDF and curated docs.

8. Wrap up.
   - Update docs if the full-book workflow changes.
   - Commit the rollout in coherent steps.
   - Push the branch.

## Validation Commands

```bash
.venv/bin/python -m torchbloom.udl_fusion_pilot validate --chapters 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21
.venv/bin/python -m pytest
.venv/bin/python -m torchbloom.wiki_validation
```

## Implementation Note

The original pilot used full PPStructureV3 outputs. During the full-book rollout, the full PPStructureV3 parser loaded table/formula recognition models and was killed under memory pressure during prediction. The production rollout therefore uses Paddle's `LayoutDetection` model directly through `torchbloom.udl_paddle_structure`. This keeps the useful Paddle behavior, namely human-like layout and figure boundaries, while avoiding the unstable heavy parser. Formula crops remain evidence only; final equations still come from LaTeX fusion.

## Outcome

Published the full textbook source layer on 2026-06-09.

- Fused Markdown pages: 436
- Block sidecars: 436
- Referenced high-resolution figure crops: 275
- Legacy DeepSeek-only files cleaned during final publish: 418
- Final block count after footer cleanup: 3,815

Final verification passed with:

```bash
.venv/bin/python -m torchbloom.udl_fusion_pilot validate --chapters 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21
.venv/bin/python -m pytest
.venv/bin/python -m torchbloom.wiki_validation
```

Targeted scans also found no lingering review notes, Markdown image syntax, GitHub-hostile math delimiters/macros, or OCR footer license artifacts in `raw/udl/textbook/pages`.

## Rollback

If full publish validation fails, keep the current reviewed chapters 1-3 in `raw/udl/textbook`, leave generated evidence in `output/`, and do not clean legacy/intermediate files until the failing chapter is corrected.
