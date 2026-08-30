# Dimension in Abstract Vector Spaces

Source: https://www.mathacademy.com/topics/2759?courseId=55
Topic ID: 2759

## Prerequisites

- [Sigma Notation](../../../high-school/integrated-math-honors/lessons/integrated-math-ii-honors/673-sigma-notation.md)
- [The Dimension of a Span](./1866-the-dimension-of-a-span.md)
- [The Coordinates of a Vector Relative to a Basis in Abstract Vector Spaces](./3212-the-coordinates-of-a-vector-relative-to-a-basis-in-abstract-vector-spaces.md)

## Lesson

### Introduction

The standard basis of the vector space $\mathbb{R}_2[t]$ of all polynomials in the variable $t$ over $\mathbb{R}$ with degree at most $2$ is

$$


\{1, \: t, \: t^2\}.


$$

Another basis of $\mathbb{R}_2[t]$ is

$$


\big\{ t^2-1, \: t+3, \: 2t-1 \big\}.


$$

In general, vector spaces have infinitely many bases.

Let's now consider the following theorem:

*If a basis of a vector space $V$ has $n$ elements, then every basis of $V$ has $n$ elements.*

The number $n$ is called the **dimension** of the vector space, and we write $\textrm{dim}(V)=n.$

So, since the standard basis of $\mathbb{R}_2[t]$ has $3$ elements, all of its bases have $3$ elements, and we write

$$


\textrm{dim}(\mathbb{R}_2[t])=3.


$$

### Example: Determining the Dimension of a Polynomial Vector Space Given Its Standard Monomial Basis

#### Question

What is the dimension of $\mathbb{R}_6[t]$, the vector space of all polynomials in the variable $t$ of degree at most $6?$

#### Explanation

The standard basis of $\mathbb{R}_n[t]$ is

$$


\{1, \: t, \: t^2, \: \ldots, \: t^n\}.


$$

So, the standard basis of $\mathbb{R}_6[t]$ is

$$


\{1, \: t, \: t^2, \: \ldots, \: t^6\}.


$$

Therefore, we have that

$$


\textrm{dim}(\mathbb{R}_6[t])=6+1=7.


$$

In general,

$$


\textrm{dim}(\mathbb{R}_n[t])=n+1.


$$

### Example: Determining the Dimension of a Matrix Vector Space Given Its Standard Basis

#### Question

What is the dimension of $\text{M}_{5\times6}(\mathbb{R}),$ the vector space of all $5\times 6$ matrices over $\mathbb{R}?$

#### Explanation

The standard basis of $\text{M}_{n\times m}(\mathbb{R})$ contains a total of $n\cdot m$ matrices, each with one nonzero entry that is equal to $1.$

For example, the standard basis of $\text{M}_{3\times 2} (\mathbb{R})$ contains $3\cdot 2= 6$ elements, and is given by

$$


\begin{aligned}1 & 0 \\ 0 & 0 \\ 0 & 0\end{aligned}


$$

However, we're asked to find the dimension of $\text{M}_{5\times6}(\mathbb{R}),$ not $\text{M}_{3\times 2} (\mathbb{R}).$

If we were to repeat the same process above for the vector space $\text{M}_{5\times6}(\mathbb{R}),$ we would have $30$ matrices in our basis, meaning that

$$


\textrm{dim}(\text{M}_{5\times 6}(\mathbb{R})) = 5\cdot 6 =30.


$$

In general,

$$


\textrm{dim}(\text{M}_{n\times m}(\mathbb{R})) = n\cdot m.


$$

### Example: Identifying True Statements About Dimensions of Vector Spaces

#### Question

Which of the following vector spaces has a dimension of $9?$

1. $\mathbb{R}^8$

2. $\mathbb{R}_8[t]$, the vector space of all polynomials in the variable $t$ of degree at most $8$

3. $\text{M}_{3}(\mathbb{R}),$ the vector space of all $3 \times 3$ matrices over $\mathbb{R}$

#### Explanation

Let's examine each of the vector spaces in turn.

1. Recall that $\textrm{dim}(\mathbb{R}^n)=n.$ Therefore,

2. Recall that $\textrm{dim}(\mathbb{R}_{n}[t])=n+1.$ Therefore,

3. Recall that $\textrm{dim}(\text{M}_{n}(\mathbb{R}))=n^2.$ Therefore,

Hence, the correct answer is "II and III only."

### Infinite-Dimensional Vector Spaces

When a vector space $V$ has a finite dimension $\textrm{dim}(V) = n < \infty,$ the vector space is **finite-dimensional**.

Some vector spaces can have arbitrarily large linearly independent sets. In such cases, the vector space is **infinite-dimensional**.

An example of an infinite-dimensional vector space is the space of all continuous functions $C(\mathbb{R})$ defined on $f: \mathbb{R} \to \mathbb{R}.$

To understand why $C(\mathbb{R})$ is an infinite-dimensional vector space, we note that for any positive integer $n,$ the following set of continuous functions is linearly independent:

$$


\big\{ 1, \: t, \: t^2, \: \ldots, t^n \big\}


$$

Indeed, we have that

$$


\sum\limits_{i=0}^n x_i t^i = 0


$$

for all $t\in\mathbb{R}$ if and only if $x_i=0$ for all $i=0,1,2,\ldots,n.$ Since $n$ can be arbitrarily large, our vector space cannot have finite dimension.

### Example: Identifying Finite and Infinite-Dimensional Vector Spaces

#### Question

Which of the following vector spaces are finite-dimensional?

1. $\mathbb{R}^{100}$

2. $\text{M}_{50\times100}(\mathbb{R}),$ the vector space of all $50 \times 100$ matrices over $\mathbb{R}$

3. $\mathbb{R}[t],$ the vector space of all polynomial functions in the variable $t$

#### Explanation

Let's examine our vector spaces.

- $\mathbb{R}^{100}$ and $\text{M}_{50\times100}(\mathbb{R})$ are finite-dimensional. Indeed, and are both finite numbers.

- $\mathbb{R}[t]$ is ** finite-dimensional. To understand why, we first note that the following set of (polynomial) functions is linearly independent: Indeed, we have that for all $t \in \mathbb{R}$ if and only if $a_i = 0$ for all $i=0,1,2,\ldots, n.$ Therefore, for any $n\in \mathbb N,$ there exists a linearly independent subset of $\mathbb{R}[t]$ of size $n,$ which imples that $\mathbb{R}[t]$ cannot have finite dimension.

Therefore, the correct answer is "I and II only."
