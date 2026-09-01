# Convergence of Geometric Series

Source: https://www.mathacademy.com/topics/684?courseId=106
Topic ID: 684

## Prerequisites

- [Writing an Infinite Geometric Series in Sigma Notation](./686-writing-an-infinite-geometric-series-in-sigma-notation.md)
- [Solving Inequalities Involving Exponential Functions](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/2857-solving-inequalities-involving-exponential-functions.md)
- [Further Convergence of Geometric Sequences](./3838-further-convergence-of-geometric-sequences.md)

## Lesson

### Introduction

In general, a geometric series with common ratio $r$ is

- convergent if $|r| <1,$ and

- divergent if $|r| \geq 1.$

For example, consider the series

$$


4+2+1+\dfrac 12+ \cdots .


$$

The common ratio is

$$


\begin{aligned}𝑟 & =\frac{2}{4}=\frac{1}{2},\end{aligned}


$$

so $|r|<1$ and therefore the series converges. (This makes sense intuitively, because the magnitude of the terms keeps getting smaller.)

On the other hand, consider the series

$$


1-3+9-27+\cdots .


$$

The common ratio is

$$


\begin{aligned}𝑟 & =\frac{(−3)}{1}=−3,\end{aligned}


$$

so $|r|>1$ and therefore the series diverges. (This makes sense intuitively, because the magnitude of the terms keeps getting bigger.)

**Note:** If $|r|=1,$ then the series diverges. For example, consider the series

$$


0.001+0.001+0.001+0.001+\cdots .


$$

The common ratio is

$$


\begin{aligned}𝑟 & =\frac{0.001}{0.001}=1,\end{aligned}


$$

so $|r|=1$ and therefore the series diverges. (This makes sense intuitively, because the terms are not approaching $0.$)

### Example: Determining Whether a Geometric Series Given in Sigma Notation Converges

#### Question

Determine whether the following geometric series converges or diverges.

$$


S = \sum_{n=1}^\infty \dfrac{5}{2}\left(\dfrac{1}{2}\right)^{n+1}


$$

#### Explanation

The series starts with $n=1.$ So the common ratio is

$$


\begin{aligned}𝑟=\frac{𝑎_{2}}{𝑎_{1}} & =\frac{\frac{5}{2}(\frac{1}{2})^{2+1}}{2} \\ & =\frac{\frac{5}{2}(\frac{1}{2})^{3}}{2} \\ & =\frac{1}{2}.\end{aligned}


$$

Therefore, the series is convergent because $|r| <1.$

### Example: Determining the Convergence of a Geometric Series With an Arbitrary Starting Index

#### Question

Determine whether the following geometric series converges or diverges.

$$


\sum_{n=0}^\infty {3}\left(\dfrac{3}{2}\right)^{n}


$$

#### Explanation

The series starts with $n=0.$ So the common ratio is

$$


\begin{aligned}𝑟=\frac{𝑎_{1}}{𝑎_{0}} & =\frac{3(\frac{3}{2})^{1}}{2} \\ & =\frac{3}{2}.\end{aligned}


$$

Therefore, the series is divergent because $|r| \geq 1.$

### Example: Identifying Convergent Geometric Series

#### Question

Which of the following geometric series converge?

1. $\displaystyle{\sum_{n = 1}^ \infty} 4 (-3)^{n}$

2. $\displaystyle{\sum_{n = 6}^\infty} 32 \left(\dfrac{1}{2}\right)^{4n}$

3. $\displaystyle{\sum_{n=0}^{\infty}} \dfrac{4^n}{2^{n+3}}$

#### Explanation

Let's look at each series in turn.

- The series $\displaystyle{\sum_{n = 1}^ \infty} 4 (-3)^{n}$ starts with $n=1.$ So the common ratio is Therefore, the series is divergent because $|r| \geq 1.$

- The series $\displaystyle{\sum_{n = 6}^\infty} 32 \left(\dfrac{1}{2}\right)^{4n}$ starts with $n=6.$ So the common ratio is Therefore, the series is convergent because $|r| < 1.$

- The series $\displaystyle{\sum_{n=0}^{\infty}} \dfrac{4^n}{2^{n+3}}$ starts with $n=0.$ So the common ratio is Therefore, the series is divergent because $|r| \geq 1.$

In conclusion, only series II converges.

### Example: Calculating the Range of Values of a Parameter for Which a Geometric Series Converges

#### Question

For which values of $k$ does the series $\displaystyle\sum_{n=1}^\infty\dfrac{3(2)^{kn}}{4^n}$ converge?

#### Explanation

First, we rewrite the series so that it's in the form $\displaystyle\sum_{n=1}^\infty a r^n,$ as follows:

$$


\begin{aligned}\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}\frac{3(2)^{𝑘𝑛}}{4^{𝑛}} & =\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}\frac{3(2^{𝑘})^{𝑛}}{4^{𝑛}} \\ & =\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}3\frac{(2^{𝑘})^{𝑛}}{4^{𝑛}} \\ & =\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}3(\frac{2^{𝑘}}{4})^{𝑛}.\end{aligned}


$$

We see that this is a geometric series with a common ratio of $r = \dfrac{2^k}{4}.$

For the series to converge, we require $|r| < 1.$ Therefore, we have

$$


\begin{aligned}\frac{2^{𝑘}}{4} & <1 \\ \frac{2^{𝑘}}{4} & <1 \\ 2^{𝑘} & <4.\end{aligned}


$$

Notice that we could remove the absolute value bars because $\dfrac{2^k}{4}$ is always positive.

The equation $2^k = 4$ has the solution $k=2.$ Now, since $2^k$ increases as $k$ increases, the solution to $2^k < 4$ must be $k < 2.$
