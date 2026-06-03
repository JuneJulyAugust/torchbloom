# UDL OCR Runbook

OCR uses a separate Python 3.12 environment because `mlx-vlm` and DeepSeek-OCR-2 are Apple-Silicon-oriented runtime dependencies.

## Setup

```bash
/opt/homebrew/bin/python3.12 -m venv .venv-ocr
.venv-ocr/bin/pip install --upgrade pip
.venv-ocr/bin/pip install -e ".[ocr]"
.venv-ocr/bin/pip install "transformers==4.46.3" "tokenizers==0.20.3"
```

## Pilot

```bash
.venv-ocr/bin/torchbloom-udl-ocr --chapters 1,2,3 --keep-page-images
.venv-ocr/bin/torchbloom-udl-ocr --status --chapters 1,2,3
```

Inspect `raw/udl/textbook/pages/`, `raw/udl/textbook/figures/`, and `raw/udl/textbook/images/` before scaling.

## Reparse

```bash
.venv-ocr/bin/torchbloom-udl-ocr --chapters 1,2,3 --reparse
```

Reparse uses saved raw OCR and does not run the model.
