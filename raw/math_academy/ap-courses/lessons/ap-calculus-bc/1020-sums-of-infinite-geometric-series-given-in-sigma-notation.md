# Sums of Infinite Geometric Series Given in Sigma Notation

Source: https://www.mathacademy.com/topics/1020?courseId=21
Topic ID: 1020

## Prerequisites

- [Writing an Infinite Geometric Series in Sigma Notation](./686-writing-an-infinite-geometric-series-in-sigma-notation.md)
- [Finding the Sum of an Infinite Geometric Series](./691-finding-the-sum-of-an-infinite-geometric-series.md)

## Lesson

### Introduction

Suppose we want to evaluate the infinite geometric series

$$


\sum_{n = 1} ^ \infty 3 \left (\dfrac 1 4\right) ^ n.


$$

The sum $S_\infty$ of an infinite geometric series is given by the formula

$$


S_{\infty} = \dfrac {\color{black}a_1} {1 - {\color{black}r}},


$$

where ${\color{black}r}$ is the common ratio and $\color{black}a_1$ is the first term. So, we need to determine $\color{black}a_1$ and $\color{black}r$ and then plug those values into this formula.

The first term is

$$


{\color{black}a_1} = 3 \left( \dfrac 1 4 \right)^1 = {\color{black}\dfrac 3 4},


$$

and the common ratio is

$$


{\color{black}r} = \dfrac {a_2}{\color{black}a_1} = \dfrac {3 \left (\dfrac 1 4 \right)^2}{3\left( \dfrac 1 4 \right)^1}= {\color{black}\dfrac 1 4}.


$$

So, the sum of the series is

$$


\begin{aligned}\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}3(\frac{1}{4})^{𝑛} & =\frac{𝑎_{1}}{1−𝑟} \\ & =\frac{(\frac{3}{4})}{4} \\ & =\frac{(\frac{3}{4})}{4} \\ & =1.\end{aligned}


$$

### Example: Evaluating an Infinite Geometric Series Given Its First Term and Common Ratio

#### Question

Given that $a_1=-2$ and $\dfrac{a_{n+1}}{a_{n}} = -0.4$ for all integers $n \geq 1,$ find the value of $\displaystyle\sum_{n=1}^\infty a_{n}.$

#### Explanation

Notice that the given series is a geometric series because the ratio of any two consecutive terms is constant.

The sum to infinity $S_\infty$ of a geometric series is given by the formula

$$


S_\infty = \dfrac{a_1}{1-r}, \qquad |r| < 1,


$$

where $a_1$ is the first term and $r$ is the common ratio.

We're told that the first term is

$$


a_1=-2.


$$

The common ratio is

$$


r = \dfrac{a_{n+1}}{a_{n}} = -0.4.


$$

So, the sum of the series is

$$


\begin{aligned}\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}𝑎_{𝑛} & =\frac{𝑎_{1}}{1−𝑟} \\ & =\frac{−2}{1−(−0.4)} \\ & =\frac{−2}{1.4} \\ & =−\frac{10}{7}.\end{aligned}


$$

### Example: Evaluating an Infinite Geometric Series Expressed in Sigma Notation

#### Question

Evaluate the series $\displaystyle\sum_{n=1}^\infty 2(0.5)^{n}.$

#### Explanation

Notice that the given series is a geometric series because it is in the form $\displaystyle \sum ar^n.$

The sum to infinity $S_\infty$ of a geometric series is given by the formula

$$


S_\infty = \dfrac{a_1}{1-r}, \qquad |r| < 1,


$$

where $a_1$ is the first term and $r$ is the common ratio.

The first term is

$$


a_1 = 2(0.5)^{1} = 1.


$$

The common ratio is

$$


r = \dfrac{a_2}{a_1} = \dfrac{2(0.5)^2}{2(0.5)^1} = 0.5.


$$

So, the sum of the series is

$$


\begin{aligned}\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}2(0.5)^{𝑛} & =\frac{𝑎_{1}}{1−𝑟} \\ & =\frac{1}{1−0.5} \\ & =\frac{1}{0.5} \\ & =2.\end{aligned}


$$

### Example: Evaluating an Infinite Geometric Series Expressed in Sigma Notation With an Arbitrary Starting Index

#### Question

Evaluate the series $\displaystyle \sum_{n=2}^\infty\left(\dfrac 2 3\right)^n.$

#### Explanation

First, note that the index $n$ starts from $2.$ However, it is still a geometric series because it is in the form $\displaystyle \sum ar^n.$

In this case, the first term is $a_2,$ and so the sum to infinity $S_\infty$ of this geometric series is given by

$$


S_\infty = \dfrac{a_2}{1-r}, \qquad |r| < 1.


$$

For the first few terms, we have:

$$


\begin{aligned}𝑎_{2} & =(\frac{2}{3})^{2}=\frac{4}{9} \\ 𝑎_{3} & =(\frac{2}{3})^{3}=\frac{8}{27}\end{aligned}


$$

The common ratio is:

$$


r = \dfrac{a_3}{a_2} = \dfrac{\left( \dfrac{8}{27}\right)}{\left( \dfrac{4}{9}\right)} = \dfrac 2 3


$$

So, the sum of the series is:

$$


\begin{aligned}\underset{\underset{𝑛=2}{∑}}{\overset{}{∞}}(\frac{2}{3})^{𝑛} & =\frac{𝑎_{2}}{1−𝑟} \\ & =\frac{(\frac{4}{9})}{9} \\ & =\frac{(\frac{4}{9})}{9} \\ & =\frac{4⋅3}{9} \\ & =\frac{4}{3}\end{aligned}


$$

### Example: Evaluating an Infinite Geometric Series Expressed in Non-Standard Form Using Sigma Notation

#### Question

Evaluate the geometric series $\displaystyle \sum_{n=3}^\infty \dfrac{5}{2}\left(\dfrac{1}{2}\right)^{2n}.$

#### Explanation

First, note that the index $n$ starts from $3.$ In this case, the first term is $a_3,$ and so the sum to infinity $S_\infty$ of this geometric series is given by

$$


S_\infty = \dfrac{a_3}{1-r}, \qquad |r| < 1.


$$

Computing the first few terms, we get:

$$


a_3 = \dfrac{5}{2}\left(\dfrac{1}{2}\right)^{2(3)} = \dfrac{5}{2}\left(\dfrac{1}{2}\right)^{6} = 5\left(\dfrac{1}{2}\right)^{7}


$$

$$


a_4 = \dfrac{5}{2}\left(\dfrac{1}{2}\right)^{2(4)} = \dfrac{5}{2}\left(\dfrac{1}{2}\right)^{8} = 5\left(\dfrac{1}{2}\right)^{9}


$$

Therefore, the common ratio is

$$


r = \dfrac{a_4}{a_3} = \dfrac{5\left(\dfrac{1}{2}\right)^{9}}{5\left(\dfrac{1}{2}\right)^{7}} = \left(\dfrac{1}{2}\right)^{2} = \dfrac{1}{4}.


$$

So, the sum of the series is

$$


\begin{aligned}\underset{\underset{𝑛=3}{∑}}{\overset{}{∞}}\frac{5}{2}(\frac{1}{2})^{2𝑛} & =\frac{𝑎_{3}}{1−𝑟} \\ & =\frac{5(\frac{1}{2})^{7}}{2} \\ & =\frac{(\frac{5}{128})}{128} \\ & =(\frac{5}{128})(\frac{4}{3}) \\ & =\frac{5}{3(32)} \\ & =\frac{5}{96}.\end{aligned}


$$
