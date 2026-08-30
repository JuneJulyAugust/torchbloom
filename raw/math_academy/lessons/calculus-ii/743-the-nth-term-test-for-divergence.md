# The Nth Term Test for Divergence

Source: https://www.mathacademy.com/topics/743?courseId=106
Topic ID: 743

## Prerequisites

- [Convergent and Divergent Infinite Series](./982-convergent-and-divergent-infinite-series.md)
- [Limits of Sequences With Factorials](./1089-limits-of-sequences-with-factorials.md)
- [Further Determining Limits of Sequences Using Relative Magnitudes](./3539-further-determining-limits-of-sequences-using-relative-magnitudes.md)

## Lesson

### Introduction

The **$n$th term test for divergence** is a method that can be used to show that an infinite series diverges.

Suppose we have an infinite series $\displaystyle\sum_{n=1}^\infty a_n.$ The $n$th term test for divergence states that

- If $\displaystyle \lim_{n\to\infty} a_n \neq 0,$ then the series is divergent.

- If $\displaystyle \lim_{n\to\infty} a_n = 0,$ then the $n$th term test gives *no conclusion* regarding the convergence or divergence of the series.

The $n$th term test can *only* be used to show that a series diverges. It *cannot* be used to show that a series converges.

**Note:** The $n$th term for divergence is simultaneously intuitive and counterintuitive.

- The first part of the $n$th term test is intuitive. If the limit of the terms of the series is not $0,$ then the partial sums of the series are always changing by a significant amount, which means they never "settle" to a single value.

- The second part of the $n$th term test may seem counterintuitive. If the limit of the terms of the series is $0,$ it's tempting to think that the series must converge. However, as we will see in the future, this is not the case. There are many series that diverge despite the limit of their terms being $0.$

### Example: Applying the Nth Term Test to Show that a Series Diverges

#### Question

Given the sequence $a_n = \dfrac{n}{n+1},$ which of the following statements are true?

1. $\lim\limits_{n\to\infty} a_n = 0$

2. $\lim\limits_{n\to\infty} a_n \neq 0$

3. The series $\displaystyle \sum_{n=1}^\infty a_n$ is divergent

#### Explanation

To calculate $\displaystyle \lim_{n\to\infty} a_n,$ we divide top and bottom by $n,$ as follows:

$$


\begin{aligned}𝑎_{𝑛} & =(\frac{𝑛}{𝑛+1}) \\ & =\frac{\frac{𝑛}{𝑛}}{𝑛} \\ & =\frac{1}{1+\frac{1}{𝑛}}.\end{aligned}


$$

Taking the limit as $n\rightarrow\infty$ gives

$$


\begin{aligned}\underset{𝑛→∞}{lim}𝑎_{𝑛} & =\underset{𝑛→∞}{lim}\frac{1}{1+\frac{1}{𝑛}} \\ & =\frac{1}{1+0} \\ & =1.\end{aligned}


$$

Since the limit of the sequence $a_n$ is not zero, the $n$th term test guarantees that the series is divergent.

Therefore, only statements II and III are true.

### Example: Applying the Nth Term Test When No Conclusion Can be Made

#### Question

Given the sequence $a_n = \dfrac{1}{n},$ which of the following statements are true?

1. $\lim\limits_{n\to\infty} a_n = 0$

2. $\lim\limits_{n\to\infty} a_n \neq 0$

3. Using the $n$th term test only, no conclusion can be made regarding the convergence or divergence of the series $\displaystyle \sum_{n=1}^\infty a_n$

#### Explanation

Taking the limit of $a_n,$ we get

$$


\lim\limits_{n\to \infty} a_n = \lim\limits_{n\to \infty} \frac{1}{n} =0.


$$

The $n$th term test tells us that a series $\displaystyle \sum_{n=1}^\infty a_n$ diverges if $\displaystyle\lim_{n\to\infty} a_n \neq 0.$

Here, the limit ** zero, so the $n$th term test gives no conclusion regarding the convergence or divergence of the series.

Therefore, only statements I and III are true.

### Example: Identifying Divergent Series by Applying the Nth Term Test

#### Question

According to the $n$th term test ****, which of the following series diverge?

1. $\displaystyle\sum_{n=1}^\infty \dfrac{2(n-1)!}{n!}$

2. $\displaystyle\sum_{n=1}^\infty \dfrac{e^n}{3n+1}$

3. $\displaystyle\sum_{n=1}^\infty \left(\dfrac{3}{2}\right)^n$

#### Explanation

Let's examine each series in-turn.

- Let $a_n = \dfrac{2(n-1)!}{n!}.$ Simplifying gives and from here we see that So the $n$th term test gives no conclusion as to the convergence or divergence of $\displaystyle\sum_{n=1}^\infty \dfrac{2(n-1)!}{n!}$.

- Next, let $b_n = \dfrac{e^n}{3n+1}.$ We have that because the numerator grows much faster than the denominator. Therefore, by the $n$th term test, $\displaystyle\sum_{n=1}^\infty \dfrac{e^n}{3n+1}$ is divergent.

- Finally, let $c_n = \left(\dfrac{3}{2}\right)^n.$ This is a geometric sequence with $|r| = \dfrac 3 2 > 1.$ So, we have that and by the $n$th term test, $\displaystyle\sum_{n=1}^\infty \left(\dfrac{3}{2}\right)^n$ is divergent.

In conclusion, the $n$th term test guarantees that II and III diverge, but gives no conclusion regarding the convergence or divergence of I.

### The Harmonic Series

The series

$$


\sum_{n=1}^\infty \frac{1}{n} = \frac{1}{1} + \frac{1}{2} + \frac{1}{3} + \cdots


$$

is called the **harmonic series**, and it is a well-known fact that this series is divergent, even though $\lim\limits_{n\to \infty} a_n=0.$

This demonstrates how we must be very careful when interpreting the results of the $n$th term test.

If $\lim\limits_{n\to \infty} a_n=0,$ then we cannot draw any conclusion about the convergence or divergence of the series.
