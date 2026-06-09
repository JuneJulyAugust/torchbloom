# UDL OCR And Fusion Runbook

The original OCR pilot used a separate Python 3.12 environment because `mlx-vlm` and DeepSeek-OCR-2 are Apple-Silicon-oriented runtime dependencies. The curated textbook layer now comes from the hybrid fusion workflow: PPStructureV3 for layout and figures, DeepSeek-OCR-2 for prose and math candidates, and Codex-session review for semantic fusion.

## Setup

```bash
/opt/homebrew/bin/python3.12 -m venv .venv-ocr
.venv-ocr/bin/pip install --upgrade pip
.venv-ocr/bin/pip install -e ".[ocr]"
.venv-ocr/bin/pip install "transformers==4.46.3" "tokenizers==0.20.3"
```

## Legacy DeepSeek OCR Pilot

```bash
.venv-ocr/bin/torchbloom-udl-ocr --chapters 1,2,3 --keep-page-images
.venv-ocr/bin/torchbloom-udl-ocr --status --chapters 1,2,3
```

This command path is kept for reproducibility, but its direct Markdown output is no longer the curated source layer.

## Reparse

```bash
.venv-ocr/bin/torchbloom-udl-ocr --chapters 1,2,3 --reparse
```

Reparse uses saved legacy raw OCR and does not run the model. It is only available before that legacy scope has been cleaned by the fused publish step.

## Fused Publish

```bash
python -m torchbloom.udl_fusion_pilot validate --chapters 1,2,3
python -m torchbloom.udl_fusion_pilot publish --chapters 1,2,3 --clean-legacy
```

The publish step validates the fused output before touching `raw/udl/textbook/`, copies book-page-key Markdown, block JSON sidecars, and final referenced figures, then removes legacy DeepSeek-only files for the validated scope.
