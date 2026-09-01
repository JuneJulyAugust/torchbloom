# Finite Population Corrections for Sample Means

Source: https://www.mathacademy.com/topics/3930?courseId=73
Topic ID: 3930

## Prerequisites

- [The Central Limit Theorem](./359-the-central-limit-theorem.md)
- [Sampling Proportions From Finite Populations](./3137-sampling-proportions-from-finite-populations.md)

## Lesson

### Introduction

If $X_1,X_2,\ldots,X_n$ is an I.I.D. random sample of size $n$ from a population with mean $\mu$ and variance $\sigma^2,$ then by the central limit theorem (CLT), the sample mean is normally distributed with mean $\mu$ and variance $\dfrac{\sigma^2}{n}{:}$

$$


\overline{X}\sim N\!\left(\mu,\frac{\sigma^2}{n}\right)


$$

This approximation is valid provided that $n$ is sufficiently large (typically $n\geq 30$) and the underlying population is *infinite.*

Populations are rarely infinite in real-world situations. In a previous lesson, we saw that if the population is finite and a sample is conducted *without* replacement, the elements of a sample are not independent! So, does this mean we cannot reliably apply the CLT to model real-world situations?

To answer this question, suppose the sample is drawn *without* replacement from a finite population of size $N.$ We have two cases:

- **Case 1**: If the population size is *large compared to the sample size*, the sample elements will be *approximately* independent. This means that the approximation for the sampling distribution of $\overline{X}$ given by the CLT remains valid.

- **Case 2**: If the population size is *not* large compared to the sample size, individual sample elements are *not* independent! This means that the approximation for the sampling distribution of $\overline{X}$ given by the CLT is no longer valid!

So, it may seem that everything is lost in the second case. However, it turns out that, to account for the dependency of the sample elements, we simply adjust the variance of the sample mean distribution as follows:

$$


\overline{X}\sim N\!\left(\mu,\frac{\sigma^2}{n}\cdot \frac{N-n}{N-1}\right)


$$

This allows us to model the distribution of $\overline X$ even when $N$ is not large compared to $n.$

Note the following:

- The so-called **finite population correction factor** is

$$


\dfrac{N-n}{N-1}.


$$

- It's appropriate to apply the correction factor whenever $n > 5\%\cdot N$ (i.e., the sample includes more than $5\%$ of the population).

- If $N$ is much larger than $n,$ then and we recover the approximation given by the CLT.

- For $N > n > 1,$ we have This means the correction factor *reduces* the variance of $\overline X$ compared to the CLT approximation. This makes intuitive sense. If we sample from a small population without replacement, the pool of remaining elements becomes smaller with each element sampled, reducing their variability.

- Finally, if $N=n >1,$ then the finite population correction factor equals zero, which means the variance of $\overline X$ equals zero. Again, this makes intuitive sense. If the sample contains *every* element from the population, then the sample mean equals the population mean, i.e., $\overline X = \mu,$ and there is no variation.

Finally, suppose that a sample is conducted from a finite population *with replacement* (in other words, we're free to select the same element from the population more than once). In this case, the sample data are independent, and a finite population correction factor is not required. Sampling with replacement effectively makes the population infinite, so a correction to the variance is unnecessary.

### Example: Identifying Situations Where a Correction Factor Is Necessary

#### Question

A customer service department of a large retailer surveys a population of $1800$ customers about their experience with recent purchases. For which of the following situations is it necessary to use a finite population correction factor to adjust the variance in the distribution of the sample mean?

1. They select a sample of $n=75$ customers, and each customer is interviewed once.

2. They select a sample of $n=100$ customers, and each customer is interviewed once.

3. They select a sample of $n=150$ customers. For data protection reasons, they decided not to keep track of the customers they interviewed so that each customer could be interviewed more than once.

**

#### Explanation

Suppose that $X_1,X_2,\ldots,X_n$ is a random sample of size $n$ from a population with population mean $\mu$ and population standard deviation $\sigma.$ The central limit theorem (or CLT) states that for sufficiently large $n,$ the distribution of the sample mean $\overline{X}$ can be approximated as

$$


\overline{X}\sim N\!\left(\mu,\frac{\sigma^2}{n}\right).


$$

We typically use this approximation when $n\geq 30.$

However, if the population size is not large compared to the sample size, the sample data is not independent. To account for this, we add a correction factor to the variance of the sample mean distribution, as follows:

$$


\overline{X}\sim N\!\left(\mu,\frac{\sigma^2}{n}\cdot \frac{N-n}{N-1}\right),


$$

where $N$ is the population size.

The term

$$


\dfrac{N-n}{N-1}


$$

is called the finite population correction factor, and it is appropriate to use it when $n > 5\%\cdot N$ (the sample includes more than $5\%$ of the entire population).

Note that if a sample is conducted from a finite population **, then the sample data are independent, and a finite population correction factor is not required.

In our case, we have

$$


N = 1800, \quad 5\%\cdot N = 90.


$$

Let's now examine each situation. Notice that $n\geq 30$ in all cases, so the central limit theorem applies.

- In situation I, we have Therefore, we can approximate the distribution of $\overline{\,X}$ using a normal distribution, but the finite population correction factor is unnecessary.

- In situation II, we have Additionally, the sample is conducted without replacement (since each customer is interviewed only once). Therefore, we can approximate the distribution of $\overline{\,X}$ using a normal distribution with the finite population correction factor

- In situation III, the finite population correction factor is unnecessary because the sample is independent (since each customer can be interviewed more than once). Therefore, we can approximate the distribution of $\overline{\,X}$ using a normal distribution, but the finite population correction factor is not necessary.

Therefore, the correct answer is "II only".

### Example: Finding an Approximate Probability for a Sample Mean

#### Question

Let $X_1, X_2, \ldots, X_{30}$ be a random sample of size $n = 30$ conducted without replacement from a population of $N=100$ individuals with population mean $\mu = 2$ and population standard deviation $\sigma = 4.$

If $\Phi(z)$ denotes the cumulative distribution function for the standard normal distribution, find the probability that the sample mean is between $2.1$ and $2.3.$ Express your answer in terms of $\Phi(z),$ the cumulative distribution function of the standard normal distribution.

#### Explanation

Suppose that $X_1,X_2,\ldots,X_n$ is a random sample of size $n$ from a population with population mean $\mu$ and population standard deviation $\sigma.$ The central limit theorem (or CLT) states that for sufficiently large $n,$ the distribution of the sample mean $\overline{X}$ can be approximated as

$$


\overline{X}\sim N\!\left(\mu,\frac{\sigma^2}{n}\right).


$$

We typically use this approximation when $n\geq 30.$

However, if the population size is not large compared to the sample size, the sample data is not independent. To account for this, we add a correction factor to the variance of the sample mean distribution, as follows:

$$


\overline{X}\sim N\!\left(\mu,\frac{\sigma^2}{n}\cdot \frac{N-n}{N-1}\right),


$$

where $N$ is the population size.

The term

$$


\dfrac{N-n}{N-1}


$$

is called the finite population correction factor, and it is appropriate to use it when $n > 5\%\cdot N$ (the sample includes more than $5\%$ of the entire population).

Note that if a sample is conducted from a finite population **, then the sample data are independent, and a finite population correction factor is not required.

In our case, we have

$$


n = 30, \qquad \mu = 2, \qquad \sigma = 4.


$$

Since $n > 5\%\cdot N = 0.05\cdot 100= 5,$ we must use the following finite population correction factor:

$$


\dfrac{N-n}{N-1} = \dfrac{100-30}{100-1} = \dfrac{70}{99}


$$

Therefore, by the CLT, we have that the distribution of the sample mean can be approximated as

$$


\begin{aligned}\overset{𝑋}{} & ∼𝑁\,(𝜇,\,\frac{𝜎^{2}}{𝑛}⋅\frac{𝑁−𝑛}{𝑁−1}) \\ & ∼𝑁\,(2,\,\frac{4^{2}}{30}⋅\frac{70}{99}) \\ & ∼𝑁(2,\,\frac{112}{297}).\end{aligned}


$$

We want to find $P(2.1 < \overline{X} < 2.3).$ So, we convert $\overline{X}$ to a standard normal random variable by $z$-scoring:

$$


\begin{aligned}𝑃(2.1<\overset{𝑋}{}<2.3) & =𝑃\frac{2.1−2}{\sqrt{\frac{112}{297}}}<𝑍<\frac{2.3−2}{\sqrt{\frac{112}{297}}} \\ & ≈𝑃(0.16<𝑍<0.49) \\ & =𝑃(𝑍≤0.49)−𝑃(𝑍≤0.16) \\ & =Φ(0.49)−Φ(0.16)\end{aligned}


$$

Therefore,

$$


P(2.1 < \overline{X} < 2.3) \approx \Phi(0.49) - \Phi(0.16).


$$

### Example: Finding an Approximate Probability for a Sample Mean in Context

#### Question

A study aims to assess the average scores of a population of $N=676$ students in a particular school district. They took the scores of a sample of $n=52$ students. Given that the population mean score is $\mu=75\%$ with population standard deviation $\sigma=15,$ what is the probability that the mean score of the students in the sample is more than $70\%?$

**

#### Explanation

Suppose that $X_1,X_2,\ldots,X_n$ is a random sample of size $n$ from a population with population mean $\mu$ and population standard deviation $\sigma.$ The central limit theorem (or CLT) states that for sufficiently large $n,$ the distribution of the sample mean $\overline{X}$ can be approximated as

$$


\overline{X}\sim N\!\left(\mu,\frac{\sigma^2}{n}\right).


$$

We typically use this approximation when $n\geq 30.$

However, if the population size is not large compared to the sample size, the sample data is not independent. To account for this, we add a correction factor to the variance of the sample mean distribution, as follows:

$$


\overline{X}\sim N\!\left(\mu,\frac{\sigma^2}{n}\cdot \frac{N-n}{N-1}\right),


$$

where $N$ is the population size.

The term

$$


\dfrac{N-n}{N-1}


$$

is called the finite population correction factor, and it is appropriate to use it when $n > 5\%\cdot N$ (the sample includes more than $5\%$ of the entire population).

Note that if a sample is conducted from a finite population **, then the sample data are independent, and a finite population correction factor is not required.

In our case, we have

$$


n = 52, \qquad \mu = 75, \qquad \sigma = 15.


$$

Since $n > 5\%\cdot N = 0.05\cdot 676= 33.8,$ we must use the following finite population correction factor:

$$


\dfrac{N-n}{N-1} = \dfrac{676-52}{676-1} = \dfrac{208}{225}


$$

Therefore, by the CLT, we have that the distribution of the sample mean can be approximated as

$$


\begin{aligned}\overset{𝑋}{} & ∼𝑁\,(𝜇,\,\frac{𝜎^{2}}{𝑛}⋅\frac{𝑁−𝑛}{𝑁−1}) \\ & ∼𝑁\,(75,\,\frac{15^{2}}{52}⋅\frac{208}{225}) \\ & ∼𝑁(75,\,4).\end{aligned}


$$

We want to find $P(\overline{X} \gt 70).$ So, we convert $\overline{X}$ to a standard normal random variable by $z$-scoring:

$$


\begin{aligned}𝑃(\overset{𝑋}{}>70) & =𝑃(𝑍>\frac{70−75}{\sqrt{4}}) \\ & =𝑃(𝑍>−2.5) \\ & =1−𝑃(𝑍≤−2.5) \\ & =1−Φ(−2.5)\end{aligned}


$$

From the table, we have

$$


\begin{aligned}Φ(−2.5)=0.0062.\end{aligned}


$$

Therefore,

$$


\begin{aligned}𝑃(\overset{𝑋}{}>70) & =1−Φ(−2.5) \\ & =1−0.0062 \\ & =0.9938.\end{aligned}


$$
