# Estimating Sample Sizes for Means

Source: https://www.mathacademy.com/topics/3319?courseId=73
Topic ID: 3319

## Prerequisites

- [The Empirical Rule for the Normal Distribution](./3594-the-empirical-rule-for-the-normal-distribution.md)
- [Confidence Intervals for One Mean: Unknown Population Variance](./3855-confidence-intervals-for-one-mean-unknown-population-variance.md)

## Lesson

### Introduction

When conducting statistical research, establishing a lower bound for the sample size needed to achieve a margin of error smaller than some pre-specified amount is often helpful. This allows those conducting the sample to achieve results whose errors are constrained and at the minimum level of time and cost.

For example, suppose you're planning a survey to estimate the average cost city commuters must pay monthly to travel to work. You'd need to figure out how many people to survey to ensure reliable results. A sample size that is too small might lead to misleading conclusions, while a sample that is too large wastes resources. This lesson explores how to determine the minimum sample size needed to strike the right balance.

Let's determine a lower bound for the sample size required to find a confidence interval for a population mean $\mu$ with a fixed margin of error.

Given a random sample and a value $\alpha$ between $0$ and $1,$ we know that the corresponding $[100(1-\alpha)]\%$ confidence interval for the population mean $\mu$ can be written as

$$


\overline{x} \pm \overbrace{z_{\alpha/2} \cdot \dfrac{\sigma}{\sqrt n}}^{\large \text{margin of error}},


$$

where

- $\!\overline{\,x}$ is the sample mean,

- $n$ is the sample size,

- $\sigma$ is the population standard deviation, and

- $P(Z > z_{\alpha/2}) = \dfrac{\alpha}{2}$ and $Z \sim N(0,1).$

Suppose that we require the margin of error to be at most $\varepsilon,$ i.e.,

$$


z_{\alpha/2} \cdot \dfrac{\sigma}{\sqrt{n}} \leq \varepsilon.


$$

We can solve this inequality for $n$ by first squaring both sides. This gives

$$


\begin{aligned}𝑧_{2𝛼/2}⋅\frac{𝜎^{2}}{𝑛} & ≤𝜀^{2}.\end{aligned}


$$

By solving this inequality for $n,$ we obtain

$$


n \geq \dfrac{z_{\alpha/2}^2 \, \sigma^2}{\varepsilon^2}.


$$

This result gives us a lower bound on the sample size $n$ needed to constrain the margin of error to $\varepsilon.$

Now, we have two possible cases:

- Case 1: The population variance $\sigma^2$ is known.

- Case 2: The population variance $\sigma^2$ is unknown.

Let's look at an example of the first case.

### Example: Finding a Minimum Sample Size: Population Variance Is Known

#### Question

A group of researchers wants to calculate a $98\%$ confidence interval for the mean number of hours wolves sleep daily in their natural habitat. The population standard deviation is known to be $\sigma = 1.2 \, \text{h}.$

Find the smallest sample size $n$ required to ensure that the margin of error for the $98\%$ confidence interval for the mean number of hours wolves sleep daily is at most $0.3 \, \text{h}.$

**

#### Explanation

We do not know the distribution of the population. However, if the sample size $n$ is **, then, according to the central limit theorem, the sample mean is approximately normally distributed.

As a result, given a value $\alpha$ between $0$ and $1,$ the corresponding $[100(1-\alpha)]\%$ confidence interval for the population mean $\mu$ can be written as

$$


\overline{x} \pm \overbrace{z_{\alpha/2} \cdot \dfrac{\sigma}{\sqrt n}}^{\large \text{margin of error}},


$$

where

- $\overline{x}$ is the sample mean,

- $n$ is the sample size,

- $\sigma$ is the population standard deviation, and

- $P(Z > z_{\alpha/2}) = \dfrac{\alpha}{2}$ and $Z \sim N(0,1).$

If we require the margin of error to be at most $\varepsilon,$ then

$$


z_{\alpha/2} \cdot \dfrac{\sigma}{\sqrt n} \leq \varepsilon \qquad\Longrightarrow\qquad n \geq \dfrac{z_{\alpha/2}^2 \, \sigma^2}{\varepsilon^2}.


$$

We are interested in finding a $98\%$ confidence interval. So, we have

$$


\alpha=1-0.98=0.02 \qquad\Longrightarrow\qquad \dfrac{\alpha}{2}=0.01.


$$

From the percentage points table of the normal distribution, we obtain that $z_{0.01}=2.326{:}$

We're given the population standard deviation $\sigma=1.2.$ Therefore, substituting

$$


\varepsilon=0.3, \qquad \sigma=1.2, \qquad z_{\alpha/2}=2.326


$$

into the inequality for $n,$ we obtain

$$


\begin{aligned}𝑛 & ≥\frac{𝑧_{2𝛼/2}\,𝜎^{2}}{𝜀^{2}} \\ & =\frac{(2.326)^{2}\,(1.2)^{2}}{(0.3)^{2}} \\ & ≈86.56.\end{aligned}


$$

Finally, rounding up to the nearest integer, we get that $n=87$ or larger. Notice that $87\geq 30,$ therefore, the sample is sufficiently large to apply the normal approximation.

### Cases Where the Population Variance is Unknown

As we've seen, the sample size $n$ required for margin of error for the $[100(1-\alpha)]\%$ confidence interval to be smaller that $\varepsilon$ is given by

$$


n \geq \dfrac{z_{\alpha/2}^2 \, \sigma^2}{\varepsilon^2}.


$$

In practice, the population variance is often unknown. How can we find a lower bound for $n$ in such cases?

First, recall that the corresponding confidence interval for the population mean $\mu$ when the variance is *unknown* can be written as

$$


\overline{x} \pm \overbrace{t_{n-1, \,\alpha/2} \cdot \dfrac{s}{\sqrt n}}^{\large \text{margin of error}},


$$

where

- $\!\overline{\,x}$ is the sample mean,

- $n$ is the sample size,

- $s$ is the sample standard deviation, and

- $P(T > t_{n-1, \,\alpha/2}) = \dfrac{\alpha}{2},$ and $T$ has a student's $t$-distribution with $n-1$ degrees of freedom.

If we require the margin of error to be at most $\varepsilon,$ then

$$


t_{n-1, \,\alpha/2} \cdot \dfrac{s}{\sqrt n} \leq \varepsilon \qquad\Longrightarrow\qquad n \geq \dfrac{t_{n-1, \,\alpha/2}^2 \, s^2}{\varepsilon^2}.


$$

Note the following:

- This lower bound can't be directly calculated because we need $n$ to determine $t_{n-1, \,\alpha/2},$ and a lower bound for $n$ is what we're trying to find!

- However, as $n$ increases, the $t$-distribution approaches the standard normal distribution.

- Therefore, we can replace $t_{n-1, \,\alpha/2}$ by $z_{\alpha/2},$ where $P(Z > z_{\alpha/2}) = \dfrac{\alpha}{2}$ and $Z$ follows a standard normal distribution.

Therefore, our lower bound for $n$ is as follows:

$$


n \geq \dfrac{z_{\alpha/2}^2 \, s^2}{\varepsilon^2}


$$

In short, we simply replace $\sigma^2$ in our original bound with its unbiased estimate!

Let's now look at how to apply this in practice.

### Example: Finding a Minimum Sample Size Using a Point Estimate for the Variance

#### Question

Consider a normal population with unknown mean and standard deviation. A small sample is taken, and the sample standard deviation is found to be $s=0.5.$ Suppose we require a $98\%$ confidence interval for the population mean to have a margin of error of at most $0.05.$ Find the smallest sample size $n$ required to construct this interval.

**

#### Explanation

We are told that the population is normally distributed, but we do not know the population standard deviation $\sigma.$

Given a value $\alpha$ between $0$ and $1,$ the corresponding $[100(1-\alpha)]\%$ confidence interval for the population mean $\mu$ can be written as

$$


\overline{x} \pm \overbrace{t_{n-1, \,\alpha/2} \cdot \dfrac{s}{\sqrt n}}^{\large \text{margin of error}},


$$

where

- $\overline{x}$ is the sample mean,

- $n$ is the sample size,

- $s$ is the sample standard deviation, and

- $P(T > t_{n-1, \,\alpha/2}) = \dfrac{\alpha}{2}$ and $T$ has a student's $t$-distribution with $n-1$ degrees of freedom.

If we require the margin of error to be at most $\varepsilon,$ then

$$


t_{n-1, \,\alpha/2} \cdot \dfrac{s}{\sqrt n} \leq \varepsilon \qquad\Longrightarrow\qquad n \geq \dfrac{t_{n-1, \,\alpha/2}^2 \, s^2}{\varepsilon^2}.


$$

Note that the above lower bound can't be directly calculated because we need $n$ to determine $t_{n-1, \,\alpha/2},$ and $n$ is the value we are trying to find. However, as $n$ increases, the $t$-distribution approaches the standard normal distribution. Therefore, we can replace $t_{n-1, \,\alpha/2}$ by $z_{\alpha/2},$ where $P(Z > z_{\alpha/2}) = \dfrac{\alpha}{2}$ and $Z$ follows a standard normal distribution.

Now, we are interested in finding a $98\%$ confidence interval. So, we have

$$


\alpha=1-0.98=0.02 \qquad\Longrightarrow\qquad \dfrac{\alpha}{2}=0.01.


$$

We are given that $P(Z > 2.326) = 0.01.$ As a result,

$$


z_{\alpha/2} = z_{0.01} = 2.326.


$$

We're given the sample standard deviation $s=0.5.$ Therefore, substituting

$$


\varepsilon=0.05, \qquad s=0.5, \qquad z_{\alpha/2}=2.326


$$

into the inequality for $n,$ we obtain

$$


\begin{aligned}𝑛 & ≥\frac{𝑧_{2𝛼/2}\,𝑠^{2}}{𝜀^{2}} \\ & =\frac{(2.326)^{2}\,(0.5)^{2}}{(0.05)^{2}} \\ & ≈541.03.\end{aligned}


$$

Finally, rounding up to the nearest integer, we get $n=542$ or larger.

### The Empirical Rule for the Normal Distribution

Let's remind ourselves of the empirical rule for the normal distribution:

- Approximately $68\%$ of the data falls within $1$ standard deviation of the mean.

- Approximately $95\%$ of the data falls within $2$ standard deviations of the mean.

- Approximately $99.7\%$ of the data falls within $3$ standard deviations of the mean.

Let's see how we can find minimum sample sizes using the empirical rule.

### Example: Finding a Minimum Sample Size Using the Empirical Rule

#### Question

Consider a normal population with unknown mean and variance, for which it is known that $99.7\%$ of the observations lie between $-5.3$ and $12.7,$ and this data is distributed symmetrically about the mean. Using the empirical rule to estimate the population standard deviation, find the smallest sample size $n$ required to ensure that the margin of error for the $95\%$ confidence interval for the population mean is at most $0.5.$

**

#### Explanation

Given a value $\alpha$ between $0$ and $1,$ the corresponding $[100(1-\alpha)]\%$ confidence interval for the population mean $\mu$ can be written as

$$


\overline{x} \pm \overbrace{z_{\alpha/2} \cdot \dfrac{\sigma}{\sqrt n}}^{\large \text{margin of error}},


$$

where

- $\!\overline{\,x}$ is the sample mean,

- $n$ is the sample size,

- $\sigma$ is the population standard deviation, and

- $P(Z > z_{\alpha/2}) = \dfrac{\alpha}{2}$ and $Z \sim N(0,1).$

If we require the margin of error to be at most $\varepsilon,$ then

$$


z_{\alpha/2} \cdot \dfrac{\sigma}{\sqrt n} \leq \varepsilon \qquad\Longrightarrow\qquad n \geq \dfrac{z_{\alpha/2}^2 \, \sigma^2}{\varepsilon^2}.


$$

To find an estimate for $\sigma^2,$ we can apply the empirical rule. According to this rule, $99.7\%$ of the observations of a random normal variable $N(\mu, \sigma^2)$ fall in the interval $(\mu-3\sigma, \mu+3\sigma).$ Therefore, we can estimate $\sigma$ by dividing the given range by $2\cdot 3 = 6{:}$

$$


\widehat{\sigma} =\dfrac{12.7-(-5.3)}{6} = 3


$$

We are interested in finding a $95\%$ confidence interval. So, we have

$$


\alpha=1-0.95=0.05 \qquad\Longrightarrow\qquad \dfrac{\alpha}{2}=0.025.


$$

We are given that $P(Z > 1.96) = 0.025.$ As a result,

$$


z_{\alpha/2} = z_{0.025} = 1.96.


$$

Therefore, substituting

$$


\varepsilon=0.5, \qquad \widehat{\sigma}=3, \qquad z_{\alpha/2}=1.96


$$

into the inequality for $n,$ we obtain

$$


\begin{aligned}𝑛 & ≥\frac{𝑧_{2𝛼/2}\,\overset{𝜎}{ˆ}^{2}}{𝜀^{2}} \\ & =\frac{(1.96)^{2}\,(3)^{2}}{(0.5)^{2}} \\ & ≈138.30\end{aligned}


$$

Finally, rounding up to the nearest integer, we get that $n=139$ or larger.

### Factors Affecting Sample Size

Suppose we conduct a random sample to find the average weekly cost commuters spend traveling to work in a certain city. Let's assume we initially used a sample of size $n_1$ to construct a $95\%$ confidence interval for the population mean $\mu.$

After completing the initial survey, the city planners decided that a new sample must be carried out, and the resulting confidence interval should have the following improvements:

- The confidence level of the new confidence interval should be $99\%.$

- The new confidence interval should be one-third as wide as the original (increased precision).

For a fixed sample size, increasing the confidence level leads to an *increase* in the width of the confidence interval. In other words, precision is reduced when we increase the confidence level. To increase precision, we need to *increase* the sample size.

Let's determine how much larger the second sample size $n_2$ should be compared to the first to satisfy these new conditions.

First, recall that, given a value $\alpha$ between $0$ and $1,$ the corresponding $[100(1-\alpha)]\%$ confidence interval for the population mean $\mu$ can be written as

$$


\overline{x} \pm \overbrace{z_{\alpha/2} \cdot \dfrac{\sigma}{\sqrt n}}^{\large \text{margin of error}},


$$

where

- $\!\overline{\,x}$ is the sample mean,

- $n$ is the sample size,

- $\sigma$ is the population standard deviation, and

- $P(Z > z_{\alpha/2}) = \dfrac{\alpha}{2}$ and $Z \sim N(0,1).$

We define the following:

- Let $I_1$ and $I_2$ be the $95\%$ and $99\%$ confidence intervals for the population mean obtained from samples of size $n_1$ and $n_2,$ respectively.

- Let $\varepsilon_1$ and $\varepsilon_2$ be the margins of error of $I_1$ and $I_2,$ respectively.

Since we want $I_2$ to be one-third of the length of $I_1,$ we must have

$$


\varepsilon_1 = 3\varepsilon_2.


$$

Then, we have

$$


z_{0.025} \cdot \dfrac{\sigma}{\sqrt{n_1}} = 3 \cdot z_{0.005} \cdot \dfrac{\sigma}{\sqrt{n_2}}


$$

Canceling $\sigma$ and solving for $\dfrac{n_2}{n_1},$ we get

$$


\begin{aligned}𝑧_{0.025}⋅\frac{1}{\sqrt{𝑛_{1}}} & =3⋅𝑧_{0.005}⋅\frac{1}{\sqrt{𝑛_{2}}} \\ \frac{\sqrt{𝑛_{2}}}{\sqrt{𝑛_{1}}} & =\frac{3⋅𝑧_{0.005}}{𝑧_{0.025}} \\ (\frac{\sqrt{𝑛_{2}}}{\sqrt{𝑛_{1}}})^{2} & =(\frac{3⋅𝑧_{0.005}}{𝑧_{0.025}})^{2} \\ \frac{𝑛_{2}}{𝑛_{1}} & =\frac{9⋅𝑧_{20.005}}{𝑧_{20.025}}\end{aligned}


$$

Now, using the fact that $z_{0.005} = 2.576$ and $z_{0.025} = 1.960$, we have

$$


\begin{aligned}\frac{𝑛_{2}}{𝑛_{1}} & =\frac{9⋅𝑧_{20.005}}{𝑧_{20.025}} \\ & =\frac{9⋅2.576^{2}}{1.960^{2}} \\ & ≈15.54.\end{aligned}


$$

This gives

$$


n_2 \approx 15.5 n_1.


$$

Therefore, $n_2$ must be larger than $n_1$ by a factor of approximately $15.5.$ Note that the additional time and resources needed to conduct a sample that's more than fifteen times the size of the first could be significant!

Let's take a look at a similar problem in the case where the population variance is unknown.

### Example: Understanding the Minimum Sample Size Formula

#### Question

Consider a normal population with unknown mean and standard deviation. Let $I_1$ be a $95\%$ confidence interval for the population mean $\mu$ obtained from a sample of size $n_1$ using as an estimate for the standard deviation $s_1=5,$ calculated from a previous study.

Suppose we require a second $98\%$ confidence interval $I_2$ to have the same length as $I_1,$ obtained using a different estimate $s_2=3.$ Find the relative size of the second sample $n_2$ we should use to construct $I_2.$

**

#### Explanation

Given a value $\alpha$ between $0$ and $1,$ the corresponding $[100(1-\alpha)]\%$ confidence interval for the population mean $\mu$ can be written as

$$


\overline{x} \pm \overbrace{z_{\alpha/2} \cdot \dfrac{\sigma}{\sqrt n}}^{\large \text{margin of error}},


$$

where

- $\!\overline{\,x}$ is the sample mean,

- $n$ is the sample size,

- $\sigma$ is the population standard deviation, and

- $P(Z > z_{\alpha/2}) = \dfrac{\alpha}{2}$ and $Z \sim N(0,1).$

Let $\varepsilon_1$ and $\varepsilon_2$ be the margins of error of $I_1$ and $I_2,$ respectively. Since we want $I_2$ to be equal to $I_1,$ we must have

$$


\varepsilon_1 = \varepsilon_2.


$$

Then, we have

$$


z_{0.025} \cdot \dfrac{s_1}{\sqrt{n_1}} = z_{0.01} \cdot \dfrac{s_2}{\sqrt{n_2}}


$$

Solving for $\dfrac{n_2}{n_1},$ we get

$$


\begin{aligned}\frac{\sqrt{𝑛_{2}}}{\sqrt{𝑛_{1}}} & =\frac{𝑧_{0.01}⋅𝑠_{2}}{𝑧_{0.025}⋅𝑠_{1}} \\ (\frac{\sqrt{𝑛_{2}}}{\sqrt{𝑛_{1}}})^{2} & =(\frac{𝑧_{0.01}⋅𝑠_{2}}{𝑧_{0.025}⋅𝑠_{1}})^{2} \\ \frac{𝑛_{2}}{𝑛_{1}} & =\frac{𝑧_{20.01}⋅𝑠_{22}}{𝑧_{20.025}⋅𝑠_{21}}\end{aligned}


$$

Now, using the fact that $s_1 = 5, s_2 = 3, z_{0.01} = 2.326, z_{0.25} = 1.960,$ we have

$$


\begin{aligned}\frac{𝑛_{2}}{𝑛_{1}} & =\frac{2.326^{2}⋅3^{2}}{1.960^{2}⋅5^{2}}≈0.507\end{aligned}


$$

which gives

$$


n_1\approx 1.97 n_2.


$$

Therefore, $n_2$ must be $\boxed{\color{blue}\text{smaller}}$ than $n_1$ by a factor of approximately $\boxed{\color{blue}1.97}.$
