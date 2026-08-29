# Transformer Chapter Knowledge Graph Pilot Design

**Date:** 2026-06-11
**Status:** Draft for review; web-app non-goal superseded by `2026-06-11-transformer-web-mvp-design.md`
**Scope:** *Understanding Deep Learning* Chapter 12, "Transformers"

## Purpose

Design the next TorchBloom pilot around the Transformer chapter rather than the first three UDL chapters.

The reason is strategic: *The Little Learner* already gives us a strong model for shallow and deep fully connected networks. TorchBloom should not spend its first curriculum-graph pilot duplicating that path. Instead, Chapter 12 is a better north-star target because it forces the system to answer the harder curriculum question:

How can a learner move from math, probability, and coding foundations toward a real transformer chapter without turning the chapter into a shallow demo?

This pilot should produce a source-grounded knowledge graph, authored Little-style concept paths, diagnostic tasks, practice items, and a small coding project. It should not yet produce a production learning app.

Later on 2026-06-11, the user explicitly asked to build the learner-facing web system as the MVP. The curriculum-first parts of this design still apply; the "no learner app" constraint no longer applies.

## Core Decision

Use UDL Chapter 12 as the pilot chapter target.

Do not use Chapters 1-3 as the pilot target. Those chapters remain useful source anchors, but the learning design should build backward from transformers:

- What math must the learner know before attention makes sense?
- What probability and normalization ideas must be fluent before softmax is meaningful?
- What coding skills are required before attention can be implemented from scratch?
- Which ideas should be experienced concretely before formulas appear?
- Which ideas require a carefully authored "next frame" sequence rather than a graph edge alone?

## Working Thesis

TorchBloom needs three curriculum layers, not just an LLM wiki.

| Layer | Role | Inspired By |
| --- | --- | --- |
| Source wiki | A grounded evidence layer that records what the book says and where. | UDL companion work |
| Knowledge graph | A prerequisite, mastery, review, and placement layer. | Math Academy |
| Authored paths | Strategic frame-by-frame concept development inside hard ideas. | Little-series books |

The wiki is necessary, but it is not sufficient. A wiki answers "what is in the source?" A learning system must also answer "what should this learner see next, why, and how do we know they are ready?"

## Source Anchors

The pilot uses local UDL Chapter 12 Markdown as the primary source layer:

- `raw/udl/textbook/pages/ch12-transformers/page_0207.md` - chapter opening and text-data motivation
- `raw/udl/textbook/pages/ch12-transformers/page_0208.md` - dot-product self-attention motivation and first value-weighting setup
- `raw/udl/textbook/pages/ch12-transformers/page_0209.md` - computing and weighting values
- `raw/udl/textbook/pages/ch12-transformers/page_0210.md` - queries, keys, and attention weights
- `raw/udl/textbook/pages/ch12-transformers/page_0211.md` - self-attention summary
- `raw/udl/textbook/pages/ch12-transformers/page_0213.md` - matrix form and positional encoding
- `raw/udl/textbook/pages/ch12-transformers/page_0214.md` - scaled dot-product attention and multiple heads
- `raw/udl/textbook/pages/ch12-transformers/page_0215.md` - multi-head attention and transformer layers
- `raw/udl/textbook/pages/ch12-transformers/page_0216.md` - transformer layer structure
- `raw/udl/textbook/pages/ch12-transformers/page_0222.md` - decoder model and autoregressive language modeling
- `raw/udl/textbook/pages/ch12-transformers/page_0223.md` - masked self-attention and generation
- `raw/udl/textbook/pages/ch12-transformers/page_0227.md` - encoder-decoder and long-sequence bridge
- `raw/udl/textbook/pages/ch12-transformers/page_0228.md` - transformer variants for longer sequences and images
- `raw/udl/textbook/pages/ch12-transformers/page_0239.md` - end-of-chapter problems

Pedagogy research anchors:

- `docs/math-academy-research.md` - adaptive graph, task selection, mastery, diagnostics, and practice evidence
- `docs/little-series-research.md` - authored sequencing, "when and next" strategy, and Little-style concept development

## Pilot Scope

The pilot is chapter-level, but the first pass should not try to teach every Chapter 12 subsection with equal depth.

### Full Chapter Inventory

Represent the whole chapter in the graph so the system knows the chapter shape:

- processing text data
- dot-product self-attention
- values, queries, keys, and attention weights
- matrix self-attention
- positional encoding
- scaled dot-product attention
- multi-head attention
- transformer layer blocks
- encoder tasks and BERT-style pretraining
- decoder tasks, autoregressive modeling, masked attention, and generation
- encoder-decoder cross-attention
- long-sequence transformer variants
- image transformers
- advanced end-of-chapter problems

### Deep Authored Pilot

Fully author the first deep route through:

1. Tokens as items in a sequence
2. Vectors as small lists of features
3. Dot product as a match score
4. Softmax as turning scores into attention shares
5. Weighted average as information mixing
6. Values, queries, and keys as three learned views of each token
7. Self-attention as learned routing among tokens
8. Scaling as a way to keep scores numerically tame
9. Multiple heads as multiple routing systems in parallel
10. A transformer layer as attention plus token-wise processing plus residual shape preservation
11. Masked attention as preventing a decoder from looking ahead
12. A tiny next-token decoder project

### Light First-Pass Coverage

Create graph nodes and source cards, but defer deep authored practice for:

- BERT-style pretraining tasks
- cross-attention
- long-sequence efficient attention
- vision transformers
- proof-heavy permutation equivariance
- kernelized or linear attention derivations

These areas become stretch routes after the core path works.

## Non-Goals

This pilot should not:

- build a production learner app,
- create a polished UI,
- train a real GPT-scale model,
- require PyTorch before the learner has implemented attention manually,
- duplicate *The Little Learner*'s shallow and deep fully connected network path,
- turn Chapter 12 into a plain wiki summary,
- treat LLM-generated explanations as source truth,
- cover every Chapter 12 advanced subsection with full practice depth in the first pass.

## Learning Architecture

### Layer 1: Source-Grounded Chapter Map

This layer answers:

- What does UDL Chapter 12 contain?
- Which source pages support each idea?
- Which equations, figures, and problems belong to each idea?
- What is uncertain or needs review?

The chapter map is not a lesson. It is the evidence backbone for the graph and authored paths.

### Layer 2: Knowledge Graph

This layer answers:

- Which concepts are prerequisites?
- Which concepts should be reviewed before and after attention?
- Which diagnostic items place a learner into the graph?
- Which task results update mastery?
- Which nodes can be skipped, repaired, or accelerated?

The graph should be fine-grained enough that "does not understand softmax" becomes actionable. It should not collapse all prerequisites into a vague "linear algebra" bucket.

### Layer 3: Authored Little-Style Paths

This layer answers:

- What should the learner see next inside a hard concept?
- Which example should appear before the symbol?
- Which wrong idea should be surfaced deliberately?
- When should a definition appear?
- When should the learner switch from words to tables, from tables to code, and from code to formulas?

This is where the Little-series influence matters most. It is not just a friendly voice. It is a carefully sequenced path through a concept.

### Layer 4: Practice, Review, And Transfer

This layer answers:

- Can the learner compute the idea?
- Can they explain it?
- Can they debug code that uses it?
- Can they use it in a new setting?
- Can they still use it later?

Practice must include math, coding, and explanation, not only multiple choice.

## Backward Graph From Transformers

The graph should be built backward from a target node:

`udl.ch12.tiny_masked_decoder`

That target depends on the following concept families.

### Math Prerequisites

- whole-number arithmetic and order of operations
- fractions, ratios, and "parts of a whole"
- weighted averages
- negative numbers
- exponents as repeated growth
- square roots as scale measures
- variables and functions
- lists of numbers as vectors
- tables of numbers as matrices
- dot product as pairwise multiply-and-add
- matrix multiplication as many dot products
- probability distributions as nonnegative values that sum to one
- normalization
- softmax as exponential normalization
- shape reasoning with rows, columns, tokens, and features
- permutation and order awareness
- optional advanced route: equivariance and proof structure

### Coding Prerequisites

- Python expressions, variables, and functions
- lists and nested lists
- loops and list comprehensions
- indexing and slicing
- dictionaries for token lookup
- writing small pure functions
- testing outputs against expected values
- simple vector operations from scratch
- table-shaped data
- masking values before normalization
- reading and debugging small numerical programs
- optional later route: NumPy arrays and PyTorch tensors

### Machine Learning Prerequisites

- learned parameters as numbers a model adjusts
- embeddings as learned token vectors
- linear transforms as learned projections
- logits as unnormalized scores
- probability over next choices
- residual addition as preserving and updating a representation
- layer normalization as stabilizing a representation
- token-wise MLP as the fully connected network reused at each position
- autoregressive prediction as one-step-ahead modeling

## Core Concept Paths

Each hard concept needs a Little-style path, not just a node.

### Path A: From Clues To Attention

1. A sentence has several words, but one word may answer the current question better than another.
2. The learner assigns hand-made clue shares that sum to one.
3. The learner mixes small "meaning cards" using those shares.
4. The learner notices that a new output can be made from old tokens without choosing only one token.
5. The formal name "attention weights" is introduced after the learner has used the idea.

### Path B: From Matching To Dot Product

1. Compare two short feature lists by checking feature-by-feature agreement.
2. Multiply matching feature strengths and add them.
3. Show that bigger aligned features create a bigger score.
4. Contrast with a misleading score from a single feature.
5. Name the dot product as a match score.

### Path C: From Scores To Softmax

1. Begin with raw scores that are not shares.
2. Show why negative scores or large scores cannot be used directly as attention shares.
3. Convert scores to positive amounts.
4. Normalize so the amounts sum to one.
5. Compare gentle scores with one very large score.
6. Connect the behavior to Chapter 12's softmax-gradient problem.

### Path D: From One View To Q/K/V

1. A token can carry content, ask a question, and offer an address.
2. Values are the content to mix.
3. Queries are what the current position is looking for.
4. Keys are what each source position offers for matching.
5. A query-key match chooses how much of each value to use.
6. The learner computes a tiny example by hand, then in code.

### Path E: From Seeing All Tokens To Masked Attention

1. In a next-token game, seeing the future makes the task fake.
2. Mark future positions as forbidden.
3. Replace forbidden scores with a value that softmax treats as zero share.
4. Compute attention one position at a time.
5. Use the result to choose a next token in a tiny decoder.

## Practice Design

Question design should use the evidence from the Math Academy research: short tasks, high signal, immediate feedback, and misconceptions encoded into answer choices.

Practice types:

- **Compute:** calculate a dot product, normalize shares, compute a weighted average.
- **Shape:** identify the dimensions of values, queries, keys, attention weights, and outputs.
- **Explain:** describe what an attention row means in ordinary language.
- **Debug:** find the error in a small attention function.
- **Predict:** decide what happens when one score becomes much larger than the others.
- **Compare:** explain why a fully connected layer cannot directly handle arbitrary sequence length in the same way.
- **Transfer:** use the same attention idea for pixels, clues in a puzzle, or neighbors in a data table.
- **Proof route:** for advanced learners, reason about permutation equivariance after concrete examples.

Distractors should represent real misunderstandings:

- attention weights are the same as values,
- query and key are interchangeable in all contexts,
- softmax simply divides by the sum of raw scores,
- a larger vector dimension always means better attention,
- masking deletes tokens rather than zeroing their attention share,
- multi-head attention means applying the same head repeatedly,
- positional encoding is unnecessary because token order is always visible.

## Diagnostic Design

The pilot diagnostic should be short enough to use before the Transformer chapter path:

- 3 arithmetic and fraction items
- 3 vector/table items
- 3 coding-reading items
- 3 probability/normalization items
- 3 attention-intuition items
- 2 explanation items

The output should not be a score only. It should place the learner into repair paths:

- weighted average repair
- dot product repair
- softmax repair
- Python nested-list repair
- token/vector representation repair
- ready for self-attention path

## Pilot Project

The first project should be:

**Tiny Attention Router**

Learner builds attention from scratch using short lists and tables:

1. tokenize a tiny sentence,
2. assign or load small hand-made token vectors,
3. compute values, queries, and keys using small fixed matrices,
4. compute query-key scores,
5. apply softmax,
6. mix values with attention weights,
7. inspect which tokens influenced each output,
8. add a mask,
9. generate one next-token choice from a toy vocabulary.

The first version should use plain Python lists. A second version may use NumPy. PyTorch should come later as a bridge, not as the first explanation.

## Chapter 12 Problem Mapping

The end-of-chapter problems should guide practice depth:

| UDL Problem | Pilot Use |
| --- | --- |
| 12.1 | Count parameters and attention weights after shape fluency is built. |
| 12.2 | Explain why self-attention preserves sequence shape. |
| 12.3 | Advanced optional proof route for permutation equivariance. |
| 12.4 | Softmax behavior and gradient intuition route. |
| 12.5 | Multi-head shape and computation route. |
| 12.6 | Later BERT pretraining extension. |
| 12.7 | Masked attention and efficient generation extension. |
| 12.8-12.9 | Later vision-transformer computation extension. |
| 12.10 | Advanced efficient-attention derivation route. |

## Artifact Model

The pilot should eventually create these curriculum artifacts:

```text
knowledge_graph/pilots/udl-ch12-transformers/
  README.md
  source_inventory.yaml
  nodes.yaml
  edges.yaml
  little_paths.yaml
  diagnostics.yaml
  practice_items.yaml
  projects/
    tiny_attention_router.md
  audit_queue.md
```

No app code should consume these artifacts until the files are stable and validated.

## Node Contract

Each graph node should record:

- `id`
- `title`
- `track`
- `stage`
- `kind`
- `source_anchors`
- `prerequisites`
- `mastery_evidence`
- `repair_paths`
- `review_tags`
- `confidence`

Tracks should include:

- `math`
- `probability`
- `coding`
- `ml`
- `transformers`
- `explanation`

Kinds should include:

- `concept`
- `skill`
- `procedure`
- `practice`
- `diagnostic`
- `project`
- `extension`

## Quality Bar

The pilot is useful when:

- the whole Transformer chapter has a source inventory,
- the core self-attention-to-masked-decoder path has graph nodes, edges, authored paths, diagnostics, and practice,
- every target node has source anchors or is clearly marked as a prerequisite synthesis,
- every hard concept has at least one Little-style authored path,
- every diagnostic result maps to a repair path or next path,
- practice includes math, code, explanation, and transfer,
- the tiny project can be completed from plain Python lists before NumPy or PyTorch,
- graph edges can be validated for missing nodes and obvious cycles,
- the plan distinguishes core pilot work from later extension routes.

## Risks

- **Too much chapter coverage:** Trying to fully teach all of Chapter 12 in the first pass could flatten the design.
- **Too little chapter coverage:** Only teaching attention would lose the chapter-level target. The inventory prevents that.
- **Wiki drift:** A source wiki can become a parallel product. It should remain evidence and source grounding.
- **Graph without path:** A prerequisite graph does not by itself teach a hard idea. Little-style authored paths are required.
- **Path without mastery:** A beautiful lesson can still fail if the learner's prerequisite gaps are hidden. Diagnostics and repair paths are required.
- **Coding too late:** Attention becomes abstract if the learner never implements it. The project must be part of the pilot, not an afterthought.

## Open Questions

- How young is the first intended pilot learner for the Transformer path: older motivated student, parent-guided younger learner, or both?
- Should the first coding project use a browser notebook, a plain Python file, or both?
- Should graph mastery be stored as authoring metadata only, or should we prototype a minimal mastery-state simulator?
- How much of positional encoding belongs in the core pilot versus the first extension route?
