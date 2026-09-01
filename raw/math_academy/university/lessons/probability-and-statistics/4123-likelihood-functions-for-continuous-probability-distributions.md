# Likelihood Functions for Continuous Probability Distributions

Source: https://www.mathacademy.com/topics/4123?courseId=73
Topic ID: 4123

## Prerequisites

- [The Normal Distribution](./1843-the-normal-distribution.md)
- [The Exponential Distribution](./3074-the-exponential-distribution.md)
- [Likelihood Functions for Discrete Probability Distributions](./3603-likelihood-functions-for-discrete-probability-distributions.md)

## Lesson

### Introduction

Likelihood functions of samples drawn from populations modeled using continuous random variables are defined similarly to discrete variables. The only difference is that we use probability density functions instead of probability mass functions.

If $X_1, X_2, \ldots, X_{n}$ are independent and identically distributed *continuous* random variables with probability density function $f(x; \theta),$ then the likelihood function of a random sample $x_1, x_2, \ldots, x_n$ is given by

$$


L(\theta) = P(X_1=x_1, X_2=x_2, \ldots , X_n = x_n) = \displaystyle\prod_{i=1}^n f(x_i;\,\theta).


$$

For example, let $X_1, X_2, X_3$ be continuous, I.I.D. random variables with the following probability density function:

$$


f(x; \theta) = \theta x^{-\theta-1}, \qquad x \geq 1


$$

Here, $\theta$ is an unknown parameter. Suppose we conduct our random sample and get the following results:

$$


x_1 = 2.5, \qquad x_2 = 3.2, \qquad x_3 = 1.2.


$$

In this case, we compute the likelihood function as follows:

$$


\begin{aligned}𝐿(𝜃) & =\underset{\underset{𝑖=1}{∏}}{\overset{}{𝑛}}(𝜃𝑥_{−𝜃−1𝑖}) \\ & =(𝜃𝑥_{−𝜃−11})⋅(𝜃𝑥_{−𝜃−12})⋯(𝜃𝑥_{−𝜃−1𝑛}) \\ & =𝜃^{𝑛}(𝑥_{−𝜃−11})⋅(𝑥_{−𝜃−12})⋯(𝑥_{−𝜃−1𝑛}) \\ & =𝜃^{𝑛}(𝑥_{1}⋅𝑥_{2}⋯𝑥_{𝑛})^{−𝜃−1} \\ & =𝜃^{𝑛}(\underset{\underset{𝑖=1}{∏}}{\overset{}{𝑛}}𝑥_{𝑖})^{−𝜃−1}\end{aligned}


$$

For our sample, we have $n=3$, and

$$


\begin{aligned}\underset{\underset{𝑖=1}{∏}}{\overset{}{𝑛}}𝑥_{𝑖} & =2.5⋅3.2⋅1.2=9.6.\end{aligned}


$$

Therefore,

$$


L(\theta) = \theta^{3} ( 9.6 )^{-\theta-1}.


$$

### Example: Likelihood Functions for Continuous Random Variables

#### Question

Let $X_1, X_2, X_3$ be I.I.D. random variables with probability density function

$$


f(x; \theta) = (\theta+1) x^{-\theta-2}, \qquad x \geq 1,


$$

where $\theta$ is an unknown parameter. Find the likelihood function of the sample $2.0, \, 4.5, \,5.1.$

#### Explanation

Recall that if $X_1, X_2, \ldots, X_{n}$ are independent and identically distributed continuous random variables with probability density function $f(x; \theta),$ where $\theta$ is an unknown parameter, then the likelihood function of a random sample $x_1, x_2, \ldots, x_n$ is

$$


L(\theta) = P(X_1=x_1, X_2=x_2, \ldots , X_n = x_n) = \displaystyle\prod_{i=1}^n f(x_i;\,\theta).


$$

$$


f(x; \theta) = (\theta+1) x^{-\theta-2}, \qquad x \geq 1.


$$

We can calculate the likelihood function as follows:

$$


\begin{aligned}𝐿(𝜃) & =\underset{\underset{𝑖=1}{∏}}{\overset{}{𝑛}}((𝜃+1)𝑥_{−𝜃−2𝑖}) \\ & =(𝜃+1)^{𝑛}⋅\underset{\underset{𝑖=1}{∏}}{\overset{}{𝑛}}𝑥_{−𝜃−2𝑖} \\ & =(𝜃+1)^{𝑛}(\underset{\underset{𝑖=1}{∏}}{\overset{}{𝑛}}𝑥_{𝑖})^{−𝜃−2}\end{aligned}


$$

For our sample, we have that

$$


\begin{aligned}\underset{\underset{𝑖=1}{∏}}{\overset{}{𝑛}}𝑥_{𝑖} & =2.0⋅4.5⋅5.1=45.9\end{aligned}


$$

and $n=3.$ Therefore,

$$


L(\theta) = (\theta+1)^{3} ( 45.9 )^{-\theta-2}.


$$

### Example: Likelihood Functions for Exponential Random Variables

#### Question

Suppose $X_1,X_2,\ldots,X_6$ is an I.I.D random sample with $X_i \sim \text{Exp}(\theta)$ and unknown rate parameter $\theta.$ Find the likelihood function of the sample $1.5, \, 2.0, \, 1.1, \, 0.4, \, 3.3, \, 2.7.$

#### Explanation

Recall that if $X_1, X_2, \ldots, X_{n}$ are independent and identically distributed continuous random variables with probability density function $f(x; \theta),$ where $\theta$ is an unknown parameter, then the likelihood function of a random sample $x_1, x_2, \ldots, x_n$ is

$$


L(\theta) = P(X_1=x_1, X_2=x_2, \ldots , X_n = x_n) = \displaystyle\prod_{i=1}^n f(x_i;\,\theta).


$$

In our case, we are given a sample of $n=6$ independent exponential random variables with unknown parameter $\theta,$ for which the probability density function is

$$


f(x; \,\theta) = \theta e^{-\theta x}, \qquad x\geq 0.


$$

We can calculate the likelihood function as follows:

$$


\begin{aligned}𝐿(𝜃) & =\underset{\underset{𝑖=1}{∏}}{\overset{}{𝑛}}𝜃𝑒^{−𝜃𝑥_{𝑖}} \\ & =(𝜃𝑒^{−𝜃𝑥_{1}})⋅(𝜃𝑒^{−𝜃𝑥_{2}})⋯(𝜃𝑒^{−𝜃𝑥_{𝑛}}) \\ & =𝜃^{𝑛}\,𝑒^{−𝜃(𝑥_{1}+𝑥_{2}+⋯+𝑥_{𝑛})} \\ & =𝜃^{𝑛}\,𝑒^{−𝜃∑𝑥_{𝑖}} \\ & =𝜃^{𝑛}\,𝑒^{−𝑆𝜃}\end{aligned}


$$

where $\displaystyle S = \sum\limits_ {i=1}^n x_i.$

For our sample, we have that

$$


\begin{aligned}𝑆 & =\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}𝑥_{𝑖} \\ & =1.5+2.0+1.1+0.4+3.3+2.7 \\ & =11\end{aligned}


$$

and $n=6.$ Therefore,

$$


\begin{aligned}𝐿(𝜃) & =𝜃^{6}\,𝑒^{−11𝜃}.\end{aligned}


$$

### The Normal Distribution

The probability density function of a normally distributed random variable $X\sim N(\mu,\sigma^2)$ is given by

$$


f(x) = \dfrac{1}{\sigma\sqrt{2\pi}}e^{-\frac12\left(\frac{x-\mu}{\sigma}\right)^2}.


$$

Some example normal distribution curves are shown below.

![Instructional graphic](../../../lesson-assets/probability-and-statistics/topic-4123/1d9b17f84b760c83.png)

If we set $\sigma=1,$ then $f(x)$ simplifies as follows:

$$


f(x) = \dfrac{1}{\sqrt{2\pi}}e^{-(x-\mu)^2/2}.


$$

This is a standard normal random variable whose mean is shifted right by $\mu$ units.

Finally, setting the unknown parameter as $\theta$ when discussing likelihood functions is common. Following this convention, we set $\mu=\theta,$ and we get

$$


f(x;\theta) = \dfrac{1}{\sqrt{2\pi}}e^{-(x-\theta)^2/2}.


$$

Let's use this to compute some likelihood functions of some normally distributed sample data.

### Example: Likelihood Functions for Normal Random Variables

#### Question

Suppose $X_1,X_2,X_3,X_4$ is an I.I.D random sample with $X_i \sim N(\theta, 1),$ where $\theta$ is an unknown mean. Find the likelihood function of the sample $0.4,\, -0.3,\, -2.2,\, -0.4.$

#### Explanation

Recall that if $X_1, X_2, \ldots, X_{n}$ are independent and identically distributed continuous random variables with probability density function $f(x; \theta),$ where $\theta$ is an unknown parameter, then the likelihood function of a random sample $x_1, x_2, \ldots, x_n$ is

$$


L(\theta) = P(X_1=x_1, X_2=x_2, \ldots , X_n = x_n) = \displaystyle\prod_{i=1}^n f(x_i;\,\theta).


$$

In our case, we are given a sample of $n=4$ independent normal random variables with unknown mean $\theta$ and variance $\sigma^2 = 1,$ for which the probability density function is

$$


f(x; \theta) = \dfrac{1}{\sigma \sqrt{2\pi}} e^{-\frac{1}{2} \left( \frac{x-\theta}{\sigma} \right)^2} = \dfrac{1}{\sqrt{2\pi}} e^{-(x-\theta)^2/2}, \qquad x \in (-\infty,\infty).


$$

We can calculate the likelihood function as follows:

$$


\begin{aligned}𝐿(𝜃) & =\underset{\underset{𝑖=1}{∏}}{\overset{}{𝑛}}(\frac{1}{\sqrt{2𝜋}}𝑒^{−(𝑥_{𝑖}−𝜃)^{2}/2}) \\ & =(2𝜋)^{−𝑛/2}\,𝑒^{−∑(𝑥_{𝑖}−𝜃)^{2}/2} \\ & =(2𝜋)^{−𝑛/2}\,𝑒^{−(∑𝑥_{2𝑖}−2𝜃∑𝑥_{𝑖}+𝑛𝜃^{2})/2} \\ & =(2𝜋)^{−𝑛/2}\,𝑒^{−(𝐶−2𝑆𝜃+𝑛𝜃^{2})/2}\end{aligned}


$$

where $\displaystyle S = \sum\limits_ {i=1}^n x_i$ and $\displaystyle C = \sum\limits_ {i=1}^n x_i^2.$

For our sample, we have that $n=4,$ and

$$


\begin{aligned}𝑆 & =\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}𝑥_{𝑖} \\ & =0.4+(−0.3)+(−2.2)+(−0.4) \\ & =−2.5 \\ 𝐶 & =\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}𝑥_{2𝑖} \\ & =(0.4)^{2}+(−0.3)^{2}+(−2.2)^{2}+(−0.4)^{2} \\ & =5.25\end{aligned}


$$

Therefore,

$$


\begin{aligned}𝐿(𝜃) & =(2𝜋)^{−4/2}\,𝑒^{−(5.25−2(−2.5)𝜃+4𝜃^{2})/2} \\ & =\frac{1}{4𝜋^{2}}\,𝑒^{−2.625\,−\,2.5𝜃\,−\,2𝜃^{2}}.\end{aligned}


$$
