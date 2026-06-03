---
id: udl-methodology
type: methodology
title: UDL Companion Methodology
chapter_scope: [ch01, ch02, ch03]
source_anchors:
  - source: udlbook-v5.0.3
    locator: docs/superpowers/specs/2026-06-03-udl-companion-wiki-mvp-design.md
confidence: directional
prerequisites: []
related: [udl-schema, udl-audit-queue]
learning_objectives:
  - Explain how TorchBloom separates source evidence from authored learning synthesis.
---

# UDL Companion Methodology

TorchBloom keeps three layers separate.

## Source Evidence

Raw PDFs, OCR text, page images, figure crops, and answer booklet pages live
under `raw/udl/`. These files are private evidence. They should be regenerated,
not hand-edited.

## Interpretation

Wiki pages under `wiki/udl/` explain the material in original TorchBloom terms.
They should cite raw anchors but should not mirror long source passages.

## Learning Design

The learning layer is question-centered. Every chapter should produce:

- a reading guide,
- a practice index,
- concept pages,
- math bridges,
- equation pages,
- practice cards,
- notebook guidance.

## Review States

- `directional`: useful draft from raw sources, not human-reviewed.
- `reviewed`: checked against source anchors by a human.
- `validated`: checked and used successfully in learning or tests.

