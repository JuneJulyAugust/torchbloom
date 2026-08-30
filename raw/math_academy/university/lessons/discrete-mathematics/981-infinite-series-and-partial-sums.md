# Infinite Series and Partial Sums

Source: https://www.mathacademy.com/topics/981?courseId=109
Topic ID: 981

## Prerequisites

- [Finding the Sum of an Arithmetic Series](../../../high-school/integrated-math-honors/lessons/integrated-math-ii-honors/675-finding-the-sum-of-an-arithmetic-series.md)
- [Sums of Finite Geometric Series Given in Sigma Notation](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/690-sums-of-finite-geometric-series-given-in-sigma-notation.md)

## Lesson

### Introduction

Any series with infinitely many terms is called an **infinite series**. Infinite series are usually denoted using sigma notation as

$$



\sum_{n=1}^\infty a_n,



$$

where each $a_n$ represents an individual term of the sequence that makes up the series.

For example, the **harmonic series** below is an example of an infinite series:

$$



\sum_{n=1}^\infty \dfrac{1}{n} = \dfrac{1}{1}+\dfrac{1}{2}+\dfrac{1}{3}+\cdots + \dfrac 1 k +\cdots



$$

A **partial sum** $s_k$ of an infinite series is a sum of the first $k$ terms. For example, the first, second, third, and fourth partial sums, denoted $s_1,$ $s_2,$ $s_3,$ and $s_4$ respectively, of the harmonic series are

$$



\begin{aligned}𝑠_{1}=\underset{\underset{𝑛=1}{∑}}{\overset{}{1}}\frac{1}{𝑛} & =\frac{1}{1}=1 \\ 𝑠_{2}=\underset{\underset{𝑛=1}{∑}}{\overset{}{2}}\frac{1}{𝑛} & =\frac{1}{1}+\frac{1}{2}=\frac{3}{2} \\ 𝑠_{3}=\underset{\underset{𝑛=1}{∑}}{\overset{}{3}}\frac{1}{𝑛} & =\frac{1}{1}+\frac{1}{2}+\frac{1}{3}=\frac{11}{6} \\ 𝑠_{4}=\underset{\underset{𝑛=1}{∑}}{\overset{}{4}}\frac{1}{𝑛} & =\frac{1}{1}+\frac{1}{2}+\frac{1}{3}+\frac{1}{4}=\frac{25}{12}.\end{aligned}



$$

### Example: Finding the First Partial Sums of an Infinite Series

#### Question

Find the first, second, and third partial sums of the series

$$



\sum_{n=1}^\infty \dfrac 1 {n^2+1} .



$$

#### Explanation

Let's start by calculating the first three terms:

$$



\begin{aligned}𝑎_{1} & =\frac{1}{1^{2}+1}=\frac{1}{2} \\ 𝑎_{2} & =\frac{1}{2^{2}+1}=\frac{1}{5} \\ 𝑎_{3} & =\frac{1}{3^{2}+1}=\frac{1}{10}.\end{aligned}



$$

Therefore, the first, second, and third partial sums are

$$



\begin{aligned}𝑠_{1} & =\frac{1}{2} \\ 𝑠_{2} & =\frac{1}{2}+\frac{1}{5}=\frac{7}{10} \\ 𝑠_{3} & =\frac{1}{2}+\frac{1}{5}+\frac{1}{10}=\frac{8}{10}.\end{aligned}



$$

### Example: Finding a Partial Sum of an Infinite Arithmetic Series

#### Question

Find the twelfth partial sum of the series $\displaystyle \sum_{n=1}^\infty (2n-1).$

#### Explanation

Let $a_n = 2n-1.$ If we compute the first few terms, we get

$$



\begin{aligned}𝑎_{1} & =2(1)−1=1 \\ 𝑎_{2} & =2(2)−1=3 \\ 𝑎_{3} & =2(3)−1=5,\end{aligned}



$$

and we notice that this is an arithmetic sequence with common difference $d=2$ and first term $a_1 = 1.$

We can compute the $k$th partial sum of an arithmetic series using the formula

$$



s_k = \dfrac{k}{2}(a_1+a_k).



$$

Since $a_{12} = 2(12)-1 = 23,$ we get

$$



s_{12} =\dfrac{12}{2}(1+23) = 144.



$$

So the twelfth partial sum of $\displaystyle \sum_{n=1}^\infty (2n-1)$ is equal to $144.$

### Example: Finding a General Partial Sum of an Infinite Arithmetic Series

#### Question

Find the $k$th partial sum of the series $\displaystyle \sum_{n=1}^\infty (6-5n).$

#### Explanation

Let $a_n = 6-5n.$ If we compute the first few terms, we get

$$



\begin{aligned}𝑎_{1} & =6−5(1)=1 \\ 𝑎_{2} & =6−5(2)=−4 \\ 𝑎_{3} & =6−5(3)=−9,\end{aligned}



$$

and we see that this is an arithmetic sequence with common difference $d=-5$ and $a_1=1.$

We can compute the $k$th partial sum of an arithmetic series using the formula

$$



s_k = \dfrac{k}{2}(a_1+a_k).



$$

Since $a_{k} = 6-5k,$ we get

$$



\begin{aligned}𝑠_{𝑘} & =\frac{𝑘}{2}(1+6−5𝑘) \\ & =\frac{𝑘}{2}(7−5𝑘).\end{aligned}



$$

### Example: Finding a Partial Sum of an Infinite Geometric Series

#### Question

Find the fifth partial sum of the series $\displaystyle \sum_{n=1}^\infty 24 \left(\dfrac{1}{2}\right)^n.$

#### Explanation

Let $a_n = 24 \left(\dfrac{1}{2}\right)^n.$ We note that this is a geometric sequence with $r=\dfrac 1 2$ and first term given by

$$



a_1 = 24\cdot \dfrac 1 2 = 12.



$$

The $k$th partial sum of a geometric series is given by

$$



s_k = a_1\left(\dfrac{1-r^k}{1-r}\right).



$$

Therefore, the fifth partial sum is

$$



\begin{aligned}𝑠_{5} & =12⋅\frac{1−(\frac{1}{2})^{5}}{2} \\ & =12⋅\frac{1−\frac{1}{32}}{32} \\ & =24⋅(1−\frac{1}{32}) \\ & =24⋅(\frac{31}{32}) \\ & =\frac{93}{4}.\end{aligned}



$$
