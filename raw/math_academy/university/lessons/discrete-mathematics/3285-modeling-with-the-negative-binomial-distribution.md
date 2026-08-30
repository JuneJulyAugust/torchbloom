# Modeling With the Negative Binomial Distribution

Source: https://www.mathacademy.com/topics/3285?courseId=109
Topic ID: 3285

## Prerequisites

- [Modeling With the Geometric Distribution](./2839-modeling-with-the-geometric-distribution.md)
- [The Negative Binomial Distribution](./3072-the-negative-binomial-distribution.md)

## Lesson

### Introduction

Recall that the *negative binomial distribution* is a discrete probability distribution used to model the number of independent Bernoulli trials, each with probability $p$ of success, needed to get $r$ successes.

If a random variable $X$ follows a negative binomial distribution, we write $X \sim \textrm{NB}(r, p).$ The PMF of $X$ is

$$



\begin{aligned}(\frac{𝑥−1}{𝑟−1})(1−𝑝)^{𝑥−𝑟}𝑝^{𝑟}, & 𝑥=𝑟,𝑟+1,𝑟+2,… \\ 0, & otherwise.\end{aligned}



$$

Suppose a fair coin is tossed repeatedly. Let the random variable $X$ model the total number of throws until we get two heads. How do we calculate the probability that the sequence will terminate on the fifth coin toss?

In this case:

- Each coin toss (trial) is independent.

- Each trial can be viewed as either "success" (the coin lands on heads) or "failure" (the coin lands on tails).

- We wish to model the number of *trials* to achieve $r$ successes.

Hence, $X$ can be modeled as a negative binomial random variable. Now, since we require $r=2$ successes, each with probability $p=\dfrac12$ of success, we have

$$



X \sim \textrm{NB}\left(2, \dfrac{1}{2}\right).



$$

We can calculate $P(X = 5)$ as follows:

$$



P(X = 5) = \binom{4}{1}\left(\dfrac12\right)^{\color{blue}3}\left(\dfrac12\right)^{\color{red}2}=0.125.



$$

Let's break this down a little:

- The factor $\left(\dfrac12\right)^{\color{red}2}$ gives the probability of getting $\color{red}2$ heads (successes).

- The factor $\left(\dfrac12\right)^{\color{blue}3}$ gives the probability of getting $\color{blue}3$ tails (failures).

- The factor $\displaystyle\binom{4}{1}$ is a binomial coefficient. It gives the number of ways of arranging the first $1$ head into $4$ possible positions. Since we have no choice in how to arrange the second head (it always comes last), we only consider the first one.

Finally, if we set $r=1$ (so the number of trials terminates after the first success), the probability mass function $f(x)$ reduces to that of a geometric distribution.

### Example: Determining Situations That Can Be Modeled as a Negative Binomial Distribution

#### Question

Which of the following random variables can be modeled as a negative binomial distribution?

1. The sum of the outcomes of two $6$-sided dice

2. The number of times a $6$-sided die will land on an even number out of $10$ throws

3. The number of times we must roll a $6$-sided die until we get an even number for the $2$nd time

#### Explanation

We can use the negative binomial distribution to model the number of repeated Bernoulli trials needed until we reach a particular number of successes.

With that in mind, let's consider each of the given random variables.

- Random variable I cannot be modeled as negative binomial distributions. This is because the sum of the outcomes of two dice cannot be interpreted as the number of Bernoulli trials until we reach a particular number of successes.

- Random variable II cannot be modeled as a negative binomial distribution. This is because it counts the number of successes, not the number of trials.

- Random variable III can be modeled as a negative binomial distribution. Getting an even number is a Bernoulli trial, and we wish to count the number of Bernoulli trials until we reach $2$ successes.

Therefore, the correct answer is "III only."

### Example: Modeling Using a Negative Binomial Random Variable

#### Question

A fair spinner with $3$ regions, red, blue, and yellow, is spun until it lands on red for the $2$nd time. What is the probability that the $2$nd red is obtained on the $5$th spin? Round your answer to $4$ decimal places.

#### Explanation

Let $X$ represent the number of times we must spin the spinner until the $2$nd red is obtained. Spinning a spinner and recording whether it lands on red is a Bernoulli trial. We wish to find the number of trials needed until we reach $2$ successes. So, we can model $X$ using the negative binomial distribution: $X \sim \textrm{NB}\left(2, \dfrac13\right).$

In general, if $X \sim \textrm{NB}(r, p),$ then $X$ has the following probability density function:

$$



\begin{aligned}(\frac{𝑥−1}{𝑟−1})(1−𝑝)^{𝑥−𝑟}𝑝^{𝑟}, & 𝑥=𝑟,𝑟+1,𝑟+2,… \\ 0, & otherwise\end{aligned}



$$

Here, $X \sim \textrm{NB}\left(2, \dfrac13\right),$ so the distribution of $X$ in this case is

$$



\begin{aligned}(\frac{𝑥−1}{1})(\frac{2}{3})^{𝑥−2}(\frac{1}{3})^{2}, & 𝑥=2,3,4,… \\ 0, & otherwise.\end{aligned}



$$

Therefore,

$$



\begin{aligned}𝑃(𝑋=5) & =(\frac{4}{1})(\frac{2}{3})^{3}(\frac{1}{3})^{2} \\ & =0.1317.\end{aligned}



$$

### Example: Calculating a Probability Over an Interval

#### Question

A fair spinner with $4$ regions, orange, red, blue, and yellow, is spun until it lands on red for the $2$nd time. What is the probability that the $2$nd red is obtained between the $8$th and the $10$th spin?

#### Explanation

Let $X$ represent the number of spins until the spinner lands on red for the $2$nd time. Recording whether the spinner lands on red is a Bernoulli trial. We wish to find the number of trials until we reach $2$ successes. So, we can model $X$ using the negative binomial distribution: $X \sim \textrm{NB}\left(2, 0.25\right).$

In general, if $X \sim \textrm{NB}(r, p),$ then $X$ has the following probability density function:

$$



\begin{aligned}(\frac{𝑥−1}{𝑟−1})(1−𝑝)^{𝑥−𝑟}𝑝^{𝑟}, & 𝑥=𝑟,𝑟+1,𝑟+2,… \\ 0, & otherwise\end{aligned}



$$

Here, $X \sim \textrm{NB}\left(2, 0.25\right),$ so the distribution of $X$ in this case is

$$



\begin{aligned}(\frac{𝑥−1}{1})(0.75)^{𝑥−2}(0.25)^{2}, & 𝑥=2,3,4,… \\ 0, & otherwise\end{aligned}



$$

Therefore,

$$



\begin{aligned}𝑃(8≤𝑋≤10) & =𝑓(8)+𝑓(9)+𝑓(10) \\ & =(\frac{7}{1})(0.75)^{6}(0.25)^{2}+(\frac{8}{1})(0.75)^{7}(0.25)^{2}+(\frac{9}{1})(0.75)^{8}(0.25)^{2} \\ & ≈0.2009\end{aligned}



$$

rounded to $4$ decimal places.
