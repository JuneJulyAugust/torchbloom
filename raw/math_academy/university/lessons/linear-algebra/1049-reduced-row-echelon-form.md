# Reduced Row Echelon Form

Source: https://www.mathacademy.com/topics/1049?courseId=55
Topic ID: 1049

## Prerequisites

- [Solving 3x3 Singular Systems of Equations Using Gaussian Elimination](./1374-solving-3x3-singular-systems-of-equations-using-gaussian-elimination.md)

## Lesson

### Introduction

Consider a system of linear equations and its respective augmented matrix $M\mathbin{:}$

$$


\begin{aligned}𝑥+𝑦+𝑧=2 \\ 𝑦+𝑧=−1 \\ −2𝑧=2\end{aligned}


$$

The matrix $M$ is already in row echelon form, but we can transform it even further into the **reduced row echelon form** (RREF) using the standard **Gauss-Jordan** method.

The algorithm is similar to the algorithm of converting a matrix to row echelon form, except that we need to make *all* the pivot entries equal to $1$ and *all* the entries below *and above* a pivot (in a pivot column) equal to $0.$

In our case, we convert $M$ to reduced row echelon form as follows:

$$


\begin{aligned}𝑀 & =\begin{aligned}1 & 1 & 1 & 2 \\ 0 & 1 & 1 & −1 \\ 0 & 0 & −2 & 2\end{aligned} & 𝑅_{3} & :=−\frac{1}{2}𝑅_{3} \\ & ∼\begin{aligned}1 & 1 & 1 & 2 \\ 0 & 1 & 1 & −1 \\ 0 & 0 & 1 & −1\end{aligned} & 𝑅_{2} & :=𝑅_{2}+(−1)𝑅_{3} \\ & ∼\begin{aligned}1 & 1 & 1 & 2 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & −1\end{aligned} & 𝑅_{1} & :=𝑅_{1}+(−1)𝑅_{3} \\ & ∼\begin{aligned}1 & 1 & 0 & 3 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & −1\end{aligned} & 𝑅_{1} & :=𝑅_{1}+(−1)𝑅_{2} \\ & ∼\begin{aligned}1 & 0 & 0 & 3 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & −1\end{aligned} & & \end{aligned}


$$

The final matrix is in reduced row echelon form:

- all the pivot entries are equal to $1$ (here we have $\color{red}1$'s on the main diagonal), and

- all the entries below and above a pivot are equal to ${\color{blue}0}.$

### General Algorithm (RREF)

For a $3\times 3$ system with $3$ pivots, the Gauss-Jordan method can be described as follows:

1. First, reduce the matrix to row echelon form using the standard Gaussian elimination method (also making all pivot entries equal to $1$).

2. We use the third row and necessary row operations to make the entries above $a_{33}$ equal to $0.$ Namely, if $a_{23} \neq 0$, then we use the row operation $R_2:=R_2 + (-a_{23})R_3$, and if $a_{13} \neq 0$, then we use the row operation $R_1:=R_1 + (-a_{13})R_3$.

3. We use the second row and necessary row operations to make the entries above $a_{22}$ equal to $0$. Namely, if $a_{12} \neq 0$, then we use the row operation $R_1:=R_1 + (-a_{12})R_2$.

Carrying out the above algorithm will convert the matrix to reduced row echelon form.

$$


\begin{aligned}1 & 0 & 0 & ∗ \\ 0 & 1 & 0 & ∗ \\ 0 & 0 & 1 & ∗\end{aligned}


$$

**Note:** Unlike the row echelon form, the *reduced* row echelon form of a matrix is unique.

### Example: Finding the Reduced Row Echelon Form of a 3x3 System That Is Already in Row Echelon Form

#### Question

Consider the following system of linear equations:

$$


\begin{aligned}𝑥−𝑦+𝑧=−3 \\ 𝑦+2𝑧=−7 \\ 𝑧=−4\end{aligned}


$$

Use the standard Gauss-Jordan method to reduce the augmented matrix $M$ of the system to reduced row echelon form, and then solve the linear system.

#### Explanation

The augmented matrix for this system is

$$


\begin{aligned}1 & −1 & 1 & −3 \\ 0 & 1 & 2 & −7 \\ 0 & 0 & 1 & −4\end{aligned}


$$

Transforming $M$ into reduced row echelon form, we have

$$


\begin{aligned}𝑀 & =\begin{aligned}1 & −1 & 1 & −3 \\ 0 & 1 & 2 & −7 \\ 0 & 0 & 1 & −4\end{aligned} & 𝑅_{2} & :=𝑅_{2}+(−2)𝑅_{3} \\ & ∼\begin{aligned}1 & −1 & 1 & −3 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & −4\end{aligned} & 𝑅_{1} & :=𝑅_{1}+(−1)𝑅_{3} \\ & ∼\begin{aligned}1 & −1 & 0 & 1 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & −4\end{aligned} & 𝑅_{1} & :=𝑅_{1}+𝑅_{2} \\ & ∼\begin{aligned}1 & 0 & 0 & 2 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & −4\end{aligned}. & & \end{aligned}


$$

The corresponding system is now

$$


\begin{aligned}𝑥=2 \\ 𝑦=1 \\ 𝑧=−4.\end{aligned}


$$

So, we have the solution $x=2,$ $y=1,$ and $z=-4.$ Or, in vector form, $\langle 2,1,-4 \rangle.$

### Example: Finding the Reduced Row Echelon Form of a 3x3 System That Is Not in Row Echelon Form

#### Question

Consider the following system of linear equations:

$$


\begin{aligned}𝑥+𝑦−𝑧=1 \\ 2𝑥+𝑦+3𝑧=4 \\ 5𝑥+4𝑦+𝑧=7\end{aligned}


$$

Use the standard Gauss-Jordan method to reduce the augmented matrix $M$ of the system to reduced row echelon form, and then solve the linear system.

#### Explanation

The augmented matrix for this system is

$$


\begin{aligned}1 & 1 & −1 & 1 \\ 2 & 1 & 3 & 4 \\ 5 & 4 & 1 & 7\end{aligned}


$$

Transforming $M$ into reduced row echelon form, we have

$$


\begin{aligned}𝑀 & =\begin{aligned}1 & 1 & −1 & 1 \\ 2 & 1 & 3 & 4 \\ 5 & 4 & 1 & 7\end{aligned} & 𝑅_{2} & :=𝑅_{2}−2𝑅_{1} \\ & ∼\begin{aligned}1 & 1 & −1 & 1 \\ 0 & −1 & 5 & 2 \\ 5 & 4 & 1 & 7\end{aligned} & 𝑅_{3} & :=𝑅_{3}−5𝑅_{1} \\ & ∼\begin{aligned}1 & 1 & −1 & 1 \\ 0 & −1 & 5 & 2 \\ 0 & −1 & 6 & 2\end{aligned} & 𝑅_{2} & :=−𝑅_{2} \\ & ∼\begin{aligned}1 & 1 & −1 & 1 \\ 0 & 1 & −5 & −2 \\ 0 & −1 & 6 & 2\end{aligned} & 𝑅_{3} & :=𝑅_{3}+𝑅_{2} \\ & ∼\begin{aligned}1 & 1 & −1 & 1 \\ 0 & 1 & −5 & −2 \\ 0 & 0 & 1 & 0\end{aligned} & 𝑅_{2} & :=𝑅_{2}+5𝑅_{3} \\ & ∼\begin{aligned}1 & 1 & −1 & 1 \\ 0 & 1 & 0 & −2 \\ 0 & 0 & 1 & 0\end{aligned} & 𝑅_{1} & :=𝑅_{1}+𝑅_{3} \\ & ∼\begin{aligned}1 & 1 & 0 & 1 \\ 0 & 1 & 0 & −2 \\ 0 & 0 & 1 & 0\end{aligned} & 𝑅_{1} & :=𝑅_{1}+(−1)𝑅_{2} \\ & ∼\begin{aligned}1 & 0 & 0 & 3 \\ 0 & 1 & 0 & −2 \\ 0 & 0 & 1 & 0\end{aligned}. & & \end{aligned}


$$

The corresponding system is now

$$


\begin{aligned}𝑥=3 \\ 𝑦=−2 \\ 𝑧=0.\end{aligned}


$$

So, we have the solution $x=3,$ $y=-2,$ and $z=0.$ Or, in vector form, $\langle 3,-2,0 \rangle.$

### Using the Gauss-Jordan Method on a 3x3 System With Two Pivots

When a $3\times3$ system of equations has two pivot columns instead of three, we can still reduce its augmented matrix to reduced row echelon form. The process is similar to what we did before.

1. First, reduce the matrix to row echelon form using the standard Gaussian elimination method (also making all pivot entries equal to $1$).

2. We use the second row and necessary row operations to make the entries above $a_{22}$ equal to $0$. Namely, if $a_{12} \neq 0$, then we use the row operation $R_1:=R_1 + (-a_{12})R_2$.

Carrying out the above algorithm will convert the matrix to reduced row echelon form.

$$


\begin{aligned}1 & 0 & ∗ & ∗ \\ 0 & 1 & ∗ & ∗ \\ 0 & 0 & 0 & ∗\end{aligned}


$$

### Example: Finding the Reduced Row Echelon Form of a Singular 3x3 System With Two Pivots

#### Question

Consider the following system of linear equations:

$$


\begin{aligned}𝑥−2𝑦=2 \\ 𝑥−4𝑧=6 \\ −3𝑥+6𝑦=−6\end{aligned}


$$

Use the standard Gauss-Jordan method to reduce the augmented matrix $M$ of the system to reduced row echelon form, and then solve the linear system.

#### Explanation

The augmented matrix for this system is

$$


\begin{aligned}1 & −2 & 0 & 2 \\ 1 & 0 & −4 & 6 \\ −3 & 6 & 0 & −6\end{aligned}


$$

Transforming $M$ into reduced row echelon form, we have

$$


\begin{aligned}𝑀 & ∼\begin{aligned}1 & −2 & 0 & 2 \\ 1 & 0 & −4 & 6 \\ −3 & 6 & 0 & −6\end{aligned} & 𝑅_{2} & :=𝑅_{2}+(−1)𝑅_{1} \\ & ∼\begin{aligned}1 & −2 & 0 & 2 \\ 0 & 2 & −4 & 4 \\ −3 & 6 & 0 & −6\end{aligned} & 𝑅_{3} & :=𝑅_{3}+3𝑅_{1} \\ & ∼\begin{aligned}1 & −2 & 0 & 2 \\ 0 & 2 & −4 & 4 \\ 0 & 0 & 0 & 0\end{aligned} & 𝑅_{2} & :=\frac{1}{2}𝑅_{2} \\ & ∼\begin{aligned}1 & −2 & 0 & 2 \\ 0 & 1 & −2 & 2 \\ 0 & 0 & 0 & 0\end{aligned}. & & \end{aligned}


$$

In the row echelon form above, we have only two pivots (in the $1$st and $2$nd columns). To transform the matrix to reduced row echelon form, we need to create zeros above the pivots only. This gives,

$$


\begin{aligned}𝑀 & ∼\begin{aligned}1 & −2 & 0 & 2 \\ 0 & 1 & −2 & 2 \\ 0 & 0 & 0 & 0\end{aligned} & 𝑅_{1} & :=𝑅_{1}+2𝑅_{2} \\ & ∼\begin{aligned}1 & 0 & −4 & 6 \\ 0 & 1 & −2 & 2 \\ 0 & 0 & 0 & 0\end{aligned}. & & \end{aligned}


$$

The corresponding system is now

$$


\begin{aligned}𝑥−4𝑧=6 \\ 𝑦−2𝑧=2 \\ 0=0.\end{aligned}


$$

Since any numbers $x,y,z$ form a solution of the final equation, we can remove this equation from the system.

The basic variables are the variables whose coefficients are pivots. In this case, the basic variables are $x$ and $y,$ and we have one free variable, $z.$ That means we need to find $x$ and $y$ in terms of $z.$

Therefore, the general solution is

$$


\begin{aligned}𝑥=4𝑧+6 \\ 𝑦=2𝑧+2 \\ 𝑧=𝑧,\end{aligned}


$$

where $z$ (the free variable) is an arbitrary number.

In vector form, the solution can be written as

$$


\begin{aligned}\begin{aligned}𝑥 \\ 𝑦 \\ 𝑧\end{aligned}=\begin{aligned}4𝑧+6 \\ 2𝑧+2 \\ 𝑧\end{aligned},\,𝑧∈(−∞,∞).\end{aligned}


$$

### Using the Gauss-Jordan Method on a 3x3 System With One Pivot

It's also possible to write the augmented matrix for a $3\times 3$ system of linear equations with only one pivot in reduced row echelon form.

Let's see an example of how this works.

### Example: Finding the Reduced Row Echelon Form of a Singular 3x3 System With One Pivot

#### Question

Consider the following system of linear equations:

$$


\begin{aligned}2𝑥−6𝑦+2𝑧=8 \\ −6𝑥+18𝑦−6𝑧=−24 \\ 4𝑥−12𝑦+4𝑧=16\end{aligned}


$$

Use the standard Gauss-Jordan method to reduce the augmented matrix $M$ of the system to reduced row echelon form.

#### Explanation

The augmented matrix for this system is

$$


\begin{aligned}2 & −6 & 2 & 8 \\ −6 & 18 & −6 & −24 \\ 4 & −12 & 4 & 16\end{aligned}


$$

Transforming $M$ to reduced row echelon form, we have

$$


\begin{aligned}𝑀 & ∼\begin{aligned}2 & −6 & 2 & 8 \\ −6 & 18 & −6 & −24 \\ 4 & −12 & 4 & 16\end{aligned} & 𝑅_{1} & :=\frac{1}{2}𝑅_{1} \\ & ∼\begin{aligned}1 & −3 & 1 & 4 \\ −6 & 18 & −6 & −24 \\ 4 & −12 & 4 & 16\end{aligned} & 𝑅_{2} & :=𝑅_{2}+6𝑅_{1} \\ & ∼\begin{aligned}1 & −3 & 1 & 4 \\ 0 & 0 & 0 & 0 \\ 4 & −12 & 4 & 16\end{aligned} & 𝑅_{3} & :=𝑅_{3}+(−4)𝑅_{1} \\ & ∼\begin{aligned}1 & −3 & 1 & 4 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0\end{aligned}. & & \end{aligned}


$$

Therefore,

$$


\begin{aligned}1 & −3 & 1 & 4 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0\end{aligned}


$$
