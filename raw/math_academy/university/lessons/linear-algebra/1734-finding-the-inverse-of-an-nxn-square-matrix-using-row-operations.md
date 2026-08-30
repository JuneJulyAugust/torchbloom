# Finding the Inverse of an NxN Square Matrix Using Row Operations

Source: https://www.mathacademy.com/topics/1734?courseId=55
Topic ID: 1734

## Prerequisites

- [Finding the Inverse of a 3x3 Matrix Using Row Operations](./1732-finding-the-inverse-of-a-3x3-matrix-using-row-operations.md)

## Lesson

### Introduction

We can find the inverse of a $3 \times 3$ matrix $A$ using elementary row operations on the augmented matrix

$$


[A\, |\, I],


$$

where $I$ is the $3 \times 3$ identity matrix. We do this by transforming the left-hand side of the augmented matrix into the identity matrix, which gives an augmented matrix of the form

$$


[ I\, |\, A^{-1}].


$$

As it turns out, this method works for any invertible matrix!

For example, suppose we want to find the inverse of the $4\times 4$ matrix $A,$ given by

$$


\begin{aligned}1 & 1 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 3 & 0 \\ 0 & 0 & 0 & 1\end{aligned}


$$

We write down $A$ and the identity matrix $I$, as shown below. Then, we apply the standard Gauss-Jordan method to transform $A$ into the identity matrix. We perform the same row operations on both matrices:

Therefore, the inverse matrix is

$$


\begin{aligned}1 & −1 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & \frac{1}{3} & 0 \\ 0 & 0 & 0 & 1\end{aligned}


$$

### Example: Transforming a Matrix Into the Identity Matrix Using Row Operations

#### Question

$$


\begin{aligned}1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 5 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0\end{aligned}


$$

Find the row operations that transform the matrix $A$ above into the identity matrix.

#### Explanation

Let's consider the augmented matrix $[A\,|\,I],$ where $I$ is the $4 \times 4$ identity matrix. Then, by applying the following row operations, we obtain

$$


\begin{aligned}[𝐴\,|\,𝐼\,] & =\begin{aligned}1 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 & 0 & 1 & 0 & 0 \\ 5 & 0 & 1 & 0 & 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 & 0 & 0 & 0 & 1\end{aligned} & & 𝑅_{3}:=𝑅_{3}+(−5)𝑅_{1} \\ & ∼\begin{aligned}1 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 & 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 & −5 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 & 0 & 0 & 0 & 1\end{aligned} & & 𝑅_{2}↔𝑅_{4} \\ & ∼\begin{aligned}1 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 & −5 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 & 0 & 1 & 0 & 0\end{aligned} & & \\ & =\,[𝐼\,|\,𝐴^{−1}]. & & \end{aligned}


$$

Therefore, the required row operations are $R_3:= R_3 + (-5) R_1$ and $R_2 \leftrightarrow R_4,$ while

$$


\begin{aligned}1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ −5 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0\end{aligned}


$$

### Example: Determining the Row Operations Required to Find the Inverse of a 4x4 Matrix

#### Question

The inverse $B$ of the $4 \times 4$ matrix $A$ is found using row operations, as shown below. Complete the process, and determine the value of $b_{11}+b_{21}+b_{31}.$

$$


\begin{aligned}[𝐴\,|\,𝐼] & =\begin{aligned}1 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\ −1 & 1 & 0 & 0 & 0 & 1 & 0 & 0 \\ 0 & 3 & 1 & 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1\end{aligned} & & 𝑅_{2}:=𝑅_{2}+𝑅_{1} \\ & ∼\begin{aligned}1 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 1 & 1 & 0 & 0 \\ 0 & 3 & 1 & 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1\end{aligned} & & 𝑅_{3}:=_________ \\ & ∼\begin{aligned}1 & 0 & 0 & 0 & 𝑎 & 𝑎 & 𝑎 & 𝑎 \\ 0 & 1 & 0 & 0 & 𝑎 & 𝑎 & 𝑎 & 𝑎 \\ 0 & 0 & 1 & 0 & 𝑎 & 𝑎 & 𝑎 & 𝑎 \\ 0 & 0 & 0 & 1 & 𝑎 & 𝑎 & 𝑎 & 𝑎\end{aligned} & & \end{aligned}


$$

#### Explanation

We write down $A$ and the identity matrix $I$ side-by-side (as shown below) and apply the standard Gauss-Jordan method to transform the matrix $A$ into the identity matrix. We perform the same row operations on both matrices:

$$


\begin{aligned}[𝐴\,|\,𝐼] & =\begin{aligned}1 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\ −1 & 1 & 0 & 0 & 0 & 1 & 0 & 0 \\ 0 & 3 & 1 & 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1\end{aligned} & & 𝑅_{2}:=𝑅_{2}+𝑅_{1} \\ & ∼\begin{aligned}1 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 1 & 1 & 0 & 0 \\ 0 & 3 & 1 & 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1\end{aligned} & & 𝑅_{3}:=𝑅_{3}−3𝑅_{2} \\ & ∼\begin{aligned}1 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 1 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 & −3 & −3 & 1 & 0 \\ 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1\end{aligned} & & \end{aligned}


$$

The matrix $B=A^{-1}$ is given by the right-hand side of our big matrix after all of the transformations have been completed:

$$


\begin{aligned}1 & 0 & 0 & 0 \\ 1 & 1 & 0 & 0 \\ −3 & −3 & 1 & 0 \\ 0 & 0 & 0 & 1\end{aligned}


$$

Therefore,

$$


b_{11}+b_{21}+b_{31} = 1 +1+ (-3) = -1.


$$

### Example: Finding the Inverse of a Square Matrix Using Row Operations

#### Question

Find the inverse of the matrix $\begin{aligned}1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & −3 & 1 & 0 \\ 0 & 0 & −1 & 1\end{aligned}$

#### Explanation

We write down $B$ and the identity matrix $I$ side-by-side (as shown below) and apply the standard Gauss-Jordan method to transform the matrix $B$ into the identity matrix. We perform the same row operations on both matrices:

The matrix $B^{-1}$ is given by the right-hand side of our big matrix after all of the transformations have been completed:

$$


\begin{aligned}1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 3 & 1 & 0 \\ 0 & 3 & 1 & 1\end{aligned}


$$
