# Determining Convergence Parameters for Infinite Series

Source: https://www.mathacademy.com/topics/3858?courseId=21
Topic ID: 3858

## Prerequisites

- [Convergence of Geometric Series](./684-convergence-of-geometric-series.md)
- [The Alternating Series Test](./747-the-alternating-series-test.md)
- [Harmonic Series and p-Series](./860-harmonic-series-and-p-series.md)

## Lesson

### Introduction

Let's remind ourselves of some convergence tests for infinite series:

- The $p$-series test states that is convergent for $p > 1.$

- The geometric series is convergent for $|r| < 1.$

We often wish to determine some parameter values that cause two series to converge simultaneously.

As an example, let's consider the following series:

$$


\sum_{n=1}^\infty \dfrac{1}{n^{3p+2}}, \qquad \displaystyle \sum_{n=1}^\infty \dfrac{1}{n^{p-1}}


$$

We wish to find the values of $p$ for which *both* series converge, The idea is to examine the convergence behavior of each series individually and then find the intersection of the solutions.

Notice that both series are $p$-series. Therefore, we will use the $p$-series test on both series:

- For the first series to converge, we require

- For the second series to converge, we require

Finding the intersection of the two solutions gives

$$


\left(-\dfrac13,\infty\right) \cap (2, \infty) = (2, \infty).


$$

Therefore, both series converge for $p \in (2, \infty).$

### Example: Determining Convergence Parameters for Multiple p-Series

#### Question

For which values of $p$ is the following sum convergent?

$$


\sum_{n=1}^\infty \dfrac{1}{n^{2p+1}}+\displaystyle \sum_{n=1}^\infty \dfrac{1}{n^{8-p}}


$$

#### Explanation

The sum is convergent if both series are individually convergent.

For the first series to be convergent, we require

$$


2p+1 > 1\quad\Longrightarrow\quad p\in (0,\infty).


$$

For the second series to be convergent, we require

$$


8-p> 1\quad\Longrightarrow\quad p\in (-\infty, 7).


$$

Finding the intersection of the two solutions gives

$$


(0,\infty) \cap (-\infty, 7) = (0,7).


$$

Therefore, $0 < p < 7.$

### Example: Determining Convergence Parameters for Geometric and p-Series

#### Question

For what values of $p$ will both $\displaystyle \sum_{n=1}^{\infty} \left(\dfrac{2p}{3}\right)^{n}$ and $\displaystyle \sum_{n=1}^{\infty} \left(\dfrac{3}{2n}\right)^{p}$ converge?

#### Explanation

Let's examine each of our series in turn:

- The first series is a geometric series with common ratio $r=\dfrac{2p}{3}.$ For convergence, we require $|r| \lt 1.$ So, this first series converges for

- The second series is a $p$-series, and converges for $p \gt 1.$

For both series to converge, we need both of the following inequalities to be satisfied:

$$


\begin{aligned}−\frac{3}{2}<𝑝<\frac{3}{2} \\ 𝑝>1\end{aligned}


$$

Therefore, both series converge provided that $1 \lt p \lt \dfrac 3 2.$

### Alternating P-Series

Recall that the alternating series test states that if $a_n$ is a positive, decreasing sequence, and $a_n\to 0$ as $n\to\infty,$ then the alternating series

$$


\sum_{n=1}^{\infty} (-1)^n a_n \qquad\textrm{and}\qquad \sum_{n=1}^{\infty} (-1)^{n+1} a_n


$$

are convergent.

Now, since the sequence

$$


a_n = \dfrac{1}{n^p}, \qquad n\geq 1


$$

is positive, decreasing, and $a_n\to0$ as $n\to\infty$ for $p>0,$ the alternating series test tells us that the **alternating $p$-series**

$$


\sum_{n=1}^{\infty} \dfrac{(-1)^n}{n^p} \qquad\textrm{and}\qquad \sum_{n=1}^{\infty} \dfrac{(-1)^{n+1}}{n^p}


$$

are convergent for $p > 0.$

### Example: Determining Convergence Parameters for Alternating, Geometric, and p-Series

#### Question

For what values of $p$ will both $\displaystyle \sum_{n=1}^{\infty} \dfrac{(-1)^n}{n^{p+1}}$ and $\displaystyle \sum_{n=1}^{\infty} (p+1)^n$ converge?

#### Explanation

Let's examine each of our series in turn:

- The first series is an alternating $p$-series and converges for

- The second series is a geometric series with common ratio $r = p+1.$ For convergence, we require $|r| < 1.$ So, this series converges for

For both series to converge, we need both of the following inequalities to be satisfied:

$$


\begin{aligned}𝑝>−1 \\ −2<𝑝<0\end{aligned}


$$

Therefore, both series converge provided that $-1 < p < 0.$
