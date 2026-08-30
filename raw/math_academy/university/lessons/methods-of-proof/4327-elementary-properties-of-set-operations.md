# Elementary Properties of Set Operations

Source: https://www.mathacademy.com/topics/4327?courseId=76
Topic ID: 4327

## Prerequisites

- [Subsets](./50-subsets.md)

## Lesson

### Introduction

Suppose that $U$ is a universal set and $A\subseteq U.$ Then, we have the following basic properties:

- The intersection of a set and its complement gives the empty set:

- The union of a set and its complement gives the universal set:

- The complement of the complement of a set gives the original set:

- The complement of the universal set is the empty set:

- The complement of the empty set is the universal set:

We'll prove these properties in future lessons. For now, let's get some practice at applying them.

### Example: Identifying Elementary Properties of Union, Intersection, and Complement

#### Question

Given that $R$ is a subset of a universal set $U,$ simplify the following expression:

$$


\overline{R} \cap R


$$

#### Explanation

The intersection of a set and its complement gives the empty set.

Therefore, $\overline{R} \cap R = \emptyset.$

### Unions and Intersections With the Universal and Empty Sets

Given that $U$ is a universal set and $A \subseteq U,$ we have the following additional properties:

- The intersection of $A$ with the empty set equals the empty set:

- The union of $A$ with the empty set equals $A{:}$

- The union of $A$ with the universal set equals the universal set.

- The intersection of $A$ with the universal set equals $A{:}$

### Idempotent Properties of Union and Intersection

We also have two **idempotent** properties of union and intersection.

- The union of the set with itself gives the original set:

- The intersection of the set with itself gives the original set:

### Example: Applying the Properties of Union and Intersection

#### Question

Simplify the expression $((A \cup A) \cap A) \cup B.$

#### Explanation

First, the expression $A \cup A$ simplifies to just $A.$ So, the given expression can be simplified to

$$


(A \cap A) \cup B.


$$

Then, the expression $A \cap A$ simplifies to just $A.$ So, the expression can be further simplified to

$$


A \cup B.


$$

Therefore,

$$


( (A \cup A) \cap A) \cup B = A \cup B.


$$

### Associative and Commutative Properties of Union and Intersection

Let $A,$ $B,$ and $C$ be subsets of a universal set $U.$

- The **associative** properties of union and intersection state the following:

- The **commutative** properties of union and intersection state the following:

### Example: Applying the Associative and Commutative Properties of Union and Intersection

#### Question

Simplify the expression $A \cap (\overline{B} \cap A).$

#### Explanation

Using the commutative, associative, and idempotent properties of intersection, we get

$$


\begin{aligned}𝐴∩(\overset{𝐵}{}∩𝐴) & =𝐴∩(𝐴∩\overset{𝐵}{}) \\ & =(𝐴∩𝐴)∩\overset{𝐵}{} \\ & =𝐴∩\overset{𝐵}{}.\end{aligned}


$$
