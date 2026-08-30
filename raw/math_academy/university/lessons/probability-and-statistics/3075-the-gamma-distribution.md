# The Gamma Distribution

Source: https://www.mathacademy.com/topics/3075?courseId=73
Topic ID: 3075

## Prerequisites

- [Mean and Variance of the Exponential Distribution](./3275-mean-and-variance-of-the-exponential-distribution.md)
- [The Gamma Function](./3289-the-gamma-function.md)

## Lesson

### Introduction

The **gamma distribution** is a two-parameter continuous probability distribution with parameters $\alpha,$ called the **shape parameter**, and $\lambda,$ called the **rate parameter**.

If a random variable $X$ is gamma-distributed with shape parameter $\alpha$ and rate parameter $\lambda,$ we write $X \sim \Gamma(\alpha, \lambda)$.

The probability density function of $X\sim \Gamma(\alpha, \lambda)$ is given by

$$


\begin{aligned}\frac{𝜆^{𝛼}}{Γ(𝛼)}𝑥^{𝛼−1}𝑒^{−𝜆𝑥},\, & 𝑥>0 \\ 0, & otherwise\end{aligned}


$$

where $\Gamma(\alpha)$ is the gamma function.

We can use the gamma distribution to model the amount of continuous space or time that passes until the $\alpha$th event occurs in a Poisson process with success rate $\lambda.$

For example, suppose that a call center receives $6$ calls every minute on average, and we're interested to know how many minutes $X$ will pass until the $30$th call is received. Then,

- $\alpha = 30,$ because we're interested in the number of minutes that pass until the $30$th call is received, and

- $\lambda = 6,$ because the center receives an average of $6$ calls every minute.

In this situation, we can write $X\sim\Gamma(30, 6).$

### Relationship to the Exponential Distribution

The probability density function of $X\sim \Gamma(\alpha, \lambda)$ is given by

$$


\begin{aligned}\frac{𝜆^{𝛼}}{Γ(𝛼)}𝑥^{𝛼−1}𝑒^{−𝜆𝑥},\, & 𝑥>0 \\ 0, & otherwise.\end{aligned}


$$

Notice that if we set $\alpha=1$, we obtain

$$


\begin{aligned}𝜆𝑒^{−𝜆𝑥},\, & 𝑥>0 \\ 0, & otherwise.\end{aligned}


$$

This is the probability density function of an exponential distribution with rate $\lambda.$ Thus,

$$


\Gamma(1, \lambda)=\text{Exp}(\lambda).


$$

In this sense, the gamma distribution extends the exponential distribution. Let's go back to our call center example to put this idea into context.

Recall that if a call center receives $6$ calls every minute on average, and we're interested to know how many minutes $X$ will pass until the call center receives the $\alpha$th call, then $X\sim \Gamma(\alpha, 6).$

Now, by setting $\alpha = 1,$ we specify that we're interested in the total number of minutes that pass until the *first* call is received. But this can simply be modeled using the random variable $X\sim \text{Exp}(6).$

In general, if $X_1, X_2, \ldots X_{\alpha} \sim \text{Exp}(\lambda)$ are independent and identically distributed, then

$$


X_1+X_2+\cdots + X_{\alpha} \sim \Gamma(\alpha, \lambda).


$$

### Example: Computing a Probability Using the Gamma Distribution

#### Question

Let $\Gamma(\alpha, \lambda)$ denote the gamma distribution with shape parameter $\alpha$ and rate parameter $\lambda.$ Given that $X \sim \Gamma\left(4,\dfrac{1}{5}\right),$ express $P(X < 1)$ as an integral.

**

$$


\begin{aligned}\frac{𝜆^{𝛼}}{Γ(𝛼)}𝑥^{𝛼−1}𝑒^{−𝜆𝑥}, & 𝑥>0 \\ 0, & otherwise\end{aligned}


$$

**

#### Explanation

A gamma random variable $X \sim \Gamma(\alpha, \lambda)$ with shape parameter $\alpha$ and rate parameter $\lambda$ has the following probability density function:

$$


\begin{aligned}\frac{𝜆^{𝛼}}{Γ(𝛼)}𝑥^{𝛼−1}𝑒^{−𝜆𝑥}, & 𝑥>0 \\ 0, & otherwise\end{aligned}


$$

We're given that $X \sim \Gamma\left(4,\dfrac{1}{5}\right),$ so $X$ has the following probability density function:

$$


\begin{aligned}\frac{(\frac{1}{5})^{4}}{5}𝑥^{3}𝑒^{−𝑥/5}, & 𝑥>0 \\ 0, & otherwise\end{aligned}


$$

Recalling that $\Gamma(n) = (n-1)!$ for any natural number $n \geq 1,$ we have

$$


\Gamma(4) = 3! = 6.


$$

So, the probability distribution becomes

$$


\begin{aligned}\frac{1}{3\,750}𝑥^{3}𝑒^{−𝑥/5}, & 𝑥>0 \\ 0, & otherwise.\end{aligned}


$$

Finally, we can express $P\left(X < 1\right)$ as follows:

$$


\begin{aligned}𝑃(𝑋<1) & =∫_{10}𝑓(𝑥)\,d𝑥 \\ & =∫_{10}\frac{1}{3\,750}𝑥^{3}𝑒^{−𝑥/5}\,d𝑥 \\ & =\frac{1}{3\,750}∫_{10}𝑥^{3}𝑒^{−𝑥/5}\,d𝑥\end{aligned}


$$

### The Mean and Variance of the Gamma Distribution

If $X \sim \Gamma(\alpha, \lambda)$, then we can show that the following formulas give the mean and variance of $X$:

$$


\textrm E[X]=\dfrac{\alpha}{\lambda},\qquad \text{Var}[X]=\dfrac{\alpha}{\lambda^2}


$$

Notice that if we set $\alpha = 1,$ we get the same results as those for an exponential distribution with rate parameter $\lambda.$

The formula for the mean of a gamma distribution is quite intuitive. Let's illustrate using an example.

Recall that if a call center receives $6$ calls every minute on average, and we're interested to know how much time $X$ will pass until the call center receives the following $30$ calls, then $X\sim \Gamma(30, 6).$

Computing $\textrm E[X]$ using the above formula, we have

$$


\textrm E[X] = \dfrac{30}{6} = 5.


$$

This result makes intuitive sense. If the call center receives an average of $6$ calls per minute, we expect it to take an average of $5$ minutes to receive $30$ calls.

### Example: The Mean and Variance of the Gamma Distribution

#### Question

Let $\Gamma(\alpha, \lambda)$ denote the gamma distribution with shape parameter $\alpha$ and rate parameter $\lambda.$ Given that $X \sim \Gamma(3,4),$ compute $\textrm E[X]$ and $\text{Var}[X].$

#### Explanation

Given a gamma random variable $X \sim \Gamma(\alpha, \lambda)$ with shape parameter $\alpha$ and rate parameter $\lambda,$ the expected value and the variance of $X$ are given by

$$


\begin{aligned}E[𝑋]=\frac{𝛼}{𝜆},\,Var[𝑋]=\frac{𝛼}{𝜆^{2}}.\end{aligned}


$$

In our case, $\alpha = 3$ and $\lambda = 4.$ Therefore,

$$


\begin{aligned}E[𝑋] & =\frac{3}{4} \\ Var[𝑋] & =\frac{3}{4^{2}}=\frac{3}{16}.\end{aligned}


$$

### Example: Modeling With the Gamma Distribution

#### Question

At a cafe, $10$ customers arrive per hour on average. What is the probability that the $4$th customer will arrive within half an hour of the cafe opening? Round your answer to $3$ decimal places. You may assume arrivals occur continuously in time, independently, and at a constant average rate.

**

$$


\int_0^{0.5} x^3 e^{-10x} \, \textrm dx \approx 0.000\,441.


$$

**

$$


\begin{aligned}\frac{𝜆^{𝛼}}{Γ(𝛼)}𝑥^{𝛼−1}𝑒^{−𝜆𝑥}, & 𝑥>0 \\ 0, & otherwise\end{aligned}


$$

**

#### Explanation

If the random variable $X$ measures the amount of continuous space or time until the $\alpha$th event occurs in a Poisson process with rate $\lambda,$ then $X \sim \Gamma(\alpha, \lambda).$

Let $X$ be the number of hours until the $4$th customer arrives. Since the rate at which customers arrive is $\lambda = 10$ per hour, and we want to measure the number of hours until the $\alpha = 4$th customer arrives, we have

$$


X \sim \Gamma \left( 4, 10 \right).


$$

We want to find the probability that the $10$th customer will arrive within half an hour of the cafe opening, which we can express as $P(X \leq 0.5).$

We first need to construct the probability density function to compute this probability. In general, a gamma random variable $X \sim \Gamma(\alpha, \lambda)$ with shape parameter $\alpha$ and rate parameter $\lambda$ has the following probability density function:

$$


\begin{aligned}\frac{𝜆^{𝛼}}{Γ(𝛼)}𝑥^{𝛼−1}𝑒^{−𝜆𝑥}, & 𝑥>0 \\ 0, & otherwise\end{aligned}


$$

In our case, we have that $X \sim \Gamma \left(4, 10 \right)$ so $X$ has the following probability density function:

$$


\begin{aligned}\frac{10^{4}}{Γ(4)}𝑥^{3}𝑒^{−10𝑥}, & 𝑥>0 \\ 0, & otherwise\end{aligned}


$$

Recalling that $\Gamma(n) = (n-1)!$ for any natural number $n \geq 1,$ we have

$$


\Gamma(4)= 3! = 6.


$$

So, the probability distribution becomes

$$


\begin{aligned}\frac{5\,000}{3}𝑥^{3}𝑒^{−10𝑥}, & 𝑥>0 \\ 0, & otherwise.\end{aligned}


$$

Finally, we compute $P\left(X < 0.5 \right)$ as follows:

$$


\begin{aligned}𝑃(𝑋<0.5) & =∫_{0.50}𝑓(𝑥)\,d𝑥 \\ & =∫_{0.50}\frac{5\,000}{3}𝑥^{3}𝑒^{−10𝑥}\,d𝑥 \\ & =\frac{5\,000}{3}∫_{0.50}𝑥^{3}𝑒^{−10𝑥}\,d𝑥 \\ & ≈\frac{5\,000}{3}⋅(0.000\,441) \\ & ≈0.735\end{aligned}


$$
