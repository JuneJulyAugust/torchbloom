# Elementary 3x3 Matrices

Source: https://www.mathacademy.com/topics/1731?courseId=55
Topic ID: 1731

## Prerequisites

- [Elementary 2x2 Matrices](./1726-elementary-2x2-matrices.md)

## Lesson

### Introduction

Just like for $2\times 2$ matrices, there are also **elementary $3\times 3$ matrices**. These are matrices that can be obtained by applying *only one* elementary row operation to the identity matrix $\begin{aligned}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{aligned}$

For instance, consider the following $3\times 3$ matrices:

$$


\begin{aligned}0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1\end{aligned}


$$

These are all examples of elementary matrices:

- $E_1$ is obtained from $I_3$ by applying the row operation $R_1 \leftrightarrow R_2.$

- $E_2$ is obtained from $I_3$ by applying the row operation $R_2:= 2R_2.$

- $E_3$ is obtained from $I_3$ by applying the row operation $R_2:= R_2 + 3R_1.$

They are also examples of the three different types of elementary matrices, defined by the corresponding row operations.

### Example: Identifying an Elementary 3x3 Matrix

#### Question

Is $\begin{aligned}1 & 0 & 0 \\ 8 & 1 & 0 \\ 0 & 0 & 1\end{aligned}$ an elementary matrix?

#### Explanation

Remember that an elementary matrix is obtained by performing exactly one elementary row operation on the identity matrix $I.$

The given matrix $E$ is an elementary matrix because it can be obtained from $I$ by applying the elementary row operation $R_2:= R_2 + 8R_1,$ as follows:

$$


\begin{aligned}𝐼 & =\begin{aligned}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{aligned} & 𝑅_{2} & :=𝑅_{2}+8𝑅_{1} \\ & ∼\begin{aligned}1 & 0 & 0 \\ 8 & 1 & 0 \\ 0 & 0 & 1\end{aligned} & & \\ & =𝐸 & & \end{aligned}


$$

### The Inverse of an Elementary Matrix

As we saw before for elementary $2\times 2$ matrices, each elementary $3\times 3$ matrix $E$ is invertible, and the corresponding inverse is always an elementary matrix of the same type as $E.$ To illustrate, let's consider the matrix

$$


\begin{aligned}1 & 0 & 0 \\ 4 & 1 & 0 \\ 0 & 0 & 1\end{aligned}


$$

To find the inverse of $E,$ we proceed as follows:

**Step 1:** Write down $\color{blue}E$ and the identity matrix $I_3$ side-by-side, as shown below:

$$


\begin{aligned}1 & 0 & 0 & 1 & 0 & 0 \\ 4 & 1 & 0 & 0 & 1 & 0 \\ 0 & 0 & 1 & 0 & 0 & 1\end{aligned}


$$

**Step 2:** Apply an elementary row operation that transforms the left matrix into the identity matrix. In our case, we need to apply the transformation $R_2:= R_2 + (-4)R_1.$ We apply the operation to entire row (not only the left part):

$$


\begin{aligned}[𝐸\,|\,𝐼_{3}] & =\begin{aligned}1 & 0 & 0 & 1 & 0 & 0 \\ 4 & 1 & 0 & 0 & 1 & 0 \\ 0 & 0 & 1 & 0 & 0 & 1\end{aligned} & & 𝑅_{2}:=𝑅_{2}+(−4)𝑅_{1} \\ & ∼\begin{aligned}1 & 0 & 0 & 1 & 0 & 0 \\ 0 & 1 & 0 & −4 & 1 & 0 \\ 0 & 0 & 1 & 0 & 0 & 1\end{aligned} & & \\ & =[𝐼_{3}\,|\,𝐸^{−1}] & & \end{aligned}


$$

We conclude that $R_2:= R_2 + (-4)R_1$ transforms $E$ back into the identity matrix. Likewise, when this row operation is applied to the identity matrix, it generates $E^{-1}.$

The matrix $E^{-1}$ is obtained on the right-hand side of our big matrix after the transformation. Therefore,

$$


\begin{aligned}1 & 0 & 0 \\ −4 & 1 & 0 \\ 0 & 0 & 1\end{aligned}


$$

We can work out the inverse of all elementary $3\times 3$ matrices in a similar way.

### Example: Finding the Inverse of an Elementary 3x3 Matrix

#### Question

What is the inverse of the elementary matrix $\begin{aligned}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & −5\end{aligned}$

#### Explanation

We write down $E$ and the identity matrix $I$ side-by-side (as shown below) and apply an elementary row operation that transforms the left matrix into the identity matrix:

$$


\begin{aligned}[𝐸\,|\,𝐼\,] & =\begin{aligned}1 & 0 & 0 & 1 & 0 & 0 \\ 0 & 1 & 0 & 0 & 1 & 0 \\ 0 & 0 & −5 & 0 & 0 & 1\end{aligned} & & 𝑅_{3}:=−\frac{1}{5}𝑅_{3} \\ & ∼\begin{aligned}1 & 0 & 0 & 1 & 0 & 0 \\ 0 & 1 & 0 & 0 & 1 & 0 \\ 0 & 0 & 1 & 0 & 0 & −\frac{1}{5}\end{aligned} & & \end{aligned}


$$

The inverse is obtained on the right-hand side of our big matrix after the transformation. Therefore,

$$


\begin{aligned}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & −\frac{1}{5}\end{aligned}


$$

### Example: Computing a Product Involving an Inverse of an Elementary 3x3 Matrix

#### Question

Find the product $E_{1}^{-1}E_2$, where

$$


\begin{aligned}𝐸_{1}=\begin{aligned}1 & 0 & 0 \\ −11 & 1 & 0 \\ 0 & 0 & 1\end{aligned},\,𝐸_{2} & =\begin{aligned}1 & 0 & −5 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{aligned}.\end{aligned}


$$

#### Explanation

Notice that $E_1$ and $E_2$ are both elementary matrices.

First, we need to find $E_1^{-1}.$ We write down $E_1$ and the identity matrix $I$ side-by-side (as shown below) and apply an elementary row operation that transforms the left matrix into the identity matrix:

$$


\begin{aligned}[𝐸_{1}\,|\,𝐼\,] & =\begin{aligned}1 & 0 & 0 & 1 & 0 & 0 \\ −11 & 1 & 0 & 0 & 1 & 0 \\ 0 & 0 & 1 & 0 & 0 & 1\end{aligned} & & 𝑅_{2}:=𝑅_{2}+11𝑅_{1} \\ & ∼\begin{aligned}1 & 0 & 0 & 1 & 0 & 0 \\ 0 & 1 & 0 & 11 & 1 & 0 \\ 0 & 0 & 1 & 0 & 0 & 1\end{aligned} & & \end{aligned}


$$

Therefore,

$$


\begin{aligned}1 & 0 & 0 \\ 11 & 1 & 0 \\ 0 & 0 & 1\end{aligned}


$$

Now, we can find the product $E_1^{-1} E_{2}\mathbin{:}$

$$


\begin{aligned}1 & 0 & 0 \\ 11 & 1 & 0 \\ 0 & 0 & 1\end{aligned}


$$
