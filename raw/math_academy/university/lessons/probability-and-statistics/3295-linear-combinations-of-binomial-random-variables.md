# Linear Combinations of Binomial Random Variables

Source: https://www.mathacademy.com/topics/3295?courseId=73
Topic ID: 3295

## Prerequisites

- [Modeling With the Binomial Distribution](./1395-modeling-with-the-binomial-distribution.md)
- [Independence of Discrete Random Variables](./3048-independence-of-discrete-random-variables.md)

## Lesson

### Introduction

The sum of two independent binomial random variables is a binomial random variable, provided that the variables have equal success probabilities.

More precisely, if $X_1\sim B(n_1,p)$ and $X_2\sim B(n_2,p)$ are independent, then

$$


Y = X_1+X_2\sim B(n_1+n_2, p).


$$

We'll prove this in a separate lesson. Notice that the probability of success $p$ must be the same for both variables.

For example, if $X_1\sim B({\color{red}{4}},0.5)$ and $X_2\sim B({\color{blue}{3}},0.5)$ are independent, then

$$


\begin{aligned}𝑌=𝑋_{1}+𝑋_{2} & ∼𝐵(4+3,0.5) \\ & ∼𝐵(7,0.5).\end{aligned}


$$

There is some nice intuition behind this rule. Suppose that $X_1$ represents the number of heads obtained when a fair coin is spun ${\color{red}{4}}$ times, and $X_2$ is the number of heads obtained when a fair coin is spun ${\color{blue}{3}}$ times. Therefore, the random variable

$$


Y = X_1+X_2


$$

represents the number of heads obtained when a fair coin is spun ${\color{red}{4}} + {\color{blue}{3}} = 7$ times. In other words, to calculate the distribution of $Y,$ we add the number of trials, but the probability of success on each trial ($0.5$) remains fixed.

**Note:** It's possible to extend this result to an arbitrary number of random variables.

Suppose that $X_1, X_2,\ldots, X_k,$ are *mutually independent* binomial random variables such that

$$


X_i\sim B(n_i,p), \qquad i=1,2,\ldots,k.


$$

It can be shown that their sum has the binomial distribution

$$


Y=X_1+X_2+\ldots+X_k\sim B(n_1+n_2+\cdots + n_k,p).


$$

### Example: Finding the Distribution of a Sum of Binomial Random Variables

#### Question

If $X_1\sim B(8,0.7)$ and $X_2 \sim B(5,0.7)$ are independent, what is the distribution of $Y = X_1+X_2?$

#### Explanation

Recall that if $X_1$ and $X_2$ are independent random variables, where $X_1\sim B(n_1,p)$ and $X_2\sim B(n_2,p)$, then

$$


Y = X_1+X_2\sim B(n_1+n_2, p).


$$

Since $X_1$ and $X_2$ are independent, we have

$$


\begin{aligned}𝑌 & =𝑋_{1}+𝑋_{2} \\ & ∼𝐵(8+5,0.7) \\ & ∼𝐵(13,0.7).\end{aligned}


$$

### Example: Computing a Probability Using a Sum of Binomial Random Variables

#### Question

If $X_1\sim B(6,0.65)$ and $X_2 \sim B(4,0.65)$ are independent, and $Y = X_1+X_2,$ what is $P(Y>7)?$ Round your answer to $3$ decimal places.

#### Explanation

Recall that if $X_1$ and $X_2$ are independent random variables, where $X_1\sim B(n_1,p)$ and $X_2\sim B(n_2,p),$ then

$$


Y = X_1+X_2\sim B(n_1+n_2, p).


$$

Since $X_1$ and $X_2$ are independent, we have

$$


\begin{aligned}𝑌=𝑋_{1}+𝑋_{2} & ∼𝐵(6+4,0.65) \\ & ∼𝐵(10,0.65).\end{aligned}


$$

For a binomial random variable $Y\sim B(n,p),$ the probability mass function is given by

$$


f(y)=\binom{n}{y}p^y(1-p)^{n-y}, \qquad y=0,1,2,\ldots,n.


$$

In this case, we have $Y\sim B(10, 0.65),$ so $Y$ has the probability mass function

$$


f(y)=\binom{10}{y}(0.65)^y(0.35)^{10-y}, \qquad y=0,1,2,\ldots,10.


$$

To find $P(Y >7),$ we need to find $f(y)$ at $y=8,9,10.$ So, we have

$$


\begin{aligned}𝑃(𝑌>7) & =𝑃(𝑌=8)+𝑃(𝑌=9)+𝑃(𝑌=10) \\ & =𝑓(8)+𝑓(9)+𝑓(10) \\ & =(\frac{10}{8})(0.65)^{8}(0.35)^{2}+(\frac{10}{9})(0.65)^{9}(0.35)^{1}+(\frac{10}{10})(0.65)^{10}(0.35)^{0} \\ & ≈0.262.\end{aligned}


$$

### Example: Finding a Sum of Binomial Random Variables in Context

#### Question

There are two blood donation centers in a certain town. On a particular day, $12$ donors arrived at the first center, and $7$ donors arrived at the second center. If it is known that $24\%$ of the town's population has blood type A+, what is the probability that at least $4$ of the donors have blood type A+?

#### Explanation

Let $X_1$ and $X_2$ be the number of A+ donors arriving at centers $A$ and $B,$ respectively. Therefore, we have two mutually independent binomial random variables:

$$


X_1\sim B(12,0.24),\qquad X_2\sim B(7,0.24).


$$

Recall that if $X_1$ and $X_2$ are independent, where $X_1\sim B(n_1,p)$ and $X_2\sim B(n_2,p),$ then

$$


Y = X_1+X_2 \sim B(n_1+n_2, p).


$$

Hence,

$$


\begin{aligned}𝑌=𝑋_{1}+𝑋_{2} & ∼𝐵(12+7,0.24) \\ & ∼𝐵(19,0.24).\end{aligned}


$$

For a binomial random variable $Y\sim B(n,p),$ the probability mass function is given by

$$


f(y)=\binom{n}{y}p^y(1-p)^{n-y}, \qquad y=0,1,2,\ldots,n.


$$

In this case, we have $Y\sim B(19, 0.24),$ so $Y$ has the probability mass function

$$


f(y)=\binom{19}{y}(0.24)^y(0.76)^{19-y}, \qquad y=0,1,2,\ldots,19.


$$

We want to find $P(Y \geq 4).$ The easiest way to do this is to use the complement, which is given by

$$


P(X \geq 4) = 1-P(X < 4).


$$

We have

$$


\begin{aligned}𝑃(𝑌<4) & =𝑃(𝑌=0)+𝑃(𝑌=1)+𝑃(𝑌=2)+𝑃(𝑌=3) \\ & =𝑓(0)+𝑓(1)+𝑓(2)+𝑓(3) \\ & =(\frac{19}{0})(0.24)^{0}(0.76)^{19}+(\frac{19}{1})(0.24)^{1}(0.76)^{18} \\ & +(\frac{19}{2})(0.24)^{2}(0.76)^{17}+(\frac{19}{3})(0.24)^{3}(0.76)^{16} \\ & ≈0.2968.\end{aligned}


$$

Finally,

$$


\begin{aligned}𝑃(𝑌≥4) & =1−𝑃(𝑌<4) \\ & =0.7032.\end{aligned}


$$

Therefore, the probability that at least $4$ of the donors have blood type A+ is $0.7032.$
