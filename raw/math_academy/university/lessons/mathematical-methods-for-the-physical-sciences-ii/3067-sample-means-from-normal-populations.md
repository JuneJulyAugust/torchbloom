# Sample Means From Normal Populations

Source: https://www.mathacademy.com/topics/3067?courseId=155
Topic ID: 3067

## Prerequisites

- [Variance of Sample Means](./3013-variance-of-sample-means.md)
- [I.I.D Normal Random Variables](./3859-i-i-d-normal-random-variables.md)

## Lesson

### Introduction

Let $X_1, X_2, \ldots, X_{n}$ be a random sample of size $n$ drawn from a normal population $N(\mu,\sigma^2)$ with mean $\mu$ and variance $\sigma^2.$ In other words,

$$


X_1, X_2, \ldots, X_{n} \sim N(\mu,\sigma^2).


$$

In this case, we can easily determine the sampling distribution of the sample mean

$$


\overline{X} = \dfrac{1}{n} \sum\limits_{i=1}^n X_i.


$$

Recall the following:

- The sum of $n$ independent and identically distributed normal random variables is normally distributed. Thus, is normally distributed.

- A normally distributed random variable scaled by a constant factor is normally distributed. Thus, is normally distributed.

Also, we previously saw that the expected value of the sample mean equals the population mean, i.e.,

$$


\textrm{E}[\overline{X}] = \mu,


$$

and the variance of the sample mean is

$$


\textrm{Var}[\overline{X}] = \dfrac{\sigma^2}{n}.


$$

Putting all of this together, we obtain that

$$


\overline{X} \sim N\left(\mu, \dfrac{\sigma^2}{n}\right),


$$

In other words, the sample mean $\overline{X}$ is normally distributed with mean $\mu$ and variance $\dfrac{\sigma^2}{n}.$

### Example: Stating the Distribution of the Sample Mean

#### Question

Given that $X_1, X_2, \ldots, X_{28} \sim N(8, 14^2)$ is a random sample of size $n = 28$ from a normal population, what is the distribution of the sample mean $\overline{X}?$

#### Explanation

If $X_1, X_2, \ldots, X_n$ is a random sample of size $n$ from a normal population, where

$$


X_i \sim N(\mu, \sigma^2), \qquad 1\leq i \leq n,


$$

then the sample mean $\overline{X}$ has the distribution

$$


\overline{X} \sim N\left(\mu, \dfrac{\sigma^2}{n}\right).


$$

In our case, we have

$$


n = 28, \qquad \mu = 8, \qquad \sigma = 14.


$$

Therefore, the distribution of the sample mean $\overline{X}$ is

$$


\begin{aligned}\overset{𝑋}{} & ∼𝑁\,(8,\frac{14^{2}}{28}) \\ & ∼𝑁(8,7).\end{aligned}


$$

### Example: Calculating a Probability Involving a Sample Mean

#### Question

Given that $X_1, X_2, \ldots,X_{100} \sim N(-4, 20^2)$ is a random sample of size $100$ from a normal population, calculate $P(-4.3 \lt \overline{X} \lt -3.9).$

**

#### Explanation

If $X_1, X_2, \ldots, X_n$ is a random sample of size $n$ from a normal population, where

$$


X_i \sim N(\mu, \sigma^2), \qquad 1\leq i\leq n,


$$

then the sample mean $\overline{X}$ has the distribution

$$


\overline{X} \sim N\left(\mu, \dfrac{\sigma^2}{n}\right).


$$

Therefore, the distribution of the sample mean $\overline{X}$ is

$$


\begin{aligned}\overset{𝑋}{} & ∼𝑁\,(−4,\frac{20^{2}}{100}) \\ & ∼𝑁(−4,4).\end{aligned}


$$

We're required to find $P(-4.3 \lt \overline{X} \lt -3.9).$

First, we transform $X$ into a standard normal random variable $Z$ by $z$-scoring:

$$


\begin{aligned}𝑃(−4.3<\overset{𝑋}{}<−3.9) & =𝑃(\frac{−4.3−(−4)}{\sqrt{√4}}<𝑍<\frac{−3.9−(−4)}{\sqrt{√4}}) \\ & =𝑃(−0.15<𝑍<0.05) \\ & =Φ(0.05)−Φ(−0.15)\end{aligned}


$$

From the table, we have

$$


\begin{aligned}Φ(0.05)=0.5199, \\ Φ(−0.15)=0.4404.\end{aligned}


$$

Therefore,

$$


\begin{aligned}𝑃(−0.15<𝑍<0.05) & =Φ(0.05)−Φ(−0.15) \\ & =0.5199−0.4404 \\ & =0.0795.\end{aligned}


$$

### Example: Calculating a Probability Involving a Sample Mean in Context

#### Question

The diastolic blood pressure of adult men in a given population is normally distributed with a mean of $75\,\text{mm}\,\text{Hg}$ and a standard deviation of $10\,\text{mm}\,\text{Hg}.$ Suppose $10$ men are selected at random. What is the probability that the mean diastolic blood pressure for this sample will be less than $70\,\text{mm}\,\text{Hg}?$

**

#### Explanation

If $X_1,X_2,\ldots,X_n$ is a random sample of size $n$ from a normal population, where

$$


X_i\sim N(\mu, \sigma^2), \qquad 1\leq i\leq n,


$$

then the sample mean $\overline{X}$ has the distribution

$$


\overline{X}\sim N\left(\mu, \dfrac{\sigma^2}{n}\right).


$$

We're told that the population mean $\mu=75,$ the population standard deviation $\sigma = 10,$ and that the sample size $n=10.$ Therefore, the distribution of the sample mean $\overline{X}$ is

$$


\begin{aligned}\overset{𝑋}{} & ∼𝑁\,(75,\frac{10^{2}}{10}) \\ & ∼𝑁(75,10).\end{aligned}


$$

We're required to find $P(\overline{X} \lt 70).$

First, we transform $X$ into a standard normal random variable $Z$ by $z$-scoring:

$$


\begin{aligned}𝑃(\overset{𝑋}{}<70) & =𝑃(𝑍<\frac{70−75}{\sqrt{√10}}) \\ & ≈𝑃(𝑍<−1.58) \\ & =Φ(−1.58)\end{aligned}


$$

From the table, we have

$$


\begin{aligned}Φ(−1.58) & =0.0571.\end{aligned}


$$

Therefore,

$$


\begin{aligned}𝑃(\overset{𝑋}{}<70) & =Φ(−1.58) \\ & =0.0571.\end{aligned}


$$
