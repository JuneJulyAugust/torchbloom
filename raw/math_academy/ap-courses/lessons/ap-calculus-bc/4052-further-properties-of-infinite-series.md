# Further Properties of Infinite Series

Source: https://www.mathacademy.com/topics/4052?courseId=21
Topic ID: 4052

## Prerequisites

- [Properties of Infinite Series](./983-properties-of-infinite-series.md)

## Lesson

### Introduction

In this lesson, we'll discuss some more properties of infinite series.

The first property we'll discuss is the following:

*If $\displaystyle\sum_{n=1}^\infty a_n$ is convergent, then $\displaystyle \sum_{n=k}^\infty a_n$ is also convergent.*

This statement tells us that if we remove the first $k-1$ terms from a convergent series, the resulting series is also convergent.

We have a similar result for divergent series:

*If $\displaystyle\sum_{n=1}^\infty a_n$ is divergent, then $\displaystyle\sum_{n=k}^\infty a_n$ is also divergent.*

This statement tells us that if we remove the first $k-1$ terms from a divergent series, the resulting series is also divergent.

### Example: Removing a Finite Number of Terms From a Convergent Series

#### Question

Given that $\displaystyle \sum_{n=1}^\infty a_n$ is convergent, what can be said about the convergence behavior of the series $\displaystyle \sum_{n=150}^\infty a_n?$

#### Explanation

Removing the first $k-1$ terms from a convergent series results in a convergent series.

More precisely, assume that $k\geq 1$ is an integer. Then, we have the following:

**

Therefore, $\displaystyle \sum_{n=150}^\infty a_n$ is convergent.

### Example: Removing a Finite Number of Terms From a Divergent Series

#### Question

Given that $\displaystyle \sum_{n=1}^\infty a_n$ is divergent, what can be said about the convergence of $\displaystyle \sum_{n=15}^\infty a_n?$ Assume that $a_n$ is well-defined for $n\geq 1.$

#### Explanation

Removing the first $k-1$ terms from a divergent series results in a divergent series.

More precisely, assume $a_n$ is well-defined for $n\geq 1$ and $k\geq 1$ is an integer. Then, we have the following:

**

So, since $\displaystyle \sum_{n=1}^\infty a_n$ is divergent, we have that $\displaystyle \sum_{n=15}^\infty a_n$ is also divergent.

### Sums of Convergent and Divergent Series

Let's now discuss properties related to sums of convergent and divergent series.

- The first property states that the sum of two convergent series is always convergent: *If $\displaystyle\sum_{n=1}^\infty a_n$ is convergent and $\displaystyle\sum_{n=1}^\infty b_n$ is convergent, then $\displaystyle\sum_{n=1}^\infty a_n + \sum_{n=1}^\infty b_n$ is convergent.* This makes intuitive sense. If $\displaystyle\sum_{n=1}^\infty a_n$ and $\displaystyle\sum_{n=1}^\infty b_n$ are both finite numbers, then their sum should also be finite.

- The second property states that the sum of a divergent series and a convergent series is always divergent: *If $\displaystyle\sum_{n=1}^\infty a_n$ is divergent and $\displaystyle\sum_{n=1}^\infty b_n$ is convergent, then $\displaystyle\sum_{n=1}^\infty a_n + \sum_{n=1}^\infty b_n$ is divergent.* Again, this makes intuitive sense. If $\displaystyle\sum_{n=1}^\infty a_n$ is infinite (or undefined), then adding a finite number to this results in an infinite (or undefined) quantity.

Summing two divergent series is a complicated business. We'll save this for future lessons.

Finally, let's recall the following properties:

*If $\displaystyle\sum_{n=1}^\infty a_n$ is convergent, then $\displaystyle \sum_{n=1}^\infty K\cdot a_n = K\cdot \sum_{n=1}^\infty a_n$ is convergent for any real number $K.$*

*If $\displaystyle\sum_{n=1}^\infty a_n$ is divergent, then $\displaystyle \sum_{n=1}^\infty K\cdot a_n$ is divergent for any real number $K\neq 0.$*

### Example: Analyzing Statements Involving Sums of Convergent Series

#### Question

Given that $\displaystyle \sum_{n=1}^\infty a_n$ is convergent and $\displaystyle \sum_{n=1}^\infty b_n$ is convergent, which of the following statements are true?

1. $\displaystyle \sum_{n=1}^\infty a_n+\sum_{n=1}^{\infty} b_n$ is convergent

2. $\displaystyle 4 \cdot \sum_{n=1}^\infty a_n$ is convergent

3. $\displaystyle \sum_{n=10}^\infty b_n$ is convergent

#### Explanation

Let's recall the properties of convergent series:

- If $\displaystyle\sum_{n=1}^\infty a_n$ is convergent, then $\displaystyle \sum_{n=1}^\infty K\cdot a_n = K\cdot \sum_{n=1}^\infty a_n$ is also convergent.

- If $\displaystyle\sum_{n=1}^\infty a_n$ is convergent and $\displaystyle\sum_{n=1}^\infty b_n$ is convergent, then $\displaystyle\sum_{n=1}^\infty a_n + \sum_{n=1}^\infty b_n$ is convergent.

- If $\displaystyle\sum_{n=1}^\infty a_n$ is convergent, then $\displaystyle \sum_{n=k}^\infty a_n$ is also convergent.

With that in mind, let's analyze each statement:

- Statement I is true. The sum of two convergent series is convergent.

- Statement II is true. Any constant multiple of a convergent series gives a convergent series.

- Statement III is true. Removing a finite number of terms from a convergent series gives a convergent series.

Therefore, the correct answer is "I, II, III."

### Example: Analyzing Statements Involving Sums of Convergent and Divergent Series

#### Question

Given that $\displaystyle \sum_{n=1}^\infty a_n$ is convergent and $\displaystyle \sum_{n=1}^\infty b_n$ is divergent, which of the following statements are true? Assume that $b_n$ is well-defined for $n\geqslant 1.$

1. $\displaystyle \sum_{n=9}^\infty a_n$ is convergent

2. $\displaystyle \dfrac{1}{10^{100}} \cdot \sum_{n=1}^\infty b_n$ is convergent

3. $\displaystyle \sum_{n=1}^\infty a_n + \sum_{n=1}^{40} b_n$ is convergent

#### Explanation

Let's recall the properties of divergent series:

- If $\displaystyle\sum_{n=1}^\infty a_n$ is divergent, then $\displaystyle \sum_{n=1}^\infty K\cdot a_n$ is also divergent for $K\neq 0.$

- If $\displaystyle\sum_{n=1}^\infty a_n$ is convergent and $\displaystyle\sum_{n=1}^\infty b_n$ is divergent, then $\displaystyle\sum_{n=1}^\infty a_n + \sum_{n=1}^\infty b_n$ is divergent.

- If $\displaystyle\sum_{n=1}^\infty a_n$ is divergent, then $\displaystyle \sum_{n=k}^\infty a_n$ is also divergent.

With that in mind, let's analyze each statement:

- Statement I is true. Removing a finite number of terms from a convergent series gives a convergent series.

- Statement II is false. Any non-zero multiple of a divergent series gives a divergent series.

- Statement III is true. Note that $\displaystyle \sum_{n=1}^{40} b_n$ is a ****. Therefore, $\displaystyle \sum_{n=1}^\infty a_n + \sum_{n=1}^{40} b_n$ is convergent.

Therefore, the correct answer is "I and III only."

### Summary

Let's summarize by restating some properties of convergent series.

- If $\displaystyle\sum_{n=1}^\infty a_n$ is convergent, then $\displaystyle K\cdot \sum_{n=1}^\infty a_n$ is convergent for any number $K.$

- If $\displaystyle\sum_{n=1}^\infty a_n$ is convergent and $\displaystyle\sum_{n=1}^\infty b_n$ is convergent, then $\displaystyle\sum_{n=1}^\infty a_n + \sum_{n=1}^\infty b_n$ is convergent.

- If $\displaystyle\sum_{n=1}^\infty a_n$ is convergent, then $\displaystyle \sum_{n=k}^\infty a_n$ is also convergent for $k\geq 1.$

We also have the following properties relating to divergent series:

- If $\displaystyle\sum_{n=1}^\infty a_n$ is divergent, then $\displaystyle \sum_{n=1}^\infty K\cdot a_n$ is divergent for any number $K\neq 0.$

- If $\displaystyle\sum_{n=1}^\infty a_n$ is divergent and $\displaystyle\sum_{n=1}^\infty b_n$ is convergent, then $\displaystyle\sum_{n=1}^\infty a_n + \sum_{n=1}^\infty b_n$ is divergent.

- If $\displaystyle\sum_{n=1}^\infty a_n$ is divergent, then $\displaystyle\sum_{n=k}^\infty a_n$ is also divergent.
