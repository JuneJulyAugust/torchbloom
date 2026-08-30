# Solving Systems of Equations Using Inverse Matrices

Source: https://www.mathacademy.com/topics/1023?courseId=101
Topic ID: 1023

## Prerequisites

- [Calculating the Inverse of a 3x3 Matrix Using the Cofactor Method](./154-calculating-the-inverse-of-a-3x3-matrix-using-the-cofactor-method.md)
- [Representing 3x3 Systems of Equations Using a Matrix Product](./155-representing-3x3-systems-of-equations-using-a-matrix-product.md)
- [Solving 2x2 Systems of Equations Using Inverse Matrices](./934-solving-2x2-systems-of-equations-using-inverse-matrices.md)

## Lesson

### Introduction

We know that we can write a system of three linear equations in three variables in the form $A\mathbf{x}=\mathbf{b},$ where

- $A$ is the $3\times 3$ coefficient matrix,

- $\mathbf{x}$ is the column vector of variables, and

- $\mathbf{b}$ is the column vector of constants.

If the $3\times 3$ matrix $A$ is invertible, then we can find a solution to the system $A\mathbf{x} = \mathbf{b}$ by "pre-multiplying" both sides of the equation by $A^{-1}{:}$

$$


\begin{aligned}𝐴𝐱 & =𝐛 \\ 𝐴^{−1}𝐴𝐱 & =𝐴^{−1}𝐛 \\ 𝐼_{3}𝐱 & =𝐴^{−1}𝐛 \\ 𝐱 & =𝐴^{−1}𝐛\end{aligned}


$$

So, to find the solution of $A\mathbf{x}=\mathbf{b},$ we simply calculate $\mathbf{x}= A^{-1}\mathbf{b}.$

Let's see how this works for a particular system in the next example.

### Example: Solving a 3x3 System of Equations Given the Inverse of the Coefficient Matrix

#### Question

Consider the following system of linear equations:

$$


\begin{aligned}−2𝑥+5𝑦−2𝑧=−2 \\ −3𝑦+𝑧=−2 \\ 3𝑥−7𝑦+3𝑧=3\end{aligned}


$$

The system above has the matrix representation $A \mathbf{x} = \mathbf{b}.$ Given that $\mathbf x = \langle x,y,z\rangle$ is unique, what is the value of $x+y+z?$

**

$$


\begin{aligned}−2 & −1 & −1 \\ 3 & 0 & 2 \\ 9 & 1 & 6\end{aligned}


$$

#### Explanation

First, let's write our system in matrix form as follows:

$$


\begin{aligned}𝐴𝐱 & =𝐛 \\ \begin{matrix}−2 & 5 & −2 \\ 0 & −3 & 1 \\ 3 & −7 & 3\end{matrix}\begin{matrix}𝑥 \\ 𝑦 \\ 𝑧\end{matrix} & =\begin{matrix}−2 \\ −2 \\ 3\end{matrix}\end{aligned}


$$

Recall that the solution to $A\mathbf{x}=\mathbf{b}$ is given by $\mathbf{x}= A^{-1}\mathbf{b}.$

Therefore, we obtain

$$


\begin{aligned}𝐱 & =𝐴^{−1}𝐛 \\ & =\begin{matrix}−2 & −1 & −1 \\ 3 & 0 & 2 \\ 9 & 1 & 6\end{matrix}\begin{matrix}−2 \\ −2 \\ 3\end{matrix} \\ & =\begin{matrix}3 \\ 0 \\ −2\end{matrix}.\end{aligned}


$$

So, the solution is $x=3, y=0, z=-2.$

Finally, $x+y+z=3+0+(-2)=1.$

### Example: Solving a 3x3 System of Equations By Calculating the Inverse of the Coefficient Matrix

#### Question

Solve the following system of linear equations using matrices:

$$


\begin{aligned}\begin{matrix}3𝑦+𝑥+𝑧=0 \\ 𝑧+4𝑦−5=2 \\ 1+2𝑥−𝑦=−3\end{matrix}\end{aligned}


$$

#### Explanation

First, we organize the system so that the variables are in the correct order and every variable has a coefficient:

$$


\begin{aligned}\begin{matrix}𝑥+3𝑦+𝑧=0 \\ 0𝑥+4𝑦+𝑧=7 \\ 2𝑥−𝑦+0𝑧=−4\end{matrix}\end{aligned}


$$

Next, we write the system in the form $A\mathbf{x} = \mathbf{b}$, where $A$ is a $3\times 3$ matrix and $\mathbf{x}$ and $\mathbf{b}$ are $3\times 1$ column vectors. We can do this as follows:

$$


\begin{aligned}1 & 3 & 1 \\ 0 & 4 & 1 \\ 2 & −1 & 0\end{aligned}


$$

Now, the solution to $A\mathbf{x}=\mathbf{b}$ is given by $\mathbf{x}= A^{-1}\mathbf{b}.$ So, we compute $A^{-1}$ as follows:

**: Find the determinant of $A.$

$$


\begin{aligned}det(𝐴)=\begin{matrix}1 & 3 & 1 \\ 0 & 4 & 1 \\ 2 & −1 & 0\end{matrix} & =1\begin{matrix}4 & 1 \\ −1 & 0\end{matrix}−3\begin{matrix}0 & 1 \\ 2 & 0\end{matrix}+1\begin{matrix}0 & 4 \\ 2 & −1\end{matrix} \\ & =(1)−3(−2)+(−8) \\ & =1+6−8 \\ & =−1\end{aligned}


$$

**: Compute the matrix of minors.

$$


\begin{aligned}𝑀 & =\begin{matrix}\begin{matrix}4 & 1 \\ −1 & 0\end{matrix} & \begin{matrix}0 & 1 \\ 2 & 0\end{matrix} & \begin{matrix}0 & 4 \\ 2 & −1\end{matrix} \\ \begin{matrix}3 & 1 \\ −1 & 0\end{matrix} & \begin{matrix}1 & 1 \\ 2 & 0\end{matrix} & \begin{matrix}1 & 3 \\ 2 & −1\end{matrix} \\ \begin{matrix}3 & 1 \\ 4 & 1\end{matrix} & \begin{matrix}1 & 1 \\ 0 & 1\end{matrix} & \begin{matrix}1 & 3 \\ 0 & 4\end{matrix}\end{matrix} \\ & =\begin{matrix}1 & −2 & −8 \\ 1 & −2 & −7 \\ −1 & 1 & 4\end{matrix}\end{aligned}


$$

**: Find the matrix of cofactors.

$$


\begin{aligned}1 & 2 & −8 \\ −1 & −2 & 7 \\ −1 & −1 & 4\end{aligned}


$$

**: Transpose the matrix of cofactors.

$$


\begin{aligned}1 & −1 & −1 \\ 2 & −2 & −1 \\ −8 & 7 & 4\end{aligned}


$$

**: Apply the inverse matrix formula.

$$


\begin{aligned}1 & −1 & −1 \\ 2 & −2 & −1 \\ −8 & 7 & 4\end{aligned}


$$

Finally, we can calculate the solution as follows:

$$


\begin{aligned}𝐱 & =𝐴^{−1}𝐛 \\ & =\begin{matrix}−1 & 1 & 1 \\ −2 & 2 & 1 \\ 8 & −7 & −4\end{matrix}\begin{matrix}0 \\ 7 \\ −4\end{matrix} \\ & =\begin{matrix}3 \\ 10 \\ −33\end{matrix}\end{aligned}


$$

Therefore, the solution is $x=3,$ $y=10,$ $z=-33.$

### Example: Solving a Matrix Equation Using Algebraic Manipulation

#### Question

Consider a matrix equation $B\,\mathbf{x} = A^{-1}\,\mathbf{d},$ where $A$ and $B$ are $10 \times 10$ non-singular matrices, while $\mathbf{x}$ and $\mathbf{d}$ are $10 \times 1$ column vectors. Solve the equation for $\mathbf{x}.$

#### Explanation

Since $B$ is not singular, it must have an inverse $B^{−1}.$ Now, pre-multiplying both sides of the equation $B\,\mathbf{x} = A^{-1}\,\mathbf{d}$ by $B^{-1},$ we obtain

$$


\begin{aligned}𝐵\,𝐱 & =𝐴^{−1}\,𝐝 \\ 𝐵^{−1}𝐵\,𝐱 & =𝐵^{−1}𝐴^{−1}\,𝐝 \\ 𝐼_{10}\,𝐱 & =𝐵^{−1}𝐴^{−1}\,𝐝 \\ 𝐱 & =𝐵^{−1}𝐴^{−1}\,𝐝.\end{aligned}


$$
