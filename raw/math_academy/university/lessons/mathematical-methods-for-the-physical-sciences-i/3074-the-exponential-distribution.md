# The Exponential Distribution

Source: https://www.mathacademy.com/topics/3074?courseId=154
Topic ID: 3074

## Prerequisites

- [Continuous Random Variables Over Infinite Domains](./4100-continuous-random-variables-over-infinite-domains.md)

## Lesson

### Introduction

A continuous random variable $X$ follows an **exponential distribution** if it has the following probability density function:

$$


\begin{aligned}𝜆𝑒^{−𝜆𝑥},\, & 𝑥≥0 \\ 0, & otherwise\end{aligned}


$$

The **rate parameter** $\lambda$ is a positive real number, and $e\approx 2.71828$ is Euler's number.

If a random variable $X$ follows an exponential distribution, we write

$$


X\sim \textrm{Exp}(\lambda).


$$

The exponential distribution models the amount of continuous space or time between two events. In a future lesson, we will learn how to model situations using the exponential distribution. But for now, let's get some practice working with the PDF to compute probabilities.

### Example: Computing a "Less Than" Probability With the Exponential Distribution

#### Question

Given that the random variable $X\sim \textrm{Exp}\left(1\right),$ calculate $P\left(X < 2\right).$ Round your final answer to four decimal places.

#### Explanation

An exponential random variable $X$ with rate $\lambda$ has the following probability density function:

$$


\begin{aligned}𝜆𝑒^{−𝜆𝑥}, & 𝑥≥0 \\ 0, & otherwise\end{aligned}


$$

We're given that

$$


X\sim \textrm{Exp} \left( 1 \right).


$$

So, $X$ has the following probability density function:

$$


\begin{aligned}𝑒^{−𝑥}, & 𝑥≥0 \\ 0, & otherwise\end{aligned}


$$

Therefore, we can calculate $P\left(X < 2\right)$ as follows:

$$


\begin{aligned}𝑃(𝑋<2) & =∫_{20}^{}𝑓(𝑥)\,d𝑥 \\ & =∫_{20}^{}𝑒^{−𝑥}\,d𝑥 \\ & =−𝑒^{−𝑥}_{20}^{} \\ & =−𝑒^{−2}+𝑒^{0} \\ & ≈0.8647\end{aligned}


$$

### Example: Computing a "Greater Than" Probability With the Exponential Distribution

#### Question

Given that the random variable $X\sim \textrm{Exp}\left(\dfrac 23\right),$ calculate $P\left(X \geq 3\right).$ Round your final answer to four decimal places.

#### Explanation

An exponential random variable $X$ with rate $\lambda$ has the following probability density function:

$$


\begin{aligned}𝜆𝑒^{−𝜆𝑥}, & 𝑥≥0 \\ 0, & otherwise\end{aligned}


$$

We're given that

$$


X\sim \textrm{Exp} \left( \dfrac 23 \right).


$$

So, $X$ has the following probability density function:

$$


\begin{aligned}\frac{2}{3}𝑒^{−2𝑥/3}, & 𝑥≥0 \\ 0, & otherwise\end{aligned}


$$

Therefore, we can calculate $P\left(X \geq 3\right)$ as follows:

$$


\begin{aligned}𝑃(𝑋≥3) & =∫_{∞3}^{}𝑓(𝑥)\,d𝑥 \\ & =∫_{∞3}^{}\frac{2}{3}𝑒^{−2𝑥/3}\,d𝑥 \\ & =−𝑒^{−2𝑥/3}_{∞3}^{} \\ & =𝑒^{−2} \\ & ≈0.1353\end{aligned}


$$

### Example: Computing a Probability on a Bounded Interval Using the Exponential Distribution

#### Question

Given that the random variable $X\sim \textrm{Exp}\left(2\right),$ calculate $P\left(\dfrac 12 < X < 2\right).$ Round your final answer to four decimal places.

#### Explanation

An exponential random variable $X$ with rate $\lambda$ has the following probability density function:

$$


\begin{aligned}𝜆𝑒^{−𝜆𝑥}, & 𝑥≥0 \\ 0, & otherwise\end{aligned}


$$

We're given that

$$


X\sim \textrm{Exp} \left( 2 \right).


$$

So, $X$ has the following probability density function:

$$


\begin{aligned}2𝑒^{−2𝑥}, & 𝑥≥0 \\ 0, & otherwise\end{aligned}


$$

Therefore, we can calculate $P\left(\dfrac 12 < X < 2\right)$ as follows:

$$


\begin{aligned}𝑃(\frac{1}{2}<𝑋<2) & =∫_{21/2}^{}𝑓(𝑥)\,d𝑥 \\ & =∫_{21/2}^{}2𝑒^{−2𝑥}\,d𝑥 \\ & =−𝑒^{−2𝑥}_{21/2}^{} \\ & =−𝑒^{−4}+𝑒^{−1} \\ & ≈0.3496\end{aligned}


$$

### The Memoryless Property

Consider a random variable $X \sim \mathrm{Exp}(\lambda),$ and two positive real numbers $s, t.$

Suppose we're given that $X>s,$ and we want to determine the probability that $X>s+t.$ In other words, we wish to compute the conditional probability

$$


P(X>s+t \,\big|\, X>s).


$$

By the definition of conditional probability, we have that

$$


P(X>s+t \, \big|\, X>s) = \dfrac{P\big((X> s+t) \cap (X > s)\big)}{P(X>s)}.


$$

Notice that $X>s+t$ implies that $X>s,$ therefore

$$


P\big((X> s+t) \cap (X > s)\big) = P(X > s+t).


$$

So, the above conditional probability simplifies to

$$


P(X>s+t \,\big|\, X>s) = \dfrac{P(X> s+t )}{P(X>s)}.


$$

Next, let's recall how to calculate $P(X > a)$ for some $a>0{:}$

$$


\begin{aligned}𝑃(𝑋>𝑎) & =1−𝑃(𝑋<𝑎) \\ & =1−∫_{𝑎0}^{}𝜆𝑒^{−𝜆𝑥}\,d𝑥 \\ & =1+𝑒^{−𝜆𝑥}_{𝑎0}^{} \\ & =1+𝑒^{−𝜆𝑎}−𝑒^{0} \\ & =𝑒^{−𝜆𝑎}.\end{aligned}


$$

Therefore, we can use this fact to calculate $P(X> s+t)$ and $P(X>s)$

$$


\begin{aligned}𝑃(𝑋>𝑠+𝑡\,\,𝑋>𝑠) & =\frac{𝑃(𝑋>𝑠+𝑡)}{𝑃(𝑋>𝑠)} \\ & =\frac{𝑒^{−𝜆(𝑠+𝑡)}}{𝑒^{−𝜆𝑠}} \\ & =\frac{𝑒^{−𝜆𝑠}⋅𝑒^{−𝜆𝑡}}{𝑒^{−𝜆𝑠}} \\ & =\frac{𝑒^{−𝜆𝑠}⋅𝑒^{−𝜆𝑡}}{𝑒^{−𝜆𝑠}} \\ & =𝑒^{−𝜆𝑡}\end{aligned}


$$

Finally, notice that $e^{-\lambda t} = P(X > t).$ So, we have proved the following property:

$$


P(X>s+t \big| X>s) = P(X > t).


$$

This property is called **memoryless property.** It can be proved that the exponential distribution is the only continuous distribution with this property (note that the geometric distribution is the only *discrete* distribution with the memoryless property).

Intuitively, the memoryless property states that the probability of an event occurring after a certain amount of time has already elapsed is independent of how much time has passed. This means that the distribution "forgets" what has happened before time $s.$

We'll discuss how the memoryless property is used for mathematical modeling in future lessons.

### A Worked Example

Given that the random variable $X\sim \textrm{Exp}(2),$ let's calculate the following probability:

$$


P\left(X > \dfrac32 \,\bigg|\, X > \dfrac12\right)


$$

Given a random variable $X \sim \mathrm{Exp}(\lambda)$ and two positive real numbers $s, t,$ the memoryless property of the exponential distribution states that

$$


P(X>s+t \, \big|\, X>s) = P(X > t) = e^{-\lambda t}.


$$

In our case, we have

$$


\lambda = 2, \qquad s=\dfrac 12,\qquad s+t=\dfrac32.


$$

From this, we can find $t$ as follows:

$$


t = (t+s) - s = \dfrac32-\dfrac12 = 1


$$

Substituting these values into the above formula, we get

$$


\begin{aligned}𝑃(𝑋>\frac{3}{2}\,\,𝑋>\frac{1}{2}) & =𝑒^{−𝜆𝑡} \\ & =𝑒^{−(2)⋅(1)} \\ & =𝑒^{−2} \\ & =\frac{1}{𝑒^{2}} \\ & ≈0.135\end{aligned}


$$

### Example: Calculating Probabilities Using the Memoryless Property

#### Question

Given that the random variable $X\sim \textrm{Exp}\left(4\right),$ calculate $P\left(X \leq 7 \, \bigg |\, X > 5\right).$

#### Explanation

Given a random variable $X \sim \mathrm{Exp}(\lambda)$ and two positive real numbers $s, t,$ the memoryless property of the exponential distribution states that

$$


P(X>s+t \, \big |\, X>s) = P(X > t) = e^{-\lambda t}.


$$

We can compute the complementary conditional probability as follows:

$$


P(X\leq s+t \, \big|\, X>s) = 1-P(X>s+t \, \big |\, X>s) = 1-e^{-\lambda t}


$$

In our case, we have $\lambda = 4,$ $s=5,$ and $s+t=7.$ From this, we can find $t$ as follows:

$$


t = (t+s) - s =7 - 5 = 2


$$

Substituting these values into the above formula, we get

$$


\begin{aligned}𝑃(𝑋≤7\,\,𝑋>5) & =1−𝑒^{−𝜆𝑡} \\ & =1−𝑒^{−(4)⋅(2)} \\ & =1−𝑒^{−8} \\ & ≈0.999\,664.\end{aligned}


$$
