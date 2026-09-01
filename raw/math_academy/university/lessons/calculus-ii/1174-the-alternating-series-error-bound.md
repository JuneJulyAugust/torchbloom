# The Alternating Series Error Bound

Source: https://www.mathacademy.com/topics/1174?courseId=106
Topic ID: 1174

## Prerequisites

- [The Alternating Series Test](./747-the-alternating-series-test.md)

## Lesson

### Introduction

Suppose that we have an alternating series

$$


S = \sum_{n =1}^\infty b_n


$$

where $b_n = (-1)^n a_n$ or $b_n = (-1)^{n+1} a_n$ with $a_n \geq 0.$ Let's assume that the above series is convergent by the alternating series test.

The $N$th partial sum of this series is

$$


s_n = \sum_{n =1}^N b_n.


$$

How good an estimate of $S$ is the $n$th partial sum of $S?$

The **alternating series error bound** states that, for a convergent alternating series,

$$


|S- s_n|< |b_{n+1}|.


$$

In other words, the magnitude of the error of the $n$th partial sum is less than the magnitude of the $(n+1)$th term.

### Example: Finding the Alternating Series Error Bound for a Given Partial Sum

#### Question

Suppose that

$$


S = \displaystyle\sum\limits_{n = 1}^\infty {\dfrac{{{{( - 1)}^n}}}{{\sqrt[4]{{{n^5}}}}}}


$$

and that $s_2$ is the second partial sum of $S.$ According to the alternating series error bound, $|S-s_2| < k$ for some real number $k.$ Find the value of $k.$

#### Explanation

Let $a_n = \dfrac{1}{\sqrt[4]{n^5}}$ and $b_n= {\dfrac{{{{(- 1)}^n}}}{{\sqrt[4]{{{n^5}}}}}}.$ Then $a_n$ is positive and decreasing for $n\geq 1,$ and $a_n \to0$ as $n\to\infty.$ So, the series is convergent by the alternating series test.

Because our series is a convergent alternating series, the alternating series error bound applies. In particular, for the second partial sum, it states that

$$


|S - {s_2}| < |{b_3}| =\left| \dfrac{(-1)^{3}}{\sqrt[4]{3^5}} \right|=\dfrac{{1}}{\sqrt[4]{243}}.


$$

Therefore, $k=\dfrac{{1}}{\sqrt[4]{243}}.$

### Example: Determining the Values of N Such That the Error in the Nth Partial Sum Is Smaller Than a Given Number

#### Question

Given that

$$


S = \sum_{n=1}^\infty \dfrac {(-1)^n}{n}


$$

and that $s_i$ is the $i$th partial sum of $S,$ use the alternating series error bound to determine the values of $i$ such that $|S - s_{i}| < 0.001.$

#### Explanation

First, let $a_n =\dfrac{1}{n}$ and $b_n=\dfrac {(-1)^n}{n}.$ Then $a_n$ is decreasing for $n \geq 1$ and $a_n \to 0$ as $n \to \infty.$ So, the series is convergent by the alternating series test.

Because our series is a convergent alternating series, the alternating series error bound applies. In particular, for the $i$th partial sum, it states that

$$


|S - s_i| < |b_{i + 1}|.


$$

So, we require

$$


\begin{aligned}|𝑏_{𝑖+1}|=\frac{(−1)^{𝑖+1}}{𝑖+1} & ≤0.001 \\ \frac{1}{𝑖+1} & ≤0.001 \\ \frac{1}{𝑖+1} & ≤\frac{1}{1\,000} \\ 𝑖+1 & ≥1\,000 \\ 𝑖 & ≥999.\end{aligned}


$$
