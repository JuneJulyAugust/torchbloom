# Proving De Morgan's Laws for Sets

Source: https://www.mathacademy.com/topics/4427?courseId=76
Topic ID: 4427

## Prerequisites

- [De Morgan's Laws for Sets](./2788-de-morgan-s-laws-for-sets.md)
- [Proving Elementary Properties of Set Operations](./2806-proving-elementary-properties-of-set-operations.md)

## Lesson

### Introduction

Suppose that $A$ and $B$ are sets, and $U$ is a universal set.

De Morgan's law for intersections states that the complement of the intersection of $A$ and $B$ is the union of their complements. Symbolically, we can express this as follows:

$$


\overline{A \cap B} = \overline{A} \cup \overline{B}


$$

We can get an intuitive understanding of De Morgan's law for intersections using the diagram shown below.

![Instructional graphic](../../lesson-assets/methods-of-proof/topic-4427/f7271351a864d369.png)

The shaded region corresponds to $\overline{A} \cup \overline{B},$ and the non-shaded region corresponds to $A \cap B.$ It's clear from the diagram that by taking the complement of the non-shaded region, we get the shaded region.

Although this diagram helps to build intuition, it does not constitute a formal mathematical proof. We usually resort to one of the following methods to formally prove De Morgan's laws.

1. Using truth tables.

2. Using the property that for sets $X$ and $Y,$ we have $X = Y$ if and only if $X$ and $Y$ are subsets of each other. In this case, we'd need to prove the following:

3. Establishing a chain of equivalent statements shows that membership of the first set is equivalent to membership of the second set. In this case, we'd need to show that for all $x\in U,$ we have

We'll focus on the second and third methods in this topic.

Before we discuss our first proof, it may be no surprise that De Morgan's law for *conjunctions* is very useful in these proofs. Recall that if $P$ and $Q$ are statements, then De Morgan's law for conjunctions states:

$$


\lnot (P\land Q) \equiv \lnot P \lor \lnot Q


$$

De Morgan's law for intersections is the set-theoretic equivalent of De Morgan's law for conjunctions, and the latter is often used to prove the former.

### Proving a Subset Relation

Let's prove the following subset relation:

$$


\overline{A} \cup \overline{B}\subseteq \overline{A \cap B}


$$

To do this, we must demonstrate that a fixed but arbitrary element of the first set is also an element of the second set.

So, we start by considering an arbitrary element of $\overline{A} \cup \overline{B}$ and use the definition of the union of sets.

$x \in \overline{A} \cup \overline{B} \quad\Rightarrow\quad (x \in \overline{A}) \lor (x \in \overline{B})$

The idea is to manipulate the statement on the right-hand side so that we can apply De Morgan's law for conjunctions.

$$


\lnot P \lor \lnot Q \equiv \lnot (P\land Q)


$$

Notice that the statements $(x \in \overline{A}) \lor (x \in \overline{B})$ and $\lnot P \lor \lnot Q$ already look quite similar:

So, our next step is to use the definition of the set complement.

$(x \in \overline{A}) \lor (x \in \overline{B}) \quad\Rightarrow\quad (x \notin A) \lor (x \notin B)$

Then, we apply the definition of negation.

$(x \notin A) \lor (x \notin B) \quad\Rightarrow\quad \lnot (x \in A) \lor \lnot (x \in B)$

Then, we use De Morgan's law for conjunctions.

$\lnot (x \in A) \lor \lnot (x \in B) \quad\Rightarrow\quad \lnot \big((x \in A) \land (x \in B) \big)$

The hard part of the proof is done at this point. We just need to rewrite this statement using set-theoretic definitions.

First, we apply the definition of intersection.

$\lnot \big((x \in A) \land (x \in B) \big) \quad\Rightarrow\quad \lnot (x \in A \cap B)$

Then, we use the definition of negation once more.

$\lnot (x \in A \cap B) \quad\Rightarrow\quad x \notin A \cap B$

Finally, we apply the definition of the set complement once more.

$x \notin A \cap B \quad\Rightarrow\quad x \in \overline{A \cap B}$

So, we have shown that $x\in \overline{A} \cup \overline{B}$ implies $x\in \overline{A \cap B}.$ Our proof is complete, and we now state our conclusion.

*So, if $x \in\overline{A} \cup \overline{B},$ then $x \in \overline{A \cap B}.$ By the definition of a subset, this means*

$$


\overline{A} \cup \overline{B} \subseteq \overline{A \cap B}.


$$

We'll now state the full proof:

### Stating the Full Proof

Lemma:

If $A$ and $B$ are sets, then $\overline{A} \cup \overline{B}\subseteq \overline{A \cap B}.$

Proof:

$$


\begin{aligned}𝑥∈\overset{𝐴}{}∪\overset{𝐵}{}\, & ⇒\,(𝑥∈\overset{𝐴}{})∨(𝑥∈\overset{𝐵}{}) \\ & ⇒\,(𝑥∉𝐴)∨(𝑥∉𝐵) \\ & ⇒\,¬(𝑥∈𝐴)∨¬(𝑥∈𝐵) \\ & ⇒\,¬((𝑥∈𝐴)∧(𝑥∈𝐵)) \\ & ⇒\,¬(𝑥∈𝐴∩𝐵) \\ & ⇒\,𝑥∉𝐴∩𝐵 \\ & ⇒\,𝑥∈\overset{𝐴∩𝐵}{}\end{aligned}


$$

*So, if $x \in\overline{A} \cup \overline{B},$ then $x \in \overline{A \cap B}.$ By the definition of a subset, this means*

$$


\overline{A} \cup \overline{B} \subseteq \overline{A \cap B}.


$$

It's worth taking the time to go through this proof line by line and check that you understand it. If you're unclear why a particular line is true, refer to the previous section for an explanation. It's highly recommended that you reproduce this proof for yourself.

The second inclusion is proved in a similar way, so let's see that next. You will note that De Morgan's law for conjunctions is needed once more.

### Example: De Morgan's Law for Intersections

#### Question

Consider the following statement:

Given that $A$ and $B$ are sets, $\overline{A \cap B} = \overline{A} \cup \overline{B}.$

A part of the proof showing that $\overline{A \cap B} \subseteq \overline{A} \cup \overline{B}$ is given below.

$\textrm{L1}{:}\:$ $x \in \overline{A \cap B}$

$\textrm{L2}{:}\:$ $\Rightarrow x \notin A \cap B$

$\textrm{L3}{:}\:$ $\Rightarrow \lnot (x \in A \cap B)$

$\textrm{L4}{:}\:$ $\Rightarrow \lnot ((x \in A) \land (x \in B))$

$\textrm{L5}{:}\:$ $\Rightarrow \lnot (x \in A) \lor \lnot (x \in B)$

$\textrm{L6}{:}\:$ $\Rightarrow (x \notin A) \lor (x \notin B)$

$\textrm{L7}{:}\:$ $\Rightarrow (x \in \overline{A}) \lor (x \in \overline{B})$

$\textrm{L8}{:}\:$ $\Rightarrow x \in \overline{A} \cup \overline{B}$

Complete the blanks in the following reasoning.

- Line $\textrm{L5}$ follows from line $\textrm{L4}$ by $\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_.$

- Line $\textrm{L7}$ follows from line $\textrm{L6}$ by the definition of $\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_.$

- Line $\textrm{L8}$ follows from line $\textrm{L7}$ by the definition of $\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_.$

- To complete the given proof, we must also show that if $x \in$ $\_\_\_\_\_\_\_\_,$ then $x\in\, \_\_\_\_\_\_\_\_.$

#### Explanation

Let's examine each statement in turn. Assume $X$ and $Y$ are sets, and $P$ and $Q$ are statements.

- First, we consider lines $\textrm{L4}$ and $\textrm{L5}.$ De Morgan's law for conjunctions states the following: Therefore, line $\textrm{L5}$ follows from line $\textrm{L4}$ by $\boxed{\color{blue}\text{De Morgan's law}}$ $\boxed{\color{blue}\text{for conjunctions}}.$

- Next, we consider lines $\textrm{L6}$ and $\textrm{L7}.$ According to the definition of the set complement, we have the following equivalence: Therefore, line $\textrm{L7}$ follows from line $\textrm{L6}$ by $\boxed{\color{blue}\text{the definition of}}$ $\boxed{\color{blue}\text{the set complement}}.$

- Then, we consider lines $\textrm{L7}$ and $\textrm{L8}.$ According to the definition of the union of sets, we have the following equivalence: Therefore, line $\textrm{L8}$ follows from line $\textrm{L7}$ by the definition of $\boxed{\color{blue}\text{the union of sets}}.$

- Finally, to prove that two sets are equal, we must show that a fixed but arbitrary element of one set is an element of another, and vice versa. Therefore, to complete the given proof, we must also demonstrate that if $x \in \boxed{\color{blue}\overline{A} \cup \overline{B}}$ then $x \in \boxed{\color{blue}\overline{A \cap B}}.$

### Proving De Morgan's Law for Unions

Suppose that $A$ and $B$ are sets, and $U$ is a universal set.

De Morgan's law for unions states that the complement of the union of $A$ and $B$ is the intersection of their complements. Symbolically, we can express this as follows:

$$


\overline{A \cup B} = \overline{A} \cap \overline{B}


$$

We can get an intuitive understanding of De Morgan's law for unions using the diagram shown below.

![Instructional graphic](../../lesson-assets/methods-of-proof/topic-4427/93152609e1c4b085.png)

The shaded region corresponds to $\overline{A} \cap \overline{B},$ and the non-shaded region corresponds to $A \cup B.$ It's clear from the diagram that by taking the complement of the non-shaded region, we get the shaded region.

We can prove De Morgan's law for unions using similar techniques to proving De Morgan's law for intersections. The difference is that we'll now need to use De Morgan's law for disjunctions.

Suppose $P$ and $Q$ are statements. Then, De Morgan's law for disjunctions states the following:

$$


\lnot (P\lor Q) \equiv \lnot P \land \lnot Q


$$

Let's see an example.

### Example: De Morgan's Law for Unions

#### Question

Consider the following statement:

Given that $A$ and $B$ are sets, $\overline{A \cup B} = \overline{A} \cap \overline{B}.$

A part of the proof showing that $\overline{A \cup B} \subseteq \overline{A} \cap \overline{B}$ is given below.

$\textrm{L1}{:}\:$ $x \in \overline{A \cup B}$

$\textrm{L2}{:}\:$ $\Rightarrow x \notin A \cup B$

$\textrm{L3}{:}\:$ $\Rightarrow \lnot (x \in A \cup B)$

$\textrm{L4}{:}\:$ $\Rightarrow \lnot ((x \in A) \lor (x \in B))$

$\textrm{L5}{:}\:$ $\Rightarrow (\lnot (x \in A))\land (\lnot (x \in B))$

$\textrm{L6}{:}\:$ $\Rightarrow (x \notin A) \land (x \notin B)$

$\textrm{L7}{:}\:$ $\Rightarrow (x \in \overline{A}) \land (x \in \overline{B})$

$\textrm{L8}{:}\:$ $\Rightarrow x \in \overline{A} \cap \overline{B}$

Complete the blanks in the following reasoning.

- Line $\textrm{L3}$ follows from line $\textrm{L2}$ by the definition of $\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\,$.

- Line $\textrm{L5}$ follows from line $\textrm{L4}$ by applying $\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\,$.

- Line $\textrm{L7}$ follows from line $\textrm{L6}$ by the definition of $\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\,$.

#### Explanation

Let's examine each statement in turn. Assume $X$ and $Y$ are sets, and $P$ and $Q$ are statements.

- First, we consider lines $\textrm{L2}$ and $\textrm{L3}.$ According to the definition of negation, we have the following equivalence: Therefore, line $\textrm{L3}$ follows from line $\textrm{L2}$ by the definition of $\boxed{\color{blue}\text{negation}}.$

- Next, we consider lines $\textrm{L4}$ and $\textrm{L5}.$ According to De Morgan's law for disjunctions, we have the following equivalence: Therefore, $\textrm{L5}$ follows from $\textrm{L4}$ by applying $\boxed{\color{blue}\textrm{De Morgan's law for disjunctions}}.$

- Finally, we consider lines $\textrm{L6}$ and $\textrm{L7}.$ According to the definition of the set complement, we have the following equivalence: Therefore, line $\textrm{L7}$ follows from line $\textrm{L6}$ by the definition of $\boxed{\color{blue}\text{the set complement}}.$

### Using Biconditionals

We can also prove De Morgan's laws for sets by forming a chain of equivalent statements.

Suppose $P, Q,$ and $R$ are statements. Then, the statement

$$


P\quad\Leftrightarrow \quad Q \quad\Leftrightarrow \quad R


$$

is true if $P,Q,$ and $R$ are either all true, or all false.

Proving a result by forming a chain of equivalent statements is sometimes difficult. However, it works well when proving De Morgan's laws. Moreover, proofs using equivalent statements are significantly shorter than proofs using two subset relations, and the logic is similar (though not identical).

Let's see an example.

### Example: Proving De Morgan's Law Using Biconditionals

#### Question

Consider the following statement:

Given that $A$ and $B$ are sets, $\overline{A \cap B} = \overline{A} \cup \overline{B}.$

A proof of this statement is given below.

$\textrm{L1}{:}\:$ $x \in \overline{A \cap B}$

$\textrm{L2}{:}\:$ $\Leftrightarrow x \notin A \cap B$

$\textrm{L3}{:}\:$ $\Leftrightarrow \lnot (x \in A \cap B)$

$\textrm{L4}{:}\:$ $\Leftrightarrow \lnot ((x \in A) \land (x \in B))$

$\textrm{L5}{:}\:$ $\Leftrightarrow (\lnot (x \in A)) \lor (\lnot (x \in B))$

$\textrm{L6}{:}\:$ $\Leftrightarrow (x \notin A) \lor (x \notin B)$

$\textrm{L7}{:}\:$ $\Leftrightarrow (x \in \overline{A}) \lor (x \in \overline{B})$

$\textrm{L8}{:}\:$ $\Leftrightarrow x \in \overline{A} \cup \overline{B}$

Complete the blanks in the following reasoning.

- Line $\textrm{L2}$ follows from line $\textrm{L1}$ by the definition of $\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_.$

- Line $\textrm{L5}$ follows from line $\textrm{L4}$ by $\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_.$

- Line $\textrm{L8}$ follows from line $\textrm{L7}$ by the definition of $\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_.$

#### Explanation

Let's examine each statement in turn. Assume $X$ and $Y$ are sets.

- First, we consider lines $\textrm{L1}$ and $\textrm{L2}.$ We have the following equivalence: Therefore, line $\textrm{L2}$ follows from line $\textrm{L1}$ by the definition of $\boxed{\color{blue}\text{the set complement}}.$

- Next, we consider lines $\textrm{L4}$ and $\textrm{L5}.$ De Morgan's law for conjunctions states the following: Therefore, line $\textrm{L5}$ follows from line $\textrm{L4}$ by $\boxed{\color{blue}\text{De Morgan's law for conjunctions}}.$

- Finally, we consider lines $\textrm{L7}$ and $\textrm{L8}.$ We have the following equivalence: Therefore, line $\textrm{L8}$ follows from line $\textrm{L7}$ by the definition of $\boxed{\color{blue}\text{the union of sets}}.$
