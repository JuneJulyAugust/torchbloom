# Mean and Variance of the Discrete Uniform Distribution

Source: https://www.mathacademy.com/topics/3402?courseId=145
Topic ID: 3402

## Prerequisites

- [Variance of Discrete Random Variables](./1388-variance-of-discrete-random-variables.md)
- [Modeling With Discrete Uniform Distributions](./3269-modeling-with-discrete-uniform-distributions.md)

## Lesson

### Introduction

We know that if a random variable $X$ follows a *discrete* uniform distribution, then it has the following probability mass function:

$$


\begin{aligned}\frac{1}{|𝑆|}, & 𝑥∈𝑆 \\ 0, & otherwise\end{aligned}


$$

Let's now suppose that

$$


X\sim U\{a, a+1, a+2, \ldots, b\},


$$

where $a$ and $b$ are integers. In other words, we're concerned with the special case where the support $S$ of $X$ contains every integer between $a$ and $b$ inclusive.

In this case, it can be shown that the mean value of $X$ is given by

$$


\text{E}[X] = \dfrac{a+b}{2}.


$$

It can also be shown that

$$


\text{Var}[X] = \dfrac{|S|^2-1}{12}.


$$

We'll prove these results at the end of the lesson.

### Example: Computing Mean Values in Context

#### Question

A fair die has $12$ sides labeled with numbers $1$ through $12.$ What is the expected value of a random roll of this die?

#### Explanation

Let $X$ represent the number the die lands on. From the problem statement, we know that $X \sim U \{1, 2, \ldots, 12\},$ and we wish to compute $\textrm E[X].$

In general, if $X \sim U \{a, a + 1, \ldots, b\},$ then $X$ has the following expected value:

$$


\textrm E[X] = \dfrac{a+b}{2}


$$

So, for our random variable $X \sim U \{1, 2, \ldots, 12\},$ we have the following expected value:

$$


\textrm E[X] = \dfrac{1+12}{2} = 6.5


$$

Therefore, the expected value is $6.5.$

### Example: Computing Variances in Context

#### Question

A fair die has sides labeled with numbers $4$ through $15.$ What is the variance of the numbers obtained when rolling this die?

#### Explanation

Let $X$ represent the number the die lands on. From the problem statement, we know that $X \sim U \{4, 5, \ldots, 15 \},$ and we wish to compute $\text{Var}[X].$

In general, if $X \sim U \{a, a + 1, \ldots, b\},$ then the variance of $X$ is

$$


\text{Var}[X] = \dfrac{|S|^2-1}{12}


$$

where $S = \{a, a+1, \ldots, b\}.$

Now, we know that

$$


\begin{aligned}|𝑆| & =𝑏−𝑎+1 \\ & =15−4+1 \\ & =12.\end{aligned}


$$

So, for our random variable $X \sim U \{4, 5, \ldots, 15 \},$ we have the following variance:

$$


\text{Var}[X] = \dfrac{12^2 - 1}{12} = \dfrac{143}{12}


$$

Therefore, the variance is $\dfrac{143}{12}.$

### Proving the Formula for the Mean

Here, we will show that for $X\sim \{a, a+1, a+2, \ldots, b\},$ we have

$$


\text{E}[X] = \dfrac{a+b}{2}.


$$

First, recall that the probability mass function of $X$ is given by

$$


\begin{aligned}\frac{1}{|𝑆|}, & 𝑥∈𝑆 \\ 0, & otherwise.\end{aligned}


$$

By the definition of expected value for discrete random variables, we have

$$


\begin{aligned}E[𝑋] & =\underset{𝑥∈𝑆}{∑}𝑥𝑓(𝑥) \\ & =\underset{𝑥∈𝑆}{∑}𝑥⋅\frac{1}{|𝑆|} \\ & =\frac{1}{|𝑆|}\underset{𝑥∈𝑆}{∑}𝑥 \\ & =\frac{1}{|𝑆|}[𝑎+(𝑎+1)+(𝑎+2)+⋯+𝑏].\end{aligned}


$$

Now, the term in the square brackets is an arithmetic series with the first term $a$ and the last term $b.$ Therefore, using the formula for the sum of an arithmetic series, we have

$$


\begin{aligned}E[𝑋] & =\frac{1}{|𝑆|}[𝑎+(𝑎+1)+(𝑎+2)+⋯+𝑏] \\ & =\frac{1}{|𝑆|}⋅\frac{|𝑆|}{2}⋅(𝑎+𝑏) \\ & =\frac{1}{|𝑆|}⋅\frac{|𝑆|}{2}⋅(𝑎+𝑏) \\ & =\frac{𝑎+𝑏}{2}\end{aligned}


$$

as required.

### Proving the Formula for the Variance

Let's now show that for $X\sim \{a, a+1, a+2, \ldots, b\},$ we have

$$


\text{Var}[X] = \dfrac{|S|^2-1}{12}.


$$

We will assume, without loss of generality, that the distribution of our random variable $X$ is given by

$$


X\sim\{1, 2, 3, \ldots, |S|\}.


$$

We do not lose generality here because, in general, the variance (i.e., spread) of a random variable is unaffected by translations:

$$


\text{Var}[X + c] = \text{Var}[X]


$$

By the definition of $\text{E}[X^2],$ we have

$$


\begin{aligned}E[𝑋^{2}] & =\underset{𝑥∈𝑆}{∑}𝑥^{2}𝑓(𝑥) \\ & =\underset{𝑥∈𝑆}{∑}𝑥^{2}⋅\frac{1}{|𝑆|} \\ & =\frac{1}{|𝑆|}⋅\underset{𝑥∈𝑆}{∑}𝑥^{2} \\ & =\frac{1}{|𝑆|}⋅[1^{2}+2^{2}+⋯+|𝑆|^{2}].\end{aligned}


$$

We now make use of the following result:

$$


\sum_{i=1}^n i^2 = \dfrac16 n (n+1)(2n+1)


$$

Therefore,

$$


\begin{aligned}E[𝑋^{2}] & =\frac{1}{|𝑆|}⋅[1^{2}+2^{2}+⋯+|𝑆|^{2}] \\ & =\frac{1}{|𝑆|}⋅\frac{1}{6}⋅|𝑆|⋅(|𝑆|+1)(2|𝑆|+1) \\ & =\frac{1}{|𝑆|}⋅\frac{1}{6}⋅|𝑆|⋅(|𝑆|+1)(2|𝑆|+1) \\ & =\frac{(|𝑆|+1)(2|𝑆|+1)}{6}.\end{aligned}


$$

Next, we use the following results:

$$


\text{Var}[X] = \text{E}[X^2] - \left(\text{E}[X]\right)^2, \qquad \textrm {E}[X] = \dfrac{1+|S|}{2}


$$

Therefore,

$$


\begin{aligned}Var[𝑋] & =E[𝑋^{2}]−(E[𝑋])^{2} \\ & =\frac{(|𝑆|+1)(2|𝑆|+1)}{6}−(\frac{|𝑆|+1}{2})^{2} \\ & =\frac{(|𝑆|+1)(2|𝑆|+1)}{6}−\frac{(|𝑆|+1)^{2}}{4} \\ & =\frac{2(|𝑆|+1)(2|𝑆|+1)}{12}−\frac{3(|𝑆|+1)^{2}}{12} \\ & =\frac{(|𝑆|+1)}{12}(2(2|𝑆|+1)−3(|𝑆|+1)) \\ & =\frac{(|𝑆|+1)}{12}(4|𝑆|+2−3|𝑆|−3) \\ & =\frac{(|𝑆|+1)}{12}(|𝑆|−1) \\ & =\frac{(|𝑆|+1)(|𝑆|−1)}{12} \\ & =\frac{|𝑆|^{2}−1}{12}\end{aligned}


$$

as required.
