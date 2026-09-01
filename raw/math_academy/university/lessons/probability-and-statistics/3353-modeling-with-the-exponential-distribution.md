# Modeling With the Exponential Distribution

Source: https://www.mathacademy.com/topics/3353?courseId=73
Topic ID: 3353

## Prerequisites

- [Modeling With the Geometric Distribution](./2839-modeling-with-the-geometric-distribution.md)
- [The Exponential Distribution](./3074-the-exponential-distribution.md)

## Lesson

### Introduction

A **Poisson process** is a mathematical model used to describe events occurring randomly over continuous space or time. A Poisson process is characterized by the following properties:

- Events occur *independently*. In other words, one event's occurrence does not affect another event's likelihood.

- Events occur at a *constant average rate*. The rate at which events occur represents the expected number of events per unit of time or space.

We encountered the exponential distribution in a previous lesson. The exponential distribution models the amount of continuous space or time $X$ between two events in a Poisson process with success rate $\lambda.$

We have already seen that if $X\sim \text{Exp}(\lambda)$ follows an exponential distribution, then the probability density function of $X$ is given by

$$


\begin{aligned}𝜆𝑒^{−𝜆𝑥},\, & 𝑥≥0 \\ 0, & otherwise.\end{aligned}


$$

The exponential distribution is often considered the continuous analog of the geometric distribution. Recall that the geometric distribution models the number of trials before the first success in a sequence of independent Bernoulli trials.

For example, suppose a call center receives telephone calls at an average rate of $3$ calls per minute. If the random variable $X$ represents the amount of time between two consecutive calls, then $X$ can be modeled using an exponential distribution, and we write

$$


X\sim \text{Exp}(3).


$$

Therefore, the probability that the time between two consecutive calls is less than one minute is given by

$$


\begin{aligned}𝑃(𝑋<1) & =∫_{10}3𝑒^{−3𝑥}\,d𝑥 \\ & =−𝑒^{−3𝑥}_{10} \\ & =[−𝑒^{−3}]−[−𝑒^{0}] \\ & =[−𝑒^{−3}]+[1] \\ & =1−𝑒^{−3} \\ & ≈0.9502.\end{aligned}


$$

Intuitively, this makes sense. If the call center receives calls at an average rate of $3$ per minute, then the probability of waiting less than one minute until the next call is received should be relatively large.

### Example: Identifying Situations That Can Be Modeled Using an Exponential Distribution

#### Question

Which of the following random variables could be modeled by an exponential distribution?

1. The time interval between successive arrivals of customers in a store

2. The number of customers in a store at a particular time

3. The weight of a child at birth

#### Explanation

The exponential distribution can be thought of as the continuous analog of the geometric distribution. It models the amount of continuous time or space until a particular event occurs, where the events should occur independently and at a constant average rate.

With that in mind, let's consider each of the given random variables.

- Random variable I could be modeled using an exponential distribution. Customer arrivals can be modeled as independent events with a constant average rate, and we wish to know the amount of time until the next customer enters the store.

- Random variable II does ** follow an exponential distribution. There is no interval of continuous time or space. The number of customers in a store is discrete, not continuous.

- Random variable III does ** follow an exponential distribution. There are no events that occur at a constant average rate.

Therefore, the correct answer is "I only."

### Example: Computing Probabilities With Exponential Random Variables on a Bounded Interval

#### Question

At an electronics store, smartphone purchases occur continuously in time, independently, and at a constant average rate of one sale every $20$ minutes. Rounded to four decimal places, what is the probability that the next smartphone is sold within the next $5$ minutes?

#### Explanation

Since the purchases occur continuously in time, independently, and at a constant average rate, we can model the time until the next purchase as an exponential distribution.

An exponential random variable $X$ with rate $\lambda$ has the following probability density function:

$$


\begin{aligned}𝜆𝑒^{−𝜆𝑥},\, & 𝑥≥0 \\ 0, & otherwise\end{aligned}


$$

Let $X$ be the amount of time until the next smartphone is purchased. Since there is a purchase every $20$ minutes on average, the rate is $\lambda = 1/20$ purchases per minute.

The time intervals between successive purchases can be modeled as an exponential random variable with rate $\lambda = 1/20,$ and we can write

$$


X\sim \text{Exp} \left( \dfrac{1}{20} \right).


$$

So, $X$ has the following probability density function:

$$


\begin{aligned}\frac{1}{20}𝑒^{−𝑥/20}, & 𝑥≥0 \\ 0, & otherwise\end{aligned}


$$

Therefore, the probability that a customer will purchase a smartphone within the next $5$ minutes is

$$


\begin{aligned}𝑃(𝑋<5) & =∫_{50}𝑓(𝑥)\,d𝑥 \\ & =∫_{50}\frac{1}{20}𝑒^{−𝑥/20}\,d𝑥 \\ & =−𝑒^{−𝑥/20}_{50} \\ & =−𝑒^{−1/4}+𝑒^{0} \\ & =1−𝑒^{−1/4} \\ & ≈0.2212\,.\end{aligned}


$$

### Example: Computing Probabilities With Exponential Random Variables on a Unbounded Interval

#### Question

At a clothing store, customers purchase clothes for newborns continuously in time, independently, and at a constant average rate of one sale every $30$ minutes. What is the probability that it takes more than $60$ minutes to sell the next set of newborn clothes?

#### Explanation

Since the purchases occur continuously in time, independently, and at a constant average rate, we can model the time until the next purchase as an exponential distribution.

An exponential random variable $X$ with rate $\lambda$ has the following probability density function:

$$


\begin{aligned}𝜆𝑒^{−𝜆𝑥}, & 𝑥≥0 \\ 0, & otherwise\end{aligned}


$$

Let $X$ be the amount of time until the next set of newborn clothes is sold. Since there is a purchase every $30$ minutes on average, the rate is $\lambda =1/30$ purchases per minute.

The time intervals between successive purchases can be modeled as an exponential random variable with rate $\lambda =1/30,$ and we can write

$$


X\sim \text{Exp} \left( \dfrac{1}{30} \right).


$$

So, $X$ has the following probability density function:

$$


\begin{aligned}\frac{1}{30}𝑒^{−𝑥/30}, & 𝑥≥0 \\ 0, & otherwise\end{aligned}


$$

Therefore, the probability that it takes more than $60$ minutes to sell the next set of newborn clothes is

$$


\begin{aligned}𝑃(𝑋≥60) & =∫_{∞60}𝑓(𝑥)\,d𝑥 \\ & =∫_{∞60}\frac{1}{30}𝑒^{−𝑥/30}\,d𝑥 \\ & =−𝑒^{−𝑥/30}_{∞60} \\ & =−𝑒^{−∞}+𝑒^{−2} \\ & =0+𝑒^{−2} \\ & =𝑒^{−2} \\ & ≈0.1353.\end{aligned}


$$

### Modeling Using the Memoryless Property

The memoryless property of the exponential distribution states that the probability of an event occurring in the future is independent of the time already passed.

For a random variable $X$, the probability that the event occurs in the next $t$ units of time, given it hasn't occurred after $s$ units of elapsed time, is

$$


P(X > s + t \mid X > s) = P(X > t) = e^{-\lambda t}.


$$

Suppose you have a radioactive particle whose decay time $X$ follows the exponential distribution with rate $\lambda = 0.8 \text{decays/minute}.$

Then, the probability that the particle will decay in the first minute is

$$


\begin{aligned}𝑃(𝑋<1) & =∫_{10}𝑓(𝑥)\,d𝑥 \\ & =∫_{10}0.8𝑒^{−0.8𝑥}\,d𝑥 \\ & =−𝑒^{−0.8𝑥}_{10} \\ & =−𝑒^{−0.8}+𝑒^{0} \\ & =1−𝑒^{−0.8} \\ & ≈0.5507.\end{aligned}


$$

Suppose the particle doesn't decay in the first minute. What is the probability that it will decay in the next minute? We can answer this question using the memoryless property.

By the memoryless property, we have

$$


P(X > s + t \mid X > s) = P(X > t) = e^{-\lambda t}.


$$

Taking the complement of this event, we have

$$


P(X < s+t \, \big|\, X>s) = P(X < t) = 1-e^{-\lambda t}.


$$

In our case, we have that $s=1$ and $t=1,$ so

$$


P(X < 1+1 \, \big|\, X>1) = P(X < 1) \approx 0.5507


$$

In other words, even if the particle has survived for one minute, the probability that it will decay in the next minute remains the same as at the start of the observations.

### Example: Computing Probabilities Using the Memoryless Property

#### Question

A malfunctioning internet server approves connection requests continuously in time, independently, and at a constant average rate of $2$ requests per minute. If a user has been waiting for $30$ seconds to connect, what is the probability that they will have to wait at least $20$ more seconds?

#### Explanation

Since connection request approval occurs continuously, independently, and at a constant average rate, we can model the time until the next request is approved using an exponential distribution.

Let $X$ be the user's waiting time in seconds. Since the server approves $2$ requests per minute on average (or $1$ request every $30$ seconds), the rate is $\lambda = \dfrac{1}{30}$ requests per second, and we can write

$$


X\sim \text{Exp} \left( \dfrac{1}{30} \right).


$$

Recall that exponential random variables have the memoryless property. So, given two positive real numbers $s, t,$ we have that

$$


P(X>s+t \, \big|\, X>s) = P(X > t) = e^{-\lambda t}.


$$

In our case, we have $\lambda = \dfrac{1}{30},$ $s=30,$ and $t=20.$

Substituting these values into the above formula, we get

$$


\begin{aligned}𝑃(𝑋>30+20\,\,𝑋>30) & =𝑃(𝑋>20) \\ & =𝑒^{−𝜆𝑡} \\ & =𝑒^{−(1/30)⋅(20)} \\ & =𝑒^{−2/3} \\ & ≈0.513.\end{aligned}


$$
