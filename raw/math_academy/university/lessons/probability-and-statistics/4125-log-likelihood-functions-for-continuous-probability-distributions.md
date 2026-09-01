# Log-Likelihood Functions for Continuous Probability Distributions

Source: https://www.mathacademy.com/topics/4125?courseId=73
Topic ID: 4125

## Prerequisites

- [Likelihood Functions for Continuous Probability Distributions](./4123-likelihood-functions-for-continuous-probability-distributions.md)
- [Log-Likelihood Functions for Discrete Probability Distributions](./4124-log-likelihood-functions-for-discrete-probability-distributions.md)

## Lesson

### Introduction

Recall that if $X_1, X_2, \ldots, X_{n}$ are independent and identically distributed *continuous* random variables with probability density function $f(x; \theta),$ then the likelihood function $L(\theta)$ of a random sample $x_1, x_2, \ldots, x_n$ is given by

$$


L(\theta) = \displaystyle\prod_{i=1}^n f(x_i;\,\theta)


$$

where $f(x;\theta)$ is the probability density function of $X_i$ for $i=1,2,\ldots, n,$ and $\theta$ is an unknown parameter.

Similar to the case of discrete random variables, the **log-likelihood function** is given by

$$


\begin{aligned}𝑙(𝜃) & =ln⁡(𝐿(𝜃)) \\ & =ln⁡(\underset{\underset{𝑖=1}{∏}}{\overset{}{𝑛}}𝑓(𝑥_{𝑖};\,𝜃)) \\ & =ln⁡(𝑓(𝑥_{1};\,𝜃)⋅𝑓(𝑥_{2};\,𝜃)⋯𝑓(𝑥_{𝑛};\,𝜃)) \\ & =ln⁡(𝑓(𝑥_{1};\,𝜃))+ln⁡(𝑓(𝑥_{2};\,𝜃))+⋯+ln⁡(𝑓(𝑥_{𝑛};\,𝜃)) \\ & =\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}ln⁡(𝑓(𝑥_{𝑖};\,𝜃)).\end{aligned}


$$

Let's get some practice at calculating log-likelihood functions for some continuous random variables.

### Example: Log-Likelihood Functions for Continuous Random Variables

#### Question

Let $X_1, X_2, X_3,X_4$ be I.I.D. random variables with probability density function

$$


f(x) = \theta x^{-\theta-1}, \qquad x \geq 1,


$$

where $\theta$ is an unknown parameter. Find the log-likelihood function of the sample $1.3, \, 2.4, \, 1.0,\, 1.7.$

#### Explanation

Recall that if $X_1, X_2, \ldots, X_{n}$ are independent and identically distributed continuous random variables with probability density function $f(x; \theta),$ where $\theta$ is an unknown parameter, then the log-likelihood function of a random sample $x_1, x_2, \ldots, x_n$ is

$$


\begin{aligned}𝑙(𝜃) & =ln⁡𝐿(𝜃) \\ & =ln⁡(\underset{\underset{𝑖=1}{∏}}{\overset{}{𝑛}}𝑓(𝑥_{𝑖};𝜃)) \\ & =\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}ln⁡(𝑓(𝑥_{𝑖};𝜃)).\end{aligned}


$$

In our case, we are given a sample of $n=4$ independent random variables with unknown parameter $\theta,$ for which the probability density function is

$$


f(x) = \theta x^{-\theta-1}, \qquad x \geq 1.


$$

First, let's write down the log-density function:

$$


\begin{aligned}ln⁡𝑓(𝑥;𝜃) & =ln⁡(𝜃𝑥^{−𝜃−1}) \\ & =ln⁡𝜃+ln⁡(𝑥^{−(𝜃+1)}) \\ & =ln⁡𝜃−(𝜃+1)ln⁡𝑥.\end{aligned}


$$

Now, we can calculate the log-likelihood function as follows:

$$


\begin{aligned}𝑙(𝜃) & =\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}(ln⁡𝜃−(𝜃+1)ln⁡𝑥_{𝑖}) \\ & =\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}ln⁡𝜃−\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}(𝜃+1)ln⁡𝑥_{𝑖} \\ & =ln⁡𝜃\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}1−(𝜃+1)\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}ln⁡𝑥_{𝑖} \\ & =𝑛ln⁡𝜃−(𝜃+1)\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}ln⁡𝑥_{𝑖}\end{aligned}


$$

For our sample, we have that $n=4,$ and

$$


\begin{aligned}\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}ln⁡𝑥_{𝑖} & =ln⁡1.3+ln⁡2.4+ln⁡1.0+ln⁡1.7≈1.67.\end{aligned}


$$

Therefore,

$$


\begin{aligned}𝑙(𝜃) & ≈4ln⁡𝜃−(𝜃+1)⋅1.67 \\ & =4ln⁡𝜃−1.67(𝜃+1).\end{aligned}


$$

### Example: Log-Likelihood Functions for Exponential Random Variables

#### Question

Suppose $X_1, X_2, X_3, X_4, X_5$ is an I.I.D random sample with $X_i \sim \text{Exp}(\theta)$ and unknown rate parameter $\theta.$ Find the log-likelihood function of the sample $2, \, 4, \, 1, \, 3, \, 7.$

#### Explanation

Recall that if $X_1, X_2, \ldots, X_{n}$ are independent and identically distributed continuous random variables with probability density function $f(x; \theta),$ where $\theta$ is an unknown parameter, then the log-likelihood function of a random sample $x_1, x_2, \ldots, x_n$ is

$$


\begin{aligned}𝑙(𝜃) & =ln⁡𝐿(𝜃) \\ & =ln⁡(\underset{\underset{𝑖=1}{∏}}{\overset{}{𝑛}}𝑓(𝑥_{𝑖};𝜃)) \\ & =\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}ln⁡(𝑓(𝑥_{𝑖};𝜃)).\end{aligned}


$$

In our case, we are given a sample of $n = 5$ independent exponential random variables with unknown parameter $\theta,$ for which the probability density function is

$$


f(x, \theta) = \theta e^{-\theta x}, \qquad x \geq 0.


$$

First, let's write down the log-density function:

$$


\begin{aligned}ln⁡𝑓(𝑥,𝜃) & =ln⁡(𝜃𝑒^{−𝜃𝑥}) \\ & =ln⁡𝜃+ln⁡(𝑒^{−𝜃𝑥}) \\ & =ln⁡𝜃−𝜃𝑥.\end{aligned}


$$

Now, we can calculate the log-likelihood function as follows:

$$


\begin{aligned}𝑙(𝜃) & =\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}(ln⁡𝜃−𝜃𝑥_{𝑖}) \\ & =\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}ln⁡𝜃−𝜃\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}𝑥_{𝑖} \\ & =𝑛ln⁡𝜃−𝜃\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}𝑥_{𝑖}\end{aligned}


$$

For our sample, we have that

$$


\begin{aligned}\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}𝑥_{𝑖} & =2+4+1+3+7=17\end{aligned}


$$

and $n = 5.$ Therefore,

$$


\begin{aligned}𝑙(𝜃) & =5ln⁡𝜃−𝜃⋅17 \\ & =5ln⁡𝜃−17𝜃.\end{aligned}


$$

### Example: Log-Likelihood Functions for Normal Random Variables

#### Question

Suppose $X_1,X_2,\ldots,X_{8}$ is an I.I.D random sample with $X_i \sim N(\theta, 1^2),$ where $\theta$ is an unknown mean. For a particular sample $x_1, x_2, \ldots, x_{8},$ you're given that

$$


\sum_{i=1}^{8} x_i = 11.8, \qquad \sum_{i=1}^{8} x_i^2 = 25.2.


$$

Find the log-likelihood function of the sample.

**

$$


f(x) = \dfrac{1}{\sqrt{2\pi}} e^{-(x-\theta)^2/2}, \qquad x \in (-\infty,\infty).


$$

#### Explanation

Recall that if $X_1, X_2, \ldots, X_{n}$ are independent and identically distributed continuous random variables with probability density function $f(x; \theta),$ where $\theta$ is an unknown parameter, then the log-likelihood function of a random sample $x_1, x_2, \ldots, x_n$ is

$$


\begin{aligned}𝑙(𝜃) & =ln⁡𝐿(𝜃) \\ & =ln⁡(\underset{\underset{𝑖=1}{∏}}{\overset{}{𝑛}}𝑓(𝑥_{𝑖};𝜃)) \\ & =\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}ln⁡(𝑓(𝑥_{𝑖};𝜃)).\end{aligned}


$$

In our case, we are given a sample of $n=8$ independent normal random variables with unknown mean $\theta$ and variance $\sigma^2 = 1,$ for which the probability density function is

$$


f(x, \theta) = \dfrac{1}{\sqrt{2\pi}} e^{-(x-\theta)^2/2}, \qquad x \in (-\infty,\infty).


$$

First, let's write down the log-density function:

$$


\begin{aligned}ln⁡𝑓(𝑥,𝜃) & =ln⁡(\frac{1}{\sqrt{2𝜋}}𝑒^{−(𝑥−𝜃)^{2}/2}) \\ & =ln⁡(\frac{1}{\sqrt{2𝜋}})+ln⁡(𝑒^{−(𝑥−𝜃)^{2}/2}) \\ & =−\frac{1}{2}ln⁡(2𝜋)−\frac{(𝑥−𝜃)^{2}}{2}\end{aligned}


$$

Now, we can calculate the log-likelihood function as follows:

$$


\begin{aligned}𝑙(𝜃) & =\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}(−\frac{1}{2}ln⁡(2𝜋)−\frac{(𝑥_{𝑖}−𝜃)^{2}}{2}) \\ & =−\frac{𝑛}{2}ln⁡(2𝜋)−\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}\frac{(𝑥_{𝑖}−𝜃)^{2}}{2} \\ & =−\frac{𝑛}{2}ln⁡(2𝜋)−\frac{1}{2}(\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}𝑥_{2𝑖}−2𝜃\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}𝑥_{𝑖}+𝑛𝜃^{2})\end{aligned}


$$

We are told that $\displaystyle\sum_{i=1}^{8} x_i = 11.8,$ $\displaystyle\sum_{i=1}^{8} x_i^2 = 25.2,$ and $n=8.$ Therefore,

$$


\begin{aligned}𝑙(𝜃) & =−\frac{8}{2}ln⁡(2𝜋)−\frac{1}{2}(25.2−2𝜃⋅11.8+8𝜃^{2}) \\ & =−4ln⁡(2𝜋)−12.6+11.8𝜃−4𝜃^{2}.\end{aligned}


$$
