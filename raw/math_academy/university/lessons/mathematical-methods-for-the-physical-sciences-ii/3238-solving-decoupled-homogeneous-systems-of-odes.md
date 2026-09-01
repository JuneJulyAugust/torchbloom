# Solving Decoupled Homogeneous Systems of ODEs

Source: https://www.mathacademy.com/topics/3238?courseId=155
Topic ID: 3238

## Prerequisites

- [Exponential Growth and Decay Models With First-Order ODEs](../../../ap-courses/lessons/ap-calculus-ab/876-exponential-growth-and-decay-models-with-first-order-odes.md)
- [General Solutions of First-Order Linear Systems of ODEs](./3237-general-solutions-of-first-order-linear-systems-of-odes.md)

## Lesson

### Introduction

A **decoupled system** of ODEs is a system in which each equation involves only its own dependent variable. For a linear homogeneous system, this means each equation has the form

$$


x'_i(t) = \lambda_i x_i(t),


$$

where $\lambda_i$ is a constant. This means that we can solve each equation independently.

For example, the system

$$


\begin{aligned}𝑥_{′1}(𝑡)=−𝑥_{1}(𝑡) \\ 𝑥_{′2}(𝑡)=5𝑥_{2}(𝑡)\end{aligned}


$$

is decoupled, while the system

$$


\begin{aligned}𝑥_{′1}(𝑡)=𝑥_{2}(𝑡) \\ 𝑥_{′2}(𝑡)=𝑥_{1}(𝑡)−𝑥_{2}(𝑡)\end{aligned}


$$

is *not* decoupled.

In matrix form, a linear system

$$


\mathbf{x}'(t) = A\mathbf{x}(t)


$$

is decoupled exactly when $A$ is a diagonal matrix. For example:

- The system is decoupled since its corresponding matrix is diagonal.

- The system is *not* decoupled because its matrix is not diagonal.

### Example: Identifying a Decoupled System of Linear ODEs

#### Question

Which of the following systems of linear ODEs are decoupled?

1. $\begin{aligned}𝑥_{′1}(𝑡)=4𝑥_{1}(𝑡)+2𝑥_{2}(𝑡) \\ 𝑥_{′2}(𝑡)=−𝑥_{1}(𝑡)+6𝑥_{2}(𝑡)\end{aligned}$

2. $\begin{aligned}𝑥_{′1}(𝑡)=−3𝑥_{1}(𝑡) \\ 𝑥_{′2}(𝑡)=7𝑥_{2}(𝑡)\end{aligned}$

3. $\begin{aligned}𝑥_{′1}(𝑡)=5𝑥_{2}(𝑡) \\ 𝑥_{′2}(𝑡)=2𝑥_{1}(𝑡)−𝑥_{2}(𝑡)\end{aligned}$

#### Explanation

A ** consists of equations depending on only one variable, such as

$$


x'_i(t) = \lambda_i x_i(t),


$$

where $\lambda_i$ is a constant. This means that we can solve each equation independently.

With this in mind, let's examine our systems.

- System I is ** decoupled because some of its equations depend on more than one variable. For example, $x'_1(t) = 4x_1(t) + 2x_2(t)$ depends on $x_1(t)$ and $x_2(t).$

- System II is decoupled since its equations depend on only one variable each. Indeed, $x'_1(t) = -3x_1(t)$ depends on only $x_1(t)$ and $x'_2(t) = 7x_2(t)$ depends on only $x_2(t).$

- System III is ** decoupled because, for example, the first equation depends on $x_2(t).$

Therefore, the correct answer is "II only".

### Solving a Decoupled System: General Solution

Now, let's consider the following decoupled system:

$$


\begin{aligned}𝑥_{′1}(𝑡)=3𝑥_{1}(𝑡) \\ 𝑥_{′2}(𝑡)=−5𝑥_{2}(𝑡)\end{aligned}


$$

Since $A$ is diagonal, we can solve the two differential equations separately using elementary calculus:

- The solution to $x_1'(t)={3}x_1(t)$ is $x_1(t)=c_1e^{{3}t}$ for $c_1\in\mathbb{R}.$

- The solution to $x_2'(t)={-5}x_2(t)$ is $x_2(t)=c_2e^{{-5}t}$ for $c_2\in\mathbb{R}.$

Therefore, we can write the solution of the system as

$$


[\begin{aligned}𝑥_{1}(𝑡) \\ 𝑥_{2}(𝑡)\end{aligned}]


$$

In general, for a decoupled system

$$


\begin{aligned}𝑥_{′1}(𝑡)=𝜆_{1}𝑥_{1}(𝑡) \\ 𝑥_{′2}(𝑡)=𝜆_{2}𝑥_{2}(𝑡)\end{aligned}


$$

the formula for the **general solution** is

$$


[\begin{aligned}1 \\ 0\end{aligned}]


$$

Note that the set

$$


[\begin{aligned}1 \\ 0\end{aligned}]


$$

always forms a linearly independent set of fundamental solutions to the system.

### Example: Finding the General Solution to a Decoupled Linear System of Differential Equations

#### Question

Find the general solution to the system of differential equations given by

$$


\begin{aligned}𝑥_{′1}(𝑡)=−6𝑥_{1}(𝑡) \\ 𝑥_{′2}(𝑡)=3𝑥_{2}(𝑡).\end{aligned}


$$

#### Explanation

Given a decoupled system of first-order linear ODEs in the form

$$


[\begin{aligned}𝑥_{′1}(𝑡) \\ 𝑥_{′2}(𝑡)\end{aligned}]


$$

the formula for the general solution is

$$


[\begin{aligned}1 \\ 0\end{aligned}]


$$

First, we write our differential equation in matrix form:

$$


[\begin{aligned}𝑥_{′1}(𝑡) \\ 𝑥_{′2}(𝑡)\end{aligned}]


$$

Since the matrix of the differential system is diagonal, the system is decoupled.

Therefore, the general solution is given by

$$


[\begin{aligned}1 \\ 0\end{aligned}]


$$

### Solving an Initial Value Problem: Particular Solution

Consider the following decoupled system of differential equations:

$$


\begin{aligned}𝑥_{′1}(𝑡)=𝑥_{1}(𝑡) \\ 𝑥_{′2}(𝑡)=−𝑥_{2}(𝑡)\end{aligned}


$$

We already know that the *general solution* to this is given by

$$


[\begin{aligned}1 \\ 0\end{aligned}]


$$

But sometimes we may need to find a **particular solution** where we give specific values to the constants $c_1$ and $c_2.$

For example, suppose that $x_1$ and $x_2$ represent the number of birds of species $A$ and $B,$ respectively, that inhabit a particular island, and the above system models the growth rates of the two species.

Given this information, we might want to know how many birds of each type there will be after $t=3$ years. To answer this question, we need an **initial condition**, which is some extra information about the system at a particular moment in time.

Suppose that at $t=0,$ there were initially $20$ birds of species $A$ and $2\,000$ birds of species $B.$ We can write this initial condition as follows:

$$


[\begin{aligned}𝑥_{1}(0) \\ 𝑥_{2}(0)\end{aligned}]


$$

Then, by substituting $t=0$ into the general solution, we can find specific values of $c_1$ and $c_2\mathbin{:}$

$$


\begin{aligned}𝐱(0) & =[\begin{matrix}20 \\ 2\,000\end{matrix}] \\ 𝑐_{1}[\begin{matrix}1 \\ 0\end{matrix}]𝑒^{0}+𝑐_{2}[\begin{matrix}0 \\ 1\end{matrix}]𝑒^{0} & =[\begin{matrix}20 \\ 2\,000\end{matrix}] \\ [\begin{matrix}𝑐_{1} \\ 𝑐_{2}\end{matrix}] & =[\begin{matrix}20 \\ 2\,000\end{matrix}]\end{aligned}


$$

So, $c_1 = 20$ and $c_2 = 2\,000$.

Therefore, the particular solution is given by

$$


[\begin{aligned}1 \\ 0\end{aligned}]


$$

Finally, we can find how many birds of each type there will be after $t=3$ years by substituting $t=3$ into the particular solution:

$$


\begin{aligned}𝐱(3) & =20[\begin{matrix}1 \\ 0\end{matrix}]𝑒^{3}+2\,000[\begin{matrix}0 \\ 1\end{matrix}]𝑒^{−3} \\ & =[\begin{matrix}20𝑒^{3} \\ 0\end{matrix}]+[\begin{matrix}0 \\ 2\,000𝑒^{−3}\end{matrix}] \\ & =[\begin{matrix}20𝑒^{3} \\ 2\,000𝑒^{−3}\end{matrix}] \\ & ≈[\begin{matrix}401.7 \\ 99.6\end{matrix}]\end{aligned}


$$

We conclude that there will be approximately $402$ birds of species $A$ and $100$ birds of species $B$ after $t=3$ years.

### Example: Solving an Initial Value Problem for a Decoupled Linear System of First-Order ODEs

#### Question

Solve the initial value problem

$$


[\begin{aligned}1 & 0 \\ 0 & 2ln⁡(3)\end{aligned}]


$$

#### Explanation

We have a decoupled system. Therefore, the general solution is given by

$$


\begin{aligned}𝐱(𝑡) & =𝑐_{1}[\begin{matrix}1 \\ 0\end{matrix}]𝑒^{1𝑡}+𝑐_{2}[\begin{matrix}0 \\ 1\end{matrix}]𝑒^{2ln⁡(3)𝑡} \\ & =𝑐_{1}[\begin{matrix}1 \\ 0\end{matrix}]𝑒^{𝑡}+𝑐_{2}[\begin{matrix}0 \\ 1\end{matrix}](𝑒^{ln⁡(9)})^{𝑡} \\ & =𝑐_{1}[\begin{matrix}1 \\ 0\end{matrix}]𝑒^{𝑡}+𝑐_{2}[\begin{matrix}0 \\ 1\end{matrix}]9^{𝑡},\,𝑐_{1},𝑐_{2}∈ℝ.\end{aligned}


$$

Now, we need to find the values of $c_1$ and $c_2$ using the initial value $\mathbf{x}(0).$ Substituting $t=0$ into the general solution gives

$$


\begin{aligned}𝐱(0) & =𝑐_{1}[\begin{matrix}1 \\ 0\end{matrix}]𝑒^{0}+𝑐_{2}[\begin{matrix}0 \\ 1\end{matrix}]9^{0} \\ [\begin{matrix}2 \\ −1\end{matrix}] & =[\begin{matrix}𝑐_{1} \\ 𝑐_{2}\end{matrix}].\end{aligned}


$$

Therefore, the solution to our initial value problem is given by

$$


\begin{aligned}𝐱(𝑡) & =2[\begin{matrix}1 \\ 0\end{matrix}]𝑒^{𝑡}+(−1)[\begin{matrix}0 \\ 1\end{matrix}]9^{𝑡} \\ & =[\begin{matrix}2 \\ 0\end{matrix}]𝑒^{𝑡}+[\begin{matrix}0 \\ −1\end{matrix}]9^{𝑡}.\end{aligned}


$$
