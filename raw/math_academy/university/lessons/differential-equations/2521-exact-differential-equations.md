# Exact Differential Equations

Source: https://www.mathacademy.com/topics/2521?courseId=61
Topic ID: 2521

## Prerequisites

- [Solving First-Order IVPs Using Separation of Variables](./1179-solving-first-order-ivps-using-separation-of-variables.md)
- [Differentials](../multivariable-calculus/1950-differentials.md)
- [Calculating Potential Functions](../multivariable-calculus/1951-calculating-potential-functions.md)

## Lesson

### Introduction

Recall from multivariable calculus that if we have a function $u(x,y),$ then the **exact derivative** of $u$ is given by

$$


\textrm d u = \dfrac{\partial u}{\partial x}\textrm d x + \dfrac{\partial u}{\partial y}\textrm d y.


$$

An **exact differential equation** is a differential equation whose left-hand side is the exact derivative of some function. That is, for some function $u(x,y),$ the equation can be written as

$$


\textrm d u = 0.


$$

So, for an exact differential equation, we have

$$


\dfrac{\partial u}{\partial x}\textrm d x + \dfrac{\partial u}{\partial y}\textrm d y = 0.


$$

Sometimes, we might be given a differential equation written in **differential form.**

$$


P(x,y)\textrm d x + Q(x,y)\textrm d y = 0


$$

Note that this is equivalent (for $Q\neq 0$) to the equation

$$


\dfrac{\textrm d y}{\textrm d x} = -\dfrac{P(x,y)}{Q(x,y)}.


$$

To determine whether an equation written in differential form is exact, we can use the **exactness test**, which checks whether $P$ and $Q$ could come from the same underlying function $u(x,y).$ Our differential equation is exact if and only if

$$


\dfrac{\partial P}{\partial y} = \dfrac{\partial Q}{\partial x}\,.


$$

We'll justify the exactness test soon, and we'll also learn how to solve these types of equations. But for now, let's get some practice at using the exactness test to determine which differential equations are exact.

### Example: Checking ODEs for Exactness

#### Question

Which of the following differential equations is exact?

1. $(2xy)\,\textrm{d}x + (x^{2}+4)\,\textrm{d}y = 0$

2. $(y^{2}+2x)\,\textrm{d}x + (xy+1)\,\textrm{d}y = 0$

3. $(7y - x)\,\textrm{d}y - (y - 3x)\,\textrm{d}x = 0$

#### Explanation

A differential equation of the form

$$


P(x,y)\textrm{d}x +Q(x,y)\textrm{d}y = 0


$$

is exact if it passes the exactness test, i.e.,

$$


\dfrac{\partial P}{\partial y} = \dfrac{\partial Q}{\partial x}.


$$

Now, let's consider each equation:

- The first equation is Therefore, the functions $P$ and $Q$ are Now, let's compute the partial derivatives: So, Thus, equation I is exact.

- The second equation is Therefore, the functions $P$ and $Q$ are Now, let's compute the partial derivatives: So, Thus, equation II is not exact.

- The third equation is Therefore, the functions $P$ and $Q$ are Now, let's compute the partial derivatives: So, Thus, equation III is exact.

Therefore, the correct answer is "I and III only".

### Example: Identifying Factors Giving an Exact ODE

#### Question

Consider the following differential equation:

$$


-\dfrac{y}{ x^2 } \textrm{d}x + Q(x,y)\textrm{d}y = 0


$$

Given that the differential equation is exact, which of the following functions could be $Q(x,y)?$

1. $\dfrac{1}{x}$

2. $\dfrac{y}{x}$

3. $e^{yx}$

#### Explanation

A differential equation of the form

$$


P(x,y)\textrm{d}x +Q(x,y)\textrm{d}y = 0


$$

is exact if it passes the exactness test,

$$


\dfrac{\partial P}{\partial y} = \dfrac{\partial Q}{\partial x}.


$$

In our case, we're given $P(x,y) = -\dfrac{y}{x^2}.$

First, let's differentiate $P(x,y)$ with respect to $y\mathbin{:}$

$$


\dfrac{\partial P}{\partial y} =\dfrac{\partial}{\partial y}\left(-\dfrac{y}{x^2}\right)=-\dfrac{1}{x^2}


$$

Now, let's apply $\dfrac{\partial}{\partial x}$ to each of the given options and determine whether the results match up with $\dfrac{\partial P}{\partial y}$ above:

- If $Q(x,y) = \dfrac{1}{x},$ then we get an exact equation:

- If $Q(x,y) = \dfrac{y}{x},$ then we do ** get an exact equation:

- If $Q(x,y) = e^{xy},$ then we do ** get an exact equation:

Therefore, the correct answer is "I only".

### General Solutions of Exact ODEs

Remember that if a differential equation

$$


P(x,y)\textrm d x + Q(x,y)\textrm d y = 0


$$

is *exact*, then the left-hand side is the total derivative of some function $u = u(x,y).$ Thus, we can write this equation as

$$


\textrm d u = 0.


$$

This condition means that $u(x,y)$ does not change as we move along a solution curve — its value stays constant. Therefore, solutions trace out the level curves

$$


u(x,y) = c


$$

where $c$ is an arbitrary constant.

Thus, to find $u(x,y),$ we look for a function whose partial derivatives satisfy

$$


\dfrac{\partial u}{\partial x} = P(x,y), \qquad \dfrac{\partial u}{\partial y} = Q(x,y).


$$

Solving an exact equation consists of finding $u(x,y)$ and then setting $u(x,y) = c.$

We will see how to perform this step by step in the next example.

### Example: Solving an Exact Differential Equation

#### Question

Find the general solution of the exact differential equation

$$


(y^2-2x)\,\textrm{d}x + (2xy +1)\textrm{d}y = 0.


$$

#### Explanation

Note that the differential equation is of the form

$$


P(x,y)\textrm{d}x +Q(x,y)\textrm{d}y = 0


$$

where $P(x,y) = y^2-2x$ and $Q(x,y) = 2xy+1.$

Since the equation is exact, our solution $u(x,y)$ must satisfy the following system:

$$


\dfrac{\partial u}{\partial x} = P(x,y),\qquad \dfrac{\partial u}{\partial y} = Q(x,y)


$$

First, we integrate $P(x,y)$ with respect to $x.$ Note that the solution should contain an arbitrary function of $y\mathbin{:}$

$$


\begin{aligned}𝑢(𝑥,𝑦) & =∫𝑃(𝑥,𝑦)\,d𝑥+𝑓(𝑦) \\ & =∫𝑦^{2}−2𝑥\,d𝑥+𝑓(𝑦) \\ & =𝑥𝑦^{2}−𝑥^{2}+𝑓(𝑦)\end{aligned}


$$

Next, we integrate $Q(x,y)$ with respect to $y$. Note that the solution should contain an arbitrary function of $x$.

$$


\begin{aligned}𝑢(𝑥,𝑦) & =∫𝑄(𝑥,𝑦)\,d𝑦+𝑔(𝑥) \\ & =∫2𝑥𝑦+1\,d𝑦+𝑔(𝑥) \\ & =𝑥𝑦^{2}+𝑦+𝑔(𝑥)\end{aligned}


$$

Comparing the two solutions, we see that we must have

$$


g(x) = -x^2, \qquad f(y) = y.


$$

Therefore, the general solution $u(x,y) = c$ is

$$


xy^2-x^2 + y = c.


$$

### Example: Rearranging an ODE Into Exact Form and Then Solving

#### Question

Find the general solution of the differential equation

$$


y' = \frac{11+ye^{xy}}{13y - xe^{xy}}.


$$

#### Explanation

We start by rewriting this equation in differential form.

$$


P(x,y)\textrm{d}x +Q(x,y)\textrm{d}y = 0


$$

Starting from

$$


\begin{aligned}𝑦^{′} & =\frac{d𝑦}{d𝑥} \\ \frac{d𝑦}{d𝑥} & =\frac{11+𝑦𝑒^{𝑥𝑦}}{13𝑦−𝑥𝑒^{𝑥𝑦}},\end{aligned}


$$

we first multiply through by $(13y-xe^{xy})\;\textrm{d}x$:

$$


(13y-xe^{xy})\;\textrm{d}y = (11+ye^{xy})\;\textrm{d}x


$$

Then, we then rearrange the terms:

$$


(11+ye^{xy})\;\textrm{d}x + (xe^{xy}-13y)\;\textrm{d}y = 0


$$

Now, we should check for exactness. A differential equation of the form

$$


P(x,y)\textrm{d}x +Q(x,y)\textrm{d}y = 0


$$

is exact if it passes the exactness test, i.e.,

$$


\dfrac{\partial P}{\partial y} = \dfrac{\partial Q}{\partial x}.


$$

For our differential equation, we have

$$


P(x,y) =11+ye^{xy}, \qquad Q(x,y) = xe^{xy}-13y.


$$

Now, let's compute the partial derivatives:

$$


\begin{aligned}\frac{𝜕𝑃}{𝜕𝑦} & =\frac{𝜕}{𝜕𝑦}(11+𝑦𝑒^{𝑥𝑦}) \\ & =𝑒^{𝑥𝑦}+𝑥𝑦𝑒^{𝑥𝑦}\end{aligned}


$$

$$


\begin{aligned}\frac{𝜕𝑄}{𝜕𝑥} & =\frac{𝜕}{𝜕𝑥}(𝑥𝑒^{𝑥𝑦}−13𝑦) \\ & =𝑒^{𝑥𝑦}+𝑥𝑦𝑒^{𝑥𝑦}\end{aligned}


$$

So,

$$


\frac{\partial P}{\partial y} {=} \frac{\partial Q}{\partial x}. \quad{\color{green}{\checkmark}}


$$

Thus, our equation is exact.

Since the equation is exact, our solution $u(x,y)$ must satisfy the following system:

$$


\dfrac{\partial u}{\partial x} = P(x,y),\qquad \dfrac{\partial u}{\partial y} = Q(x,y)


$$

First, we integrate $P(x,y)$ with respect to $x.$ Note that the solution should contain an arbitrary function of $y \mathbin{:}$

$$


\begin{aligned}𝑢(𝑥,𝑦) & =∫𝑃(𝑥,𝑦)\,d𝑥+𝑓(𝑦) \\ & =∫(11+𝑦𝑒^{𝑥𝑦})\,d𝑥+𝑓(𝑦) \\ & =11𝑥+𝑒^{𝑥𝑦}+𝑓(𝑦)\end{aligned}


$$

Next, we integrate $Q(x,y)$ with respect to $y.$ Note that the solution should contain an arbitrary function of $x \mathbin{:}$

$$


\begin{aligned}𝑢(𝑥,𝑦) & =∫𝑄(𝑥,𝑦)\,d𝑦+𝑔(𝑥) \\ & =∫(𝑥𝑒^{𝑥𝑦}−13𝑦)\,d𝑦+𝑔(𝑥) \\ & =𝑒^{𝑥𝑦}−\frac{13}{2}𝑦^{2}+𝑔(𝑥)\end{aligned}


$$

Comparing the two solutions, we see that we must have

$$


g(x) = 11x, \quad f(y) = - \dfrac{13}{2}y^2.


$$

Therefore, the general solution $u(x,y) = c$ is

$$


e^{xy} - \dfrac{13}{2}y^2 + 11x = c.


$$

### Justifying the Exactness Test

So far in this lesson, we have been using the exactness test, which states that a differential equation

$$


P(x,y)\textrm d x + Q(x,y)\textrm d y = 0


$$

is exact if and only if

$$


\dfrac{\partial P}{\partial y} = \dfrac{\partial Q}{\partial x}\,.


$$

Now, let's explain why this test works.

The reason this test works lies in the very definition of an exact equation. An exact differential equation must come from a single function $u(x,y).$ The equation itself is simply the total differential of this function set to zero

$$


\dfrac{\partial u}{\partial x}\textrm d x + \dfrac{\partial u}{\partial y}\textrm d y = 0,


$$

where $u = u(x,y) = c$ is the solution.

By comparing the terms of our original ODE with the total differential, we immediately see how $P$ and $Q$ must be defined in terms of $u:$

$$


P = \dfrac{\partial u}{\partial x}\qquad \textrm{and}\qquad Q = \dfrac{\partial u}{\partial y}


$$

To derive the exactness condition, we take the partial derivative of $P$ with respect to $y$ and the partial derivative of $Q$ with respect to $x$. This requires us to look at the second-order partial derivatives of the function $u$:

$$


\begin{aligned}\frac{𝜕𝑃}{𝜕𝑦} & =\frac{𝜕}{𝜕𝑦}\frac{𝜕𝑢}{𝜕𝑥} \\ & =\frac{𝜕^{2}𝑢}{𝜕𝑦𝜕𝑥} \\ & =\frac{𝜕^{2}𝑢}{𝜕𝑥𝜕𝑦} \\ & =\frac{𝜕}{𝜕𝑥}\frac{𝜕𝑢}{𝜕𝑦} \\ & =\frac{𝜕𝑄}{𝜕𝑥}\end{aligned}


$$

Thus, the exactness test condition is equivalent to the equality of the mixed second partial derivatives of the function $u.$

Notice that we assumed the equality of the mixed partials, meaning that $\dfrac{\partial^2 u}{\partial y\partial x}=\dfrac{\partial^2 u}{\partial x\partial y}.$ This requires that $\dfrac{\partial^2 u}{\partial y\partial x}$ and $\dfrac{\partial^2 u}{\partial x\partial y}$ both exist and are continuous, which is true for almost all of the functions that we'll come across.
