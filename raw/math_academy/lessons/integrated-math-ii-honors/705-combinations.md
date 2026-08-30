# Combinations

Source: https://www.mathacademy.com/topics/705?courseId=128
Topic ID: 705

## Prerequisites

- [Permutations](../geometry/703-permutations.md)

## Lesson

### Introduction

A **combination** is a selection of objects in which order does *not* matter. Two selections of the same items are always counted as the same selections, even if the items are in a different order.

For example, suppose we have $5$ books but can only take $3$ of them on a trip. How many combinations are there? In other words, how many ways can we take $3$ of the books?

First, recall that the total number of ways of selecting $3$ books from $5$ (where order matters) is given by the permutation ${}_5P_3{:}$

$$


\begin{aligned}_{5}𝑃_{3} & =\frac{5!}{(5−3)!} \\ & =\frac{5!}{2!} \\ & =60\end{aligned}


$$

However, the permutation calculation ${}_5P_3$ assumes that order of selection matters, but in our problem order is not important. Regardless of the order in which we choose the books, the chosen books are coming with us on the trip and the rest of the books will be left behind.

So, we must divide by the number of ways to order the $3$ books that we selected, which is $3!.$ Doing this, we get

$$


\begin{aligned}\frac{_{5}𝑃_{3}}{3!} & =\frac{60}{3!} \\ & =\frac{60}{6} \\ & =10.\end{aligned}


$$

Therefore, there are $10$ ways that we can take $3$ of the books with us.

### The General Formula for Combinations

In general, the number of unique combinations of $n$ objects taken $r$ at a time is given by the formula

$$


{}_nC_r = \frac{{}_nP_r}{r!} = \dfrac{n!}{(n-r)!r!}.


$$

This is pronounced "en-see-arr." The "C" stands for "combination."

In the previous example, we had $n=5$ books, taking $r=3$ books with us on the trip. Using the formula, the total number of combinations is computed as

$$


\begin{aligned}_{5}𝐶_{3} & =\frac{5!}{(5−3)!3!} \\ & =\frac{5!}{2!3!} \\ & =\frac{5×4×3!}{2!3!} \\ & =\frac{5×4×3!}{2!3!} \\ & =\frac{5×4}{2!} \\ & =\frac{20}{2} \\ & =10.\end{aligned}


$$

We got the same result as before!

**Note:** An alternative notation for ${}_nC_r$ is $\displaystyle {{n}\choose{r}}.$

### Example: Evaluating Combinations

#### Question

Evaluate ${}_{7}C_5.$

#### Explanation

The number of combinations of $n$ objects taken $r$ at a time is given by the formula

$$


{}_nC_r = \dfrac{n!}{(n-r)!r!}.


$$

Substituting $n=7$ and $r=5,$ we get

$$


 \begin{aligned} {}_{7}C_5 &= \dfrac {7!} {(7 - 5)!5!} \\\[5pt] &= \dfrac {7!} {2!5!} \\\[5pt] &= \dfrac {7 \cdot 6 \cdot 5!} {2!5!} \\\[5pt] &= \dfrac {7 \cdot 6 } {2 \cdot 1 } \\\[5pt] & = \dfrac {42}{2} \\\[5pt] &= 21. \end{aligned}


$$

### Example: Evaluating Combinations Given Using Alternate Notation

#### Question

Evaluate $(\begin{aligned}12 \\ 10\end{aligned})$

#### Explanation

First, note that $\displaystyle{{12}\choose{10}}$ means the same thing as $_{12}C_{10}.$

In general, the number of combinations of $n$ objects taken $r$ at a time is given by the formula

$$


{}_nC_r = \dfrac{n!}{(n-r)!\,r!}.


$$

Substituting $n=12$ and $r=10,$ we get

$$


 \begin{aligned} _{12}C_{10} &= \dfrac {12!} {(12 - 10)!10!} \\\[5pt] &= \dfrac {12!} {2!10!} \\\[5pt] &= \dfrac {12 \cdot 11 \cdot 10!} {2!\cdot10!} \\\[5pt] &= \dfrac {12 \cdot 11} {2} \\\[5pt] &= 66. \end{aligned}


$$

### Example: Calculating the Number of Combinations of Objects Chosen From a Group Fewer Than Ten

#### Question

There are $10$ employees in a company, and $3$ of them are to be selected to form a committee. How many different selections are possible?

#### Explanation

The number of combinations of $n$ objects taken $r$ at a time is given by the formula

$$


{}_nC_r = \dfrac{n!}{(n-r)!r!}.


$$

There are $10$ employees, so $n=10.$ We want to select $3$ of those employees to form a committee, so we have $r=3.$

Therefore, the number of different ways to form the committee is

$$


\begin{aligned}_{𝑛}𝐶_{𝑟} & =_{10}𝐶_{3} \\ & =\frac{10!}{(10−3)!3!} \\ & =\frac{10!}{7!3!} \\ & =\frac{10⋅9⋅8⋅7!}{7!3!} \\ & =\frac{720}{6} \\ & =120.\end{aligned}


$$

### Example: Calculating the Number of Combinations of Objects Chosen From a Group of at Least Ten

#### Question

Suppose a teacher needs to select a group of $4$ students from a class of $20$ students to represent the class in a competition. How many different ways can the teacher form a team of $4$ students?

#### Explanation

The number of combinations of $n$ objects taken $r$ at a time is given by the formula

$$


{}_nC_r = \dfrac{n!}{(n-r)!r!}.


$$

There are $20$ students, so $n=20.$ We want to select $4$ of those students to form a group, so we have $r=4.$

Therefore, the number of different ways in which the teacher can form the team is

$$


\begin{aligned}_{20}𝐶_{4} & =\frac{20!}{(20−4)!4!} \\ & =\frac{20!}{16!4!} \\ & =\frac{20⋅19⋅18⋅17⋅16!}{16!4!} \\ & =\frac{116\,280}{24} \\ & =4\,845.\end{aligned}


$$
