# Calculating Probabilities With Continuous Random Variables

Source: https://www.mathacademy.com/topics/4043?courseId=73
Topic ID: 4043

## Prerequisites

- [Definite Integrals of Piecewise Functions](../../../ap-courses/lessons/ap-calculus-ab/626-definite-integrals-of-piecewise-functions.md)
- [Probability Density Functions of Continuous Random Variables](./1347-probability-density-functions-of-continuous-random-variables.md)

## Lesson

### Introduction

Recall that the **probability density function** (or **pdf**) of a continuous random variable $X$ defined over a set $S$ is a function $f(x)$ that satisfies the following conditions:

- $f(x) \geq 0$ for all $x$ in $S$

- $\displaystyle \int_{S} f(x) \, \textrm dx = 1$

The probability that $X$ lies in the interval $[a,b]$ is given by

$$


P(a \leq X \leq b) = \int_a^b f(x) \, \textrm dx.


$$

This probability can be interpreted as the area bounded between $f(x)$ and the $x$-axis over the interval $x\in [a,b],$ as shown below.

![Instructional graphic](../../../lesson-assets/probability-and-statistics/topic-4043/b331585a4bfca0a9.png)

Also, remember that for continuous random variables, we get the same answer whether or not we include the endpoints of an interval $[a,b].$ In other words,

$$


P(a \leq X \leq b) = P(a < X < b) = P(a < X \leq b) = P(a \leq X < b).


$$

In this lesson, we'll get some practice at computing probabilities with continuous random variables.

### Example: Computing the Probability That a Random Variable Lies Within a Bounded Interval

#### Question

Compute $P\left(1 \lt X \lt 3 \right)$ given that the random variable $X$ has the probability density function

$$


\begin{aligned}\frac{1}{18}(𝑥^{2}−1),\, & 1≤𝑥≤4, \\ 0,\, & otherwise.\end{aligned}


$$

#### Explanation

If a continuous random variable $X$ has the probability density function $f(x),$ then

$$


P(a \lt X \lt b) = \int_a^b f(x) \, \textrm dx.


$$

So, in our case, we have

$$


\begin{aligned}𝑃(1<𝑋<3) & =∫_{31}^{}𝑓(𝑥)\,d𝑥 \\ & =∫_{31}^{}\frac{1}{18}(𝑥^{2}−1)\,d𝑥 \\ & =\frac{1}{18}∫_{31}^{}(𝑥^{2}−1)\,d𝑥 \\ & =\frac{1}{18}[\frac{1}{3}𝑥^{3}−𝑥]_{31}^{} \\ & =\frac{1}{18}([\frac{1}{3}(3)^{3}−(3)]−[\frac{1}{3}(1)^{3}−(1)]) \\ & =\frac{1}{18}([9−3]−[\frac{1}{3}−1]) \\ & =\frac{1}{18}(6+\frac{2}{3}) \\ & =\frac{1}{18}⋅\frac{20}{3} \\ & =\frac{10}{27}.\end{aligned}


$$

### Example: Computing the Probability That a Random Variable Lies Within an Unbounded Interval

#### Question

Compute $P\left(X \leq 3 \right)$ given that the random variable $X$ has the probability density function

$$


\begin{aligned}\frac{2𝑥}{45},\, & 2≤𝑥≤7, \\ 0,\, & otherwise.\end{aligned}


$$

#### Explanation

If a continuous random variable $X$ has the probability density function $f(x),$ then

$$


P(a \leq X \leq b) = \int_a^b f(x) \, \textrm dx.


$$

Since $f(x)$ is identical to zero for all $x \lt 2,$ we have

$$


\begin{aligned}𝑃(𝑋≤3) & =∫_{32}^{}𝑓(𝑥)\,d𝑥 \\ & =∫_{32}^{}\frac{2𝑥}{45}\,d𝑥 \\ & =[\frac{1}{45}\,𝑥^{2}]_{32}^{} \\ & =\frac{1}{45}(3^{2}−2^{2}) \\ & =\frac{1}{45}⋅5 \\ & =\frac{1}{9}.\end{aligned}


$$

### Example: Calculating Probabilities With Piecewise PDFs

#### Question

Compute $P\left(2 \leq X \leq 4 \right)$ given that the random variable $X$ has the probability density function

$$


\begin{aligned}\frac{1}{9}𝑥,\, & 0≤𝑥<3, \\ 𝑥−3, & 3≤𝑥≤4, \\ 0,\, & otherwise.\end{aligned}


$$

#### Explanation

If a continuous random variable $X$ has the probability density function $f(x),$ then

$$


P(a \leq X \leq b) = \int_a^b f(x) \, \textrm dx.


$$

So, in our case, we have

$$


\begin{aligned}𝑃(2≤𝑋≤4) & =∫_{42}^{}𝑓(𝑥)\,d𝑥 \\ & =∫_{32}^{}\frac{1}{9}𝑥\,d𝑥+∫_{43}^{}(𝑥−3)\,d𝑥 \\ & =[\frac{1}{18}𝑥^{2}]_{32}^{}+[\frac{1}{2}𝑥^{2}−3𝑥]_{43}^{} \\ & =\frac{1}{18}[3^{2}−2^{2}]+([\frac{1}{2}(4)^{2}−3(4)]−[\frac{1}{2}(3)^{2}−3(3)]) \\ & =\frac{5}{18}−4+\frac{9}{2} \\ & =\frac{14}{18} \\ & =\frac{7}{9}.\end{aligned}


$$
