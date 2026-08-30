# Finding Determinants Using Row and Column Operations

Source: https://www.mathacademy.com/topics/1773?courseId=154
Topic ID: 1773

## Prerequisites

- [Row and Column Operations on Determinants](./1772-row-and-column-operations-on-determinants.md)

## Lesson

### Introduction

One way to simplify a determinant calculation is to create a row (or column) containing all zeros except for one entry. Then, we can use a Laplace expansion across that row (or column) to compute the determinant.

Let's demonstrate this method on the matrix $A$ below.

$$


\begin{aligned}2 & 1 & 1 \\ 1 & 2 & 3 \\ 8 & 14 & 17\end{aligned}


$$

Notice that we can make entries to the right of $a_{21}=1$ equal to zero using elementary *column* operations.

Since adding a multiple of one column to another column in a matrix does not change the value of its determinant, we obtain

$$


\begin{aligned} & \,\,=\begin{matrix}2 & 1 & 1 \\ 1 & 2 & 3 \\ 8 & 14 & 17\end{matrix} & & \,\begin{matrix}𝐶_{2}:=𝐶_{2}+(−2)𝐶_{1} \\ 𝐶_{3}:=𝐶_{3}+(−3)𝐶_{1}\end{matrix} \\ & =\begin{matrix}2 & −3 & −5 \\ 1 & 0 & 0 \\ 8 & −2 & −7\end{matrix}. & & \end{aligned}


$$

Expanding the result along the $2$nd row, we get

$$


\begin{aligned} & \,\,=\begin{matrix}2 & −3 & −5 \\ 1 & 0 & 0 \\ 8 & −2 & −7\end{matrix} \\ & =1⋅(−1)^{2+1}\begin{matrix}−3 & −5 \\ −2 & −7\end{matrix} \\ & =−(21−10) \\ & =−11.\end{aligned}


$$

### Example: Reducing a 4x4 Determinant to a 3x3 Determinant Using Row Operations

#### Question

$$


\begin{aligned}1 & 2 & 3 & 1 \\ 2 & −1 & 5 & −7 \\ 4 & −2 & 4 & −5 \\ −3 & 3 & −3 & −4\end{aligned}


$$

Consider the above $4\times 4$ determinant. Find a $3\times 3$ determinant that has the same value.

**

#### Explanation

Let's make entries below $a_{11}=1$ equal to zero using elementary row operations.

Since adding a multiple of one row (or column) to another row (or column) in a matrix does not change the value of its determinant, we obtain

$$


\begin{aligned} & \,\,=\begin{matrix}1 & 2 & 3 & 1 \\ 2 & −1 & 5 & −7 \\ 4 & −2 & 4 & −5 \\ −3 & 3 & −3 & −4\end{matrix} & & \,\begin{matrix}𝑅_{2}:=𝑅_{2}+(−2)𝑅_{1} \\ 𝑅_{3}:=𝑅_{3}+(−4)𝑅_{1} \\ 𝑅_{4}:=𝑅_{4}+3𝑅_{1}\end{matrix} \\ & =\begin{matrix}1 & 2 & 3 & 1 \\ 0 & −5 & −1 & −9 \\ 0 & −10 & −8 & −9 \\ 0 & 9 & 6 & −1\end{matrix}. & & \end{aligned}


$$

Expanding the result along the $1$st column, we get

$$


\begin{aligned} & \,\,=\begin{matrix}1 & 2 & 3 & 1 \\ 0 & −5 & −1 & −9 \\ 0 & −10 & −8 & −9 \\ 0 & 9 & 6 & −1\end{matrix} \\ & =1⋅(−1)^{1+1}\begin{matrix}−5 & −1 & −9 \\ −10 & −8 & −9 \\ 9 & 6 & −1\end{matrix} \\ & =\begin{matrix}−5 & −1 & −9 \\ −10 & −8 & −9 \\ 9 & 6 & −1\end{matrix}.\end{aligned}


$$

### Example: Reducing a 4x4 Determinant to a 3x3 Determinant Using Column Operations

#### Question

$$


\begin{aligned}2 & 3 & 2 & 2 \\ −1 & 2 & 1 & −3 \\ 2 & −2 & −2 & 4 \\ −4 & −4 & 3 & 2\end{aligned}


$$

Consider the above $4\times 4$ determinant. Find a $3\times 3$ determinant that has the same value.

**

#### Explanation

Let's make entries to the left and to the right of $a_{23}=1$ equal to zero using elementary column operations.

Since adding a multiple of one row (or column) to another row (or column) in a matrix does not change the value of its determinant, we obtain

$$


\begin{aligned} & \,\,=\begin{matrix}2 & 3 & 2 & 2 \\ −1 & 2 & 1 & −3 \\ 2 & −2 & −2 & 4 \\ −4 & −4 & 3 & 2\end{matrix} & & \,\begin{matrix}𝐶_{1}:=𝐶_{1}+𝐶_{3} \\ 𝐶_{2}:=𝐶_{2}+(−2)𝐶_{3} \\ 𝐶_{4}:=𝐶_{4}+3𝐶_{3}\end{matrix} \\ & =\begin{matrix}4 & −1 & 2 & 8 \\ 0 & 0 & 1 & 0 \\ 0 & 2 & −2 & −2 \\ −1 & −10 & 3 & 11\end{matrix}. & & \end{aligned}


$$

Expanding the result along the $2$nd row, we get

$$


\begin{aligned} & \,\,=\begin{matrix}4 & −1 & 2 & 8 \\ 0 & 0 & 1 & 0 \\ 0 & 2 & −2 & −2 \\ −1 & −10 & 3 & 11\end{matrix} \\ & =1⋅(−1)^{2+3}\begin{matrix}4 & −1 & 8 \\ 0 & 2 & −2 \\ −1 & −10 & 11\end{matrix} \\ & =−\begin{matrix}4 & −1 & 8 \\ 0 & 2 & −2 \\ −1 & −10 & 11\end{matrix}.\end{aligned}


$$

### Example: Computing 4x4 Determinants Using Row and Column Operations

#### Question

Calculate the value of $\begin{aligned}1 & −1 & 3 & 2 \\ 2 & −4 & −2 & 6 \\ 1 & −2 & −3 & 3 \\ −3 & 3 & 4 & 2\end{aligned}$

**

#### Explanation

Using elementary column operations, let's make entries to the right of $a_{31}=1$ equal to zero.

Since adding a multiple of one row (or column) to another row (or column) in a matrix does not change the value of its determinant, we obtain

$$


\begin{aligned} & \,\,=\begin{matrix}1 & −1 & 3 & 2 \\ 2 & −4 & −2 & 6 \\ 1 & −2 & −3 & 3 \\ −3 & 3 & 4 & 2\end{matrix} & & \,\begin{matrix}𝐶_{2}:=𝐶_{2}+2𝐶_{1} \\ 𝐶_{3}:=𝐶_{3}+3𝐶_{1} \\ 𝐶_{4}:=𝐶_{4}+(−3)𝐶_{1}\end{matrix} \\ & =\begin{matrix}1 & 1 & 6 & −1 \\ 2 & 0 & 4 & 0 \\ 1 & 0 & 0 & 0 \\ −3 & −3 & −5 & 11\end{matrix}. & & \end{aligned}


$$

Expanding the result along the $3$rd row, we get

$$


\begin{aligned} & \,\,=\begin{matrix}1 & 1 & 6 & −1 \\ 2 & 0 & 4 & 0 \\ 1 & 0 & 0 & 0 \\ −3 & −3 & −5 & 11\end{matrix} \\ & =1⋅(−1)^{3+1}\begin{matrix}1 & 6 & −1 \\ 0 & 4 & 0 \\ −3 & −5 & 11\end{matrix} \\ & =\begin{matrix}1 & 6 & −1 \\ 0 & 4 & 0 \\ −3 & −5 & 11\end{matrix} \\ & =4⋅(−1)^{2+2}\begin{matrix}1 & −1 \\ −3 & 11\end{matrix} \\ & =4(11−3) \\ & =32.\end{aligned}


$$
