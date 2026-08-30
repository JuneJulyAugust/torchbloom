# Harmonic Series and p-Series

Source: https://www.mathacademy.com/topics/860?courseId=106
Topic ID: 860

## Prerequisites

- [Compound AND Inequalities](../../../high-school/traditional/lessons/algebra-i/350-compound-and-inequalities.md)
- [Writing Radical Expressions Using Fractional Exponents](../../../high-school/traditional/lessons/algebra-i/380-writing-radical-expressions-using-fractional-exponents.md)
- [Further Properties of Infinite Series](./4052-further-properties-of-infinite-series.md)

## Lesson

### Introduction

A **$p$-series** is any series that takes the form

$$


\sum_{n=1}^{\infty} \dfrac 1 {n^p},


$$

where $p$ is a constant.

For example,

- the series $\displaystyle \sum_{n=1}^{\infty} \dfrac{1}{n}$ is a $p$-series with $p=1,$ and

- the series $\displaystyle \sum_{n=1}^{\infty} \dfrac{1}{n^2}$ is a $p$-series with $p=2.$

A rule called the **$p$-series test** can help us determine whether a $p$-series converges or diverges. The $p$-series test states that

- if $p > 1,$ then the series converges, while

- if $p \leq 1,$ then the series diverges.

To demonstrate,

- the series $\displaystyle \sum_{n=1}^{\infty} \dfrac{1}{n}$ *diverges* because it is a $p$-series with $p \leq 1,$ while

- the series $\displaystyle \sum_{n=1}^{\infty} \dfrac{1}{n^2}$ *converges* because it is a $p$-series $p > 1.$

The $p$-series with $p=1$ is also known as the **harmonic series**. It is often used as an example of a series that diverges even though its terms approach $0.$

The harmonic series is the edge case used to distinguish between convergent and divergent $p$-series. To remember the $p$-series test, we can use the following mnemonics:

- The $p$-series converges when the terms are *smaller* than those in the harmonic series, meaning that the denominator is *larger* (i.e., $p>1$).

- The $p$-series diverges when the terms are *larger or the same* as those in the harmonic series, meaning that the denominator is smaller (i.e., $p \leq 1$).

**Note:** As we will show at the end of the lesson, the $p$-series test can be proven using the integral test:

$\displaystyle \int \dfrac{1}{x^p} \, \textrm dx$ converges if $p > 1$ and diverges if $p \leq 1.$

### Example: Determining Whether a p-Series with Integer Exponent Converges

#### Question

Determine whether the series below converges or diverges.

$$


\sum_{n=1}^\infty \dfrac 2 {7n^5}.


$$

#### Explanation

The series can be written as

$$


\dfrac{2}{7} \sum_{n=1}^\infty \dfrac 1 {n^5}.


$$

This is a $p$-series with $p=5.$ Since $p > 1,$ the series is convergent.

Note that the factor of $\dfrac{2}{7}$ multiplying the series does not affect the convergence or divergence of the series.

### Example: Determining Whether a p-Series With Fractional Exponent Converges

#### Question

Determine whether the series below converges or diverges.

$$


\sum_{n=1}^\infty \dfrac 1 {\sqrt {n^5}}.


$$

#### Explanation

The series can be written as

$$


\sum_{n=1}^\infty \dfrac 1 {n^{5/2}},


$$

which is a $p$-series with $p = \dfrac 5 2.$ Since $p > 1,$ the series is convergent.

### Example: Determining Which Series Converge From a List

#### Question

Which of the following series are convergent?

1. $\displaystyle\sum_{n=1}^\infty \dfrac{1}{n^2\sqrt n}$

2. $\displaystyle\sum_{n=1}^\infty \dfrac{5}{n^2}$

3. $\displaystyle\sum_{n=1}^\infty \dfrac{\sqrt{n}}{\sqrt{n^3}}$

#### Explanation

We analyze each series in turn.

- First, we look at $\displaystyle\sum_{n=1}^\infty \dfrac{1}{n^2\sqrt n}.$ Rewriting this series gives which is a $p$-series with $p=\dfrac 5 2.$ Since $p > 1,$ the series converges by the $p$-series test.

- For the second series, we have which is a $p$-series with $p=2.$ Since $p>1,$ the series is convergent by the $p$-series test.

- For the third series, we have which is a $p$-series with $p=1$ (the harmonic series). Since $p \leq 1,$ the series diverges by the $p$-series test.

Therefore, only series I and II are convergent.

### Example: Convergence Parameters for p-Series

#### Question

For which values of $q$ does the series $\displaystyle \sum_{n=1}^\infty \dfrac{1}{n^{4q-2}}$ converge?

#### Explanation

A $p$-series is any series that takes the form

$$


\sum_{n=1}^{\infty} \dfrac 1 {n^p},


$$

where $p$ is a constant. The $p$-series test states that

- if $p > 1,$ then the series converges, while

- if $p \leq 1,$ then the series diverges.

Comparing our series to the $p$-series, we have

$$


p = 4q-2.


$$

According to the $p$-series test, the given series converges if

$$


4q-2 > 1\qquad\Longrightarrow\qquad q >\dfrac 3 4.


$$

Therefore, the series is convergent for all $q > \dfrac 3 4.$

### Proof that the Harmonic Series Diverges

To understand why the harmonic series diverges, we need to apply the integral test.

Given the series

$$


\sum_{n=1}^{\infty} \dfrac 1 {n},


$$

we can define a function $f(x)$ such that

$$


f(x) = \dfrac 1 {x}.


$$

Then we have

$$


\begin{aligned}∫_{∞1}^{}\frac{1}{𝑥}\,d𝑥 & =\underset{𝑏→∞}{lim}[ln⁡𝑥]_{𝑏1}^{} \\ & =\underset{𝑏→∞}{lim}(ln⁡𝑏−ln⁡1) \\ & =∞,\end{aligned}


$$

and therefore, the integral is divergent.

### Proof of the p-Series Test

To understand why the $p$-series test works, we need to apply the integral test.

Given the series

$$


\sum_{n=1}^{\infty} \dfrac 1 {n^p},


$$

we can define a function $f(x)$ such that

$$


f(x) = \dfrac 1 {x^p}.


$$

First, if $p=1,$ then our series is the harmonic series, which we have already proven diverges.

On the other hand, if $p \neq 1,$ then we have

$$


\begin{aligned}∫_{∞1}^{}\frac{1}{𝑥^{𝑝}}\,d𝑥 & =\underset{𝑏→∞}{lim}∫_{𝑏1}^{}𝑥^{−𝑝}\,d𝑥 \\ & =\underset{𝑏→∞}{lim}[\frac{𝑥^{−𝑝+1}}{−𝑝+1}]_{𝑏1}^{} \\ & =\underset{𝑏→∞}{lim}[\frac{1}{(1−𝑝)𝑥^{𝑝−1}}]_{𝑏1}^{} \\ & =\underset{𝑏→∞}{lim}(\frac{1}{(1−𝑝)𝑏^{𝑝−1}}−\frac{1}{(1−𝑝)}) \\ & =\frac{1}{1−𝑝}\underset{𝑏→∞}{lim}[\frac{1}{𝑏^{𝑝−1}}]−\frac{1}{(1−𝑝)},\end{aligned}


$$

which results in two cases:

- If $p>1,$ then $\displaystyle \lim_{b\to \infty}\left[\frac {1}{b ^{p - 1}}\right] = 0$ and the integral converges.

- If $p<1,$ then $\displaystyle \lim_{b\to \infty}\left[\frac {1}{b ^{p - 1}}\right] = \infty$ and the integral diverges.

So, if $p \leq 1$ then the integral diverges, while if $p>1$ then the integral converges.

Consequently, if $p \leq 1$ then the series diverges, while if $p > 1$ then the integral converges.
