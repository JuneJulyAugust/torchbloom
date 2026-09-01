# Equivalence Relations

Source: https://www.mathacademy.com/topics/2622?courseId=76
Topic ID: 2622

## Prerequisites

- [Similarity Transformations](../../../high-school/traditional/lessons/geometry/491-similarity-transformations.md)
- [Grammatical Constructions for Conditional Statements](./4422-grammatical-constructions-for-conditional-statements.md)
- [Symmetric and Antisymmetric Relations](./4821-symmetric-and-antisymmetric-relations.md)
- [Transitive Relations](./4822-transitive-relations.md)

## Lesson

### Introduction

You may have noticed that the congruence of integers modulo $n$ satisfies the following important properties:

- The *reflexive* property. Every integer is congruent to itself:

- The *symmetric* property. If $a$ is congruent to $b,$ then $b$ is congruent to $a{:}$

- The *transitive* property. If $a$ is congruent to $b,$ and $b$ is congruent to $c,$ then $a$ is congruent to $c{:}$

Generally, if a relation is reflexive, symmetric, and transitive, it's called an **equivalence relation**. The congruence of integers modulo $n$ is an example of an equivalence relation.

The symbol "$\sim$" is often used to represent an equivalence relation. So, if $R$ is an equivalence relation, instead of $(x,y) \in R$ or $x \: R \: y,$ one can simply write $x \sim y.$

Some other important equivalence relations include the following:

- Equality ($=$) over $\mathbb R$

- Parity over $\mathbb Z$

- Triangle similarity over the (infinite) set containing all possible triangles

In particular, you may recall that when two triangles $P$ and $Q$ are similar, we write $P\sim Q.$ Now you know why we use this notation!

Equivalence relations are important because they encode our natural intuitions (namely, reflexivity, symmetry, and transitivity) describing what it means for two objects to be, in some sense, equal, equivalent, or "the same."

To understand this concretely, suppose we have a bag containing many colored balls, and we sort them into groups according to their color. Then, the following properties must be true:

- Each ball is the same color as itself. Therefore, each ball satisfies the reflexive property.

- If ball $x$ is the same color as ball $y,$ then ball $y$ is the same color as ball $x.$ Therefore, the balls within a given group satisfy the symmetric property.

- If ball $x$ is the same color as ball $y,$ and ball $y$ is the same color as ball $z,$ then ball $x$ must be the same color as ball $z.$ Therefore, the balls within a given group satisfy the transitive property.

Since the relation "is the same color as" over the set of balls is reflexive, symmetric, and transitive, it's an equivalence relation.

### Example: Determining Whether a Standard Relation Is an Equivalence

#### Question

Consider the following relation defined on the set $\mathcal{P}({B}),$ where $B=\{1,2,3,4\}.$

$$


X \,R\, Y \qquad\Leftrightarrow\qquad X \subseteq Y


$$

Which of the following statements are true?

1. $R$ is reflexive

2. $R$ is symmetric

3. $R$ is transitive

4. $R$ is an equivalence relation

#### Explanation

Given a relation $R$ on a set $A$:

- $R$ is reflexive if and only if for all $x \in A,$ $x \, R\, x.$

- $R$ is symmetric if and only if for all $x,y \in A,$ if $x \,R\, y,$ then $y \,R\, x.$

- $R$ is transitive if and only if for all $x,y,z \in A,$ if $x \,R\, y$ and $y \,R\, z,$ then $x \,R\, z.$

If $R$ is reflexive, symmetric, and transitive, then $R$ is an equivalence relation.

Let's consider each of the properties in turn.

- The relation $R$ is reflexive. For all $X \in \mathcal{P}({B}),$ $X \, \subseteq \, X.$

- The relation $R$ is not symmetric. For example, $\{1\} \subseteq \{1,2\}$ but $\{1,2\} \not \subseteq \{1\}.$

- The relation $R$ is transitive. For all $X,Y,Z \in \mathcal{P}({B}),$ if $X \subseteq Y$ and $Y \subseteq Z,$ then $X \subseteq Z.$

- The relation $R$ is not an equivalence relation since it's not symmetric.

Therefore, the correct answer is "I and III only."

### Example: Identifying Equivalence Relations on Finite Sets

#### Question

Consider the relation $R$ on the set $A=\{\alpha,\beta,\gamma\}$ defined as

$$


R=\big\{(\alpha, \alpha), (\beta,\beta), (\gamma,\gamma), (\beta,\gamma), (\gamma,\beta)\big\}.


$$

Which of the following statements are true?

1. $R$ is reflexive

2. $R$ is symmetric

3. $R$ is transitive

4. $R$ is an equivalence relation

#### Explanation

Given a relation $R$ on a set $A$:

- $R$ is reflexive if and only if for all $x \in A,$ $x \, R\, x.$

- $R$ is symmetric if and only if for all $x,y \in A,$ if $x \,R\, y,$ then $y \,R\, x.$

- $R$ is transitive if and only if for all $x,y,z \in A,$ if $x \,R\, y$ and $y \,R\, z,$ then $x \,R\, z.$

If $R$ is reflexive, symmetric, and transitive, then $R$ is an equivalence relation.

Let's consider each of the properties in turn.

- The relation $R$ is reflexive because $(\alpha, \alpha), (\beta,\beta), (\gamma,\gamma) \in R.$\:\:{\color{green}\checkmark}$

- The relation $R$ is symmetric because $(y,x) \in R$ whenever $(x,y) \in R.$ $\:\:{\color{green}\checkmark}$

- The relation $R$ is transitive because for all $x,y,z\in \{\alpha,\beta,\gamma\},$ if $(x,y)\in R$ and $(y,z)\in R,$ then $(x,z)\in R.$ Recall that it's sufficient to check only the cases when both pairs have different components: $({\color{blue}\beta},{\color{red}\gamma}) \in R$ and $({\color{red}\gamma},{\color{blue}\beta}) \in R,$ and also $({\color{blue}\beta},{\color{blue}\beta}) \in R$ $\:\:{\color{green}\checkmark}$ $({\color{blue}\gamma},{\color{red}\beta}) \in R$ and $({\color{red}\beta},{\color{blue}\gamma}) \in R,$ and also $({\color{blue}\gamma},{\color{blue}\gamma}) \in R$ $\:\:{\color{green}\checkmark}$

- Since $R$ is reflexive, symmetric, and transitive, it is an equivalence relation.$\:\:{\color{green}\checkmark}$

Therefore, the correct answer is "I, II, III, and IV."

### Example: Identifying Equivalence Relations

#### Question

Which of the following relations are equivalence relations on $\mathbb{Z}?$

1. $a \not \mid b$

2. $a \,R\, b$ if $a - b$ is a multiple of $7$

3. $a\, R \,b$ if $a \equiv (b - 1) \; (\text{mod}\:5)$

#### Explanation

Given a relation $R$ on a set $A$:

- $R$ is reflexive if and only if for all $x \in A,$ $x \, R\, x.$

- $R$ is symmetric if and only if for all $x,y \in A,$ if $x \,R\, y,$ then $y \,R\, x.$

- $R$ is transitive if and only if for all $x,y,z \in A,$ if $x \,R\, y$ and $y \,R\, z,$ then $x \,R\, z.$

If $R$ is reflexive, symmetric, and transitive, then $R$ is an equivalence relation.

With this in mind, let's consider each of the given relations.

- Relation I is not an equivalence relation. For example, it is not reflexive because $1 \mid 1.$

- Relation II is an equivalence relation. It is reflexive because for all $a \in \mathbb{Z},$ we have that $a - a=0$ is a multiple of $7.$ It is symmetric because for all $a, b \in \mathbb{Z},$ if $a - b$ is a multiple of $7,$ then $b - a=-(a-b)$ is also a multiple of $7.$ It is transitive because for all $a, b, c \in \mathbb{Z},$ if $a - b=7n$ and $b - c=7m,$ where $n, m$ are arbitrary integers, then This means that if $a - b$ is a multiple of $7$ and $b - c$ is a multiple of $7$ then $a-c$ is also a multiple of $7.$

- Relation III is not an equivalence relation. For example, it is not reflexive because $1 \not\equiv (1 - 1) \; (\text{mod}\:5).$

Therefore, the correct answer is "II only".
