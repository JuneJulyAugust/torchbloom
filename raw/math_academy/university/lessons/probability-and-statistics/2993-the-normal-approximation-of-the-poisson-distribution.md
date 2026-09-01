# The Normal Approximation of the Poisson Distribution

Source: https://www.mathacademy.com/topics/2993?courseId=73
Topic ID: 2993

## Prerequisites

- [Modeling With the Normal Distribution](./788-modeling-with-the-normal-distribution.md)
- [Mean and Variance of the Poisson Distribution](./2991-mean-and-variance-of-the-poisson-distribution.md)
- [Approximating Discrete Random Variables as Continuous](./2994-approximating-discrete-random-variables-as-continuous.md)

## Lesson

### Introduction

Suppose that $X \sim \text{Po}(\lambda)$ is a Poisson random variable. Recall that the probability mass function of $X$ is given by

$$


f(x) = \dfrac{\lambda^x e^{-\lambda}}{x!}\,,\qquad x=0,1,2,3,\ldots


$$

If the rate parameter $\lambda$ is large, then $e^{-\lambda}$ is very small, and $\lambda^x$ could be large. This means that computing exact probabilities for $X$ using its probability mass function can be difficult due to rounding errors.

Fortunately, if $\lambda$ is large, we can approximate the *discrete* random variable $X$ using a *continuous* normal random variable $Y,$ given by

$$


Y \sim N(\mu, \sigma^2)


$$

where $\mu$ and $\sigma^2$ are calculated using the formulas for the mean and variance of the Poisson random variable $X\mathbin{:}$

$$


\mu = \lambda, \qquad \sigma^2 = \lambda


$$

In other words, $Y \sim N(\lambda, \lambda).$

Although there is no set rule for what we mean by "large $\lambda$," we will use the rule of thumb that $\lambda \geq 10$ for the normal approximation to be valid. In general, the larger $\lambda$ is, the better!

### Example: Identifying Situations Where the Normal Approximation is Appropriate

#### Question

Which of the following probabilities could be approximated using the normal approximation of the Poisson distribution?

1. The probability that $12$ accidents occur on a particular road in a given year if there are $7$ accidents per year on average.

2. The probability that an amusement park receives more than $60$ visitors in a particular hour if there are $80$ visitors per hour on average.

3. The probability that a bakery sells more than $46$ cakes in a day if it sells $53$ cakes per day on average.

#### Explanation

Given a Poisson random variable $X \sim \text{Po}(\lambda),$ if $\lambda$ is large, we can approximate $X$ as a normal variable $Y$ with mean $\mu = \lambda$ and variance $\sigma^2 = \lambda,$ that is, $Y \sim N(\lambda, \lambda).$ Typically, we require $\lambda \geq 10$ for the approximation to be valid.

- In situation I, we have $\lambda = 7.$ So, $\lambda$ is ** large, which means we ** use the normal approximation of the Poisson distribution.

- In situation II, we have $\lambda = 80.$ So, $\lambda$ is large, which means we can use the normal approximation of the Poisson distribution.

- In situation III, we have $\lambda = 53.$ So, $\lambda$ is large, which means we can use the normal approximation of the Poisson distribution.

Therefore, the correct answer is "II and III only."

### Using the Normal Approximation to the Poisson Distribution

Suppose we have a random variable $X \sim \text{Po}(20).$ Let's estimate the value of $P(X=21)$ using the normal approximation.

Since $\lambda=20$ is large, we can approximate $X$ as a normal variable $Y$ with mean $\mu = 20$ and variance $\sigma^2 = 20 \mathbin{:}$

$$


Y \sim N(20,20)


$$

Now, since $X$ is discrete and $Y$ is continuous, we need to apply a continuity correction. The required continuity correction in this case is

$$


P(X = 21) \approx P(20.5 \leq Y \leq 21.5).


$$

To compute this probability, we transform to a standard normal random variable by $z$-scoring:

$$


\begin{aligned}𝑃(20.5≤𝑌≤21.5) & =𝑃(\frac{20.5−20}{\sqrt{20}}≤𝑍≤\frac{21.5−20}{\sqrt{20}}) \\ & ≈𝑃(0.11≤𝑍≤0.34) \\ & =𝑃(𝑍≤0.34)−𝑃(𝑍<0.11) \\ & =𝑃(𝑍≤0.34)−𝑃(𝑍≤0.11) \\ & =Φ(0.34)−Φ(0.11)\end{aligned}


$$

Using a table of values for the CDF of the standard normal distribution, we find that

$$


\Phi(0.34) = 0.6331 , \qquad \Phi(0.11) = 0.5438.


$$

So, we have

$$


\begin{aligned}𝑃(20.5≤𝑌≤21.5) & =Φ(0.34)−Φ(0.11) \\ & =0.6331−0.5438 \\ & =0.0893.\end{aligned}


$$

Therefore,

$$


P(X = 21) \approx 0.0893.


$$

The actual value (rounded to four decimal places) is $0.0846,$ so our approximation is pretty close!

### A Note on Rounding Errors

In the last example, we approximated the Poisson random variable

$$


X \sim \text{Po}(20)


$$

using a normal random variable

$$


Y \sim N(20,20),


$$

and we arrived at the approximation

$$


P(X=21) \approx P(20.5 \leq Y \leq 21.5) \approx 0.0893.


$$

If you were to use a software package to evaluate this approximation, you might get an answer like

$$


P(X=21) \approx P(20.5 \leq Y \leq 21.5) \approx 0.0868.


$$

Notice that there is a difference of $0.0025$ between the two answers.

There is a reason for this discrepancy. When we calculated that $P(X=21) \approx P(20.5 \leq Y \leq 21.5) \approx 0.0893,$ we rounded our $z$-values two decimal places and then used a lookup table to find $\Phi(z)$ for those rounded values. As a result, we introduced some small rounding errors.

Typically, the rounding errors are small, so we will continue to work with a table of values. However, it's worth bearing this in mind if you're using a software package or calculator to compute $\Phi(z).$

### Example: Using the Normal Approximation to Compute a Probability at a Single Point

#### Question

A library receives $90$ visitors per hour on average. The visitors arrive at a constant rate, randomly in time, and independently of one another. Using the normal approximation to the Poisson distribution, approximate the probability that the library receives $95$ visitors over the next hour. Give your final answer to three decimal places.

**

#### Explanation

Given a Poisson random variable $X \sim \text{Po}(\lambda),$ if $\lambda$ is large, we can approximate $X$ as a normal variable $Y$ with mean $\mu = \lambda$ and variance $\sigma^2 = \lambda,$ that is, $Y \sim N(\lambda, \lambda).$

Here, we have $\lambda = 90.$ So $\lambda$ is large, which means we can approximate $X$ as a normal random variable $Y$ with mean $\mu = 90$ and variance $\sigma^2 = 90,$ that is, $Y \sim N(90, 90).$

Now, we can approximate the desired probability $P(X = 95).$ Using a continuity correction, we have

$$


P(X = 95) \approx P(94.5 \leq Y \leq 95.5).


$$

To compute this probability, we transform to a standard normal random variable by $z$-scoring:

$$


\begin{aligned}𝑃(94.5≤𝑌≤95.5) & =𝑃(\frac{94.5−90}{\sqrt{90}}≤𝑍≤\frac{95.5−90}{\sqrt{90}}) \\ & ≈𝑃(0.47≤𝑍≤0.58) \\ & =𝑃(𝑍≤0.58)−𝑃(𝑍<0.47) \\ & =𝑃(𝑍≤0.58)−𝑃(𝑍≤0.47) \\ & =Φ(0.58)−Φ(0.47) \\ & =0.7190−0.6808 \\ & =0.0382\end{aligned}


$$

Therefore,

$$


P(X=95)\approx 0.038.


$$

Note: Using a software package for the approximation gives a probability of $0.0366.$

### Example: Using the Normal Approximation to Compute a Probability Over an Interval

#### Question

A bakery sells an average of $95$ cookies per day. The sales occur at a constant rate, randomly in time and independently of one another. Using the normal approximation to the Poisson distribution, approximate the probability that the bakery will sell at least $100$ cookies tomorrow. Give your final answer to three decimal places.

**

#### Explanation

Given a Poisson random variable $X \sim \text{Po}(\lambda),$ if $\lambda$ is large, we can approximate $X$ as a normal variable $Y$ with mean $\mu = \lambda$ and variance $\sigma^2 = \lambda,$ that is, $Y \sim N(\lambda, \lambda).$

Here, we have $\lambda = 95.$ So $\lambda$ is large, which means we can approximate $X$ as a normal random variable $Y$ with mean $\mu = 95$ and variance $\sigma^2 = 95,$ that is, $Y \sim N(95, 95).$

Now, we can estimate the desired probability $P(X \geq 100).$ Using a continuity correction, we have

$$


P(X\geq 100) \approx P(Y > 99.5).


$$

To compute this probability, we transform to a standard normal random variable by $z$-scoring:

$$


\begin{aligned}𝑃(𝑌>99.5) & =𝑃(𝑍>\frac{99.5−95}{\sqrt{95}}) \\ & ≈𝑃(𝑍>0.46) \\ & =1−𝑃(𝑍≤0.46) \\ & =1−Φ(0.46) \\ & =1−0.6772 \\ & =0.3228\end{aligned}


$$

Therefore,

$$


P(X\geq 100) \approx 0.323.


$$

Note: Using a software package for the approximation gives a probability of $0.3222.$
