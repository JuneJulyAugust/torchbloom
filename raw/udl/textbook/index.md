# UDL Textbook Fused Source Layer

This directory stores validated private, source-derived UDL fused OCR pages.
Final Markdown filenames use printed book page numbers; each page keeps `pdf_page` provenance in frontmatter.

## Published Scope

- Chapter 1: Introduction (`pages/ch01-introduction/page_0001.md` through `page_0016.md`)
- Chapter 2: Supervised learning (`pages/ch02-supervised-learning/page_0017.md` through `page_0024.md`)
- Chapter 3: Shallow neural networks (`pages/ch03-shallow-neural-networks/page_0025.md` through `page_0040.md`)

## Assets

- Referenced figure files: 31
- Block sidecars: `blocks/chXX/page_XXXX.blocks.json`

## Cleanup Policy

Legacy DeepSeek-only raw text, old rendered page images, and old PDF-page-key Markdown are removed only for pages that have a validated fused replacement.
