---
id: udl-schema
type: schema
title: UDL Wiki Schema
chapter_scope: []
source_anchors:
  - source: torchbloom-design
    locator: docs/superpowers/specs/2026-06-03-udl-companion-wiki-mvp-design.md
confidence: directional
prerequisites: []
related: [udl-methodology, udl-audit-queue]
learning_objectives:
  - Define the required metadata and body structures for UDL companion wiki pages.
---

# UDL Wiki Schema

Normative schema for `wiki/udl/`.

## Required Frontmatter

```yaml
---
id: supervised-learning
type: concept
title: Supervised Learning
chapter_scope: [ch02]
source_anchors:
  - source: udlbook-v5.0.3
    locator: raw/udl/textbook/pages/ch02-supervised-learning/page_0031.md
confidence: directional
prerequisites: [functions-as-machines]
related: [linear-regression, loss-functions]
learning_objectives:
  - Explain supervised learning as fitting a function from inputs to targets.
---
```

## Field Rules

| Field | Required | Rule |
| --- | --- | --- |
| `id` | Yes | Stable kebab-case id. Prefer matching the filename except chapter indexes. |
| `type` | Yes | `chapter-pack`, `reading-guide`, `practice-index`, `concept`, `math-bridge`, `equation`, `practice-card`, `notebook-guide`, `index`, `methodology`, `schema`, or `audit`. |
| `title` | Yes | Human-readable page title. |
| `chapter_scope` | Yes | List of chapter ids, or `[]` for cross-book infrastructure. |
| `source_anchors` | Yes | At least one source and locator, unless the page is a pure schema page. |
| `confidence` | Yes | `directional`, `reviewed`, or `validated`. |
| `prerequisites` | Yes | List of page ids or pending ids. Use `[]` when none. |
| `related` | Yes | List of page ids or pending ids. |
| `learning_objectives` | Yes | Action-oriented outcomes that can become questions or checks. |

## Page Types

- `chapter-pack`: chapter landing page and chapter-specific navigation.
- `reading-guide`: section-by-section reading plan for one chapter.
- `practice-index`: chapter question inventory with answer policy and review state.
- `concept`: shared conceptual explanation.
- `math-bridge`: prerequisite ramp from high-school math to UDL notation.
- `equation`: one equation as a first-class learning object.
- `practice-card`: active-recall, compute, derive, code, debug, or transfer prompt.
- `notebook-guide`: study guide for an official UDL notebook.

## Body Sections

Concept pages should use:

```markdown
# Page Title

## Core Idea
## Why It Matters In UDL
## High-School Bridge
## Formal Version
## Worked Example
## Common Misconceptions
## Practice Hooks
## Source Anchors
## Related
```

Practice cards should use:

```markdown
# Practice Title

## Prompt
## What This Tests
## Hints
## Solution Notes
## Self-Check Rubric
## Source Anchors
## Related
```
