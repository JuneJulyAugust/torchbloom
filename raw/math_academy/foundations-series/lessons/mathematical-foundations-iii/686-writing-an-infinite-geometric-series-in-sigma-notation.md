# Writing an Infinite Geometric Series in Sigma Notation

Source: https://www.mathacademy.com/topics/686?courseId=136
Topic ID: 686

## Prerequisites

- [Infinite Series and Partial Sums](./981-infinite-series-and-partial-sums.md)

## Lesson

### Introduction

Suppose we want to write down the infinite geometric series

$$


S = 1+ \dfrac 1 2 + \dfrac 1 4 + \dfrac 1 8 + \dfrac{1}{16} + \dots


$$

in a compact way. We can express this using sigma notation with summation to infinity, as follows:

$$


S = \displaystyle\sum_{n = 1}^\infty a_n.


$$

Let us define $a_n.$ The common ratio for the given series is $r = \dfrac 1 2$ and the first term is $a_1 = 1.$ Therefore, we have

$$


\begin{aligned}𝑎_{𝑛} & =𝑎_{1}⋅𝑟^{𝑛−1} \\ & =(\frac{1}{2})^{𝑛−1} \\ & =(\frac{1}{2})^{𝑛}⋅(\frac{1}{2})^{−1} \\ & =2(\frac{1}{2})^{𝑛}.\end{aligned}


$$

Finally, the infinite geometric series can be written in sigma notation as

$$


S = \displaystyle\sum_{n =1}^\infty 2\left(\dfrac 1 2\right)^{n} .


$$

### Example: Expressing an Infinite Series Using Sigma Notation Given The First Few Terms

#### Question

Express the sum to infinity of the following geometric series using sigma notation:

$$


\dfrac{5}{3}-\dfrac{5}{9}+\dfrac{5}{27}-\dfrac{5}{81}+\cdots


$$

#### Explanation

The first term $a_1 = \dfrac{5}{3}$ and the second term $a_2 = - \dfrac{5}{9}.$ Using these two terms, we compute the common ratio:

$$


r = \frac{a_2}{a_1} = \frac{\left(-\dfrac{5}{9} \right)}{\left(\dfrac{5}{3} \right)} = - \dfrac{1}{3}.


$$

Therefore, the general term $a_n$ can be expressed as

$$


\begin{aligned}𝑎_{𝑛} & =𝑎_{1}(𝑟)^{𝑛−1} \\ & =\frac{5}{3}(−\frac{1}{3})^{𝑛−1} \\ & =\frac{5}{3}(−\frac{1}{3})^{−1}(−\frac{1}{3})^{𝑛} \\ & =(−5)(−\frac{1}{3})^{𝑛}.\end{aligned}


$$

Finally, the infinite geometric series can be written in sigma notation as

$$


\begin{aligned}\frac{5}{3}−\frac{5}{9}+\frac{5}{27}−\frac{5}{81}+⋯ & =\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}𝑎_{𝑛} \\ & =\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}(−5)(−\frac{1}{3})^{𝑛}.\end{aligned}


$$

### Example: Expressing an Infinite Series Using Sigma Notation Given Its First Term and Common Ratio

#### Question

Consider the sequence starting from $a_1=-20$ with the property $\dfrac{a_{n+1}}{a_n}=-\dfrac{1}{5}$ for all $n\geq 1.$ Write the sum to infinity of the terms of this sequence using sigma notation.

#### Explanation

Notice that the sequence is a geometric sequence since the ratio of any two successive terms is constant.

The first term of the sequence is $a_1 = - 20,$ and the common ratio is

$$


r = \dfrac{a_{n+1}}{a_n} = - \dfrac{1}{5}.


$$

Therefore, the general term $a_n$ can be expressed as

$$


\begin{aligned}𝑎_{𝑛} & =𝑎_{1}(𝑟)^{𝑛−1} \\ & =(−20)(−\frac{1}{5})^{𝑛−1} \\ & =(−20)(−\frac{1}{5})^{−1}(−\frac{1}{5})^{𝑛} \\ & =100(−\frac{1}{5})^{𝑛}.\end{aligned}


$$

Finally, the infinite geometric series can be written in sigma notation as

$$


\sum_{n=1}^\infty a_n=\sum_{n=1}^\infty 100\left(-\frac{1}{5}\right)^{n}.


$$
