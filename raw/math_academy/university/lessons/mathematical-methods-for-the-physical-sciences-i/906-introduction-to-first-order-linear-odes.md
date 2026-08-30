# Introduction to First-Order Linear ODEs

Source: https://www.mathacademy.com/topics/906?courseId=154
Topic ID: 906

## Prerequisites

- [Introduction to Differential Equations](../../../ap-courses/lessons/ap-calculus-ab/3215-introduction-to-differential-equations.md)

## Lesson

### Introduction

A **first-order linear ordinary differential equation** is a differential equation in the variable $y(x)$ that can be expressed in the **general form**

$$


a(x)y'(x)+b(x)y(x)=f(x)


$$

where

- $a(x),$ $b(x),$ and $f(x)$ are functions of $x$ only, and

- $a(x)$ is not identically zero (i.e., it is not zero for all $x$).

For example, the differential equation

$$


xy' + e^x y=1


$$

is a first-order linear ODE with $a(x) = x, b(x) = e^x,$ and $f(x) = 1.$

On the other hand, the differential equation

$$


x(y')^2 + e^x \sin(y)=1


$$

is *not* a first-order linear ODE. Notice that it contains the terms $(y')^2$ and $\sin(y),$ and therefore cannot be presented in the general form.

### The Standard Form of a First-Order Linear ODE

The general form of a first-order linear ODE is

$$


a(x)y'+b(x)y=f(x).


$$

Now, if we take the general form and divide both sides by $a(x),$ we get

$$


\begin{aligned}\frac{𝑎(𝑥)}{𝑎(𝑥)}𝑦^{′}+\frac{𝑏(𝑥)}{𝑎(𝑥)}𝑦 & =\frac{𝑓(𝑥)}{𝑎(𝑥)} \\ 𝑦^{′}+\frac{𝑏(𝑥)}{𝑎(𝑥)}𝑦 & =\frac{𝑓(𝑥)}{𝑎(𝑥)}.\end{aligned}


$$

Remember that $a(x)$ is not identically zero, so we're allowed to perform this division.

Now, if we define the functions $P$ and $Q$ as

$$


P(x)=\dfrac{b(x)}{a(x)}, \qquad Q(x)=\dfrac{f(x)}{a(x)},


$$

then we can write our equation in the following **standard form**:

$$


y'+P(x)y =Q(x)


$$

For example, given the first-order linear ODE

$$


y' \sin x+ y e^x= \cos x,


$$

the standard form of this equation can be found by dividing through by $\sin x,$ as follows:

$$


\begin{aligned}𝑦^{′}+𝑦(\frac{𝑒^{𝑥}}{sin⁡𝑥}) & =\frac{cos⁡𝑥}{sin⁡𝑥} \\ 𝑦^{′}+𝑦𝑒^{𝑥}csc⁡𝑥 & =cot⁡𝑥.\end{aligned}


$$

Here, we have

$$


P(x) = e^x \csc x, \qquad Q(x) = \cot x.


$$

### Example: Writing First-Order Linear ODEs in Standard Form

#### Question

Write the following first-order linear ODE in standard form.

$$


\dfrac {\text{d}y} {\text{d}x} + y\sin x - \cos x =0


$$

#### Explanation

A first-order linear ODE is in standard form if it is written as

$$


\dfrac {\text{d}y} {\text{d}x} + P(x)y = Q(x).


$$

Converting the given equation to standard form, we have

$$


\begin{aligned}\frac{d𝑦}{d𝑥}+𝑦sin⁡𝑥−cos⁡𝑥 & =0 \\ \frac{d𝑦}{d𝑥}+𝑦sin⁡𝑥 & =cos⁡𝑥 \\ \frac{d𝑦}{d𝑥}+\underset{𝑃(𝑥)}{\underset{}{(sin⁡𝑥)}}𝑦 & =\underset{𝑄(𝑥)}{\underset{}{cos⁡𝑥}}\,.\end{aligned}


$$

Now, the equation is written in standard form with $P(x)=\sin x$ and $Q(x) = \cos x.$

### Example: Identifying First-Order Linear ODEs

#### Question

Determine whether the following equation is a first-order linear ODE:

$$


x^2\dfrac {\text{d}y} {\text{d}x} + \sin(2x)y = e^x.


$$

#### Explanation

We attempt to write the equation in the standard form

$$


\dfrac {\text{d}y} {\text{d}x} + P(x)y = Q(x) \,.


$$

Dividing the equation through by $x^2$ gives

$$


\begin{aligned}𝑥^{2}\frac{d𝑦}{d𝑥}+sin⁡(2𝑥)𝑦 & =𝑒^{𝑥} \\ \frac{d𝑦}{d𝑥}+\frac{sin⁡(2𝑥)}{𝑥^{2}}𝑦 & =\frac{𝑒^{𝑥}}{𝑥^{2}}.\end{aligned}


$$

We can see that this equation is now in standard form with $P(x) = \dfrac{\sin{2x}}{x^2}$ and $Q(x) = \dfrac{e^x}{x^2}.$

Because the equation can be written in standard form, we conclude that it is a first-order linear ODE.

### Homogeneous and Inhomogeneous Equations

Recall that the standard form of a first-order linear differential equation is

$$


y' + P(x)y = Q(x).


$$

Note that $Q(x)$ is called the **forcing function.**

A first-order linear ODE is **homogeneous** if the forcing function $Q(x) = 0$ for all $x.$ In other words, the equation is homogeneous if it can be written in the form

$$


y' + P(x)y = 0.


$$

A first-order linear ODE is **inhomogeneous** if it is not homogeneous.

Let's consider some examples:

- Suppose we have the equation The equation matches the form $y' + P(x)y = 0$ with $P(x) = -x.$ Therefore, this equation *is* homogeneous.

- Now, consider the equation The presence of the constant term $Q(x) = 6$ means that the equation cannot be written in the form $y' + P(x)y = 0.$ Therefore, this equation is *not* homogeneous (i.e., it is *inhomogeneous*).

- Finally, we consider the equation We move the term involving $y$ to the left-hand side so that all $y$-terms are together: This matches the homogeneous form $y' + P(x)y = 0$ with $P(x) = (x-2).$ Therefore, this equation *is* homogeneous.

### Example: Identifying Homogeneous and Inhomogeneous ODEs

#### Question

Which of the following first-order linear differential equations are inhomogeneous?

1. $y' + x^3 y = 0$

2. $y' + x^3 y = x^4$

3. $y' + x^3 y = y$

#### Explanation

A first-order linear differential equation is homogeneous if it can be written in the form

$$


y' + P(x)y = 0.


$$

A first-order linear differential equation is inhomogeneous if it is not homogeneous, i.e., if it can be written as

$$


y' + P(x)y = Q(x)


$$

where $Q$ is not identical to zero.

To determine which equations are inhomogeneous, we examine each one in turn.

- First, we consider the equation Notice that this has the form $y' + P(x)y = 0.$ Therefore, this equation is homogeneous.

- Next, we consider the equation Notice that this is written in the form $y' + P(x)y = Q(x)$ where $Q(x) = x^4$ is not identically zero. Therefore, this equation is inhomogeneous.

- Finally, we consider the equation We collect the $y$-terms on the left side: Since our equation can be written in the form $y' + P(x)y = 0,$ the equation is homogeneous.

Therefore, the correct answer is "II only."
