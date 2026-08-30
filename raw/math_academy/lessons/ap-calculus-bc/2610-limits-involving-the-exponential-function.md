# Limits Involving the Exponential Function

Source: https://www.mathacademy.com/topics/2610?courseId=21
Topic ID: 2610

## Prerequisites

- [The Power and Root Rules for Limits](../ap-calculus-ab/37-the-power-and-root-rules-for-limits.md)
- [Limits of Exponential Functions](../ap-calculus-ab/1717-limits-of-exponential-functions.md)

## Lesson

### Introduction

Let's consider the following limit:

$$


\lim_{n \to \infty} \left(1+\dfrac{1}{n}\right)^{n}


$$

Notice that as $n \to \infty,$

- the expression inside the parentheses approaches $1,$ while

- the exponent approaches $\infty.$

If we attempt to evaluate the limit directly, we get

$$


\lim_{n \to \infty} \left(1+\dfrac{1}{n}\right)^{n} = 1^\infty,


$$

which is an indeterminate form (i.e., its meaning is ambiguous and therefore cannot be used to determine the true value of the limit). So, if we want to evaluate this limit, we need to find another way to do it.

To get a feel for how this limit behaves, we create a table of values, as follows:

Now, recall Euler's number $e\approx 2.718\,28$ to five decimal places. It appears that our expression converges to $e$ as $n\to\infty.$ It can be shown that this is indeed the case.

Therefore, we have the following important result:

$$


e = \lim_{n \to \infty} \left(1+\dfrac{1}{n}\right)^{n}


$$

### Example: Evaluating a Limit Using the Limit Definition of Euler's Number

#### Question

Calculate $\displaystyle{\lim_{n \to \infty} \left(1+\dfrac{1}{n}\right)^{3n}}.$

#### Explanation

Recall the following special limit:

$$


e = \lim_{n \to \infty} \left(1+\dfrac{1}{n}\right)^{n}


$$

Now, we rewrite the given limit using the algebra of limits, as follows:

$$


\begin{aligned}\underset{𝑛→∞}{lim}(1+\frac{1}{𝑛})^{3𝑛} & =\underset{𝑛→∞}{lim}[(1+\frac{1}{𝑛})^{𝑛}]^{3} \\ & =[\underset{𝑛→∞}{lim}(1+\frac{1}{𝑛})^{𝑛}]^{3} \\ & =𝑒^{3}\end{aligned}


$$

### Example: Evaluating a Limit Using the Limit Definition of Euler's Number: Limits Containing Variables

#### Question

Calculate $\displaystyle{\lim_{n \to \infty} \left(1+\dfrac{1}{n}\right)^{nx/3}}.$

#### Explanation

Recall the following special limit:

$$


e = \lim_{n \to \infty} \left(1+\dfrac{1}{n}\right)^{n}


$$

Now, we rewrite the given limit using the algebra of limits, as follows:

$$


\begin{aligned}\underset{𝑛→∞}{lim}(1+\frac{1}{𝑛})^{𝑛𝑥/3} & =\underset{𝑛→∞}{lim}[(1+\frac{1}{𝑛})^{𝑛}]^{𝑥/3} \\ & =[\underset{𝑛→∞}{lim}(1+\frac{1}{𝑛})^{𝑛}]^{𝑥/3} \\ & =𝑒^{𝑥/3} \\ & =\sqrt[√𝑒^{𝑥}]{3}\end{aligned}


$$

### Another Definition of the Exponential Function

Let's now consider the limit

$$


\lim_{n \to \infty} \left(1+\dfrac{x}{n}\right)^{n},


$$

where $x$ is a real number.

First, we rewrite the given limit using the algebra of limits, as follows:

$$


\begin{aligned}\underset{𝑛→∞}{lim}(1+\frac{𝑥}{𝑛})^{𝑛} & =\underset{𝑛→∞}{lim}(1+\frac{1}{𝑛/𝑥})^{𝑛} \\ & =\underset{𝑛→∞}{lim}(1+\frac{1}{𝑛/𝑥})^{(𝑛/𝑥)⋅𝑥} \\ & =[\underset{𝑛→∞}{lim}(1+\frac{1}{𝑛/𝑥})^{𝑛/𝑥}]^{𝑥}\end{aligned}


$$

Let's now perform the substitution $m=n/x.$ Since $m\to\infty$ as $n\to\infty,$ we obtain

$$


\begin{aligned}[\underset{𝑛→∞}{lim}(1+\frac{1}{𝑛/𝑥})^{𝑛/𝑥}]^{𝑥} & =[\,\underset{𝑒}{\underset{}{\underset{𝑚→∞}{lim}(1+\frac{1}{𝑚})^{𝑚}}}\,]^{𝑥} \\ & =𝑒^{𝑥}.\end{aligned}


$$

Therefore, we conclude that

$$


\begin{aligned}𝑒^{𝑥}=\underset{𝑛→∞}{lim}(1+\frac{𝑥}{𝑛})^{𝑛}.\end{aligned}


$$

### Example: Applying the Limit Definition of the Exponential Function

#### Question

Calculate $\displaystyle{\lim_{n \to \infty} \left(1+\dfrac{x}{n}\right)^{-n/2}}.$

#### Explanation

Recall the following special limit:

$$


e^x = \lim_{n \to \infty} \left(1+\dfrac{x}{n}\right)^{n}


$$

Now, we rewrite the given limit using the algebra of limits, as follows:

$$


\begin{aligned}\underset{𝑛→∞}{lim}(1+\frac{𝑥}{𝑛})^{−𝑛/2} & =\underset{𝑛→∞}{lim}[(1+\frac{𝑥}{𝑛})^{𝑛}]^{−1/2} \\ & =[\underset{𝑛→∞}{lim}(1+\frac{𝑥}{𝑛})^{𝑛}]^{−1/2} \\ & =(𝑒^{𝑥})^{−1/2} \\ & =\sqrt{√\frac{1}{𝑒^{𝑥}}}\end{aligned}


$$
