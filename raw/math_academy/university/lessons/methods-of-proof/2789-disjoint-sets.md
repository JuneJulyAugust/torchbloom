# Disjoint Sets

Source: https://www.mathacademy.com/topics/2789?courseId=76
Topic ID: 2789

## Prerequisites

- [Describing Planar Regions Using Set-Builder Notation](./4392-describing-planar-regions-using-set-builder-notation.md)

## Lesson

### Introduction

Two sets $A$ and $B$ are **disjoint** if they have no element in common. In other words, their intersection is empty:

$$


A \cap B = \emptyset


$$

For example, consider the following sets:

$$


A = \{ -1,-2,-3 \}, \qquad B=\{ 5,10 \}


$$

These sets are disjoint since their intersection is empty:

$$


A\cap B = \{ -1,-2,-3 \} \cap \{ 5,10 \} = \emptyset


$$

On the other hand, $C=(-\infty,5]$ and $D=(-2,\infty)$ are *not* disjoint since the intersection of these sets is *not* empty:

$$


C\cap D = (-\infty,5] \cap (-2,\infty) = (-2,5] \neq \emptyset


$$

### Example: Identifying Disjoint Sets

#### Question

Consider the following sets:

$$


A = \{ 2n \mid n \in \mathbb{N}\}, \qquad B = \left\{ 2^{-n} \mid n \in \mathbb {N}\right\}


$$

Which of the following statements are true?

1. $A = \{2, 4, 6,\ldots \}$

2. $A \cap B = \emptyset$

3. $A$ and $B$ are disjoint

#### Explanation

Two sets $A$ and $B$ are ** if they have no element in common, i.e., their intersection is empty:

$$


A \cap B = \emptyset


$$

With that in mind, let's examine our sets.

- Statement I is true.

- Statement II is true. First, note that Then, the intersection of $A$ and $B$ is

- Statement III is true. Since the intersection is empty, the two sets are disjoint.

Therefore, the correct answer is "I, II and III."

### The Disjoint Union of Non-Overlapping Sets

The **disjoint union** of two sets is defined differently depending on whether the sets are non-overlapping (disjoint) or overlapping (have a non-empty intersection). We'll use the special symbol "$\sqcup$" (square cup) to denote the disjoint union.

The disjoint union of two non-overlapping (disjoint) sets $A$ and $B$ is simply the union of the sets.

For example, since

$$


\{ 0,2,4 \} \cap \{ 1, 3 \} = \emptyset,


$$

we find the disjoint union of these sets as follows:

$$


\begin{aligned}{0,2,4}⊔{1,3} & ={0,2,4}∪{1,3} \\ & ={0,1,2,3,4}\end{aligned}


$$

### Example: Finding the Disjoint Union of Non-Overlapping Sets

#### Question

Find the disjoint union of the sets $\{-1, 1, \sqrt{5} \}$ and $\{v, w \}.$

#### Explanation

Notice that the sets are disjoint since

$$


\{ -1, 1, \sqrt{5} \} \cap \{ v, w \} = \emptyset.


$$

Therefore, the disjoint union is simply the union:

$$


\begin{aligned}{−1,1,\sqrt{√5}}⊔{𝑣,𝑤} & ={−1,1,\sqrt{√5}}∪{𝑣,𝑤} \\ & ={−1,1,\sqrt{√5},𝑣,𝑤}\end{aligned}


$$

### The Disjoint Union of Overlapping Sets

Now, consider the following overlapping sets:

$$


A_1 = \{ \square, \triangle \}, \qquad A_2 = \{ \heartsuit, \square\}.


$$

These sets overlap because their intersection is non-empty.

$$


A_1 \cap A_2 = \{ \square \} \neq \emptyset.


$$

To construct the disjoint union of these overlapping sets, we proceed as follows:

- For each of our sets, we form the associated set, where each element is "tagged" with the corresponding index:

- As a result, the new sets $A_1^\ast$ and $A_2^\ast$ are non-overlapping. So, the disjoint union of our sets is simply the union of the associated tagged sets:

### Example: Finding the Disjoint Union of Overlapping Sets

#### Question

Find the disjoint union of the sets $A_1 = \{7,8 \}$ and $A_2 = \{2,4,8 \}.$

#### Explanation

Notice that the sets are overlapping since

$$


\{ 7,8 \} \cap \{ 2,4,8 \} = \{ 8 \} \neq \emptyset.


$$

So, for each of our sets, we form the associated set, where each element is tagged with the corresponding index, as follows:

$$


\begin{aligned} & 𝐴_{1} & & \,→\, & & 𝐴_{∗1}^{}={(7,1),(8,1)} \\ & 𝐴_{2} & & \,→\, & & 𝐴_{∗2}^{}={(2,2),(4,2),(8,2)}\end{aligned}


$$

Now, the disjoint union of our sets is simply the union of the associated tagged sets:

$$


\begin{aligned}𝐴_{1}⊔𝐴_{2} & ={7,8}⊔{2,4,8} \\ & =𝐴_{∗1}^{}∪𝐴_{∗2}^{} \\ & ={(7,1),(8,1)}∪{(2,2),(4,2),(8,2)} \\ & ={(7,1),(8,1),(2,2),(4,2),(8,2)}\end{aligned}


$$
