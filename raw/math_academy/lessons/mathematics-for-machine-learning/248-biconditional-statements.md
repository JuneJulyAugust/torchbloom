# Biconditional Statements

Source: https://www.mathacademy.com/topics/248?courseId=145
Topic ID: 248

## Prerequisites

- [Logical Equivalence with Conditional Statements](./247-logical-equivalence-with-conditional-statements.md)

## Lesson

### Introduction

Of particular importance in mathematical proofs are so-called **biconditional statements.** These are statements of the form

$$


(P\Rightarrow Q) \land (Q\Rightarrow P).


$$

In words, a biconditional statement states that *"$P$ implies $Q,$ **** $Q$ implies $P.$"*

Let's construct a truth table for this biconditional statement.

Biconditional statements are so important that we give them a special symbol.

$$


P\Leftrightarrow Q


$$

So, we now have the following logical equivalence:

$$


P \Leftrightarrow Q \equiv (P \Rightarrow Q) \land (Q \Rightarrow P)


$$

The truth table for $P\Leftrightarrow Q$ is as follows:

According to the truth table, $P\Leftrightarrow Q$ is true if $P$ and $Q$ have the *same* truth value. Otherwise, it is false. We can express this as another logical equivalence:

$$


P\Leftrightarrow Q \equiv \big(P \land Q\big) \lor \big(\neg P \land \neg Q\big)


$$

There are many ways to say $P\Leftrightarrow Q$ in words. Among the most common are the following:

- *$P$ is equivalent to $Q$*

- *$P$ if and only if $Q$*

- *If $P$ then $Q,$ and if $Q$ then $P$*

- *$P$ implies $Q$, and $Q$ implies $P$*

### Example: Using the Equivalence Truth Table

#### Question

If $A$ is true and $B$ is true, what is the truth value of $A \Leftrightarrow B?$

#### Explanation

According to the definition of the biconditional,

- $A \Leftrightarrow B$ is true if $A\Rightarrow B$ **** $B\Rightarrow A.$ Otherwise, it is false.

- In other words, $A \Leftrightarrow B$ is true if $A$ and $B$ have the same truth values. Otherwise, it is false.

So, when $A = \textrm T$ and $B = \textrm T,$ we have

$$


\begin{aligned}(𝐴⇔𝐵) & =(T⇔T) \\ & =T.\end{aligned}


$$

The complete truth table is shown below:

### Example: Completing a Truth Table for an Equivalence

#### Question

What are the missing entries in the following truth table?

#### Explanation

According to the definition of the biconditional,

- $A \Leftrightarrow B$ is true if $A\Rightarrow B$ **** $B\Rightarrow A.$ Otherwise, it is false.

- In other words, $A \Leftrightarrow B$ is true if $A$ and $B$ have the same truth values. Otherwise, it is false.

First, we add columns for $\neg P$ and $\neg P \land Q{:}$

Finally, we add a column for $(\neg P \land Q) \Leftrightarrow Q.$

### Example: Writing Biconditionals as Conditionals

#### Question

Express the following statement as a conjunction of implications.

$$


\neg P \Leftrightarrow Q


$$

#### Explanation

According to the definition of the biconditional,

- $A \Leftrightarrow B$ is true if $A\Rightarrow B$ **** $B\Rightarrow A.$ Otherwise, it is false.

- In other words, $A \Leftrightarrow B$ is true if $A$ and $B$ have the same truth values. Otherwise, it is false.

Therefore, in this case, we have

$$


\neg P \Leftrightarrow Q \equiv (\neg P \Rightarrow Q) \land (Q \Rightarrow \neg P).


$$

### Example: Simplifying Expressions Involving Equivalences

#### Question

Which of the following statements are equivalent to $\lnot (\neg Y \Leftrightarrow Z)?$

1. $Y \Rightarrow \lnot Z$

2. $(Y \lor Z) \Rightarrow (Y \land Z)$

3. $(Y \land Z) \land (Y \land \lnot Z)$

#### Explanation

First, we use the definition of the biconditional statement to write the equivalence as a conjunction of implications:

$$


\lnot (\lnot Y \Leftrightarrow Z) \equiv \lnot \big[(\lnot Y \Rightarrow Z) \land (Z \Rightarrow \lnot Y)\big]


$$

Now, we represent all the implications using disjunctions and negations:

$$


\lnot \big[(\lnot Y \Rightarrow Z) \land (Z \Rightarrow \lnot Y)\big] \equiv \lnot \big[(\lnot \lnot Y \lor Z) \land (\lnot Z \lor \lnot Y)\big]


$$

Next, we simplify the double negations:

$$


\lnot \big[(\lnot \lnot Y \lor Z) \land (\lnot Z \lor \lnot Y)\big] \equiv \lnot \big[(Y \lor Z) \land (\lnot Z \lor \lnot Y)\big]


$$

Now, we use De Morgan's laws:

$$


\begin{aligned}¬[(𝑌∨𝑍)∧(¬𝑍∨¬𝑌)] & ≡¬(𝑌∨𝑍)∨¬(¬𝑍∨¬𝑌) \\ & ≡¬(𝑌∨𝑍)∨¬¬(𝑍∧𝑌)\end{aligned}


$$

Finally, we again simplify the double negations and write down symbols in alphabetic order inside the parentheses using commutative laws:

$$


\begin{aligned}¬(𝑌∨𝑍)∨¬¬(𝑍∧𝑌) & ≡¬(𝑌∨𝑍)∨(𝑍∧𝑌) \\ & ≡¬(𝑌∨𝑍)∨(𝑌∧𝑍) \\ & ≡(𝑌∨𝑍)⇒(𝑌∧𝑍)\end{aligned}


$$

Therefore, the correct answer is only II.
