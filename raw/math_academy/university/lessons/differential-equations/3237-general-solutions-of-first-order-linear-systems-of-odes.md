# General Solutions of First-Order Linear Systems of ODEs

Source: https://www.mathacademy.com/topics/3237?courseId=61
Topic ID: 3237

## Prerequisites

- [Linear Independence for Homogeneous Systems of ODEs](./6374-linear-independence-for-homogeneous-systems-of-odes.md)
- [General Solutions of First-Order Linear ODEs](./6678-general-solutions-of-first-order-linear-odes.md)

## Lesson

### Introduction

Given two solutions to a linear system of differential equations, any *constant-coefficient* linear combination of those solutions is also a solution to the system. This property of linear systems is called the **linearity principle** (or the **superposition principle**).

Let's state this again, more precisely. If $\mathbf{u}(t)$ and $\mathbf{v}(t)$ are solutions to the homogeneous matrix differential equation

$$


\mathbf{x}'(t)=A\mathbf{x}(t),


$$

then the expression

$$


c \, \mathbf{u}(t) + d \, \mathbf{v}(t)


$$

is also a solution to that equation for all $c,d\in\mathbb{R}.$

We can prove this by substituting $\mathbf x(t) = c\mathbf{u}(t) +d\mathbf{v}(t)$ into the matrix differential equation and verifying that it results in a true statement:

$$


\begin{aligned}𝐱^{′}(𝑡) & =𝐴𝐱(𝑡) \\ (𝑐\,𝐮(𝑡)+𝑑\,𝐯(𝑡))^{′} & =𝐴(𝑐\,𝐮(𝑡)+𝑑\,𝐯(𝑡)) \\ 𝑐\,𝐮^{′}(𝑡)+𝑑\,𝐯^{′}(𝑡) & =𝑐𝐴\,𝐮(𝑡)+𝑑𝐴\,𝐯(𝑡) \\ 𝑐\,𝐮^{′}(𝑡)+𝑑\,𝐯^{′}(𝑡) & =𝑐\,𝐮^{′}(𝑡)+𝑑\,𝐯^{′}(𝑡)\,✓\end{aligned}


$$

Therefore, $c\,\mathbf{u}(t) +d\,\mathbf{v}(t)$ is a solution!

In general, the *linearity principle* for systems of linear ordinary differential equations states that if

$$


\mathbf{x}_{1}(t), \: \mathbf{x}_{2}(t), \: \ldots, \: \mathbf{x}_{k}(t)


$$

are solutions to a homogeneous linear system $\mathbf{x}'(t) = A \mathbf{x}(t),$ then any linear combination

$$


c_1 \, \mathbf{x}_{1}(t) + c_2 \, \mathbf{x}_{2}(t) + \cdots + c_k \, \mathbf{x}_{k}(t)


$$

with $c_1, c_2, \ldots, c_k \in\mathbb R$ is also a solution of the same homogeneous system.

Next, let's see a concrete example.

### Example: Applying the Linearity Principle to the Solutions of a Homogeneous System of ODEs

#### Question

Suppose $\mathbf{x}_1(t)$ and $\mathbf{x}_2(t)$ are both solutions of the homogeneous system $\mathbf{x}'(t) = A \ \mathbf{x}(t).$ Which of the following is **** a solution of the same system?

1. $\mathbf{x}(t) = 6 \cdot \mathbf{x}_1(t) - \mathbf{x}_2(t)$

2. $\mathbf{x}(t) = -3 \cdot \mathbf{x}_1(t) + 4 \cdot \mathbf{x}_2(t)$

3. $\mathbf{x}(t) = (1+t^2)\cdot \mathbf{x}_1(t) + e^{t}\cdot \mathbf{x}_2(t)$

#### Explanation

The ** for systems of linear ordinary differential equations (ODEs) states that if $\mathbf{x}_{1}(t)$ and $\mathbf{x}_{2}(t)$ are solutions to a homogeneous linear system, then for any constants $c_1$ and $c_2,$ the linear combination

$$


c_{1}\mathbf{x}_{1}(t)+c_{2}\mathbf{x}_{2}(t)


$$

is also a solution of the system.

With that in mind, let's examine the given expressions.

- Option I is a solution to the system. Indeed, notice that is a linear combination of the solutions $\mathbf{x}_{1}(t)$ and $\mathbf{x}_{2}(t)$ with constant multiplies $c_1=6$ and $c_2=-1,$ respectively.

- Option II is a solution to the system. Indeed, notice that is a linear combination of the solutions $\mathbf{x}_{1}(t)$ and $\mathbf{x}_{2}(t)$ with constant multiplies $c_1=-3$ and $c_2=4,$ respectively.

- Option III might be ** a solution to the system since it's not a linear combination of the solutions $\mathbf{x}_{1}(t)$ and $\mathbf{x}_{2}(t).$ Notice that the multipliers of the first and the second terms are not constant.

Therefore, the correct answer is "I and II only".

### Example: Finding the Image of a Vector Under a Matrix Given Solutions to a Matrix ODE

#### Question

If $[\begin{aligned}𝑒^{4𝑡} \\ 0\end{aligned}]$ and $[\begin{aligned}0 \\ 𝑒^{5𝑡}\end{aligned}]$ are solutions to $\mathbf{x}'(t)=A\mathbf{x}(t),$ find $A\mathbf{w}(t)$ where $[\begin{aligned}4𝑒^{4𝑡} \\ 6𝑒^{5𝑡}\end{aligned}]$

#### Explanation

Since $\mathbf{u}(t)$ and $\mathbf{v}(t)$ are solutions to $\mathbf{x}'(t)=A\mathbf{x}(t),$ the superposition principle guarantees that

$$


c\mathbf{u}(t) + d\mathbf{v}(t)


$$

is also a solution to $\mathbf{x}'(t)=A\mathbf{x}(t)$ for all $c,d\in\mathbb{R}.$

Notice that

$$


\mathbf{w}(t)=4\mathbf{u}(t)+6\mathbf{v}(t).


$$

Therefore, $\mathbf{w}$ is a solution to $\mathbf{x}'(t)=A\mathbf{x}(t).$ So, in order to find $A\mathbf{w}(t)$ we just need to find $\mathbf{w}'(t)$ as follows:

$$


\begin{aligned}𝐴𝐰 & =𝐰^{′}(𝑡) \\ & =[\begin{aligned}(4𝑒^{4𝑡})^{′} \\ (6𝑒^{5𝑡})^{′}\end{aligned}] \\ & =[\begin{aligned}16𝑒^{4𝑡} \\ 30𝑒^{5𝑡}\end{aligned}]\end{aligned}


$$

### General Solutions of First-Order Linear Systems of ODEs

If $\mathbf{x}_h(t)$ satisfies a *homogeneous* linear system

$$


\mathbf{x}'(t) = A \mathbf{x}(t)


$$

and $\mathbf{x}_p(t)$ is a particular solution to an *inhomogeneous* linear system

$$


\mathbf{x}'(t) = A \mathbf{x}(t) + \mathbf{f}(t),


$$

where $\mathbf{f}(t)$ is some nonzero vector of functions, then

$$


\mathbf{x}_h(t) + \mathbf{x}_p(t)


$$

is also a solution to the same inhomogeneous system.

This gives us the **general solution** structure:

$$


\text{(every solution)} = \text{(homogeneous solution)} + \text{(a particular solution)}


$$

Let's see some examples.

### Example: Constructing General Solutions of First-Order Linear Systems of ODEs

#### Question

Let $\mathbf{x}_1(t)$ and $\mathbf{x}_2(t)$ satisfy the homogeneous system $\mathbf{x}'(t) = A \ \mathbf{x}(t)$ and $\mathbf{x}_p(t)$ satisfy the inhomogeneous system $\mathbf{x}'(t) = A \ \mathbf{x}(t) + \mathbf{f}(t).$ Which of the following is **** a solution of the same inhomogeneous system?

1. $\mathbf{x}_1(t) + 2\cdot \mathbf{x}_2(t) + \mathbf{x}_p(t)$

2. $4\cdot \mathbf{x}_2(t) + \mathbf{x}_p(t)$

3. $-\mathbf{x}_1(t) - \mathbf{x}_p(t)$

#### Explanation

Recall that if $\mathbf{x}_h(t)$ satisfies a homogeneous linear system $\mathbf{x}'(t) = A \mathbf{x}(t)$ and $\mathbf{x}_p(t)$ is a particular solution to an inhomogeneous linear system $\mathbf{x}'(t) = A \mathbf{x}(t) + \mathbf{f}(t),$ then $\mathbf{x}_h(t) + \mathbf{x}_p(t)$ is also a solution to the same inhomogeneous system.

Additonally, the ** for systems of linear ordinary differential equations (ODEs) states that if $\mathbf{x}_{1}(t),$ $\mathbf{x}_{2}(t),\ldots, \mathbf{x}_{k}(t)$ are solutions to a homogeneous linear system $\mathbf{x}'(t) = A \mathbf{x}(t),$ then any linear combination

$$


c_1 \mathbf{x}_{1}(t) + c_2\mathbf{x}_{2}(t) + \cdots + c_k\mathbf{x}_{k}(t)


$$

with $c_1, c_2, \ldots, c_k \in\mathbb R$ is also a solution of the same homogeneous system.

With that in mind, let's examine the given expression.

- Option I is a solution to the inhomogeneous system. Indeed, notice that the linear combination is a solution to the homogeneous system $\mathbf{x}'(t) = A \mathbf{x}(t)$ according to the linearity principle. Thus, is a solution to our inhomogeneous system $\mathbf{x}'(t) = A \mathbf{x}(t) + \mathbf{f}(t).$

- Option II is a solution to the inhomogeneous system. Indeed, notice that the linear combination is a solution to the homogeneous system $\mathbf{x}'(t) = A \mathbf{x}(t)$ according to the linearity principle. Thus, is a solution to our inhomogeneous system $\mathbf{x}'(t) = A \mathbf{x}(t) + \mathbf{f}(t).$

- Option III might be ** a solution to the inhomogeneous system. Notice that $-\mathbf{x}_1(t) - \mathbf{x}_p(t)$ can't be written as where $\mathbf{x}_h(t)$ is a solution of the homogeneous system, because of the multiplier $-1$ next to the particular solution $\mathbf{x}_p(t).$

Therefore, the correct answer is "I and II only".
