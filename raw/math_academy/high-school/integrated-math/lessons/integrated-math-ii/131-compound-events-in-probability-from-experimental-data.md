# Compound Events in Probability From Experimental Data

Source: https://www.mathacademy.com/topics/131?courseId=133
Topic ID: 131

## Prerequisites

- [The Union of Sets](../../../traditional/lessons/geometry/2826-the-union-of-sets.md)
- [The Intersection of Sets](../../../traditional/lessons/geometry/2827-the-intersection-of-sets.md)
- [Using Experimental Probability to Make Predictions](../../../traditional/lessons/geometry/7220-using-experimental-probability-to-make-predictions.md)

## Lesson

### Introduction

Sometimes, we want to find the probability that two or more events co-occur (occur together). Events like this, involving a combination of two or more events, are called **compound events**.

For instance, the $100$ members of a volleyball club were asked about their preferences between Chinese food and Italian pizza. The results of the survey are represented in the two-way frequency table below.

Suppose that we want to find the probability that a randomly selected club member is a male that prefers pizza.

First, let $A$ be the event that a randomly selected member is **"Male"** and let $B$ be the event that a randomly selected member prefers **"Italian pizza"**.

The probability that $A$ *and* $B$ co-occur, denoted by $P(A\cap B)$ and called the **intersection**, is found by identifying the intersection of these events in the table.

The number at the intersection of the column **"Italian pizza"** and the row **"Male"** is highlighted in the table below.

Dividing this number by the total number of data points in the table $(100),$ we get

$$


\begin{aligned}𝑃(𝐴∩𝐵) & =\frac{35}{100} \\ & =0.35.\end{aligned}


$$

This represents the experimental probability that a randomly selected member prefers Italian pizza and is male.

### Example: Estimating the Probability of the Intersection of Events

#### Question

Anna surveys some students in a school, asking them what pets out of cats or dogs they have at home. Her findings are summarized in the two-way frequency table below.

Let $C$ be the event that a randomly selected student in the school ****, and $D$ be the event that a randomly selected student in the school ****. Estimate $P(C \cap D).$

#### Explanation

The event $C \cap D$ is the event that a randomly selected student in the school has both a cat and a dog.

To estimate the probability of $C \cap D,$ we need to

- find the number at the intersection of the row **** and the column ****, and then

- divide by the total number of data points in the table.

The number at the intersection of the row **** and the column **** is highlighted in the table below.

Dividing by the total number of data points in the table $(200),$ we get

$$


P(C \cap D) = \dfrac{30}{200} = 0.15.


$$

### The Union of Two Events

Let's return to our first example, where the Volleyball club members were asked about whether they preferred Italian pizza or Chinese food. The data is shown below.

Suppose we want to find the probability that a randomly selected club member either prefers Chinese food *or* is female (or both).

Let $A$ be the event that a randomly selected member prefers **"Chinese food"** and let $B$ be the event that a randomly selected member is **"Female"**.

The probability that $A$ *or* $B$ (or both) occurs, denoted by $P(A\cup B)$ and called the **union**, is found by counting the number of data points in which $A$ or $B$ occurred and dividing by the total number of data points in the table.

The numbers that are in *either* the column **"Chinese food"** *or* the row **"Female"** (or both) are highlighted in the table below.

Adding up these numbers and then dividing by the total number of data points in the table $(100),$ we get

$$


\begin{aligned}𝑃(𝐴∪𝐵) & =\frac{20+20+25}{100} \\ & =\frac{65}{100} \\ & =0.65.\end{aligned}


$$

This represents the experimental probability that a randomly selected member prefers Chinese food or is female.

### Example: Estimating the Probability of the Union of Events

#### Question

In a class, each student selected one course among the two possible options, math or physics. The results are given in the two-way frequency table below.

Estimate the probability that a randomly chosen student selected physics or is male (or both).

#### Explanation

To estimate the probability that a randomly chosen student selected physics or is male, we

- add up the numbers that are in the column **** or the row ****, and then

- divide by the total number of data points in the table.

The numbers in the column **** or the row **** are highlighted in the table below.

Adding up these numbers and then dividing by the total number of data points in the table $(50),$ we get

$$


p =\dfrac{12+20+6}{50} = \dfrac{38}{50} =0.76.


$$

### Example: Estimating Using Probabilities

#### Question

There are $250$ boys and $250$ girls in a school. Of them, $40$ boys and $40$ girls were randomly selected and asked which sport they prefer between volleyball, basketball, football, or soccer. The results of the survey are given in the two-way frequency table below.

Estimate the probability that a randomly selected student in the survey is a boy who prefers football or soccer, and then use this to estimate the number of students in the entire school who are boys that prefer football or soccer.

#### Explanation

To estimate the probability that a randomly selected student is a boy who prefers football or soccer, we

- add up the numbers at the intersection of the row **** and the columns **** and ****, and then

- divide by the total number of data points in the table.

The numbers at the intersection of the row **** and the columns **** and **** are highlighted in the table below.

Adding up these numbers and then dividing by the total number of data points in the table $(80),$ we get

$$


p = \dfrac{11+9}{80} = \dfrac{20}{80} = 0.25.


$$

This represents the estimated probability that a randomly selected student is a boy who prefers football or soccer.

Finally, to estimate the number of students in the entire school who are boys that prefer football or soccer, we multiply the total number of students in the school $(500)$ by the probability above:

$$


\begin{aligned}𝑛 & =500⋅𝑝 \\ & =500⋅0.25 \\ & =125\end{aligned}


$$
