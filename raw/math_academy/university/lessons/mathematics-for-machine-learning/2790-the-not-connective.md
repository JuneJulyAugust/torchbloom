# The "Not" Connective

Source: https://www.mathacademy.com/topics/2790?courseId=145
Topic ID: 2790

## Prerequisites

- [Truth Tables](./4252-truth-tables.md)

## Lesson

### Introduction

The **negation** of a mathematical statement is its *opposite* statement. A mathematical statement and its negation have opposite truth values.

For example:

- The negation of the *true* statement "$4$ is divisible by $2$" is the *false* statement "$4$ is **not** divisible by $2.$"

- The negation of the *false* statement "$5$ is even" is the *true* statement "$5$ is odd."

We can express negations using the symbol "$\neg$". The negation of $A$ is denoted $\neg A,$ and has the opposite truth values as $A{:}$

We can negate compound statements as well. For example, the statement $\neg (A \land B)$ has the opposite truth values as the statement $A \land B{:}$

### Example: Negating a Plain English Statement

#### Question

Consider the following statement.

$P: 1$ is **** smaller than $2$

What statement represents $\neg P?$

#### Explanation

The symbol "$\neg$" represents negation. So, our task is to negate the given sentence.

To negate our plain English sentence, we place the words "It is not true that" in front of it. This gives the following:

It is **** true that $1$ is **** smaller than $2.$

In other words, $1$ is smaller than $2.$ Therefore, $\neg P$ means the following:

$1$ is smaller than $2.$

Note that $P$ is **** while $\neg P$ is ****

### Example: Expressing a Negated Sentence in Symbolic Form

#### Question

Consider the following statement:

$\dfrac12$ is **** a natural number, or $\sqrt{2}$ is **** a real number.

Express the compound statement above in symbolic form given the following:

- $\frac{1}{2}$

- $\sqrt{√2}$

#### Explanation

The sentence

$\dfrac12$ is **** a natural number

can be expressed symbolically as $\neg P.$

The sentence

$\sqrt{2}$ is **** a real number

can be expressed symbolically as $\neg Q.$

Therefore, the sentence

$\dfrac12$ is **** a natural number, or $\sqrt{2}$ is **** a real number

can be expressed symbolically as $\neg P \lor \neg Q.$

### Example: Completing a Truth Table for a Compound Statement

#### Question

Find the missing values in the following truth table:

#### Explanation

First, we add a column for $\neg Q.$ Remember that the truth values of $\neg Q$ are opposite those of $Q.$

Then, we add a column for $P \land \neg Q.$ Remember that $P \land \neg Q$ is true if both $P$ and $\neg Q$ are true.

Finally, we add a column for $\neg (P \land \neg Q).$ Remember that the truth values of $\neg (P \land \neg Q)$ are opposite those of $P \land \neg Q.$

### Double Negations

When we have two negations in a row, we can cancel them out.

- For example, $\neg (\neg A)$ can be simplified to $A.$

- Likewise, $\neg (\neg (A \land B))$ can be simplified to $A \land B.$

To understand why negations cancel with each other, consider the following statement:

$4$ is divisible by $2.$

The negation of this statement is

$4$ is **not** divisible by $2.$

If we negate again, we get back the original sentence:

$4$ divisible by $2.$

So, if we negate a statement twice, we end up with the original statement.

More formally, we can prove that $\neg (\neg A) \equiv A$ using a truth table.

Since $A$ and $\neg(\neg A)$ have the same truth values, they are logically equivalent.

### Example: Simplifying a Double Negation

#### Question

Simplify the statement $\neg(\neg C) \lor \neg(\neg(C \land D)).$

#### Explanation

Two negations in a row cancel each other out. So:

- we can simplify $\neg(\neg C)$ to $C,$ and

- we can also simplify $\neg(\neg(C \land D))$ to $C \land D.$

Therefore, the given statement can be simplified to

$$


C \lor (C \land D).


$$
