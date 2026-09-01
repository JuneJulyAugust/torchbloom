# The Binomial Distribution

Source: https://www.mathacademy.com/topics/3281?courseId=109
Topic ID: 3281

## Prerequisites

- [Combinations](../../../high-school/traditional/lessons/geometry/705-combinations.md)
- [Exponential Functions](../../../high-school/traditional/lessons/algebra-i/1153-exponential-functions.md)
- [Probability Mass Functions of Discrete Random Variables](./1290-probability-mass-functions-of-discrete-random-variables.md)

## Lesson

### Introduction

A **Bernoulli trial** is a random experiment whose outcome can be interpreted as either "success" or "failure."

For example, suppose we toss a coin and define a "success" as the event of getting a head and a "failure" as getting tails. Then, the tossing of a coin can be thought of as a Bernoulli trial.

Now suppose that a fair coin is tossed ${\color{blue}3}$ times. What is the probability of getting exactly $\color{red}2$ heads?

First, notice that each coin toss is a Bernoulli trial. And since we are tossing the coin ${\color{blue}3}$ times, we have a *sequence* of $\color{blue}3$ Bernoulli trials. There are $2^{\color{blue}3} = 8$ possible outcomes of this experiment, given below:

$$



\text{HHH}, \quad \textbf{HHT}, \quad \textbf{HTH}, \quad \text{HTT}, \quad \textbf{THH}, \quad \text{THT}, \quad\text{TTH}, \quad \text{TTT}



$$

Let the random variable $X$ denote the number of heads obtained when a coin is tossed three times. We wish to compute $P(X = {\color{red}{2}}).$ From the list above, we can see that there are $3$ possibilities (highlighted in bold) where we get precisely $\color{red}{2}$ heads. And since there are $8$ possible outcomes, we have

$$



P(X = 2) = \dfrac 3 8.



$$

We can also calculate this probability by considering each possible sequence where we have $X = 2$ (two heads and one tail), finding the probability of each, and then adding them.

- First, let's calculate the probability of getting the sequence $\text{HHT}{:}$ Notice that we've written the probability of obtaining a tail as $\left(1 - \dfrac12\right).$ The reason for this will become clear shortly.

- Next, we calculate the probability of getting the sequence $\text{HTH}{:}$ Notice that this is the same as $P(\text{HHT}).$

- Finally, we calculate the probability of getting the sequence $\text{THH}{:}$ Again, this is the same as $P(\text{HHT})$ and $P(\text{THH}).$

Therefore, we have

$$



\begin{aligned}𝑃(𝑋=2) & =𝑃(HHT)+𝑃(HTH)+𝑃(THH) \\ & =3⋅𝑃(HHT) \\ & =3⋅(\frac{1}{2})^{2}⋅(1−\frac{1}{2}).\end{aligned}



$$

Let's break this result down a little:

- The factor $\left(\dfrac12\right)^2$ represents the probability that we get two heads (i.e., two "successes").

- The factor $\left(1-\dfrac12\right)$ represents the probability that we get one tail (i.e., one "failure").

- The coefficient $3$ represents the number of ways we can make a sequence containing two heads and one tail.

Let's now see how this can be generalized.

### The Probability Mass Function of a Binomial Distribution

Suppose that we have a sequence of $n$ Bernoulli trials, each resulting in success or failure, and with a probability of success $p.$ Let the random variable $X$ represent the number of successes.

It can be shown that $X$ follows a so-called **binomial distribution** and has the following probability mass function:

$$



f(x) = \displaystyle \binom{n}{x} p^x (1-p)^{n-x}, \qquad x=0,1,2,\ldots, n



$$

Let's break this formula down a bit:

- The factor $p^x$ represents the probability that exactly $x$ trials result in "success."

- The factor $(1-p)^{n-x}$ represents the probability that $n-x$ trials result in "failure".

- The binomial coefficient $\displaystyle\binom{n}{x}$ counts the number of ways in which we can get exactly $x$ successes in $n$ trials. Remember that binomial coefficients are the same as combinations and can be computed as

If a random variable $X$ follows a binomial distribution, we write

$$



X\sim B(n,p).



$$

Let's go back to our first example and show that we get the same result.

### Applying the Probability Mass Function of a Binomial Distribution

Let $X$ be the number of heads obtained when a coin is tossed $\color{blue}3$ times. Since we have a sequence of $n=\color{blue}3$ Bernoulli trials, each with a probability of success $p=\dfrac12,$ the number of heads $X$ can be modeled as a binomial random variable, and we write

$$



X\sim B\left({\color{blue}3}, \dfrac12\right).



$$

Therefore, the probability of getting $X=2$ heads is

$$



\begin{aligned}𝑃(𝑋=2) & =𝑓(2) \\ & =(\frac{3}{2})(\frac{1}{2})^{2}(1−\frac{1}{2})^{3\,−\,2} \\ & =3⋅(\frac{1}{2})^{2}(\frac{1}{2}) \\ & =3⋅(\frac{1}{2})^{3} \\ & =\frac{3}{8}\end{aligned}



$$

which agrees with our previous result.

### Example: Computing a Probability at a Point

#### Question

Given that $X \sim B(6, 0.7),$ compute $P(X = 2).$ Round your final answer to $4$ decimal places.

#### Explanation

For a binomial random variable $X \sim B(n,p),$ where $n$ is the number of trials, and $p$ is the probability of success on each trial, we have the following probability mass function:

$$



f(x) = \displaystyle \binom{n}{x} p^x (1-p)^{n-x}



$$

Here, we have $X \sim B(6, 0.7),$ so $X$ has the probability mass function

$$



f(x) = \displaystyle \binom{6}{x} (0.7)^x (0.3)^{6-x}.



$$

Therefore,

$$



\begin{aligned}𝑃(𝑋=2) & =𝑓(2) \\ & =(\frac{6}{2})(0.7)^{2}(0.3)^{6−2} \\ & =15(0.7)^{2}(0.3)^{4} \\ & ≈0.0595\end{aligned}



$$

to $4$ decimal places.

### Example: Computing a Binomial Probability Over an Unbounded Interval

#### Question

Given that $X \sim B(10, 0.7),$ compute $P(X > 8).$ Round your final answer to $4$ decimal places.

#### Explanation

For a binomial random variable $X \sim B(n,p),$ where $n$ is the number of trials, and $p$ is the probability of success on each trial, we have the following probability mass function:

$$



f(x) = \displaystyle \binom{n}{x} p^x (1-p)^{n-x}



$$

Here, we have $X \sim B(10, 0.7),$ so $X$ has the probability mass function

$$



f(x) = \displaystyle \binom{10}{x} (0.7)^x (0.3)^{10-x}.



$$

Therefore, we have

$$



\begin{aligned}𝑃(𝑋>8) & =𝑃(𝑋∈{9,10}) \\ & =𝑓(9)+𝑓(10) \\ & =(\frac{10}{9})(0.7)^{9}(0.3)^{10−9}+(\frac{10}{10})(0.7)^{10}(0.3)^{10−10} \\ & =10(0.7)^{9}(0.3)+1(0.7)^{10}(0.3)^{0} \\ & ≈0.1493\end{aligned}



$$

to $4$ decimal places.

### Example: Computing a Probability Over a Bounded Interval

#### Question

Given $X \sim B(5, 0.3),$ compute $P(0 < X < 3).$ Round your final answer to $4$ decimal places.

#### Explanation

For a binomial random variable $X \sim B(n,p),$ where $n$ is the number of trials, and $p$ is the probability of success on each trial, we have the following probability mass function:

$$



f(x) = \displaystyle \binom{n}{x} p^x (1-p)^{n-x}



$$

Here, we have $X \sim B(5, 0.3),$ so $X$ has the probability mass function

$$



f(x) = \displaystyle \binom{5}{x} (0.3)^x (0.7)^{5-x}.



$$

Therefore, we have

$$



\begin{aligned}𝑃(0<𝑋<3) & =𝑃(𝑋∈{1,2}) \\ & =𝑓(1)+𝑓(2) \\ & =(\frac{5}{1})(0.3)^{1}(0.7)^{5−1}+(\frac{5}{2})(0.3)^{2}(0.7)^{5−2} \\ & =5(0.3)(0.7)^{4}+10(0.3)^{2}(0.7)^{3} \\ & ≈0.6689\end{aligned}



$$

to $4$ decimal places.

### Example: Computing a Probability Over an Interval Using the Complement

#### Question

Given that $X \sim B(7, 0.2),$ compute $P(X \geq 2).$ Round your final answer to $4$ decimal places.

#### Explanation

For a binomial random variable $X \sim B(n,p),$ we have the following probability mass function:

$$



f(x) = \displaystyle \binom{n}{x} p^x (1-p)^{n-x}



$$

Here, we have $X \sim B(7, 0.2),$ so $X$ has the probability mass function

$$



f(x) = \displaystyle \binom{7}{x} (0.2)^x (0.8)^{7-x}.



$$

Computing $P(X \geq 2)$ will require us to compute $f(x)$ at $x=2, 3, 4, \ldots, 7.$ However, if we compute the complement $P(X < 2)$ instead, then we will only have to compute $f(x)$ at $x=0, 1,$ which will result in a much faster computation.

Computing $P(X < 2),$ we get

$$



\begin{aligned}𝑃(𝑋<2) & =𝑃(𝑋∈{0,1}) \\ & =𝑓(0)+𝑓(1) \\ & =(\frac{7}{0})(0.2)^{0}(0.8)^{7−0}+(\frac{7}{1})(0.2)^{1}(0.8)^{7−1} \\ & =(0.8)^{7}+7(0.2)(0.8)^{6} \\ & ≈0.5767\end{aligned}



$$

rounded to $4$ decimal places.

Therefore, we have

$$



\begin{aligned}𝑃(𝑋≥2) & =1−𝑃(𝑋<2) \\ & ≈1−0.5767 \\ & =0.4233\end{aligned}



$$

rounded to $4$ decimal places.
