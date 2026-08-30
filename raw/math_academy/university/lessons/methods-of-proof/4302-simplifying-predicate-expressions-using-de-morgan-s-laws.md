# Simplifying Predicate Expressions Using De Morgan's Laws

Source: https://www.mathacademy.com/topics/4302?courseId=76
Topic ID: 4302

## Prerequisites

- [De Morgan's Laws for Logic](./230-de-morgan-s-laws-for-logic.md)
- [The "And" and "Or" Connectives With Predicates](./4255-the-and-and-or-connectives-with-predicates.md)
- [The "Not" Connective With Predicates](./4256-the-not-connective-with-predicates.md)

## Lesson

### Introduction

Logical operations with predicates generalize the corresponding operations on statements. As a result, all the properties of these operations are held.

In particular, for predicates $P(x_1,x_2\ldots,x_n)$ and $Q(y_1,y_2\ldots,y_m),$ De Morgan's laws state the following:

$$


\begin{aligned}¬(𝑃∧𝑄) & ≡¬𝑃∨¬𝑄 \\ ¬(𝑃∨𝑄) & ≡¬𝑃∧¬𝑄\end{aligned}


$$

These can be used to negate open sentences containing conjunctions and disjunctions. For example, let's negate the following:

$$


n \ge 0 \:\textbf{ or }\: 2 \mid m


$$

Applying De Morgan's law for disjunctions, we obtain

$$


\begin{aligned}¬(𝑛≥0\, 𝐨𝐫 \,2∣𝑚) & ≡¬(𝑛≥0∨2∣𝑚) \\ & ≡¬(𝑛≥0)∧¬(2∣𝑚) \\ & ≡𝑛<0∧2∤𝑚 \\ & ≡𝑛<0\, 𝐚𝐧𝐝 \,2∤𝑚.\end{aligned}


$$

### Example: Expressing a Predicate in Symbolic Form

#### Question

$\qquad$ $x$ is greater than $4,$ or $x$ is irrational.

Express the compound predicate above in symbolic form given the following predicates:

- $P(x):$ $x$ is greater than $4$

- $Q(x):$ $x$ is rational

#### Explanation

The sentence

$\qquad$ $x$ is irrational

can be expressed in symbolic form as $\lnot Q.$

Therefore, the given sentence is expressed symbolically as

$$


P\lor \lnot Q.


$$

### Example: Negating a Conjunction Using De Morgan's Law

#### Question

$\qquad$ $x$ is prime and $y$ divides $12$.

What is the negation of the composite predicate above?

#### Explanation

De Morgan's law for conjunctions states that

$$


\neg ( A \land B) = \neg A \lor \neg B.


$$

So, the negation of "$x$ is prime and $y$ divides $12$" is

$$


\begin{aligned}¬(𝑥 is prime and 𝑦 divides 12) & ≡¬(𝑥 is prime∧𝑦 divides 12) \\ & ≡¬(𝑥 is prime)∨¬(𝑦 divides 12) \\ & ≡𝑥 is not prime∨𝑦 does not divide 12 \\ & ≡𝑥 is not prime or 𝑦 does not divide 12.\end{aligned}


$$

### Example: Negating a Disjunction Using De Morgan's Law

#### Question

$\qquad$ $x$ is a multiple of $5$ or $y$ divides $24$.

What is the negation of the composite predicate above?

#### Explanation

De Morgan's law for disjunctions states that

$$


\neg ( A \lor B) = \neg A \land \neg B.


$$

So, the negation of "$x$ is a multiple of $5$ or $y$ divides $24$" is

$$


\begin{aligned}¬(𝑥 is a multiple of 5 or 𝑦 divides 24) & ≡¬(𝑥 is a multiple of 5∨𝑦 divides 24) \\ & ≡¬(𝑥 is a multiple of 5)∧¬(𝑦 divides 24) \\ & ≡𝑥 is not a multiple of 5∧𝑦 does not divide 24 \\ & ≡𝑥 is not a multiple of 5 and 𝑦 does not divide 24.\end{aligned}


$$
