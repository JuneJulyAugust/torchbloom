---
id: eq-3-2-relu
type: equation
title: "Equation 3.2: ReLU"
chapter_scope: [ch03]
source_anchors:
  - source: udlbook-v5.0.3
    locator: raw/udl/textbook/pages/ch03-shallow-neural-networks/page_0025.md
confidence: directional
prerequisites: [piecewise-linear-functions]
related: [relu-activation, hidden-units]
learning_objectives:
  - Explain ReLU as a piecewise function with a zero region and pass-through region.
---

# Equation 3.2: ReLU

## Equation

`ReLU[z] = 0 if z < 0, and ReLU[z] = z if z >= 0`

## Symbols

- `z`: the input to the activation function.
- `ReLU[z]`: the clipped output.

## Intuition

Negative values are clipped to zero. Nonnegative values pass through unchanged.

## Practice Hooks

- ch03-q01
- ch03-q05
- ch03-q06
- ch03-q08

## Source Anchors

- `raw/udl/textbook/pages/ch03-shallow-neural-networks/page_0025.md`
