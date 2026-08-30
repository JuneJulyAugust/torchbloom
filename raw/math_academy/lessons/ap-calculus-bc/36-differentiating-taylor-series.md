# Differentiating Taylor Series

Source: https://www.mathacademy.com/topics/36?courseId=21
Topic ID: 36

## Prerequisites

- [Radius of Convergence of Power Series Centered at the Origin](./984-radius-of-convergence-of-power-series-centered-at-the-origin.md)
- [Taylor Series](./3826-taylor-series.md)

## Lesson

### Introduction

Suppose the Taylor (Maclaurin) series for the function $f(x)$ about $x=0$ is given by

$$


f(x) = \sum_{n=0}^\infty \dfrac{(-1)^n}{2n+1} x^{2n+1}


$$

and converges to $f(x)$ for $|x| < R,$ where $R$ is the radius of convergence of the Taylor series. How can we calculate the first three non-zero terms of Taylor series for the derivative, $f'(x),$ about $x=0?$

All we need to do is differentiate the Taylor series of $f(x).$ Writing out the first three terms, we get

$$


f(x) = \sum_{n=0}^\infty \dfrac{(-1)^n}{2n+1} x^{2n+1} = x - \dfrac{x^3}{3} + \dfrac{x^5}{5} - \cdots.


$$

Now, to find $f'(x),$ we differentiate term-by-term and get

$$


\begin{aligned}𝑓^{′}(𝑥) & =\frac{d}{d𝑥}(𝑥)−\frac{d}{d𝑥}(\frac{𝑥^{3}}{3})+\frac{d}{d𝑥}(\frac{𝑥^{5}}{5})−⋯ \\ & =1−𝑥^{2}+𝑥^{4}−⋯.\end{aligned}


$$

And that's it! The radius of convergence of the Taylor series for $f'(x)$ is $R,$ the same as $f(x).$

### Example: Finding the First Few Terms for the Derivative of a Taylor Series

#### Question

The Taylor series for the function $f(x)$ about $x=1$ is given by

$$


\displaystyle f(x) = \sum_{n=1}^\infty { {{n}}(x-1)^{n}}.


$$

Calculate the first three non-zero terms of the Taylor series expansion about $x=1$ of $f'(x).$

#### Explanation

Writing the first few terms of the series explicitly, we have

$$


\sum_{n=1}^\infty { {{n}}(x-1)^{n}} = (x-1) + {2(x-1)^2} + {3(x-1)^3} +\cdots .


$$

To find $f'(x),$ we differentiate term-by-term. This gives

$$


\begin{aligned}𝑓^{′}(𝑥) & =1+0+4(𝑥−1)+9(𝑥−1)^{2}+⋯ \\ & =1+4(𝑥−1)+9(𝑥−1)^{2}+⋯.\end{aligned}


$$

### Example: Finding the General Term for the Derivative of a Taylor Series

#### Question

The Taylor series for the function $f(x)$ about $x=3$ is given by

$$


\displaystyle f(x) = \sum_{n=1}^\infty \dfrac{ (x-3)^{n}}{n}


$$

Find $a_n,$ given that

$$


f'(x) = \sum_{n=1}^\infty a_n.


$$

#### Explanation

Writing the terms of the series explicitly, we have

$$


𝑛


$$

Differentiating the above series term-by-term gives

$$


𝑛


$$

We can now write the Taylor series for $f'(x)$ using the sigma notation as follows:

$$


f'(x) = \sum_{n=1}^\infty (x-3)^{n-1}.


$$

Comparing the series above with the given series, we can deduce that

$$


a_n = (x-3)^{n-1}.


$$

### Example: Finding the Radius of Convergence for the Derivative of a Taylor Series

#### Question

The Taylor series for the function $f(x)$ about $x=0$ is given by

$$


\displaystyle f(x) = \sum_{n=1}^\infty \dfrac{(-3)^{n}\,x^n}{n^3}


$$

The series converges to $f(x)$ for $|x| < R,$ where $R$ is the radius of convergence of the Taylor series. Calculate the radius of convergence of the series expansion of $f'(x),$ the derivative of $f(x),$ about $x=0.$

#### Explanation

The radius of convergence for the Taylor series of $f'(x)$ is the same as the Taylor series of $f(x).$ So, to find the radius of convergence of $f'(x),$ we need to compute $R.$

To calculate $R,$ we can use the ratio test. Computing the limit of the absolute value of the ratio of two consecutive terms, we get

$$


\begin{aligned}𝐿 & =\underset{𝑛→∞}{lim}\frac{𝑎_{𝑛+1}}{𝑎_{𝑛}} \\ & =\underset{𝑛→∞}{lim}\frac{(−3)^{𝑛+1}\,𝑥^{𝑛+1}}{(𝑛+1)^{3}}⋅\frac{𝑛^{3}}{(−3)^{𝑛}\,𝑥^{𝑛}} \\ & =\underset{𝑛→∞}{lim}\frac{(−3)𝑥⋅𝑛^{3}}{(𝑛+1)^{3}} \\ & =3|𝑥|\underset{𝑛→∞}{lim}\frac{1}{(1+\frac{1}{𝑛})^{3}} \\ & =3|𝑥|.\end{aligned}


$$

The series converges when $L<1.$ So, it converges when

$$


\begin{aligned}3|𝑥| & <1 \\ |𝑥| & <\frac{1}{3}\end{aligned}


$$

Therefore, the radius of convergence is $R = \dfrac 1 3.$
