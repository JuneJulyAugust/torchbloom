# Positive-Definite and Negative-Definite Quadratic Forms

Source: https://www.mathacademy.com/topics/3127?courseId=145
Topic ID: 3127

## Prerequisites

- [The Characteristic Equation of a Matrix](./1964-the-characteristic-equation-of-a-matrix.md)
- [The Difference of Sets](./2828-the-difference-of-sets.md)
- [Quadratic Forms](./3123-quadratic-forms.md)

## Lesson

### Introduction

In certain applications involving quadratic forms, an important question is whether a particular quadratic form $Q(\mathbf x)$ is *always* positive or *always* negative.

We classify quadratic forms using the following terminology:

- A quadratic form $Q(\mathbf{x})$ is **positive-definite** if $Q(\mathbf{x}) > 0$ for all $\mathbf{x} \in \mathbb{R}^n \setminus \{\mathbf{0} \}.$ For example, the quadratic form is positive-definite since $8x_1^2+3x_2^2 > 0$ for all nonzero $\mathbf{x}.$

- A quadratic form $Q(\mathbf{x})$ is **negative-definite** if $Q(\mathbf{x}) < 0$ for all $\mathbf{x} \in \mathbb{R}^n \setminus \{\mathbf{0} \}.$ For example, the quadratic form is negative-definite since $-x_1^2-3x_2^2 \lt 0$ for all nonzero $\mathbf{x}.$

- A quadratic form $Q(\mathbf{x})$ is **indefinite** if $Q(\mathbf{x}_1) > 0$ for some $\mathbf{x}_1 \in \mathbb{R}^n,$ and $Q(\mathbf{x}_2) < 0$ for some $\mathbf{x}_2 \in \mathbb{R}^n.$ For example, the form is indefinite. Substituting $[\begin{aligned}1 \\ 0\end{aligned}]$ we get while substituting $[\begin{aligned}1 \\ 1\end{aligned}]$ we obtain

### Example: Identifying Possible Quadratic Form Types Using Substitution

#### Question

Consider the vector $[\begin{aligned}2 \\ 7\end{aligned}]$ By evaluating the following quadratic forms at $\mathbf{x}$ **** determine which of them **** be negative-definite.

1. $R(\mathbf{x})=x_1^2 - 3x_2^2 + 5x_1x_2$

2. $[\begin{aligned}3 & 0 \\ 0 & 2\end{aligned}]$

3. $T(\mathbf{x})=x_2^2 + 8x_1x_2$

#### Explanation

A quadratic form $Q(\mathbf{x})$ is negative-definite if $Q(\mathbf{x}) \lt 0$ for all $\mathbf{x} \in \mathbb{R}^n \setminus \{\mathbf{0} \}.$

With that in mind, let's examine each of the quadratic forms by substituting $[\begin{aligned}2 \\ 7\end{aligned}]$

- Quadratic form I ** be negative-definite. Indeed,

- Quadratic form II ** be negative-definite since

- Quadratic form III ** be negative-definite since

Therefore, the correct answer is "II and III only."

### Positive and Negative Semi-Definite Quadratic Forms

There are two further classifications of quadratic forms that turn out to be useful:

- A quadratic form $Q(\mathbf{x})$ is **positive semi-definite** if $Q(\mathbf{x}) \geq 0$ for all $\mathbf{x} \in \mathbb{R}^n.$ For example, the form $A(\mathbf{x})=x_1^2$ over $\mathbb{R}^2$ is positive semi-definite. Notice that this particular form is not positive-definite since it gives zero on the nonzero vector $[\begin{aligned}0 \\ 1\end{aligned}]$

- A quadratic form $Q(\mathbf{x})$ is **negative semi-definite** if $Q(\mathbf{x}) \leq 0$ for all $\mathbf{x} \in \mathbb{R}^n.$ For example, the form $B(\mathbf{x})=-x_1^2$ over $\mathbb{R}^2$ is negative semi-definite. Notice that this particular form is not negative-definite since it gives zero on the nonzero vector $[\begin{aligned}0 \\ 1\end{aligned}]$

It's also worth noting that

- any positive-definite quadratic form is positive semi-definite, and

- any negative-definite quadratic form is negative semi-definite.

### Using Eigenvalues to Classify Quadratic Forms

Given a quadratic form $Q(\mathbf x) = \mathbf{x}^T A \mathbf{x}$ with a symmetric matrix $A$, we have the following theorem:

- $Q$ is positive-definite if and only if all the eigenvalues of $A$ are positive,

- $Q$ is positive semi-definite if and only if all the eigenvalues of $A$ are non-negative,

- $Q$ is negative-definite if and only if all the eigenvalues of $A$ are negative,

- $Q$ is negative semi-definite if and only if all the eigenvalues of $A$ are non-positive,

- $Q$ is indefinite if and only if $A$ has both positive and negative eigenvalues.

Using the same criteria, we can also classify the symmetric matrix $A$ as positive-definite, positive semi-definite, etc.

For example, consider the matrix $A,$ given by

$$


[\begin{aligned}−5 & −1 \\ −1 & −5\end{aligned}]


$$

Computing the characteristic equation of $A,$ we obtain

$$


\begin{aligned}|𝐴−𝜆𝐼| & =0 \\ \begin{matrix}−5−𝜆 & −1 \\ −1 & −5−𝜆\end{matrix} & =0 \\ (−5−𝜆)(−5−𝜆)−1 & =0 \\ 𝜆^{2}+10𝜆+24 & =0 \\ (𝜆+4)(𝜆+6) & =0 \\ 𝜆 & =−4,\,−6.\end{aligned}


$$

Since all the eigenvalues of $A$ are negative, the quadratic form $Q(\mathbf x) = \mathbf{x}^T A \, \mathbf{x}$ (as well as the matrix $A$) is negative-definite.

### Example: Identifying a Quadratic Form Type by Calculating the Corresponding Eigenvalues

#### Question

Consider the matrix $[\begin{aligned}−4 & 5 \\ 5 & −4\end{aligned}]$ Which of the following statements are true?

1. The eigenvalues of $A$ are $\lambda_1=-1$ and $\lambda_2=9$

2. $\mathbf{x}^T \! A \, \mathbf{x}$ is indefinite

3. $A$ is positive-definite

#### Explanation

Given a quadratic form $Q(\mathbf x) = \mathbf{x}^T A \mathbf{x},$ we have the following theorem:

- $Q$ is positive-definite if and only if all the eigenvalues of $A$ are positive,

- $Q$ is positive semi-definite if and only if all the eigenvalues of $A$ are non-negative (note that positive semi-definite quadratic forms include all positive-definite quadratic forms),

- $Q$ is negative-definite if and only if all the eigenvalues of $A$ are negative,

- $Q$ is negative semi-definite if and only if all the eigenvalues of $A$ are non-positive (note that negative semi-definite quadratic forms include all negative-definite quadratic forms), and

- $Q$ is indefinite if and only if $A$ has both positive and negative eigenvalues.

With that in mind, let's examine our statements in turn.

- Statement I is false. Computing the characteristic equation of $A,$ we obtain

- Statement II is true, while statement III is false. Since $A$ has positive and negative eigenvalues, the quadratic form $\mathbf{x}^T \! A \, \mathbf{x}$ (as well as the matrix $A$) is indefinite.

Therefore, the correct answer is "II only."

### The Leading Principal Minors of a Square Matrix

The **leading principal minors** of an matrix are the determinants formed by the first rows and first columns of for The leading principal minors of are denoted

Note that:

- the first leading principal minors equals and

- the th leading principal minors equals

For example, consider the matrix given by

Since is a matrix, it has leading principal minors. Let's compute them:

- The first leading principal minors is the determinant formed by the first row and first column of

- The second leading principal minors is the determinant formed by the first rows and first columns of

- The third leading principal minors is the determinant formed by the first rows and first columns of

### Sylvester's Criterion

Let for denote the leading principal minors of an matrix

According to **Sylvester's criterion**, the quadratic form is

- positive-definite if and only if for all

- negative-definite if and only if, for all we have when is odd, and when is even.

In particular, if is negative-definite, then the leading principal minors alternate in sign, with the *first* leading principal minors being negative.

For example, consider the matrix

Let's compute its leading leading principal minors:

All leading principal minors are positive. Therefore, by Sylvester's criterion, the quadratic form is positive-definite.

### Example: Identifying a Quadratic Form Type Using Sylvester's Criterion

#### Question

$$


\begin{aligned}−6 & −5 & 1 \\ 5 & −2 & 2 \\ 1 & 2 & −1\end{aligned}


$$

Consider the matrix $A$ shown above. Which of the following statements are true?

1. $a_{11}=-6$ and $\det(A) \lt 0$

2. $\mathbf{x}^T \! A \, \mathbf{x}$ is negative-definite

3. $A$ is positive-definite

#### Explanation

Let $\Delta_i$ for $i=1,2,\ldots,n$ denote the principal minors of an $n \times n$ matrix $A.$ Then, according to Sylvester's criterion, the quadratic form $\mathbf{x}^T \! A \, \mathbf{x}$ (as well as the matrix $A$) is

- positive-definite if and only if $\Delta_i > 0$ for all $i=1,2,\ldots,n,$

- negative-definite if and only if, for all $i=1,2,\ldots,n,$ we have $\Delta_i < 0$ when $i$ is odd, and $\Delta_i > 0$ when $i$ is even.

With that in mind, let's examine each of the statements in turn.

- Statement I is true. Indeed, $a_{11}=-6.$ Expanding $\det(A)$ along the top row, we get

- Statement II is true, while statement III is false. Notice the following: So, by Sylvester's criterion, the quadratic form $\mathbf{x}^T \! A \, \mathbf{x},$ and the matrix $A,$ are negative-definite.

Therefore, the correct answer is "I and II only."
