# The PMF of the Hypergeometric Distribution

Source: https://www.mathacademy.com/topics/5412?courseId=109
Topic ID: 5412

## Prerequisites

- [Compound AND Inequalities](../../../high-school/traditional/lessons/algebra-i/350-compound-and-inequalities.md)
- [The Hypergeometric Distribution](./3073-the-hypergeometric-distribution.md)

## Lesson

### Introduction

In this lesson, we will learn how the hypergeometric distribution can be used to model real-world situations. We'll also discuss the structure of a hypergeometric random variable's probability mass function (PMF).

Suppose a chess club has $18$ members, of whom $12$ are veteran players and $6$ are beginners. A sample of $6$ players is randomly chosen to participate in a chess tournament. If $X$ represents the number of veterans in the sample, find an expression that represents $P(X = x)$ for $X \in \{0,1,2,3,4,5,6\}.$

The probability that the sample contains precisely $x$ veteran players is given by

$$



6



$$

Here, a "success" means selecting a veteran player, and a "failure" means choosing a beginner.

Let's calculate the numerator and denominator separately.

- First, let's find the number of samples of size $6$ with precisely $x$ veteran players. The number of ways of selecting $x$ veteran players from a total of $12$ in the population is The other $6-x$ players in the sample are beginners. The number of ways of selecting $6-x$ beginners from a total of $18-12=6$ in the population is So, by the rule of product, the number of samples of size $6$ with precisely $x$ veteran players is

- Next, we find the number of samples of size $6$ from a population of size $18.$ This is given by

Therefore, for $X \in \{0,1,2,3,4,5,6\},$ we get

$$



\begin{aligned}𝑃(𝑋=𝑥) & =\frac{# of samples of size 6 with x successes}{# of samples of size 6} \\ & =\frac{(\frac{12}{𝑥})⋅(\frac{6}{6−𝑥})}{𝑥}.\end{aligned}



$$

### Example: Constructing a Probability Mass Function

#### Question

If $X \sim \textrm{Hypergeometric}(24,15, 8),$ then find $P(X = x)$ for $X \in \{0,1,\ldots,8\}.$

#### Explanation

A hypergeometric random variable $X \sim \textrm{Hypergeometric}(N, K, n)$ counts the number of successes in a random sample of size $n,$ drawn without replacement from a population of size $N,$ which contains $K$ items with a successful characteristic.

The probability that the sample contains precisely $x$ successes is given by

$$



8



$$

Let's calculate the numerator and denominator separately.

- First, let's find the number of samples of size $8$ with precisely $x$ successes. The number of ways of selecting $x$ successes from a total of $10$ successes in the population is The other $8-x$ items in the sample are failures. The number of ways of selecting $8-x$ failures from a total of $24-15=9$ failures in the population is So, by the rule of product, the number of samples of size $8$ with precisely $x$ successes is

$$



\begin{aligned}# of samples with precisely x successes & =# of ways to select x successes \\ & \,\,×\,# of ways to select (8-x) failures \\ & =(\frac{15}{𝑥})⋅(\frac{9}{8−𝑥}).\end{aligned}



$$

- Next, we find the number of samples of size $8$ from a population of size $24.$ This is given by

Therefore, for $X \in \{0,1,\ldots,8\},$ we get

$$



\begin{aligned}𝑃(𝑋=𝑥) & =\frac{# of samples of size 8 with precisely x successes}{# of samples of size 8} \\ & =\frac{(\frac{15}{𝑥})⋅(\frac{9}{8−𝑥})}{𝑥}.\end{aligned}



$$

### The Structure of the Probability Mass Function

In general, the probability mass function of a hypergeometric random variable $X\sim \textrm{Hypergeometric}(N,K,n)$ is given by

$$



\begin{aligned}\frac{(\frac{𝐾}{𝑥})(\frac{𝑁−𝐾}{𝑛−𝑥})}{𝑥}, & if max(0,𝑛+𝐾−𝑁)≤𝑥≤min(𝑛,𝐾) \\ 0, & otherwise.\end{aligned}



$$

Let's break down the structure of this formula:

- The factor $\displaystyle \binom{K}{x}$ in the numerator gives the number of ways getting $x$ successes out of $K.$

- The factor $\displaystyle \binom{N-K}{n-x}$ in the numerator gives the number of ways getting $n-x$ failures out of $N-K.$

- The value $\displaystyle \binom{N}{n}$ in the denominator gives the number of ways to select $n$ objects out of $N.$

We also have the following upper-bound:

$$



X \leq \min(n, K)



$$

This states that the number of successes cannot be larger than $n$ (the number of draws) and $K$ (the number of items considered successes).

Additionally, we have the following lower-bound:

$$



\max(0, n+K-N) \leq X



$$

If the number of possible failures $N-K$ is smaller than $n$ (the number of draws), we must get *at least* $n-(N-K)$ successes.

For example, suppose there are ${\color{blue}5}$ candies in a bag, where there are ${\color{red}4}$ red, ${\color{blue}5} - {\color{red}4} = 1$ yellow. We randomly select ${\color{violet}3}$ candies and count the number of red ones.

Consider the worst-case scenario where we select the smallest possible number of red candies. One way to do this is to select all the yellow candies before selecting red. We cannot avoid selecting some red candies since the number of draws $({\color{violet}3})$ exceeds the number of yellow candies $({\color{blue}5} - {\color{red}4} = 1).$ Therefore, in this case, we must select a minimum of

$$



{\color{violet}3} - \left({\color{blue}5} - {\color{red}4}\right) = 2



$$

red candies.

### Example: Finding the Support of a Hypergeometric Random Variable

#### Question

A classic card deck contains $52$ cards, $13$ of which are hearts and the rest are spades, clubs, or diamonds. A sample of $5$ cards is drawn from the deck at random. If $X$ represents the number of heart cards in the sample, what is the support of $X?$

#### Explanation

We need to find an upper-bound and lower-bound of $X.$

- Clearly, the number of heart cards $X$ in the sample cannot be larger than the sample size $(5)$ and cannot be larger than the number of heart cards in the population $(13).$ So, we have

- There are $52-13=39$ spades, clubs, and diamond cards in the population, so it is ** for a sample of size $5$ to contain only spades, clubs, and diamond cards. In this case, the sample would contain no heart cards. So, we have

Therefore, since $X$ takes integer values, the support of $X$ is an integer such that

$$



\boxed{\color{blue}0} \leq X \leq \boxed{\color{blue}5}.



$$
