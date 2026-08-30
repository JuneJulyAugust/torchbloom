# Conformability for Matrix Multiplication

Source: https://www.mathacademy.com/topics/1198?courseId=136
Topic ID: 1198

## Prerequisites

- [Multiplying Square Matrices](./147-multiplying-square-matrices.md)
- [Multiplying a Matrix by a Column Vector](./1195-multiplying-a-matrix-by-a-column-vector.md)

## Lesson

### Introduction

Given two matrices, it is not always possible to multiply them together. To demonstrate why, consider the following two matrices:

$$


[\begin{aligned}1 & 12 \\ 6 & −4\end{aligned}]


$$

Normally, to compute the product $AB,$ we multiply each row of $A$ by each column of $B.$ However, in this case, each row of $A$ has $\color{blue}2$ entries, while each column of $B$ has $\color{red}3$ entries. The number of entries do not match!

$$


[\begin{aligned}1 & 12 \\ 6 & −4\end{aligned}]


$$

As a result, we cannot compute the dot product, and therefore the product $AB$ is not defined.

### Conformability for Matrix Multiplication

We can only multiply two matrices if they are **conformable** for multiplication, which means that the number of columns in the first matrix must equal the number of rows in the second matrix. In other words, we can only multiply two matrices if the first matrix has dimensions $𝑛$ and the second matrix has dimensions $𝑛$

If the matrices $A$ and $B$ (in that order) are conformable for multiplication and have dimensions $𝑛$ and $𝑛$ respectively, then the product $AB$ will have the dimensions $m \times k.$

Let's illustrate these ideas with some concrete examples.

### Example: Determining Whether Two Matrices Are Conformable for Multiplication

#### Question

Let $[\begin{aligned}19 & 2 \\ \sqrt{√2} & −1\end{aligned}]$ and $[\begin{aligned}1 & 2 & −1 \\ −1 & 1 & 2\end{aligned}]$

Which of the following statements are true?

1. The product $A\times B$ is well defined

2. The product $B\times A$ is well defined

#### Explanation

Notice that $A$ is a $2 \times 2$ matrix, and $B$ is a $2 \times 3$ matrix.

There are $2$ columns in $A$ and $2$ rows in $B.$ Since the number of columns in $A$ equals the number of rows in $B,$ the matrices $A$ and $B$ are conformable for multiplication:

$$


\underset{2 \times \color{green}{\fbox{2}}}{A} \underset{\color{green}\checkmark}{\times} \underset{{\color{green}\fbox{2}} \times 3}{B} = {\color{green}\text{well defined}}


$$

On the other hand, there are $3$ columns in $B$ and $2$ rows in $A.$ Since the number of columns in $B$ does **** equal the number of rows in $A,$ the matrices $B$ and $A$ are **** conformable for multiplication:

$$


\underset{2 \times \color{red}{3}}{B} \underset{\color{red}\neq}{\times} \underset{{\color{red}2} \times 2}{A} = {\color{red}\text{undefined}}


$$

Therefore, statement I is true, while statement II is false.

### Example: Determining the Dimension of the Product of Two Matrices Given the Dimensions of the Factors

#### Question

Suppose $A$ is a $3 \times 4$ matrix and $B$ is a $4 \times 2$ matrix. What are the dimensions of $AB$?

#### Explanation

There are $4$ columns in $A$ and $4$ rows in $B.$ Since the number of columns in $A$ equals the number of rows in $B,$ the matrices $A$ and $B$ are conformable for multiplication, and $AB$ is a $3 \times 2$ matrix:

$$


\underset{\boxed{3} \times \color{green}{\fbox{4}}}{A} \underset{\color{green}\checkmark}{\times} \underset{{\color{green}\fbox{4}} \times \boxed{2}}{B} = \underset{\boxed{3} \times \boxed{2}}{AB}


$$

### Example: Determining the Dimension of the Product of Two Matrices

#### Question

Let $\begin{aligned}−2 & 0 \\ −1 & −1 \\ 3 & −1 \\ −2 & 9\end{aligned}$ and $[\begin{aligned}−2 & −1 & 1 & −1 \\ 1 & 0 & 3 & 8\end{aligned}]$ What are the dimensions of $BA?$

#### Explanation

We notice that $A$ is a $4 \times 2$ matrix and $B$ is a $2 \times 4$ matrix.

There are $4$ columns in $B$ and $4$ rows in $A.$ Since the number of columns in $B$ equals the number of rows in $A,$ the matrices $B$ and $A$ are conformable for multiplication.

The product $BA$ has dimensions $2 \times 2\mathbin{:}$

$$


\underset{\boxed{2} \times \color{green}{\fbox{4}}}{B} \underset{\color{green}\checkmark}{\times} \underset{{\color{green}\fbox{4}} \times \boxed{2}}{A} = \underset{\boxed{2} \times \boxed{2}}{BA}


$$
