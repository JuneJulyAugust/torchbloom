# Maclaurin Series

Source: https://www.mathacademy.com/topics/340?courseId=21
Topic ID: 340

## Prerequisites

- [Convergent and Divergent Infinite Series](./982-convergent-and-divergent-infinite-series.md)
- [Higher-Degree Taylor Polynomials](./3771-higher-degree-taylor-polynomials.md)

## Lesson

### Introduction

The $n$th-degree Taylor polynomial of $f(x)=e^x$ about $x=0$ is

$$


P_n(x) = 1 + x + \dfrac{x^2}{2!}+ \dfrac{x^3}{3!} + \cdots \dfrac{x^n}{n!},


$$

or in sigma notation,

$$


P_n(x)=\sum_{k=0}^n \dfrac{x^k}{k!}.


$$

If we let $n\to\infty,$ we get an **infinite power series,** and the series *converges to* $f(x).$ Therefore, we can write

$$


e^x = \sum_{k=0}^\infty \dfrac{x^k}{k!}.


$$

The infinite series above is called the **Maclaurin series** (or **Maclaurin expansion**) of $e^x.$

This particular Maclaurin series converges for any $x\in(-\infty,\infty).$ We call this the **interval of convergence** of the series.

In general, for a function $f(x)$ that's infinitely differentiable at $x=0,$ the Maclaurin series of that function is

$$


\begin{aligned}𝑓(𝑥) & =𝑓(0)+𝑓^{′}(0)𝑥+\frac{𝑓^{″}(0)}{2!}𝑥^{2}+\frac{𝑓^{‴}(0)}{3!}𝑥^{3}+⋯ \\ & =\underset{\underset{𝑘=0}{∑}}{\overset{}{∞}}\frac{𝑓^{(𝑘)}(0)}{𝑘!}𝑥^{𝑘}.\end{aligned}


$$

The series converges to $f(x)$ provided that $x$ lies within the interval of convergence of the series.

In this lesson, we will state the interval of convergence for a given Maclaurin series. We will discuss how to calculate intervals of convergence in separate lessons.

### Example: Finding the First Few Terms of the Maclaurin Series of a Function

#### Question

Find the first three non-zero terms of the Maclaurin expansion of the function $f(x) = \ln(1+x),$ valid for $x\in(-1,1].$

#### Explanation

The Maclaurin expansion is

$$


f(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{f'''(0)}{3!}x^3+\cdots.


$$

Computing the necessary derivatives, we get

$$


\begin{aligned}𝑓(𝑥) & =ln⁡(1+𝑥) & ⟹ & & 𝑓(0) & =ln⁡(1+0)=0 \\ 𝑓^{′}(𝑥) & =\frac{1}{1+𝑥}=(1+𝑥)^{−1} & ⟹ & & 𝑓^{′}(0) & =(1+0)^{−1}=1 \\ 𝑓^{″}(𝑥) & =−\frac{1}{(1+𝑥)^{2}}=−(1+𝑥)^{−2} & ⟹ & & 𝑓^{″}(0) & =−(1+0)^{−2}=−1 \\ 𝑓^{‴}(𝑥) & =\frac{2}{(1+𝑥)^{3}}=2(1+𝑥)^{−3} & ⟹ & & 𝑓^{‴}(0) & =2(1+0)^{−3}=2.\end{aligned}


$$

Therefore, the Maclaurin expansion is

$$


\begin{aligned}ln⁡(1+𝑥) & =(0)+(1)𝑥+\frac{(−1)}{2!}𝑥^{2}+\frac{(2)}{3!}𝑥^{3}+⋯ \\ & =𝑥−\frac{1}{2}𝑥^{2}+\frac{1}{3}𝑥^{3}+⋯.\end{aligned}


$$

### Example: Expressing the Maclaurin Series of a Function in Sigma Notation

#### Question

Express the Maclaurin series expansion for $\cos{x},$ given by

$$


\cos{x} = 1 - \frac{x^2}{2} + \frac{x^4}{4!}- \frac{x^6}{6!}+\cdots ,


$$

using sigma notation.

#### Explanation

The first four terms of the series are

$$


\begin{aligned}𝑎_{0} & =1 \\ 𝑎_{1} & =−\,\frac{𝑥^{2}}{2} \\ 𝑎_{2} & =\frac{𝑥^{4}}{4!} \\ 𝑎_{3} & =−\frac{𝑥^{6}}{6!}.\end{aligned}


$$

Notice that we can express these terms using a common format, as follows:

$$


\begin{aligned}𝑎_{0} & =\frac{(−1)^{0}𝑥^{2⋅0}}{(2⋅0)!} \\ 𝑎_{1} & =\frac{(−1)^{1}𝑥^{2⋅1}}{(2⋅1)!} \\ 𝑎_{2} & =\frac{(−1)^{2}𝑥^{2⋅2}}{(2⋅2)!} \\ 𝑎_{3} & =\frac{(−1)^{3}𝑥^{2⋅3}}{(2⋅3)!}.\end{aligned}


$$

We deduce that the general formula for the $n$th term is

$$


a_n = \dfrac{(-1)^n x^{2n}}{(2n)!} \,.


$$

Therefore, we have

$$


\begin{aligned}cos⁡𝑥 & =\underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}\frac{(−1)^{𝑛}𝑥^{2𝑛}}{(2𝑛)!}\,.\end{aligned}


$$
