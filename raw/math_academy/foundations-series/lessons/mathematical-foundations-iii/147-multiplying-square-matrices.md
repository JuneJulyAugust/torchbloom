# Multiplying Square Matrices

Source: https://www.mathacademy.com/topics/147?courseId=136
Topic ID: 147

## Prerequisites

- [Calculating the Dot Product Using Components](./177-calculating-the-dot-product-using-components.md)
- [Zero, Square, Diagonal and Identity Matrices](./862-zero-square-diagonal-and-identity-matrices.md)

## Lesson

### Introduction

If we want to multiply one square matrix by another (which has the same dimensions), we multiply each row in the first matrix by each column in the second.

For example, suppose we want to multiply two matrices $A = \left\lbrack \matrix {1 & 6 \ 4 & 3} \right\rbrack$ and $B = \left\lbrack \matrix {-3 & 0 \ 2 & -5} \right\rbrack.$

The matrices $A$ and $B$ are both $2 \times 2$ matrices, and their product will be another $2 \times 2$ matrix $C,$ as follows:

$$


\begin{aligned} \underbrace{ \left\lbrack \matrix { 1 & 6 \\4 & 3 } \right\rbrack}_{A} \underbrace{ \left\lbrack \matrix { -3 & 0 \\2 & -5 } \right\rbrack}_{B} &= \underbrace{ \left\lbrack \matrix { \ast & \ast \\\ast & \ast } \right\rbrack }_{C} \end{aligned}


$$

Now, we calculate the entries of $C$ (shown as $\ast$'s in the equation above).

To find $c_{11},$ the entry at the intersection of the 1st row and 1st column, we calculate the dot product of the 1st row of $A$ and the 1st column of $B\mathbin{:}$

$$


\begin{aligned} \left\lbrack \matrix { \color{blue}{1} & \color{blue}{6} \\4 & 3 } \right\rbrack \left\lbrack \matrix { \color{red}{-3} & 0 \\\color{red}{2} & -5 } \right\rbrack &= \left\lbrack \matrix { {\color{blue}{1}} \cdot ({\color{red}{-3}}) + {\color{blue}{6}} \cdot {\color{red}{2}} & \ast \\\ast & \ast } \right\rbrack = \left\lbrack \matrix { 9 & \ast \\\ast & \ast } \right\rbrack \end{aligned}


$$

To find $c_{12},$ the entry at the intersection of the 1st row and 2nd column, we calculate the dot product of the 1st row of $A$ and the 2nd column of $B\mathbin{:}$

$$


\begin{aligned} \left\lbrack \matrix { \color{blue}{1} & \color{blue}{6} \\4 & 3 } \right\rbrack \left\lbrack \matrix { -3 & \color{red}{0} \\2 & \color{red}{-5} } \right\rbrack &= \left\lbrack \matrix { 9 & {\color{blue}{1}} \cdot {\color{red}{0}} + {\color{blue}{6}} \cdot ({\color{red}{-5}}) \\\ast & \ast } \right\rbrack = \left\lbrack \matrix { 9 & -30 \\\ast & \ast } \right\rbrack \end{aligned}


$$

To find $c_{21},$ the entry at the intersection of the 2nd row and 1st column, we calculate the dot product of the 2nd row of $A$ and the 1st column of $B\mathbin{:}$

$$


\begin{aligned} \left\lbrack \matrix { {1} & {6} \\\color{blue}{4} & \color{blue}{3} } \right\rbrack \left\lbrack \matrix { \color{red}{-3} & 0 \\\color{red}{2} & -5 } \right\rbrack &= \left\lbrack \matrix { 9 & -30 \\{\color{blue}{4}} \cdot ({\color{red}{-3}}) + {\color{blue}{3}} \cdot {\color{red}{2}} & \ast } \right\rbrack = \left\lbrack \matrix { 9 & -30 \\-6 & \ast } \right\rbrack \end{aligned}


$$

To find $c_{22},$ the entry at the intersection of the 2nd row and 2nd column, we calculate the dot product of the 2nd row of $A$ and the 2nd column of $B\mathbin{:}$

$$


\begin{aligned} \left\lbrack \matrix { {1} & {6} \\\color{blue}{4} & \color{blue}{3} } \right\rbrack \left\lbrack \matrix { -3 & \color{red}{0} \\2 & \color{red}{-5} } \right\rbrack &= \left\lbrack \matrix { 9 & -30 \\-6 & {\color{blue}{4}} \cdot {\color{red}{0}} + {\color{blue}{3}} \cdot ({\color{red}{-5}}) } \right\rbrack = \left\lbrack \matrix { 9 & -30 \\-6 & -15 } \right\rbrack \end{aligned}


$$

Therefore, our final answer is

$$


\begin{aligned} \left\lbrack \matrix { {1} & {6} \\4 & 3 } \right\rbrack \left\lbrack \matrix { -3 & 0 \\2 & -5 } \right\rbrack = \left\lbrack \matrix { 9 & -30 \\-6 & -15 } \right\rbrack. \end{aligned}


$$

### Example: Multiplying 2x2 Square Matrices

#### Question

Find $AB$ and $BA,$ if $[\begin{aligned}1 & 0 \\ −5 & 1\end{aligned}]$ and $[\begin{aligned}0 & 1 \\ −1 & 2\end{aligned}]$

#### Explanation

Multiplying each row in the first matrix by each column in the second, we get

$$


\begin{aligned}𝐴𝐵 & =[\begin{aligned}1 & 0 \\ −5 & 1\end{aligned}][\begin{aligned}0 & 1 \\ −1 & 2\end{aligned}] \\ & =[\begin{aligned}1⋅0+0⋅(−1) & 1⋅1+0⋅2 \\ −5⋅0+1⋅(−1) & −5⋅1+1⋅2\end{aligned}] \\ & =[\begin{aligned}0 & 1 \\ −1 & −3\end{aligned}]\end{aligned}


$$

and

$$


\begin{aligned}𝐵𝐴 & =[\begin{aligned}0 & 1 \\ −1 & 2\end{aligned}][\begin{aligned}1 & 0 \\ −5 & 1\end{aligned}] \\ & =[\begin{aligned}0⋅1+1⋅(−5) & 0⋅0+1⋅1 \\ −1⋅1+2⋅(−5) & −1⋅0+2⋅1\end{aligned}] \\ & =[\begin{aligned}−5 & 1 \\ −11 & 2\end{aligned}].\end{aligned}


$$

**** Notice that

$$


AB \neq BA.


$$

Matrix multiplication is not ****, meaning that when we switch the order of multiplication, we often get a different result (like we did in this example).

### Example: Finding an Entry of the Product of Two Matrices

#### Question

Let $Z=XY.$ What is the value of $z_{32}$, if

$$


\begin{aligned}1 & 2 & 0 \\ −2 & 0 & −1 \\ 1 & 2 & 3\end{aligned}


$$

#### Explanation

Multiplying the $3$rd row in $X$ by the $2$nd column in $Y$, we get

$$


\begin{aligned}𝑧_{32} & =[\begin{aligned}1 & 2 & 3\end{aligned}]\begin{aligned}−1 \\ 4 \\ −2\end{aligned} \\ & =1⋅(−1)+2⋅4+3⋅(−2) \\ & =−1+8−6 \\ & =1.\end{aligned}


$$

### Example: Multiplying 3x3 Square Matrices

#### Question

Find $AB$, if $\begin{aligned}−2 & 0 & 3 \\ 3 & −1 & −2 \\ −2 & 0 & −1\end{aligned}$ and $\begin{aligned}0 & 3 & −2 \\ 1 & −2 & 4 \\ −3 & −1 & 2\end{aligned}$

#### Explanation

Multiplying each row in the first matrix by each column in the second, we get

$$


\begin{aligned}𝐴𝐵 & =\begin{aligned}−2 & 0 & 3 \\ 3 & −1 & −2 \\ −2 & 0 & −1\end{aligned}\begin{aligned}0 & 3 & −2 \\ 1 & −2 & 4 \\ −3 & −1 & 2\end{aligned} \\ & =\begin{aligned}0+0−9 & −6+0−3 & 4+0+6 \\ 0−1+6 & 9+2+2 & −6−4−4 \\ 0+0+3 & −6+0+1 & 4+0−2\end{aligned} \\ & =\begin{aligned}−9 & −9 & 10 \\ 5 & 13 & −14 \\ 3 & −5 & 2\end{aligned}.\end{aligned}


$$
