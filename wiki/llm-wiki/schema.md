# Schema

Normative schema for `wiki/llm-wiki/` pages.

## Frontmatter

```yaml
---
id: knn-distance-voting
type: method
title: k-Nearest Neighbors: Distance and Voting
track: classical-ml
stage: stage-1
source_anchors:
  - source: example-source-id
    locator: section 2.1
confidence: directional
prerequisites: [coordinates-and-distance, tables-as-data]
related: [classification, nearest-neighbor-search]
learning_objectives:
  - Classify a point by comparing distances to labeled examples.
  - Explain how changing k can change a prediction.
---
```

## Field Rules

| Field | Required | Rule |
| --- | --- | --- |
| `id` | Yes | Stable kebab-case id. Prefer matching the filename. |
| `type` | Yes | `concept`, `math`, `programming`, `method`, `model`, `project`, or `source-note`. |
| `title` | Yes | Human-readable page title. |
| `track` | Yes | Planned track from `index.md`, in kebab-case. |
| `stage` | Yes | Learning stage such as `stage-0`, `stage-1`, or `stage-4`. |
| `source_anchors` | Yes | At least one manifest-backed source and locator. |
| `confidence` | Yes | `directional`, `reviewed`, or `validated`. |
| `prerequisites` | Yes | List of page ids or pending ids. Use `[]` when none. |
| `related` | Yes | List of page ids or pending ids. |
| `learning_objectives` | Yes | Action-oriented objectives that can become exercises or diagnostics. |

## Body Template

```markdown
# Page Title

## Core Idea

## Why It Matters

## Prerequisites

## Learner-Friendly Explanation

## Formal Version

## Worked Example

## Common Misconceptions

## Practice Hooks

## Source Anchors

## Related
```

## Review Checklist

- `id` matches the filename.
- Every frontmatter field is present.
- Source ids resolve to `raw/llm-wiki/manifests/`.
- The learner-friendly section is understandable before formal notation.
- The formal section is mathematically or computationally honest.
- Misconceptions are concrete.
- Practice hooks can feed exercises, diagnostics, or projects.
