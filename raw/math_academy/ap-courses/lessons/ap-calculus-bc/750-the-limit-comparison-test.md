# The Limit Comparison Test

Source: https://www.mathacademy.com/topics/750?courseId=21
Topic ID: 750

## Prerequisites

- [Dividing Rational Expressions](../../../high-school/traditional/lessons/algebra-ii/436-dividing-rational-expressions.md)
- [The Comparison Test](./745-the-comparison-test.md)

## Lesson

### Introduction

The **limit comparison test** states that if $a_n$ and $b_n$ are both positive, and

$$


\lim_{n\rightarrow\infty} \frac{a_n}{b_n} = L,


$$

where $L$ is positive and finite, then the series $\displaystyle\sum_{n=1}^\infty a_n$ and $\displaystyle\sum_{n=1}^\infty b_n$ either *both* converge or *both* diverge.

Intuitively, the limit comparison test states that if the ratio of the two series' terms approaches a positive, constant value, both series must share the same convergence behavior.

The limit comparison test is particularly useful when comparing a series with an unknown convergence behavior to a simpler series with known convergence properties, such as a geometric or $p$-series.

Let's take a look at a concrete example.

### A Concrete Example

Let's use the limit comparison test to determine whether the following series converges or diverges:

$$


\sum_{n=1}^\infty \dfrac{1}{n + 2}


$$

This looks a bit like the diverging $p$-series $\displaystyle\sum_{n=1}^\infty \dfrac{1}{n}.$ However, we cannot use the comparison test because

$$


\dfrac{1}{n + 2} < \dfrac{1}{n}.


$$

Let's instead try the limit comparison test. Let

$$


a_n = \dfrac{1}{n + 2}, \qquad b_n = \dfrac{1}{n}.


$$

Computing the limit of the ratio, we get

$$


\begin{aligned}\underset{𝑛→∞}{lim}\frac{𝑎_{𝑛}}{𝑏_{𝑛}} & =\underset{𝑛→∞}{lim}\frac{1}{𝑛+2}÷\frac{1}{𝑛} \\ & =\underset{𝑛→∞}{lim}\frac{𝑛}{𝑛+2} \\ & =\underset{𝑛→∞}{lim}\frac{(\frac{𝑛}{𝑛})}{𝑛} \\ & =\underset{𝑛→∞}{lim}\frac{1}{(1+\frac{2}{𝑛})} \\ & =\frac{1}{1+0} \\ & =1.\end{aligned}


$$

Since $a_n$ and $b_n$ are both positive and $\displaystyle\lim_{n\rightarrow\infty} \frac{a_n}{b_n} = 1$ is positive and finite, we can use the limit comparison test.

So, since $\displaystyle\sum_{n=1}^\infty b_n$ diverges, then $\displaystyle\sum_{n=1}^\infty a_n$ diverges as well. Therefore, the series $\displaystyle \sum_{n=1}^\infty \dfrac{1}{n + 2}$ diverges.

### Example: Applying the Limit Comparison Test for Divergence

#### Question

Given the sequences $a_n = \dfrac{2n^3-n^2}{4n^4+n}$ and $b_n = \dfrac{1}{n},$ calculate $\displaystyle L = \lim_{n\to\infty}\dfrac{a_n}{b_n}$ and determine whether $\displaystyle\sum_{n=1}^\infty a_n$ converges or diverges.

#### Explanation

The limit comparison test states that if $a_n$ and $b_n$ are both positive, and

$$


\lim_{n\rightarrow\infty} \frac{a_n}{b_n} = L,


$$

where $L$ is positive and finite, then the series $\displaystyle\sum_{n=1}^\infty a_n$ and $\displaystyle\sum_{n=1}^\infty b_n$ either ** converge or ** diverge.

The given series looks as though it will behave like the divergent series

$$


\displaystyle \sum_{n=1}^\infty \dfrac{2n^3}{4n^4} = \dfrac 2 4\sum_{n=1}^\infty \dfrac{n^3}{n^4} = \dfrac 1 2\sum_{n=1}^\infty \dfrac{1}{n}.


$$

So, we let

$$


a_n = \dfrac{2n^3 - n^2}{4n^4+n}, \qquad b_n = \dfrac{1}{n}.


$$

Computing the limit of the ratio, we get

$$


\begin{aligned}\underset{𝑛→∞}{lim}\frac{𝑎_{𝑛}}{𝑏_{𝑛}} & =\underset{𝑛→∞}{lim}(\frac{2𝑛^{3}−𝑛^{2}}{4𝑛^{4}+𝑛}÷\frac{1}{𝑛}) \\ & =\underset{𝑛→∞}{lim}(\frac{2𝑛^{3}−𝑛^{2}}{4𝑛^{4}+𝑛}⋅𝑛) \\ & =\underset{𝑛→∞}{lim}(\frac{2𝑛^{4}−𝑛^{3}}{4𝑛^{4}+𝑛}) \\ & =\underset{𝑛→∞}{lim}\frac{(2−\frac{1}{𝑛})}{𝑛} \\ & =\frac{2−0}{4+0} \\ & =\frac{1}{2}.\end{aligned}


$$

Since $a_n$ and $b_n$ are both positive, and $\displaystyle\lim_{n\rightarrow\infty} \frac{a_n}{b_n} = \dfrac{1}{2}$ is positive and finite, we can use the limit comparison test.

So, since $\displaystyle\sum_{n=1}^\infty b_n$ diverges, then $\displaystyle\sum_{n=1}^\infty a_n$ diverges as well. Therefore, the series $\displaystyle \sum_{n=1}^\infty \dfrac{2n^3-n^2}{4n^4+n}$ diverges.

### Example: Applying the Limit Comparison Test for Convergence

#### Question

Given the sequences $a_n = \dfrac{1}{2n^2+n}$ and $b_n = \dfrac{1}{n^2},$ calculate $\displaystyle L = \lim_{n\to \infty} \dfrac{a_n}{b_n}$ and determine whether $\displaystyle\sum_{n=1}^\infty a_n$ converges or diverges.

#### Explanation

The limit comparison test states that if $a_n$ and $b_n$ are both positive, and

$$


\lim_{n\rightarrow\infty} \frac{a_n}{b_n} = L,


$$

where $L$ is positive and finite, then the series $\displaystyle\sum_{n=1}^\infty a_n$ and $\displaystyle\sum_{n=1}^\infty b_n$ either ** converge or ** diverge.

The given series looks as though it will behave like the convergent series

$$


\displaystyle \sum_{n=1}^\infty \dfrac{1}{2n^2} = \dfrac 1 2\sum_{n=1}^\infty \dfrac{1}{n^2}.


$$

So, we let

$$


a_n = \dfrac{1}{2n^2+n}, \qquad b_n = \dfrac{1}{n^2}.


$$

Computing the limit of the ratio, we get

$$


\begin{aligned}\underset{𝑛→∞}{lim}\frac{𝑎_{𝑛}}{𝑏_{𝑛}} & =\underset{𝑛→∞}{lim}(\frac{1}{2𝑛^{2}+𝑛}÷\frac{1}{𝑛^{2}}) \\ & =\underset{𝑛→∞}{lim}(\frac{𝑛^{2}}{2𝑛^{2}+𝑛}) \\ & =\underset{𝑛→∞}{lim}\frac{1}{(2+\frac{1}{𝑛})} \\ & =\frac{1}{2+0} \\ & =\frac{1}{2}.\end{aligned}


$$

Since $a_n$ and $b_n$ are both positive and $\displaystyle\lim_{n\rightarrow\infty} \frac{a_n}{b_n} = \dfrac12$ is positive and finite, we can use the limit comparison test.

So, since $\displaystyle\sum_{n=1}^\infty b_n$ converges, then $\displaystyle\sum_{n=1}^\infty a_n$ converges as well. Therefore, the series $\displaystyle \sum_{n=1}^\infty \dfrac{1}{2n^2+n}$ converges.

### Example: Applying the Limit Comparison Test Using Geometric Series

#### Question

Given the sequences $a_n = \dfrac{3(2^n)+1}{2(3^n)+1}$ and $b_n = \left(\dfrac{2}{3}\right)^n,$ calculate $\displaystyle L = \lim_{n\to\infty}\dfrac{a_n}{b_n}$ and determine whether $\displaystyle\sum_{n=1}^\infty a_n$ converges or diverges.

#### Explanation

The limit comparison test states that if $a_n$ and $b_n$ are both positive, and

$$


\lim_{n\rightarrow\infty} \frac{a_n}{b_n} = L,


$$

where $L$ is positive and finite, then the series $\displaystyle\sum_{n=1}^\infty a_n$ and $\displaystyle\sum_{n=1}^\infty b_n$ either ** converge or ** diverge.

The given series looks as though it will behave like the convergent geometric series

$$


\sum_{n=1}^\infty \dfrac{2^n}{3^n} = \sum_{n=1}^\infty \left( \dfrac{2}{3} \right)^n.


$$

We know the above series converges because it is a geometric series with common ratio $|r| = \dfrac{2}{3} < 1.$

So, we let

$$


a_n = \dfrac{3(2^n)+1}{2(3^n)+1}, \qquad b_n = \left( \dfrac{2}{3} \right)^n.


$$

Computing the limit of the ratio, we get

$$


\begin{aligned}\underset{𝑛→∞}{lim}\frac{𝑎_{𝑛}}{𝑏_{𝑛}} & =\underset{𝑛→∞}{lim}(\frac{3(2^{𝑛})+1}{2(3^{𝑛})+1}÷\frac{2^{𝑛}}{3^{𝑛}}) \\ & =\underset{𝑛→∞}{lim}(\frac{3(2^{𝑛})+1}{2(3^{𝑛})+1}⋅\frac{3^{𝑛}}{2^{𝑛}}) \\ & =\underset{𝑛→∞}{lim}(\frac{2^{𝑛}(3+2^{−𝑛})}{3^{𝑛}(2+3^{−𝑛})}⋅\frac{3^{𝑛}}{2^{𝑛}}) \\ & =\underset{𝑛→∞}{lim}(\frac{2^{𝑛}(3+2^{−𝑛})}{3^{𝑛}(2+3^{−𝑛})}⋅\frac{3^{𝑛}}{2^{𝑛}}) \\ & =\underset{𝑛→∞}{lim}(\frac{3+2^{−𝑛}}{2+3^{−𝑛}}) \\ & =\frac{3+2(0)}{2+3(0)} \\ & =\frac{3}{2}.\end{aligned}


$$

Since $a_n$ and $b_n$ are both positive and $\displaystyle\lim_{n\rightarrow\infty} \frac{a_n}{b_n} = \dfrac{3}{2}$ is positive and finite, we can use the limit comparison test.

So, since $\displaystyle\sum_{n=1}^\infty b_n$ converges, then $\displaystyle\sum_{n=1}^\infty a_n$ converges as well. Therefore, the series $\displaystyle \sum_{n=1}^\infty \dfrac{3(2^n)+1}{2(3^n)+1}$ converges.

### One-Sided Versions of the Limit Comparison Test

Suppose that $a_n$ and $b_n$ are two positive sequences.

Up to now, we've only considered cases where the ratio

$$


L = \lim_{n\rightarrow\infty} \frac{a_n}{b_n}


$$

gives a positive, finite number. However, the limit comparison test can be extended to form the so-called **one-sided comparison tests,** stated below:

- If $L = 0,$ and it is known that $\displaystyle \sum_{n=1}^\infty b_n$ converges, then $\displaystyle \sum_{n=1}^\infty a_n$ also converges.

- If $L = \infty,$ and it is known that $\displaystyle \sum_{n=1}^\infty b_n$ diverges, then $\displaystyle \sum_{n=1}^\infty a_n$ also diverges.

There's some nice intuition behind these one-sided tests:

- Suppose $L = 0.$ Since the $a_n$'s are in the numerator of our limit fraction, this suggests that the $a_n$'s are (in some sense) smaller than the $b_n$'s. So, if the sum of the $b_n$'s converges, the sum of the $a_n$'s must also converge.

- Suppose $L = \infty.$ Since the $a_n$'s are in the numerator of our limit fraction, this suggests that the $a_n$'s are (in some sense) larger than the $b_n$'s. So, if the sum of the $b_n$'s diverges, the sum of the $a_n$'s must also diverge.

### Example: Applying the One-Sided Versions of the Limit Comparison Test

#### Question

Given the sequences $a_n = \dfrac{\sqrt[3]{n^2}}{3n+4}$ and $b_n = \dfrac{1}{\sqrt{n}},$ calculate $\displaystyle L = \lim_{n\to\infty}\dfrac{a_n}{b_n}$ and determine whether $\displaystyle\sum_{n=1}^\infty a_n$ converges or diverges.

#### Explanation

Let $a_n$ and $b_n$ be two positive sequences. The one-sided limit comparison tests state the following:

- If $\displaystyle \lim_{n\rightarrow\infty} \frac{a_n}{b_n} = 0,$ and it is known that $\displaystyle \sum_{n=1}^\infty b_n$ converges, then $\displaystyle \sum_{n=1}^\infty a_n$ also converges.

- If $\displaystyle \lim_{n\rightarrow\infty} \frac{a_n}{b_n} = \infty,$ and it is known that $\displaystyle \sum_{n=1}^\infty b_n$ diverges, then $\displaystyle \sum_{n=1}^\infty a_n$ also diverges.

First, notice that $\displaystyle\sum_{n=1}^\infty b_n$ is a divergent $p$-series.

Computing the limit of the ratio, we get

$$


\begin{aligned}𝐿 & =\underset{𝑛→∞}{lim}\frac{𝑎_{𝑛}}{𝑏_{𝑛}} \\ & =\underset{𝑛→∞}{lim}(\frac{\sqrt[√𝑛^{2}]{3}}{3𝑛+4}÷\frac{1}{\sqrt{𝑛}}) \\ & =\underset{𝑛→∞}{lim}(\frac{\sqrt[√𝑛^{2}]{3}}{3𝑛+4}⋅\sqrt{𝑛}) \\ & =\underset{𝑛→∞}{lim}(\frac{𝑛^{2/3}}{3𝑛+4}⋅𝑛^{1/2}) \\ & =\underset{𝑛→∞}{lim}(\frac{𝑛^{7/6}}{3𝑛+4}) \\ & =\underset{𝑛→∞}{lim}(\frac{𝑛^{1/6}}{3+4/𝑛}) \\ & =\frac{∞}{3+0} \\ & =∞.\end{aligned}


$$

Since $a_n$ and $b_n$ are both positive and $\lim\limits_{n \to\infty} \dfrac{a_n}{b_n}=\infty,$ we can use the one-sided comparison test.

So, since $\displaystyle\sum_{n=1}^\infty b_n$ diverges, then $\displaystyle\sum_{n=1}^\infty a_n$ diverges as well. Therefore, the series $\displaystyle\sum_{n=1}^\infty \dfrac{\sqrt[3]{n^2}}{3n+4}$ diverges.
