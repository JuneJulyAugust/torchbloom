# Matrices With Easy-to-Find Inverses

Source: https://www.mathacademy.com/topics/42?courseId=145
Topic ID: 42

## Prerequisites

- [Introduction to the Inverse of a Matrix](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/863-introduction-to-the-inverse-of-a-matrix.md)
- [Triangular Matrices](./1777-triangular-matrices.md)

## Lesson

### Introduction

For some types of matrices, finding the inverse is relatively easy. One of the more common examples of this is diagonal matrices.

A diagonal matrix is invertible only if it has nonzero entries on its main diagonal. In such cases, we have

$$


\begin{aligned}𝑎_{11} & 0 & ⋯ & 0 \\ 0 & 𝑎_{22} & ⋯ & 0 \\ ⋮ & ⋮ & ⋱ & ⋮ \\ 0 & 0 & ⋯ & 𝑎_{𝑛𝑛}\end{aligned}


$$

For example,

$$


\begin{aligned}1 & 0 & 0 \\ 0 & 5 & 0 \\ 0 & 0 & 3\end{aligned}


$$

### Example: Inverting a Diagonal Matrix

#### Question

Find the inverse of the following matrix:

$$


\begin{aligned}−4 & 0 & 0 \\ 0 & \frac{1}{3} & 0 \\ 0 & 0 & 5\end{aligned}


$$

#### Explanation

Notice that the given matrix is diagonal.

The inverse of a diagonal matrix can be found as follows:

$$


\begin{aligned}𝑎_{11} & 0 & ⋯ & 0 \\ 0 & 𝑎_{22} & ⋯ & 0 \\ ⋮ & ⋮ & ⋱ & ⋮ \\ 0 & 0 & ⋯ & 𝑎_{𝑛𝑛}\end{aligned}


$$

In our case, we obtain

$$


\begin{aligned}−4 & 0 & 0 \\ 0 & \frac{1}{3} & 0 \\ 0 & 0 & 5\end{aligned}


$$

### Permutation Matrices

A **permutation matrix** is a square matrix that can be obtained from the identity matrix by **permuting** (i.e., reordering) its columns. Notice that the identity matrix itself is considered a permutation matrix.

Let's consider the $4\times4$ identity matrix:

$$


\begin{aligned}𝐼_{4}= & \begin{aligned}1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1\end{aligned} \\ & \,\,\,\begin{aligned}↑ & ↑ & ↑ & ↑\end{aligned} \\ & \,\,\,\begin{aligned}1 & 2 & 3 & 4\end{aligned}\end{aligned}


$$

Notice that we have numbered its columns.

Now, let's create a new matrix $P$ by permuting its columns as follows:

- insert the ${\color{purple}{3}}\textrm{rd}$ column of $I_4$ to the $1\textrm{st}$ column of the new matrix:

$$


\begin{aligned} & \begin{aligned}0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0\end{aligned} \\ & \,\,\,\begin{aligned}↑ & ↑ & ↑ & ↑\end{aligned} \\ & \,\,\,\begin{aligned}3 & 0 & 0 & 0\end{aligned}\end{aligned}


$$

- insert the ${\color{blue}{1}}\textrm{st}$ column of $I_4$ to the $2\textrm{nd}$ column of the new matrix:

$$


\begin{aligned} & \begin{aligned}0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0\end{aligned} \\ & \,\,\,\begin{aligned}↑ & ↑ & ↑ & ↑\end{aligned} \\ & \,\,\,\begin{aligned}0 & 1 & 0 & 0\end{aligned}\end{aligned}


$$

- insert the ${\color{red}{2}}\textrm{nd}$ column of $I_4$ to the $3\textrm{rd}$ column of the new matrix:

$$


\begin{aligned} & \begin{aligned}0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0\end{aligned} \\ & \,\,\,\begin{aligned}↑ & ↑ & ↑ & ↑\end{aligned} \\ & \,\,\,\begin{aligned}3 & 1 & 2 & 4\end{aligned}\end{aligned}


$$

- insert the $4\textrm{th}$ column of $I_4$ to the $4\textrm{th}$ column of the new matrix:

This gives the following permutation matrix:

$$


\begin{aligned}𝑃= & \begin{aligned}0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1\end{aligned} \\ & \,\,\,\begin{aligned}↑ & ↑ & ↑ & ↑\end{aligned} \\ & \,\,\,\begin{aligned}3 & 1 & 2 & 4\end{aligned}\end{aligned}


$$

We have the following theorem regarding permutation matrices:

*If $P$ is a permutation matrix, then its inverse is given by*

$$


P^{-1}=P^T.


$$

Using this theorem, we get

$$


\begin{aligned}\begin{aligned}0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1\end{aligned}^{−1}=\begin{aligned}0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1\end{aligned}^{𝑇}=\begin{aligned}0 & 0 & 1 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1\end{aligned}.\end{aligned}


$$

### Example: Inverting a Permutation Matrix

#### Question

Find the inverse of the following matrix:

$$


\begin{aligned}1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0\end{aligned}


$$

#### Explanation

The given matrix can be obtained from the identity matrix by permuting its columns. Therefore, $A$ is a permutation matrix.

The inverse of a permutation matrix can be found as follows:

$$


P^{-1} = P^T


$$

In our case, we obtain

$$


\begin{aligned}𝐴^{−1}=\begin{aligned}1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0\end{aligned}^{−1}=\begin{aligned}1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0\end{aligned}^{𝑇}=\begin{aligned}1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0\end{aligned}.\end{aligned}


$$

### Frobenius Matrices

An **atomic triangular matrix** or **Frobenius matrix** is a square matrix with the following properties:

- all entries on the main diagonal are ones

- the matrix has only one column where some entries below the main diagonal can be non-zero

- all other entries outside the main diagonal equal zero

The following matrix is an example of a Frobenius matrix:

$$


\begin{aligned}1 & 0 & 0 & 0 \\ 3 & 1 & 0 & 0 \\ 5 & 0 & 1 & 0 \\ 7 & 0 & 0 & 1\end{aligned}


$$

Note that this matrix has nonzero entries only in the first column and on the main diagonal, and all of the main diagonal entries equal one.

We have the following theorem regarding Frobenius matrices:

*If $F$ is a Frobenius matrix, then its inverse is also a Frobenius matrix, where the corresponding nonzero entries outside the main diagonal have opposite signs.*

Using this theorem, we get

$$


\begin{aligned}\begin{aligned}1 & 0 & 0 & 0 \\ 3 & 1 & 0 & 0 \\ 5 & 0 & 1 & 0 \\ 7 & 0 & 0 & 1\end{aligned}^{−1}=\begin{aligned}1 & 0 & 0 & 0 \\ −3 & 1 & 0 & 0 \\ −5 & 0 & 1 & 0 \\ −7 & 0 & 0 & 1\end{aligned}\end{aligned}


$$

### Example: Inverting a Frobenius Matrix

#### Question

Find the inverse of the following matrix:

$$


\begin{aligned}1 & 0 & 0 & 0 \\ \frac{1}{3} & 1 & 0 & 0 \\ −6 & 0 & 1 & 0 \\ −2 & 0 & 0 & 1\end{aligned}


$$

#### Explanation

Notice that we're given a Frobenius matrix:

- all entries on the main diagonal are ones

- the matrix has only one column (the $1$st column) where some entries below the main diagonal are not zeros

- all the other entries outside the main diagonal are zeros

To find the inverse of a Frobenius matrix, we simply change the signs of the non-zero entries outside the main diagonal.

In our case, we obtain

$$


\begin{aligned}𝐴^{−1}=\begin{aligned}1 & 0 & 0 & 0 \\ \frac{1}{3} & 1 & 0 & 0 \\ −6 & 0 & 1 & 0 \\ −2 & 0 & 0 & 1\end{aligned}^{−1}=\begin{aligned}1 & 0 & 0 & 0 \\ −\frac{1}{3} & 1 & 0 & 0 \\ 6 & 0 & 1 & 0 \\ 2 & 0 & 0 & 1\end{aligned}.\end{aligned}


$$
