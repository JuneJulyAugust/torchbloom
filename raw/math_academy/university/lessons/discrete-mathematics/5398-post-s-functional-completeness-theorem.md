# Post's Functional Completeness Theorem

Source: https://www.mathacademy.com/topics/5398?courseId=109
Topic ID: 5398

## Prerequisites

- [Truth-Preserving Boolean Functions](./3783-truth-preserving-boolean-functions.md)
- [Self-Dual Boolean Functions](./3785-self-dual-boolean-functions.md)
- [Monotonic Boolean Functions](./3786-monotonic-boolean-functions.md)
- [Affine Boolean Functions](./3787-affine-boolean-functions.md)
- [Functionally Complete Sets](./3788-functionally-complete-sets.md)

## Lesson

### Introduction

We can determine if a set of Boolean functions is functionally complete with the following theorem.

**Post's functional completeness theorem** states that a set of Boolean functions (logical operators) is functionally complete if and only if this set contains

- at least one function that is *not* truth-preserving,

- at least one function that is *not* falsity-preserving,

- at least one function that is *not* self-dual,

- at least one function that is *not* monotonic,

- at least one function that is *not* affine.

Let's determine whether the set $\{f_1, f_2 \}$ is functionally complete, where $f_1 = \overline{x_2}$ is negation and $f_2 = x_1 \land x_2$ is conjunction given by the truth table below.

We use Post's functional completeness theorem by examining the corresponding properties of these functions in turn.

- For the function $f_1,$ we have the following: The function is not truth-preserving since $f_1(1,1) = 0.$ The function is not falsity-preserving since $f_1(0,0) = 1.$ The function is self-dual since it is negated by negating all inputs: $f_1(0,0)=1$ and $f_1(1,1)=0,$ $f_1(0,1)=0$ and $f_1(1,0)=1.$ The function is not monotonic since $(0,0) \leq (0,1)$ but $f_1(0,0) > f_1(0,1).$ The function is affine since the corresponding Boolean polynomial $f_1 \equiv \overline{x_2} \equiv 1 \oplus x_2$ does not contain conjunctions.

- For the function $f_2,$ we have the following: The function is truth-preserving since $f_2(1,1) = 1.$ The function is falsity-preserving since $f_2(0,0) = 0.$ The function is not self-dual since $f_2(0,1) = 0$ but $f_2(1,0) \neq 1.$ The function is monotonic since, for any comparable pair of binary tuples, we have The function is not affine since the corresponding Boolean polynomial $f_2(x_1,x_2) \equiv x_1x_2$ contains conjunctions.

We can summarize these properties in the table below.

The set $\{f_1, f_2 \}$ contains functions that are *not* truth-preserving, *not* falsity-preserving, *not* self-dual, *not* monotonic, and *not* affine. Therefore, the set is functionally complete.

Note that $\{f_1, f_2 \}$ is also a *minimal* functionally complete set since removing one of the functions from it makes the resulting set not functionally complete. Removing $f_1$ means the set only contains truth-preserving (or falsity-preserving, or monotonic) functions, and removing $f_2$ means the set only contains self-dual (or affine) functions.

### Example: Applying Post's Theorem

#### Question

Consider the Boolean functions $f_1,f_2,f_3$ whose properties are given in the table above. Which of the following statements are true?

1. $\{f_1,f_2,f_3 \}$ is a functionally complete set

2. $\{f_2,f_3 \}$ is a functionally complete set

3. $\{f_1,f_2,f_3 \}$ is a minimal functionally complete set

#### Explanation

Recall that according to Post's functional completeness theorem, a set of Boolean functions (logical operators) is functionally complete if and only if this set contains

- at least one function that is ** truth-preserving,

- at least one function that is ** falsity-preserving,

- at least one function that is ** self-dual,

- at least one function that is ** monotonic,

- at least one function that is ** affine.

A minimal functionally complete set is a functionally complete set such that removing any of the functions from it makes the resulting set not functionally complete.

With that in mind, let's examine our statements.

- Statement I is true. The set $\{f_1,f_2,f_3 \}$ is functionally complete since it contains a function that is not truth-preserving (for example, $f_1$), a function that is not falsity-preserving (for example, $f_2$), a function that is not self-dual (for example, $f_3$), a function that is not monotonic (for example, $f_2$), a function that is not affine (for example, $f_1$).

- Statement II is false since both $f_2$ and $f_3$ are affine.

- Statement III is false. If we remove the function $f_3$ from $\{f_1,f_2,f_3 \},$ the resulting set $\{f_1,f_2 \}$ still remains functionally complete according to Post's theorem.

Therefore, the correct answer is "I only."

### Example: Classifying Boolean Functions

#### Question

Fill in (choosing "Yes" or "No") the table below summarizing the properties of the Boolean function $\Rightarrow$ (implication).

#### Explanation

The truth table for $f(x_1,x_2) = x_1 \Rightarrow x_2$ is the following:

With that in mind, let's examine the corresponding properties of the function.

- The function is truth-preserving since $f(1,1) = 1.$

- The function is not falsity-preserving since $f(0,0) \neq 0.$

- The function is not self-dual since $f(0,0) = 1$ but $f(1,1) \neq 0.$

- The function is not monotonic since $(0,0) \leq (1,0)$ but $f(0,0) > f(1,0).$

- The function is not affine since the corresponding Boolean polynomial contains a conjuction.

Therefore, we obtain the following table:

### Example: Applying Post's Theorem for Functions of Two Variables

#### Question

Select the correct options in the table below and complete the reasoning about the set of Boolean functions.

The set $\{f_1, f_2 \}$ $\boxed{\phantom{XX}}$ functionally complete.

#### Explanation

The truth table for these functions is the following:

With that in mind, let's examine the corresponding properties of these functions.

- Function $f_1{:}$ The function is truth-preserving since $f_1(1,1) = 1.$ The function is ** falsity-preserving since $f_1(0,0) \neq 0.$ The function is ** self-dual since $f_1(0,0) = 1$ but $f_1(1,1) \neq 0.$ The function is not monotonic since $(0,0) \leq (0,1)$ but $f_1(0,0) > f_1(0,1).$ The function is not affine since the corresponding Boolean polynomial contains a conjunction.

- Function $f_2{:}$ The function is truth-preserving since $f_2(1,1) =1.$ The function is not falsity-preserving since $f_2(0,0) \neq 0.$ The function is not self-dual since $f_2(0,1) = 1$ but $f_2(1,0) \neq 0.$ The function is monotonic since, for any comparable pair of binary tuples, we have The function is affine since the corresponding Boolean polynomial $f_2(x_1,x_2) \equiv 1$ does not contain conjunctions.

We can summarize these properties in the table below.

Recall that according to Post's functional completeness theorem, a set of Boolean functions (logical operators) is functionally complete if and only if this set contains at least one function that is ** truth-preserving, ** falsity-preserving, ** self-dual, ** monotonic, and ** affine.

In our set, both $f_1$ and $f_2$ are truth-preserving. Therefore, $\{f_1, f_2 \}$ $\boxed{\color{blue}\textrm{isn't}}$ functionally complete.
