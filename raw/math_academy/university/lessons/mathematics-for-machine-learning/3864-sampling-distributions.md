# Sampling Distributions

Source: https://www.mathacademy.com/topics/3864?courseId=145
Topic ID: 3864

## Prerequisites

- [The Sample Mean](./2980-the-sample-mean.md)

## Lesson

### Introduction

Recall that, given a random sample $X_1, X_2,\ldots X_n$ of size $n,$ the sample mean $\overline{X}$ is an unbiased estimator of the population mean $\mu,$ and is defined as

$$


\overline{X} = \dfrac1n\sum_{i=1}^n X_i .


$$

The sample mean is an example of a **statistic**. A statistic is a random variable computed using values from a sample. Statistics are often used to estimate population parameters, although they also have other uses.

Let's take a look at some other examples of statistics:

- The following statistic could be used as an estimator for the population variance $\sigma^2\mathbin{:}$

- The following statistic could be used as an estimator for the population maximum:

- The following statistic could be used as an estimator for the population range:

- The following statistic could be used as an estimator for the population median:

Statistics cannot include any *unknown* population parameters. For example:

- If the population mean $\mu$ is *unknown,* then the following quantity is *not* a statistic:

- However, if the population parameters $\mu$ and $\sigma$ are *both* known, then the following quantity *is* a statistic:

Finally, since statistics are described using observations from a random sample, they are random variables and therefore have a probability distribution. The probability distribution of a statistic is called the **sampling distribution** of the statistic.

### Example: Identifying Statistics

#### Question

A sample $X_1, X_2, \ldots, X_{8}$ is drawn from a population with population mean $\mu$ and population standard deviation $\sigma.$ If $\mu$ and $\sigma$ are both unknown, which of the following are statistics?

1. $\displaystyle \min(X_1, X_2, \dots, X_8)$

2. $\displaystyle \sum_{i=1}^{4} X_{2i}^2$

3. $\displaystyle \sum_{i=1}^{8} \left(\dfrac{X_i}{\sigma} - 1 \right)^2$

#### Explanation

Suppose $X_1, X_2, \ldots, X_n$ is a sequence of random variables representing a random sample of size $n$ drawn from a population. A statistic is a random variable expressed as a function of $X_i.$

Statistics cannot involve unknown population parameters.

With that in mind, let's examine each expression.

- Expression I is a statistic. It is a function of the sample $X_1, X_2,\ldots, X_n$ only.

- Expression II is a statistic. It is a function of the sample $X_1, X_2,\ldots, X_n$ only. Note that a statistic doesn't need to include every sample element.

- Expression III is ** a statistic. It is a function that contains the population standard deviation $\sigma.$

Therefore, the correct answer is "I and II only."

### Example: Calculating Statistics

#### Question

The weights, in kilograms, of five randomly selected 2-year-old children visiting a pediatrician were measured. The results are shown below.

$$


12.5, \quad 11.7,\quad 13.2,\quad 12.8, \quad 12.1


$$

Calculate the value of the statistic $\displaystyle\sum_{i=1}^n X_i^2$ for this particular sample.

#### Explanation

Suppose $X_1, X_2, \ldots, X_n$ is a sequence of random variables representing a random sample of size $n$ drawn from a population. A statistic is a random variable expressed as a function of $X_i.$

Statistics cannot involve unknown population parameters.

Note the following notation:

- $X_i$ denotes the random variable representing the $i$th observation in a random sample, and

- $x_i$ is the value of $X_i$ in a specific sample.

For the given sample, we have

$$


\begin{aligned}\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}𝑥_{2𝑖} & =(12.5)^{2}+(11.7)^{2}+(13.2)^{2}+(12.8)^{2}+(12.1)^{2} \\ & =156.25+136.89+174.24+163.84+146.41 \\ & =777.63\end{aligned}


$$

Therefore, the value of our statistic for this particular sample is $777.63\,\textrm {kg}^2.$
