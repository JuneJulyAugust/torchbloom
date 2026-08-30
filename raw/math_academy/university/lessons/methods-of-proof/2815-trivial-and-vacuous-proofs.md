# Trivial and Vacuous Proofs

Source: https://www.mathacademy.com/topics/2815?courseId=76
Topic ID: 2815

## Prerequisites

- [Splitting Rational Expressions Into Separate Terms](../../../high-school/traditional/lessons/algebra-ii/355-splitting-rational-expressions-into-separate-terms.md)
- [Formal and Informal Language](./2798-formal-and-informal-language.md)

## Lesson

### Introduction

There are two types of "obvious" proof in math. The first type is so-called **trivial** proof.

We say that an implication has a trivial proof if the consequent is always true:

$$


P \quad \Rightarrow \overbrace{{\color{blue}Q}}^{\textrm{Always true}}


$$

If $Q$ is true, it does not matter whether the antecedent $P$ is true or false.

Recall that an implication is false only when the antecedent is true while the consequent is false. This corresponds to the second row in the truth table.

So, if we know that the consequent is true (which corresponds to either the first or the third row in the table), the implication must also be true.

For example, suppose $n \in \mathbb{N}.$ Let's prove the following statement:

$\qquad$ *If $n$ is odd, then $n \geq 0.$*

First, notice that our statement can be written as the implication

$$


𝑛


$$

Since $n \in \mathbb{N},$ it is always non-negative. So, the consequent $n \geq 0$ of our implication is always true:

$$


𝑛


$$

Therefore, the statement is *trivially* true.

### Example: Completing Trivial Statements

#### Question

Let $x \in \mathbb{R}.$ Consider the following statement:

$\qquad$ If $x < 0,$ then $\_\_\_\_\_\_.$

Which of the following could be placed into the blank space above to create a statement whose proof is trivial?

1. $\pi < 3$

2. $2x+1 \in \mathbb{Z}$

3. $|x| \geq 0$

#### Explanation

We say that an implication has a ** if the consequent is always true:

$$


P \quad \Rightarrow \overbrace{{\color{blue}Q}}^{\textrm{Always true}}


$$

It does not matter whether the antecedent is true or false.

With that in mind, let's examine our consequents in turn.

- Statement I is always false. $\:{\color{red}\times}$

- Predicate II, defined for $x \in \mathbb{R},$ is ** always true. $\:{\color{red}\times}$

- Predicate III, defined for $x \in \mathbb{R},$ is always true. $\:{\color{darkgreen}\checkmark}$

Therefore, the correct answer is "III only."

### Vacuous Proofs

Another type of "obvious" proof is the so-called **vacuous** proof.

We say that an implication has *vacuous proof* if the antecedent is always *false*:

$$


\overbrace{{\color{blue}P}}^{\textrm{Always false}} \Rightarrow \quad Q


$$

If $P$ is false, then $P\Rightarrow Q$ is true: It does not matter whether the consequent is true or false.

To see why, note that an implication is false only when the antecedent is true while the consequent is false. This corresponds to the second row in the truth table.

So, if we know that the antecedent is false (which corresponds to either the third or the fourth row), the implication must be true.

For example, suppose $x \in \mathbb{R}.$ Let's prove the following statement:

$\qquad$ *If $x^2 - 2x + 3 \lt 0,$ then $2x + 7 \gt 0.$*

First, notice that our statement can be written as the implication

$$


x^2 - 2x + 3 \lt 0 \qquad\Rightarrow\qquad 2x + 7 \gt 0.


$$

Now, for each $x \in \mathbb{R},$ notice that

$$


\begin{aligned}𝑥^{2}−2𝑥+3 & =(𝑥^{2}−2𝑥+1)+2 \\ & =(𝑥−1)^{2}+2 \\ & ≥2.\end{aligned}


$$

So, the antecedent $x^2 - 2x + 3 \lt 0$ of our implication is always false:

$$


𝑥\,∈\,ℝ


$$

Therefore, the implication is *vacuously* true.

### Example: Completing Vacuous Statement

#### Question

Let $x \in \mathbb{R}.$ Consider the following statement:

$\qquad$ If $\_\_\_\_\_\_,$ then $|\tan x| < 1.$

Which of the following could be placed into the blank space above to create a statement whose proof is vacuous?

1. $\cos{\pi}= -1$

2. $(x+1)^2 \ge 3$

3. $|\sin{x}| > 1$

#### Explanation

We say that an implication has a ** if the antecedent is always false:

$$


\overbrace{{\color{blue}P}}^{\textrm{Always false}} \Rightarrow \quad Q


$$

It does not matter whether the consequent is true or false.

With that in mind, let's examine our antecedents in turn.

- Statement I is always true. $\:{\color{red}\times}$

- Predicate II, defined for $x \in \mathbb{R},$ is ** always false. $\:{\color{red}\times}$

- Predicate III, defined for $x \in \mathbb{R},$ is always false. $\:{\color{darkgreen}\checkmark}$

Therefore, the correct answer is "III only."

### Example: Proving a Trivial or Vacuous Statement

#### Question

Let $n\in\mathbb{N}.$ Prove that if $n\gt 4,$ then $n^2 + \dfrac{1}{n} > 1.$

#### Explanation

We say that an implication has a ** if the consequent is always true:

$$


P \quad \Rightarrow \overbrace{{\color{blue}Q}}^{\textrm{Always true}}


$$

It does not matter whether the antecedent is true or false.

With that in mind, we proceed as follows:

The theorem can be written as the implication

$$


n\gt 4 \qquad\Rightarrow\qquad n^2 + \dfrac{1}{n} > 1.


$$

Notice that for $n\in\mathbb{N},$ we have

$$


\begin{aligned}𝑛^{2}+\frac{1}{𝑛} & >𝑛^{2} \\ & >1.\end{aligned}


$$

So, we have the following fact:

The consequent $n^2 + \dfrac{1}{n} > 1$ of our implication is always true.

Finally, we can make the following conclusion:

Therefore, the theorem is trivially true.
