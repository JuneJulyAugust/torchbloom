# Transformer Web MVP Design

**Date:** 2026-06-11
**Status:** Implemented graph-first course MVP, expanded after learner/subagent review
**Scope:** Local Next.js web course for learning UDL Chapter 12 transformers

## Purpose

Build the first learner-facing TorchBloom web system around the Transformer chapter. This is no longer only a curriculum-artifact pilot. The system should be usable by an experienced learner who wants a Math Academy-style course path through transformers, with graph navigation, equations, diagnostic placement, practice, and an interactive attention lab.

## Scaffold Borrowed From BioBloom

BioBloom's useful patterns:

- Next.js app under `web/`
- `src/app` for the route shell
- `src/components` for learner workspace components
- `src/lib` for course/study logic
- Vitest and Testing Library for behavior tests
- build/lint/test scripts in `package.json`
- static/local data first, backend later

TorchBloom does not copy BioBloom's biology content, auth roles, Supabase path, or parent/admin flows in this first MVP.

## Architecture

```text
web/
  src/app/
    layout.tsx
    page.tsx
    globals.css
  src/components/
    transformer-course-app.tsx
    math-markdown.tsx
  src/lib/course/
    course-data.ts
    course-engine.ts
    types.ts
  src/__tests__/
    course-engine.test.ts
    transformer-course-app.test.tsx
```

The course is currently static and local. The course engine owns diagnostic grading, repair routing, practice feedback, graph ordering, and selected-node lookup. The React app owns interaction state and presentation.

The current data contract is intentionally richer than the first MVP:

- each node has source anchors into UDL Chapter 12 markdown pages;
- each node has graph coordinates for node-link rendering;
- each node has a rendered LaTeX equation when relevant;
- each node has Little-style lesson frames;
- each node has mastery evidence and misconception notes;
- each node has at least one mastery-gated practice item.

## MVP Capabilities

- Displays a persistent graph canvas with visible prerequisite edges and node states.
- Shows a 42-node, source-grounded Transformer course spine covering text problem framing, tokenization, embeddings, positional encodings, attention mechanics, transformer layers, encoder/decoder models, cross-attention, long-context variants, vision transformers, and the masked-decoder capstone.
- Lets the learner select graph nodes and inspect summaries, rendered equations, Little-style lesson frames, mastery evidence, misconceptions, and source anchors in a corner inspector panel.
- Provides a nine-item diagnostic for experienced learner placement.
- Routes strong learners into the next ready graph node.
- Routes prerequisite misses to repair nodes.
- Provides one mastery-gated practice item per graph node, with misconception-aware feedback.
- Prevents manual mastery marking until the selected node's practice check is passed.
- Includes a KaTeX-rendered lesson surface and equation blocks.
- Includes an attention lab for Q/K/V projection, scaled scores, softmax shares, causal masking, prediction-before-reveal, and mixed value outputs.
- Includes a Tiny Masked Decoder project route.

## Non-Goals

- No account system.
- No backend.
- No payment system.
- No parent dashboard.
- No full spaced-repetition scheduler yet.
- No PyTorch sandbox yet.
- No executable Python/PyTorch capstone runner yet.
- No YAML curriculum artifact pipeline yet; course content still lives in TypeScript while the schema stabilizes.
- No true adaptive mastery model beyond diagnostic repair routing, local practice pass state, and local mastered nodes.

## Quality Bar

- Web tests pass.
- Lint passes.
- Next production build passes.
- UI starts directly as the learning workspace, not a marketing page.
- Graph and equation interactions are visible without signing in.
- The system remains curriculum-first: course logic lives in `lib/course`, not hard-coded only in JSX.

## Next Improvements

- Persist progress in local storage.
- Add non-multiple-choice practice for numeric compute, shape tracing, code reading, explanation, and debug tasks.
- Add a real code workspace for the Tiny Masked Decoder.
- Promote course content from inline TypeScript into validated curriculum data files once the shape stabilizes.
- Add graph validation for cycles, missing prerequisites, orphan nodes, source-anchor existence, and required lesson/practice fields.
- Add spaced review states: introduced, practiced, mastered, durable, and transfer-ready.
