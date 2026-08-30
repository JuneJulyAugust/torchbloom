# Using the Implicit Euler Method With Newton's Method

Source: https://www.mathacademy.com/topics/6686?courseId=61
Topic ID: 6686

## Prerequisites

- [Newton's Method](../calculus-i/912-newton-s-method.md)
- [The Implicit Euler Method](./6396-the-implicit-euler-method.md)

## Lesson

### Introduction

We know how to apply the implicit Euler method to initial value problems

$$


y' = f(x,y), \qquad y_0 = y(x_0),


$$

that are linear in $y,$ that is, where $f(x,y) = a(x)y + b(x).$ However, in general, $f$ can be a nasty, nonlinear function in $y.$ For example, consider the following initial value problem:

$$


y' = x^2 - xy^4,\qquad y(0)=1


$$

Can we apply the implicit Euler method with step size $\Delta x = 0.5$ to this IVP to approximate the value of $y(0.5)?$

Yes, we can! However, doing so requires defining a function $g$ to which the next $y$-value $y_\text{new}$ is a solution of the equation $g(y_\text{new})=0.$ Then, we apply a root-finding method to solve for $y_\text{new}.$

To see how, let's start by applying the implicit Euler method as we normally would. In general, the change $\Delta y$ for our ODE is given by

$$


\begin{aligned}Δ𝑦 & =𝑦_{′new}^{}⋅Δ𝑥 \\ & =((𝑥_{new})^{2}−𝑥_{new}(𝑦_{new})^{4})⋅0.5 \\ & =0.5(𝑥_{new})^{2}−0.5𝑥_{new}(𝑦_{new})^{4}.\end{aligned}


$$

We substitute this into the update formula $y_\text{new} = y + \Delta y$ and move all terms to the left-hand side:

$$


\begin{aligned}𝑦_{new} & =𝑦+Δ𝑦 \\ 𝑦_{new} & =𝑦+0.5(𝑥_{new})^{2}−0.5𝑥_{new}(𝑦_{new})^{4} \\ 0.5𝑥_{new}(𝑦_{new})^{4}+𝑦_{new}−𝑦−0.5(𝑥_{new})^{2} & =0\end{aligned}


$$

Now, with terms such as $0.5x_\text{new}(y_\text{new})^4$ and $y_\text{new},$ there’s no simple algebraic rearrangement, and solving exactly is impractical.

Instead, let's define a new function $g$ of $y_\text{new}$ by the expression on the left-hand side:

$$


g(y_\text{new}) = 0.5x_\text{new}(y_\text{new})^4 + y_\text{new} - y - 0.5(x_\text{new})^2


$$

Note that, at any step, $y$ and $x_\text{new}$ are known constants, so $g$ is truly a one-variable function in $y_\text{new}.$

Then, the next $y$-value $y_\text{new}$ is a root of this function: $g(y_\text{new}) = 0.$ Therefore, to find $y_\text{new},$ we apply a root-finding method, such as Newton's method.

For instance, in the first step, the new $x$-value is $x_\text{new}=0+0.5=0.5.$ So, the function used in the first step is

$$


\begin{aligned}𝑔(𝑦_{new}) & =0.5⋅0.5⋅(𝑦_{new})^{4}+𝑦_{new}−1−0.5⋅(0.5)^{2} \\ & =0.25(𝑦_{new})^{4}+𝑦_{new}−1.125.\end{aligned}


$$

Then, we would proceed to use a root-finding method with starting point $y=1$ to solve $g(y_\text{new}) = 0.$

### Example: Determining the Function on Which to Apply a Root-Finding Method When Applying the Implicit Euler Method

#### Question

Consider the following initial value problem:

$$


y' = y^3 - x\,y, \qquad y(1)=1


$$

Using the implicit Euler method with step size $\Delta x = 1,$ the new value $y_\text{new}$ is obtained by solving the equation $g(y_\text{new}) = 0$ at each step. Which of the following is the **** $g(y_\text{new})$ used in the first step?

1. $g(y_\text{new}) = (y_\text{new})^3 - 3y_\text{new} - 1$

2. $g(y_\text{new}) = 3y_\text{new} - (y_\text{new})^3 + 1$

3. $g(y_\text{new}) = 3y_\text{new} - (y_\text{new})^3 - 1$

4. $g(y_\text{new}) = y_\text{new} - (y_\text{new})^3 + x_\text{new}y_\text{new}$

#### Explanation

For an initial value problem

$$


y' = f(x,y), \qquad y_0 = y(x_0),


$$

the implicit Euler method with step size $\Delta x$ is given by

$$


\Delta y = y'_\text{new} \cdot \Delta x,


$$

with $y'_\text{new} = f(x_\text{new},y_\text{new})$ evaluated at the next $x$ and $y$ values.

In general, $\Delta y$ is given by

$$


\begin{aligned}Δ𝑦 & =𝑦_{′new}^{}⋅Δ𝑥 \\ & =(𝑦_{new})^{3}−𝑥_{new}𝑦_{new} \\ & =(𝑦_{new})^{3}−𝑥_{new}𝑦_{new}.\end{aligned}


$$

We substitute this into $y_\text{new} = y + \Delta y$ and move all terms to the left-hand side and define the resulting expression as $g(y_\text{new}){:}$

$$


\begin{aligned}𝑦_{new} & =𝑦+Δ𝑦 \\ 𝑦_{new} & =𝑦+(𝑦_{new})^{3}−𝑥_{new}𝑦_{new} \\ \underset{𝑔(𝑦_{new})}{\underset{}{𝑦_{new}−(𝑦_{new})^{3}+𝑥_{new}𝑦_{new}−𝑦}} & =0.\end{aligned}


$$

So, the general form of the function $g$ for step size $\Delta x = 1$ is

$$


g(y_\text{new}) = y_\text{new} - (y_\text{new})^3 + x_\text{new}y_\text{new} - y.


$$

Now, in the first step, the new $x$ value is $x_\text{new} = x + \Delta x = 1 + 1 = 2.$ Therefore, the function used in the first step is

$$


\begin{aligned}𝑔(𝑦_{new}) & =𝑦_{new}−(𝑦_{new})^{3}+2𝑦_{new}−1 \\ & =3𝑦_{new}−(𝑦_{new})^{3}−1.\end{aligned}


$$

### Example: Approximating the Solution to an Initial Value Problem Using the Implicit Euler Method: One Step

#### Question

Consider the following initial value problem:

$$


y' = 2xy + y^3, \qquad y(1.5)=-0.3


$$

Use the implicit Euler method with one step and Newton's method to approximate $y(2).$ Round your answer to two decimal places.

#### Explanation

For an initial value problem

$$


y' = f(x,y), \qquad y_0 = y(x_0),


$$

the implicit Euler method with step size $\Delta x$ is given by

$$


\Delta y = y'_\text{new} \cdot \Delta x,


$$

with $y'_\text{new} = f(x_\text{new},y_\text{new})$ evaluated at the next $x$ and $y$ values.

Since we want to find the value of $y$ at $x=2,$ we will use a step size of

$$


\Delta x = 2 - 1.5 = 0.5.


$$

Now, let's proceed with the implicit Euler method. In general, $\Delta y$ is given by

$$


\begin{aligned}Δ𝑦 & =𝑦_{′new}^{}⋅Δ𝑥 \\ & =(2𝑥_{new}𝑦_{new}+(𝑦_{new})^{3})⋅0.5 \\ & =𝑥_{new}𝑦_{new}+0.5(𝑦_{new})^{3}.\end{aligned}


$$

We substitute this into $y_\text{new} = y + \Delta y$ and move all terms to the left-hand side and define the resulting expression as $g(y_\text{new}){:}$

$$


\begin{aligned}𝑦_{new} & =𝑦+Δ𝑦 \\ 𝑦_{new} & =𝑦+𝑥_{new}𝑦_{new}+0.5(𝑦_{new})^{3}\end{aligned}


$$

which gives the equation

$$


0.5(y_\text{new})^3 + (x_\text{new}-1)y_\text{new} + y = 0.


$$

So, the general form of the function $g$ for step size $\Delta x = 0.5$ is

$$


g(y_\text{new}) = 0.5(y_\text{new})^3 + (x_\text{new}-1)y_\text{new} + y.


$$

Now, in the first step, the new $x$ value is $x_\text{new} = x + \Delta x = 1.5 + 0.5 = 2.$ The old $y$ value is $y = -0.3.$ Then, the function $g$ is

$$


\begin{aligned}𝑔(𝑦_{new}) & =0.5(𝑦_{new})^{3}+(2−1)𝑦_{new}−0.3 \\ & =0.5(𝑦_{new})^{3}+𝑦_{new}−0.3.\end{aligned}


$$

We use a root-finding method with starting point $y=-0.3$ to solve $g(y_\text{new}) = 0.$ We'll use Newton's method.

$$


(y_\text{new})_{n+1} = (y_\text{new})_n - \dfrac{g(y_\text{new})}{g'(y_\text{new})}


$$

Note that the derivative of $g$ is

$$


g'(y_\text{new}) = 1.5(y_\text{new})^2 + 1.


$$

Therefore, our Newton's method iterative scheme is as follows:

$$


(y_\text{new})_{n+1} = (y_\text{new})_n - \dfrac{0.5((y_\text{new})_n)^3 + (y_\text{new})_n - 0.3}{1.5((y_\text{new})_n)^2 + 1}


$$

Applying several iterations of Newton's method starting with $y(1.5) = -0.3,$ we get the following:

$$


\begin{aligned}(𝑦_{new})_{1} & =−0.3 \\ (𝑦_{new})_{2} & ≈0.240529 \\ (𝑦_{new})_{3} & ≈0.288849 \\ (𝑦_{new})_{4} & ≈0.288050\end{aligned}


$$

Therefore, we conclude that $y(2) \approx 0.29,$ rounded to two decimal places.
