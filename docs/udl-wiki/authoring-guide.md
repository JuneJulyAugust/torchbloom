# UDL Wiki Authoring Guide

## Authoring Loop

1. Read the relevant fused OCR pages in `raw/udl/textbook/pages/`.
2. Check answer availability in `raw/udl/answers/index.md`.
3. Write original TorchBloom explanations in `wiki/udl/`.
4. Add source anchors for every UDL-specific claim.
5. Mark uncertain OCR, equations, figures, or answer interpretation in
   `wiki/udl/audit-queue.md`.
6. Keep `confidence: directional` until a human checks the page against the PDF.

## Page Priorities

Write pages in this order for each chapter:

1. Chapter reading guide.
2. Practice index.
3. Required concept pages.
4. Required math bridges.
5. Equation pages.
6. Practice cards.
7. Notebook guide.

## High-School Math Bridge Rule

Every formal object should have a bridge from familiar ideas:

- functions as input-output machines,
- graphs as shape stories,
- vectors as lists of numbers,
- matrices as organized function machines,
- derivatives as local slope,
- probability as weighted uncertainty.

If a page needs a bridge that does not exist yet, create the bridge page before
depending on it heavily.

## Practice Cards

Practice cards should test one clear skill. They may anchor to UDL questions,
but the prompt, hints, and rubric should be written in TorchBloom language.

Use `answer_policy` carefully:

- `selected-answer`: the student answer booklet has a relevant selected answer.
- `torchbloom-derived`: TorchBloom worked the answer independently.
- `review-needed`: no reliable answer is attached yet.

Do not paste full selected answers into public-style wiki pages. Keep answer
booklet text in `raw/udl/answers/` and use concise private notes only when
needed.
