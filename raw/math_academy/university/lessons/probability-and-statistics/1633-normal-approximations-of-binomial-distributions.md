# Normal Approximations of Binomial Distributions

Source: https://www.mathacademy.com/topics/1633?courseId=73
Topic ID: 1633

## Prerequisites

- [Modeling With the Normal Distribution](./788-modeling-with-the-normal-distribution.md)
- [Mean and Variance of the Binomial Distribution](./2149-mean-and-variance-of-the-binomial-distribution.md)
- [Approximating Discrete Random Variables as Continuous](./2994-approximating-discrete-random-variables-as-continuous.md)

## Lesson

### Introduction

Suppose the random variable $X\sim B(n,p)$ follows a binomial distribution.

There are certain situations where working with binomial random variables becomes difficult. For example, when the parameter $n$ is large, computing exact probabilities can become problematic due to the large numbers involved.

Under certain conditions, we can approximate the *discrete* random variable $X$ using a *continuous normal* random variable $Y,$ given by

$$


Y \sim N(\mu, \sigma^2),


$$

where $\mu$ and $\sigma^2$ are calculated using the formulas for the mean and variance of the binomial random variable $X\mathbin{:}$

$$


\mu = np, \qquad \sigma^2 = np(1-p)


$$

To determine whether a given binomial distribution can be approximated using a normal distribution, we use the following rule of thumb:

- $np > 5,$ and

- $n(1-p) > 5.$

To get a feel for how this works, let's consider a few examples of binomial distributions and their corresponding normal approximations:

- First, consider the case where $n=5$ and $p=0.2.$ In this case, it's straightforward to show that and Since $np < 5,$ the normal distribution $N({\color{blue}{1}},{\color{red}{0.8}})$ is *not* a good approximation to $B(5, 0.2).$ The diagram below compares the two distributions. The yellow rectangles correspond to the values of the PMF of $B(5, 0.2),$ and the smooth blue curve is the PDF of the corresponding normal distribution.

- Next, we consider the case where $n=5$ and $p=0.5.$ In this case, it's straightforward to show that and Since $np = n(1-p) < 5,$ the normal distribution $N({\color{blue}{2.5}},{\color{red}{1.25}})$ is *not* a good approximation to $B(5, 0.5).$

- Finally, we consider the case where $n=20$ and $p=0.5.$ In this case, it's straightforward to show that and Since $np > 5$ and $n(1-p) > 5,$ the normal distribution $N({\color{blue}{10}},{\color{red}{5}})$ *is* a good approximation to $B(20, 0.5).$

The fact that we can approximate binomial random variables as normal when $np > 5$ and $n(1-p) > 5$ is a consequence of the so-called **central limit theorem** (or CLT). We'll discuss this in more detail at the end of the lesson.

### Example: Identifying Situations Where a Normal Approximation is Appropriate

#### Question

Which of the following probabilities could be approximated using the normal approximation of the binomial distribution?

1. The probability that a basketball player scores at least $2$ baskets in a series of $3$ free throws if the probability of scoring a basket on each free throw is $0.55.$

2. The probability of getting $35$ even numbers on $60$ rolls of a $6$-sided die.

3. The probability that a fair spinner with three regions, red, green, and blue, lands on green in $5$ out of $12$ spins.

#### Explanation

Given a binomial random variable $X \sim B(n,p),$ if

- $np > 5,$ and

- $n(1-p) > 5,$

we can approximate $X$ as a normal random variable $Y$ with mean $\mu = np$ and variance $\sigma^2 = np(1-p),$ that is,

$$


Y \sim N(np, np(1-p)).


$$

Let's now examine each situation.

- In situation I, we have $n=3$ and $p=0.55.$ Therefore, So, we ** use the normal approximation of the binomial distribution.

- In situation II, we have $n=60$ and $p=\dfrac12.$ Therefore, So, we can use the normal approximation of the binomial distribution.

- In situation III, we have $n=12$ and $p=\dfrac13.$ Therefore, So, we ** use the normal approximation of the binomial distribution.

Therefore, the correct answer is "II only."

### Using the Normal Approximation to the Binomial Distribution

Suppose we have a random variable $X \sim B(50,0.6).$ Let's estimate the value of $P(X=33)$ using the normal approximation.

Given a binomial random variable $X \sim B(n,p),$ if

- $np > 5,$ and

- $n(1-p) > 5,$

we can approximate $X$ as a normal random variable $Y$ with mean $\mu = np$ and variance $\sigma^2 = np(1-p),$ that is,

$$


Y \sim N(np, np(1-p)).


$$

Here, we have $n=50$ and $p = 0.6.$ Therefore,

$$


\begin{aligned}𝑛𝑝 & =50⋅0.6 \\ & =30 \\ & >5\,✓ \\ 𝑛(1−𝑝) & =50⋅(1−0.6) \\ & =20 \\ & >5.\,✓\end{aligned}


$$

So, we can approximate our binomial random variable $X$ with a normal random variable $Y$ with mean

$$


\mu = 50\cdot0.6 = 30


$$

and variance

$$


\sigma^2 = 50\cdot0.6\cdot(1-0.6)=12.


$$

That is, we can approximate $X$ by

$$


Y \sim N(30,12).


$$

Now, since $X$ is discrete and $Y$ is continuous, we need to apply a continuity correction. The required continuity correction in this case is

$$


P(X = 33) \approx P(32.5 \leq Y \leq 33.5).


$$

To compute this probability, we transform to a standard normal random variable by $z$-scoring:

$$


\begin{aligned}𝑃(32.5≤𝑌≤33.5) & =𝑃(\frac{32.5−30}{\sqrt{12}}≤𝑍≤\frac{33.5−30}{\sqrt{12}}) \\ & ≈𝑃(0.72≤𝑍≤1.01) \\ & =𝑃(𝑍≤1.01)−𝑃(𝑍<0.72) \\ & =𝑃(𝑍≤1.01)−𝑃(𝑍≤0.72) \\ & =Φ(1.01)−Φ(0.72).\end{aligned}


$$

Using a table of values for the CDF of the standard normal distribution, we find that

$$


\Phi(1.01) = 0.8438, \qquad \Phi(0.72) = 0.7642.


$$

So, we have

$$


\begin{aligned}𝑃(32.5≤𝑌≤33.5) & =Φ(1.01)−Φ(0.72) \\ & =0.8438−0.7642 \\ & =0.0796.\end{aligned}


$$

Therefore,

$$


P(X = 33) \approx 0.0796.


$$

### A Note on Rounding Errors

In the last example, we approximated the binomial random variable

$$


X \sim B(50,0.6)


$$

using a normal random variable

$$


Y \sim N(30,12),


$$

and we arrived at the approximation

$$


P(X=33) \approx P(32.5 \leq Y \leq 33.5) \approx 0.0796.


$$

If you were to use a software package to evaluate this approximation, you might get an answer like

$$


P(X = 33) \approx P(32.5 \leq Y \leq 33.5) \approx 0.0791.


$$

Notice that there is a difference of around $0.0005$ between the two answers.

There is a reason for this discrepancy. When we calculated that $P(X = 33) \approx P(32.5 \leq Y \leq 33.5) \approx 0.0796,$ we rounded our $z$-values two decimal places and then used a lookup table to find $\Phi(z)$ for those rounded values. As a result, we introduced some small rounding errors.

Typically, the rounding errors are small, so we will continue to work with a table of values. However, it's worth bearing this in mind if you're using a software package or calculator to compute $\Phi(z).$

### Example: Using a Normal Approximation to Approximate a Binomial Probability

#### Question

In a city, $44\%$ of the people have blood type A. Using the normal approximation to the binomial distribution, approximate the probability that if $150$ people are picked at random, then $70$ of them will have blood type A. Give your answer to three decimal places.

**

#### Explanation

Given a binomial random variable $X \sim B(n,p),$ if

- $np > 5,$ and

- $n(1-p) > 5,$

we can approximate $X$ as a normal random variable $Y$ with mean $\mu = np$ and variance $\sigma^2 = np(1-p),$ that is,

$$


Y \sim N(np, np(1-p)).


$$

Here, we have $n=150$ and $p = 0.44.$ Therefore,

$$


\begin{aligned}𝑛𝑝 & =150⋅0.44 \\ & =66 \\ & >5\,✓ \\ 𝑛(1−𝑝) & =150⋅(1−0.44) \\ & =84 \\ & >5.\,✓\end{aligned}


$$

So, we can approximate our binomial random variable $X$ with a normal random variable $Y$ with mean

$$


\mu = np = (150)(0.44) = 66


$$

and variance

$$


\sigma^2 = np(1-p) = (150)(0.44)(1-0.44) = 36.96.


$$

That is, we can approximate $X$ by $Y \sim N(66, 36.96).$

Now, we can approximate the desired probability $P(X = 70).$ Using a continuity correction, we have

$$


P(X =70) \approx P(69.5 \leq Y \leq 70.5).


$$

To compute this probability, we transform to a standard normal random variable by $z$-scoring:

$$


\begin{aligned}𝑃(69.5≤𝑌≤70.5) & =𝑃(\frac{69.5−66}{\sqrt{36.96}}≤𝑍≤\frac{70.5−66}{\sqrt{36.96}}) \\ & ≈𝑃(0.58≤𝑍≤0.74) \\ & =𝑃(𝑍≤0.74)−𝑃(𝑍<0.58) \\ & =𝑃(𝑍≤0.74)−𝑃(𝑍≤0.58) \\ & =Φ(0.74)−Φ(0.58) \\ & =0.7704−0.7190 \\ & =0.0514\end{aligned}


$$

Therefore,

$$


P(X = 70)\approx 0.051.


$$

Note: Using a software package for the approximation gives a probability of $0.0528.$

### Example: Using a Normal Approximation to Approximate a Binomial Probability Over an Interval

#### Question

An archer practices firing an arrow at a target $50$ times. The archer has a $47\%$ chance of hitting the bull's eye on each shot. Using the normal approximation to the binomial distribution, estimate the probability that the archer hits the bull's eye more than $29$ times but less than $35$ times. Give your final answer to three decimal places.

**

#### Explanation

Given a binomial random variable $X \sim B(n,p),$ if

- $np > 5,$ and

- $n(1-p) > 5,$

we can approximate $X$ as a normal random variable $Y$ with mean $\mu = np$ and variance $\sigma^2 = np(1-p),$ that is,

$$


Y \sim N(np, np(1-p)).


$$

Here, we have $n=50$ and $p = 0.47.$ Therefore,

$$


\begin{aligned}𝑛𝑝 & =50⋅0.47 \\ & =23.5 \\ & >5\,✓ \\ 𝑛(1−𝑝) & =50⋅(1−0.47) \\ & =26.5 \\ & >5.\,✓\end{aligned}


$$

So, we can approximate our binomial random variable $X$ with a normal random variable $Y$ with mean

$$


\mu = np = (50)(0.47) = 23.5


$$

and variance

$$


\sigma^2 = np(1-p) = (50)(0.47)(1-0.47) = 12.455.


$$

That is, we can approximate $X$ by $Y \sim N(23.5, 12.455).$

Now, we can estimate the desired probability $P(29 < X < 35).$ Using a continuity correction, we have

$$


P(29 < X < 35) = P(30 \leq X \leq 34) \approx P(29.5 \leq Y \leq 34.5).


$$

To compute this probability, we transform to a standard normal random variable by $z$-scoring:

$$


\begin{aligned}𝑃(29.5≤𝑌<34.5) & =𝑃(\frac{29.5−23.5}{\sqrt{12.455}}≤𝑍≤\frac{34.5−23.5}{\sqrt{12.455}}) \\ & ≈𝑃(1.70≤𝑍≤3.12) \\ & =𝑃(𝑍≤3.12)−𝑃(𝑍<1.70) \\ & =𝑃(𝑍≤3.12)−𝑃(𝑍≤1.70) \\ & =Φ(3.12)−Φ(1.70) \\ & =0.9991−0.9554 \\ & =0.0437\end{aligned}


$$

Therefore,

$$


P(29 < X < 35) \approx 0.044.


$$

**** Using a software package for the approximation gives a probability of $0.0436.$

### The Normal Approximation as a Consequence of the Central Limit Theorem

According to the so-called **central limit theorem**, if $X_1, X_2, \ldots X_n$ are independent and identically distributed (I.I.D) random variables, then

$$


X = \sum_{i=1}^n X_i \approx N(n\mu, n\sigma^2),


$$

where $n$ is "sufficiently large," and

$$


\text{E}[X_i] = \mu, \qquad \text{Var}[X_i] = \sigma^2.


$$

Now, if $X\sim B(n,p),$ then $X$ can be thought of as a sum of $n$ I.I.D Bernoulli random variables

$$


X_i\sim\text{Bernoulli}(p),


$$

where the PMF of each $X_i$ is given by

$$


\begin{aligned}𝑝, & \,𝑥=1 \\ 1−𝑝, & \,𝑥=0 \\ 0, & \,otherwise.\end{aligned}


$$

It can be shown that

$$


\text{E}[X_i] = \mu = p, \qquad \text{Var}[X_i] = \sigma^2 = p(1-p).


$$

Therefore, by substituting our values of $\mu$ and $\sigma^2$ into our normal approximation for $X,$ we get

$$


X \approx N\left(np, np(1-p)\right).


$$

The "sufficiently large" condition on $n$ is taken care of by stipulating that $np > 5$ and $n(1-p) > 5\mathbin{:}$

- When $p\approx 0.5,$ then $n\approx 10$ is sufficiently large for the normal approximation to be applied.

- However, if $p$ is closer to zero or one, then the distribution of $X$ is not symmetric, and consequently, we need $n$ to be much larger for the central limit theorem to be valid.
