# Finding the Inverse of a 2x2 Matrix Using Row Operations

Source: https://www.mathacademy.com/topics/1728?courseId=145
Topic ID: 1728

## Prerequisites

- [Reduced Row Echelon Form](./1049-reduced-row-echelon-form.md)

## Lesson

### Introduction

Suppose we want to find the inverse of the matrix

$$


[\begin{aligned}1 & 2 \\ 3 & 7\end{aligned}]


$$

We can compute the inverse of $A$ using elementary row operations. There are two key advantages to using row operations to compute the inverse of a matrix:

1. The method works for any invertible matrix of any size, not just $2\times 2$ matrices.

2. It requires significantly less computation than some alternative methods. This is especially true for large matrices.

Here, we'll focus on the $2\times 2$ case. We use the following fact:

*The row operations that transform $A$ into the identity matrix $I_2$ also transform $I_2$ into $A^{-1}$*.

So, to find the inverse of $A,$ we proceed as follows:

**Step 1:** Write down $\color{blue}A$ and the identity matrix $I_2$ side-by-side, as shown below:

$$


\begin{aligned}1 & 2 & 1 & 0 \\ 3 & 7 & 0 & 1\end{aligned}


$$

**Step 2:** Apply the standard Gauss-Jordan method to transform the matrix $A$ into the identity matrix. We perform the same row operations on both matrices:

$$


\begin{aligned}[𝐴\,|\,𝐼_{2}\,] & =[\begin{matrix}1 & 2 & 1 & 0 \\ 3 & 7 & 0 & 1\end{matrix}] & 𝑅_{2} & :=𝑅_{2}+(−3)𝑅_{1} \\ & ∼[\begin{matrix}1 & 2 & 1 & 0 \\ 0 & 1 & −3 & 1\end{matrix}] & 𝑅_{1} & :=𝑅_{1}+(−2)𝑅_{2} \\ & ∼[\begin{matrix}1 & 0 & 7 & −2 \\ 0 & 1 & −3 & 1\end{matrix}] & & \\ & =[\,𝐼\,|\,𝐴^{−1}] & & \end{aligned}


$$

The matrix $A^{-1}$ is obtained on the right-hand side of our big matrix after the transformation. Therefore,

$$


[\begin{aligned}7 & −2 \\ −3 & 1\end{aligned}]


$$

We can easily check our result by computing $AA^{-1}\mathbin{:}$

$$


\begin{aligned}𝐴𝐴^{−1} & =[\begin{matrix}1 & 2 \\ 3 & 7\end{matrix}][\begin{matrix}7 & −2 \\ −3 & 1\end{matrix}]=[\begin{matrix}1 & 0 \\ 0 & 1\end{matrix}]\,✓\end{aligned}


$$

### Example: Transforming a 2x2 Matrix Into the Identity Matrix Using Row Operations

#### Question

Which of the following matrices are transformed into the $2\times 2$ identity matrix after applying the row operations $R_1 \leftrightarrow R_2 \,$ and $\, R_2:= R_2+(-1)R_1?$

$$


\begin{aligned}−2 & −1 \\ 1 & 0\end{aligned}


$$

#### Explanation

Let's apply the operations to each of the matrices:

$$


\begin{aligned}𝐴 & =[\begin{matrix}−2 & −1 \\ 1 & 0\end{matrix}] & 𝑅_{1} & ↔𝑅_{2} \\ & ∼[\begin{matrix}1 & 0 \\ −2 & −1\end{matrix}] & 𝑅_{2} & :=𝑅_{2}+(−1)𝑅_{1} \\ & ∼[\begin{matrix}1 & 0 \\ −3 & −1\end{matrix}] & & \\ & ≠𝐼\,× & & \\ 𝐵 & =[\begin{matrix}1 & 1 \\ 1 & 0\end{matrix}] & 𝑅_{1} & ↔𝑅_{2} \\ & ∼[\begin{matrix}1 & 0 \\ 1 & 1\end{matrix}] & 𝑅_{2} & :=𝑅_{2}+(−1)𝑅_{1} \\ & ∼[\begin{matrix}1 & 0 \\ 0 & 1\end{matrix}] & & \\ & =𝐼\,✓ & & \end{aligned}


$$

Therefore, the correct answer is "$B$ only".

### Example: Identifying the Inverse of a 2x2 Matrix Calculated Using Row Operations

#### Question

The inverse of the $2\times 2$ matrix $A$ is found using row operations, as shown below. Complete the process, and determine $A^{-1}.$

$$


\begin{aligned}[𝐴\,|\,𝐼\,] & =[\begin{matrix}1 & 1 & 1 & 0 \\ 1 & 2 & 0 & 1\end{matrix}] & 𝑅_{2} & :=𝑅_{2}+(−1)𝑅_{1} \\ & ∼[\begin{matrix}1 & 1 & 1 & 0 \\ 0 & 1 & −1 & 1\end{matrix}] & 𝑅_{1} & :=\underline{\hspace{3em}} \\ & ∼[\begin{matrix}1 & 0 & 𝑎 & 𝑎 \\ 0 & 1 & 𝑎 & 𝑎\end{matrix}] & & \end{aligned}


$$

#### Explanation

We write down $A$ and the identity matrix $I$ side-by-side (as shown below) and apply the standard Gauss-Jordan method to transform the matrix $A$ into the identity matrix. We perform the same row operations on both matrices:

$$


\begin{aligned}[𝐴\,|\,𝐼\,] & =[\begin{matrix}1 & 1 & 1 & 0 \\ 1 & 2 & 0 & 1\end{matrix}] & 𝑅_{2} & :=𝑅_{2}+(−1)𝑅_{1} \\ & ∼[\begin{matrix}1 & 1 & 1 & 0 \\ 0 & 1 & −1 & 1\end{matrix}] & 𝑅_{1} & :=𝑅_{1}+(−1)𝑅_{2} \\ & ∼[\begin{matrix}1 & 0 & 2 & −1 \\ 0 & 1 & −1 & 1\end{matrix}] & & \end{aligned}


$$

The matrix $A^{-1}$ is given by the right-hand side of our big matrix after all of the transformations have been completed. Therefore,

$$


[\begin{aligned}2 & −1 \\ −1 & 1\end{aligned}]


$$

### Example: Determining the Row Operations Required To Find the Inverse of a 2x2 Matrix

#### Question

The inverse of the matrix $A$ is found using row operations, as shown below. What are the row operations corresponding to each step?

$$


\begin{aligned}[𝐴\,|\,𝐼\,] & =[\begin{matrix}2 & 6 & 1 & 0 \\ 0 & 1 & 0 & 1\end{matrix}] & & \underline{\hspace{3em}} \\ & ∼[\begin{matrix}1 & 3 & \frac{1}{2} & 0 \\ 0 & 1 & 0 & 1\end{matrix}] & & \underline{\hspace{3em}} \\ & ∼[\begin{matrix}1 & 0 & \frac{1}{2} & −3 \\ 0 & 1 & 0 & 1\end{matrix}] & & \end{aligned}


$$

#### Explanation

We write down $A$ and the identity matrix $I$ side-by-side (as shown below) and apply the standard Gauss-Jordan method to transform the matrix $A$ into the identity matrix. We perform the same row operations on both matrices:

$$


\begin{aligned}[𝐴\,|\,𝐼\,] & =[\begin{matrix}2 & 6 & 1 & 0 \\ 0 & 1 & 0 & 1\end{matrix}] & 𝑅_{1} & :=\frac{1}{2}𝑅_{1} \\ & ∼[\begin{matrix}1 & 3 & \frac{1}{2} & 0 \\ 0 & 1 & 0 & 1\end{matrix}] & 𝑅_{1} & :=𝑅_{1}+(−3)𝑅_{2} \\ & ∼[\begin{matrix}1 & 0 & \frac{1}{2} & −3 \\ 0 & 1 & 0 & 1\end{matrix}] & & \end{aligned}


$$

The corresponding row operations are

$$


R_1 := \dfrac{1}{2}R_1, \qquad R_1 := R_1+(-3)R_2.


$$

The matrix $A^{-1}$ is given by the right-hand side of our big matrix after all of the transformations have been completed. Therefore,

$$


[\begin{aligned}\frac{1}{2} & −3 \\ 0 & 1\end{aligned}]


$$
