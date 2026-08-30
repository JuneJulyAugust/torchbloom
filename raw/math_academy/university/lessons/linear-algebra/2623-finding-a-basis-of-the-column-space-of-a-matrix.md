# Finding a Basis of the Column Space of a Matrix

Source: https://www.mathacademy.com/topics/2623?courseId=55
Topic ID: 2623

## Prerequisites

- [The Column Space of a Matrix](./1850-the-column-space-of-a-matrix.md)
- [Finding a Basis of a Span](./1855-finding-a-basis-of-a-span.md)

## Lesson

### Introduction

Remember that the column space of a matrix is the span of its columns. For example, for the matrix

$$


[\begin{aligned}1 & 2 & −1 \\ 3 & 2 & 5\end{aligned}]


$$

the column space is

$$


[\begin{aligned}1 \\ 3\end{aligned}]


$$

So, to find a basis of $\text{Col}(A),$ we can apply the usual procedure of converting the matrix $A$ to row echelon form and then picking the pivot columns from the original matrix $A.$

### Example: Finding a Basis of the Column Space of a Matrix

#### Question

Consider the matrix $[\begin{aligned}1 & 2 & −1 \\ 3 & 2 & 5\end{aligned}]$ Find a basis $\mathcal B$ of $\text{Col}(A).$

#### Explanation

In order to find a basis of $\text{Col}(A),$ we need reduce the matrix $A$ to row echelon form:

$$


\begin{aligned}𝐴 & =[\begin{matrix}1 & 2 & −1 \\ 3 & 2 & 5\end{matrix}] & 𝑅_{2} & :=𝑅_{2}+(−3)𝑅_{1} \\ & ∼[\begin{matrix}1 & 2 & −1 \\ 0 & −4 & 8\end{matrix}] & & \end{aligned}


$$

The pivot columns correspond to linearly independent vectors, while the non-pivot columns correspond to linearly dependent vectors that can be removed. Here, the $1$st and $2$nd columns are pivot columns, while the $3$rd column is a non-pivot column.

Remember that we need to pick the pivot columns from the **, not from the reduced one.

The $1$st and $2$nd columns from the original matrix are $\mathbf{a}_1$ and $\mathbf{a}_2.$ So, a basis of $\text{Col}(A)$ is $\{\mathbf{a}_1, \mathbf{a}_2 \},$ that is to say,

$$


[\begin{aligned}1 \\ 3\end{aligned}]


$$

### Finding a Particular Linear Combination of Vectors

In the previous example, we computed a basis of $\text{Col}(A),$ where

$$


[\begin{aligned}1 & 2 & −1 \\ 3 & 2 & 5\end{aligned}]


$$

The basis that we found previously was

$$


[\begin{aligned}1 \\ 3\end{aligned}]


$$

Therefore, we can write

$$


[\begin{aligned}1 \\ 3\end{aligned}]


$$

The vector $\mathbf{a}_3$ was not included in the basis because the $3$rd column of $A$ was not a pivot column. This means that $\mathbf{a}_3$ can be written as a linear combination of $\mathbf{a}_1$ and $\mathbf{a}_2.$

Now, what if we want to find the exact linear combination of $\mathbf{a}_1$ and $\mathbf{a}_2$ that yields $\mathbf{a}_3?$ That is to say, we want to find $x_1, x_2 \in \mathbb{R}$ such that

$$


[\begin{aligned}1 \\ 3\end{aligned}]


$$

This is equivalent to a system with the augmented matrix

$$


\begin{aligned}1 & 2 & −1 \\ 3 & 2 & 5\end{aligned}


$$

If we reduced this matrix to the *reduced* row echelon form, we get

$$


\begin{aligned}1 & 0 & 3 \\ 0 & 1 & −2\end{aligned}


$$

Finally, the third column of the *reduced* matrix tells us that $x_1=3$ and $x_2=-2,$ meaning that

$$


[\begin{aligned}−1 \\ 5\end{aligned}]


$$

In general, if the $n$th column of the reduced matrix is a non-pivot column, then the entries in that column tell us the coefficients needed to express $\mathbf{a}_n$ as a linear combination of all the other columns in the original matrix.

**Watch out!** The matrix must be written in *reduced* row echelon form (with $1$'s for pivots and $0$'s above and below the pivots), not just in a row echelon form.

### Example: Determining Whether a Given Set Is a Basis of the Column Space of a Matrix With Two Rows

#### Question

The matrix $A$ is given below. Let $\mathbf{a}_1$, $\mathbf{a}_2$, and $\mathbf{a}_3$ be the respective columns of $A.$ Determine if $𝐚_{1},𝐚_{2}$ is a basis of $\text{Col}(A).$ If that is the case, find $x_1 \cdot x_2$, where $\mathbf{a}_3=x_1\mathbf{a}_1+x_2\mathbf{a}_2.$

$$


[\begin{aligned}1 & 2 & 9 \\ 3 & 1 & 17\end{aligned}]


$$

#### Explanation

First, we reduce the matrix $A$ to reduced row echelon form (RREF):

$$


\begin{aligned}𝐴 & =[\begin{matrix}1 & 2 & 9 \\ 3 & 1 & 17\end{matrix}] & 𝑅_{2} & :=𝑅_{2}+(−3)𝑅_{1} \\ & ∼[\begin{matrix}1 & 2 & 9 \\ 0 & −5 & −10\end{matrix}] & 𝑅_{2} & :=(−\frac{1}{5})𝑅_{2} \\ & ∼[\begin{matrix}1 & 2 & 9 \\ 0 & 1 & 2\end{matrix}] & 𝑅_{1} & :=𝑅_{1}+(−2)𝑅_{2} \\ & ∼[\begin{matrix}1 & 0 & 5 \\ 0 & 1 & 2\end{matrix}] & & \end{aligned}


$$

From the matrix above, we see that the pivot columns are the $1$st and $2$nd columns. So, a basis of $\text{Col}(A)$ is $\{\mathbf{a}_1,\mathbf{a}_2 \},$ that is to say,

$$


[\begin{aligned}1 \\ 3\end{aligned}]


$$

Now, since the $3$rd column of the reduced matrix is a non-pivot column, then the entries in that column tell us the coefficients needed to express $\mathbf{a}_3$ as a linear combination of all the other columns in the original matrix. So, we have

$$


[\begin{aligned}9 \\ 17\end{aligned}]


$$

This gives us $x_1 \cdot x_2 = 5 \cdot 2=10.$

### Example: Determining Whether a Given Set Is a Basis of the Column Space of a Matrix For a Larger Matrix

#### Question

The matrix $A$ is given below. Let $\mathbf{a}_1$, $\mathbf{a}_2$, $\mathbf{a}_3$, and $\mathbf{a}_4$ be the respective columns of $A.$ Determine if $𝐚_{1},𝐚_{2}$ is a basis of $\text{Col}(A).$ If that is the case, find $x_1 \cdot x_2$, where $\mathbf{a}_4=x_1\mathbf{a}_1+x_2\mathbf{a}_2.$

$$


\begin{aligned}2 & 0 & −4 & 4 \\ 0 & 1 & −6 & −3 \\ 1 & 2 & −14 & −4\end{aligned}


$$

#### Explanation

First, we reduce the matrix $A$ to reduced row echelon form (RREF):

$$


\begin{aligned}𝐴 & =\begin{matrix}2 & 0 & −4 & 4 \\ 0 & 1 & −6 & −3 \\ 1 & 2 & −14 & −4\end{matrix} & 𝑅_{1} & :=\frac{1}{2}𝑅_{1} \\ & ∼\begin{matrix}1 & 0 & −2 & 2 \\ 0 & 1 & −6 & −3 \\ 1 & 2 & −14 & −4\end{matrix} & 𝑅_{3} & :=𝑅_{3}+(−1)𝑅_{1} \\ & ∼\begin{matrix}1 & 0 & −2 & 2 \\ 0 & 1 & −6 & −3 \\ 0 & 2 & −12 & −6\end{matrix} & 𝑅_{3} & :=𝑅_{3}+(−2)𝑅_{2} \\ & ∼\begin{matrix}1 & 0 & −2 & 2 \\ 0 & 1 & −6 & −3 \\ 0 & 0 & 0 & 0\end{matrix} & & \end{aligned}


$$

From the matrix above, we see that the pivot columns are the $1$st and $2$nd columns. So, a basis of $\text{Col}(A)$ is $\{\mathbf{a}_1,\mathbf{a}_2 \},$ that is to say,

$$


\begin{aligned}2 \\ 0 \\ 1\end{aligned}


$$

Now, since the $4$th column of the reduced matrix is a non-pivot column, then the entries in that column tell us the coefficients needed to express $\mathbf{a}_4$ as a linear combination of all the other columns in the original matrix. So, we have

$$


\begin{aligned}4 \\ −3 \\ −4\end{aligned}


$$

This gives us $x_1 \cdot x_2 = 2 \cdot (-3) = -6.$
