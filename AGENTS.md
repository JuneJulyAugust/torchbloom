# TorchBloom AI Agent Guide

This repository is in the vision and planning stage for TorchBloom AI, a mastery-based learning path from elementary math to real AI implementation. Agents should keep the project rigorous, warm, and curriculum-first.

## Operating Principles

1. **Curriculum before platform.** Do not build app or infrastructure pieces before the learning model, source material, and artifact contracts are clear.
2. **Depth before demos.** Avoid shallow AI demos that do not connect back to math, programming, data, and explanation skills.
3. **Artifact boundaries matter.** Keep raw inputs, synthesized wiki pages, design docs, generated output, and application code in separate places.
4. **Source-grounded writing.** Wiki pages must cite source anchors and distinguish verified facts from directional synthesis.
5. **Child-friendly rigor.** Write for young learners and mentors without diluting the underlying math or computing ideas.
6. **Small commits.** Commit coherent steps separately: vision, scaffold, source intake, wiki synthesis, tests, app changes.
7. **Verify claims.** Before saying work is complete or tests pass, run the relevant check and read the output.

## Repository Map

- `README.md` - project vision, mission, learning pillars, and early roadmap.
- `docs/` - durable design notes, repo conventions, and initiative docs.
- `docs/superpowers/` - dated specs and implementation plans produced by the Superpowers workflow.
- `docs/llm-wiki/` - design and process docs for the LLM/AI knowledge wiki.
- `raw/` - source intake and manifests. Treat raw source material as immutable.
- `wiki/` - source-grounded, synthesized study pages intended for review and future product use.
- `output/` - generated build products and temporary reports. This is ignored by git.

Do not create large future application folders just because they appear in the README. Add new top-level areas only when a concrete design or implementation task needs them.

## LLM Wiki Workflow

1. Record each source in `raw/llm-wiki/manifests/` before using it.
2. Put local extracts or OCR outputs under `raw/llm-wiki/extracts/` only when the license and repository policy allow it.
3. Write synthesized, original study pages under `wiki/llm-wiki/`.
4. Give each wiki page stable frontmatter: `id`, `type`, `track`, `stage`, `source_anchors`, `confidence`, `prerequisites`, and `related`.
5. Put uncertain mappings, source gaps, and review needs in `wiki/llm-wiki/audit-queue.md`.

## Documentation Workflow

For meaningful new work:

1. Add or update a focused design note under `docs/`.
2. If using the Superpowers workflow, write specs to `docs/superpowers/specs/` and plans to `docs/superpowers/plans/`.
3. Keep generated logs and one-off outputs out of git unless they are curated evidence.
4. Update `docs/README.md` when adding a new durable documentation area.

## Quality Bar

Every durable artifact should answer:

- What is its purpose?
- What source or decision does it depend on?
- What can safely consume it later?
- What is still uncertain?

If an artifact cannot answer those questions, keep it in `output/` or `scratch/` until it is ready.
