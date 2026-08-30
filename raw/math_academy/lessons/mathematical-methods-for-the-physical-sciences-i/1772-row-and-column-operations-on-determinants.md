# Row and Column Operations on Determinants

Source: https://www.mathacademy.com/topics/1772?courseId=154
Topic ID: 1772

## Prerequisites

- [Basic Properties of Determinants](./1771-basic-properties-of-determinants.md)
- [Creating Rows or Columns Containing Zeros Using Gaussian Elimination](./3029-creating-rows-or-columns-containing-zeros-using-gaussian-elimination.md)

## Lesson

### Introduction

Remember the following three standard elementary row operations:

I. Swapping two rows

II. Multiplying a row by a non-zero number

III. Adding a multiple of one row to another row

Of these three elementary row operations, only III (adding a multiple of one row to another row) *preserves* the determinant. The other two operations, switching two rows or multiplying a row by a non-zero number, *change* the determinant.

To demonstrate, let's consider the matrix $[\begin{aligned}1 & 2 \\ 3 & 4\end{aligned}]$ Taking the determinant, we have

$$


\begin{aligned}1 & 2 \\ 3 & 4\end{aligned}


$$

If we swap the two rows, we get a different determinant:

$$


\begin{aligned}\begin{aligned}3 & 4 \\ 1 & 2\end{aligned} & =3⋅2−1⋅4 \\ & =2 \\ & ≠−2\,×\end{aligned}


$$

Likewise, if we multiply top row by ${\color{red}2},$ then we get a different determinant:

$$


\begin{aligned}\begin{aligned}2⋅1 & 2⋅2 \\ 3 & 4\end{aligned} & =\begin{aligned}2 & 4 \\ 3 & 4\end{aligned} \\ & =2⋅4−3⋅4 \\ & =−4 \\ & ≠−2\,×\end{aligned}


$$

However, if we add twice the top row to the bottom row, then we get the same determinant:

$$


\begin{aligned}\begin{aligned}1 & 2 \\ 3+2⋅1 & 4+2⋅2\end{aligned} & =\begin{aligned}1 & 2 \\ 5 & 8\end{aligned} \\ & =1⋅8−2⋅5 \\ & =−2\,✓\end{aligned}


$$

### Switching Two Rows Changes the Sign of the Determinant

As we saw, swapping two rows does not preserve the determinant. However, the only difference is the sign of the determinant changes.

$$


\begin{aligned}\begin{aligned}1 & 2 \\ 3 & 4\end{aligned} & =1⋅4−2⋅3=−2 \\ \begin{aligned}3 & 4 \\ 1 & 2\end{aligned} & =3⋅2−1⋅4=2\end{aligned}


$$

So, in the above example, we have

$$


\begin{aligned}\begin{aligned}1 & 2 \\ 3 & 4\end{aligned} & =−\begin{aligned}3 & 4 \\ 1 & 2\end{aligned}.\end{aligned}


$$

In general, swapping any two rows of a matrix changes the sign of the determinant to the opposite one. That is to say,

$$


\begin{aligned}det\begin{aligned}⋮ & ⋮ & … & ⋮ \\ ◻ & ◻ & … & ◻ \\ ⋮ & ⋮ & … & ⋮ \\ △ & △ & … & △ \\ ⋮ & ⋮ & … & ⋮\end{aligned}=−det\begin{aligned}⋮ & ⋮ & … & ⋮ \\ △ & △ & … & △ \\ ⋮ & ⋮ & … & ⋮ \\ ◻ & ◻ & … & ◻ \\ ⋮ & ⋮ & … & ⋮\end{aligned}.\end{aligned}


$$

### Example: Calculating a Determinant After Switching Two Rows

#### Question

Suppose $A$ is a $3 \times 3$ matrix and $\det (A) = -16.$ The matrix $B$ is obtained from $A$ by applying the elementary row operation $R_1 \leftrightarrow R_2$ (switching the first and the second rows). What is the value of $\det(B)?$

#### Explanation

Since swapping any two rows changes the sign of the determinant to the opposite sign, we have

$$


\begin{aligned}det(𝐵) & =−det(𝐴) \\ & =−(−16) \\ & =16.\end{aligned}


$$

### Multiplying a Row By a Number Scales the Determinant By That Number

As we have seen, multiplying a row by a number does not preserve the determinant. However, it does affect the determinant in a predictable way: multiplying a row by a number scales the determinant by that number as well.

$$


\begin{aligned}\begin{aligned}1 & 2 \\ 3 & 4\end{aligned} & =1⋅4−2⋅3=−2 \\ \begin{aligned}2⋅1 & 2⋅2 \\ 3 & 4\end{aligned}=\begin{aligned}2 & 4 \\ 3 & 4\end{aligned} & =2⋅4−3⋅4=−4\end{aligned}


$$

So, in the above example, we have

$$


\begin{aligned}2⋅1 & 2⋅2 \\ 3 & 4\end{aligned}


$$

In general, multiplying a row of a matrix by a number multiplies the determinant by that number. That is to say, we can factor out the common multiplier from the row of the determinant:

$$


\begin{aligned}det\begin{aligned}⋮ & ⋮ & … & ⋮ \\ 𝑘△ & 𝑘△ & … & 𝑘△ \\ ⋮ & ⋮ & … & ⋮\end{aligned}=𝑘⋅det\begin{aligned}⋮ & ⋮ & … & ⋮ \\ △ & △ & … & △ \\ ⋮ & ⋮ & … & ⋮\end{aligned}\end{aligned}


$$

### Example: Calculating a Determinant After Multiplying a Row by a Number

#### Question

Suppose $A$ is a $6 \times 6$ matrix and $\det(A) = 32.$ The matrix $B$ is obtained from $A$ by applying the elementary row operation $R_3:= \dfrac{1}{8} R_3$. What is the value of $\det(B)?$

#### Explanation

The row operation applied to $A$ consists of multiplying a row by the number $\dfrac{1}{8}.$

When we do this, the determinant is multiplied by the same number. So, we have

$$


\begin{aligned}det(𝐵) & =\frac{1}{8}det(𝐴) \\ & =\frac{1}{8}⋅32 \\ & =4.\end{aligned}


$$

### Multiplying a Matrix By a Scalar

Let's check what happens if we multiply the entire matrix (not only one row) by a number. For example,

$$


\begin{aligned}\begin{aligned}1 & 2 \\ 3 & 4\end{aligned} & =1⋅4−2⋅3=−2 \\ \begin{aligned}3⋅1 & 3⋅2 \\ 3⋅3 & 3⋅4\end{aligned}=\begin{aligned}3 & 6 \\ 9 & 12\end{aligned} & =3⋅12−6⋅9=−18\end{aligned}


$$

So, in the above example, we have

$$


\begin{aligned}3⋅1 & 3⋅2 \\ 3⋅3 & 3⋅4\end{aligned}


$$

The above is equivalent to multiplying both rows of the matrix by $3$. Multiplying the first row scales the determinant by $3$, and then multiplying the second row scales it by $3$ once more.

In general, multiplying an entire $n \times n$ matrix by a number multiplies the determinant by that number to the power of $n$. That is to say, we can factor out the common multiplier from the entire matrix, as follows:

$$


\begin{aligned}det(𝑘⋅𝐴)=𝑘^{𝑛}⋅det(𝐴),\end{aligned}


$$

where $A$ is an $n \times n$ matrix.

### Example: Calculating a Determinant After Multiplying a Matrix by a Scalar

#### Question

Suppose $A$ is a $4\times4$ matrix and $\det(A)=5.$ What is the value of $\det(2A)?$

#### Explanation

Multiplying a $n\times n$ matrix by a scalar $k$ is equivalent to multiplying each row by $k,$ and this occurs $n$ times. This leads to the result

$$


\begin{aligned}det(𝑘⋅𝐴)=𝑘^{𝑛}⋅det(𝐴).\end{aligned}


$$

In our case, we have $k=2$ and $n=4.$ Therefore,

$$


\begin{aligned}det(2𝐴) & =2^{4}⋅det(𝐴) \\ & =16⋅5 \\ & =80.\end{aligned}


$$

### Example: Calculating a Determinant After Applying Several Elementary Operations

#### Question

Suppose $A$ is an $8 \times 8$ matrix and $\det(A) = 5.$ The matrix $B$ is obtained from $A$ by applying the elementary row operations $R_4 \leftrightarrow R_5,$ $R_6:= 4 R_6,$ and $R_8: = R_8 - \dfrac{1}{2} R_7.$ What is the value of $\det(B)?$

#### Explanation

First, let's figure out what each operation does to the determinant.

- The operation $R_4 \leftrightarrow R_5$ involves swapping two rows, so it changes the sign of the determinant to the opposite one.

- The operation $R_6:= 4 R_6$ involves multiplying a row by $4,$ so the determinant is multiplied by $4$ as well.

- The operation $R_8:= R_8 - \dfrac{1}{2} R_7$ involves adding a multiple of one row to another row, so it does not change the determinant.

Therefore, we have to change the sign of the determinant to the opposite one and multiply by $4$ as well. Consequently, we get

$$


\begin{aligned}det(𝐵) & =4⋅(−det(𝐴)) \\ & =−4det(𝐴) \\ & =−4⋅5 \\ & =−20.\end{aligned}


$$

### Example: Identifying a Row Operation Given the Connection Between Two Determinants

#### Question

Given that $\det(X)=\det(Y),$ which elementary row operations transforms matrix $X$ to matrix $Y,$ where

$$


\begin{aligned}2 & −1 & 2 \\ 3 & 0 & −1 \\ −1 & 1 & 1\end{aligned}


$$

#### Explanation

Since $\det(X)=\det(Y)$, the row operation applied to $X$ must be to add or subtract a multiple of one row to another row. In other words, it is of the form

$$


R_j := R_j + (k)R_i, \quad i \neq j.


$$

By considering the given row operations that are of the above form, we notice that

$$


\begin{aligned}det(𝑋) & =\begin{aligned}2 & −1 & 2 \\ 3 & 0 & −1 \\ −1 & 1 & 1\end{aligned} & 𝑅_{2} & :=𝑅_{2}+3𝑅_{3} \\ & =\begin{aligned}2 & −1 & 2 \\ 0 & 3 & 2 \\ −1 & 1 & 1\end{aligned} & & \\ & =det(𝑌). & & \end{aligned}


$$

Therefore, the required row operation is

$$


R_2:= R_2 + 3R_3.


$$

### Column Operations on Determinants

Since $\det(A^T)=\det(A),$ the corresponding elementary column operations on determinants have the same properties as the elementary row ones.

- Swapping two columns changes the sign of the determinant.

- Multiplying a column by a number scales the determinant by that number.

- Adding a multiple of one column to another column does not change the determinant.
