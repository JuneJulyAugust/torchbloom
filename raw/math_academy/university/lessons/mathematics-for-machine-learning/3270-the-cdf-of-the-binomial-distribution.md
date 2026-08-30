# The CDF of the Binomial Distribution

Source: https://www.mathacademy.com/topics/3270?courseId=145
Topic ID: 3270

## Prerequisites

- [Cumulative Distribution Functions for Discrete Random Variables](../discrete-mathematics/2024-cumulative-distribution-functions-for-discrete-random-variables.md)
- [The Binomial Distribution](../discrete-mathematics/3281-the-binomial-distribution.md)

## Lesson

### Introduction

When performing certain types of statistical tests (e.g., hypothesis testing), we often need to use standard cumulative distribution function (CDF) tables to carry out the test.

In this lesson, we'll learn how to construct CDF tables for the binomial distribution and use them to calculate probabilities.

First, recall that the probability mass function of the binomial distribution $B(n,p)$ is given by

$$


f(x) = \binom{n}{x} \, p^x (1-p)^{n-x}, \qquad x=0,1,2,\ldots, n


$$

where $n$ is the number of trials, and $p$ is the probability of success.

Also, recall that the CDF of a discrete random variable $X$ is a function $F(x)$ such that

$$


F(x) = P(X \leq x).


$$

With that in mind, let's compute the value of $F(x)$ for the distribution $B(5,0.37)$ at $x=0$ and $x=1.$

To do that, we use the definition of the cumulative distribution function:

$$


\begin{aligned}𝐹(0) & =𝑃(𝑋≤0) \\ & =𝑃(𝑋=0) \\ & =(\frac{5}{0})(0.37)^{0}(1−0.37)^{5−0} \\ & =1⋅(0.37)^{0}⋅(0.63)^{5} \\ & ≈0.0992 \\ 𝐹(1) & =𝑃(𝑋≤1) \\ & =𝑃(𝑋=0)+𝑃(𝑋=1) \\ & =(\frac{5}{0})(0.37)^{0}(1−0.37)^{5−0}+(\frac{5}{1})(0.37)^{1}(1−0.37)^{5−1} \\ & =1⋅(0.37)^{0}⋅(0.63)^{5}+5⋅(0.37)^{1}⋅(0.63)^{4} \\ & ≈0.3907.\end{aligned}


$$

The CDF data is usually presented as a table. If we were to continue this process and calculate $F(2), F(3), F(4),$ and $F(5),$ our table would look as follows:

Note the following:

- $F(x)$ is an increasing function.

- Since $n$ is the largest possible value of the binomial distribution, we have $F(n) = 1.$

### Example: Constructing a Binomial CDF Table

#### Question

Consider the binomial random variable $X\sim B(7, 0.63).$ Rounding to $4$ decimal places, fill in the missing values in the cumulative distribution function table below.

#### Explanation

The cumulative distribution function of a discrete random variable $X$ is a function $F(x)$ such that

$$


F(x) = P(X \leq x).


$$

The probability mass function for the Binomial distribution $B(n,p)$ is given by

$$


f(x) = \displaystyle \binom{n}{x} p^x (1-p)^{n-x}, \qquad x=0,1,2,\ldots,n.


$$

In our case, $n=7$ and $p=0.63.$

Therefore, we compute the missing elements of the table as follows:

- For $F(6),$ we have

$$


\begin{aligned}𝐹(6) & =𝑃(𝑋≤6) \\ & =𝑃(𝑋≤5)+𝑃(𝑋=6) \\ & =𝐹(5)+𝑃(𝑋=6) \\ & =0.7987+(\frac{7}{6})(0.63)^{6}(1−0.63)^{7−6} \\ & =0.7987+7⋅(0.63)^{6}⋅(0.37)^{1} \\ & ≈0.9606.\end{aligned}


$$

- Since $n=7,$ we have that $F(7) = P(X\leq 7) = 1.$

Therefore, our completed table looks as follows:

### Example: Computing a Binomial Probability Using the CDF

#### Question

Using the cumulative distribution function table of the binomial random variable $X \sim B(6, 0.67)$ given below, compute $P(X=2).$

#### Explanation

The cumulative distribution function of a discrete random variable $X$ is a function $F(x)$ such that

$$


F(x) = P(X \leq x).


$$

So, we have

$$


\begin{aligned}𝐹(2) & =𝑃(𝑋≤2) \\ & =𝑃(𝑋∈{0,1,2}) \\ & =𝑃(𝑋∈{0,1})+𝑃(𝑋=2) \\ & =𝑃(𝑋≤1)+𝑃(𝑋=2) \\ & =𝐹(1)+𝑃(𝑋=2).\end{aligned}


$$

Therefore,

$$


\begin{aligned}𝑃(𝑋=2) & =𝐹(2)−𝐹(1) \\ & =0.0969−0.0170 \\ & =0.0799\end{aligned}


$$

### Example: Computing a Binomial Probability Over an Interval Using the CDF

#### Question

Using the cumulative distribution function table of the binomial random variable $X \sim B(6, 0.47)$ given below, compute $P(1 \leq X \lt 5).$

#### Explanation

The cumulative distribution function of a discrete random variable $X$ is a function $F(x)$ such that

$$


F(x) = P(X \leq x).


$$

So, we have

$$


\begin{aligned}𝐹(4) & =𝑃(𝑋≤4) \\ & =𝑃(𝑋∈{0,1,2,3,4}) \\ & =𝑃(𝑋∈{0})+𝑃(𝑋∈{1,2,3,4}) \\ & =𝑃(𝑋≤0)+𝑃(1≤𝑋<5) \\ & =𝐹(0)+𝑃(1≤𝑋<5).\end{aligned}


$$

Therefore,

$$


\begin{aligned}𝑃(1≤𝑋<5) & =𝐹(4)−𝐹(0) \\ & =0.9163−0.0222 \\ & =0.8941.\end{aligned}


$$

### Example: Computing a Binomial Probability Over an Interval Containing a "Greater Than" Symbol

#### Question

Using the cumulative distribution function table of the binomial random variable $X \sim B(7, 0.52)$ given below, compute $P(X \geq 2).$

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


P(X \geq 2) = P(X \gt 1).


$$

Therefore, we have

$$


\begin{aligned}𝑃(𝑋≥2) & =𝑃(𝑋>1) \\ & =1−𝑃(𝑋≤1) \\ & =1−𝐹(1) \\ & =1−0.0504 \\ & =0.9496.\end{aligned}


$$
