# Negating Quantified Statements

Source: https://www.mathacademy.com/topics/2791?courseId=76
Topic ID: 2791

## Prerequisites

- [Formal and Informal Language](./2798-formal-and-informal-language.md)

## Lesson

### Introduction

In this lesson, we'll learn how to negate statements involving universal and existential quantifiers.

To negate the universally quantified statement

$$


\forall x \in U, \, P(x)


$$

we flip the quantifier to existential and negate the predicate:

$$


\neg \left( {\color{blue}\forall} x \in U, \, {\color{red}P(x)} \right) \equiv {\color{blue}\exists} x \in U, \, \neg {\color{red}P(x)}


$$

To see why it makes sense to do this, let's negate the following statement:

$\qquad$ *All integers are even.*

This statement can be re-phrased as follows:

$\qquad$ *For all* $n \in \mathbb{Z},$ $\left(2 \mid n\right).$

Introducing the universal quantifier, we get the following:

$\qquad$ $\forall n \in \mathbb{Z}, \, \left(2 \mid n \right)$

Negating this according to the above rule, we obtain

$$


\begin{aligned}¬(∀𝑛∈ℤ,\,(2∣𝑛)) & ≡∃𝑛∈ℤ,\,¬(2∣𝑛) \\ & ≡∃𝑛∈ℤ,\,(2∤𝑛).\end{aligned}


$$

This statement now reads

$\qquad$ *There exists $n \in \mathbb{Z}$ such that $n$ is not even.*

We can write this in more everyday English in the following ways:

- *There is at least one odd integer.*

- *Some integers are odd.*

This makes intuitive sense. The statement that "all integers are even" is false, and the reason it's false is that at least one integer is odd.

### Negating a Statement Involving an Existential Quantifier

To negate the existentially quantified statement

$$


\exists x \in U, \, P(x)


$$

we flip the quantifier to universal and negate the predicate:

$$


\neg \left( {\color{blue}\exists} x \in U, \, {\color{red}P(x)} \right) \equiv {\color{blue}\forall} x \in U, \, \neg {\color{red}P(x)}


$$

To see why it makes sense to do this, let's negate the following statement:

$\qquad$ *There is a real number whose square is negative.*

The given statement can be re-phrased as follows:

$\qquad$ *There exists* $x \in \mathbb{R},\, x^2 < 0.$

Introducing the existential quantifier, we get the following:

$\qquad$ $\exists x \in \mathbb{R},\, x^2 < 0.$

This statement is false, and so its negation must be true.

Negating this according to the above rule, we obtain

$$


\begin{aligned}¬(∃𝑥∈ℝ,\,𝑥^{2}<0) & ≡∀𝑥∈ℝ,\,¬(𝑥^{2}<0) \\ & ≡∀𝑥∈ℝ,\,𝑥^{2}≥0.\end{aligned}


$$

This statement now reads

$\qquad$ *For all $x \in \mathbb{R},$ $x^2\geq 0$.*

We can write this in more everyday English as follows:

$\qquad$ *The square of every real number is nonnegative*.

This makes intuitive sense. The statement "there is a real number whose square is negative" is false, and the reason it's false is that *every* real number has a nonnegative square.

### Example: Identifying the Formula For Negating a Quantified Statement

#### Question

What is the negation of the following statement?

$$


\forall y \in \overline{S}, \, \neg P(y)


$$

#### Explanation

To negate the universal statement $\forall y \in \overline{S}, \, \neg P(y),$ we flip the quantifier to existential and negate the predicate:

$$


\begin{aligned}¬(∀𝑦∈\overset{𝑆}{},\,¬𝑃(𝑦)) & ≡∃𝑦∈\overset{𝑆}{},\,¬¬𝑃(𝑦) \\ & ≡∃𝑦∈\overset{𝑆}{},\,𝑃(𝑦)\end{aligned}


$$

### Example: Negating Universal Statements

#### Question

Negate the following statement:

$\qquad$ For all $n \in \mathbb{N},$ $n$ is a composite number.

#### Explanation

If we denote

$$


𝑛


$$

our statement can be written as

$$


\forall n \in \mathbb{N}, \, P(n).


$$

Negating this, we obtain

$$


\neg \left( \forall n \in \mathbb{N}, \, P(n) \right) \equiv \exists n \in \mathbb{N}, \, \neg P(n).


$$

Finally, $\exists n \in \mathbb{N}, \, \neg P(n)$ reads as follows:

$\qquad$ **** $n \in \mathbb{N}$ such that $n$ is **** a composite number.

### Example: Negating Existential Statements

#### Question

Negate the following statement:

$\qquad$ Some quadrilaterals are squares.

#### Explanation

Let $Q$ be the set of all quadrilaterals and $S$ the set of all squares. The given statement can be re-phrased as follows:

$\qquad$ There exists $q \in Q$ such that $q \in S$

Introducing the existential quantifier, we get the following:

$\qquad$ $\exists q \in Q, \, q \in S.$

Negating this, we obtain

$$


\begin{aligned}¬(∃𝑞∈𝑄,\,𝑞∈𝑆) & ≡∀𝑞∈𝑄,\,¬(𝑞∈𝑆) \\ & ≡∀𝑞∈𝑄,\,𝑞∉𝑆\end{aligned}


$$

which reads

$\qquad$ For all $q \in Q,$ $q \not\in S.$

or simply

$\qquad$ All quadrilaterals are not squares.
