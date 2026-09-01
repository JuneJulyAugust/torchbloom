# The Geometric Distribution

Source: https://www.mathacademy.com/topics/3284?courseId=109
Topic ID: 3284

## Prerequisites

- [Exponential Functions](../../../high-school/traditional/lessons/algebra-i/1153-exponential-functions.md)
- [Probability Mass Functions of Discrete Random Variables](./1290-probability-mass-functions-of-discrete-random-variables.md)

## Lesson

### Introduction

A **Bernoulli trial** is a random experiment whose outcome can be interpreted as either "success" or "failure."

For example, suppose we throw a die and define a "success" as the event of getting a six and a "failure" as getting any other number. Then, the throw of a die can be thought of as a Bernoulli trial with the following probabilities:

$$



P(\text{six}) = \dfrac16, \qquad P(\text{not six}) = \dfrac56



$$

Now suppose that a fair die is repeatedly thrown *until* we get a six. What is the probability that we need to throw the die precisely ${\color{blue}{3}}$ times to get our first six?

First, notice that each throw of the die is a Bernoulli trial. And since we throw the die repeatedly until we get a six, we have a *sequence* of Bernoulli trials.

Let $X$ be the number of times the die is thrown until we get a six. We wish to compute $P(X = {\color{blue}{3}}).$

To get our first six on the *third* throw, we need to throw "not a six" on the *first two* throws, followed by a "six" on the *final* throw. Assuming that each throw of the die is independent, by the multiplication law for independent events, we have

$$



\begin{aligned}𝑃(𝑋=3) & =𝑃(not six)⋅𝑃(not six)⋅𝑃(six) \\ & =\frac{5}{6}⋅\frac{5}{6}⋅\frac{1}{6} \\ & =\frac{25}{216}.\end{aligned}



$$

The random variable $X$ in this example follows a so-called **geometric distribution**. Let's now discuss geometric distributions a little more generally.

### The Probability Mass Function of a Geometric Distribution

Suppose that we have a sequence of Bernoulli trials, each resulting in success or failure, and with a probability of success $p.$ Let the random variable $X$ represent the number of Bernoulli trials *until the first success*.

It can be shown that $X$ follows a **geometric distribution** and has the following probability mass function:

$$



\begin{aligned}(1−𝑝)^{𝑥−1}𝑝,\, & 𝑥=1,2,3,… \\ 0, & otherwise\end{aligned}



$$

Let's break this formula down a bit:

- The factor $(1-p)^{x-1}$ represents the probability of getting exactly $(x-1)$ failures, each with probability $(1-p).$

- The factor ${\color{purple}{p}}$ represents the probability of getting a single success.

- The condition $x=1,2,3,\ldots$ indicates that the sequence of Bernoulli trials terminates after a minimum of $1$ trial, and there is no maximum number of trials.

If a random variable $X$ follows a geometric distribution, we say it is a geometric random variable and write

$$



X\sim \text{Geom}(p).



$$

### Applying the Probability Mass Function of a Geometric Distribution

Let $X$ be the number of times a fair die is thrown until we get a six. Since we have a sequence of Bernoulli trials, each with a probability of success $p=\dfrac16,$ the number of throws until the first six can be modeled as a geometric random variable, and we write

$$



X\sim \text{Geom}\left(\dfrac16\right).



$$

Therefore, the probability of getting our first six on the $\color{blue}3$rd roll is

$$



\begin{aligned}𝑃(𝑋=3) & =𝑓(3) \\ & =(1−\frac{1}{6})^{3−1}⋅\frac{1}{6} \\ & =(\frac{5}{6})^{2}⋅\frac{1}{6} \\ & =\frac{25}{36}⋅\frac{1}{6} \\ & =\frac{25}{216}\end{aligned}



$$

which agrees with our previous result.

### Example: Computing a Probability at a Point

#### Question

Given $X \sim \text{Geom}\left(\dfrac{2}{3}\right),$ compute $P(X = 3).$

#### Explanation

If $X \sim \text{Geom}(p),$ then $X$ has the following probability mass function:

$$



\begin{aligned}(1−𝑝)^{𝑥−1}𝑝, & 𝑥=1,2,3,… \\ 0, & otherwise\end{aligned}



$$

Here, $X \sim \text{Geom}\left(\dfrac{2}{3}\right),$ so the distribution of $X$ in this case is

$$



\begin{aligned}(\frac{1}{3})^{𝑥−1}(\frac{2}{3}), & 𝑥=1,2,3,… \\ 0, & otherwise.\end{aligned}



$$

Therefore,

$$



\begin{aligned}𝑃(𝑋=3) & =𝑓(3) \\ & =(\frac{1}{3})^{2}(\frac{2}{3}) \\ & =\frac{2}{27}.\end{aligned}



$$

### Example: Computing a Probability Over a Bounded Interval: Lower Bound is Zero

#### Question

Given $X \sim \text{Geom}\left(\dfrac 37\right),$ compute $P(X < 5).$

#### Explanation

If $X \sim \text{Geom}(p),$ then $X$ has the following probability mass function:

$$



\begin{aligned}(1−𝑝)^{𝑥−1}𝑝, & 𝑥=1,2,3,… \\ 0, & otherwise\end{aligned}



$$

Here, $X \sim \text{Geom}\left(\dfrac 37\right),$ so the distribution of $X$ in this case is

$$



\begin{aligned}(\frac{4}{7})^{𝑥−1}(\frac{3}{7}), & 𝑥=1,2,3,… \\ 0, & otherwise.\end{aligned}



$$

Therefore,

$$



\begin{aligned}𝑃(𝑋<5) & =𝑃(𝑋∈{1,2,3,4}) \\ & =𝑃(𝑋=1)+𝑃(𝑋=2)+𝑃(𝑋=3)+𝑃(𝑋=4) \\ & =𝑓(1)+𝑓(2)+𝑓(3)+𝑓(4) \\ & =(\frac{4}{7})^{0}(\frac{3}{7})+(\frac{4}{7})^{1}(\frac{3}{7})+(\frac{4}{7})^{2}(\frac{3}{7})+(\frac{4}{7})^{3}(\frac{3}{7}) \\ & ≈0.893\end{aligned}



$$

to $3$ decimal places.

### Example: Computing a Probability Over a Bounded Interval: Lower Bound is Not Zero

#### Question

Given that $X \sim \text{Geom}\left(\dfrac 15\right),$ compute $P(2 \leq X \leq 3).$

#### Explanation

If $X \sim \text{Geom}(p),$ then $X$ has the following probability mass function:

$$



\begin{aligned}(1−𝑝)^{𝑥−1}𝑝, & 𝑥=1,2,3,… \\ 0, & otherwise\end{aligned}



$$

Here, $X \sim \text{Geom}\left(\dfrac 15\right),$ so the distribution of $X$ in this case is

$$



\begin{aligned}(\frac{4}{5})^{𝑥−1}(\frac{1}{5}), & 𝑥=1,2,3,… \\ 0, & otherwise.\end{aligned}



$$

Therefore,

$$



\begin{aligned}𝑃(2≤𝑋≤3) & =𝑃(𝑋∈{2,3}) \\ & =𝑃(𝑋=2)+𝑃(𝑋=3) \\ & =𝑓(2)+𝑓(3) \\ & =(\frac{4}{5})^{1}(\frac{1}{5})+(\frac{4}{5})^{2}(\frac{1}{5}) \\ & =\frac{36}{125}.\end{aligned}



$$

### Example: Computing a Probability Over a Bounded Interval Using the Complement

#### Question

Given $X \sim \text{Geom}\left(\dfrac 56\right),$ compute $P(X > 2).$

#### Explanation

If $X \sim \text{Geom}(p),$ then $X$ has the following probability mass function:

$$



\begin{aligned}(1−𝑝)^{𝑥−1}𝑝, & 𝑥=1,2,3,… \\ 0, & otherwise\end{aligned}



$$

Here, $X \sim \text{Geom}\left(\dfrac 56\right),$ so the distribution of $X$ in this case is

$$



\begin{aligned}(\frac{1}{6})^{𝑥−1}(\frac{5}{6}), & 𝑥=1,2,3… \\ 0, & otherwise.\end{aligned}



$$

There are infinitely many values of $X$ such that $X > 2.$ However, we can simplify the computation by using the complement instead:

$$



\begin{aligned}𝑃(𝑋>2) & =1−𝑃(𝑋≤2)\end{aligned}



$$

Computing the complement, we get

$$



\begin{aligned}𝑃(𝑋≤2) & =𝑃(𝑋∈{1,2}) \\ & =𝑃(𝑋=1)+𝑃(𝑋=2) \\ & =𝑓(1)+𝑓(2) \\ & =(\frac{1}{6})^{0}(\frac{5}{6})+(\frac{1}{6})^{1}(\frac{5}{6}) \\ & =\frac{35}{36}.\end{aligned}



$$

Therefore,

$$



\begin{aligned}𝑃(𝑋>2) & =1−𝑃(𝑋≤2) \\ & =1−\frac{35}{36} \\ & =\frac{1}{36}.\end{aligned}



$$

### Showing That a Geometric Distribution Is a Probability Distribution

You might be wondering where the geometric distribution gets its name. The answer is that the probability mass function forms a geometric sequence!

Suppose that $X\sim \text{Geom}(p).$ Then, the probability mass function for this geometric distribution is

$$



\begin{aligned}𝑓(𝑥) & =(1−𝑝)^{𝑥−1}𝑝 \\ 𝑓(𝑥) & =𝑝(1−𝑝)^{𝑥−1} \\ \underset{𝑎_{𝑥}}{\underset{}{𝑓(𝑥)}} & =\underset{𝑎_{1}}{\underset{}{𝑝}}⋅(\underset{𝑟}{\underset{}{1−𝑝}})^{𝑥−1} \\ 𝑎_{𝑥} & =𝑎_{1}⋅𝑟^{𝑥−1}\end{aligned}



$$

So, we see that the probability mass function can be interpreted as a geometric sequence where the first term is $a_1=p,$ and the common ratio is $r=1-p.$

Moreover, notice that $f(x)$ satisfies all the criteria to be a probability mass function, namely

1. $0 \leq f(x) \leq 1$ for all $x$ in $S$

2. $\displaystyle \sum\limits_{x \in S} f(x) = 1$

Criterion 1 is clearly true because $0 \leq p \leq 1.$

To show that criterion 2 is true, we simply need to calculate the sum of this infinite geometric series, as follows:

$$



\begin{aligned}\underset{𝑥∈𝑆}{∑}𝑓(𝑥) & =\underset{\underset{𝑥=1}{∑}}{\overset{}{∞}}𝑝(1−𝑝)^{𝑥−1} \\ & =\frac{𝑝}{1−(1−𝑝)} \\ & =\frac{𝑝}{𝑝} \\ & =1\end{aligned}



$$

Therefore, $f(x)$ is indeed a probability distribution.
