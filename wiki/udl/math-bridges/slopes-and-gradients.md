---
id: slopes-and-gradients
type: math-bridge
title: Slopes And Gradients
chapter_scope: [ch02, ch03]
source_anchors:
  - source: udlbook-v5.0.3
    locator: raw/udl/textbook/pages/ch02-supervised-learning/page_0022.md
confidence: directional
prerequisites: [coordinates-and-graphs]
related: [eq-2-5-least-squares-loss, model-training]
learning_objectives:
  - Explain a gradient as the collection of one-parameter-at-a-time slopes.
---

# Slopes And Gradients

## Core Idea

A slope tells you how fast one quantity changes when another quantity moves.
A gradient collects several slopes, one for each parameter.

## High-School Bridge

On a line, positive slope goes up as `x` increases and negative slope goes down.
On a loss surface, each parameter direction has its own slope. Training uses
these slopes to find a direction that lowers loss.

## Ready For UDL When

- You can explain slope as "change in output divided by change in input."
- You can imagine taking a slope with respect to one parameter while holding the others fixed.
- You can say why walking opposite the uphill direction lowers a surface.

## Source Anchors

- `raw/udl/textbook/pages/ch02-supervised-learning/page_0022.md`
- `raw/udl/textbook/pages/ch02-supervised-learning/page_0024.md`
