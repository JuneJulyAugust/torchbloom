# The Uniqueness Property of MGFs

Source: https://www.mathacademy.com/topics/3293?courseId=73
Topic ID: 3293

## Prerequisites

- [Combining Two Normally Distributed Random Variables](./3009-combining-two-normally-distributed-random-variables.md)
- [Properties of Moment-Generating Functions](./3070-properties-of-moment-generating-functions.md)
- [Linear Combinations of Binomial Random Variables](./3295-linear-combinations-of-binomial-random-variables.md)
- [Linear Combinations of Poisson Random Variables](./3296-linear-combinations-of-poisson-random-variables.md)

## Lesson

### Introduction

In this lesson, we'll use moment-generating functions to prove certain properties about sums of independent random variables with known distributions.

First, let's introduce some notation:

*The random variables $X$ and $Y$ are **** written as*

$$


X \overset{d}{=} Y


$$

*if the cumulative distribution functions (CDFs) of $X$ and $Y$ are the same for all real values of $x{:}$*

$$


F_X(x) = F_Y(x), \qquad \forall x \in \mathbb{R},


$$

*where $F_X(x)$ and $F_Y(x)$ are the CDFs of $X$ and $Y$ respectively.*

We're now ready for the main result of this lesson:

*Let $X$ and $Y$ be random variables, and $M_X(t)$ and $M_Y(t)$ be the moment-generating functions of $X$ and $Y,$ respectively. If*

$$


M_X(t) = M_Y(t)


$$

*for all values of $t$ in an open interval around $t=0,$ then*

$$


X \overset{d}{=} Y.


$$

*This result is called the *****

This means a random variable's probability distribution is *uniquely determined* by its MGF. Therefore, if the MGF of a random variable matches that of a known distribution, they have the same distribution.

We can use this result to identify the distributions of sums of independent random variables. Let's see some examples.

### Example: Identifying the Distribution of a Sum of Discrete Random Variables

#### Question

Consider the independent random variables $Y_1, Y_2, \ldots, Y_{10}$ where $Y_i\sim \mathrm{B}(5,0.3)$ for $1\leq i \leq 10.$ What is the distribution of $Y=Y_1+Y_2+\cdots + Y_{10}?$

**

#### Explanation

Recall that a random variable's probability distribution is uniquely determined by its moment-generating function (MGF). Therefore, if the MGF of a random variable $X$ matches that of a known distribution, then $X$ has the same distribution.

For a binomial random variable $Y_i \sim \text{B}(n,p),$ we have

$$


M_{Y_i}(t) = (1-p+pe^t)^n.


$$

In our case, since $Y_i \sim \text{B}(5,0.3),$ we have

$$


\begin{aligned}𝑀_{𝑌_{𝑖}}(𝑡) & =(1−0.3+0.3𝑒^{𝑡})^{5} \\ & =(0.7+0.3𝑒^{𝑡})^{5}.\end{aligned}


$$

If $Y = Y_1+Y_2+\cdots + Y_{10},$ where $Y_1, Y_2,\ldots Y_{10}$ are independent random variables with moment-generating function $M_{Y_i}(t),$ then the moment-generating function of $Y$ is

$$


M_Y(t) = M_{Y_1}(t) \cdot M_{Y_2}(t) \cdots M_{Y_{10}}(t)


$$

In our case, we have

$$


\begin{aligned}𝑀_{𝑌}(𝑡) & =\overset{(0.7+0.3𝑒^{𝑡})^{5}⋅(0.7+0.3𝑒^{𝑡})^{5}⋯(0.7+0.3𝑒^{𝑡})^{5}}{}}{10 times} \\ & =(0.7+0.3𝑒^{𝑡})^{50}.\end{aligned}


$$

Notice that $M_Y(t)$ is the MGF of a binomial random variable with $n = 50$ and $p= 0.3.$

Therefore, we conclude that $Y\sim B(50,0.3).$

### Example: Identifying the Distribution of a Sum of Continuous Random Variables

#### Question

Consider the independent random variables $Y_1\sim \chi^2(2)$ and $Y_2\sim \chi^2(3).$ What is the distribution of $Y=Y_1+Y_2?$

**

#### Explanation

Recall that a random variable's probability distribution is uniquely determined by its moment-generating function (MGF). Therefore, if the MGF of a random variable $X$ matches that of a known distribution, then $X$ has the same distribution.

For a chi-square random variable $Y_i \sim \chi^2(k),$ we have

$$


M_{Y_i}(t) = \left(1 - 2t \right)^{-k/2}, \quad t < \dfrac12.


$$

In our case, since $Y_{1} \sim \chi^2(2),$ we have

$$


M_{Y_1}(t) = \left(1 - 2t \right)^{-1}, \quad t < \dfrac12.


$$

Similarly, since $Y_{2} \sim \chi^2(3),$ we have

$$


M_{Y_{2}}(t) = \left(1 - 2t \right)^{-3/2}, \quad t < \dfrac12.


$$

If $Y = Y_1+Y_2,$ where $Y_1$ and $Y_2$ are independent random variables with moment-generating functions $M_{Y_1}(t)$ and $M_{Y_2}(t),$ respectively, then the moment-generating function of $Y$ is

$$


M_Y(t) = M_{Y_1}(t) M_{Y_2}(t).


$$

So, for $t < \dfrac12,$ we have

$$


\begin{aligned}𝑀_{𝑌}(𝑡) & =(1−2𝑡)^{−1}⋅(1−2𝑡)^{−3/2} \\ & =(1−2𝑡)^{−5/2}.\end{aligned}


$$

Notice that $M_Y(t)$ has the form of the MGF of a chi-square random variable with $k = 5.$

Therefore, we conclude that $Y_1+Y_2 \sim \chi^2(5).$

### Example: Identifying True Statements Regarding Sums of Random Variables

#### Question

Let $X_1 \sim N(5, 4)$ and $X_2 \sim N(3, 2)$ be independent, and $Y = X_1 + X_2.$ Which of the following statements are true?

1. $M_Y(t) = M_{X_1}(t) \cdot M_{X_2}(t)$

2. $Y \stackrel{d}{=} X_1 + X_2$

3. $Y \sim N(8, 6)$

**

$$


M_X(t) = e^{\mu t + \sigma^2 t^2/2}, \qquad t\in\mathbb R.


$$

#### Explanation

Let's inspect each statement in turn.

- Statement I is true. In general, if $Y = X_1 + X_2,$ where $X_1$ and $X_2$ are independent random variables with MGF's $M_{X_1}(t)$ and $M_{X_2}(t),$ respectively, then the MGF of $Y$ is

- Statement II is true. Since $Y = X_1 + X_2,$ we know that $Y$ and $X_1+X_2$ have the same probability distribution. We represent this as $Y \stackrel{d}{=} X_1 + X_2.$

- Statement III is true. A normally distributed random variable $X \sim N(\mu, \sigma^2)$ has the following MGF: So the MGF's for $X_1 \sim N(5, 4)$ and $X_2 \sim N(3, 2)$ are and we have Since $M_Y(t)$ is the MGF for the distribution $N(8, 6),$ we conclude that $Y \sim N(8, 6).$

Therefore, the correct answer is "I, II, and III."

### Proving Some Well-Known Results

Let's use our knowledge of the uniqueness property of moment-generating functions to prove some general results.

- **Sums of Bernoulli Random Variables**: Suppose $X_1, X_2, \ldots, X_n\sim \text{Bernoulli}(p)$ are independent. Then To prove this, let $M_{X_i}(t)$ be the moment-generating function of $X_i$ for $i=1,2,\ldots, n$. Then, we have By the multiplicative property of moment-generating functions, we have that which is the moment-generating function of a binomial random variable with distribution $B(n, p).$ Now, since any given distribution is characterized by its moment-generating function (meaning that no other distribution can have the same moment-generating function), we conclude that

- **Sums of Binomial Random Variables**: Suppose $X_1\sim B(n_1,p)$ and $X_2\sim B(n_2,p)$ are independent. Then To prove this, let $M_{X_1}(t)$ and $M_{X_2}(t)$ be the moment-generating functions of $X_1$ and $X_2$ respectively. Then, we have By the multiplicative property of moment-generating functions, we have This is the moment-generating function of a binomial random variable with distribution $B(n_1+n_2, p).$ Therefore, by the uniqueness property, we conclude

- **Sums of Poisson Random Variables**: If $X_1\sim \text{Po}(\lambda_1)$ and $X_2\sim \text{Po}(\lambda_2)$ are independent, then To prove this, let $M_{X_1}(t)$ and $M_{X_2}(t)$ be the moment-generating functions of $X_1$ and $X_2$ respectively. Then, we have By the multiplicative property of moment-generating functions, we have This is the moment-generating function of a Poisson random variable with distribution $\text{Po}(\lambda_1+\lambda_2).$ Therefore, by the uniqueness property, we conclude

- **Sums of Normal Random Variables**: Suppose $X_1\sim N(\mu_1,\sigma_1^2)$ and $X_2\sim N(\mu_2,\sigma_2^2)$ are independent. Then To prove this, let $M_{X_1}(t)$ and $M_{X_2}(t)$ be the moment-generating functions of $X_1$ and $X_2$ respectively. Then, we have where $\exp(x) = e^x$ is the exponential function. By the multiplicative property of moment-generating functions and by the properties of the exponential function, we have that This is the moment-generating function of a normal random variable with distribution $N(\mu_1+\mu_2, \sigma_1^2+\sigma_2^2).$ Therefore, by the uniqueness property, we conclude

- **Sums of Chi-Square Random Variables**: Suppose $X_1\sim \chi^2(k_1)$ and $X_2\sim \chi^2(k_2)$ are independent. Then To prove this, let $M_{X_1}(t)$ and $M_{X_2}(t)$ be the moment-generating functions of $X_1$ and $X_2$ respectively. Then, we have By the multiplicative property of moment-generating functions, we have that This is the moment-generating function of a chi-square random variable with distribution $\chi^2(k_1+k_2).$ Therefore, by the uniqueness property, we conclude
