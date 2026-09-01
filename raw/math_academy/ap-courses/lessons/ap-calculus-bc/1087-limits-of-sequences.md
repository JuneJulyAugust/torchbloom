# Limits of Sequences

Source: https://www.mathacademy.com/topics/1087?courseId=21
Topic ID: 1087

## Prerequisites

- [Limits at Infinity and Horizontal Asymptotes of Rational Functions](../ap-calculus-ab/1903-limits-at-infinity-and-horizontal-asymptotes-of-rational-functions.md)
- [Introduction to Sequences](../../../high-school/traditional/lessons/algebra-i/2271-introduction-to-sequences.md)

## Lesson

### Introduction

Let's consider the sequence $a_n,$ given by

$$


a_n = \dfrac {n^3 + 5 n}{2 n^3 - n^2}, \qquad\ n\geq 1,


$$

and suppose that we want to determine the **limit of the sequence** $a_n.$ In the context of sequences, this means to work out $\displaystyle\lim_{n\to\infty} a_n.$

Finding the limit of a rational sequence $a_n$ is very similar to finding the horizontal asymptotes of a rational function. We divide the numerator and the denominator by the variable part of the dominant term in the denominator.

In our case, the variable part of the dominant term in the denominator is $n^3,$ so we divide the numerator and denominator by $n^3$ and get

$$


\begin{aligned}\underset{𝑛→∞}{lim}𝑎_{𝑛} & =\underset{𝑛→∞}{lim}\frac{𝑛^{3}+5𝑛}{2𝑛^{3}−𝑛^{2}} \\ & =\underset{𝑛→∞}{lim}\frac{(\frac{𝑛^{3}}{𝑛^{3}}+\frac{5𝑛}{𝑛^{3}})}{𝑛^{3}} \\ & =\underset{𝑛→∞}{lim}\frac{(1+\frac{5}{𝑛^{2}})}{𝑛^{2}} \\ & =\frac{1+0}{2−0} \\ & =\frac{1}{2}.\end{aligned}


$$

Since the finite limit exists, we say that the sequence **converges** and its limit is $\dfrac 1 2.$

If the limit of a sequence does *not* exist, then we say that the sequence **diverges**.

### Example: Determining the Limit of a Convergent Rational Sequence

#### Question

Does the sequence $a_n = \dfrac {3 n ^ 5 - n} {5 n ^ 6 - n}$ for $n\geq 1$ converge or diverge? If the sequence converges, what is its limit?

#### Explanation

To determine whether the sequence converges or diverges, we need to determine the limit of the sequence as $n$ approaches infinity:

$$


\lim_{n \to \infty} a_n = \lim_{n \to \infty}\dfrac {3 n ^ 5 - n} {5 n ^ 6 - n}


$$

The dominant term in the denominator is $5n^6,$ so we divide the numerator and the denominator by $n^6$ and get

$$


\begin{aligned}\underset{𝑛→∞}{lim}\frac{3𝑛^{5}−𝑛}{5𝑛^{6}−𝑛} & =\underset{𝑛→∞}{lim}\frac{(\frac{3𝑛^{5}}{𝑛^{6}}−\frac{𝑛}{𝑛^{6}})}{𝑛^{6}} \\ & =\underset{𝑛→∞}{lim}\frac{(\frac{3}{𝑛}−\frac{1}{𝑛^{5}})}{𝑛} \\ & =\frac{0−0}{5−0} \\ & =0.\end{aligned}


$$

Since the limit exists, the sequence converges, and its limit is $0.$

### Example: Identifying Divergent Sequences

#### Question

Which of the following sequences diverge?

1. $a_n = \dfrac{1}{n^2}$ for $n \geq 1$

2. $a_n = \dfrac{n^4}{2n^3+1}$ for $n \geq 1$

3. $a_n = \dfrac {3 n ^ 5 + 7} {5 n ^ 4 - 3 n ^ 3}$ for $n\geq 1?$

#### Explanation

Let's analyze each sequence in turn. We need to calculate the limit of each sequence as $n$ approaches at infinity.

- In sequence I, the limit is The limit exists, so the sequence converges.

- In sequence II, the dominant term in the denominator is $2n^3,$ so we divide the numerator and the denominator by $n^3$ and get The limit does not exist, so the sequence diverges.

- In sequence III, the dominant term in the denominator is $5n^4,$ so we divide the numerator and the denominator by $n^4$ and get The limit does not exist, so the sequence diverges.

In conclusion, sequences II and III diverge.

### Example: Finding the Limit of a Factored Rational Sequence

#### Question

What is the limit of the sequence $a_n = \dfrac {n(3n-7)} {(3n-1)(3n+1)}$ for $n\geq 1?$

#### Explanation

First, we multiply out the numerator and denominator of the sequence and get

$$


a_n=\dfrac {n(3n-7)} {(3n-1)(3n+1)}=\dfrac {3 n ^ 2 - 7 n} {9 n ^ 2-1}.


$$

So to find the limit, we will need to compute

$$


\lim_{n \to \infty} a_n = \lim_{n \to \infty} \dfrac {3 n ^ 2 - 7 n} {9 n ^ 2-1}.


$$

The dominant term in the denominator is $n^2,$ so we divide the numerator and the denominator by $n^2$ and get

$$


\begin{aligned}\underset{𝑛→∞}{lim}\frac{3𝑛^{2}−7𝑛}{9𝑛^{2}−1} & =\underset{𝑛→∞}{lim}\frac{(\frac{3𝑛^{2}}{𝑛^{2}}−\frac{7𝑛}{𝑛^{2}})}{𝑛^{2}} \\ & =\underset{𝑛→∞}{lim}\frac{(3−\frac{7}{𝑛})}{𝑛} \\ & =\frac{3−0}{9−0} \\ & =\frac{1}{3}.\end{aligned}


$$

Consequently, the sequence converges and its limit is $\dfrac 1 3.$
