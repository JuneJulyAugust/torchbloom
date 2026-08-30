# Finite Population Corrections for Sample Proportions

Source: https://www.mathacademy.com/topics/5020?courseId=73
Topic ID: 5020

## Prerequisites

- [Finite Population Corrections for Sample Means](./3930-finite-population-corrections-for-sample-means.md)
- [Point Estimates of Population Proportions](./3932-point-estimates-of-population-proportions.md)

## Lesson

### Introduction

Consider a population in which an unknown proportion $p$ of individuals has a particular characteristic. Suppose we draw an independent random sample of size $n$ from this population and use it to find an estimate for $p.$

By the central limit theorem, the sampling distribution of the sample proportion $\widehat{\,p}$ can be approximated as

$$


\widehat{\,p} \sim N\left( p, \dfrac{p(1-p)}{n}\right).


$$

For this approximation to be valid, we require that

- more than five sample elements have the characteristic $(np>5),$ and

- more than five sample elements do *not* have the characteristic $(n(1-p)>5).$

This approximation assumes that the population from which the sample is drawn is infinite. So what happens when the population is finite?

Similar to previous cases we've seen, we can apply a *finite population correction factor* whenever a sample is conducted *without* replacement, and the population size is not large compared to the sample size. In such cases, the distribution of the sample proportion $\widehat{\,p}$ is given by

$$


\widehat{\,p} \sim N\left( p, \dfrac{p(1-p)}{n}\cdot \dfrac{N-n}{N-1} \right),


$$

where $N$ is the population size.

The correction factor should be applied whenever the sample size is at least $5\%$ of the population size.

$$


n > 5\%\cdot N


$$

Finally, note that if samples are drawn *with* replacement, each element can be selected multiple times. This effectively makes the population infinite, so the correction factor is unnecessary in this case.

### Example: Identifying Situations Where a Correction Factor Is Necessary

#### Question

A container contains $480$ yellow peppers and $320$ red peppers. We wish to construct a statistical model for $\widehat{\,p},$ the proportion of red peppers in a random sample.

Consider the following random samples.

1. $35$ peppers are drawn from the container without replacement.

2. $40$ peppers are drawn from the container with replacement.

3. $50$ peppers are drawn from the container without replacement.

Which of these sampling methods requires a finite population correction factor to be applied to model $\widehat{\,p}$ as normal?

**

#### Explanation

Given a population of $N$ individuals in which a proportion $p$ of the population has a particular characteristic, the sampling distribution of the sample proportion $\widehat{\,p}$ can be approximated as

$$


\widehat{\,p} \sim N\left( p, \dfrac{p(1-p)}{n}\cdot \dfrac{N-n}{N-1} \right),


$$

where

- $n$ is the sample size,

- $np > 5$ (more than $5$ sample elements have the characteristic), and

- $n(1-p) > 5$ (more than $5$ sample elements do not have the characteristic).

The factor

$$


\dfrac{N-n}{N-1}


$$

is the finite population correction factor for the variance. This is used in cases of finite samples where

- $n\gt 5\%\cdot N$ (i.e., the sample comprises more than $5\%$ of the population), and

- the sample is conducted without replacement.

If a sample is conducted from a finite population **, then the sample data are independent, and a finite population correction factor is not required.

In our case, we have

$$


N = 480 + 320 = 800, \qquad p=\dfrac{320}{800} = 0.4, \qquad 5\%\cdot N = 40.


$$

Let's now examine each situation. In all cases, we are told that $np>5, n(1-p)>5.$ So, we only need to check the requirement $n\gt 5\%\cdot N$ and that the samples are conducted without replacement.

- In situation I, we have $n \leq 40.$ Since the sample size is ** than $5\%$ of the population, the finite population correction factor is **** necessary when modeling the distribution of $\widehat{\,p}.$

- In situation II, since the sample is conducted with replacement, the finite population correction factor is **** necessary when modeling the distribution of $\widehat{\,p}.$

- In situation III, we have $n \gt 40.$ Since the sample size is ** than $5\%$ of the population and the sample is conducted without replacement, the finite population correction factor is necessary when modeling the distribution of $\widehat{\,p}.$

Therefore, the correct answer is "III only".

### Example: Finding an Approximate Probability for a Sample Proportion

#### Question

Let $X_1, X_2, \ldots, X_{30}$ be a random sample of size $n = 30$ conducted without replacement from a population of $N=100$ individuals where $25\%$ of the population has a particular characteristic.

Find the probability that the proportion of individuals in the sample having the characteristic is between $35\%$ and $50\%.$ Express your answer in terms of $\Phi(z),$ the cumulative distribution function for the standard normal distribution.

#### Explanation

Given a population of $N$ individuals in which a proportion $p$ of the population has a particular characteristic, the sampling distribution of the sample proportion $\widehat{\,p}$ can be approximated as

$$


\widehat{\,p} \sim N\left( p, \dfrac{p(1-p)}{n}\cdot \dfrac{N-n}{N-1} \right),


$$

where

- $n$ is the sample size,

- $np > 5$ (more than $5$ sample elements have the characteristic), and

- $n(1-p) > 5$ (more than $5$ sample elements do not have the characteristic).

The factor

$$


\dfrac{N-n}{N-1}


$$

is the finite population correction factor for the variance. This is used in cases of finite samples where

- $n\gt 5\%\cdot N$ (i.e., the sample comprises more than $5\%$ of the population), and

- The sample is conducted without replacement.

If a sample is conducted from a finite population **, then the sample data are independent, and a finite population correction factor is not required.

In our case, we have

$$


n = 30, \qquad p = 0.25, \qquad N = 100.


$$

Now, since

$$


\begin{aligned}𝑛 & >5\%⋅100=5 \\ 𝑛𝑝 & =30(0.25)=7.5>5 \\ 𝑛(1−𝑝) & =30(0.75)=22.5>5\end{aligned}


$$

we can apply the above approximation.

The sampling distribution of the sample proportion, in this case, can be approximated as

$$


\begin{aligned}\overset{\,𝑝}{ˆ} & ∼𝑁(𝑝,\,\frac{𝑝(1−𝑝)}{𝑛}⋅\frac{𝑁−𝑛}{𝑁−1}) \\ & ∼𝑁(0.25,\,\frac{0.25(1−0.25)}{30}⋅\frac{70}{99}) \\ & ∼𝑁(0.25,\frac{7}{1\,584}).\end{aligned}


$$

The probability we wish to find is $P\left(0.35 \lt \widehat{\,p} \lt 0.5\right).$ So, we convert $\widehat{\,p}$ to a standard normal random variable by $z$-scoring:

$$


\begin{aligned}𝑃(0.35<\overset{\,𝑝}{ˆ}<0.5) & =𝑃\frac{0.35−0.25}{\sqrt{√\frac{7}{1\,584}}}<𝑍<\frac{0.5−0.25}{\sqrt{√\frac{7}{1\,584}}} \\ & ≈𝑃(1.50<𝑍<3.76) \\ & =𝑃(𝑍<3.76)−𝑃(𝑍<1.50) \\ & =Φ(3.76)−Φ(1.50)\end{aligned}


$$

Therefore,

$$


P\left(0.35 \lt \widehat{\,p} \lt 0.5\right) \approx \Phi(3.76) - \Phi(1.50).


$$

### Example: Finding an Approximate Probability for a Sample Proportion in Context

#### Question

Of the $182$ members of a gym, $80\%$ work out for more than $100$ minutes each visit. Suppose we draw a random sample of $32$ members of this gym. Find the probability that the number of gym members in the sample who work out for more than $100$ minutes each visit is at least $24.$

**

#### Explanation

Given a population of $N$ individuals in which a proportion $p$ of the population has a particular characteristic, the sampling distribution of the sample proportion $\widehat{\,p}$ can be approximated as

$$


\widehat{\,p} \sim N\left( p, \dfrac{p(1-p)}{n}\cdot \dfrac{N-n}{N-1} \right),


$$

where

- $n$ is the sample size,

- $np > 5$ (more than $5$ sample elements have the characteristic), and

- $n(1-p) > 5$ (more than $5$ sample elements do not have the characteristic).

The factor

$$


\dfrac{N-n}{N-1}


$$

is the finite population correction factor for the variance. This is used in cases of finite samples where

- $n\gt 5\%\cdot N$ (i.e., the sample comprises more than $5\%$ of the population), and

- the sample is conducted without replacement.

If a sample is conducted from a finite population **, then the sample data are independent, and a finite population correction factor is not required.

In our case, we have

$$


n = 32, \qquad p = 0.8, \qquad N = 182.


$$

Now, since

$$


\begin{aligned}𝑛 & >5\%⋅182=9.1 \\ 𝑛𝑝 & =32(0.8)=25.6>5 \\ 𝑛(1−𝑝) & =32(0.2)=6.4>5\end{aligned}


$$

we can apply the above approximation.

The sampling distribution of the sample proportion, in this case, can be approximated as

$$


\begin{aligned}\overset{\,𝑝}{ˆ} & ∼𝑁(𝑝,\,\frac{𝑝(1−𝑝)}{𝑛}⋅\frac{𝑁−𝑛}{𝑁−1}) \\ & ∼𝑁(0.8,\,\frac{0.8(1−0.8)}{32}⋅\frac{150}{181}) \\ & ∼𝑁(0.8,\frac{3}{724}).\end{aligned}


$$

The probability we wish to find is $P\left(\widehat{\,p} \geq \dfrac{24}{32}\right) = P\left(\widehat{\,p} \geq 0.75 \right).$ So, we convert $\widehat{\,p}$ to a standard normal random variable by $z$-scoring:

$$


\begin{aligned}𝑃(\overset{\,𝑝}{ˆ}≥0.75) & =𝑃𝑍≥\frac{0.75−0.8}{\sqrt{√\frac{3}{724}}} \\ & =𝑃(𝑍≥−0.78) \\ & =1−𝑃(𝑍<−0.78) \\ & =1−Φ(−0.78)\end{aligned}


$$

From the table, we have

$$


\begin{aligned}Φ(−0.78)=0.2177.\end{aligned}


$$

Therefore,

$$


\begin{aligned}𝑃(\overset{\,𝑝}{ˆ}≥0.75) & =1−Φ(−0.78) \\ & =1−0.2177 \\ & =0.7823.\end{aligned}


$$
