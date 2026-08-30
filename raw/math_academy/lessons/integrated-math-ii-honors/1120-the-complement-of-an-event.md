# The Complement of an Event

Source: https://www.mathacademy.com/topics/1120?courseId=128
Topic ID: 1120

## Prerequisites

- [Using Probability to Make Predictions](../geometry/7222-using-probability-to-make-predictions.md)

## Lesson

### Introduction

The **complement** of an event $A,$ denoted $A',$ is the *opposite* of $A.$ That is to say, $A'$ is the set of outcomes in which $A$ *does not* happen.

For example, let $A$ be the event of rolling a $2$ on a fair six-sided die. Then $A'$ is the event of *not* rolling a $2.$ In other words, $A'$ is the event that we roll a $1,$ $3,$ $4,$ $5,$ or $6.$

Note that in the above scenario, we have $P(A) = \dfrac{1}{6}$ and $P(A') = \dfrac{5}{6},$ and

$$


P(A) + P(A') = \dfrac{1}{6} + \dfrac{5}{6} = 1.


$$

This is not a coincidence. The above result holds in general: for any event $A,$ we have

$$


P(A) + P(A') = 1.


$$

### Example: Computing the Probability of the Complement of an Event: Symbolic Statement

#### Question

Two fair coins are tossed. Define $A$ to be the event "we get different outcomes." What is $A'$ described in natural language, and what is $P(A')?$

#### Explanation

The **** of an event $A,$ denoted $A',$ is the ** of $A.$ That is to say, $A'$ is the set of outcomes in which $A$ ** happen.

Here, $A'$ is the opposite of the event "we get different outcomes." So $A'$ is the event "we get the same outcome." In other words, $A'$ is the event "both coins land on heads, or both coins land on tails."

Now, let's calculate the probability $P(A').$ The sample space is

$$


\mathcal S=\{ HH, HT, TH, TT \},


$$

and since the coin is fair, on each toss, we have the same probability of having "head" or "tail."

There are $4$ outcomes in the sample space, and $2$ of these outcomes ($HH, TT$) belong to $A'.$ Therefore,

$$


P(A')=\dfrac{2}{4} = \dfrac{1}{2} = 0.5.


$$

### Example: Computing the Probability of the Complement of an Event: Verbal Statement

#### Question

Five cards are picked at random from a standard $52$-cards deck. Define $A$ to be the event "there are no aces among the $5$ selected cards." It is known that $P(A) = 0.66$ to $2$ decimal places. What is the probability of the event "at least one card among the $5$ selected cards is an ace"?

#### Explanation

The event "at least one card among the $5$ selected cards is an ace" is the opposite of the event $A,$ "there are no aces among the $5$ selected cards."

So, the event "at least one card among the $5$ selected cards is an ace" is the complement of $A,$ denoted $A'.$

Since we know that $P(A)=0.66$ to $2$ decimal places, we can calculate $P\left(A'\right)$ using the formula

$$


\begin{aligned}𝑃(𝐴)+𝑃(𝐴^{′}) & =1 \\ 𝑃(𝐴^{′}) & =1−𝑃(𝐴) \\ & =1−0.66 \\ & =0.34.\end{aligned}


$$

### Example: Identifying True Statements Regarding an Event and its Complement

#### Question

A class of $25$ students took a trigonometry test and a literature test, and only $5$ students passed both tests. We randomly select a student among the $25$ students who sat the examinations. Let us call $A$ the event "the student passed both tests." Which of the following statements are true regarding this event?

1. $P(A)=0.25$

2. $A'$ is the event "the student failed at least one test"

3. $P\left(A'\right)=0.8$

#### Explanation

Let's inspect each statement in turn.

- Statement I is false. Since there were $25$ total students, and only $5$ of them passed both tests, we have that

- Statement II is true. The complement $A'$ is the opposite of the event $A,$ "the student passed both tests." So $A'$ is the event "the student failed at least one test."

- Statement III is true. Since we know that $P(A) = 0.2,$ we can calculate $P\left(A'\right)$ using the formula

Therefore, the correct answer is "II and III only."
