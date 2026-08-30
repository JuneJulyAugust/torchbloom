# Creating Rows or Columns Containing Zeros Using Gaussian Elimination

Source: https://www.mathacademy.com/topics/3029?courseId=154
Topic ID: 3029

## Prerequisites

- [Elementary Row Operations](./149-elementary-row-operations.md)

## Lesson

### Introduction

When studying linear algebra, it is common to use elementary row operations to reduce a matrix $A$ to another matrix $B$ such that $B$ contains many zeros.

To illustrate, let's consider the matrix $A,$ given by

$$


\begin{aligned}1 & 1 & −4 \\ 3 & 2 & −2 \\ −5 & −3 & 6\end{aligned}


$$

Consider the entry $a_{11}$ located in the top left-hand corner. We can reduce *all* of the entries *below* it using elementary row operations.

First, we subtract $3$ times the first row from the second row.

$$


\begin{aligned}𝐴= & \begin{aligned}1 & 1 & −4 \\ 3 & 2 & −2 \\ −5 & −3 & 6\end{aligned} & & \,\begin{aligned}𝑅_{2}:=𝑅_{2}−3𝑅_{1}\end{aligned} \\ ∼ & \begin{aligned}1 & 1 & −4 \\ 0 & −1 & 10 \\ −5 & −3 & 6\end{aligned} & & \end{aligned}


$$

Then, we add $5$ times the first row to the third row.

$$


\begin{aligned} & \begin{aligned}1 & 1 & −4 \\ 0 & −1 & 10 \\ −5 & −3 & 6\end{aligned} & & \,\begin{aligned}𝑅_{3}:=𝑅_{3}+5𝑅_{1}\end{aligned} \\ ∼ & \begin{aligned}1 & 1 & −4 \\ 0 & −1 & 10 \\ 0 & 2 & −14\end{aligned} & & \end{aligned}


$$

And we're done! We have successfully performed elementary row operations to reduce all of the entries below $a_{11}$ to zero.

### Example: Using Row Operations to Create a Column of Zeros in a 3x3 Matrix

#### Question

$$


\begin{aligned}1 & 4 & −7 \\ 2 & 2 & −8 \\ −3 & −2 & 1\end{aligned}


$$

By applying elementary row operations of the form $R_i:=R_i+kR_1,$ the matrix $A$ can be transformed into the matrix $B.$ What are the elementary row operations?

#### Explanation

To transform $A$ into $B,$ we need to make the entries below $a_{11}={\color{blue}\boxed{1}}$ equal to ${\color{red}0}.$

To do this, we can apply the following elementary row operations:

$$


\begin{aligned}𝐴 & =\begin{aligned}1 & 4 & −7 \\ 2 & 2 & −8 \\ −3 & −2 & 1\end{aligned} & & \,\begin{aligned}𝑅_{2}:=𝑅_{2}−2𝑅_{1}\end{aligned} \\ & ∼\begin{aligned}1 & 4 & −7 \\ 0 & −6 & 6 \\ −3 & −2 & 1\end{aligned} & & \,\begin{aligned}𝑅_{3}:=𝑅_{3}+3𝑅_{1}\end{aligned} \\ & ∼\begin{aligned}1 & 4 & −7 \\ 0 & −6 & 6 \\ 0 & 10 & −20\end{aligned} & & \\ & =𝐵 & & \end{aligned}


$$

Therefore, the elementary row operations are

$\qquad$ $R_2:=R_2-2R_1\quad$ and $\quad R_3:=R_3+3R_1.$

### Example: Using Row Operations to Create a Column of Zeros in a 4x4 Matrix

#### Question

$$


\begin{aligned}−1 & 2 & 1 & 5 \\ 1 & 1 & 2 & −1 \\ −1 & 3 & 1 & 1 \\ 0 & −2 & 1 & 5\end{aligned}


$$

Consider the matrices $A$ and $B$ above. By applying three matrix elementary row operations

1. $R_1:= \ldots$

2. $R_3:=R_3-3R_2$

3. $R_4:= \ldots$

each of the form $R_i:=R_i+kR_2,$ the matrix $A$ can be transformed into the matrix $B.$ What are the missing elementary row operations?

#### Explanation

To transform $A$ into $B,$ we need to make entries above and below $a_{22}={\color{blue}\boxed{1}}$ equal to ${\color{red}0}.$

To do this, we can apply the following elementary row operations:

$$


\begin{aligned}𝐴 & =\begin{aligned}−1 & 2 & 1 & 5 \\ 1 & 1 & 2 & −1 \\ −1 & 3 & 1 & 1 \\ 0 & −2 & 1 & 5\end{aligned} & & \,\begin{aligned}𝑅_{1}:=𝑅_{1}−2𝑅_{2}\end{aligned} \\ & ∼\begin{aligned}−3 & 0 & −3 & 7 \\ 1 & 1 & 2 & −1 \\ −1 & 3 & 1 & 1 \\ 0 & −2 & 1 & 5\end{aligned} & & \,\begin{aligned}𝑅_{3}:=𝑅_{3}−3𝑅_{2}\end{aligned} \\ & ∼\begin{aligned}−3 & 0 & −3 & 7 \\ 1 & 1 & 2 & −1 \\ −4 & 0 & −5 & 4 \\ 0 & −2 & 1 & 5\end{aligned} & & \,\begin{aligned}𝑅_{4}:=𝑅_{4}+2𝑅_{2}\end{aligned} \\ & ∼\begin{aligned}−3 & 0 & −3 & 7 \\ 1 & 1 & 2 & −1 \\ −4 & 0 & −5 & 4 \\ 2 & 0 & 5 & 3\end{aligned} & & \\ & =𝐵 & & \end{aligned}


$$

Therefore, the missing elementary row operations are

$\qquad$ $R_1:= R_1 - 2R_2\quad$ and $\quad R_4:=R_4+2R_2.$

### Column Operations

We can do the same trick using the **elementary column operations** instead of row operations.

There are three types of elementary *column* operations, which are entirely analogous to the corresponding row operations:

- Switching any two columns:

- Multiplying (each element of) a column by a non-zero number:

- Adding a multiple of one column to another column:

**Watch out!**

- Unlike elementary row operations, elementary *column* operations change the solutions of a system of linear equations. This is because column operations alter the coefficients associated with each variable across the system, changing the equations.

- The exception is swapping two columns - this doesn't alter the solutions *provided that* we swap the corresponding variables in the solution vector. For example, if we swap the first and second columns, we must treat the second variable as the first and vice versa. The solution set remains unchanged because the relationships between the variables and their coefficients are preserved.

### Example: Using Column Operations to Create a Row of Zeros in a 3x3 Matrix

#### Question

$$


\begin{aligned}−6 & −5 & 1 \\ 8 & 3 & −4 \\ 9 & 7 & −2\end{aligned}


$$

By applying elementary column operations of the form $C_i:=C_i+kC_3,$ the matrix $A$ can be transformed into the matrix $B.$ What are the elementary column operations?

#### Explanation

To transform $A$ into $B,$ we need to make entries to the left of $a_{13}={\color{blue}\boxed{1}}$ equal to ${\color{red}0}.$

To do this, we can apply the following elementary column operations:

$$


\begin{aligned}𝐴 & =\begin{aligned}−6 & −5 & 1 \\ 8 & 3 & −4 \\ 9 & 7 & −2\end{aligned} & & \,\begin{aligned}𝐶_{1}:=𝐶_{1}+6𝐶_{3}\end{aligned} \\ & ∼\begin{aligned}0 & −5 & 1 \\ −16 & 3 & −4 \\ −3 & 7 & −2\end{aligned} & & \,\begin{aligned}𝐶_{2}:=𝐶_{2}+5𝐶_{3}\end{aligned} \\ & ∼\begin{aligned}0 & 0 & 1 \\ −16 & −17 & −4 \\ −3 & −3 & −2\end{aligned} & & \\ & =𝐵 & & \end{aligned}


$$

Therefore, the elementary column operations are

$\qquad$ $C_1:=C_1+6C_3\quad$ and $\quad C_2:=C_2+5C_3.$

### Example: Using Column Operations to Create a Row of Zeros in a 4x4 Matrix

#### Question

$$


\begin{aligned}7 & −3 & −1 & −6 \\ 7 & −2 & −2 & −4 \\ −5 & 1 & 4 & 2 \\ −8 & −3 & −6 & −4\end{aligned}


$$

Consider the matrices $A$ and $B$ above. By applying three matrix elementary column operations

1. $C_1:=\ldots$

2. $C_3:= C_3 - 4C_2$

3. $C_4:= \ldots$

each of the form $C_i:=C_i+kC_2,$ the matrix $A$ can be transformed into the matrix $B.$ What are the missing elementary column operations?

#### Explanation

To transform $A$ into $B,$ we need to make entries to the left and to the right of $a_{32}={\color{blue}\boxed{1}}$ equal to ${\color{red}0}.$

To do this, we can apply the following elementary column operations:

$$


\begin{aligned}𝐴 & =\begin{aligned}7 & −3 & −1 & −6 \\ 7 & −2 & −2 & −4 \\ −5 & 1 & 4 & 2 \\ −8 & −3 & −6 & −4\end{aligned} & & \,\begin{aligned}𝐶_{1}:=𝐶_{1}+5𝐶_{2}\end{aligned} \\ & ∼\begin{aligned}−8 & −3 & −1 & −6 \\ −3 & −2 & −2 & −4 \\ 0 & 1 & 4 & 2 \\ −23 & −3 & −6 & −4\end{aligned} & & \,\begin{aligned}𝐶_{3}:=𝐶_{3}−4𝐶_{2}\end{aligned} \\ & ∼\begin{aligned}−8 & −3 & 11 & −6 \\ −3 & −2 & 6 & −4 \\ 0 & 1 & 0 & 2 \\ −23 & −3 & 6 & −4\end{aligned} & & \,\begin{aligned}𝐶_{4}:=𝐶_{4}−2𝐶_{2}\end{aligned} \\ & ∼\begin{aligned}−8 & −3 & 11 & 0 \\ −3 & −2 & 6 & 0 \\ 0 & 1 & 0 & 0 \\ −23 & −3 & 6 & 2\end{aligned} & & \\ & =𝐵 & & \end{aligned}


$$

Therefore, the corresponding elementary column operations are

$\qquad$ $C_1:=C_1+5C_2\quad$ and $\quad C_4:=C_4-2C_2.$
