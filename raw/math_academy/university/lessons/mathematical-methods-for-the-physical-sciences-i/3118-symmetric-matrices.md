# Symmetric Matrices

Source: https://www.mathacademy.com/topics/3118?courseId=154
Topic ID: 3118

## Prerequisites

- [The Transpose of a Matrix](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/232-the-transpose-of-a-matrix.md)
- [Introduction to the Inverse of a Matrix](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/863-introduction-to-the-inverse-of-a-matrix.md)
- [Powers of Matrices](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/1725-powers-of-matrices.md)

## Lesson

### Introduction

A square matrix $A$ is **symmetric** if it is equal to its transpose:

$$


A^T = A


$$

Equivalently, an $n\times n$ matrix is symmetric if $a_{ij} = a_{ji}$ for all $1 \leq i,j\leq n.$

If $A$ is symmetric, this really means that it is symmetric across its main diagonal.

For example, the matrix

$$


[\begin{aligned}3 & 4 \\ 4 & −5\end{aligned}]


$$

is symmetric since $A^T = A.$

On the other hand, the matrix

$$


[\begin{aligned}3 & 4 \\ 2 & −5\end{aligned}]


$$

is not symmetric. Indeed, since $b_{12} \neq b_{21},$ we have $B^T \neq B.$

### Example: Identifying Symmetric Matrices

#### Question

Which of the following matrices are symmetric?

$$


[\begin{aligned}1 & −6 \\ −6 & 1\end{aligned}]


$$

#### Explanation

A square matrix $A$ is symmetric if it is equal to its transpose:

$$


A = A^T


$$

Equivalently, $a_{ij} = a_{ji}$ for all $i,j.$ In other words, $A$ is symmetric across its main diagonal.

With that in mind, let's examine each matrix in turn.

- $P$ is a symmetric matrix. Indeed, $P=P^T.$

- $Q$ is a symmetric matrix. Indeed, $Q=Q^T.$

- $R$ is ** a symmetric matrix. Since $r_{12} \neq r_{21},$ we obtain $R \neq R^T.$

Therefore, the correct answer is "$P$ and $Q$ only."

### Properties of Symmetric Matrices

Suppose that $A$ is a symmetric matrix. Then, we have the following properties:

- $-A$ is symmetric

- $A^m$ is symmetric for any positive integer $m$

- $A^{-1}$ is symmetric for nonsingular $A$

If $A$ and $B$ are $n\times n$ symmetric matrices, we have the following properties:

- $A+B$ is symmetric

- The product $A\cdot B$ is *not* always symmetric. For example, if then the product $A\cdot B$ is which is *not* symmetric.

Finally, the following two properties can be used to construct symmetric matrices:

- $A + A^T$ is symmetric for any *square* matrix $A$

- $A^T A$ and $A A^T$ are symmetric for *any* matrix $A$

The last property is true for *any* $m\times n$ matrix. This property is particularly useful, as we'll discover in future lessons.

### Example: Identifying True Statements Regarding Properties of Symmetric Matrices

#### Question

Which of the following statements are true?

1. If $A$ is ** $n\times n$ matrix, then $A+A^T$ is always symmetric.

2. The difference between two $n\times n$ symmetric matrices is symmetric.

3. The product of two $n\times n$ symmetric matrices is symmetric.

#### Explanation

A square matrix $A$ is symmetric if it is equal to its transpose:

$$


A = A^T


$$

Equivalently, $a_{ij} = a_{ji}$ for all $i,j.$ In other words, $A$ is symmetric across its main diagonal.

With that in mind, let's examine our statements in turn.

- Statement I is true. Indeed, for any matrix $A,$ we have

- Statement II is true. Indeed, the sum or difference between two symmetric matrices is symmetric.

- Statement III is false. As a counterexample, consider the symmetric matrices Their product is not symmetric:

Therefore, the correct answer is "I and II only."
