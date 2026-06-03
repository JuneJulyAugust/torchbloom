# LLM Wiki Design

**Status:** Bootstrap design. **Scope:** `wiki/llm-wiki/`. **Consumers:** curriculum planning, future knowledge graph, diagnostics, projects, and app surfaces.

## Purpose

The LLM wiki is TorchBloom's source-grounded AI knowledge layer. It should turn trusted resources into original study pages that a learner, parent, mentor, or future app can use without losing provenance.

It is not a mirror of any book, paper, course, or website. It is a reviewed synthesis layer that records what the learner must understand, which sources support it, what prerequisites it depends on, and how it can be practiced.

## Organization

```text
wiki/llm-wiki/
  index.md
  methodology.md
  schema.md
  audit-queue.md
  tracks/
    math-foundations/
    programming-foundations/
    data-and-probability/
    classical-ml/
    deep-learning/
    transformers/
    ai-olympiad/
    paper-reproductions/
```

Do not create all track folders until pages exist for them. The index and schema define the target shape first.

## Page Model

Use one unified concept page model with a `type` field instead of parallel trees for entities, methods, formulas, and models.

Allowed `type` values:

- `concept` - an idea or principle.
- `math` - a mathematical object, operation, theorem, or technique.
- `programming` - a programming construct or computational pattern.
- `method` - an ML or data method.
- `model` - a model family or architecture.
- `project` - a guided build that integrates several concepts.
- `source-note` - a review note about a source, paper, or course.

## Required Frontmatter

```yaml
---
id: knn-distance-voting
type: method
title: k-Nearest Neighbors: Distance and Voting
track: classical-ml
stage: stage-1
source_anchors:
  - source: source-id
    locator: chapter-or-section
confidence: directional
prerequisites: [coordinates-and-distance, tables-as-data]
related: [classification, nearest-neighbor-search]
learning_objectives:
  - Classify a point by comparing distances to labeled examples.
  - Explain how changing k can change a prediction.
---
```

Confidence values:

- `directional` - useful synthesis, not yet independently reviewed.
- `reviewed` - checked against source anchors by one reviewer.
- `validated` - checked by two reviewers or supported by tests/fixtures.

## Required Body Sections

Use these sections in order:

1. `## Core Idea`
2. `## Why It Matters`
3. `## Prerequisites`
4. `## Learner-Friendly Explanation`
5. `## Formal Version`
6. `## Worked Example`
7. `## Common Misconceptions`
8. `## Practice Hooks`
9. `## Source Anchors`
10. `## Related`

For early-stage pages, the formal section can be short. Do not remove it; the page should show how intuition will eventually connect to formal AI learning.

## Source Standard

- Every source used by a page must have a manifest under `raw/llm-wiki/manifests/`.
- Every substantive claim should map to a source anchor, an accepted domain convention, or an explicit project decision.
- Private or copyrighted full text should remain local unless license review says it can be committed.
- Shareable wiki pages should paraphrase and synthesize.

## Build Sequence

1. Add a source manifest.
2. Add allowed raw extracts, if any.
3. Draft a small concept map for one track.
4. Write one pilot concept page.
5. Run the schema checklist in `wiki/llm-wiki/schema.md`.
6. Add unresolved issues to `wiki/llm-wiki/audit-queue.md`.
7. Only then scale to more pages.

## Acceptance Checklist

A page is ready for review when:

- Its `id` matches the filename.
- Frontmatter has all required fields.
- Source anchors resolve to a manifest entry.
- It names prerequisites and related pages, even if some are pending.
- It includes learner-friendly and formal explanations.
- Misconceptions are concrete wrong-answer patterns.
- Practice hooks connect to TorchBloom's mastery-learning path.
