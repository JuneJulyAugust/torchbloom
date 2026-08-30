# Hypothesis Tests for the Rate of a Poisson Distribution

Source: https://www.mathacademy.com/topics/4126?courseId=73
Topic ID: 4126

## Prerequisites

- [Modeling With the Poisson Distribution](./2838-modeling-with-the-poisson-distribution.md)
- [Introduction to Hypothesis Testing](./2995-introduction-to-hypothesis-testing.md)
- [The CDF of the Poisson Distribution](./3274-the-cdf-of-the-poisson-distribution.md)

## Lesson

### Introduction

In this lesson, we'll learn how to conduct one-tailed hypothesis tests in cases where the null hypothesis can be modeled using a Poisson distribution.

Suppose an online shop typically receives $25$ orders per day. The owner suspects the average number of orders has dropped after poor online reviews. They decide to conduct a hypothesis test at the $5\%$ significance level to determine whether their suspicions are correct.

Let $\lambda$ be the average rate number of orders received per day. Then, we have the following null and alternative hypotheses:

- $H_0: \:\:\lambda = 25$

- $H_1: \:\:\lambda < 25$

The significance level is $\alpha = 5\%.$ Furthermore, we'll assume that events occur independently and at a constant average rate. Therefore, if the null hypothesis is true, we have

$$


X \sim \textrm{Po}(25).


$$

Suppose the shop received $15$ orders on a randomly selected day after the reviews were posted. Does this data provide enough evidence to reject $H_0?$

Using a CDF table for the Poisson distribution, the value of our test statistic is

$$


\begin{aligned}𝑃(𝑋≤15) & =0.0223=2.23\%<5\%.\end{aligned}


$$

Let's interpret this result:

- Since $P(X \leq 15) < 5\%,$ the experimental result is unlikely under the null hypothesis.

- In other words, there is *sufficient* evidence to reject $H_0.$

- Therefore, we conclude that the order rate *has* reduced.

### Example: Setting up a Hypothesis Test

#### Question

The manager of a bicycle rental company estimates that, on average, $13$ bicycles were rented daily over the last few months. After the company bought new bicycles and improved the service, the manager decided to conduct a statistical hypothesis test at the $10\%$ significance level to see whether there had been an increase in the number of bicycles rented daily.

The manager randomly selected a day in a particular week and found that $19$ bicycles were rented that day.

Let $\lambda$ be the average number of bicycles rented each day, and let $X$ equal the number of bikes rented on a randomly selected day. By assuming that rentals occur independently, state the null and alternative hypothesis and the test statistic for this hypothesis test.

#### Explanation

A hypothesis is a statement about a population parameter that we wish to test by collecting sample data.

In this case, the population parameter we wish to test is $\lambda,$ the average number of bicycles rented daily.

- The default assumption is that the average number of bicycles rented is the same as before. Therefore, the null hypothesis is $H_0: \boxed{\color{blue}\lambda = 13}.$

- The manager wishes to test the hypothesis that the average number of bicycles rented per day has **. Therefore, the alternative hypothesis is $H_1: \boxed{\color{blue}\lambda > 13}.$

- Under the null hypothesis, the rentals occur independently at a constant average rate of $13$ per day. Therefore, $X\sim \boxed{\color{blue}\textrm{Po}(13)}.$

- The manager conducted an experiment and found that $19$ bicycles were rented on a particular day. Therefore, a suitable test statistic is $P(\boxed{\color{blue}X\geq 19}).$ Note that: Since we wish to test $\lambda > 13,$ this is a **. We're interested in $X\geq 19,$ not just $X=19.$ This is because we also want to include ** events in the right tail that more unlikely than $X=19.$

### Example: Conducting a Left-Tailed Test

#### Question

A website has an average visitor rate of $16$ visits per hour. A web designer is asked to rebrand the website, but the designer thinks the requested style will negatively impact the visitor rate. They wish to conduct a hypothesis test at the $10\%$ significance level to test whether the visitor rate has subsequently decreased.

A total of $10$ people visited the website in the first hour after launching the rebranded website. The web designer compares this experimental evidence against a null hypothesis, making use of the cumulative distribution table below, where $X\sim \textrm{Po}(16).$

Assuming the visits occur independently, complete this hypothesis test and state your conclusion.

#### Explanation

Let $\lambda$ be the average rate at which the website is visited per hour. Then, we have the following null and alternative hypotheses:

- $H_0:\quad\lambda = 16$

- $H_1:\quad\lambda < 16$

The significance level is $\alpha = 10\%=0.1.$

Under the null hypothesis, the visits occur independently at a constant average rate of $\lambda=16$ per hour. Therefore,

$$


X\sim \textrm{Po}(16).


$$

The web designer conducted an experiment and found that $10$ visits to the website occurred one hour after the website was rebranded. Therefore, a suitable test statistic is $P(X\leq 10).$

Under the null hypothesis, the value of our test statistic is

$$


\begin{aligned}𝑃(𝑋≤10) & =0.0774.\end{aligned}


$$

Let's interpret this result:

- Since $P(\boxed{\color{blue}X\leq 10}) \boxed{\color{blue}<} 10\%,$ the experimental result is unlikely under the null hypothesis.

- In other words, there is $\boxed{\color{blue}\textrm{sufficient}}$ evidence to reject $H_0.$

- Therefore, we $\boxed{\color{blue}\textrm{can conclude}}$ that visitor rate has reduced since the website was rebranded.

### Example: Conducting a Right-Tailed Test

#### Question

A technology company produced an electronic component at an average rate of $20$ units per day. The company then decided to make some mechanical improvements to increase production efficiency. After the improvements were made, the company supervisor conducted a hypothesis test at the $10\%$ significance level to test whether the production rate had increased.

The supervisor noticed that $23$ units were produced on a randomly selected day after the upgrade. He compared this experimental evidence against a null hypothesis, making use of the cumulative distribution table below, where $X \sim \textrm{Po}(20).$

Assuming that the production of electronic components occurs independently, complete this hypothesis test and state your conclusion.

#### Explanation

Let $\lambda$ be the average production rate of electronic components per day. Then, we have the following null and alternative hypotheses:

- $H_0:\quad\lambda = 20$

- $H_1:\quad\lambda \gt 20$

The significance level is $\alpha = 10\% = 0.1.$

Under the null hypothesis, the production of electronic components occurs independently at a constant average rate of $\lambda = 20$ per day. Therefore,

$$


X \sim \textrm{Po}(20).


$$

The supervisor conducted an experiment and found that $23$ electronic components were produced on a particular day since the mechanical improvements were made. Therefore, a suitable test statistic is $P(X \geq 23).$

Under the null hypothesis, the value of our test statistic is

$$


\begin{aligned}𝑃(𝑋≥23) & =1−𝑃(𝑋≤22) \\ & =1−0.7206 \\ & =0.2794.\end{aligned}


$$

Let's interpret this result:

- Since $P(\boxed{\color{blue}X \geq 23}) \boxed{\color{blue}\gt} 10 \%,$ the experimental result is likely under the null hypothesis.

- In other words, there is $\boxed{\color{blue}\textrm{insufficient}}$ evidence to reject $H_0.$

- Therefore, we $\boxed{\color{blue}\textrm{cannot conclude}}$ that the production rate has increased since the improvements to the machines were made.

### Justification for Using Equality for the Null Hypothesis

Suppose we're testing whether a shop's order rate has *decreased* from its usual orders per day. We set up the hypotheses and with a significance level of

Now, suppose we observe orders on a randomly selected day. This is *more* than not less! What should we conclude?

Under the null hypothesis, using we have Since we do *not* reject This makes sense: observing orders provides *zero* evidence that the rate has decreased. In fact, it suggests the rate might be *higher*—but that's not what our alternative hypothesis claims.

This example highlights an important point. Strictly speaking, the null hypothesis—that the rate has *not* decreased—should be not So, why do we use the equality form?

To calculate a probability like we need a *single* value of The statement "" describes infinitely many Poisson distributions—one for each value of from to infinity. We cannot compute a single probability under all of these distributions at once.

The solution is to use the *boundary* value This is called the **least favorable value** because it's the point in the null region closest to the alternative. Among all values low observations are most likely when making it the *hardest* point to reject in favor of

To see this concretely, suppose we had observed orders instead. Under the null hypothesis, testing different values of:

- At the boundary so we reject.

- At so we reject.

- At so we reject.

The probability of the observation under each null hypothesis option gets *smaller* as increases, because low values become increasingly unlikely.

If our data provide sufficient evidence to reject at they provide sufficient evidence to reject at any fixed value of as well. So, by testing at the boundary, we effectively test the entire null region.
