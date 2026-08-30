# Identifying the Pivot Columns of a Matrix

Source: https://www.mathacademy.com/topics/1904?courseId=55
Topic ID: 1904

## Prerequisites

- [Solving 3x3 Systems of Equations Using Gaussian Elimination](./1048-solving-3x3-systems-of-equations-using-gaussian-elimination.md)

## Lesson

### Introduction

The **pivots** of a matrix in row echelon form are the first non-zero entries in each row of the matrix.

For example, given the matrix

$$


\begin{aligned}1 & 0 & −2 & 0 \\ 0 & 1 & 5 & 0 \\ 0 & 0 & 0 & 1\end{aligned}


$$

which is in row echelon form, let's find the pivots of $A.$

- The first non-zero entry in the first row is the entry $a_{11}=1.$ So this is a pivot.

- The first non-zero entry of the second row is $a_{22}=1.$ So this is also a pivot.

- The first non-zero entry in the third row is $a_{34}=1.$ Therefore this is a pivot.

The pivots of $A$ are highlighted below.

$$


\begin{aligned}1 & 0 & −2 & 0 \\ 0 & 1 & 5 & 0 \\ 0 & 0 & 0 & 1\end{aligned}


$$

The **pivot columns** of a matrix in row echelon form are simply the columns in which the pivots appear.

For our matrix $A$, we can see that the pivot columns are the $1$st, $2$nd, and $4$th columns.

The non-pivot columns are the columns that do not contain a pivot. So for the matrix $A,$ the only non-pivot column is the $3$rd column.

### Example: Finding the Pivot Columns of a Matrix in Row Echelon Form

#### Question

The row echelon form matrix $B$ is given below. What are its pivot columns?

$$


\begin{aligned}0 & 1 & −3 & 4 \\ 0 & 0 & −1 & 1 \\ 0 & 0 & 0 & 1\end{aligned}


$$

#### Explanation

Remember that the pivots of a matrix in row echelon form are the first non-zero entries in each row of the matrix.

We can see that $B$ has $3$ pivots in the $2$nd, $3$rd, and $4$th columns:

$$


\begin{aligned}0 & 1 & −3 & 4 \\ 0 & 0 & −1 & 1 \\ 0 & 0 & 0 & 1\end{aligned}


$$

### Example: Finding the Non-Pivot Columns of a Matrix in Row Echelon Form

#### Question

The row echelon form matrix $C$ is given below. What are its ****-pivot columns?

$$


\begin{aligned}1 & 0 & 3 & 0 \\ 0 & 0 & 5 & 1 \\ 0 & 0 & 0 & 2 \\ 0 & 0 & 0 & 0\end{aligned}


$$

#### Explanation

Remember that the pivots of a matrix in row echelon form are the first non-zero entries in each row of the matrix.

We can see that $C$ has $3$ pivots in the $1$st, $3$rd, and $4$th columns:

$$


\begin{aligned}1 & 0 & 3 & 0 \\ 0 & 0 & 5 & 1 \\ 0 & 0 & 0 & 2 \\ 0 & 0 & 0 & 0\end{aligned}


$$

Therefore, the only non-pivot column is the $2$nd column.

### Pivot Columns of a General Matrix

To find the pivots and pivot columns of a general matrix, we first need to convert the matrix to row echelon form (REF).

- The pivots of any matrix are the pivots of its row equivalent REF matrix.

- The pivot columns of a matrix are the pivot columns of its row equivalent REF matrix.

To reduce a general $n\times m$ matrix to row echelon form, we follow a similar procedure to the $2\times 2$ and $3\times 3$ cases, as we'll see in the next example.

### Example: Finding the Number of Pivot Columns of a Matrix

#### Question

Determine the number of pivot columns of the matrix $A,$ given by

$$


\begin{aligned}1 & 0 & 0 & 0 \\ 0 & 3 & 0 & −2 \\ 0 & −6 & 1 & 4\end{aligned}


$$

#### Explanation

First, we need to convert $A$ to row echelon form:

$$


\begin{aligned}𝐴 & =\begin{aligned}1 & 0 & 0 & 0 \\ 0 & 3 & 0 & −2 \\ 0 & −6 & 1 & 4\end{aligned} & 𝑅_{3}:=𝑅_{3}+2𝑅_{2} \\ & ∼\begin{aligned}1 & 0 & 0 & 0 \\ 0 & 3 & 0 & −2 \\ 0 & 0 & 1 & 0\end{aligned} & \end{aligned}


$$

Looking at the row echelon form, we see that $A$ has $3$ pivots, and therefore the number of pivot columns is $3.$

### Example: Finding the Pivot Columns of a Matrix

#### Question

What are the pivot columns of the matrix $B,$ given by

$$


\begin{aligned}1 & −5 & 0 & 0 \\ 0 & 0 & 2 & 0 \\ 0 & 0 & −4 & 7 \\ 0 & 0 & 0 & 2\end{aligned}


$$

#### Explanation

First, we need to convert $B$ to row echelon form:

$$


\begin{aligned}𝐵 & =\begin{aligned}1 & −5 & 0 & 0 \\ 0 & 0 & 2 & 0 \\ 0 & 0 & −4 & 7 \\ 0 & 0 & 0 & 2\end{aligned} & 𝑅_{3} & :=𝑅_{3}+2𝑅_{2} \\ & ∼\begin{aligned}1 & −5 & 0 & 0 \\ 0 & 0 & 2 & 0 \\ 0 & 0 & 0 & 7 \\ 0 & 0 & 0 & 2\end{aligned} & 𝑅_{4} & :=𝑅_{4}+(−\frac{2}{7})𝑅_{3} \\ & ∼\begin{aligned}1 & −5 & 0 & 0 \\ 0 & 0 & 2 & 0 \\ 0 & 0 & 0 & 7 \\ 0 & 0 & 0 & 0\end{aligned} & & \end{aligned}


$$

Looking at the row echelon form, we see that $B$ has $3$ pivots. In particular, the pivot columns are the $1$st, $3$rd, and $4$th columns.
