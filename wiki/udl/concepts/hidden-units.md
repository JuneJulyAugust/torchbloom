---
id: hidden-units
type: concept
title: Hidden Units
chapter_scope: [ch03]
source_anchors:
  - source: udlbook-v5.0.3
    locator: raw/udl/textbook/pages/ch03-shallow-neural-networks/page_0041.md
confidence: directional
prerequisites: [relu-activation, linear-regression]
related: [shallow-neural-networks, linear-regions]
learning_objectives:
  - Explain a hidden unit as a pre-activation followed by an activation.
---

# Hidden Units

## Core Idea

A hidden unit computes a simple function of the input and then applies an
activation function. In Chapter 3, each hidden unit is a line clipped by ReLU.

## Why It Matters In UDL

Each hidden unit can create a joint in the final function. More hidden units
give the network more places where the slope can change.

## High-School Bridge

One hidden unit is not mysterious: it is a line plus a clipping rule. The
network becomes interesting when several clipped lines are added together.

## Practice Hooks

- ch03-q02
- ch03-q03
- ch03-q10

## Source Anchors

- `raw/udl/textbook/pages/ch03-shallow-neural-networks/page_0041.md`
- `raw/udl/textbook/pages/ch03-shallow-neural-networks/page_0042.md`

