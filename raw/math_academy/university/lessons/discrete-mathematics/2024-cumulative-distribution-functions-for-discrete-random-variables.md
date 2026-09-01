# Cumulative Distribution Functions for Discrete Random Variables

Source: https://www.mathacademy.com/topics/2024?courseId=109
Topic ID: 2024

## Prerequisites

- [Probability Mass Functions of Discrete Random Variables](./1290-probability-mass-functions-of-discrete-random-variables.md)
- [Increasing and Decreasing Functions](../../../high-school/traditional/lessons/algebra-i/1628-increasing-and-decreasing-functions.md)

## Lesson

### Introduction

The **cumulative distribution function** (or **CDF**) of a discrete random variable $X$ is a function $F(x)$ such that

$$



F(x) = P(X \leq x).



$$

Similar to a probability distribution function, a cumulative distribution function is another method that we can use to describe the distribution of a random variable.

To illustrate the usage of a cumulative distribution function in a concrete situation, suppose that the random variable $X$ represents the roll of a fair six-sided die. Then

- The probability of rolling a number less than or equal to $2$ (i.e., rolling a $1$ or a $2$) is So, we write $F(2) = \dfrac{1}{3}.$

- The probability of rolling a number less than or equal to $5$ (i.e. rolling a $1,$ $2,$ $3,$ $4,$ or $5$) is So, we write $F(5) = \dfrac{5}{6}.$

One benefit to using a cumulative distribution function is that it allows us to easily compute the probability of a random variable over an interval. In general, we have the following rule:

$$



P(a < X \leq b) = F(b) - F(a)



$$

Continuing the example above, if we want to calculate the probability that the roll of the six-sided die is greater than $2$ and less than or equal to $5,$ then we can use the rule as follows:

$$



\begin{aligned}𝑃(2<𝑋≤5) & =𝐹(5)−𝐹(2) \\ & =\frac{5}{6}−\frac{1}{3} \\ & =\frac{5}{6}−\frac{2}{6} \\ & =\frac{3}{6} \\ & =\frac{1}{2}\end{aligned}



$$

Indeed, the result is correct. The only numbers greater than $2$ and less than or equal to $5$ are $3,$ $4,$ and $5,$ and the probability of rolling any of these three numbers is $\dfrac{3}{6} = \dfrac{1}{2}.$

### Example: Computing a CDF Given the PMF

#### Question

Given that the discrete random variable $Y$ has the probability mass function $f(y),$ shown in the table below, and the cumulative distribution function $F(y),$ compute $F(2).$

#### Explanation

The cumulative distribution function of a discrete random variable $Y$ is the function $F(y)$ defined by

$$



F(y) = P(Y \leq y).



$$

So, we have

$$



\begin{aligned}𝐹(2) & =𝑃(𝑌≤2) \\ & =𝑃(𝑌∈{1,2}) \\ & =𝑃(𝑌=1)+𝑃(𝑌=2) \\ & =𝑓(1)+𝑓(2) \\ & =\frac{1}{2}+\frac{1}{8} \\ & =\frac{5}{8}.\end{aligned}



$$

### Example: Computing the Probability of an Event Given the CDF

#### Question

Given that the discrete random variable $X$ has the cumulative distribution function $F(x)$ shown in the table below, compute $P(X=5).$

#### Explanation

The cumulative distribution function of a discrete random variable $X$ is the function $F(x)$ defined by

$$



F(x) = P(X \leq x).



$$

So, we have

$$



\begin{aligned}𝐹(5) & =𝑃(𝑋≤5) \\ & =𝑃(𝑋∈{1,3,5}) \\ & =𝑃(𝑋=1)+𝑃(𝑋=3)+𝑃(𝑋=5) \\ & =𝑃(𝑋∈{1,3})+𝑃(𝑋=5) \\ & =𝑃(𝑋≤3)+𝑃(𝑋=5) \\ & =𝐹(3)+𝑃(𝑋=5).\end{aligned}



$$

Therefore,

$$



\begin{aligned}𝑃(𝑋=5) & =𝐹(5)−𝐹(3) \\ & =0.50−0.45 \\ & =0.05.\end{aligned}



$$

### Example: Computing a Probability Over an Interval Given the CDF

#### Question

Given that the discrete random variable $Y$ has the cumulative distribution function $F(y)$ shown in the table below, compute $P\left(2 \leq Y < 5 \right).$

#### Explanation

The cumulative distribution function of a discrete random variable $Y$ is the function $F(y)$ defined by

$$



F(y) = P(Y \leq y).



$$

To compute the probability of a random variable $Y$ over an interval, we can use the rule

$$



P(a < X \leq b) = F(b) - F(a).



$$

Here, we want to compute $P\left(2 \leq Y < 5 \right).$ However, this interval is stated in the form $a \leq Y < b,$ not $a < Y \leq b.$

So first, we must convert the interval $2 \leq Y < 5$ to the form $a < X \leq b.$ Looking at the given possible values of $Y,$ we see that $2 \leq Y$ is equivalent to $1 < Y,$ and $Y< 5$ is equivalent to $Y \leq 4.$ Therefore,

$$



\begin{aligned}𝑃(2≤𝑌<5) & =𝑃(1<𝑌≤4) \\ & =𝐹(4)−𝐹(1) \\ & =\frac{3}{4}−\frac{1}{4} \\ & =\frac{1}{2}.\end{aligned}



$$

### Computing Probabilities Involving Greater Than Symbols

So far, we've used cumulative distribution functions to compute probabilities of the form

$$



P(X \leq x) = F(x)



$$

and

$$



P(a < X \leq b) = F(b) - F(a).



$$

But what if we want to compute a probability of the form $P(X > a)?$ Is there a way to do this using the cumulative distribution function?

Indeed, there is. Recall the following rule of probability:

$$



P(X > a) = 1 - P(X\leq a)



$$

Substituting $P(X \leq a) = F(a)$ into the above formula, we have

$$



P(X > a) = 1-F(a).



$$

### Example: Computing a Probability Over an Interval Containing a Greater Than Symbol

#### Question

Given that the discrete random variable $X$ has the cumulative distribution function $F(x)$ shown in the table below, compute $P(X \gt 2).$

#### Explanation

The cumulative distribution function of a discrete random variable $X$ is the function $F(x)$ defined by

$$



F(x) = P(X \leq x).



$$

To solve the given problem, we can use the rule

$$



P(X > a) = 1 - P(X\leq a) = 1-F(a).



$$

In our case, we have

$$



\begin{aligned}𝑃(𝑋>2) & =1−𝑃(𝑋≤2) \\ & =1−𝐹(2) \\ & =1−0.6 \\ & =0.4.\end{aligned}



$$
