# Multiplying Matrices

Source: https://www.mathacademy.com/topics/1196?courseId=43
Topic ID: 1196

## Prerequisites

- [Conformability for Matrix Multiplication](./1198-conformability-for-matrix-multiplication.md)

## Lesson

### Introduction

When multiplying two matrices in general, we apply the same approach as usual:

1. First, we verify that the two matrices are conformable for multiplication.

2. Then, we multiply each row in the first matrix by each column in the second.

For example, let's find $AB,$ where $[\begin{aligned}−2 & 2 & 1 \\ 1 & −1 & 3\end{aligned}]$ and $\begin{aligned}−5 & 2 \\ 2 & −2 \\ −4 & 1\end{aligned}$

First, we verify the conformability for multiplication:

$$



\underset{\boxed{2} \times \color{green}{\fbox{3}}}{A} \underset{\color{green}\checkmark}{\cdot} \underset{{\color{green}\fbox{3}} \times \boxed{2}}{B} = \underset{\boxed{2} \times \boxed{2}}{C}



$$

So the matrices are conformable for multiplication, and the product is a $2 \times 2$ matrix. Let's set up the multiplication:

$$



\begin{aligned} \underbrace{ \left\lbrack \matrix { -2 & 2 & 1 \\1 & -1 & 3 } \right\rbrack}_{A} \underbrace{ \left\lbrack \matrix { -5 & 2 \\2 & -2 \\-4 & 1 } \right\rbrack}_{B} &= \underbrace{ \left\lbrack \matrix { \ast & \ast \\\ast & \ast } \right\rbrack }_{C} \end{aligned}



$$

Now, we calculate the entries of the product matrix (shown as $\ast$'s in the equation above).

To find $c_{11},$ the entry at the intersection of the $1$st row and $1$st column, we calculate the dot product of the $1$st row of $A$ and the $1$st column of $B\mathbin{:}$

$$



\begin{aligned} \left\lbrack \matrix { \color{blue}-2 & \color{blue}2 & \color{blue}1 \\\color{lightgray}1 & \color{lightgray}-1 & \color{lightgray}3 } \right\rbrack \left\lbrack \matrix { \color{red}-5 & \color{lightgray}2 \\\color{red}2 & \color{lightgray}-2 \\\color{red}-4 & \color{lightgray}1 } \right\rbrack \% &= \% \left\lbrack \% \matrix { \% ({\color{blue}{-2}}) \cdot ({\color{red}{-5}}) + {\color{blue}{2}} \cdot {\color{red}{2}} + {\color{blue}{1}} \cdot ({\color{red}{-4}}) & \ast \\\% \ast & \ast \% } \% \right\rbrack = \left\lbrack \matrix { \boxed{10} & \ast \\\ast & \ast } \right\rbrack, && \quad \boxed{10} = ({\color{blue}{-2}}) \cdot ({\color{red}{-5}}) + {\color{blue}{2}} \cdot {\color{red}{2}} + {\color{blue}{1}} \cdot ({\color{red}{-4}}) \end{aligned}



$$

To find $c_{12},$ we calculate the dot product of the $1$st row of $A$ and the $2$nd column of $B\mathbin{:}$

$$



\begin{aligned} \left\lbrack \matrix { \color{blue}-2 & \color{blue}2 & \color{blue}1 \\\color{lightgray}1 & \color{lightgray}-1 & \color{lightgray}3 } \right\rbrack \left\lbrack \matrix { \color{lightgray}-5 & \color{red}2 \\\color{lightgray}2 & \color{red}-2 \\\color{lightgray}-4 & \color{red}1 } \right\rbrack \% &= \% \left\lbrack \% \matrix { \% 10 & ({\color{blue}{-2}}) \cdot {\color{red}{2}} + {\color{blue}{2}} \cdot ({\color{red}{-2}}) + {\color{blue}{1}} \cdot {\color{red}{1}} \\\% \ast & \ast \% } \% \right\rbrack = \left\lbrack \matrix { 10 & \boxed{-7} \\\ast & \ast } \right\rbrack, && \quad \boxed{-7} = ({\color{blue}{-2}}) \cdot {\color{red}{2}} + {\color{blue}{2}} \cdot ({\color{red}{-2}}) + {\color{blue}{1}} \cdot {\color{red}{1}} \end{aligned}



$$

To find $c_{21},$ we calculate the dot product of the $2$nd row of $A$ and the $1$st column of $B\mathbin{:}$

$$



\begin{aligned} \left\lbrack \matrix { \color{lightgray}-2 & \color{lightgray}2 & \color{lightgray}1 \\\color{blue}1 & \color{blue}-1 & \color{blue}3 } \right\rbrack \left\lbrack \matrix { \color{red}-5 & \color{lightgray}2 \\\color{red}2 & \color{lightgray}-2 \\\color{red}-4 & \color{lightgray}1 } \right\rbrack \% &= \% \left\lbrack \% \matrix { \% 10 & -7 \\\% {\color{blue}{1}} \cdot ({\color{red}{-5}}) + ({\color{blue}{-1}}) \cdot {\color{red}{2}} + {\color{blue}{3}} \cdot ({\color{red}{-4}}) & \ast \% } \% \right\rbrack = \left\lbrack \matrix { 10 & -7 \\\boxed{-19} & \ast } \right\rbrack, && \quad \boxed{-19} = {\color{blue}{1}} \cdot ({\color{red}{-5}}) + ({\color{blue}{-1}}) \cdot {\color{red}{2}} + {\color{blue}{3}} \cdot ({\color{red}{-4}}) \end{aligned}



$$

Finally, to find $c_{22},$ we calculate the dot product of the $2$nd row of $A$ and the $2$nd column of $B\mathbin{:}$

$$



\begin{aligned} \left\lbrack \matrix { \color{lightgray}-2 & \color{lightgray}2 & \color{lightgray}1 \\\color{blue}1 & \color{blue}-1 & \color{blue}3 } \right\rbrack \left\lbrack \matrix { \color{lightgray}-5 & \color{red}2 \\\color{lightgray}2 & \color{red}-2 \\\color{lightgray}-4 & \color{red}1 } \right\rbrack \% &= \% \left\lbrack \% \matrix { \% 10 & -7 \\\% -19 & {\color{blue}{1}} \cdot {\color{red}{2}} + ({\color{blue}{-1}}) \cdot ({\color{red}{-2}}) + {\color{blue}{3}} \cdot {\color{red}{1}} \% } \% \right\rbrack = \left\lbrack \matrix { 10 & -7 \\-19 & \boxed{7} } \right\rbrack, && \quad \boxed{7} = {\color{blue}{1}} \cdot {\color{red}{2}} + ({\color{blue}{-1}}) \cdot ({\color{red}{-2}}) + {\color{blue}{3}} \cdot {\color{red}{1}} \end{aligned}



$$

Therefore, we have $[\begin{aligned}10 & −7 \\ −19 & 7\end{aligned}]$

### Example: Multiplying Two Matrices When They Are Conformable

#### Question

Find $CD$, if $[\begin{aligned}1 & −2 & 0 \\ 2 & 1 & 1\end{aligned}]$ and $\begin{aligned}0 & 1 \\ 2 & 0 \\ −3 & 2\end{aligned}$

#### Explanation

Here, $C$ is a $2 \times 3$ matrix and $D$ is a $3 \times 2$ matrix.

There are $3$ columns in $C$ and $3$ rows in $D,$ so $C$ and $D$ are conformable for multiplication:

$$



\underset{\boxed{2} \times \color{green}{\fbox{3}}}{C} \underset{\color{green}\checkmark}{\cdot} \underset{{\color{green}\fbox{3}} \times \boxed{2}}{D} = \underset{\boxed{2} \times \boxed{2}}{CD}



$$

Let's compute $CD,$ one element at a time:

$$



\begin{aligned} & [\begin{aligned}1 & −2 & 0 \\ 2 & 1 & 1\end{aligned}]\begin{aligned}0 & 1 \\ 2 & 0 \\ −3 & 2\end{aligned}=[\begin{aligned}−4 & ∗ \\ ∗ & ∗\end{aligned}], & & \,−4=1⋅0+(−2)⋅2+0⋅(−3) \\ & [\begin{aligned}1 & −2 & 0 \\ 2 & 1 & 1\end{aligned}]\begin{aligned}0 & 1 \\ 2 & 0 \\ −3 & 2\end{aligned}=[\begin{aligned}−4 & 1 \\ ∗ & ∗\end{aligned}], & & \,1=1⋅1+(−2)⋅0+0⋅2 \\ & [\begin{aligned}1 & −2 & 0 \\ 2 & 1 & 1\end{aligned}]\begin{aligned}0 & 1 \\ 2 & 0 \\ −3 & 2\end{aligned}=[\begin{aligned}−4 & 1 \\ −1 & ∗\end{aligned}], & & \,−1=2⋅0+1⋅2+1⋅(−3) \\ & [\begin{aligned}1 & −2 & 0 \\ 2 & 1 & 1\end{aligned}]\begin{aligned}0 & 1 \\ 2 & 0 \\ −3 & 2\end{aligned}=[\begin{aligned}−4 & 1 \\ −1 & 4\end{aligned}], & & \,4=2⋅1+1⋅0+1⋅2\end{aligned}



$$

Therefore, $[\begin{aligned}−4 & 1 \\ −1 & 4\end{aligned}]$

### Example: Finding an Entry of the Product of Two Matrices

#### Question

Let $C=AB.$ What is the value of $c_{32}$, if

$$



\begin{aligned}1 & 2 \\ −2 & 0 \\ 1 & 2\end{aligned}



$$

#### Explanation

Multiplying the $3$rd row in $A$ by the $2$nd column in $B$, we get

$$



\begin{aligned}𝑐_{32} & =\begin{aligned}1 & 2 \\ −2 & 0 \\ 1 & 2\end{aligned}[\begin{aligned}3 & 4 & −1 \\ 1 & −2 & 2\end{aligned}] \\ & =[\begin{aligned}1 & 2\end{aligned}][\begin{aligned}4 \\ −2\end{aligned}] \\ & =1⋅4+2⋅(−2) \\ & =4−4 \\ & =0.\end{aligned}



$$

### Example: Multiplying a Column-Vector By a Row-Vector

#### Question

Compute the product $\left\lbrack \matrix {-1 \ 0 \ -2} \right\rbrack \left\lbrack \matrix {2 & -5} \right\rbrack.$

#### Explanation

Here, the first factor is a $3 \times 1$ matrix and the second factor is a $1 \times 2$ matrix.

There is $1$ column in the first matrix and $1$ row in the second matrix, so the product is well defined:

$$



\boxed{3} \times {\color{green}\fbox{1}} {\color{green}\checkmark} {\color{green}\fbox{1}} \times \boxed{2} = \boxed{3} \times \boxed{2}



$$

Computing the product, we have

$$



\begin{aligned} \left\lbrack \matrix { -1 \\0 \\-2 } \right\rbrack \left\lbrack \matrix { 2 & -5 } \right\rbrack &= \left\lbrack \matrix { (-1)\cdot 2 & (-1)\cdot (-5) \\0\cdot 2 & 0\cdot (-5)\\(-2)\cdot 2 & (-2)\cdot (-5) } \right\rbrack \\\[5pt] &= \left\lbrack \matrix { -2 & 5 \\0 & 0 \\-4 & 10 } \right\rbrack \end{aligned}



$$

### Index Notation of Matrix Multiplication

It's possible to express matrix multiplication using index notation.

To see how, first let $C=AB,$ where $A$ and $B$ are two matrices that are conformable for multiplication.

Then $c_{\color{red}{i}\color{blue}{j}}$ represents the entry at the intersection of the $\color{red}i$th row and $\color{blue}j$th column in $C.$

To compute $c_{\color{red}{i}\color{blue}{j}},$ we take the dot product of the $\color{red}i$th row of $\color{red}A$ and the $\color{blue}j$th column of ${\color{blue}B},$ as follows:

$$



[\begin{aligned}𝑎_{𝑖1} & 𝑎_{𝑖2} & ⋯ & 𝑎_{𝑖𝑛}\end{aligned}]



$$
