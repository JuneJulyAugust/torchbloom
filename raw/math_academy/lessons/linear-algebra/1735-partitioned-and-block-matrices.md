# Partitioned and Block Matrices

Source: https://www.mathacademy.com/topics/1735?courseId=55
Topic ID: 1735

## Prerequisites

- [The Determinant of a 3x3 Matrix](../integrated-math-iii-honors/153-the-determinant-of-a-3x3-matrix.md)
- [Triangular Matrices](./1777-triangular-matrices.md)

## Lesson

### Introduction

Consider the $3 \times 4$ matrix $M,$ given by

$$


\begin{aligned}2 & 1 & 0 & 4 \\ 0 & 5 & 1 & −2 \\ 4 & 0 & 0 & −5\end{aligned}


$$

We can subdivide $M$ using horizontal and vertical lines, as follows:

$$


\begin{aligned}2 & 1 & 0 & 4 \\ 0 & 5 & 1 & −2 \\ 4 & 0 & 0 & −5\end{aligned}


$$

When partitioned in this way, we say that the matrix $M$ consists of four **blocks**, where each block is itself a matrix:

$$


\begin{aligned}\overset{\overset{[\begin{aligned}2 & 1 \\ 0 & 5\end{aligned}]}{}}{𝑀_{11}} & \,\,\overset{\overset{[\begin{aligned}0 & 4 \\ 1 & −2\end{aligned}]}{}}{𝑀_{12}} \\ \underset{𝑀_{21}}{\underset{}{[\begin{aligned}4\, & 0\end{aligned}]}}\, & \,\,\,\underset{𝑀_{22}}{\underset{}{[\begin{aligned}0\, & −5\end{aligned}]}}\end{aligned}


$$

Quite often, a matrix can be partitioned in various ways. Another partition of $M$ is shown below:

$$


\begin{aligned}2 & 1 & 0 & 4 \\ 0 & 5 & 1 & −2 \\ 4 & 0 & 0 & −5\end{aligned}


$$

Under this partition, we obtain different blocks.

### Example: Identifying Dimensions of Blocks in Partitioned Matrices

#### Question

A partitioned matrix $M$ contains the following blocks:

- $M_{11},$ which is a $1 \times 2$ block

- $M_{12},$ which is a $1 \times 3$ block

- $M_{21},$ which is a $2 \times 2$ block

Find the dimensions of the block $M_{22}$.

#### Explanation

We have a matrix of the form

$$


\begin{aligned}𝑀_{11} & 𝑀_{12} \\ 𝑀_{21} & 𝑀_{22}\end{aligned}


$$

Therefore, $M_{22}$ must be a $2 \times 3$ block.

### Block Diagonal Matrices

Consider the following matrix:

$$


\begin{aligned}1 & −3 & 0 & 0 & 0 & 0 \\ 9 & 2 & 0 & 0 & 0 & 0 \\ 0 & 0 & 5 & −2 & −6 & 0 \\ 0 & 0 & 7 & 4 & 0 & 0 \\ 0 & 0 & 1 & 2 & 10 & 0 \\ 0 & 0 & 0 & 0 & 0 & −2\end{aligned}


$$

Notice that this matrix satisfies the following conditions:

- it's a square matrix

- all blocks that lie on the main diagonal are square matrices

- all blocks that lie outside the main diagonal are zero matrices

Matrices that have these properties are called **block diagonal** matrices.

### Block Triangular Matrices

Now consider the following matrix:

$$


\begin{aligned}2 & 0 & 0 & 1 & 0 & −3 \\ 7 & −1 & 3 & 0 & 9 & 0 \\ 0 & 0 & 11 & −2 & 0 & −1 \\ 0 & 0 & 1 & 5 & 0 & −4 \\ 0 & 0 & 3 & −1 & 4 & 5 \\ 0 & 0 & 0 & 0 & 0 & 4\end{aligned}


$$

Notice that this matrix satisfies the following conditions:

- it's a square matrix

- all blocks that lie on the main diagonal are square matrices

- all blocks that lie *below* the main diagonal are zero matrices

When a matrix satisfies these conditions, we say that it is **block upper triangular**.

A **block lower triangular matrix** can be defined similarly. In that case, we need the zero blocks to be above the main diagonal.

### Example: Identifying Block Diagonal and Block Triangular Matrices

#### Question

Which of the following matrices are block diagonal?

$$


\begin{aligned}9 & 7 & 0 \\ 10 & 5 & 0 \\ 0 & 0 & 12\end{aligned}


$$

#### Explanation

A block diagonal matrix can be partitioned so that it has only square blocks on the main diagonal, and all the other blocks contain only zeros.

With that in mind, let's examine our matrices.

- $A$ is a block diagonal matrix. Indeed, we can partition it as follows:

- $B$ is ** a block diagonal matrix since it can't be partitioned in the way described above:

- $C$ is ** a block diagonal matrix since it can't be partitioned in the way described above:

Therefore, the correct answer is "$A$ only."

### Determinants of Block Diagonal and Block Triangular Matrices

One nice property of block diagonal matrices is that we can calculate their determinants relatively easily.

To compute the determinant of a block diagonal matrix, we simply calculate the product of the determinants of the diagonal blocks. The determinant of a block lower triangular or block upper triangular matrix can be computed similarly.

For instance, consider the following matrix:

$$


\begin{aligned}3 & 0 & 0 & 0 \\ 5 & −1 & 0 & 0 \\ 0 & 3 & 2 & 0 \\ 1 & 5 & 1 & 1\end{aligned}


$$

Notice that our matrix is block lower triangular. Therefore, we can compute its determinant as follows:

$$


\begin{aligned}\begin{aligned}3 & 0 & 0 & 0 \\ 5 & −1 & 0 & 0 \\ 0 & 3 & 2 & 0 \\ 1 & 5 & 1 & 1\end{aligned} & =\begin{aligned}3 & 0 & 0 & 0 \\ 5 & −1 & 0 & 0 \\ 0 & 3 & 2 & 0 \\ 1 & 5 & 1 & 1\end{aligned} \\ & =\begin{aligned}3 & 0 \\ 5 & −1\end{aligned}⋅\begin{aligned}2 & 0 \\ 1 & 1\end{aligned} \\ & =(−3)⋅2 \\ & =−6\end{aligned}


$$

### Example: Finding the Determinant of a Block Diagonal or Block Triangular Matrix

#### Question

Find $\begin{aligned}7 & 0 & −5 \\ 0 & 𝑒 & 4 \\ 0 & ℎ & 8\end{aligned}$ given that $\begin{aligned}𝑒 & 4 \\ ℎ & 8\end{aligned}$

#### Explanation

Notice that we have a block upper triangular matrix. Therefore, its determinant is equal to the product of the determinants of the diagonal blocks:

$$


\begin{aligned}\begin{aligned}7 & 0 & −5 \\ 0 & 𝑒 & 4 \\ 0 & ℎ & 8\end{aligned} & =\begin{aligned}7 & 0 & −5 \\ 0 & 𝑒 & 4 \\ 0 & ℎ & 8\end{aligned} \\ & =7⋅\begin{aligned}𝑒 & 4 \\ ℎ & 8\end{aligned} \\ & =7⋅6 \\ & =42\end{aligned}


$$
