# The Law of Total Expectation for Discrete Random Variables

Source: https://www.mathacademy.com/topics/5997?courseId=73
Topic ID: 5997

## Prerequisites

- [Extending the Law of Total Probability](./971-extending-the-law-of-total-probability.md)
- [Conditional Expectation for Discrete Random Variables](./3053-conditional-expectation-for-discrete-random-variables.md)
- [Mean and Variance of the Discrete Uniform Distribution](./3402-mean-and-variance-of-the-discrete-uniform-distribution.md)

## Lesson

### Introduction

Recall that if $X$ is a discrete random variable, the expected value of $X$ is given by

$$


\textrm{E}[X] = \sum_{x} x\cdot P(X = x).


$$

There is an alternative method for computing $\textrm{E}[X],$ which allows us to compute the expected value of a random variable by conditioning on another variable.

Suppose another discrete random variable $Y$ takes on a set of possible values. If we know $\textrm{E}[X \mid Y = y]$ for each value $y,$ then the **law of total expectation** states

$$


\textrm{E}[X] = \sum_{y} \textrm{E}[X \mid Y = y] \cdot P(Y = y).


$$

Conceptually, this tells us that $\textrm{E}[X]$ is just a weighted average of the conditional expectations $\textrm{E}[X \mid Y = y],$ where each weight is the probability $P(Y = y).$

In many problems, directly computing $\textrm{E}[X]$ from the definition can be difficult. It turns out that breaking $\textrm{E}[X]$ up into conditional pieces often simplifies things. The law of total expectation is especially useful when $X$ depends on an underlying condition $Y,$ and each conditional case is easier to analyze than the full distribution of $X.$

Let’s see how this works in practice with a few examples.

### A Worked Example of the Total Expectation

Let $X$ and $Y$ be discrete random variables, where $Y$ takes values $\alpha$ and $\beta$ with probabilities $0.4$ and $0.6,$ respectively. Suppose we are given the following conditional expectations:

- $\textrm{E}[X \mid Y = \alpha] = 7$

- $\textrm{E}[X \mid Y = \beta] = 3$

Let's compute $\textrm{E}[X]$ using the law of total expectation.

The law of total expectation states

$$


\textrm{E}[X]= \sum_y \textrm{E} [X \mid Y = y] \cdot P(Y=y).


$$

In this problem, $Y$ takes two values:

- $Y = \alpha$ with probability $0.4,$ and $\textrm{E}[X \mid Y = \alpha] = 7$

- $Y = \beta$ with probability $0.6,$ and $\textrm{E}[X \mid Y = \beta] = 3$

So, we calculate our expected value as follows:

$$


\begin{aligned}E[𝑋] & =E[𝑋∣𝑌=𝛼]⋅𝑃(𝑌=𝛼)+E[𝑋∣𝑌=𝛽]⋅𝑃(𝑌=𝛽) \\ & =7⋅0.4+3⋅0.6 \\ & =2.8+1.8 \\ & =4.6\end{aligned}


$$

### Example: Calculating an Expectation

#### Question

Let $X$ and $Y$ be discrete random variables, where $Y$ takes values $u,$ $v,$ and $w$ with probabilities $0.2,$ $0.5,$ and $0.3,$ respectively. You are given the following conditional expectations:

$$


\textrm{E}[X \mid Y=u] = 6, \quad \textrm{E}[X \mid Y=v] = 9, \quad \textrm{E}[X \mid Y=w] = 3.


$$

What is $\textrm{E}[X]?$

#### Explanation

We are given the conditional expectations of $X$ given different values of another random variable $Y,$ along with the probabilities of those values. This is a direct application of the law of total expectation, which states:

$$


\textrm{E}[X] = \sum_y \textrm{E}[X \mid Y = y] \cdot P(Y = y).


$$

In this problem, $Y$ takes three values:

- $Y = u$ with probability $0.2,$ and $\textrm{E}[X \mid Y = u] = 6$

- $Y = v$ with probability $0.5,$ and $\textrm{E}[X \mid Y = v] = 9$

- $Y = w$ with probability $0.3,$ and $\textrm{E}[X \mid Y = w] = 3$

So, we calculate our expected value as follows:

$$


\begin{aligned}E[𝑋] & =E[𝑋∣𝑌=𝑢]⋅𝑃(𝑌=𝑢)+E[𝑋∣𝑌=𝑣]⋅𝑃(𝑌=𝑣) \\ & \,+E[𝑋∣𝑌=𝑤]⋅𝑃(𝑌=𝑤) \\ & =6⋅0.2+9⋅0.5+3⋅0.3 \\ & =1.2+4.5+0.9 \\ & =6.6\end{aligned}


$$

### Example: Calculating an Expectation in Context

#### Question

A wildlife researcher is sent to either Forest $1$ or Forest $2$ to record animal sightings. With probability $0.7,$ he is sent to Forest $1,$ where the expected number of sightings in a day is $6.2.$ With probability $0.3,$ he is sent to Forest $2,$ where the expected number is $3.8.$

What is the expected number of animal sightings in a day?

#### Explanation

We are asked to compute the expected number of animal sightings the researcher records daily. This is a classic application of the law of total expectation, which allows us to calculate an overall expected value by conditioning on a related variable — in this case, the forest where the researcher is stationed.

Let $X$ be the number of animal sightings in a day, and let $Y$ be the forest to which the researcher is assigned.

- $Y = 1$ with probability $0.7,$ and $\textrm{E}[X \mid Y = 1] = 6.2.$

- $Y = 2$ with probability $0.3,$ and $\textrm{E}[X \mid Y = 2] = 3.8.$

So, we calculate our expected value as follows:

$$


\begin{aligned}E[𝑋] & =E[𝑋∣𝑌=1]⋅𝑃(𝑌=1)+E[𝑋∣𝑌=2]⋅𝑃(𝑌=2) \\ & =6.2⋅0.7+3.8⋅0.3 \\ & =4.34+1.14 \\ & =5.48\end{aligned}


$$

### The Tower Property

We’ve seen that the law of total expectation allows us to compute the expected value of a random variable $X$ by conditioning on another variable $Y.$ This idea extends naturally to a more general and elegant identity called the **tower property**:

$$


\textrm{E}[X] = \textrm{E}[\textrm{E}[X \mid Y]]


$$

At first glance, this may look abstract, so let’s unpack what it means.

The inner term $\textrm{E}[X \mid Y]$ is itself a *random variable*—its value depends on the outcome of $Y.$ The outer expectation then takes the average of that conditional expectation over all possible values of $Y.$

In other words, we are averaging $X$ in two stages:

- Within each scenario (for each possible value of $Y$), we find the expected value of $X.$

- Across all scenarios, we take the weighted average of those conditional expectations, where the weights are the probabilities of each $Y.$

Let’s explore a few examples to build some intuition.

### A Worked Example of the Tower Property

Let $X$ and $Y$ be discrete random variables, and suppose

$$


\textrm{E}[X \mid Y] = \sqrt{3}\,Y + 1.


$$

If $\textrm{E}[Y] = \sqrt3,$ let's compute $\textrm{E}[X]$.

This is a direct application of the tower property, which states that

$$


\textrm{E}[X] = \textrm{E}[\textrm{E}[X \mid Y]].


$$

So, we substitute the given expression for the inner expectation:

$$


\textrm{E}[X] = \textrm{E}\left[\sqrt{3}\,Y + 1\right]


$$

Now, we apply the linearity of expectation:

$$


\begin{aligned}E[𝑋] & =E[\sqrt{√3}\,𝑌+1] \\ & =\sqrt{√3}⋅E[𝑌]+E[1] \\ & =\sqrt{√3}⋅\sqrt{√3}+1 \\ & =4\end{aligned}


$$

### Example: Applying the Tower Property

#### Question

Let $Y$ be a discrete random variable, and suppose $\textrm{E}[X \mid Y] = 3Y + 2.$ If $\textrm{E}[X] = 20,$ what is $\textrm{E}[Y]?$

#### Explanation

We are given an expression for $\textrm{E}[X \mid Y]$ in terms of $Y,$ and the value of $\textrm{E}[X].$ This is a direct application of the tower property, which states that

$$


\textrm{E}[X] = \textrm{E}[\textrm{E}[X \mid Y]].


$$

So, we substitute the given expression for the inner expectation, which gives

$$


\textrm{E}[X] = \textrm{E}[3Y + 2].


$$

Now, we apply the linearity of expectation:

$$


\begin{aligned}E[𝑋] & =E[3𝑌+2] \\ & =3⋅E[𝑌]+2\end{aligned}


$$

We are told that $\textrm{E}[X] = 20,$ so we solve this equation as follows:

$$


\begin{aligned}20 & =3⋅E[𝑌]+2 \\ 18 & =3⋅E[𝑌] \\ E[𝑌] & =6\end{aligned}


$$

### Example: Applying the Tower Property in Context

#### Question

In a fantasy card game, a random mana level $m$ is drawn uniformly from $1$ to $201.$ A player selects a random spell costing an integer amount of mana between $1$ and $m,$ chosen uniformly at random. What is the expected cost of the spell selected?

#### Explanation

This is a two-step random process: first, a mana level $m$ is chosen uniformly from $1$ to $201,$ and then a spell is chosen uniformly from $1$ to $m.$ We are asked to find the expected value of the mana cost selected in the second step.

- Let $Y$ be the first random number, the mana level drawn uniformly from $1$ to $201.$

- Let $X$ be the cost of the spell selected, uniformly from $1$ to $Y.$

We are asked to compute $\textrm{E}[X].$ Since the distribution of $X$ depends on $Y,$ we apply the tower property:

$$


\textrm{E}[X] = \textrm{E}[\textrm{E}[X \mid Y]]


$$

Given $Y = m,$ the value of $X$ is uniformly distributed on $\{1, 2, \dots, m\},$ so

$$


\textrm{E}[X \mid Y = m] = \frac{m + 1}{2}.


$$

Therefore,

$$


\textrm{E}[X] = \textrm{E}\left[\frac{1 + Y}{2}\right].


$$

Now, we apply the linearity of expectation:

$$


\begin{aligned}E[𝑋] & =\frac{1}{2}⋅E[1+𝑌] \\ & =\frac{1}{2}⋅(1+E[𝑌])\end{aligned}


$$

Since $Y$ is uniformly distributed on $\{1, 2, \dots, 201\},$ we compute

$$


\textrm{E}[Y] = \frac{1 + 201}{2} = 101.


$$

Substituting, we find

$$


\begin{aligned}E[𝑋] & =\frac{1}{2}⋅(1+101) \\ & =\frac{1}{2}⋅102 \\ & =51.\end{aligned}


$$

### Proof of the Law of Total Expectation

Let $X$ and $Y$ be discrete random variables, and suppose $Y$ takes only two values $y_1$ and $y_2.$ We want to show that the *law of total expectation* holds in this simple case:

$$


\mathbb{E}[X] = \mathbb{E}[X \mid Y = y_1] \cdot P(Y = y_1) + \mathbb{E}[X \mid Y = y_2] \cdot P(Y = y_2)


$$

We start with the definition of expectation, given by

$$


\textrm{E}[X] = \sum_x x \cdot P(X = x).


$$

Next, we express $P(X = x)$ using the law of total probability:

$$


P(X = x) = P(X = x \mid Y = y_1) \cdot P(Y = y_1) + P(X = x \mid Y = y_2) \cdot P(Y = y_2)


$$

Substituting this expression into the expectation formula, we get

$$


\textrm{E}[X] = \sum_x x \left( P(X = x \mid Y = y_1) \cdot P(Y = y_1) + P(X = x \mid Y = y_2) \cdot P(Y = y_2) \right).


$$

We can now distribute the sum across the two terms

$$


\textrm{E}[X] = P(Y = y_1) \cdot \sum_x x \cdot P(X = x \mid Y = y_1) + P(Y = y_2) \cdot \sum_x x \cdot P(X = x \mid Y = y_2).


$$

But each of the sums above is just a conditional expectation according to the definition:

$$


\begin{aligned}\underset{𝑥}{∑}𝑥⋅𝑃(𝑋=𝑥∣𝑌=𝑦_{1}) & =E[𝑋∣𝑌=𝑦_{1}] \\ \underset{𝑥}{∑}𝑥⋅𝑃(𝑋=𝑥∣𝑌=𝑦_{2}) & =E[𝑋∣𝑌=𝑦_{2}]\end{aligned}


$$

So, we conclude that

$$


\boxed{\textrm{E}[X] = \textrm{E}[X \mid Y = y_1] \cdot P(Y = y_1) + \textrm{E}[X \mid Y = y_2] \cdot P(Y = y_2)},


$$

as required.

We can use a similar argument to prove the more general case, where $Y$ takes more than two values.

### Proof of the Tower Property

Let $X$ and $Y$ be discrete random variables. Now, we want to prove that the tower property holds:

$$


\textrm{E}[X] = \textrm{E}[\textrm{E}[X \mid Y]]


$$

We start with the definition of expectation

$$


\textrm{E}[X] = \sum_x x \cdot P(X = x).


$$

Next, we apply the law of total probability to express $P(X = x)$ in terms of $Y.$ Let $S_Y$ denote the support of $Y.$ Then, we have

$$


P(X = x) = \sum_{y \in S_Y} P(X = x \mid Y = y) \cdot P(Y = y).


$$

Substituting this into the expectation formula, we get

$$


\textrm{E}[X] = \sum_x x \left( \sum_{y \in S_Y} P(X = x \mid Y = y) \cdot P(Y = y) \right).


$$

We can now switch the order of summation:

$$


\textrm{E}[X] = \sum_{y \in S_Y} P(Y = y) \cdot \sum_x x \cdot P(X = x \mid Y = y)


$$

Each inner sum is just the conditional expectation $\textrm{E}[X \mid Y = y]{:}$

$$


\sum_x x \cdot P(X = x \mid Y = y) = \textrm{E}[X \mid Y = y]


$$

So, we conclude that

$$


\textrm{E}[X] = \sum_{y \in S_Y} \textrm{E}[X \mid Y = y] \cdot P(Y = y).


$$

But this expression is just the definition of $\textrm{E}[\textrm{E}[X \mid Y]]$ for discrete $Y{:}$

$$


\textrm{E}[\textrm{E}[X \mid Y]] = \sum_{y \in S_Y} \textrm{E}[X \mid Y = y] \cdot P(Y = y)


$$

Therefore, we have shown that

$$


\boxed{\textrm{E}[X] = \textrm{E}[\textrm{E}[X \mid Y]]},


$$

as required.
