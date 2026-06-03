# Repository Structure

TorchBloom separates source material, synthesized knowledge, planning docs, and generated output from the beginning. This avoids the artifact drift that made later BioBloom work harder to audit.

## Top-Level Areas

| Path | Tracked | Purpose |
| --- | --- | --- |
| `README.md` | Yes | Product vision and project framing. |
| `AGENTS.md` | Yes | Operating instructions for coding and research agents. |
| `docs/` | Yes | Durable project docs, designs, and workflow records. |
| `docs/superpowers/` | Yes | Specs and plans from the Superpowers workflow. |
| `raw/` | Selective | Source intake, manifests, and license-aware extracts. |
| `wiki/` | Yes | Synthesized, source-grounded study pages. |
| `output/` | No | Generated reports, temporary build products, and one-off outputs. |
| `scratch/` | No | Local experiments and disposable notes. |

## Artifact Lifecycle

```text
source record
  -> raw manifest
  -> optional raw extract
  -> synthesized wiki page
  -> reviewed curriculum or product artifact
  -> generated output
```

Rules:

- Raw source files are not edited in place. Add corrected or normalized derivatives as explicit extracts.
- Wiki pages are original synthesis, not copied source material.
- Generated files are ignored unless promoted into a curated, reviewed artifact.
- Every durable artifact should expose source anchors, confidence, and review status.

## Naming Conventions

- Use kebab-case for directories and Markdown files.
- Use dated Superpowers docs: `YYYY-MM-DD-topic-design.md` and `YYYY-MM-DD-topic.md`.
- Use stable wiki ids that match filenames when possible.
- Keep source manifests human-readable and reviewable.
