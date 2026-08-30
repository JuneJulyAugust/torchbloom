# Systems of Equations as Augmented Matrices

Source: https://www.mathacademy.com/topics/148?courseId=145
Topic ID: 148

## Prerequisites

- [Introduction to Matrices](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/861-introduction-to-matrices.md)
- [Introduction to Systems of Linear Equations](../../../middle-school/lessons/grade-7/2225-introduction-to-systems-of-linear-equations.md)

## Lesson

### Introduction

We can use matrices to solve systems of linear equations. To do this, we need to set up the **augmented matrix** for the system.

As an example, let's consider the system of equations below.

$$


\begin{aligned}2𝑥+5𝑦=−1 \\ −3𝑥+7𝑦=1\end{aligned}


$$

First, we find the **coefficient matrix**, which consists of the coefficients of the variables:

$$


\begin{aligned}2 & 5 \\ −3 & 7\end{aligned}


$$

Then, we create the **augmented matrix**. This is the coefficient matrix augmented with the column that represents the right-hand sides of the equations:

$$


\begin{aligned}2 & 5 & −1 \\ −3 & 7 & 1\end{aligned}


$$

In the future, we will learn how to use coefficient and augmented matrices to solve systems of equations. But for now, let's practice setting them up.

### The Order of the Variables in a Linear System

We will use mostly systems with the following variables:

- $x,y,z,$ or

- $x_1,x_2,x_3,$ or

- $a,b,c.$

These sets of variables will always have a *natural* order:

- alphabetical order in the case of $x,y,z$ or $a,b,c,$ and

- numerical order in the case of $x_1, x_2, x_3.$

### Example: Finding the Coefficient Matrix of a System of Linear Equations

#### Question

What is the coefficient matrix for the following system of linear equations?

$$


\begin{aligned}𝑥−2𝑦=1 \\ 2𝑦=−1\end{aligned}


$$

#### Explanation

First, we organize the system so that every variable has a coefficient:

$$


\begin{aligned}𝑥−2𝑦=1 \\ 0𝑥+2𝑦=−1\end{aligned}


$$

The coefficient matrix consists of the coefficients of the variables:

$$


\left\lbrack \matrix { 1 & -2 \ 0 & 2 } \right\rbrack


$$

### Example: Finding the Augmented Matrix of a System of Linear Equations

#### Question

What is the augmented matrix for the following system of linear equations?

$$


\begin{aligned}𝑦+𝑥−5−3𝑧=0 \\ 𝑧=𝑦+7𝑥 \\ 𝑦+3−2𝑧=1−2𝑥\end{aligned}


$$

#### Explanation

First, we organize the system so that the variables are ordered $x,y,z$ on the left-hand side, the constants are on the right-hand side, and every variable has a coefficient:

$$


\begin{aligned}𝑥+𝑦−3𝑧=5 \\ −7𝑥−𝑦+𝑧=0 \\ 2𝑥+𝑦−2𝑧=−2\end{aligned}


$$

The coefficient matrix consists of the coefficients of the variables:

$$


\left\lbrack \matrix { 1 & 1 & -3 \ -7 & -1 & 1 \ 2 & 1 & -2 } \right\rbrack


$$

The augmented matrix is the coefficient matrix augmented with the column that represents the right-hand sides of the equations:

$$


\begin{aligned}1 & 1 & −3 & 5 \\ −7 & −1 & 1 & 0 \\ 2 & 1 & −2 & −2\end{aligned}


$$

### Example: Finding the System of Equations Associated With an Augmented Matrix

#### Question

What would be the system of equations for the following augmented matrix?

$$


\begin{aligned}5 & −4 & −12 \\ 3 & 1 & 1\end{aligned}


$$

#### Explanation

The augmented matrix consists of two parts: the coefficient matrix and the column of constants.

The coefficient matrix represents the coefficients in the linear system, while the column of constants represents the constants on the right-hand sides of the equations.

Using the variables $x$ and $y,$ then, the corresponding system of equations is

$$


\begin{aligned}5𝑥−4𝑦=−12 \\ 3𝑥+𝑦=1.\end{aligned}


$$

### Example: Finding the Augmented Matrix of a Linear System With Variables Other Than x, y, z

#### Question

What is the augmented matrix for the following system of linear equations?

$$


\begin{aligned}\frac{𝑐}{2}=𝑎 \\ 5+3𝑏−𝑎=4𝑐 \\ 𝑑=1\end{aligned}


$$

#### Explanation

First, we organize the system so that the variables are ordered $a,b,c,d$ on the left-hand side, the constants are on the right-hand side, and every variable has a coefficient:

$$


\begin{aligned}−𝑎+0𝑏+\frac{1}{2}𝑐+0𝑑=0 \\ −𝑎+3𝑏−4𝑐+0𝑑=−5 \\ 0𝑎+0𝑏+0𝑐+𝑑=1\end{aligned}


$$

The coefficient matrix consists of the coefficients of the variables:

$$


\begin{aligned}−1 & 0 & \frac{1}{2} & 0 \\ −1 & 3 & −4 & 0 \\ 0 & 0 & 0 & 1\end{aligned}


$$

The augmented matrix is the coefficient matrix augmented with the column that represents the right-hand sides of the equations:

$$


\begin{aligned}−1 & 0 & \frac{1}{2} & 0 & 0 \\ −1 & 3 & −4 & 0 & −5 \\ 0 & 0 & 0 & 1 & 1\end{aligned}


$$
