# The Sample Variance

Source: https://www.mathacademy.com/topics/3820?courseId=145
Topic ID: 3820

## Prerequisites

- [Variance of Sample Means](./3013-variance-of-sample-means.md)

## Lesson

### Introduction

Suppose we have a random sample $X_1, X_2, \ldots X_n$ of size $n$ drawn from a population with population mean $\mu$ and population variance $\sigma^2.$

We've already seen that the sample mean $\overline{X},$ given by

$$


\overline{X} = \dfrac1n\sum_{i=1}^n X_i


$$

is an *unbiased* estimator of $\mu,$ which means that

$$


\text{E}[\overline{X}] = \mu.


$$

The definition of the sample mean follows naturally from the definition of $\mu.$

However, when constructing estimators for the population variance $\sigma^2,$ things are not so simple!

From the definition of the population variance, you might expect that

$$


\dfrac{1}{n} \sum_{i=1}^n \left( X_i - \overline{X} \right)^2


$$

is an *unbiased* estimator for $\sigma^2.$ However, it can be shown that it is a *biased* estimator of $\sigma^2,$ meaning that

$$


\text{E}\left[\dfrac{1}{n} \sum_{i=1}^n \left( X_i - \overline{X} \right)^2\right] \neq \sigma^2.


$$

This might seem surprising, but it's true.

To compute an *unbiased* estimate of $\sigma^2,$ we use the so-called **sample variance**. The sample variance is denoted $S^2,$ and is defined as

$$


S^2 = \dfrac{1}{n-1} \sum_{i=1}^n \left( X_i - \overline{X} \right)^2.


$$

At the end of this lesson, we will prove that $S^2$ is an unbiased estimator of $\sigma^2$.

Note the following:

- Notice that instead of dividing by $n$ (as with our original biased estimator), we instead divide by $n-1.$ This is sometimes referred to as **Bessel's correction**, as it corrects the bias of the original estimator.

- We should think of $S^2$ as a random variable whose value varies according to the particular sample under consideration.

- Since $S^2$ is a random variable, it has a sampling distribution (i.e., a probability distribution). We'll learn more about the sampling distribution of $S^2$ in future lessons.

Finally, we have an alternative formula for the sample variance that's often more convenient in practice:

$$


S^2 =\dfrac{n}{n-1}\left[ \overline{X^2} - \left( \overline{X} \right)^2 \right]


$$

We'll derive this formula at the end of the lesson.

### Example: Computing an Estimate of the Population Variance

#### Question

A random sample of size $n=81$ is conducted from a population. It is known that

$$


\sum_{i=1}^{81} \left( x_i - \overline{x} \right)^2 = 180


$$

where each $x_i$ is a sample observation. Compute an unbiased estimate of the population standard deviation.

#### Explanation

Suppose $X_1, X_2, \ldots X_n$ is a sequence of random variables representing a random sample of size $n$ drawn from a population with population mean $\mu$ and population variance $\sigma^2.$ Then the sample variance $S^2$ is given by

$$


S^2 = \dfrac{1}{n-1} \sum_{i=1}^n \left( X_i - \overline{X} \right)^2 = \dfrac{n}{n-1} \left[ \overline{X^2} - \left( \overline{X} \right)^2 \right] .


$$

Note that

- $\overline{X}$ is the sample mean,

- the sample variance $S^2$ is an unbiased estimator of the population variance $\sigma^2,$ and

- $\hat{\sigma}^2 = s^2$ denotes an unbiased estimate of $\sigma^2$ that's computed from the sample $x_1, x_2, \ldots, x_n.$

We're given that $\displaystyle\sum_{i=1}^{81} \left(x_i - \overline{x} \right)^2 = 180$ and $n=81.$ Therefore,

$$


\begin{aligned}\hat{𝜎}^{2} & =𝑠^{2} \\ & =\frac{1}{𝑛−1}\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}(𝑥_{𝑖}−\overset{𝑥}{})^{2} \\ & =\frac{1}{81−1}⋅180 \\ & =\frac{1}{80}⋅180 \\ & =2.25.\end{aligned}


$$

Therefore, an unbiased estimate of the population variance is $\hat{\sigma}^2 = 2.25.$ We take the square root to compute an unbiased estimate of the standard deviation. This gives

$$


\hat{\sigma} = \sqrt{2.25} = 1.5.


$$

### Example: Computing an Estimate of the Population Variance Using the Alternative Formula

#### Question

Suppose that $x_1, x_2, \ldots, x_9$ is a random sample of size $n=9$ from a population, and

$$


\overline{x^2} - \left( \overline{x} \right)^2 = 4.


$$

Compute an unbiased estimate of the population variance.

#### Explanation

Suppose $X_1, X_2, \ldots X_n$ is a sequence of random variables representing a random sample of size $n$ drawn from a population with population mean $\mu$ and population variance $\sigma^2.$ Then the sample variance $S^2$ is given by

$$


S^2 = \dfrac{1}{n-1} \sum_{i=1}^n \left( X_i - \overline{X} \right)^2 = \dfrac{n}{n-1} \left[ \overline{X^2} - \left( \overline{X} \right)^2 \right] .


$$

Note that

- $\overline{X}$ is the sample mean,

- the sample variance $S^2$ is an unbiased estimator of the population variance $\sigma^2,$ and

- $\hat{\sigma}^2 = s^2$ denotes an unbiased estimate of $\sigma^2$ that's computed from the sample $x_1, x_2, \ldots, x_n.$

Here, there are $n=9$ data points in the sample, and we have

$$


\overline{x^2} - \left( \overline{x} \right)^2 = 4.


$$

Therefore, an unbiased estimate of the population variance is

$$


\begin{aligned}\hat{𝜎}^{2} & =𝑠^{2} \\ & =\frac{𝑛}{𝑛−1}[\overset{𝑥^{2}}{}−(\overset{𝑥}{})^{2}] \\ & =\frac{9}{9−1}⋅4 \\ & =\frac{36}{8} \\ & =4.5.\end{aligned}


$$

### Example: Estimating the Population Variance From Sample Data

#### Question

Suppose the following data is sampled from a population. Compute an unbiased estimate of the population variance.

$$


5, \quad 3, \quad 6, \quad 4, \quad 7


$$

#### Explanation

Suppose $X_1, X_2, \ldots X_n$ is a sequence of random variables representing a random sample of size $n$ drawn from a population with population mean $\mu$ and population variance $\sigma^2.$ Then the sample variance $S^2$ is given by

$$


S^2 = \dfrac{1}{n-1} \sum_{i=1}^n \left( X_i - \overline{X} \right)^2 = \dfrac{n}{n-1} \left[ \overline{X^2} - \left( \overline{X} \right)^2 \right] .


$$

Note that

- $\overline{X}$ is the sample mean,

- the sample variance $S^2$ is an unbiased estimator of the population variance $\sigma^2,$ and

- $\hat{\sigma}^2 = s^2$ denotes the unbiased estimate of $\sigma^2$ computed from the sample $x_1, x_2, \ldots, x_n.$

First, we will compute the quantity

$$


\overline{x^2} - \left( \overline{x} \right)^2.


$$

We proceed as follows:

- The mean of the data is given by

- The mean of the squared data is given by

Therefore,

$$


\begin{aligned}\overset{𝑥^{2}}{}−(\overset{𝑥}{})^{2} & =27−5^{2} \\ & =2.\end{aligned}


$$

Finally, the sample variance is

$$


\begin{aligned}\hat{𝜎}^{2} & =𝑠^{2} \\ & =\frac{𝑛}{𝑛−1}[\overset{𝑥^{2}}{}−(\overset{𝑥}{})^{2}] \\ & =\frac{5}{5−1}⋅2 \\ & =2.5.\end{aligned}


$$

Therefore, an unbiased estimate of the population variance is $2.5.$

### Proof of the Alternative Formula

Here, we will show that

$$


S^2 =\dfrac{n}{n-1}\left[ \overline{X^2} - \left( \overline{X} \right)^2 \right].


$$

We start with the definition of $S^2\mathbin{:}$

$$


S^2 = \dfrac{1}{n-1} \sum_{i=1}^n \left( X_i - \overline{X} \right)^2


$$

Expanding the parentheses and distributing the summation, we have

$$


\begin{aligned}𝑆^{2} & =\frac{1}{𝑛−1}\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}(𝑋_{2𝑖}−2𝑋_{𝑖}\overset{𝑋}{}+(\overset{𝑋}{})^{2}) \\ & =\frac{1}{𝑛−1}[\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}𝑋_{2𝑖}−\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}2𝑋_{𝑖}\overset{𝑋}{}+\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}(\overset{𝑋}{})^{2}] \\ & =\frac{1}{𝑛−1}[\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}𝑋_{2𝑖}−2\overset{𝑋}{}\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}𝑋_{𝑖}+(\overset{𝑋}{})^{2}⋅\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}1].\end{aligned}


$$

We now consider each sum separately:

- $\displaystyle\sum_{i=1}^n X_i^2 = n\cdot \overline{X^2}$ follows directly from the definition of the mean of $X^2$

- $\displaystyle\sum_{i=1}^n X_i = n\cdot \overline{X}$ follows directly from the definition of the mean of $X$

- $\displaystyle\sum_{i=1}^n 1 = \underbrace{1+1+\cdots+1}_{n\, \text{times}} = n$

Therefore,

$$


\begin{aligned}𝑆^{2} & =\frac{1}{𝑛−1}[\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}𝑋_{2𝑖}−2\overset{𝑋}{}\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}𝑋_{𝑖}+(\overset{𝑋}{})^{2}⋅\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}1] \\ & =\frac{1}{𝑛−1}[𝑛⋅\overset{𝑋^{2}}{}−2\overset{𝑋}{}⋅𝑛⋅\overset{𝑋}{}+(\overset{𝑋}{})^{2}⋅𝑛] \\ & =\frac{𝑛}{𝑛−1}[\overset{𝑋^{2}}{}−2(\overset{𝑋}{})^{2}+(\overset{𝑋}{})^{2}] \\ & =\frac{𝑛}{𝑛−1}[\overset{𝑋^{2}}{}−(\overset{𝑋}{})^{2}],\end{aligned}


$$

as required.

### Proof That the Sample Variance Is an Unbiased Estimator

Recall that for a sample of size $n,$ the sample variance $S^2$ is given by

$$


S^2 = \dfrac{1}{n-1}\sum_{i=1}^n (X_i - \overline X)^2.


$$

We will now prove that $S^2$ is an unbiased estimator of $\sigma^2,$ that is,

$$


\text{E}\left[S^2\right] = \sigma^2.


$$

A major step towards this goal is to find the expected value of the sum of squares term:

$$


\textrm E \left[ \sum_{i=1}^n (X_i - \overline X)^2 \right] \qquad\qquad (\ast)


$$

First, consider the following sum of squares:

$$


\sum_{i=1}^n (X_i - \mu)^2


$$

We can rewrite this term by adding and subtracting the sample mean $\overline X,$ as follows:

$$


\sum_{i=1}^n \left((X_i - \overline X) + (\overline X - \mu)\right)^2


$$

Squaring and applying the laws of summations, we get

$$


\begin{aligned}\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}((𝑋_{𝑖}−\overset{𝑋}{})+(\overset{𝑋}{}−𝜇))^{2} & = \\ \underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}((𝑋_{𝑖}−\overset{𝑋}{})^{2}+2(𝑋_{𝑖}−\overset{𝑋}{})(\overset{𝑋}{}−𝜇)+(\overset{𝑋}{}−𝜇)^{2}) & = \\ \underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}(𝑋_{𝑖}−\overset{𝑋}{})^{2}+2\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}(𝑋_{𝑖}−\overset{𝑋}{})(\overset{𝑋}{}−𝜇)+\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}(\overset{𝑋}{}−𝜇)^{2} & = \\ \underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}(𝑋_{𝑖}−\overset{𝑋}{})^{2}+2(\overset{𝑋}{}−𝜇)\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}(𝑋_{𝑖}−\overset{𝑋}{})+\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}(\overset{𝑋}{}−𝜇)^{2} & = \\ \underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}(𝑋_{𝑖}−\overset{𝑋}{})^{2}+\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}(\overset{𝑋}{}−𝜇)^{2} & = \\ \underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}(𝑋_{𝑖}−\overset{𝑋}{})^{2}+𝑛(\overset{𝑋}{}−𝜇)^{2} & \end{aligned}


$$

where we have used the fact that $\displaystyle\sum_{i=1}^n(X_i - \overline X) = 0$ and that $(\overline X - \mu)$ does not depend on $i$. Thus, we have that

$$


\sum_{i=1}^n (X_i - \mu)^2 = \sum_{i=1}^n (X_i - \overline X)^2 + n(\overline X- \mu)^2.


$$

Therefore,

$$


\sum_{i=1}^n (X_i - \overline X)^2 = \sum_{i=1}^n (X_i - \mu)^2 - n(\overline X- \mu)^2 . \qquad\qquad (\ast\ast)


$$

Notice that the left-hand side is the summation term $(\ast)$ we wish to find the expectation of.

Now, we make use of the following results:

$$


\begin{aligned}E[(𝑋_{𝑖}−𝜇)^{2}] & =𝜎^{2} \\ E[(\overset{𝑋}{}−𝜇)^{2}] & =Var[\overset{𝑋}{}]=\frac{𝜎^{2}}{𝑛}\end{aligned}


$$

Finding the expectation of $(\ast\ast),$ we have

$$


\begin{aligned}E[\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}(𝑋_{𝑖}−\overset{𝑋}{})^{2}] & =E[\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}(𝑋_{𝑖}−𝜇)^{2}]−𝑛E[(\overset{𝑋}{}−𝜇)^{2}] \\ & =𝑛𝜎^{2}−𝑛⋅\frac{𝜎^{2}}{𝑛} \\ & =𝑛𝜎^{2}−𝜎^{2} \\ & =(𝑛−1)𝜎^{2}.\end{aligned}


$$

Therefore,

$$


\begin{aligned}E[\frac{1}{𝑛}\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}(𝑋_{𝑖}−\overset{𝑋}{})^{2}]=\frac{(𝑛−1)𝜎^{2}}{𝑛}.\end{aligned}


$$

This tells us that the statistic

$$


\dfrac1n\sum_{i=1}^n (X_i - \overline X)^2


$$

is a *biased* estimate of $\sigma^2.$ Therefore, to form an unbiased estimate of $\sigma^2,$ we must divide our summation term by $n-1,$ not $n.$

Therefore, we conclude that

$$


\begin{aligned}E[𝑆^{2}] & =E[\frac{1}{𝑛−1}\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}(𝑋_{𝑖}−\overset{𝑋}{})^{2}] \\ & =\frac{1}{𝑛−1}⋅(𝑛−1)𝜎^{2} \\ & =𝜎^{2}\end{aligned}


$$

as required.
