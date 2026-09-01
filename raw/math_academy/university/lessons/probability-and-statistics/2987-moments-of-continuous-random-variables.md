# Moments of Continuous Random Variables

Source: https://www.mathacademy.com/topics/2987?courseId=73
Topic ID: 2987

## Prerequisites

- [Moments of Discrete Random Variables](./3642-moments-of-discrete-random-variables.md)
- [Expected Values of Continuous Random Variables](./4012-expected-values-of-continuous-random-variables.md)

## Lesson

### Introduction

Suppose $X$ is a continuous random variable with probability density function $f(x)$ defined over a set $S.$

The values $\text{E}[X]$ and $\text{E}[X^2]$ are called the **first moment** and **second moment** of $X,$ respectively.

Recall that the first moment $\text{E}[X]$ is also called the *expected value* of $X$ and is computed as follows:

$$


\displaystyle \text{E}[X] = \int_S x \cdot f(x) \,\text{d}x


$$

To find second moment $\text{E}[X^2],$ the expected value of the the random variable $X^2,$ we simply substitute $x^2$ for $x$ in the formula above, as follows:

$$


\displaystyle \text{E}[X^2] = \int_S x^2 \cdot f(x) \,\text{d}x


$$

Let's compute the second moment $\text{E}[X^2]$ of the continuous random variable $X$ with the probability density function

$$


f(x) = \dfrac{3}{2}\sqrt{x}, \qquad 0 \leq x \leq 1.


$$

We compute the expected value of $X^2$ as follows:

$$


\begin{aligned}E[𝑋^{2}] & =∫_{𝑆}𝑥^{2}⋅𝑓(𝑥)\,d𝑥 \\ & =∫_{10}𝑥^{2}⋅\frac{3}{2}\sqrt{𝑥}\,d𝑥 \\ & =\frac{3}{2}∫_{10}𝑥^{5/2}\,d𝑥 \\ & =\frac{3}{2}(\frac{2}{7}𝑥^{7/2})_{10} \\ & =\frac{3}{2}(\frac{2}{7}−0) \\ & =\frac{3}{7}\end{aligned}


$$

### Example: Calculating the Second Moment of a Random Variable

#### Question

A continuous random variable $X$ has the probability density function

$$


\begin{aligned}\frac{1}{8}, & −2<𝑥<0, \\ \frac{3}{2}\,𝑥, & 0≤𝑥<1.\end{aligned}


$$

Calculate $\text{E}[X^2].$

#### Explanation

For a continuous random variable $X$ with probability density function $f(x)$ defined over a set $S,$ the expected value of $X^2$ is given by

$$


\text{E}[X^2] = \int_{S} x^2 \cdot f(x) \,\text{d}x.


$$

So, we compute the expected value of $X^2$ as follows:

$$


\begin{aligned}E[𝑋^{2}] & =∫_{1−2}𝑥^{2}⋅𝑓(𝑥)\,d𝑥 \\ & =∫_{0−2}𝑥^{2}⋅\frac{1}{8}\,d𝑥+∫_{10}𝑥^{2}⋅\frac{3}{2}\,𝑥\,d𝑥 \\ & =\frac{1}{8}∫_{0−2}𝑥^{2}\,d𝑥+\frac{3}{2}∫_{10}𝑥^{3}\,d𝑥 \\ & =\frac{1}{24}\,𝑥^{3}\,_{0−2}+\frac{3}{8}\,𝑥^{4}\,_{10} \\ & =\frac{1}{24}(0+8)+\frac{3}{8}(1−0) \\ & =\frac{1}{3}+\frac{3}{8} \\ & =\frac{17}{24}\end{aligned}


$$

### Higher Moments

It's also possible to define higher moments. For example, $\text{E}[X^3]$ is the **third moment** of the random variable $X.$

Notice the pattern:

- $\displaystyle \text{E}[X] = \int_S x \cdot f(x) \,\text{d}x$ is the *first* moment

- $\displaystyle \text{E}[X^2] = \int_S x^2 \cdot f(x) \,\text{d}x$ is the *second* moment

- $\displaystyle \text{E}[X^3] = \int_S x^3 \cdot f(x) \,\text{d}x$ is the *third* moment

and so on. In general, the **$n$th moment** is given by

$$


\text{E}[X^n] = \int_S x^n \cdot f(x) \,\text{d}x.


$$

Finally, note that

$$


\text{E}[X], \quad \text{E}[X^2], \quad \text{E}[X^3], \quad \ldots


$$

are sometimes referred to as the first, second, and third **raw moments**. This is because it's possible to define other types of moments.

In general, $\text{E}[X^n]$ can be called either the $n$th *moment* or $n$th *raw moment*.

### Example: Calculating a Higher Moments of a Random Variable

#### Question

A continuous random variable $X$ has the probability density function

$$


\begin{aligned}1−𝑥, & 0≤𝑥≤1 \\ \frac{1}{2}, & 1<𝑥≤2.\end{aligned}


$$

Calculate $\textrm E [X^4].$

#### Explanation

For a continuous random variable $X$ with probability density function $f(x)$ defined over a set $S,$ the $n$th raw moment of $X$ is given by

$$


\text{E}[X^n] = \int_{S} x^n \cdot f(x) \,\text{d}x.


$$

So, we compute the fourth raw moment of $X$ as follows:

$$


\begin{aligned}E[𝑋^{4}] & =∫_{20}𝑥^{4}⋅𝑓(𝑥)\,d𝑥 \\ & =∫_{10}𝑥^{4}⋅(1−𝑥)\,d𝑥+∫_{21}𝑥^{4}⋅\frac{1}{2}\,d𝑥 \\ & =∫_{10}(𝑥^{4}−𝑥^{5})\,d𝑥+\frac{1}{2}∫_{21}𝑥^{4}\,d𝑥 \\ & =(\frac{1}{5}\,𝑥^{5}−\frac{1}{6}\,𝑥^{6})\,_{10}+\frac{1}{10}\,𝑥^{5}\,_{21} \\ & =(\frac{1}{5}−\frac{1}{6}−0)+\frac{1}{10}(32−1) \\ & =\frac{1}{30}+\frac{31}{10} \\ & =\frac{47}{15}\end{aligned}


$$

### Example: Computing the Mean of a Transformed Random Variable

#### Question

The continuous random variable $X$ has the following probability density function:

$$


f(x) = 2x, \quad 0 \leq x \leq 1


$$

Given that $\text{E}[X] = \dfrac{2}{3},$ compute $\text{E}[5X^2 - 2X].$

**

#### Explanation

First, we simplify using the hint and the properties of expected value:

$$


\begin{aligned}E[5𝑋^{2}−2𝑋] & =5E[𝑋^{2}]−2E[𝑋]\end{aligned}


$$

For a continuous random variable $X$ with probability density function $f(x)$ defined over a set $S,$ the $n$th raw moment of $X$ is given by

$$


\text{E}[X^n] = \int_S x^n \cdot f(x) \,\text{d}x.


$$

We already know $\textrm E [X].$ So, we compute the second raw moment of $X$ as follows:

$$


\begin{aligned}E[𝑋^{2}] & =∫_{10}𝑥^{2}⋅2𝑥\,d𝑥 \\ & =2∫_{10}𝑥^{3}\,d𝑥 \\ & =\frac{1}{2}\,𝑥^{4}\,_{10} \\ & =\frac{1}{2}(1−0) \\ & =\frac{1}{2}\end{aligned}


$$

Substituting $\text{E}[X] = \dfrac{2}{3}$ and $\text{E}[X^2] = \dfrac{1}{2}$ into the simplified expression, we conclude that

$$


\begin{aligned}E[5𝑋^{2}−2𝑋] & =5E[𝑋^{2}]−2E[𝑋] \\ & =5⋅\frac{1}{2}−2⋅\frac{2}{3} \\ & =\frac{5}{2}−\frac{4}{3} \\ & =\frac{7}{6}.\end{aligned}


$$
