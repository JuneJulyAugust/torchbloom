# Zero, Square, Diagonal and Identity Matrices

Source: https://www.mathacademy.com/topics/862?courseId=43
Topic ID: 862

## Prerequisites

- [Index Notation for Matrices](./1167-index-notation-for-matrices.md)

## Lesson

### Introduction

Some important types of matrices have special names.

- An $m \times n$ matrix in which all entries are zeros is called a **zero matrix**. For example, the following matrices are both zero matrices: We use the notation $O_{m \times n}$ to represent the zero-matrix with $m$ rows and $n$ columns. So, the zero matrices shown above are $O_{3 \times 2}$ and $O_{2 \times 2},$ respectively.

- A $n \times n$ matrix (meaning the number of rows equals the number of columns) is called a **square matrix**. For example, the following matrices are square matrices of dimensions $2\times 2$ and $3\times 3,$ respectively:

### Example: Identifying a Zero Matrix

#### Question

Which of the following are zero matrices?

$$



[\begin{aligned}0 & 0 \\ 0 & 0\end{aligned}]



$$

#### Explanation

- $P$ is a zero matrix since ** its entries are zeros.

- $Q$ is ** a zero matrix since some of its entries are not zeros (for instance, $q_{12}=0.1\neq0$).

- $R$ is a zero matrix since ** its entries are zeros.

Therefore, only $P$ and $R$ are zero matrices.

### Example: Identifying a Square Matrix

#### Question

Which of the following are square matrices?

$$



[\begin{aligned}1 & 0 & 1 \\ 2 & 3 & 1\end{aligned}]



$$

#### Explanation

- $U$ is ** a square matrix since the numbers of rows and columns are not the same. It has $2$ rows and $3$ columns, so it's a $2 \times 3$ matrix.

- $W$ is a square matrix since it has the same number of rows and columns. It has $3$ rows and $3$ columns, so it is a $3 \times 3$ matrix.

- $Z$ is a square matrix since it has the same number of rows and columns. It has $2$ rows and $2$ columns, so it is a $2 \times 2$ matrix.

Therefore, $W$ and $Z$ are square matrices.

### Diagonal, Identity, and Other Matrices

There are some special types of square matrices.

- A square matrix is called **diagonal**, if all entries that do not lie on the main diagonal (from top-left to bottom-right) are zeros. For example, the following matrices are all diagonal matrices: Note that we can have any number (including $0$) on the diagonal.

- An **identity matrix** is a diagonal matrix where the entries on the diagonal are all $1$'s (and all other entries are $0$'s). For example, the following matrices are all identity matrices: We use the notation $I_n$ for the $n \times n$ identity matrix.

Finally, as we've seen before:

- If a matrix has only one row, then it's called a **row vector**. An example of a row vector is shown below.

- If a matrix has only one column, then it's called a **column vector**. An example of a column vector is shown below.

### Example: Identifying a Special Square Matrix

#### Question

Which of the following are diagonal matrices?

$$



[\begin{aligned}3 & 0 \\ 0 & 3\end{aligned}]



$$

#### Explanation

- $Q$ is a diagonal matrix. It's a square matrix since it has the same number of rows and columns. Also, all the entries that do not lie on the main diagonal are zeros.

Notice that $Q$ is not an identity matrix since the diagonal entries are not all ones.

- $R$ is ** a diagonal matrix. It's a square matrix since it has the same number of rows and columns. But some of the entries that do not lie on the main diagonal are not zeros (for instance, $r_{13}=1 \neq 0$).

- $S$ is a diagonal matrix. It's a square matrix since it has the same number of rows and columns. Also, all the entries that do not lie on the main diagonal are zeros.

Notice that $S$ is not an identity matrix since the diagonal entries are not all ones.

Therefore, only $Q$ and $S$ are diagonal matrices.

### Example: Identifying Other Matrices

#### Question

How can we best describe the following matrix?

$$



\begin{aligned}5 \\ −9 \\ 2\end{aligned}



$$

#### Explanation

Notice that $F$ is a matrix that has a single column. Therefore, it is a column vector.
