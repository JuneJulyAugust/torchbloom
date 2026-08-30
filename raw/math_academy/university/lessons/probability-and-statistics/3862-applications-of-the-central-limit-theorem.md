# Applications of the Central Limit Theorem

Source: https://www.mathacademy.com/topics/3862?courseId=73
Topic ID: 3862

## Prerequisites

- [The Central Limit Theorem](./359-the-central-limit-theorem.md)
- [Mean and Variance of the Binomial Distribution](./2149-mean-and-variance-of-the-binomial-distribution.md)
- [Mean and Variance of the Poisson Distribution](./2991-mean-and-variance-of-the-poisson-distribution.md)
- [Mean and Variance of the Geometric Distribution](./2992-mean-and-variance-of-the-geometric-distribution.md)
- [Mean and Variance of the Continuous Uniform Distribution](./3277-mean-and-variance-of-the-continuous-uniform-distribution.md)

## Lesson

### Introduction

Suppose $X_1, X_2, \ldots, X_n$ is a random sample of size $n$ from a distribution with population mean $\mu$ and population variance $\sigma^2.$ Let's define a new random variable as the sum of all $X_i$'s as follows:

$$


X = \sum_{i=1}^n X_i


$$

The sample mean $\overline{X}$ is given by

$$


\overline{X} = \dfrac1n \sum_{i=1}^n X_i


$$

which is equivalent to

$$


n\cdot \overline{X} =\sum_{i=1}^n X_i.


$$

Therefore, our random variable $X$ is simply the product of $n$ with the sample mean:

$$


X = n\cdot \overline{X}.


$$

Now, the central limit theorem (CLT) states that for sufficiently large $n,$ the distribution of $\overline{X}$ can be approximated as

$$


\overline{X}\sim N\!\left(\mu,\frac{\sigma^2}{n}\right).


$$

Therefore, since

$$


\textrm{E}[\overline X] = \mu, \qquad \textrm{Var}[\overline X] = \dfrac{\sigma^2}{n}


$$

we can calculate $\textrm E[X]$ and $\textrm{Var}[X]$ using the properties of mean and variance as follows:

$$


\begin{aligned}E[𝑋] & =E[𝑛\overset{𝑋}{}] \\ & =𝑛⋅E[\overset{𝑋}{}] \\ & =𝑛𝜇 \\ Var[𝑋] & =Var[𝑛\overset{𝑋}{}] \\ & =𝑛^{2}⋅Var[\overset{𝑋}{}] \\ & =𝑛^{2}⋅\frac{𝜎^{2}}{𝑛} \\ & =𝑛𝜎^{2}\end{aligned}


$$

Finally, since $\overline{X}$ is (approximately) normally distributed, we have that $X$ is also approximately normal. Therefore,

$$


X\sim N(n\mu, n\sigma^2).


$$

This is an important result. It tells us that provided that we have a sufficiently large I.I.D. sample, the sum of the elements from that sample is approximately normally distributed with mean $n\mu$ and variance $n\sigma^2.$ This result does not depend on the distribution of the $X_i$'s!

### Example: Applying the CLT to Continuous Uniform Random Variables

#### Question

Let $X_1,X_2,\ldots,X_{110} \sim U[1,5]$ be an I.I.D. sample of size $110$ from the continuous uniform distribution on the interval $[1,5].$ Suppose we define the random variable $X$ as

$$


X = \sum_{i=1}^{110} X_i.


$$

What is the approximate distribution of $X?$

#### Explanation

Recall that the central limit theorem states the following:

**

$$


\overline{X}\sim N\!\left(\mu,\frac{\sigma^2}{n}\right).


$$

Moreover, if we define

$$


X = \sum_{i=1}^n X_i


$$

then, by the properties of mean and variance, we have

$$


\textrm{E}[X] = n\mu, \qquad \textrm{Var}[X] = n\sigma^2


$$

and consequently,

$$


X\sim N(n\mu, n\sigma^2).


$$

The expected value and the variance of a uniform random variable $X_i \sim U[a,b]$ can be found as

$$


\textrm{E}[X_i] = \dfrac{a+b}{2}, \qquad \textrm{Var}[X_i] = \dfrac{(b-a)^2}{12}.


$$

So, in our case, we have

$$


\begin{aligned}𝑛 & =110, \\ 𝜇 & =E[𝑋_{𝑖}] \\ & =\frac{𝑎+𝑏}{2} \\ & =\frac{1+5}{2} \\ & =\frac{6}{2} \\ & =3, \\ 𝜎^{2} & =Var[𝑋_{𝑖}] \\ & =\frac{(𝑏−𝑎)^{2}}{12} \\ & =\frac{(5−1)^{2}}{12} \\ & =\frac{16}{12} \\ & =\frac{4}{3}.\end{aligned}


$$

Therefore, for the approximate distribution of $X,$ we obtain

$$


\begin{aligned}𝑋 & ∼𝑁\,(𝑛𝜇,𝑛𝜎^{2}) \\ & ∼𝑁\,(110⋅3,110⋅\frac{4}{3}) \\ & ∼𝑁\,(330,\frac{440}{3}).\end{aligned}


$$

### Example: Applying the CLT to Binomial Random Variables

#### Question

Given that $X_i\sim B\left(25,\dfrac{9}{20}\right)$ for $i=1,2,\ldots,66$ are independent binomial random variables, what is the approximate distribution of the sample mean $\overline{X}?$

#### Explanation

Recall that the central limit theorem states the following:

**

$$


\overline{X}\sim N\!\left(\mu,\frac{\sigma^2}{n}\right).


$$

The expected value and the variance of a binomial random variable $X_i \sim B(m,p)$ can be found as

$$


\textrm{E}[X_i] = mp, \qquad \textrm{Var}[X_i] = mp(1-p).


$$

So, in our case, we have

$$


\begin{aligned}𝑛 & =66, \\ 𝜇 & =E[𝑋_{𝑖}] \\ & =𝑚𝑝 \\ & =25⋅\frac{9}{20} \\ & =\frac{45}{4}, \\ 𝜎^{2} & =Var[𝑋_{𝑖}] \\ & =𝑚𝑝(1−𝑝) \\ & =25⋅\frac{9}{20}⋅\frac{11}{20} \\ & =\frac{99}{16}.\end{aligned}


$$

Therefore, for the approximate distribution of the sample mean $\overline{X},$ we obtain

$$


\begin{aligned}\overset{𝑋}{} & ∼𝑁\,(𝜇,\frac{𝜎^{2}}{𝑛}) \\ & ∼𝑁(\frac{45}{4},\,\frac{99}{16}⋅\frac{1}{66}) \\ & ∼𝑁(\frac{45}{4},\frac{3}{32}).\end{aligned}


$$

### Example: Applying the CLT to Geometric Random Variables

#### Question

Let $X_i \sim \textrm{Geom}(0.4)$ for $i=1,2,\ldots,80$ be independent geometric random variables. Suppose we define the random variable $X$ as

$$


X = \sum_{i=1}^{80} X_i.


$$

What is the approximate distribution of $X?$

#### Explanation

Recall that the central limit theorem states the following:

**

$$


\overline{X}\sim N\!\left(\mu,\frac{\sigma^2}{n}\right).


$$

Moreover, if we define

$$


X = \sum_{i=1}^n X_i


$$

then by the properties of mean and variance, we have

$$


\textrm{E}[X] = n\mu, \qquad \textrm{Var}[X] = n\sigma^2


$$

and consequently,

$$


X\sim N(n\mu, n\sigma^2).


$$

The expected value and the variance of a geometric random variable $X_i \sim \textrm{Geom}(p)$ can be found as

$$


\textrm{E}[X_i] = \dfrac{1}{p}, \qquad \textrm{Var}[X_i] = \dfrac{1-p}{p^2}.


$$

So, in our case, we have

$$


\begin{aligned}𝑛 & =80, \\ 𝜇 & =E[𝑋_{𝑖}] \\ & =\frac{1}{𝑝} \\ & =\frac{1}{0.4} \\ & =\frac{5}{2}, \\ 𝜎^{2} & =Var[𝑋_{𝑖}] \\ & =\frac{1−𝑝}{𝑝^{2}} \\ & =\frac{1−0.4}{0.4^{2}} \\ & =\frac{0.6}{0.16} \\ & =\frac{15}{4}.\end{aligned}


$$

Therefore, for the approximate distribution of $X,$ we obtain

$$


\begin{aligned}𝑋 & ∼𝑁\,(𝑛𝜇,𝑛𝜎^{2}) \\ & ∼𝑁\,(80⋅\frac{5}{2},80⋅\frac{15}{4}) \\ & ∼𝑁\,(200,300).\end{aligned}


$$

### Example: Applying the CLT to Poisson Random Variables

#### Question

Given that $X_i \sim \textrm{Po}(12)$ for $i=1,2,\ldots,60$ are independent Poisson random variables, what is the approximate distribution of the sample mean $\overline{X}?$

#### Explanation

Recall that the central limit theorem states the following:

**

$$


\overline{X}\sim N\!\left(\mu,\frac{\sigma^2}{n}\right).


$$

The expected value and the variance of a Poisson random variable $X_i \sim \textrm{Po}(\lambda)$ can be found as

$$


\textrm{E}[X_i] = \textrm{Var}[X_i] = \lambda.


$$

So, in our case, we have

$$


\begin{aligned}𝑛 & =60, \\ 𝜇 & =E[𝑋_{𝑖}]=12, \\ 𝜎^{2} & =Var[𝑋_{𝑖}]=12.\end{aligned}


$$

Therefore, for the approximate distribution of the sample mean $\overline{X},$ we obtain

$$


\begin{aligned}\overset{𝑋}{} & ∼𝑁\,(𝜇,\frac{𝜎^{2}}{𝑛}) \\ & ∼𝑁\,(12,\frac{12}{60}) \\ & ∼𝑁\,(12,\frac{1}{5}).\end{aligned}


$$
