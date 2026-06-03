# UDL Raw Source Intake

This folder stores private, noncommercial source material and OCR artifacts for the TorchBloom companion wiki for Simon J. D. Prince's *Understanding Deep Learning*.

## Layout

- `manifests/` - source records, license notes, checksums, retrieval dates, and review status.
- `source/` - downloaded source PDFs approved for this private MVP.
- `textbook/raw_ocr/` - immutable DeepSeek-OCR-2 raw output per textbook page.
- `textbook/pages/` - parsed per-page Markdown from textbook OCR.
- `textbook/figures/` - cropped figure images from textbook OCR.
- `textbook/images/` - optional rendered page images kept during pilot review.
- `answers/pages/` - extracted answer booklet pages for selected answers.

Raw artifacts are evidence. Do not edit them by hand; regenerate them through the pipeline and record the change in `textbook/log.md` or `answers/index.md`.
