# Cramer's Rule for 2x2 Systems of Linear Equations

Source: https://www.mathacademy.com/topics/1775?courseId=154
Topic ID: 1775

## Prerequisites

- [The Determinant of a 2x2 Matrix](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/152-the-determinant-of-a-2x2-matrix.md)
- [Two-Dimensional Vectors Expressed in Component Form](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/1165-two-dimensional-vectors-expressed-in-component-form.md)

## Lesson

### Introduction

**Cramer's Rule** is a method for solving a linear system of equations using determinants.

Suppose we have a square system of linear equations

$$


\begin{aligned}𝑎_{11}𝑥+𝑎_{12}𝑦=𝑏_{1} \\ 𝑎_{21}𝑥+𝑎_{22}𝑦=𝑏_{2},\end{aligned}


$$

where $\begin{aligned}𝑎_{11} & 𝑎_{12} \\ 𝑎_{21} & 𝑎_{22}\end{aligned}$ Then Cramer's rule states that

$$


x = \dfrac{D_x}{D}, \qquad y = \dfrac{D_y}{D}


$$

is the unique solution of the system, where

$$


\begin{aligned}𝑏_{1} & 𝑎_{12} \\ 𝑏_{2} & 𝑎_{22}\end{aligned}


$$

For example, let's use Cramer's rule to solve the following system of equations:

$$


\begin{aligned}3𝑥−2𝑦=−1 \\ −1𝑥+2𝑦=3\end{aligned}


$$

We start by finding the **determinant of the coefficient matrix**:

$$


\begin{aligned}𝐷 & =\begin{aligned}3 & −2 \\ −1 & 2\end{aligned} \\ & =3⋅2−(−1)⋅(−2) \\ & =4\end{aligned}


$$

Now, we compute $D_x$ and $D_y\mathbin{:}$

$$


\begin{aligned}𝐷_{𝑥} & =\begin{aligned}−1 & −2 \\ 3 & 2\end{aligned} \\ & =(−1)⋅2−3⋅(−2) \\ & =4 \\ 𝐷_{𝑦} & =\begin{aligned}3 & −1 \\ −1 & 3\end{aligned} \\ & =3⋅3−(−1)⋅(−1) \\ & =8\end{aligned}


$$

Finally, the solution to the system is given by

$$


\begin{aligned}𝑥 & =\frac{𝐷_{𝑥}}{𝐷}=\frac{4}{4}=1, \\ 𝑦 & =\frac{𝐷_{𝑦}}{𝐷}=\frac{8}{4}=2.\end{aligned}


$$

It is common to write the solutions to a linear system as a vector. So, in this case, we have

$$


\left< x,y \right> = \left< 1,2 \right>.


$$

### Example: Identifying the Parts of Cramer's Rule Formula

#### Question

Consider the system of linear equations

$$


\begin{aligned}𝑥−𝑦=2 \\ 2𝑥+𝑦=1.\end{aligned}


$$

According to Cramer's rule, the unknown $x$ can be written as $\begin{aligned}1 & −1 \\ 2 & 1\end{aligned}$ Express $D_x$ in terms of a $2 \times 2$ determinant.

#### Explanation

We are given the system

$$


\begin{aligned}𝑥−𝑦=2 \\ 2𝑥+𝑦=1.\end{aligned}


$$

The determinant of the coefficient matrix is

$$


\begin{aligned}𝐷 & =\begin{aligned}1 & −1 \\ 2 & 1\end{aligned}.\end{aligned}


$$

Now, to construct $D_x$, we replace the first column of the coefficient matrix by the right-hand side column of the given system:

$$


\begin{aligned}𝐷_{𝑥} & =\begin{aligned}2 & −1 \\ 1 & 1\end{aligned}\end{aligned}


$$

### Example: Expressing an Unknown in Terms of 2x2 Determinants

#### Question

Consider the system of equations

$$


\begin{aligned}5𝑥+2𝑦=−1 \\ −3𝑥+3𝑦=9.\end{aligned}


$$

Express $y$ in terms of $2 \times 2$ determinants.

#### Explanation

We are given the system

$$


\begin{aligned}5𝑥+2𝑦=−1 \\ −3𝑥+3𝑦=9.\end{aligned}


$$

The determinant of the coefficient matrix is

$$


\begin{aligned}𝐷 & =\begin{aligned}5 & 2 \\ −3 & 3\end{aligned}.\end{aligned}


$$

Now, to construct $D_y$, we replace the second column of the coefficient matrix by the right-hand side column of the given system:

$$


\begin{aligned}𝐷_{𝑦} & =\begin{aligned}5 & −1 \\ −3 & 9\end{aligned}\end{aligned}


$$

Finally, according to Cramer's rule, we have

$$


\begin{aligned}𝑦 & =\frac{𝐷_{𝑦}}{𝐷}=\frac\begin{aligned}5 & −1 \\ −3 & 9\end{aligned}}\begin{aligned}5 & 2 \\ −3 & 3\end{aligned}}.\end{aligned}


$$

### Example: Solving for a Coefficient in a 2x2 Linear System Using Cramer's Rule

#### Question

Let $\langle x,3 \rangle$ be the solution of the system of equations below.

$$


\begin{aligned}5𝑥−2𝑦=4 \\ 𝑥+𝑘𝑦=8\end{aligned}


$$

Which of the following equations could be solved to find the value of $k?$

1. $\begin{aligned}5 & −2 \\ 1 & 𝑘\end{aligned}$

2. $\begin{aligned}5 & −2 \\ 1 & 𝑘\end{aligned}$

3. $\begin{aligned}5 & −2 \\ 1 & 𝑘\end{aligned}$

#### Explanation

The determinant of the coefficient matrix is

$$


\begin{aligned}𝐷 & =\begin{aligned}5 & −2 \\ 1 & 𝑘\end{aligned}.\end{aligned}


$$

According to Cramer's rule, the value of $y$ is given by $y=\dfrac{D_y}{D},$ where

$$


\begin{aligned}𝐷_{𝑦} & =\begin{aligned}5 & 4 \\ 1 & 8\end{aligned} \\ & =5⋅8−4⋅1 \\ & =36.\end{aligned}


$$

Therefore:

$$


\begin{aligned}𝑦 & =\frac{𝐷_{𝑦}}{𝐷} \\ 3 & =\frac{36}\begin{aligned}5 & −2 \\ 1 & 𝑘\end{aligned}} \\ \begin{aligned}5 & −2 \\ 1 & 𝑘\end{aligned} & =12\end{aligned}


$$

So, the correct answer is "II only".
