---
id: eq-2-5-least-squares-loss
type: equation
title: "Equation 2.5: Least-Squares Loss"
chapter_scope: [ch02, ch03]
source_anchors:
  - source: udlbook-v5.0.3
    locator: raw/udl/textbook/pages/ch02-supervised-learning/page_0033.md
confidence: directional
prerequisites: [linear-regression, coordinates-and-graphs]
related: [loss-functions, model-training]
learning_objectives:
  - Explain least-squares loss as the sum of squared prediction errors.
---

# Equation 2.5: Least-Squares Loss

## Equation

`L[phi] = sum_i (f[x_i, phi] - y_i)^2`

For 1D linear regression, `f[x_i, phi]` becomes `phi_0 + phi_1 x_i`.

## Symbols

- `x_i`: the input for training example `i`.
- `y_i`: the observed output for training example `i`.
- `f[x_i, phi]`: the model prediction.
- `L[phi]`: the total mismatch for the chosen parameters.

## Intuition

Each prediction error is squared, then all squared errors are added. A line with
smaller total squared error fits the training data better.

## Practice Hooks

- ch02-q01
- ch02-q02
- ch03-q07

## Source Anchors

- `raw/udl/textbook/pages/ch02-supervised-learning/page_0033.md`
- `raw/udl/textbook/pages/ch02-supervised-learning/page_0035.md`
