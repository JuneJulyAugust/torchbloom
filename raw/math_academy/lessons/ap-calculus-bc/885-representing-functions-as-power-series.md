# Representing Functions as Power Series

Source: https://www.mathacademy.com/topics/885?courseId=21
Topic ID: 885

## Prerequisites

- [Convergence of Geometric Series](./684-convergence-of-geometric-series.md)
- [Finding the Sum of an Infinite Geometric Series](./691-finding-the-sum-of-an-infinite-geometric-series.md)
- [Taylor Series](./3826-taylor-series.md)

## Lesson

### Introduction

Suppose that we want to calculate the Maclaurin expansion for $f(x) = e^{3x}.$ Computing this using the formula is a lot of work because we have to calculate many derivatives and then plug them into the formula. Is there any easier way?

Yes, there is! First, let's recall the Maclaurin expansion of $e^x{:}$

$$


e^x = 1 + x + \dfrac{x^2}{2!} + \dfrac{x^3}{3!} + \cdots, \qquad x \in (-\infty, \infty)


$$

Simply replacing $x$ with $3x$ in the above gives

$$


\begin{aligned}𝑒^{3𝑥} & =1+(3𝑥)+\frac{(3𝑥)^{2}}{2!}+\frac{(3𝑥)^{3}}{3!}+⋯ \\ & =1+3𝑥+\frac{9𝑥^{2}}{2}+\frac{27𝑥^{3}}{6}+⋯ \\ & =1+3𝑥+\frac{9𝑥^{2}}{2}+\frac{9𝑥^{3}}{2}+⋯\end{aligned}


$$

To compute the new interval of convergence, we do the same:

$$


\begin{aligned}3𝑥 & ∈(−∞,∞) \\ −∞ & <3𝑥<∞ \\ −∞ & <𝑥<∞ \\ 𝑥 & ∈(−∞,∞)\end{aligned}


$$

So the interval of convergence stays the same, and we have

$$


e^{3x} = 1 + 3x + \dfrac{9x^2}{2} + \dfrac{9x^3}{2} + \cdots, \qquad x \in (-\infty, \infty).


$$

And that's it! Notice how much quicker this was compared with calculating the expansion from scratch.

### The Basic Maclaurin Expansions

In order to quickly compute the Maclaurin expansions of a variety of functions, it's worth memorizing some of the most basic Maclaurin expansions so that you can use them as starting points. These are summarized below.

$$


\begin{aligned} & 𝑒^{𝑥}=1+𝑥+\frac{1}{2!}𝑥^{2}+\frac{1}{3!}𝑥^{3}+⋯\, & & 𝑥∈(−∞,∞) \\ & sin⁡(𝑥)=𝑥−\frac{1}{3!}𝑥^{3}+\frac{1}{5!}𝑥^{5}−⋯\, & & 𝑥∈(−∞,∞) \\ & cos⁡(𝑥)=1−\frac{1}{2!}𝑥^{2}+\frac{1}{4!}𝑥^{4}−⋯\, & & 𝑥∈(−∞,∞) \\ & ln⁡(1+𝑥)=𝑥−\frac{1}{2}𝑥^{2}+\frac{1}{3}𝑥^{3}−⋯\, & & 𝑥∈(−1,1] \\ & \frac{1}{1−𝑥}=1+𝑥+𝑥^{2}+𝑥^{3}+⋯\, & & 𝑥∈(−1,1) \\ & \frac{1}{1+𝑥}=1−𝑥+𝑥^{2}−𝑥^{3}+⋯ & & 𝑥∈(−1,1)\end{aligned}


$$

**Note:** To memorize the Maclaurin expansions above, it's helpful to notice the following:

- The series for $\dfrac{1}{1-x}$ consists a geometric series whose first term is $1$ and whose common ratio is $x.$ This makes sense, because the sum formula for a geometric series with first term $a_1$ and common ratio $r$ is $\dfrac{a_1}{1-r}.$

- The series for $\sin (x)$ consists of the alternating sum of the odd-degree terms in the series for $e^x.$ This makes sense because $\sin(x)$ is an odd function (its graph is symmetric across the origin).

- The series for $\cos (x)$ consists of the alternating sum of the even-degree terms in the series for $e^x.$ This makes sense because $\cos(x)$ is an even function (its graph is symmetric across the $y$-axis).

- The series for $e^x,$ $\sin(x),$ and $\cos(x)$ all have a factorial in the denominator and no factorial in the numerator. For all of our standard series, any term with a factorial in the denominator will converge for all $x,$ because the factorial grows much more quickly than the powers of $x.$ So, their intervals of convergence are $x \in (-\infty, \infty).$

### Example: Finding the Maclaurin Expansion of a Composite Function Using a Standard Maclaurin Expansion

#### Question

Find the first three non-zero terms of the Maclaurin expansion of $\sin{(2x^2)}.$

#### Explanation

The standard Maclaurin expansion for $\sin{x}$ is

$$


\begin{aligned}sin⁡𝑥 & =𝑥−\frac{𝑥^{3}}{3!}+\frac{𝑥^{5}}{5!}+⋯\,.\end{aligned}


$$

Replacing $x$ with $2x^2$ in the above expansion and simplifying gives

$$


\begin{aligned}sin⁡(2𝑥^{2}) & =(2𝑥^{2})−\frac{(2𝑥^{2})^{3}}{3!}+\frac{(2𝑥^{2})^{5}}{5!}+⋯ \\ & =2𝑥^{2}−\frac{8𝑥^{6}}{6}+\frac{32𝑥^{10}}{120}+⋯ \\ & =2𝑥^{2}−\frac{4𝑥^{6}}{3}+\frac{4𝑥^{10}}{15}+⋯\,.\end{aligned}


$$

This series has an infinite radius of convergence because the series expansion for $\sin x$ has an infinite radius of convergence.

### The Maclaurin Expansion of a Sum, Difference, or Product of Functions

To find the Maclaurin expansion for a sum, difference, or product of functions, we can

1. find the Maclaurin expansions of the individual functions, and then

2. perform the corresponding operation on the expansions.

The only catch is that we must take the intersection of the intervals of convergence, since we want to find where *both* of the individual functions converge.

For example, recall the following two Maclaurin expansions:

$$


\begin{aligned} & 𝑒^{𝑥}=1+𝑥+\frac{1}{2!}𝑥^{2}+\frac{1}{3!}𝑥^{3}+⋯\, & & 𝑥∈(−∞,∞) \\ & \frac{1}{1−𝑥}=1+𝑥+𝑥^{2}+𝑥^{3}+⋯\, & & 𝑥∈(−1,1)\end{aligned}


$$

To find the Maclaurin expansion of $e^x+\dfrac{1}{1-x},$ we can simply add the two expansions:

$$


\begin{aligned}𝑒^{𝑥}+\frac{1}{1−𝑥} & =(1+𝑥+\frac{1}{2!}𝑥^{2}+\frac{1}{3!}𝑥^{3}+⋯)+(1+𝑥+𝑥^{2}+𝑥^{3}+⋯) \\ & =(1+1)+(1+1)𝑥+(\frac{1}{2!}+1)𝑥^{2}+(\frac{1}{3!}+1)𝑥^{3}+⋯ \\ & =2+2𝑥+\frac{3}{2}𝑥^{2}+\frac{7}{6}𝑥^{3}+⋯\end{aligned}


$$

To find the interval of convergence, we take the intersection of the intervals of convergence of the individual functions:

$$


(-\infty, \infty) \cap (-1, 1) = (-1, 1)


$$

Therefore, we have

$$


\begin{aligned}𝑒^{𝑥}+\frac{1}{1−𝑥}=2+2𝑥+\frac{3}{2}𝑥^{2}+\frac{7}{6}𝑥^{3}+⋯,\, & & 𝑥∈(−1,1).\end{aligned}


$$

### Example: Finding the Maclaurin Expansion of a Sum of Functions Using Standard Maclaurin Expansions

#### Question

Find the first four non-zero terms of the Maclaurin expansion of $e^x+\sin(2x).$

#### Explanation

The Maclaurin series for $e^x$ is

$$


\begin{aligned}𝑒^{𝑥} & =1+𝑥+\frac{1}{2!}\,𝑥^{2}+\frac{1}{3!}\,𝑥^{3}+⋯ \\ & =1+𝑥+\frac{1}{2}\,𝑥^{2}+\frac{1}{6}\,𝑥^{3}+⋯\,.\end{aligned}


$$

The Maclaurin series for $\sin{x}$ is

$$


\begin{aligned}sin⁡𝑥=𝑥−\frac{1}{3!}𝑥^{3}+⋯\,.\end{aligned}


$$

Replacing $x$ with $2x,$ we get

$$


\begin{aligned}sin⁡(2𝑥) & =2𝑥−\frac{1}{3!}(2𝑥)^{3}+⋯ \\ & =2𝑥−\frac{4}{3}\,𝑥^{3}+⋯\,.\end{aligned}


$$

Adding the expansions for $e^{x}$ and $\sin(2x)$ we get

$$


\begin{aligned}𝑒^{𝑥}+sin⁡(2𝑥) & =(1+𝑥+\frac{1}{2}\,𝑥^{2}+\frac{1}{6}\,𝑥^{3}+⋯)+(2𝑥−\frac{4}{3}\,𝑥^{3}+⋯) \\ & =1+(1+2)𝑥+\frac{1}{2}\,𝑥^{2}+(\frac{1}{6}−\frac{4}{3})𝑥^{3}+⋯ \\ & =1+3𝑥+\frac{1}{2}\,𝑥^{2}−\frac{7}{6}\,𝑥^{3}+⋯\,.\end{aligned}


$$

This series has an infinite radius of convergence because the series expansions for $e^x$ and $\sin x$ both have an infinite radius of convergence.

### Example: Finding the Maclaurin Expansion of a Logarithmic Function

#### Question

Find the first three non-zero terms of the expansion of $f(x) = \ln{\left(\dfrac{1+2x}{1+x}\right)}.$

#### Explanation

First, using the laws of logarithms, we observe that

$$


\begin{aligned}ln⁡(\frac{1+2𝑥}{1+𝑥}) & =ln⁡(1+2𝑥)−ln⁡(1+𝑥)\,.\end{aligned}


$$

For the expansion of $\ln(1+x),$ we use the standard result

$$


\begin{aligned}ln⁡(1+𝑥) & =𝑥−\frac{1}{2}𝑥^{2}+\frac{1}{3}𝑥^{3}−⋯.\end{aligned}


$$

To obtain the expansion of $\ln{(1+2x)},$ we replace $x$ with $2x$ in the standard expansion:

$$


\begin{aligned}ln⁡(1+2𝑥) & =2𝑥−\frac{1}{2}(2𝑥)^{2}+\frac{1}{3}(2𝑥)^{3}−⋯ \\ & =2𝑥−2𝑥^{2}+\frac{8}{3}𝑥^{3}−⋯\end{aligned}


$$

Finally, we subtract the two series to give the desired result:

$$


\begin{aligned}ln⁡(\frac{1+2𝑥}{1+𝑥}) & =ln⁡(1+2𝑥)−ln⁡(1+𝑥) \\ & =(2𝑥−2𝑥^{2}+\frac{8}{3}𝑥^{3}−⋯)−(𝑥−\frac{1}{2}𝑥^{2}+\frac{1}{3}𝑥^{3}−⋯) \\ & =𝑥−\frac{3}{2}𝑥^{2}+\frac{7}{3}𝑥^{3}−⋯\end{aligned}


$$

For the series $\ln(1+2x),$ the radius of convergence is given by

$$


-1 < 2x \leq 1\quad\Longrightarrow\quad x\in \left(-\dfrac12,\dfrac12\right].


$$

The series $\ln(1+x)$ has a radius of convergence of $x\in(-1,1].$ Therefore, the radius of convergence of $f(x)$ is

$$


x\in \left(-\dfrac12,\dfrac12\right] \cap (-1,1] = \left(-\dfrac12,\dfrac12\right] .


$$

### Example: Finding the Maclaurin Expansion of a Product of Functions Using Standard Maclaurin Expansions

#### Question

Find the first three non-zero terms of the Maclaurin expansion of $e^x \cos{x}.$

#### Explanation

The standard Maclaurin expansion for $e^x$ is

$$


\begin{aligned}𝑒^{𝑥} & =1+𝑥+\frac{1}{2!}𝑥^{2}+\frac{1}{3!}𝑥^{3}+⋯ \\ & =1+𝑥+\frac{1}{2}𝑥^{2}+\frac{1}{6}𝑥^{3}+⋯\,.\end{aligned}


$$

The standard Maclaurin expansion for $\cos{x}$ is

$$


\begin{aligned}cos⁡𝑥 & =1−\frac{1}{2!}𝑥^{2}+\frac{1}{4!}𝑥^{4}+⋯ \\ & =1−\frac{1}{2}𝑥^{2}+\frac{1}{24}𝑥^{4}+⋯\,.\end{aligned}


$$

To find the expansion of $e^x \cos{x},$ we multiply the expansion of $e^x$ and $\cos{x},$ as follows:

$$


\begin{aligned}𝑒^{𝑥}cos⁡𝑥 & =(1+𝑥+\frac{1}{2}𝑥^{2}+\frac{1}{6}𝑥^{3}+⋯)(1−\frac{1}{2}𝑥^{2}+\frac{1}{24}𝑥^{4}+⋯)\end{aligned}


$$

Let's work out each term individually:

- There is a single constant term, given by

- There is a single $x$ term, given by

- There are two $x^2$ terms which cancel out

- There are two $x^3$ terms and their sum is given by

So, the first three non-zero terms of the expansion are

$$


\begin{aligned}𝑒^{𝑥}cos⁡𝑥 & =1+𝑥−\frac{1}{3}𝑥^{3}+⋯.\end{aligned}


$$

This series has an infinite radius of convergence because the series expansions for $e^x$ and $\cos x$ both have an infinite radius of convergence.
