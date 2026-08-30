# Modeling With the Binomial Distribution

Source: https://www.mathacademy.com/topics/1395?courseId=101
Topic ID: 1395

## Prerequisites

- [The Binomial Distribution](./3281-the-binomial-distribution.md)

## Lesson

### Introduction

A **binomial distribution** is a probability distribution that models the number of successes in a sequence of $n$ independent experiments (or trials) where each outcome is either success or failure. In a binomial distribution, the probability of success in each experiment is the same.

If there are $n$ experiments and $p$ is the probability of success on each experiment, then the number of successes has the following probability mass function:

$$


f(x) = \binom{n}{x} p^x (1-p)^{n-x}, \qquad x=0,1,2, \ldots, n


$$

For example, if we flip a coin $5$ times, then the number of heads follows a binomial distribution.

- Each toss is an experiment that either results in success (i.e., heads) or failure (i.e., tails).

- There are $n=5$ experiments.

- Each experiment has a probability $p=\dfrac{1}{2}$ of success.

So, the number of heads has the following probability mass function:

$$


\begin{aligned}𝑓(𝑥) & =(\frac{5}{𝑥})(\frac{1}{2})^{𝑥}(1−\frac{1}{2})^{5−𝑥} \\ & =(\frac{5}{𝑥})(\frac{1}{2})^{𝑥}(\frac{1}{2})^{5−𝑥} \\ & =(\frac{5}{𝑥})(\frac{1}{2})^{5}\end{aligned}


$$

When a random variable $X$ follows a binomial distribution consisting of $n$ experiments (or trials) and the probability of success on each trial is $p,$ we often write

$$


X\sim B(n,p).


$$

In words, we say, "the random variable $X$ follows a binomial distribution with $n$ trials and probability $p$ of success on each trial."

### Example: Identifying Random Variables that Follow a Binomial Distribution

#### Question

Which of the following random variables could be modeled as a binomial distribution?

1. The ages of $20$ college professors

2. The number of questions answered correctly by a student in a $12$-question exam

3. The heights of $10$ elementary school children

#### Explanation

A binomial distribution models the number of successes in a sequence of $n$ independent experiments (where each outcome is either success or failure).

With that in mind, let's consider each of the given random variables.

- Random variable I could ** be modeled as a binomial distribution. The ages cannot be interpreted as "success" or "failure."

- Random variable II could be modeled as a binomial distribution. The number of questions answered in a $12$- question exam can be interpreted as the number of successes in a sequence of $12$ independent experiments.

- Random variable III could ** be modeled as a binomial distribution. The heights cannot be interpreted as "success" or "failure."

Therefore, the correct answer is "II only."

### Example: Computing the Probability of a Binomial Random Variable for Some Value

#### Question

It is known that $75\%$ of students pass a particular exam. If $5$ students who took the exam are randomly selected, what is the probability that $3$ of them passed the exam? Round your answer to $3$ decimal places.

#### Explanation

Let the random variable $X$ be equal to the number of students that passed the exam.

Here, we have the following information:

- there are $n=5$ students

- the probability that each student passed the exam is $p=75\%=0.75$

So, $X$ follows a binomial distribution, where $X\sim B(5,0.75).$ We want to find the probability that $x=3$ of the students passed the exam.

The number of successes of a binomial random variable has the probability mass function

$$


P(X=x) = \binom{n}{x} p^x (1-p)^{n-x},


$$

where $n$ is the number of experiments, and $p$ is the probability of success on each experiment.

Substituting the above information into the formula for probability mass function, we get

$$


\begin{aligned}𝑃(𝑋=3) & =(\frac{5}{3})(0.75)^{3}(1−0.75)^{5−3} \\ & =\frac{5!}{3!(5−3)!}(0.75)^{3}(0.25)^{2} \\ & =10(0.75)^{3}(0.25)^{2} \\ & =0.264\end{aligned}


$$

rounded to $3$ decimal places.

### Example: Computing the Probability of a Binomial Random Variable Over an Interval

#### Question

A standard fair die is rolled $8$ times. What is the probability of rolling an even number at least $7$ times? Round your answer to $3$ decimal places.

#### Explanation

Let the random variable $X$ be equal to the number of times we get an even number.

Here, we have the following information:

- there are $n=8$ rolls

- the probability of rolling an even number on any roll of the die is

So, $X$ follows a binomial distribution, where $X\sim B(8,0.5).$

The number of successes of a binomial random variable has the probability mass function

$$


P(X=x) = \binom{n}{x} p^x (1-p)^{n-x},


$$

where $n$ is the number of experiments, and $p$ is the probability of success on each experiment.

Substituting the above information into the formula for probability mass function, we get

$$


\begin{aligned}𝑃(𝑋=𝑥) & =(\frac{8}{𝑥})(0.5)^{𝑥}(1−0.5)^{8−𝑥} \\ & =(\frac{8}{𝑥})(0.5)^{𝑥}(0.5)^{8−𝑥}.\end{aligned}


$$

We want to find the probability of rolling an even number at least $7$ times. So, we compute

$$


\begin{aligned}𝑃(𝑋≥7) & =𝑃(𝑋=7)+𝑃(𝑋=8) \\ & =(\frac{8}{7})(0.5)^{7}(0.5)^{8−7}+(\frac{8}{8})(0.5)^{8}(0.5)^{8−8} \\ & =8(0.5)^{7}(0.5)+1(0.5)^{8} \\ & =0.035\end{aligned}


$$

rounded to $3$ decimal places.

### Example: Computing the Probability of a Binomial Distribution Over an Interval Using the Complement

#### Question

In a random card game, there is a $40\%$ chance of winning a game. If the player plays $12$ games, what is the probability that he wins at least $2$ of the games? Round your answer to $3$ decimal places.

#### Explanation

Let the random variable $X$ be equal to the number of games that the player wins.

Here, we have the following information:

- there are $n=12$ games

- the probability of winning each game is $p=40\%=0.4$

So, $X$ follows a binomial distribution, where $X\sim B(12,0.4).$

The number of successes of a binomial random variable has the probability mass function

$$


P(X=x) = \binom{n}{x} p^x (1-p)^{n-x},


$$

where $n$ is the number of experiments, and $p$ is the probability of success on each experiment.

Substituting the above information into the formula for probability mass function, we get

$$


\begin{aligned}𝑃(𝑋=𝑥) & =(\frac{12}{𝑥})(0.4)^{𝑥}(1−0.4)^{12−𝑥} \\ & =(\frac{12}{𝑥})(0.4)^{𝑥}(0.6)^{12−𝑥}.\end{aligned}


$$

We want to find the probability that the player wins at least 2 of the games. This corresponds to $P(X \geq 2).$

However, computing

$$


P(X \geq 2) = P(X=2) + P(X=3) + \ldots + P(X=12)


$$

will involve many computations, so let's express our answer in terms of the complement instead. By doing this, we get

$$


\begin{aligned}𝑃(𝑋≥2) & =1−𝑃(𝑋<2) \\ & =1−[𝑃(𝑋=0)+𝑃(𝑋=1)] \\ & =1−[(\frac{12}{0})(0.4)^{0}(0.6)^{12−0}+(\frac{12}{1})(0.4)^{1}(0.6)^{12−1}] \\ & =1−[(0.6)^{12}+12(0.4)(0.6)^{11}] \\ & =1−0.019\,591 \\ & =0.980\end{aligned}


$$

rounded to $3$ decimal places.
