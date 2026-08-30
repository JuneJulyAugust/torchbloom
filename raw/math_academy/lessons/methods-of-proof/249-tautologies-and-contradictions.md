# Tautologies and Contradictions

Source: https://www.mathacademy.com/topics/249?courseId=76
Topic ID: 249

## Prerequisites

- [Logical Equivalence with Conditional Statements](./247-logical-equivalence-with-conditional-statements.md)

## Lesson

### Introduction

An expression is a **tautology** if it is always true, regardless of the truth values of inputs.

For example, let's consider the expression $A \lor \neg A,$ and fill out the corresponding truth table:

According to the table, $A \lor \neg A$ is always true. Therefore, it is a tautology.

Tautologies are represented by the symbol $\textbf t,$ so we write

$$


A \lor \neg A = \textbf t.


$$

### Example: Identifying Tautologies

#### Question

Complete the truth table below and use it to determine whether $(A \land B) \Rightarrow (B \Rightarrow A)$ is a tautology.

#### Explanation

An expression is a tautology if it is always true, regardless of the inputs.

By completing the final column in the truth table below, we obtain the following:

According to the table, $(A \land B) \Rightarrow (B \Rightarrow A)$ is always true. Therefore, it is a tautology.

### Contradictions

An expression is a **contradiction** if it is always false, regardless of the truth values of inputs.

For example, let's consider the expression $A \land \neg A,$ and fill out the corresponding truth table:

According to the table, $A \land \neg A$ is always false. Therefore, it is a contradiction.

Contradictions are represented by the symbol $\textbf c,$ so we write

$$


A \land \neg A = \textbf c.


$$

### Example: Identifying Contradictions

#### Question

Complete the truth table below and use it to determine whether $P \land (P \Rightarrow \neg Q)$ is a contradiction.

#### Explanation

An expression is a contradiction if it is always false, regardless of the inputs.

By completing the final column in the truth table below, we obtain the following:

According to the table, $P \land (P \Rightarrow \neg Q)$ isn't always false. Therefore, it isn't a contradiction.

### Properties of Tautologies and Contradictions

Tautologies have the following properties:

- The disjunction of an expression and a tautology gives a tautology:

- The conjunction of an expression and a tautology gives the initial expression:

Contradictions have the following properties:

- The disjunction of an expression and a contradiction gives the initial expression:

- The conjunction of an expression and a contradiction gives a contradiction:

To prove these properties, we need to fill out the corresponding truth tables. For example, the truth table for the first property is shown below.

Finally, note the following:

$$


\begin{aligned}𝐭∨𝐭=𝐭\, & & 𝐭∧𝐭 & =𝐭 \\ 𝐭∨𝐜=𝐭\, & & 𝐭∧𝐜 & =𝐜 \\ 𝐜∨𝐭=𝐭\, & & 𝐜∧𝐭 & =𝐜 \\ 𝐜∨𝐜=𝐜\, & & 𝐜∧𝐜 & =𝐜\end{aligned}


$$

Again, all of these properties can be proved using truth tables.

### Example: Applying Properties of Tautologies and Contradictions

#### Question

If $P$ is a statement, $\textbf t$ is a tautology, and $\textbf c$ is a contradiction, complete the following table of logical equivalences.

#### Explanation

Recall the following properties of tautologies and contradictions:

$$


\begin{aligned}𝐴∨𝐭=𝐭\, & & 𝐴∧𝐭 & =𝐴 \\ 𝐴∨𝐜=𝐴\, & & 𝐴∧𝐜 & =𝐜 \\ 𝐭∨𝐭=𝐭\, & & 𝐭∧𝐭 & =𝐭 \\ 𝐭∨𝐜=𝐭\, & & 𝐭∧𝐜 & =𝐜 \\ 𝐜∨𝐭=𝐭\, & & 𝐜∧𝐭 & =𝐜 \\ 𝐜∨𝐜=𝐜\, & & 𝐜∧𝐜 & =𝐜\end{aligned}


$$

The completed table is shown below.

### Example: Simplifying Expressions Involving Tautologies and Contradictions

#### Question

Simplify the expression $(A \land \neg B)\Rightarrow \neg B.$

#### Explanation

Let's simplify the expression using the properties of logical operation

- First, we use that $X \Rightarrow Y \equiv \neg X \lor Y {:}$

- Next, we use a De Morgan's law:

- Then, we simplify the double negation:

- Next, we use the associative law:

- Then, we use the fact that the disjunction of an expression and its negation is a tautology:

- Finally, we use the fact that the disjunction of an expression and a tautology gives a tautology:

Therefore, we conclude that

$$


(A \land \neg B) \Rightarrow \neg B \equiv \textrm{t}


$$
