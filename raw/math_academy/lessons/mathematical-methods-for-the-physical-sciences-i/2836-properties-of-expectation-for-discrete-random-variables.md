# Properties of Expectation for Discrete Random Variables

Source: https://www.mathacademy.com/topics/2836?courseId=154
Topic ID: 2836

## Prerequisites

- [Expected Values of Discrete Random Variables](./730-expected-values-of-discrete-random-variables.md)
- [One-to-One Transformations of Discrete Random Variables](./3631-one-to-one-transformations-of-discrete-random-variables.md)

## Lesson

### Introduction

There are several important properties that we can use to simplify expressions involving expected values.

The first property is that the expected value of a constant is just the constant itself. That is, for any constant $a,$ we have

$$


\textrm E[a] = a.


$$

For example,

$$


\textrm E[5] = 5,\qquad \textrm E[-99] = -99,\qquad \textrm E[\sqrt 2] = \sqrt 2.


$$

The idea that the expected value of a constant is equal to the same constant makes intuitive sense. If $a$ is a constant, then it does not vary. Therefore, it is always sure to have the same value.

### Example: Computing the Expected Value of a Constant

#### Question

Compute $\textrm E[1.2].$

#### Explanation

For any constant $a,$ we have

$$


\textrm E[a] = a.


$$

Therefore,

$$


\textrm E[1.2] = 1.2.


$$

### The Expected Value of a Scaled Random Variable

We can also factor constants outside of an expected value expression. So for any constant $a$ and any random variable $X,$ we have

$$


\textrm E[aX] = a \textrm E[X].


$$

For example,

$$


\textrm E[5X] = 5 \textrm E[X],\qquad\textrm E[-9X] = -9 \textrm E[X], \qquad \textrm E[\pi X] = \pi \textrm E[X].


$$

We can prove this rule using the definition of the expected value, as follows:

$$


\begin{aligned}E[𝑎𝑋] & =\underset{𝑥∈𝑆}{∑}𝑎𝑥⋅𝑓(𝑥) \\ & =𝑎\underset{𝑥∈𝑆}{∑}𝑥⋅𝑓(𝑥) \\ & =𝑎E[𝑋]\end{aligned}


$$

### Example: Computing the Expected Value of a Scaled Random Variable

#### Question

A random variable $X$ has the probability distribution given below.

Calculate $\textrm E\left[\dfrac{1}{4}X\right].$

#### Explanation

First, let's find $\textrm E[X].$

The expected value of a discrete random variable $X$ with probability mass function $f(x)$ and sample space $S$ is given by

$$


\textrm E[X] = \sum\limits_{x \in S} x \cdot f(x).


$$

Summing up the products of each value of $X$ and its associated probability, we get

$$


\begin{aligned}E[𝑋] & =\underset{𝑥∈𝑆}{∑}𝑥⋅𝑓(𝑥) \\ & =0⋅\frac{1}{5}+1⋅\frac{1}{10}+2⋅\frac{3}{10}+3⋅\frac{3}{10}+4⋅\frac{1}{10} \\ & =2.\end{aligned}


$$

Therefore,

$$


\begin{aligned}E[\frac{1}{4}𝑋] & =E[\frac{1}{4}𝑋] \\ & =\frac{1}{4}E[𝑋] \\ & =\frac{1}{4}⋅2 \\ & =\frac{1}{2}.\end{aligned}


$$

### The Expected Value of a Transformed Random Variable

Finally, we can combine the factor and constant rules into one simple rule.

Suppose that $X$ is a random variable and $a$ and $b$ are constants. By combining our two rules, we have

$$


\textrm E[aX + b] = a\textrm E[X] + b.


$$

For example, if we know that $\textrm{E}[X] = 4,$ then

$$


\begin{aligned}E[3𝑋+2] & =E[3𝑋+2] \\ & =3E[𝑋]+2 \\ & =3(4)+2 \\ & =12+2 \\ & =14.\end{aligned}


$$

### Example: Computing the Expected Value of a Transformed Random Variable

#### Question

Compute $\textrm E[1-4X]$ if $\textrm E[X]=\dfrac{1}{2}.$

#### Explanation

For any constants $a$ and $b$ and any random variable $X,$ we have

$$


\textrm E[aX+b] = a \textrm E[X]+b.


$$

Therefore,

$$


\begin{aligned}E[1−4𝑋] & =E[−4𝑋+1] \\ & =−4E[𝑋]+1 \\ & =−4(\frac{1}{2})+1 \\ & =−2+1 \\ & =−1.\end{aligned}


$$
