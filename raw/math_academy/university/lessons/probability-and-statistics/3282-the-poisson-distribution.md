# The Poisson Distribution

Source: https://www.mathacademy.com/topics/3282?courseId=73
Topic ID: 3282

## Prerequisites

- [Factorials](../../../high-school/traditional/lessons/geometry/774-factorials.md)
- [Exponential Functions](../../../high-school/traditional/lessons/algebra-i/1153-exponential-functions.md)
- [Probability Mass Functions of Discrete Random Variables](../discrete-mathematics/1290-probability-mass-functions-of-discrete-random-variables.md)

## Lesson

### Introduction

A discrete random variable $X$ follows a **Poisson distribution** (pronounced "pwaas-on") if it has the following probability mass function:

$$


f(x) = \dfrac{\lambda^x e^{-\lambda}}{x!}, \qquad x=0,1,2,\ldots


$$

The **rate parameter** $\lambda$ is a positive real number, and $e\approx 2.71828$ is Euler's number.

If a random variable $X$ follows a Poisson distribution, we write

$$


X \sim \textrm{Po}(\lambda).


$$

The Poisson distribution models the number of independent events $X$ that occur within a fixed interval of space or time. The parameter $\lambda$ represents the mean number of events that occur in an interval (we'll justify this in a future lesson).

For example, suppose that an average of $\lambda={\color{blue}2}$ buses stop at a particular bus shelter every $10$ minutes. The number of buses that stop at the shelter in a randomly selected $10$-minute period can be modeled by a Poisson random variable

$$


X \sim \textrm{Po}({\color{blue}2}).


$$

Therefore, the probability that $X={\color{red}3}$ buses will stop at the shelter in the next $10$ minutes is

$$


\begin{aligned}𝑃(𝑋=3) & =𝑓(3) \\ & =\frac{2^{3}𝑒^{−2}}{3!} \\ & ≈0.1804,\end{aligned}


$$

rounded to $4$ decimal places.

We will learn more about modeling situations using Poisson random variables shortly. But for now, let's concentrate on computing probabilities for Poisson random variables.

### Example: Computing a Probability at a Point

#### Question

Given $X \sim \textrm{Po}(4),$ compute $P(X = 2),$ rounded to $4$ decimal places.

#### Explanation

If $X \sim \textrm{Po}(\lambda),$ then $X$ has the following probability mass function:

$$


f(x) = \dfrac{\lambda^x e^{-\lambda}}{x!}


$$

Here, $X \sim \textrm{Po}(4),$ so the distribution of $X$ in this case is

$$


f(x) = \dfrac{4^x e^{-4}}{x!}.


$$

Therefore,

$$


\begin{aligned}𝑃(𝑋=2) & =𝑓(2) \\ & =\frac{4^{2}𝑒^{−4}}{2!} \\ & ≈0.1465.\end{aligned}


$$

### Example: Computing a Probability Over a Bounded Interval: Lower Bound is Zero

#### Question

Given $X \sim \textrm{Po}(5),$ compute $P(X < 3),$ rounded to $4$ decimal places.

#### Explanation

If $X \sim \textrm{Po}(\lambda),$ then $X$ has the following probability mass function:

$$


f(x) = \dfrac{\lambda^x e^{-\lambda}}{x!}


$$

Here, $X \sim \textrm{Po}(5),$ so the probability distribution of $X$ in this case is

$$


f(x) = \dfrac{5^x e^{-5}}{x!}.


$$

Therefore,

$$


\begin{aligned}𝑃(𝑋<3) & =𝑃(𝑋∈{0,1,2}) \\ & =𝑃(𝑋=0)+𝑃(𝑋=1)+𝑃(𝑋=2) \\ & =𝑓(0)+𝑓(1)+𝑓(2) \\ & =\frac{5^{0}𝑒^{−5}}{0!}+\frac{5^{1}𝑒^{−5}}{1!}+\frac{5^{2}𝑒^{−5}}{2!} \\ & ≈0.1247.\end{aligned}


$$

### Example: Computing a Probability Over a Bounded Interval: Lower Bound is Not Zero

#### Question

Given $X \sim \textrm{Po}(3),$ compute $P(2 < X < 5),$ rounded to $4$ decimal places.

#### Explanation

If $X \sim \textrm{Po}(\lambda),$ then $X$ has the following probability mass function:

$$


f(x) = \dfrac{\lambda^x e^{-\lambda}}{x!}


$$

Here, $X \sim \textrm{Po}(3),$ so the probability distribution of $X$ in this case is

$$


f(x) = \dfrac{3^x e^{-3}}{x!}.


$$

Therefore,

$$


\begin{aligned}𝑃(2<𝑋<5) & =𝑃(𝑋∈{3,4}) \\ & =𝑃(𝑋=3)+𝑃(𝑋=4) \\ & =𝑓(3)+𝑓(4) \\ & =\frac{3^{3}𝑒^{−3}}{3!}+\frac{3^{4}𝑒^{−3}}{4!} \\ & ≈0.3921.\end{aligned}


$$

### Example: Computing a Probability Over an Unbounded Interval Using the Complement

#### Question

Given $X \sim \textrm{Po}(3),$ compute $P(X > 2),$ rounded to $4$ decimal places.

#### Explanation

If $X \sim \textrm{Po}(\lambda),$ then $X$ has the following probability mass function:

$$


f(x) = \dfrac{\lambda^x e^{-\lambda}}{x!}


$$

Here, $X \sim \textrm{Po}(3),$ so the probability distribution of $X$ in this case is

$$


f(x) = \dfrac{3^x e^{-3}}{x!}.


$$

There are infinitely many values of $X$ such that $X > 2.$ However, we can simplify the computation by using the complement instead:

$$


\begin{aligned}𝑃(𝑋>2) & =1−𝑃(𝑋≤2)\end{aligned}


$$

Computing the complement, we get

$$


\begin{aligned}𝑃(𝑋≤2) & =𝑃(𝑋∈{0,1,2}) \\ & =𝑃(𝑋=0)+𝑃(𝑋=1)+𝑃(𝑋=2) \\ & =𝑓(0)+𝑓(1)+𝑓(2) \\ & =\frac{3^{0}𝑒^{−3}}{0!}+\frac{3^{1}𝑒^{−3}}{1!}+\frac{3^{2}𝑒^{−3}}{2!} \\ & ≈0.4232.\end{aligned}


$$

Therefore,

$$


\begin{aligned}𝑃(𝑋>2) & =1−𝑃(𝑋≤2) \\ & ≈1−0.4232 \\ & =0.5768.\end{aligned}


$$

### Justification That the Poisson Distribution Forms a Probability Distribution

Recall that for a function $f(x)$ with support $S$ to be a valid probability mass function for a discrete random variable $X,$ it must satisfy the following conditions:

- $0 \leq f(x) \leq 1$ for all $x$ in $S$

- $\displaystyle \sum\limits_{x \in S} f(x) = 1$

Let's check these two conditions for the Poisson distribution. First, let's write down the pmf of a Poisson random variable:

$$


f(x) = \dfrac{\lambda^x e^{-\lambda}}{x!}, \qquad x=0,1,2,3, \ldots


$$

We'll also make use of the following result:

$$


e^{\lambda} = \sum\limits_{x = 0}^\infty \dfrac{\lambda^x}{x!}


$$

You'll learn where this result comes from when you study calculus. But for now, let's assume it's true.

Using this result, we can show that $\displaystyle \sum\limits_{x \in S} f(x) = 1$ is true as follows:

$$


\begin{aligned}\underset{𝑥∈𝑆}{∑}𝑓(𝑥) & =\underset{\underset{𝑥=0}{∑}}{\overset{}{∞}}𝑓(𝑥) \\ & =\underset{\underset{𝑥=0}{∑}}{\overset{}{∞}}\frac{𝜆^{𝑥}𝑒^{−𝜆}}{𝑥!} \\ & =𝑒^{−𝜆}\underset{\underset{𝑥=0}{∑}}{\overset{}{∞}}\frac{𝜆^{𝑥}}{𝑥!} \\ & =𝑒^{−𝜆}⋅𝑒^{𝜆} \\ & =𝑒^{0} \\ & =1\end{aligned}


$$

Next, we note that

$$


f(x) = \dfrac{\lambda^x e^{-\lambda}}{x!} \geq 0


$$

for all $x$ because $\lambda^x,$ $e^{-\lambda},$ and $x!$ are all positive. Furthermore, because $f(x)$ is non-negative and the sum of all values is $1,$ we must have $f(x) \leq 1$ for all $x.$ Therefore, $0 \leq f(x) \leq 1.$

Finally, we conclude that $f(x)$ is a valid probability mass function.
