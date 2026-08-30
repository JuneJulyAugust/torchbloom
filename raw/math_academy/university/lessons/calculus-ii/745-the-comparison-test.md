# The Comparison Test

Source: https://www.mathacademy.com/topics/745?courseId=106
Topic ID: 745

## Prerequisites

- [Convergence of Geometric Series](./684-convergence-of-geometric-series.md)
- [The Nth Term Test for Divergence](./743-the-nth-term-test-for-divergence.md)
- [Harmonic Series and p-Series](./860-harmonic-series-and-p-series.md)

## Lesson

### Introduction

The **comparison test for convergence** is a method that we can use to show that a series is convergent. The idea is to show that the series is *less than or equal to* some other series that is known to be convergent.

More precisely, the comparison test for convergence states the following:

*Consider two series $\displaystyle \sum_{n=1}^\infty a_n$ and $\displaystyle \sum_{n=1}^\infty b_n$ such that $a_n$ and $b_n$ are both positive and $a_n \leq b_n$ for all $n.$ If $\displaystyle \sum_{n=1}^\infty b_n$ is convergent, then $\displaystyle \sum_{n=1}^\infty a_n$ is also convergent.*

For example, let's apply the comparison test to show that the series

$$


\displaystyle \sum_{n=1}^\infty \dfrac{1}{n^2+1}


$$

is convergent. We will compare the series above to the series

$$


\displaystyle \sum_{n=1}^\infty \dfrac{1}{n^2}.


$$

Indeed, both $\dfrac{1}{n^2+1}$ and $\dfrac{1}{n^2}$ are positive, and

$$


\dfrac{1}{n^2+1} < \dfrac{1}{n^2}


$$

for all $n \geq 1.$ In particular, the above inequality is true because the denominator on the left-hand side is larger than the denominator on the right-hand side, which means the fraction on the left-hand side is smaller.

We know that $\displaystyle \sum_{n=1}^\infty \dfrac{1}{n^2}$ is convergent because it is a $p$-series with $p =2 > 1.$ Therefore, by the comparison test, we conclude that $\displaystyle \sum_{n=1}^\infty \dfrac{1}{n^2+1}$ is also convergent.

### Example: Selecting a Suitable Series For the Comparison Test For Convergence

#### Question

Consider the following argument regarding the convergence of the series $\displaystyle \sum_{n=1}^\infty \dfrac{1}{\sqrt{n^3}+1}.$

1. Let $a_n = \dfrac{1}{\sqrt{n^3}+1}.$ Note that $a_n > 0$ for all $n\geq 1,$ so we can use the comparison test.

2. The series $\displaystyle \sum_{n=1}^\infty b_n$ is convergent, and $b_n > 0$ for all $n\geq 1.$

3. $a_n\leq b_n,$ for all $n \geq 1.$

4. Therefore, by the comparison test, $\displaystyle \sum_{n=1}^\infty \dfrac{1}{\sqrt{n^3}+1}$ is convergent.

Which of the following sequences could be used for $b_n$ in steps 2 and 3 to make the argument valid?

1. $b_n = \dfrac{1}{n^2}$

2. $b_n = \dfrac{1}{n^{3/2}}$

3. $b_n =\dfrac{1}{n}$

#### Explanation

The comparison test for convergence states the following:

**

For the test to be valid, we require that $\displaystyle \sum_{n=1}^\infty b_n$ is convergent, and $\dfrac{1}{\sqrt{n^3} + 1} \leq b_n,$ for all $n \geq 1.$ Let's look at each potential sequence in-turn.

- The inequality $\dfrac{1}{\sqrt{n^3}+1} \leq \dfrac{1}{n^2}$ is equivalent to $n^2 \leq n^{3/2} + 1,$ which is ** true for all $n \geq 1.$

- The inequality $\dfrac{1}{\sqrt{n^3}+1} \leq\dfrac{1}{n^{3/2}}$ is equivalent to $n^{3/2} \leq n^{3/2} + 1.$ This inequality is true for all $n \geq 1.$

- The sequence $b_n = \dfrac{1}{n}$ is not suitable since the series $\displaystyle \sum_{n=1}^\infty \dfrac{1}{n}$ is divergent.

Therefore, the correct answer is, "II only."

### Example: Applying the Comparison Test to Show That a Series Converges

#### Question

Prove that the series $\displaystyle \sum_{n=1}^\infty \dfrac{1}{2^n + n}$ is convergent by the comparison test.

#### Explanation

The comparison test for convergence states the following:

**

We follow four steps to show that $S$ is convergent.

****: First, we let $a_n = \dfrac{1}{2^n + n}$ and $b_n = \dfrac{1}{2^n}.$ We note that $a_n > 0$ and $b_n > 0$ for all $n \geq 1.$

****: We show that $\displaystyle \sum_{n=1}^\infty b_n$ is convergent. We have

$$


\displaystyle \sum_{n=1}^\infty b_n = \displaystyle \sum_{n=1}^\infty \dfrac{1}{2^n}


$$

which is a geometric series with common ratio $r = \dfrac{1}{2}$ and $|r| < 1,$ so it is convergent.

****: We show that $a_n \leq b_n$ for all $n\geq 1.$

$$


\begin{aligned}𝑎_{𝑛} & \overset{≤}{?}𝑏_{𝑛} \\ \frac{1}{2^{𝑛}+𝑛} & ≤\frac{1}{2^{𝑛}}.\,✓\end{aligned}


$$

The above statement is true because the denominator on the left-hand side is larger than the denominator on the right-hand side.

****: We conclude that $\displaystyle \sum_{n=1}^\infty a_n$ is convergent by the comparison test.

### The Comparison Test for Divergence

We can use the **comparison test for divergence** to check if a series is divergent. The idea is to show that the series is *greater than or equal to* some other series that is known to be divergent.

More precisely, the comparison test for divergence states the following:

*Consider two series $\displaystyle \sum_{n=1}^\infty a_n$ and $\displaystyle \sum_{n=1}^\infty b_n$ such that $a_n$ and $b_n$ are both positive and $a_n \geq b_n$ for all $n.$ If $\displaystyle \sum_{n=1}^\infty b_n$ is divergent, then $\displaystyle \sum_{n=1}^\infty a_n$ is also divergent.*

For example, let's apply the comparison test to show that the series

$$


\displaystyle \sum_{n=1}^\infty \dfrac{1}{2n-1}.


$$

is divergent. We will compare the series above to the series

$$


\displaystyle \sum_{n=1}^\infty \dfrac{1}{2n}.


$$

Indeed, both $\dfrac{1}{2n-1}$ and $\dfrac{1}{2n}$ are positive, and

$$


\dfrac{1}{2n-1} \geq \dfrac{1}{2n}.


$$

for all $n \geq 1.$ The above inequality is true because the denominator on the left-hand side is smaller than the denominator on the right-hand side, which means the fraction on the left-hand side is larger.

We know that $\displaystyle \sum_{n=1}^\infty \dfrac{1}{2n}$ is divergent because it is a $p$-series with $p \leq 1.$ Therefore, by the comparison test, we conclude that $\displaystyle \sum_{n=1}^\infty \dfrac{1}{2n-1}$ is also divergent.

### Example: Selecting a Suitable Series For the Comparison Test For Divergence

#### Question

Consider the following argument regarding the divergence of the series $\displaystyle \sum_{n=1}^\infty \dfrac{\cos{n} +2}{\sqrt{n}}.$

1. Let $a_n=\dfrac{\cos{n} +2}{\sqrt{n}}.$ Note that $a_n >0$ for all $n \geq 1,$ so we can use the comparison test.

2. The series $\displaystyle \sum_{n=1}^\infty b_n$ is divergent, and $b_n > 0$ for all $n \geq 1.$

3. $a_n \geq b_n,$ for all $n \geq 1.$

4. Therefore, by the comparison test, $\displaystyle \sum_{n=1}^\infty \dfrac{\cos{n} +2}{\sqrt{n}}$ is divergent.

Which of the following sequences could be used for $b_n$ in steps 2 and 3 to make the argument valid?

1. $b_n = \dfrac{1}{\sqrt{n}}$

2. $b_n = \dfrac{2}{\sqrt{n}}$

3. $b_n = \dfrac{2}{n^2}$

#### Explanation

The comparison test for divergence states the following:

**

For the test to be valid, we require that $\displaystyle \sum_{n=1}^\infty b_n$ is divergent, and $\dfrac{\cos{n} + 2}{\sqrt{n}} \geq b_n,$ for all $n \geq 1.$ Let's look at each potential sequence in turn.

- The inequality $\dfrac{\cos{n} +2}{\sqrt{n}} \geq \dfrac{1}{\sqrt{n}}$ is equivalent to $\cos{n} \geq -1.$ This inequality is true for all $n \geq 1.$

- The inequality $\dfrac{\cos{n} +2}{\sqrt{n}} \geq \dfrac{2}{\sqrt{n}}$ is equivalent to $\cos{n} \geq 0.$ This inequality is ** true for all $n\geq 1.$

- The sequence $b_n = \dfrac{2}{n^2}$ is not suitable since the series $\displaystyle \sum_{n=1}^\infty \dfrac{2}{n^2}$ is convergent.

Therefore, the correct answer is "I only."

### Example: Applying the Comparison Test to Show That a Series Diverges

#### Question

Prove that the series $\displaystyle \sum_{n=1}^\infty \dfrac{5 + \sin n}{n}$ is divergent by the comparison test.

#### Explanation

The comparison test for divergence states the following:

**

We follow four steps to show that $S$ is divergent.

****: First, we let $a_n = \dfrac{5 + \sin n}{n}$ and $b_n = \dfrac{1}{n}.$ We note that $a_n > 0$ and $b_n > 0$ for all $n \geq 1.$

****: We show that $\displaystyle \sum_{n=1}^\infty b_n$ is divergent. We have,

$$


\displaystyle \sum_{n=1}^\infty b_n = \displaystyle \sum_{n=1}^\infty \dfrac{1}{n}


$$

which is divergent by the $p$-series test.

****: We show that $a_n \geq b_n$ for all $n\geq 1.$

$$


\begin{aligned}𝑎_{𝑛} & \overset{≥}{?}𝑏_{𝑛} \\ \frac{5+sin⁡𝑛}{𝑛} & \overset{≥}{?}\frac{1}{𝑛} \\ 5+sin⁡𝑛 & \overset{≥}{?}1 \\ sin⁡𝑛 & ≥−4.\,✓\end{aligned}


$$

****: We conclude that $\displaystyle \sum_{n=1}^\infty a_n$ is divergent by the comparison test.
