# Many-to-One Transformations of Discrete Random Variables

Source: https://www.mathacademy.com/topics/3647?courseId=73
Topic ID: 3647

## Prerequisites

- [One-To-One Functions](../../../high-school/traditional/lessons/algebra-ii/1886-one-to-one-functions.md)
- [One-to-One Transformations of Discrete Random Variables](./3631-one-to-one-transformations-of-discrete-random-variables.md)

## Lesson

### Introduction

Suppose that the random variable $X$ has the following probability distribution.

Note that $f_X$ is the probability mass function of $X.$

Let's define a new random variable $Y = X^2.$ What is the probability distribution of $X^2?$

Let's start by adding a $Y=X^2$ row to our table.

Now, notice that the transformation $Y = X^2$ is one-to-one for $X\in \{1,2,3\}.$ Since the transformation is one-to-one, we can immediately write down the distribution of $Y.$

From this table, we can deduce the following results:

$$


\begin{aligned}𝑃(𝑌=1) & =𝑃(𝑋^{2}=1)=0.25 \\ 𝑃(𝑌=4) & =𝑃(𝑋^{2}=4)=0.5 \\ 𝑃(𝑌=9) & =𝑃(𝑋^{2}=9)=0.25\end{aligned}


$$

### Example: Finding Distributions of Squared Random Variables: One-to-One Transformations

#### Question

The random variable $X$ has the following probability distribution.

Let $Y=\dfrac12X^2.$ The distribution of $Y$ is given below.

Find the values of $a,b,c,$ and $d.$

#### Explanation

First, let's add a $Y = \dfrac12X^2$ row to our table:

Therefore, the distribution of $Y$ is as follows:

Hence, $a=2, b=8, c=0.2,$ and $d=0.3.$

### Calculating Probability Distributions for Two-to-One Transformations

Until now, when defining a new random variable using a transformation of the form $Y = Y(X),$ we have only considered one-to-one transformations.

In these cases, this means that

- there is a one-to-one correspondence between the support of $X$ and the support of $Y,$ and

- consequently, there is a one-to-one correspondence between the probability mass functions $f_X(x)$ and $f_Y(y).$

This makes it very easy to write down $f_Y$ when we know $f_X.$

When the transformation is many-to-one, we need to be more careful.

To illustrate, consider the random variable $X$ with the distribution given below,

To summarize, we have a $25\%$ chance of getting $X=-2,$ and a $75\%$ chance of getting $X=2.$

Suppose we then define $Y = X^2.$ Let's add this row to our table.

Something interesting has happened. Notice that $Y=4$ is the *only* possible value of $Y!$ So, we have

$$


P(Y=4) = {\color{red}{0.25}} + {\color{blue}{0.75}} = 1.


$$

Therefore, the probability distribution of $Y$ is as follows:

To summarise, when working with a transformation $Y=Y(X)$ that is many-to-one, we should apply the following steps:

- Find all of the possible values of $Y.$

- Calculate $f_Y(y)$ for each possible value of $Y$ by adding together *all* of the values of $f_X$ that correspond to $f_Y(y).$

### Example: Finding Distributions of Squared Random Variables: Many-to-One Transformations

#### Question

The random variable $X$ has the following probability distribution.

Let $Y=1-X^2.$ The distribution of $Y$ is given below.

Find the values of $a,b,c,$ and $d.$

#### Explanation

First, let's add a $Y = 1-X^2$ row to our table.

From the table, we see that $Y \in \{-3,0,1\}.$ Notice that we now have two columns for both $Y=-3$ and $Y=0.$

We calculate the probabilities associated with each value of $Y$ as follows:

$$


\begin{aligned}𝑃(𝑌=−3) & =0.2+0.1 \\ 𝑃(𝑌=0) & =0.1+0.3 \\ 𝑃(𝑌=1) & =0.3\end{aligned}


$$

This gives the following table:

### A Word on Notation

Suppose we have a random variable $X$ with probability mass function $f(x).$

When computing probabilities relating to the random variable $X^2,$ rather than establishing a new random variable $Y,$ we often work directly with $f(x).$ This often makes our calculations faster.

Let's see an example.

### Example: Calculating a Probability Involving a Squared Random Variable

#### Question

The random variable $X$ has the following probability distribution.

Calculate $P(X^2 = 4).$

#### Explanation

Let's first add an $X^2$ row to our table.

From the second and third rows of our table, we can immediately conclude that

$$


P(X^2 = 4) = 0.2+0.1 = 0.3.


$$
