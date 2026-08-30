# Translating Between Logical and Set Operations

Source: https://www.mathacademy.com/topics/251?courseId=76
Topic ID: 251

## Prerequisites

- [The Difference of Sets](./2828-the-difference-of-sets.md)
- [Negating Statements With Nested Quantifiers](./4258-negating-statements-with-nested-quantifiers.md)

## Lesson

### Introduction

It's often necessary to switch between logic and set notation when constructing certain mathematical arguments.

According to the definitions of the union, intersection, difference, and complement of sets, we have the following equivalences:

- If $x\in A\cup B,$ then $x$ is an element of $A$ *or* $x$ is an element of $B.$

- If $x\in A\cap B,$ then $x$ is an element of $A$ *and* $x$ is an element of $B.$

- If $x\in A\setminus B,$ then $x$ is an element of $A$ *and* $x$ is *not* an element of $B.$

- If $x\in \overline{A},$ then $x$ is *not* an element of $A.$ Alternatively, if $U$ is the universal set, we can also express this equivalence as follows:

These equivalences can be summarized in the table below.

### Example: Translating Between Set and Logical Operations

#### Question

Complete the following table.

#### Explanation

Recall the following equivalences:

- If $x\in A\cup B,$ then $x$ is an element of $A$ ** $x$ is an element of $B.$

- If $x\in A\cap B,$ then $x$ is an element of $A$ ** $x$ is an element of $B.$

- If $x\in A\setminus B,$ then $x$ is an element of $A$ ** $x$ is ** an element of $B.$

- If $x\in \overline{A},$ then $x$ is ** an element of $A.$ Alternatively, if $U$ is the universal set, we can also express this equivalence as follows:

Therefore, the completed table looks as follows:

### Example: Translating Between Set and Logical Operations Using De Morgan's Laws

#### Question

If $A$ and $B$ are sets, and $x\in U$ for some universal set $U,$ then find a logical expression that's equivalent to $x\notin B\setminus A.$

#### Explanation

Recall that if $x\in B\setminus A,$ then $x$ is an element of $B$ ** $x$ is ** an element of ${A}.$ We can write this as the following equivalence:

$$


x\in B\setminus A \quad\Leftrightarrow\quad (x\in B) \land (x\notin {A})


$$

However, we're interested in finding a logical expression that's equivalent to $x\notin B\setminus A.$ So, if we negate the above equivalence, we get the following:

$$


\begin{aligned}¬[𝑥∈𝐵∖𝐴] & \,⇔\,¬[(𝑥∈𝐵)∧(𝑥∉𝐴)] \\ 𝑥∉(𝐵∖𝐴) & \,⇔\,¬[(𝑥∈𝐵)∧(𝑥∉𝐴)]\end{aligned}


$$

We can simplify the right-hand side of our equivalence using De Morgan's law for conjunctions:

$$


\begin{aligned}𝑥∉(𝐵∖𝐴) & \,⇔\,¬[(𝑥∈𝐵)∧(𝑥∉𝐴)] \\ & \,⇔\,¬(𝑥∈𝐵)∨¬(𝑥∉𝐴) \\ & \,⇔\,(𝑥∉𝐵)∨(𝑥∈𝐴) \\ & \,⇔\,(𝑥∈\overset{𝐵}{})∨(𝑥∈𝐴) \\ & \,⇔\,(𝑥∈𝑈∖𝐵)∨(𝑥∈𝐴)\end{aligned}


$$

Note that we used the fact that $\overline{B} = U\setminus B.$

Therefore, we conclude that

$$


\begin{aligned}𝑥∉(𝐵∖𝐴) & \,⇔\,(𝑥∈𝑈∖𝐵)∨(𝑥∈𝐴).\end{aligned}


$$

### Example: Translating Between Set and Logical Operations in More Advanced Cases

#### Question

Which of the following statements is logically equivalent to $x \in \overline{A \setminus \overline{B}} \,?$

1. $x \not\in A \land x \in B$

2. $x \not\in A \lor x \not\in B$

3. $x \in A \lor x \in B$

#### Explanation

Recall the following equivalences:

- If $x\in A\cup B,$ then $x$ is an element of $A$ ** $x$ is an element of $B.$

- If $x\in A\cap B,$ then $x$ is an element of $A$ ** $x$ is an element of $B.$

- If $x\in A\setminus B,$ then $x$ is an element of $A$ ** $x$ is ** an element of $B.$

- If $x\in \overline{A},$ then $x$ is ** an element of $A.$ Alternatively, if $U$ is the universal set, we can also express this equivalence as follows:

Now, we express the set operations as logical operations and simplify (if possible):

$$


\begin{aligned}𝑥∈\overset{𝐴∖\overset{𝐵}{}\, & ⇔\,𝑥∉𝐴∖\overset{𝐵}{} \\ \, & ⇔\,¬(𝑥∈𝐴∖\overset{𝐵}{}) \\ \, & ⇔\,¬((𝑥∈𝐴)∧(𝑥∉\overset{𝐵}{})) \\ \, & ⇔\,¬((𝑥∈𝐴)∧(𝑥∈𝐵)) \\ \, & ⇔\,¬(𝑥∈𝐴)∨¬(𝑥∈𝐵) \\ \, & ⇔\,(𝑥∉𝐴)∨(𝑥∉𝐵) \\ \, & ⇔\,𝑥∉𝐴∨𝑥∉𝐵\end{aligned}


$$

Therefore, we conclude that

$$


x \in \overline{A \setminus \overline{B}} \quad \Leftrightarrow \quad x \not\in A \lor x \not\in B.


$$

Thus, the correct answer is option II.

### Subsets

Suppose $A$ and $B$ are sets, and $U$ is a universal set. Recall the following:

- $A\subseteq B$ means that $A$ is a subset of $B.$ This means that every element of $A$ is an element of $B.$

- $A\subset B$ means that $A$ is a proper subset of $B.$ This means that every element of $A$ is an element of $B,$ *and* $A\neq B.$

We can translate these statements into equivalent logical notations as follows:

- By definition, $A\subseteq B$ means for all $x\in U,$ if $x$ is an element of $A,$ then $x$ is an element of $B.$ We can write this as the following equivalence: We can form an alternative equivalence by eliminating the implication as follows:

- By definition, $A\subset B$ means for all $x\in U,$ if $x$ is an element of $A,$ then $x$ is an element of $B,$ and $A\neq B.$ We can write this as the following equivalence: We can form an alternative equivalence by eliminating the implication, similar to the case for $A\subseteq B.$

### Example: Writing Subset Inclusion or Exclusion Using Logic Notation

#### Question

Which of the following statements is logically equivalent to $D \subset E \,?$

1. $\exists x \in U \big(x \in D \Rightarrow x \in E \big) \land \big(D \neq E\big)$

2. $\exists x \in U \big(x \in D \Rightarrow x \in E \big) \lor \big(D \neq E\big)$

3. $\forall x \in U \big(x \in D \Rightarrow x \in E \big) \land \big(D \neq E\big)$

#### Explanation

The notation $D \subset E$ means that $D$ is a proper subset of $E.$ By definition, $D \subset E$ means for all $x \in U,$ if $x$ is an element of $D,$ then $x$ is an element of $E,$ and $D \neq E.$

We can write this as the following equivalence:

$$


D \subset E \quad \Leftrightarrow \quad \forall x \in U \big(x \in D \Rightarrow x \in E \big) \land \big(D \neq E\big)


$$

Therefore, the correct answer is option III.
