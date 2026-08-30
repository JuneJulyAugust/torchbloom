# LU Factorization of 2x2 Matrices

Source: https://www.mathacademy.com/topics/1779?courseId=55
Topic ID: 1779

## Prerequisites

- [Row Operations on 2x2 Matrices as Products of Elementary Matrices](./1727-row-operations-on-2x2-matrices-as-products-of-elementary-matrices.md)
- [Triangular Matrices](./1777-triangular-matrices.md)

## Lesson

### Introduction

In the same way that we can factor numbers or polynomials, we can factor a matrix by writing it as a product of two or more matrices. In fact, there is one factorization technique that works for *all* matrices, called **LU factorization** (or **LU decomposition**).

LU factorization involves writing a matrix $A$ as a product of two matrices $L$ and $U,$ where

- $[\begin{aligned}1 & 0 \\ ∗ & 1\end{aligned}]$ is a *unit lower triangular matrix* (a lower triangular matrix that has only $1$'s on the main diagonal), and

- $[\begin{aligned}∗ & ∗ \\ 0 & ∗\end{aligned}]$ is an *upper triangular matrix*.

For example, we can write the matrix $[\begin{aligned}−2 & 1 \\ 6 & −6\end{aligned}]$ in LU factored form as follows:

$$


\begin{aligned}[\begin{aligned}−2 & 1 \\ 6 & −6\end{aligned}]=\underset{𝐿}{\underset{}{[\begin{aligned}1 & 0 \\ −3 & 1\end{aligned}]}}⋅\underset{𝑈}{\underset{}{[\begin{aligned}−2 & 1 \\ 0 & −3\end{aligned}]}}\end{aligned}


$$

You may be wondering how we arrived at this factorization. Shortly, we'll discuss an algorithm that explains how to compute $L$ and $U$ for any $2\times2$ matrix $A.$ But for now, let's focus on recognizing LU factored forms.

### Example: Identifying LU Factorizations

#### Question

Which of the following products is the LU factorization of a matrix $A?$

1. $[\begin{aligned}1 & 0 \\ 4 & 1\end{aligned}]$

2. $[\begin{aligned}2 & 0 \\ 2 & −3\end{aligned}]$

3. $[\begin{aligned}1 & 0 \\ −3 & 1\end{aligned}]$

#### Explanation

Remember that in the LU factorization of a matrix $A,$ we write $A=LU$ where the matrix $L$ is a unit lower triangular matrix (a lower triangular matrix that has only $1$'s on the main diagonal) and the matrix $U$ is an upper triangular matrix:

$$


[\begin{aligned}1 & 0 \\ ∗ & 1\end{aligned}]


$$

With that in mind, let's inspect each product in turn.

- The first product is in $LU$ form because the left matrix is a unit lower triangular matrix, and the right matrix is an upper triangular matrix.

- The second product is ** in $LU$ form. Although the left matrix is a lower triangular matrix, it is not a ** lower triangular matrix because it does not have $1$'s on the diagonal.

- The third product is ** in $LU$ form because the matrix on the right is not an upper triangular matrix, as it has a non-zero entry below the diagonal.

Therefore, the correct answer is "I only."

### An Algorithm for Finding the LU Factorization of a 2x2 Matrix

Let $[\begin{aligned}−2 & 1 \\ 6 & −6\end{aligned}]$ To perform LU factorization, we need to write $A$ as

$$


[\begin{aligned}−2 & 1 \\ 6 & −6\end{aligned}]


$$

To find the matrices $L$ and $U,$ we reduce the matrix $A$ to row echelon form. Whilst doing this, we simultaneously write down the row operations applied to $A$ in terms of matrix multiplication using elementary matrices:

$$


\begin{aligned}𝐴 & =[\begin{aligned}−2 & 1 \\ 6 & −6\end{aligned}] & 𝑅_{2} & :=𝑅_{2}+3𝑅_{1}\,⟺\,\overset{\overset{[\begin{aligned}1 & 0 \\ 3 & 1\end{aligned}]}{}}{𝐸_{1}}⋅𝐴 \\ & ∼[\begin{aligned}−2 & 1 \\ 0 & −3\end{aligned}] & & \\ & =𝑈 & & \end{aligned}


$$

The reduced matrix is upper triangular, so it is our matrix $U.$ Now, since $E_1A=U,$ we can invert $E_1$ to arrive at the desired LU factorization:

$$


\begin{aligned}𝐸_{1}𝐴 & =𝑈 \\ 𝐴 & =𝐸_{−11}^{}𝑈 \\ 𝐴 & =[\begin{aligned}1 & 0 \\ 3 & 1\end{aligned}]^{−1}𝑈 \\ 𝐴 & =\underset{𝐿}{\underset{}{[\begin{aligned}1 & 0 \\ −3 & 1\end{aligned}]}}⋅\underset{𝑈}{\underset{}{[\begin{aligned}−2 & 1 \\ 0 & −3\end{aligned}]}}\end{aligned}


$$

**Caution:** To get a unit lower triangular matrix at the end, we have the following restriction while reducing a matrix $A$ to row echelon form:

- we can only add a multiple of the $1$st row to the $2$nd row ($R_2:=R_2+k R_1$), and

- the other elementary row operations (swapping or multiplying a row by a number) are not allowed.

### Example: Finding the LU Factorization of a 2x2 Matrix

#### Question

Given $[\begin{aligned}7 & 9 \\ −7 & −6\end{aligned}]$ find its LU decomposition.

#### Explanation

To find the matrices $L$ and $U,$ we reduce the matrix $A$ to row echelon form. Whilst doing this, we simultaneously write down the row operations applied to $A$ in terms of matrix multiplication using elementary matrices.

$$


\begin{aligned}𝐴 & =[\begin{aligned}7 & 9 \\ −7 & −6\end{aligned}] & 𝑅_{2} & :=𝑅_{2}+1⋅𝑅_{1}\,⟺\,\overset{\overset{[\begin{aligned}1 & 0 \\ 1 & 1\end{aligned}]}{}}{𝐸_{1}}⋅𝐴 \\ & ∼[\begin{aligned}7 & 9 \\ 0 & 3\end{aligned}] & & \\ & =𝑈 & & \end{aligned}


$$

The reduced matrix is upper triangular, so it is our matrix $U.$ Now, since $E_1A=U,$ we can invert $E_1$ to arrive at the desired LU factorization:

$$


\begin{aligned}𝐸_{1}𝐴 & =𝑈 \\ 𝐴 & =𝐸_{−11}^{}𝑈 \\ 𝐴 & =[\begin{aligned}1 & 0 \\ 1 & 1\end{aligned}]^{−1}𝑈 \\ 𝐴 & =\underset{𝐿}{\underset{}{[\begin{aligned}1 & 0 \\ −1 & 1\end{aligned}]}}\underset{𝑈}{\underset{}{[\begin{aligned}7 & 9 \\ 0 & 3\end{aligned}]}}\end{aligned}


$$

### Example: Finding the LU Factorization of a Singular 2x2 Matrix

#### Question

Given $[\begin{aligned}4 & 3 \\ 12 & 9\end{aligned}]$, find its LU decomposition.

#### Explanation

To find the matrices $L$ and $U,$ we reduce the matrix $A$ to row echelon form. Whilst doing this, we simultaneously write down the row operations applied to $A$ in terms of matrix multiplication using elementary matrices.

$$


\begin{aligned}𝐴 & =[\begin{aligned}4 & 3 \\ 12 & 9\end{aligned}] & 𝑅_{2} & :=𝑅_{2}+(−3)𝑅_{1}\,⟺\,\overset{\overset{[\begin{aligned}1 & 0 \\ −3 & 1\end{aligned}]}{}}{𝐸_{1}}⋅𝐴 \\ & ∼[\begin{aligned}4 & 3 \\ 0 & 0\end{aligned}] & & \\ & =𝑈. & & \end{aligned}


$$

The reduced matrix is upper triangular, so it is our matrix $U.$ Now, since $E_1A=U,$ we can invert $E_1$ to arrive at the desired LU factorization:

$$


\begin{aligned}𝐸_{1}𝐴 & =𝑈 \\ 𝐴 & =𝐸_{−11}^{}𝑈 \\ 𝐴 & =[\begin{aligned}1 & 0 \\ −3 & 1\end{aligned}]^{−1}𝑈 \\ 𝐴 & =\underset{𝐿}{\underset{}{[\begin{aligned}1 & 0 \\ 3 & 1\end{aligned}]}}\underset{𝑈}{\underset{}{[\begin{aligned}4 & 3 \\ 0 & 0\end{aligned}]}}.\end{aligned}


$$
