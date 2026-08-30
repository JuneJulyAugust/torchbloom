# Additional Rules of Logical Inference

Source: https://www.mathacademy.com/topics/4306?courseId=76
Topic ID: 4306

## Prerequisites

- [Disjunctive Syllogism and Transitivity of Implication](./4305-disjunctive-syllogism-and-transitivity-of-implication.md)

## Lesson

### Introduction

There are many inference rules in mathematical logic. In this lesson, we'll consider three more of them:

- The first of them is called **conjunction introduction** It asserts that if $P$ and $Q$ are both true, then "$P$ and $Q$" is also true.

- The second one is **conjunction elimination**: It asserts that if "$P$ and $Q$" is true, then both $P$ and $Q$ are true.

- And the third one is called **disjunction introduction**: It asserts that if $P$ is true, then "$P$ or $Q$" is also true.

### A Concrete Example

Let's complete the following logical inference using conjunction elimination.

$$


\begin{aligned}x is positive and irrational \\ ∴\,𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴\end{aligned}


$$

Recall that conjunction elimination asserts that if "$P$ and $Q$" is true, then both $P$ and $Q$ are true.

Let's denote:

- $P(x):$ $x$ is positive

- $Q(x):$ $x$ is irrational

Then, using the conjunction elimination rule, we obtain the following:

$$


\begin{aligned}𝑃∧𝑄 \\ ∴𝑄\end{aligned}


$$

Therefore, we have:

$$


\begin{aligned}x is positive and irrational \\ ∴\,x is irrational\end{aligned}


$$

Since conjunction is commutative, $𝑥$ is also a valid conclusion.

### Example: Completing an Inference Rule

#### Question

$$


\begin{aligned}𝑃∧𝑄 \\ ∴\,𝐴\end{aligned}


$$

Which of the following is the missing part of the logical inference rule above?

1. $P$

2. $\mathbf{t}$ (tautology)

3. $\lnot Q$

#### Explanation

The logical inference rule of ** asserts that if "$P$ and $Q$" is true, then both $P$ and $Q$ are true.

The logical inference rule of ** can be written as follows:

$$


\begin{aligned}𝑃∧𝑄 \\ ∴𝑃\end{aligned}


$$

We can also write the following:

$$


\begin{aligned}𝑃∧𝑄 \\ ∴𝑄\end{aligned}


$$

Therefore, from the given options, the correct answer is "I only."

### Example: Logical Inference Using the Additional Rules

#### Question

$$


\begin{aligned}x is a perfect square and odd \\ ∴\,𝐴𝐴\end{aligned}


$$

Which of the following is the missing part of the logical inference rule above?

1. $x$ is not a perfect square

2. $x$ is odd

3. $x$ is not odd

#### Explanation

The logical inference rule of ** asserts that if "$P$ and $Q$" is true, then both $P$ and $Q$ are true.

Let's denote:

- $P(x):$ $x$ is a perfect square

- $Q(x):$ $x$ is odd

Then, using the conjunction elimination rule, we obtain the following:

$$


\begin{aligned}𝑃∧𝑄 \\ ∴𝑄\end{aligned}


$$

Therefore, we have:

$$


\begin{aligned}x is a perfect square and x is odd \\ ∴\,x is odd\end{aligned}


$$

Hence, the correct answer is "II only."

### Combining the Rules of Logical Inference

The inference rules can be combined into multi-step derivations.

For example, suppose we are given the following facts:

- $n$ is positive and even

- If $n$ is even, then $6 \mid 3n$ is integer

Let's see what can be inferred from this.

Let's denote:

- $P(n):$ $n$ is positive

- $Q(n):$ $n$ is even

- $R(n):$ $6 \mid 3n$

With that in mind, let's apply some logical inference rules.

- Using the logical inference rule of *conjunction elimination*, we obtain the following:

- Using the logical inference rule of *implication elimination* (also known as *modus ponens*) with the conclusion of the previous step, we get the following:

In other words, given the above information, we can conclude that $3n$ must be divisible by $6.$

### Example: Combining Inference Rules in Symbolic Form

#### Question

$$


\begin{aligned}𝑃⇒¬𝑄 \\ 𝑃 \\ ∴¬𝑄 \\ 𝑄∨𝑅 \\ ∴\,𝐴𝐴𝐴𝐴\end{aligned}


$$

Which of the following statements complete the above proof?

1. $R$

2. $\lnot R \lor Q$

3. $\lnot Q$

#### Explanation

Using the logical inference rule of implication elimination (also known as modus ponens), we obtain the following:

$$


\begin{aligned}𝑃⇒¬𝑄 \\ 𝑃 \\ ∴¬𝑄\end{aligned}


$$

Using the logical inference rule of disjunctive syllogism with the conclusion from the previous step, we get the following:

$$


\begin{aligned}¬𝑄 \\ 𝑄∨𝑅 \\ ∴𝑅\end{aligned}


$$

Therefore, the correct answer is "I only."

### Example: Combining Rules of Inference

#### Question

$$


\begin{aligned}If y is prime, then y is not divisible by 3 \\ y is divisible by 3 \\ ∴y is not prime \\ y is prime or y \geq 3 \\ ∴\,𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴\end{aligned}


$$

What is the missing part of the logical inference rule above?

#### Explanation

Let's denote:

- $P(y):$ $y$ is prime

- $Q(y):$ $y$ is divisible by $3$

- $R(y):$ $y\geq 3$

With that in mind, let's apply some logical inference rules.

- Using the logical inference rule of ** (also known as **), we obtain the following:

- Using the logical inference rule of ** (also known as **) with the conclusion from the previous step, we get the following:

So, the missing part is $y \geq 3.$
