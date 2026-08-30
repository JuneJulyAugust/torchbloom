# Disproving Implications

Source: https://www.mathacademy.com/topics/4927?courseId=76
Topic ID: 4927

## Prerequisites

- [The Division Properties of Modular Arithmetic](./2675-the-division-properties-of-modular-arithmetic.md)
- [Disproving Universal Statements](./3412-disproving-universal-statements.md)

## Lesson

### Introduction

In this lesson, we'll learn how to disprove conditional statements.

Suppose we wish to disprove a conditional statement of the following form:

$$


\forall x \in \mathbb{Z}, \: P(x) \Rightarrow Q(x)


$$

To disprove this statement, we must show its negation is true.

The negation of our statement is

$$


\begin{aligned}¬(∀𝑥∈ℤ,\,𝑃⇒𝑄) & ≡\,∃𝑥∈ℤ,\,¬(𝑃⇒𝑄) \\ & ≡\,∃𝑥∈ℤ,\,¬(¬𝑃∨𝑄) \\ & ≡\,∃𝑥∈ℤ,\,𝑃∧¬𝑄.\end{aligned}


$$

Therefore, to disprove the implication $P\Rightarrow Q,$ it's sufficient to find one value of the variable such that $P$ and $\lnot Q$ are both true. This value of $x$ is a *counterexample* that disproves the original implication.

Let's see an example.

### Disproving a Divisibility Statement

Suppose we wish to disprove the following statement:

*For any $a \in \mathbb{Z},$ if $2 \mid a,$ then $4 \mid a$*

By denoting the predicates $P$ and $Q$ as

- $P(a){:} \quad 2 \mid a$

- $Q(a){:} \quad 4 \mid a$

our statement can be written as

$$


\forall a \in \mathbb{Z}, \: P \Rightarrow Q.


$$

We can disprove this statement by finding a counterexample. In other words, we need to find a value of $a$ such that its negation is true.

The negation of our statement is

$$


\begin{aligned}¬(∀𝑎∈ℤ,\,𝑃⇒𝑄) & ≡\,∃𝑎∈ℤ,\,¬(𝑃⇒𝑄) \\ & ≡\,∃𝑎∈ℤ,\,¬(¬𝑃∨𝑄) \\ & ≡\,∃𝑎∈ℤ,\,𝑃∧¬𝑄 \\ & ≡\,∃𝑎∈ℤ,\,(2∣𝑎)\,∧\,(4∤𝑎)\end{aligned}


$$

So, we begin as follows:

*To disprove a universal statement, it's sufficient to find a counterexample. In other words, we need to show that there exists an integer $a$ such that*

$$


2 \mid a \qquad\textrm{and}\qquad 4 \not\mid a.


$$

Finding a counterexample is sometimes a nontrivial task, but we only need one. In this case, substituting $a=2$ suffices.

*Let's choose $a = 2.$ Then, we have that*

$$


2 \mid 2 \qquad\textrm{and}\qquad 4 \not\mid 2.


$$

Finally, we state our conclusion:

*So, $a=2$ is our counterexample. Therefore, the given statement is false.*

Now that we've figured out the details, let's write down the full argument.

### Stating the Full Counterexample

Disprove the following statement:

*For any $a \in \mathbb{Z},$ if $2 \mid a,$ then $4 \mid a.$*

Counterexample:

*To disprove a universal statement, it's sufficient to find a counterexample. In other words, we need to show that there exists an integer $a$ such that*

$$


2 \mid a \qquad\textrm{and}\qquad 4 \not\mid a.


$$

*Let's choose $a = 2.$ Then, we have that*

$$


2 \mid 2 \qquad\textrm{and}\qquad 4 \not\mid 2.


$$

*So, $a=2$ is our counterexample. Therefore, the given statement is false.*

### Example: Stating Counterexample Conditions

#### Question

Consider the following false statement.

If $2a \equiv 2b \: (\textrm{mod}\:4),$ then $a \equiv b \: (\textrm{mod}\:4)$ for any $a,b \in \mathbb{Z}.$

A counterexample for the above statement would be a pair of integers $a$ and $b$ such that

$$


\boxed{\phantom{RRR} }\, (\textrm{mod}\:4) \qquad\textrm{and}\qquad \boxed{\phantom{RRR} }\, (\textrm{mod}\:4).


$$

Find the missing expressions.

#### Explanation

By denoting $P(a)$ and $Q(a)$ as

- $P(a,b){:} \quad 2a \equiv 2b \: (\textrm{mod}\:4)$

- $Q(a,b){:} \quad a \equiv b \: (\textrm{mod}\:4)$

our statement can be written as

$$


\forall a,b \in \mathbb{Z}, \: P \Rightarrow Q.


$$

Since this statement is false, its negation is true.

A ** is a particular case that disproves the statement. Equivalently, it's a case that proves the negation is true.

The negation of our statement is

$$


\begin{aligned}¬(∀𝑎,𝑏∈ℤ,\,𝑃⇒𝑄) & ≡\,∃𝑎,𝑏∈ℤ,\,¬(𝑃⇒𝑄) \\ & ≡\,∃𝑎,𝑏∈ℤ,\,¬(¬𝑃∨𝑄) \\ & ≡\,∃𝑎,𝑏∈ℤ,\,𝑃∧¬𝑄 \\ & ≡\,∃𝑎,𝑏∈ℤ,\,(2𝑎≡2𝑏\,(mod\,4))\,∧\,(𝑎≢𝑏\,(mod\,4)).\end{aligned}


$$

Therefore, we have the following:

A counterexample for the above statement would be a pair of integers $a$ and $b$ such that

$$


\boxed{\color{blue}2a \equiv 2b} \: (\textrm{mod}\:4) \qquad\textrm{and}\qquad \boxed{\color{blue}a \not\equiv b} \: (\textrm{mod}\:4).


$$

### Example: Disproving Divisibility Statements

#### Question

Disprove the following statement:

For any $a \in \mathbb{Z},$ if $4 \mid a$ and $6 \mid a,$ then $24 \mid a.$

#### Explanation

By denoting $P(a),$ $Q(a),$ and $R(a)$ as

- $P(a){:} \quad 4 \mid a$

- $Q(a){:} \quad 6 \mid a$

- $R(a){:} \quad 24 \mid a$

our statement can be written as

$$


\forall a \in \mathbb{Z}, \:(P \land Q) \Rightarrow R.


$$

We want to disprove this statement. In other words, we must show that its negation is true:

$$


\begin{aligned}¬(∀𝑎∈ℤ,\,(𝑃∧𝑄)⇒𝑅) & ≡\,∃𝑎∈ℤ,\,¬((𝑃∧𝑄)⇒𝑅) \\ & ≡\,∃𝑎∈ℤ,\,¬(¬(𝑃∧𝑄)∨𝑅) \\ & ≡\,∃𝑎∈ℤ,\,(𝑃∧𝑄)∧¬𝑅 \\ & ≡\,∃𝑎∈ℤ,\,𝑃∧𝑄∧¬𝑅 \\ & ≡\,∃𝑎∈ℤ,\,(4∣𝑎)\,∧\,(6∣𝑎)\,∧\,(24∤𝑎)\end{aligned}


$$

So, we begin as follows:

To disprove a universal statement, it's sufficient to find a counterexample. In other words, we need to show that there exists an integer $a$ such that

$$


4 \mid a \qquad\textrm{and}\qquad 6 \mid a \qquad\textrm{and}\qquad 24 \not\mid a.


$$

Finding a counterexample is sometimes a nontrivial task, but we only need one. In this case, substituting $a=12$ suffices.

Let's choose $a =12.$ Then, we have that

$$


4 \mid 12 \qquad\textrm{and}\qquad 6 \mid 12 \qquad\textrm{and}\qquad 24 \not\mid 12.


$$

Finally, we state our conclusion:

So, $a=12$ is our counterexample. Therefore, the given statement is false.

### Example: Disproving Congruences

#### Question

Disprove the following statement:

For any $a,b \in \mathbb{Z},$ if $3a \equiv 3b \: (\textrm{mod}\:6),$ then $a \equiv b \: (\textrm{mod}\:6).$

#### Explanation

By denoting $P(a,b)$ and $Q(a,b)$ as

- $P(a,b){:} \quad 3a \equiv 3b \: (\textrm{mod}\:6)$

- $Q(a,b){:} \quad a \equiv b \: (\textrm{mod}\:6)$

our statement can be written as

$$


\forall a,b \in \mathbb{Z}, \: P \Rightarrow Q.


$$

We want to disprove this statement. In other words, we must show that its negation is true:

$$


\begin{aligned}¬(∀𝑎,𝑏∈ℤ,\,𝑃⇒𝑄) & ≡\,∃𝑎,𝑏∈ℤ,\,¬(𝑃⇒𝑄) \\ & ≡\,∃𝑎,𝑏∈ℤ,\,¬(¬𝑃∨𝑄) \\ & ≡\,∃𝑎,𝑏∈ℤ,\,𝑃∧¬𝑄 \\ & ≡\,∃𝑎,𝑏∈ℤ,\,(3𝑎≡3𝑏\,(mod\,6))\,∧\,(𝑎≢𝑏\,(mod\,6))\end{aligned}


$$

So, we begin as follows:

To disprove a universal statement, it's sufficient to find a counterexample. In other words, we need to show that there exist integers $a$ and $b$ such that

$$


3a \equiv 3b \: (\textrm{mod}\:6) \qquad\textrm{and}\qquad a \not\equiv b\: (\textrm{mod}\:6).


$$

Finding a counterexample is sometimes a nontrivial task, but we only need one. In this case, substituting $(a,b) =(0,2)$ suffices.

Let's choose

$$


a = 0, \qquad b = 2.


$$

Then, $3a=0$ and $3b=6.$

To check that this is a required counterexample, we proceed as follows:

Hence, we have that

$$


\underbrace{0}_{3a} \equiv \underbrace{6}_{3b} \: (\textrm{mod}\:6) \qquad\textrm{and}\qquad \underbrace{0}_{a} \not\equiv \underbrace{2}_{b} \: (\textrm{mod}\:6).


$$

Finally, we state our conclusion:

So, the pair $a=0$ and $b=2$ is our counterexample. Therefore, the given statement is false.
