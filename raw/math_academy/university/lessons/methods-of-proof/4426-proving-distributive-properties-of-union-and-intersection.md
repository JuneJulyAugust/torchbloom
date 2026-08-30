# Proving Distributive Properties of Union and Intersection

Source: https://www.mathacademy.com/topics/4426?courseId=76
Topic ID: 4426

## Prerequisites

- [Proving Elementary Properties of Set Operations](./2806-proving-elementary-properties-of-set-operations.md)
- [Distributive Properties of Set Operations](./4430-distributive-properties-of-set-operations.md)

## Lesson

### Introduction

In this lesson, we will learn how to prove the distributive properties of union and intersection using various techniques.

First, recall that intersections distribute over unions according to the following distributive law:

$$


A\cap (B \cup C) = (A \cap B) \cup (A \cap C)


$$

Similarly, unions distribute over intersections according to the following distributive law:

$$


A\cup (B \cap C) = (A \cup B) \cap (A \cup C)


$$

Note that these distributive properties are analogous to the distributive laws in propositional logic for statements $P, Q,$ and $R.$

$$


\begin{aligned}𝑃∧(𝑄∨𝑅) & =(𝑃∧𝑄)∨(𝑃∧𝑅) \\ 𝑃∨(𝑄∧𝑅) & =(𝑃∨𝑄)∧(𝑃∨𝑅)\end{aligned}


$$

We will often make use of these logical laws when proving the corresponding set identity.

Also, recall that $A=B$ if and only if $A\subseteq B$ and $B\subseteq A.$

These concepts are all that's needed to prove the distributive laws for sets.

### Proof by Translating Between Logic and Set Operations

Suppose we wish to prove that

$$


A\cup (B \cap C) = (A \cup B) \cap (A \cup C).


$$

To prove this law, one strategy we can employ is the following:

- First, we prove that This can be achieved by translating the left-hand side into an equivalent logical statement and applying the distributive laws for logic to show this is equivalent to the right-hand side.

- Then, we use a similar method to prove that

The two proofs, in conjunction, give a valid proof of this distributive law.

Let's see an example of how we might typically prove one of these subset relations.

### Example: Set Inclusions: Translating Between Logical and Set Operations

#### Question

Consider the following statement regarding the sets $A,$ $B,$ and $C.$

$$


(A \cup B) \cap (A \cup C) \subseteq A \cup (B \cap C)


$$

A proof of this statement is given below.

$\text{L1}{:}\:$ $x \in (A \cup B) \cap (A \cup C)$

$\text{L2}{:}\:$ $\Rightarrow(x \in A\cup B)\land (x \in A \cup C)$

$\text{L3}{:}\:$ $\Rightarrow((x \in A)\lor (x\in B))\land ((x \in A) \lor (x \in C))$

$\text{L4}{:}\:$ $\Rightarrow(x \in A) \lor ((x \in B) \land (x \in C))$

$\text{L5}{:}\:$ $\Rightarrow (x \in A) \lor (x \in B\cap C)$

$\text{L6}{:}\:$ $\Rightarrow x \in A \cup (B \cap C)$

What words are missing from the reasoning below?

- Line $\text{L2}$ follows from line $\text{L1}$ by the definition of $\:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_.$

- Line $\text{L4}$ follows from line $\text{L3}$ by the definition of $\:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_.$

- Line $\text{L6}$ follows from line $\text{L5}$ by the definition of $\:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_.$

#### Explanation

Let's examine each statement in turn. Assume that $X$ and $Y$ are sets, and $P, Q,$ and $R$ are statements.

- We first consider lines $\text{L1}$ and $\text{L2}.$ We have the following equivalence: Therefore, $\text{L2}$ follows from $\text{L1}$ by the definition of the $\boxed{\color{blue}\text{the intersection of sets}}.$

- Next, we consider lines $\text{L3}$ and $\text{L4}.$ The distributive law (disjunctions over conjunctions) states: Therefore, $\text{L4}$ follows from $\text{L3}$ by $\boxed{\color{blue}\text{the distributive law}}.$

- Finally, we consider lines $\text{L5}$ and $\text{L6}.$ We have the following equivalence: Therefore, $\text{L6}$ follows from $\text{L5}$ by the definition of the $\boxed{\color{blue}\text{the union of sets}}.$

### Proof by Cases

We can also prove the distributive laws using cases.

To demonstrate how this works, let's prove the following subset relation:

$$


A \cap (B \cup C) \subseteq (A \cap B) \cup (A \cap C)


$$

We start by considering an arbitrary element of $A \cap (B \cup C)$ and use the definition of intersection.

*Let $x \in A \cap (B \cup C).$ Then $x \in A$ and $x \in B \cup C.$*

Therefore, by the definition of union, we have two cases.

*Therefore, we have two cases: $x \in B$ or $x\in C.$*

*Let's consider each case in turn.*

We first consider the case $x\in B.$

****** *If $x \in B,$ then*

$$


x \in A \,\text{ and }\, x \in B \quad\Leftrightarrow\quad x \in A \cap B \subseteq (A\cap B) \cup (A \cap C).


$$

Note that we used the fact that $X\subseteq X\cup Y$ for any sets $X$ and $Y.$

*Hence, $x \in (A \cap B) \cup (A \cap C).$*

Now, we consider the case $x \in C.$ The argument is similar.

****** *If $x \in C,$ then*

$$


x \in A \,\text{ and }\, x \in C \quad\Leftrightarrow\quad x \in A \cap C \subseteq (A\cap B) \cup (A \cap C).


$$

*Hence, $x \in (A \cap B) \cup (A \cap C).$*

So, we have shown that $x \in (A \cap B) \cup (A \cap C)$ in either case, as we can write our conclusion:

*In both cases, we conclude that $x \in (A \cap B) \cup (A \cap C).$ Thus*

$$


A \cap (B \cup C) \subseteq (A \cap B) \cup (A \cap C).


$$

Let's now state this lemma and its proof.

### Stating the Full Proof

Lemma:

*If $A, B,$ and $C$ are sets, then $A \cap (B \cup C) \subseteq (A \cap B) \cup (A \cap C).$*

Proof:

*Let $x \in A \cap (B \cup C).$ Then $x \in A$ and $x \in B \cup C.$*

*Therefore, we have two cases: $x \in B$ or $x\in C.$ Let's consider each case in turn.*

****** *If $x \in B,$ then*

$$


x \in A \,\text{ and }\, x \in B \quad\Leftrightarrow\quad x \in A \cap B \subseteq (A\cap B) \cup (A \cap C).


$$

*Hence, $x \in (A \cap B) \cup (A \cap C).$*

****** *If $x \in C,$ then*

$$


x \in A \,\text{ and }\, x \in C \quad\Leftrightarrow\quad x \in A \cap C \subseteq (A\cap B) \cup (A \cap C).


$$

*Hence, $x \in (A \cap B) \cup (A \cap C).$*

*In both cases, we conclude that $x \in (A \cap B) \cup (A \cap C).$ Thus*

$$


A \cap (B \cup C) \subseteq (A \cap B) \cup (A \cap C).


$$

Let's now see a proof of the second inclusion.

### Example: Proving Set Inclusions Using Cases

#### Question

Given that $A,$ $B,$ and $C$ are sets, $(A \cap B) \cup (A \cap C) \subseteq A \cap (B \cup C).$

A proof of this statement is given below.

$\text{L1}:$ Let $x \in (A \cap B) \cup (A \cap C).$

$\text{L2}:$ Then, $x \in A \cap B$ or $x \in A \cap C.$

$\text{L3}:$ **** $x \in A \cap B$

$\text{L4}:$ $\Rightarrow x \in A \,\text{and} \, x \in B$

$\text{L5}:$ $\Rightarrow x \in A \,\text{and} x \in B \cup C$

$\text{L6}:$ $\Rightarrow A \cap (B \cup C).$

$\text{L7}:$ **** Similarly, if $x \in A \cap C,$ then $x \in A \,\text{and} x \in B \cup C \Rightarrow x\in A \cap (B \cup C).$

$\text{L8}:$ In both cases, $x \in A \cap (B \cup C).$

$\text{L9}:$ Therefore, $(A \cap B) \cup (A \cap C) \subseteq A \cap (B \cup C).$

Select the correct options in the following reasoning.

- Line $\text{L2}$ follows from line $\text{L1}$ by the definition of $\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_.$

- Line $\text{L4}$ follows from line $\text{L3}$ by the definition of $\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_.$

- Line $\text{L5}$ follows from line $\text{L4}$ due to the fact that $\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_$ for any sets $X$ and $Y.$

#### Explanation

Let's examine each statement in turn. Assume $X$ and $Y$ are sets.

- First, we consider lines $\text{L1}$ and $\text{L2}.$ We have the following equivalence: Therefore, line $\text{L2}$ follows from line $\text{L1}$ by the definition of $\boxed{\color{blue}\text{the union of sets}}.$

- Next, we consider lines $\text{L3}$ and $\text{L4}.$ We have the following equivalence: Therefore, line $\text{L4}$ follows from line $\text{L3}$ by the definition of $\boxed{\color{blue}\text{the intersection of sets}}.$

- Finally, we consider lines $\text{L4}$ and $\text{L5}.$ Since and $x \in B,$ it follows that $x\in B \cup C.$ Therefore, $\text{L5}$ follows from line $\text{L4}$ due to the fact that $\boxed{\color{blue}X\subseteq X\cup Y}$ for any sets $X$ and $Y.$

### A Summary of Proof Strategies

Let's summarize the strategies that we've studied for proving set identities:

- The first method is to prove two inclusions ($X\subseteq Y$ and $Y\subseteq X$) by translating between set and logical operations.

- The second method is to prove two inclusions ($X\subseteq Y$ and $Y\subseteq X$) using cases.

- The third is to form a chain of equivalent statements.

Let's see an example of how to prove a distributive law using the third strategy.

### Example: Proving the Distributive Properties

#### Question

Let $A,$ $B,$ and $C$ be sets, and let $U$ be a universal set. Prove that

$$


(A \cup B)\cap C = (A \cap C) \cup (B \cap C).


$$

#### Explanation

Suppose $X$ and $Y$ are sets, and $U$ is a universal set. Then we have the following definition for $X = Y{:}$

$$


X = Y \quad\Leftrightarrow \quad \forall x\in U,\: x\in X \Leftrightarrow x\in Y


$$

To prove a set equality using biconditionals, we must show an element belongs to one set if and only if it belongs to the other.

In this case, we're required to prove the following:

$$


(A \cup B)\cap C = (A \cap C) \cup (B \cap C)


$$

So, we start by considering an arbitrary element of $(A \cup B)\cap C$ and use the definition of intersection.

Given an element $x\in U,$ we have the following sequence of equivalent statements:

$$


x \in (A \cup B)\cap C\quad\Leftrightarrow\quad (x \in A \cup B)\land (x \in C)


$$

Then, we apply the definition of union:

$(x \in A \cup B)\land (x \in C) \quad\Leftrightarrow\quad ((x \in A) \lor (x \in B))\land (x \in C)$

Then, we distribute the conjunction over the disjunction:

$((x \in A) \lor (x \in B))\land (x \in C) \quad\Leftrightarrow\quad ((x \in A) \land (x \in C)) \lor ((x \in B) \land (x \in C))$

Then, we apply the definition of intersection once more:

$((x \in A) \land (x \in C)) \lor ((x \in B) \land (x \in C)) \quad\Leftrightarrow\quad (x \in (A \cap C)) \lor (x\in (B \cap C))$

Finally, we apply the definition of union:

$(x \in (A \cap C)) \lor (x\in (B \cap C)) \quad\Leftrightarrow\quad x \in (A \cap C) \cup (B \cap C)$

So, by a sequence of biconditional statements, we have proved the following equivalence:

$$


x \in A \cap (B \cup C)\qquad\Leftrightarrow\qquad x \in (A \cap C) \cup (B \cap C)


$$

So, we write our conclusion:

Therefore, we conclude that

$$


(A \cup B)\cap C = (A \cap C) \cup (B \cap C).


$$
