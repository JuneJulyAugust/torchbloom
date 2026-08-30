# I.I.D Normal Random Variables

Source: https://www.mathacademy.com/topics/3859?courseId=145
Topic ID: 3859

## Prerequisites

- [Combining Multiple Normally Distributed Random Variables](./3638-combining-multiple-normally-distributed-random-variables.md)

## Lesson

### Introduction

A set of random variables is said to be **independent and identically distributed** (or **I.I.D.**) if the random variables are mutually independent and have the same probability distribution.

When we conduct a random sample of size $n$ from a population, the sample elements

$$


X_1,\quad X_2,\quad \ldots,\quad X_n


$$

are often considered to be I.I.D. random variables. This assumption often allows us to simplify the statistical analysis.

Suppose that the random variables $X_1, X_2, \ldots, X_n$ are I.I.D, where

$$


X_i\sim N(\mu, \sigma^2), \qquad 1\leq i \leq n.


$$

Let's consider their sum

$$


Y = X_1+X_2+\cdots + X_n.


$$

Since each $X_i$ is normally distributed, it follows that $Y$ is normally distributed as well. Moreover, we can compute the mean and the variance of $Y$ as follows:

- Calculating the mean using the properties of expectation, we get

- Similarly, using the properties of variance, we get

Therefore,

$$


Y = X_1+X_2+\cdots+X_n\sim N(n\mu, n\sigma^2).


$$

We will soon use this important result to develop models of how random samples are distributed. But for now, let's practice working with I.I.D normal random variables.

### Example: Calculating Distributions and Probabilities With I.I.D Normal Random Variables

#### Question

Given that $X_1, X_2, \ldots, X_{6}$ are I.I.D random variables, where

$$


X_i \sim N(2,3^2), \qquad 1\leq i \leq 6,


$$

calculate $P(10\leq Y\leq 14),$ where $Y = X_1+X_2+\cdots + X_{6}.$

**

#### Explanation

Recall that if $X_1, X_2, \ldots, X_{n}$ are independent and identically distributed (I.I.D) normal random variables, where

$$


X_i \sim N(\mu,\sigma^2), \qquad 1\leq i \leq n,


$$

then

$$


Y = X_1+X_2+\cdots + X_n\sim N(n\mu, \: n\sigma^2).


$$

Therefore, since $X_1, X_2, \ldots, X_{6}$ are independent and identically distributed, we have

$$


\begin{aligned}𝑌=𝑋_{1}+𝑋_{2}+⋯+𝑋_{6} & ∼𝑁(6⋅2,\,6⋅3^{2}) \\ & ∼𝑁(6⋅2,\,6⋅9) \\ & =𝑁(12,54).\end{aligned}


$$

We wish to compute the probability $P(10\leq Y \leq 14).$ We first convert $Y$ into a standard normal random variable by $z$-scoring:

$$


\begin{aligned}𝑃(10≤𝑌≤14) & =𝑃(\frac{10−12}{\sqrt{54}}≤𝑍≤\frac{14−12}{\sqrt{54}}) \\ & =𝑃(−\frac{2}{\sqrt{54}}≤𝑍≤\frac{2}{\sqrt{54}}) \\ & =𝑃(−0.27≤𝑍≤0.27) \\ & =Φ(0.27)−Φ(−0.27) \\ & =Φ(0.27)−(1−Φ(0.27)) \\ & =2Φ(0.27)−1\end{aligned}


$$

From the $z$-table, we have

$$


\Phi(0.27) = 0.6064.


$$

Therefore,

$$


P(10\leq Y \leq 14) = 2\Phi(0.27) - 1 = 0.2128.


$$

### Example: Calculating Distributions and Probabilities With I.I.D Normal Random Variables In Context

#### Question

In a library, each shelf is filled with $20$ volumes of an encyclopedia, plus one bookend. The weight of one volume, in grams, is normally distributed with a mean of $150\,\textrm g$ and a standard deviation of $5\,\textrm g,$ while the weight of a bookend, in grams, is normally distributed with a mean of $50\,\textrm g$ and a standard deviation of $2\,\textrm g.$ If one shelf is randomly selected, what is the probability that it supports a weight of more than $3\,000\,\textrm g?$ You may assume that the weights of the volumes and bookend are mutually independent.

**

#### Explanation

Let $X_i$ denote the weight of the $i$th volume, and let $Y$ denote the weight of a bookend. Then, we have

$$


X_i \sim N(150, 5^2), \qquad 1\leq i \leq 20,


$$

and

$$


Y \sim N(50, 2^2).


$$

Let the random variable $W$ denote the weight of a randomly selected shelf. Then, since

$$


W = X_1+X_2+\cdots + X_{20} + Y,


$$

we have that $W$ is normally distributed, where

$$


\begin{aligned}E[𝑊] & =20⋅150+50 \\ & =3\,050, \\ Var[𝑊] & =20⋅5^{2}+2^{2} \\ & =504.\end{aligned}


$$

Therefore,

$$


W \sim N(3\,050, 504).


$$

In order to find $P(W > 3\,000),$ we convert $W$ to a standard normal random variable by $z$-scoring:

$$


\begin{aligned}𝑃(𝑊>3\,000) & =𝑃(𝑍>\frac{3\,000−3\,050}{\sqrt{504}}) \\ & ≈𝑃(𝑍>−2.23) \\ & =𝑃(𝑍<2.23) \\ & =Φ(2.23)\end{aligned}


$$

Using the $z$-table, we see that

$$


\Phi(2.23)\approx 0.9871.


$$

Therefore,

$$


\begin{aligned}𝑃(𝑊>3\,000) & ≈Φ(2.23) \\ & =0.9871.\end{aligned}


$$
