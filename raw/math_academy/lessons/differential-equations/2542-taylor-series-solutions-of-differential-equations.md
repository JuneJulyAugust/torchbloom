# Taylor Series Solutions of Differential Equations

Source: https://www.mathacademy.com/topics/2542?courseId=61
Topic ID: 2542

## Prerequisites

- [Differentiating Taylor Series](../ap-calculus-bc/36-differentiating-taylor-series.md)
- [Introduction to Second-Order Linear ODEs](./2548-introduction-to-second-order-linear-odes.md)

## Lesson

### Introduction

We can use Taylor series to approximate the solution to a differential equation. For example, let's find a series solution about $x=0,$ in ascending powers of $x$ up to and including the term in $x^3,$ of the initial value problem

$$


y''=x+y, \qquad y(0)=2, \quad y'(0)=3.


$$

We start by writing the form of the Taylor series of $y(x)$ about $x=0\mathbin{:}$

$$


y(x) = y(0) + xy'(0) + \dfrac{x^2}{2!}y''(0) + \dfrac{x^3}{3!}y^{(3)}(0)+\cdots


$$

We're given $y(0)$ and $y'(0),$ so we need to calculate $y''(0)$ and $y^{(3)}(0).$

- We know that $y(0)=2,$ so we substitute this into the given equation to find $y''(0)\mathbin{:}$

- Next, to find an expression for $y^{(3)}(x),$ we differentiate both sides on the given equation with respect to $x\mathbin{:}$ We can now find $y^{(3)}(0)$ by substituting in the known values:

Finally, we substitute the obtained values in the Taylor series:

$$


\begin{aligned}𝑦(𝑥) & =𝑦(0)+𝑥𝑦^{′}(0)+\frac{𝑥^{2}}{2!}𝑦^{″}(0)+\frac{𝑥^{3}}{3!}𝑦^{(3)}(0)+⋯ \\ & =2+𝑥⋅3+\frac{𝑥^{2}}{2!}⋅2+\frac{𝑥^{3}}{3!}⋅4+⋯ \\ & =2+3𝑥+𝑥^{2}+\frac{2𝑥^{3}}{3}+⋯\end{aligned}


$$

### Example: Finding a Series Solution to a Second-Order Initial Value Problem About Zero

#### Question

Use the Taylor series method to find a series solution about $x=0,$ in ascending powers of $x$ up to and including the term in $x^3,$ of the initial value problem

$$


y''=y+e^{-4x}, \qquad y(0)=0, \quad y'(0)=2.


$$

#### Explanation

We wish to express $y(x)$ as a Taylor series about $x=0\mathbin{:}$

$$


y(x) = y(0) + xy'(0) + \dfrac{x^2}{2!}y''(0) + \dfrac{x^3}{3!}y^{(3)}(0)+\cdots


$$

We're given $y(0)$ and $y'(0),$ so we need to calculate $y''(0)$ and $y^{(3)}(0).$

- We know that $y(0)=0,$ so we substitute this into the given equation to find $y''(0)\mathbin{:}$

- Next, to find an expression for $y^{(3)}(x),$ we differentiate both sides on the given equation with respect to $x\mathbin{:}$ We can now find $y^{(3)}(0)$ by substituting in the known values:

Finally, we substitute the obtained values in the Taylor series:

$$


\begin{aligned}𝑦(𝑥) & =𝑦(0)+𝑥𝑦^{′}(0)+\frac{𝑥^{2}}{2!}𝑦^{″}(0)+\frac{𝑥^{3}}{3!}𝑦^{(3)}(0)+⋯ \\ & =0+𝑥⋅2+\frac{𝑥^{2}}{2!}⋅1+\frac{𝑥^{3}}{3!}⋅(−2)+⋯ \\ & =2𝑥+\frac{𝑥^{2}}{2}−\frac{𝑥^{3}}{3}+⋯\end{aligned}


$$

### Example: Finding a Series Solution to a Second-Order Initial Value Problem About a Non-Zero Point

#### Question

Use the Taylor series method to find a series solution about $x=2$, in ascending powers of $(x-2)$ up to and including the term in $(x-2)^3,$ of the initial value problem

$$


y''=y-2xy', \qquad y(2)=0, \quad y'(2)=1.


$$

#### Explanation

We wish to express $y(x)$ as a Taylor series about $x=2\mathbin{:}$

$$


y(x) = y(2) + (x-2)y'(2) + \dfrac{(x-2)^2}{2!}y''(2) + \dfrac{(x-2)^3}{3!}y^{(3)}(2)+\cdots


$$

We're given $y(2)$ and $y'(2),$ so we need to calculate $y''(2)$ and $y^{(3)}(2).$

- We substitute $y(2)=0$ and $y'(2)=1$ into the given equation to find $y''(2)\mathbin{:}$

- Next, to find an expression for $y^{(3)}(x),$ we differentiate both sides on the given equation with respect to $x\mathbin{:}$ We can now find $y^{(3)}(2)$ by substituting in the known values:

Finally, we substitute the obtained values in the Taylor series:

$$


\begin{aligned}𝑦(𝑥) & =𝑦(2)+(𝑥−2)𝑦^{′}(2)+\frac{(𝑥−2)^{2}}{2!}𝑦^{″}(2)+\frac{(𝑥−2)^{3}}{3!}𝑦^{(3)}(2)+⋯ \\ & =0+(𝑥−2)⋅1+\frac{(𝑥−2)^{2}}{2}⋅(−4)+\frac{(𝑥−2)^{3}}{6}⋅15+… \\ & =(𝑥−2)−2(𝑥−2)^{2}+\frac{5(𝑥−2)^{3}}{2}+⋯\end{aligned}


$$

### Example: Finding a Series Solution to a First-Order Initial Value Problem

#### Question

Use the Taylor series method to find a series solution about $x=0,$ in ascending powers of $x$ up to and including the term in $x^3,$ of the initial value problem

$$


y'=2x-y \cos x, \qquad y(0)=4.


$$

#### Explanation

We wish to express $y(x)$ as a Taylor series about $x=0\mathbin{:}$

$$


y(x) = y(0) + xy'(0) + \dfrac{x^2}{2!}y''(0) + \dfrac{x^3}{3!}y^{(3)}(0)+\cdots


$$

We're given $y(0),$ so we need to calculate $y'(0),$ $y''(0),$ and $y^{(3)}(0).$

- We know that $y(0)=4,$ so we substitute this into the given equation to find $y'(0)\mathbin{:}$

- Next, to find an expression for $y''(x),$ we differentiate both sides on the given equation with respect to $x\mathbin{:}$ We can now find $y''(0)$ by substituting in the known values:

- To find an expression for $y^{(3)}(x),$ we differentiate $y''(x)$ with respect to $x\mathbin{:}$ We can now find $y^{(3)}(0)$ by substituting in the known values:

Finally, we substitute the obtained values in the Taylor series:

$$


\begin{aligned}𝑦(𝑥) & =𝑦(0)+𝑥𝑦^{′}(0)+\frac{𝑥^{2}}{2!}𝑦^{″}(0)+\frac{𝑥^{3}}{3!}𝑦^{(3)}(0)+⋯ \\ & =4+𝑥⋅(−4)+\frac{𝑥^{2}}{2}⋅6+\frac{𝑥^{3}}{6}⋅(−2)+⋯ \\ & =4−4𝑥+3𝑥^{2}−\frac{𝑥^{3}}{3}+⋯\end{aligned}


$$
