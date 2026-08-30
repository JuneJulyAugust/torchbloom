# Continuity of Functions

Source: https://www.mathacademy.com/topics/2006?courseId=136
Topic ID: 2006

## Prerequisites

- [Continuity Over an Interval](../../../ap-courses/lessons/ap-calculus-ab/612-continuity-over-an-interval.md)
- [Properties of Transformed Secant and Cosecant Functions](../../../high-school/traditional/lessons/algebra-ii/778-properties-of-transformed-secant-and-cosecant-functions.md)
- [Properties of Transformed Logarithmic Functions](../../../high-school/traditional/lessons/algebra-ii/1610-properties-of-transformed-logarithmic-functions.md)
- [Vertical Asymptotes of Rational Functions](./1815-vertical-asymptotes-of-rational-functions.md)
- [Properties of Transformed Tangent and Cotangent Functions](../../../high-school/traditional/lessons/algebra-ii/2064-properties-of-transformed-tangent-and-cotangent-functions.md)

## Lesson

### Introduction

Polynomial, rational, power, radical, exponential, logarithmic, and trigonometric functions are all continuous at every point in their respective domains. Therefore, to work out where any of these types of functions are continuous, we just need to work out what the domain is.

For example, the polynomial $f(x) = 3x^3-2x^2-1$ defined for all real numbers $x.$ Therefore, it is continuous on the interval $(-\infty, \infty).$

On the other hand, the radical function $g(x) = \sqrt{x}$ is defined for all numbers $x \geq 0.$ Therefore, it is continuous on the interval $[0,\infty).$

### Example: Finding the Intervals on Which a Radical Function Is Continuous

#### Question

Determine the largest interval on which the function $f(x)=\sqrt{4-x}$ is continuous.

#### Explanation

Our function is a radical function, so it is continuous over all points in its domain.

To find the domain of $\sqrt{4-x}$, we set the expression under the radical to be greater than or equal to zero:

$$


4-x\geq 0 \qquad \Longrightarrow\qquad x\leq 4


$$

Therefore, the domain of $f(x)$ is $(-\infty,4]$, and the function is continuous on this interval.

### Example: Finding the Intervals on Which a Rational Function Is Continuous

#### Question

Determine the largest union of intervals on which the function $f(x)=\dfrac{x-3}{x^2-5x+6}$ is continuous.

#### Explanation

This is a rational function, so it is continuous at all points in its domain. To find its domain, we start by factoring the denominator:

$$


\begin{aligned}𝑓(𝑥) & =\frac{𝑥−3}{𝑥^{2}−5𝑥+6} \\ & =\frac{𝑥−3}{(𝑥−2)(𝑥−3)} \\ & =\frac{1}{𝑥−2},\end{aligned}


$$

where $x \neq 3$.

This function is continuous everywhere except at the excluded points $x=2$ and $x=3.$

Therefore, the domain consists of the union of the intervals $(-\infty, 2),$ $(2,3),$ and $(3, \infty),$ namely

$$


(-\infty, 2)\cup(2,3)\cup(3, \infty)


$$

and the function is continuous on these intervals.

### Example: Finding the Intervals on Which a Logarithmic Function Is Continuous

#### Question

Find the largest interval of continuity for the function $f(x)=\log (2x-3) + x^2+1.$

#### Explanation

The function consists of two parts, a logarithm, and a polynomial.

The polynomial $x^2+1$ is continuous at all points in its domain, and its domain consists of all real numbers. So, we focus on the logarithm.

Likewise, the logarithmic function $\log(2x-3)$ is continuous at all points in its domain. However, the logarithm is only defined for positive inputs, so to find its domain, we set the expression inside the logarithm to be greater than zero:

$$


\begin{aligned}2𝑥−3 & >0 \\ 2𝑥 & >3 \\ 𝑥 & >\frac{3}{2}\end{aligned}


$$

Therefore, the function $f(x)=\log (2x-3) + x^2 + 1$ is continuous on the interval $\left(\dfrac 32,\infty\right).$

### Example: Finding the Intervals on Which a Trigonometric Function Is Continuous

#### Question

The interval $I$ consists of all real numbers $x$ such that $0 \leq x \leq 2\pi.$ What is the largest subset of $I$ on which the function $g(x) = \sin{x}+\cot{x}$ is continuous?

#### Explanation

Trigonometric functions are continuous at all points in their respective domains.

The function $\sin{x}$ is continuous over the entire interval $[0,2\pi],$ but the function $\cot{x}$ is not defined at $x=0, \pi, 2\pi.$

Therefore, the domain of $g(x)$ consists of the union of the intervals $(0, \pi)$ and $(\pi, 2\pi),$ namely

$$


(0, \pi)\cup(\pi, 2\pi)


$$

and the function is continuous on this union of intervals.
