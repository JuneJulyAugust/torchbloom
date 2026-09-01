# Defining the Derivative Using Derivative Notation

Source: https://www.mathacademy.com/topics/812?courseId=105
Topic ID: 812

## Prerequisites

- [The Instantaneous Rate of Change of a Function at a Point](./337-the-instantaneous-rate-of-change-of-a-function-at-a-point.md)

## Lesson

### Introduction

The instantaneous rate of change of a function $f(x)$ at the point $x=a,$ denoted $f'(a),$ is given by the limit

$$


f'(a) = \lim_{h\to 0}\dfrac{f(a+h) - f(a)}{h}.


$$

This formula works for a specific point $x=a.$ If we want a method that works for a *general* point $x,$ then we substitute $a=x$ in the formula and get

$$


f'(x) = \lim_{h\to 0}\dfrac{f(x+h) - f(x)}{h}.


$$

The function $f'(x)$ is called the **derivative of $f(x)$ with respect to $x$**. It gives the slope of the tangent line to the curve $y=f(x)$ at a general point with coordinates $(x,f(x)).$

### Example: Constructing an Expression that Represents the Derivative of a Function

#### Question

Given that $f(x) = x^2,$ what is $f'(x)$ according to the definition of the derivative?

#### Explanation

The derivative $f '(x)$ is given by the limit

$$


\lim_{h\to 0} \dfrac{f(x+h)-f(x)}{h} .


$$

Since $f(x) = x^2$, we have that $f(x+h) = (x+h)^2.$ Hence, we get

$$


\displaystyle f'(x)=\lim_{h\to 0} \dfrac{(x+h)^2-x^2}{h} .


$$

### Alternative Definitions For the Derivative

For a given curve $y=f(x),$ the derivative can be represented using several different notations. They are

$$


f'(x),\qquad y'(x), \qquad \dfrac{\text{d}f}{\text{d}x}, \qquad \dfrac{\text{d}y}{\text{d}x}.


$$

In words, the term $y'(x)$ is said like

- "$y$ prime of $x$," or

- "$y$ prime," or sometimes

- "$y$ dash."

The term $\dfrac{\text{d}y}{\text{d}x}$ is said like "dee $y$ by dee $x$."

The important thing to remember is that they all represent the same thing, the derivative.

### Example: Calculating the Derivative of a Function

#### Question

Given $y =x^2,$ calculate $\dfrac{\text{d}y}{\text{d}x}$ using the limit of a difference quotient.

#### Explanation

We let $y=f(x)$ and apply the formula for the derivative:

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =\underset{ℎ→0}{lim}\frac{𝑓(𝑥+ℎ)−𝑓(𝑥)}{ℎ} \\ & =\underset{ℎ→0}{lim}\frac{(𝑥+ℎ)^{2}−𝑥^{2}}{ℎ} \\ & =\underset{ℎ→0}{lim}\frac{𝑥^{2}+2𝑥ℎ+ℎ^{2}−𝑥^{2}}{ℎ} \\ & =\underset{ℎ→0}{lim}\frac{2𝑥ℎ+ℎ^{2}}{ℎ} \\ & =\underset{ℎ→0}{lim}(\frac{2𝑥ℎ}{ℎ}+\frac{ℎ^{2}}{ℎ}) \\ & =\underset{ℎ→0}{lim}(2𝑥+ℎ) \\ & =2𝑥+0 \\ & =2𝑥\end{aligned}


$$
