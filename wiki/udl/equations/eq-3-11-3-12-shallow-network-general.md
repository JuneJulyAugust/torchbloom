---
id: eq-3-11-3-12-shallow-network-general
type: equation
title: "Equations 3.11-3.12: General Shallow Network"
chapter_scope: [ch03]
source_anchors:
  - source: udlbook-v5.0.3
    locator: raw/udl/textbook/pages/ch03-shallow-neural-networks/page_0047.md
  - source: udlbook-v5.0.3
    locator: raw/udl/textbook/pages/ch03-shallow-neural-networks/page_0049.md
confidence: directional
prerequisites: [vectors-as-lists-of-numbers, hidden-units, relu-activation]
related: [shallow-neural-networks, linear-regions]
learning_objectives:
  - Generalize the one-input shallow network to multiple inputs, hidden units, and outputs.
---

# Equations 3.11-3.12: General Shallow Network

## Equation

For hidden unit `d`:

`h_d = a[theta_d0 + sum_i theta_di x_i]`

For output `j`:

`y_j = phi_j0 + sum_d phi_jd h_d`

## Symbols

- `x_i`: input coordinate `i`.
- `h_d`: hidden unit `d`.
- `y_j`: output coordinate `j`.
- `theta`: parameters from input to hidden units.
- `phi`: parameters from hidden units to outputs.

## Intuition

Each hidden unit draws a boundary in input space and clips one side. The output
layer combines all hidden-unit activations into each prediction.

## Practice Hooks

- ch03-q11
- ch03-q12
- ch03-q14
- ch03-q16

## Source Anchors

- `raw/udl/textbook/pages/ch03-shallow-neural-networks/page_0047.md`
- `raw/udl/textbook/pages/ch03-shallow-neural-networks/page_0049.md`
