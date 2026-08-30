# Inverses of 2x2 Matrices

Source: https://www.mathacademy.com/topics/864?courseId=101
Topic ID: 864

## Prerequisites

- [Scalar Multiplication of Matrices](./146-scalar-multiplication-of-matrices.md)
- [The Determinant of a 2x2 Matrix](./152-the-determinant-of-a-2x2-matrix.md)
- [Solving Quadratic Equations by Factoring](../algebra-i/375-solving-quadratic-equations-by-factoring.md)
- [Introduction to the Inverse of a Matrix](./863-introduction-to-the-inverse-of-a-matrix.md)

## Lesson

### Introduction

Given a $2 \times 2$ matrix

$$


[\begin{aligned}𝑎 & 𝑏 \\ 𝑐 & 𝑑\end{aligned}]


$$

the **inverse** of $A$ can be found using the following formula:

$$


\begin{aligned}𝐴^{−1} & =\frac{1}{det(𝐴)}[\begin{aligned}𝑑 & −𝑏 \\ −𝑐 & 𝑎\end{aligned}].\end{aligned}


$$

### Example: Calculating the Inverse of a 2x2 Matrix

#### Question

Calculate $A^{-1},$ where

$$


[\begin{aligned}1 & 0 \\ −2 & 1\end{aligned}]


$$

#### Explanation

Given a $2 \times 2$ matrix

$$


[\begin{aligned}𝑎 & 𝑏 \\ 𝑐 & 𝑑\end{aligned}]


$$

the inverse of $A$ can be found using the following formula:

$$


\begin{aligned}𝐴^{−1} & =\frac{1}{det(𝐴)}[\begin{aligned}𝑑 & −𝑏 \\ −𝑐 & 𝑎\end{aligned}].\end{aligned}


$$

First, we compute the determinant:

$$


\det(A) = 1 \cdot 1 - 0 \cdot (-2) = 1


$$

Using the formula, then, the inverse is given by

$$


\begin{aligned}𝐴^{−1} & =\frac{1}{det(𝐴)}[\begin{aligned}𝑑 & −𝑏 \\ −𝑐 & 𝑎\end{aligned}]. \\ & =\frac{1}{1}[\begin{aligned}1 & −0 \\ −(−2) & 1\end{aligned}] \\ & =[\begin{aligned}1 & 0 \\ 2 & 1\end{aligned}].\end{aligned}


$$

We can verify the result as follows:

$$


\begin{aligned}𝐴𝐴^{−1} & =[\begin{aligned}1 & 0 \\ −2 & 1\end{aligned}][\begin{aligned}1 & 0 \\ 2 & 1\end{aligned}] \\ & =[\begin{aligned}1 & 0 \\ 0 & 1\end{aligned}] \\ & =𝐼_{2}\,✓ \\ 𝐴^{−1}𝐴 & =[\begin{aligned}1 & 0 \\ 2 & 1\end{aligned}][\begin{aligned}1 & 0 \\ −2 & 1\end{aligned}] \\ & =[\begin{aligned}1 & 0 \\ 0 & 1\end{aligned}] \\ & =𝐼_{2}\,✓\end{aligned}


$$

### Invertible and Singular Matrices

Remember that the inverse of a $2\times 2$ matrix $[\begin{aligned}𝑎 & 𝑏 \\ 𝑐 & 𝑑\end{aligned}]$ is given by

$$


[\begin{aligned}𝑑 & −𝑏 \\ −𝑐 & 𝑎\end{aligned}]


$$

If $\det(A)=0,$ then $A^{-1}$ doesn't exist since we can't divide by zero. In fact, we have the following statement:

$A^{-1}$ exists if and only if $\det(A) \neq 0.$

A matrix that has an inverse is called **invertible**. Otherwise, the matrix doesn't have an inverse and is called **non-invertible**. A square matrix that is non-invertible is called **singular**.

### Example: Identifying Singular Matrices

#### Question

Which of the matrices below are singular?

$$


[\begin{aligned}1 & 1 \\ 1 & 1\end{aligned}]


$$

#### Explanation

- For the matrix $A$, we have Because $\det(A)=0,$ we conclude that $A$ is not invertible. Since $A$ is a square matrix that is not invertible, we also say that $A$ is singular.

- The matrix $B$ is a $3 \times 2$ matrix. So, it is not invertible. Since the matrix is not square, we can't say that it's singular.

- For the matrix $C$, we have Because $\det(C) \neq 0,$ we conclude that $C$ is invertible.

Therefore, only $A$ is singular.

### Example: Solving for a Variable in a Singular Matrix

#### Question

If $[\begin{aligned}1−𝑘 & 2 \\ 2 & 1−𝑘\end{aligned}]$ is a singular matrix, calculate the value(s) of $k.$

#### Explanation

The matrix $A$ is singular if and only if $\det(A)=0.$ Calculating the determinant, we get

$$


\begin{aligned}det(𝐴) & =(1−𝑘)(1−𝑘)−4 \\ & =𝑘^{2}−2𝑘−3.\end{aligned}


$$

Now, we set the determinant equal to $0$ and solve for $k\mathbin{:}$

$$


\begin{aligned}𝑘^{2}−2𝑘−3 & =0 \\ (𝑘−3)(𝑘+1) & =0 \\ 𝑘 & =3,−1\end{aligned}


$$

Therefore, the values of $k$ are $k=3$ and $k=-1.$

### Verifying the Formula

Given a matrix $[\begin{aligned}𝑎 & 𝑏 \\ 𝑐 & 𝑑\end{aligned}]$ we have been using the following formula to compute the inverse:

$$


[\begin{aligned}𝑑 & −𝑏 \\ −𝑐 & 𝑎\end{aligned}]


$$

To check that this formula is correct for a general matrix $A$, we need to verify that

$$


AA^{-1} = A^{-1}A = I_2.


$$

First, we compute $A^{-1}A\mathbin{:}$

$$


\begin{aligned}𝐴^{−1}⋅𝐴 & =\frac{1}{𝑎𝑑−𝑏𝑐}[\begin{aligned}𝑑 & −𝑏 \\ −𝑐 & 𝑎\end{aligned}]⋅[\begin{aligned}𝑎 & 𝑏 \\ 𝑐 & 𝑑\end{aligned}] \\ & =\frac{1}{𝑎𝑑−𝑏𝑐}[\begin{aligned}𝑎𝑑−𝑏𝑐 & 0 \\ 0 & −𝑏𝑐+𝑎𝑑\end{aligned}] \\ & =[\begin{aligned}1 & 0 \\ 0 & 1\end{aligned}] \\ & =𝐼_{2}\,✓\end{aligned}


$$

Then, we compute $A A^{-1}\mathbin{:}$

$$


\begin{aligned}𝐴⋅𝐴^{−1} & =[\begin{aligned}𝑎 & 𝑏 \\ 𝑐 & 𝑑\end{aligned}]⋅\frac{1}{𝑎𝑑−𝑏𝑐}[\begin{aligned}𝑑 & −𝑏 \\ −𝑐 & 𝑎\end{aligned}] \\ & =\frac{1}{𝑎𝑑−𝑏𝑐}[\begin{aligned}𝑎 & 𝑏 \\ 𝑐 & 𝑑\end{aligned}]⋅[\begin{aligned}𝑑 & −𝑏 \\ −𝑐 & 𝑎\end{aligned}] \\ & =\frac{1}{𝑎𝑑−𝑏𝑐}[\begin{aligned}𝑎𝑑−𝑏𝑐 & 0 \\ 0 & −𝑏𝑐+𝑎𝑑\end{aligned}] \\ & =[\begin{aligned}1 & 0 \\ 0 & 1\end{aligned}] \\ & =𝐼_{2}\,✓\end{aligned}


$$

So, we have verified that

$$


AA^{-1} = A^{-1}A = I_2,


$$

and we can be sure that the given formula is the correct formula for $A^{-1}.$
