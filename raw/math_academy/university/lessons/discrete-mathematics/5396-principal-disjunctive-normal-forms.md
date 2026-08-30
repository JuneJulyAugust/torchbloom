# Principal Disjunctive Normal Forms

Source: https://www.mathacademy.com/topics/5396?courseId=109
Topic ID: 5396

## Prerequisites

- [Disjunctive Normal Forms](./3780-disjunctive-normal-forms.md)

## Lesson

### Introduction

Suppose we only consider Boolean functions with a fixed number of variables, $N.$ Then, a **minterm** is a conjunction of exactly $N$ literals, where each variable occurs exactly once.

For instance, considering only Boolean functions with $3$ variables $x_1,$ $x_2,$ and $x_3{:}$

- $\overline{x_1} \land \overline{x_2} \land x_3$ is a minterm since it is a conjunction of exactly $3$ literals, where each variable occurs exactly once.

- $x_1 \land x_2$ is *not* a minterm because it is a conjunction of only $2$ literals (instead of $3$).

A formula is in **principal disjunctive normal form** (PDNF) if it is a disjunction of one or more minterms.

For example, considering only Boolean functions with $3$ variables $x_1,$ $x_2,$ and $x_3{:}$

- $(x_1 \land x_2 \land x_3) \lor (\overline{x_1} \land \overline{x_2} \land \overline{x_3})$ is in PDNF, whereas

- $(x_1 \land \overline{x_2}) \lor (\overline{x_1} \land \overline{x_2} \land \overline{x_3})$ is *not* in PDNF because $x_1 \land \overline{x_2}$ is not a minterm.

### Example: Identifying Principal Disjunctive Normal Forms

#### Question

Given that we are considering only Boolean functions with $3$ variables $A,$ $B,$ and $C,$ which of the following statements are true?

1. $\overline{A}$ is a literal

2. $\overline{A} \land \overline{B}$ is a minterm

3. $(\overline{A} \lor \overline{B} \lor \overline{C}) \land (A \lor B \lor C)$ is a disjunctive normal form

4. $(\overline{A} \land \overline{B} \land \overline{C}) \lor (A \land \overline{B} \land C)$ is a principal disjunctive normal form

#### Explanation

Recall that a ** is a variable or a negation of a variable, and an ** is a conjunction of one or more literals. Then, a formula is in ** (DNF) if it is a disjunction of one or more elementary conjunctions.

If the number of variables is fixed (say, $N$), then a ** is a conjunction of exactly $N$ literals where each variable occurs exactly once. A formula is in ** (PDNF) if it is a disjunction of one or more minterms.

With that in mind, let's examine our statements.

- Statement I is true. Indeed, $A$ is a variable, and $\overline{A}$ is the negation of the variable. So, it's a literal.

- Statement II is false. Notice that we have a conjunction of only $2$ literals (instead of $3$).

- Statement III is false. Notice that, $(\overline{A} \lor \overline{B} \lor \overline{C})$ and $(A \lor B \lor C)$ are disjunction of literals, not a conjunction.

- Statement IV is true. Indeed $(\overline{A} \land \overline{B} \land \overline{C})$ and $(A \land \overline{B} \land C)$ are conjunctions of exactly $3$ literals where each variable occurs exactly once and, hence, are minterms. Our formula contains a disjunction of these minterms.

Therefore, the correct answer is "I and IV only."

### The Binary Tuple Associated With a Minterm

Given a fixed number of variables, each minterm has a value of $1$ for exactly *one unique combination* of its variables’ values. This unique combination is the binary tuple associated with the minterm.

To demonstrate, consider only Boolean functions with $2$ variables. Then, $x_1 \land\overline{x_2}$ is a minterm and has a value of $1$ for the following values only:

$$



(x_1,x_2) = (1, 0)



$$

Indeed, we can show this by substituting these values into the minterm:

$$



\begin{aligned}𝑥_{1}∧\overset{𝑥_{2}}{} & ≡1∧\overset{0}{–} \\ & ≡1∧1 \\ & ≡1\end{aligned}



$$

For any other values of $x_1$ and $x_2,$ we have $x_1 \land\overline{x_2} \equiv 0.$

### Example: Determining a Tuple Given a Minterm

#### Question

Given that we are considering only Boolean functions with $4$ variables, find the combination of the variables' values on which the minterm $\overline{x_1} \land x_2 \land x_3\land \overline{x_4}$ has a value of $1$ (true).

#### Explanation

Each minterm has a value of $1$ (true) for exactly one combination of its variables' values.

In our example, these are the following values:

$$



(x_1,x_2,x_3,x_4) = (0, 1, 1,0)



$$

Indeed, we have

$$



\begin{aligned}\overset{𝑥_{1}}{}∧𝑥_{2}∧𝑥_{3}∧\overset{𝑥_{4}}{} & ≡\overset{0}{–}∧1∧1∧\overset{0}{–} \\ & ≡1∧1∧1∧1 \\ & ≡1.\end{aligned}



$$

### Example: Determining a Minterm Given a Tuple

#### Question

Given that we are considering only Boolean functions with $4$ variables, find the minterm that gives $1$ on the tuple $(x_1,x_2,x_3,x_4)=(1,0,1,0).$

#### Explanation

Each minterm has a value of $1$ (true) for exactly one combination of its variables' values.

In our example, the minterm that gives $1$ on $(1,0,1,0)$ is

$$



x_1 \land \overline{x_2} \land x_3 \land \overline{x_4}.



$$

Indeed, we have

$$



\begin{aligned}𝑥_{1}∧\overset{𝑥_{2}}{}∧𝑥_{3}∧\overset{𝑥_{4}}{} & ≡1∧\overset{0}{–}∧1∧\overset{0}{–} \\ & ≡1∧1∧1∧1 \\ & ≡1.\end{aligned}



$$

### Truth Tables and PDNFs

We've seen that each minterm has a value of $1$ for exactly one combination of its variables' values.

As a result, a minterm is in the principal disjunctive normal form of a Boolean function if and only if the binary tuple associated with the minterm evaluates the function to $1.$

To demonstrate this, let's find the PDNF of the Boolean function with $3$ variables, as defined by the following table.

The PDNF of the function has $3$ minterms since this is the number of rows with output $1$ in the given truth table. The tuple in each of these rows corresponds to one of the minterms in the PCNF.

The rows containing ones of the function and their corresponding minterms are shown below.

Consequently, the corresponding PDNF of the function $f$ is

$$



f\equiv (\overline{x_1} \land \overline{x_2} \land x_3)\lor(\overline{x_1} \land \ x_2 \land x_3 ) \lor (x_1 \land \overline{x_2} \land x_3).



$$

This method also works in reverse, i.e., we can construct the truth table of a function given in PDNF. Let's see how with an example.

### Example: Finding the PDNF of a Boolean Function

#### Question

Consider the following Boolean function.

$$



f \equiv (\overline{x_1} \land \overline{x_2} \land x_3) \lor (\overline{x_1} \land x_2 \land x_3) \lor (x_1 \land \overline{x_2} \land \overline{x_3})



$$

Find the truth table for this function corresponding to the principal disjunctive normal form (PDNF) above.

#### Explanation

Each minterm has a value of $1$ (true) for exactly one combination of its variables' values.

Since our principal disjunctive normal form has $3$ minterms, the resulting truth table must contain $3$ ones.

The rows containing ones of the function and their corresponding minterms are shown below.
