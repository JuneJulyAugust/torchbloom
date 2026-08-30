# Mean and Variance of the Negative Binomial Distribution

Source: https://www.mathacademy.com/topics/3273?courseId=73
Topic ID: 3273

## Prerequisites

- [Mean and Variance of the Geometric Distribution](./2992-mean-and-variance-of-the-geometric-distribution.md)
- [Variance of Sums of Independent Random Variables](./3062-variance-of-sums-of-independent-random-variables.md)
- [Modeling With the Negative Binomial Distribution](./3285-modeling-with-the-negative-binomial-distribution.md)

## Lesson

### Introduction

Suppose the random variable $X$ follows a negative binomial distribution with $r$ successes and success probability $p{:}$

$$


X \sim \text{NB}(r, p)


$$

The expected value of $X$ is given by

$$


\textrm E[X] = \dfrac{r}{p}.


$$

To understand this result, we can compare it to the expected value of a geometric random variable:

$$


X_{\text{G}}\sim \text{Geom}(p)


$$

In a previous lesson, we showed that

$$


\textrm E[X_{\text{G}}] = \dfrac{1}{p}.


$$

Remember that a geometric random variable is a negative binomial random variable with $r=1$ successes. In other words:

- $X_{\textrm G}$ measures the number of trials needed for the *first* success, while

- $X$ measures the number of trials for $r$ successes.

Thus, $X$ can be thought of as the *sum* of $r$ independent geometric random variables:

$$


X = \underbrace{X_{\text{G}_1} + X_{\text{G}_2} +\cdots + X_{\text{G}_r}}_{r \text{ times}}


$$

where $X_{\text{G}_1}, X_{\text{G}_2}, \ldots, X_{\text{G}_r} \sim \text{Geom}(p)$ (note that this can be proved formally).

We can interpret our result for the expected value of $\text{NB}(r,p)$ as follows:

- If the expected value of $X_{\text{G}}$ is $\dfrac1p,$ then there should be (on average) $\dfrac1p$ trials to reach the first success. For example, if $X_{\text{G}}$ represents the number of times a fair coin is spun before the first head, we have $p = \dfrac12,$ and therefore, we'd expect (on average) two trials to reach the first success:

- Now, since $X\sim \text{NB}(r, p),$ there should be $r\cdot \dfrac{1}{p} = \dfrac{r}{p}$ trials (on average) before the first $r$ successes. For example, if $X$ represents the number of times a fair coin is spun before the *five* heads, we have $r=5$ and $p = \dfrac12.$ Therefore, we'd expect ten trials to achieve the first five successes:

### Example: Finding the Expected Value of a Negative Binomial Distribution

#### Question

Given that $X\sim \text{NB}\left(4, 0.25\right),$ what is $\textrm E[X]?$

#### Explanation

In general, if $X \sim \text{NB}(r, p)$ is a negative binomial random variable, then

$$


\textrm E[X] = \dfrac{r}{p}.


$$

So, for our random variable $X \sim \text{NB}\left(4, 0.25\right),$ we have the following expected value:

$$


\textrm E[X] = \dfrac{4}{0.25} = 16


$$

### Example: Finding the Expected Value of a Negative Binomial Distribution in Context

#### Question

A fair die is rolled until five $6$s are obtained. What is the expected number of rolls?

#### Explanation

Let $X$ represent the number of rolls until the fifth $6$ is obtained. Rolling a die is a Bernoulli trial, and we wish to find the number of repeated trials until we reach $5$ successes. So, we can model $X$ using the negative binomial distribution:

$$


X \sim \text{NB}\left(5, \dfrac16\right).


$$

We wish to compute $\textrm E[X].$ In general, if $X \sim \text{NB}(r, p),$ then

$$


\textrm E[X] = \dfrac{r}{p}.


$$

So, for our random variable $X \sim \text{NB}\left(5, \dfrac16\right),$ we have the following expected value:

$$


\textrm E[X] = \dfrac{5}{\left(\dfrac16\right)} = 30


$$

Therefore, the expected number of rolls is $30.$

### The Variance of a Negative Binomial Random Variable

The variance of $X$ is determined by the following formula:

$$


\text{Var}[X] = \dfrac{r(1-p)}{p^2}


$$

Again, it's worth comparing this to the variance of $X_{\textrm G}\sim \text{Geom}(p).$ Recall that

$$


\text{Var}[X_{\textrm G}] = \dfrac{(1-p)}{p^2}.


$$

It's easy to see how the two rules are related. First, we can think of $X$ as a sum of $r$ independent geometric random variables:

$$


X = \underbrace{X_{\text{G}_1} + X_{\text{G}_2} +\cdots + X_{\text{G}_r}}_{r \text{ times}}


$$

where $X_{\text{G}_1}, X_{\text{G}_2}, \ldots, X_{\text{G}_r} \sim \text{Geom}(p).$ By the properties of variance for sums of independent random variables, we have

$$


\begin{aligned}Var[𝑋] & =Var[𝑋_{G_{1}}]+Var[𝑋_{G_{2}}]+⋯+Var[𝑋_{G_{𝑟}}] \\ & =\underset{𝑟 times}{\underset{}{\frac{(1−𝑝)}{𝑝^{2}}+\frac{(1−𝑝)}{𝑝^{2}}+⋯+\frac{(1−𝑝)}{𝑝^{2}}}} \\ & =\frac{𝑟(1−𝑝)}{𝑝^{2}}.\end{aligned}


$$

### Example: Finding the Variance of a Negative Binomial Distribution

#### Question

Given that $X\sim \text{NB}\left(4, 0.25\right),$ what is $\text{Var}[X]?$

#### Explanation

In general, if $X \sim \text{NB}(r, p)$ is a negative binomial random variable, then

$$


\text{Var}[X] = \dfrac{r(1-p)}{p^2}.


$$

So, for our random variable $X \sim \text{NB}\left(4, 0.25\right),$ we have the following variance:

$$


\text{Var}[X] = \dfrac{4\left(0.75\right)}{\left(0.25\right)^2} = 48


$$

### Example: Finding the Variance of a Negative Binomial Distribution in Context

#### Question

A fair die is rolled until an even number is obtained $14$ times. What is the variance in the number of rolls?

#### Explanation

Let $X$ represent the number of rolls until the $14$th even number is obtained. Rolling a die is a Bernoulli trial, and we wish to find the number of repeated trials until we reach $14$ successes. So, we can model $X$ using the negative binomial distribution: $X \sim NB\left(14, 0.5\right).$

We wish to compute $\text{Var}[X].$ In general, if $X \sim \text{NB}(r, p),$ then

$$


\text{Var}[X] = \dfrac{r(1-p)}{p^2}.


$$

So, for our random variable $X \sim \text{NB}\left(14, 0.5\right),$ we have the following variance:

$$


\text{Var}[X] = \dfrac{14(0.5)}{(0.5)^2} = 28


$$

Therefore, the variance is $28.$
