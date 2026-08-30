# The Root Test

Source: https://www.mathacademy.com/topics/749?courseId=106
Topic ID: 749

## Prerequisites

- [Convergent and Divergent Infinite Series](./982-convergent-and-divergent-infinite-series.md)
- [Limits of Sequences](./1087-limits-of-sequences.md)
- [Combining the Rules of Exponents With Algebraic Expressions](../../../high-school/traditional/lessons/algebra-i/1417-combining-the-rules-of-exponents-with-algebraic-expressions.md)
- [Factorials in Variable Expressions](../../../high-school/traditional/lessons/geometry/3710-factorials-in-variable-expressions.md)

## Lesson

### Introduction

When the $n$th term $a_n$ of an infinite series involves $n$th powers, we can determine whether the series converges or diverges using the **root test**.

Suppose we have a series $\displaystyle \sum_{n =1} ^\infty a_n$ such that $a_n \geq 0$ for all $n \geq 1$. We define $L$ as the following limit:

$$


L = \lim_{n \to \infty}\sqrt [n] {a_n} = \lim_{n \to \infty}\left({a_n}\right)^{1/n}


$$

Then, the root test states the following:

- if $L < 1$, the series converges.

- if $L >1$ or $L = \infty$, the series diverges.

- if $L = 1$, the root test is inconclusive.

Let's use the root test to show that the following geometric series converges:

$$


\displaystyle \sum_{n=1}^\infty \dfrac {1 } {2^n}


$$

In this case, our sequence $a_n$ is defined as

$$


a_n = \dfrac{1}{2^n}, \qquad n\geq 1.


$$

To apply the root test, we calculate the limit of $\sqrt[n]{a_n}$ as $n\to\infty{:}$

$$


\begin{aligned}𝐿 & =\underset{𝑛→∞}{lim}\sqrt[√\frac{1}{2^{𝑛}}]{𝑛} \\ & =\underset{𝑛→∞}{lim}\frac{\sqrt[√1]{𝑛}}{\sqrt[√2^{𝑛}]{𝑛}} \\ & =\underset{𝑛→∞}{lim}\frac{1}{2} \\ & =\frac{1}{2}\end{aligned}


$$

Since $L=\dfrac12 < 1,$ our series converges by the root test.

Finally, when applying the root test, it's worth bearing the following limit facts in mind:

- $\displaystyle \lim_{n \to \infty} \sqrt [n] {a} = 1$ for $a > 0$

- $\displaystyle \lim_{n \to \infty} \sqrt [n] {n} = 1$

- $\displaystyle \lim_{n \to \infty} \sqrt [n] {\dfrac 1 {n!}} = 0$

### Example: Applying the Root Test to a Convergent Series

#### Question

Use the root test to show that the following series is convergent.

$$


\sum_{n=1}^\infty \dfrac {(7n)^n n} {(8n + 1) ^ n}


$$

#### Explanation

Suppose we have the series $\displaystyle \sum_{n =1} ^\infty a_n$ such that $a_n \geq 0$ for all $n \geq 1,$ and that $L$ is defined as

$$


L = \lim_{n \to \infty}\sqrt [n] {a_n} = \lim_{n \to \infty}\left({a_n}\right)^{1/n}.


$$

Then, the root test states the following:

- If $L\lt 1$, the series converges.

- If $L \gt 1$ or $L = \infty$, the series diverges.

- If $L = 1$, the root test is inconclusive.

We have the sequence $a_n,$ defined as

$$


a_n = \dfrac {(7n)^n n} {(8n + 1) ^ n}.


$$

To apply the root test, we find the limit of $\sqrt[n]{a_n}$ as $n\to\infty\mathbin{:}$

$$


\begin{aligned}𝐿 & =\underset{𝑛→∞}{lim}\sqrt[√𝑎_{𝑛}]{𝑛} \\ & =\underset{𝑛→∞}{lim}(𝑎_{𝑛})^{1/𝑛} \\ & =\underset{𝑛→∞}{lim}[\frac{(7𝑛)^{𝑛}𝑛}{(8𝑛+1)^{𝑛}}]^{1/𝑛} \\ & =\underset{𝑛→∞}{lim}\frac{7𝑛⋅\sqrt[√𝑛]{𝑛}}{8𝑛+1} \\ & =\underset{𝑛→∞}{lim}\frac{(\frac{7𝑛⋅\sqrt[√𝑛]{𝑛}}{𝑛})}{𝑛} \\ & =\underset{𝑛→∞}{lim}\frac{7\sqrt[√𝑛]{𝑛}}{(8+\frac{1}{𝑛})} \\ & =\frac{7⋅1}{8+0} \\ & =\frac{7}{8}\end{aligned}


$$

Note that we used the fact that

$$


\lim_{n\to\infty} \sqrt[n]{n}=1.


$$

Since $L =\dfrac{7}{8} \lt 1,$ the series converges by the root test.

### Example: Applying the Root Test in Divergent and Inconclusive Cases

#### Question

Use the root test to show that the following series is divergent.

$$


\sum_{n=1}^\infty \dfrac{n^45^n}{3^n}


$$

#### Explanation

Suppose we have the series $\displaystyle \sum_{n =1} ^\infty a_n$ such that $a_n \geq 0$ for all $n \geq 1,$ and that $L$ is defined as

$$


L = \lim_{n \to \infty}\sqrt [n] {a_n} = \lim_{n \to \infty}\left({a_n}\right)^{1/n}.


$$

Then, the root test states the following:

- If $L \lt 1$, the series converges.

- If $L \gt 1$ or $L = \infty$, the series diverges.

- If $L = 1$, the root test is inconclusive.

We have the sequence $a_n,$ defined as

$$


a_n = \dfrac{n^45^n}{3^n}.


$$

To apply the root test, we find the limit of $\sqrt[n]{a_n}$ as $n\to\infty\mathbin{:}$

$$


\begin{aligned}𝐿 & =\underset{𝑛→∞}{lim}\sqrt[√𝑎_{𝑛}]{𝑛} \\ & =\underset{𝑛→∞}{lim}(𝑎_{𝑛})^{1/𝑛} \\ & =\underset{𝑛→∞}{lim}(\frac{𝑛^{4}5^{𝑛}}{3^{𝑛}})^{1/𝑛} \\ & =\underset{𝑛→∞}{lim}(\frac{\sqrt[√𝑛^{4}]{𝑛}⋅5}{3}) \\ & =\frac{5}{3}\underset{𝑛→∞}{lim}\sqrt[√𝑛^{4}]{𝑛} \\ & =\frac{5}{3}⋅1^{4} \\ & =\frac{5}{3}\end{aligned}


$$

Note that we used the fact that

$$


\lim_{n\to\infty} \sqrt[n]{n} = 1.


$$

Since $L =\dfrac{5}{3} \gt 1,$ the series diverges by the root test.
