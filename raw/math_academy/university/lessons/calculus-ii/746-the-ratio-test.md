# The Ratio Test

Source: https://www.mathacademy.com/topics/746?courseId=106
Topic ID: 746

## Prerequisites

- [Dividing Rational Expressions](../../../high-school/traditional/lessons/algebra-ii/436-dividing-rational-expressions.md)
- [Convergent and Divergent Infinite Series](./982-convergent-and-divergent-infinite-series.md)
- [Limits of Sequences With Factorials](./1089-limits-of-sequences-with-factorials.md)
- [Determining Limits of Sequences Using Relative Magnitudes](./1245-determining-limits-of-sequences-using-relative-magnitudes.md)

## Lesson

### Introduction

The **ratio test** can allow us to determine whether an infinite series converges or diverges, based on the limit of the absolute value of the ratio of consecutive terms.

Let the number $L\geq 0$ be defined as

$$


L = \lim_{n\rightarrow\infty}\left|\frac{a_{n+1}}{a_n}\right|.


$$

The ratio test states that:

- if $L<1,$ then the series is convergent

- if $L>1,$ then the series is divergent

- if $L=1,$ then the ratio test gives no conclusion about the convergence or divergence of the series

**Note:** There is some nice intuition behind the ratio test. Loosely speaking, we can think of the series as eventually looking similar to a geometric series whose common ratio has magnitude $L.$

- If $L<1,$ then the terms of the series decrease in magnitude, so it's intuitive that they would converge (rather than diverge).

- If $L>1,$ then the terms of the series increase in magnitude, so it's intuitive that they would diverge.

### Example: Applying the Ratio Test for Convergence

#### Question

Use the ratio test to show that $\displaystyle \sum_{n=1}^\infty \frac{n}{3^n}$ is convergent.

#### Explanation

Let $a_n = \dfrac{n}{3^n}.$ If we replace $n$ with $n+1,$ we get

$$


\begin{aligned} a_{n+1}= \frac{n+1}{3^{n+1}}= \frac{n+1}{3\cdot 3^n}. \end{aligned}


$$

Now that we have expressions for the consecutive terms $a_n$ and $a_{n+1},$ we can work out the necessary limit:

$$


\begin{aligned} L &=\lim_{n\to\infty}\left|\frac{a_{n+1}}{a_n} \right|\\[5pt] &=\lim_{n\to\infty}\left(\frac{n+1}{3\cdot 3^n} \div \frac{n}{3^n}\right)\\[5pt] &= \lim_{n\to\infty}\left(\frac{n+1}{3\cdot 3^n} \cdot \frac{3^n}{n}\right)\\[5pt] &= \lim_{n\to\infty}\left(\frac{n+1}{3n} \right)\\[5pt] &= \lim_{n\to\infty}\left(\frac{1}{3}\cdot \frac{n+1}{n}\right)\\[5pt] &= \frac{1}{3}\lim_{n\to\infty}\left(1 + \frac{1}{n}\right)\\[5pt] &=\frac{1}{3}\left(1 + 0\right)\\[5pt] &=\frac{1}{3}. \end{aligned}


$$

Note that we dropped the absolute value bars because the sequence is positive for all $n\geq 1.$

Since $L = \dfrac{1}{3}<1,$ we conclude that the series is convergent by the ratio test.

### Example: Applying the Ratio Test for Divergence

#### Question

Use the ratio test to show that $\displaystyle \sum_{n=1}^\infty \frac{(-1)^n\, n!}{3^n}$ is divergent.

#### Explanation

This is an example of an ****. The $(-1)^n$ causes the signs of the successive terms to alternate between positive and negative.

Let $a_n = \dfrac{(-1)^n\,n!}{3^n}.$ If we replace $n$ with $n+1,$ we get

$$


\begin{aligned} a_{n+1}= \dfrac{(-1)^{n+1}(n+1)!}{3^{n+1}}= \frac{(-1)^{n+1}\,(n+1)!}{3\cdot 3^n}. \end{aligned}


$$

Now that we have expressions for the consecutive terms $a_n$ and $a_{n+1},$ we can work out the necessary limit:

$$


\begin{aligned}  L &=\lim_{n\to\infty}\left|\frac{a_{n+1}}{a_n} \right|\\[5pt] &=\lim_{n\to\infty}\left| \dfrac{(-1)^{n+1}\,(n+1)!}{3\cdot 3^n} \div \dfrac{(-1)^n\,n!}{3^n}\right|\\[5pt] &=\lim_{n\to\infty}\left| \dfrac{(-1)^{n+1}\,(n+1)!}{3\cdot 3^n} \cdot \dfrac{3^n}{(-1)^n\,n!}\right|\\[5pt] &=\lim_{n\to\infty}\left|-\dfrac{n+1}{3}\right|\\[5pt] &=\dfrac 1 3\lim_{n\to\infty}\left(n+1\right)\\[5pt] &=\infty. \end{aligned}


$$

Since $L=\infty > 1,$ we conclude that the series is divergent by the ratio test.

### Example: Applying the Ratio Test in the Indeterminate Case

#### Question

Use the ratio test to determine whether the series $\displaystyle\sum_{n=1}^\infty \frac{1}{2n+1}$ is convergent or divergent.

#### Explanation

Let $a_n = \dfrac{1}{2n+1}.$ If we replace $n$ with $n+1,$ we get

$$


a_{n+1} = \frac{1}{2(n+1)+1}= \frac{1}{2n+3}.


$$

Now that we have expressions for the consecutive terms $a_n$ and $a_{n+1},$ we can work out the necessary limit:

$$


\begin{aligned}𝐿 & =\underset{𝑛→∞}{lim}\frac{𝑎_{𝑛+1}}{𝑎_{𝑛}} \\ & =\underset{𝑛→∞}{lim}\frac{𝑎_{𝑛+1}}{𝑎_{𝑛}} \\ & =\underset{𝑛→∞}{lim}\frac{1}{2𝑛+3}÷\frac{1}{2𝑛+1} \\ & =\underset{𝑛→∞}{lim}(\frac{1}{2𝑛+3}⋅\frac{2𝑛+1}{1}) \\ & =\underset{𝑛→∞}{lim}(\frac{2𝑛+1}{2𝑛+3}) \\ & =\underset{𝑛→∞}{lim}\frac{2+\frac{1}{𝑛}}{𝑛} \\ & =\frac{2}{2} \\ & =1.\end{aligned}


$$

Since $L=1,$ the ratio test gives ** about whether the series is convergent or divergent.

**** Although the ratio test gave no conclusion, the series $\displaystyle\sum_{n=1}^\infty \frac{1}{2n+1}$ is actually divergent.
