# Radius of Convergence of Power Series Centered at the Origin

Source: https://www.mathacademy.com/topics/984?courseId=21
Topic ID: 984

## Prerequisites

- [Selecting Procedures for Analyzing Infinite Series](./1172-selecting-procedures-for-analyzing-infinite-series.md)

## Lesson

### Introduction

Suppose that we are given the **infinite power series**

$$


\sum_{n=1}^{\infty} \frac{x^n}{n^2}=x +\frac{x^2}{2^2}+\frac{x^3}{3^2}+\frac{x^4}{4^2} +\cdots \,.


$$

This series is a function of $x,$ and it may converge for some values of $x$ and diverge for other values. How can we determine the values of $x$ for which the series is convergent?

One method that often works is the ratio test for convergence. We define $a_n=\dfrac{x^n}{n^2},$ and we calculate the limit of the ratio of two successive terms, as follows:

$$


\begin{aligned}𝐿 & =\underset{𝑛→∞}{lim}\frac{𝑎_{𝑛+1}}{𝑎_{𝑛}} \\ & =\underset{𝑛→∞}{lim}\frac{𝑥^{𝑛+1}}{(𝑛+1)^{2}}⋅\frac{𝑛^{2}}{𝑥^{𝑛}} \\ & =\underset{𝑛→∞}{lim}\frac{𝑛^{2}}{(𝑛+1)^{2}}\,|𝑥| \\ & =|𝑥|\underset{𝑛→∞}{lim}\frac{𝑛^{2}}{(𝑛+1)^{2}} \\ & =|𝑥|\underset{𝑛→∞}{lim}\frac{𝑛^{2}}{𝑛^{2}+2𝑛+1} \\ & =|𝑥|\underset{𝑛→∞}{lim}\frac{1}{1+\frac{2}{𝑛}+\frac{1}{𝑛^{2}}} \\ & =|𝑥|⋅1 \\ & =|𝑥|\end{aligned}


$$

The ratio test says that the series converges if $L<1,$ diverges if $L>1,$ and is inconclusive if $L=1.$ So, the series converges if $|x|<1.$ Therefore, the series converges for any $x$ that lies in the open interval $(-1,1).$

Unfortunately, the ratio test gives no conclusion about the convergence when $|x|=1,$ so the endpoints $x=1$ and $x=-1$ need to be investigated separately using another test for convergence.

- When $x=1,$ we have which is convergent by the $p$-series test.

- When $x=-1,$ we have which is convergent by the alternating series test.

Therefore, the series is convergent provided that $x \in [-1,1].$ We call the interval $[-1,1]$ the **interval of convergence**.

The **radius of convergence** $R$ is half of the length of the interval (in the same way that the radius of a circle is equal to half the diameter of the circle). In our case, we have

$$


R = \dfrac{1-(-1)}{2} = 1.


$$

### Example: Finding the Radius of Convergence of a Given Power Series

#### Question

Find the radius of convergence $R$ of the series

$$


\sum_{n=1}^{\infty} \frac{(-1)^{n}x^n}{n \cdot 2^n} = -\frac{x}{1 \cdot 2} + \frac{x^2}{2 \cdot 2^2}-\frac{x^3}{3 \cdot 2^3}+\frac{x^4}{4 \cdot 2^4}+\cdots \,.


$$

#### Explanation

To apply the ratio test, we define $a_n=\dfrac{(-1)^{n}x^n}{n \cdot 2^n}.$ Then, we calculate the ratio of two successive terms and take the limit as $n\to\infty\mathbin{:}$

$$


\begin{aligned}𝐿 & =\underset{𝑛→∞}{lim}\frac{𝑎_{𝑛+1}}{𝑎_{𝑛}} \\ & =\underset{𝑛→∞}{lim}\frac{(−1)^{𝑛+1}𝑥^{𝑛+1}}{(𝑛+1)⋅2^{𝑛+1}}⋅\frac{𝑛⋅2^{𝑛}}{(−1)^{𝑛}𝑥^{𝑛}} \\ & =\underset{𝑛→∞}{lim}\frac{−𝑛𝑥}{2(𝑛+1)} \\ & =−\frac{𝑥}{2}⋅\underset{𝑛→∞}{lim}\frac{𝑛}{𝑛+1} \\ & =\frac{𝑥}{2}⋅1 \\ & =\frac{|𝑥|}{2}\end{aligned}


$$

The series converges if $L< 1.$ In this case, the convergence condition is satisfied if

$$


\dfrac{|x|}{2} < 1 \quad\Rightarrow\quad |x| < 2.


$$

Therefore, we conclude that the radius of convergence is $R=2.$

### Example: Finding the Interval of Convergence of a Given Power Series

#### Question

Find the interval of convergence for the series

$$


\sum_{n=1}^{\infty} \frac{x^{n}}{3^n\sqrt{n}}=\dfrac{x}{3}+\frac{x^2}{3^2\cdot \sqrt{2}}+\frac{x^3}{3^3\cdot \sqrt{3}}+\frac{x^4}{3^4\cdot 2}+\cdots \,.


$$

#### Explanation

To apply the ratio test, we define $a_n= \dfrac{x^{n}}{3^n\sqrt{n}}.$ Then, we calculate the ratio of two successive terms and take the limit as $n\to\infty\mathbin{:}$

$$


\begin{aligned}𝐿 & =\underset{𝑛→∞}{lim}\frac{𝑎_{𝑛+1}}{𝑎_{𝑛}} \\ & =\underset{𝑛→∞}{lim}\frac{𝑥^{𝑛+1}}{3^{𝑛+1}\sqrt{√𝑛+1}}⋅\frac{3^{𝑛}\sqrt{√𝑛}}{𝑥^{𝑛}} \\ & =\underset{𝑛→∞}{lim}\frac{\sqrt{√𝑛}𝑥}{3\sqrt{√𝑛+1}} \\ & =\frac{|𝑥|}{3}\underset{𝑛→∞}{lim}(\frac{\sqrt{√𝑛}}{\sqrt{√𝑛+1}}) \\ & =\frac{|𝑥|}{3}⋅1 \\ & =\frac{|𝑥|}{3}\end{aligned}


$$

The series converges if $L < 1.$ In this case, the convergence condition is satisfied for

$$


\dfrac{|x|}{3}< 1


$$

which gives

$$


|x| < 3.


$$

So, the radius of convergence is $3,$ and the series converges for any $x$ that lies in the open interval $(-3,3).$

The ratio test gives no conclusion about the convergence of the series when $L=1.$ So, when $|x|=3,$ we do not know if the series converges. This means that the endpoints $x=-3$ and $x=3$ need to be investigated separately using another test for convergence.

- When $x=3,$ we have which is divergent by the $p$-series test. So the endpoint $x=3$ is ** included in our interval.

- When $x=-3,$ we have which is convergent by the alternating series test. So the endpoint $x=-3$ ** included in our interval.

Therefore, the interval of convergence is $[-3,3).$

### Example: Finding the Radius and Interval of Convergence of a Power Series when the Limit of the Ratio is Zero

#### Question

Find the radius and interval of convergence for the series

$$


\sum_{n=0}^{\infty}\dfrac{ (-1)^n x^{n}}{n!}.


$$

#### Explanation

To apply the ratio test, we define $a_n=\dfrac{(-1)^n x^{n}}{n!}.$ Then, we calculate the ratio of two successive terms and take the limit as $n\to\infty\mathbin{:}$

$$


\begin{aligned}𝐿 & =\underset{𝑛→∞}{lim}\frac{𝑎_{𝑛+1}}{𝑎_{𝑛}} \\ & =\underset{𝑛→∞}{lim}\frac{(−1)^{𝑛+1}𝑥^{𝑛+1}}{(𝑛+1)!}⋅\frac{𝑛!}{(−1)^{𝑛}𝑥^{𝑛}} \\ & =\underset{𝑛→∞}{lim}−\,\frac{𝑥}{(𝑛+1)} \\ & =|−𝑥|\underset{𝑛→∞}{lim}\frac{1}{𝑛+1} \\ & =|𝑥|⋅0 \\ & =0\end{aligned}


$$

The series converges if $L< 1.$ In this case, the convergence condition is satisfied for all $x\in (-\infty,\infty).$ Therefore, we conclude that the radius of convergence is $R=\infty,$ and the interval of convergence is $x\in(-\infty, \infty).$
