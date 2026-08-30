# Identifying Monotonic Sequences Using Ratios

Source: https://www.mathacademy.com/topics/3861?courseId=106
Topic ID: 3861

## Prerequisites

- [Fractions of Fractions](../grade-7/323-fractions-of-fractions.md)
- [Monotonic Sequences](./1096-monotonic-sequences.md)
- [The Power of Quotient Rule With Algebraic Expressions](../algebra-i/1428-the-power-of-quotient-rule-with-algebraic-expressions.md)
- [Factorials in Variable Expressions](../geometry/3710-factorials-in-variable-expressions.md)

## Lesson

### Introduction

There are several ways to check whether a sequence is increasing or decreasing. One way is to consider the ratio between two successive terms.

- A sequence $a_n$ is *increasing* if every term is greater than or equal to the previous term. That is, for all $n\geq 1,$ we have If $a_n$ is positive for all $n,$ we can divide the above inequality by $a_n,$ which gives

- Similarly, if a sequence $a_n$ is *decreasing* if every term is less than or equal to the previous term. That is, for all $n\geq 1,$ we have If $a_n$ is positive for all $n,$ we can divide the above inequality by $a_n,$ which gives

Let's now formulate our findings into a single test.

### Testing Whether a Sequence Is Monotonic

Suppose $a_n$ is a positive sequence defined for $n \geq 1,$ and that the positive real number $L$ is defined as

$$


L = \dfrac{a_{n+1}}{a_n}.


$$

Then,

- if $L \geq 1$ for all $n \geq 1,$ then $a_n$ is *increasing,* and

- if $0 < L \leq 1$ for all $n \geq1,$ then $a_n$ is *decreasing.*

Let's take a look at some examples of how to apply this test.

### Example: Identifying Monotonic Polynomial and Rational Sequences

#### Question

Given that $a_n = \dfrac{3}{2n^2}$ for $n\geq 1,$ which of the following statements are true?

1. $\dfrac{a_{n+1}}{a_n} \leq 1$ for all $n \geq 1$

2. $a_n$ is an increasing sequence

3. $a_n$ is a decreasing sequence

#### Explanation

Suppose $a_n$ is a positive sequence defined for $n \geq 1,$ and that

$$


L = \dfrac{a_{n+1}}{a_n}.


$$

Then,

- if $L \geq 1$ for all $n \geq 1,$ then $a_n$ is ** and

- if $0 < L \leq 1$ for all $n \geq1,$ then $a_n$ is **

Notice that, in this case, $a_n = \dfrac{3}{2n^2}$ is positive for all $n \geq 1.$

With that in mind, let's analyze each statement.

- Statement I is true. Computing the ratio $L,$ we get Now, since $n \geq 1,$ it follows that since the numerator is always smaller than the denominator. Therefore Since the sequence is positive for all $n,$ we can conclude that

- Statement II is false, whereas statement III is true. Since $0\lt L \leq 1$ for all $n\geq 1,$ we can conclude that the sequence $a_n$ is decreasing.

Therefore, the correct answer is "I and III only."

### Example: Identifying Monotonic Geometric Sequences

#### Question

Given that $a_n = 3^{n}$ for $n\geq 1,$ which of the following statements are true?

1. $\dfrac{a_{n+1}}{a_n} \leq 1$ for all $n\geq 1$

2. $a_n$ is an increasing sequence

3. $a_n$ is a decreasing sequence

#### Explanation

Suppose $a_n$ is a positive sequence defined for $n \geq 1,$ and that

$$


L = \dfrac{a_{n+1}}{a_n}.


$$

Then,

- if $L \geq 1$ for all $n \geq 1,$ then $a_n$ is ** and

- if $0 < L \leq 1$ for all $n \geq 1,$ then $a_n$ is **

Notice that, in this case, $a_n = 3^{n}$ is positive for all $n \geq 1.$

With that in mind, let's analyze each statement.

- Statement I is false. Computing the ratio $L,$ we get

- Statement II is true, whereas statement III is false. Since $L \geq 1$ for all $n \geq 1,$ we can conclude that the sequence $a_n$ is increasing.

Therefore, the correct answer is "II only."

### Example: Identifying Monotonic Sequences Containing Factorials

#### Question

Given that $a_n = \dfrac{6^n}{(n+4)!}$ for $n\geq 1,$ which of the following statements are true?

1. $\dfrac{a_{n+1}}{a_n} \leq 1$ for all $n\geq 1$

2. $a_n$ is an increasing sequence

3. $a_n$ is a decreasing sequence

#### Explanation

Suppose $a_n$ is a positive sequence defined for $n\geq 1,$ and that

$$


L = \dfrac{a_{n+1}}{a_n}.


$$

Then,

- if $L \geq 1$ for all $n \geq 1,$ then $a_n$ is ** and

- if $0 < L \leq 1$ for all $n \geq1,$ then $a_n$ is **

Notice that, in this case, $a_n = \dfrac{6^n}{(n+4)!}$ is positive for all $n\geq 1.$

With that in mind, let's analyze each statement.

- Statement I is true. Computing the ratio $L,$ we get

- Statement II is false, whereas statement III is true. Since $0\lt L\leq 1$ for all $n\geq 1,$ we can conclude that the sequence $a_n$ is decreasing.

Therefore, the correct answer is "I and III only."
