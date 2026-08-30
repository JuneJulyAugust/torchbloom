# Variance of Discrete Random Variables

Source: https://www.mathacademy.com/topics/1388?courseId=154
Topic ID: 1388

## Prerequisites

- [Variance and Standard Deviation](../integrated-math-ii-honors/1632-variance-and-standard-deviation.md)
- [Moments of Discrete Random Variables](./3642-moments-of-discrete-random-variables.md)

## Lesson

### Introduction

The **variance** of a discrete random variable $X$ with probability mass function $f(x)$ defined over a set $S$ is given by

$$


\textrm{Var}[X] = \sum\limits_{x \in S} (x - \textrm E[X])^2 \cdot f(x).


$$

In other words, the variance is the expected value of the squared difference between $X$ and the expected value of $X{:}$

$$


\textrm{Var}[X] = \textrm E [ (X - \textrm E[X])^2 ]


$$

The variance quantifies how "spread out" a probability distribution is. The expected value $\textrm E[X]$ can be interpreted as the "center" of a probability distribution, and the squared difference $(X - \textrm E[X])^2$ represents the squared distance between $X$ and the center. So, the variance quantifies how far the possible values of $X$ are from the center, on average.

In general,

- a probability distribution that is *spread out* over many possible values will have a *high* variance, while

- a probability distribution that is *concentrated* (or *clumped*) near a single value will have a *low* variance.

### Example: Computing Variance Using the Definition Given a Probability Mass Function

#### Question

Let $X$ be the number obtained by a spinner with four sections labeled $1, 2, 3, 4.$ The probability mass function $f(x)$ of $X$ is shown in the table below. What is $\textrm{Var}[X]?$

#### Explanation

The variance of a discrete random variable $X$ with probability mass function $f(x)$ defined over a set $S$ is given by

$$


\textrm{Var}[X] = \sum\limits_{x \in S} (x - \textrm E[X])^2 \cdot f(x).


$$

First, we need to compute $\textrm E[X].$ Summing up the products of each value of $X$ and its associated probability, we get

$$


\begin{aligned}E[𝑋] & =1⋅𝑓(1)+2⋅𝑓(2)+3⋅𝑓(3)+4⋅𝑓(4) \\ & =1(\frac{1}{6})+2(\frac{1}{4})+3(\frac{1}{3})+4(\frac{1}{4}) \\ & =\frac{8}{3}.\end{aligned}


$$

Substituting $\textrm E[X]=\dfrac{8}{3}$ into the variance formula, we get

$$


\textrm{Var}[X] = \sum\limits_{x \in S} \left(x - \dfrac{8}{3} \right)^2 \cdot f(x).


$$

Now, we compute the variance as follows:

$$


\begin{aligned}Var[𝑋] & =(1−\frac{8}{3})^{2}⋅𝑓(1)+(2−\frac{8}{3})^{2}⋅𝑓(2)+(3−\frac{8}{3})^{2}⋅𝑓(3)+(4−\frac{8}{3})^{2}⋅𝑓(4) \\ & =\frac{25}{9}⋅𝑓(1)+\frac{4}{9}⋅𝑓(2)+\frac{1}{9}⋅𝑓(3)+\frac{16}{9}⋅𝑓(4) \\ & =\frac{25}{9}(\frac{1}{6})+\frac{4}{9}⋅(\frac{1}{4})+\frac{1}{9}⋅(\frac{1}{3})+\frac{16}{9}(\frac{1}{4}) \\ & =\frac{19}{18}\end{aligned}


$$

### A Formula for Quickly Computing the Variance

Using the properties of the expected value of a discrete random variable $X,$ we can arrive at the following alternative formula for the variance of $X{:}$

$$


\textrm{Var}[X] = \textrm E [ X^2 ] - \textrm E[X]^2


$$

As we will see in the following example, using this formula often speeds up the process of computing the variance.

### Example: Computing Variance Given the Expected Value of a Random Variable and Its Square

#### Question

If $\textrm E[X] = 4$ and $\textrm E[X^2] = 21,$ then what is $\textrm{Var}[X]?$

#### Explanation

We can compute the variance of a discrete random variable $X$ using the following formula:

$$


\textrm{Var}[X] = \textrm E[X^2] - \textrm E[X]^2


$$

Substituting the given values, we get

$$


\begin{aligned}Var[𝑋] & =21−4^{2} \\ & =21−16 \\ & =5\end{aligned}


$$

### Example: Computing Variance Given a Probability Mass Function

#### Question

A fair die with sides labeled with numbers $1$ through $6$ is thrown once. If $X$ is the outcome of the die, what is the variance of $X?$

#### Explanation

We can compute the variance of a discrete random variable $X$ using the following formula:

$$


\textrm{Var}[X] = \textrm E[X^2] - \textrm E[X]^2


$$

First, we need to compute the probability mass function $f(x).$ Here, there are $6$ possible outcomes ($1,2,3,4,5,6$) and each outcome has the same probability, so the probability mass function is as follows:

Next, we compute $\textrm E[X].$ Summing up the products of each value of $X$ and its associated probability, we get

$$


\begin{aligned}E[𝑋] & =1⋅𝑓(1)+2⋅𝑓(2)+3⋅𝑓(3)+4⋅𝑓(4)+5⋅𝑓(5)+6⋅𝑓(6) \\ & =1(\frac{1}{6})+2(\frac{1}{6})+3(\frac{1}{6})+4(\frac{1}{6})+5(\frac{1}{6})+6(\frac{1}{6}) \\ & =\frac{7}{2}.\end{aligned}


$$

Now, we compute $\textrm E[X^2].$ Summing up the products of each value of $X^2$ and its associated probability, we get

$$


\begin{aligned}E[𝑋^{2}] & =1^{2}⋅𝑓(1)+2^{2}⋅𝑓(2)+3^{2}⋅𝑓(3)+4^{2}⋅𝑓(4)+5^{2}⋅𝑓(5)+6^{2}⋅𝑓(6) \\ & =1(\frac{1}{6})+4(\frac{1}{6})+9(\frac{1}{6})+16(\frac{1}{6})+25(\frac{1}{6})+36(\frac{1}{6}) \\ & =\frac{91}{6}.\end{aligned}


$$

Therefore,

$$


\begin{aligned}Var[𝑋] & =E[𝑋^{2}]−E[𝑋]^{2} \\ & =\frac{91}{6}−(\frac{7}{2})^{2} \\ & =\frac{91}{6}−\frac{49}{4} \\ & =\frac{35}{12}.\end{aligned}


$$

### The Standard Deviation of a Random Variable

The **standard deviation** of a random variable $X$ is defined as the square root of the variance:

$$


\textrm{SD}[X] = \sqrt{ \textrm{Var}[X] }


$$

As we will see in the future, the standard deviation is often used when we observe a random variable and wish to quantify how "surprising" a particular observation was.

In those contexts, we often compute how many standard deviations the observed value was away from the expected value: the further away, the more surprising the observation.

For now, though, let's get some practice computing the standard deviation of a random variable.

### Example: Computing the Standard Deviation of a Random Variable

#### Question

A fair die with sides labeled with numbers $1$ through $6$ is thrown once. If $X$ is the outcome of the die, what is $\textrm{SD}[X]?$

#### Explanation

The standard deviation of a random variable $X$ is defined as

$$


\textrm{SD}[X] = \sqrt{ \textrm{Var}[X] },


$$

where the variance can be computed using the following formula:

$$


\textrm{Var}[X] = \textrm E[X^2] - \textrm E[X]^2


$$

First, we need to compute the probability mass function $f(x).$ Here, there are $6$ possible outcomes ($1,2,3,4,5,6$) and each outcome has the same probability, so the probability mass function is as follows:

Next, we compute $\textrm E[X].$ Summing up the products of each value of $X$ and its associated probability, we get

$$


\begin{aligned}E[𝑋] & =1⋅𝑓(1)+2⋅𝑓(2)+3⋅𝑓(3)+4⋅𝑓(4)+5⋅𝑓(5)+6⋅𝑓(6) \\ & =1(\frac{1}{6})+2(\frac{1}{6})+3(\frac{1}{6})+4(\frac{1}{6})+5(\frac{1}{6})+6(\frac{1}{6}) \\ & =\frac{7}{2}.\end{aligned}


$$

Now, we compute $\textrm E[X^2].$ Summing up the products of each value of $X^2$ and its associated probability, we get

$$


\begin{aligned}E[𝑋^{2}] & =1^{2}⋅𝑓(1)+2^{2}⋅𝑓(2)+3^{2}⋅𝑓(3)+4^{2}⋅𝑓(4)+5^{2}⋅𝑓(5)+6^{2}⋅𝑓(6) \\ & =1(\frac{1}{6})+4(\frac{1}{6})+9(\frac{1}{6})+16(\frac{1}{6})+25(\frac{1}{6})+36(\frac{1}{6}) \\ & =\frac{91}{6}.\end{aligned}


$$

Therefore,

$$


\begin{aligned}Var[𝑋] & =E[𝑋^{2}]−E[𝑋]^{2} \\ & =\frac{91}{6}−(\frac{7}{2})^{2} \\ & =\frac{91}{6}−\frac{49}{4} \\ & =\frac{35}{12}.\end{aligned}


$$

Finally,

$$


\begin{aligned}SD[𝑋] & =\sqrt{√Var[𝑋]} \\ & =\sqrt{√\frac{35}{12}}.\end{aligned}


$$

### Proving the Formula For the Variance in Terms of First and Second Raw Moments

We wish to prove the following formula for the variance:

$$


\textrm{Var}[X] = \textrm{E}[X^2] - \textrm{E}[X]^2


$$

To begin, recall that the variance of a random variable $X$ is defined as

$$


\textrm{Var}[X] = \textrm E [ (X - \textrm E[X])^2 ].


$$

Expanding out the perfect square, we get

$$


\textrm{Var}[X] =\textrm E [ X^2 - 2\textrm E[X] \cdot X + \textrm E[X]^2 ] .


$$

Then, distributing the expectation over the sum, we get

$$


\textrm{Var}[X] = \textrm E [ X^2 ] + \textrm E[ - 2\textrm E[X] \cdot X ] + \textrm E[ \textrm E[X]^2 ] .


$$

Now, we make the following simplifications:

- Since $\textrm E[aX] = a \textrm E[X]$ for any constant $a,$ we can write

- Since $\textrm{E}[X]$ is a constant, and $\textrm E[a] = a$ for any constant $a,$ we can write

So, we have

$$


\begin{aligned}Var[𝑋] & =E[𝑋^{2}]+E[−2E[𝑋]⋅𝑋]+E[𝐸[𝑋]^{2}] \\ & =E[𝑋^{2}]−2E[𝑋]^{2}+E[𝑋]^{2} \\ & =E[𝑋^{2}]−E[𝑋]^{2}.\end{aligned}


$$
