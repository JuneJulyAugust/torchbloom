# The Distributive Laws

Source: https://www.mathacademy.com/topics/2822?courseId=145
Topic ID: 2822

## Prerequisites

- [Logical Equivalence](./2821-logical-equivalence.md)

## Lesson

### Introduction

Just like we can distribute multiplication over addition, we can also distribute conjunctions over disjunctions (and vice versa).

- We can distribute a conjunction over a disjunction, as follows:

- Likewise, we can distribute a disjunction over a conjunction, as follows:

The rules above are called the **distributive laws** for propositional logic. To prove that these laws hold, we can construct truth tables.

- The following truth table shows that $A \land (B \lor C) \equiv (A \land B) \lor (A \land C){:}$

- The following truth table shows that $A \lor (B \land C) \equiv (A \lor B) \land (A \lor C){:}$

### Example: Expanding a Statement by Distributing a Conjunction

#### Question

Expand the statement $P \land (Q \lor R)$ by distributing the conjunction.

#### Explanation

We distribute the conjunction over the disjunction, as follows:

$$


P \land (Q \lor R) \equiv (P \land Q) \lor (P \land R)


$$

### Example: Expanding a Statement by Distributing a Disjunction

#### Question

Expand the statement $(C \land B) \lor A$ by distributing the disjunction.

#### Explanation

We distribute the disjunction over the conjunction, as follows:

$$


(C \land B) \lor A \equiv (C \lor A) \land (B \lor A)


$$

### Example: Simplifying a Statement Using the Distributive Property for Conjunctions

#### Question

Simplify the statement $(A \land C) \lor (A \land B)$ using the distributive property for conjunctions.

#### Explanation

We can factor out the conjunction with $A,$ as follows:

$$


(A \land C) \lor (A \land B) \equiv A \land (C \lor B)


$$

### Example: Simplifying a Statement Using the Distributive Property for Disjunctions

#### Question

Simplify the statement $(P \lor Q) \land (P \lor R)$ using the distributive property for disjunctions.

#### Explanation

We can factor out the disjunction with $P,$ as follows:

$$


(P \lor Q) \land (P \lor R) \equiv P \lor (Q \land R)


$$
