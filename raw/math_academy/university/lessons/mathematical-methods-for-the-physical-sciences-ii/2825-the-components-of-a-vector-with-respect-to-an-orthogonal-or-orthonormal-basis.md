# The Components of a Vector with Respect to an Orthogonal or Orthonormal Basis

Source: https://www.mathacademy.com/topics/2825?courseId=155
Topic ID: 2825

## Prerequisites

- [Writing Vectors in Different Bases](../linear-algebra/1865-writing-vectors-in-different-bases.md)
- [Orthogonal Sets in Euclidean Spaces](./2103-orthogonal-sets-in-euclidean-spaces.md)
- [Projecting Vectors Onto One-Dimensional Subspaces](./2122-projecting-vectors-onto-one-dimensional-subspaces.md)

## Lesson

### Introduction

Given an orthogonal basis $\mathcal{B}=\{\mathbf{q}_1, \mathbf{q}_2, \ldots, \mathbf{q}_n\}$ of $S=\text{Span}\{\mathcal{B}\},$ there is an easy way to find the components of a vector $\mathbf{x}\in S$ with respect to this basis. The vector $\mathbf{x}$ with respect to the basis $\mathcal{B}$ is

$$


\begin{aligned}𝑥_{1} \\ 𝑥_{2} \\ ⋮ \\ 𝑥_{𝑛}\end{aligned}


$$

Furthermore, if the basis is *orthonormal*, then we know that $\mathbf{q}_i\cdot\mathbf{q}_i=1$. So, the formula for each component is

$$


\begin{aligned}𝑥_{1} \\ 𝑥_{2} \\ ⋮ \\ 𝑥_{𝑛}\end{aligned}


$$

### Example: Finding a Component of a Vector With Respect to a Given Orthogonal Basis

#### Question

Given the orthogonal basis $\mathcal{B}$ of $\mathbb{R}^3$ and the vector $\mathbf{x}$ below, find the value of $x_2,$ the second component of $[\mathbf{x}]_{\mathcal{B}}.$

$$


\begin{aligned}2 \\ 2 \\ 1\end{aligned}


$$

#### Explanation

Let's denote the vectors of $\mathcal{B}$ as $\mathbf{q}_1,\, \mathbf{q}_2,\,\mathbf{q}_3.$

Since $\mathcal{B}$ is an orthogonal basis, we have that $\begin{aligned}𝑥_{1} \\ 𝑥_{2} \\ 𝑥_{3}\end{aligned}$ where $x_i = \dfrac{\mathbf{x} \cdot \mathbf{q}_i}{\mathbf{q}_i \cdot \mathbf{q}_i}.$

Computing $x_2,$ we obtain

$$


\begin{aligned}𝑥_{2} & =\frac{𝐱⋅𝐪_{2}}{𝐪_{2}⋅𝐪_{2}} \\ & =\frac{4⋅1+6⋅1+(−2)⋅(−4)}{1^{2}+1^{2}+(−4)^{2}} \\ & =\frac{4+6+8}{1+1+16} \\ & =1.\end{aligned}


$$

### Example: Calculating the Components of a Vector With Respect to a Given Orthonormal Basis

#### Question

Given the **** basis $\begin{aligned}\frac{1}{\sqrt{5}} \\ −\frac{2}{\sqrt{5}}\end{aligned}$ of $\mathbb R^2,$ find $[\mathbf{x}]_{\mathcal{B}}$ if $[\begin{aligned}−2\sqrt{5} \\ 3\sqrt{5}\end{aligned}]$

#### Explanation

Let's denote the vectors of $\mathcal{B}$ as $\mathbf{q}_1,\, \mathbf{q}_2.$

Since $\mathcal{B}$ is an orthonormal basis, we have that $[\begin{aligned}𝑥_{1} \\ 𝑥_{2}\end{aligned}]$ where $x_i = \mathbf{x} \cdot \mathbf{q}_i.$ Computing the components of $\mathbf{x},$ we get the following:

$$


\begin{aligned}𝑥_{1} & =[\begin{matrix}−2\sqrt{5} \\ 3\sqrt{5}\end{matrix}]⋅\begin{matrix}\frac{1}{\sqrt{5}} \\ −\frac{2}{\sqrt{5}}\end{matrix}=−2−6=−8 \\ 𝑥_{2} & =[\begin{matrix}−2\sqrt{5} \\ 3\sqrt{5}\end{matrix}]⋅\begin{matrix}\frac{2}{\sqrt{5}} \\ \frac{1}{\sqrt{5}}\end{matrix}=−4+3=−1\end{aligned}


$$

Therefore, we have

$$


[\begin{aligned}−8 \\ −1\end{aligned}]


$$

### The Orthogonal Decomposition Theorem

Given any vector $\mathbf{x}$ and any subspace $W$ in $\mathbb{R}^n,$ we can always write $\mathbf{x}$ as a sum of a vector from $W$ and a vector from $W^{\perp}.$ This fact is known as the **orthogonal decomposition theorem.** We can state it formally as follows:

*Let $W$ be a subspace of $\mathbb{R}^n.$ Then each $\mathbf{x}\in\mathbb{R}^n$ can be written uniquely in the form where $\mathbf{y} \in W$ and $\mathbf{z} \in W^{\perp}.$*

*Moreover, since $\mathbf y$ is the orthogonal projection of $\mathbf x$ onto the subspace $W,$ if $\{\mathbf{u}_1\,\dots,\mathbf{u}_p\}$ is any orthogonal basis of $W,$ then*

$$


\begin{aligned}𝐲 & =proj_{𝑊}\,𝐱 \\ & =proj_{𝐮_{1}}\,𝐱+proj_{𝐮_{2}}\,𝐱+⋯+proj_{𝐮_{𝑝}}\,𝐱 \\ & =\frac{𝐱⋅𝐮_{1}}{𝐮_{1}⋅𝐮_{1}}𝐮_{𝟏}+\frac{𝐱⋅𝐮_{2}}{𝐮_{2}⋅𝐮_{2}}𝐮_{𝟐}+⋯+\frac{𝐱⋅𝐮_{𝑝}}{𝐮_{𝑝}⋅𝐮_{𝑝}}𝐮_{𝐩}.\end{aligned}


$$
