# Modeling With Continuous Uniform Distributions

Source: https://www.mathacademy.com/topics/2990?courseId=73
Topic ID: 2990

## Prerequisites

- [Mean and Variance of the Continuous Uniform Distribution](./3277-mean-and-variance-of-the-continuous-uniform-distribution.md)

## Lesson

### Introduction

In general, if $X \sim U[a,b]$ is uniformly distributed, then $X$ has the following probability density function:

$$


\begin{aligned}\frac{1}{𝑏−𝑎}, & 𝑎≤𝑥≤𝑏 \\ 0, & otherwise\end{aligned}


$$

We can use a continuous uniform distribution to model situations where all possible outcomes on a finite interval are equally likely.

For instance, suppose a dental receptionist wants to model the waiting time of a randomly selected patient. After observing a number of patients over several days, the receptionist notices that the waiting time is uniformly distributed between $6$ and $14$ minutes, inclusive.

Then, by letting $X$ be the amount of time a randomly selected patient spends waiting, we can model the waiting time using the continuous uniform distribution:

$$


X \sim U[6,14]


$$

Therefore, $X$ has the following probability density function:

$$


\begin{aligned}\frac{1}{8}, & 6≤𝑥≤14 \\ 0, & otherwise\end{aligned}


$$

With this model, we can now make predictions about patient waiting times.

For example, the probability that a randomly selected patient waits longer than $9$ minutes is equal to

$$


\begin{aligned}𝑃(𝑋≥9) & =∫_{149}^{}\frac{1}{8}\,d𝑥 \\ & =\frac{1}{8}∫_{149}^{}\,d𝑥 \\ & =\frac{1}{8}[𝑥]_{149}^{} \\ & =\frac{1}{8}[14−9] \\ & =\frac{5}{8}.\end{aligned}


$$

We can also calculate the mean waiting time by finding the expected value of $X\mathbin{:}$

$$


\begin{aligned}E[𝑋] & =\frac{𝑎+𝑏}{2} \\ & =\frac{6+14}{2} \\ & =10\end{aligned}


$$

Therefore, the mean waiting time is $10$ minutes.

### Example: Calculating a Probability in Context

#### Question

The duration of a radio program is uniformly distributed between $27$ and $34$ minutes, inclusive. What is the probability that a randomly chosen program lasts less than $30$ minutes?

#### Explanation

Let $X$ represent the duration of the radio program. From the problem statement, we know that $X \sim U[27,34],$ and we wish to compute $P(X < 30).$

In general, if $X \sim U[a,b],$ then $X$ has the following probability density function:

$$


\begin{aligned}\frac{1}{𝑏−𝑎}, & 𝑎≤𝑥≤𝑏 \\ 0, & otherwise\end{aligned}


$$

So, for our random variable $X \sim U[27,34],$ we have the following probability density function:

$$


\begin{aligned}\frac{1}{7}, & 27≤𝑥≤34 \\ 0, & otherwise\end{aligned}


$$

Therefore,

$$


\begin{aligned}𝑃(𝑋<30) & =∫_{3027}^{}𝑓(𝑥)\,d𝑥 \\ & =∫_{3027}^{}\frac{1}{7}\,d𝑥 \\ & =\frac{𝑥}{7}_{3027}^{} \\ & =\frac{30}{7}−\frac{27}{7} \\ & =\frac{3}{7}.\end{aligned}


$$

### Example: Calculating an Expected Value in Context

#### Question

A video game randomly generates an obstacle the player has to avoid. The obstacle's $x$-coordinate is uniformly distributed along a segment whose endpoints have $x$-coordinates of $-6$ and $12.$ What is the mean $x$-coordinate of the obstacle?

#### Explanation

Let $X$ represent the $x$-coordinate of a randomly generated obstacle. From the problem statement, we know that $X \sim U[-6,12],$ and we wish to compute $\textrm E[X].$

In general, if $X \sim U[a,b],$ then $X$ has the following expected value:

$$


\textrm E[X] = \dfrac{a+b}{2}


$$

So, for our random variable $X \sim U[-6,12],$ we have the following expected value:

$$


\textrm E[X] = \dfrac{-6+12}{2} = 3


$$

Therefore, the mean $x$-coordinate is $3.$

### Example: Calculating a Variance in Context

#### Question

A museum manager notices that the minimum visiting time of visitors to the museum is $1.5$ hours, whereas the maximum time is $4.5$ hours. If the visiting time is uniformly distributed, what is its variance?

#### Explanation

Let $X$ represent the visiting time of a randomly chosen visitor. From the problem statement, we know that $X \sim U[1.5,4.5],$ and we wish to compute $\textrm{Var}[X].$

In general, if $X \sim U[a,b],$ then $X$ has the following variance:

$$


\textrm{Var}[X] = \dfrac{(b-a)^2}{12}


$$

So, for our random variable $X \sim U[1.5,4.5],$ we have the following variance:

$$


\textrm{Var}[X] = \dfrac{(4.5-1.5)^2}{12} = \dfrac{9}{12} = \dfrac{3}{4}


$$

Therefore, the variance is $\dfrac{3}{4}\,\textrm{hr}^2.$
