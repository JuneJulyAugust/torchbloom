# Cramer’s Rule for 3x3 Systems

Source: https://www.mathacademy.com/topics/1776?courseId=55
Topic ID: 1776

## Prerequisites

- [The Determinant of a 3x3 Matrix](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/153-the-determinant-of-a-3x3-matrix.md)
- [Cramer's Rule for 2x2 Systems of Linear Equations](./1775-cramer-s-rule-for-2x2-systems-of-linear-equations.md)

## Lesson

### Introduction

Cramer's rule applies to square systems of linear equations with any number of variables. In this lesson, we will practice applying Cramer's rule to solve $3 \times 3$ systems of equations.

Suppose we have a square system of linear equations

$$


\begin{aligned}𝑎_{11}𝑥+𝑎_{12}𝑦+𝑎_{13}𝑧=𝑏_{1} \\ 𝑎_{21}𝑥+𝑎_{22}𝑦+𝑎_{23}𝑧=𝑏_{2} \\ 𝑎_{31}𝑥+𝑎_{32}𝑦+𝑎_{33}𝑧=𝑏_{3},\end{aligned}


$$

where $\begin{aligned}𝑎_{11} & 𝑎_{12} & 𝑎_{13} \\ 𝑎_{21} & 𝑎_{22} & 𝑎_{23} \\ 𝑎_{31} & 𝑎_{32} & 𝑎_{33}\end{aligned}$. Then Cramer's rule states that

$$


\left< x,y,z \right> = \left\langle \dfrac{D_x}{D}, \dfrac{D_y}{D}, \dfrac{D_z}{D} \right\rangle


$$

is the unique solution of the system, where

$$


\begin{aligned}𝑏_{1} & 𝑎_{12} & 𝑎_{13} \\ 𝑏_{2} & 𝑎_{22} & 𝑎_{23} \\ 𝑏_{3} & 𝑎_{32} & 𝑎_{33}\end{aligned}


$$

### A Demonstration of Cramer's Rule on a 3x3 Linear System

To demonstrate using Cramer's rule on a $3 \times 3$ system, consider the following system of equations:

$$


\begin{aligned}4𝑥+2𝑦+𝑧=9 \\ 2𝑦+3𝑧=7 \\ −8𝑥+𝑦+6𝑧=0\end{aligned}


$$

First, let's rewrite the system to reveal the coefficients:

$$


\begin{aligned}4𝑥+2𝑦+1𝑧=9 \\ 0𝑥+2𝑦+3𝑧=7 \\ −8𝑥+1𝑦+6𝑧=0\end{aligned}


$$

We start finding the determinant of the coefficients matrix:

$$


\begin{aligned}𝐷=\begin{aligned}4 & 2 & 1 \\ 0 & 2 & 3 \\ −8 & 1 & 6\end{aligned} & =4⋅\begin{aligned}2 & 3 \\ 1 & 6\end{aligned}−2⋅\begin{aligned}0 & 3 \\ −8 & 6\end{aligned}+1⋅\begin{aligned}0 & 2 \\ −8 & 1\end{aligned} \\ & =4(12−3)−2(0+24)+(0+16) \\ & =36−48+16 \\ & =4\end{aligned}


$$

Now, let's find $D_x,$ $D_y,$ and $D_z.$

- To find $D_x,$ we take the coefficients matrix, replace the *first* column by the right-hand side of the system, and calculate the determinant:

- To find $D_y,$ we take the coefficients matrix, replace the *second* column by the right-hand side of the system, and calculate the determinant:

- To find $D_z,$ we take the coefficients matrix, replace the *third* column by the right-hand side of the system, and calculate the determinant:

Finally, the solution to the system is given by

$$


\begin{aligned}⟨𝑥,𝑦,𝑧⟩ & =⟨\frac{𝐷_{𝑥}}{𝐷},\frac{𝐷_{𝑦}}{𝐷},\frac{𝐷_{𝑧}}{𝐷}⟩ \\ & =⟨\frac{4}{4},\frac{8}{4},\frac{4}{4}⟩ \\ & =⟨1,2,1⟩.\end{aligned}


$$

### Example: Identifying Parts of Cramer's Rule

#### Question

Consider the system of equations

$$


\begin{aligned}9𝑥+3𝑦−6𝑧=8 \\ −6𝑥+4𝑦+2𝑧=3 \\ 5𝑥−5𝑦−15𝑧=10.\end{aligned}


$$

According to Cramer's rule, $x=\dfrac{D_x}{D}$, where $D$ is the determinant of the coefficient matrix and $D_x=$

#### Explanation

We are given the system

$$


\begin{aligned}9𝑥+3𝑦+(−6)𝑧=8 \\ (−6)𝑥+4𝑦+2𝑧=3 \\ 5𝑥+(−5)𝑦+(−15)𝑧=10.\end{aligned}


$$

The determinant of the coefficient matrix is

$$


\begin{aligned}9 & 3 & −6 \\ −6 & 4 & 2 \\ 5 & −5 & −15\end{aligned}


$$

Now, to construct $D_x$, we replace the first column of the coefficient matrix by the right-hand side column of the given system:

$$


\begin{aligned}8 & 3 & −6 \\ 3 & 4 & 2 \\ 10 & −5 & −15\end{aligned}


$$

### Example: Solving for an Unknown in a 3x3 Linear System Using Cramer's Rule

#### Question

Let $\langle x,y,z \rangle$ be the solution of the system of equations below. Find $z.$

$$


\begin{aligned}𝑥−𝑦+3𝑧=−1 \\ 4𝑥−2𝑧=1 \\ 3𝑥+𝑦−𝑧=−2\end{aligned}


$$

#### Explanation

First, let's rewrite the system to reveal the coefficients:

$$


\begin{aligned}1𝑥−1𝑦+3𝑧=−1 \\ 4𝑥+0𝑦−2𝑧=1 \\ 3𝑥+1𝑦−1𝑧=−2\end{aligned}


$$

We start by finding the determinant of the coefficients matrix:

$$


\begin{aligned}𝐷=\begin{aligned}1 & −1 & 3 \\ 4 & 0 & −2 \\ 3 & 1 & −1\end{aligned} & =1⋅\begin{aligned}0 & −2 \\ 1 & −1\end{aligned}−(−1)⋅\begin{aligned}4 & −2 \\ 3 & −1\end{aligned}+3⋅\begin{aligned}4 & 0 \\ 3 & 1\end{aligned} \\ & =(0−(−2))+(−4+6)+3(4−0) \\ & =2+2+12 \\ & =16\end{aligned}


$$

Now, to find $D_z,$ we take the coefficients matrix, replace the ** column by the right-hand side of the system, and calculate the determinant:

$$


\begin{aligned}𝐷_{𝑧}=\begin{aligned}1 & −1 & −1 \\ 4 & 0 & 1 \\ 3 & 1 & −2\end{aligned} & =1⋅\begin{aligned}0 & 1 \\ 1 & −2\end{aligned}−(−1)⋅\begin{aligned}4 & 1 \\ 3 & −2\end{aligned}+(−1)⋅\begin{aligned}4 & 0 \\ 3 & 1\end{aligned} \\ & =(0−1)+(−8−3)−(4−0) \\ & =−1−11−4 \\ & =−16\end{aligned}


$$

Finally, applying Cramer's rule, we get

$$


\begin{aligned}𝑧 & =\frac{𝐷_{𝑧}}{𝐷}=\frac{−16}{16}=−1.\end{aligned}


$$

### Example: Solving for a Coefficient in a 3x3 Linear System Using Cramer's Rule

#### Question

Let $\langle x,y,z \rangle$ be the solution of the system of equations below. Given that $x = 2,$ find the value of $k.$

$$


\begin{aligned}𝑥+2𝑦−𝑧=−1 \\ 𝑘𝑥+3𝑦−2𝑧=1 \\ 3𝑥−𝑦+2𝑧=3\end{aligned}


$$

#### Explanation

First, let's find the determinant of the coefficients matrix:

$$


\begin{aligned}𝐷=\begin{aligned}1 & 2 & −1 \\ 𝑘 & 3 & −2 \\ 3 & −1 & 2\end{aligned} & =1⋅\begin{aligned}3 & −2 \\ −1 & 2\end{aligned}−2⋅\begin{aligned}𝑘 & −2 \\ 3 & 2\end{aligned}+(−1)⋅\begin{aligned}𝑘 & 3 \\ 3 & −1\end{aligned} \\ & =(6−2)−2(2𝑘+6)−(−𝑘−9) \\ & =4−4𝑘−12+𝑘+9 \\ & =1−3𝑘\end{aligned}


$$

According to Cramer's rule, the value of $x$ is given by $x = \dfrac{D_x}{D},$ where

$$


\begin{aligned}𝐷_{𝑥}=\begin{aligned}−1 & 2 & −1 \\ 1 & 3 & −2 \\ 3 & −1 & 2\end{aligned} & =(−1)⋅\begin{aligned}3 & −2 \\ −1 & 2\end{aligned}−2⋅\begin{aligned}1 & −2 \\ 3 & 2\end{aligned}+(−1)⋅\begin{aligned}1 & 3 \\ 3 & −1\end{aligned} \\ & =−(6−2)−2(2+6)−(−1−9) \\ & =−4−16+10 \\ & =−10.\end{aligned}


$$

Therefore, we have

$$


x = \dfrac{D_x}{D} = \dfrac{-10}{1-3k}.


$$

From the problem statement, we know that $x=2.$ So, we can solve for $k$ as follows:

$$


\begin{aligned}\frac{−10}{1−3𝑘} & =2 \\ −10 & =2−6𝑘 \\ 6𝑘 & =12 \\ 𝑘 & =2\end{aligned}


$$
