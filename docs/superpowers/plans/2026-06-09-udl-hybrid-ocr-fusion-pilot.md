# UDL Hybrid OCR Fusion Pilot Implementation Plan

> **For agentic workers:** Keep generated source-derived artifacts in ignored `output/`. Do not call external OCR or LLM APIs. The semantic fusion work happens inside the Codex session or assigned Codex subagents.

**Goal:** Produce a 3-chapter fusion pilot that combines PPStructureV3 layout/figures with DeepSeek-OCR-2 prose/math for UDL chapters 1-3.

**Status:** Completed successfully. Final generated artifacts live under ignored `output/udl-fusion-pilot/`; durable conventions and validation code are tracked in this branch.

**Architecture:** Add a small deterministic Python CLI to prepare page evidence and validate fused outputs. Use Codex subagents to write meaning-aware fused Markdown and block JSON for disjoint chapter batches. Keep durable design and plan files under `docs/superpowers/`.

**Tech Stack:** Python 3.12, stdlib JSON/argparse/shutil/pathlib, existing `PyYAML` dependency for frontmatter checks, pytest, Codex subagents for chapter synthesis.

---

## File Structure

- Create: `docs/superpowers/specs/2026-06-09-udl-hybrid-ocr-fusion-pilot-design.md`
- Create: `docs/superpowers/plans/2026-06-09-udl-hybrid-ocr-fusion-pilot.md`
- Create: `src/torchbloom/udl_fusion_pilot.py`
- Create: `tests/test_udl_fusion_pilot.py`
- Modify: `pyproject.toml`
- Generate ignored: `output/udl-fusion-pilot/`
- Remove ignored after evidence copy: `output/udl-ocr-comparison/`

## Task 1: Clean Confusing Old Wiki Areas

- [x] Delete the old confusing raw/wiki/docs wiki directories.
- [x] Remove stale README and lesson references to those directories.
- [x] Verify no old wiki-directory references remain.

## Task 2: Add Fusion Utility

- [x] Add `torchbloom-udl-fusion-pilot` CLI with `prepare` and `validate` subcommands.
- [x] Load chapter ranges from `raw/udl/textbook/chapter_map.json`.
- [x] Copy DeepSeek Markdown, PPStructureV3 Markdown, original page images, and PPStructureV3 figure crops into `output/udl-fusion-pilot/inputs/`.
- [x] Write stable figure copies under `output/udl-fusion-pilot/figures/`.
- [x] Write one fusion prompt per page under `output/udl-fusion-pilot/prompts/`.
- [x] Write `reports/summary.md` describing expected fused outputs.
- [x] Validate fused Markdown frontmatter, block JSON, page coverage, and referenced figure paths.

## Task 3: Add Focused Tests

- [x] Test that `prepare` writes manifests, prompts, source copies, and stable figure paths from a small fake UDL workspace.
- [x] Test that `validate` accepts a minimal fused page plus block sidecar.
- [x] Test that `validate` reports a missing fused figure reference.

## Task 4: Build Pilot Inputs And Clean Old Output

- [x] Run `prepare --chapters 1,2,3` using current DeepSeek and PPStructureV3 outputs.
- [x] Confirm 40 page prompts and manifests were generated.
- [x] Remove `output/udl-ocr-comparison/` after the needed PPStructureV3 evidence has been copied into the fusion pilot workspace.

## Task 5: Run Codex Subagent Fusion

- [x] Assign Chapter 1 pages 15-30 to a subagent writing only `output/udl-fusion-pilot/fused/ch01/`, `blocks/ch01/`, and `reports/ch01.md`.
- [x] Assign Chapter 2 pages 31-38 to a subagent writing only `output/udl-fusion-pilot/fused/ch02/`, `blocks/ch02/`, and `reports/ch02.md`.
- [x] Assign Chapter 3 pages 39-54 to a subagent writing only `output/udl-fusion-pilot/fused/ch03/`, `blocks/ch03/`, and `reports/ch03.md`.
- [x] Review the chapter reports and spot-check representative pages.

## Task 6: Verify And Summarize

- [x] Run unit tests.
- [x] Run fusion output validation.
- [x] Write or update `output/udl-fusion-pilot/reports/summary.md`.
- [x] Report what was created, what was cleaned, and which quality issues still need human review.

## Task 7: Fix Pilot Review Gaps And Rerun Fusion

- [x] Add validation that rejects final Markdown links to PPStructureV3 formula crops.
- [x] Add validation that rejects final JSON figure blocks pointing to formula crops.
- [x] Add validation that rejects Markdown image paths that do not resolve from `fused/chXX/`.
- [x] Refresh prompts so formula crops are evidence-only and final Markdown links use `../../figures/...`.
- [x] Delete the previous fused Markdown, block JSON, and chapter reports before rerunning fusion.
- [x] Rerun chapter fusion subagents from the refreshed prompts.
- [x] Revalidate all 40 pages with the stricter validator.
- [x] Update the final pilot summary with the corrected output counts and review flags.

## Task 8: Center Final Figures

- [x] Refresh prompts to require centered HTML image blocks for final visual crops.
- [x] Add validation that rejects plain Markdown image syntax for final visual crops.
- [x] Convert existing fused pages to centered `<p align="center"><img ... /></p>` blocks.
- [x] Revalidate all 40 pages after centering figures.

## Task 9: Regenerate High-Resolution Figure Assets

- [x] Add `recrop-figures` CLI to crop from high-resolution source pages using PPStructureV3 layout boxes.
- [x] Add a regression test for layout-box scaling onto a higher-resolution page image.
- [x] Recrop all Ch1-3 stable figure assets from the original PDF at 600 DPI.
- [x] Use modest side/top padding and larger bottom padding so axis labels are not clipped.
- [x] Revalidate all 40 fused pages after the high-resolution asset swap.

## Task 10: Patch Manual Figure-Crop Misses Found In Review

- [x] Add a validator gate for leading figure captions that do not have enough final visual image blocks.
- [x] Record manual high-resolution crop overrides for page 37 Figure 2.4 and page 40 Figures 3.1-3.2.
- [x] Regenerate those corrected crops from the source PDF at 600 DPI.
- [x] Update page 40 Markdown and block JSON to include centered figure images.
- [x] Re-run full pilot validation and the unit test suite.

## Task 11: Switch Final Artifacts To Book Page Keys

- [x] Add `book_page` metadata and keep `pdf_page` as source provenance.
- [x] Rename final fused Markdown, block JSON, prompts, and stable figure assets to printed book-page keys.
- [x] Keep source evidence input folders under their original PDF-page keys.
- [x] Remove review-note frontmatter and body text from final Markdown.
- [x] Center figure-caption text below visual crops and bold the `Figure X.Y` label.
- [x] Add validation for book-page metadata, removed Markdown review notes, and centered/bold figure captions.

## Final Verification

- [x] `python -m torchbloom.udl_fusion_pilot validate --chapters 1,2,3` passed for 40 pages and 306 blocks.
- [x] `python -m pytest` passed for the full test suite.
- [x] Final Markdown uses printed book-page filenames, records `pdf_page`, removes review notes, and centers/bolds figure captions.
