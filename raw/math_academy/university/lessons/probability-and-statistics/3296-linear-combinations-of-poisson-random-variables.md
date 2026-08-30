# Linear Combinations of Poisson Random Variables

Source: https://www.mathacademy.com/topics/3296?courseId=73
Topic ID: 3296

## Prerequisites

- [Modeling With the Poisson Distribution](./2838-modeling-with-the-poisson-distribution.md)
- [Independence of Discrete Random Variables](./3048-independence-of-discrete-random-variables.md)

## Lesson

### Introduction

The sum of two independent Poisson random variables is also a Poisson random variable.

More precisely, if $X_1$ and $X_2$ are independent Poisson random variables such that $X_1\sim \textrm{Po}(\lambda_1)$ and $X_2\sim \textrm{Po}(\lambda_2)$, then

$$


Y = X_1+X_2\sim \textrm{Po}(\lambda_1+\lambda_2).


$$

We'll prove this in a separate lesson.

For example, if $X_1\sim \textrm{Po}({\color{red}{4}})$ and $X_2\sim \textrm{Po}({\color{blue}{5}})$ are independent, then

$$


\begin{aligned}𝑌=𝑋_{1}+𝑋_{2} & ∼Po(4+5) \\ & ∼Po(9).\end{aligned}


$$

There is some nice intuition behind this rule. For example, consider the following situation:

- the random variable $X_1\sim \textrm{Po}({\color{red}{4}})$ represents the number of red buses that arrive at a bus station every hour, and

- the random variable $X_2\sim \textrm{Po}({\color{blue}{5}})$ represents the number of blue buses that arrive the same bus station every hour.

Under this model, we assume that an average of $\color{red}{4}$ red buses and $\color{blue}{5}$ blue buses arrive at the bus station every hour.

Then, the random variable

$$


Y = X_1+X_2 \sim \textrm{Po}(9)


$$

represents the number of buses (both red and blue) that arrive at the bus station every hour, arriving at an average rate of ${\color{red}{4}}+{\color{blue}{5}} = 9$ buses per hour.

**Watch out!** The discussion above only applies to sums. The *difference* of two independent Poisson random variables is *not* a Poisson random variable!

### Example: Finding the Distribution of a Sum of Poisson Random Variables

#### Question

If $X_1\sim \textrm{Po}(4)$ and $X_2\sim \textrm{Po}(2.3)$ are independent, then what is the distribution of $Y = X_1+X_2?$

#### Explanation

Recall that if $X_1$ and $X_2$ are independent Poisson random variables, where $X_1\sim \textrm{Po}(\lambda_1)$ and $X_2\sim \textrm{Po}(\lambda_2)$, then

$$


X_1+X_2\sim \textrm{Po}(\lambda_1+\lambda_2).


$$

Because $X_1$ and $X_2$ are independent variables, we have

$$


\begin{aligned}𝑌=𝑋_{1}+𝑋_{2} & ∼Po(4+2.3) \\ & ∼Po(6.3).\end{aligned}


$$

### Example: Calculating a Probability Involving a Sum of Poisson Random Variables

#### Question

If $X_1\sim \textrm{Po}(2)$ and $X_2\sim \textrm{Po}(4)$ are independent, and $Y=X_1+X_2$, then calculate $P(Y<3).$ Round your answer to $3$ decimal places.

#### Explanation

Recall that if $X_1$ and $X_2$ are independent Poisson random variables, where $X_1\sim \textrm{Po}(\lambda_1)$ and $X_2\sim \textrm{Po}(\lambda_2)$, then

$$


X_1+X_2\sim \textrm{Po}(\lambda_1+\lambda_2).


$$

Because $X_1$ and $X_2$ are independent variables, we have

$$


\begin{aligned}𝑌=𝑋_{1}+𝑋_{2} & ∼Po(2+4) \\ & ∼Po(6).\end{aligned}


$$

The probability mass function of $Y\sim \textrm{Po}(\lambda)$ is given by

$$


f(y) = \dfrac{\lambda^y e^{-\lambda}}{y!}, \qquad y=0,1,2,\ldots


$$

Here, $Y\sim \textrm{Po}(6)$, so the probability distribution of $Y$ is

$$


f(y) = \dfrac{6^y e^{-6}}{y!}, \qquad y=0,1,2,\ldots


$$

Therefore,

$$


\begin{aligned}𝑃(𝑌<3) & =𝑃(𝑌=0)+𝑃(𝑌=1)+𝑃(𝑌=2) \\ & =𝑓(0)+𝑓(1)+𝑓(2) \\ & =\frac{6^{0}𝑒^{−6}}{0!}+\frac{6^{1}𝑒^{−6}}{1!}+\frac{6^{2}𝑒^{−6}}{2!} \\ & ≈0.062.\end{aligned}


$$

### Example: Calculating a Probability Involving a Sum of Poisson Random Variables in Context

#### Question

A popular mobile app has two download options, one for tablets and one for smartphones. Customers downloaded the app at an average rate of $5$ times per minute on tablets and $6$ times per minute on smartphones. Assuming that each download is mutually independent, find the probability that the app will be downloaded more than five times over the next minute.

#### Explanation

Let's define the following random variables:

- Let $X_1$ be the number of times the app is downloaded on tablets over the next minute.

- Let $X_2$ be the number of times the app is downloaded on smartphones over the next minute.

We assume that $X_1$ and $X_2$ are independent Poisson random variables.

- The app is downloaded, on average, at a rate of $5$ times per minute on tablets. Thus, $X_1 \sim \textrm{Po}(5).$

- The app is downloaded, on average, at a rate of $6$ times per minute on smartphones. Thus, $X_2 \sim \textrm{Po}(6).$

Let $Y = X_1+X_2.$ We want to find $P(Y > 5).$

Since $X_1\sim \textrm{Po}(5)$ and $X_2\sim \textrm{Po}(6)$ are independent Poisson random variables, then

$$


\begin{aligned}𝑌=𝑋_{1}+𝑋_{2} & ∼Po(5+6) \\ & ∼Po(11).\end{aligned}


$$

So, the probability distribution of $Y$ is

$$


f(y) = \dfrac{11^y e^{-11}}{y!}, \qquad y=0,1,2,\ldots\,.


$$

There are infinitely many values of $Y$ such that $Y >5.$ However, we can simplify the computation by using the complement instead:

$$


\begin{aligned}𝑃(𝑌>5) & =1−𝑃(𝑌≤5)\end{aligned}


$$

Computing the complement, we get

$$


\begin{aligned}𝑃(𝑌≤5) & =𝑃(𝑌∈{0,1,2,3,4,5}) \\ & =𝑃(𝑌=0)+𝑃(𝑌=1)+𝑃(𝑌=2) \\ & \,+𝑃(𝑌=3)+𝑃(𝑌=4)+𝑃(𝑌=5) \\ & =𝑓(0)+𝑓(1)+𝑓(2)+𝑓(3)+𝑓(4)+𝑓(5) \\ & =\frac{11^{0}𝑒^{−11}}{0!}+\frac{11^{1}𝑒^{−11}}{1!}+\frac{11^{2}𝑒^{−11}}{2!} \\ & \,+\frac{11^{3}𝑒^{−11}}{3!}+\frac{11^{4}𝑒^{−11}}{4!}+\frac{11^{5}𝑒^{−11}}{5!} \\ & ≈0.0375.\end{aligned}


$$

Therefore,

$$


\begin{aligned}𝑃(𝑌>5) & =1−𝑃(𝑌≤5) \\ & ≈1−0.0375 \\ & =0.9625.\end{aligned}


$$
