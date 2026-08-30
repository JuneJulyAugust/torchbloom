# Solving Systems of Equations Using LU Factorization

Source: https://www.mathacademy.com/topics/1782?courseId=154
Topic ID: 1782

## Prerequisites

- [Representing 3x3 Systems of Equations Using a Matrix Product](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/155-representing-3x3-systems-of-equations-using-a-matrix-product.md)
- [Solving Systems of Equations Using Back Substitution](./1047-solving-systems-of-equations-using-back-substitution.md)
- [LU Factorization of 3x3 Matrices](./1780-lu-factorization-of-3x3-matrices.md)

## Lesson

### Introduction

There is an algorithm that uses $LU$ factorization to solve systems of equations of the form

$$


A\mathbf{x}=\mathbf{b} .


$$

For example, let's solve the following equation:

$$


[\begin{aligned}1 & −3 \\ −1 & 2\end{aligned}]


$$

Since the LU factorization of $A$ is

$$


[\begin{aligned}1 & 0 \\ −1 & 1\end{aligned}]


$$

our equation $A\mathbf{x}=\mathbf{b}$ can be written as

$$


[\begin{aligned}1 & 0 \\ −1 & 1\end{aligned}]


$$

i.e.,

$$


LU\mathbf{x}= \mathbf{b}.


$$

Now, suppose we set $U\mathbf{x}=\mathbf{y}.$ Substituting this into the above, we have

$$


L\mathbf{y}= \mathbf{b}.


$$

In other words, we can reduce the problem to the following system of matrix equations:

$$


\begin{aligned}𝐿𝐲=𝐛 \\ 𝑈𝐱=𝐲\end{aligned}


$$

Since $L$ and $U$ are both triangular, each of these equations is easily solvable using back and forward substitution.

- First, we solve $L\mathbf{y} = \mathbf{b}.$ Let's assume that $[\begin{aligned}𝑦_{1} \\ 𝑦_{2}\end{aligned}]$ Then, we have which gives the system of equations Solving this equation using *forward* substitution, we get the solution

- Finally, we solve $U\mathbf{x}=\mathbf{y}.$ We have which gives the system of equations Solving this equation using *back* substitution, we get the solution

### Example: Finding the Solution of an Intermediate System Using the LU Factorization of a 2x2 Matrix

#### Question

Consider the matrix $L$ and the vector $\mathbf b,$ given by

$$


[\begin{aligned}1 & 0 \\ 15 & 1\end{aligned}]


$$

If $A=LU$ is the LU factorization of some $2\times 2$ matrix $A,$ find the vector $\mathbf{y}$ such that

$$


\begin{aligned}𝐿𝐲=𝐛 \\ 𝑈𝐱=𝐲\end{aligned}


$$

is equivalent to $A\mathbf{x}=\mathbf{b}.$

#### Explanation

First, notice that since $A=LU,$ we can write

$$


\begin{aligned}𝐴𝐱=𝐛\,⟹\,\underset{𝐴}{\underset{}{(𝐿𝑈)}}𝐱=𝐛.\end{aligned}


$$

Now, setting $U\mathbf{x}=\mathbf{y},$ we obtain

$$


\begin{aligned}𝐿𝐲=𝐛 \\ 𝑈𝐱=𝐲.\end{aligned}


$$

We now solve $L\mathbf{y} = \mathbf{b}.$ Writing this equation in matrix form, we get

$$


\begin{aligned}[\begin{matrix}1 & 0 \\ 15 & 1\end{matrix}][\begin{matrix}𝑦_{1} \\ 𝑦_{2}\end{matrix}] & =[\begin{matrix}5 \\ 66\end{matrix}].\end{aligned}


$$

This gives the system of equations

$$


\begin{aligned}𝑦_{1}=5 \\ 15𝑦_{1}+𝑦_{2}=66.\end{aligned}


$$

The solution to this system is $y_1=5$ and $y_2=-9.$

Therefore, $[\begin{aligned}5 \\ −9\end{aligned}]$

### Example: Finding the Solution of an Intermediate System Using the LU Factorization of a 3x3 Matrix

#### Question

Consider the matrix $L$ and the vector $\mathbf b,$ given by

$$


\begin{aligned}1 & 0 & 0 \\ 1 & 1 & 0 \\ 1 & −2 & 1\end{aligned}


$$

If $A=LU$ is the LU factorization of some $3\times 3$ matrix $A,$ find the vector $\mathbf{y}$ such that

$$


\begin{aligned}𝐿𝐲=𝐛 \\ 𝑈𝐱=𝐲\end{aligned}


$$

is equivalent to $A\mathbf{x}=\mathbf{b}.$

#### Explanation

First, notice that since $A=LU,$ we can write

$$


\begin{aligned}𝐴𝐱=𝐛\,⟹\,\underset{𝐴}{\underset{}{(𝐿𝑈)}}𝐱=𝐛.\end{aligned}


$$

Now, setting $U\mathbf{x}=\mathbf{y},$ we obtain

$$


\begin{aligned}𝐿𝐲=𝐛 \\ 𝑈𝐱=𝐲.\end{aligned}


$$

We now solve $L\mathbf{y} = \mathbf{b}.$ Writing this equation in matrix form, we get

$$


\begin{aligned}1 & 0 & 0 \\ 1 & 1 & 0 \\ 1 & −2 & 1\end{aligned}


$$

This gives the system of equations

$$


\begin{aligned}𝑦_{1}=2 \\ 𝑦_{1}+𝑦_{2}=4 \\ 𝑦_{1}−2𝑦_{2}+𝑦_{3}=1.\end{aligned}


$$

We can compute the solution to this system using forward substitution, as follows:

$$


\begin{aligned}𝑦_{1} & =2, \\ 𝑦_{2} & =4−𝑦_{1} \\ & =4−(2) \\ & =2, \\ 𝑦_{3} & =1−𝑦_{1}+2𝑦_{2} \\ & =1−(2)+2(2) \\ & =3.\end{aligned}


$$

Therefore, $\begin{aligned}2 \\ 2 \\ 3\end{aligned}$

### Example: Solving a 2x2 Linear System Using LU Factorization

#### Question

Consider the LU decomposition of the matrix $A$ and the vector $\mathbf{b},$ given by

$$


[\begin{aligned}1 & 0 \\ −2 & 1\end{aligned}]


$$

If $\langle x_1,x_2 \rangle$ and $\langle y_1,y_2 \rangle$ are the solutions to the systems $A\mathbf{x}=\mathbf{b}$ and $L\mathbf{y}=\mathbf{b}$ respectively, what is the value of $x_1 \cdot y_2?$

#### Explanation

First, notice that since $A=LU,$ we can write

$$


\begin{aligned}𝐴𝐱=𝐛\,⟹\,\underset{𝐴}{\underset{}{(𝐿𝑈)}}𝐱=𝐛.\end{aligned}


$$

Now, setting $U\mathbf{x}=\mathbf{y},$ we obtain

$$


\begin{aligned}𝐿𝐲=𝐛 \\ 𝑈𝐱=𝐲.\end{aligned}


$$

Now, we solve the two systems in turn.

- First, we solve $L\mathbf{y} = \mathbf{b}.$ Writing this equation in matrix form, we get This gives the system of equations The solution to this system is $y_1=6$ and $y_2=4.$ Therefore,

- Next, we solve $U\mathbf{x}=\mathbf{y}.$ Writing this equation in matrix form, we get This gives the system of equations The solution to this system is $x_2=-2$ and $x_1=2.$ Therefore,

Finally, $x_1 \cdot y_2 = 2 \cdot 4 = 8.$
