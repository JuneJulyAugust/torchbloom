# TorchBloom Web

This is the learner-facing Transformer course MVP.

It is a local Next.js app modeled after the useful parts of BioBloom's web scaffold: course logic in `src/lib`, learner workspace components in `src/components`, and tests in `src/__tests__`.

## Commands

```bash
npm test -- --run
npm run lint
npm run build
npm run dev
```

## Current Scope

- UDL Chapter 12 Transformer course graph
- experienced-learner diagnostic
- repair routing for prerequisite gaps
- lesson/equation panel
- misconception-aware practice
- interactive attention lab
- Tiny Attention Router project route

The app currently uses static local course data. Backend accounts, parent dashboards, and long-term spaced review are later work.
