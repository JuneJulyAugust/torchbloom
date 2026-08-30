# Solving 2x2 Systems of Equations Using Inverse Matrices

Source: https://www.mathacademy.com/topics/934?courseId=136
Topic ID: 934

## Prerequisites

- [Inverses of 2x2 Matrices](./864-inverses-of-2x2-matrices.md)
- [Representing 2x2 Systems of Equations Using a Matrix Product](./1729-representing-2x2-systems-of-equations-using-a-matrix-product.md)
- [Consistency and Dependency in Linear Systems](../algebra-i/4638-consistency-and-dependency-in-linear-systems.md)

## Lesson

### Introduction

If the $2\times 2$ matrix $A$ is invertible, then we can find a solution to the system

$$


A\mathbf{x} = \mathbf{b}


$$

by "pre-multiplying" both sides of the equation by $A^{-1}\mathbin{:}$

$$


\begin{aligned}𝐴𝐱 & =𝐛 \\ 𝐴^{−1}𝐴𝐱 & =𝐴^{−1}𝐛 \\ 𝐼_{2}𝐱 & =𝐴^{−1}𝐛 \\ 𝐱 & =𝐴^{−1}𝐛\end{aligned}


$$

So, to find the solution of $A\mathbf{x} = \mathbf{b},$ we simply calculate $\mathbf{x}=A^{-1}\mathbf{b}.$

For instance, to find the solution to the system of equations

$$


[\begin{aligned}1 & 1 \\ 0 & 1\end{aligned}]


$$

we first calculate the inverse of the coefficient matrix $[\begin{aligned}1 & 1 \\ 0 & 1\end{aligned}]$ This gives

$$


[\begin{aligned}1 & −1 \\ 0 & 1\end{aligned}]


$$

Then, the solution to this system is

$$


\begin{aligned}𝐱 & =𝐴^{−1}𝐛 \\ & =[\begin{aligned}1 & −1 \\ 0 & 1\end{aligned}][\begin{aligned}5 \\ 2\end{aligned}] \\ & =[\begin{aligned}3 \\ 2\end{aligned}].\end{aligned}


$$

So the solution is $x=3$ and $y=2.$

### Example: Solving a 2x2 System of Equations Using an Inverse Matrix

#### Question

Find a solution to the system of linear equations

$$


\begin{aligned}2𝑥+𝑦=2 \\ 4𝑥+3𝑦=6.\end{aligned}


$$

#### Explanation

This system can be written as

$$


[\begin{aligned}2 & 1 \\ 4 & 3\end{aligned}]


$$

To find the solution, we need to calculate the inverse of the coefficient matrix $[\begin{aligned}2 & 1 \\ 4 & 3\end{aligned}]$ This gives

$$


\begin{aligned}𝐴^{−1} & =\frac{1}{3⋅2−4⋅1}[\begin{aligned}3 & −1 \\ −4 & 2\end{aligned}] \\ & =\frac{1}{2}[\begin{aligned}3 & −1 \\ −4 & 2\end{aligned}].\end{aligned}


$$

We can now find the solution to this system:

$$


\begin{aligned}𝐱 & =𝐴^{−1}𝐛 \\ & =\frac{1}{2}[\begin{aligned}3 & −1 \\ −4 & 2\end{aligned}][\begin{aligned}2 \\ 6\end{aligned}] \\ & =\frac{1}{2}[\begin{aligned}0 \\ 4\end{aligned}] \\ & =[\begin{aligned}0 \\ 2\end{aligned}]\end{aligned}


$$

So the solution is $x=0$ and $y=2.$

### Example: Solving a 2x2 System of Equations Using an Inverse Matrix With Reorganization

#### Question

Solve the system of linear equations

$$


\begin{aligned}2𝑥−3𝑦=5 \\ 6𝑦−5𝑥=−8.\end{aligned}


$$

#### Explanation

First, we reorganize the equations so that they are in the right order, to get

$$


\begin{aligned}2𝑥−3𝑦=5 \\ −5𝑥+6𝑦=−8.\end{aligned}


$$

Now, we can represent this system of equations in the form $A\mathbf{x} =\mathbf{b}\mathbin{:}$

$$


[\begin{aligned}2 & −3 \\ −5 & 6\end{aligned}]


$$

To find the solution, we need to calculate the inverse of the coefficient matrix $[\begin{aligned}2 & −3 \\ −5 & 6\end{aligned}]$ This gives

$$


\begin{aligned}𝐴^{−1} & =\frac{1}{6⋅2−3⋅5}[\begin{aligned}6 & 3 \\ 5 & 2\end{aligned}] \\ & =−\frac{1}{3}[\begin{aligned}6 & 3 \\ 5 & 2\end{aligned}].\end{aligned}


$$

We can now find the solution to this system:

$$


\begin{aligned}𝐱 & =𝐴^{−1}𝐛 \\ & =−\frac{1}{3}[\begin{aligned}6 & 3 \\ 5 & 2\end{aligned}][\begin{aligned}5 \\ −8\end{aligned}] \\ & =−\frac{1}{3}[\begin{aligned}6 \\ 9\end{aligned}] \\ & =[\begin{aligned}−2 \\ −3\end{aligned}].\end{aligned}


$$

Therefore, the solution is $x=-2$ and $y=-3.$

### Systems of Equations Where the Coefficient Matrix is Singular

Consider the system of equations

$$


\begin{aligned}2𝑥+𝑦=3 \\ 6𝑥+3𝑦=9.\end{aligned}


$$

Can we use the matrix method of $\mathbf{x} = A^{-1}\mathbf{b}$ to find a solution to this system?

This system can be represented in the form $A\mathbf{x}=\mathbf{b}$ as

$$


[\begin{aligned}2 & 1 \\ 6 & 3\end{aligned}]


$$

To use this matrix method, we need to find $A^{-1}.$ However

$$


\det (A) = 2\cdot 3 - 1\cdot 6 =0.


$$

Therefore, $A$ is not invertible. So we cannot use the matrix method to find a solution to the system.

In general, if the coefficient matrix $A$ is not invertible, there is no unique solution. This means that either

- a solution may not exist, or

- there may be infinitely many solutions.
