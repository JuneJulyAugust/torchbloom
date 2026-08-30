# Expected Values of Discrete Random Variables

Source: https://www.mathacademy.com/topics/730?courseId=101
Topic ID: 730

## Prerequisites

- [Probability Mass Functions of Discrete Random Variables](./1290-probability-mass-functions-of-discrete-random-variables.md)
- [The Mean of a Data Set](../integrated-math-ii-honors/1634-the-mean-of-a-data-set.md)

## Lesson

### Introduction

The **expected value** (also known as the **expectation** or **mean**) of a discrete random variable is the average value we'd expect to get if we observed the random variable many times.

For a discrete random variable $X$ with probability mass function $f(x)$ defined over a set $S,$ we can calculate the expected value using the following formula:

$$


\textrm E[X] = \sum\limits_{x \in S} x \cdot f(x)


$$

In other words, the expected value is the sum of products of each value of $X$ and its associated probability, taken over all possible values of $X.$

### Example: Calculating the Expected Value for a Random Variable with Uniform Probability

#### Question

What is the expected value of one roll of a tetrahedral die?

#### Explanation

The expected value of a discrete random variable $X$ with probability mass function $f(x)$ defined over a set $S$ is given by

$$


\textrm E[X] = \sum\limits_{x \in S} x \cdot f(x).


$$

A tetrahedral die has four sides. Let $X$ be the score attained on a random roll of the die. Then the support is $S = \{1,2,3,4 \},$ and the corresponding probabilities are all $\dfrac{1}{4}{:}$

$$


f(1) = f(2) = f(3) = f(4) = \dfrac{1}{4}


$$

Summing up the products of each value of $X$ and its associated probability, we get

$$


\begin{aligned}E[𝑋] & =1⋅𝑓(1)+2⋅𝑓(2)+3⋅𝑓(3)+4⋅𝑓(4) \\ & =1(\frac{1}{4})+2(\frac{1}{4})+3(\frac{1}{4})+4(\frac{1}{4}) \\ & =\frac{1}{4}+\frac{2}{4}+\frac{3}{4}+\frac{4}{4} \\ & =\frac{1+2+3+4}{4} \\ & =\frac{10}{4} \\ & =2.5.\end{aligned}


$$

### Example: Calculating the Expected Value for a Random Variable with Non-Uniform Probability

#### Question

The rolls of an unfair tetrahedral die follow the probability mass function $f(x)$ as shown in the table below. What is the expected value of one roll of the die?

#### Explanation

The expected value of a discrete random variable $X$ with probability mass function $f(x)$ defined over a set $S$ is given by

$$


\textrm E[X] = \sum\limits_{x \in S} x \cdot f(x).


$$

Summing up the products of each value of $X$ and its associated probability, we get

$$


\begin{aligned}E[𝑋] & =1⋅𝑓(1)+2⋅𝑓(2)+3⋅𝑓(3)+4⋅𝑓(4) \\ & =1(\frac{1}{10})+2(\frac{3}{10})+3(\frac{2}{5})+4(\frac{1}{5}) \\ & =\frac{1}{10}+\frac{6}{10}+\frac{6}{5}+\frac{4}{5} \\ & =\frac{1}{10}+\frac{6}{10}+\frac{12}{10}+\frac{8}{10} \\ & =\frac{1+6+12+8}{10} \\ & =\frac{27}{10} \\ & =2.7\,.\end{aligned}


$$

### Example: Calculating the Expected Value Given the Frequency of a Random Variable

#### Question

Several children were asked about how many pets they have. The results were recorded below. If $X$ is the number of pets that a randomly selected child has, what is the expected value of $X?$

#### Explanation

The expected value of a discrete random variable $X$ with probability mass function $f(x)$ defined over a set $S$ is given by

$$


\textrm E[X] = \sum\limits_{x \in S} x \cdot f(x).


$$

We're given the frequencies of the number of pets, so we can start by computing the corresponding probabilities. The total number of children is $5+6+5=16,$ so the corresponding probabilities are as follows:

$$


\begin{aligned}𝑃(𝑋=0)=𝑓(0) & =\frac{5}{16} \\ 𝑃(𝑋=1)=𝑓(1) & =\frac{6}{16}=\frac{3}{8} \\ 𝑃(𝑋=2)=𝑓(2) & =\frac{5}{16}\end{aligned}


$$

We organize these results in the table below.

Now, summing up the products of each value of $X$ and its associated probability, we get

$$


\begin{aligned}E[𝑋] & =0⋅𝑓(0)+1⋅𝑓(1)+2⋅𝑓(2) \\ & =0(\frac{5}{16})+1(\frac{3}{8})+2(\frac{5}{16}) \\ & =0+\frac{3}{8}+\frac{10}{16} \\ & =0+\frac{6}{16}+\frac{10}{16} \\ & =\frac{0+6+10}{16} \\ & =\frac{16}{16} \\ & =1\,.\end{aligned}


$$

### Example: Calculating the Expected Profit of a Game

#### Question

Suppose that we play a game with a stack of five cards labeled $1$ through $5.$ A card is drawn at random. Drawing $1,2,3,$ or $4$ means that you lose $1,$ and drawing a $5$ means that you win $ 5.$ What is the expected profit at each drawing in this game?

#### Explanation

Let $p$ represent the profit on a draw in this game. On each draw in the game, there are two possible outcomes:

- drawing $1,2,3,4$, the player loses $1,$ so we have $p=-1.$

- drawing $5$, the player wins $5,$ so we have $p=5.$

The probabilities for the outcomes are

$$


P(-1)=\dfrac{4}{5}, \qquad P(5)=\dfrac{1}{5}.


$$

Let's summarize this in a table. If $p$ is the profit (in dollars) on a single draw, and $f(p)$ is the probability mass function for $p,$ then we have the following:

Therefore, the expected value of $p$ is given by

$$


\begin{aligned} \textrm E[p] &= -1 \cdot f(-1) + 5 \cdot f(5) \\\[5pt] &= -1 \left( \dfrac{4}{5} \right) + 5 \left( \dfrac{1}{5} \right) \\\[5pt] &=-\dfrac{4}{5} + 1 \\[3pt] &=\dfrac{1}{5} \\[3pt] &=0.2 \end{aligned}


$$

Therefore, the expected profit at each draw in this game is $0.20$.
