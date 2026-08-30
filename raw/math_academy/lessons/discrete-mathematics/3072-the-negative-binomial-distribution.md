# The Negative Binomial Distribution

Source: https://www.mathacademy.com/topics/3072?courseId=109
Topic ID: 3072

## Prerequisites

- [Combinations](../geometry/705-combinations.md)
- [The Geometric Distribution](./3284-the-geometric-distribution.md)

## Lesson

### Introduction

In this lesson, we will discuss the **negative binomial distribution**, which can be thought of as an extension of the geometric distribution. It is used to model the number of independent Bernoulli trials needed to get a particular number of successes.

Let's build some intuition by considering an example.

Suppose a fair die is thrown repeatedly until a total of $\color{red}3$ sixes are shown. The sixes do not need to be consecutive, so the sequence

$$



{\color{black}{1}},\quad {\color{black}{4}},\quad {\color{black}{3}},\quad \stackrel{\color{green}{\checkmark}}{6},\quad {\color{black}{4}},\quad {\color{black}{3}},\quad {\color{black}{2}},\quad \stackrel{\color{green}{\checkmark}}{6},\quad {\color{black}{5}},\quad \stackrel{\color{green}{\checkmark}}{6}



$$

is an acceptable sequence. Note the following:

- We interpret rolling a $6$ as a "success" and anything else as "failure."

- In the above example, we have $\color{red}3$ successes, $\color{blue}7$ failures, and ${\color{red}{3}} + {\color{blue}{7}} = 10$ throws in total.

- The sequence terminated on a success.

Let the random variable $X$ model the total number of throws until we get $\color{red} 3$ successes. In the example above, we have $X=10.$ How do we calculate the probability that the sequence will terminate on the 10th throw?

We can calculate $P(X = 10)$ as follows:

$$



P(X = 10) = \binom{9}{2}\left(\dfrac56\right)^{\color{blue}7}\left(\dfrac16\right)^{\color{red}3}.



$$

Let's break this down a little:

- The factor $\left(\dfrac16\right)^{\color{red}3}$ gives the probability of getting $\color{red}3$ successes.

- The factor $\left(\dfrac56\right)^{\color{blue}7}$ gives the probability of getting $\color{blue}7$ failures.

- The factor $\displaystyle\binom{9}{2}$ is a binomial coefficient. It gives the number of ways of arranging the first $2$ successes into $9$ possible positions. We have no choice in how to arrange the third success (it has to come last), so we only consider the first two here.

The random variable $X$ in this example is a negative binomial random variable. Let's now discuss negative binomial random variables more generally.

### The Probability Mass Function of a Negative Binomial Random Variable

A discrete random variable $X$ follows a negative binomial distribution if it has the following probability mass function:

$$



\begin{aligned}(\frac{𝑥−1}{𝑟−1})(1−𝑝)^{𝑥−𝑟}𝑝^{𝑟},\, & 𝑥=𝑟,𝑟+1,𝑟+2,… \\ \,0, & otherwise\end{aligned}



$$

The negative binomial distribution models the number $X$ of independent Bernoulli trials, each with probability $p$ of success, before $r$ successes occur.

It's worth taking some time to understand the above formula:

- The factor $p^{r}$ gives the probability of getting $r$ successes.

- The factor $(1-p)^{x-r}$ gives the probability of getting $x-r$ failures.

- The factor $\displaystyle\binom{x-1}{r-1}$ gives the number of ways of arranging the first $r-1$ successes into $x-1$ positions.

- $x\geq r$ because there should be a minimum of $r$ Bernoulli trials before the sequence terminates.

If a random variable $X$ follows a negative binomial distribution, we write

$$



X \sim \textrm{NB}(r, p).



$$

Finally, notice that if we set $r=1$ (so the number of trials terminates after the first success), then the probability mass function $f(x)$ reduces to that of a geometric distribution.

### Example: Computing a Probability at a Point

#### Question

Given that $X \sim \textrm{NB}(3, 0.8),$ compute $P(X = 7),$ rounded to $4$ decimal places.

#### Explanation

For a negative binomial random variable $X \sim \textrm{NB}(r, p),$ we have the following probability distribution:

$$



\begin{aligned}(\frac{𝑥−1}{𝑟−1})(1−𝑝)^{𝑥−𝑟}𝑝^{𝑟}, & 𝑥=𝑟,𝑟+1,𝑟+2,… \\ 0, & otherwise\end{aligned}



$$

Here, $X \sim \textrm{NB}(3, 0.8),$ so the distribution of $X$ in this case is

$$



\begin{aligned}(\frac{𝑥−1}{2})(0.2)^{𝑥−3}(0.8)^{3}, & 𝑥=3,4,5,… \\ 0, & otherwise.\end{aligned}



$$

Therefore,

$$



\begin{aligned}𝑃(𝑋=7) & =𝑓(7) \\ & =(\frac{7−1}{2})(0.2)^{7−3}(0.8)^{3} \\ & =(\frac{6}{2})(0.2)^{4}(0.8)^{3} \\ & ≈0.0123\end{aligned}



$$

rounded to $4$ decimal places.

### Example: Computing a "Less Than" Probability

#### Question

Given $X \sim \textrm{NB}(6, 0.28),$ compute $P(X < 9),$ rounded to $4$ decimal places.

#### Explanation

For a negative binomial random variable $X \sim \textrm{NB}(r, p),$ we have the following probability distribution:

$$



\begin{aligned}(\frac{𝑥−1}{𝑟−1})(1−𝑝)^{𝑥−𝑟}𝑝^{𝑟}, & 𝑥=𝑟,𝑟+1,𝑟+2,… \\ 0, & otherwise\end{aligned}



$$

Here, $X \sim \textrm{NB}(6, 0.28),$ so the distribution of $X$ in this case is

$$



\begin{aligned}(\frac{𝑥−1}{5})(0.72)^{𝑥−6}(0.28)^{6}, & 𝑥=6,7,8,… \\ 0, & otherwise.\end{aligned}



$$

Therefore,

$$



\begin{aligned}𝑃(𝑋<9) & =𝑃(𝑋∈{6,7,8}) \\ & =𝑃(𝑋=6)+𝑃(𝑋=7)+𝑃(𝑋=8) \\ & =𝑓(6)+𝑓(7)+𝑓(8) \\ & =(\frac{5}{5})(0.72)^{0}(0.28)^{6}+(\frac{6}{5})(0.72)^{1}(0.28)^{6}+(\frac{7}{5})(0.72)^{2}(0.28)^{6} \\ & ≈0.0078\end{aligned}



$$

rounded to $4$ decimal places.

### Example: Computing a Probability Over a Bounded Interval

#### Question

Given $X \sim \textrm{NB}(11, 0.6),$ compute $P(12< X < 16),$ rounded to $4$ decimal places.

#### Explanation

For a negative binomial random variable $X \sim \textrm{NB}(r, p),$ we have the following probability distribution:

$$



\begin{aligned}(\frac{𝑥−1}{𝑟−1})(1−𝑝)^{𝑥−𝑟}𝑝^{𝑟}, & 𝑥=𝑟,𝑟+1,𝑟+2,… \\ 0, & otherwise\end{aligned}



$$

Here, $X \sim \textrm{NB}(11, 0.6),$ so the distribution of $X$ in this case is

$$



\begin{aligned}(\frac{𝑥−1}{10})(0.4)^{𝑥−11}(0.6)^{11}, & 𝑥=11,12,13,… \\ 0, & otherwise.\end{aligned}



$$

Therefore,

$$



\begin{aligned}𝑃(12<𝑋<16) & =𝑃(𝑋∈{13,14,15}) \\ & =𝑃(𝑋=13)+𝑃(𝑋=14)+𝑃(𝑋=15) \\ & =𝑓(13)+𝑓(14)+𝑓(15) \\ & =(\frac{12}{10})(0.4)^{2}(0.6)^{11}+(\frac{13}{10})(0.4)^{3}(0.6)^{11}+(\frac{14}{10})(0.4)^{4}(0.6)^{11} \\ & ≈0.1977\end{aligned}



$$

rounded to $4$ decimal places.

### Example: Computing a Probability Over a Bounded Interval Using the Complement

#### Question

Given $X \sim \textrm{NB}(14, 0.65),$ compute $P(X \geq 16),$ rounded to $4$ decimal places.

#### Explanation

For a negative binomial random variable $X \sim \textrm{NB}(r, p),$ we have the following probability distribution:

$$



\begin{aligned}(\frac{𝑥−1}{𝑟−1})(1−𝑝)^{𝑥−𝑟}𝑝^{𝑟}, & 𝑥=𝑟,𝑟+1,𝑟+2,… \\ 0, & otherwise\end{aligned}



$$

Here, $X \sim \textrm{NB}(14,0.65),$ so the distribution of $X$ in this case is

$$



\begin{aligned}(\frac{𝑥−1}{13})(0.35)^{𝑥−14}(0.65)^{14}, & 𝑥=14,15,16,… \\ 0, & otherwise.\end{aligned}



$$

There are infinitely many values of $X$ such that $X \geq 16.$ However, we can simplify the computation by using the complement instead:

$$



\begin{aligned}𝑃(𝑋≥16) & =1−𝑃(𝑋<16)\end{aligned}



$$

Computing the complement, we get

$$



\begin{aligned}𝑃(𝑋<16) & =𝑃(𝑋∈{14,15}) \\ & =𝑃(𝑋=14)+𝑃(𝑋=15) \\ & =𝑓(14)+𝑓(15) \\ & =(\frac{13}{13})(0.35)^{0}(0.65)^{14}+(\frac{14}{13})(0.35)^{1}(0.65)^{14} \\ & ≈0.0142.\end{aligned}



$$

Therefore,

$$



\begin{aligned}𝑃(𝑋≥16) & =1−𝑃(𝑋<16) \\ & ≈1−0.0142 \\ & =0.9858\end{aligned}



$$

rounded to $4$ decimal places.
