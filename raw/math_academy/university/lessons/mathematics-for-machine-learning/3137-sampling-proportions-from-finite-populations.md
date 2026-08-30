# Sampling Proportions From Finite Populations

Source: https://www.mathacademy.com/topics/3137?courseId=145
Topic ID: 3137

## Prerequisites

- [Mean and Variance of the Binomial Distribution](./2149-mean-and-variance-of-the-binomial-distribution.md)
- [Properties of Variance for Discrete Random Variables](./3028-properties-of-variance-for-discrete-random-variables.md)
- [The Bernoulli Distribution](./3071-the-bernoulli-distribution.md)
- [Sampling Distributions](./3864-sampling-distributions.md)

## Lesson

### Introduction

Suppose that a company is about to elect a new union representative. We're interested in determining the proportion $p$ of a company's employees that will vote for "candidate $A.$"

If the company has $N = 50$ employees, and $30$ of them will vote for candidate $A,$ then the proportion $p$ is given by

$$


p = \dfrac{30}{50} = 0.6.


$$

In other words, $60\%$ of the company's employees will vote for candidate $A.$

Note the following:

- $N$ is the **population size**

- $p$ is the **population proportion**

- The number of employees that will vote for candidate $A$ is given by

In this lesson, our goal is to build foundations for estimating $p$ in cases where the population size $N$ is very large. Note that although the population size $N$ is not very large in this example, we can still use it to help develop the key ideas.

We start by modeling the response from each member of the population as a random variable $X_i,$ defined by

$$


\begin{aligned}1,\,ith member of the population will vote for candidate 𝐴 \\ 0,\,otherwise\end{aligned}


$$

for $i = 1,\ldots,50.$

Calculating the probability that a randomly selected member of the population will vote for candidate $A$ is straightforward:

$$


\begin{aligned}𝑃(𝑋_{𝑖}=1) & =\frac{the number of members that will vote for candidate 𝐴}{population size} \\ & =\frac{𝑁𝑝}{𝑁} \\ & =\frac{30}{50} \\ & =0.6\end{aligned}


$$

**Watch out!** It's important to note that the $X_i$'s are *dependent!* For example,

$$


P(X_2 = 1 | X_1 = 1) \neq P(X_2 = 1 ).


$$

To see why, note that $P(X_2 = 1) = 0.6,$ as before. However,

$$


\begin{aligned}𝑃(𝑋_{2}=1|𝑋_{1}=1) & =\frac{(the number of members that will vote for candidate 𝐴)−1}{population size−1} \\ & =\frac{𝑁𝑝−1}{𝑁−1} \\ & =\frac{50⋅0.6−1}{50−1} \\ & =\frac{30−1}{49} \\ & =\frac{29}{49} \\ & ≈0.592 \\ & ≠𝑃(𝑋_{2}=1).\end{aligned}


$$

Let's interpret this result. We know that the first member will vote for candidate $A.$ So, to compute the conditional probability that the second member will *also* vote for candidate $A,$ we consider a reduced population with $N-1 = 49$ members, of which only $30-1 = 29$ will vote for candidate $A.$

Calculating $P(X_2 = 1 | X_1 = 0)$ works similarly, as we'll see in the following example.

### Example: Finding a Conditional Probability Given a Population Proportion

#### Question

Workers of a small company decided to elect a new union representative. There are $50$ workers, and $60\%$ of this worker population will vote for candidate $A.$ Let the random variable $X_i$ be equal to

$$


\begin{aligned}1,\,ith member of the population will vote for candidate 𝐴 \\ 0,\,otherwise\end{aligned}


$$

for $i = 1,\ldots,50.$ Find $P(X_2 = 0 | X_1 = 0).$

#### Explanation

We have a population of size $N = 50,$ and $p = 0.6$ represents the proportion of the population that will vote for candidate $A.$

Therefore:

- The number of members that will vote for candidate $A$ equals

- The number of members that will ** vote for candidate $A$ equals

We select two members of the population at random. We need to find $P(X_2 = 0 | X_1 = 0),$ the probability that the second member will ** vote for candidate $A$ given that the first member will ** vote for candidate $A$ either.

If the first member does ** vote for candidate $A,$ we have

$\qquad$ $N - 1 = 50 - 1 = 49$ members remaining, and

$\qquad$ $N(1 - p)-1 = 19$ members remaining that will not vote for candidate $A.$

Therefore,

$$


P(X_2 = 0 | X_1 = 0) = \dfrac{N(1 - p)-1}{N-1} = \dfrac{19}{49}.


$$

### Independence in Large Populations

Suppose we have a population of size $N=1\,000$ of which the proportion $p=0.5$ has a particular characteristic. We denote the random variable $X_i$ as follows:

$$


\begin{aligned}1,\,ith member of the population has the characteristic \\ 0,\,otherwise\end{aligned}


$$

for $i = 1,\ldots,1\,000.$

Technically speaking, as we saw previously, the $X_i$'s are *dependent*.

This time, however, since the population size $N = 1\,000$ is large, we may *approximate* that the $X_i$'s are *independent*.

To see why, we first note that

$$


P(X_2=1) = \dfrac{Np}{N} = 0.5.


$$

Now, computing $P(X_2 = 1 | X_1 = 1),$ we have

$$


\begin{aligned}𝑃(𝑋_{2}=1|𝑋_{1}=1) & =\frac{𝑁𝑝−1}{𝑁−1} \\ & =\frac{1\,000⋅0.5−1}{1\,000−1} \\ & =\frac{500−1}{999} \\ & =\frac{499}{999} \\ & ≈0.5.\end{aligned}


$$

To summarize, we've shown that

$$


P(X_2 = 1 | X_1 = 1) \approx P(X_2 = 1),


$$

suggesting that $X_1$ and $X_2$ are (approximately) independent.

### The Number of Sample Elements With a Characteristic

Now, suppose we conduct a random sample of size $n$ where some proportion $p$ of the population has a particular characteristic. Let's denote the random variable $X_i$ as follows:

$$


\begin{aligned}1,\,ith member of the sample has the characteristic \\ 0,\,otherwise\end{aligned}


$$

for $i = 1,\ldots,n.$

It can be shown that the $X_i$'s can be modeled as mutually independent random variables *provided that* the population size $N$ is *significantly larger* than the sample size $n$ (which we denote as $N \gg n$). In practice, this typically means that the sample size should be no larger than $5\%$ of the population size.

The assumption that the population size is much larger than the sample size is true in many cases. For example, the U.S. voting population consists of hundreds of millions of people, yet a typical sample from this population might consist of only a few thousand voters.

Let's now consider the following statistic:

$$


X = \sum\limits_{i=1}^{n} X_i


$$

where $X_i \sim \textrm{Bernoulli}(p).$

Since the $X_i$'s take the value $1$ if the $i$th element has the characteristic or $0$ if the $i$th element doesn't have the characteristic, the statistic $X$ can be used to count the number of elements with the characteristic. In other words, $X$ represents the number of sample elements with the characteristic.

We wish to determine the sampling distribution of $X.$ Note the following:

- Each $X_i$ can be modeled as a Bernoulli random variable, i.e., $X_i\sim \textrm{Bernoulli}(p).$

- Since we're assuming that $N\gg n,$ it follows that $X_1, X_2, \ldots, X_n$ are (approximately) *independent and identically distributed* (I.I.D) Bernoulli random variables.

- It can be shown that a sum of $n$ I.I.D. Bernoulli random variables with parameter $p$ is a binomial random variable $B(n,p)$ (we'll prove this in a separate lesson). Therefore,

$$


X = \sum\limits_{i=1}^{n} X_i \approx B(n,p).


$$

We summarize this process using the following flow chart.

![Instructional graphic](../../../lesson-assets/mathematics-for-machine-learning/topic-3137/f345334e5083c805.png)

Finally, using the formulas for the mean and variance of a Binomial random variable, we have the following approximations:

$$


\textrm{E}[X] = np, \qquad \textrm{Var}[X] = np(1-p)


$$

### Example: Properties of Sums of Bernoulli Random Variables

#### Question

Suppose we have a random sample of size $n = 360$ from a population where $35 \%$ of the population has a particular characteristic. Let the random variable $X_i$ be equal to

$$


\begin{aligned}1,\,ith member of the sample has the characteristic \\ 0,\,otherwise\end{aligned}


$$

where $i = 1, \ldots, 360.$ If the statistic $X$ is defined as

$$


\displaystyle X = \sum_{i=1}^{360} X_i


$$

find approximate values of $\textrm{E}[X]$ and $\textrm{Var}[X].$

**

#### Explanation

Suppose we have a random sample of size $n$ from a population of size $N,$ and we define the sequence of random variables $X_i$ as follows:

$$


\begin{aligned}1,\,ith member of the sample has the characteristic \\ 0,\,otherwise\end{aligned}


$$

Now, provided that $N \gg n,$ the random variables $X_i$ can be considered independent and identically distributed. Under this assumption, we have

$$


X_i\sim \textrm{Bernoulli}(p) \qquad 1\leq i\leq n


$$

where $p$ is the proportion of the population that has the characteristic.

Therefore, the random variable $X,$ defined as

$$


X = \sum_{i=1}^n X_i


$$

can be approximated as a binomial random variable $X\approx B(n,p),$ where

$$


\textrm{E}[X] = np, \qquad \textrm{Var}[X] = np(1-p).


$$

In our case, we're told that the population size is significantly larger than the sample size. Moreover, we have

$$


p = 35 \% = 0.35, \qquad n = 360.


$$

Therefore,

$$


X\approx B(360,0.35)


$$

and we have the following results for the mean and variance:

$$


\begin{aligned}E[𝑋] & =𝑛𝑝 \\ & =360⋅0.35 \\ & =126 \\ Var[𝑋] & =𝑛𝑝(1−𝑝) \\ & =360⋅0.35⋅(1−0.35) \\ & =81.9\end{aligned}


$$

### Mean and Variance of Sample Proportions

Suppose we conduct a random sample of size $n$ where some proportion $p$ of the population has a particular characteristic. Let's denote the random variable $X_i$ as follows:

$$


\begin{aligned}1,\,ith member of the sample has the characteristic \\ 0,\,otherwise\end{aligned}


$$

for $i = 1,\ldots,n.$

We know that if the population sample size $n$ is small compared to the population size $N,$ then the $X_i$'s can be modeled as mutually independent random variables. Therefore,

$$


X = \sum\limits_{i=1}^{n} X_i \approx B(n,p).


$$

Remember that $X$ represents the number of sample elements with the characteristic. Therefore, we can form an *estimate* for the population proportion $p$ as follows:

$$


\widehat{\,p} = \dfrac{X}{n} = \dfrac1 n \sum\limits_{i=1}^{n} X_i = \overline{X}


$$

Let's calculate the mean and variance of $\widehat{\,p}.$ First, recall that

$$


\textrm{E}[X] = np, \qquad \textrm{Var}[X] = np(1-p).


$$

Therefore, for the mean of $\widehat{\,p},$ we have

$$


\begin{aligned}E[\overset{\,𝑝}{ˆ}] & =E[\frac{𝑋}{𝑛}] \\ & =\frac{1}{𝑛}⋅E[𝑋] \\ & =\frac{1}{𝑛}⋅𝑛𝑝 \\ & =𝑝.\end{aligned}


$$

For the variance of $\widehat{\,p},$ we have

$$


\begin{aligned}Var[\overset{\,𝑝}{ˆ}] & =Var[\frac{𝑋}{𝑛}] \\ & =\frac{1}{𝑛^{2}}⋅Var[𝑋] \\ & =\frac{1}{𝑛^{2}}⋅𝑛𝑝(1−𝑝) \\ & =\frac{𝑝(1−𝑝)}{𝑛}.\end{aligned}


$$

To summarize, we have the following important results:

$$


\textrm{E}[\widehat{\,p}] = p, \qquad \textrm{Var}[\widehat{\,p}] = \dfrac{p(1-p)}{n}


$$

It should be noted that we don't yet know the sampling distribution of $\widehat{\,p}.$ What we *do* know is that whatever the sampling distribution of $\widehat{\,p}$ is, it has mean $p$ and variance $\dfrac{p(1-p)}{n}.$

### The Standard Error

The standard deviation of $\widehat{\,p}$ is called the **standard error** of $\widehat{\,p}$ and is denoted $\textrm{SE}[\widehat{\,p}]\mathbin{:}$

$$


\textrm{SE}[\widehat{\,p}] = \sqrt{\textrm{Var}[\widehat{\,p}]} = \sqrt{\dfrac{p(1-p)}{n}}


$$

If $p$ is unknown, we can replace it with its estimate $\widehat{\,p}$ in the standard error formula, as follows:

$$


\widehat{\textrm{SE}}[\widehat{\,p}] = \sqrt{\dfrac{\widehat{\,p}(1-\widehat{\,p})}{n}}


$$

Note that we have written $\widehat{\textrm{SE}}[\widehat{\,p}]$ to denote that the above expression is an estimate of $\textrm{SE}[\widehat{\,p}].$

### Example: Mean and Variance of Sample Proportions

#### Question

Suppose that in a population of children with only one pet, $42\%$ of children have a dog. A random sample of $n = 40$ children is taken from the population and asked what pet they have.

What is the mean and variance of $\widehat{\,p},$ the proportion of children in the sample that have a dog? Round your answers to $4$ decimal places where appropriate.

**

#### Explanation

Suppose we have a random sample of size $n$ from a population of size $N,$ and we define the sequence of random variables $X_i$ as follows:

$$


\begin{aligned}1,\,ith member of the sample has the characteristic, \\ 0,\,otherwise.\end{aligned}


$$

Now, provided that $N \gg n,$ we have that

$$


X = \sum_{i=1}^n X_i \approx B(n,p)


$$

where $p$ is the proportion of the population that have the characteristic, and

$$


\textrm{E}[X] = np, \qquad \textrm{Var}[X] = np(1-p).


$$

The sample proportion $\widehat{\,p}$ is given by

$$


\widehat{\,p} = \overline{X} = \dfrac{X}{n}.


$$

Using the properties of expectation and variance, it is straightforward to show that

$$


\textrm{E}[\widehat{\,p} ] = p, \qquad \textrm{Var}[\widehat{\,p} ] = \dfrac{p(1-p)}{n}.


$$

In our case, we have $p = 42 \% = 0.42,$ and $n = 40.$ Therefore,

$$


\begin{aligned}E[\overset{\,𝑝}{ˆ}] & =42\%=0.42, \\ Var[\overset{\,𝑝}{ˆ}] & =\frac{0.42(1−0.42)}{40} \\ & ≈0.0061\end{aligned}


$$

rounded to $4$ decimal places.
