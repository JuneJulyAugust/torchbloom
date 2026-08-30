# The Rank of a Matrix

Source: https://www.mathacademy.com/topics/1867?courseId=55
Topic ID: 1867

## Prerequisites

- [The Dimension of a Span](./1866-the-dimension-of-a-span.md)
- [Finding a Basis of the Column Space of a Matrix](./2623-finding-a-basis-of-the-column-space-of-a-matrix.md)

## Lesson

### Introduction

The dimension of the column space of a matrix $A$ is called the **rank of $A$**. It's usually denoted by $\textrm{rank}(A)$. So,

$$


\textrm{rank}(A) = \textrm{dim}(\textrm{Col}(A)).


$$

For example, to find the rank of

$$


\begin{aligned}3 & 2 & 5 \\ 0 & 1 & 0 \\ 6 & 4 & 10\end{aligned}


$$

we write $A$ in row echelon form, as follows:

$$


\begin{aligned}𝐴 & =\begin{aligned}3 & 2 & 5 \\ 0 & 1 & 0 \\ 6 & 4 & 10\end{aligned} & 𝑅_{3} & :=𝑅_{3}+(−2)𝑅_{1} \\ & ∼\begin{aligned}3 & 2 & 5 \\ 0 & 1 & 0 \\ 0 & 0 & 0\end{aligned}. & & \end{aligned}


$$

From the reduced matrix above, we see that there are $2$ pivot columns, namely, the $1$st and the $2$nd. This implies that the first and the second columns of $A$ form a basis of $\textrm{Col}(A)$ and, therefore, the dimension of $\textrm{Col}(A)$ is equal to $2.$

### Example: Determining the Rank of a Matrix Given the Number of Pivot Columns

#### Question

Let $A$ be a $4 \times 7$ matrix that has $3$ **** columns. Find $\textrm{rank}(A).$

#### Explanation

We know that $\textrm{rank}(A)$ is the number of pivot columns in $A$.

Since $A$ has $7$ columns and $3$ of them are non-pivots, then the number of pivot columns in $A$ is

$$


7-3=4.


$$

Therefore, $\textrm{rank}(A)=4$.

### An Alternative Definition of the Rank

Note that the number of pivot columns always coincides with the number of non-zero rows in the corresponding row echelon form matrix. So, technically,

$\textrm{rank}(A)$ is the number of *pivot columns* in the corresponding row echelon form matrix of $A$.

Or, equivalently,

$\textrm{rank}(A)$ is the number of *non-zero rows* in the corresponding row echelon form matrix of $A$.

### Example: Identifying the Matrix With a Given Rank by Inspection

#### Question

Which of the following matrices have a rank of $4?$

$$


\begin{aligned}1 & −2 & 0 & −1 \\ 0 & 2 & 7 & 1 \\ 0 & 0 & 3 & 0 \\ 0 & 0 & 0 & 0\end{aligned}


$$

#### Explanation

First, notice that a matrix of rank $4$ must have at least $4$ columns and at least $4$ rows. So, we disregard the matrix $B$ since it has only $3$ rows.

Also, the matrix must have $4$ pivot columns. As we can see, the matrix $A$ has only $3$ pivot columns, while the matrix $C$ has exactly $4$ pivot columns. So, $\textrm{rank}(A)=3$ and $\textrm{rank}(C)=4.$

Therefore, the correct answer is "$C$ only".

### Example: Finding the Rank of a Matrix Using Row Reduction

#### Question

If $\begin{aligned}2 & 3 & 0 \\ 0 & −1 & 5 \\ −4 & 0 & 5\end{aligned}$, find $\textrm{rank}(A).$

#### Explanation

To find the rank of $A,$ we first reduce it to row echelon form, as follows:

$$


\begin{aligned}𝐴 & =\begin{aligned}2 & 3 & 0 \\ 0 & −1 & 5 \\ −4 & 0 & 5\end{aligned} & 𝑅_{3} & :=𝑅_{3}+2𝑅_{1} \\ & ∼\begin{aligned}2 & 3 & 0 \\ 0 & −1 & 5 \\ 0 & 6 & 5\end{aligned} & 𝑅_{3} & :=𝑅_{3}+6𝑅_{2} \\ & ∼\begin{aligned}2 & 3 & 0 \\ 0 & −1 & 5 \\ 0 & 0 & 35\end{aligned} & & \end{aligned}


$$

The reduced matrix above has $3$ pivot columns (or, alternatively, it has exactly $3$ non-zero rows).

Therefore, $\textrm{rank}(A)=3.$
