# Triangular Matrices

Source: https://www.mathacademy.com/topics/1777?courseId=145
Topic ID: 1777

## Prerequisites

- [The Transpose of a Matrix](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/232-the-transpose-of-a-matrix.md)
- [Zero, Square, Diagonal and Identity Matrices](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/862-zero-square-diagonal-and-identity-matrices.md)

## Lesson

### Introduction

Recall that a matrix is square if the number of rows equals the number of columns. There are other types of square matrices with special names.

- An **upper triangular** matrix is a square matrix in which all entries *below* the diagonal are zeros. For example, the following matrices are all upper triangular matrices: Note that we can have any number (including $0$) on the diagonal and above.

- A **lower triangular** matrix is a square matrix in which all entries *above* the diagonal are zeros. For example, the following matrices are all lower triangular matrices: Again, note that we can have any number (including $0$) on the diagonal and below.

### Example: Describing a Triangular Matrix

#### Question

How can we best describe the following matrix?

$$


\begin{aligned}−2 & 0 & 0 \\ 6 & −1 & 0 \\ 0 & 0 & 0\end{aligned}


$$

#### Explanation

Notice that $A$ is a matrix for which all entries above the diagonal are $0$'s:

$$


\begin{aligned}−2 & 0 & 0 \\ 6 & −1 & 0 \\ 0 & 0 & 0\end{aligned}


$$

Therefore, it is a lower triangular matrix.

It is not an upper triangular matrix or a diagonal matrix since there is a non-zero element below the diagonal: $a_{21}=6 \neq 0.$

### Example: Identifying a Triangular Matrix

#### Question

Which of the following matrices are lower triangular matrices?

$$


\begin{aligned}0 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0\end{aligned}


$$

#### Explanation

The matrix $B$ is a lower triangular matrix since all the entries above the main diagonal are zeros.

The matrices $A$ and $C$ are ** lower triangular matrices since they each have a non-zero element above the main diagonal:

$$


\begin{aligned}𝑎_{23} & =1≠0 \\ 𝑐_{13} & =1≠0\end{aligned}


$$

### Example: Identifying Correct Statements About a Matrix

#### Question

Consider the matrix $\begin{aligned}0 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 2\end{aligned}$ Which of the following statements are true?

1. $A$ is upper triangular

2. $A$ is lower triangular

3. $A^T-A$ is lower triangular

#### Explanation

Let's analyze each statement in turn.

- Statement I is false, since $A$ has non-zero entries below the main diagonal:

- Statement II is true, since all the entries above the main diagonal are zeros:

- Statement III is false, since the result of $A^T-A$ has non-zero entries above the main diagonal:

Therefore, the correct answer is "II only".
