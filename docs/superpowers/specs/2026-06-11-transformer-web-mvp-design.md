# Transformer Web MVP Design

**Date:** 2026-06-11
**Status:** Implemented initial MVP
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

The course is currently static and local. The course engine owns diagnostic grading, repair routing, practice feedback, graph visibility, and selected-node lookup. The React app owns interaction state and presentation.

## MVP Capabilities

- Displays the Transformer course graph by stage.
- Shows source-grounded nodes for foundations, attention core, transformer block, decoder project, and extensions.
- Lets the learner select nodes and inspect summaries, equations, Little-style paths, and mastery evidence.
- Provides a five-item diagnostic for experienced learner placement.
- Routes strong learners into the attention core.
- Routes prerequisite misses to repair nodes.
- Provides multiple practice items with misconception-aware feedback.
- Includes a lesson frame that displays equations.
- Includes an attention lab for query-token selection, softmax shares, and future-token masking.
- Includes a Tiny Attention Router project route.

## Non-Goals

- No account system.
- No backend.
- No payment system.
- No parent dashboard.
- No full spaced-repetition scheduler yet.
- No PyTorch sandbox yet.
- No full UDL Chapter 12 coverage beyond the initial core route and extension map.

## Quality Bar

- Web tests pass.
- Lint passes.
- Next production build passes.
- UI starts directly as the learning workspace, not a marketing page.
- Graph and equation interactions are visible without signing in.
- The system remains curriculum-first: course logic lives in `lib/course`, not hard-coded only in JSX.

## Next Improvements

- Persist progress in local storage.
- Add a richer graph visualization with edge lines and prerequisites.
- Add more UDL Chapter 12 practice items.
- Add a real code workspace for the Tiny Attention Router.
- Promote course content from inline TypeScript into validated curriculum data files once the shape stabilizes.
