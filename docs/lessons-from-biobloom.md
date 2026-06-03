# Lessons From BioBloom

TorchBloom starts with useful patterns from BioBloom, but tightens artifact organization earlier.

## What Worked

- A clear mission helped keep the project educational instead of tool-driven.
- The split between `raw/`, `wiki/`, `docs/`, and app code gave later work places to land.
- Dated Superpowers specs and plans preserved design intent.
- Methodology pages made generated wiki content easier to audit.
- Tests became valuable once source-derived artifacts started feeding product behavior.

## What Got Messy

- Raw source files, generated outputs, and curated wiki pages were sometimes added before their contracts were clear.
- Some docs were written after implementation, which made early decisions harder to reconstruct.
- Large generated outputs and local editor artifacts needed stronger default ignore rules.
- Retired directions remained discoverable, but not always clearly separated from active work.
- Wiki methodology existed, but each new corpus still needed a cleaner intake checklist.

## TorchBloom Adjustments

- Create only the folders needed for the current planning and LLM-wiki work. Do not pre-create every future app, package, or curriculum directory.
- Add `AGENTS.md` now so future agents share the same artifact boundaries.
- Treat `raw/llm-wiki/manifests/` as the first stop for every source.
- Keep synthesized pages under `wiki/llm-wiki/` with frontmatter, source anchors, confidence, and audit queues from day one.
- Keep generated outputs in ignored `output/` until a human promotes them.
- Keep Superpowers specs and plans under `docs/superpowers/` with dated names.
- Prefer one source-grounded concept page model over parallel entity trees unless a real second use case appears.
