# N-ary Relations

Source: https://www.mathacademy.com/topics/4824?courseId=76
Topic ID: 4824

## Prerequisites

- [Power Sets](./51-power-sets.md)
- [The Domain and Range of a Relation](./4819-the-domain-and-range-of-a-relation.md)

## Lesson

### Introduction

In this lesson, we'll see how the concept of a relation can be extended to subsets of Cartesian products containing more than three factors.

First, recall that a binary relation over $A$ is any subset of the Cartesian product $A\times A = A^2.$ We can extend this idea as follows:

*A **** $R$ over the set $A$ is a subset of the Cartesian product $A \times A \times A = A^3$*

$$


R \subseteq A^3


$$

For example, consider the relation $R$ defined on $A = \big\{1, 2, \ldots, 10 \big\}$ by

$$


(x,y,z) \in R \qquad \Leftrightarrow \qquad x + y \equiv z \quad (\textrm{mod} \: 4).


$$

Note that, for example,

- $(2,3,9) \in R$ since $2 + 3 \equiv 9 \: (\textrm{mod} \: 4),$ but

- $(1,1,1) \not\in R$ since $1+1 \not\equiv 1 \: (\textrm{mod} \: 4).$

Similar to binary relations, there is no need for the factors of the Cartesian product always to be the same set:

*A **** $R$ over the sets $A,B,C$ is a subset of $A \times B \times C{:}$*

$$


R \subseteq A \times B \times C


$$

Let's see some more examples.

### Example: Identifying True Statements Given a Finite Ternary Relation

#### Question

Consider the set $A = \big\{1, 2, 3, 4, 5 \big\}.$ Given the relation $R$ on $A$ defined by

$$


(x,y,z) \in R \qquad \Leftrightarrow \qquad xyz = 9,


$$

which of the following statements are true?

1. $(2,2,4)\in R$

2. $(3,1,3)\in R$

3. $(1,3,4)\in R$

#### Explanation

A ternary ($3$-ary) relation $R$ over the sets $A,B,C$ is a subset of the Cartesian product $A \times B \times C.$

$$


R \subseteq A \times B \times C


$$

In this case, we have $(x,y,z) \in R \subseteq A^3$ if and only if $xyz = 9.$

With that in mind, let's examine our statements in turn:

- Statement I is false. We have $(2,2,4) \notin R$ since $2 \cdot 2 \cdot 4 = 16 \neq 9.$

- Statement II is true. We have $(3,1,3) \in R$ since $3 \cdot 1 \cdot 3 = 9.$

- Statement III is false. We have $(1,3,4) \notin R$ since $1 \cdot 3 \cdot 4 = 12 \neq 9.$

Therefore, the correct answer is "II only."

### N-ary Relations

A **$n$-ary relation** $R$ over the sets $A_1,A_2,\ldots,A_n$ is a subset of the Cartesian product $A_1 \times A_2 \times \cdots \times A_n{:}$

$$


R \subseteq A_1 \times A_2 \times \cdots \times A_n


$$

Note that:

- Cases where $n=2$ are commonly referred to as a *binary* relations ($2$-ary relations).

- Cases where $n=3$ is commonly referred to as a *ternary* relations ($3$-ary relations).

### Example: Identifying True Statements Given a Infinite N-ary Relation

#### Question

Given the relation $R$ on $\mathcal{P}(\mathbb{N})^4$ defined by

$$


(A_1, A_2, A_3, A_4) \in R \qquad \Leftrightarrow \qquad A_1 \cup A_2 = A_3 \cup A_4,


$$

which of the following statements are true?

1. $\big(\{1\}, \{3\}, \emptyset, \{1,3\}\big) \in R$

2. $\big(\mathbb{N}, \emptyset, \{2\}, \{2,3\}\big) \in R$

3. $\big(\{1\}, \{2\}, \{3\}, \{4\}\big) \in R$

#### Explanation

A $n$-ary relation $R$ over the sets $A_1,A_2,\ldots,A_n$ is a subset of the Cartesian product $A_1 \times A_2 \times \cdots \times A_n.$

$$


R \subseteq A_1 \times A_2 \times \cdots \times A_n


$$

In this case, we have $(A_1, A_2, A_3, A_4) \in R \subseteq \mathcal{P}(\mathbb{N})^4$ if and only if $A_1 \cup A_2 = A_3 \cup A_4.$

With that in mind, let's examine our statements in turn:

- Statement I is true. We have $\big(\{1\}, \{3\}, \emptyset, \{1,3\}\big) \in R$ since

- Statement II is false. We have $\big(\mathbb{N}, \emptyset, \{2\}, \{2,3\}\big) \not\in R$ since

- Statement III is false. We have $\big(\{1\}, \{2\}, \{3\}, \{4\}\big) \not\in R$ since

Therefore, the correct answer is "I only."
