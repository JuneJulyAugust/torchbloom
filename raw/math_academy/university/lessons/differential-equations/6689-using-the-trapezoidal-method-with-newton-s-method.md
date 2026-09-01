# Using the Trapezoidal Method With Newton's Method

Source: https://www.mathacademy.com/topics/6689?courseId=61
Topic ID: 6689

## Prerequisites

- [Newton's Method](../calculus-i/912-newton-s-method.md)
- [The Trapezoidal Method](./6373-the-trapezoidal-method.md)

## Lesson

### Introduction

We know how to apply the trapezoidal method to initial value problems that are linear in $y.$ Can we apply it to more complex initial value problems, such as

$$


y' = 2x^2 - y^4, \qquad y(0)=1?


$$

Yes, we can. To do so, we define a function $g$ such that the next $y$-value, $y_\text{new},$ satisfies the equation $g(y_\text{new})=0.$ Then, we apply a root-finding method to solve for $y_\text{new}.$

To demonstrate, let's apply the trapezoidal method to the IVP above with step size $\Delta x = 0.5.$

We begin as usual. In general, the change $\Delta y$ is given by

$$


\begin{aligned}Δ𝑦 & =\frac{1}{2}(𝑦^{′}+𝑦_{′new})⋅Δ𝑥 \\ & =\frac{1}{2}(2𝑥^{2}−𝑦^{4}+2(𝑥_{new})^{2}−(𝑦_{new})^{4})⋅0.5 \\ & =0.5𝑥^{2}−0.25𝑦^{4}+0.5(𝑥_{new})^{2}−0.25(𝑦_{new})^{4}.\end{aligned}


$$

Substituting this into the update formula for $\Delta y,$ we have

$$


\begin{aligned}𝑦_{new} & =𝑦+Δ𝑦 \\ 𝑦_{new} & =𝑦+0.5𝑥^{2}−0.25𝑦^{4}+0.5(𝑥_{new})^{2}−0.25(𝑦_{new})^{4},\end{aligned}


$$

and moving all terms to the left-hand side gives the equation

$$


0.25(y_\text{new})^4 + y_\text{new} + 0.25y^4 - y - 0.5x^2 - 0.5(x_\text{new})^2 = 0.


$$

Here, there is no simple algebraic rearrangement to isolate $y_\text{new},$ so solving exactly is impractical. Instead, we define a new function $g$ of $y_\text{new}$ by the expression on the left-hand side:

$$


g(y_\text{new}) = 0.25(y_\text{new})^4 + y_\text{new} + 0.25y^4 - y - 0.5x^2 - 0.5(x_\text{new})^2


$$

Note that $x,$ $y,$ and $x_\text{new}$ are known constants at each step, so $g$ is truly a one-variable function in $y_\text{new}.$

Then, the next $y$-value $y_\text{new}$ is a root of this function: $g(y_\text{new}) = 0.$ Therefore, to find $y_\text{new},$ we apply a root-finding method, such as Newton's method.

For instance, in the first step, the new $x$-value is $x_\text{new} = 0 + 0.5 = 0.5.$ So, the function used in the first step is

$$


\begin{aligned}𝑔(𝑦_{new}) & =0.25(𝑦_{new})^{4}+𝑦_{new}+0.25⋅(1)^{4}−1−0.5⋅(0)^{2}−0.5⋅(0.5)^{2} \\ & =0.25(𝑦_{new})^{4}+𝑦_{new}−0.875.\end{aligned}


$$

Then, we would proceed to use a root-finding method with starting point $y=1$ to solve $g(y_\text{new})=0.$

### Example: Determining the Function on Which to Apply a Root-Finding Method When Applying the Trapezoidal Method

#### Question

Consider the following initial value problem:

$$


y' = 2y^2 - \sqrt{x}, \qquad y(1)=1


$$

Using the trapezoidal method with step size $\Delta x = 1,$ the new value $y_\text{new}$ is obtained by solving the equation $g(y_\text{new}) = 0$ at each step. Which of the following is the **** $g(y_\text{new})$ used in the first step?

1. $g(y_\text{new}) = y_\text{new} - (y_\text{new})^2 - 1 + \dfrac12\sqrt{2}$

2. $g(y_\text{new}) = y_\text{new} - \dfrac12 (y_\text{new})^2 - \dfrac32 + \dfrac12\sqrt{2}$

3. $g(y_\text{new}) = y_\text{new} - (y_\text{new})^2 - \dfrac32 + \dfrac12\sqrt{2}$

4. $g(y_\text{new}) = y_\text{new} - (y_\text{new})^2 - \dfrac32 - \dfrac12\sqrt{2}$

#### Explanation

For an initial value problem

$$


y' = f(x,y), \qquad y(a) = c,


$$

the trapezoidal method with step size $\Delta x$ is given by

$$


\Delta y = \dfrac12(y' + y'_\text{new}) \cdot \Delta x,


$$

with $y'_\text{new} = f(x_\text{new},y_\text{new})$ evaluated at the next $x$ and $y$ values.

In this example, $\Delta y$ is given by

$$


\begin{aligned}Δ𝑦 & =\frac{1}{2}(𝑦^{′}+𝑦_{′new})⋅Δ𝑥 \\ & =\frac{1}{2}(2𝑦^{2}−\sqrt{𝑥}+2(𝑦_{new})^{2}−\sqrt{𝑥_{new}})⋅1 \\ & =𝑦^{2}−\frac{1}{2}\sqrt{𝑥}+(𝑦_{new})^{2}−\frac{1}{2}\sqrt{𝑥_{new}}.\end{aligned}


$$

Substituting this into $y_\text{new} = y + \Delta y,$ we have

$$


\begin{aligned}𝑦_{new} & =𝑦+Δ𝑦 \\ 𝑦_{new} & =𝑦+𝑦^{2}−\frac{1}{2}\sqrt{𝑥}+(𝑦_{new})^{2}−\frac{1}{2}\sqrt{𝑥_{new}}.\end{aligned}


$$

Moving all terms to the left-hand side gives the equation

$$


y_\text{new} - (y_\text{new})^2 - y - y^2 + \dfrac12\sqrt{x} + \dfrac12\sqrt{x_\text{new}} = 0.


$$

So, the general form of the function $g$ for step size $\Delta x = 1$ is

$$


g(y_\text{new}) = y_\text{new} - (y_\text{new})^2 - y - y^2 + \dfrac12\sqrt{x} + \dfrac12\sqrt{x_\text{new}}.


$$

Now, in the first step, the new $x$ value is

$$


x_\text{new} = x + \Delta x = 1 + 1 = 2.


$$

Therefore, the function used in the first step is

$$


\begin{aligned}𝑔(𝑦_{new}) & =𝑦_{new}−(𝑦_{new})^{2}−1−1^{2}+\frac{1}{2}\sqrt{1}+\frac{1}{2}\sqrt{2} \\ & =𝑦_{new}−(𝑦_{new})^{2}−\frac{3}{2}+\frac{1}{2}\sqrt{2}.\end{aligned}


$$

### Example: Approximating the Solution to an Initial Value Problem Using the Trapezoidal Method

#### Question

Consider the following initial value problem:

$$


y' = 2 - xy^2, \qquad y(1)=1


$$

Use the trapezoidal method with one step and Newton's method to approximate $y(2).$ Round your answer to two decimal places.

#### Explanation

For an initial value problem

$$


y' = f(x,y), \qquad y(a) = c,


$$

the trapezoidal method with step size $\Delta x$ is given by

$$


\Delta y = \dfrac12(y' + y'_\text{new}) \cdot \Delta x,


$$

with $y'_\text{new} = f(x_\text{new},y_\text{new})$ evaluated at the next $x$ and $y$ values.

Since we want to find the value of $y$ at $x=2,$ we will use a step size of

$$


\Delta x = 2 - 1 = 1.


$$

Now, let's proceed with the trapezoidal method. In general, $\Delta y$ is given by

$$


\begin{aligned}Δ𝑦 & =\frac{1}{2}(𝑦^{′}+𝑦_{′new})⋅Δ𝑥 \\ & =\frac{1}{2}((2−𝑥𝑦^{2})+(2−𝑥_{new}(𝑦_{new})^{2}))⋅1 \\ & =\frac{1}{2}(4−𝑥𝑦^{2}−𝑥_{new}(𝑦_{new})^{2}) \\ & =2−0.5𝑥𝑦^{2}−0.5𝑥_{new}(𝑦_{new})^{2}.\end{aligned}


$$

Substituting this into $y_\text{new} = y + \Delta y,$ we have

$$


\begin{aligned}𝑦_{new} & =𝑦+Δ𝑦 \\ 𝑦_{new} & =𝑦+2−0.5𝑥𝑦^{2}−0.5𝑥_{new}(𝑦_{new})^{2},\end{aligned}


$$

and moving all terms to the left-hand side gives the equation

$$


0.5x_\text{new}(y_\text{new})^2 + y_\text{new} - y - 2 + 0.5xy^2 = 0.


$$

So, the general form of the function $g$ for step size $\Delta x = 1$ is

$$


g(y_\text{new}) = 0.5x_\text{new}(y_\text{new})^2 + y_\text{new} - y - 2 + 0.5xy^2.


$$

Now, in the first step, the new $x$ value is

$$


x_\text{new} = x + \Delta x = 1 + 1 = 2.


$$

Then, the function $g$ is

$$


\begin{aligned}𝑔(𝑦_{new}) & =0.5⋅2\,(𝑦_{new})^{2}+𝑦_{new}−1−2+0.5⋅1⋅1^{2} \\ & =(𝑦_{new})^{2}+𝑦_{new}−2.5.\end{aligned}


$$

We use a root-finding method with starting point $y=1$ to solve $g(y_\text{new}) = 0.$ We'll use Newton's method:

$$


(y_\text{new})_{n+1} = (y_\text{new})_n - \dfrac{g(y_\text{new})}{g'(y_\text{new})}.


$$

Note that the derivative of $g$ is

$$


g'(y_\text{new}) = 2(y_\text{new}) + 1.


$$

Therefore, our Newton's method iterative scheme is as follows:

$$


(y_\text{new})_{n+1} = (y_\text{new})_n - \dfrac{((y_\text{new})_n)^2 + (y_\text{new})_n - 2.5} {2(y_\text{new})_n + 1}.


$$

Applying several iterations of Newton's method starting with $y(1) = 1,$ we get the following:

$$


\begin{aligned}(𝑦_{new})_{1} & =1 \\ (𝑦_{new})_{2} & ≈1.166\,667 \\ (𝑦_{new})_{3} & ≈1.158\,333 \\ (𝑦_{new})_{4} & ≈1.158\,312\end{aligned}


$$

Therefore, we conclude that $y(2) \approx \boxed{1.16},$ rounded to two decimal places.
