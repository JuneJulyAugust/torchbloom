# The Domain and Range of a Relation

Source: https://www.mathacademy.com/topics/4819?courseId=76
Topic ID: 4819

## Prerequisites

- [Index Notation for Matrices](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/1167-index-notation-for-matrices.md)
- [Properties of Transformed Logarithmic Functions](../../../high-school/traditional/lessons/algebra-ii/1610-properties-of-transformed-logarithmic-functions.md)
- [Domain and Range of Quadratic Functions](../../../high-school/traditional/lessons/algebra-i/1882-domain-and-range-of-quadratic-functions.md)
- [Relations on Infinite Sets](./4826-relations-on-infinite-sets.md)
- [Finding Zeros and Extrema of Transformed Sine and Cosine Functions](../../../high-school/traditional/lessons/algebra-ii/5088-finding-zeros-and-extrema-of-transformed-sine-and-cosine-functions.md)

## Lesson

### Introduction

Recall that a relation $R$ over a set $A$ is a subset of the Cartesian product $A \times A = A^2.$

$$


R\subseteq A^2


$$

More generally, the two factors in the Cartesian product do not have to be the same set. This gives the following definition:

*A relation $R$ over $A$*and*$B$ is a subset of $A \times B.$*

$$


R \subseteq A\times B


$$

For example, consider the following sets:

$$


A = \{ 1, 2, 3, 4 \}, \qquad B = \{ 4,5,6,7 \}


$$

The following set is a relation over $A$ and $B.$

$$


R = \{ (1,4), (1,5), (2, 4), (3,5) \}


$$

For each ordered pair $(x,y)\in R,$ we have that $x\in A$ and $y\in B.$

### The Domain and Range of a Relation

Given a relation $R \subseteq A \times B,$ we have the following definitions:

- The **domain** of $R$ is the set containing all elements from $A$ that appear as the first component of the ordered pairs in $R.$

- The **range** of $R$ is the set containing all elements from $B$ that appear as the second component of the ordered pairs in $R.$

- The **codomain** of $R$ is any superset of the range.

For example, consider the sets $A = \{1, 2, 3, 4 \}, B = \{4,5,6,7 \}$ and the relation $R\subseteq A\times B$ given by

$$


R = \{ (1,4), (1,5), (2, 4), (3,5) \}.


$$

Let's calculate the domain and range of this relation:

- To find the domain, we consider the first components of the ordered pairs belonging to our relation: The set of first components is $\{1,1,2,3 \} = \{1,2,3 \}.$ Hence, the *domain* of $R$ is $\{1,2,3 \}.$

- To find the range, we consider the second components of the pairs belonging to our relation: The set of second components is $\{4,5,4,5 \} = \{4,5 \}.$ Hence, the *range* of $R$ is $\{4,5 \}.$

We can visualize the domain and range using a mapping diagram, where each ordered pair is represented by the arrow starting at the first component and ending in the second component:

![Instructional graphic](../../../lesson-assets/methods-of-proof/topic-4819/60a501c1e1a45be2.png)

### Example: Finding the Domain and Range of a Relation

#### Question

Consider the following relation on $\mathbb R^2.$

$$


R = \big\{ (x,y) \in \mathbb R^2 \: : \: y = \sin{x} \big\}


$$

What are the domain and range of this relation?

#### Explanation

Given a relation $R \subseteq A \times B,$

- the ** of $R$ is the set containing all elements from $A$ that appear as the first component of the ordered pairs in $R,$ and

- the ** of $R$ is the set containing all elements from $B$ that appear as the second component of the ordered pairs in $R.$

With that in mind, we examine the given relation.

- The set of first components contains all real numbers $\mathbb{R}.$ Hence, the domain is $\mathbb{R}.$

- Notice that $-1 \leq \sin{x} \leq 1$ for all $x\in\mathbb R,$ and it is continuous on $\mathbb R.$ So, the set of second components contains all real numbers greater than or equal to $-1$ and less than or equal to $1$: Therefore, the range is $\{y\in \mathbb R\:: \: -1 \leq y \leq 1 \}.$

### Adjacency Matrix of a Relation

If a relation $R$ is defined over $A = \{a_1, a_2, \ldots, a_m \}$ and $B = \{b_1, b_2, \ldots b_n \}$ of cardinalities $m$ and $n,$ respectively, the **adjacency matrix** of $R$ is a $m \times n$-matrix (or table), where the element $r_{ij}$ at the intersection of the $i$th row and the $j$th column is given by

$$


\begin{aligned}1,\,if a_i \: R \: b_j, \\ 0,\,otherwise.\end{aligned}


$$

For example, let's construct the adjacent matrix for the relation

$$


S = \{ (1,2), (1,3), (2,1), (3,2) \},


$$

defined on $A = \{1,2,3 \}.$ We start by writing down the elements of $A$ along the rows and columns of the matrix:

To fill in the matrix, we run over the ordered pairs in our relation:

- Since $(1,2)$ belongs to the relation, we write $1$ in the intersection of the $1$st row and $2$nd column.

- Since $(1,3)$ belongs to the relation, we write $1$ in the intersection of the $1$st row and $3$rd column.

- Since $(2,1)$ belongs to the relation, we write $1$ in the intersection of the $2$nd row and $1$st column.

- Since $(3,2)$ belongs to the relation, we write $1$ in the intersection of the $3$rd row and $2$nd column.

All the other cells should be filled with zeros. Therefore, we obtain the following adjacency matrix:

### Example: Interpreting an Adjacency Matrix

#### Question

The adjacency matrix of the relation $R,$ defined over the sets $\{3, 4, 5 \}$ and $\{\bigstar, \maltese \},$ is given above. Which of the following ordered pairs belong to the relation?

1. $(4, \bigstar)$

2. $(5, \maltese)$

3. $(3, \maltese)$

#### Explanation

If a relation $R$ is defined over $A = \{a_1, a_2, \ldots, a_m \}$ and $B = \{b_1, b_2, \ldots b_n \}$ of cardinalities $m$ and $n,$ respectively, the ** of $R$ is a $m \times n$-matrix (or table), where the element $r_{ij}$ at the intersection of the $i$th row and the $j$th column is given by

$$


\begin{aligned}1,\,if a_i \: R \: b_j, \\ 0,\,otherwise.\end{aligned}


$$

With that in mind, let's examine the given ordered pairs.

- The pair $(4, \bigstar)$ belongs to the relation. Indeed, the adjacency matrix has $1$ on the intersection of the $4$-row and the $\bigstar$-column.

- The pair $(5, \maltese)$ belongs to the relation. Indeed, the adjacency matrix has $1$ on the intersection of the $5$-row and the $\maltese$-column.

- The pair $(3, \maltese)$ does not belong to the relation since the adjacency matrix has $0$ on the intersection of the $3$-row and the $\maltese$-column.

Therefore, the correct answer is "I and II only."

### Example: Building an Adjacency Matrix

#### Question

Consider the sets $A = \{2,4,6\}$ and $B= \big\{\{1,6\}, \{2,3\}, \mathbb{N}\big\},$ and the relation $R = \{(x,y) \in A \times B \::\: x \in y \}.$ Fill in the missing values in the adjacency matrix of the relation:

#### Explanation

If a relation $R$ is defined over $A = \{a_1, a_2, \ldots, a_m \}$ and $B = \{b_1, b_2, \ldots b_n \}$ of cardinalities $m$ and $n,$ respectively, the ** of $R$ is a $m \times n$-matrix (table), where the element $r_{ij}$ at the intersection of the $i$th row and the $j$th column is given by

$$


\begin{aligned}1,\,if a_i \: R \: b_j, \\ 0,\,otherwise.\end{aligned}


$$

The relation $R$ is the set of ordered pairs $(x,y) \in A \times B$ with $x \in y.$

Let's consider each row in our table.

- If $x = 2,$ then the values $y=\{2,3\}$ and $y= \mathbb{N}$ satisfy $x \in y.$ So, $R$ contains the ordered pairs $(2,\{2,3\})$ and $(2,\mathbb{N}),$ and we write $1$ in the intersection of the $1$st row and the $2$nd column and in the intersection of the $1$st row and the $3$rd column in the adjacency matrix.

- If $x = 4,$ then the value $y = \mathbb{N}$ satisfies $x \in y.$ So, $R$ contains the ordered pair $\big(4, \mathbb{N} \big),$ and we write $1$ in the intersection of the $2$nd row and the $3$rd column in the adjacency matrix.

- If $x = 6,$ then the values $y=\{1,6\}$ and $y= \mathbb{N}$ satisfy $x \in y.$ So, $R$ contains the ordered pairs $(6,\{1,6\})$ and $(6,\mathbb{N}),$ and we write $1$ in the intersection of the $3$rd row and the $1$st column and in the intersection of the $3$rd row and the $3$rd column in the adjacency matrix.

All the other cells in the matrix must be filled with zeros. Therefore, we have the following adjacency matrix:
