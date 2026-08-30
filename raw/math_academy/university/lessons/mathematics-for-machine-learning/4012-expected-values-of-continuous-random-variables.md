# Expected Values of Continuous Random Variables

Source: https://www.mathacademy.com/topics/4012?courseId=145
Topic ID: 4012

## Prerequisites

- [Properties of Expectation for Discrete Random Variables](./2836-properties-of-expectation-for-discrete-random-variables.md)
- [Continuous Random Variables Over Infinite Domains](./4100-continuous-random-variables-over-infinite-domains.md)

## Lesson

### Introduction

The **expected value** (also known as the **expectation** or **mean**) of a continuous random variable is the average value we'd expect to get if we observed the random variable many times.

For a continuous random variable $X$ with probability density function $f(x)$ defined over a set $S,$ we can calculate the expected value using the following formula:

$$


\textrm E[X] = \int_S x \cdot f(x) \, \textrm dx


$$

For example, consider the continuous random variable $X$ with the following probability density function:

$$


f(x) = \dfrac{x}{4}, \quad 1 < x < 3


$$

We compute the expected value as follows:

$$


\begin{aligned}E[𝑋] & =∫_{31}𝑥⋅\frac{𝑥}{4}\,d𝑥 \\ & =∫_{31}\frac{𝑥^{2}}{4}\,d𝑥 \\ & =\frac{𝑥^{3}}{12}_{31} \\ & =\frac{13}{6}\end{aligned}


$$

### Example: Computing the Mean of a Continuous Random Variable

#### Question

Given that $X$ is a continuous random variable with the following probability density function, compute $\textrm E[X].$

$$


f(x) = \dfrac{x^2}{9}, \quad 0 \leq x \leq 3


$$

#### Explanation

For a continuous random variable $X$ with probability density function $f(x)$ defined over a set $S,$ we can calculate the expected value using the following formula:

$$


\textrm E[X] = \int_S x \cdot f(x) \, \textrm dx


$$

We compute the expected value of $X$ as follows:

$$


\begin{aligned}E[𝑋] & =∫_{30}𝑥⋅\frac{𝑥^{2}}{9}\,d𝑥 \\ & =∫_{30}\frac{𝑥^{3}}{9}\,d𝑥 \\ & =\frac{𝑥^{4}}{36}_{30} \\ & =\frac{9}{4}\end{aligned}


$$

### Example: Computing the Mean of a Continuous Random Variable With a Piecewise PDF

#### Question

Given that $X$ is a continuous random variable with the following probability density function, compute $\textrm E[X].$

$$


\begin{aligned}\frac{1}{4}, & 0<𝑥<2 \\ \frac{𝑥}{2}−\frac{3}{4}, & 2≤𝑥≤3\end{aligned}


$$

#### Explanation

For a continuous random variable $X$ with probability density function $f(x)$ defined over a set $S,$ we can calculate the expected value using the following formula:

$$


\textrm E[X] = \int_S x \cdot f(x) \, \textrm dx


$$

We compute the expected value of $X$ as follows:

$$


\begin{aligned}E[𝑋] & =∫_{30}𝑥⋅𝑓(𝑥)\,d𝑥 \\ & =∫_{20}𝑥⋅𝑓(𝑥)\,d𝑥+∫_{32}𝑥⋅𝑓(𝑥)\,d𝑥 \\ & =∫_{20}𝑥⋅\frac{1}{4}\,d𝑥+∫_{32}𝑥⋅(\frac{𝑥}{2}−\frac{3}{4})\,d𝑥 \\ & =∫_{20}\frac{𝑥}{4}\,d𝑥+∫_{32}(\frac{𝑥^{2}}{2}−\frac{3𝑥}{4})\,d𝑥 \\ & =\frac{𝑥^{2}}{8}_{20}+(\frac{𝑥^{3}}{6}−\frac{3𝑥^{2}}{8})_{32} \\ & =\frac{1}{2}+\frac{31}{24} \\ & =\frac{43}{24}\end{aligned}


$$

### Example: Computing the Mean of a Transformed Continuous Random Variable

#### Question

Given that $X$ is a continuous random variable with the following probability density function, compute $\textrm E[7X-4].$

$$


f(x) = \dfrac{3x^2}{7}, \quad 1 < x < 2


$$

#### Explanation

First, we simplify using the properties of expected value:

$$


\textrm E[7X-4] = 7 \textrm E[X] - 4


$$

For a continuous random variable $X$ with probability density function $f(x)$ defined over a set $S,$ we can calculate the expected value using the following formula:

$$


\text{E}[X] = \int_S x \cdot f(x) \,\text{d}x


$$

So, we calculate the expected value of $X$ as follows:

$$


\begin{aligned}E[𝑋] & =∫_{𝑆}𝑥⋅𝑓(𝑥)\,d𝑥 \\ & =∫_{21}𝑥⋅\frac{3𝑥^{2}}{7}\,d𝑥 \\ & =∫_{21}\frac{3𝑥^{3}}{7}\,d𝑥 \\ & =\frac{3𝑥^{4}}{28}_{21} \\ & =\frac{45}{28}\end{aligned}


$$

Therefore,

$$


\begin{aligned}E[7𝑋−4] & =7E[𝑋]−4 \\ & =7⋅\frac{45}{28}−4 \\ & =\frac{29}{4}.\end{aligned}


$$
