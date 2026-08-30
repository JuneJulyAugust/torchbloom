# Properties of Infinite Series

Source: https://www.mathacademy.com/topics/983?courseId=106
Topic ID: 983

## Prerequisites

- [Convergent and Divergent Infinite Series](./982-convergent-and-divergent-infinite-series.md)
- [Properties of Finite Series](../../../high-school/integrated-math-honors/lessons/integrated-math-ii-honors/3958-properties-of-finite-series.md)

## Lesson

### Introduction

Many of the properties that apply to *finite* series also apply to *convergent* infinite series.

For example, consider the following convergent series:

$$


\sum_{n =1}^\infty \frac{1}{4^n} = \frac 1 3, \qquad \sum_{n =1}^\infty \frac{1}{5^n} = \frac 1 4


$$

Let's use these results to calculate

$$


\sum_{n =1}^\infty \frac{3}{4^n} + \sum_{n =1}^\infty \frac{4}{5^n}.


$$

Since both series converge, we can take the constant factors outside the summation signs, similar to finite series.

$$


\begin{aligned}\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}\frac{3}{4^{𝑛}}+\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}\frac{4}{5^{𝑛}} & =3\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}\frac{1}{4^{𝑛}}+4\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}\frac{1}{5^{𝑛}} \\ & =3(\frac{1}{3})+4(\frac{1}{4}) \\ & =2\end{aligned}


$$

Let's now describe the general result.

### The Sum and Constant Multiple Rules for Convergent Series

If $a_n$ and $b_n$ are sequences such that

$$


\sum_{n =1}^\infty a_n = A,\qquad\qquad \sum_{n =1}^\infty b_n = B


$$

are both convergent, and if $\alpha$ and $\beta$ are both real numbers, then

$$


\sum_{n =1}^\infty \alpha a_n + \sum_{n =1}^\infty \beta b_n


$$

is also convergent, and

$$


\begin{aligned}\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}𝛼𝑎_{𝑛}+\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}𝛽𝑏_{𝑛} & =𝛼\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}𝑎_{𝑛}+𝛽\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}𝑏_{𝑛} \\ & =𝛼𝐴+𝛽𝐵.\end{aligned}


$$

### Example: Calculating a Sum of Convergent Series

#### Question

If $\displaystyle{\sum_{n=1}^\infty a_n} = 3$ and $\displaystyle{\sum_{n =1}^\infty b_n} = \frac 3 4,$ then calculate $\displaystyle{\sum_{n =1}^\infty 2 a_n} + \displaystyle{\sum_{n =1}^\infty 4 b_n}.$

#### Explanation

Taking the constant factors outside of the summation signs gives

$$


\begin{aligned}\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}2𝑎_{𝑛}+\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}4𝑏_{𝑛} & =2\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}𝑎_{𝑛}+4\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}𝑏_{𝑛} \\ & =2(3)+4(\frac{3}{4}) \\ & =6+3 \\ & =9.\end{aligned}


$$

### Scalar Multiplication of Infinite Series

Note the following rules regarding the multiplication of an infinite series by a scalar $K\mathbin{:}$

- If $\displaystyle\sum_{n=1}^\infty a_n$ is convergent, then $\displaystyle \sum_{n=1}^\infty K\cdot a_n = K\cdot \sum_{n=1}^\infty a_n$ is convergent for any real number $K.$

- If $\displaystyle\sum_{n=1}^\infty a_n$ is divergent, then $\displaystyle \sum_{n=1}^\infty K\cdot a_n$ is divergent for any real number $K\neq 0.$

### Example: Scalar Multiplication of a Convergent Series

#### Question

Given that $\displaystyle \sum_{n=1}^\infty a_n$ is convergent, determine all real values of $K$ for which $\displaystyle \dfrac1{\sqrt{K}} \cdot \sum_{n=1}^\infty a_n$ is convergent.

#### Explanation

Any constant multiple of a convergent series gives a convergent series.

However, the expression $\dfrac1{\sqrt{K}}$ is not defined when $K \leq 0.$

Therefore, the series

$$


\dfrac1{\sqrt{K}} \cdot \sum_{n=1}^\infty a_n


$$

is convergent for $K > 0.$

### Example: Scalar Multiplication of a Divergent Series

#### Question

Given that $\displaystyle \sum_{n=1}^\infty a_n$ is divergent, determine all real values of $K$ for which $\displaystyle \sum_{n=1}^\infty \left(K-\dfrac 12\right) \cdot a_n$ is ****

#### Explanation

If we multiply the terms of a divergent series by a non-zero constant, the resulting series is divergent.

However, multiplying the terms of a divergent series by $0$ gives a series that converges to $0.$

Therefore, the series

$$


\displaystyle \sum_{n=1}^\infty \left(K-\dfrac 12\right) \cdot a_n


$$

is convergent when

$$


\begin{aligned}𝐾−\frac{1}{2} & =0 \\ 𝐾 & =\frac{1}{2}.\end{aligned}


$$
