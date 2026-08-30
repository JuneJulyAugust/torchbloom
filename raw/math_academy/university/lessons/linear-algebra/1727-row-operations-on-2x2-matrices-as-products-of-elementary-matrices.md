# Row Operations on 2x2 Matrices as Products of Elementary Matrices

Source: https://www.mathacademy.com/topics/1727?courseId=55
Topic ID: 1727

## Prerequisites

- [Elementary 2x2 Matrices](./1726-elementary-2x2-matrices.md)

## Lesson

### Introduction

To compute the product of an elementary matrix and another matrix, one option is to perform the matrix multiplication as usual. However, there's an easier, quicker way.

Remember that every elementary matrix is the result of applying an elementary row operation to the identity matrix. If we multiply another matrix by an elementary matrix, we're effectively applying the elementary row operation to the other matrix.

For example, suppose we are asked to find the product $EA$ where

$$


[\begin{aligned}0 & 1 \\ 1 & 0\end{aligned}]


$$

The elementary matrix $E$ comes from swapping the two rows of the identity matrix ($R_1 \leftrightarrow R_2$). So, to compute the product $EA,$ all we have to do is swap the two rows of $A\mathbin{:}$

$$


[\begin{aligned}8 & 6 \\ 3 & 4\end{aligned}]


$$

This may seem almost too easy. But it's true! And we can verify it by computing the product the long way, using matrix multiplication. Indeed, we get the same result:

$$


\begin{aligned}𝐸𝐴 & =[\begin{aligned}0 & 1 \\ 1 & 0\end{aligned}][\begin{aligned}3 & 4 \\ 8 & 6\end{aligned}] \\ & =[\begin{aligned}8 & 6 \\ 3 & 4\end{aligned}]\end{aligned}


$$

So, we say that $E \cdot A$ is equivalent to applying to $A$ the elementary row operation $R_1 \leftrightarrow R_2.$

**Watch out!** It's important to multiply $A$ from the *left*. If we multiply $A$ by an elementary matrix from the *right*, we will perform a *column* operation on $A$ (not a row operation). In this case, multiplying $A$ by $E$ from the right will have the effect of switching the *columns* of $A,$ not the rows.

$$


\begin{aligned}𝐴𝐸 & =[\begin{aligned}3 & 4 \\ 8 & 6\end{aligned}][\begin{aligned}0 & 1 \\ 1 & 0\end{aligned}] \\ & =[\begin{aligned}4 & 3 \\ 6 & 8\end{aligned}]\end{aligned}


$$

### Example: Finding a Row Operation That's Equivalent To Left Multiplication by an Elementary Matrix

#### Question

Let $[\begin{aligned}1 & 0 \\ 5 & 1\end{aligned}]$ Find the row operation that, when applied to a $2\times 2$ matrix $A,$ gives the result of the product $EA.$

#### Explanation

The matrix $E$ is obtained by taking the identity matrix and replacing the second row with the result of adding $5$ times the first row to the second row:

$$


\begin{aligned}𝐼 & =[\begin{aligned}1 & 0 \\ 0 & 1\end{aligned}] & 𝑅_{2} & :=5𝑅_{1}+𝑅_{2} \\ & ∼[\begin{aligned}1 & 0 \\ 5 & 1\end{aligned}] & & \\ & =𝐸 & & \end{aligned}


$$

Therefore, $EA$ is equivalent to applying the row operation $R_2:=5R_1+ R_2$ to $A.$

### Example: Finding a Matrix Product That's Equivalent To a Given Row Operation

#### Question

Suppose we are applying the elementary row operation $R_1:=R_1 - R_2$ to a $2\times 2$ matrix $A.$ Find the equivalent notation in terms of matrix multiplication.

#### Explanation

We need to find an elementary matrix $E$ such that $EA$ is equivalent to applying the elementary row operation $R_1:=R_1 - R_2$ to $A.$

To find $E,$ we apply the given row operation to the identity matrix as follows:

$$


\begin{aligned}𝐼 & =[\begin{aligned}1 & 0 \\ 0 & 1\end{aligned}] & 𝑅_{1} & :=𝑅_{1}−𝑅_{2} \\ & ∼[\begin{aligned}1 & −1 \\ 0 & 1\end{aligned}] & & \\ & =𝐸 & & \end{aligned}


$$

Therefore, the equivalent notation in terms of matrix multiplication is $EA\mathbin{:}$

$$


[\begin{aligned}1 & −1 \\ 0 & 1\end{aligned}]


$$

### Example: Finding a Matrix Product That's Equivalent To a Sequence of Row Operations

#### Question

Suppose that the following elementary row operations, in the given order, are to be applied to a $2\times 2$ matrix $A\mathbin{:}$

$$


R_1 \leftrightarrow R_2, \qquad R_2:=R_2+3R_1


$$

Find the equivalent notation in terms of matrix multiplication.

#### Explanation

First, let's find the elementary matrices corresponding to the two given elementary row operations.

- The first elementary row operation is $R_1 \leftrightarrow R_2.$ The corresponding elementary matrix can be found by applying this same elementary row operation to the identity matrix as follows:

- The second elementary row operation is $R_2:=R_2+3R_1.$ The corresponding elementary matrix can be found by applying this same elementary row operation to the identity matrix as follows:

To apply the first elementary row operation to the matrix $A,$ we multiply by $E_1$ on the left and get $E_1 A\mathbin{:}$

$$


[\begin{aligned}0 & 1 \\ 1 & 0\end{aligned}]


$$

Then, to apply the second elementary row operation to $E_1 A,$ we multiply by $E_2$ on the left and get $E_2 E_1 A\mathbin{:}$
