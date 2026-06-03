# TorchBloom Docs

This folder holds durable project knowledge: design decisions, artifact conventions, source and wiki methodology, and dated Superpowers specs/plans.

## Start Here

- [repo-structure.md](repo-structure.md) - how tracked and generated artifacts are organized.
- [lessons-from-biobloom.md](lessons-from-biobloom.md) - what TorchBloom is borrowing and improving from BioBloom.
- [llm-wiki/](llm-wiki/) - design docs for the source-grounded LLM/AI concept wiki.
- [superpowers/](superpowers/) - dated specs and implementation plans.

## Documentation Rules

- Keep initiative docs close to the initiative: `docs/llm-wiki/` for wiki design, future `docs/curriculum/` for curriculum architecture, and so on.
- Prefer small, named docs over one giant planning file.
- Link from this README when a doc becomes part of the durable repo map.
- Put transient reports, generated logs, and scratch notes in `output/` or `scratch/`; they are ignored by git.
