# Finding Conditional Probabilities From Frequency Tables

Source: https://www.mathacademy.com/topics/6222?courseId=120
Topic ID: 6222

## Prerequisites

- [Solving Rational Equations Using Cross-Multiplication](../../../high-school/traditional/lessons/algebra-i/698-solving-rational-equations-using-cross-multiplication.md)
- [The Multiplication Law for Conditional Probability](../../../high-school/traditional/lessons/geometry/715-the-multiplication-law-for-conditional-probability.md)
- [Joint Frequency Tables](../../../middle-school/lessons/grade-7/1498-joint-frequency-tables.md)

## Lesson

### Introduction

In this lesson, we'll learn how to calculate conditional probabilities from frequency tables. The key is to recognize that we will usually be comparing two counts:

- the number of outcomes that satisfy both the *event* $(A)$ and the *condition* $(B),$ and

- the number of outcomes that satisfy the condition alone.

Recall that in symbols, the conditional probability is given by

$$


P(A \mid B) = \dfrac{P(A \cap B)}{P(B)} = \dfrac{\#(A \cap B)}{\#(B)},


$$

where $\#$ denotes the function that returns the number of elements in the corresponding set.

For example, the table below shows the distribution of participants’ workout durations.

If a participant who exercised at least $40$ minutes is selected at random, what is the probability that the participant exercised at least $60$ minutes?

To determine the desired probability, we must find the fraction of participants who exercised at least $60$ minutes among those who exercised at least $40$ minutes:

$$


\begin{aligned}\,\,\,\,\,\,𝑃(Exercised≥60\,|\,Exercised≥40) & = \\ \frac{# participants who exercised at least 40 and at least 60}{# participants who exercised at least 40} & = \\ \frac{# participants who exercised at least 60}{# participants who exercised at least 40} & \end{aligned}


$$

The total number of participants who exercised at least $40$ minutes is the sum of the participants in the $40 - 59,$ $60 - 79,$ and $80 - 100$ groups:

$$


{\color{blue}12 + 9 + 4} = {\color{blue}25}


$$

On the other hand, the number of participants who exercised at least $60$ minutes is the sum of the participants in the $60 - 79$ and $80 - 100$ groups:

$$


{\color{red}9} + {\color{red}4} = {\color{red}13}


$$

Therefore, the fraction of participants who exercised at least $60$ minutes out of those who exercised at least $40$ minutes is

$$


P(\text{Exercised} \geq 60 \: | \: \text{Exercised} \geq 40) = \dfrac{\color{red}13}{\color{blue}25}.


$$

**Watch out!** A common mistake is dividing by the grand total instead of the conditional group. So, we always identify the condition first, then narrow down to the event.

### Example: Finding Conditional Probabilities From a Frequency Table

#### Question

The table above shows the distribution of online order values. If an order between $25$ and $100$ is selected at random, what is the probability that the order is between $50$ and $75?$

#### Explanation

To determine the desired probability, we must find the fraction of orders between $50$ and $75$ among those between $25$ and $100:$

$$


\begin{aligned}\,\,\,\,\,\,\,\,\,\,\,\,\,\,\, 𝑃(50≤Value≤75\,|\,25 & ≤Value≤100) \\ & =\frac{# orders between 25 and 100 and between 50 and 75}{# orders between 25 and 100} \\ & =\frac{# orders between 50 and 75}{# orders between 25 and 100}\end{aligned}


$$

The total number of orders between $25$ and $100$ is the sum of the orders in the $25 - 50$, $50 - 75,$ and $75 - 100$ groups:

$$


12 + 15 + 9 = 36


$$

On the other hand, the number of orders between $50$ and $75$ is the number of orders in the $50 - 75$ group:

$$


15


$$

Therefore, the fraction of orders between $50$ and $75$ out of those between $25$ and $100$ is

$$


P(50 \leq \text{Value} \leq 75 \: | \: 25 \leq \text{Value} \leq 100) = \dfrac{15}{36} = \dfrac{5}{12}.


$$

### Joint Frequency Tables

So far, we have seen how to calculate conditional probabilities from a one-way frequency table. But many real data sets are organized by two features at once. In such cases, we summarize the data in a *joint frequency table*.

The formula remains the same:

$$


P(A \mid B) = \dfrac{P(A \cap B)}{P(B)} = \dfrac{\#(A \cap B)}{\#(B)}


$$

But now, the events $A$ and $B$ often refer to different categories from different features.

For example, the table below shows the number of people by group and library membership.

If an adult is selected at random, what is the probability that the adult does not have a library card?

To determine the desired probability, we must find the fraction of adults without a library card among all adults:

$$


P(\text{No card} \: | \: \text{Adult}) = \dfrac{\text{# Adults without a card}}{\text{# Adults}}


$$

From the table, we can see that a total of $\color{red}{42}$ adults responded. Of these, $\color{blue}{24}$ do not have a card.

Therefore, the fraction of adults without a library card among all adults is

$$


P(\text{No card} \: | \: \text{Adult}) = \dfrac{24}{42} = \dfrac{4}{7}.


$$

### Example: Finding Conditional Probabilities From a Joint Frequency Table

#### Question

The table above shows the employment types of different groups of employees. If an employee from the Managers group is selected at random, what is the probability that they are either full-time or contract?

#### Explanation

To determine the desired probability, we must find the fraction of employees who are full-time or contract among those who are managers:

$$


\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\! P(\text{Full-Time or Contract} \: | \: \text{Managers}) = \dfrac{\text{# Managers working full-time or contract}}{\text{# Managers}}


$$

From the table, we can see that a total of $\color{red}{40}$ managers are listed. Of these,

$$


{\color{blue}{21}} + {\color{blue}{9}} = 30


$$

are full-time or contract employees.

Therefore, the fraction of employees who are full-time or contract among those who are managers is

$$


P(\text{Full-Time or Contract} \: | \: \text{Managers}) = \dfrac{30}{40} = \dfrac{3}{4}.


$$

### Example: Finding Conditional Probabilities From a Joint Frequency Table: Totals Not Given

#### Question

The table above shows the attendance at different events by groups of people. If a couple is selected at random, what is the probability that they attended either concerts or sports?

#### Explanation

To determine the desired probability, we must find the fraction of couples who attended either concerts or sports:

$$


\!\!\!\!\!\!\!\!\!\!\!\!\!\! P(\text{Concerts or Sports} \: | \: \text{Couples}) = \dfrac{\text{# Couples attending concerts or sports}}{\text{# Couples}}


$$

From the table, we can see that a total of

$$


20 + 18 + 24 = {\color{red}62}


$$

couples were surveyed. Of these,

$$


{\color{blue}{20}} + {\color{blue}{24}} = 44


$$

attended either concerts or sports.

Therefore, the fraction of couples who attended either concerts or sports is

$$


P(\text{Concerts or Sports} \: | \: \text{Couples}) = \dfrac{44}{62} = \dfrac{22}{31}.


$$

### Example: Conditional Probabilities With Unknown Frequencies

#### Question

A survey records whether people are vegetarians and whether they prefer organic food. The data is summarized in the table below.

Complete the frequency table given that, if a person who prefers conventional food is selected at random, the probability that the person is a vegetarian is $\dfrac{3}{8}.$

#### Explanation

We are told that

$$


P(\text{Vegetarian} \: | \: \text{Conventional}) = \dfrac38.


$$

This probability is the fraction of vegetarians among those who prefer conventional food:

$$


P(\text{Vegetarian} \: | \: \text{Conventional}) = \dfrac{\text{# Vegetarians who prefer conventional food}}{\text{# People who prefer conventional food}}


$$

Let $x$ be the number of vegetarians who prefer conventional food. From the table, we can see that a total of

$$


\color{red}20 + x


$$

people prefer conventional food. Of these, $\color{blue}x$ are vegetarians.

Therefore, the fraction of vegetarians among those who prefer conventional food is

$$


P(\text{Vegetarian} \: | \: \text{Conventional}) = \dfrac{x}{20+x}.


$$

Since this probability is equal to $\dfrac38,$ we can solve for $x$ as follows:

$$


\begin{aligned}\frac{3}{8} & =\frac{𝑥}{20+𝑥} \\ 3(20+𝑥) & =8𝑥 \\ 60+3𝑥 & =8𝑥 \\ 5𝑥 & =60 \\ 𝑥 & =12\end{aligned}


$$

The completed table is shown below.
