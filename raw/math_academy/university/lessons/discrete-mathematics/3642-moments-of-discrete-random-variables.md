# Moments of Discrete Random Variables

Source: https://www.mathacademy.com/topics/3642?courseId=109
Topic ID: 3642

## Prerequisites

- [Properties of Expectation for Discrete Random Variables](./2836-properties-of-expectation-for-discrete-random-variables.md)
- [Many-to-One Transformations of Discrete Random Variables](./3647-many-to-one-transformations-of-discrete-random-variables.md)

## Lesson

### Introduction

Recall that for a discrete random variable $X$ defined over a set $S,$ the expected value of $X,$ denoted $\textrm E[X],$ is given by

$$



\textrm E[X] = \sum\limits_{x \in S} x \cdot f(x),



$$

where $f(x)$ is the probability mass function of $X.$

Therefore, we can calculate the expected value of the random variable $X^2$ as

$$



\textrm E[X^2] = \sum\limits_{x \in S} x^2 \cdot f(x).



$$

For example, suppose that the random variable $X$ has the following probability distribution.

In this case, $\textrm E[X^2]$ is given by

$$



\begin{aligned}E[𝑋^{2}] & =\underset{𝑥∈𝑆}{∑}𝑥^{2}⋅𝑓(𝑥) \\ & =1^{2}⋅0.25+2^{2}⋅0.5+3^{2}⋅0.25 \\ & =1⋅0.25+4⋅0.5+9⋅0.25 \\ & =4.5.\end{aligned}



$$

**Watch out!** When computing $\textrm E[X^2],$ it's important to remember that we still evaluate the probability mass function as $f(x),$ *not* $f(x^2).$

### Example: Calculating the Second Moment of a Random Variable

#### Question

A random variable $X$ has the probability distribution given below.

Calculate $\textrm E[X^2].$

#### Explanation

If $X$ is a discrete random variable with probability mass function $f(x)$ and sample space $S,$ the expected value of $X^2$ is given by

$$



\textrm E[X^2] = \sum\limits_{x \in S} x^2 \cdot f(x).



$$

Summing up the products of each squared value of $X$ and its associated probability, we get

$$



\begin{aligned}E[𝑋^{2}] & =\underset{𝑥∈𝑆}{∑}𝑥^{2}⋅𝑓(𝑥) \\ & =0^{2}⋅0.2+1^{2}⋅0.25+2^{2}⋅0.15+3^{2}⋅0.35+4^{2}⋅0.05 \\ & =0⋅0.2+1⋅0.25+4⋅0.15+9⋅0.35+16⋅0.05 \\ & =4.8.\end{aligned}



$$

### The Moments of a Random Variable

Suppose that $X$ is a discrete random variable with probability mass function $f(x)$ defined over $S.$

The values $\textrm E[X]$ and $\textrm E[X^2]$ are called the **first moment** and **second moment**, respectively.

It's also possible to define higher moments. For example, $\textrm E[X^3]$ is the **third moment.**

Notice the pattern:

- $\displaystyle \textrm E[X] = \sum\limits_{x \in S} x \cdot f(x)$ is the first moment

- $\displaystyle \textrm E[X^2] = \sum\limits_{x \in S} x^2 \cdot f(x)$ is the second moment

- $\displaystyle \textrm E[X^3] = \sum\limits_{x \in S} x^3 \cdot f(x)$ is the third moment

- $\,\cdots$

In general, the $n$th moment is given by

$$



\displaystyle \textrm E[X^n] = \sum\limits_{x \in S} x^n \cdot f(x).



$$

The concept of a moment will become important later. In particular, we'll soon see how $\textrm{E}[X^2]$ can be used to compute the **variance** of a random variable.

Finally, note that $\textrm E[X], \textrm E[X^2], \textrm E[X^3],$ etc. are sometimes referred to as the first, second, and third **raw moments**. This is because it's possible to define other types of moment.

In general, $\textrm{E}[X^n]$ can be called either the $n$th *moment* or $n$th *raw moment*.

### Example: Calculating Higher Moments of a Random Variable

#### Question

A random variable $X$ has the probability distribution given below.

Calculate $\textrm E[X^3].$

#### Explanation

If $X$ is a discrete random variable with probability mass function $f(x)$ and sample space $S,$ the expected value of $X^3$ is given by

$$



\textrm E[X^3] = \sum\limits_{x \in S} x^3 \cdot f(x).



$$

Summing up the products of each cubed value of $X$ and its associated probability, we get

$$



\begin{aligned}E[𝑋^{3}] & =\underset{𝑥∈𝑆}{∑}𝑥^{3}⋅𝑓(𝑥) \\ & =1^{3}⋅0.15+2^{3}⋅0.25+3^{3}⋅0.5+4^{3}⋅0.1 \\ & =1⋅0.15+8⋅0.25+27⋅0.5+64⋅0.1 \\ & =0.15+2+13.5+6.4 \\ & =22.05.\end{aligned}



$$

### Example: Simplifying Expressions Using the Properties of Expected Value

#### Question

Compute $\textrm E[X(X-3) + 4]$ if $\textrm E[X^2] = 4$ and $\textrm E[X] = 1.$

#### Explanation

Expanding out the product inside the expected value, using the properties of the expected value, and substituting in the given information, we get

$$



\begin{aligned}E[𝑋(𝑋−3)+4] & =E[𝑋^{2}−3𝑋+4] \\ & =E[𝑋^{2}]−3E[𝑋]+E[4] \\ & =E[𝑋^{2}]−3E[𝑋]+4 \\ & =4−3(1)+4 \\ & =5.\end{aligned}



$$
