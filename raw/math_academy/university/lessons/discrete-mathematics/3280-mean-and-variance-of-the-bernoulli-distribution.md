# Mean and Variance of the Bernoulli Distribution

Source: https://www.mathacademy.com/topics/3280?courseId=109
Topic ID: 3280

## Prerequisites

- [Variance of Discrete Random Variables](./1388-variance-of-discrete-random-variables.md)
- [The Bernoulli Distribution](./3071-the-bernoulli-distribution.md)

## Lesson

### Introduction

We can use a Bernoulli distribution to model the outcome of a *single* event when the outcome can be interpreted as either "success" or "failure."

Imagine that you're playing a board game. It's your turn to roll a fair six-sided die, and you win the game if you roll $5$ or higher.

To model this situation, we define the random variable $X$ as follows:

- $X=1$ represents a "success." In this case, success means rolling $5$ or higher.

- $X=0$ represents a "failure". In this case, failure means rolling $4$ or less.

There are $6$ possible outcomes of the roll, and $2$ of those outcomes (namely, rolling a $5$ or $6$) will result in a success. So, the probability $p$ of success is

$$



p=\dfrac26=\dfrac13.



$$

Therefore, we have

$$



X\sim \text{Bernoulli}\left(\dfrac13\right).



$$

Any random experiment that can be interpreted either as success or failure is called a **Bernoulli trial.**

### Example: Determining Situations That Can Be Modeled as a Bernoulli Distribution

#### Question

Which of the following random variables could be modeled as a Bernoulli distribution?

1. Rolling a die and observing whether it lands on a number greater than $2$

2. The number of visitors to a particular web page over a specific time interval

3. The number of times a die is thrown until a $6$ is obtained

#### Explanation

We can use a Bernoulli distribution to model a ** event when the event outcome can be interpreted as either success or failure.

With that in mind, let's consider each of the given random variables.

- Random variable I could be modeled as a Bernoulli distribution. For example, we could interpret the event of getting a number greater than $2$ as "success" and the event of getting a number less than or equal to $2$ as "failure."

- Random variable II cannot be modeled as a Bernoulli distribution. The number of visitors to a web page cannot be interpreted as "success" or "failure."

- Random variable III cannot be modeled as a Bernoulli distribution. Although getting $6$ on a particular throw can be interpreted as "success" or "failure," we can only use the Bernoulli distribution to model the outcome of a single throw.

Therefore, the correct answer is "I only."

### Example: Modeling With the Bernoulli Distribution

#### Question

Betty will pass a trigonometry course if she answers the final question on her exam correctly. Unfortunately, she doesn't know the correct answer, but the question is multiple-choice with three options, so she randomly picks one answer. By modeling the situation as a Bernoulli trial, determine the probability that Betty passes the course.

#### Explanation

Let the random variable $X$ represent whether Betty passes the course: $X=1$ if she passes and $X=0$ if she doesn't. We wish to compute $P(X = 1).$

We know that Betty passes if she answers the last question correctly, which happens with probability $p = \dfrac{1}{3}.$ So, we have $X \sim \textrm{Bernoulli} \left(\dfrac{1}{3} \right).$

If $X \sim \textrm{Bernoulli}(p),$ then $X$ has the following probability mass function:

$$



\begin{aligned}𝑝, & 𝑥=1 \\ 1−𝑝, & 𝑥=0\end{aligned}



$$

Here, $X \sim \textrm{Bernoulli} \left(\dfrac{1}{3} \right),$ so the distribution of $X$ in this case is

$$



\begin{aligned}\frac{1}{3}, & 𝑥=1 \\ \frac{2}{3}, & 𝑥=0.\end{aligned}



$$

Therefore, the probability that Betty passes the course is

$$



P(X = 1) = f(1) = \dfrac{1}{3}.



$$

### Mean and Variance of the Bernoulli Distribution

It can be shown that if $X\sim \textrm{Bernoulli}(p),$ then

$$



\textrm{E}[X] = p, \qquad \textrm{Var}[X] = p(1-p).



$$

We'll now prove these two results. First, recall that if $X\sim \textrm{Bernoulli}(p),$ then the PMF of $X$ is given by

$$



\begin{aligned}𝑝, & 𝑥=1, \\ 1−𝑝, & 𝑥=0.\end{aligned}



$$

By definition, we have

$$



\textrm E[X] = \sum_{x\in \{0,1\}} x \cdot f(x).



$$

Therefore,

$$



\begin{aligned}E[𝑋]=1⋅𝑝+0⋅(1−𝑝)=𝑝.\end{aligned}



$$

For the variance, we first recall that

$$



\textrm{Var}[X] = \textrm E[X^2] - \left(\textrm{E}[X]\right)^2.



$$

Therefore,

$$



\begin{aligned}Var[𝑋] & =E[𝑋^{2}]−(E[𝑋])^{2} \\ & =1^{2}⋅𝑝+0^{2}⋅(1−𝑝)−𝑝^{2} \\ & =𝑝−𝑝^{2} \\ & =𝑝(1−𝑝).\end{aligned}



$$

### Example: Finding the Mean of a Bernoulli Random Variable

#### Question

George is playing poker with his friends. He wins if he gets a queen from a shuffled deck of $24$ cards, $4$ of which are queens. Let $X$ represent the game's outcome: $X=1$ if George wins and $X=0$ if George loses. By modeling the situation as a Bernoulli trial, determine the expected value of $X.$

#### Explanation

We know that George wins if the first card from the deck is a queen, which happens with probability $p = \dfrac{4}{24} = \dfrac{1}{6}.$ So, we have $X \sim \textrm{Bernoulli} \left(\dfrac{1}{6} \right).$

We wish to compute $\textrm E[X].$ In general, if $X \sim \textrm{Bernoulli}(p),$ then

$$



\textrm E[X] = p.



$$

Therefore, in this case, we have

$$



\textrm E[X] = \dfrac{1}{6}.



$$

### Example: Finding the Variance or Standard Deviation of a Bernoulli Random Variable

#### Question

Sarah knows $56\%$ of the emails she receives are spam. Let $X$ represent whether the next email Sarah receives is spam: $X=1$ if the email is spam and $X=0$ if it isn't. By modeling the situation as a Bernoulli trial, determine the standard deviation of $X.$ Round your answer to $3$ decimal places.

#### Explanation

We know that Sarah receives a spam email with probability $p =56\% = 0.56.$ So, we have $X \sim \textrm{Bernoulli} \left(0.56 \right).$

We wish to compute $\textrm{SD}[X].$ In general, if $X \sim \textrm{Bernoulli}(p),$ then

$$



\textrm{SD}[X] = \sqrt{p(1-p)}.



$$

Therefore, in this case, we have

$$



\textrm{SD}[X] = \sqrt{\left(0.56\right)\left(0.44\right)} \approx 0.496



$$

rounded to $3$ decimal places.
