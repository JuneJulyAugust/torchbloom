# Solving First-Order ODEs With Time-Delayed Forcing Using Laplace Transforms

Source: https://www.mathacademy.com/topics/6718?courseId=155
Topic ID: 6718

## Prerequisites

- [Solving First-Order ODEs Using Laplace Transforms](./2531-solving-first-order-odes-using-laplace-transforms.md)
- [The Second Shifting Theorem of Laplace Transforms](./6370-the-second-shifting-theorem-of-laplace-transforms.md)

## Lesson

### Introduction

In this topic, we will use Laplace transforms to handle **time-delayed forcing**, where the forcing function turns on at some time $t=a>0$.

We represent this “turning on” using the **unit step function** $u_a(t)=u(t-a)$.

To see what this looks like, consider the initial value problem

$$


y' - 4y = u_2(t)\cdot e^{t-2}, \qquad y(0)=0.


$$

Here, the forcing is $0$ for $t<2$ and becomes $e^{t-2}$ for $t\ge 2$.

To find the Laplace transform of the forcing term, we note that

$$


u_2(t)\cdot e^{t-2}


$$

is in the form $u(t-a)\cdot f(t)$ where $a=2$ and $f(t)=e^{t-2}.$

Now, recall that the **second shifting theorem** (time-shifting property) states

$$


\mathcal L\{u(t-a)\cdot f(t)\} = e^{-as} \cdot \mathcal L\{f(t+a)\}.


$$

So, by the second shifting theorem, we have

$$


\begin{aligned}L{𝑢(𝑡−2)⋅𝑒^{𝑡−2}} & =𝑒^{−2𝑠}⋅L{𝑒^{(𝑡+2)−2}} \\ & =𝑒^{−2𝑠}⋅L{𝑒^{𝑡}} \\ & =𝑒^{−2𝑠}⋅\frac{1}{𝑠−1}.\end{aligned}


$$

After this step, we proceed as usual: we take the Laplace transform of the entire differential equation, solve for $Y(s)=\mathcal L\{y(t)\}$, and then (when needed) take $\mathcal L^{-1}$ to recover $y(t)$.

### A Worked Example

Suppose we wish to solve the initial value problem

$$


y' - 4y = u_2(t)\cdot e^{t-2}, \qquad y(0)=0,


$$

where $u_2(t)=u(t-2)$ is the unit step function.

First, we take the Laplace transform of both sides and use the linearity properties of the Laplace transform:

$$


\begin{aligned}L{𝑦^{′}−4𝑦} & =L{𝑢_{2}(𝑡)⋅𝑒^{𝑡−2}} \\ L{𝑦^{′}}−4L{𝑦} & =L{𝑢_{2}(𝑡)⋅𝑒^{𝑡−2}}.\end{aligned}


$$

To compute $\mathcal L\{y'\},$ we use the derivative formula and the initial condition $y(0)=0{:}$

$$


\mathcal L\{y'\} = sY(s) - y(0) = sY(s).


$$

To compute the right-hand side, we note that

$$


u_2(t)\cdot e^{t-2}


$$

is in the form $u(t-a)\cdot f(t)$ where $a=2$ and $f(t)=e^{t-2}.$

Now, recall that the **second shifting theorem** (time-shifting property) states

$$


\mathcal L\{u(t-a)\cdot f(t)\}=e^{-as}\cdot \mathcal L\{f(t+a)\}.


$$

So, by the second shifting theorem, we have

$$


\begin{aligned}L{𝑢(𝑡−2)⋅𝑒^{𝑡−2}} & =𝑒^{−2𝑠}⋅L{𝑒^{(𝑡+2)−2}} \\ & =𝑒^{−2𝑠}⋅L{𝑒^{𝑡}} \\ & =𝑒^{−2𝑠}⋅\frac{1}{𝑠−1} \\ & =\frac{𝑒^{−2𝑠}}{𝑠−1}.\end{aligned}


$$

Finally, we substitute these back into our transformed differential equation and solve for $Y(s){:}$

$$


\begin{aligned}𝑠𝑌(𝑠)−4𝑌(𝑠) & =\frac{𝑒^{−2𝑠}}{𝑠−1} \\ (𝑠−4)𝑌(𝑠) & =\frac{𝑒^{−2𝑠}}{𝑠−1} \\ 𝑌(𝑠) & =\frac{𝑒^{−2𝑠}}{(𝑠−1)(𝑠−4)}.\end{aligned}


$$

Taking the inverse Laplace transform of $Y(s)$ will give us the solution to our initial value problem.

### Example: Laplace Transforms of First-Order Linear ODEs With Time-Delayed (Discontinuous) Forcing

#### Question

Find the Laplace transform $Y(s) = \mathcal L\{y(t)\}$ if

$$


y' - 3y = 2u_{\pi/2}(t)\cdot \sin\!\left(2t-\pi\right)\,, \qquad y(0)=-2,


$$

where $u_{\pi/2}(t)=u\!\left(t-\dfrac{\pi}{2}\right)$ is the unit step function.

You may make use of the following result:

$$


\mathcal L\{\sin\omega t\} = \dfrac{\omega}{s^2+\omega^2}, \qquad s > 0


$$

#### Explanation

First, we take the Laplace transform of both sides and use the addition and scalar multiplication properties of the Laplace transform:

$$


\begin{aligned}L{𝑦^{′}−3𝑦} & =L{2𝑢_{𝜋/2}(𝑡)⋅sin\,(2𝑡−𝜋)} \\ L{𝑦^{′}}−3L{𝑦} & =L{2𝑢_{𝜋/2}(𝑡)⋅sin\,(2𝑡−𝜋)}\end{aligned}


$$

To calculate $\mathcal L\left\{y' \right\},$ we use the formula for the Laplace transform of a derivative and the initial condition $y(0)=-2\mathbin{:}$

$$


\mathcal{L}\left\{y' \right\} = sY(s) - y(0) = sY(s) + 2


$$

To find the transform of the right-hand side, we note that the term

$$


2u_{\pi/2}(t)\cdot \sin\!\left(2t-\pi\right)


$$

is in the form $u(t-a)\cdot f(t)$ where $a=\dfrac{\pi}{2}$ and $f(t)=2\sin(2t-\pi).$ This can be interpreted as time-delayed sinusoidal forcing.

Now, recall that the second shifting theorem (time-shifting property) states

$$


\mathcal L\{u(t-a)\cdot f(t)\} = e^{-as} \cdot \mathcal L\{f(t+a)\}.


$$

So, by the second shifting theorem, we have

$$


\begin{aligned}L{𝑢\,(𝑡−\frac{𝜋}{2})⋅2sin⁡(2𝑡−𝜋)} & =𝑒^{−(𝜋/2)𝑠}⋅L{2sin\,(2\,(𝑡+\frac{𝜋}{2})−𝜋)} \\ & =𝑒^{−(𝜋/2)𝑠}⋅L{2sin⁡(2𝑡)} \\ & =𝑒^{−(𝜋/2)𝑠}⋅2⋅\frac{2}{𝑠^{2}+4} \\ & =\frac{4𝑒^{−𝜋𝑠/2}}{𝑠^{2}+4}.\end{aligned}


$$

Finally, we substitute these back into our transformed differential equation:

$$


\begin{aligned}L{𝑦^{′}}−3L{𝑦} & =L{2𝑢_{𝜋/2}(𝑡)sin⁡(2𝑡−𝜋)} \\ (𝑠𝑌(𝑠)+2)−3𝑌(𝑠) & =\frac{4𝑒^{−𝜋𝑠/2}}{𝑠^{2}+4} \\ (𝑠−3)𝑌(𝑠)+2 & =\frac{4𝑒^{−𝜋𝑠/2}}{𝑠^{2}+4} \\ (𝑠−3)𝑌(𝑠) & =−2+\frac{4𝑒^{−𝜋𝑠/2}}{𝑠^{2}+4} \\ 𝑌(𝑠) & =−\frac{2}{𝑠−3}+\frac{4𝑒^{−𝜋𝑠/2}}{(𝑠^{2}+4)(𝑠−3)}\end{aligned}


$$

### Taking the Inverse Transform and Applying the Second Shifting Theorem

When working with time-delayed forcing, a delay often appears in the $s$-domain as a factor of $e^{-as}$.

Suppose $F(s)=\mathcal L\{f(t)\}.$ Then the second shifting theorem can be written as

$$


\mathcal L\{u(t-a)\cdot f(t-a)\} = e^{-as}\,F(s), \qquad a>0.


$$

Equivalently, we can read this rule *backwards* as an inverse Laplace transform statement:

$$


\mathcal L^{-1}\{e^{-as}F(s)\}=u(t-a)\cdot f(t-a), \qquad a>0.


$$

So, if $Y(s)$ contains a term like $e^{-as}F(s)$, we can handle it using the following steps.

- **Step 1:** Compute $f(t)=\mathcal L^{-1}\{F(s)\}$.

- **Step 2:** Shift the function by replacing $t$ with $(t-a)$.

- **Step 3:** Multiply by the unit step function $u(t-a)$.

We consider the concrete example below.

### A Worked Example

Consider the following initial value problem:

$$


y' + 3y = u_\pi(t)\cdot \cos(t-\pi)\,, \qquad y(0)=2,


$$

where $u_\pi(t)=u(t-\pi)$ is the unit step function.

Assume we are given that the Laplace transform $Y(s) = \mathcal L\{y(t)\}$ is

$$


Y(s) = \dfrac{2}{s+3} + \dfrac{s\,e^{-\pi s}}{(s^2+1)(s+3)}


$$

and that the solution to the initial value problem can be expressed as

$$


y(t) = 2e^{-3t} + \dfrac{1}{10} u(t-\pi)\cdot g(t).


$$

Our goal is to find the function $g(t).$ To do this, we'll need to compute the inverse Laplace transform of the second term in $Y(s).$ We can use the following standard results:

$$


\mathcal L\{\sin\omega t\} = \dfrac{\omega}{s^2+\omega^2}, \qquad \mathcal L\{\cos\omega t\} = \dfrac{s}{s^2+\omega^2}, \qquad s > 0.


$$

We focus on the term with the exponential $e^{-\pi s}$ and identify its rational function part:

$$


F(s) = \dfrac{s}{(s^2+1)(s+3)}.


$$

We'll find the inverse transform in three steps.

**Step 1. Partial fraction decomposition**

To handle the rational function $F(s),$ we use *partial fraction decomposition*. Since the denominator contains a linear factor $(s+3)$ and an irreducible quadratic factor $(s^2+1),$ the decomposition takes the form

$$


\dfrac{s}{(s^2+1)(s+3)} = \dfrac{A}{s+3} + \dfrac{Bs+C}{s^2+1}.


$$

To find the constants, we clear the denominators:

$$


s = A(s^2+1) + (Bs+C)(s+3).


$$

Now, we find the constants $A, B,$ and $C.$

- Setting $s=-3,$ we have

- Comparing the coefficients of $s^2,$ we have

- Comparing the coefficients of $s,$ we have Thus, we can rewrite $F(s)$ as

**Step 2. Finding the inverse of the base function**

We find the inverse transform $f(t) = \mathcal L^{-1}\{F(s)\}$ using standard transforms:

$$


\begin{aligned}𝑓(𝑡) & =L^{−1}{−\frac{3}{10}⋅\frac{1}{𝑠+3}+\frac{3}{10}⋅\frac{𝑠}{𝑠^{2}+1}+\frac{1}{10}⋅\frac{1}{𝑠^{2}+1}} \\ & =−\frac{3}{10}𝑒^{−3𝑡}+\frac{3}{10}cos⁡𝑡+\frac{1}{10}sin⁡𝑡 \\ & =\frac{1}{10}(−3𝑒^{−3𝑡}+3cos⁡𝑡+sin⁡𝑡).\end{aligned}


$$

**Step 3. Applying the time-shifting property**

Finally, we use the *second shifting theorem* to handle the $e^{-\pi s}$ factor. The theorem states:

$$


\mathcal L^{-1} \{ e^{-as}F(s) \} = u(t-a) \cdot f(t-a).


$$

In our case, $a=\pi.$ Therefore, we shift $f(t)$ by replacing every instance of $t$ with $(t-\pi):$

$$


\begin{aligned}𝑢(𝑡−𝜋)𝑓(𝑡−𝜋) & =𝑢(𝑡−𝜋)⋅\frac{1}{10}[−3𝑒^{−3(𝑡−𝜋)}+3cos⁡(𝑡−𝜋)+sin⁡(𝑡−𝜋)] \\ & =\frac{1}{10}𝑢(𝑡−𝜋)⋅[−3𝑒^{−3(𝑡−𝜋)}+3(−cos⁡𝑡)+(−sin⁡𝑡)]\end{aligned}


$$

Using the trigonometric identities $\cos(t-\pi)=-\cos t$ and $\sin(t-\pi)=-\sin t,$ we simplify:

$$


u(t-\pi)f(t-\pi) = \dfrac{1}{10}u(t-\pi)\cdot \left(-3e^{-3(t-\pi)} - 3\cos t - \sin t\right).


$$

**Conclusion: Identifying g(t)**

This result is the inverse transform of the second term in $Y(s).$ The problem statement gives the complete solution in the form

$$


y(t) = 2e^{-3t} + \dfrac{1}{10} u(t-\pi)\cdot g(t).


$$

The first term, $2e^{-3t},$ is the inverse transform of $\dfrac{2}{s+3}.$ By comparing our calculated term with the form above, we can identify **$g(t)$**:

$$


g(t)= -3e^{-3(t-\pi)} - 3\cos t - \sin t.


$$

### Example: Solving a First-Order Initial Value Problem Using a Laplace Transform

#### Question

Consider the following initial value problem:

$$


y' + 4y = u_3(t)\cdot (t-3)\,, \qquad y(0)=-2,


$$

where $u_3(t)=u(t-3)$ is the unit step function.

You're given that the Laplace transform $Y(s) = \mathcal L\{y(t)\}$ is

$$


Y(s) = -\dfrac{2}{s+4} + \dfrac{e^{-3s}}{s^2(s+4)}


$$

and that the solution to the initial value problem can be expressed as

$$


y(t) = -2e^{-4t} + u(t-3)\cdot g(t).


$$

Find the function $g(t).$

#### Explanation

To find the function $g(t),$ we need to compute the inverse Laplace transform of the term containing the time delay in $Y(s).$

We focus on the term with the exponential $e^{-3s}$ (which corresponds to the step function in the time domain) and identify the rational function part:

$$


F(s) = \dfrac{1}{s^2(s+4)}.


$$

We'll solve this in three steps.

**** Partial fraction decomposition

Since the denominator contains a linear factor $(s+4)$ and a repeated linear factor $s^2,$ the decomposition takes the form

$$


\dfrac{1}{s^2(s+4)} = \dfrac{A}{s} + \dfrac{B}{s^2} + \dfrac{C}{s+4}.


$$

To find the constants, we clear the denominators:

$$


1 = As(s+4) + B(s+4) + Cs^2.


$$

Now, we find the constants $A, B,$ and $C.$

- Setting $s=0,$ we have

- Setting $s=-4,$ we have

- Comparing the coefficients of $s^2,$ we have

Thus, we can rewrite $F(s)$ as

$$


F(s) = -\dfrac{1}{16s} + \dfrac{1}{4s^2} + \dfrac{1}{16(s+4)}.


$$

**** Finding the Inverse of the base function

We find the inverse transform $f(t) = \mathcal L^{-1}\{F(s)\}$ using standard transforms:

$$


\begin{aligned}𝑓(𝑡) & =L^{−1}{−\frac{1}{16𝑠}+\frac{1}{4𝑠^{2}}+\frac{1}{16(𝑠+4)}} \\ & =−\frac{1}{16}+\frac{𝑡}{4}+\frac{1}{16}𝑒^{−4𝑡}.\end{aligned}


$$

**** Applying the time-shifting property

Finally, we address the $e^{-3s}$ term. By the second shifting theorem, we have

$$


e^{-as}\cdot F(s) = \mathcal L\{u(t-a)\cdot f(t-a)\}.


$$

Taking the inverse Laplace transform gives

$$


\mathcal L^{-1} \{ e^{-as}F(s) \} = u(t-a) \cdot f(t-a).


$$

In our case, $a=3.$ Therefore, we shift $f(t)$ by replacing every instance of $t$ with $(t-3){:}$

$$


\begin{aligned}𝑢(𝑡−3)𝑓(𝑡−3) & =𝑢(𝑡−3)[−\frac{1}{16}+\frac{𝑡−3}{4}+\frac{1}{16}𝑒^{−4(𝑡−3)}] \\ & =𝑢(𝑡−3)(\frac{1}{16}𝑒^{−4(𝑡−3)}+\frac{4𝑡−13}{16}).\end{aligned}


$$

Comparing this to the second term of the form given in the problem statement $y(t) = -2e^{-4t} + u(t-3)\cdot g(t),$ we identify $g(t)$ as

$$


g(t) = \dfrac{1}{16}e^{-4(t-3)} + \dfrac{4t-13}{16}.


$$
