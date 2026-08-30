# The Absorption Laws

Source: https://www.mathacademy.com/topics/2823?courseId=76
Topic ID: 2823

## Prerequisites

- [Logical Associative and Commutative Laws](./2830-logical-associative-and-commutative-laws.md)

## Lesson

### Introduction

There are two laws, called the **absorption laws**, that can be used to drastically simplify some logical expressions.

- The law that conjunction absorbs disjunction is stated as

- Likewise, the law that disjunction absorbs conjunction is stated as

Sometimes, the laws are stated more concisely as

$$


A \land (A \lor B) \equiv A \lor (A \land B) \equiv A.


$$

To prove that these laws hold, we can construct truth tables:

### Example: Simplifying an Expression Using the Law that Conjunction Absorbs Disjunction

#### Question

Which of the following are logically equivalent to $X?$

1. $X \land (Y \lor X)$

2. $(X \lor Y) \land Y$

3. $(X \lor Y) \land X$

#### Explanation

The law that conjunction absorbs disjunction is stated as

$$


X \land (X \lor Y) \equiv X.


$$

With that in mind, let's inspect each of the given statements.

- Statement I is logically equivalent to $X.$ We have

- Statement II is ** logically equivalent to $X.$ We have

- Statement III is logically equivalent to $X.$ We have

Therefore, the correct answer is "I and III only."

### Example: Simplifying an Expression Using the Law that Disjunction Absorbs Conjunction

#### Question

Which of the following are logically equivalent to $C?$

1. $(C \land B) \lor C$

2. $B \lor (B \land C)$

3. $C \lor (C \lor B)$

#### Explanation

The law that disjunction absorbs conjunction is stated as

$$


C \lor (C \land B) \equiv C.


$$

With that in mind, let's inspect each of the given statements.

- Statement I is logically equivalent to $C.$ We have

- Statement II is ** logically equivalent to $C.$ We have

- Statement III is ** logically equivalent to $C.$ This statement cannot be simplified using the absorption laws.

Therefore, the correct answer is "I only."
