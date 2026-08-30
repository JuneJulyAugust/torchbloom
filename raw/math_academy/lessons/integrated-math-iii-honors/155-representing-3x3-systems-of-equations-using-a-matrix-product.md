# Representing 3x3 Systems of Equations Using a Matrix Product

Source: https://www.mathacademy.com/topics/155?courseId=101
Topic ID: 155

## Prerequisites

- [Representing 2x2 Systems of Equations Using a Matrix Product](./1729-representing-2x2-systems-of-equations-using-a-matrix-product.md)

## Lesson

### Introduction

Remember that we can represent a system of two linear equations in two variables using matrices. We can do the same thing for a system of three linear equations in three variables, such as the following:

$$


\begin{aligned}3𝑥+2𝑦 − 2𝑧=7 \\ 2𝑥 − 1𝑦 − 4𝑧=2 \\ 2𝑥+1𝑦 − 3𝑧=3\end{aligned}


$$

For a $3 \times 3$ system like the one above, we put the coefficients of the system into a $3 \times 3$ coefficient matrix:

$$


\begin{aligned}3 & 2 & −2 \\ 2 & −1 & −4 \\ 2 & 1 & −3\end{aligned}


$$

Each row has the coefficients of one of the equations in the system, and each column consists of the coefficients of one particular variable. We also have the $3 \times 1$ column vectors

$$


\begin{aligned}7 \\ 2 \\ 3\end{aligned}


$$

where $\mathbf{b}$ consists of each constant on the right side of the system and $\mathbf{x}$ contains the variables. With these matrices, we can write our system as $A\mathbf{x} = \mathbf{b},$ or

$$


\begin{aligned}3 & 2 & −2 \\ 2 & −1 & −4 \\ 2 & 1 & −3\end{aligned}


$$

We can write any system of three equations with three variables in this form. Just to check that the above equation is true, let's multiply out the left-hand side to see if it equals the right-hand side:

$$


\begin{aligned}𝐴𝐱 & =\begin{aligned}3 & 2 & −2 \\ 2 & −1 & −4 \\ 2 & 1 & −3\end{aligned}\begin{aligned}𝑥 \\ 𝑦 \\ 𝑧\end{aligned} \\ & =\begin{aligned}3𝑥+2𝑦 − 2𝑧 \\ 2𝑥 − 1𝑦 − 4𝑧 \\ 2𝑥+1𝑦 − 3𝑧\end{aligned} \\ & =\begin{aligned}7 \\ 2 \\ 3\end{aligned} \\ & =𝐛\,✓\end{aligned}


$$

### Example: Identifying Entries of a Matrix Product Representing a 3x3 System of Equations

#### Question

The system of equations

$$


\begin{aligned}\begin{aligned}6𝑥+4𝑦=1 \\ 𝑥−8𝑦−𝑧=−2 \\ 3𝑥+2𝑦−2𝑧=1\end{aligned}\end{aligned}


$$

can be represented using matrix notation as

$$


\begin{aligned}𝑎 & 4 & 0 \\ 1 & −8 & −1 \\ 3 & 𝑏 & −2\end{aligned}


$$

What are the values of $a,$ $b$ and $c?$

#### Explanation

First, let's write the system so that $x$, $y$, and $z$ appear in each equation:

$$


\begin{aligned}6𝑥+4𝑦+0𝑧=1 \\ 𝑥−8𝑦−𝑧=−2 \\ 3𝑥+2𝑦−2𝑧=1\end{aligned}


$$

Now, we can write the system in the form $A\mathbf{x} = \mathbf{b},$ where

$$


\begin{aligned}6 & 4 & 0 \\ 1 & −8 & −1 \\ 3 & 2 & −2\end{aligned}


$$

is the coefficient matrix,

$$


\begin{aligned}1 \\ −2 \\ 1\end{aligned}


$$

is the column vector of constants, and

$$


\begin{aligned}𝑥 \\ 𝑦 \\ 𝑧\end{aligned}


$$

is the column vector of variables.

So, the equation $A\mathbf{x} = \mathbf{b}$ becomes

$$


\begin{aligned}6 & 4 & 0 \\ 1 & −8 & −1 \\ 3 & 2 & −2\end{aligned}


$$

Therefore, $a=6,$ $b=2,$ and $c=-2.$

### Example: Identifying Entries of a Matrix Product Representing a 3x3 System of Equations by Reorganizing

#### Question

The system of equations

$$


\begin{aligned}\begin{aligned}2𝑥−𝑦+𝑧=4 \\ 𝑧−𝑥+2=−1 \\ 2𝑦−2𝑥−4𝑧=−4\end{aligned}\end{aligned}


$$

can be represented using matrix notation as

$$


\begin{aligned}2 & −1 & 1 \\ −1 & 𝑎 & 1 \\ 𝑏 & 2 & −4\end{aligned}


$$

What are the values of $a,$ $b$ and $c?$

#### Explanation

First, let's write the system so that $x$, $y$, and $z$ appear in each equation in the correct order and all constants are on the right-hand side of the system:

$$


\begin{aligned}2𝑥−𝑦+𝑧=4 \\ −𝑥+0𝑦+𝑧=−3 \\ −2𝑥+2𝑦−4𝑧=−4\end{aligned}


$$

Now, we can write the system in the form $A\mathbf{x} = \mathbf{b},$ where

$$


\begin{aligned}2 & −1 & 1 \\ −1 & 0 & 1 \\ −2 & 2 & −4\end{aligned}


$$

is the coefficient matrix,

$$


\begin{aligned}4 \\ −3 \\ −4\end{aligned}


$$

is the column vector of constants, and

$$


\begin{aligned}𝑥 \\ 𝑦 \\ 𝑧\end{aligned}


$$

is the column vector of variables.

So, the equation $A\mathbf{x} = \mathbf{b}$ becomes

$$


\begin{aligned}2 & −1 & 1 \\ −1 & 0 & 1 \\ −2 & 2 & −4\end{aligned}


$$

Therefore $a=0,$ $b=-2,$ $c=-3.$
