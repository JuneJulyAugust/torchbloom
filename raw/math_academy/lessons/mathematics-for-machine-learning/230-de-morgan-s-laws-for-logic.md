# De Morgan's Laws for Logic

Source: https://www.mathacademy.com/topics/230?courseId=145
Topic ID: 230

## Prerequisites

- [Logical Equivalence](./2821-logical-equivalence.md)

## Lesson

### Introduction

**De Morgan's laws** for logic tell us how to distribute a negation over a conjunction or disjunction.

- De Morgan's law for conjunctions states that

- De Morgan's law for disjunctions states that

Intuitively, you can think that the negation "flips" the conjunction into a disjunction, and vice versa.

To prove that these laws hold, we can construct truth tables:

- The following truth table shows that $\neg (A \land B) \equiv \neg A \lor \neg B{:}$

- The following truth table shows that $\neg (A \lor B) \equiv \neg A \land \neg B{:}$

### Example: Negating a Sentence Containing a Conjunction

#### Question

What is the negation of the following compound statement?

$\qquad$ $6$ is composite and $5\!\not{|} \, 3.$

#### Explanation

De Morgan's law posits that the negation of a conjunction of two statements is equivalent to the disjunction of the negated individual statements. It can be stated symbolically as follows.

$$


\neg ( A \land B) = \neg A \lor \neg B


$$

So, the negation of our statement is

$$


\begin{aligned}¬(6 is composite and 5\,⧸|\,3) & ≡¬((6 is composite)∧(5\,⧸|\,3)) \\ & ≡¬(6 is composite)∨¬(5\,⧸|\,3) \\ & ≡(6 is not composite)∨(5\,|\,3) \\ & ≡6 is not composite or 5\,|\,3.\end{aligned}


$$

### Example: Negating a Sentence Containing a Disjunction

#### Question

What is the negation of the following compound statement?

$\qquad$ $3$ is not prime or $\pi$ is not rational.

#### Explanation

De Morgan's law for disjunctions states that the negation of a disjunction of two statements is equivalent to the conjunction of the negations of the individual statements. It can be stated symbolically as follows:

$$


\neg ( A \lor B) = \neg A \land \neg B.


$$

So, the negation of our statement is

$$


\begin{aligned}¬(3 is not prime or 𝜋 is not rational) & ≡¬((3 is not prime)∨(𝜋 is not rational)) \\ & ≡¬(3 is not prime)∧¬(𝜋 is not rational) \\ & ≡(3 is prime)∧(𝜋 is rational) \\ & ≡3 is prime and 𝜋 is rational.\end{aligned}


$$

### Example: Simplifying a Statement Using De Morgan's Laws

#### Question

Simplify the statement $\neg ((P \lor \neg Q) \land (Q \lor \neg P))$ using De Morgan's laws.

#### Explanation

De Morgan's laws state that

$$


\begin{aligned}¬(𝑃∧𝑄)≡¬𝑃∨¬𝑄, \\ ¬(𝑃∨𝑄)≡¬𝑃∧¬𝑄.\end{aligned}


$$

So, we can simplify the given statement as follows:

$$


\begin{aligned}¬((𝑃∨¬𝑄)∧(𝑄∨¬𝑃)) & ≡¬(𝑃∨¬𝑄)∨¬(𝑄∨¬𝑃) \\ & ≡(¬𝑃∧¬(¬𝑄))∨(¬𝑄∧¬(¬𝑃)) \\ & ≡(¬𝑃∧𝑄)∨(¬𝑄∧𝑃)\end{aligned}


$$
