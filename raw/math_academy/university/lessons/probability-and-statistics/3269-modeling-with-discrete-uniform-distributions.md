# Modeling With Discrete Uniform Distributions

Source: https://www.mathacademy.com/topics/3269?courseId=73
Topic ID: 3269

## Prerequisites

- [The Discrete Uniform Distribution](./3010-the-discrete-uniform-distribution.md)

## Lesson

### Introduction

Recall that a discrete uniform distribution is a probability distribution that models the outcome of a single event when the support $S$ is finite, and each $x\in S$ is equally likely.

In general, if $X$ follows a discrete uniform distribution over a set $S,$ then $X$ has the following probability mass function:

$$


\begin{aligned}\frac{1}{|𝑆|}, & 𝑥∈𝑆 \\ 0, & otherwise\end{aligned}


$$

where $|S|$ is the size (cardinality) of $S$.

Discrete uniform distributions occur regularly in games of chance.

For example, suppose that in a particular lottery, players must select a number from the following set:

$$


\{1,2,\ldots,50\}


$$

Let's assume that a player randomly selects a number from this set such that each number has an equal probability of being selected. Then, if $X$ represents the number the player chooses, we can model this situation using a discrete uniform distribution, where

$$


X \sim U \{1,2,\ldots,50\}.


$$

Further, since $S = \{1,2,\ldots,50\}$ has $|S| = 50$ items, the probability mass function for the random variable $X$ is

$$


\begin{aligned}\frac{1}{50}, & 𝑥∈{1,2,…,50} \\ 0, & otherwise.\end{aligned}


$$

### Determining When a Discrete Uniform Distribution is Appropriate

To apply a discrete uniform probability model to a situation in context, there are two things we need to check for:

- The support $S$ of our random variable should be *finite*, and

- each $x\in S$ must be *equally likely*.

There are some common pitfalls that we need to be aware of!

- First, we cannot use a discrete uniform distribution to model continuous phenomena. For example, weight, time, and distance are all quantities that can take *any* real number within a given interval. Such quantities should be modeled as continuous, so a discrete uniform distribution is usually inappropriate.

- Second, we must be wary of discrete phenomena requiring infinitely large support. For example, suppose $X$ represents the number of road accidents at a particular junction in a given month. Now, while $X$ is (hopefully) a very small number, it could theoretically be *any* positive integer for modeling purposes! For this reason, a variable with infinite support is more appropriate. Moreover, $X$ is unlikely to be uniformly distributed since having $X=2$ accidents per month is more likely than $X=1\,000\,000.$

### Example: Determining Situations That Can Be Modeled as a Discrete Uniform Distribution

#### Question

Which of the following random variables can be modeled as a discrete uniform distribution?

1. The amount of time, in seconds, needed to download a video.

2. The number obtained when rolling a fair $4$-sided die whose sides are labeled with the numbers $5, 6, 7, 8.$

3. The number of rainy days in a randomly selected summer month in New York City.

#### Explanation

We can use the discrete uniform distribution to model the outcome of a single event when the support $S$ is finite, and each $x\in S$ is equally likely.

With that in mind, let's consider each given random variable.

- Random variable I cannot be modeled as a discrete uniform distribution. This is because an amount of time is a real number, so the support is not finite.

- Random variable II can be modeled as a discrete uniform distribution. There are a finite number of sides, and since the die is fair, each integer between $5$ and $8$ has an equal probability of being selected.

- Random variable III cannot be modeled as a discrete uniform distribution. This is because each possible number of rainy days is not equally likely. For example, it's more likely that there will be $5$ rainy days than $31$ rainy days.

Therefore, the correct answer is "II only."

### Example: Modeling a Situation in Context With the Discrete Uniform Distribution

#### Question

A fair die has $9$ sides labeled with numbers $1$ through $9.$ What is the probability of getting a number greater than or equal to $6$ on the next throw of the die?

#### Explanation

Let $X$ represent the number the die lands on. From the problem statement, we know that $X \sim U \{1, 2, \ldots, 9\},$ and we wish to compute $P(X \geq 6).$

In general, if $X$ follows a discrete uniform distribution over a set $S,$ then $X$ has the following probability mass function:

$$


\begin{aligned}\frac{1}{|𝑆|}, & 𝑥∈𝑆 \\ 0, & otherwise\end{aligned}


$$

Here, we have $X \sim U \{1, 2, \ldots, 9\},$ and the set $S = \{1, 2, \ldots, 9\}$ has $|S| = 9-1 + 1 = 9$ items. So, we have

$$


\begin{aligned}\frac{1}{9}, & 𝑥=1,2,…,9 \\ 0, & otherwise\end{aligned}


$$

In $S,$ the items that satisfy $X \geq 6$ are $6, 7, 8, 9.$ Since there are $4$ elements in total, we have

$$


P(X \geq 6) = 4 \cdot \dfrac{1}{9} = \dfrac{4}{9}.


$$
