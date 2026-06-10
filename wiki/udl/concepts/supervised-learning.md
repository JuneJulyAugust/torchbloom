---
id: supervised-learning
type: concept
title: Supervised Learning
chapter_scope: [ch02]
source_anchors:
  - source: udlbook-v5.0.3
    locator: raw/udl/textbook/pages/ch02-supervised-learning/page_0017.md
confidence: directional
prerequisites: [functions-as-machines, vectors-as-lists-of-numbers]
related: [linear-regression, loss-functions, model-training]
learning_objectives:
  - Explain supervised learning as learning a parameterized map from inputs to targets.
---

# Supervised Learning

## Core Idea

Supervised learning starts with examples where both the input and correct output
are known. The goal is to learn a model that predicts outputs for new inputs.

## Why It Matters In UDL

Chapter 2 introduces nearly every moving part that later chapters reuse: model,
parameters, training data, loss, fitting, and testing.

## High-School Bridge

Imagine drawing a line through points on graph paper. The points are examples,
the line is the model, and changing the line's slope or intercept changes the
predictions.

## Formal Version

UDL writes a supervised model as a function with parameters, such as
`y = f[x, phi]`. Training chooses `phi` so predictions match training outputs as
closely as possible.

## Practice Hooks

- ch02-q01
- ch02-q02
- ch02-q03

## Source Anchors

- `raw/udl/textbook/pages/ch02-supervised-learning/page_0017.md`
- `raw/udl/textbook/pages/ch02-supervised-learning/page_0022.md`

