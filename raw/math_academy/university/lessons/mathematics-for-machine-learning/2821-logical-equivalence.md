# Logical Equivalence

Source: https://www.mathacademy.com/topics/2821?courseId=145
Topic ID: 2821

## Prerequisites

- [The "Not" Connective](./2790-the-not-connective.md)

## Lesson

### Introduction

Two statements are **logically equivalent** if they have identical truth values in their respective truth tables. In this lesson, we'll use truth tables to show that two complex compound statements are logically equivalent.

If two statements $P$ and $Q$ are logically equivalent, we write

$$


P\equiv Q


$$

where the symbol "$\equiv$" means "is logically equivalent to."

For example, let's use a truth table to prove the following logical equivalence:

$$


(A \land \neg A) \lor B \equiv B


$$

First, we construct truth tables with columns $A$ and $B$ containing all possible combinations of truth values. Then, we create another column for $\neg A,$ which has the opposite truth values to $A.$

Now, we add a column for $A \land \neg A.$ Recall that $A\land \neg A$ is true if $A$ is true and $\neg A$ is true and is false otherwise. In this case, $A\land \neg A$ is always false.

Finally, we complete the table with a column for $(A \land \neg A) \lor B.$ Recall that $(A \land \neg A) \lor B$ is true if $(A \land \neg A)$ is true, or $B$ is true, or both are true.

We see that the truth values of $(A \land \neg A) \lor B$ are the same as the truth values of $B.$ This proves that $(A \land \neg A) \lor B$ is logically equivalent to $B.$

### Example: Completing a Truth Table

#### Question

What are the missing values in the following truth table?

#### Explanation

First, we add a column for $\neg Y{:}$

Then, we add a column for $X \lor \neg Y{:}$

Finally, we add a column for $X \land (X \lor \neg Y){:}$

### Example: Identifying Equivalent Statements Using Partially Completed Truth Tables

#### Question

Find the missing values in the following truth table:

Use your results to determine whether $\neg A \land \neg B$ is logically equivalent to $\neg (A \lor B).$

#### Explanation

First, let's solve for the missing values:

- When $A \equiv \textrm T$ and $B \equiv \textrm F,$ we have

- When $A \equiv \textrm F$ and $B \equiv \textrm T,$ we have

- When $A \equiv \textrm F$ and $B \equiv \textrm F,$ we have

Our completed table is shown below.

To determine whether $\neg A \land \neg B$ is logically equivalent to $\neg (A \lor B),$ we need to check whether their truth tables are equivalent.

Looking at the last two columns, we see that they are the same $(\text{F},\text{F},\text{F},\text{T}).$ Therefore, we conclude that $\neg A \land \neg B$ is logically equivalent to $\neg (A \lor B),$ that is,

$$


\neg A \land \neg B \boxed{\color{blue}\equiv} \neg (A \lor B).


$$

### Example: Identifying Logically Equivalent Statements

#### Question

Which of the following statements are logically equivalent?

1. $B \land \neg A$

2. $\neg (A \lor \neg B)$

3. $\neg (\neg A \lor B)$

#### Explanation

Two statements are logically equivalent if they have the same truth table. So, we construct a truth table for the three given statements:

We see that only the statements $B \land \neg A$ and $\neg (A \lor \neg B)$ have the same truth table, so they are logically equivalent.

Therefore, the correct answer is "I and II only."
