---
id: eq-3-1-shallow-network-example
type: equation
title: "Equation 3.1: One-Input Shallow Network"
chapter_scope: [ch03]
source_anchors:
  - source: udlbook-v5.0.3
    locator: raw/udl/textbook/pages/ch03-shallow-neural-networks/page_0039.md
confidence: directional
prerequisites: [linear-regression, relu-activation, hidden-units]
related: [shallow-neural-networks, piecewise-linear-functions]
learning_objectives:
  - Decompose the example shallow network into hidden-unit computations and output weights.
---

# Equation 3.1: One-Input Shallow Network

## Equation

`y = phi_0 + phi_1 a[theta_10 + theta_11 x] + phi_2 a[theta_20 + theta_21 x] + phi_3 a[theta_30 + theta_31 x]`

## Symbols

- `x`: scalar input.
- `a[...]`: activation function.
- `theta_d0`, `theta_d1`: intercept and slope feeding hidden unit `d`.
- `phi_d`: output weight applied to hidden unit `d`.
- `phi_0`: output offset.

## Intuition

The network makes three clipped lines, scales them, adds them, and shifts the
result up or down.

## Practice Hooks

- ch03-q01
- ch03-q03
- ch03-q07

## Source Anchors

- `raw/udl/textbook/pages/ch03-shallow-neural-networks/page_0039.md`
