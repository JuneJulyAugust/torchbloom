# Row Operations on 3x3 Matrices as Products of Elementary Matrices

Source: https://www.mathacademy.com/topics/2089?courseId=55
Topic ID: 2089

## Prerequisites

- [Row Operations on 2x2 Matrices as Products of Elementary Matrices](./1727-row-operations-on-2x2-matrices-as-products-of-elementary-matrices.md)
- [Elementary 3x3 Matrices](./1731-elementary-3x3-matrices.md)

## Lesson

### Introduction

Applying a row operation to any $3\times 3$ matrix is the same as *pre-multiplying* (multiplying on the left) the matrix by the corresponding elementary matrix.

For instance, if we wish to swap the first row and the second row of a $3\times 3$ matrix $A,$ we pre-multiply $A$ by the corresponding elementary matrix

$$


\begin{aligned}0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1\end{aligned}


$$

to get $E_1 A.$

To perform a sequence of row operations to a $3\times 3$ matrix, we pre-multiply the matrix by the elementary matrix corresponding to the first operation, and then pre-multiply the result by the elementary matrix corresponding to the second operation.

For instance, given a $3 \times 3$ matrix $A,$ suppose that we would like to multiply the second row by $2$ and then add $3$ times the first row to the second row. To do this, we first pre-multiply $A$ by

$$


\begin{aligned}1 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1\end{aligned}


$$

to get $E_2 A.$ Then we pre-multiply the result by

$$


\begin{aligned}1 & 0 & 0 \\ 3 & 1 & 0 \\ 0 & 0 & 1\end{aligned}


$$

to get $E_3 E_2 A.$

### Example: Finding the Row Operation Equivalent To Left Multiplication by an Elementary Matrix

#### Question

Consider $\begin{aligned}1 & 0 & 0 \\ 0 & 1 & 7 \\ 0 & 0 & 1\end{aligned}$ and a $3\times 3$ matrix $A.$ Find the row operation that, when applied to $A,$ is equivalent to multiplying $A$ by the given elementary matrix $E$ from the left.

#### Explanation

The given matrix $E$ is obtained by taking the second row of $I$ and adding $7$ times the third row:

$$


\begin{aligned}𝐼 & =\begin{aligned}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{aligned} & 𝑅_{2} & :=𝑅_{2}+7𝑅_{3} \\ & ∼\begin{aligned}1 & 0 & 0 \\ 0 & 1 & 7 \\ 0 & 0 & 1\end{aligned} & & \\ & =𝐸 & & \end{aligned}


$$

Therefore, $EA$ is equivalent to applying the elementary row operation $R_2:=R_2+7R_3$ to $A.$

### Example: Finding the Matrix Left Multiplication Equivalent To a Given Row Operation

#### Question

Suppose we are applying the elementary row operation $R_2:=R_2-2R_1$ to a $3\times 3$ matrix $A.$ What is the equivalent notation in terms of matrix multiplication?

#### Explanation

We need to find a matrix $E$ such that $EA$ is equivalent to applying the elementary row operation $R_2:= R_2-2R_1$ to $A.$

To find $E,$ we apply the given row operation to the identity matrix as follows:

$$


\begin{aligned}𝐼 & =\begin{aligned}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{aligned} & 𝑅_{2} & :=𝑅_{2}−2𝑅_{1} \\ & ∼\begin{aligned}1 & 0 & 0 \\ −2 & 1 & 0 \\ 0 & 0 & 1\end{aligned} & & \\ & =𝐸 & & \end{aligned}


$$

Therefore, the equivalent notation in terms of matrix multiplication is $EA\mathbin{:}$

$$


\begin{aligned}1 & 0 & 0 \\ −2 & 1 & 0 \\ 0 & 0 & 1\end{aligned}


$$

### Example: Finding the Matrix Left Multiplication Equivalent To a Sequence of Row Operations

#### Question

Suppose we are applying these two elementary row operations, in the given order, to a $3\times 3$ matrix $A\mathbin{:}$

$$


R_2\leftrightarrow R_3, \qquad R_1:=6R_1


$$

Find the equivalent notation in terms of matrix multiplication.

#### Explanation

First, let's find the elementary matrices corresponding to the two given elementary row operations.

- The first operation is $R_2\leftrightarrow R_3.$ The corresponding elementary matrix can be found by applying this same elementary row operation to the identity matrix as follows:

- The second operation is $R_1:=6R_1.$ The corresponding elementary matrix can be found by applying this same elementary row operation to the identity matrix as follows:

To apply the first elementary row operation to the matrix $A,$ we multiply by $E_1$ on the left and get $E_1 A\mathbin{:}$

$$


\begin{aligned}1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0\end{aligned}


$$

Then, to apply the second elementary row operation to $E_1 A,$ we multiply by $E_2$ on the left and get $E_2 E_1 A\mathbin{:}$

$$


\begin{aligned}6 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{aligned}


$$
