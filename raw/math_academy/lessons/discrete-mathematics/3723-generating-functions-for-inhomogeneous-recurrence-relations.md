# Generating Functions for Inhomogeneous Recurrence Relations

Source: https://www.mathacademy.com/topics/3723?courseId=109
Topic ID: 3723

## Prerequisites

- [Sums of Infinite Geometric Series Given in Sigma Notation](./1020-sums-of-infinite-geometric-series-given-in-sigma-notation.md)
- [Generating Functions of Homogeneous Recurrence Relations](./3140-generating-functions-of-homogeneous-recurrence-relations.md)

## Lesson

### Introduction

A first-order linear **homogeneous** recurrence relation is a recurrence relation that takes the form

$$



a_n + P \cdot a_{n-1} = 0



$$

where $P$ is a nonzero constant.

For example, let's consider the following first-order recurrence relation:

$$



a_n -2 a_{n-1}= 0



$$

This equation is first-order homogeneous because the left-hand is a linear combination of $a_n$ and $a_{n-1},$ and the right-hand side is zero.

A first-order linear **inhomogeneous** recurrence relation is a recurrence relation that can be written as

$$



a_n + P \cdot a_{n-1} = f(n).



$$

The function $f(n)$ is sometimes called a **forcing function.**

For example, let's consider the following first-order recurrence relation:

$$



a_n -2 a_{n-1}= 2^n



$$

This equation is inhomogeneous because the right-hand side is $f(n) = 2^n,$ which is different from zero.

### Generating Functions for Inhomogeneous Recurrence Relations

Suppose we want to find the generating function for the sequence satisfying the inhomogeneous recurrence relation

$$



a_n-2a_{n-1}=2, \qquad a_0=1, \qquad n \ge 1.



$$

Since the equation is inhomogeneous, the method we used in the homogeneous case will not work. However, we can still find a closed-form solution.

Let's suppose that the generating function of our sequence is

$$



f(x) = \sum\limits_{n=0}^\infty a_n x^n.



$$

Next, we multiply both sides of the recurrence relation by $x^n.$ This gives

$$



a_nx^n -2a_{n−1}x^n =2 x^n.



$$

Now, if we sum this equation over all values of $n \geq 1,$ we get

$$



\sum\limits_{n=1}^\infty a_n x^n - \sum\limits_{n=1}^\infty 2a_{n−1}x^n = \sum\limits_{n=1}^\infty 2 x^n.\qquad (\ast)



$$

The idea now is to write each of the summations in equation $(\ast)$ terms of $f(x).$

- The first sum on the left-hand side is almost the same as $f(x).$ It's just missing the first term. Therefore,

- The second sum on the left-hand side has a mismatch between the indexes. To correct this, we can pull a single factor of $x$ outside the sum: Now, we can start the index from zero, which gives

- The sum on the right-hand side can be evaluated as geometric series:

Therefore, the equation $(\ast)$ can be rewritten as follows:

$$



\begin{aligned}(𝑓(𝑥)−1)−2𝑥𝑓(𝑥) & =\frac{2𝑥}{1−𝑥} \\ 𝑓(𝑥)(1−2𝑥)−1 & =\frac{2𝑥}{1−𝑥} \\ 𝑓(𝑥)(1−2𝑥) & =\frac{2𝑥}{1−𝑥}+1 \\ 𝑓(𝑥)(1−2𝑥) & =\frac{1+𝑥}{1−𝑥} \\ 𝑓(𝑥) & =\frac{1+𝑥}{(1−𝑥)(1−2𝑥)}\end{aligned}



$$

### Example: First-Order Inhomogeneous Recurrence Relations With Constant or Exponential Forcing

#### Question

Find the generating function for the sequence that satisfies the recurrence relation $a_n + 4a_{n−1}=(-2)^n$ with $a_0=1.$

#### Explanation

Let's denote the generating function of our sequence as

$$



f(x) = \sum\limits_{n=0}^\infty a_n x^n.



$$

We start by multiplying both sides of the recurrence relation by $x^n.$ This gives

$$



a_n x^n + 4a_{n−1}x^n = (-2)^n x^n.



$$

If we sum this over all values of $n \geq 1,$ we get

$$



\sum\limits_{n=1}^\infty a_n x^n + \sum\limits_{n=1}^\infty 4a_{n−1}x^n = \sum\limits_{n=1}^\infty (-2)^n x^n.



$$

Now, notice the following:

- $\displaystyle \sum\limits_{n=1}^\infty a_n x^n = \sum\limits_{n=0}^\infty a_n x^n - a_0 = f(x) - 1$

- $\displaystyle \sum\limits_{n=1}^\infty 4a_{n−1}x^n = 4x \sum\limits_{n=1}^\infty a_{n−1}x^{n-1} = 4x \sum\limits_{n=0}^\infty a_n x^n = 4x f(x)$

- $\displaystyle \sum\limits_{n=1}^\infty (-2)^n x^n = \sum\limits_{n=1}^\infty (-2x)^n = \dfrac{-2x}{1-(-2x)} = -\dfrac{2x}{1+2x}$

Therefore, our equation can be rewritten as follows:

$$



\begin{aligned}(𝑓(𝑥)−1)+4𝑥𝑓(𝑥) & =−\frac{2𝑥}{1+2𝑥} \\ 𝑓(𝑥)(1+4𝑥)−1 & =−\frac{2𝑥}{1+2𝑥} \\ 𝑓(𝑥)(1+4𝑥) & =1−\frac{2𝑥}{1+2𝑥} \\ 𝑓(𝑥)(1+4𝑥) & =\frac{1}{1+2𝑥} \\ 𝑓(𝑥) & =\frac{1}{(1+2𝑥)(1+4𝑥)}\end{aligned}



$$

### Example: First-Order Inhomogeneous Recurrence Relations With Linear Forcing

#### Question

Find the generating function for the sequence that satisfies the recurrence relation $a_n-a_{n−1}=1-3n$ with $a_0=2.$

**

#### Explanation

Let's denote the generating function of our sequence as

$$



f(x) = \sum\limits_{n=0}^\infty a_n x^n.



$$

We start by multiplying both sides of the recurrence relation by $x^n.$ This gives

$$



a_nx^n -a_{n−1}x^n =(1-3n) x^n.



$$

If we sum this over all values of $n \geq 1,$ we get

$$



\sum\limits_{n=1}^\infty a_n x^n - \sum\limits_{n=1}^\infty a_{n−1}x^n = \sum\limits_{n=1}^\infty (1-3n) x^n.



$$

Now, notice the following:

- $\displaystyle \sum\limits_{n=1}^\infty a_n x^n = \sum\limits_{n=0}^\infty a_n x^n - a_0 = f(x) - 2$

- $\displaystyle \sum\limits_{n=1}^\infty a_{n−1}x^n = x \sum\limits_{n=1}^\infty a_{n−1}x^{n-1} = x \sum\limits_{n=0}^\infty a_{n}x^n = x f(x)$

- $\displaystyle \sum\limits_{n=1}^\infty (1-3n) x^n = \sum\limits_{n=1}^\infty x^n -3 \sum\limits_{n=1}^\infty n x^n = \dfrac{x}{1-x}-\dfrac{3x}{(1-x)^2}$

Therefore, our equation can be rewritten as follows:

$$



\begin{aligned}(𝑓(𝑥)−2)−𝑥𝑓(𝑥) & =\frac{𝑥}{1−𝑥}−\frac{3𝑥}{(1−𝑥)^{2}} \\ 𝑓(𝑥)(1−𝑥)−2 & =\frac{−2𝑥−𝑥^{2}}{(1−𝑥)^{2}} \\ 𝑓(𝑥)(1−𝑥) & =\frac{−2𝑥−𝑥^{2}}{(1−𝑥)^{2}}+2 \\ 𝑓(𝑥)(1−𝑥) & =\frac{𝑥^{2}−6𝑥+2}{(1−𝑥)^{2}} \\ 𝑓(𝑥) & =\frac{𝑥^{2}−6𝑥+2}{(1−𝑥)^{3}}\end{aligned}



$$

### Example: Second-Order Inhomogeneous Recurrence Relations

#### Question

Consider the recurrence relation $a_n+a_{n−1}+a_{n-2}=1$ with $a_0=1$ and $a_1=0.$ Find the generating function of this recurrence relation.

#### Explanation

Let's denote the generating function of our sequence as

$$



f(x) = \sum\limits_{n=0}^\infty a_n x^n.



$$

We start by multiplying both sides of the recurrence relation by $x^n.$ This gives

$$



a_n x^n + a_{n−1}x^n + a_{n-2} x^n = x^n.



$$

If we sum this over all values of $n \geq 2,$ we get

$$



\sum\limits_{n=2}^\infty a_n x^n + \sum\limits_{n=2}^\infty a_{n−1}x^n + \sum\limits_{n=2}^\infty a_{n-2}x^n = \sum\limits_{n=2}^\infty x^n. \qquad (\ast)



$$

The idea now is to write each of the summations in equation $(\ast)$ terms of $f(x).$

- The first sum on the left-hand side is almost the same as $f(x).$ It's just missing the first two terms. Therefore,

$$



\displaystyle \sum\limits_{n=2}^\infty a_n x^n = \sum\limits_{n=0}^\infty a_n x^n - a_0 - a_1 x = f(x) - 1.



$$

- The second sum on the left-hand side has a mismatch between the indexes. To correct this, we can pull a single factor of $x$ outside the sum, as follows: Then, we recognize that the summation is almost $f(x),$ but the first term is missing. Therefore, we have

- For the third term, we can pull out a factor of $x^2$ to correct the mismatch of the indexes, which gives

$$



\displaystyle \sum\limits_{n=2}^\infty a_{n−2}x^n = x^2 \sum\limits_{n=2}^\infty a_{n−2}x^{n-2} = x^2 \sum\limits_{n=0}^\infty a_{n}x^n = x^2 f(x).



$$

- Finally, the right-hand side can be evaluated as a geometric series:

Therefore, our equation $(\ast)$ can be rewritten as follows:

$$



\begin{aligned}(𝑓(𝑥)−1)+𝑥(𝑓(𝑥)−1)+𝑥^{2}𝑓(𝑥) & =\frac{𝑥^{2}}{1−𝑥} \\ 𝑓(𝑥)(1+𝑥+𝑥^{2})−1−𝑥 & =\frac{𝑥^{2}}{1−𝑥} \\ 𝑓(𝑥)(1+𝑥+𝑥^{2}) & =\frac{𝑥^{2}}{1−𝑥}+1+𝑥 \\ 𝑓(𝑥)(1+𝑥+𝑥^{2}) & =\frac{1}{1−𝑥} \\ 𝑓(𝑥) & =\frac{1}{(1−𝑥)(1+𝑥+𝑥^{2})}\end{aligned}



$$
