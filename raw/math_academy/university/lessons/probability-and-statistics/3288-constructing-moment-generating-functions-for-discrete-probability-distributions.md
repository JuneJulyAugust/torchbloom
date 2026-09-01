# Constructing Moment-Generating Functions for Discrete Probability Distributions

Source: https://www.mathacademy.com/topics/3288?courseId=73
Topic ID: 3288

## Prerequisites

- [Representing Functions as Power Series](../../../ap-courses/lessons/ap-calculus-bc/885-representing-functions-as-power-series.md)
- [Expanding a Binomial Using Binomial Coefficients](../../../high-school/integrated-math-honors/lessons/integrated-math-ii-honors/1156-expanding-a-binomial-using-binomial-coefficients.md)
- [The Discrete Uniform Distribution](./3010-the-discrete-uniform-distribution.md)
- [The Bernoulli Distribution](./3071-the-bernoulli-distribution.md)
- [The Negative Binomial Distribution](./3072-the-negative-binomial-distribution.md)
- [The Binomial Distribution](./3281-the-binomial-distribution.md)
- [The Poisson Distribution](./3282-the-poisson-distribution.md)
- [Moment-Generating Functions](./3401-moment-generating-functions.md)

## Lesson

### Introduction

Recall that if $X$ is a discrete random variable with probability mass function $f(x)$ and support $S,$ then the moment-generating function (or MGF) of $X$ is defined as

$$


M(t) = \textrm E \!\left[ e^{tX} \right] = \sum_{x \in S} f(x) e^{tx}.


$$

In this lesson, we'll construct moment-generating functions for some important discrete probability distributions, namely:

- the discrete uniform distribution

- the Poisson distribution

- the binomial distribution

- the geometric distribution

As we'll soon see, we can use the moment-generating functions to prove certain properties about these distributions.

Let's begin by considering the MGF of a uniformly distributed random variable.

### Example: MGFs of Discrete Uniform Random Variables

#### Question

Find the moment-generating function $M(t)$ of $X\sim U\{-3, 0, 3\}.$

#### Explanation

The moment-generating function of a discrete random variable $X$ is given by

$$


M(t) = \textrm E\! \left[ e^{tX} \right] = \sum_{x \in S} f(x) e^{tx}


$$

where $S$ is the support of $X,$ and $f(x)$ is its probability mass function.

Given that $X\sim U\{-3, 0, 3\},$ we have the following probability mass function:

Therefore,

$$


\begin{aligned}𝑀(𝑡) & =\underset{𝑥∈𝑆}{∑}𝑓(𝑥)𝑒^{𝑡𝑥} \\ & =\underset{𝑥∈{−3,0,3}}{∑}𝑓(𝑥)𝑒^{𝑡𝑥} \\ & =𝑓(−3)𝑒^{−3𝑡}+𝑓(0)𝑒^{0}+𝑓(3)𝑒^{3𝑡} \\ & =\frac{1}{3}𝑒^{−3𝑡}+\frac{1}{3}𝑒^{0}+\frac{1}{3}𝑒^{3𝑡} \\ & =\frac{1}{3}𝑒^{−3𝑡}+\frac{1}{3}+\frac{1}{3}𝑒^{3𝑡}\end{aligned}


$$

which is finite for every $t \in \mathbb{R}.$

### Example: MGFs of Poisson Random Variables

#### Question

Find the moment-generating function $M(t)$ of $X\sim \text{Po}(2).$

#### Explanation

The moment-generating function of a discrete random variable $X$ is given by

$$


M(t) = \textrm E\! \left[ e^{tX} \right] = \sum_{x \in S} f(x) e^{tx}


$$

where $S$ is the support of $X,$ and $f(x)$ is its probability mass function.

Given that $X\sim \text{Po}(2),$ we have the following probability mass function:

$$


f(x) = \dfrac{e^{-2}\cdot 2^x }{x!}, \qquad x=0,1,2,\ldots\,.


$$

Therefore,

$$


\begin{aligned}𝑀(𝑡) & =\underset{𝑥∈𝑆}{∑}𝑓(𝑥)𝑒^{𝑡𝑥} \\ & =\underset{𝑥∈{0,1,2,…}}{∑}𝑓(𝑥)𝑒^{𝑡𝑥} \\ & =𝑓(0)𝑒^{0}+𝑓(1)𝑒^{𝑡}+𝑓(2)𝑒^{2𝑡}+𝑓(3)𝑒^{3𝑡}+⋯ \\ & =\frac{𝑒^{−2}⋅2^{0}⋅𝑒^{0}}{0!}+\frac{𝑒^{−2}⋅2^{1}⋅𝑒^{𝑡}}{1!}+\frac{𝑒^{−2}⋅2^{2}⋅𝑒^{2𝑡}}{2!}+\frac{𝑒^{−2}⋅2^{3}⋅𝑒^{3𝑡}}{3!}+⋯ \\ & =𝑒^{−2}(\frac{2^{0}⋅𝑒^{0}}{0!}+\frac{2^{1}⋅𝑒^{𝑡}}{1!}+\frac{2^{2}⋅𝑒^{2𝑡}}{2!}+\frac{2^{3}⋅𝑒^{3𝑡}}{3!}+⋯) \\ & =𝑒^{−2}(1+\frac{2^{1}⋅𝑒^{𝑡}}{1!}+\frac{2^{2}⋅𝑒^{2𝑡}}{2!}+\frac{2^{3}⋅𝑒^{3𝑡}}{3!}+⋯) \\ & =𝑒^{−2}(1+\frac{2𝑒^{𝑡}}{1!}+\frac{(2𝑒^{𝑡})^{2}}{2!}+\frac{(2𝑒^{𝑡})^{3}}{3!}+⋯).\end{aligned}


$$

Now, recall that the Maclaurin expansion of $e^{f(x)}$ is

$$


e^{f(x)} = 1 + f(x) + \dfrac{f^2(x)}{2!} + \dfrac{f^3(x)}{3!} + \cdots .


$$

Therefore,

$$


\begin{aligned}𝑀(𝑡) & =𝑒^{−2}(1+\frac{2𝑒^{𝑡}}{1!}+\frac{(2𝑒^{𝑡})^{2}}{2!}+\frac{(2𝑒^{𝑡})^{3}}{3!}+⋯) \\ & =𝑒^{−2}⋅𝑒^{2𝑒^{𝑡}} \\ & =𝑒^{2𝑒^{𝑡}−2} \\ & =𝑒^{2(𝑒^{𝑡}−1)}\end{aligned}


$$

which is finite for every $t\in\mathbb R.$

### Example: MGFs of Binomial Random Variables

#### Question

Find the moment-generating function $M(t)$ of $X\sim B(6,0.7).$

#### Explanation

The moment-generating function of a discrete random variable $X$ is given by

$$


M(t) = \textrm E\! \left[ e^{tX} \right] = \sum_{x \in S} f(x) e^{tx}


$$

where $S$ is the support of $X,$ and $f(x)$ is its probability mass function.

Given that $X\sim B(6,0.7),$ we have the following probability mass function:

$$


f(x) = \binom{6}{x} (0.7)^x(0.3)^{6-x}, \qquad x=0,1,2,\ldots, 6.


$$

Therefore,

$$


\begin{aligned}𝑀(𝑡) & =\underset{𝑥∈𝑆}{∑}𝑓(𝑥)𝑒^{𝑡𝑥} \\ & =\underset{𝑥∈{0,1,2,…,6}}{∑}𝑓(𝑥)𝑒^{𝑡𝑥} \\ & =𝑓(0)𝑒^{0}+𝑓(1)𝑒^{𝑡}+𝑓(2)𝑒^{2𝑡}+⋯+𝑓(6)𝑒^{6𝑡} \\ & =(\frac{6}{0})(0.7)^{0}(0.3)^{6}𝑒^{0}+(\frac{6}{1})(0.7)^{1}(0.3)^{5}𝑒^{𝑡}+⋯+(\frac{6}{6})(0.7)^{6}(0.3)^{0}𝑒^{6𝑡} \\ & =(\frac{6}{0})(0.7𝑒^{𝑡})^{0}(0.3)^{6}+(\frac{6}{1})(0.7𝑒^{𝑡})(0.3)^{5}+⋯+(\frac{6}{6})(0.7𝑒^{𝑡})^{6}(0.3)^{0}.\end{aligned}


$$

Now, recall that the binomial expansion of $(a+b)^{6}$ is

$$


(a+b)^{6} = \binom{6}{0}a^0b^{6} + \binom{6}{1}a b^{5} + \cdots + \binom{6}{6}a^{6}b^{0}.


$$

Therefore,

$$


\begin{aligned}𝑀(𝑡) & =(\frac{6}{0})(0.7𝑒^{𝑡})^{0}(0.3)^{6}+(\frac{6}{1})(0.7𝑒^{𝑡})(0.3)^{5}+⋯+(\frac{6}{6})(0.7𝑒^{𝑡})^{6}(0.3)^{0} \\ & =(0.7𝑒^{𝑡}+0.3)^{6}\end{aligned}


$$

which is finite for every $t\in\mathbb R.$

### Example: MGFs of Geometric Random Variables

#### Question

Find the moment-generating function $M(t)$ of $X\sim \text{Geom}(0.1).$

#### Explanation

The moment-generating function of a discrete random variable $X$ is given by

$$


M(t) = \textrm E\! \left[ e^{tX} \right] = \sum_{x \in S} f(x) e^{tx}


$$

where $S$ is the support of $X,$ and $f(x)$ is its probability mass function.

Given that $X\sim \text{Geom}(0.1),$ we have the following probability mass function:

$$


f(x) = (0.1)(0.9)^{x-1}, \qquad x=1,2,3,\ldots\,.


$$

Therefore,

$$


\begin{aligned}𝑀(𝑡) & =\underset{𝑥∈𝑆}{∑}𝑓(𝑥)𝑒^{𝑡𝑥} \\ & =\underset{𝑥∈{1,2,3,…}}{∑}𝑓(𝑥)𝑒^{𝑡𝑥} \\ & =𝑓(1)𝑒^{𝑡}+𝑓(2)𝑒^{2𝑡}+𝑓(3)𝑒^{3𝑡}+⋯ \\ & =(0.1)𝑒^{𝑡}+(0.1)(0.9)𝑒^{2𝑡}+(0.1)(0.9)^{2}𝑒^{3𝑡}+⋯ \\ & =(0.1)𝑒^{𝑡}(1+(0.9)𝑒^{𝑡}+(0.9)^{2}𝑒^{2𝑡}+⋯) \\ & =(0.1)𝑒^{𝑡}(1+0.9𝑒^{𝑡}+(0.9𝑒^{𝑡})^{2}+⋯).\end{aligned}


$$

Now, recall the sum of an infinite geometric series for $|x| < 1{:}$

$$


1 + x + x^2 + x^3 + \cdots = \dfrac{1}{1-x}


$$

Therefore, assuming $0.9 e^{t} < 1,$ we have

$$


\begin{aligned}𝑀(𝑡) & =(0.1)𝑒^{𝑡}(1+0.9𝑒^{𝑡}+(0.9𝑒^{𝑡})^{2}+⋯) \\ & =(0.1)𝑒^{𝑡}⋅\frac{1}{1−0.9𝑒^{𝑡}} \\ & =\frac{0.1𝑒^{𝑡}}{1−0.9𝑒^{𝑡}}\end{aligned}


$$

valid for $0.9 e^{t} < 1,$ i.e., $t < -\ln (0.9).$

### A Summary of the MGFs for Some Important Discrete Distributions

The table below gives the moment-generating functions $M(t)$ of some common discrete probability distributions.

We can make a few observations from this table:

- Notice the similarity between the MGFs of the Bernoulli and binomial random variables. This is reflective of the relationship between the distributions: $\text{Bernoulli}(p)$ gives the probability of success after one Bernoulli trial, whereas $B(n,p)$ gives the probability of $x$ successes after $n$ Bernoulli trials.

- Similarly, there is a similarity between the MGFs of the geometric and negative binomial distributions. Again, this is reflective of the relationship between the distributions: $\text{Geom}(p)$ gives the number of Bernoulli trials until the first success, whereas $\text{NB}(r,p)$ models the number of Bernoulli trials until the $r$th success.

In a future lesson, we will discuss the precise relationships between these MGF pairs.
