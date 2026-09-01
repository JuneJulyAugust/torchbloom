# Pooled Variance

Source: https://www.mathacademy.com/topics/4117?courseId=73
Topic ID: 4117

## Prerequisites

- [The Sample Variance](./3820-the-sample-variance.md)

## Lesson

### Introduction

Suppose we have two independent random samples with the same *unknown* variance $\sigma^2.$ Let $S_1^2$ and $S_2^2$ be the sample variances of each sample, and let $n_1$ and $n_2$ be the respective sample sizes.

The **pooled variance** $S_p^2$ is an estimator for $\sigma^2$ that combines data from both samples. It is defined as follows:

$$


S_p^2 = \dfrac{(n_1-1)S_1^2 + (n_2-1)S_2^2}{n_1+n_2-2}


$$

To construct this estimator, let's write down the sample variance of each sample:

$$


S_1^2 = \dfrac{1}{n_1-1}\sum_{i=1}^{n_1} (X_i - \overline{X})^2, \qquad S_2^2 = \dfrac{1}{n_2-1}\sum_{j=1}^{n_2} (Y_j - \overline{Y})^2


$$

Multiplying the above by $(n_1-1)$ and $(n_2-1)$ respectively, we get

$$


(n_1-1)S_1^2 = \sum_{i=1}^{n_1} (X_i - \overline{X})^2, \qquad (n_2-1)S_2^2 = \sum_{j=1}^{n_2} (Y_j - \overline{Y})^2.


$$

Thus, the total sum of squared deviations from *both* samples is given by

$$


\sum_{i=1}^{n_1} (X_i - \overline{X})^2 + \sum_{j=1}^{n_2} (Y_j - \overline{Y})^2 = (n_1-1)S_1^2 + (n_2-1)S_2^2.


$$

To find the pooled estimate of the variance, we divide the sum of the squared deviations by

$$


(n_1-1) + (n_2-1) = n_1 + n_2 - 2,


$$

which yields our formula for $S_p^2.$

### Some Notes

The pooled variance $S_p^2$ is given by

$$


S_p^2 = \dfrac{(n_1-1)S_1^2 + (n_2-1)S_2^2}{n_1+n_2-2}


$$

Note the following:

- $S_p^2$ is an *unbiased* estimator of $\sigma^2.$ We'll prove this later in the lesson.

- The pooled variance extends naturally to three independent random samples with population variance $\sigma^2.$

- Note that when the samples are equal, i.e., $n_1=n_2=n,$ the formula reduces to the average of the sample variances: Similarly, for three random samples with equal sample sizes, we have

- Similar to Bessel's correction for the sample variance, the denominator $(n_1+n_2 - 2)$ guarantees that $S_p^2$ is unbiased.

- More technically, the denominator represents our combined sample's **degrees of freedom**. The number of degrees of freedom is the number of *independent* elements in the sample. The degrees of freedom concept is tricky, so let's break it down in this case: The number of elements in the first sample is $n_1.$ However, for a fixed $\overline{X},$ only $(n_1 - 1)$ of these elements may vary freely. In other words, if the first $(n_1-1)$ elements are free to vary yet $\overline{X}$ is fixed, this fixes the last sample element (it is *not* free to vary because the sum of all elements divided by $n_1$ must equal $\overline X$). Thus, the number of independent sample elements in the first sample is $(n_1-1).$ By the same argument, the number of independent sample elements in the second sample is $(n_2-1).$ Thus, the total number of independent sample elements is You'll learn more about degrees of freedom in future lessons.

### Example: Finding a Pooled Estimate of Variance for Samples of Equal Size

#### Question

A research firm conducted a survey comparing two random samples of $10$ customers from two different gas stations in Miami. The time, in minutes per week, that customers of stations $A$ and $B$ spend at the stations is denoted by $x_i$ and $y_i,$ respectively. The results are summarized below.

$$


\!\!\!\!\!\! \sum_{i=1}^{10} x_i = 72, \qquad \sum_{i=1}^{10} x_i^2 = 548, \qquad \sum_{i=1}^{10} y_i = 100, \qquad \sum_{i=1}^{10} y_i^2 = 1020


$$

Given that the samples from each station are independent and the population variance $\sigma^2$ in each station may be assumed to be the same, find a pooled estimate for $\sigma^2,$ rounded to one decimal place.

#### Explanation

Given two independent random samples from populations with the same variance $\sigma^2,$ the pooled sample variance $S_p^2$ is an unbiased estimator of $\sigma^2$ and is calculated as follows:

$$


S_p^2 = \dfrac{(n_1-1)S_1^2 + (n_2-1)S_2^2}{n_1+n_2-2},


$$

where

- $n_1$ and $n_2$ are the sample sizes,

- $S_1^2$ and $S_2^2$ are the sample variances.

If $n_1=n_2,$ the above formula reduces to

$$


S_p^2 = \dfrac{S_1^2 + S_2^2}{2}.


$$

We must first compute the estimates $s_1^2$ and $s_2^2{:}$

$$


\begin{aligned}𝑠_{21} & =\frac{𝑛_{1}}{𝑛_{1}−1}(\overset{𝑥^{2}}{}−\overset{𝑥}{}^{2}) \\ & =\frac{10}{10−1}(\frac{548}{10}−(\frac{72}{10})^{2}) \\ & ≈3.2889 \\ 𝑠_{22} & =\frac{𝑛_{2}}{𝑛_{2}−1}(\overset{𝑦^{2}}{}−\overset{𝑦}{–}^{2}) \\ & =\frac{10}{10−1}(\frac{1020}{10}−(\frac{100}{10})^{2}) \\ & ≈2.2222\end{aligned}


$$

Therefore, our estimate for the pooled variance is

$$


s_p^2 = \dfrac{s_1^2+s_2^2}{2} \approx\dfrac{ 3.2889 + 2.222}{2} \approx 2.8\,\text{min}^2.


$$

### Example: Finding a Pooled Estimate of Variance for Two Samples of Different Size

#### Question

A health technician selects random samples of newborn babies from two different hospitals. In kilograms, the babies' weights from the first and second samples are denoted as $x_i$ and $y_i,$ respectively, where the sizes of each sample are $n_1 = 9$ and $n_2 = 7.$ The results are summarized below.

$$


\sum_{i=1}^{9} x_i = 29.90, \qquad \sum_{i=1}^{9} x_i^2 = 100.99, \qquad \sum_{i=1}^{7} y_i = 24.7, \qquad \sum_{i=1}^{7} y_i^2 = 89.59


$$

Given that the samples from each hospital are independent and the population variance $\sigma^2$ in each hospital may be assumed to be the same, find a pooled estimate for $\sigma^2,$ rounded to one decimal place.

#### Explanation

Given two independent random samples from populations with the same variance $\sigma^2,$ the pooled sample variance $S_p^2$ is an unbiased estimator of $\sigma^2$ and is calculated as follows:

$$


S_p^2 = \dfrac{(n_1 - 1)S_1^2 + (n_2 - 1)S_2^2}{n_1 + n_2 - 2},


$$

where

- $n_1$ and $n_2$ are the sample sizes,

- $S_1^2$ and $S_2^2$ are the sample variances.

We must first compute the estimates $s_1^2$ and $s_2^2{:}$

$$


\begin{aligned}𝑠_{21} & =\frac{𝑛_{1}}{𝑛_{1}−1}(\overset{𝑥^{2}}{}−\overset{𝑥}{}^{2}) \\ & =\frac{9}{9−1}(\frac{100.99}{9}−(\frac{29.90}{9})^{2}) \\ & ≈0.206\,9 \\ 𝑠_{22} & =\frac{𝑛_{2}}{𝑛_{2}−1}(\overset{𝑦^{2}}{}−\overset{𝑦}{–}^{2}) \\ & =\frac{7}{7−1}(\frac{89.59}{7}−(\frac{24.7}{7})^{2}) \\ & ≈0.405\,7\end{aligned}


$$

Therefore, our estimate for the pooled variance is

$$


\begin{aligned}𝑠_{2𝑝} & =\frac{(9−1)⋅0.206\,9+(7−1)⋅0.405\,7}{9+7−2} \\ & =\frac{4.089\,4}{14} \\ & ≈0.3\,kg^{2}\end{aligned}


$$

rounded to one decimal place.

### A General Formula for N Independent Samples

Given $N$ independent random samples from $N$ populations that have the same variance $\sigma^2,$ the pooled sample variance $S_p^2$ is an unbiased estimator of $\sigma^2$ and is calculated as follows:

$$


S_p^2 = \dfrac{\displaystyle\sum_{i=1}^N (n_i - 1)S_i^2}{\displaystyle\left(\sum_{i=1}^N n_i\right) - N},


$$

where

- $n_1, n_2, \ldots, n_N$ are the sample sizes,

- $S_1^2, S_2^2, \ldots, S_N^2$ are the sample variances.

Note that when $N=2,$ we get our formula of the pooled variance for two samples:

$$


\begin{aligned}𝑆_{2𝑝} & =\frac{\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑁}}(𝑛_{𝑖}−1)𝑆_{2𝑖}}{(\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑁}}𝑛_{𝑖})−𝑁} \\ & =\frac{\underset{\underset{𝑖=1}{∑}}{\overset{}{2}}(𝑛_{𝑖}−1)𝑆_{2𝑖}}{(\underset{\underset{𝑖=1}{∑}}{\overset{}{2}}𝑛_{𝑖})−2} \\ & =\frac{(𝑛_{1}−1)𝑆_{21}+(𝑛_{2}−1)𝑆_{22}}{𝑛_{1}+𝑛_{2}−2}\end{aligned}


$$

### Example: Finding a Pooled Estimate of Variance for Three Or More Samples

#### Question

Consider four random samples from four populations having the same variance. The following table gives the sample sizes $n$ and the sample variances $s^2$ for each sample. Rounded to two decimal places, what is the pooled estimate of the variance?

#### Explanation

Given $N$ independent random samples from $N$ populations that have the same variance $\sigma^2,$ the pooled sample variance $S_p^2$ is an unbiased estimator of $\sigma^2$ and is calculated as follows:

$$


S_p^2 = \dfrac{\displaystyle\sum_{i=1}^N (n_i - 1)S_i^2}{\displaystyle\left(\sum_{i=1}^N n_i\right) - N},


$$

where

- $n_1, n_2, \ldots, n_N$ are the sample sizes,

- $S_1^2, S_2^2, \ldots, S_N^2$ are the sample variances.

In our case, $N=4.$

Therefore, by substituting the given values in the formula, we get

$$


\begin{aligned}𝑠_{2𝑝} & =\frac{(10−1)(7.2)+(12−1)(8.4)+(18−1)(8.0)+(20−1)(8.1)}{10+12+18+20−4} \\ & =\frac{64.8+92.4+136+153.9}{56} \\ & =\frac{447.1}{56} \\ & ≈7.98,\end{aligned}


$$

rounded to two decimal places.

### Proof of the Unbiasedness of the Pooled Variance

Let's now prove that the pooled sample variance $S_p^2$ for two independent random samples from populations with the same variance is an unbiased estimator of the variance $\sigma^2.$

Let $n_1, n_2$ be the sample sizes and $S_1^2, S_2^2$ the sample variances.

Recall that a statistic is an unbiased estimator for a parameter if its expected value equals the parameter. So, we need to prove that the expected value of the pooled variance $S_p^2$ equals $\sigma^2.$

First, recall the formula for the pooled variance of two samples:

$$


S_p^2 = \dfrac{(n_1 - 1)S_1^2 + (n_2-1)S_2^2}{n_1+n_2-2}


$$

So, we must calculate the expected value of the above expression:

$$


\textrm E[S_p^2] = \textrm E\left[ \dfrac{(n_1 - 1)S_1^2 + (n_2-1)S_2^2}{n_1+n_2-2} \right].


$$

Recall that for any random variables $X$ and $Y,$ and for any constants $a$ and $b,$ we have

$$


\textrm E[aX+bY] = a\textrm E[X] + b\textrm E[Y].


$$

Using this property, we can factor the denominator of our expression outside the expected value and simplify the numerator as follows:

$$


\begin{aligned}E[𝑆_{2𝑝}] & =E[\frac{(𝑛_{1}−1)𝑆_{21}+(𝑛_{2}−1)𝑆_{22}}{𝑛_{1}+𝑛_{2}−2}] \\ & =\frac{E[(𝑛_{1}−1)𝑆_{21}+(𝑛_{2}−1)𝑆_{22}]}{𝑛_{1}+𝑛_{2}−2} \\ & =\frac{(𝑛_{1}−1)⋅E[𝑆_{21}]+(𝑛_{2}−1)⋅E[𝑆_{22}]}{𝑛_{1}+𝑛_{2}−2}\end{aligned}


$$

We already know that the sample variance is an unbiased estimator for $\sigma^2,$ so $\mathrm E[S_1^2]=\sigma^2$ and $\mathrm E[S_2^2] = \sigma^2.$

We substitute $\mathrm E[S_1^2]$ and $\mathrm E[S_2^2]$ with $\sigma^2$ and get

$$


\begin{aligned}E[𝑆_{2𝑝}] & =\frac{(𝑛_{1}−1)E[𝑆_{21}]+(𝑛_{2}−1)E[𝑆_{22}]}{𝑛_{1}+𝑛_{2}−2} \\ & =\frac{(𝑛_{1}−1)𝜎^{2}+(𝑛_{2}−1)𝜎^{2}}{𝑛_{1}+𝑛_{2}−2} \\ & =\frac{(𝑛_{1}+𝑛_{2}−2)𝜎^{2}}{𝑛_{1}+𝑛_{2}−2} \\ & =𝜎^{2}.\end{aligned}


$$
