# The Bernoulli Distribution

Source: https://www.mathacademy.com/topics/3071?courseId=109
Topic ID: 3071

## Prerequisites

- [Probability Mass Functions of Discrete Random Variables](./1290-probability-mass-functions-of-discrete-random-variables.md)

## Lesson

### Introduction

A discrete random variable $X$ follows a **Bernoulli distribution** if it has the following probability mass function:

$$



\begin{aligned}𝑝, & \,𝑥=1 \\ 1−𝑝, & \,𝑥=0\end{aligned}



$$

The Bernoulli distribution models the outcome of a **Bernoulli trial**, an experiment with only two events: "success" and "failure". We label "success" by $X=1$ with a probability of $p$ and "failure" by $X=0$ with a probability of $1-p.$

If a random variable $X$ follows a Bernoulli distribution, we write

$$



X \sim \text{Bernoulli} (p).



$$

For example, suppose a fair die is rolled. Each roll of the die is a Bernoulli trial. Let's interpret a "success" as the event that we roll a $6.$ Then, the outcome of a roll of the die $X$ can be modeled as a Bernoulli random variable

$$



X \sim \text{Bernoulli} \left(\dfrac16\right).



$$

Therefore, the probability of success ($X=1$) is

$$



\begin{aligned}𝑃(𝑋=1) & =𝑓(1)=\frac{1}{6},\end{aligned}



$$

while the probability of failure ($X=0$) is

$$



\begin{aligned}𝑃(𝑋=0) & =𝑓(0)=1−\frac{1}{6}=\frac{5}{6}.\end{aligned}



$$

### Example: Computing the Probability at X=1

#### Question

Given that $X \sim \text{Bernoulli}(0.55),$ compute $P(X = 1).$

#### Explanation

If $X \sim \text{Bernoulli}(p),$ then $X$ has the following probability mass function:

$$



\begin{aligned}𝑝, & 𝑥=1 \\ 1−𝑝, & 𝑥=0\end{aligned}



$$

Here, $X \sim \text{Bernoulli}(0.55),$ so the distribution of $X$ in this case is

$$



\begin{aligned}0.55, & 𝑥=1 \\ 0.45, & 𝑥=0.\end{aligned}



$$

Therefore,

$$



P(X = 1) = f(1) = 0.55.



$$

### Example: Computing the Probability at X=0

#### Question

Given that $X \sim \text{Bernoulli}(0.65),$ compute $P(X = 0).$

#### Explanation

If $X \sim \text{Bernoulli}(p),$ then $X$ has the following probability mass function:

$$



\begin{aligned}𝑝, & 𝑥=1 \\ 1−𝑝, & 𝑥=0\end{aligned}



$$

Here, $X \sim \text{Bernoulli}(0.65),$ so the distribution of $X$ in this case is

$$



\begin{aligned}0.65, & 𝑥=1 \\ 0.35, & 𝑥=0.\end{aligned}



$$

Therefore,

$$



P(X = 0) = f(0) = 0.35.



$$

### Example: Computing the Probability of an Intersection

#### Question

Given that $X\sim \text{Bernoulli}(0.7)$ and $Y \sim \text{Bernoulli}(0.6)$ are independent, calculate $P(X=1 \, \cap \, Y=1).$

#### Explanation

Using the multiplication law for independent events, we have

$$



\begin{aligned}𝑃(𝑋=1\,∩\,𝑌=1) & =𝑃(𝑋=1)⋅𝑃(𝑌=1).\end{aligned}



$$

Now, since $X\sim \text{Bernoulli}(0.7),$ we have

$$



P(X=1) = 0.7, \quad P(X=0) = 0.3,



$$

and since $Y \sim \text{Bernoulli}(0.6),$ we have

$$



P(Y=1)=0.6, \quad P(Y=0)=0.4.



$$

Therefore,

$$



\begin{aligned}𝑃(𝑋=1\,∩\,𝑌=1) & =𝑃(𝑋=1)⋅𝑃(𝑌=1) \\ & =0.7⋅0.6 \\ & =0.42.\end{aligned}



$$

### Example: Computing the Probability of a Union

#### Question

Given that $X\sim \text{Bernoulli}(0.3)$ and $Y \sim \text{Bernoulli}(0.7)$ are independent, calculate $P(X=0 \, \cup \, Y=0).$

#### Explanation

By the addition law, we have

$$



\begin{aligned}𝑃(𝑋=0\,∪\,𝑌=0) & =𝑃(𝑋=0)+𝑃(𝑌=0)−𝑃(𝑋=0\,∩\,𝑌=0).\end{aligned}



$$

Using the multiplication law for independent events, we have

$$



\begin{aligned}𝑃(𝑋=0\,∩\,𝑌=0) & =𝑃(𝑋=0)⋅𝑃(𝑌=0).\end{aligned}



$$

Therefore,

$$



\begin{aligned}𝑃(𝑋=0\,∪\,𝑌=0) & =𝑃(𝑋=0)+𝑃(𝑌=0)−𝑃(𝑋=0)⋅𝑃(𝑌=0).\end{aligned}



$$

Now, since $X\sim \text{Bernoulli}(0.3),$ we have

$$



P(X=1) = 0.3, \quad P(X=0) = 0.7,



$$

and since $Y \sim \text{Bernoulli}(0.7),$ we have

$$



P(Y=1)=0.7, \quad P(Y=0)=0.3.



$$

Therefore,

$$



\begin{aligned}𝑃(𝑋=0\,∪\,𝑌=0) & =𝑃(𝑋=0)+𝑃(𝑌=0)−𝑃(𝑋=0)⋅𝑃(𝑌=0) \\ & =0.7+0.3−0.7⋅0.3 \\ & =1−0.21 \\ & =0.79.\end{aligned}



$$
