# Linear Independence for Homogeneous Systems of ODEs

Source: https://www.mathacademy.com/topics/6374?courseId=155
Topic ID: 6374

## Prerequisites

- [Introduction to Systems of Linear ODEs](./2086-introduction-to-systems-of-linear-odes.md)
- [Linear Independence of Solutions to Homogeneous ODEs](../differential-equations/2547-linear-independence-of-solutions-to-homogeneous-odes.md)

## Lesson

### Introduction

The **Wronskian** $W(\mathbf{x}_1,\mathbf{x}_2)$ of two vector-valued functions

$$


[\begin{aligned}𝑥_{11}(𝑡) \\ 𝑥_{21}(𝑡)\end{aligned}]


$$

is defined as

$$


\begin{aligned}𝑥_{11}(𝑡) & 𝑥_{12}(𝑡) \\ 𝑥_{21}(𝑡) & 𝑥_{22}(𝑡)\end{aligned}


$$

Analogous to scalar ordinary differential equations (ODEs), the Wronskian of vector-valued functions can be used to determine linear dependency. In particular:

- If the Wronskian is not identically zero, then $\mathbf{x}_1$ and $\mathbf{x}_2$ are *linearly independent*.

- If the Wronskian is identically zero, and it's known that $\mathbf{x}_1$ and $\mathbf{x}_2$ are solutions to the same system of linear ODEs, then $\mathbf{x}_1$ and $\mathbf{x}_2$ are *linearly dependent*.

Let's see some concrete examples.

### Example: Calculating the Wronskian of Two Vector-Valued Functions

#### Question

$$


[\begin{aligned}𝑡^{3} \\ 2\end{aligned}]


$$

Find the Wronskian $W(\mathbf{x}_1, \mathbf{x}_2)$ of the above vector-valued functions.

#### Explanation

The Wronskian $W(\mathbf{x}_1,\mathbf{x}_2)$ of two vector-valued functions

$$


[\begin{aligned}𝑥_{11}(𝑡) \\ 𝑥_{21}(𝑡)\end{aligned}]


$$

is defined as

$$


\begin{aligned}𝑥_{11}(𝑡) & 𝑥_{12}(𝑡) \\ 𝑥_{21}(𝑡) & 𝑥_{22}(𝑡)\end{aligned}


$$

Therefore, our Wronskian is

$$


\begin{aligned}𝑊(𝐱_{1},𝐱_{2}) & =\begin{matrix}𝑡^{3} & 𝑡^{3}−5 \\ 2 & 4\end{matrix} \\ & =𝑡^{3}⋅4−(𝑡^{3}−5)⋅2 \\ & =4𝑡^{3}−2𝑡^{3}+10 \\ & =2𝑡^{3}+10.\end{aligned}


$$

### Example: Identifying Linearly Independent Vector-Valued Functions

#### Question

$$


[\begin{aligned}−4𝑒^{2𝑡} \\ 𝑒^{2𝑡}\end{aligned}]


$$

Consider the vector-valued functions $\mathbf{x}_1(t)$ and $\mathbf{x}_2(t)$ above. Given that $\mathbf x_1$ and $\mathbf x_2$ are solutions of the same system of linear ODEs, compute the Wronskian is $W(\mathbf{x}_1, \mathbf{x}_2)$ and determine if the set $\left\{\mathbf{x}_1(t), \mathbf{x}_2(t) \right\}$ is linearly dependent on $\mathbb R.$

#### Explanation

The Wronskian $W(\mathbf{x}_1,\mathbf{x}_2)$ of two vector-valued functions

$$


[\begin{aligned}𝑥_{11}(𝑡) \\ 𝑥_{21}(𝑡)\end{aligned}]


$$

is defined as

$$


\begin{aligned}𝑥_{11}(𝑡) & 𝑥_{12}(𝑡) \\ 𝑥_{21}(𝑡) & 𝑥_{22}(𝑡)\end{aligned}


$$

Note the following:

- If the Wronskian is not identically zero, then $\mathbf{x}_1$ and $\mathbf{x}_2$ are linearly independent.

- If the Wronskian is identically zero, and it's known that $\mathbf{x}_1$ and $\mathbf{x}_2$ are solutions to the same system of linear ODEs, then $\mathbf{x}_1$ and $\mathbf{x}_2$ are linearly dependent.

In our case, our Wronskian is given by

$$


\begin{aligned}𝑊(𝐱_{1},𝐱_{2}) & =\begin{matrix}−4𝑒^{2𝑡} & 𝑒^{𝑡} \\ 𝑒^{2𝑡} & 2𝑒^{𝑡}\end{matrix} \\ & =(−4𝑒^{2𝑡})⋅(2𝑒^{𝑡})−𝑒^{𝑡}⋅(𝑒^{2𝑡}) \\ & =−8𝑒^{3𝑡}−𝑒^{3𝑡} \\ & =−9𝑒^{3𝑡}\end{aligned}


$$

which is nonzero for at least one $t\in \mathbb R.$

Therefore, the set $\left\{\mathbf{x}_1(t), \mathbf{x}_2(t) \right\}$ is linearly independent on $\mathbb R.$

### Fundamental Sets of Solutions for Systems of Linear ODEs

A pair of solutions $\mathbf{x}_1(t)$ and $\mathbf{x}_2(t)$ to a $2\times 2$ homogeneous linear system

$$


\mathbf{x}'(t)=A\mathbf{x}(t)


$$

is called a **fundamental set of solutions** on an interval if the solutions are linearly independent on that interval.

A practical test for determining whether a pair of functions forms a fundamental set of solutions is to use the Wronskian:

If $\mathbf{x}_1$ and $\mathbf{x}_2$ are solutions to the system and

$$


W(\mathbf{x}_1,\mathbf{x}_2) \neq 0


$$

for at least one $t_0$ in the interval, then they form a fundamental set of solutions on that interval.

This definition generalizes to any $n\times n$ homogeneous linear system $\mathbf{x}'(t)=A\mathbf{x}(t).$ A set of solutions

$$


\mathbf{x}_1(t),\ \mathbf{x}_2(t),\ \ldots,\ \mathbf{x}_n(t)


$$

is a *fundamental set of solutions* on an interval if the solutions are linearly independent on that interval.

The same Wronskian idea applies: compute the determinant of the $n\times n$ matrix whose columns are $\mathbf{x}_1(t),\ldots,\mathbf{x}_n(t).$ If it is nonzero at some $t_0$ in the interval, then the solutions form a fundamental set on that interval.

Next, we will look at a concrete example applying this test.

### Example: Identifying Fundamental Sets of Solutions to Systems of Linear ODEs

#### Question

$$


\begin{aligned}𝑥_{′1}(𝑡)=2𝑥_{1}(𝑡)+𝑥_{2}(𝑡) \\ 𝑥_{′2}(𝑡)=−4𝑥_{1}(𝑡)−2𝑥_{2}(𝑡).\end{aligned}


$$

Consider the system of linear ODEs above, where $t\in\mathbb R.$ Which of the following statements are true?

1. The function $[\begin{aligned}𝑡^{2}+1 \\ −4𝑡\end{aligned}]$ is a solution of the system.

2. The function $[\begin{aligned}2𝑡+1 \\ −4𝑡\end{aligned}]$ is a solution of the system.

3. The function $[\begin{aligned}𝑡 \\ 1−2𝑡\end{aligned}]$ is a solution of the system.

Also, determine which pair of solutions forms a set of fundamental solutions to the system.

#### Explanation

The Wronskian $W(\mathbf{x}_1,\mathbf{x}_2)$ of two vector-valued functions

$$


[\begin{aligned}𝑥_{11}(𝑡) \\ 𝑥_{21}(𝑡)\end{aligned}]


$$

is defined as

$$


\begin{aligned}𝑥_{11}(𝑡) & 𝑥_{12}(𝑡) \\ 𝑥_{21}(𝑡) & 𝑥_{22}(𝑡)\end{aligned}


$$

Note the following:

- If the Wronskian is not identically zero, then $\mathbf{x}_1$ and $\mathbf{x}_2$ are linearly independent.

- If the Wronskian is identically zero, and it's known that $\mathbf{x}_1$ and $\mathbf{x}_2$ are solutions to the same system of linear ODEs, then $\mathbf{x}_1$ and $\mathbf{x}_2$ are linearly dependent.

First, we write our system in matrix form:

$$


[\begin{aligned}2 & 1 \\ −4 & −2\end{aligned}]


$$

Now, let's substitute the given vectors into the matrix differential equation:

- $[\begin{aligned}𝑡^{2}+1 \\ −4𝑡\end{aligned}]$ $\text{isn't}$ a solution of the system. Indeed:

- $[\begin{aligned}2𝑡+1 \\ −4𝑡\end{aligned}]$ $\text{is}$ a solution of the system. Indeed:

- $[\begin{aligned}𝑡 \\ 1−2𝑡\end{aligned}]$ $\text{is}$ a solution of the system. Indeed:

Now, consider the set of solutions $\big\{\mathbf{b},\mathbf{c} \big\}.$ Its Wronskian is

$$


\begin{aligned}𝑊(𝐛,𝐜) & =\begin{matrix}2𝑡+1 & 𝑡 \\ −4𝑡 & 1−2𝑡\end{matrix} \\ & =(2𝑡+1)⋅(1−2𝑡)−𝑡⋅(−4𝑡) \\ & =(2𝑡+1)(1−2𝑡)+4𝑡^{2} \\ & =1\end{aligned}


$$

which is nonzero for at least one $t \in \mathbb R.$ Thus, since $\mathbf b$ and $\mathbf c$ are both solutions of the same linear system, and their Wronskian is nonzero for at least one $t\in\mathbb R,$ $\big\{\mathbf{b},\mathbf{c} \big\}$ is a set of fundamental solutions of the system.
