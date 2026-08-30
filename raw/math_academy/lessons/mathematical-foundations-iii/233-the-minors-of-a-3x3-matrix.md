# The Minors of a 3x3 Matrix

Source: https://www.mathacademy.com/topics/233?courseId=136
Topic ID: 233

## Prerequisites

- [The Determinant of a 2x2 Matrix](./152-the-determinant-of-a-2x2-matrix.md)
- [Solving Quadratic Equations with No Constant Term](../algebra-i/393-solving-quadratic-equations-with-no-constant-term.md)
- [Solving Quadratic Equations Using a Difference of Squares](../algebra-i/394-solving-quadratic-equations-using-a-difference-of-squares.md)
- [The Quadratic Formula](../algebra-i/422-the-quadratic-formula.md)
- [Index Notation for Matrices](./1167-index-notation-for-matrices.md)
- [Solving Quadratic Equations with Leading Coefficients by Factoring](../algebra-i/1422-solving-quadratic-equations-with-leading-coefficients-by-factoring.md)

## Lesson

### Introduction

The **minor** of the entry $a_{ij}$ in a matrix $A$ is the determinant of the remaining entries when the row and column containing $a_{ij}$ are removed.

For instance, suppose we want to find the minor of $a_{{\color{red}1}{\color{blue}2}} = {\boxed{-1}}$ (row ${\color{red}1}$, column ${\color{blue}2}$) in the matrix $A$ given by

$$


\begin{aligned}3 & −1 & 6 \\ 5 & 2 & 7 \\ 8 & 9 & 4\end{aligned}


$$

To find the minor, we exclude all entries in row $1$ and all entries in column $2\mathbin{:}$

$$


\begin{aligned}3 & −1 & 6 \\ 5 & 2 & 7 \\ 8 & 9 & 4\end{aligned}


$$

This leaves us with the $2\times 2$ determinant given by

$$


\begin{aligned}5 & 7 \\ 8 & 4\end{aligned}


$$

We call it $M_{{\color{red}{1}}{\color{blue}{2}}}$ to denote the fact that it was obtained by deleting row $\color{red}1$ and column $\color{blue}2$ of the matrix $A.$

Finally, we compute the above determinant:

$$


\begin{aligned}\begin{aligned}5 & 7 \\ 8 & 4\end{aligned} & =5⋅4−7⋅8 \\ & =20−56 \\ & =−36\end{aligned}


$$

### Example: Calculating a Minor in a 3x3 Matrix With Integer Entries

#### Question

Calculate the minor of the entry $b_{21}$ in the matrix

$$


\begin{aligned}10 & 1 & 5 \\ 3 & 6 & 8 \\ 4 & 7 & 2\end{aligned}


$$

#### Explanation

The minor of $b_{21} = 3$ (second row, first column) is the determinant of the remaining entries when the column and row containing $3$ are removed:

$$


\begin{aligned}∗ & 1 & 5 \\ 3 & ∗ & ∗ \\ ∗ & 7 & 2\end{aligned}


$$

So, the minor of $b_{21}=3$ is

$$


\begin{aligned}det[\begin{aligned}1 & 5 \\ 7 & 2\end{aligned}] & =\begin{aligned}1 & 5 \\ 7 & 2\end{aligned} \\ & =1⋅2−5⋅7 \\ & =2−35 \\ & =−33.\end{aligned}


$$

### Example: Calculating a Minor in a 3x3 Matrix With Variable Entries

#### Question

What is the minor of $c_{22}$ in the matrix

$$


\begin{aligned}7𝑥 & 0 & −3𝑦 \\ 1 & 𝑥+2𝑦 & 4 \\ −𝑦 & 0 & 5\end{aligned}


$$

#### Explanation

First, we remove the second row and second column:

$$


\begin{aligned}7𝑥 & ∗ & −3𝑦 \\ ∗ & 𝑥+2𝑦 & ∗ \\ −𝑦 & ∗ & 5\end{aligned}


$$

Next, we calculate the determinant:

$$


\begin{aligned}det[\begin{aligned}7𝑥 & −3𝑦 \\ −𝑦 & 5\end{aligned}] & =\begin{aligned}7𝑥 & −3𝑦 \\ −𝑦 & 5\end{aligned} \\ & =7𝑥⋅5−(−3𝑦)⋅(−𝑦) \\ & =35𝑥−3𝑦^{2}\end{aligned}


$$

### Example: Solving for an Unknown Given the Value of a Minor

#### Question

Given that the minor of $a_{23}$ is $5,$ find all the possible values of $k$ in the matrix

$$


\begin{aligned}𝑘 & 3 & −1 \\ −5 & 2 & 7 \\ −1 & 2𝑘 & −6\end{aligned}


$$

#### Explanation

First, we remove the second row and third column:

$$


\begin{aligned}𝑘 & 3 & ∗ \\ ∗ & ∗ & 7 \\ −1 & 2𝑘 & ∗\end{aligned}


$$

The minor of $a_{23}$ is

$$


\begin{aligned}det[\begin{aligned}𝑘 & 3 \\ −1 & 2𝑘\end{aligned}] & =\begin{aligned}𝑘 & 3 \\ −1 & 2𝑘\end{aligned} \\ & =𝑘⋅2𝑘−3⋅(−1) \\ & =2𝑘^{2}+3.\end{aligned}


$$

We're told that the minor of $a_{23}$ is $5,$ so we must have:

$$


\begin{aligned}2𝑘^{2}+3 & =5 \\ 2𝑘^{2} & =2 \\ 𝑘^{2} & =1 \\ 𝑘 & =±1\end{aligned}


$$

Therefore, the solutions are $k=-1$ and $k=1.$
