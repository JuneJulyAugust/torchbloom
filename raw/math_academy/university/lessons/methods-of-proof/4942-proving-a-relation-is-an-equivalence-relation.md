# Proving a Relation Is an Equivalence Relation

Source: https://www.mathacademy.com/topics/4942?courseId=76
Topic ID: 4942

## Prerequisites

- [The Floor and Ceiling Functions](./290-the-floor-and-ceiling-functions.md)
- [Solving Systems of Equations Using Inverse Matrices](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/1023-solving-systems-of-equations-using-inverse-matrices.md)
- [Equivalence Relations](./2622-equivalence-relations.md)
- [Bijections](./2679-bijections.md)
- [Direct Proof](./2801-direct-proof.md)

## Lesson

### Introduction

In this lesson, we'll learn how to formally prove that a relation on a set is an equivalence relation.

Consider the relation defined below:

Let if and only if the integers and have the same last digit.

Let's prove that this relation is an equivalence relation. First, we recall the definition of an equivalence relation:

A relation is an equivalence relation if it is reflexive, symmetric, and transitive. Let's prove each part in turn.

Now, we'll verify all three properties in turn:

Checking reflexivity:

**Reflexivity.** Let Then since each integer has the same last digit as itself.

Checking symmetricity:

**Symmetricity.** Let and meaning that where is the last digit of integer Then, since

Checking transitivity:

**Transitivity:** Let and meaning that and Then, Hence, we have that So, is transitive.

Finally, since all three properties above hold, we can write the conclusion:

Therefore, is reflexive, symmetric, and transitive, meaning it's an equivalence relation.

Now that we've figured out all the details, let's write down our formal proof.

### Stating the Full Proof

Theorem:

Let $x \sim y$ if and only if the integers $x$ and $y$ have the same last digit. Then, $\sim$ is an equivalence relation.

Proof:

A relation $\sim$ is an equivalence relation if it is reflexive, symmetric, and transitive. Let's prove each part in turn.

**Reflexivity.** Let $x \in \mathbb{Z}.$ Then $x \sim x$ since each integer has the same last digit as itself.

**Symmetry.** Let $x,y \in \mathbb{Z}$ and $x \sim y,$ meaning that $d(x)=d(y),$ where $d(x)$ is the last digit of integer $x.$ Then, $y \sim x$ since

$$


d(x)=d(y) \quad\Leftrightarrow\quad d(y)=d(x).


$$

**Transitivity:** Let $x,y,z \in \mathbb{Z},$ $x \sim y,$ and $y \sim z,$ meaning that $d(x)=d(y)$ and $d(y)=d(z).$ Then,

$$


d(x)=d(y)=d(z).


$$

Hence, we have that $d(x)=d(z).$ So, $\sim$ is transitive.

Therefore, $\sim$ is reflexive, symmetric, and transitive, meaning it's an equivalence relation.

### Example: Proving Reflexivity, Symmetricity, and Transitivity

#### Question

Consider the following statement:

Let $X$ be the set of all people, and $a \sim b$ if and only if $a$ and $b$ are of the same age, for $a, b \in X.$ Then, $\sim$ is a transitive relation on $X.$

A proof of this statement is given below.

$\text{L1}{:}\:$ Let $a, b, c \in X$ such that $a \sim b$ and $b \sim c.$

$\text{L2}{:}\:$ Then, $a$ and $b,$ and $b$ and $c$ are of the same age.

$\text{L3}{:}\:$ So, $a$ and $c$ are the same age.

$\text{L4}{:}\:$ Thus, $a \sim c.$

$\text{L5}{:}\:$ Therefore, $\sim$ is transitive on $X.$

What words are missing from the reasoning below?

- Line $\text{L2}$ follows from line $\text{L1}$ by the definition of $\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\:.$

- Line $\text{L5}$ follows from $\text{L1}$ and $\text{L4}$ by the definition of $\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_$ of relations.

- To prove that $\sim$ is an equivalence relation, we also need to demonstrate that $\sim$ is $\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\:$ and $\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\:.$

#### Explanation

Let's examine each statement in turn.

- First, we consider lines $\text{L1}$ and $\text{L2}.$ From the facts that $a \sim b$ and $b \sim c,$ we can conclude that $a$ and $b,$ and $b$ and $c,$ are of the same age by the definition of $∼$

- Next, we consider lines $\text{L1},$ $\text{L4},$ and $\text{L5}.$ Since $a \sim b$ and $b \sim c$ implies $a \sim c,$ we can conclude that our relation is transitive. Therefore, $\text{L5}$ follows from $\text{L1}$ and $\text{L4}$ by the definition of $\boxed{\color{blue}\text{transitivity}}$ of relations.

- Finally, to prove that we have an equivalence relation, we also need to demonstrate that $\sim$ is $\boxed{\color{blue}\text{reflexive}}$ and $\boxed{\color{blue}\text{symmetric}}.$

### Example: Proving a Relation Is an Equivalence Relation

#### Question

Let $A \sim B$ for $2\times 2$ square matrices $A$ and $B$ if and only if there exists an invertible $2\times 2$ matrix $S$ such that $B = S^{-1}AS.$ Prove that $\sim$ is an equivalence relation on the set of all $2\times 2$ square matrices.

**

#### Explanation

A relation $\sim$ is an equivalence relation if it is reflexive, symmetric, and transitive. Let's prove each part in turn.

**** Let $A$ be an $2 \times 2$ matrix. Then, $A \sim A$ since

$$


\begin{aligned}𝐴 & =(𝐼_{2})^{−1}𝐴𝐼_{2} \\ & =𝐼_{2}𝐴𝐼_{2}\end{aligned}


$$

where $I_2$ is the $2 \times 2$ identity matrix.

**** Let $A$ and $B$ be $2\times 2$ matrices and $A \sim B,$ meaning that there exists an invertible $2\times 2$ matrix $S$ such that $B = S^{-1}AS.$ Then, $y \sim x$ since, if we pre-multiply this equation by $S,$ we get

$$


\begin{aligned}𝐵 & =𝑆^{−1}𝐴𝑆 \\ 𝑆𝐵 & =𝑆𝑆^{−1}𝐴𝑆 \\ 𝑆𝐵 & =𝐼_{2}𝐴𝑆 \\ 𝑆𝐵 & =𝐴𝑆\end{aligned}


$$

and then post-multiplying by $S^{-1},$ we get

$$


\begin{aligned}𝑆𝐵𝑆^{−1} & =𝐴𝑆𝑆^{−1} \\ 𝑆𝐵𝑆^{−1} & =𝐴𝐼_{2} \\ 𝑆𝐵𝑆^{−1} & =𝐴 \\ 𝐴 & =𝑆𝐵𝑆^{−1} \\ 𝐴 & =(𝑆^{′})^{−1}𝐵𝑆^{′},\end{aligned}


$$

where we have defined $S'=S^{-1}.$

**** Let $A,B,$ and $C$ be $2\times 2$ square matrices where $A \sim B,$ and $B \sim C,$ meaning that there exist invertible matrices $S$ and $T$ such that $B = S^{-1}AS$ and $C = T^{-1}BT.$ Then,

$$


\begin{aligned}𝐶 & =𝑇^{−1}𝐵𝑇 \\ & =𝑇^{−1}(𝑆^{−1}𝐴𝑆)𝑇 \\ & =(𝑇^{−1}𝑆^{−1})𝐴(𝑆𝑇) \\ & =(𝑆𝑇)^{−1}𝐴(𝑆𝑇).\end{aligned}


$$

Since $S$ and $T$ are invertible, we know that $ST$ is also invertible. Hence, there exists an invertible matrix $S'=ST$ such that $C = (S')^{-1}AS'.$ So, $\sim$ is transitive.

Therefore, $\sim$ is reflexive, symmetric, and transitive, meaning it's an equivalence relation.
