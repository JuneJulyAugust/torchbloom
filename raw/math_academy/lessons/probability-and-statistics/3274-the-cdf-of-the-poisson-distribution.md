# The CDF of the Poisson Distribution

Source: https://www.mathacademy.com/topics/3274?courseId=73
Topic ID: 3274

## Prerequisites

- [Limits of Sequences](../ap-calculus-bc/1087-limits-of-sequences.md)
- [Cumulative Distribution Functions for Discrete Random Variables](../discrete-mathematics/2024-cumulative-distribution-functions-for-discrete-random-variables.md)
- [The Poisson Distribution](./3282-the-poisson-distribution.md)

## Lesson

### Introduction

When performing certain types of statistical tests (e.g., hypothesis testing), we often need to use standard cumulative distribution function (CDF) tables to carry out the test.

In this lesson, we'll learn how to construct CDF tables for the Poisson distribution and use them to calculate probabilities.

First, recall that the probability mass function of the Poisson distribution $\textrm{Po}(\lambda)$ is given by

$$


f(x) = \dfrac{\lambda^x e^{-\lambda}}{x!}, \qquad x=0,1,2,\ldots


$$

where $\lambda$ is a positive parameter.

The CDF of a discrete random variable $X$ is a function $F(x)$ such that

$$


F(x) = P(X \leq x).


$$

With that in mind, let's compute the values of $F(x)$ for the distribution $\textrm{Po}(2)$ at $x=0$ and $x=1.$

To do that, we use the definition of the cumulative distribution function:

$$


\begin{aligned}𝐹(0) & =𝑃(𝑋≤0) \\ & =𝑃(𝑋=0) \\ & =\frac{2^{0}⋅𝑒^{−2}}{0!} \\ & =\frac{1⋅𝑒^{−2}}{1} \\ & ≈0.1353 \\ 𝐹(1) & =𝑃(𝑋≤1) \\ & =𝑃(𝑋=0)+𝑃(𝑋=1) \\ & =\frac{2^{0}⋅𝑒^{−2}}{0!}+\frac{2^{1}⋅𝑒^{−2}}{1!} \\ & =\frac{1⋅𝑒^{−2}}{1}+\frac{2⋅𝑒^{−2}}{1} \\ & ≈0.4060\end{aligned}


$$

The CDF data is usually presented as a table. If we were to continue this process and calculate $F(2), F(3), F(4),$ and $F(5),$ our table would look as follows:

Note the following:

- $F(x)$ is an increasing function.

- Since $\textrm{Po}(\lambda)$ takes arbitrarily large values, we have $F(x) < 1$ for all $n,$ and $F(x) \to 1$ as $x\to\infty.$

### Example: Constructing a Poisson CDF Table

#### Question

Consider the Poisson distribution $\textrm{Po}(9).$ Rounding to $4$ decimal places, fill in the missing value in the corresponding table for the cumulative distribution function below.

#### Explanation

The cumulative distribution function of a discrete random variable $X$ is a function $F(x)$ such that

$$


F(x) = P(X \leq x).


$$

The probability mass function for the Poisson distribution $\textrm{Po}(\lambda)$ is given by

$$


f(x) = \dfrac{\lambda^x e^{-\lambda}}{x!}, \qquad x=0,1,2,3, \ldots\,.


$$

In our case, $\lambda=9.$

Therefore, we compute the missing element of the table as follows:

$$


\begin{aligned}𝐹(8) & =𝑃(𝑋≤8) \\ & =𝑃(𝑋≤7)+𝑃(𝑋=8) \\ & =𝐹(7)+𝑃(𝑋=8) \\ & =0.3239+\frac{9^{8}⋅𝑒^{−9}}{8!} \\ & ≈0.4557\end{aligned}


$$

### Example: Computing a Poisson Probability Using a CDF Table

#### Question

Using the cumulative distribution function table of the Poisson random variable $X \sim \textrm{Po}(6)$ given below, compute $P(X=7).$

#### Explanation

The cumulative distribution function of a discrete random variable $X$ is a function $F(x)$ such that

$$


F(x) = P(X \leq x).


$$

So, we have

$$


\begin{aligned}𝐹(7) & =𝑃(𝑋≤7) \\ & =𝑃(𝑋∈{0,1,…,7}) \\ & =𝑃(𝑋∈{0,1,…,6})+𝑃(𝑋=7) \\ & =𝑃(𝑋≤6)+𝑃(𝑋=7) \\ & =𝐹(6)+𝑃(𝑋=7).\end{aligned}


$$

Therefore,

$$


\begin{aligned}𝑃(𝑋=7) & =𝐹(7)−𝐹(6) \\ & =0.7440−0.6063 \\ & =0.1377.\end{aligned}


$$

### Example: Computing a Poisson Probability Over an Interval Using a CDF Table

#### Question

Using the cumulative distribution function table of the Poisson random variable $X \sim \textrm{Po}(8)$ given below, compute $P(3 \leq X \leq 6).$

#### Explanation

The cumulative distribution function of a discrete random variable $X$ is a function $F(x)$ such that

$$


F(x) = P(X \leq x).


$$

So, we have

$$


\begin{aligned}𝐹(6) & =𝑃(𝑋≤6) \\ & =𝑃(𝑋∈{0,1,…,6}) \\ & =𝑃(𝑋∈{0,1,2})+𝑃(𝑋∈{3,4,5,6}) \\ & =𝑃(𝑋≤2)+𝑃(3≤𝑋≤6) \\ & =𝐹(2)+𝑃(3≤𝑋≤6).\end{aligned}


$$

Therefore,

$$


\begin{aligned}𝑃(3≤𝑋≤6) & =𝐹(6)−𝐹(2) \\ & =0.3134−0.0138 \\ & =0.2996.\end{aligned}


$$

### Example: Computing a Probability Over an Interval Containing a "Greater Than" Symbol

#### Question

Using the cumulative distribution function table of the Poisson random variable $X \sim \textrm{Po}(7)$ given below, compute $P(X \geq 5).$

#### Explanation

The cumulative distribution function of a discrete random variable $X$ is a function $F(x)$ such that

$$


F(x) = P(X \leq x).


$$

To solve the given problem, we can use the rule

$$


P(X > a) = 1 - P(X\leq a) = 1-F(a).


$$

Now, note that

$$


P(X \geq 5) = P(X \gt 4).


$$

Therefore, we have

$$


\begin{aligned}𝑃(𝑋≥5) & =𝑃(𝑋>4) \\ & =1−𝑃(𝑋≤4) \\ & =1−𝐹(4) \\ & =1−0.1730 \\ & =0.8270.\end{aligned}


$$
