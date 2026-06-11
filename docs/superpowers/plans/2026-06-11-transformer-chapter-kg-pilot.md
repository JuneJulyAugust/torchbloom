# Transformer Chapter Knowledge Graph Pilot Implementation Plan

> **For agentic workers:** This plan was written before the Transformer web MVP decision. The user later asked to build the learner-facing web system now. Keep the curriculum contract first, but do not treat web work as out of scope anymore.

**Goal:** Build a chapter-level knowledge graph pilot for UDL Chapter 12, with deep authored coverage from self-attention through a tiny masked decoder.

**Status:** Draft plan for review.

**Architecture:** Treat UDL Chapter 12 as the source target. Create a validated curriculum artifact set under `knowledge_graph/pilots/udl-ch12-transformers/`, backed by source anchors from `raw/udl/textbook/pages/ch12-transformers/` and pedagogy anchors from the Math Academy and Little-series research docs.

**Primary Design:** `docs/superpowers/specs/2026-06-11-transformer-chapter-kg-pilot-design.md`

---

## File Structure

Create only after the design is accepted:

```text
knowledge_graph/
  README.md
  pilots/
    udl-ch12-transformers/
      README.md
      source_inventory.yaml
      nodes.yaml
      edges.yaml
      little_paths.yaml
      diagnostics.yaml
      practice_items.yaml
      audit_queue.md
      projects/
        tiny_attention_router.md
src/torchbloom/
  kg_validate.py
tests/
  test_kg_validate.py
```

Modify:

```text
docs/README.md
pyproject.toml
```

## Commit Boundary 1: Source Inventory And Contract

### Task 1: Create The Pilot Directory Contract

- [ ] Create `knowledge_graph/README.md` explaining the artifact boundary: curriculum graph data only, no app code.
- [ ] Create `knowledge_graph/pilots/udl-ch12-transformers/README.md` with pilot goal, scope, source anchors, non-goals, and review status.
- [ ] Add `audit_queue.md` for uncertain mappings, missing source anchors, and advanced routes.

### Task 2: Inventory UDL Chapter 12

- [ ] Read `raw/udl/textbook/pages/ch12-transformers/page_0207.md` through `page_0239.md`.
- [ ] Create `source_inventory.yaml` with one entry per section, equation family, figure family, and end-of-chapter problem group.
- [ ] Mark each inventory entry as `core`, `extension`, or `advanced`.
- [ ] Anchor each entry to local page files rather than copying source text.

Expected core inventory:

- text-data motivation
- dot-product self-attention
- values, queries, keys
- attention weights
- matrix self-attention
- scaling
- multiple heads
- transformer layer
- masked attention
- tiny decoder/generation

Expected extension inventory:

- positional encoding
- BERT-style encoder tasks
- cross-attention
- long-sequence variants
- vision transformers

Expected advanced inventory:

- permutation equivariance proof
- softmax derivative analysis
- efficient attention derivations

### Task 3: Define The Data Schema In Documentation First

- [ ] Add schema notes to the pilot README for `nodes.yaml`, `edges.yaml`, `little_paths.yaml`, `diagnostics.yaml`, and `practice_items.yaml`.
- [ ] Include a short valid example for each file.
- [ ] Define allowed `track`, `kind`, `confidence`, and `mastery_evidence` values.

Do not write validation code until the human-readable contract is clear.

## Commit Boundary 2: Validator And Tests

### Task 4: Add A Minimal Graph Validator

- [ ] Create `src/torchbloom/kg_validate.py`.
- [ ] Add a CLI command that validates one pilot directory.
- [ ] Validate YAML parseability.
- [ ] Validate required fields for nodes.
- [ ] Validate edge endpoints exist.
- [ ] Validate prerequisite edges have no obvious cycles.
- [ ] Validate every `source_anchor` local path exists.
- [ ] Validate every core transformer node has at least one `mastery_evidence` entry.
- [ ] Validate every core transformer node has either a Little path or an explicit reason it is covered inside another path.

Suggested command:

```bash
python -m torchbloom.kg_validate knowledge_graph/pilots/udl-ch12-transformers
```

### Task 5: Add Focused Validator Tests

- [ ] Create `tests/test_kg_validate.py`.
- [ ] Test that a tiny valid pilot passes.
- [ ] Test that a missing node endpoint fails.
- [ ] Test that a missing source anchor fails.
- [ ] Test that a prerequisite cycle fails.
- [ ] Test that a core node without mastery evidence fails.

### Task 6: Add CLI Entry Point If Needed

- [ ] If the project uses console scripts for internal tools, add `torchbloom-kg-validate` to `pyproject.toml`.
- [ ] Keep `python -m torchbloom.kg_validate ...` working even if no console script is added.

## Commit Boundary 3: Seed Graph

### Task 7: Create Core Transformer Nodes

- [ ] Create `nodes.yaml` with the core target path.
- [ ] Add transformer nodes for:
  - tokens in sequence
  - token vectors
  - dot-product match score
  - attention score
  - softmax attention distribution
  - weighted value mixture
  - value projection
  - query projection
  - key projection
  - self-attention output
  - attention matrix
  - scaled dot-product attention
  - multi-head attention
  - residual update
  - layer normalization intuition
  - token-wise MLP
  - transformer layer
  - autoregressive prediction
  - masked attention
  - tiny masked decoder

### Task 8: Create Math And Probability Prerequisite Nodes

- [ ] Add nodes for weighted averages, normalization, probability distributions, exponents, square roots, vectors, dot products, matrices, and shape reasoning.
- [ ] Keep prerequisites fine-grained enough that repair paths can target the actual gap.
- [ ] Mark prerequisite-synthesis nodes clearly when they are not directly sourced from Chapter 12.

### Task 9: Create Coding Prerequisite Nodes

- [ ] Add nodes for Python functions, lists, nested lists, loops, indexing, dictionaries, pure vector operations, matrix-shaped data, simple tests, and masking.
- [ ] Include mastery evidence that can be checked with short coding tasks.

### Task 10: Create Edges

- [ ] Create `edges.yaml` using typed edges:
  - `prerequisite`
  - `review_after`
  - `repair_to`
  - `extension_to`
- [ ] Make prerequisite edges acyclic.
- [ ] Link extension routes from the core path rather than forcing them into the first pass.

## Commit Boundary 4: Little-Style Authored Paths

### Task 11: Author Core Concept Paths

- [ ] Create `little_paths.yaml`.
- [ ] Add authored paths for:
  - clues to attention
  - matching to dot product
  - scores to softmax
  - one view to values/queries/keys
  - rows and columns to attention matrix
  - single head to multi-head
  - seeing all tokens to masked attention
  - attention block to transformer layer

Each path should include:

- concrete setup
- first learner action
- expected misconception
- next prompt
- representation shift
- formal name introduction
- mastery check

### Task 12: Make Sequencing Explicit

- [ ] For each authored path, record why each frame comes next.
- [ ] Avoid relying on tone alone. The Little-series influence should appear as strategic ordering, not just a dialogue format.
- [ ] Include at least one "wrong but useful" learner move per hard concept.

## Commit Boundary 5: Diagnostics And Practice

### Task 13: Author Diagnostic Items

- [ ] Create `diagnostics.yaml`.
- [ ] Add 15 to 18 diagnostic items covering arithmetic/fractions, vectors/tables, coding, probability/normalization, attention intuition, and explanation.
- [ ] Map each diagnostic result to a repair path or ready path.
- [ ] Include misconception-aware distractors.

### Task 14: Author Practice Items

- [ ] Create `practice_items.yaml`.
- [ ] Add practice types:
  - compute
  - shape
  - explain
  - debug
  - predict
  - compare
  - transfer
- [ ] Map UDL problems 12.1, 12.2, 12.4, 12.5, and 12.7 into reachable practice.
- [ ] Mark UDL problems 12.3 and 12.10 as advanced routes.

### Task 15: Define Mastery Evidence

- [ ] For every core target node, define at least two mastery signals.
- [ ] Require at least one non-multiple-choice signal for hard concepts.
- [ ] Include review tags so future spaced review can revisit dot product, softmax, masking, and shape reasoning.

## Commit Boundary 6: Project Blueprint

### Task 16: Author Tiny Attention Router

- [ ] Create `projects/tiny_attention_router.md`.
- [ ] Design the project in plain Python lists first.
- [ ] Include project stages:
  1. tokenize a tiny sentence,
  2. create small token vectors,
  3. compute values, queries, and keys,
  4. compute attention scores,
  5. apply softmax,
  6. compute weighted value mixtures,
  7. inspect attention rows,
  8. add a future-token mask,
  9. generate one next-token choice from a toy vocabulary.
- [ ] Include expected learner explanations after key stages.
- [ ] Add optional follow-up versions for NumPy and PyTorch without making them required.

### Task 17: Add Project Rubric

- [ ] Define correctness checks.
- [ ] Define explanation checks.
- [ ] Define debugging checks.
- [ ] Define extension checks for advanced learners.

## Commit Boundary 7: Verification And Documentation

### Task 18: Run Validation

- [ ] Run unit tests.
- [ ] Run the graph validator against the pilot directory.
- [ ] Fix every missing anchor, missing edge endpoint, invalid enum, and missing mastery signal.

Commands:

```bash
python -m pytest tests/test_kg_validate.py
python -m torchbloom.kg_validate knowledge_graph/pilots/udl-ch12-transformers
```

### Task 19: Update Documentation Indexes

- [ ] Update `docs/README.md` with the accepted design and plan.
- [ ] Update `knowledge_graph/README.md` after the pilot artifacts exist.
- [ ] Record what remains uncertain in `audit_queue.md`.

### Task 20: Final Review

- [ ] Confirm web app code still consumes an explicit course contract rather than burying all curriculum logic inside JSX.
- [ ] Confirm the graph is source-grounded and not a free-floating LLM synthesis.
- [ ] Confirm the authored paths include strategic "when and next" sequencing.
- [ ] Confirm practice includes math, code, explanation, and transfer.
- [ ] Confirm the Transformer chapter is represented as a chapter, even though only the core route is deeply authored in the first pass.

## Acceptance Criteria

- [ ] `source_inventory.yaml` covers all major UDL Chapter 12 sections.
- [ ] `nodes.yaml` contains the core Transformer path plus math, probability, coding, and ML prerequisites.
- [ ] `edges.yaml` validates with no missing endpoints or prerequisite cycles.
- [ ] `little_paths.yaml` includes authored paths for the hard core concepts.
- [ ] `diagnostics.yaml` places learners into repair or ready paths.
- [ ] `practice_items.yaml` includes misconception-aware math, coding, explanation, and transfer tasks.
- [ ] `projects/tiny_attention_router.md` gives a from-scratch path to self-attention and masked attention using plain Python lists.
- [ ] The validator and tests pass.
- [ ] The docs make clear why this pilot uses Chapter 12 instead of UDL Chapters 1-3.
