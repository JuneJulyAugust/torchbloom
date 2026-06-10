# UDL Source Intake

This folder stores private, noncommercial source material and source-derived working artifacts for the TorchBloom companion wiki for Simon J. D. Prince's *Understanding Deep Learning*.

## Layout

- `manifests/` - source records, license notes, checksums, retrieval dates, and review status.
- `source/` - downloaded source PDFs approved for this private MVP. Keep these PDFs.
- `textbook/pages/` - validated fused Markdown pages using printed book page filenames.
- `textbook/blocks/` - validated block JSON sidecars for LLM parsing.
- `textbook/figures/` - final referenced high-resolution figure crops.
- `answers/pages/` - extracted answer booklet pages for selected answers.

The old DeepSeek-only text layer is being replaced in stages by the PPStructureV3 plus Codex fusion method. Cleanup is allowed only after the selected fused scope validates and is published by `torchbloom-udl-fusion-pilot publish`.

The answer booklet pages are extracted from embedded PDF text rather than DeepSeek OCR, so they are not part of the DeepSeek-only cleanup. Regenerate them through `torchbloom-udl-answers` when their metadata contract changes.

Do not edit source-derived pages by hand; regenerate or publish them through the pipeline and record the change in `textbook/log.md` or `answers/index.md`.
