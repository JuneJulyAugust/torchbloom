# The Method of Moments: Two-Parameter Distributions

Source: https://www.mathacademy.com/topics/5363?courseId=73
Topic ID: 5363

## Prerequisites

- [The Normal Distribution](./1843-the-normal-distribution.md)
- [Mean and Variance of the Binomial Distribution](./2149-mean-and-variance-of-the-binomial-distribution.md)
- [Mean and Variance of the Continuous Uniform Distribution](./3277-mean-and-variance-of-the-continuous-uniform-distribution.md)
- [The Method of Moments](./4945-the-method-of-moments.md)

## Lesson

### Introduction

In this lesson, we'll learn how to apply the method of moments to two-parameter probability distributions, such as $U(a,b)$ (continuous uniform distribution), $B(m,p)$ (binomial distribution), and $N(\mu, \sigma)$ (normal distribution).

First, let's remind ourselves of the method of moments.

Suppose we have an I.I.D. random sample of size $n{:}$

$$


X_1,\quad X_2,\quad \ldots, \quad X_n


$$

The $k$th theoretical moment is defined as

$$


\mu_k = \textrm{E}[X_i^k] = \sum_{x\in S} x^k \cdot p(x).


$$

The $k$th sample moment is defined as

$$


M_k = \dfrac1n \sum_{i=1}^n X_i^k.


$$

To find the method of moments estimator for some population parameter, we equate the corresponding theoretical and sample moments.

$$


\textrm{E}[X_i] = M_1, \qquad \textrm{E}[X_i^2] = M_2, \qquad \textrm{E}[X_i^3] = M_3, \qquad \ldots


$$

Let's see some examples.

### Example: Finding MM Estimators for Continuous Uniform Random Variables

#### Question

Suppose $X_1,X_2,\ldots,X_{5}$ is an I.I.D. random sample with $X_i\sim U(\theta, \theta+6),$ where $\theta$ is an unknown parameter and $\theta>0.$ For a particular sample $x_1, x_2, x_3\ldots,x_{5}$ you're given that

$$


\displaystyle\sum_{i=1}^{5} x_i^2 = 140.


$$

Find the method of moments estimate $\widehat{\theta}_{MM}$ for $\theta.$

#### Explanation

Recall that the $k$th sample moment $M_k$ of a sample $X_1, X_2, \ldots, X_n$ is given by

$$


M_k = \dfrac1n \sum_{i=1}^n X_i^k.


$$

In particular, the first and second sample moments are given by

$$


M_1 = \dfrac1n \sum_{i=1}^n X_i \,, \qquad M_2 = \dfrac1n \sum_{i=1}^n X_i^2.


$$

To find the method of moments estimator for a parameter, we calculate a sample moment and the corresponding theoretical moment and equate them.

We are given the sum of the squared values in the sample. So, we can calculate the second sample moment:

$$


m_2 = \dfrac{1}{n} \sum_{i=1}^{n} x_i^2 = \dfrac{140}{5}=28


$$

We are given that the variables follow a uniform distribution $U(a,b).$ Therefore,

$$


\textrm{E}[X_i] = \dfrac{a+b}{2}, \qquad \textrm{Var}[X_i] = \dfrac{(b-a)^2}{12}.


$$

We also have

$$


\textrm{Var}[X_i] = \textrm{E}[X^2_i] - \left(\textrm{E}[X_i]\right)^2.


$$

Therefore, we can calculate the second theoretical moment as follows:

$$


\begin{aligned}E[𝑋_{2𝑖}^{}] & =Var[𝑋_{𝑖}]+(E[𝑋_{𝑖}])^{2} \\ & =\frac{((𝜃+6)−𝜃)^{2}}{12}+(\frac{𝜃+(𝜃+6)}{2})^{2} \\ & =\frac{36}{12}+(𝜃+3)^{2} \\ & =3+𝜃^{2}+6𝜃+9 \\ & =𝜃^{2}+6𝜃+12.\end{aligned}


$$

Now, equating the sample and theoretical second moments and using the estimator $\widehat\theta_{MM}$ in place of $\theta,$ we get

$$


\begin{aligned}\overset{𝜃}{ˆ}_{2𝑀𝑀}^{}+6\overset{𝜃}{ˆ}_{𝑀𝑀}+12 & =28.\end{aligned}


$$

Then, we solve for $\widehat\theta_{MM}{:}$

$$


\begin{aligned}\overset{𝜃}{ˆ}_{2𝑀𝑀}^{}+6\overset{𝜃}{ˆ}_{𝑀𝑀}+12 & =28 \\ \overset{𝜃}{ˆ}_{2𝑀𝑀}^{}+6\overset{𝜃}{ˆ}_{𝑀𝑀}−16 & =0 \\ (\overset{𝜃}{ˆ}_{𝑀𝑀}+8)(\overset{𝜃}{ˆ}_{𝑀𝑀}−2) & =0\end{aligned}


$$

This gives the solutions

$$


\widehat{\theta}_{MM}= -8, \qquad \widehat{\theta}_{MM}= 2.


$$

However, we discard the negative solution since we are given that $\theta > 0.$ Therefore, our method of moments estimate for $\theta$ is

$$


\widehat{\theta}_{MM}= \boxed{\color{blue}2}.


$$

### Example: Finding MM Estimators for Binomial Random Variables

#### Question

Suppose $X_1,X_2,\ldots,X_6$ is an I.I.D. random sample with $X_i\sim B(3, \theta)$ and unknown probability of success $\theta.$ For a particular sample $x_1, x_2,\ldots, x_{6},$ you're given that

$$


\displaystyle\sum_{i=1}^{6} x_i^2 = 10.


$$

Find the method of moments estimate $\widehat{\theta}_{MM}$ for $\theta.$

#### Explanation

Recall that the $k$th sample moment $M_k$ of a sample $X_1, X_2, \ldots, X_n$ is given by

$$


M_k = \dfrac1n \sum_{i=1}^n X_i^k.


$$

In particular, the first and second sample moments are given by

$$


M_1 = \dfrac1n \sum_{i=1}^n X_i \,, \qquad M_2 = \dfrac1n \sum_{i=1}^n X_i^2.


$$

To find the method of moments estimator for a parameter, we calculate a sample moment and the corresponding theoretical moment and equate them.

We are given the sum of the squared values in the sample. So, we can calculate the second sample moment:

$$


m_2 = \dfrac{1}{n} \sum_{i=1}^{n} x_i^2 = \dfrac{10}{6}=\dfrac53


$$

We are given that the variables follow a binomial distribution $B(m,\theta)$ Therefore,

$$


\textrm{E}[X_i] = m\theta, \qquad \textrm{Var}[X_i] = m\theta (1-\theta).


$$

We also have

$$


\textrm{Var}[X_i] = \textrm{E}[X^2_i] - \left(\textrm{E}[X_i]\right)^2.


$$

Therefore, we can calculate the second theoretical moment as follows:

$$


\begin{aligned}E[𝑋_{2𝑖}^{}] & =Var[𝑋_{𝑖}]+(E[𝑋_{𝑖}])^{2} \\ & =𝑚𝜃(1−𝜃)+𝑚^{2}𝜃^{2} \\ & =3𝜃(1−𝜃)+3^{2}𝜃^{2} \\ & =3𝜃−3𝜃^{2}+9𝜃^{2} \\ & =6𝜃^{2}+3𝜃.\end{aligned}


$$

Now, equating the sample and theoretical second moments and using the estimator $\widehat\theta_{MM}$ in place of $\theta,$ we get

$$


\begin{aligned}6\overset{𝜃}{ˆ}_{2𝑀𝑀}^{}+3\overset{𝜃}{ˆ}_{𝑀𝑀}=\frac{5}{3} & \\ 18\overset{𝜃}{ˆ}_{2𝑀𝑀}^{}+9\overset{𝜃}{ˆ}_{𝑀𝑀}−5 & =0.\end{aligned}


$$

Then, we solve for $\widehat{\theta}_{MM}{:}$

$$


\begin{aligned}\overset{𝜃}{ˆ}_{𝑀𝑀} & =\frac{−9±\sqrt{√9^{2}−4(18)(−5)}}{2(18)} \\ \overset{𝜃}{ˆ}_{𝑀𝑀} & =\frac{−3±7}{12}\end{aligned}


$$

This gives the solutions

$$


\widehat{\theta}_{MM}= -\dfrac{5}{6}, \qquad \widehat{\theta}_{MM}= \dfrac{1}{3}.


$$

However, we discard the negative solution since $\theta > 0.$ Therefore, our method of moments estimate for $\theta$ is

$$


\widehat{\theta}_{MM} = \dfrac 13.


$$

### Example: Finding MM Estimators for Normal Random Variables

#### Question

Suppose $X_1, X_2, \ldots, X_{10}$ is an I.I.D. random sample with $X_i \sim N(\mu, \, \sigma^2),$ where $\mu$ and $\sigma^2$ are unknown parameters. For a particular sample $x_1, x_2, \ldots, x_{10},$ you're given that

$$


\displaystyle\sum_{i=1}^{10} x_i = 70, \qquad \sum_{i=1}^{10} x_i^2 = 550.


$$

Find the method of moments estimates $\widehat{\mu}_{MM}$ and $\widehat{\sigma^2}_{MM}$ for $\mu$ and $\sigma^2,$ respectively.

#### Explanation

Recall that the $k$th sample moment $M_k$ of a sample $X_1, X_2, \ldots, X_n$ is given by

$$


M_k = \dfrac1n \sum_{i=1}^n X_i^k.


$$

In particular, the first and second sample moments are given by

$$


M_1 = \dfrac1n \sum_{i=1}^n X_i \,, \qquad M_2 = \dfrac1n \sum_{i=1}^n X_i^2.


$$

To find the method of moments estimator for a parameter, we calculate a sample moment and the corresponding theoretical moment and equate them.

We are given the sum of the values in the sample and the sum of squares. So, we can calculate the first and second sample moments:

$$


\begin{aligned}𝑚_{1} & =\frac{1}{𝑛}\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}𝑥_{𝑖}=\frac{70}{10}=7 \\ 𝑚_{2} & =\frac{1}{𝑛}\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}𝑥_{2𝑖}^{}=\frac{550}{10}=55\end{aligned}


$$

We are given that the variables $X_i$ follow a normal distribution. Therefore:

$$


\begin{aligned}E[𝑋_{𝑖}] & =𝜇 \\ E[𝑋_{2𝑖}^{}] & =Var[𝑋_{𝑖}]+(E[𝑋_{𝑖}])^{2}=𝜎^{2}+𝜇^{2}\end{aligned}


$$

Now, equating the sample and theoretical first and second moments, using the estimators $\widehat\mu_{MM}$ and $\widehat{\sigma^2}_{MM}$ in place of $\mu$ and $\sigma^2,$ we get

$$


\begin{aligned}\overset{𝜇}{ˆ}_{𝑀𝑀} & =7, \\ \overset{𝜎^{2}}{ˆ}_{𝑀𝑀}+\overset{𝜇}{ˆ}_{2𝑀𝑀}^{} & =55 \\ \overset{𝜎^{2}}{ˆ}_{𝑀𝑀}+7^{2} & =55 \\ \overset{𝜎^{2}}{ˆ}_{𝑀𝑀} & =6.\end{aligned}


$$
