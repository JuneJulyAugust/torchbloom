# Mean and Variance of the Binomial Distribution

Source: https://www.mathacademy.com/topics/2149?courseId=73
Topic ID: 2149

## Prerequisites

- [Variance of Discrete Random Variables](./1388-variance-of-discrete-random-variables.md)
- [Modeling With the Binomial Distribution](./1395-modeling-with-the-binomial-distribution.md)

## Lesson

### Introduction

Remember that if $X$ is a binomial random variable in which there are $n$ experiments and $p$ is the probability of success on each experiment, then $X$ has the following probability mass function:

$$


f(x) = \binom{n}{x} p^x (1-p)^{n-x}.


$$

It can be shown that the expected value, variance, and standard deviation of a binomial random variable $X$ can be computed as follows:

$$


\begin{aligned}E[𝑋] & =𝑛𝑝 \\ Var[𝑋] & =𝑛𝑝(1−𝑝) \\ SD[𝑋] & =\sqrt{𝑛𝑝(1−𝑝)}\end{aligned}


$$

### Example: Finding the Mean of a Binomial Random Variable

#### Question

A coin is biased so that the probability of it landing on heads is $0.4.$ The coin is tossed $7$ times. What is the mean number of times the coin lands on heads?

#### Explanation

Let the random variable $X$ be equal to the number of times the coin lands on heads.

Here, we have the following information:

- there are $n=7$ tosses

- the probability of landing on heads for each toss is $p=0.4$

So, $X$ follows a binomial distribution, where $X\sim B(7,0.4).$

For a binomial random variable $X,$ the mean is given by

$$


\textrm E[X] = np,


$$

where $n$ is the number of experiments, and $p$ is the probability of success on each experiment.

So, the mean of the number of times the coin lands on heads is

$$


\begin{aligned}E[𝑋] & =𝑛𝑝 \\ & =(7)(0.4) \\ & =2.8.\end{aligned}


$$

### Example: Finding the Variance of a Binomial Random Variable

#### Question

An archer practices shooting $12$ arrows at a target. The archer has a $50\%$ chance of hitting the bull's eye. What is the variance in the number of arrows that hit the bull's eye?

#### Explanation

Let the random variable $X$ be equal to the number of arrows that hit the bull's eye.

Here, we have the following information:

- there are $n=12$ shots

- the probability of hitting the bull's eye for each arrow is $p=50\%=0.5$

So, $X$ follows a binomial distribution, where $X\sim B(12,0.5).$

For a binomial random variable $X,$ the variance is given by

$$


\text{Var}[X] = np(1-p),


$$

where $n$ is the number of experiments, and $p$ is the probability of success on each experiment.

So, the variance of the number of arrows hitting the bull's eye is

$$


\begin{aligned}Var[𝑋] & =𝑛𝑝(1−𝑝) \\ & =(12)(0.5)(1−0.5) \\ & =(6)(0.5) \\ & =3.\end{aligned}


$$

### Example: Finding the Standard Deviation of a Binomial Random Variable

#### Question

A fair five-sided die is rolled $8$ times. What is the standard deviation of the number of times we get an even number? Round your answer to $3$ decimal places.

#### Explanation

Let the random variable $X$ be equal to the number of times we get an even number.

Here, we have the following information:

- there are $n=8$ rolls of the die

- the probability of getting an even number (i.e., a $2,$ or $4$) on any roll of the die is

So, $X$ follows a binomial distribution, where $X\sim B\left(8,\dfrac25\right).$

For a binomial random variable $X,$ the standard deviation is given by

$$


\text{SD}[X] = \sqrt{\text{Var}[X]}=\sqrt{np(1-p)},


$$

where $n$ is the number of experiments, and $p$ is the probability of success on each experiment.

So, the standard deviation of the number of times we get an even number is

$$


\begin{aligned}SD[𝑋] & =\sqrt{𝑛𝑝(1−𝑝)} \\ & =\sqrt{8⋅\frac{2}{5}⋅(1−\frac{2}{5})} \\ & =\sqrt{1.92} \\ & =1.386\end{aligned}


$$

rounded to $3$ decimal places.
