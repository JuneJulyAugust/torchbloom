# Elementary 2x2 Matrices

Source: https://www.mathacademy.com/topics/1726?courseId=154
Topic ID: 1726

## Prerequisites

- [Introduction to the Inverse of a Matrix](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/863-introduction-to-the-inverse-of-a-matrix.md)
- [Creating Rows or Columns Containing Zeros Using Gaussian Elimination](./3029-creating-rows-or-columns-containing-zeros-using-gaussian-elimination.md)

## Lesson

### Introduction

An **elementary matrix** is a matrix that can be obtained from the identity matrix by applying *only one* elementary row operation.

For example, starting with the $2 \times 2$ identity matrix $[\begin{aligned}1 & 0 \\ 0 & 1\end{aligned}]$ we can apply a single elementary row operation to get any of the matrices below:

$$


[\begin{aligned}0 & 1 \\ 1 & 0\end{aligned}]


$$

- $E_1$ is obtained from $I_2$ by applying the row operation $R_1 \leftrightarrow R_2.$

- $E_2$ is obtained from $I_2$ by applying the row operation $R_1:=2R_1.$

- $E_3$ is obtained from $I_2$ by applying the row operation $R_2:= R_2 + (-7)R_1.$

### Example: Identifying an Elementary 2x2 Matrix

#### Question

Is $\begin{aligned}𝐸=[\begin{aligned}1 & 0 \\ −5 & 1\end{aligned}]\end{aligned}$ an elementary matrix?

#### Explanation

An elementary matrix is a matrix obtained from the identity matrix by applying exactly one elementary row operation.

The given matrix $E$ is an elementary matrix because it can be obtained from $I_2$ by applying the elementary row operation $R_2:= R_2+(-5) R_1,$ as follows:

$$


\begin{aligned}𝐼_{2} & =[\begin{aligned}1 & 0 \\ 0 & 1\end{aligned}] & 𝑅_{2} & :=𝑅_{2}+(−5)𝑅_{1} \\ & ∼[\begin{aligned}1 & 0 \\ −5 & 1\end{aligned}] & & \\ & =𝐸 & & \end{aligned}


$$

### The Inverse of an Elementary Matrix

Each elementary matrix $E$ is invertible, and the corresponding inverse is always an elementary matrix of the same type as $E$. To illustrate, let's consider the matrix

$$


[\begin{aligned}1 & 0 \\ 4 & 1\end{aligned}]


$$

To find the inverse of $E,$ we proceed as follows:

**Step 1:** Write down $\color{blue}E$ and the identity matrix $I_2$ side-by-side, as shown below:

$$


\begin{aligned}1 & 0 & 1 & 0 \\ 4 & 1 & 0 & 1\end{aligned}


$$

**Step 2:** Apply an elementary row operation that transforms the left matrix into the identity matrix. In our case, we need to apply the transformation $R_2:= R_2 + (-4)R_1.$ We apply the operation to the entire row (not only the left part):

$$


\begin{aligned}[𝐸\,|\,𝐼_{2}] & =[\begin{aligned}1 & 0 & 1 & 0 \\ 4 & 1 & 0 & 1\end{aligned}] & & 𝑅_{2}:=𝑅_{2}+(−4)𝑅_{1} \\ & ∼[\begin{aligned}1 & 0 & 1 & 0 \\ 0 & 1 & −4 & 1\end{aligned}] & & \\ & =[𝐼_{2}\,|\,𝐸^{−1}] & & \end{aligned}


$$

The matrix $E^{-1}$ is obtained on the right-hand side of our big matrix after the transformation. Therefore,

$$


[\begin{aligned}1 & 0 \\ −4 & 1\end{aligned}]


$$

We can work out the inverse of all elementary $2 \times 2$ matrices in a similar way.

### Example: Finding the Inverse of an Elementary 2x2 Matrix

#### Question

Find the inverse of the elementary matrix $\begin{aligned}1 & 0 \\ 0 & \frac{2}{5}\end{aligned}$

#### Explanation

We write down $E$ and the identity matrix $I$ side-by-side (as shown below) and apply an elementary row operation that transforms the left matrix into the identity matrix:

$$


\begin{aligned}[𝐸\,|\,𝐼\,] & =\begin{aligned}1 & 0 & 1 & 0 \\ 0 & \frac{2}{5} & 0 & 1\end{aligned} & & 𝑅_{2}:=\frac{5}{2}𝑅_{2} \\ & ∼\begin{aligned}1 & 0 & 1 & 0 \\ 0 & 1 & 0 & \frac{5}{2}\end{aligned} & & \end{aligned}


$$

The inverse is obtained on the right-hand side of our big matrix after the transformation. Therefore,

$$


\begin{aligned}1 & 0 \\ 0 & \frac{5}{2}\end{aligned}


$$

### Example: Computing a Product Involving the Inverse of an Elementary 2x2 Matrix

#### Question

Find the product $E_1 E_{2}^{-1},$ where $[\begin{aligned}1 & 0 \\ −5 & 1\end{aligned}]$ and $[\begin{aligned}1 & −2 \\ 0 & 1\end{aligned}]$

#### Explanation

Notice that $E_1$ and $E_2$ are both elementary matrices.

First, we need to find $E_2^{-1}.$ We write down $E_2$ and the identity matrix $I$ side-by-side (as shown below) and apply an elementary row operation that transforms the left matrix into the identity matrix:

$$


\begin{aligned}[𝐸_{2}\,|\,𝐼\,] & =[\begin{aligned}1 & −2 & 1 & 0 \\ 0 & 1 & 0 & 1\end{aligned}] & & 𝑅_{1}:=𝑅_{1}+2𝑅_{2} \\ & ∼[\begin{aligned}1 & 0 & 1 & 2 \\ 0 & 1 & 0 & 1\end{aligned}] & & \end{aligned}


$$

Therefore,

$$


[\begin{aligned}1 & 2 \\ 0 & 1\end{aligned}]


$$

Now, we can find the product $E_1 E_{2}^{-1}\mathbin{:}$

$$


[\begin{aligned}1 & 0 \\ −5 & 1\end{aligned}]


$$
