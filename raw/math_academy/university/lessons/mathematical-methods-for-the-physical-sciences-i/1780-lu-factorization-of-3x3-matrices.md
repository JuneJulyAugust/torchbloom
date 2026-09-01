# LU Factorization of 3x3 Matrices

Source: https://www.mathacademy.com/topics/1780?courseId=154
Topic ID: 1780

## Prerequisites

- [LU Factorization of 2x2 Matrices](./1779-lu-factorization-of-2x2-matrices.md)
- [Row Operations on 3x3 Matrices as Products of Elementary Matrices](./2089-row-operations-on-3x3-matrices-as-products-of-elementary-matrices.md)

## Lesson

### Introduction

Recall that LU factorization involves writing a matrix $A$ as a product of two matrices $L$ and $U,$ where

- $\begin{aligned}1 & 0 & 0 \\ ∗ & 1 & 0 \\ ∗ & ∗ & 1\end{aligned}$ is a *unit lower triangular matrix* (a lower triangular matrix that has only $1$'s on the main diagonal), and

- $\begin{aligned}∗ & ∗ & ∗ \\ 0 & ∗ & ∗ \\ 0 & 0 & ∗\end{aligned}$ is an *upper triangular matrix*.

For example, suppose we're given the matrix $\begin{aligned}1 & −1 & −2 \\ 0 & 2 & −3 \\ −2 & 2 & 7\end{aligned}$ To perform LU factorization, we need to write $A$ as

$$


\begin{aligned}1 & −1 & −2 \\ 0 & 2 & −3 \\ −2 & 2 & 7\end{aligned}


$$

As usual, to find the matrices $L$ and $U,$ we can reduce the matrix $A$ to *echelon form* while simultaneously performing the same elementary row operations on the identity matrix:

$$


\begin{aligned}𝐴 & =\begin{matrix}1 & −1 & −2 \\ 0 & 2 & −3 \\ −2 & 2 & 7\end{matrix} & 𝑅_{3} & :=𝑅_{3}+2𝑅_{1} & ⇔ & \,\overset{\begin{matrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 2 & 0 & 1\end{matrix}}{𝐸_{1}}⋅𝐴 \\ & ∼\begin{matrix}1 & −1 & −2 \\ 0 & 2 & −3 \\ 0 & 0 & 3\end{matrix}=𝑈 & & & & \end{aligned}


$$

The reduced matrix is upper triangular, so it is our matrix $U.$ Now, since $E_1A=U,$ we can invert $E_1$ to arrive at the desired LU factorization:

$$


\begin{aligned}𝐸_{1}𝐴 & =𝑈 \\ 𝐴 & =𝐸_{−11}𝑈 \\ 𝐴 & =\begin{matrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 2 & 0 & 1\end{matrix}^{−1}𝑈 \\ 𝐴 & =\underset{𝐿}{\begin{matrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ −2 & 0 & 1\end{matrix}}\underset{𝑈}{\begin{matrix}1 & −1 & −2 \\ 0 & 2 & −3 \\ 0 & 0 & 3\end{matrix}}\end{aligned}


$$

**Caution:** In order to get a unit lower triangular matrix at the end, we have the following restriction while reducing a matrix $A$ to its *echelon form*:

- we can only add multiples of higher rows to lower rows ($R_j:=R_j+k R_i$ where $i < j$), and

- the other elementary row operations (swapping or multiplying a row by a number) are not allowed.

### Example: Finding the LU Factorization Using a Single Elementary Row Operation

#### Question

Given that $\begin{aligned}4 & 1 & −6 \\ 0 & 3 & 1 \\ 0 & 6 & −2\end{aligned}$ has the LU decomposition $A=LU,$ then $L=$

#### Explanation

To find the matrices $L$ and $U,$ we reduce the matrix $A$ to row echelon form. Whilst doing this, we simultaneously write down the row operations applied to $A$ in terms of matrix multiplication using elementary matrices.

$$


\begin{aligned}𝐴 & =\begin{matrix}4 & 1 & −6 \\ 0 & 3 & 1 \\ 0 & 6 & −2\end{matrix} & 𝑅_{3} & :=𝑅_{3}+(−2)𝑅_{2} & ⟺ & \,\overset{\begin{matrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & −2 & 1\end{matrix}}{𝐸_{1}}⋅𝐴 \\ & ∼\begin{matrix}4 & 1 & −6 \\ 0 & 3 & 1 \\ 0 & 0 & −4\end{matrix} & & & & \\ & =𝑈 & & & & \end{aligned}


$$

The reduced matrix is upper triangular, so it is our matrix $U.$ Now, since $E_1A=U,$ we can invert $E_1$ to arrive at the desired LU factorization:

$$


\begin{aligned}𝐸_{1}𝐴 & =𝑈 \\ 𝐴 & =𝐸_{−11}𝑈 \\ 𝐴 & =\begin{matrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & −2 & 1\end{matrix}^{−1}𝑈 \\ 𝐴 & =\underset{𝐿}{\begin{matrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 2 & 1\end{matrix}}\underset{𝑈}{\begin{matrix}4 & 1 & −6 \\ 0 & 3 & 1 \\ 0 & 0 & −4\end{matrix}}\end{aligned}


$$

### Example: Finding the Lower Triangular Matrix Given the Elementary Row Operations

#### Question

Suppose that a $3 \times 3$ matrix $F$ is reduced to row echelon form using the following elementary row operations, applied in the order in which they appear:

$$


R_2:=R_2+R_1, \qquad R_3:=R_3+2R_1


$$

Given that $F$ has the LU factorization $F=LU,$ then $L=$

#### Explanation

Applying $R_2:=R_2 + {\color{red}1} \cdot R_1$ and then $R_3:=R_3+ {\color{red}2} \cdot R_1$ is equivalent to multiplying $F$ from the left by the following elementary matrices:

$$


\begin{aligned}1 & 0 & 0 \\ 0 & 1 & 0 \\ 2 & 0 & 1\end{aligned}


$$

Now, since $E_2E_1F=U,$ we can invert $E_2$ and $E_1$ to arrive at the desired LU factorization:

$$


\begin{aligned}𝐸_{2}𝐸_{1}𝐹 & =𝑈 \\ 𝐸_{1}𝐹 & =𝐸_{−12}𝑈 \\ 𝐹 & =𝐸_{−11}𝐸_{−12}𝑈 \\ 𝐹 & =\begin{matrix}1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1\end{matrix}^{−1}\begin{matrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 2 & 0 & 1\end{matrix}^{−1}𝑈 \\ 𝐹 & =\begin{matrix}1 & 0 & 0 \\ −1 & 1 & 0 \\ 0 & 0 & 1\end{matrix}\begin{matrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ −2 & 0 & 1\end{matrix}𝑈 \\ 𝐹 & =\underset{𝐿}{\begin{matrix}1 & 0 & 0 \\ −1 & 1 & 0 \\ −2 & 0 & 1\end{matrix}}⋅𝑈\end{aligned}


$$

### Example: Finding the LU Factorization Using Two or More Elementary Row Operations

#### Question

Given that $\begin{aligned}4 & 8 & 0 \\ 5 & 11 & −6 \\ 0 & −4 & 16\end{aligned}$ has the LU decomposition $A=LU,$ then $L=$

#### Explanation

To find the matrices $L$ and $U,$ we reduce the matrix $A$ to row echelon form. Whilst doing this, we simultaneously write down the row operations applied to $A$ in terms of matrix multiplication using elementary matrices.

$$


\begin{aligned}𝐴 & =\begin{matrix}4 & 8 & 0 \\ 5 & 11 & −6 \\ 0 & −4 & 16\end{matrix} & 𝑅_{2} & :=𝑅_{2}+(−\frac{5}{4})𝑅_{1} & ⟺ & \,\overset{\begin{matrix}1 & 0 & 0 \\ −\frac{5}{4} & 1 & 0 \\ 0 & 0 & 1\end{matrix}}{𝐸_{1}}⋅𝐴 \\ & ∼\begin{matrix}4 & 8 & 0 \\ 0 & 1 & −6 \\ 0 & −4 & 16\end{matrix} & 𝑅_{3} & :=𝑅_{3}+4𝑅_{2} & ⟺ & \,\overset{\begin{matrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 4 & 1\end{matrix}}{𝐸_{2}}⋅𝐸_{1}⋅𝐴 \\ & ∼\begin{matrix}4 & 8 & 0 \\ 0 & 1 & −6 \\ 0 & 0 & −8\end{matrix} & & & & \\ & =𝑈 & & & & \end{aligned}


$$

The reduced matrix is upper triangular, so it is our matrix $U.$ Now, since $E_2E_1A=U,$ we can invert $E_2$ and $E_1$ to arrive at the desired LU factorization:

$$


\begin{aligned}𝐸_{2}𝐸_{1}𝐴 & =𝑈 \\ 𝐸_{1}𝐴 & =𝐸_{−12}𝑈 \\ 𝐴 & =𝐸_{−11}𝐸_{−12}𝑈 \\ 𝐴 & =\begin{matrix}1 & 0 & 0 \\ −\frac{5}{4} & 1 & 0 \\ 0 & 0 & 1\end{matrix}^{−1}\begin{matrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 4 & 1\end{matrix}^{−1}𝑈 \\ 𝐴 & =\begin{matrix}1 & 0 & 0 \\ \frac{5}{4} & 1 & 0 \\ 0 & 0 & 1\end{matrix}\begin{matrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & −4 & 1\end{matrix}𝑈 \\ 𝐴 & =\underset{𝐿}{\begin{matrix}1 & 0 & 0 \\ \frac{5}{4} & 1 & 0 \\ 0 & −4 & 1\end{matrix}}\underset{𝑈}{\begin{matrix}4 & 8 & 0 \\ 0 & 1 & −6 \\ 0 & 0 & −8\end{matrix}}\end{aligned}


$$
