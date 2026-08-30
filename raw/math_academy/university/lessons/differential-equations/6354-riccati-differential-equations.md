# Riccati Differential Equations

Source: https://www.mathacademy.com/topics/6354?courseId=61
Topic ID: 6354

## Prerequisites

- [Bernoulli Differential Equations](./2522-bernoulli-differential-equations.md)
- [Solving First-Order ODEs by Substitution](./3179-solving-first-order-odes-by-substitution.md)

## Lesson

### Introduction

A **Riccati differential equation** is an ordinary differential equation of the form

$$


\dfrac{\mathrm{d}y}{\mathrm{d}x} = a(x)y^2 + b(x)y + c(x)


$$

where $a(x)$, $b(x)$, and $c(x)$ are continuous functions.

For example, consider the equation

$$


\dfrac{\mathrm{d}y}{\mathrm{d}x} = xy^2 + y +1.


$$

This is a Riccati differential equation with

$$


a(x) = x, \qquad b(x) = 1, \qquad c(x) = 1.


$$

Note that this equation is *nonlinear* because of the $y^2$ term. In general, Riccati equations cannot be solved directly using the methods we have learned so far. Later in the lesson, we will learn how to reduce a Riccati equation to a Bernoulli differential equation.

For now, let’s get some practice identifying Riccati differential equations.

### Example: Identifying Riccati Differential Equations

#### Question

Which of the following equations is a Riccati differential equation?

1. $y' = 4xy^2 - 3y + 1$

2. $y' - 2y = (x^2 + 5)y^2 + \sin(x)$

3. $y' = e^xy^3 + y - x$

#### Explanation

A first-order differential equation is a Riccati differential equation if it can be written in the form

$$


y' = a(x)y^2 + b(x)y + c(x).


$$

With that in mind, let's examine the given options.

- Equation I is a Riccati differential equation with

- Equation II is a Riccati differential equation. Writing the equation in standard form, we get This is a Riccati differential equation with

- Equation III is not a Riccati differential equation. Writing the equation in standard form, we get This is not a Riccati differential equation since it includes a $y^3$ term.

Therefore, the correct answer is "I and II only."

### The Relationship Between Riccati and Bernoulli Differential Equations

Now that we have practiced identifying Riccati equations, let’s learn how to solve them.

In general, Riccati equations cannot be solved directly. There is, however, one useful strategy.

If we are able to guess one particular solution of the Riccati equation, call it $y_0(x),$ then the substitution

$$


y(x) = z(x) + y_0(x)


$$

transforms the Riccati equation into a Bernoulli differential equation for $z(x)$, which we already know how to solve.

Starting from the Riccati equation

$$


y' = a(x)y^2 + b(x)y + c(x),


$$

we substitute $y = z + y_0.$ Then

$$


\begin{aligned}𝑦^{′} & =𝑧^{′}(𝑥)+𝑦_{′0}(𝑥) \\ & =𝑎(𝑧+𝑦_{0})^{2}+𝑏(𝑧+𝑦_{0})+𝑐 \\ & =𝑎𝑧^{2}+2𝑎𝑧𝑦_{0}+𝑎𝑦_{20}+𝑏𝑧+𝑏𝑦_{0}+𝑐.\end{aligned}


$$

Since $y_0(x)$ is a particular solution, it satisfies

$$


y_0' =a y_0^2 + b y_0 + c.


$$

Subtracting this equation from the previous expression and re-arranging gives

$$


z' - [2a(x) y_0(x) + b(x)] z = a(x) z^2.


$$

This is a Bernoulli equation of the form

$$


\frac{ \text{d} z}{\text{d}x} + P(x)z = Q(x)z^n,


$$

where

$$


P(x) = - [2a(x) y_0(x) + b(x)], \qquad Q(x) = a(x) , \qquad n = 2.


$$

In the next slide, we will apply this strategy to a concrete example.

### Example: Reducing a Riccati Differential Equation to a Bernoulli Equation

#### Question

The function $y_0(x) = 1$ is a particular solution of the Riccati differential equation

$$


y' = 3y^2 - 7y + 4.


$$

Express this equation in the Bernoulli form

$$


\frac{\text{d}z}{\text{d}x} + P(x)z = Q(x)z^n


$$

and state the functions $P(x)$ and $Q(x),$ and the value of $n.$

#### Explanation

A Riccati differential equation has the form

$$


y' = a(x)y^2 + b(x)y + c(x).


$$

To reduce the given Riccati equation to a Bernoulli equation, we use the substitution

$$


y(x) = z(x) + y_0(x),


$$

where $y_0(x)$ is a known particular solution. Differentiating gives

$$


y'(x) = z'(x) + y_0'(x).


$$

In our case, $y_0(x) = 1.$ Since $y_0'(x) = 0$, we have

$$


y = z + 1 \qquad \Rightarrow \qquad y' = z'.


$$

Let's substitute these expressions into our Riccati equation:

$$


z' = 3(z + 1)^2 - 7(z + 1) + 4.


$$

Now, we expand the right-hand side, and simplify:

$$


\begin{aligned}𝑧^{′} & =3(𝑧+1)^{2}−7(𝑧+1)+4 \\ 𝑧^{′} & =3𝑧^{2}−𝑧 \\ 𝑧^{′}+𝑧 & =3𝑧^{2}\end{aligned}


$$

This is a Bernoulli equation of the form

$$


\frac{ \text{d} z}{\text{d}x} + P(x)z = Q(x)z^n


$$

where

$$


P(x) = 1, \qquad Q(x) = 3, \qquad n = 2.


$$

### Example: Solving Riccati Differential Equations

#### Question

Given that $y_0(x) = 4x$ is a particular solution of the Riccati differential equation

$$


y' = 2x\,y^2 - 16x^2 y + 32x^3 + 4


$$

find the general solution of the equation.

#### Explanation

The equation

$$


y' = 2x\,y^2 - 16x^2 y + 32x^3 + 4,


$$

is a Riccati differential equation of the form

$$


y' = a(x)y^2 + b(x)y + c(x),


$$

where

$$


a(x) = 2x, \qquad b(x) = -16x^2, \qquad c(x) = 32x^3 + 4.


$$

To reduce the given Riccati equation to a Bernoulli equation, we use the substitution

$$


y(x) = z(x) + y_0(x),


$$

where $y_0(x)$ is a known particular solution. Differentiating gives

$$


y'(x) = z'(x) + y_0'(x).


$$

In our case, $y_0(x) = 4x.$ Since $y_0'(x) = 4$, we have

$$


y = z + 4x \qquad \Rightarrow \qquad y' = z' + 4.


$$

Let's substitute these expressions into our Riccati equation:

$$


z' + 4 = 2x\,(z + 4x)^2 - 16x^2 (z + 4x) + 32x^3 + 4.


$$

Now, we expand the right-hand side, and simplify:

$$


\begin{aligned}𝑧^{′}+4 & =2𝑥(𝑧^{2}+8𝑥𝑧+16𝑥^{2})−16𝑥^{2}(𝑧+4𝑥)+32𝑥^{3}+4 \\ 𝑧^{′}+4 & =2𝑥𝑧^{2}+4 \\ 𝑧^{′} & =2𝑥𝑧^{2}\end{aligned}


$$

We can solve the obtained equation using separation of variables:

$$


\begin{aligned}\frac{d𝑧}{d𝑥} & =2𝑥𝑧^{2} \\ \frac{1}{𝑧^{2}}\frac{d𝑧}{d𝑥} & =2𝑥 \\ ∫\frac{1}{𝑧^{2}}\frac{d𝑧}{d𝑥}\,d𝑥 & =∫2𝑥\,d𝑥 \\ ∫𝑧^{−2}\,d𝑧 & =∫2𝑥\,d𝑥 \\ −\frac{1}{𝑧} & =𝑥^{2}+𝐶 \\ 𝑧 & =−\frac{1}{𝑥^{2}+𝐶}\end{aligned}


$$

where $C$ is an arbitrary constant.

Finally, let's substitute $z = y-4x$ to recover the initial variable $y{:}$

$$


\begin{aligned}𝑧 & =−\frac{1}{𝑥^{2}+𝐶} \\ 𝑦−4𝑥 & =−\frac{1}{𝑥^{2}+𝐶} \\ 𝑦 & =−\frac{1}{𝑥^{2}+𝐶}+4𝑥 \\ & =4𝑥−\frac{1}{𝑥^{2}+𝐶}.\end{aligned}


$$
