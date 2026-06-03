# UDL Companion Wiki MVP Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the private Ch1-3 UDL companion wiki source pipeline and first learning artifacts for understanding *Understanding Deep Learning* from high-school math foundations.

**Architecture:** Raw UDL PDFs live under `raw/udl/source/`; DeepSeek-OCR-2 produces immutable per-page raw artifacts under `raw/udl/textbook/`; answer booklet extraction lands under `raw/udl/answers/`; original TorchBloom companion pages live under `wiki/udl/`. Small Python utilities provide source verification, chapter mapping, OCR orchestration, and wiki validation.

**Tech Stack:** Python 3.12 for OCR, PyMuPDF, Pillow, PyYAML, pytest, mlx-vlm with DeepSeek-OCR-2 on Apple Silicon, Markdown/YAML wiki files, git for commit boundaries.

---

## File Structure

Create or modify these areas:

- Modify `.gitignore` to allow only the two UDL source PDFs while keeping other raw PDFs ignored.
- Create `raw/udl/` for source intake, manifests, downloaded PDFs, OCR output, parsed pages, figures, logs, and answer extraction.
- Create `docs/udl-wiki/` for source policy, OCR runbook, and authoring guide.
- Create `wiki/udl/` for chapter packs, shared concepts, math bridges, equation pages, practice cards, notebook guides, methodology, schema, and audit queue.
- Create `pyproject.toml`, `src/torchbloom/`, and `tests/` for source verification, chapter mapping, OCR orchestration, and wiki validation.

## Task 1: UDL Source Intake Policy

**Files:**
- Modify: `.gitignore`
- Create: `raw/udl/README.md`
- Create: `raw/udl/manifests/udlbook-v5.0.3.md`
- Create: `raw/udl/source/SHA256SUMS`
- Create: `docs/udl-wiki/source-policy.md`

- [ ] **Step 1: Update `.gitignore` for private UDL source PDFs**

Add this block immediately after the existing raw PDF ignore rules:

```gitignore
# Private/noncommercial UDL MVP source PDFs
!raw/udl/source/
!raw/udl/source/UnderstandingDeepLearning_02_09_26_C.pdf
!raw/udl/source/UDL_Answer_Booklet_Students.pdf
!raw/udl/source/SHA256SUMS
```

- [ ] **Step 2: Create the raw UDL directory skeleton**

Run:

```bash
mkdir -p raw/udl/manifests raw/udl/source raw/udl/textbook/raw_ocr raw/udl/textbook/pages raw/udl/textbook/figures raw/udl/textbook/images raw/udl/answers/pages docs/udl-wiki
```

Expected: command exits 0 and creates the listed directories.

- [ ] **Step 3: Write `raw/udl/README.md`**

Use this content:

```markdown
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
```

- [ ] **Step 4: Download the latest textbook and answer booklet**

Run:

```bash
curl -L -o raw/udl/source/UnderstandingDeepLearning_02_09_26_C.pdf https://github.com/udlbook/udlbook/releases/download/v5.0.3/UnderstandingDeepLearning_02_09_26_C.pdf
curl -L -o raw/udl/source/UDL_Answer_Booklet_Students.pdf https://raw.githubusercontent.com/udlbook/udlbook/main/UDL_Answer_Booklet_Students.pdf
```

Expected: first file is about 22 MB; second file is about 1.8 MB.

- [ ] **Step 5: Verify checksums and write `SHA256SUMS`**

Run:

```bash
shasum -a 256 raw/udl/source/UnderstandingDeepLearning_02_09_26_C.pdf raw/udl/source/UDL_Answer_Booklet_Students.pdf
```

Expected:

```text
f8237d393163900fa8e43210e680a3f987b45ccac7750b372e156fae3df0bf32  raw/udl/source/UnderstandingDeepLearning_02_09_26_C.pdf
ec58fde8a42da57979808b284e52a26e0b67142817d47a657772b09144d1dcf3  raw/udl/source/UDL_Answer_Booklet_Students.pdf
```

Write those two lines to `raw/udl/source/SHA256SUMS`.

- [ ] **Step 6: Write `raw/udl/manifests/udlbook-v5.0.3.md`**

Use this content:

```markdown
# UDL Source Manifest: v5.0.3

**Source id:** udlbook-v5.0.3

**Title:** Understanding Deep Learning

**Author:** Simon J. D. Prince

**Official website:** https://udlbook.github.io/udlbook/

**Textbook PDF:** https://github.com/udlbook/udlbook/releases/download/v5.0.3/UnderstandingDeepLearning_02_09_26_C.pdf

**Textbook release:** v5.0.3, Understanding Deep Learning Chapters 1-21, 5th printing, released 2026-02-09.

**Textbook SHA-256:** f8237d393163900fa8e43210e680a3f987b45ccac7750b372e156fae3df0bf32

**Student answer booklet:** https://raw.githubusercontent.com/udlbook/udlbook/main/UDL_Answer_Booklet_Students.pdf

**Student answer booklet Git blob SHA:** e175e817fad73ceb1458571629c8fd6fbbc89e53

**Student answer booklet SHA-256:** ec58fde8a42da57979808b284e52a26e0b67142817d47a657772b09144d1dcf3

**License:** Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International.

**TorchBloom use:** Private, noncommercial source intake for OCR, source anchoring, practice indexing, selected-answer checks, and original companion-wiki synthesis.

**Committed source artifacts:** The two PDFs listed above and `SHA256SUMS`.

**Restricted policy:** Do not publish OCR text, adapted answer notes, or UDL-derived wiki pages without separate license review.

**Review notes:** The UDL GitHub repository contains notebooks, figures, slides, equations, and site source, but it does not appear to contain the full book TeX source. The textbook PDF is the source of truth for prose and exercises in this MVP.
```

- [ ] **Step 7: Write `docs/udl-wiki/source-policy.md`**

Use this content:

```markdown
# UDL Source Policy

TorchBloom's UDL companion wiki is private and noncommercial in this MVP.

## Allowed In This Private MVP

- Store the official UDL textbook PDF in `raw/udl/source/`.
- Store the official student answer booklet in `raw/udl/source/`.
- OCR pilot chapters 1, 2, and 3 into private raw artifacts.
- Write original TorchBloom study pages that cite raw source anchors.
- Use selected answers to check practice-card correctness.

## Restricted

- Do not publish OCR text or adapted source-derived pages.
- Do not copy full UDL solutions into public-style wiki pages.
- Do not vendor the complete UDL GitHub repository in this stage.
- Do not add unrelated advanced repositories to the UDL MVP.

## Future Public Or Commercial Review

Before any public or commercial use, remove or rewrite adapted UDL-derived materials and keep only original TorchBloom explanations, source citations, and links unless explicit permission allows more.
```

- [ ] **Step 8: Verify source intake state**

Run:

```bash
git check-ignore -v raw/udl/source/UnderstandingDeepLearning_02_09_26_C.pdf raw/udl/source/UDL_Answer_Booklet_Students.pdf
git status --short
```

Expected: `git check-ignore` prints no matching ignore rule for the two PDFs. `git status --short` shows `.gitignore`, `docs/udl-wiki/source-policy.md`, `raw/udl/README.md`, `raw/udl/manifests/udlbook-v5.0.3.md`, `raw/udl/source/SHA256SUMS`, and the two PDFs as untracked or modified.

- [ ] **Step 9: Commit source intake**

Run:

```bash
git add .gitignore docs/udl-wiki/source-policy.md raw/udl/README.md raw/udl/manifests/udlbook-v5.0.3.md raw/udl/source/SHA256SUMS raw/udl/source/UnderstandingDeepLearning_02_09_26_C.pdf raw/udl/source/UDL_Answer_Booklet_Students.pdf
git commit -m "chore: add UDL source intake"
```

Expected: commit succeeds with the source-policy files and two PDFs.

## Task 2: Python Project And Source Verification

**Files:**
- Create: `pyproject.toml`
- Create: `src/torchbloom/__init__.py`
- Create: `src/torchbloom/udl_sources.py`
- Create: `tests/test_udl_sources.py`

- [ ] **Step 1: Write the failing source-verification tests**

Create `tests/test_udl_sources.py`:

```python
from pathlib import Path

from torchbloom.udl_sources import (
    ANSWER_BOOKLET,
    TEXTBOOK,
    verify_sha256,
)


def test_udl_source_metadata_is_pinned():
    assert TEXTBOOK.filename == "UnderstandingDeepLearning_02_09_26_C.pdf"
    assert TEXTBOOK.sha256 == "f8237d393163900fa8e43210e680a3f987b45ccac7750b372e156fae3df0bf32"
    assert ANSWER_BOOKLET.filename == "UDL_Answer_Booklet_Students.pdf"
    assert ANSWER_BOOKLET.sha256 == "ec58fde8a42da57979808b284e52a26e0b67142817d47a657772b09144d1dcf3"


def test_verify_sha256_rejects_mismatch(tmp_path: Path):
    sample = tmp_path / "sample.txt"
    sample.write_text("TorchBloom", encoding="utf-8")

    assert verify_sha256(sample, "7daa00e2b5305f2e8a8052e40944b1a885c6baec87e08dcad1d85cca86b67711")
    assert not verify_sha256(sample, "0" * 64)
```

- [ ] **Step 2: Run tests to verify they fail**

Run:

```bash
pytest tests/test_udl_sources.py -q
```

Expected: FAIL with `ModuleNotFoundError: No module named 'torchbloom'`.

- [ ] **Step 3: Create `pyproject.toml`**

Use this content:

```toml
[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[project]
name = "torchbloom"
version = "0.1.0"
description = "TorchBloom project utilities"
requires-python = ">=3.12"
dependencies = [
  "Pillow>=10,<12",
  "pymupdf>=1.26,<2",
  "PyYAML>=6,<7",
]

[project.optional-dependencies]
dev = [
  "pytest>=8,<9",
]
ocr = [
  "mlx-vlm==0.5.0",
]

[project.scripts]
torchbloom-udl-ocr = "torchbloom.udl_ocr_pipeline:main"
torchbloom-udl-answers = "torchbloom.udl_answer_extract:main"
torchbloom-validate-wiki = "torchbloom.wiki_validation:main"

[tool.pytest.ini_options]
pythonpath = ["src"]
testpaths = ["tests"]
```

- [ ] **Step 4: Create `src/torchbloom/__init__.py`**

Use this content:

```python
"""TorchBloom project utilities."""
```

- [ ] **Step 5: Create `src/torchbloom/udl_sources.py`**

Use this content:

```python
from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path


@dataclass(frozen=True)
class UdlSource:
    source_id: str
    filename: str
    url: str
    sha256: str

    @property
    def local_path(self) -> Path:
        return Path("raw/udl/source") / self.filename


TEXTBOOK = UdlSource(
    source_id="udlbook-v5.0.3-textbook",
    filename="UnderstandingDeepLearning_02_09_26_C.pdf",
    url="https://github.com/udlbook/udlbook/releases/download/v5.0.3/UnderstandingDeepLearning_02_09_26_C.pdf",
    sha256="f8237d393163900fa8e43210e680a3f987b45ccac7750b372e156fae3df0bf32",
)

ANSWER_BOOKLET = UdlSource(
    source_id="udlbook-answer-booklet-students",
    filename="UDL_Answer_Booklet_Students.pdf",
    url="https://raw.githubusercontent.com/udlbook/udlbook/main/UDL_Answer_Booklet_Students.pdf",
    sha256="ec58fde8a42da57979808b284e52a26e0b67142817d47a657772b09144d1dcf3",
)


def file_sha256(path: Path) -> str:
    digest = sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def verify_sha256(path: Path, expected: str) -> bool:
    return file_sha256(path) == expected
```

- [ ] **Step 6: Run source tests**

Run:

```bash
pytest tests/test_udl_sources.py -q
```

Expected: `2 passed`.

- [ ] **Step 7: Commit source verifier**

Run:

```bash
git add pyproject.toml src/torchbloom/__init__.py src/torchbloom/udl_sources.py tests/test_udl_sources.py
git commit -m "chore: add UDL source verifier"
```

Expected: commit succeeds.

## Task 3: UDL Chapter Map

**Files:**
- Create: `src/torchbloom/udl_chapter_map.py`
- Create: `tests/test_udl_chapter_map.py`
- Create: `raw/udl/chapter_map.json`

- [ ] **Step 1: Write failing tests for chapter-map logic**

Create `tests/test_udl_chapter_map.py`:

```python
from torchbloom.udl_chapter_map import build_chapter_map, slugify_title


def test_slugify_title_is_stable():
    assert slugify_title("Shallow Neural Networks") == "shallow-neural-networks"
    assert slugify_title("Background Mathematics") == "background-mathematics"


def test_build_chapter_map_from_outline_entries():
    outline = [
        (1, "Preface", 1),
        (1, "1 Background Mathematics", 9),
        (1, "2 Supervised Learning", 31),
        (1, "3 Shallow Neural Networks", 47),
        (1, "References", 100),
    ]

    chapters = build_chapter_map(outline, page_count=120)

    assert [chapter.number for chapter in chapters] == [1, 2, 3]
    assert chapters[0].slug == "ch01-background-mathematics"
    assert chapters[0].pdf_start == 9
    assert chapters[0].pdf_end == 30
    assert chapters[1].slug == "ch02-supervised-learning"
    assert chapters[1].pdf_start == 31
    assert chapters[1].pdf_end == 46
    assert chapters[2].slug == "ch03-shallow-neural-networks"
    assert chapters[2].pdf_start == 47
    assert chapters[2].pdf_end == 99
```

- [ ] **Step 2: Run tests to verify they fail**

Run:

```bash
pytest tests/test_udl_chapter_map.py -q
```

Expected: FAIL with `ModuleNotFoundError: No module named 'torchbloom.udl_chapter_map'`.

- [ ] **Step 3: Implement chapter-map logic**

Create `src/torchbloom/udl_chapter_map.py`:

```python
from __future__ import annotations

from dataclasses import asdict, dataclass
import json
import re
from pathlib import Path

import fitz


CHAPTER_RE = re.compile(r"^(\d{1,2})\s+(.+)$")


@dataclass(frozen=True)
class ChapterRange:
    number: int
    title: str
    slug: str
    pdf_start: int
    pdf_end: int


def slugify_title(title: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return re.sub(r"-+", "-", slug)


def build_chapter_map(outline: list[tuple[int, str, int]], page_count: int) -> list[ChapterRange]:
    starts: list[tuple[int, str, int]] = []
    first_post_chapter_page = page_count + 1

    for level, title, page in outline:
        if level != 1:
            continue
        match = CHAPTER_RE.match(title.strip())
        if match:
            number = int(match.group(1))
            starts.append((number, match.group(2).strip(), page))
        elif starts and first_post_chapter_page == page_count + 1:
            first_post_chapter_page = page

    chapters: list[ChapterRange] = []
    for index, (number, title, pdf_start) in enumerate(starts):
        if index + 1 < len(starts):
            pdf_end = starts[index + 1][2] - 1
        else:
            pdf_end = first_post_chapter_page - 1
        chapters.append(
            ChapterRange(
                number=number,
                title=title,
                slug=f"ch{number:02d}-{slugify_title(title)}",
                pdf_start=pdf_start,
                pdf_end=pdf_end,
            )
        )
    return chapters


def load_chapter_map(pdf_path: Path) -> list[ChapterRange]:
    with fitz.open(pdf_path) as doc:
        return build_chapter_map(doc.get_toc(), page_count=doc.page_count)


def write_chapter_map(pdf_path: Path, output_path: Path) -> list[ChapterRange]:
    chapters = load_chapter_map(pdf_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps([asdict(chapter) for chapter in chapters], indent=2) + "\n",
        encoding="utf-8",
    )
    return chapters
```

- [ ] **Step 4: Run chapter-map tests**

Run:

```bash
pytest tests/test_udl_chapter_map.py -q
```

Expected: `2 passed`.

- [ ] **Step 5: Generate the real UDL chapter map**

Run:

```bash
PYTHONPATH=src python -c 'from pathlib import Path; from torchbloom.udl_chapter_map import write_chapter_map; chapters = write_chapter_map(Path("raw/udl/source/UnderstandingDeepLearning_02_09_26_C.pdf"), Path("raw/udl/chapter_map.json")); print(len(chapters)); print(chapters[0]); print(chapters[1]); print(chapters[2])'
```

Expected: command exits 0, prints a chapter count, and prints chapter ranges for chapters 1, 2, and 3.

- [ ] **Step 6: Commit chapter map**

Run:

```bash
git add src/torchbloom/udl_chapter_map.py tests/test_udl_chapter_map.py raw/udl/chapter_map.json
git commit -m "feat: add UDL chapter map"
```

Expected: commit succeeds.

## Task 4: UDL OCR Pipeline

**Files:**
- Create: `src/torchbloom/udl_ocr_parse.py`
- Create: `src/torchbloom/udl_ocr_pipeline.py`
- Create: `tests/test_udl_ocr_parse.py`
- Create: `tests/test_udl_ocr_pipeline.py`
- Create: `docs/udl-wiki/ocr-runbook.md`

- [ ] **Step 1: Port the tested BioBloom parser as a starting point**

Use BioBloom as the source reference:

```text
/Users/fang/projects/biobloom/src/biobloom/campbell_ocr_parse.py
/Users/fang/projects/biobloom/src/biobloom/campbell_ocr_pipeline.py
/Users/fang/projects/biobloom/tests/test_campbell_ocr_parse.py
/Users/fang/projects/biobloom/tests/test_campbell_ocr_pipeline.py
```

Port names from `campbell` to `udl`, replace `raw/campbell-12e` defaults with `raw/udl/textbook`, replace the source PDF default with `raw/udl/source/UnderstandingDeepLearning_02_09_26_C.pdf`, and use `raw/udl/chapter_map.json` for chapter ranges.

- [ ] **Step 2: Preserve these required OCR behaviors**

Confirm the port keeps:

```text
raw_ocr/page_NNNN.txt is written before parsing
pages/<chapter-slug>/page_NNNN.md is regenerated from raw OCR during --reparse
figures/page_NNNN_fig_K.png names are globally unique
--chapters 1,2,3 selects chapter ranges from raw/udl/chapter_map.json
--pages N-M selects explicit PDF page numbers
--all selects the full book
--status reports done, total, complete, and error_pages
--force reruns OCR for existing raw pages
--keep-page-images preserves rendered page PNGs for pilot inspection
```

- [ ] **Step 3: Write `docs/udl-wiki/ocr-runbook.md`**

Use this content:

````markdown
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
````

- [ ] **Step 4: Run OCR parser and pipeline tests**

Run:

```bash
pytest tests/test_udl_ocr_parse.py tests/test_udl_ocr_pipeline.py -q
```

Expected: all parser and pipeline unit tests pass without loading the model.

- [ ] **Step 5: Commit OCR pipeline**

Run:

```bash
git add src/torchbloom/udl_ocr_parse.py src/torchbloom/udl_ocr_pipeline.py tests/test_udl_ocr_parse.py tests/test_udl_ocr_pipeline.py docs/udl-wiki/ocr-runbook.md pyproject.toml
git commit -m "feat: add UDL OCR pipeline"
```

Expected: commit succeeds.

## Task 5: Run Ch1-3 OCR Pilot

**Files:**
- Create or update: `raw/udl/textbook/raw_ocr/`
- Create or update: `raw/udl/textbook/pages/`
- Create or update: `raw/udl/textbook/figures/`
- Create or update: `raw/udl/textbook/images/`
- Create or update: `raw/udl/textbook/index.md`
- Create or update: `raw/udl/textbook/log.md`

- [ ] **Step 1: Start the Ch1-3 OCR pilot**

Run:

```bash
.venv-ocr/bin/torchbloom-udl-ocr --chapters 1,2,3 --keep-page-images
```

Expected: command exits 0 or writes resumable progress before interruption. If interrupted, rerun the same command; completed pages are skipped.

- [ ] **Step 2: Check OCR status**

Run:

```bash
.venv-ocr/bin/torchbloom-udl-ocr --status --chapters 1,2,3
```

Expected: output reports `complete=True` and `error_pages=[]` for chapters 1, 2, and 3.

- [ ] **Step 3: Inspect representative pages**

Open at least one parsed page from each chapter and check:

```text
frontmatter has source, pdf_page, chapter, chapter_slug, title, figure_count, figures, headings
body text follows the visual reading order
equations are readable enough to anchor an equation page
figures have useful crops
captions stay near the correct figures
```

- [ ] **Step 4: Reparse Ch1-3**

Run:

```bash
.venv-ocr/bin/torchbloom-udl-ocr --chapters 1,2,3 --reparse
.venv-ocr/bin/torchbloom-udl-ocr --status --chapters 1,2,3
```

Expected: reparse exits 0 without model inference and status remains complete.

- [ ] **Step 5: Commit Ch1-3 raw OCR pilot**

Run:

```bash
git add raw/udl/textbook
git commit -m "data: add UDL chapters 1-3 OCR pilot"
```

Expected: commit succeeds with raw OCR text, parsed Markdown, figures, page images, index, and log.

## Task 6: Extract Ch1-3 Selected Answers

**Files:**
- Create: `src/torchbloom/udl_answer_extract.py`
- Create: `tests/test_udl_answer_extract.py`
- Create or update: `raw/udl/answers/pages/`
- Create or update: `raw/udl/answers/index.md`

- [ ] **Step 1: Write a failing answer-extraction test**

Create `tests/test_udl_answer_extract.py`:

```python
from torchbloom.udl_answer_extract import chapter_answer_heading


def test_chapter_answer_heading():
    assert chapter_answer_heading(1) == "Chapter 1"
    assert chapter_answer_heading(3) == "Chapter 3"
```

- [ ] **Step 2: Run the failing test**

Run:

```bash
pytest tests/test_udl_answer_extract.py -q
```

Expected: FAIL with `ModuleNotFoundError: No module named 'torchbloom.udl_answer_extract'`.

- [ ] **Step 3: Implement the first extraction helper**

Create `src/torchbloom/udl_answer_extract.py`:

```python
from __future__ import annotations

from pathlib import Path

import fitz


def chapter_answer_heading(chapter: int) -> str:
    return f"Chapter {chapter}"


def extract_answer_pages(pdf_path: Path, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    index_lines = ["# UDL Student Answer Booklet Extract\n"]
    with fitz.open(pdf_path) as doc:
        for page_index, page in enumerate(doc, start=1):
            text = page.get_text("text")
            page_path = output_dir / f"page_{page_index:04d}.md"
            page_path.write_text(
                f"---\nsource: udl-answer-booklet\npdf_page: {page_index}\n---\n\n{text.strip()}\n",
                encoding="utf-8",
            )
            index_lines.append(f"- [page_{page_index:04d}.md](pages/page_{page_index:04d}.md)\n")
    (output_dir.parent / "index.md").write_text("".join(index_lines), encoding="utf-8")


def main() -> None:
    extract_answer_pages(
        Path("raw/udl/source/UDL_Answer_Booklet_Students.pdf"),
        Path("raw/udl/answers/pages"),
    )
```

- [ ] **Step 4: Run answer extraction tests**

Run:

```bash
pytest tests/test_udl_answer_extract.py -q
```

Expected: `1 passed`.

- [ ] **Step 5: Extract answer booklet pages**

Run:

```bash
PYTHONPATH=src python -m torchbloom.udl_answer_extract
```

Expected: `raw/udl/answers/pages/page_0001.md` and `raw/udl/answers/index.md` exist.

- [ ] **Step 6: Commit answer extraction**

Run:

```bash
git add src/torchbloom/udl_answer_extract.py tests/test_udl_answer_extract.py raw/udl/answers
git commit -m "feat: extract UDL answer booklet"
```

Expected: commit succeeds.

## Task 7: UDL Wiki Schema And Skeleton

**Files:**
- Create: `docs/udl-wiki/README.md`
- Create: `docs/udl-wiki/authoring-guide.md`
- Create: `wiki/udl/index.md`
- Create: `wiki/udl/methodology.md`
- Create: `wiki/udl/schema.md`
- Create: `wiki/udl/audit-queue.md`
- Create: `wiki/udl/chapters/ch01/index.md`
- Create: `wiki/udl/chapters/ch02/index.md`
- Create: `wiki/udl/chapters/ch03/index.md`

- [ ] **Step 1: Create wiki directories**

Run:

```bash
mkdir -p docs/udl-wiki wiki/udl/chapters/ch01 wiki/udl/chapters/ch02 wiki/udl/chapters/ch03 wiki/udl/concepts wiki/udl/math-bridges wiki/udl/equations wiki/udl/practices wiki/udl/notebook-guides
```

Expected: command exits 0 and creates the directories.

- [ ] **Step 2: Write `wiki/udl/schema.md`**

Use the page schema from `docs/superpowers/specs/2026-06-03-udl-companion-wiki-mvp-design.md` section 6. Required page types are `chapter-pack`, `concept`, `math-bridge`, `equation`, `practice-card`, and `notebook-guide`.

- [ ] **Step 3: Write chapter index pages**

Create each chapter `index.md` with frontmatter:

```yaml
---
id: ch01
type: chapter-pack
title: Chapter 1
source_anchors:
  - source: udlbook-v5.0.3
    locator: chapter 1
confidence: directional
---
```

Use `ch02` and `ch03` for the other two pages.

- [ ] **Step 4: Commit wiki skeleton**

Run:

```bash
git add docs/udl-wiki wiki/udl
git commit -m "feat: add UDL wiki skeleton"
```

Expected: commit succeeds.

## Task 8: Wiki Validation

**Files:**
- Create: `src/torchbloom/wiki_validation.py`
- Create: `tests/test_wiki_validation.py`

- [ ] **Step 1: Write failing validation tests**

Create `tests/test_wiki_validation.py`:

```python
from torchbloom.wiki_validation import required_frontmatter_keys


def test_required_frontmatter_keys_include_source_anchors():
    keys = required_frontmatter_keys()
    assert "id" in keys
    assert "type" in keys
    assert "source_anchors" in keys
    assert "confidence" in keys
```

- [ ] **Step 2: Implement minimal validation helper**

Create `src/torchbloom/wiki_validation.py`:

```python
from __future__ import annotations


def required_frontmatter_keys() -> set[str]:
    return {
        "id",
        "type",
        "title",
        "source_anchors",
        "confidence",
        "prerequisites",
        "related",
        "learning_objectives",
    }


def main() -> None:
    print("UDL wiki validation helper loaded")
```

- [ ] **Step 3: Run validation tests**

Run:

```bash
pytest tests/test_wiki_validation.py -q
```

Expected: `1 passed`.

- [ ] **Step 4: Commit validation helper**

Run:

```bash
git add src/torchbloom/wiki_validation.py tests/test_wiki_validation.py pyproject.toml
git commit -m "feat: add wiki validation helper"
```

Expected: commit succeeds.

## Task 9: Author Ch1-3 Pilot Learning Artifacts

**Files:**
- Modify: `wiki/udl/chapters/ch01/index.md`
- Modify: `wiki/udl/chapters/ch02/index.md`
- Modify: `wiki/udl/chapters/ch03/index.md`
- Create: `wiki/udl/chapters/ch01/reading-guide.md`
- Create: `wiki/udl/chapters/ch02/reading-guide.md`
- Create: `wiki/udl/chapters/ch03/reading-guide.md`
- Create: `wiki/udl/chapters/ch01/practice-index.md`
- Create: `wiki/udl/chapters/ch02/practice-index.md`
- Create: `wiki/udl/chapters/ch03/practice-index.md`
- Create: concept, math-bridge, equation, practice-card, and notebook-guide pages required by Ch1-3.

- [ ] **Step 1: Build the Ch1-3 concept inventory from OCR**

Read:

```text
raw/udl/textbook/pages/<ch01-slug>/
raw/udl/textbook/pages/<ch02-slug>/
raw/udl/textbook/pages/<ch03-slug>/
raw/udl/answers/index.md
```

Write each chapter's `reading-guide.md` with:

```markdown
# Reading Guide

## What This Chapter Teaches

## Before You Read

## Section Map

## Concepts To Master

## Equations To Understand

## Questions And Practice

## Notebook Work

## Source Anchors
```

- [ ] **Step 2: Write shared concept pages**

For every concept needed by Ch1-3, create one page under `wiki/udl/concepts/`. Use this frontmatter:

```yaml
---
id: supervised-learning
type: concept
title: Supervised Learning
chapter_scope: [ch02]
source_anchors:
  - source: udlbook-v5.0.3
    locator: ch02
confidence: directional
prerequisites: []
related: []
learning_objectives:
  - Explain supervised learning as fitting a function from inputs to targets.
---
```

Replace the id, title, chapter scope, prerequisites, related pages, and learning objectives for each concept.

- [ ] **Step 3: Write practice cards for each Ch1-3 book question**

For each end-of-chapter question discovered in the OCR pages, create a file under `wiki/udl/practices/` with this structure:

```markdown
---
id: ch02-q01
type: practice-card
title: Ch02 Q01
chapter_scope: [ch02]
source_anchors:
  - source: udlbook-v5.0.3
    locator: ch02 question 1
confidence: directional
prerequisites: []
related: []
learning_objectives:
  - Answer the source question using the linked concept pages.
answer_policy: review-needed
---

# Ch02 Q01

## Prompt

## What This Tests

## Hints

## Solution Notes

## Self-Check Rubric

## Source Anchors

## Related
```

If the answer booklet contains a selected answer, set `answer_policy: selected-answer`; otherwise use `answer_policy: torchbloom-derived` only after the answer is independently worked.

- [ ] **Step 4: Commit pilot learning artifacts**

Run:

```bash
git add wiki/udl
git commit -m "feat: add UDL chapters 1-3 pilot wiki"
```

Expected: commit succeeds.

## Task 10: Final Verification

**Files:**
- No new files.

- [ ] **Step 1: Run tests**

Run:

```bash
pytest -q
```

Expected: all tests pass.

- [ ] **Step 2: Run source checksum verification**

Run:

```bash
shasum -a 256 -c raw/udl/source/SHA256SUMS
```

Expected:

```text
raw/udl/source/UnderstandingDeepLearning_02_09_26_C.pdf: OK
raw/udl/source/UDL_Answer_Booklet_Students.pdf: OK
```

- [ ] **Step 3: Check git state**

Run:

```bash
git status --short --branch
git log --oneline --decorate -5
```

Expected: working tree is clean on `main`; latest commits show the UDL source, tooling, OCR, and wiki work.

## Self-Review

- Spec coverage: the tasks cover source intake, private source policy, DeepSeek OCR, answer extraction, Ch1-3 pilot scope, wiki schema, practice cards, and validation.
- Placeholder scan: the plan uses exact source URLs, hashes, paths, commands, and page templates. Content generated from OCR is intentionally discovered from source pages during execution.
- Type consistency: page types are consistent across the design and plan: `chapter-pack`, `concept`, `math-bridge`, `equation`, `practice-card`, and `notebook-guide`.
