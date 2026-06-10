# UDL Full Fusion And Branding Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development for full-book chapter fusion. This low-risk branch may be implemented inline because it only publishes the already validated pilot scope and adds guardrails.

**Goal:** Publish the validated UDL chapters 1-3 fusion layer safely, document the full-book migration, and add TorchBloom brand assets to the README.

**Architecture:** Extend the existing deterministic UDL fusion utility with a guarded `publish` command. Keep semantic fusion in Codex/subagents, keep validation before cleanup, and store final source-derived fused pages under `raw/udl/textbook/`.

**Tech Stack:** Python 3.12, pathlib/shutil/json/yaml, pytest, SVG assets, Markdown docs.

---

## File Structure

- Create: `docs/superpowers/specs/2026-06-09-udl-full-fusion-and-branding-design.md`
- Create: `docs/superpowers/plans/2026-06-09-udl-full-fusion-and-branding.md`
- Create: `assets/brand/torchbloom-icon.svg`
- Create: `assets/brand/torchbloom-logo.svg`
- Create: `assets/brand/torchbloom-title-banner-v2.svg`
- Modify: `README.md`
- Modify: `raw/udl/README.md`
- Modify: `src/torchbloom/udl_fusion_pilot.py`
- Modify: `src/torchbloom/udl_answer_extract.py`
- Modify: `tests/test_udl_fusion_pilot.py`
- Modify: `tests/test_udl_answer_extract.py`
- Generate tracked: `raw/udl/textbook/pages/`, `raw/udl/textbook/blocks/`, `raw/udl/textbook/figures/`, `raw/udl/textbook/index.md`, `raw/udl/textbook/log.md`
- Regenerate tracked: `raw/udl/answers/pages/`, `raw/udl/answers/index.md`

## Task 1: Branch And Baseline

- [x] Pull merged `main`.
- [x] Create branch `codex/udl-full-fusion-branding`.
- [x] Run the current fusion validator for chapters 1-3.
- [x] Run the focused pytest suite before publish.

## Task 2: Documentation

- [x] Write the design spec.
- [x] Write this implementation plan.
- [x] Update `raw/udl/README.md` so it describes the new staged source layout.

## Task 3: Branding

- [x] Add the square SVG icon.
- [x] Add the compact SVG logo.
- [x] Add the versioned README title banner SVG.
- [x] Insert the banner at the top of `README.md`.

## Task 4: Guarded Publish Command

- [x] Add `publish` to `torchbloom-udl-fusion-pilot`.
- [x] Make `publish` validate the selected chapters before copying or cleaning.
- [x] Copy fused Markdown to `raw/udl/textbook/pages/<chapter-slug>/page_XXXX.md`.
- [x] Copy block JSON to `raw/udl/textbook/blocks/chXX/page_XXXX.blocks.json`.
- [x] Copy only final referenced figure assets to `raw/udl/textbook/figures/`.
- [x] With `--clean-legacy`, remove only legacy DeepSeek raw text, old rendered page images, old PDF-page Markdown, and old legacy figures for the published pages.
- [x] Write a publish report to `raw/udl/textbook/log.md`.

## Task 5: Tests

- [x] Add a test that `publish` refuses to run when validation fails.
- [x] Add a test that `publish --clean-legacy` copies the fused page, sidecar, and referenced figure while removing only matching legacy files.
- [x] Run targeted fusion utility tests.

## Task 6: Normalize Answer Booklet Metadata

- [x] Add `page_key`, `answer_page`, `extraction_method`, and `fusion_status` to extracted answer-page frontmatter.
- [x] Update answer extractor tests for the expanded metadata contract.
- [x] Regenerate `raw/udl/answers/pages/` from `UDL_Answer_Booklet_Students.pdf`.

## Task 7: Publish Validated Pilot Scope

- [x] Run `python -m torchbloom.udl_fusion_pilot validate --chapters 1,2,3`.
- [x] Run `python -m torchbloom.udl_fusion_pilot publish --chapters 1,2,3 --clean-legacy`.
- [x] Verify `raw/udl/textbook/pages/` now uses book-page filenames.
- [x] Verify `raw/udl/textbook/raw_ocr/` and `raw/udl/textbook/images/` no longer contain files for the published Ch1-3 scope.

## Task 8: Final Verification

- [x] Run `python -m pytest`.
- [x] Run `python -m torchbloom.udl_fusion_pilot validate --chapters 1,2,3`.
- [x] Run `python -m torchbloom.wiki_validation`.
- [x] Parse SVG assets as XML.
- [x] Review `git status --short`.
- [x] Review `git diff --stat`.
- [ ] Commit and push the branch.

## Task 9: GitHub Rendering Follow-Up

- [x] Redesign brand SVGs to remove the dotted icon arc and avoid decorative overlap with banner text.
- [x] Convert published display equations from `\[` and `\]` to `$$`.
- [x] Convert published inline equations from `\(...\)` to `$...$`.
- [x] Replace GitHub-blocked `\operatorname{...}` math macros with `\mathrm{...}`.
- [x] Convert inline set braces from `\{...\}` to `\lbrace ...\rbrace`.
- [x] Add validation that rejects bracket display math, parenthesis inline math, blocked `\operatorname` macros, and escaped inline set braces in fused Markdown.
- [x] Run focused tests and full validation.
- [x] Replace published `\tag{...}` equation numbering with visible plain equation numbers such as `\quad (15.1)` to avoid GitHub sanitizer and vertical-stack failures.
- [x] Convert `$^1$` footnote markers to Markdown footnotes.
- [x] Add validation for any published `\tag{...}` display numbering and `$^n$` footnote markers.
