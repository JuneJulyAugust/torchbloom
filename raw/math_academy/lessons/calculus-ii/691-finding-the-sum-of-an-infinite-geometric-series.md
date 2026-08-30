# Finding the Sum of an Infinite Geometric Series

Source: https://www.mathacademy.com/topics/691?courseId=106
Topic ID: 691

## Prerequisites

- [Infinite Series and Partial Sums](./981-infinite-series-and-partial-sums.md)

## Lesson

### Introduction

The sum $S_\infty$ of an infinite geometric series with first term $a_1$ and common ratio $r$ can be computed using the formula

$$


S_\infty = \dfrac{a_1}{1-r}, \qquad |r| < 1.


$$

Note that $|r| < 1$ is a very important condition for the sum to exist. If the condition $|r|<1$ is *not* satisfied, then the formula does *not* work!

For example, suppose we want to calculate the sum of the infinite geometric series

$$


3 + 1 + \dfrac 1 3 + \dfrac 1 9 + \dfrac{1}{27} + \cdots\,.


$$

The first term is $a_1=3,$ and the common ratio is $r = \dfrac{a_2}{a_1} = \dfrac{1}{3}.$ Indeed, we have $|r|<1.$ Therefore, the sum is

$$


\begin{aligned}𝑆_{∞} & =\frac{𝑎_{1}}{1−𝑟} \\ & =\frac{3}{(1−\frac{1}{3})} \\ & =\frac{3}{(\frac{2}{3})} \\ & =3(\frac{3}{2}) \\ & =\frac{9}{2}.\end{aligned}


$$

Therefore, we conclude that

$$


3 + 1 + \dfrac 1 3 + \dfrac 1 9 + \dfrac{1}{27} + \cdots = \dfrac{9}{2}.


$$

### Example: Calculating the Sum to Infinity of a Geometric Series Expressed Using Fractions

#### Question

Calculate the sum to infinity of the geometric series $1 - \dfrac{1}{4} + \dfrac{1}{16} - \dfrac{1}{64} + \dots.$

#### Explanation

The sum to infinity $S_\infty$ of a geometric series is given by the formula

$$


S_\infty = \dfrac{a_1}{1-r}, \qquad |r| < 1,


$$

where $a_1$ is the first term and $r$ is the common ratio.

For the given geometric series, the first term is $a_1 = 1$ and the common ratio is

$$


r = \dfrac{a_2}{a_1} = \frac{\left(-\dfrac{1}{4}\right)}{1} = - \dfrac{1}{4}.


$$

So, using the formula, we find that the sum to infinity is

$$


\begin{aligned}𝑆_{∞} & =\frac{𝑎_{1}}{1−𝑟} \\ & =\frac{1}{1−(−\frac{1}{4})} \\ & =\frac{1}{(\frac{5}{4})} \\ & =\frac{4}{5}.\end{aligned}


$$

### Example: Calculating the Sum to Infinity of a Geometric Series Expressed Using Decimals

#### Question

Calculate the sum to infinity of the geometric series $0.25 + 0.125 + 0.062\ 5 + 0.031\ 25 + \dots.$

#### Explanation

The sum to infinity $S_\infty$ of a geometric series is given by the formula

$$


S_\infty = \dfrac{a_1}{1-r}, \qquad |r| < 1,


$$

where $a_1$ is the first term and $r$ is the common ratio.

For the given geometric series, the first term is $a_1 = 0.25$ and the common ratio is

$$


r = \dfrac{a_2}{a_1} = \frac{0.125}{0.25} = 0.5.


$$

So, using the formula, we find that the sum to infinity is

$$


\begin{aligned}𝑆_{∞} & =\frac{𝑎_{1}}{1−𝑟} \\ & =\frac{0.25}{1−0.5} \\ & =\frac{0.25}{0.5} \\ & =0.5.\end{aligned}


$$

### Example: Calculating the Sum to Infinity of a Geometric Series Given Two of Its Terms

#### Question

Consider the infinite geometric sequence that has a first term equal to $4$ and a fourth term equal to $\dfrac{1}{16}.$ What is the sum to infinity of the terms of this sequence?

#### Explanation

The sum to infinity $S_\infty$ of a geometric series is given by the formula

$$


S_\infty = \dfrac{a_1}{1-r}, \qquad |r| < 1,


$$

where $a_1$ is the first term and $r$ is the common ratio.

From the question statement we have $a_1=4$ and $a_4=\dfrac{1}{16}.$ We can find the common ratio using the following formula:

$$


r^{n-m} = \dfrac{a_n}{a_m}


$$

Substituting the known information into the above gives:

$$


\begin{aligned}𝑟^{4−1} & =\frac{(\frac{1}{16})}{16} \\ 𝑟^{3} & =\frac{1}{64} \\ 𝑟^{3} & =(\frac{1}{4})^{3} \\ 𝑟 & =\frac{1}{4}\end{aligned}


$$

So, using the formula, we find that the sum to infinity is

$$


\begin{aligned}𝑆_{∞} & =\frac{𝑎_{1}}{1−𝑟} \\ & =\frac{4}{(1−\frac{1}{4})} \\ & =\frac{4}{(\frac{3}{4})} \\ & =4(\frac{4}{3}) \\ & =\frac{16}{3}.\end{aligned}


$$

### Justification of the Formula

We've been using the following formula for the sum to infinity of a geometric series with first term $a_1$ and common ratio $r\mathbin{:}$

$$


S_\infty = \dfrac{a_1}{1-r}, \qquad |r| < 1


$$

To see where this formula comes from, first, we remember the formula for the sum of the first $n$ terms of a geometric series is given by

$$


S_n = a_1 \cdot \dfrac {1 - r ^ n} {1 - r}.


$$

Notice that if $|r| < 1$ then $r^n\to 0$ as $n\to\infty.$ Therefore, as $n\to\infty,$ we have:

$$


\begin{aligned}𝑆_{𝑛} & →𝑎_{1}⋅\frac{1−0}{1−𝑟} \\ & =𝑎_{1}⋅\frac{1}{1−𝑟} \\ & =\frac{𝑎_{1}}{1−𝑟} \\ & =𝑆_{∞}\end{aligned}


$$
