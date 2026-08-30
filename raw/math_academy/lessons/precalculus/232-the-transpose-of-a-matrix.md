# The Transpose of a Matrix

Source: https://www.mathacademy.com/topics/232?courseId=43
Topic ID: 232

## Prerequisites

- [Scalar Multiplication of Matrices](./146-scalar-multiplication-of-matrices.md)

## Lesson

### Introduction

To take the **transpose of a matrix**, we interchange each of its columns with the corresponding row. That is, row $1$ becomes column $1,$ row $2$ becomes column $2,$ and so on. A superscript ${}^{T}$ is used to denote the transpose operation.

For example, the transpose of the $2 \times 3$ matrix ${X}$ is the following $3 \times 2$ matrix $X^T\mathbin{:}$

$$



{X} = \left\lbrack \matrix { {\color{red}7} & {\color{red}2} & {\color{red}-4} \ {\color{blue}-3} & {\color{blue}1} & {\color{blue}0} } \right\rbrack \qquad\implies\qquad {X}^T = \left\lbrack \matrix { {\color{red}7} & {\color{blue}-3} \ {\color{red}2} & {\color{blue}1} \ {\color{red}-4} & {\color{blue}0} } \right\rbrack



$$

The first row of $X$ becomes the first column of $X^T,$ and the second row of $X$ becomes the second column of $X^T.$

Note that transposing a matrix swaps its dimensions. In general, we have the following property:

*When a matrix is transposed, its dimensions switch from $m \times n$ to $n \times m.$*

Also, notice that the transpose of a column vector is a row vector:

$$



{A} = \left\lbrack \matrix { 5 \ 4 \ 2 } \right\rbrack \qquad \implies\qquad {A}^T = \left\lbrack \matrix { 5 & 4 & 2 } \right\rbrack



$$

Similarly, the transpose of a row vector is a column vector:

$$



{B} = \left\lbrack \matrix { 8 & -10 & 0 & 6 } \right\rbrack \qquad\implies\qquad {B}^T = \left\lbrack \matrix { 8 \ -10 \ 0 \ 6 } \right\rbrack



$$

### Example: Finding the Transpose of a Matrix

#### Question

Find $C^T,$ if $\begin{aligned}−1 & 1 \\ 0 & 2 \\ −2 & −3\end{aligned}$

#### Explanation

To find the transpose, we interchange the rows and columns:

$$



[\begin{aligned}−1 & 0 & −2 \\ 1 & 2 & −3\end{aligned}]



$$

### Example: Finding the Transpose of a Row Vector or Column Vector

#### Question

If ${A} = \left\lbrack \matrix {5 & -1 & 0 \} \right\rbrack,$ then what is ${A^T}?$

#### Explanation

To find the transpose, we interchange the rows and columns.

Here, there is just a single row, so it becomes a single column:

$$



{A}^T = \left\lbrack \matrix { 5 \ -1 \ 0 \ } \right\rbrack



$$

### Example: Determining the Dimensions of the Transpose of a Matrix

#### Question

Consider the matrix ${B} = \left\lbrack \matrix {1 & 2 & 4 & 2\ 4 & 4 & 1 & 1\ 3 & -3 & 0 & -1} \right\rbrack.$ What are the dimensions of ${B}^T?$

#### Explanation

When a matrix is transposed, its dimensions switch from $N \times M$ to $M \times N.$

So, since $B$ is a $3 \times 4$ matrix, the transpose ${B}^T$ is a $4\times3$ matrix.

### Properties of the Transpose of a Matrix

Remember that transposing a matrix swaps the rows and columns. So, if $B=A^T,$ then $b_{ij}=a_{ji}$ for all values of $i$ and $j.$

Geometrically, when a matrix is transposed, the diagonal elements (those with $i=j$) remain the same while all other elements are reflected across the diagonal. For example,

$$



{A} = \left\lbrack \matrix { \color{red}{3} & \color{blue}{7} \ 1 & \color{red}{6} } \right\rbrack \qquad \implies\qquad {A}^T = \left\lbrack \matrix { \color{red}{3} & 1 \ \color{blue}{7} & \color{red}{6} } \right\rbrack.



$$

Also, transposing a matrix twice results in the original matrix. More precisely, for any matrix $A,$ we have

$$



\left( A^T\right)^T = A.



$$

This happens because, in the first transpose, we swap the rows of $A$ for the columns, and then in the second transpose, we swap them back again. For example,

$$



{A} = \left\lbrack \matrix { \color{red}{3} & \color{blue}{7} \ 1 & \color{red}{6} } \right\rbrack \quad \implies\quad {A}^T = \left\lbrack \matrix { \color{red}{3} & 1 \ \color{blue}{7} & \color{red}{6} } \right\rbrack \quad \implies\quad \left( {A}^T\right)^T = \left\lbrack \matrix { \color{red}{3} & \color{blue}{7} \ 1 & \color{red}{6} } \right\rbrack =A.



$$

Finally, for any numbers $c_1,c_2$ and any $m \times n$ matrices $A,B$ we have the following rule:

$$



(c_1 A \pm c_2 B)^T = c_1 A^T \pm c_2 B^T



$$
