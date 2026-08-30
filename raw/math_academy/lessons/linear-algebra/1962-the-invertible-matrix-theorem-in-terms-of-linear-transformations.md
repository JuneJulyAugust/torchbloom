# The Invertible Matrix Theorem in Terms of Linear Transformations

Source: https://www.mathacademy.com/topics/1962?courseId=55
Topic ID: 1962

## Prerequisites

- [The Invertible Matrix Theorem in Terms of Dimension, Rank and Nullity](./1869-the-invertible-matrix-theorem-in-terms-of-dimension-rank-and-nullity.md)
- [Invertible Functions](../algebra-ii/1889-invertible-functions.md)
- [The Kernel of a Linear Transformation](./1960-the-kernel-of-a-linear-transformation.md)
- [The Image and Rank of a Linear Transformation](./1963-the-image-and-rank-of-a-linear-transformation.md)

## Lesson

### Introduction

A linear transformation is **invertible** if there is another linear transformation such that

for every vector The transformation is called the **inverse** of An invertible linear transformation is also called a **bijection**.

We have the following theorem regarding invertible linear transformations:

*If is the standard matrix of, then is invertible if and only if is invertible*.

Recall that the invertible matrix theorem in terms of dimension, rank, and nullity states that if is an matrix, then

is invertible

In the theorem above, we can make the following swaps, where is a linear transformation with the standard matrix

As a result, we obtain the **invertible matrix theorem in terms of linear transformations:**

is a bijection (invertible) is invertible

### Example: Recognizing Parts of the Invertible Matrix Theorem

#### Question

$\mathbf{T}$ is a bijection $\begin{aligned} & 𝑊𝑊=ℝ^{𝑛} \\ & rank(𝐓)=𝑛 \\ & Ker(𝐓)={𝟎} \\ & nullity(𝐓)=0\end{aligned}$ $\qquad \Longleftrightarrow \qquad$ $T$ is invertible

Consider the equivalence above, where $\mathbf{T}:\mathbb{R}^n \to \mathbb{R}^n$ is a linear transformation whose standard matrix is $T.$ What should be placed into the blank space to make a true statement?

#### Explanation

Recall that the ** (in terms of linear transformations) states the following:

$\mathbf{T}$ is a bijection $\begin{aligned} & Im(𝐓)=ℝ^{𝑛} \\ & rank(𝐓)=𝑛 \\ & Ker(𝐓)={𝟎} \\ & nullity(𝐓)=0\end{aligned}$ $\qquad \Longleftrightarrow \qquad$ $T$ is invertible

Therefore, the missing expression is $\textrm{Im}(\mathbf{T}).$

### Example: Identifying True Statements Using the Invertible Matrix Theorem

#### Question

Which of the following statements are true given that $\mathbf{T}:\mathbb{R}^3 \to \mathbb{R}^3$ is a linear transformation whose standard matrix is $T,$ and $T$ is invertible?

1. $\textrm{Ker}(\mathbf{T}) \neq \{\mathbf{0}\}$

2. $\textrm{nullity}(\mathbf{T})=0$

3. $\textrm{rank}(\mathbf{T}) = 3$

#### Explanation

Since $\mathbf{T}$ is a linear transformation from $\mathbb{R}^3$ into $\mathbb{R}^3,$ the invertible matrix theorem states the following:

$\mathbf{T}$ is a bijection (an invertible transformation) $\begin{aligned} & Im(𝐓)=ℝ^{3} \\ & rank(𝐓)=3 \\ & Ker(𝐓)={𝟎} \\ & nullity(𝐓)=0\end{aligned}$

With that in mind, let's examine each statement in turn.

- Statement I is false. Since $T$ is invertible, the invertible matrix theorem implies that $\textrm{Ker}(\mathbf{T}) = \{\mathbf{0}\}.$

- Statement II is true. Since $T$ is invertible, the invertible matrix theorem implies that $\textrm{nullity}(\mathbf{T}) = 0.$

- Statement III is true. Since $T$ is invertible, the invertible matrix theorem implies that $\textrm{rank}(\mathbf{T}) = 3.$

Therefore, the correct answer is "II and III only."

### Example: Сompleting a Sentence Using the Invertible Matrix Theorem

#### Question

Let $\mathbf{T}:\mathbb{R}^3\rightarrow \mathbb{R}^3$ be a linear transformation whose standard matrix is $T.$ Consider the following statement:

**

Which of the following can be placed into the blank space to make a true statement?

1. $\textrm{Im}(\mathbf{T})=\mathbb{R}^3$

2. $\textrm{Ker}(\mathbf{T})\ne\{\mathbf{0}\}$

3. $\mathbf{T}$ is invertible

#### Explanation

Since $\mathbf{T}$ is a linear transformation from $\mathbb{R}^3$ into $\mathbb{R}^3,$ the invertible matrix theorem states the following:

$\mathbf{T}$ is a bijection (an invertible transformation) $\begin{aligned} & Im(𝐓)=ℝ^{3} \\ & rank(𝐓)=3 \\ & Ker(𝐓)={𝟎} \\ & nullity(𝐓)=0\end{aligned}$

With that in mind, let's examine each statement in turn.

- Statement I is false. Since $[1, 2, 1]^T \not\in \textrm{Im}(\mathbf{T}),$ we must have that $\textrm{Im}(\mathbf{T}) \neq \mathbb{R}^3.$

- Statement II is true. Since the vector $[1, 2, 1]^T$ does not lie in $\textrm{Im}(\mathbf{T})$, then $\textrm{Im}(\mathbf{T}) \neq \mathbb{R}^3.$ Therefore, according to the invertible matrix theorem, we must have $\textrm{Ker}(\mathbf{T}) \neq \{\mathbf{0}\}.$

- Statement III is false. According to the invertible matrix theorem, since $\textrm{Im}(\mathbf{T}) \neq \mathbb{R}^3,$ the transformation $\mathbf T$ can't be invertible.

Therefore, the correct answer is "II only."
