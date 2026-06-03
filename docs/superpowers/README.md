# Superpowers Docs

This folder stores durable records from the Superpowers workflow.

## Layout

- `specs/` - design specs, named `YYYY-MM-DD-topic-design.md`.
- `plans/` - implementation plans, named `YYYY-MM-DD-topic.md`.

## Rules

- Specs explain what is being built and why.
- Plans explain exact implementation steps, verification, and commit boundaries.
- Keep these files focused on decisions that future agents need.
- Do not store generated command logs here. Use `output/` for transient evidence.
