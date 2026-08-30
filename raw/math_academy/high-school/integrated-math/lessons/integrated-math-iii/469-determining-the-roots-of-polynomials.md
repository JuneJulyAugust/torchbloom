# Determining the Roots of Polynomials

Source: https://www.mathacademy.com/topics/469?courseId=134
Topic ID: 469

## Prerequisites

- [Introduction to Polynomials](../../../traditional/lessons/algebra-i/655-introduction-to-polynomials.md)
- [The Roots of a Function](../../../traditional/lessons/algebra-i/2022-the-roots-of-a-function.md)

## Lesson

### Introduction

A **root** of a polynomial is a value that will make the polynomial equal zero when substituted for the polynomial's variable.

For example, consider the polynomial $x^2-9.$ This polynomial has two roots, $x=3$ and $x=-3,$ because the polynomial evaluates to $0$ when either of these values is substituted for $x\mathbin{:}$

$$


\begin{aligned}𝑥=3\,⇒\,𝑥^{2}−9 & = \\ (3)^{2}−9 & = \\ 9−9 & = \\ 0 & \,✓ \\ 𝑥=−3\,⇒\,𝑥^{2}−9 & = \\ (−3)^{2}−9 & = \\ 9−9 & = \\ 0 & \,✓\end{aligned}


$$

On the other hand, a number like $x=1$ is *not* a root of the polynomial because the polynomial does not evaluate to $0$ when this value is substituted for $x\mathbin{:}$

$$


\begin{aligned}𝑥=1\,⇒\,𝑥^{2}−9 & = \\ (1)^{2}−9 & = \\ 1−9 & = \\ −8 & \,×\end{aligned}


$$

### Example: Identifying Values that are Roots of a Given Polynomial

#### Question

Is $x=3$ a root of the polynomial $2x^3+8x^2-2x-8?$

#### Explanation

Substituting $3$ for $x$ in the polynomial and evaluating, we get the following result:

$$


\begin{aligned} 2(3)^3+8(3)^2-2(3)-8 &= \\2(27)+8(9)-6-8 &= \\54+72-14 &= \\112 \end{aligned}


$$

The polynomial does ** equal $0$ when $3$ is substituted for $x.$

Therefore, $3$ is ** a root.

### Solving for an Unknown Parameter Given the Root of a Polynomial

A **parametric polynomial** is a polynomial in which one of the coefficients is itself represented as another variable.

For example, the polynomial below is a parametric polynomial:

$$


f(x)=2x^2 -px


$$

Here, $p$ is a **parameter**, which means that it corresponds to a certain constant value. Unlike the variable $x,$ the parameter is treated exactly like any other coefficient. It's only special in that we don't know its numerical value.

If we're given the root of a polynomial, we can find the numerical value of a parameter. Let's say, for instance, that a root of the above polynomial is $x=1.$ This means that the polynomial is zero for that value:

$$


f(1)=0


$$

Therefore, we can evaluate the polynomial at $x=1,$ set it equal to $0,$ and solve the equation for the parameter $p\mathbin{:}$

$$


\begin{aligned}𝑓(1) & =0 \\ 2(1)^{2}−𝑝(1) & =0 \\ 2−𝑝 & =0 \\ 𝑝 & =2\end{aligned}


$$

### Example: Solving for an Unknown Parameter Given the Root of a Polynomial

#### Question

Find $p$ if $3$ is a root of $x^3-3x+p.$

#### Explanation

Since $x=3$ is a root, we have $f(3)=0.$ Therefore, we can evaluate the polynomial at $x=3,$ set it equal to $0,$ and solve the equation for the parameter $p\mathbin{:}$

$$


\begin{aligned}(3)^{3}−3(3)+𝑝 & =0 \\ 27−9+𝑝 & =0 \\ 𝑝 & =−18\end{aligned}


$$
