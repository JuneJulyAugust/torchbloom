# Conjunctive Normal Forms

Source: https://www.mathacademy.com/topics/3781?courseId=109
Topic ID: 3781

## Prerequisites

- [Boolean Functions And Logical Operations](./3779-boolean-functions-and-logical-operations.md)

## Lesson

### Introduction

A **literal** is a variable or a negation of a variable in a Boolean expression. For example, the following are all literals:

$$



x, \quad y, \quad \overline{x}, \quad \overline{y}



$$

Note that $\overline{x}$ is the same as $\lnot\,x.$ In contrast, the following are *not* literals:

$$



\overline{\overline{x}}, \qquad x \land y, \qquad x \lor y, \qquad x \mid x



$$

An **elementary disjunction** is a disjunction of one or more literals. Some examples are as follows:

$$



x, \qquad \overline{y}, \qquad x \lor y, \qquad \overline{x} \lor y \lor \overline{z}



$$

A formula is in **conjunctive normal form** (CNF) if it is a conjunction of one or more elementary disjunctions. For instance,

$$



x, \qquad x \land \overline{y}, \qquad x \lor y, \qquad x \land (\overline{y} \lor z),\qquad (x \lor y) \land ({y} \lor \overline{z} \lor k)



$$

are all in CNF. In contrast, the following expressions are *not* in CNF:

$$



x \Rightarrow y, \qquad \overline{x \land y}, \qquad x \land \overline{(y \lor z)}, \qquad x\land (y \lor (z\land k))



$$

### Example: Identifying Conjunctive Normal Forms

#### Question

Which of the following statements is true?

1. $\overline{Y}$ is a literal

2. $Y \lor \overline{X}$ is an elementary disjunction

3. $(Y \lor \overline{X}) \land \overline{Z}$ is a conjunctive normal form

#### Explanation

Recall that a ** is a variable or a negation of a variable, and an ** is a disjunction of one or more literals.

A formula is in ** (CNF) if it is a conjunction of one or more elementary disjunctions. Also, $\overline{A}$ means the same as $\lnot A.$

With that in mind, let's examine our statements.

- Statement I is true. Indeed, $Y$ is a variable, and $\overline Y$ is the negation of the variable. So, it's a literal.

- Statement II is true. Indeed, $Y \lor \overline{X}$ is a disjunction of one or more literals.

- Statement III is true. Indeed, $(Y \lor \overline{X})$ and $\overline{Z}$ are disjunctions of one or more literals. Our formula contains a conjunction of these elementary disjunctions.

Therefore, the correct answer is "I, II, and III."

### Conjunctive Normal Forms of a Function

Every Boolean function can be expressed in an equivalent conjunctive normal form (CNF). In other words, for any Boolean function $f(x_1, x_2, \dots, x_n),$ there exists an expression $C(x_1, x_2, \dots, x_n)$ in CNF such that

$$



f(x_1, x_2, \dots, x_n) \equiv C(x_1, x_2, \dots, x_n).



$$

To write a given Boolean function in conjunctive normal form,

- we eliminate all instances of logical operations other than $\lnot, \land, \lor,$ then

- we rewrite the expression as a conjunction of elementary disjunctions.

For example, let's deduce a conjunctive normal form of $(\overline{x_3} \Rightarrow x_2) \land (x_1 \Rightarrow x_2).$

- First, using the fact that $A \Rightarrow B \equiv \overline{A} \lor B,$ we eliminate $\Rightarrow$ from the expression:

$$



\begin{aligned}(\overset{𝑥_{3}}{}⇒𝑥_{2})∧(𝑥_{1}⇒𝑥_{2}) & ≡(\overset{𝑥_{3}}{}}{}∨𝑥_{2})∧(𝑥_{1}⇒𝑥_{2}) \\ & ≡(\overset{𝑥_{3}}{}}{}∨𝑥_{2})∧(\overset{𝑥_{1}}{}∨𝑥_{2})\end{aligned}



$$

- Then, we simplify the expression by applying the laws of logic:

Therefore, we conclude that

$$



(\overline{x_3} \Rightarrow x_2) \land (x_1 \Rightarrow x_2) \equiv (x_3 \lor x_2) \land ( \overline{x_1} \lor x_2),



$$

where the expression on the right-hand side is in conjunctive normal form.

In this example, we used the fact that $A \Rightarrow B \equiv \overline{A} \lor B.$ Some logical equivalences we might use when writing a formula in CNF are

$$



\begin{aligned}𝐴⇒𝐵 & ≡\overset{𝐴}{}∨𝐵, \\ 𝐴⇔𝐵 & ≡(\overset{𝐴}{}∨𝐵)∧(𝐴∨\overset{𝐵}{}), \\ 𝐴⊕𝐵 & ≡(𝐴∨𝐵)∧(\overset{𝐴}{}∨\overset{𝐵}{}).\end{aligned}



$$

### Example: Completing a Derivation of a Conjunctive Normal Form

#### Question

Complete the derivation of a disjunctive normal form below.

$$



\begin{aligned}\overset{𝑥_{3}}{}⇒(𝑥_{1}⊕𝑥_{2}) & ≡ \\ 𝑥_{2}∨(𝑥_{1}⊕𝑥_{2}) & ≡ \\ 𝑥_{2}∨(𝑥_{1}⊕𝑥_{2}) & ≡ \\ 𝑥_{2}∨((\,𝑥_{2}∨𝑥_{2})∧(\overset{𝑥_{1}}{}∨𝑥_{2}\,)) & ≡ \\ (\,𝑥_{2}∨𝑥_{2}∨𝑥_{2}\,)∧(\overset{𝑥_{1}}{}∨𝑥_{2}∨𝑥_{3}) & \end{aligned}



$$

#### Explanation

In general, to write down a formula in conjunctive normal form,

- We eliminate all instances of logical operations other than $\overline{}, \land, \lor,$ then

- we rewrite the expression as a conjunction of elementary disjunctions.

In this example, we proceed as follows:

- First, we use the fact that $A \Rightarrow B \equiv \overline{A} \lor B$ to eliminate $\Rightarrow$ from the expression:

- Then, we use $\overline{\overline{A}} \equiv A$ to simplify the double negation:

- Next, we use the fact that $A \oplus B \equiv (A \lor B) \land (\overline{A} \lor \overline{B})$ to eliminate $\oplus$ from the expression:

- Finally, we distribute the disjunction over the conjunction:

Notice that the final expression is a conjunction of one or more elementary disjunctions. Therefore, this is a conjunctive normal form.

### Example: Finding a Conjunctive Normal Form

#### Question

What is the conjunctive normal form of $x_1 \Rightarrow (\overline{x_1} \oplus x_2)?$

#### Explanation

Recall the following logical equivalences:

$$



\begin{aligned}𝐴⇒𝐵 & ≡\overset{𝐴}{}∨𝐵 \\ 𝐴⇔𝐵 & ≡(\overset{𝐴}{}∨𝐵)∧(𝐴∨\overset{𝐵}{}) \\ 𝐴⊕𝐵 & ≡(𝐴∨𝐵)∧(\overset{𝐴}{}∨\overset{𝐵}{})\end{aligned}



$$

With that in mind, let's find an equivalent disjunctive normal form for the given formula.

- First, we eliminate $\Rightarrow$ and $\oplus$ from the expression:

- Finally, we use the laws of logic to simplify the expression:

Our final expression is in conjunctive normal form.
