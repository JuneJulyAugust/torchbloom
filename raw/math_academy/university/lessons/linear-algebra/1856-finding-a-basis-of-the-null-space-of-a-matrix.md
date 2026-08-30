# Finding a Basis of the Null Space of a Matrix

Source: https://www.mathacademy.com/topics/1856?courseId=55
Topic ID: 1856

## Prerequisites

- [The Null Space of a Matrix](./1854-the-null-space-of-a-matrix.md)
- [Finding a Basis of a Span](./1855-finding-a-basis-of-a-span.md)

## Lesson

### Introduction

Remember that the null space $\textrm{Null}(A)$ of a matrix $A$ consists of the solutions to the equation $A\mathbf{x} = \mathbf{0}.$ To find a basis of $\textrm{Null}(A),$ we solve the equation $A\mathbf{x} = \mathbf{0}$ and express the solution as a linear combination of linearly independent vectors. Those vectors form a basis of $\textrm{Null}(A).$

To illustrate, consider the matrix $\begin{aligned}1 & 2 & 2 \\ 2 & 4 & 4 \\ 1 & 3 & 3\end{aligned}$ Computing the reduced row echelon form of $A,$ we get

$$


\begin{aligned}1 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 0\end{aligned}


$$

So, the equation $A\mathbf{x} = \mathbf{0}$ is equivalent to the system

$$


\begin{aligned}𝑥_{1}=0 \\ 𝑥_{2}+𝑥_{3}=0 \\ 0=0\end{aligned}


$$

where $\color{blue}x_1$ and $\color{blue}x_2$ are basic variables (corresponding to the pivot columns) and $\color{red}x_3$ is a free variable (corresponding to the non-pivot column).

Therefore, any vector $\mathbf{x}$ in $\textrm{Null}(A)$ has the form

$$


\begin{aligned}𝑥_{1} \\ 𝑥_{2} \\ 𝑥_{3}\end{aligned}


$$

So, the set $\begin{aligned}0 \\ −1 \\ 1\end{aligned}$ is a basis of $\textrm{Null}(A)$ since it is a linearly independent set and the vector $\begin{aligned}0 \\ −1 \\ 1\end{aligned}$ generates the null space of $A.$

**Note:** It might be the case that $\textrm{Null}(A)$ for a particular matrix $A$ equals the so-called zero subspace $\{\mathbf{0} \}$ containing only the zero-vector. The basis of $\{\mathbf{0} \}$ is said to be the *empty set*, which is a set that does not contain any vectors. The empty set is denoted by $\emptyset$ or $\{\,\}.$

### Example: Finding a Basis for a Given Null Space

#### Question

Given that $\begin{aligned}3𝑥_{3}−𝑥_{4} \\ 4𝑥_{3} \\ 𝑥_{3} \\ 𝑥_{4}\end{aligned}$ find a basis for $\textrm{Null}(A).$

#### Explanation

Any vector in $\textrm{Null}(A)$ has the form

$$


\begin{aligned}3𝑥_{3}−𝑥_{4} \\ 4𝑥_{3} \\ 𝑥_{3} \\ 𝑥_{4}\end{aligned}


$$

Expanding, we get

$$


\begin{aligned}\begin{aligned}3𝑥_{3}−𝑥_{4} \\ 4𝑥_{3} \\ 𝑥_{3} \\ 𝑥_{4}\end{aligned} & =\begin{aligned}3𝑥_{3} \\ 4𝑥_{3} \\ 𝑥_{3} \\ 0\end{aligned}+\begin{aligned}−𝑥_{4} \\ 0 \\ 0 \\ 𝑥_{4}\end{aligned} \\ & =𝑥_{3}\begin{aligned}3 \\ 4 \\ 1 \\ 0\end{aligned}+𝑥_{4}\begin{aligned}−1 \\ 0 \\ 0 \\ 1\end{aligned}.\end{aligned}


$$

Therefore, a basis for $\textrm{Null}(A)$ is

$$


\begin{aligned}3 \\ 4 \\ 1 \\ 0\end{aligned}


$$

since it is a linearly independent set and its vectors generate $\textrm{Null}(A).$

### Example: Finding a Basis for the Null Space of a Matrix Given in Reduced Row Echelon Form

#### Question

Find a basis of the null space of the matrix $\begin{aligned}1 & 3 & 0 & 0 \\ 0 & 0 & 1 & −4 \\ 0 & 0 & 0 & 0\end{aligned}$

#### Explanation

To find a basis of $\textrm{Null}(A),$ we need to solve the equation $A\mathbf{x} = \mathbf{0}$ and express the solution as a linear combination of linearly independent vectors. Those vectors form a basis of $\textrm{Null}(A).$

The given matrix is already in reduced row echelon form. So, the equation $A\mathbf{x}=\mathbf{0}$ corresponds to the following system:

$$


\begin{aligned}𝑥_{1}+3𝑥_{2}=0 \\ 𝑥_{3}−4𝑥_{4}=0 \\ 0=0\end{aligned}


$$

Here, $x_1$ and $x_3$ are basic variables corresponding to the pivot columns ($1$st and $3$rd) and $x_2,x_4$ are free variables corresponding to the non-pivot columns. Therefore, if $\mathbf{x} \in \textrm{Null}(A),$ then

$$


\begin{aligned}\begin{aligned}𝑥_{1} \\ 𝑥_{2} \\ 𝑥_{3} \\ 𝑥_{4}\end{aligned} & =\begin{aligned}−3𝑥_{2} \\ 𝑥_{2} \\ 4𝑥_{4} \\ 𝑥_{4}\end{aligned} \\ & =\begin{aligned}−3𝑥_{2} \\ 𝑥_{2} \\ 0 \\ 0\end{aligned}+\begin{aligned}0 \\ 0 \\ 4𝑥_{4} \\ 𝑥_{4}\end{aligned} \\ & =𝑥_{2}\begin{aligned}−3 \\ 1 \\ 0 \\ 0\end{aligned}+𝑥_{4}\begin{aligned}0 \\ 0 \\ 4 \\ 1\end{aligned}\end{aligned}


$$

where $x_2,x_4\in\mathbb{R}.$ This implies that

$$


\begin{aligned}−3 \\ 1 \\ 0 \\ 0\end{aligned}


$$

is a basis of $\textrm{Null}(A)$ since it is a linearly independent set and its vectors generate $\textrm{Null}(A).$

### Example: Finding a Basis of the Null Space of a Matrix Given a Row Equivalent Matrix

#### Question

The matrices $A$ and $B$ are given below. If $A$ is row equivalent to $B$, then find a basis of $\textrm{Null}(A).$

$$


\begin{aligned}−9 & 3 & −1 & 2 \\ 1 & 3 & −1 & 2 \\ −5 & 9 & −3 & 6\end{aligned}


$$

#### Explanation

To find a basis of $\textrm{Null}(A),$ we need to solve the equation $A\mathbf{x} = \mathbf{0}$ and express the solution as a linear combination of linearly independent vectors. Those vectors form a basis of $\textrm{Null}(A).$

Since $A\sim B,$ the equation $A \mathbf{x} = \mathbf{0}$ is equivalent to the equation $B\mathbf{x}=\mathbf{0},$ which corresponds to the following system:

$$


\begin{aligned}𝑥_{1}=0 \\ 𝑥_{2}−\frac{1}{3}𝑥_{3}+\frac{2}{3}𝑥_{4}=0\end{aligned}


$$

So, the general solution is $x_1=0$ and $x_2=\dfrac{1}{3}x_3 - \dfrac{2}{3} x_4$ where $x_3$ and $x_4$ are free variables. Therefore, if $\mathbf{x}\in\textrm{Null}(A),$ then

$$


\begin{aligned}\begin{aligned}𝑥_{1} \\ 𝑥_{2} \\ 𝑥_{3} \\ 𝑥_{4}\end{aligned} & =\begin{aligned}0 \\ \frac{1}{3}𝑥_{3}−\frac{2}{3}𝑥_{4} \\ 𝑥_{3} \\ 𝑥_{4}\end{aligned}=𝑥_{3}\begin{aligned}0 \\ \frac{1}{3} \\ 1 \\ 0\end{aligned}+𝑥_{4}\begin{aligned}0 \\ −\frac{2}{3} \\ 0 \\ 1\end{aligned},\,𝑥_{3},𝑥_{4}∈ℝ.\end{aligned}


$$

This implies that

$$


\begin{aligned}0 \\ \frac{1}{3} \\ 1 \\ 0\end{aligned}


$$

is a basis of $\textrm{Null}(A)$ since it is a linearly independent set and its vectors generate $\textrm{Null}(A).$

### Example: Finding a Basis for the Null Space of a Matrix That Is Not in Reduced Row Echelon Form

#### Question

Given the matrix $\begin{aligned}1 & 0 & 2 \\ 0 & 1 & 2 \\ 0 & 2 & 5\end{aligned}$ find a basis of $\textrm{Null}(A).$

#### Explanation

First, we reduce the matrix $A$ to reduced row echelon form (RREF):

$$


\begin{aligned}𝐴 & =\begin{aligned}1 & 0 & 2 \\ 0 & 1 & 2 \\ 0 & 2 & 5\end{aligned} & 𝑅_{3} & :=𝑅_{3}+(−2)𝑅_{2} \\ & ∼\begin{aligned}1 & 0 & 2 \\ 0 & 1 & 2 \\ 0 & 0 & 1\end{aligned} & 𝑅_{2} & :=𝑅_{2}+(−2)𝑅_{3} \\ & ∼\begin{aligned}1 & 0 & 2 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{aligned} & 𝑅_{1} & :=𝑅_{1}+(−2)𝑅_{3} \\ & ∼\begin{aligned}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{aligned} & & \end{aligned}


$$

So, the equation $A\mathbf{x} = \mathbf{0}$ is equivalent to the system

$$


\begin{aligned}𝑥_{1}=0 \\ 𝑥_{2}=0 \\ 𝑥_{3}=0.\end{aligned}


$$

This implies that the only solution of $A\mathbf{x}=\mathbf{0}$ is $\mathbf{x}=\mathbf{0}.$ So $\textrm{Null}(A)=\{\mathbf{0} \},$ which means that the basis of $\textrm{Null}(A)$ is the empty set, i.e., $\mathcal{B}=\{\,\}.$
