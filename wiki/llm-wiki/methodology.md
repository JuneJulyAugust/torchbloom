# Methodology

How the LLM wiki is built, extended, and reviewed.

## Inputs

Primary source records live in `raw/llm-wiki/manifests/`.

Optional source files and extracts live in:

- `raw/llm-wiki/sources/`
- `raw/llm-wiki/extracts/`
- local-only `raw/llm-wiki/private/`

## Confidence Tiers

| Tier | Meaning | Use it for |
| --- | --- | --- |
| `directional` | Useful synthesis from trusted sources, not independently reviewed. | Draft concept pages and early curriculum mapping. |
| `reviewed` | Checked against source anchors by one reviewer. | Learner-facing drafts and diagnostic planning. |
| `validated` | Checked by two reviewers or backed by tests/fixtures. | Stable curriculum and app-consumed artifacts. |

## Authoring Rules

1. Write Markdown-first with source-aware frontmatter.
2. Use original prose and examples unless the source license explicitly permits reuse.
3. Cite source anchors through manifest ids and stable locators.
4. Explain concepts twice when useful: learner-friendly intuition first, formal version second.
5. Add prerequisites, related pages, and practice hooks even when the linked pages are pending.
6. Keep unresolved source, license, or review questions in [audit-queue.md](audit-queue.md).

## Workflow For A New Concept Page

1. Choose one small concept with clear prerequisites.
2. Confirm at least one source manifest exists.
3. Draft frontmatter from [schema.md](schema.md).
4. Write the required body sections.
5. Check that every substantive claim has a source anchor or clear project rationale.
6. Add pending related pages to the audit queue.
7. Mark confidence as `directional` until reviewed.

## Regeneration And Drift

When source extracts, curriculum goals, or concept relationships change:

1. Update raw manifests or extracts first.
2. Diff affected wiki pages.
3. Update only claims, anchors, and links that changed.
4. Record broad reclassification work in the audit queue before sweeping edits.

## Out Of Scope For The Bootstrap

- Full coverage of deep learning or transformer resources.
- Public redistribution of restricted source material.
- A complete knowledge graph.
- App ingestion contracts beyond the frontmatter draft in [schema.md](schema.md).
