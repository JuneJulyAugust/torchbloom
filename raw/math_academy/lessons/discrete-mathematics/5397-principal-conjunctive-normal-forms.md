# Principal Conjunctive Normal Forms

Source: https://www.mathacademy.com/topics/5397?courseId=109
Topic ID: 5397

## Prerequisites

- [Conjunctive Normal Forms](./3781-conjunctive-normal-forms.md)

## Lesson

### Introduction

Suppose we only consider Boolean functions with a fixed number of variables, $N.$ Then, a **maxterm** is a disjunction of exactly $N$ literals, where each literal occurs exactly once.

For instance, considering only Boolean functions with $3$ variables $x_1,$ $x_2,$ and $x_3{:}$

- $\overline{x_1} \lor x_2 \lor \overline{x_3}$ is a maxterm since it is a disjunction of exactly $3$ literals, each occurring once.

- $\overline{x_1} \lor \overline{x_2}$ is *not* a maxterm because it is a disjunction of only $2$ literals (instead of $3$).

A formula is in **principal conjunctive normal form** (PCNF) if it is a conjunction of one or more maxterms.

For example, only considering functions with $3$ variables $x_1$, $x_2,$ and $x_3{:}$

- $(\overline{x_1} \lor x_2 \lor \overline{x_3}) \land (x_1 \lor \overline{x_2} \lor x_3)$ is in PCNF, whereas

- $(\overline{x_1} \lor \overline{x_2}) \land (\overline{x_1} \lor x_2 \lor \overline{x_3})$ is *not* in PCNF because $\overline{x_1} \lor \overline{x_2}$ is not a maxterm.

### Example: Identifying Principal Conjunctive Normal Forms

#### Question

Given that we are considering only Boolean functions with $3$ variables $A,$ $B,$ and $C,$ which of the following statements are true?

1. $\overline{C}$ is a literal

2. $A \lor B$ is a maxterm

3. $(\overline{A} \lor \overline{C}) \land (A \lor B \lor C)$ is a conjunctive normal form

4. $(A \lor \overline{B} \lor C) \land (\overline{A} \lor \overline{B} \lor \overline{C})$ is a principal conjunctive normal form

#### Explanation

Recall that a ** is a variable or a negation of a variable, and an ** is a disjunction of one or more literals. Then, a formula is in ** (CNF) if it is a conjunction of one or more elementary disjunctions.

If the number of variables is fixed (say, $N$), then a ** is a disjunction of exactly $N$ literals where each variable occurs exactly once. A formula is in ** (PCNF) if it is a conjunction of one or more maxterms.

With that in mind, let's examine our statements.

- Statement I is true. Indeed, $C$ is a variable, and $\overline{C}$ is the negation of the variable. So, it's a literal.

- Statement II is false. Notice that we have a disjunction of only $2$ literals (instead of $3$).

- Statement III is true. Indeed, $\overline{A} \lor \overline{C}$ and $A \lor B \lor C$ are disjunctions of one or more literals and, hence are elementary disjunctions. Our formula contains a conjunction of these elementary disjunctions.

- Statement IV is true. Indeed, $(A \lor \overline{B} \lor C)$ and $(\overline{A} \lor \overline{B} \lor \overline{C})$ are disjunctions of exactly $3$ literals where each variable occurs exactly once and, hence, are maxterms. Our formula contains a conjunction of these maxterms.

Therefore, the correct answer is "I, III, and IV only."

### The Binary Tuple Associated With a Maxterm

Given a fixed number of variables, each maxterm has a value of $0$ for exactly *one unique combination* of its variables’ values. This unique combination is the binary tuple associated with the maxterm.

To demonstrate, consider only Boolean functions with $2$ variables. Then, $\overline{x_1} \lor x_2$ is a maxterm and has a value of $0$ for the following values only:

$$



(x_1,x_2) = (1, 0)



$$

Indeed, we can show this by substituting these values into the maxterm:

$$



\begin{aligned}\overset{𝑥_{1}}{}∨𝑥_{2} & ≡\overset{1}{–}∨0 \\ & ≡0∨0 \\ & ≡0\end{aligned}



$$

For any other values of $x_1$ and $x_2,$ we have $\overline{x_1} \lor x_2 \equiv 1.$

### Example: Determining a Tuple Given a Maxterm

#### Question

Given that we are considering only Boolean functions with $4$ variables, find the combination of the variables' values on which the maxterm $x_1\lor x_2\lor \overline{x_3}\lor \overline{x_4}$ has a value of $0$ (false).

#### Explanation

Each maxterm has a value of $0$ (false) for exactly one combination of its variables' values.

In our example, these are the following values:

$$



(x_1,x_2,x_3,x_4) = (0,0,1,1)



$$

Indeed, we have

$$



\begin{aligned}𝑥_{1}∨𝑥_{2}∨\overset{𝑥_{3}}{}∨\overset{𝑥_{4}}{} & ≡0∨0∨\overset{1}{–}∨\overset{1}{–} \\ & ≡0∨0∨0∨0 \\ & ≡0.\end{aligned}



$$

### Example: Determining a Maxterm Given a Tuple

#### Question

Given that we are considering only Boolean functions with $4$ variables, find the maxterm that gives $0$ on the tuple $(x_1,x_2,x_3,x_4) = (1,0,0,0).$

#### Explanation

Each maxterm has a value of $0$ (false) for exactly one combination of its variables' values.

In our example, the maxterm that gives $0$ on $(1,0,0,0)$ is

$$



\overline{x_1} \lor x_2 \lor x_3\lor x_4.



$$

Indeed, we have

$$



\begin{aligned}\overset{𝑥_{1}}{}∨𝑥_{2}∨𝑥_{3}∨𝑥_{4} & ≡\overset{1}{–}∨0∨0∨0 \\ & ≡0∨0∨0∨0 \\ & ≡0.\end{aligned}



$$

### Truth Tables and PCNFs

We've seen that each maxterm has a value of $0$ for exactly one combination of its variables' values.

As a result, a maxterm is in the principal conjunctive normal form of a Boolean function if and only if the binary tuple associated with the maxterm evaluates the function to $0.$

To demonstrate this, consider the following principal conjunctive normal form (PCNF) of a Boolean function $f.$

$$



f \equiv (\overline{x_1} \lor x_2 \lor \overline{x_3}) \land (\overline{x_1} \lor \overline{x_2} \lor x_3) \land (\overline{x_1} \lor \overline{x_2} \lor \overline{x_3})



$$

Let's see how to fill the truth table for $f$ corresponding to the PCNF above.

Since our PCNF has $3$ maxterms, the resulting truth table must contain $3$ rows with output $0.$ The tuple in each of these rows corresponds to one of the maxterms in the PCNF.

The rows containing zeros of the function and their corresponding maxterms are shown below.

This is the truth table corresponding to the Boolean function $f.$

This method also works in reverse, i.e., we can find the PCNF of a Boolean function defined by a given truth table. Let's see how with an example.

### Example: Finding the Principal Conjunctive Normal Form

#### Question

Consider the Boolean function with $3$ variables defined by the following table.

#### Explanation

Note that each maxterm has a value of $0$ (false) for exactly one combination of its variables' values.

Therefore, the principal conjunctive normal form of the given function has $3$ maxterms since this is the number of zeros in the given truth table.

The rows containing zeros of the function and their corresponding maxterms are shown below.

Consequently, the corresponding PCNF is

$$



(x_1 \lor x_2 \lor \overline{x_3}) \land (\overline{x_1} \lor x_2 \lor x_3) \land (\overline{x_1} \lor \overline{x_2} \lor \overline{x_3}).



$$
