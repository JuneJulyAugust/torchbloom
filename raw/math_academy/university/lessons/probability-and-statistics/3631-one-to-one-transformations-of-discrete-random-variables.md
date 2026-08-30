# One-to-One Transformations of Discrete Random Variables

Source: https://www.mathacademy.com/topics/3631?courseId=73
Topic ID: 3631

## Prerequisites

- [Probability Mass Functions of Discrete Random Variables](../discrete-mathematics/1290-probability-mass-functions-of-discrete-random-variables.md)

## Lesson

### Introduction

Suppose that the random variable $X$ has the following probability distribution.

Note that $f_X(x)$ denotes the probability mass function of $X.$

Now, imagine that we define the variable $Y$ as follows:

$$


Y = 2X


$$

Since $Y$ is a function of $X,$ it must also be a random variable. What is the probability distribution of $Y?$

We start by computing all possible values of $Y,$ so let's add a $Y=2X$ row to our table.

So, the possible values of $Y$ are $2,4,6,8,$ and $10.$

We now need to calculate the probability mass function $f_Y(y)$ for each possible value of $Y.$

The crucial thing to realize is that $f_X(x) = f_Y(y)$ for corresponding values of $X$ and $Y.$ So, for example, we have the following:

$$


\begin{aligned}𝑓_{𝑋}(1)=𝑃(𝑋=1) & =𝑃(𝑌=2)=𝑓_{𝑌}(2)=0.25 \\ 𝑓_{𝑋}(2)=𝑃(𝑋=2) & =𝑃(𝑌=4)=𝑓_{𝑌}(4)=0.2 \\ & ⋮\end{aligned}


$$

Therefore, the distribution of $Y$ is as follows:

### Example: Finding the Distribution of a Transformed Random Variable

#### Question

The random variable $X$ has the following probability distribution.

Let $Y=2-4X.$ The distribution of $Y$ is given below.

What is the value of $a+b+c?$

#### Explanation

First, let's add a $Y = 2-4X$ row to our table.

Now, $f_X(x) = f_Y(y)$ for corresponding values of $X$ and $Y.$ Therefore, the distribution of $Y$ is as follows:

So, we have $a=4, b=0.2, c=2,$ and therefore $a+b+c =6.2.$

### Example: Calculating a Probability Involving a Transformed Random Variable

#### Question

The random variable $X$ has the following probability distribution.

Let $Y=2-4X.$ Calculate $P(Y \gt 2).$

#### Explanation

First, let's add a $Y = 2-4X$ row to our table.

Now, $f_X(x) = f_Y(y)$ for corresponding values of $X$ and $Y.$ So, the distribution of $Y$ is as follows:

Therefore,

$$


\begin{aligned}𝑃(𝑌>2) & =𝑃(𝑌=3)+𝑃(𝑌=4) \\ & =0.2+0.25 \\ & =0.45.\end{aligned}


$$
