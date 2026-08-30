# Permutations

Source: https://www.mathacademy.com/topics/703?courseId=111
Topic ID: 703

## Prerequisites

- [Introduction to Functions](../algebra-i/470-introduction-to-functions.md)
- [Ordering Objects](./775-ordering-objects.md)

## Lesson

### Introduction

A **permutation** is a selection of objects in which order matters. Two selections of the same items are counted as different selections if they are in a different order.

For example, suppose that we have $5$ books, but our bookshelf can only hold $3.$ We want to place $3$ books on the shelf and the rest will stay in the drawer.

How many permutations are there? In other words, how many ways can we place $3$ books on the shelf (in a particular order)?

Let's think about all the choices we have as we fill up the bookshelf:

- We can place any of our $5$ books in the first slot of the bookshelf.

- Now that we've placed one book on the bookshelf, we have $4$ books remaining. We can place any of these $4$ remaining books in the second slot.

- Now that we've placed two books on the bookshelf, we have $3$ books remaining. We can place any of these $3$ remaining books in the third slot.

The number of choices we have for each slot is shown below:

$$


\begin{aligned}5 choices & 4 choices & 3 choices\end{aligned}


$$

To find the total number of arrangements, we can use the multiplication principle:

$$


5\times4\times3 = 60.


$$

### The General Formula for Permutations

In general, the number of permutations of $n$ objects taken $r$ at a time is given by the formula

$$


_{n}P_r = \frac{n!}{(n-r)!}


$$

In the previous example, we had $n=5$ books and $r=3$ slots in the bookshelf. Using the formula, the total number of permutations is computed as

$$


\begin{aligned}_{5}𝑃_{3} & =\frac{5!}{(5−3)!} \\ & =\frac{5!}{2!} \\ & =\frac{5×4×3×2!}{2!} \\ & =\frac{5×4×3×2!}{2!} \\ & =5×4×3 \\ & =60.\end{aligned}


$$

We got the same result as before!

**Note:** We can write ${}_nP_r$ in a number of ways:

$$


{}_nP_r = {}^nP_r = P(n,r)


$$

All of these mean the same thing.

### Example: Calculating a Permutation

#### Question

Calculate the value of ${}_{11}P_2.$

#### Explanation

The formula for ${}_nP_r$ is given by

$$


{}_nP_r = \dfrac {n!} {(n - r)!} \,.


$$

Substituting $n={11}$ and $r=2$ into the above, we get

$$


 \begin{aligned} {}_{11}P_2 &= \dfrac {11!} {(11 - 2)!} \\\[5pt] &= \dfrac {11!}{9!} \\\[5pt] &= \dfrac {11 \cdot 10 \cdot 9!} {9!} \\\[5pt] &= 11 \cdot 10 \\\[5pt] &= 110. \end{aligned}


$$

### Example: Calculating a Permutation Given Using Alternate Notation

#### Question

Evaluate $P(9,3).$

#### Explanation

The formula for ${}_nP_r$ is given by

$$


{}_nP_r = \dfrac {n!} {(n - r)!} \,.


$$

$P(9,3)$ means the same thing as $_{9}P_3.$ Using the usual formula for ${}_nP_r,$ we get

$$


\begin{aligned}𝑃(9,3) & =\frac{9!}{(9−3)!} \\ & =\frac{9!}{6!} \\ & =\frac{9⋅8⋅7⋅6!}{6!} \\ & =9⋅8⋅7 \\ & =504.\end{aligned}


$$

### Example: Calculating the Number of Permutations of Objects Chosen From a Group Fewer Than Ten

#### Question

In a horse race with $8$ horses, how many different ways can the gold, silver, and bronze medals be awarded?

#### Explanation

The number of permutations of $n$ objects taken $r$ at a time is given by the formula

$$


_{n}P_r = \frac{n!}{(n-r)!}.


$$

There are $8$ horses, so $n=8.$ We want to select $3$ of those horses for gold, silver, and bronze, so we have $r=3.$

Therefore, the number of different ways to award the medals is

$$


\begin{aligned}_{8}𝑃_{3} & =\frac{8!}{(8−3)!} \\ & =\frac{8!}{5!} \\ & =\frac{8⋅7⋅6⋅5!}{5!} \\ & =8⋅7⋅6 \\ & =336.\end{aligned}


$$

### Example: Calculating the Number of Permutations of Objects Chosen From a Group of at Least Ten

#### Question

A company has $20$ employees. A total of $4$ employees are needed to fill the roles of president, vice president, treasurer, and secretary. How many different ways can this be achieved?

#### Explanation

The number of permutations of $n$ objects taken $r$ at a time is given by the formula

$$


_{n}P_r = \frac{n!}{(n-r)!}.


$$

There are $20$ employees, so $n=20.$ We want to select $4$ of those employees to fill the roles of president, vice president, treasurer, and secretary, so we have $r=4.$

Therefore, the number of different ways to fill the roles is

$$


\begin{aligned}_{20}𝑃_{4} & =\frac{20!}{(20−4)!} \\ & =\frac{20!}{16!} \\ & =\frac{20⋅19⋅18⋅17⋅16!}{16!} \\ & =20⋅19⋅18⋅17 \\ & =116\,280.\end{aligned}


$$
