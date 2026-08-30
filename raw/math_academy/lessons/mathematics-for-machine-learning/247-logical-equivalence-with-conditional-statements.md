# Logical Equivalence with Conditional Statements

Source: https://www.mathacademy.com/topics/247?courseId=145
Topic ID: 247

## Prerequisites

- [De Morgan's Laws for Logic](./230-de-morgan-s-laws-for-logic.md)
- [Conditional Statements](./250-conditional-statements.md)
- [The Absorption Laws](./2823-the-absorption-laws.md)

## Lesson

### Introduction

The conditional statement $A \Rightarrow B$ is logically equivalent to the disjunction $\lnot A \lor B{:}$

$$


A \Rightarrow B \equiv \lnot A \lor B


$$

We can verify this by the following truth table:

In other words, any conditional statement of the form

$\qquad$ *if antecedent, then consequent*

can be expressed equivalently as

$\qquad$ *not antecedent, or consequent.*

For example, consider the following conditional statement:

$\qquad$ *If you do not take your watch, then you will be late for the meeting.*

Let's rewrite this statement using its logically equivalent form.

First, we denote the antecedent $A$ and consequent $B$ as follows:

- $A{:}$ You do not take your watch.

- $B{:}$ You will be late for the meeting.

Then, our initial statement can be written as $A \Rightarrow B,$ which is logically equivalent to

$$


\neg A \lor B.


$$

The negation of $A$ is:

- $\neg A{:}$ You take your watch.

Therefore, the given statement is logically equivalent to the following:

$\qquad$ *You take your watch, or you will be late for the meeting.*

We can write this using more everyday language as follows:

$\qquad$ *Take your watch, or you will be late for the meeting.*

Another way to write this is to append the word "either" to the beginning of the sentence, like so:

$\qquad$ *Either you take your watch, or you will be late for the meeting.*

Using the word "either" helps clarify that the sentence structure presents two alternatives and is particularly useful when employing the disjunctive form $(\lnot A\lor B)$ in conversational or formal English. So, the phrase effectively conveys that one of the two stated conditions will hold true.

### Example: Expressing Conditional Statements as Disjunctions

#### Question

Which statement is logically equivalent to the following conditional statement?

$\qquad$ If you take an umbrella, then you will stay dry.

#### Explanation

Let's denote by $A$ and $B$ the following statements:

- $A{:}$ You take an umbrella.

- $B{:}$ You will stay dry.

Then, our initial statement can be written as $A \Rightarrow B,$ which is logically equivalent to

$$


\neg A \lor B.


$$

The negation of $A$ can be written as

- $\neg A{:}$ You do not take an umbrella.

Therefore, the given statement is logically equivalent to the following:

$\qquad$ You do not take an umbrella, or you will stay dry.

We can write this in more everyday language as follows:

$\qquad$ Either you do not take an umbrella, or you will stay dry.

### Example: Expressing Disjunctive Statements as Conditionals

#### Question

Which conditional statement is logically equivalent to the disjunctive statement below?

$\qquad$ Use sunscreen, or you will get sunburn.

#### Explanation

Let's denote by $A$ and $B$ the following statements:

- $A{:}$ Use sunscreen.

- $B{:}$ You will get sunburn.

Then, our initial statement can be written as $A \lor B,$ which is logically equivalent to

$$


\neg A \Rightarrow B.


$$

The negation of $A$ can be written as

- $\neg A{:}$ You don't use sunscreen.

Therefore, the given statement is logically equivalent to the following:

$\qquad$ If you don't use sunscreen, then you will get sunburn.

### Example: Rewriting Symbolic Conditional Statements

#### Question

Which of the following statements are true?

1. $X \Rightarrow \neg Y \equiv \neg (X \land Y)$

2. $\neg \left(X \Rightarrow \neg Y\right)\equiv \neg X \land Y$

3. $\neg \left(X \Rightarrow \neg Y\right)\equiv X \land Y$

#### Explanation

Let's examine each of our statements:

- Statement I is true. Indeed, $X \Rightarrow \neg Y$ is logically equivalent to the disjunction $\neg X \lor \neg Y,$ which by De Morgan's law is equivalent to $\neg (X\land Y).$

- Statement III is true, while statement II is false. From part I, we have the following equivalence: By negating this statement, we get Canceling out double negation, we reach So, $\neg \left(X \Rightarrow \neg Y\right)$ is equivalent to $X \land Y.$

Therefore, the correct answer is "I and III only."

### Example: Rewriting Conditional Statement Using the Associative, Commutative, and Absorption Laws

#### Question

Simplify the statement $\neg (A \Rightarrow \neg B) \lor A.$

#### Explanation

First, note that the conditional statement $A \Rightarrow \neg B$ is logically equivalent to the disjunction $\lnot A \lor \neg B.$ So, we have

$$


\neg (A \Rightarrow \neg B) \lor A \equiv \neg (\neg A \lor \neg B) \lor A.


$$

Now, we can distribute the negation over the disjunction using De Morgan's law:

$$


\neg (\neg A \lor \neg B) \lor A \equiv ( \neg (\neg A) \land \neg (\neg B) ) \lor A


$$

Canceling out double negations, we reach

$$


( \neg (\neg A) \land \neg (\neg B) ) \lor A \equiv (A \land B) \lor A.


$$

Finally, by the absorption law, we have

$$


(A \land B) \lor A \equiv A.


$$

So the given statement is equivalent to $A.$
