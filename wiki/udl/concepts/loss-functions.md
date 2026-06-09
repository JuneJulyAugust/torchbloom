---
id: loss-functions
type: concept
title: Loss Functions
chapter_scope: [ch02, ch03]
source_anchors:
  - source: udlbook-v5.0.3
    locator: raw/udl/textbook/pages/ch02-supervised-learning/page_0019.md
confidence: directional
prerequisites: [coordinates-and-graphs]
related: [eq-2-5-least-squares-loss, model-training]
learning_objectives:
  - Explain loss as a number that measures prediction mismatch.
---

# Loss Functions

## Core Idea

A loss function converts bad predictions into a number. Smaller loss means the
model matches the training examples better.

## Why It Matters In UDL

Training needs a target to optimize. In Chapter 2, the target is least-squares
loss for a line; in later chapters, the same idea drives neural-network fitting.

## High-School Bridge

If a predicted point is far from the true point, the error is large. Squaring
errors makes all errors positive and makes large misses especially expensive.

## Practice Hooks

- ch02-q01
- ch02-q02
- ch03-q07

## Source Anchors

- `raw/udl/textbook/pages/ch02-supervised-learning/page_0019.md`
- `raw/udl/textbook/pages/ch02-supervised-learning/page_0021.md`
