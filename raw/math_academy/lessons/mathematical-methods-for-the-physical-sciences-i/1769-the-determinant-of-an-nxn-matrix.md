# The Determinant of an NxN Matrix

Source: https://www.mathacademy.com/topics/1769?courseId=154
Topic ID: 1769

## Prerequisites

- [The Determinant of a 3x3 Matrix](../integrated-math-iii-honors/153-the-determinant-of-a-3x3-matrix.md)

## Lesson

### Introduction

The minor of the entry $a_{ij}$ in a $n\times n$ matrix is the determinant that we get when the rows and columns containing $a_{ij}$ are removed.

For example, suppose that we wish to find the minor of $a_{32}$ in the following matrix:

$$


\begin{aligned}2 & 3 & 2 & 3 \\ 4 & 2 & 5 & 12 \\ 1 & −2 & 0 & −5 \\ −5 & 1 & 3 & 0\end{aligned}


$$

To get the minor of $a_{\color{red}{3}\color{blue}{2}}$, we remove the $\color{red}3$rd row and $\color{blue}2$nd column:

$$


\begin{aligned}2 & ∗ & 2 & 3 \\ 4 & ∗ & 5 & 12 \\ ∗ & −2 & ∗ & ∗ \\ −5 & ∗ & 3 & 0\end{aligned}


$$

So, the minor of $a_{32}$, denoted $M_{32}$, is

$$


\begin{aligned}2 & 2 & 3 \\ 4 & 5 & 12 \\ −5 & 3 & 0\end{aligned}


$$

We can now calculate the value of $M_{32}$ by evaluating the determinant using previously discussed methods.

### Example: Calculating a Minor in a NxN Matrix

#### Question

What is the minor of $a_{13}$ in $\begin{aligned}0 & 0 & 2 & 3 \\ 5 & 1 & 2 & 0 \\ 1 & 6 & 0 & −1 \\ −6 & 3 & 1 & 0\end{aligned}$

#### Explanation

To get the minor of $a_{13}$, we remove the $1$st row and $3$rd column:

$$


\begin{aligned}∗ & ∗ & 2 & ∗ \\ 5 & 1 & ∗ & 0 \\ 1 & 6 & ∗ & −1 \\ −6 & 3 & ∗ & 0\end{aligned}


$$

So, the minor is

$$


\begin{aligned}5 & 1 & 0 \\ 1 & 6 & −1 \\ −6 & 3 & 0\end{aligned}


$$

### Calculating a Cofactor of a NxN Matrix

In general, for any $n\times n$ matrix $A,$ the **cofactor** $C_{ij}$ of the entry $\color{red}a_{ij}$ is

$$


{\color{blue}C_{ij}}=(-1)^{i+j}{\color{blue}M_{ij}}.


$$

Cofactors are a useful tool in helping us to compute determinants of larger matrices. Before we learn how, let's get some practice at computing cofactors.

### Example: Calculating a Cofactor in a NxN Matrix

#### Question

Find the cofactor of $d_{23}$ in $\begin{aligned}0 & 2 & 3 & −6 \\ 7 & −3 & −2 & −1 \\ 6 & 0 & 8 & 9 \\ 5 & 4 & 0 & 0\end{aligned}$

#### Explanation

First, to get the minor of $d_{23}$, we remove the $2$nd row and $3$rd column:

$$


\begin{aligned}0 & 2 & ∗ & −6 \\ ∗ & ∗ & −2 & ∗ \\ 6 & 0 & ∗ & 9 \\ 5 & 4 & ∗ & 0\end{aligned}


$$

So, the minor is

$$


\begin{aligned}0 & 2 & −6 \\ 6 & 0 & 9 \\ 5 & 4 & 0\end{aligned}


$$

Now, the cofactor of $d_{23}$ is

$$


\begin{aligned}𝐶_{23} & =(−1)^{2+3}𝑀_{23} \\ & =−𝑀_{23} \\ & =−\begin{aligned}0 & 2 & −6 \\ 6 & 0 & 9 \\ 5 & 4 & 0\end{aligned}.\end{aligned}


$$

### Calculating Determinants Using Cofactors

One way to find the determinant of a $3\!\times\! 3$ matrix $A$ is to take the alternating sum of the entries of the top row of the matrix, multiplied by their respective minors, as follows:

$$


\det(A) = {\color{red}a_{11}}{\color{blue}M_{11}} - {\color{red}a_{12}}{\color{blue}M_{12}} + {\color{red}a_{13}}{\color{blue}M_{13}}


$$

Remember that we had to change the sign of the second product. When we multiply a minor of an entry by the respective sign in the formula like this, we get the cofactor of the entry. The cofactors in the above formula were ${\color{blue}M_{11}},$ $-{\color{blue}M_{12}},$ and ${\color{blue}M_{13}}.$

Using this idea, we can write the formula for the determinant of a $3\!\times\! 3$ matrix $A$ in terms of cofactors, as follows:

$$


\det(A) = {\color{red}a_{11}}{\color{blue}C_{11}} + {\color{red}a_{12}}{\color{blue}C_{12}} + {\color{red}a_{13}}{\color{blue}C_{13}}


$$

This is called the **cofactor expansion** of the determinant across the first row.

In fact, we can use a similar method of multiplying the entries of the top row of the matrix by their respective cofactors to find the determinant for any $n\!\times\! n$ matrix $A$ when $n \ge 3$. The formula is

$$


\begin{aligned}det(𝐴) & =\underset{\underset{𝑗=1}{∑}}{\overset{}{𝑛}}𝑎_{1𝑗}𝐶_{1𝑗} \\ & =𝑎_{11}𝐶_{11}+𝑎_{12}𝐶_{12}+⋯+𝑎_{1𝑛}𝐶_{1𝑛}.\end{aligned}


$$

Let's see how to use this formula in the next example.

### Example: Calculating the Determinant of a NxN Matrix Using Cofactor Expansion

#### Question

Calculate the determinant of the matrix $\begin{aligned}0 & 0 & 2 & 0 \\ 5 & 1 & 2 & 0 \\ 1 & 6 & 0 & −1 \\ −6 & 3 & 1 & 0\end{aligned}$

#### Explanation

We use the cofactor expansion along the first row:

$$


\begin{aligned}det(𝐴) & =𝑎_{11}𝐶_{11}+𝑎_{12}𝐶_{12}+𝑎_{13}𝐶_{13}+𝑎_{14}𝐶_{14} \\ & =0⋅𝐶_{11}+0⋅𝐶_{12}+2⋅𝐶_{13}+0⋅𝐶_{14} \\ & =2𝐶_{13} \\ & =2⋅\begin{aligned}∗ & ∗ & 2 & ∗ \\ 5 & 1 & ∗ & 0 \\ 1 & 6 & ∗ & −1 \\ −6 & 3 & ∗ & 0\end{aligned} \\ & =2(−1)^{1+3}\begin{aligned}5 & 1 & 0 \\ 1 & 6 & −1 \\ −6 & 3 & 0\end{aligned} \\ & =2(5\begin{aligned}6 & −1 \\ 3 & 0\end{aligned}−1\begin{aligned}1 & −1 \\ −6 & 0\end{aligned}+0\begin{aligned}1 & 6 \\ −6 & 3\end{aligned}) \\ & =2(5(6⋅0+1⋅3)−(1⋅0−(−1)⋅(−6))+0(1⋅3−6⋅(−6))) \\ & =2(15+6+0) \\ & =2⋅21 \\ & =42\end{aligned}


$$
