# Mean and Variance of the Geometric Distribution

Source: https://www.mathacademy.com/topics/2992?courseId=109
Topic ID: 2992

## Prerequisites

- [Variance of Discrete Random Variables](./1388-variance-of-discrete-random-variables.md)
- [Modeling With the Geometric Distribution](./2839-modeling-with-the-geometric-distribution.md)

## Lesson

### Introduction

Let the random variable $X$ have a geometric distribution with success probability $p{:}$

$$



X\sim \textrm{Geom}(p)



$$

The mean (expected value) of $X$ is given by

$$



\textrm E[X] = \dfrac{1}{p}.



$$

We'll justify this rule at the end of the lesson.

The variance of $X$ is given by

$$



\textrm{Var}[X] = \dfrac{1-p}{p^2}.



$$

For example, if $X \sim \textrm{Geom}(0.2),$ then the mean is

$$



\textrm E[X] = \dfrac{1}{0.2}=5,



$$

and the variance is

$$



\textrm{Var}[X] = \dfrac{1-0.2}{(0.2)^2}=20.



$$

### Example: The Mean of a Geometric Distribution

#### Question

Given that $X \sim \textrm{Geom} \left(0.02\right),$ what is $\textrm E[X]?$

#### Explanation

If $X \sim \textrm{Geom}(p)$ is a geometric random variable, then

$$



\textrm E[X] = \dfrac{1}{p}.



$$

Therefore, for our random variable $X \sim \textrm{Geom}\left(0.02\right),$ we have the following expected value:

$$



\textrm E[X] = \dfrac{1}{0.02} = 50



$$

### Example: Finding the Mean of a Geometric Distribution in Context

#### Question

A regular deck of cards contains $52$ cards, $13$ of which are heart cards. Daniel repeatedly draws a card at random from the deck and puts it back until he draws a heart. On average, how many draws must Daniel make until he draws a heart card?

#### Explanation

We interpret a "success" as the event that Daniel draws a heart card and a "failure" as the event that he draws some other card. So, the success probability is

$$



p = \dfrac{13}{52} = \dfrac{1}{4}.



$$

Let $X$ represent the number of cards we must draw until we get a heart card. So, we can model $X$ using a geometric distribution:

$$



X \sim \textrm{Geom}\left(\dfrac {1}{4}\right)



$$

We wish to compute the expected number of draws, i.e., $\textrm E[X].$ Recall that, if $X \sim \textrm{Geom}\left(p\right),$ then

$$



\textrm E[X] = \dfrac{1}{p}.



$$

Therefore, for our random variable $X \sim \textrm{Geom}\left(\dfrac 1 4\right),$ we have the following expected value:

$$



\textrm E[X] = \dfrac{1}{\left(\dfrac14\right)} = 4



$$

So, the expected number of draws is $4.$

### Example: The Variance of a Geometric Distribution

#### Question

Given that $X\sim \textrm{Geom}\left(\dfrac{1}{3}\right),$ what is $\textrm{SD}[X]?$

#### Explanation

If $X \sim \textrm{Geom}(p)$ is a geometric random variable, then

$$



\textrm{SD}[X] = \sqrt{\textrm{Var}[X]} = \dfrac{\sqrt{1-p}}{p}.



$$

Therefore, for our random variable $X \sim \textrm{Geom}\left(\dfrac{1}{3}\right),$ we have the following standard deviation:

$$



\begin{aligned}SD[𝑋] & =\frac{\sqrt{√1−\frac{1}{3}}}{3} \\ & =\frac{\sqrt{√\frac{2}{3}}}{3} \\ & =\sqrt{√6}\end{aligned}



$$

### Example: Finding the Variance of a Geometric Distribution in Context

#### Question

A fair $8$-sided die is rolled until it shows a score of $2.$ What is the variance in the number of rolls that are required?

#### Explanation

We interpret a "success" as the event that a $2$ is shown and a "failure" when some other number is displayed. So, the success probability is

$$



p=\dfrac{1}{8}.



$$

Let $X$ represent the number of rolls we must do until a 2 is obtained. So, we can model X using a geometric distribution:

$$



X \sim \textrm{Geom}\left(\dfrac{1}{8}\right)



$$

Recall that, if $X \sim\textrm{Geom}\left(p\right),$ then

$$



\textrm{Var}[X] = \dfrac{1-p}{p^2}.



$$

Therefore, for our random variable $X \sim \textrm{Geom}\left(\dfrac{1}{8}\right),$ we have the following variance:

$$



\begin{aligned}Var[𝑋] & =\frac{1−\frac{1}{8}}{8} \\ & =\frac{(\frac{7}{8})}{8} \\ & =56\end{aligned}



$$

### Justification for the Mean

Throughout this lesson, we used the fact that if $X\sim\textrm{Geom}(p),$ then

$$



\textrm E[X] = \dfrac1p.



$$

Let's now justify this result.

First, recall that if $X\sim \textrm{Geom}(p),$ then the PMF of $X$ is given by

$$



\begin{aligned}𝑝(1−𝑝)^{𝑥−1}, & 𝑥=1,2,3…, \\ 0, & otherwise.\end{aligned}



$$

By definition, we have

$$



\textrm E[X] = \sum_{x\in \{1,2,3\ldots\}} x \cdot f(x).



$$

It's convenient to write this as follows:

$$



\textrm E[X] = \sum_{x=1}^\infty x \cdot f(x)



$$

Therefore,

$$



\textrm{E}[X] = \sum_{x=1}^\infty x \cdot p(1-p)^{x-1}.



$$

We can factor $p$ out of the summation since it's a constant:

$$



\textrm{E}[X] = p \sum_{x=1}^\infty x (1-p)^{x-1}.



$$

Let $q = 1-p.$ Then, we have

$$



\textrm{E}[X] = p \sum_{x=1}^\infty x q^{x-1}.



$$

Now, using the generalized binomial theorem, we have that if $|q| < 1$ then

$$



\sum_{x=1}^\infty x q^{x-1} = \frac{1}{(1-q)^2}.



$$

Therefore,

$$



\begin{aligned}E[𝑋] & =𝑝⋅\frac{1}{(1−𝑞)^{2}} \\ & =𝑝⋅\frac{1}{𝑝^{2}} \\ & =\frac{1}{𝑝}.\end{aligned}



$$
