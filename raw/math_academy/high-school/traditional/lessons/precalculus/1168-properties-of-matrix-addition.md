# Properties of Matrix Addition

Source: https://www.mathacademy.com/topics/1168?courseId=43
Topic ID: 1168

## Prerequisites

- [Adding and Subtracting Matrices](./29-adding-and-subtracting-matrices.md)
- [Distributing the Negative Sign in a Linear Expression](../../../../middle-school/lessons/grade-7/137-distributing-the-negative-sign-in-a-linear-expression.md)

## Lesson

### Introduction

If we want to add (or subtract) three or more matrices, all operations should be done elementwise. For example, suppose

$$



\begin{aligned}1 \\ 1 \\ −1\end{aligned}



$$

Then we can calculate ${A}+{B}-{C}$ by performing the operations on each corresponding entry, as follows:

$$



\begin{aligned}𝐴+𝐵−𝐶 & =\begin{matrix}1 \\ 1 \\ −1\end{matrix}+\begin{matrix}−1 \\ 2 \\ 0\end{matrix}−\begin{matrix}0 \\ 5 \\ −2\end{matrix} \\ & =\begin{matrix}1+(−1)−0 \\ 1+2−5 \\ −1+0−(−2)\end{matrix} \\ & =\begin{matrix}0 \\ −2 \\ 1\end{matrix}\end{aligned}



$$

### Example: Calculating the Sum or Difference of Three or More Matrices

#### Question

Calculate $A-(B-C),$ where

$$



[\begin{aligned}−1 & 0 \\ 2 & −2\end{aligned}]



$$

#### Explanation

Performing the operations on each corresponding entry, we get:

$$



\begin{aligned}𝐴−(𝐵−𝐶) & =[\begin{matrix}−1 & 0 \\ 2 & −2\end{matrix}]−([\begin{matrix}−1 & −1 \\ 2 & 0\end{matrix}]−[\begin{matrix}0 & −5 \\ 1 & 1\end{matrix}]) \\ & =[\begin{matrix}−1 & 0 \\ 2 & −2\end{matrix}]−[\begin{matrix}−1−0 & −1−(−5) \\ 2−1 & 0−1\end{matrix}] \\ & =[\begin{matrix}−1 & 0 \\ 2 & −2\end{matrix}]−[\begin{matrix}−1 & 4 \\ 1 & −1\end{matrix}] \\ & =[\begin{matrix}−1−(−1) & 0−4 \\ 2−1 & −2−(−1)\end{matrix}] \\ & =[\begin{matrix}0 & −4 \\ 1 & −1\end{matrix}]\end{aligned}



$$

### Properties of Matrix Addition and Subtraction

Since addition and subtraction of matrices are performed elementwise, they have the same properties as addition and subtraction of real numbers.

For example, if $A,$ $B,$ and $C$ are three $m \times n$ matrices then we can add them in any order:

$$



(A+B)+C = A+(B+C) = A+B+C



$$

Moreover, we can distribute a subtraction over matrices in parentheses:

$$



A - (B + C) = A - B - C



$$

### Example: Calculating the Sum or Difference of Three or More Matrices Using Distributivity

#### Question

Find $A+C-(B+A),$ if

$$



\begin{aligned}1 & −2 \\ \sqrt{2} & 0 \\ 0 & −2\end{aligned}



$$

#### Explanation

First, we simplify the expression by distributing the subtraction over the matrices in the parentheses:

$$



\begin{aligned}𝐴+𝐶−(𝐵+𝐴) & =𝐴+𝐶−𝐵−𝐴 \\ & =𝐴+𝐶−𝐵−𝐴 \\ & =𝐶−𝐵\end{aligned}



$$

We are left with a single subtraction. So, we subtract the corresponding entries of the two matrices:

$$



\begin{aligned}𝐶−𝐵 & =\begin{matrix}3 & −1 \\ 1 & 2 \\ −6 & 1\end{matrix}−\begin{matrix}3 & −1 \\ 2 & 0 \\ −4 & 1\end{matrix} \\ & =\begin{matrix}3−3 & −1−(−1) \\ 1−2 & 2−0 \\ −6−(−4) & 1−1\end{matrix} \\ & =\begin{matrix}0 & 0 \\ −1 & 2 \\ −2 & 0\end{matrix}\end{aligned}



$$
