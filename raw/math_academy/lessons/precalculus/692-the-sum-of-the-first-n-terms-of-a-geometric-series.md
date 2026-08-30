# The Sum of the First N Terms of a Geometric Series

Source: https://www.mathacademy.com/topics/692?courseId=43
Topic ID: 692

## Prerequisites

- [The Sum of a Finite Geometric Series](./1016-the-sum-of-a-finite-geometric-series.md)

## Lesson

### Introduction

Suppose we want to determine a formula for the sum $S_N$ for the first $N$ terms of a geometric series, knowing that the common ratio is $r=3$ and that the first term is $a_1=2.$ The sum $S_N$ is given by the formula

$$


S_N = \dfrac {a_1(1 - r ^ N)}{1 - r}.


$$

Plugging the values $r=3$ and $a_1=2$ into the formula for above, we get a formula for the sum of the first $N$ terms of this geometric series:

$$


\begin{aligned}𝑆_{𝑁} & =\frac{2(1−3^{𝑁})}{1−3} \\ & =−\frac{2}{2}(1−3^{𝑁}) \\ & =3^{𝑁}−1\end{aligned}


$$

### Example: Finding the Formula for the Sum of a Geometric Series Given the First Term and Common Ratio

#### Question

What is the sum of the first $N$ terms of a geometric series if the first term is $-3$ and the common ratio is $2?$

#### Explanation

The sum of the first $N$ terms of a geometric series can be determined by the formula

$$


S_N =\dfrac{a_1(1-r^N)}{1-r}.


$$

In this case, $a_1= -3$ and $r = 2.$ Therefore, we have

$$


\begin{aligned}𝑆_{𝑁} & =\frac{−3(1−2^{𝑁})}{1−2} \\ & =\frac{(−3)}{(−1)}(1−2^{𝑁}) \\ & =3(1−2^{𝑁}).\end{aligned}


$$

### Example: Finding the Formula for the Sum of a Geometric Series Given the First Few Terms

#### Question

What is the sum of the first $N$ terms of the geometric series $2+8+32+\cdots \:?$

#### Explanation

First, we determine the common ratio $r$ for this geometric series:

$$


\begin{aligned}𝑟 & =\frac{𝑎_{2}}{𝑎_{1}} \\ & =\frac{8}{2} \\ & =4\end{aligned}


$$

The sum of the first $N$ terms of a geometric series can be determined by the formula

$$


S_N = \dfrac{a_1 (1-r^N) }{1-r}.


$$

In this case, $a_1=2$ and $r=4.$ Substituting these values into the formula for $S_N$ gives the following:

$$


\begin{aligned}𝑆_{𝑁} & =\frac{𝑎_{1}(1−𝑟^{𝑁})}{1−𝑟} \\ & =\frac{2(1−4^{𝑁})}{1−4} \\ & =\frac{2(1−4^{𝑁})}{(−3)} \\ & =−\frac{2}{3}(1−4^{𝑁}) \\ & =\frac{2}{3}(4^{𝑁}−1)\end{aligned}


$$

### Example: Finding the Formula for the Sum of a Geometric Series Given an Arbitrary Term and the Common Ratio

#### Question

What is the sum of the first $N$ terms of a geometric series if the $3$rd term is $18$ and the common ratio is $3?$

#### Explanation

We use the formula for the $n$th term of a geometric sequence to determine $a_1\mathbin{:}$

$$


\begin{aligned}𝑎_{𝑛} & =𝑎_{1}𝑟^{𝑛−1} \\ 18 & =𝑎_{1}⋅3^{(3−1)} \\ 18 & =9𝑎_{1} \\ 𝑎_{1} & =2\end{aligned}


$$

The sum of the first $N$ terms of a geometric series can be determined by the formula

$$


S_N = \dfrac{a_1 (1-r^N) }{1-r} .


$$

In this case, $a_1=2$ and $r=3.$ Substituting our values into the formula for $S_N$ gives

$$


\begin{aligned}𝑆_{𝑁} & =\frac{2(1−3^{𝑁})}{1−3} \\ & =−\frac{2}{2}(1−3^{𝑁}) \\ & =3^{𝑁}−1.\end{aligned}


$$
