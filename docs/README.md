# TorchBloom Docs

This folder holds durable project knowledge: design decisions, artifact conventions, source and wiki methodology, and dated Superpowers specs/plans.

## Start Here

- [repo-structure.md](repo-structure.md) - how tracked and generated artifacts are organized.
- [lessons-from-biobloom.md](lessons-from-biobloom.md) - what TorchBloom is borrowing and improving from BioBloom.
- [superpowers/](superpowers/) - dated specs and implementation plans.

## Recent Successful Pilots

- [UDL hybrid OCR fusion pilot design](superpowers/specs/2026-06-09-udl-hybrid-ocr-fusion-pilot-design.md) - completed Ch1-3 fusion contract combining PPStructureV3 layout/crops with DeepSeek prose/math.
- [UDL hybrid OCR fusion pilot implementation plan](superpowers/plans/2026-06-09-udl-hybrid-ocr-fusion-pilot.md) - completed task checklist and verification record.

## Documentation Rules

- Keep durable initiative specs and implementation plans under `docs/superpowers/` until an initiative needs its own stable documentation area.
- Prefer small, named docs over one giant planning file.
- Link from this README when a doc becomes part of the durable repo map.
- Put transient reports, generated logs, and scratch notes in `output/` or `scratch/`; they are ignored by git.
