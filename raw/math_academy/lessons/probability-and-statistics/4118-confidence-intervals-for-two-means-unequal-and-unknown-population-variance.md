# Confidence Intervals for Two Means: Unequal and Unknown Population Variance

Source: https://www.mathacademy.com/topics/4118?courseId=73
Topic ID: 4118

## Prerequisites

- [Confidence Intervals for Two Means: Known and Unequal Population Variances](./3298-confidence-intervals-for-two-means-known-and-unequal-population-variances.md)

## Lesson

### Introduction

In this lesson, we will learn how to construct confidence intervals for the difference between the means of two normal populations with unknown and unequal variances.

Suppose we have two populations $X_1$ and $X_2,$

$$


X_1\sim N(\mu_1, \sigma^2_1), \qquad X_2\sim N(\mu_2, \sigma^2_2),


$$

where $\mu_1$ and $\mu_2$ are the population means, and $\sigma_1^2$ and $\sigma_2^2$ are the population variances.

In a previous lesson, we saw that the difference between the sample means follows a standard normal distribution:

$$


Z = \dfrac{\overline{X_1} - \overline{X_2}- (\mu_1 - \mu_2)}{\sqrt{\dfrac{\sigma_1^2}{n_1} + \dfrac{\sigma_2^2}{n_2}}} \sim N(0,1)


$$

where $\overline{X}_1$ and $\overline{X}_2$ are the sample means, and $n_1$ and $n_2$ are the sample sizes.

In most practical situations, the population variances $\sigma_1^2$ and $\sigma_2^2$ are unknown and must be replaced with estimates $S_1^2$ and $S_2^2$. In this situation, the random variable

$$


\begin{aligned}𝑇 & =\frac{(\overset{𝑋}{}_{1}−\overset{𝑋}{}_{2})−(𝜇_{1}−𝜇_{2})}{\sqrt{√\frac{𝑆_{21}^{}}{𝑛_{1}}+\frac{𝑆_{22}^{}}{𝑛_{2}}}}\end{aligned}


$$

follows a $t$-distribution with $r$ degrees of freedom, where $r$ can be approximated from sample data using the formula

$$


r = \dfrac{\left( \dfrac{s_1^2}{n_1} + \dfrac{s_2^2}{n_2} \right)^2 }{\dfrac{s_1^4}{n_1^2(n_1-1)} + \dfrac{s_2^4}{n_2^2(n_2-1)}}


$$

rounded *down* to the nearest integer.

Following the usual procedure, a $[100(1-\alpha)]\%$ confidence interval for the difference $\mu_1 - \mu_2$ is given by

$$


(\overline{x}_1-\overline{x}_2) \pm E


$$

where

- $E=t_{r, \alpha/2} \cdot \sqrt{\dfrac{s_1^2}{n_1} + \dfrac{s_2^2}{n_2}}$ is the margin of error, and

- $P(T > t_{r, \alpha/2}) = \dfrac{\alpha}{2}.$

This confidence interval is sometimes called a **Welch's $\boldsymbol t$-interval,** named after its inventor, the British statistician Bernard Lewis Welch.

Finally, note that if the underlying populations $X_1$ and $X_2$ are *not* normally distributed, we can still use this procedure to construct a confidence interval *provided that* the sample sizes $n_1$ and $n_2$ are sufficiently large (typically, $n_1, n_2 \geq 30$).

Let's see some examples.

### Example: Finding Confidence Intervals for Two Means

#### Question

Consider two independent random samples from normal populations. The summary statistics of these samples are given in the table below, where $n$ is the size of each sample, $\overline{x}$ is the sample mean, and $s^2$ is the sample variance.

Find a $95\%$ confidence interval for the difference $\mu_1-\mu_2$ between the corresponding population means.

**

**

$$


\dfrac{\left( \dfrac{s_1^2}{n_1} + \dfrac{s_2^2}{n_2} \right)^2 }{\left(\dfrac{s_1^4}{n_1^2(n_1-1)} + \dfrac{s_2^4}{n_2^2(n_2-1)}\right)}.


$$

#### Explanation

Notice that

- the samples are independent,

- both populations are normally distributed.

As a result, given a value $\alpha$ between $0$ and $1,$ the corresponding $[100(1-\alpha)]\%$ confidence interval for the difference $\mu_1-\mu_2$ between the corresponding population means can be written as

$$


(\overline{x}_1-\overline{x}_2) \pm E


$$

where

- $E=t_{r, \alpha/2} \cdot \sqrt{\dfrac{s_1^2}{n_1} + \dfrac{s_2^2}{n_2}}$ is the margin of error,

- $\overline{x}_1$ and $\overline{x}_2$ are the sample means, $\mu_1$ and $\mu_2$ are the population means, $s_1^2$ and $s_2^2$ are the sample variances, $n_1$ and $n_2$ are the sample sizes,

- $P(T > t_{r, \alpha/2}) = \dfrac{\alpha}{2}$ and $T$ has a student's $t$-distribution with $r$ degrees of freedom.

Now, to construct the confidence interval, we proceed as follows:

- **** Find the point estimate:

- **** Approximate the degrees of freedom. Therefore, we have $r=36.$

- **** Find the margin of error. Since we are interested in finding a $95\%$ confidence interval, we have From the table we can see that $P(T > 2.028) = 0.025.$ As a result, Now, we can compute the margin of error:

- **** Construct the $95\%$ confidence interval for the difference between the population means:

### Interpreting Confidence Intervals

A confidence interval for the difference $\mu_x-\mu_y$ between the population means can be interpreted in the following ways:

- If all values within the confidence interval are *positive*, this suggests that $\mu_x - \mu_y > 0.$ In other words

- If all values within the confidence interval are *negative*, this suggests that $\mu_x - \mu_y < 0.$ In other words

- If the confidence interval contains zero, then there is *insufficient evidence* of a statistically significant difference between the two means. Therefore, we conclude

We can also use confidence intervals to determine whether the difference between two means is greater than or smaller than some number:

- If all values within the confidence interval are greater than some number $k,$ this suggests that

- If all values within the confidence interval are smaller than some value $k,$ this suggests that

Statistical hypothesis tests should be conducted to verify such claims in all these cases.

### Example: Finding Confidence Intervals for Two Means: Applications

#### Question

The length of matchsticks, in millimeters, produced by machines X and Y are known to be normally distributed with means $\mu_1$ and $\mu_2.$ Engineers sampled matchsticks from both machines. The summary statistics of these samples are given in the table below, where $n$ is the number of matchsticks in each sample, in millimeters, $\overline{x}$ is the sample mean length, and $s^2$ is the sample variance.

Assuming that the samples are independent, which statements are true?

1. The end-points of the $99\%$ confidence interval for the difference between the mean lengths are approximately $1 \pm 0.375.$

2. All values contained within the $99\%$ confidence interval are positive.

3. The confidence interval data suggests that the mean lengths of matchsticks produced by the machines are not equal.

**

$$


\dfrac{\left( \dfrac{s_1^2}{n_1} + \dfrac{s_2^2}{n_2} \right)^2 }{\left(\dfrac{s_1^4}{n_1^2(n_1-1)} + \dfrac{s_2^4}{n_2^2(n_2-1)}\right)}


$$

**

#### Explanation

Notice that

- the samples are independent,

- both populations are normally distributed.

As a result, given a value $\alpha$ between $0$ and $1,$ the corresponding $[100(1-\alpha)]\%$ confidence interval for the difference $\mu_1-\mu_2$ between the corresponding population means can be written as

$$


(\overline{x}_1-\overline{x}_2) \pm E


$$

where

- $E=t_{r, \alpha/2} \cdot \sqrt{\dfrac{s_1^2}{n_1} + \dfrac{s_2^2}{n_2}}$ is the margin of error,

- $\overline{x}_1$ and $\overline{x}_2$ are the sample means, $\mu_1$ and $\mu_2$ are the population means, $s_1^2$ and $s_2^2$ are the sample variances, $n_1$ and $n_2$ are the sample sizes,

- $P(T > t_{r, \alpha/2}) = \dfrac{\alpha}{2}$ and $T$ has a student's $t$-distribution with $r$ degrees of freedom.

Now, to construct the confidence interval, we proceed as follows:

- **** Find the point estimate:

- **** Approximate the degrees of freedom. Therefore, we have $r=260.$

- **** Find the margin of error. Since we are interested in finding a $99\%$ confidence interval, we have We are given that $P(T > 2.595) = 0.005.$ As a result, Now, we can compute the margin of error:

- **** Construct the $99\%$ confidence interval for the difference between the population means:

Let's now examine our statements.

- Statement I is true. The endpoints of the confidence interval are approximately $1 \pm 0.375.$

- Statement II is true. The confidence interval contains only positive values.

- Statement III is true. Since the confidence interval does not contain zero, there is sufficient evidence to suggest that means are not equal.

Therefore, the correct answer is "I, II and III."
