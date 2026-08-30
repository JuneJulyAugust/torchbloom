# Disproving Universal Statements

Source: https://www.mathacademy.com/topics/3412?courseId=76
Topic ID: 3412

## Prerequisites

- [Negating Quantified Statements](./2791-negating-quantified-statements.md)
- [Parity](./3411-parity.md)

## Lesson

### Introduction

To **disprove** a statement means to show that it is false. In this lesson, we will learn how to disprove universal statements.

Suppose we wish to disprove a universal statement of the form

$$


\forall x \in U, \: P(x),


$$

where $U$ is some universal set. To do that, we must demonstrate that the statement's negation is true.

The negation of this statement is

$$


\neg \big( \forall x \in U, \: P(x) \big) \: \equiv \: \exists x \in U, \: \lnot P(x).


$$

Therefore, to disprove a universal statement, finding one value of the variable that makes the negation true is sufficient. This value is called a **counterexample** to the original statement.

### Disproving a Statement About Parity

For example, suppose we wish to disprove the following statement:

$5n-1$ is odd for any $n \in \mathbb{Z}.$

Our statement can be written using formal notation as follows:

$$


5𝑛−1


$$

We want to disprove this statement. In other words, we must show that its negation is true:

$$


5𝑛−1


$$

So, we begin as follows:

*To disprove a universal statement, it's sufficient to find a counterexample. In other words, we need to show that there exists an integer $n$ such that $5n-1$ is even.*

Finding a counterexample is sometimes a nontrivial task, but we only need one. In this case, substituting $n=1$ suffices:

*Notice that by substituting $n=1$ into the expression, we obtain*

$$


\begin{aligned}5𝑛−1 & =5(1)−1 \\ & =4\end{aligned}


$$

*which is even.*

Finally, we state our conclusion:

*So, $n=1$ is our counterexample. Therefore, the given statement is false.*

Now that we've figured out the details, let's write down the full argument.

### Stating the Full Counterexample

Disprove the following statement:

*$5n-1$ is odd for any $n \in \mathbb{Z}.$*

Counterexample:

*To disprove a universal statement, it's sufficient to find a counterexample. In other words, we need to show that there exists an integer $n$ such that $5n-1$ is even.*

*Notice that by substituting $n=1$ into the expression, we obtain*

$$


\begin{aligned}5𝑛−1 & =5(1)−1 \\ & =4\end{aligned}


$$

*which is even.*

*So, $n=1$ is our counterexample. Therefore, the given statement is false.*

### Example: Stating Counterexample Conditions

#### Question

What would be a counterexample for the following false statement?

$7n-2$ is even for any $n \in \mathbb{Z}$

#### Explanation

Our statement can be written as

$$


7𝑛−2


$$

Since this statement is false, its negation is true.

A ** is a particular case that disproves the statement. Equivalently, it's a case that proves the negation is true.

The negation of our statement is

$$


7𝑛−2


$$

Therefore, we have the following:

A counterexample for the above statement would be an integer $n$ such that $7n-2$ is odd.

### Example: Disproving Parity and Divisibility Statements

#### Question

Disprove the following statement:

$2 \mid n^2-3$ for any $n \in \mathbb{Z}.$

#### Explanation

Our statement can be written as

$$


\forall n \in \mathbb{Z}, \: 2 \mid n^2-3.


$$

We want to disprove this statement. In other words, we must show that its negation is true:

$$


\neg \big( \forall n \in \mathbb{Z}, \: 2 \mid n^2-3\big) \: \equiv \: \exists n \in \mathbb{Z}, \: 2 \not\mid n^2-3


$$

So, we begin as follows:

To disprove a universal statement, it's sufficient to find a counterexample. In other words, we need to show that there exists an integer $n$ such that

$$


2 \not\mid n^2-3.


$$

Finding a counterexample is sometimes a nontrivial task, but we only need one. In this case, substituting $n=0$ suffices:

Notice that by substituting $n=0$ into the expression, we obtain

$$


\begin{aligned}𝑛^{2}−3 & =(0)^{2}−3 \\ & =−3\end{aligned}


$$

which is not divisible by $2.$

Finally, we state our conclusion:

So, $n=0$ is our counterexample. Therefore, the given statement is false.

### Example: Disproving Inequalities

#### Question

Disprove the following statement:

$3q^2-2 \gt 0$ for any $q \in \mathbb{Q}.$

#### Explanation

Our statement can be written as

$$


\forall q \in \mathbb{Q}, \: 3q^2-2 \gt 0.


$$

We want to disprove this statement. In other words, we must show that its negation is true:

$$


\neg \big( \forall q \in \mathbb{Q}, \: 3q^2-2 \gt 0 \big) \: \equiv \: \exists q \in \mathbb{Q}, \: 3q^2-2 \leq 0


$$

So, we begin as follows:

To disprove a universal statement, it's sufficient to find a counterexample. In other words, we need to show that there exists a rational number $q$ such that

$$


3q^2-2 \leq 0.


$$

Finding a counterexample is sometimes a nontrivial task, but we only need one. In this case, substituting $q=0$ suffices:

By substituting $q=0$ into the expression, we obtain

$$


\begin{aligned}3𝑞^{2}−2 & =3(0)^{2}−2 \\ & =−2 \\ & ≤0.\end{aligned}


$$

Finally, we state our conclusion:

So, $q=0$ is our counterexample. Therefore, the given statement is false.
