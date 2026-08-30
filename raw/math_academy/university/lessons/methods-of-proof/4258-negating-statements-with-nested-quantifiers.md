# Negating Statements With Nested Quantifiers

Source: https://www.mathacademy.com/topics/4258?courseId=76
Topic ID: 4258

## Prerequisites

- [Negating Quantified Statements](./2791-negating-quantified-statements.md)
- [Simplifying Predicate Expressions Using De Morgan's Laws](./4302-simplifying-predicate-expressions-using-de-morgan-s-laws.md)

## Lesson

### Introduction

To negate a statement with nested quantifiers, we apply the formulas for negating a quantifier several times, from left to right.

For example, let's negate the following (true) statement:

$$


\forall x \in \mathbb{N}, \, \exists y \in \mathbb{R}, \, x < y


$$

First, we negate the external quantifier $\forall{:}$

$$


\begin{aligned}¬(\,∀𝑥∈ℕ,\,∃𝑦∈ℝ,\,𝑥<𝑦\,)≡∃𝑥∈ℕ,\,¬(\,∃𝑦∈ℝ,\,𝑥<𝑦\,)\end{aligned}


$$

Next, we negate the internal quantifier $\exists{:}$

$$


\begin{aligned}∃𝑥∈ℕ,\,¬(\,∃𝑦∈ℝ,\,𝑥<𝑦\,)≡∃𝑥∈ℕ,\,∀𝑦∈ℝ,\,¬(𝑥<𝑦)\end{aligned}


$$

Finally, we negate the underlying predicate:

$$


\begin{aligned}∃𝑥∈ℕ,\,∀𝑦∈ℝ,\,¬(𝑥<𝑦)≡∃𝑥∈ℕ,\,∀𝑦∈ℝ,\,𝑥≥𝑦\end{aligned}


$$

In short, we flip all the quantifiers and negate the predicate.

### Example: Negating Statements in Symbolic Form Containing a General Predicate

#### Question

Consider the following statement:

$$


\exists x \in X, \, \exists y \in Y, \, P(x,y) \Rightarrow Q(x,y)


$$

What is the negation of this statement?

#### Explanation

First, we recall that

$$


P(x,y) \Rightarrow Q(x,y)\equiv \neg P(x,y) \lor Q(x,y).


$$

So, our statement now reads

$$


\exists x \in X, \, \exists y \in Y, \, \neg P(x,y) \lor Q(x,y).


$$

To negate this statement, we flip the quantifiers and negate the predicate:

$$


\begin{aligned}¬(\,∃𝑥∈𝑋,\,∃𝑦∈𝑌,\,¬𝑃(𝑥,𝑦)∨𝑄(𝑥,𝑦)\,) & ≡∀𝑥∈𝑋,\,∀𝑦∈𝑌,\,¬(¬𝑃(𝑥,𝑦)∨𝑄(𝑥,𝑦))\end{aligned}


$$

Finally, by applying De Morgan's law for disjunctions, we have the following:

$$


\begin{aligned}∀𝑥∈𝑋,\,∀𝑦∈𝑌,\,¬(¬𝑃(𝑥,𝑦)∨𝑄(𝑥,𝑦)) & ≡∀𝑥∈𝑋,\,∀𝑦∈𝑌,\,¬(¬𝑃(𝑥,𝑦))∧¬𝑄(𝑥,𝑦) \\ & ≡∀𝑥∈𝑋,\,∀𝑦∈𝑌,\,𝑃(𝑥,𝑦)∧¬𝑄(𝑥,𝑦)\end{aligned}


$$

### Example: Negating Statements in Symbolic Form Containing a Specific Predicate

#### Question

Consider the following statement:

$$


\forall n \in \mathbb{N}, \, \exists m \in \mathbb{N}, \, n \lt m


$$

What is the negation of this statement?

#### Explanation

To negate a quantified statement, we flip the quantifiers and negate the predicate:

$$


\begin{aligned}¬(\,∀𝑛∈ℕ,\,∃𝑚∈ℕ,\,𝑛<𝑚\,) & ≡∃𝑛∈ℕ,\,∀𝑚∈ℕ,\,¬(𝑛<𝑚) \\ & ≡∃𝑛∈ℕ,\,∀𝑚∈ℕ,\,𝑛≥𝑚\end{aligned}


$$

### Example: Negating Statements Involving Nested Quantifiers

#### Question

Negate the following quantified statement:

$\qquad$ There exists a natural number $n$ such that $x^n \geq 0$ for any real number $x.$

#### Explanation

The given statement can be re-phrased as follows:

$\qquad$ There exists $n \in \mathbb{N}$ such that, for all $x \in \mathbb{R},$ $x^n \geq 0.$

Writing this symbolically, we have:

$\qquad$ $\exists n \in \mathbb{N}, \, \forall x \in \mathbb{R}, \, x^n \geq 0$

To negate a quantified statement, we flip the quantifiers and negate the predicate:

$$


\begin{aligned}¬(\,∃𝑛∈ℕ,\,∀𝑥∈ℝ,\,𝑥^{𝑛}≥0\,) & ≡∀𝑛∈ℕ,\,∃𝑥∈ℝ,\,¬(𝑥^{𝑛}≥0) \\ & ≡∀𝑛∈ℕ,\,∃𝑥∈ℝ,\,𝑥^{𝑛}<0\end{aligned}


$$

which reads

$\qquad$ For all $n \in \mathbb{N}$ there exists $x \in \mathbb{R}$ such that $x^n \lt 0,$

or simply

$\qquad$ For any natural number $n$ there exists a real number $x$ such that $x^n \lt 0.$
