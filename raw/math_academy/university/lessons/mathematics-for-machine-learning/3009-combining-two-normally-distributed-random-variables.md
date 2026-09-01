# Combining Two Normally Distributed Random Variables

Source: https://www.mathacademy.com/topics/3009?courseId=145
Topic ID: 3009

## Prerequisites

- [Modeling With the Normal Distribution](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/788-modeling-with-the-normal-distribution.md)
- [Variance of Sums of Independent Random Variables](./3062-variance-of-sums-of-independent-random-variables.md)
- [Expected Values of Sums and Products of Random Variables](./3292-expected-values-of-sums-and-products-of-random-variables.md)
- [Independence of Continuous Random Variables](./3863-independence-of-continuous-random-variables.md)

## Lesson

### Introduction

Let $X_1$ and $X_2$ be *independent* random variables that are normally distributed with

$$


X_1\sim N(\mu_1, \sigma_1^2), \qquad X_2\sim N(\mu_2, \sigma_2^2).


$$

We can show that the random variable $Y = X_1\pm X_2$ is normally distributed, and

$$


Y = X_1\pm X_2 \sim N(\mu_1\pm\mu_2, \sigma_1^2+\sigma_2^2).


$$

We'll prove this in a separate lesson.

For example, if $X_1\sim N(2,3)$ and $X_2\sim N(1,4)$ are independent, then

$$


\begin{aligned}𝑋_{1}+𝑋_{2} & ∼𝑁(2+1,3+4)∼𝑁(3,7),\end{aligned}


$$

and

$$


\begin{aligned}𝑋_{1}−𝑋_{2} & ∼𝑁(2−1,3+4)∼𝑁(1,7).\end{aligned}


$$

When computing a sum or difference of normal random variables, there are a few things to watch out for:

- Firstly, when we compute the distribution of a *difference*, we subtract the means, but *add* the variances!

- Secondly, it is vital to check that $X_1$ and $X_2$ are independent. Cases where $X_1$ and $X_2$ are *dependent* will be dealt with in future lessons.

### Example: Finding the Distribution of a Sum or Difference of Normal Random Variables

#### Question

If $X_1\sim N(2,5)$ and $X_2\sim N(-2, 2)$ are independent, then what is the distribution of $Y = X_1+X_2?$

#### Explanation

Recall that if $X_1$ and $X_2$ are independent random variables, where $X_1\sim N(\mu_1,\sigma^2_1)$ and $X_2\sim N(\mu_2,\sigma^2_2),$ then

$$


Y = X_1+X_2\sim N(\mu_1+\mu_2, \sigma^2_1+\sigma^2_2).


$$

Since $X_1$ and $X_2$ are independent, we have

$$


\begin{aligned}𝑌=𝑋_{1}+𝑋_{2} & ∼𝑁(2+(−2),5+2) \\ & ∼𝑁(0,7).\end{aligned}


$$

Therefore, $Y\sim N(0, 7).$

### Finding a Sum or Difference of Scaled Normal Random Variables

If $X_1\sim N(\mu_1, \sigma_1^2)$ and $X_2\sim N(\mu_2, \sigma_2^2)$ are *independent* random variables and $a$ and $b$ are constants, we have

$$


aX_1+bX_2\sim N(a\mu_1+b\mu_2, a^2\sigma^2_1+b^2\sigma^2_2).


$$

For example, if $X_1\sim N(2,3)$ and $X_2\sim N(1,4)$ are independent, then

$$


\begin{aligned}2𝑋_{1}+3𝑋_{2} & ∼𝑁(2⋅2+3⋅1,2^{2}⋅3+3^{2}⋅4) \\ & ∼𝑁(4+3,4⋅3+9⋅4) \\ & ∼𝑁(7,48),\end{aligned}


$$

and

$$


\begin{aligned}2𝑋_{1}−3𝑋_{2} & ∼𝑁(2⋅2+(−3)⋅1,2^{2}⋅3+3^{2}⋅4) \\ & ∼𝑁(4−3,4⋅3+9⋅4) \\ & ∼𝑁(1,48).\end{aligned}


$$

### Example: Finding the Distribution of a Sum or Difference of Scaled Normal Random Variables

#### Question

Suppose that $X$ and $Y$ are independent random variables such that $X \sim N(2,7)$ and $Y \sim N(5, 4).$ Find the distribution of the random variable $W = 2X-Y.$

#### Explanation

Recall that if $X_1$ and $X_2$ are independent random variables, where $X_1\sim N(\mu_1,\sigma^2_1)$ and $X_2\sim N(\mu_2,\sigma^2_2),$ and $a$ and $b$ are constants, then

$$


aX_1+bX_2\sim N(a\mu_1+b\mu_2, a^2\sigma^2_1+b^2\sigma^2_2).


$$

Since $X$ and $Y$ are independent, we have

$$


\begin{aligned}𝑊=2𝑋−𝑌 & ∼𝑁(2⋅2+(−1)⋅5,2^{2}⋅7+(−1)^{2}⋅4) \\ & ∼𝑁(−1,32).\end{aligned}


$$

Therefore, $Y\sim N(-1, 32).$

### Example: Calculating a Probability Involving a Sum or Difference of Normally Distributed Random Variables

#### Question

If $X_1\sim N(10,3^2)$ and $X_2\sim N(20,5^2)$ are independent and $Y=5X_1-4X_2,$ calculate $P(3 \lt Y \lt 40).$ Round your final answer to two decimal places.

**

#### Explanation

Recall that if $X_1$ and $X_2$ are independent random variables, where $X_1\sim N(\mu_1,\sigma^2_1)$ and $X_2\sim N(\mu_2,\sigma^2_2),$ and $a$ and $b$ are constants, then

$$


aX_1+bX_2\sim N(a\mu_1+b\mu_2, a^2\sigma^2_1+b^2\sigma^2_2).


$$

Since $X_1$ and $X_2$ are independent, the distribution of $Y$ is given by

$$


\begin{aligned}𝑌=5𝑋_{1}−4𝑋_{2} & ∼𝑁(5𝜇_{1}−4𝜇_{2},5^{2}⋅𝜎_{21}+4^{2}⋅𝜎_{22}) \\ & ∼𝑁(5𝜇_{1}−4𝜇_{2},25𝜎_{21}+16𝜎_{22}) \\ & ∼𝑁(5⋅10+(−4)⋅20,25⋅3^{2}+16⋅5^{2}) \\ & ∼𝑁(−30,625).\end{aligned}


$$

Therefore, $Y$ is normally distributed with mean $\mu = -30$ and standard deviation $\sigma = \sqrt{625} = 25.$

We want to find $P(3 \lt Y \lt 40).$ Thus, we convert $Y$ to a standard normal random variable by $z$-scoring:

$$


\begin{aligned}𝑃(3<𝑌<40) & =𝑃(\frac{3−(−30)}{25}<𝑍<\frac{40−(−30)}{25}) \\ & =𝑃(1.32<𝑍<2.8) \\ & =𝑃(𝑍<2.8)−𝑃(𝑍<1.32) \\ & =Φ(2.8)−Φ(1.32)\end{aligned}


$$

Using the $z$-table, we see that

$$


\begin{aligned}Φ(1.32) & ≈0.9066 \\ Φ(2.8) & ≈0.9974.\end{aligned}


$$

Therefore,

$$


\begin{aligned}𝑃(3<𝑌<40) & =Φ(2.8)−Φ(1.32) \\ & ≈0.9974−0.9066 \\ & ≈0.09.\end{aligned}


$$

### Example: Calculating a Probability Involving a Sum or Difference of Normally Distributed Random Variables in Context

#### Question

The math test results of a group of students are normally distributed with a mean of $67$ and a standard deviation of $12.$ The results of the same group on a history test are normally distributed with a mean of $73$ and a standard deviation of $9.$ If one student is randomly selected, what is the probability their combined score from both tests is more than $150?$ You may assume that the student's scores on both tests are independent.

**

#### Explanation

Let $X$ denote the student's math test result, and let $Y$ denote the student's history test result. We want to find

$$


P( X+Y > 150).


$$

Since $X$ and $Y$ are independent random variables such that $X\sim N(67,12^2)$ and $Y\sim N(73,9^2),$ then

$$


\begin{aligned}𝑋+𝑌 & ∼𝑁(67+73,12^{2}+9^{2}) \\ & ∼𝑁(140,225).\end{aligned}


$$

So, the variable $X+Y$ is normally distributed with mean $\mu = 140$ and standard deviation $\sigma = \sqrt{225} = 15.$

In order to find $P(X+Y > 150),$ we convert $X+Y$ to a standard normal random variable by $z$-scoring:

$$


\begin{aligned}𝑃(𝑋+𝑌>150) & =𝑃(𝑍>\frac{150−140}{15}) \\ & ≈𝑃(𝑍>0.67) \\ & =1−𝑃(𝑍≤0.67) \\ & =1−Φ(0.67)\end{aligned}


$$

Using the $z$-table, we see that

$$


\Phi(0.67 )\approx 0.7486.


$$

Therefore,

$$


\begin{aligned}𝑃(𝑋+𝑌>150) & ≈1−Φ(0.67) \\ & ≈1−0.7486 \\ & =0.2514.\end{aligned}


$$

So, we conclude that the probability that the combined score is more than $150$ is $0.2514.$
