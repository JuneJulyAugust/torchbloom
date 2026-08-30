# Conditional Statements

Source: https://www.mathacademy.com/topics/250?courseId=145
Topic ID: 250

## Prerequisites

- [Logical Equivalence](./2821-logical-equivalence.md)

## Lesson

### Introduction

A **conditional statement** (or **implication**) is a mathematical statement that takes the form

$\qquad$ *$P$ implies $Q,$*

or equivalently,

$\qquad$ *if $P,$ then $Q.$*

Symbolically, it can be written as $P \Rightarrow Q,$ where $P$ is called the **antecedent** (or **hypothesis**) and $Q$ is called the **consequent** (or **conclusion**).

The truth table for $P \Rightarrow Q$ is shown below.

Intuitively, an implication can be viewed as a "promise" that whenever $P$ is true, $Q$ is also true. The implication is true unless the promise is broken, i.e., $P$ is true, and $Q$ is false.

We'll discuss the intuition behind implications in more detail later in the lesson.

### Example: Identifying Truth Values of Implications

#### Question

If $A$ is true, then $A \Rightarrow B$ is $\boxed{\phantom{0}}.$

Which of the following could fill in the blank space above to make a true statement?

1. always true

2. always false

3. sometimes false

#### Explanation

The statement $A \Rightarrow B$ is true ** $A$ is true and $B$ is false.

Let's break this down into cases:

- When $A = \textrm T$ and $B = \textrm T,$ we have

- When $A = \textrm T$ and $B = \textrm F,$ we have

Therefore, if $A$ is true, then $A \Rightarrow B$ is $\boxed{\color{blue}\text{sometimes false}}.$

The complete truth table for $A\Rightarrow B$ is shown below:

Therefore, the correct answer is "III only."

### Example: Completing a Truth Table With Compound Statements

#### Question

What are the missing values in the following truth table?

#### Explanation

First, we add columns for $\neg A$ and $A \land B{:}$

Now, we add a column for $\neg A \Rightarrow (A \land B).$ This statement is true unless $\neg A$ is true and $A \land B$ is false.

### Intuition Behind the Implication Truth Table

Let's recall the truth table for $P\Rightarrow Q.$

We consider a concrete example to build further intuition behind the truth values in this table.

Suppose your teacher promises that *if* you score at least $90$ on the exam, *then* you will receive an A. In other words, the teacher has promised that a score of at least $90$ on the exam implies that you will receive an A:

$$


90


$$

Now, the teacher may or may not be lying. The implication is true if the teacher tells the truth and false if the teacher lies.

The following four situations are possible:

1. You score $90$ and receive an A. In this case, the teacher has told the truth. They have kept the promise. $\quad \color{green}\checkmark$

2. You score $90$ and do *not* receive an A. In this case, the teacher has lied. They have broken the promise. $\quad \color{red}\times$

3. You do *not* score $90,$ yet you receive an A. In this case, the teacher has told the truth! The promise does not apply because you did not score at least $90.$ $\quad \color{green}\checkmark$

4. You do *not* score $90$ and do *not* receive an A. Again, the teacher has told the truth. The promise does not apply because you did not score at least $90.$ $\quad \color{green}\checkmark$

Each of these situations corresponds to a row in the following truth table:

### Example: Identifying True Conditional Statements

#### Question

Which of the following statements are true?

1. **** $2$ is an even number, **** $3$ is an odd number.

2. **** $2$ is an even number, **** $3$ is an even number.

3. **** $2$ is an odd number, **** $3$ is an odd number.

#### Explanation

An implication $A \Rightarrow B$ is true ** $A$ is true and $B$ is false. In other words, the implication is true unless the "promise" is broken.

- Statement I is true. The antecedent "$2$ is an even number" is true, and the consequent "$3$ is an odd number" is true. So the promise is kept, and the statement is true.

- Statement II is false. The antecedent "$2$ is an even number" is true, and the consequent "$3$ is an even number" is false. So the promise is broken, and the statement is false.

- Statement III is true. The antecedent "$2$ is an odd number" is false, so the promise does not apply. Regardless of the consequent, the promise is ** broken, and the statement is true.

Therefore, the correct answer is "I and III only."
