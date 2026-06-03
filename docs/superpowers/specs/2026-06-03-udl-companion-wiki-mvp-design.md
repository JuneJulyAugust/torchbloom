# UDL Companion Wiki MVP Design

**Date:** 2026-06-03
**Status:** Draft for user review
**Pilot:** Understanding Deep Learning chapters 1, 2, and 3

## 1. Purpose

Build a private, noncommercial TorchBloom companion wiki for Simon J. D. Prince's *Understanding Deep Learning* (UDL). The MVP should help a learner understand the book from high-school math foundations through structured interpretation, questions, practice, and notebook guidance.

The wiki is a companion, not a mirror of the book. It should not copy the book into Markdown. It should build original TorchBloom explanations, source anchors, prerequisite bridges, worked examples, and practice scaffolds that let a learner read UDL with less friction and more active recall.

## 2. Confirmed Decisions

- TorchBloom stays private and noncommercial for now.
- Do not vendor the full UDL GitHub repository in this stage.
- Do not introduce Ilya-30u30 or any other advanced repo into this MVP.
- The UDL repo does not appear to contain the complete book TeX source, so the textbook PDF remains the source of truth for chapter prose, exercises, figures, and equations.
- Download the latest textbook PDF and the student answer booklet into `raw/udl/source/`.
- Use DeepSeek-OCR-2, following the proven BioBloom OCR approach, for the textbook raw layer.
- Pilot chapters are 1, 2, and 3. Chapter 1 is easy, but it is useful as a smoke test for OCR, source anchoring, math-bridge style, and exercise extraction before chapters 2 and 3 carry the real learning load.

## 3. Source Inputs

Source metadata verified on 2026-06-03:

| Source | URL | Version / Status | Use |
| --- | --- | --- | --- |
| Latest UDL textbook PDF | `https://github.com/udlbook/udlbook/releases/download/v5.0.3/UnderstandingDeepLearning_02_09_26_C.pdf` | `v5.0.3`, released 2026-02-09, 5th printing, SHA-256 `f8237d393163900fa8e43210e680a3f987b45ccac7750b372e156fae3df0bf32` | Primary source for book prose, figures, equations, and end-of-chapter questions. |
| Student answer booklet | `https://raw.githubusercontent.com/udlbook/udlbook/main/UDL_Answer_Booklet_Students.pdf` | Git blob SHA `e175e817fad73ceb1458571629c8fd6fbbc89e53`, SHA-256 `ec58fde8a42da57979808b284e52a26e0b67142817d47a657772b09144d1dcf3` | Source for selected answers and solution anchors. |
| UDL website | `https://udlbook.github.io/udlbook/` | Public project site | Human-facing source discovery for official links, coding exercises, errata, and book status. |

The repository root license for UDL is Creative Commons Attribution-NonCommercial-NoDerivatives 4.0. Because the TorchBloom wiki is private and noncommercial, local source intake and private adapted study notes are acceptable for this stage. If TorchBloom becomes public or commercial, UDL-derived adapted wiki pages must be reviewed and likely rewritten or removed before sharing.

## 4. Repository Organization

The MVP adds a UDL-specific source and wiki area without changing the broader TorchBloom structure.

```text
raw/
  udl/
    README.md
    manifests/
      udlbook-v5.0.3.md
    source/
      UnderstandingDeepLearning_02_09_26_C.pdf
      UDL_Answer_Booklet_Students.pdf
      SHA256SUMS
    chapter_map.json
    textbook/
      raw_ocr/
      pages/
      figures/
      images/
      index.md
      log.md
    answers/
      pages/
      index.md

docs/
  udl-wiki/
    README.md
    source-policy.md
    ocr-runbook.md
    authoring-guide.md

wiki/
  udl/
    index.md
    methodology.md
    schema.md
    audit-queue.md
    chapters/
      ch01/
      ch02/
      ch03/
    concepts/
    math-bridges/
    equations/
    practices/
    notebook-guides/
```

`raw/udl/` is source evidence. It is read-only after creation except for regenerated OCR artifacts. `wiki/udl/` is authored study knowledge. `docs/udl-wiki/` explains the workflow and decisions.

## 5. OCR Strategy

Use the BioBloom OCR architecture as the model:

1. Render PDF pages with PyMuPDF.
2. Run local DeepSeek-OCR-2 in grounding mode through `mlx-vlm`.
3. Persist raw OCR output per page immediately.
4. Parse raw OCR into clean per-page Markdown, source metadata, and figure crops.
5. Support resume, force retry, and reparse without rerunning the model.

For the textbook, DeepSeek-OCR-2 is preferred over embedded PDF text because UDL has equations, figures, captions, and layout-dependent explanations. The PDF text layer can still help with outline extraction, sanity checks, and search, but it is not the primary wiki-building artifact.

For the answer booklet, start with embedded text extraction because the booklet is simpler and shorter. Use OCR fallback only when equations, layout, or answer numbering cannot be trusted.

## 6. Wiki Design

The wiki should be question- and practice-centered, not just concept summaries.

### 6.1 Chapter Packs

Each pilot chapter gets a chapter pack:

```text
wiki/udl/chapters/ch02/
  index.md
  reading-guide.md
  concept-map.md
  equation-map.md
  practice-index.md
  notebook-guide.md
```

Chapter pack responsibilities:

- State what the chapter is trying to teach.
- List prerequisite math and programming ideas.
- Map UDL sections to TorchBloom concept pages.
- Track equations and symbols that the learner must understand.
- Index all book questions and selected answers.
- Connect notebook exercises to concepts and practice cards.

### 6.2 Shared Concept Pages

Concept pages live in `wiki/udl/concepts/` and are shared across chapters. A concept should not be duplicated under each chapter.

Required sections:

- `## Core Idea`
- `## Why It Matters In UDL`
- `## High-School Bridge`
- `## Formal Version`
- `## Worked Example`
- `## Common Misconceptions`
- `## Practice Hooks`
- `## Source Anchors`
- `## Related`

The high-school bridge is the heart of TorchBloom's contribution. It explains what background math is actually needed and gives a ramp from familiar algebra, functions, graphs, tables, and probability into UDL notation.

### 6.3 Math Bridge Pages

Math bridge pages live in `wiki/udl/math-bridges/`. They are not generic textbook chapters. They exist only when UDL needs a piece of math and a high-school learner may not have it yet.

Examples:

- `functions-as-machines.md`
- `vectors-as-lists-of-numbers.md`
- `matrices-as-function-machines.md`
- `partial-derivatives-as-one-variable-at-a-time-slopes.md`
- `logarithms-for-loss-functions.md`

Each bridge page ends with a "Ready for UDL when..." checklist.

### 6.4 Equation Pages

Equation pages live in `wiki/udl/equations/`. UDL is equation-heavy, and equations should become first-class learning objects rather than buried inside prose.

Each equation page records:

- The equation in LaTeX.
- What each symbol means.
- The shape or graph intuition.
- A small numerical example.
- What can change and what stays fixed.
- Which UDL section and page introduced it.
- Which concept and practice pages consume it.

### 6.5 Practice Cards

Practice cards live in `wiki/udl/practices/`. They are the MVP's learning engine.

Each card has:

- A source question or TorchBloom-created question id.
- Prerequisites.
- Type: `recall`, `explain`, `compute`, `derive`, `code`, `debug`, or `transfer`.
- A prompt written in original TorchBloom wording.
- Hints.
- Answer policy: `selected-answer`, `torchbloom-derived`, or `review-needed`.
- A short self-check rubric.
- Links to concept pages, equation pages, and notebook guides.

Book questions and selected answers are used as anchors, but the wiki should not copy full solutions into public-style pages. For the private MVP, concise answer notes may be stored, but they should be treated as restricted source-derived content.

### 6.6 Notebook Guides

Notebook guides live in `wiki/udl/notebook-guides/`. The UDL website provides notebook exercises for the whole text, including chapter 1, chapter 2, and several chapter 3 notebooks. The MVP should not clone the full repo. It should link to official notebooks and, when needed, download only the pilot notebook files into raw intake after a source-policy review.

Each notebook guide explains:

- What concept the notebook reinforces.
- What code the learner should inspect before filling blanks.
- What output shape or plot to expect.
- What mistakes reveal.
- What practice cards should be completed before and after.

## 7. Pilot Scope

The Ch1-3 pilot is complete when these artifacts exist:

- Raw source manifest and checksums for textbook and answer booklet.
- OCR chapter map derived from the textbook outline.
- DeepSeek OCR output and parsed Markdown for chapters 1, 2, and 3.
- Answer booklet extracted pages for selected answers covering chapters 1, 2, and 3 when available.
- Chapter packs for Ch1, Ch2, and Ch3.
- A concept inventory for all concepts required by Ch1-3.
- Math bridge pages for every high-school foundation gap that blocks Ch1-3.
- Equation pages for every equation used by Ch1-3 practice cards.
- Practice cards for every Ch1-3 end-of-chapter question.
- Notebook guide pages for official notebooks associated with Ch1-3.
- Validation checks for source checksums, wiki frontmatter, source-anchor existence, and broken links.

## 8. Quality And Review Standards

Every wiki page must be source-grounded and learner-centered.

Acceptance checklist:

- The page has frontmatter with `id`, `type`, `chapter_scope`, `source_anchors`, `confidence`, `prerequisites`, `related`, and `learning_objectives`.
- Every UDL-specific claim has a source anchor into raw OCR pages, answer pages, or official site metadata.
- The page distinguishes intuition from formal notation.
- Practice cards include hints and a self-check rubric.
- Answer-derived material is marked with restricted private status.
- OCR uncertainty is recorded in `wiki/udl/audit-queue.md`.
- No generated page is treated as reviewed until a human checks it against raw source pages.

Confidence values:

- `directional`: agent-authored from raw sources, not human-reviewed.
- `reviewed`: checked by one human against source anchors.
- `validated`: checked against source anchors and used successfully in practice or tests.

## 9. Non-Goals

- Do not build a web app in this MVP.
- Do not cover the whole UDL book yet.
- Do not train models or run GPU workloads.
- Do not ingest Ilya-30u30.
- Do not clone or vendor the full UDL GitHub repository.
- Do not publish UDL-derived adapted wiki content.
- Do not build a general-purpose OCR framework beyond what the Ch1-3 UDL workflow needs.

## 10. Open Design Risks

- OCR may mangle equations or math symbols. Mitigation: keep page images, compare against PDF rendering, and create equation pages only after source review.
- The answer booklet may not include every exercise. Mitigation: mark practice cards as `selected-answer`, `torchbloom-derived`, or `review-needed`.
- A private repo can drift toward public reuse. Mitigation: source-derived answer notes and OCR text stay under raw/restricted policy, and wiki pages remain original synthesis where possible.
- The Ch1-3 pilot may reveal that concept pages alone are not enough. Mitigation: treat practice cards and equation pages as first-class wiki objects from the beginning.
