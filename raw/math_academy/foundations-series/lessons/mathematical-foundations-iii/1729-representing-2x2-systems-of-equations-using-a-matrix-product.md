# Representing 2x2 Systems of Equations Using a Matrix Product

Source: https://www.mathacademy.com/topics/1729?courseId=136
Topic ID: 1729

## Prerequisites

- [Multiplying a Matrix by a Column Vector](./1195-multiplying-a-matrix-by-a-column-vector.md)

## Lesson

### Introduction

Matrices can be used to represent systems of equations, such as the following:

$$


\begin{aligned}2𝑥+3𝑦=5 \\ 4𝑥 − 5𝑦=−1\end{aligned}


$$

For a $2\times 2$ system like the one above, we put the coefficients of the system into a $2\times 2$ matrix, called the **coefficient matrix**:

$$


[\begin{aligned}2 & 3 \\ 4 & −5\end{aligned}]


$$

Each row has the coefficients of one of the equations in the system, and each column consists of the coefficients of one particular variable. We also have the $2\times 1$ column vectors

$$


[\begin{aligned}5 \\ −1\end{aligned}]


$$

where $\mathbf{b}$ consists of each constant on the right side of the system and $\mathbf{x}$ contains the variables. With these matrices, we can write our system as $A\mathbf{x} = \mathbf{b},$ or

$$


[\begin{aligned}2 & 3 \\ 4 & −5\end{aligned}]


$$

We can write any system of two equations with two variables in this form. Just to check that the above equation is true, let's multiply out the left-hand side to see if it equals the right-hand side:

$$


\begin{aligned}𝐴𝐱 & =[\begin{matrix}2 & 3 \\ 4 & −5\end{matrix}][\begin{matrix}𝑥 \\ 𝑦\end{matrix}] \\ & =[\begin{matrix}2𝑥+3𝑦 \\ 4𝑥 − 5𝑦\end{matrix}] \\ & =[\begin{matrix}5 \\ −1\end{matrix}] \\ & =𝐛\,✓\end{aligned}


$$

### Example: Representing a 2x2 System of Equations Using a Matrix Product

#### Question

Represent the following system of equations using matrices:

$$


\begin{aligned}2𝑥=5 \\ −5𝑥+6𝑦=−8\end{aligned}


$$

#### Explanation

First, let's write the system so that both $x$ and $y$ appear in each equation. The variable $y$ does not appear in the first equation, but this just means its coefficient is $0.$ So, we get

$$


\begin{aligned}2𝑥+0𝑦=5 \\ −5𝑥+6𝑦=−8\end{aligned}


$$

Now, we can write the system in the form $A\mathbf{x} = \mathbf{b},$ where

$$


[\begin{aligned}2 & 0 \\ −5 & 6\end{aligned}]


$$

is the coefficient matrix,

$$


[\begin{aligned}5 \\ −8\end{aligned}]


$$

is the column vector of constants, and

$$


[\begin{aligned}𝑥 \\ 𝑦\end{aligned}]


$$

is the column vector of variables.

So, the equation $A\mathbf{x} = \mathbf{b}$ becomes

$$


[\begin{aligned}2 & 0 \\ −5 & 6\end{aligned}]


$$

### Example: Representing a 2x2 System of Equations Using a Matrix Product by Reorganizing

#### Question

Represent the following system of equations using matrices:

$$


\begin{aligned}\begin{matrix}−5𝑦=−3𝑥 \\ 6+𝑥=−2+𝑦\end{matrix}\end{aligned}


$$

#### Explanation

First, we organize the system so that it’s in the correct order:

$$


\begin{aligned}\begin{matrix}3𝑥−5𝑦=0 \\ 𝑥−𝑦=−8.\end{matrix}\end{aligned}


$$

Now, we can write the system in the form $A\mathbf{x} = \mathbf{b},$ where

$$


[\begin{aligned}3 & −5 \\ 1 & −1\end{aligned}]


$$

is the coefficient matrix,

$$


[\begin{aligned}0 \\ −8\end{aligned}]


$$

is the column vector of constants, and

$$


[\begin{aligned}𝑥 \\ 𝑦\end{aligned}]


$$

is the column vector of variables.

So, the equation $A\mathbf{x} = \mathbf{b}$ becomes

$$


[\begin{aligned}3 & −5 \\ 1 & −1\end{aligned}]


$$

### Example: Expressing a Matrix Product as a 2x2 System of Equations

#### Question

What is the system of equations represented by

$$


[\begin{aligned}10 & −15 \\ 1 & 0\end{aligned}]


$$

#### Explanation

The $2\times 2$ matrix represents the coefficients of $x$ and $y,$ while the $2\times 1$ column vector on the right-hand side represents the constants of the equations. So, we get the following system of equations:

$$


\begin{aligned}\begin{matrix}10𝑥−15𝑦=5 \\ 1𝑥+0𝑦=−2\end{matrix}\end{aligned}


$$

Simplifying both equations in the system, we get

$$


\begin{aligned}\begin{matrix}2𝑥−3𝑦=1 \\ 𝑥=−2.\end{matrix}\end{aligned}


$$
