# Solving Second-Order ODEs With Time-Delayed Forcing Using Laplace Transforms

Source: https://www.mathacademy.com/topics/6728?courseId=155
Topic ID: 6728

## Prerequisites

- [Solving Second-Order ODEs Using Laplace Transforms](./2540-solving-second-order-odes-using-laplace-transforms.md)
- [Solving First-Order ODEs With Time-Delayed Forcing Using Laplace Transforms](./6718-solving-first-order-odes-with-time-delayed-forcing-using-laplace-transforms.md)

## Lesson

### Introduction

In previous lessons, we solved second-order initial value problems using Laplace transforms when the forcing term was an ordinary function of $t.$

In this lesson, we extend the same method to **time-delayed forcing**, where the right-hand side turns on at a specific time. This type of forcing is modeled using the **unit step function**.

For a fixed constant $a>0,$ we write

$$


u_a(t) = u(t-a),


$$

which represents a signal that is zero for $t< a$ and turns on at $t = a.$ For example, $u(t-3)$ remains zero until $t=3,$ at which point it jumps to $1.$

When a second-order differential equation includes a term involving $u_a(t),$ we still begin by taking the Laplace transform of both sides and solving for $Y(s)=\mathcal L\{y(t)\}$ (for $s>0$). The left-hand side is handled exactly as before, using the Laplace transforms of derivatives and the given initial conditions.

The main new idea is how the unit step function affects the transform of the forcing term. We will see how to account for this delay and how it changes the algebraic equation for $Y(s).$ To do this, we first need to determine the transform of the step function itself. Let's find some Laplace transforms.

### A Worked Example

Consider a second-order initial value problem with step function forcing, such as

$$


y'' + y = u_2(t), \qquad y(0)=0,\qquad y'(0)=0,


$$

where $u_2(t)=u(t-2)$ is the unit step function.

**Step 1: Transform the left-hand side.**

We begin by taking the Laplace transform of both sides. Let $Y(s)=\mathcal L\{y(t)\}.$ Using the formula for the second derivative and the initial conditions, we have

$$


\mathcal L\{y''\}=s^2Y(s)-sy(0)-y'(0) = s^2Y(s).


$$

**Step 2: Transform the right-hand side.**

From the table of Laplace transforms, the unit step function satisfies

$$


\mathcal L\{u_2(t)\}=\frac{e^{-2s}}{s},


$$

which is valid for $s>0.$

**Step 3: Solve for $Y(s).$**

Substituting these results into the transformed equation gives

$$


s^2Y(s)+Y(s)=\frac{e^{-2s}}{s}.


$$

We now collect terms and solve algebraically for $Y(s){:}$

$$


\begin{aligned}(𝑠^{2}+1)𝑌(𝑠) & =\frac{𝑒^{−2𝑠}}{𝑠} \\ 𝑌(𝑠) & =\frac{𝑒^{−2𝑠}}{𝑠(𝑠^{2}+1)}\end{aligned}


$$

Aside from the exponential factor $e^{-2s},$ the steps are exactly the same as in problems without time delay.

### Example: Finding the Laplace Transform of a Second-Order ODE With Step Function Forcing

#### Question

Find the Laplace transform of $y(t),$ if

$$


y''+ y = u_1(t), \quad y(0)=0, \quad y'(0)=0,


$$

where $u_1(t)=u(t-1)$ is the unit step function.

#### Explanation

First, we take the Laplace transform of both sides and use the addition property of the Laplace transform:

$$


\begin{aligned}L{𝑦^{″}+𝑦} & =L{𝑢_{1}(𝑡)} \\ L{𝑦^{″}}+L{𝑦} & =L{𝑢_{1}(𝑡)}\end{aligned}


$$

Let's introduce $\mathcal{L}\left\{y \right\}=Y(s).$

To calculate $\mathcal L\left\{y''\right\},$ we use the formula for the Laplace transform of a second derivative:

$$


\mathcal{L}\left\{y'' \right\} = s^2 \mathcal{L}\{ y \} - s y(0) - y'(0) = s^2 Y(s) - s y(0) - y'(0)


$$

Taking into account the given initial conditions, we get

$$


\mathcal{L}\left\{y''\right\} = s^2 Y(s).


$$

From the table of Laplace transforms, we have the following result:

$$


\mathcal{L}\left\{ u_1(t) \right\} = \dfrac{e^{-s}}{s}


$$

Therefore, we can solve for $Y(s)\mathbin{:}$

$$


\begin{aligned}L{𝑦^{″}}+L{𝑦} & =L{𝑢_{1}(𝑡)} \\ 𝑠^{2}𝑌(𝑠)+𝑌(𝑠) & =\frac{𝑒^{−𝑠}}{𝑠} \\ (𝑠^{2}+1)𝑌(𝑠) & =\frac{𝑒^{−𝑠}}{𝑠} \\ 𝑌(𝑠) & =\frac{𝑒^{−𝑠}}{𝑠(𝑠^{2}+1)}\end{aligned}


$$

### Time-Delayed Forcing and the Second Shifting Theorem

In the first-order case, we saw that a time delay in the forcing term appears in the $s$-domain as a factor of $e^{-as},$ and that we can handle this using the second shifting theorem.

The same idea applies when working with **second-order** differential equations.

Consider the initial value problem

$$


y'' + 4y = 7u_2(t)e^{-2(t-2)}, \qquad y(0)=0,\qquad y'(0)=0,


$$

where $u_2(t)=u(t-2)$ is the unit step function.

Again, we begin by taking the Laplace transform of both sides and writing

$$


Y(s)=\mathcal L\{y(t)\}.


$$

Using the initial conditions, the left-hand side becomes

$$


\mathcal L\{y''\}+4\mathcal L\{y\}=s^2Y(s)+4Y(s).


$$

The forcing term has the form

$$


u_2(t)\,f(t-2),


$$

where

$$


f(t-2)=7e^{-2(t-2)} \quad\text{and}\quad f(t)=7e^{-2t}.


$$

As in the first-order case, we apply the **second shifting theorem**. That is, if

$$


F(s)=\mathcal L\{f(t)\},


$$

then

$$


\mathcal L\{u(t-a)\cdot f(t-a)\}=e^{-as}F(s),


$$

which is valid for $s>0.$

Here, using $a=2,$ we have

$$


F(s)=\mathcal L\{7e^{-2t}\}=\frac{7}{s+2},


$$

so the transformed forcing term is

$$


\mathcal L\{7u_2(t)e^{-2(t-2)}\} = e^{-2s}\cdot\frac{7}{s+2}.


$$

Substituting into the transformed differential equation gives

$$


s^2Y(s)+4Y(s)=\frac{7e^{-2s}}{s+2}.


$$

We now solve algebraically for $Y(s){:}$

$$


\begin{aligned}(𝑠^{2}+4)𝑌(𝑠) & =\frac{7𝑒^{−2𝑠}}{𝑠+2} \\ 𝑌(𝑠) & =\frac{7𝑒^{−2𝑠}}{(𝑠+2)(𝑠^{2}+4)}\end{aligned}


$$

Just as in the first-order case, the delay introduces the factor $e^{-as}.$ Once this factor is identified, the remaining steps follow the same algebraic process used for second-order equations without time delay.

### Example: Finding the Laplace Transform of a Second-Order ODE With Time-Delayed Forcing

#### Question

Find the Laplace transform $Y(s) = \mathcal L\{y(t)\}$ if

$$


y'' + 25y = 6u_2(t)\sin(5(t-2)), \quad y(0)=0, \quad y'(0)=0,


$$

where $u_2(t)=u(t-2)$ is the unit step function.

#### Explanation

First, we take the Laplace transform of both sides and use the addition and scalar multiplication properties of the Laplace transform:

$$


\begin{aligned}L{𝑦^{″}+25𝑦} & =L{6𝑢_{2}(𝑡)sin⁡(5(𝑡−2))} \\ L{𝑦^{″}}+25L{𝑦} & =L{6𝑢_{2}(𝑡)sin⁡(5(𝑡−2))}\end{aligned}


$$

To calculate $\mathcal L\left\{y'' \right\},$ we use the formula for the Laplace transform of a second derivative and the initial conditions $y(0)=0$ and $y'(0)=0$:

$$


\mathcal{L}\left\{y'' \right\} = s^2Y(s) - sy(0) - y'(0) = s^2Y(s)


$$

For the right-hand side, we use the second shifting theorem:

$$


\mathcal{L}\{u(t-a)f(t-a)\} = e^{-as}F(s)


$$

Here, $a=2$ and $f(t-2) = 6\sin(5(t-2))$, so $f(t) = 6\sin(5t).$ The transform of $f(t)$ is

$$


F(s) = \mathcal{L}\{6\sin(5t)\} = 6 \cdot \frac{5}{s^2+5^2} = \frac{30}{s^2+25}.


$$

Applying the shift, we get

$$


\mathcal{L}\{6u_2(t)\sin(5(t-2))\} = e^{-2s} \cdot \frac{30}{s^2+25} = \frac{30e^{-2s}}{s^2+25}.


$$

Substituting these into the differential equation:

$$


\begin{aligned}𝑠^{2}𝑌(𝑠)+25𝑌(𝑠) & =\frac{30𝑒^{−2𝑠}}{𝑠^{2}+25} \\ (𝑠^{2}+25)𝑌(𝑠) & =\frac{30𝑒^{−2𝑠}}{𝑠^{2}+25} \\ 𝑌(𝑠) & =\frac{30𝑒^{−2𝑠}}{(𝑠^{2}+25)^{2}}\end{aligned}


$$

### Solving for the Laplace Transform With Step Function Forcing

Once the Laplace transform has been found, solving a second-order initial value problem with step function forcing follows the same overall strategy as before: we take the inverse Laplace transform.

The key difference is handling terms that include a factor of $e^{-as}$.

Consider the initial value problem

$$


y'' + y = u_2(t), \qquad y(0)=0,\qquad y'(0)=0,


$$

where $u_2(t)=u(t-2)$ is the unit step function.

We previously found the Laplace transform

$$


Y(s)=e^{-2s}\cdot\frac{1}{s(s^2+1)}.


$$

To take the inverse Laplace transform, we first focus on the *base function*

$$


F(s)=\frac{1}{s(s^2+1)}.


$$

Using partial fraction decomposition, we write

$$


\frac{1}{s(s^2+1)}=\frac{1}{s}-\frac{s}{s^2+1}.


$$

Now we compute the inverse transform of $F(s)$ and call it $f(t){:}$

$$


f(t) = \mathcal L^{-1}\!\left\{\frac{1}{s}-\frac{s}{s^2+1}\right\} = 1-\cos t.


$$

Next, we apply the **second shifting theorem**. Since $Y(s)=e^{-2s}F(s)$, we have

$$


\mathcal L^{-1}\{e^{-2s}F(s)\} = u(t-2)\cdot f(t-2).


$$

Substituting our result for $f(t)$, the solution to the initial value problem is

$$


y(t)=u(t-2)\left(1-\cos(t-2)\right).


$$

The important idea is that once the exponential factor $e^{-as}$ has been identified, we first find the inverse transform of the base function, then shift the result and multiply by the unit step function.

### Example: Solving a Second-Order Initial Value Problem With Step Function Forcing

#### Question

Find the solution $y(t)$ given that the Laplace transform of the initial value problem

$$


y''(t) + y(t) = u_2(t), \qquad y(0) = 0, \qquad y'(0)=0


$$

is given by

$$


s^2Y(s) + Y(s) = \dfrac{e^{-2s}}{s}.


$$

#### Explanation

Using the transformed equation, we solve for $Y(s)$:

$$


\begin{aligned}(𝑠^{2}+1)𝑌(𝑠) & =\frac{𝑒^{−2𝑠}}{𝑠} \\ 𝑌(𝑠) & =𝑒^{−2𝑠}⋅\frac{1}{𝑠(𝑠^{2}+1)}\end{aligned}


$$

To find the inverse transform, we first use partial fraction decomposition on the algebraic part:

$$


\dfrac{1}{s(s^2+1)} = \dfrac{A}{s} + \dfrac{Bs+C}{s^2+1}


$$

Solving for the constants, we find $A=1$, $B=-1$, and $C=0$, giving:

$$


\dfrac{1}{s(s^2+1)} = \dfrac{1}{s} - \dfrac{s}{s^2+1}


$$

Now, we apply the inverse Laplace transform. Let

$$


F(s) = \frac{1}{s} - \frac{s}{s^2+1},


$$

then, we have

$$


f(t) = 1 - \cos(t).


$$

According to the second shifting theorem,

$$


\mathcal{L}^{-1}\{e^{-as}F(s)\} = u_a(t)f(t-a).


$$

Thus, we have

$$


\begin{aligned}𝑦(𝑡) & =L^{−1}{𝑒^{−2𝑠}(\frac{1}{𝑠}−\frac{𝑠}{𝑠^{2}+1})} \\ 𝑦(𝑡) & =𝑢_{2}(𝑡)(1−cos⁡(𝑡−2))\end{aligned}


$$

$$


y(t) = u(t-2)\left(1-\cos(t-2)\right).


$$
