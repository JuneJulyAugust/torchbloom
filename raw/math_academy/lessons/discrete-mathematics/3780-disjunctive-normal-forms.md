# Disjunctive Normal Forms

Source: https://www.mathacademy.com/topics/3780?courseId=109
Topic ID: 3780

## Prerequisites

- [Boolean Functions And Logical Operations](./3779-boolean-functions-and-logical-operations.md)

## Lesson

### Introduction

A **literal** is a variable or a negation of a variable in a Boolean expression. For example, the following are all literals: Note that is the same as In contrast, the following are *not* literals:

An **elementary conjunction** is a conjunction of one or more literals. Some examples are as follows:

A formula is in **disjunctive normal form** (DNF) if it is a disjunction of one or more elementary conjunctions. For instance, are all in DNF. In contrast, the following expressions are *not* in DNF:

As we'll see, disjunctive normal forms provide a standard way of representing Boolean functions, allowing them to be compared easily.

### Example: Identifying Disjunctive Normal Forms

#### Question

Which of the following statements are true?

1. $\overline{P}$ is a literal

2. $\overline{Q} \land \overline{R}$ is an elementary conjunction

3. $P \lor (Q \land R) \lor (\overline{Q} \land \overline{R})$ is a disjunctive normal form

#### Explanation

Recall that a ** is a variable or a negation of a variable, and an ** is a conjunction of one or more literals.

A formula is in ** (DNF) if it is a disjunction of one or more elementary conjunctions. Also $\overline{A}$ means the same as $\lnot A.$

With that in mind, let's examine our statements.

- Statement I is true. Indeed, $P$ is a variable, and $\overline{P}$ is the negation of the variable. So, it's a literal.

- Statement II is true. Indeed, $\overline{Q} \land \overline{R}$ is a conjunction of one or more literals.

- Statement III is true. Indeed, $P,$ $(Q \land R),$ and $\overline{Q} \land \overline{R}$ are conjunctions of one or more literals. Our formula contains a disjunction of these elementary conjunctions.

Therefore, the correct answer is "I, II, and III."

### The Disjunctive Normal Form of a Function

Every Boolean function can be expressed in an equivalent disjunctive normal form (DNF). In other words, for any Boolean function $f(x_1, x_2, \dots, x_n)$, there exists an expression $D(x_1, x_2, \dots, x_n)$ in DNF such that

$$



f(x_1, x_2, \dots, x_n) \equiv D(x_1, x_2, \dots, x_n).



$$

To write a given Boolean function in disjunctive normal form,

- we eliminate all instances of logical operations other than $\lnot, \land, \lor,$ then

- we rewrite the expression as a disjunction of elementary conjunctions.

For example, let's deduce a disjunctive normal form of $x_1 \land (x_2 \Rightarrow x_3).$

- First, using the fact that $A \Rightarrow B \equiv \overline{A} \lor B,$ we eliminate $\Rightarrow$ from the expression:

- Then, we simplify the expression by applying the laws of logic, distributing the conjunction over the disjunction:

Therefore, we conclude that

$$



x_1 \land (x_2 \Rightarrow x_3 ) \equiv (x_1 \land \overline{x_2}) \lor (x_1 \land x_3 ),



$$

where the expression on the right-hand side is in disjunctive normal form.

In this example, we used the fact that $A \Rightarrow B \equiv \overline{A} \lor B.$ Some logical equivalences we might use when writing a formula in DNF are

$$



\begin{aligned}𝐴⇒𝐵 & ≡\overset{𝐴}{}∨𝐵, \\ 𝐴⇔𝐵 & ≡(𝐴∧𝐵)∨(\overset{𝐴}{}∧\overset{𝐵}{}), \\ 𝐴⊕𝐵 & ≡(𝐴∧\overset{𝐵}{})∨(\overset{𝐴}{}∧𝐵).\end{aligned}



$$

### Example: Completing a Derivation of a Disjunctive Normal Form

#### Question

Express $x_1 \Rightarrow (x_2 \oplus x_3)$ in disjunctive normal form.

#### Explanation

In general, to write down a formula in disjunctive normal form,

- we eliminate all instances of logical operations other than $\neg,$ $\land,$ $\lor,$ then

- we rewrite the expression as a disjunction of elementary conjunctions.

In this example, we proceed as follows.

- Use the fact that $A \Rightarrow B \equiv \overline{A} \lor B$ to eliminate $\Rightarrow$ from the expression:

- Use the fact that $A \oplus B \equiv (A \land \overline{B}) \lor (\overline{A} \land B)$ to eliminate $\oplus$ from the expression:

Notice that the final expression is a disjunction of one or more elementary conjunctions. Therefore, this is a disjunctive normal form.

### Example: Finding a Disjunctive Normal Form

#### Question

A disjunctive normal form of $x_1 \oplus (x_2 \Rightarrow x_3)$ is

$$



\big(x_1 \land \boxed{\phantom{x_2}} \land \overline{x_3}\big) \lor \big(\,\boxed{\phantom{x_1}} \land \overline{x_2}\big) \lor \big(\,\boxed{\phantom{x_1}} \land x_3 \big).



$$

#### Explanation

Recall the following equivalent formulas:

$$



\begin{aligned}𝐴⇒𝐵 & ≡\overset{𝐴}{}∨𝐵 \\ 𝐴⇔𝐵 & ≡(𝐴∧𝐵)∨(\overset{𝐴}{}∧\overset{𝐵}{}) \\ 𝐴⊕𝐵 & ≡(𝐴∧\overset{𝐵}{})∨(\overset{𝐴}{}∧𝐵)\end{aligned}



$$

With that in mind, let's find an equivalent disjunctive normal form to the given formula.

- Eliminate $\Rightarrow$ and $\oplus$ from the expression:

- Use the laws of logic to simplify the expression:

The final expression is in disjunctive normal form.
