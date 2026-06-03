---
id: relu-activation
type: concept
title: ReLU Activation
chapter_scope: [ch03]
source_anchors:
  - source: udlbook-v5.0.3
    locator: raw/udl/textbook/pages/ch03-shallow-neural-networks/page_0039.md
confidence: directional
prerequisites: [piecewise-linear-functions]
related: [hidden-units, shallow-neural-networks, eq-3-2-relu]
learning_objectives:
  - Explain ReLU as a function that clips negative values and passes positive values through.
---

# ReLU Activation

## Core Idea

ReLU returns zero for negative inputs and returns the input itself for positive
inputs.

## Why It Matters In UDL

The ReLU is what makes the Chapter 3 network nonlinear. Without a nonlinear
activation, stacking linear operations would still produce a linear mapping.

## High-School Bridge

Draw a line. Now erase the part below the x-axis and replace it with zero. That
clipped line is the shape a ReLU hidden unit contributes.

## Practice Hooks

- ch03-q01
- ch03-q05
- ch03-q08

## Source Anchors

- `raw/udl/textbook/pages/ch03-shallow-neural-networks/page_0039.md`
- `raw/udl/textbook/pages/ch03-shallow-neural-networks/page_0040.md`
