# PaddleOCR UDL OCR Evaluation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Evaluate PaddleOCR output against the existing DeepSeek-OCR-2 conversion for UDL chapters 1-3 and decide whether PaddleOCR should replace or supplement the current OCR path.

**Architecture:** Treat the existing DeepSeek artifacts as the baseline and keep `raw/udl/` immutable during the pilot. Run PaddleOCR from a local Python virtualenv, not Docker, against the already-rendered page PNGs for PDF pages 15-54. Write all generated comparison artifacts under ignored `output/`, and commit only the curated evaluation note/runbook updates after review.

**Tech Stack:** Python 3.12, existing TorchBloom UDL chapter map, existing DeepSeek-OCR-2 raw Markdown artifacts, PaddleOCR PP-StructureV3, PaddlePaddle CPU or local GPU runtime, Markdown/JSON comparison reports, git for the final documentation commit.

---

## Context

Existing first-three-chapter source state as of 2026-06-08:

- Ch1 Introduction: PDF pages 15-30, 16 pages.
- Ch2 Supervised learning: PDF pages 31-38, 8 pages.
- Ch3 Shallow neural networks: PDF pages 39-54, 16 pages.
- DeepSeek baseline is complete: `40/40 pages done | complete=True | error_pages=[]`.
- Page PNG inputs exist for all 40 pages under `raw/udl/textbook/images/`.
- Parsed DeepSeek Markdown exists for all 40 pages under `raw/udl/textbook/pages/`.
- Raw DeepSeek model output exists for all 40 pages under `raw/udl/textbook/raw_ocr/`.

Official PaddleOCR references checked on 2026-06-08:

- PaddleOCR GitHub README: https://github.com/PaddlePaddle/PaddleOCR
- PaddleOCR quick start: https://www.paddleocr.ai/main/en/quick_start.html
- PP-StructureV3 usage tutorial: https://www.paddleocr.ai/main/en/version3.x/pipeline_usage/PP-StructureV3.html
- PaddleOCR says it converts PDFs/images into structured JSON/Markdown and highlights PP-StructureV3 plus PaddleOCR-VL.
- The quick start documents installing `paddlepaddle==3.2.0` and `paddleocr[all]`, and supports both PaddlePaddle and Transformers inference engines.
- The PP-StructureV3 tutorial shows `res.save_to_json(...)`, `res.save_to_markdown(...)`, and PDF/page Markdown concatenation APIs.
- The PP-StructureV3 tutorial notes that English-only documents should use English recognition settings such as `lang="en"` or an English text-recognition model.
- PaddleOCR's Apple Silicon tutorial says official Docker images are not currently supported for that hardware and recommends manual virtualenv installation.
- PaddleOCR's Apple Silicon acceleration path is for PaddleOCR-VL with an MLX-VLM service backend. Standard PP-StructureV3/PP-OCR should be treated as CPU-only on macOS for this evaluation.

## Runtime Choice

Use Python for the primary comparison:

```python
from paddleocr import PPStructureV3

pipeline = PPStructureV3(
    lang="en",
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False,
    device="cpu",
    engine="paddle",
)
```

Do not use Docker for the local Apple Silicon run. PaddleOCR publishes Docker paths for CPU and NVIDIA CUDA environments, but the Apple Silicon documentation says official Docker image setup is not currently supported for that hardware.

Do not expect Metal acceleration from `PPStructureV3(device="gpu")` or `PPStructureV3(device="mps")` on macOS. PaddleOCR's generic device parameters include CPU, CUDA-style GPU, NPU, XPU, MLU, DCU, MetaX GPU, and Iluvatar GPU, but not an Apple Metal/MPS device for PP-StructureV3.

If raw speed is a blocker after the CPU PP-StructureV3 quality check, add a separate candidate using PaddleOCR-VL with MLX-VLM:

```bash
.venv-paddleocr/bin/python -m pip install "paddleocr[doc-parser]" "mlx-vlm>=0.3.11"
mlx_vlm.server --port 8111
paddleocr doc_parser \
  --input raw/udl/textbook/images/page_0015.png \
  --vl_rec_backend mlx-vlm-server \
  --vl_rec_server_url http://localhost:8111/ \
  --vl_rec_api_model_name PaddlePaddle/PaddleOCR-VL-1.6
```

That is a different model family from PP-StructureV3, so compare it as a third candidate rather than silently swapping it into the PaddleOCR baseline.

## File Structure

Do not change raw source artifacts during the evaluation.

- Read only: `raw/udl/textbook/chapter_map.json`
- Read only: `raw/udl/textbook/images/page_0015.png` through `page_0054.png`
- Read only: `raw/udl/textbook/pages/ch01-introduction/page_0015.md` through `page_0030.md`
- Read only: `raw/udl/textbook/pages/ch02-supervised-learning/page_0031.md` through `page_0038.md`
- Read only: `raw/udl/textbook/pages/ch03-shallow-neural-networks/page_0039.md` through `page_0054.md`
- Create ignored output: `output/udl-ocr-comparison/paddleocr/pages/`
- Create ignored output: `output/udl-ocr-comparison/paddleocr/json/`
- Create ignored output: `output/udl-ocr-comparison/deepseek-pages/`
- Create ignored output: `output/udl-ocr-comparison/page-metrics.csv`
- Create ignored output: `output/udl-ocr-comparison/manual-review.md`
- Create ignored output: `output/udl-ocr-comparison/summary.md`
- Create durable note: `docs/udl-wiki/paddleocr-evaluation.md`
- Modify durable runbook: `docs/udl-wiki/ocr-runbook.md`

## Task 1: Confirm Baseline Inputs

**Files:**
- Read: `raw/udl/textbook/chapter_map.json`
- Read: `raw/udl/textbook/images/`
- Read: `raw/udl/textbook/pages/`
- Read: `raw/udl/textbook/raw_ocr/`

- [ ] **Step 1: Verify the existing DeepSeek status with the repo virtualenv**

Run:

```bash
.venv/bin/python -m torchbloom.udl_ocr_pipeline --status --chapters 1,2,3
```

Expected:

```text
40/40 pages done | complete=True | error_pages=[]
  ch01: 16/16
  ch02: 8/8
  ch03: 16/16
```

- [ ] **Step 2: Verify rendered image inputs exist**

Run:

```bash
find raw/udl/textbook/images -maxdepth 1 -type f -name 'page_*.png' | sort | sed -n '1p;$p'
find raw/udl/textbook/images -maxdepth 1 -type f -name 'page_*.png' | wc -l
```

Expected:

```text
raw/udl/textbook/images/page_0015.png
raw/udl/textbook/images/page_0054.png
      40
```

- [ ] **Step 3: Create the ignored comparison workspace**

Run:

```bash
mkdir -p output/udl-ocr-comparison/paddleocr/pages output/udl-ocr-comparison/paddleocr/json output/udl-ocr-comparison/deepseek-pages
```

Expected: command exits 0 and `git status --short output/udl-ocr-comparison` prints nothing because `output/` is ignored.

## Task 2: Prepare PaddleOCR Runtime

**Files:**
- Create local-only env: `.venv-paddleocr/`
- Create ignored output: `output/udl-ocr-comparison/paddleocr-smoke.md`

- [ ] **Step 1: Create a separate PaddleOCR environment**

Run:

```bash
/opt/homebrew/bin/python3.12 -m venv .venv-paddleocr
.venv-paddleocr/bin/python -m pip install --upgrade pip
```

Expected: `.venv-paddleocr/bin/python --version` prints Python 3.12.x.

- [ ] **Step 2: Install PaddlePaddle and PaddleOCR**

Run CPU install first:

```bash
.venv-paddleocr/bin/python -m pip install paddlepaddle==3.2.0 -i https://www.paddlepaddle.org.cn/packages/stable/cpu/
.venv-paddleocr/bin/python -m pip install "paddleocr[all]"
```

Expected: both commands exit 0. If local hardware has an approved GPU runtime, record the GPU install command used in `output/udl-ocr-comparison/paddleocr-smoke.md`.

- [ ] **Step 3: Verify PaddleOCR imports**

Run:

```bash
.venv-paddleocr/bin/python - <<'PY'
from paddleocr import PPStructureV3
print(PPStructureV3.__name__)
PY
```

Expected:

```text
PPStructureV3
```

- [ ] **Step 4: Smoke test one page**

Run:

```bash
.venv-paddleocr/bin/python - <<'PY'
from pathlib import Path
from paddleocr import PPStructureV3

out = Path("output/udl-ocr-comparison/paddleocr")
out.mkdir(parents=True, exist_ok=True)
pipeline = PPStructureV3(
    lang="en",
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False,
    device="cpu",
    engine="paddle",
)
result = pipeline.predict("raw/udl/textbook/images/page_0015.png")
markdown_pages = []
for res in result:
    res.save_to_json(save_path=str(out / "json"))
    res.save_to_markdown(save_path=str(out / "pages"))
    markdown_pages.append(res.markdown)
combined = pipeline.concatenate_markdown_pages(markdown_pages)
(out / "pages" / "page_0015.combined.md").write_text(combined, encoding="utf-8")
print((out / "pages" / "page_0015.combined.md").as_posix())
PY
```

Expected: command prints `output/udl-ocr-comparison/paddleocr/pages/page_0015.combined.md`, and that file contains readable Markdown.

- [ ] **Step 5: Record runtime details**

Create `output/udl-ocr-comparison/paddleocr-smoke.md` with:

```markdown
# PaddleOCR Smoke Test

Date: 2026-06-08

Input page: `raw/udl/textbook/images/page_0015.png`

Runtime:

- Python:
- PaddlePaddle:
- PaddleOCR:
- Device:
- Engine:
- Model/pipeline: `PPStructureV3`
- English settings: `lang="en"`, orientation/unwarping/textline orientation disabled

Smoke result:

- Markdown generated:
- JSON generated:
- Runtime notes:
- Errors or warnings:
```

Fill each blank with the observed values before moving on.

## Task 3: Run PaddleOCR On Ch1-3

**Files:**
- Read: `raw/udl/textbook/images/page_0015.png` through `page_0054.png`
- Create ignored output: `output/udl-ocr-comparison/paddleocr/pages/page_0015.md` through `page_0054.md`
- Create ignored output: `output/udl-ocr-comparison/paddleocr/json/`

- [ ] **Step 1: Run PP-StructureV3 on all 40 page PNGs**

Run:

```bash
.venv-paddleocr/bin/python - <<'PY'
from pathlib import Path
from paddleocr import PPStructureV3

image_dir = Path("raw/udl/textbook/images")
out_dir = Path("output/udl-ocr-comparison/paddleocr")
pages_dir = out_dir / "pages"
json_dir = out_dir / "json"
pages_dir.mkdir(parents=True, exist_ok=True)
json_dir.mkdir(parents=True, exist_ok=True)

pipeline = PPStructureV3(
    lang="en",
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False,
    device="cpu",
    engine="paddle",
)

for page in range(15, 55):
    image_path = image_dir / f"page_{page:04d}.png"
    markdown_pages = []
    result = pipeline.predict(str(image_path))
    for idx, res in enumerate(result, start=1):
        res.save_to_json(save_path=str(json_dir))
        markdown_pages.append(res.markdown)
    combined = pipeline.concatenate_markdown_pages(markdown_pages)
    dest = pages_dir / f"page_{page:04d}.md"
    dest.write_text(combined.strip() + "\n", encoding="utf-8")
    print(f"page {page}: {dest}")
PY
```

Expected: command prints one `page NN: ...` line for every page from 15 through 54.

- [ ] **Step 2: Confirm PaddleOCR output count**

Run:

```bash
find output/udl-ocr-comparison/paddleocr/pages -maxdepth 1 -type f -name 'page_*.md' | wc -l
```

Expected:

```text
      40
```

## Task 4: Normalize DeepSeek Baseline For Comparison

**Files:**
- Read: `raw/udl/textbook/pages/`
- Create ignored output: `output/udl-ocr-comparison/deepseek-pages/page_0015.md` through `page_0054.md`

- [ ] **Step 1: Copy DeepSeek page Markdown into a flat comparison directory**

Run:

```bash
for page in $(seq -f "%04g" 15 54); do
  src=$(find raw/udl/textbook/pages -type f -name "page_${page}.md" | head -n 1)
  cp "$src" "output/udl-ocr-comparison/deepseek-pages/page_${page}.md"
done
```

Expected: command exits 0.

- [ ] **Step 2: Confirm DeepSeek comparison output count**

Run:

```bash
find output/udl-ocr-comparison/deepseek-pages -maxdepth 1 -type f -name 'page_*.md' | wc -l
```

Expected:

```text
      40
```

## Task 5: Generate Mechanical Metrics

**Files:**
- Read: `output/udl-ocr-comparison/deepseek-pages/`
- Read: `output/udl-ocr-comparison/paddleocr/pages/`
- Create ignored output: `output/udl-ocr-comparison/page-metrics.csv`

- [ ] **Step 1: Generate per-page metrics**

Run:

```bash
.venv/bin/python - <<'PY'
import csv
import re
from pathlib import Path

root = Path("output/udl-ocr-comparison")
rows = []

def stats(text: str) -> dict[str, int]:
    body = re.sub(r"(?s)^---.*?---\s*", "", text)
    return {
        "chars": len(body),
        "words": len(re.findall(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)?", body)),
        "headings": len(re.findall(r"(?m)^#{1,6}\s+", body)),
        "images": len(re.findall(r"!\[[^\]]*\]\([^)]+\)", body)),
        "tables": len(re.findall(r"(?m)^\s*\|.*\|\s*$", body)),
        "math_markers": body.count("$") + body.count("\\(") + body.count("\\["),
    }

for page in range(15, 55):
    deepseek = (root / "deepseek-pages" / f"page_{page:04d}.md").read_text(encoding="utf-8")
    paddle = (root / "paddleocr" / "pages" / f"page_{page:04d}.md").read_text(encoding="utf-8")
    ds = stats(deepseek)
    po = stats(paddle)
    rows.append({
        "page": page,
        "deepseek_chars": ds["chars"],
        "paddleocr_chars": po["chars"],
        "char_delta": po["chars"] - ds["chars"],
        "deepseek_words": ds["words"],
        "paddleocr_words": po["words"],
        "word_delta": po["words"] - ds["words"],
        "deepseek_headings": ds["headings"],
        "paddleocr_headings": po["headings"],
        "deepseek_images": ds["images"],
        "paddleocr_images": po["images"],
        "deepseek_tables": ds["tables"],
        "paddleocr_tables": po["tables"],
        "deepseek_math_markers": ds["math_markers"],
        "paddleocr_math_markers": po["math_markers"],
    })

dest = root / "page-metrics.csv"
with dest.open("w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)
print(dest)
PY
```

Expected: command prints `output/udl-ocr-comparison/page-metrics.csv`.

- [ ] **Step 2: Inspect outlier pages**

Run:

```bash
.venv/bin/python - <<'PY'
import csv
from pathlib import Path

path = Path("output/udl-ocr-comparison/page-metrics.csv")
rows = list(csv.DictReader(path.open(encoding="utf-8")))
for row in rows:
    ds = int(row["deepseek_words"])
    po = int(row["paddleocr_words"])
    if ds and abs(po - ds) / ds >= 0.35:
        print(f"page {row['page']}: DeepSeek words={ds}, PaddleOCR words={po}, delta={po-ds}")
PY
```

Expected: prints only pages that need manual review because PaddleOCR is much shorter or longer than the baseline.

## Task 6: Manual Quality Review

**Files:**
- Read: `raw/udl/textbook/images/`
- Read: `output/udl-ocr-comparison/deepseek-pages/`
- Read: `output/udl-ocr-comparison/paddleocr/pages/`
- Create ignored output: `output/udl-ocr-comparison/manual-review.md`

- [ ] **Step 1: Review representative pages**

Review these pages side by side against the page PNG:

```text
15 - chapter opening/front matter style
17 - prose plus figure
22 - dense concept page with multiple figures
31 - supervised learning chapter start
34 - equations/least-squares content
39 - shallow neural networks chapter start
40 - network diagram/equation-heavy page
48 - multi-panel figure page
54 - chapter-end page
```

- [ ] **Step 2: Score each reviewed page**

Create `output/udl-ocr-comparison/manual-review.md` with this table:

```markdown
# Manual OCR Review: DeepSeek-OCR-2 vs PaddleOCR

Score scale: 0 = unusable, 1 = needs heavy cleanup, 2 = usable with light cleanup, 3 = wiki-ready.

| Page | Winner | DeepSeek text | PaddleOCR text | DeepSeek math | PaddleOCR math | DeepSeek figures | PaddleOCR figures | Reading order notes | Hallucination/omission notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 15 |  |  |  |  |  |  |  |  |  |
| 17 |  |  |  |  |  |  |  |  |  |
| 22 |  |  |  |  |  |  |  |  |  |
| 31 |  |  |  |  |  |  |  |  |  |
| 34 |  |  |  |  |  |  |  |  |  |
| 39 |  |  |  |  |  |  |  |  |  |
| 40 |  |  |  |  |  |  |  |  |  |
| 48 |  |  |  |  |  |  |  |  |  |
| 54 |  |  |  |  |  |  |  |  |  |
```

Fill every score cell before writing the summary.

## Task 7: Write Decision Summary

**Files:**
- Read: `output/udl-ocr-comparison/page-metrics.csv`
- Read: `output/udl-ocr-comparison/manual-review.md`
- Create ignored output: `output/udl-ocr-comparison/summary.md`
- Create durable note: `docs/udl-wiki/paddleocr-evaluation.md`
- Modify durable runbook: `docs/udl-wiki/ocr-runbook.md`

- [ ] **Step 1: Write ignored working summary**

Create `output/udl-ocr-comparison/summary.md` with:

```markdown
# PaddleOCR Evaluation Summary

Date:

Scope:

- UDL textbook pages 15-54.
- Chapters 1, 2, and 3.
- Baseline: existing DeepSeek-OCR-2 output in `raw/udl/textbook/`.
- Candidate: PaddleOCR PP-StructureV3 with English settings.

Mechanical metrics:

- Total pages compared:
- Pages where PaddleOCR word count differs by >=35%:
- Pages where PaddleOCR produced more Markdown image references:
- Pages where PaddleOCR produced more math markers:
- Runtime per page:

Manual review:

- Pages reviewed:
- DeepSeek wins:
- PaddleOCR wins:
- Tie / mixed:

Recommendation:

- Decision:
- Why:
- Follow-up work:
```

Fill each blank with observed values.

- [ ] **Step 2: Promote the curated summary into durable docs**

Create `docs/udl-wiki/paddleocr-evaluation.md` with:

```markdown
# PaddleOCR Evaluation For UDL Ch1-3

**Date:** 2026-06-08

**Purpose:** Decide whether PaddleOCR should replace or supplement DeepSeek-OCR-2 for UDL textbook conversion.

**Source dependency:** Private UDL source intake in `raw/udl/source/`, existing rendered page images in `raw/udl/textbook/images/`, and existing DeepSeek-OCR-2 baseline in `raw/udl/textbook/`.

**Generated evidence:** Local comparison artifacts under `output/udl-ocr-comparison/`; these are ignored by git and should not be committed.

## Scope

- Ch1 Introduction: PDF pages 15-30.
- Ch2 Supervised learning: PDF pages 31-38.
- Ch3 Shallow neural networks: PDF pages 39-54.

## PaddleOCR Configuration

- Pipeline:
- Device:
- Engine:
- English recognition setting:
- Formula/table/chart settings:
- Install notes:

## Results

- Pages compared:
- Mechanical outliers:
- Manual pages reviewed:
- DeepSeek wins:
- PaddleOCR wins:
- Mixed/tie pages:

## Recommendation

Write one of:

- Keep DeepSeek-OCR-2 as the primary converter.
- Switch Ch1-3 and future chapters to PaddleOCR.
- Use a hybrid workflow: DeepSeek for prose/figures and PaddleOCR for selected layout/math checks.

## Open Questions

- Runtime/cost tradeoff:
- Math fidelity:
- Figure and table extraction:
- Required cleanup before scaling:
```

Replace every bullet value with observed evidence before committing.

- [ ] **Step 3: Update the OCR runbook**

Append this section to `docs/udl-wiki/ocr-runbook.md`:

```markdown
## PaddleOCR Evaluation

Use `docs/udl-wiki/paddleocr-evaluation.md` for the Ch1-3 comparison between the existing DeepSeek-OCR-2 baseline and PaddleOCR PP-StructureV3.

Generated evidence belongs under `output/udl-ocr-comparison/` and should not be committed. Promote only the curated recommendation and reproducible configuration details into docs.
```

- [ ] **Step 4: Verify docs**

Run:

```bash
git diff -- docs/udl-wiki/paddleocr-evaluation.md docs/udl-wiki/ocr-runbook.md
git status --short
```

Expected: only the durable docs are tracked changes; `output/udl-ocr-comparison/` remains ignored.

- [ ] **Step 5: Commit the evaluation task result**

Run:

```bash
git add docs/udl-wiki/paddleocr-evaluation.md docs/udl-wiki/ocr-runbook.md
git commit -m "docs: record PaddleOCR UDL evaluation"
```

Expected: commit succeeds with only curated documentation changes.

## Acceptance Criteria

- PaddleOCR has been run on all 40 page PNGs for UDL chapters 1-3.
- The comparison uses the existing DeepSeek-OCR-2 output as a read-only baseline.
- Generated PaddleOCR Markdown/JSON and metric files stay under ignored `output/udl-ocr-comparison/`.
- Manual review covers prose, equations, figures, reading order, omissions, and hallucinations.
- `docs/udl-wiki/paddleocr-evaluation.md` states a clear recommendation with evidence.
- `docs/udl-wiki/ocr-runbook.md` points future OCR work to the evaluation note.
