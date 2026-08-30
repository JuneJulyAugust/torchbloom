# Multiplying a Matrix by a Column Vector

Source: https://www.mathacademy.com/topics/1195?courseId=101
Topic ID: 1195

## Prerequisites

- [Scalar Multiplication of Matrices](./146-scalar-multiplication-of-matrices.md)
- [Calculating the Dot Product Using Components](./177-calculating-the-dot-product-using-components.md)
- [Zero, Square, Diagonal and Identity Matrices](./862-zero-square-diagonal-and-identity-matrices.md)

## Lesson

### Introduction

To multiply a matrix by a column vector, we multiply each row in the matrix by the column vector using the dot product.

For example, suppose we would like to multiply $[\begin{aligned}1 & 3 \\ 6 & 7\end{aligned}]$ and $[\begin{aligned}−3 \\ 4\end{aligned}]$

First, we write the multiplication as follows:

$$


[\begin{aligned}1 & 3 \\ 6 & 7\end{aligned}]


$$

The result of the multiplication is another column vector $\mathbf{y}$ with the same dimensions as $\mathbf{x}$. Now, we calculate the entries of the product (shown as $\ast$'s in the equation above).

To find $y_1,$ the $1$st component of $\mathbf{y}$, we calculate the dot product of the $1$st row of $A$ and the vector $\mathbf{x}\mathbin{:}$

$$


[\begin{aligned}1 & 3 \\ 6 & 7\end{aligned}]


$$

To find $y_2,$ the $2$nd component of $\mathbf{y},$ we calculate the dot product of the $2$nd row of $A$ and the vector $\mathbf{x}\mathbin{:}$

$$


[\begin{aligned}1 & 3 \\ 6 & 7\end{aligned}]


$$

Therefore,

$$


[\begin{aligned}9 \\ 10\end{aligned}]


$$

### Example: Multiplying a 2x2 Matrix by a Column Vector

#### Question

Find $A\mathbf{x}$ if $[\begin{aligned}1 & 3 \\ 7 & −2\end{aligned}]$ and $[\begin{aligned}2 \\ 5\end{aligned}]$

#### Explanation

We multiply each row in the matrix by the column vector using the dot product. Multiplying the first row, we get

$$


\begin{aligned}[\begin{aligned}1 & 3 \\ 7 & −2\end{aligned}][\begin{aligned}2 \\ 5\end{aligned}] & =[\begin{aligned}1⋅2+3⋅5 \\ ∗\end{aligned}]=[\begin{aligned}17 \\ ∗\end{aligned}].\end{aligned}


$$

Multiplying the second row, we get

$$


\begin{aligned}[\begin{aligned}1 & 3 \\ 7 & −2\end{aligned}][\begin{aligned}2 \\ 5\end{aligned}] & =[\begin{aligned}17 \\ 7⋅2+(−2)⋅5\end{aligned}]=[\begin{aligned}17 \\ 4\end{aligned}].\end{aligned}


$$

Therefore, $[\begin{aligned}17 \\ 4\end{aligned}]$

### Example: Multiplying a 3x3 Matrix by a Column Vector

#### Question

Find $A\mathbf{x}$ if $\begin{aligned}−3 & 1 & 1 \\ 2 & 0 & 0 \\ −1 & −2 & 5\end{aligned}$ and $\begin{aligned}1 \\ −2 \\ 0\end{aligned}$

#### Explanation

We multiply each row in the matrix by the column vector using the dot product:

$$


\begin{aligned}𝐴𝐱 & =\begin{aligned}−3 & 1 & 1 \\ 2 & 0 & 0 \\ −1 & −2 & 5\end{aligned}\begin{aligned}1 \\ −2 \\ 0\end{aligned} \\ & =\begin{aligned}(−3)⋅1+1⋅(−2)+1⋅0 \\ 2⋅1+0⋅(−2)+0⋅0 \\ (−1)⋅1+(−2)⋅(−2)+5⋅0\end{aligned} \\ & =\begin{aligned}−3−2+0 \\ 2+0+0 \\ −1+4+0\end{aligned} \\ & =\begin{aligned}−5 \\ 2 \\ 3\end{aligned}\end{aligned}


$$

### Example: Multiplying a Matrix With Variable Entries by a Column Vector

#### Question

Find $A\mathbf{x}$ if $[\begin{aligned}𝑎 & 𝑐 \\ 𝑏 & 𝑑\end{aligned}]$ and $[\begin{aligned}3 \\ 2\end{aligned}]$

#### Explanation

We multiply each row in the matrix by the column vector using the dot product:

$$


\begin{aligned}𝐴𝐱 & =[\begin{aligned}𝑎 & 𝑐 \\ 𝑏 & 𝑑\end{aligned}][\begin{aligned}3 \\ 2\end{aligned}] \\ & =[\begin{aligned}𝑎⋅3+𝑐⋅2 \\ 𝑏⋅3+𝑑⋅2\end{aligned}] \\ & =[\begin{aligned}3𝑎+2𝑐 \\ 3𝑏+2𝑑\end{aligned}]\end{aligned}


$$

### Alternative Rule

An alternative, yet equivalent, procedure for multiplying a matrix by a column vector involves adding scaled columns of the matrix $A$ as follows:

$$


\begin{aligned}𝐴𝐱 & =[\begin{aligned}𝑎 & 𝑐 \\ 𝑏 & 𝑑\end{aligned}][\begin{aligned}3 \\ 2\end{aligned}] \\ & =3[\begin{aligned}𝑎 \\ 𝑏\end{aligned}]+2[\begin{aligned}𝑐 \\ 𝑑\end{aligned}] \\ & =[\begin{aligned}3𝑎 \\ 3𝑏\end{aligned}]+[\begin{aligned}2𝑐 \\ 2𝑑\end{aligned}] \\ & =[\begin{aligned}3𝑎+2𝑐 \\ 3𝑏+2𝑑\end{aligned}]\end{aligned}


$$

If we denote $[\begin{aligned}𝑎 \\ 𝑏\end{aligned}]$ and $[\begin{aligned}𝑐 \\ 𝑑\end{aligned}]$ then we can also write the multiplication as follows:

$$


A\mathbf{x}={\color{blue}3}\mathbf{u}_1 + {\color{blue}2} \mathbf{u}_2


$$

The expression above is a **linear combination** of the vectors $\mathbf{u}_1$ and $\mathbf{u}_2,$ where the corresponding coefficients are given by the entries of the vector $\mathbf{x}.$
