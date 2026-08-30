# Variance of Sample Means

Source: https://www.mathacademy.com/topics/3013?courseId=73
Topic ID: 3013

## Prerequisites

- [Limits of Reciprocal Functions](../ap-calculus-ab/1905-limits-of-reciprocal-functions.md)
- [Solving Radical Inequalities](../integrated-math-iii-honors/2856-solving-radical-inequalities.md)
- [Variance of Sums of Independent Random Variables](./3062-variance-of-sums-of-independent-random-variables.md)
- [Sampling Distributions](./3864-sampling-distributions.md)

## Lesson

### Introduction

Recall that if $X_1, X_2, \ldots, X_{n}$ is a random sample of size $n$ drawn from a population with mean $\mu$ and variance $\sigma^2,$ then the sample mean, denoted $\overline{X},$ is given by

$$


\overline{X} = \dfrac1n\sum_{i=1}^n X_i.


$$

The sample mean is a random variable whose probability distribution (also called the **sampling distribution**) has an expected value of $\mu\mathbin{:}$

$$


\textrm{E}[\overline{X}] = \mu


$$

In other words, the sample mean $\overline{X}$ is an unbiased estimate of the population mean $\mu.$

Let's now find the variance of the sampling distribution of $\overline{X}.$ Using the properties of variance for sums of independent random variables, we obtain the following:

$$


\begin{aligned}Var[\overset{𝑋}{}] & =Var[\frac{1}{𝑛}\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}𝑋_{𝑖}] \\ & =(\frac{1}{𝑛})^{2}⋅Var[\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}𝑋_{𝑖}] \\ & =\frac{1}{𝑛^{2}}⋅Var[𝑋_{1}+𝑋_{2}+⋯+𝑋_{𝑛}] \\ & =\frac{1}{𝑛^{2}}⋅(Var[𝑋_{1}]+Var[𝑋_{2}]+⋯+Var[𝑋_{𝑛}]) \\ & =\frac{1}{𝑛^{2}}⋅(𝜎^{2}+𝜎^{2}+⋯+𝜎^{2}) \\ & =\frac{1}{𝑛^{2}}⋅𝑛𝜎^{2} \\ & =\frac{𝜎^{2}}{𝑛}\end{aligned}


$$

To summarize, we have the following important result:

$$


\textrm{Var}[\overline{X}] = \dfrac{\sigma^2}{n}


$$

It should be noted that we don't yet know the sampling distribution of $\overline{X}.$ What we *do* know is that whatever the sampling distribution of $\overline{X}$ is, it has mean $\mu$ and variance $\dfrac{\sigma^2}{n}.$

### Example: Finding the Variance of a Sample Mean

#### Question

A sample $X_1, X_2$ of two pills is drawn from a population. The population has pills of two different active ingredient concentrations, $30\,\textrm{mg/ml}$ and $\textrm{15}\,\textrm{mg/ml},$ distributed in the ratio $1:2.$ Calculate $\textrm{Var}[\overline{X}].$

#### Explanation

If $X_1, X_2, \ldots, X_{n}$ is a sample of size $n$ from a population with population mean $\mu$ and population variance $\sigma^2,$ then

$$


\textrm{E}[\overline{X}] = \mu, \qquad \textrm{Var}[\overline{X}] = \dfrac{\sigma^2}{n}.


$$

We're told that the pills in the population have concentrations of $30\,\textrm{mg/ml}$ and $15\,\textrm{mg/ml},$ and these are distributed in the ratio $1:2.$ Therefore, to compute the population mean and variance, we can consider a population consisting of $1+2 = 3$ pills with only the following concentrations:

$$


30\,\textrm{mg/ml}, \qquad 15\,\textrm{mg/ml}, \qquad 15\,\textrm{mg/ml}.


$$

Therefore, the population mean is

$$


\begin{aligned}𝜇 & =\frac{1}{3}\underset{𝑖}{∑}𝑥_{𝑖} \\ & =\frac{1}{3}(30+2⋅15) \\ & =\frac{60}{3} \\ & =20\,mg/ml,\end{aligned}


$$

and the population variance is

$$


\begin{aligned}𝜎^{2} & =\frac{1}{3}\underset{𝑖}{∑}𝑥_{2𝑖}^{}−𝜇^{2} \\ & =\frac{1}{3}(30^{2}+2⋅15^{2})−20^{2} \\ & =\frac{1}{3}(900+450)−400 \\ & =\frac{1}{3}⋅1\,350−400 \\ & =450−400 \\ & =50\,(mg/ml)^{2}.\end{aligned}


$$

Finally, since the sample size $n=2,$ we have

$$


\textrm{Var}[\overline{X}] =\dfrac{\sigma^2}{n} = \dfrac{50}{2} = 25\,(\textrm{mg/ml})^2.


$$

### The Standard Error

The standard deviation of the sample mean is called the **standard error** of the sample mean and is denoted $\textrm{SE}[\overline{X}]\mathbin{:}$

$$


\textrm{SE}[\overline{X}] = \sqrt{\textrm{Var}[\overline{X}]}


$$

So, if we have a random sample of size $n$ drawn from a population with mean $\mu$ and variance $\sigma^2,$ then the standard error is given by

$$


\textrm{SE}[\overline{X}] = \sqrt{\dfrac{\sigma^2}{n}} = \dfrac{\sigma}{\sqrt n}.


$$

### Example: Finding the Standard Error

#### Question

If $X_1, X_2, \ldots, X_{200}$ is a sample of size $n=200$ drawn from a population with mean $\mu = 23$ and variance $\sigma^2 = 4,$ calculate the standard error of $\overline{X}.$ Round your answer to two decimal places.

#### Explanation

If $X_1, X_2, \ldots, X_{n}$ is a sample of size $n$ from a population with population mean $\mu$ and population variance $\sigma^2,$ then

$$


\textrm{E}[\overline{X}] = \mu, \qquad \textrm{Var}[\overline{X}] = \dfrac{\sigma^2}{n},


$$

and the standard error is given by

$$


\textrm{SE}[\overline{X}] = \sqrt{\textrm{Var}[\overline{X}]} = \dfrac{\sigma}{\sqrt n}.


$$

Since the population variance is $\sigma^2 = 4$ and the sample size is $n=200,$ we have that

$$


\begin{aligned}Var[\overset{𝑋}{}] & =\frac{4}{200} \\ & =0.02.\end{aligned}


$$

Therefore,

$$


\textrm{SE}[\overline{X}] = \sqrt{0.02} \approx 0.14 .


$$

### The Sample Mean and Large Samples

Suppose we have a random sample $X_1, X_2, \ldots X_n$ of size $n$ from a population with mean $\mu$ and variance $\sigma^2.$ We know that the sample mean

$$


\overline{X} = \dfrac1n\sum_{i=1}^n X_i


$$

is an unbiased estimator of $\mu.$

However, it should be noted that selecting a single observation $X_i$ to represent the whole could *also* be considered an unbiased estimator of the population mean.! Recall that, by assumption

$$


\textrm{E}[X_i] = \mu, \qquad 1\leq i\leq n.


$$

In what sense is $\overline{X}$ a "better" estimator of $\mu$ than, say, $X_1?$ The answer lies in their respective variances.

As the sample size $n$ becomes larger and larger, the variance and standard error of $\overline{X}$ become smaller and smaller. It is easy to see that, as $n\to\infty,$ we have

$$


\textrm{Var}[\overline{X}] = \dfrac{\sigma^2}{n} \to 0, \qquad \textrm{SE}[\overline{X}] = \dfrac{\sigma}{\sqrt{n}} \to 0.


$$

So, when the sample size $n$ is large, there is less variance in the sampling distribution of $\overline{X}.$ Therefore, the larger the sample, the more likely it is that $\overline{X}$ will give good estimates for $\mu.$ The individual sample elements do not have this property since $\textrm{Var}[X_i] = \sigma^2.$

The key takeaway is that the sample mean $\overline{X}$ becomes a better estimator for the corresponding population mean $\mu$ as the sample size $n$ increases.

### Example: Calculating an Appropriate Sample Size

#### Question

A sample $X_1, X_2, \ldots, X_{n}$ of $n$ coconuts is drawn from a population. The population has coconuts of two different weights, $1.5\,\textrm{lb}$ and $2\,\textrm{lb},$ distributed in the ratio $2:3.$ Determine the smallest sample size required to give a standard error of less than $0.02\,\textrm{lb}.$

#### Explanation

If $X_1, X_2, \ldots, X_{n}$ is a sample of size $n$ from a population with population mean $\mu$ and population variance $\sigma^2,$ then

$$


\textrm{E}[\overline{X}] = \mu, \qquad \textrm{Var}[\overline{X}] = \dfrac{\sigma^2}{n},


$$

and the standard error is given by

$$


\textrm{SE}[\overline{X}] = \sqrt{\textrm{Var}[\overline{X}]} = \dfrac{\sigma}{\sqrt n}.


$$

We're told that the coconuts in the population have weights $1.5\,\textrm{lb}$ and $2\,\textrm{lb},$ and these are distributed in the ratio $2:3.$ Therefore, to compute the population's mean and variance, we can consider a population consisting of $2+3 = 5$ coconuts with only the following weights:

$$


1.5\,\textrm{lb}, \qquad 1.5\,\textrm{lb}, \qquad 2\,\textrm{lb}, \qquad 2\,\textrm{lb}, \qquad 2\,\textrm{lb}.


$$

Therefore, the population mean is

$$


\begin{aligned}𝜇 & =\frac{1}{5}\underset{𝑖}{∑}𝑥_{𝑖} \\ & =\frac{1}{5}(2⋅1.5+3⋅2) \\ & =\frac{1}{5}(3+6) \\ & =\frac{9}{5} \\ & =1.8\,lb,\end{aligned}


$$

and the population variance is

$$


\begin{aligned}𝜎^{2} & =\frac{1}{5}\underset{𝑖}{∑}𝑥_{2𝑖}^{}−𝜇^{2} \\ & =\frac{1}{5}(2⋅1.5^{2}+3⋅2^{2})−1.8^{2} \\ & =\frac{1}{5}(16.5)−3.24 \\ & =3.3−3.24 \\ & =0.06\,lb^{2}.\end{aligned}


$$

Thus, the population standard deviation is $\sigma= \sqrt{0.06},$ and we have that

$$


\textrm{SE}[\overline{X}] = \sqrt{\dfrac{0.06}{ n}}.


$$

We require that the standard error is less than $0.02\,\textrm{lb}.$ Therefore

$$


\begin{aligned}\sqrt{√\frac{0.06}{𝑛}} & <0.02 \\ \frac{\sqrt{√0.06}}{\sqrt{√𝑛}} & <0.02 \\ \sqrt{√𝑛} & >\frac{\sqrt{√0.06}}{0.02} \\ \sqrt{√𝑛} & >\sqrt{√\frac{0.06}{0.02^{2}}} \\ \sqrt{√𝑛} & >\sqrt{√\frac{0.06}{0.0004}} \\ \sqrt{√𝑛} & >\sqrt{√150} \\ 𝑛 & >150.\end{aligned}


$$

Therefore, the smallest sample size is $n=151.$
