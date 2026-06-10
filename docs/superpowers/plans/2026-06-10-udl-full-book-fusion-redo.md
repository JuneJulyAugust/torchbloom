# UDL Full Book Fusion Redo Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rebuild every *Understanding Deep Learning* fused Markdown page from source evidence with chapter-scoped subagents, replacing the weak validator-driven rollout.

**Architecture:** Workers produce fresh page-level synthesis in a new ignored staging area, `output/udl-fusion-redo/`, using DeepSeek text, Paddle layout/figure evidence, original page images, and the accepted chapters 1-3 style contract. The main session owns the contract, worker orchestration, review gates, validation, and final publish into `raw/udl/textbook` only after staged output passes.

**Tech Stack:** Codex subagents, Python 3.12 utilities in `src/torchbloom/udl_fusion_pilot.py`, Markdown with GitHub math, JSON block sidecars, Paddle layout evidence, DeepSeek OCR evidence.

---

## File Structure

- Create: `docs/superpowers/plans/2026-06-10-udl-full-book-fusion-redo.md`
- Create or regenerate ignored: `output/udl-fusion-redo/fused/chXX/page_XXXX.md`
- Create or regenerate ignored: `output/udl-fusion-redo/blocks/chXX/page_XXXX.blocks.json`
- Create or regenerate ignored: `output/udl-fusion-redo/reports/chXX.md`
- Create or regenerate ignored: `output/udl-fusion-redo/reports/review-queue.md`
- Copy or regenerate ignored: `output/udl-fusion-redo/figures/page_XXXX_fig_N.jpg`
- Preserve as read-only evidence: `output/udl-fusion-pilot/inputs/page_YYYY/manifest.json`
- Preserve as read-only evidence: `output/udl-fusion-pilot/inputs/page_YYYY/deepseek.md`
- Preserve as read-only evidence: `output/udl-fusion-pilot/inputs/page_YYYY/paddle.md`
- Preserve as read-only evidence: `output/udl-fusion-pilot/inputs/page_YYYY/original_page.png`
- Preserve as read-only source: `raw/udl/source/UnderstandingDeepLearning_02_09_26_C.pdf`
- Preserve as read-only accepted style oracle: `raw/udl/textbook/pages/ch01-introduction/`, `raw/udl/textbook/pages/ch02-supervised-learning/`, `raw/udl/textbook/pages/ch03-shallow-neural-networks/`
- Modify only after staging validation passes: `raw/udl/textbook/pages/`, `raw/udl/textbook/blocks/`, `raw/udl/textbook/figures/`, `raw/udl/textbook/index.md`, `raw/udl/textbook/log.md`

## Non-Negotiable Fusion Contract

Every worker must follow this contract exactly.

1. Do not use current `raw/udl/textbook/pages/ch04-*` through `ch21-*` as source text. They are failed rollout output and may only be used as negative examples.
2. For each final book page `page_XXXX`, read its `manifest.json` from `output/udl-fusion-pilot/inputs/page_YYYY/`, where `YYYY` is the manifest `source_pdf_page_name`. Workers must not assume book page and PDF page are the same.
3. Read `deepseek.md`, `deepseek_raw.txt`, `paddle.md`, `original_page.png`, and `paddle_figures/` for each page before writing the fused page.
4. Use DeepSeek as the first prose/math candidate, Paddle as the layout and figure backbone, and the page image/formula crops as visual truth for equations and layout breaks.
5. Keep visual figures and captions centered:

```html
<p align="center">
  <img src="../../figures/page_XXXX_fig_N.jpg" alt="Figure X.Y concise description" />
</p>

<p align="center">
  <strong>Figure X.Y</strong> Caption text...
</p>
```

6. Do not include formula crops as final images when LaTeX can be transcribed. Equation crops are evidence only.
7. Do not leave review notes in final Markdown. Put uncertainty in `output/udl-fusion-redo/reports/chXX.md` and mark the relevant block confidence honestly.
8. Block JSON `source` is provenance: use `deepseek`, `paddle`, `deepseek+paddle`, or `codex-fusion`. Use `codex-fusion` only when the worker reconstructs content from page evidence.
9. Headings must be textual. Do not put complex `$...$` math in headings. Move formula descriptions into the first paragraph or a display equation.
10. Final Markdown must be readable and parseable by LLMs: one logical paragraph per paragraph block, no OCR line-break hyphenation, no duplicated caption prose, no duplicated section transition text.

## GitHub-Safe Math Contract

Every equation must satisfy these rules before a worker can mark a page complete.

1. Inline math uses `$...$`; display math uses `$$` fences with delimiters on their own lines.
2. No `\[` / `\]`, no `\(` / `\)`, no `\tag{...}`, no `\operatorname`, and no `$^1$` footnote markers.
3. Use `\mathrm{argmin}`, `\mathrm{ReLU}`, `\mathrm{HardSwish}`, or plain text instead of `\operatorname{...}`.
4. Use `\Pr`, `\log`, `\exp`, `\sum`, `\prod`, `\int`, `\frac`, `\sqrt`, `\mathbf`, `\boldsymbol`, `\mathbb`, and `\mathcal` only in normal LaTeX form, not double escaped.
5. Use `\mid` or `\,|\,` for conditional bars in probability expressions. Do not write literal OCR `||`.
6. Do not leave bare OCR math tokens such as `argmin`, `argmax`, `Pr(...)`, `Norm(...)`, or `log(...)` in display math. Use `\mathrm{argmin}`, `\mathrm{argmax}`, `\Pr[...]`, `\mathcal{N}(...)`, and `\log[...]` or equivalent GitHub-renderable LaTeX.
7. Do not nest display math environments. A `$$` block must not contain `\begin{align}`, `\begin{align*}`, `\[` or another display wrapper. Use only the inner `aligned` environment when alignment is needed.
8. Multi-row equations must not be compressed onto one line. Put each aligned row on its own Markdown line.
9. Display equations that need alignment must use this shape:

```markdown
$$
\begin{aligned}
left_hand_side
&= first line \\
&= second line
\end{aligned}
\qquad (18.21)
$$
```

10. No equation line may consist only of `=`, `&=`, `+`, `-`, or other operators. If GitHub fails to render, the fallback text must still not become a Markdown heading or horizontal rule.
11. Equation numbers are plain visible math at the end, such as `\qquad (18.21)`.
12. Inline set literals use `$\lbrace x_i, y_i\rbrace$`, not escaped Markdown braces.
13. Any page with an equation reconstructed from visual evidence must list the equation number in the chapter report.

## Subagent Work Split

Use fresh worker subagents with disjoint output ownership. Workers may read all evidence but may write only their owned staging paths.

- Worker A: chapters 1-3, writes `output/udl-fusion-redo/fused/ch01/` through `ch03/`, matching `blocks/` and `reports/ch01-03.md`.
- Worker B: chapters 4-6, writes `output/udl-fusion-redo/fused/ch04/` through `ch06/`, matching `blocks/` and `reports/ch04-06.md`.
- Worker C: chapters 7-9, writes `output/udl-fusion-redo/fused/ch07/` through `ch09/`, matching `blocks/` and `reports/ch07-09.md`.
- Worker D: chapters 10-12, writes `output/udl-fusion-redo/fused/ch10/` through `ch12/`, matching `blocks/` and `reports/ch10-12.md`.
- Worker E: chapters 13-15, writes `output/udl-fusion-redo/fused/ch13/` through `ch15/`, matching `blocks/` and `reports/ch13-15.md`.
- Worker F: chapters 16-18, writes `output/udl-fusion-redo/fused/ch16/` through `ch18/`, matching `blocks/` and `reports/ch16-18.md`.
- Worker G: chapters 19-21, writes `output/udl-fusion-redo/fused/ch19/` through `ch21/`, matching `blocks/` and `reports/ch19-21.md`.

## Task 1: Reset Contract And Staging

**Files:**
- Create: `docs/superpowers/plans/2026-06-10-udl-full-book-fusion-redo.md`
- Create ignored: `output/udl-fusion-redo/`

- [ ] **Step 1: Confirm the failed rollout is not a source**

Run:

```bash
git status --short
find raw/udl/textbook/pages -name '*.md' | wc -l
find output/udl-fusion-pilot/inputs -maxdepth 1 -type d -name 'page_*' | wc -l
```

Expected: a clean or understood git state, 436 published Markdown pages, and 436 prepared input directories.

- [ ] **Step 2: Create a clean staging root**

Run:

```bash
mkdir -p output/udl-fusion-redo/fused output/udl-fusion-redo/blocks output/udl-fusion-redo/figures output/udl-fusion-redo/reports
```

Expected: no changes to tracked files except this plan.

- [ ] **Step 3: Record the reset decision**

Update `output/udl-fusion-redo/reports/review-queue.md` with:

```markdown
# UDL Fusion Redo Review Queue

The previous full-book rollout is treated as failed output, not source evidence.
Workers must fuse from `output/udl-fusion-pilot/inputs/page_YYYY/` evidence and write fresh staged pages here.
```

## Task 2: Dispatch Chapter Fusion Workers

**Files:**
- Workers write only their assigned `output/udl-fusion-redo/fused/chXX/`
- Workers write only their assigned `output/udl-fusion-redo/blocks/chXX/`
- Workers write only their assigned `output/udl-fusion-redo/reports/chXX*.md`

- [ ] **Step 1: Spawn workers A-F**

Dispatch six workers for chapters 1-18 using the worker prompt in this plan. Do not dispatch two workers for the same chapter. Tell every worker that other agents are working in the repo and they must not revert or edit unrelated files.

- [ ] **Step 2: Spawn worker G when capacity is available**

Dispatch worker G for chapters 19-21 with the same prompt after one of workers A-F completes or the agent pool has capacity.

- [ ] **Step 3: Require a DONE_WITH_REPORT response**

Each worker must return:

```text
Status: DONE_WITH_REPORT or BLOCKED
Owned chapters:
Pages completed:
Files written:
Validation run:
Equation pages visually checked:
Figure/caption pages visually checked:
Review queue:
```

If a worker returns `BLOCKED`, the main session must inspect that chapter locally, provide missing context, and redispatch or split the chapter.

## Worker Prompt Template

Use this exact prompt shape and fill in chapter ownership.

```text
You are a chapter fusion worker in /Users/fang/projects/torchbloom.

The user rejected the previous full-book rollout because equations rendered badly on GitHub. Your job is a fresh page-level fusion from evidence, not a patch pass.

Ownership:
- You own chapters: <CHAPTERS>
- You may write only:
  - output/udl-fusion-redo/fused/chXX/
  - output/udl-fusion-redo/blocks/chXX/
  - output/udl-fusion-redo/figures/page_XXXX_fig_N.jpg for figures referenced by your owned pages
  - output/udl-fusion-redo/reports/<YOUR_REPORT>.md
- You may read all source evidence.
- You are not alone in the codebase. Other workers may be writing other chapter folders. Do not revert or edit unrelated files.

Read first:
- docs/superpowers/plans/2026-06-10-udl-full-book-fusion-redo.md
- docs/superpowers/specs/2026-06-09-udl-hybrid-ocr-fusion-pilot-design.md
- raw/udl/textbook/chapter_map.json
- Accepted style examples:
  - raw/udl/textbook/pages/ch03-shallow-neural-networks/page_0035.md
  - raw/udl/textbook/pages/ch03-shallow-neural-networks/page_0037.md

For every owned book page:
1. Use the chapter map to identify book page and PDF page.
2. Read `output/udl-fusion-pilot/inputs/page_YYYY/manifest.json`, where `YYYY` is the manifest `source_pdf_page_name`.
3. Read that page's `deepseek.md`, `deepseek_raw.txt`, `paddle.md`, `original_page.png`, and any `paddle_figures/`.
4. Write a fresh fused Markdown page under `output/udl-fusion-redo/fused/chXX/page_XXXX.md`.
5. Write matching block JSON under `output/udl-fusion-redo/blocks/chXX/page_XXXX.blocks.json`.
6. Copy or regenerate only final non-formula visual figures under `output/udl-fusion-redo/figures/`.
7. For equations, transcribe LaTeX from evidence and enforce the GitHub-Safe Math Contract. Formula crops are evidence only, not final images.
8. For heading text, remove complex inline math from headings; put math in prose or equation blocks.
9. Add uncertain pages to your chapter report, not the final Markdown.

Before reporting DONE:
- Check every final referenced figure path exists.
- Check no final Markdown contains `\\[`, `\\]`, `\\(`, `\\)`, `\\tag{`, `\\operatorname`, `Review note`, `review_notes`, `![`, or formula crop images.
- Check no final Markdown contains nested display math environments, one-line multi-row `align`/`aligned` blocks, or bare OCR math tokens such as `argmin`, `argmax`, `Pr(`, `Norm(`, or `log(` inside display equations.
- Check no line inside a display equation consists only of `=`, `&=`, `+`, or `-`.
- Check every page has frontmatter and matching block JSON.
- Spot-check equation-heavy pages against `original_page.png` or formula crops.

Return:
Status: DONE_WITH_REPORT or BLOCKED
Owned chapters:
Pages completed:
Files written:
Validation run:
Equation pages visually checked:
Figure/caption pages visually checked:
Review queue:
```

## Task 3: Main-Session Spec Review

**Files:**
- Read: `output/udl-fusion-redo/fused/`
- Read: `output/udl-fusion-redo/blocks/`
- Read: `output/udl-fusion-redo/reports/`

- [ ] **Step 1: Review worker reports**

Run:

```bash
find output/udl-fusion-redo/reports -type f -maxdepth 1 -print -exec sed -n '1,220p' {} \;
```

Expected: every chapter group reports completed pages and no hidden review notes in final Markdown.

- [ ] **Step 2: Verify output counts**

Run:

```bash
find output/udl-fusion-redo/fused -name '*.md' | wc -l
find output/udl-fusion-redo/blocks -name '*.blocks.json' | wc -l
```

Expected: 436 Markdown pages and 436 block JSON files.

- [ ] **Step 3: Audit high-risk pages manually**

At minimum inspect staged pages and source evidence for:

```text
page_0025
page_0027
page_0038
page_0277
page_0278
page_0354
page_0358
page_0359
page_0362
```

Expected: no raw inline math, no failed display math, no duplicated page fragments, no formula crops as final images.

## Task 4: Automated Validation

**Files:**
- Modify only if needed: `src/torchbloom/udl_fusion_pilot.py`
- Modify only if needed: `tests/test_udl_fusion_pilot.py`

- [ ] **Step 1: Run existing validation on staged output**

Run:

```bash
.venv/bin/python -m torchbloom.udl_fusion_pilot validate --chapters 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21 --output-dir output/udl-fusion-redo
```

Expected: validation passes. If it fails, fix the staged page from evidence, not by global regex substitution.

- [ ] **Step 2: Add validator coverage for failures discovered during review**

If manual review discovers a repeated structural failure, add a focused failing test to `tests/test_udl_fusion_pilot.py`, update `src/torchbloom/udl_fusion_pilot.py`, and run:

```bash
.venv/bin/python -m pytest tests/test_udl_fusion_pilot.py -q
```

Expected: the new test fails before the validator change and passes after the validator change.

- [ ] **Step 3: Run final project checks**

Run:

```bash
.venv/bin/python -m pytest
.venv/bin/python -m torchbloom.wiki_validation
```

Expected: all tests pass and wiki validation passes.

## Task 5: GitHub Rendering Review

**Files:**
- Read: staged pages from `output/udl-fusion-redo/fused/`
- Read after publish: GitHub pages on branch `codex/udl-full-fusion-branding`

- [ ] **Step 1: Render a local high-risk sample**

Open or preview the staged Markdown for the high-risk pages from Task 3.

Expected: local preview renders math and figures cleanly.

- [ ] **Step 2: Publish to `raw/udl/textbook` only after staged validation**

Run:

```bash
.venv/bin/python -m torchbloom.udl_fusion_pilot publish --chapters 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21 --output-dir output/udl-fusion-redo --clean-legacy
```

Expected: publish report lists 436 pages and 436 block sidecars copied.

- [ ] **Step 3: Push and sample GitHub rendering**

After commit and push, inspect at least 50 pages on GitHub, weighted toward equation-heavy chapters 15-18 and the high-risk pages from Task 3.

Expected: no GitHub red math errors, no raw `$...$` math in prose, no heading math corruption, no missing figures.

- [ ] **Step 4: Re-run validation against the published raw tree**

After publishing to `raw/udl/textbook`, run a second validation or scan against the published tree, not only `output/udl-fusion-redo`.

Expected: the published corpus matches the staged corpus and does not reintroduce path, math, or sidecar drift.

## Task 6: Final Commit And Wrap-Up

**Files:**
- Modify: `raw/udl/textbook/`
- Modify: docs only if process changed

- [ ] **Step 1: Review diff**

Run:

```bash
git status --short
git diff --stat
git diff --check
```

Expected: only the redo plan, validated corpus replacement, and intentional validator/doc changes are present.

- [ ] **Step 2: Commit**

Run:

```bash
git add docs/superpowers/plans/2026-06-10-udl-full-book-fusion-redo.md raw/udl/textbook src/torchbloom/udl_fusion_pilot.py tests/test_udl_fusion_pilot.py
git commit -m "Redo UDL fusion from source evidence"
```

Expected: one coherent redo commit.

- [ ] **Step 3: Push**

Run:

```bash
git push origin codex/udl-full-fusion-branding
```

Expected: branch updates on GitHub.

## Follow-Up Correction After GitHub Spot Checks

Updated on 2026-06-10 after GitHub page review found that the earlier redo still allowed OCR math residue in later chapters, especially embedded diffusion equations around pages 357-359.

Root cause:

- The corrected staged output was not enough by itself; the published `raw/udl/textbook` layer had to be regenerated from the validated redo output.
- The validator caught many Markdown body failures, but block sidecar validation did not inspect `alt` fields.
- Semantic OCR residue needed explicit checks, not only syntax checks.

Additional validator coverage now rejects:

- Standalone equation-number residue in prose or blocks, such as `(18.17)`.
- Raw OCR math braces in prose, such as `{z_{t}}`.
- Bare OCR math tokens inside inline math, such as `$Pr(y|x)$`.
- Broken sized delimiters before norm bars.
- Missing closing `\rbrace` in display-math set notation.
- Glued OCR commands such as `\lambdaK`, `\inR`, `\inne`, `\par`, and `\lbrac`.
- The same string checks now cover block `alt` fields as well as `text`, `latex`, and `caption`.

Current follow-up publish stats:

- Published Markdown pages: 436
- Published block sidecars: 436
- Validated blocks: 3,601
- Referenced high-resolution figure crops: 271
- Legacy files cleaned during publish: 414

Current verification:

```bash
.venv/bin/python -m torchbloom.udl_fusion_pilot validate --chapters 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21 --raw-root raw/udl/textbook --output-dir output/udl-fusion-redo
# validation passed: 436 pages, 3601 blocks

.venv/bin/python -m pytest tests/test_udl_fusion_pilot.py -q
# 38 passed

.venv/bin/python -m pytest -q
# 79 passed

.venv/bin/python -m torchbloom.wiki_validation
# wiki/udl: ok
```

Published-output residue scan:

- Scanned 436 Markdown pages and 436 JSON sidecars under `raw/udl/textbook`.
- Found zero matches for the OCR residue patterns above.

## Execution Outcome

Completed on 2026-06-10.

- Fusion staging root: `output/udl-fusion-redo/`
- Published root: `raw/udl/textbook/`
- Fused Markdown pages: 436
- Block sidecars: 436
- Validated blocks: 3,608
- Referenced high-resolution figure crops: 271
- Legacy files cleaned during publish: 418

Subagent rollout:

- Chapters 1-3: 40 pages
- Chapters 4-6: 55 pages
- Chapters 7-9: 65 pages
- Chapters 10-12: 79 pages
- Chapters 13-15: 64 pages
- Chapters 16-18: 70 pages
- Chapters 19-21: 63 pages

Validator changes added during the redo:

- Reject nested display math wrappers such as `\begin{align}` inside `$$`.
- Reject blank lines inside display math, which GitHub can split into an unrenderable expression.
- Reject stray dollar signs inside display math, which indicate broken OCR/fusion fences.
- Reject mismatched probability delimiters such as `\Pr\left(...|...)\right]`.
- Reject one-line multi-row `aligned` equations that render poorly on GitHub.
- Reject bare OCR math tokens such as `argmin`, `argmax`, `Pr(`, `Norm(`, and `log(` in display equations.

Final verification:

```bash
.venv/bin/python -m torchbloom.udl_fusion_pilot validate --chapters 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21 --output-dir output/udl-fusion-redo
# validation passed: 436 pages, 3608 blocks

.venv/bin/python -m pytest tests/test_udl_fusion_pilot.py -q
# 35 passed

.venv/bin/python -m pytest -q
# 78 passed

.venv/bin/python -m torchbloom.wiki_validation
# wiki/udl: ok

git diff --check
# no output
```

Published-output audits:

- Staged and published Markdown/sidecar files matched byte-for-byte.
- All final image references resolved.
- Scans found no `\operatorname`, `\tag{`, `\[`, `\]`, `\(`, `\)`, `review_notes`, `Review note`, or Markdown image syntax in published pages.
- GitHub rendering checks found and fixed additional equation/fence failures on `page_0058`, `page_0059`, `page_0061`, `page_0069`, `page_0070`, and `page_0362`.
- Follow-up scans found zero display-math dollar leaks, zero blank display-math bodies, and zero mismatched probability delimiters in published pages.
- A pushed-branch GitHub HTML sample of 50 pages, including all high-risk pages above, found zero rendered math error messages.
