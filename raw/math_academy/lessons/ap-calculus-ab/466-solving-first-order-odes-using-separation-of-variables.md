# Solving First-Order ODEs Using Separation of Variables

Source: https://www.mathacademy.com/topics/466?courseId=24
Topic ID: 466

## Prerequisites

- [Solving First-Order ODEs Using Direct Integration](./1061-solving-first-order-odes-using-direct-integration.md)

## Lesson

### Introduction

Consider the differential equation

$$


\dfrac{\textrm{d}y}{\textrm{d}x} = e^{x - y}\,.


$$

The right-hand side is a function of both $x$ and $y,$ so we can't solve the equation by integrating both sides with respect to $x,$ at least not straight away. So, how do we find a general solution to the equation?

First of all, note that it is possible to separate the variables $x$ and $y$ on each side of the equation as follows:

$$


\begin{aligned}\frac{d𝑦}{d𝑥}=𝑒^{𝑥−𝑦}=\frac{𝑒^{𝑥}}{𝑒^{𝑦}}\,⟹\,𝑒^{𝑦}⋅\frac{d𝑦}{d𝑥}=𝑒^{𝑥}.\end{aligned}


$$

Next, we integrate both sides with respect to $x,$ and get

$$


\begin{aligned}∫𝑒^{𝑦}⋅\frac{d𝑦}{d𝑥}\,d𝑥 & =∫𝑒^{𝑥}\,d𝑥.\end{aligned}


$$

Using the rule for integration by substitution, we can simplify the integrand on the left-hand side and carry out the integration as follows:

$$


\begin{aligned}∫𝑒^{𝑦}⋅\frac{d𝑦}{d𝑥}\,d𝑥 & =∫𝑒^{𝑥}\,d𝑥 \\ ∫𝑒^{𝑦}⋅\frac{d𝑦}{d𝑥}\,d𝑥 & =∫𝑒^{𝑥}\,d𝑥 \\ ∫𝑒^{𝑦}\,d𝑦 & =∫𝑒^{𝑥}\,d𝑥 \\ 𝑒^{𝑦} & =𝑒^{𝑥}+𝐶\,.\end{aligned}


$$

So, the general solution to the differential equation is

$$


e^y = e^x + C.


$$

This is an **implicit form** of the solution since it is not written explicitly as $y=y(x).$

We can write our general solution in **explicit form** (i.e., in the form $y=y(x)$) by noting that since $e^y > 0$ for all $y$, we may assume that the right-hand side is positive and apply the natural logarithm, as follows:

$$


\begin{aligned}ln⁡(𝑒^{𝑦}) & =ln⁡(𝑒^{𝑥}+𝐶) \\ 𝑦 & =ln⁡(𝑒^{𝑥}+𝐶)\end{aligned}


$$

### First-Order Separable Equations

The differential equation that we just solved was **separable**. A first-order differential equation is separable if it can be written in the form

$$


\dfrac {\textrm{d}y} {\textrm{d}x} = h(x)g(y).


$$

If an equation is separable, we say that the variables are *separated* when it is written in the form

$$


\dfrac{1}{g(y)} \cdot \dfrac{\textrm{d}y}{\textrm{d}x} = h(x).


$$

Once the variables are separated, we can integrate both sides of the equation with respect to $x,$ as follows:

$$


\begin{aligned}∫\frac{1}{𝑔(𝑦)}⋅\frac{d𝑦}{d𝑥}\,d𝑥 & =∫ℎ(𝑥)\,d𝑥 \\ ∫\frac{d𝑦}{𝑔(𝑦)} & =∫ℎ(𝑥)\,d𝑥.\end{aligned}


$$

We then evaluate both integrals and find the solution. Note that for the solution to be valid, we require $g(y)\neq 0.$

### Example: Separating the Variables in a Differential Equation

#### Question

Given that $x,y \geq 0,$ separate the variables in the following differential equation:

$$


\dfrac{\textrm{d}y}{\textrm{d}x} = \sqrt{2xy}


$$

#### Explanation

A differentiable equation is ** if it can be written in the form

$$


\dfrac{\textrm{d}y}{\textrm{d}x} = h(x)g(y).


$$

If an equation is separable, we say that the variables are ** when it is written in the form

$$


\dfrac{1}{g(y)} \cdot \dfrac{\textrm{d}y}{\textrm{d}x} = h(x).


$$

Notice that our differentiable equation is separable since it can be written as

$$


\dfrac{\textrm{d}y}{\textrm{d}x} = \sqrt{2x} \cdot \sqrt{y}.


$$

Therefore, we separate the variables as follows:

$$


\dfrac{1}{\sqrt{y}} \cdot \dfrac {\textrm{d}y} {\textrm{d}x} = \sqrt{2x}


$$

### Example: Finding a General Solution in Implicit Form

#### Question

Find the general solution to the differential equation $\dfrac{\textrm{d}y}{\textrm{d}x} = \dfrac{x}{y}.$

#### Explanation

To find the general solution, we first separate the variables:

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =\frac{𝑥}{𝑦} \\ 𝑦\frac{d𝑦}{d𝑥} & =𝑥\end{aligned}


$$

Then, we integrate both sides with respect to $x{:}$

$$


\begin{aligned}∫𝑦\,\frac{d𝑦}{d𝑥}\,d𝑥 & =∫𝑥\,d𝑥 \\ ∫𝑦\,\frac{d𝑦}{d𝑥}\,d𝑥 & =∫𝑥\,d𝑥 \\ ∫𝑦\,d𝑦 & =∫𝑥\,d𝑥 \\ \frac{𝑦^{2}}{2} & =\frac{𝑥^{2}}{2}+𝐾 \\ 𝑦^{2} & =𝑥^{2}+2𝐾 \\ 𝑦^{2} & =𝑥^{2}+𝐶,\end{aligned}


$$

where $C= 2K.$

Therefore, the general solution to the differential equation (in implicit form) is

$$


y^2 = x^2 + C .


$$

### Example: Finding a General Solution in Explicit Form

#### Question

Find the general solution to the differential equation $y' = \dfrac {x^2}{y}.$

#### Explanation

To find the general solution, we first separate the variables:

$$


\begin{aligned}𝑦^{′} & =\frac{𝑥^{2}}{𝑦} \\ \frac{d𝑦}{d𝑥} & =\frac{𝑥^{2}}{𝑦} \\ 𝑦\,\frac{d𝑦}{d𝑥} & =𝑥^{2}\end{aligned}


$$

Then, we integrate both sides with respect to $x{:}$

$$


\begin{aligned}∫𝑦\,\frac{d𝑦}{d𝑥}\,d𝑥 & =∫𝑥^{2}\,d𝑥 \\ ∫𝑦\,\frac{d𝑦}{d𝑥}\,d𝑥 & =∫𝑥^{2}\,d𝑥 \\ ∫𝑦\,d𝑦 & =∫𝑥^{2}\,d𝑥 \\ \frac{1}{2}𝑦^{2} & =\frac{1}{3}𝑥^{3}+𝐶\end{aligned}


$$

Therefore, the general solution to the differential equation (in implicit form) is

$$


\dfrac{1}{2}y^2 = \dfrac{1}{3}x^3 + C.


$$

We can express the solution in the form $y = y(x)$ as follows:

$$


\begin{aligned}\frac{1}{2}𝑦^{2} & =\frac{1}{3}𝑥^{3}+𝐶 \\ 𝑦^{2} & =\frac{2}{3}𝑥^{3}+2𝐶 \\ 𝑦 & =±\sqrt{√\frac{2}{3}𝑥^{3}+2𝐶} \\ 𝑦 & =±\sqrt{√\frac{2}{3}𝑥^{3}+𝐾}\end{aligned}


$$

where $K = 2C.$

### Example: Finding General Solutions by Rearranging Then Integrating

#### Question

Find the general solution to the differential equation $y' + 2xy = 0$ for $y\neq 0.$

#### Explanation

To find the general solution, we first separate the variables:

$$


\begin{aligned}𝑦^{′}+2𝑥𝑦 & =0 \\ \frac{d𝑦}{d𝑥}+2𝑥𝑦 & =0 \\ \frac{d𝑦}{d𝑥} & =−2𝑥𝑦 \\ \frac{1}{𝑦}⋅\frac{d𝑦}{d𝑥} & =−2𝑥\end{aligned}


$$

Then, we integrate both sides with respect to $x{:}$

$$


\begin{aligned}∫\frac{1}{𝑦}⋅\frac{d𝑦}{d𝑥}\,d𝑥 & =∫(−2𝑥)\,d𝑥 \\ ∫\frac{1}{𝑦}\,d𝑦 & =−2∫𝑥\,d𝑥 \\ ln⁡|𝑦| & =−𝑥^{2}+𝐶\end{aligned}


$$

Therefore, the general solution to the differential equation (in implicit form) is

$$


\ln \vert y \vert = -x^2 + C.


$$

We're required to write the solution in the form $y = y(x).$ By doing this, we get

$$


\begin{aligned}ln⁡|𝑦| & =−𝑥^{2}+𝐶 \\ |𝑦| & =𝑒^{−𝑥^{2}+𝐶} \\ |𝑦| & =𝑒^{−𝑥^{2}}⋅𝑒^{𝐶} \\ |𝑦| & =𝐾𝑒^{−𝑥^{2}}\end{aligned}


$$

where $K = e^C$ and $K > 0.$

We can drop the absolute value bars by allowing $K$ to be either positive or negative. Therefore, the most general solution is

$$


y = Ke^{-x^2}.


$$
