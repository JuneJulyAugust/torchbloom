# Orthogonal Linear Transformations

Source: https://www.mathacademy.com/topics/4319?courseId=155
Topic ID: 4319

## Prerequisites

- [Orthogonal Matrices](./2105-orthogonal-matrices.md)

## Lesson

### Introduction

A linear transformation $\mathbf{Q}:\mathbb{R}^n \to \mathbb{R}^n$ is an **orthogonal linear transformation** if for any $\mathbf{x}, \mathbf{y} \in \mathbb{R}^n,$ we have that

$$


\mathbf{Q}(\mathbf{x}) \cdot \mathbf{Q}(\mathbf{y}) = \mathbf{x} \cdot \mathbf{y}.


$$

In this case, we say that $\mathbf{Q}$ *preserves the dot product*.

The linear transformation $\mathbf{Q}$ being orthogonal is equivalent to the following:

- The matrix $Q$ of transformation $\mathbf{Q}$ relative to any orthonormal basis (including the standard basis) of $\mathbb{R}^n$ is orthogonal.

- $\| \mathbf{Q}(\mathbf{x}) \| = \| \mathbf{x} \|$. In other words, $\mathbf{Q}$ preserves vector norms.

- If $\mathbf{x} \perp \mathbf{y}$ then $\mathbf{Q}(\mathbf{x}) \perp \mathbf{Q}(\mathbf{y})$ for any $\mathbf{x}, \mathbf{y} \in \mathbb{R}^n.$ In general, $\mathbf{Q}$ preserves the angle between any two vectors.

- $\mathbf{Q}$ maps any orthogonal (orthonormal) set into an orthogonal (orthonormal) set.

### Example: Applying the Angle Preserving Property of Orthogonal Linear Transformations

#### Question

Let $\mathbf{Q}$ be an orthogonal linear transformation. If $\begin{aligned}−1 \\ −2 \\ 2\end{aligned}$ and $\begin{aligned}3 \\ 0 \\ 5\end{aligned}$, find

1. $\Vert \mathbf{Q}(\mathbf{x}) \Vert.$

2. $\mathbf{Q}(\mathbf{x}) \cdot \mathbf{Q}(\mathbf{y}).$

#### Explanation

Since $\mathbf{Q}$ is orthogonal, we have that $\mathbf{Q}(\mathbf{x}) \cdot \mathbf{Q}(\mathbf{y}) = \mathbf{x} \cdot \mathbf{y}$ for any vectors $\mathbf{x}$ and $\mathbf{y}.$

The linear transformation $\mathbf{Q}$ being orthogonal is equivalent to the following:

- The matrix $Q$ of transformation $\mathbf{Q}$ relative to any orthonormal basis (including the standard basis) of $\mathbb{R}^n$ is orthogonal.

- $|| \mathbf{Q}(\mathbf{x}) || = || \mathbf{x} ||.$

- If $\mathbf{x} \perp \mathbf{y}$ then $\mathbf{Q}(\mathbf{x}) \perp \mathbf{Q}(\mathbf{y})$ for any $\mathbf{x}, \mathbf{y} \in \mathbb{R}^n.$ In general, $\mathbf{Q}$ preserves the angle between any two vectors.

- $\mathbf{Q}$ maps any orthogonal (orthonormal) set into an orthogonal (orthonormal) set.

In this case, since $\mathbf{Q}$ is orthogonal, we have

$$


\begin{aligned}‖𝐐(𝐱)‖ & =‖𝐱‖ \\ & =\sqrt{𝑥_{21}+𝑥_{22}+𝑥_{23}} \\ & =\sqrt{(−1)^{2}+(−2)^{2}+2^{2}} \\ & =3.\end{aligned}


$$

Also, $\mathbf{Q}(\mathbf{x}) \cdot \mathbf{Q}(\mathbf{y}) = \mathbf{x} \cdot \mathbf{y}.$ As a result,

$$


\begin{aligned}𝐐(𝐱)⋅𝐐(𝐲) & =𝐱⋅𝐲 \\ & =(−1)⋅3+(−2)⋅0+2⋅5 \\ & =7.\end{aligned}


$$

### Example: Identifying the Orthogonality of a Two-Vector Set

#### Question

$$


\begin{aligned}\frac{2\sqrt{2}}{3} \\ \frac{1}{3}\end{aligned}


$$

Consider the vectors above, and let $\mathbf{Q}$ be an orthogonal linear transformation. Which of the following statements are true?

1. $\mathbf{u}_1 \cdot \mathbf{u}_2 = 0$

2. $\{\mathbf{Q}(\mathbf{u}_1),\mathbf{Q}(\mathbf{u}_2)\}$ is orthogonal

3. $\{\mathbf{Q}(\mathbf{u}_1),\mathbf{Q}(\mathbf{u}_2)\}$ is orthonormal

#### Explanation

Since $\mathbf{Q}$ is orthogonal, we have that $\mathbf{Q}(\mathbf{x}) \cdot \mathbf{Q}(\mathbf{y}) = \mathbf{x} \cdot \mathbf{y}$ for any vectors $\mathbf{x}$ and $\mathbf{y}.$

The linear transformation $\mathbf{Q}$ being orthogonal is equivalent to the following:

- The matrix $Q$ of transformation $\mathbf{Q}$ relative to any orthonormal basis (including the standard basis) of $\mathbb{R}^n$ is orthogonal.

- $|| \mathbf{Q}(\mathbf{x}) || = || \mathbf{x} ||.$

- If $\mathbf{x} \perp \mathbf{y}$ then $\mathbf{Q}(\mathbf{x}) \perp \mathbf{Q}(\mathbf{y})$ for any $\mathbf{x}, \mathbf{y} \in \mathbb{R}^n.$ In general, $\mathbf{Q}$ preserves the angle between any two vectors.

- $\mathbf{Q}$ maps any orthogonal (orthonormal) set into an orthogonal (orthonormal) set.

With that in mind, let's examine our statements.

- Statement I is true. Indeed,

- Statement II is true. Indeed, $\mathbf{Q}(\mathbf{u}_1) \perp \mathbf{Q}(\mathbf{u}_2)$ since

- Statement III is true. Indeed, both $\mathbf{Q}(\mathbf{u}_1)$ and $\mathbf{Q}(\mathbf{u}_2)$ are unit vectors:

Therefore, the correct answer is "I, II, and III."
