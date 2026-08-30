# Finding the Inverse of a 3x3 Matrix Using Row Operations

Source: https://www.mathacademy.com/topics/1732?courseId=154
Topic ID: 1732

## Prerequisites

- [Finding the Inverse of a 2x2 Matrix Using Row Operations](./1728-finding-the-inverse-of-a-2x2-matrix-using-row-operations.md)

## Lesson

### Introduction

Given the matrix $\begin{aligned}1 & 0 & 0 \\ 0 & 1 & 0 \\ 1 & 0 & 4\end{aligned}$, we can find its inverse just by performing some row operations.

To start, we consider the augmented matrix

$$


\begin{aligned}1 & 0 & 0 & 1 & 0 & 0 \\ 0 & 1 & 0 & 0 & 1 & 0 \\ 1 & 0 & 4 & 0 & 0 & 1\end{aligned}


$$

where $I_3$ is the $3\times 3$ identity matrix.

We can find the inverse of $A$ by performing row operations on this augmented matrix. The idea is as follows:

1. Perform row operations to transform the left-hand side of the augmented matrix to reduced row echelon form, which means reducing it to the identity matrix

2. Simultaneously, perform the same row operations on the right-hand side of the augmented matrix

3. When the left-hand side is in reduced row echelon form, the right-hand side will be the inverse of $A$

Let's now try this for our example.

$$


\begin{aligned}[𝐴\,|\,𝐼_{3}] & =\begin{aligned}1 & 0 & 0 & 1 & 0 & 0 \\ 0 & 1 & 0 & 0 & 1 & 0 \\ 1 & 0 & 4 & 0 & 0 & 1\end{aligned} & 𝑅_{3} & :=𝑅_{3}+(−1)𝑅_{1} \\ & ∼\begin{aligned}1 & 0 & 0 & 1 & 0 & 0 \\ 0 & 1 & 0 & 0 & 1 & 0 \\ 0 & 0 & 4 & −1 & 0 & 1\end{aligned} & 𝑅_{3} & :=\frac{1}{4}𝑅_{3} \\ & ∼\begin{aligned}1 & 0 & 0 & 1 & 0 & 0 \\ 0 & 1 & 0 & 0 & 1 & 0 \\ 0 & 0 & 1 & −\frac{1}{4} & 0 & \frac{1}{4}\end{aligned}. & & \end{aligned}


$$

We are left with another augmented matrix $[I_3\, |\, {\color{blue}A^{-1}}]$. So the inverse of the matrix is

$$


\begin{aligned}1 & 0 & 0 \\ 0 & 1 & 0 \\ −\frac{1}{4} & 0 & \frac{1}{4}\end{aligned}


$$

We can easily check that this is indeed the inverse by computing $AA^{-1}$ and showing that it equals $I_3$. Try it for yourself!

This method works for any invertible $3\times 3$ matrix. Moreover, it is significantly more efficient than many other methods for finding the inverse.

### Example: Transforming a 3x3 Matrix Into the Identity Matrix Using Row Operations

#### Question

Given the matrix $\begin{aligned}1 & 0 & 4 \\ 0 & 1 & 0 \\ 0 & 0 & −1\end{aligned}$ find the row operations that transform $A$ into the $3 \times 3$ identity matrix.

#### Explanation

We consider the augmented matrix $[A\,|\,I]$ where $I$ is the $3\times 3$ identity. Applying the indicated row operations we have

Therefore, the required row operations are $R_3:= (-1) R_3$ and $R_1:= R_1+(-4)R_3,$ and inverse matrix is

$$


\begin{aligned}1 & 0 & 4 \\ 0 & 1 & 0 \\ 0 & 0 & −1\end{aligned}


$$

### Example: Identifying the Inverse of a 3x3 Matrix Calculated Using Row Operations

#### Question

The inverse of the $3 \times 3$ matrix $K$ is found using row operations, as shown below. Complete the process, and determine $K^{-1}.$

$$


\begin{aligned}[𝐾\,|\,𝐼\,] & =\begin{aligned}1 & 0 & 0 & 1 & 0 & 0 \\ 5 & 3 & 0 & 0 & 1 & 0 \\ 0 & 0 & 1 & 0 & 0 & 1\end{aligned} & 𝑅_{2} & :=𝑅_{2}+(−5)𝑅_{1} \\ & ∼\begin{aligned}1 & 0 & 0 & 1 & 0 & 0 \\ 0 & 3 & 0 & −5 & 1 & 0 \\ 0 & 0 & 1 & 0 & 0 & 1\end{aligned} & 𝑅_{2} & :=___________ \\ & ∼\begin{aligned}1 & 0 & 0 & 𝑎 & 𝑎 & 𝑎 \\ 0 & 1 & 0 & 𝑎 & 𝑎 & 𝑎 \\ 0 & 0 & 1 & 𝑎 & 𝑎 & 𝑎\end{aligned} & & \end{aligned}


$$

#### Explanation

We write down $K$ and the identity matrix $I$ side-by-side (as shown below) and apply the standard Gauss-Jordan method to transform the matrix $K$ into the identity matrix. We perform the same row operations on both matrices:

$$


\begin{aligned}[𝐾\,|\,𝐼\,] & =\begin{aligned}1 & 0 & 0 & 1 & 0 & 0 \\ 5 & 3 & 0 & 0 & 1 & 0 \\ 0 & 0 & 1 & 0 & 0 & 1\end{aligned} & 𝑅_{2} & :=𝑅_{2}+(−5)𝑅_{1} \\ & ∼\begin{aligned}1 & 0 & 0 & 1 & 0 & 0 \\ 0 & 3 & 0 & −5 & 1 & 0 \\ 0 & 0 & 1 & 0 & 0 & 1\end{aligned} & 𝑅_{2} & :=\frac{1}{3}𝑅_{2} \\ & ∼\begin{aligned}1 & 0 & 0 & 1 & 0 & 0 \\ 0 & 1 & 0 & −\frac{5}{3} & \frac{1}{3} & 0 \\ 0 & 0 & 1 & 0 & 0 & 1\end{aligned} & & \end{aligned}


$$

The matrix $K^{-1}$ is given by the right-hand side of our big matrix after all of the transformations have been completed. Therefore,

$$


\begin{aligned}1 & 0 & 0 \\ −\frac{5}{3} & \frac{1}{3} & 0 \\ 0 & 0 & 1\end{aligned}


$$

### Example: Determining the Row Operations Required To Find the Inverse of a 3x3 Matrix

#### Question

The inverse of the matrix $H$ is found using row operations, as shown below. What are the row operations corresponding to each step?

$$


\begin{aligned}[𝐻\,|\,𝐼] & =\begin{aligned}1 & 0 & −1 & 1 & 0 & 0 \\ 0 & 1 & 0 & 0 & 1 & 0 \\ −3 & 0 & 2 & 0 & 0 & 1\end{aligned} & 𝑅_{3} & :=___________ \\ & ∼\begin{aligned}1 & 0 & −1 & 1 & 0 & 0 \\ 0 & 1 & 0 & 0 & 1 & 0 \\ 0 & 0 & −1 & 3 & 0 & 1\end{aligned} & 𝑅_{3} & :=(−1)𝑅_{3} \\ & ∼\begin{aligned}1 & 0 & −1 & 1 & 0 & 0 \\ 0 & 1 & 0 & 0 & 1 & 0 \\ 0 & 0 & 1 & −3 & 0 & −1\end{aligned} & 𝑅_{1} & :=___________ \\ & ∼\begin{aligned}1 & 0 & 0 & −2 & 0 & −1 \\ 0 & 1 & 0 & 0 & 1 & 0 \\ 0 & 0 & 1 & −3 & 0 & −1\end{aligned} & & \end{aligned}


$$

#### Explanation

We write down $H$ and the identity matrix $I$ side-by-side (as shown below) and apply the standard Gauss-Jordan method to transform the matrix $H$ into the identity matrix. We perform the same row operations on both matrices:

$$


\begin{aligned}[𝐻\,|\,𝐼] & =\begin{aligned}1 & 0 & −1 & 1 & 0 & 0 \\ 0 & 1 & 0 & 0 & 1 & 0 \\ −3 & 0 & 2 & 0 & 0 & 1\end{aligned} & 𝑅_{3} & :=𝑅_{3}+3𝑅_{1} \\ & ∼\begin{aligned}1 & 0 & −1 & 1 & 0 & 0 \\ 0 & 1 & 0 & 0 & 1 & 0 \\ 0 & 0 & −1 & 3 & 0 & 1\end{aligned} & 𝑅_{3} & :=(−1)𝑅_{3} \\ & ∼\begin{aligned}1 & 0 & −1 & 1 & 0 & 0 \\ 0 & 1 & 0 & 0 & 1 & 0 \\ 0 & 0 & 1 & −3 & 0 & −1\end{aligned} & 𝑅_{1} & :=𝑅_{1}+𝑅_{3} \\ & ∼\begin{aligned}1 & 0 & 0 & −2 & 0 & −1 \\ 0 & 1 & 0 & 0 & 1 & 0 \\ 0 & 0 & 1 & −3 & 0 & −1\end{aligned} & & \end{aligned}


$$

The corresponding row operations are

$$


R_3 := R_3 + 3R_1, \qquad R_1 := R_1+R_3.


$$

The matrix $H^{-1}$ is given by the right-hand side of our big matrix after all of the transformations have been completed. Therefore,

$$


\begin{aligned}−2 & 0 & −1 \\ 0 & 1 & 0 \\ −3 & 0 & −1\end{aligned}


$$
