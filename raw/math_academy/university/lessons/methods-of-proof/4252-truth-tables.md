# Truth Tables

Source: https://www.mathacademy.com/topics/4252?courseId=76
Topic ID: 4252

## Prerequisites

- [The "And" and "Or" Connectives](./60-the-and-and-or-connectives.md)

## Lesson

### Introduction

Recall that the statement "$A$ and $B$", represented symbolically as $A \land B,$ is true if $A$ is true *and* $B$ is true. Otherwise, it is false.

We can represent all possible permutations of the truth values of $A$ and $B$ and the subsequent truth values of $A\land B$ using a **truth table**:

Each row of the truth table contains an input for $A,$ an input for $B,$ and the corresponding output for $A \land B.$

- The first row says that if $A$ is true and $B$ is true, then $A \land B$ is true.

- The second row says that if $A$ is true and $B$ is false, then $A \land B$ is false.

- The third row says that if $A$ is false and $B$ is true, then $A \land B$ is false.

- The fourth row says that if $A$ is false and $B$ is false, then $A \land B$ is false.

### The Truth Table of the "Or" Operator

The statement "$A$ or $B$," represented symbolically as $A \lor B,$ is true if $A$ is true, or $B$ is true, or both $A$ and $B$ are true. Otherwise, it is false.

The corresponding truth table is shown below:

As we'll see, truth tables provide a convenient way to determine the truth values of complex logical statements. They can also be used to prove some mathematical theorems!

### Example: Completing a Truth Table

#### Question

What are the missing entries in the following truth table?

#### Explanation

The statement $A \land B$ is true if both $A$ and $B$ are true.

The complete truth table is shown below:

### Truth Tables of Compound Statements

Consider the following statement:

$$


A \land (B\lor A)


$$

We can use a truth table to calculate the truth values of this statement given all possible permutations of the truth values of $A$ and $B.$

First, we complete a truth table for the part in parentheses, $B \lor A.$ The statement $B \lor A$ is true if either $A$ is true, $B$ is true, or both $A$ and $B$ are true.

Next, we add a new column for $A \land (B\lor A).$

To fill in the rows, we consider the truth values of $A$ and $(B\lor A)$ and use this to determine the truth value of $A \land (B\lor A)$ in each case.

- Consider the first row. Since $A$ is true and $(B\lor A)$ is true, their conjunction $A \land (B\lor A)$ is *true*:

- Next, consider the second row. Since $A$ is true and $(B\lor A)$ is true, their conjunction $A \land (B\lor A)$ is *true*:

- Now, consider the third row. Since $A$ is false and $(B\lor A)$ is true, their conjunction $A \land (B\lor A)$ is *false*:

- Finally, consider the fourth row. Since $A$ is false and $(B\lor A)$ is false, their conjunction $A \land (B\lor A)$ is *false*:

The completed truth table is shown below:

### Example: Completing a Truth Table for a Compound Statement

#### Question

Construct the truth table of the statement $(A \land B) \lor (A \lor B).$

#### Explanation

First, we complete a truth table for the first part in parentheses, $A \land B.$ The statement $A \land B$ is true if both $A$ and $B$ are true.

Next, we append the truth table for the second part in parentheses, $A \lor B.$ The statement $A \lor B$ is true if either $A$ is true, $B$ is true, or both $A$ and $B$ are true.

Finally, we look at the columns labeled $(A \land B)$ and $(A \lor B)$ to complete the column $(A \land B) \lor (A \lor B).$ The statement $(A \land B) \lor (A \lor B)$ is true if either $(A \land B)$ is true, $(A \lor B)$ is true, or both $(A \land B)$ and $(A \lor B)$ are true.

The completed truth table is shown below:

### The Idempotent Laws

Two statements are **logically equivalent** if they have identical truth tables.

A trivial logical equivalence is that every statement is logically equivalent to itself. We write this as follows:

$$


P \equiv P


$$

To prove this, we can use a truth table.

Since $P$ and $P$ have identical truth values, they're logically equivalent.

Another trivial equivalence is that the conjunction of a statement with itself is equivalent to the original statement.

$$


P \land P \equiv P


$$

For example, the compound statement "$x=3$ and $x=3$" is logically equivalent to "$x=3$", which matches our intuition.

Again, we can prove the general result using a truth table.

The statements $P$ and $P\land P$ are logically equivalent since they have identical truth values.

We also have the following logical equivalence for the disjunction of $P$ with itself.

$$


P \lor P \equiv P


$$

We can justify this result using a truth table.

The statements $P$ and $P\lor P$ are logically equivalent since they have identical truth values.

Collectively, the results

$$


P\land P \equiv P ,\qquad P\lor P \equiv P


$$

are known as the **idempotent laws.**

### Example: Simplifying a Compound Statement

#### Question

Simplify the statement $P \land (Q \lor Q).$

#### Explanation

The expression $Q \lor Q$ simplifies to just $Q.$

So, the given statement can be simplified to

$$


P \land Q.


$$
