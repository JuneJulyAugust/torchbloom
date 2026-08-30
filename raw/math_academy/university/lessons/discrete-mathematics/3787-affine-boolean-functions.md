# Affine Boolean Functions

Source: https://www.mathacademy.com/topics/3787?courseId=109
Topic ID: 3787

## Prerequisites

- [Boolean Polynomials](./3782-boolean-polynomials.md)

## Lesson

### Introduction

A Boolean polynomial is **linear** if it does not contain conjunctions. For example, the polynomial

$$



f(x_1,x_2, x_3) = 1 \oplus x_1 \oplus x_2 \oplus x_3



$$

is linear because it does not contain conjunctions. On the other hand, the polynomial

$$



g(x_1,x_2, x_3) = 1 \oplus x_1 \oplus x_2 x_3



$$

is *not* linear since it contains the conjunction $x_2 x_3 \equiv x_2 \land x_3.$

### Example: Identifying Linear Boolean Polynomials

#### Question

Which of the following Boolean polynomials are linear?

1. $x_1 \oplus x_2$

2. $x_1 \oplus 1 \oplus x_3$

3. $1 \oplus x_2x_3$

#### Explanation

A Boolean polynomial is ** if it does not contain conjunctions.

With that in mind, let's examine our polynomials.

- Polynomial I is linear since it does not contain conjunctions.

- Polynomial II is linear since it does not contain conjunctions.

- Polynomial III is ** linear since it contains the conjunction $x_2 x_3 \equiv x_2 \land x_3.$

Therefore, the correct answer is "I and II only."

### Affine Boolean Functions

A Boolean function is **affine** if its corresponding Boolean polynomial is linear. In other words, the Boolean function can be expressed as a linear combination of variables and constants using the $\oplus$ operation.

For example, consider the following truth table of a Boolean function $f.$

To determine whether the function is affine or not, we first construct the principal disjunctive normal form corresponding to $f.$ The rows containing ones of the function and their corresponding minterms are shown below.

So, the corresponding PDNF is

$$



f \equiv (\overline{x_1} \land \overline{x_2}) \lor (\overline {x_1} \land x_2 ) .



$$

Then, we substitute $\overline{x} = x \oplus 1$ for each negation. Also, since each minterm in our PDNF gives $1$ on distinct combinations of variables' values, we can change all instances of $\lor$ to $\oplus.$

$$



\begin{aligned}𝑓≡(𝑥_{1}⊕1)∧(𝑥_{2}⊕1)⊕(𝑥_{1}⊕1)∧𝑥_{2}\end{aligned}



$$

Finally, we simplify the expression:

- Drop the $\land$-sign as we do with multiplication in algebraic expression to make the expressions shorter:

- Using logical equivalences $(A \oplus B)C \equiv C(A \oplus B) \equiv A C \oplus B C$ and $1 \land A \equiv A \land 1 \equiv A,$ we expand the parentheses:

- Using the fact that $A \oplus B \equiv B \oplus A,$ $A \oplus A \equiv 0,$ and $0 \oplus A \equiv A,$ we cancel out pairs of identical terms:

Therefore, the Boolean polynomial corresponding to $f$ is $x_1 \oplus 1.$ Since this polynomial is linear, the function $f$ *is* affine.

### Example: Identifying Affine Boolean Functions Using Tables

#### Question

Consider the Boolean function $f$ given above. Find the Boolean polynomial corresponding to $f$ and determine whether this polynomial is affine or not.

#### Explanation

A boolean function is affine if the corresponding Boolean polynomial for this function is linear (doesn't contain conjunctions).

First, we construct the principal disjunctive normal form corresponding to $f.$ The rows containing ones of the function and their corresponding minterms are shown below.

So, the corresponding PDNF is

$$



f \equiv (\overline{x_1} \land\overline {x_2} ) \lor ({x_1} \land \overline{x_2})\lor({x_1} \land x_2 ) .



$$

Now, we substitute $\overline{x} = x \oplus 1$ for each negation. Also, since each minterm in our PDNF gives $1$ on distinct combinations of variables' values, we can change all instances of $\lor$ to $\oplus.$

$$



\begin{aligned}𝑓≡(𝑥_{1}⊕1)∧(𝑥_{2}⊕1)⊕𝑥_{1}∧(𝑥_{2}⊕1)⊕𝑥_{1}∧𝑥_{2}\end{aligned}



$$

Finally, we simplify the expression:

- Drop the $\land$-sign as we do with multiplication in algebraic expression to make the expressions shorter:

- Using logical equivalences $(A \oplus B)C \equiv C(A \oplus B) \equiv A C \oplus B C$ and $1 \land A \equiv A \land 1 \equiv A,$ we expand the parentheses:

- Using the fact that $A \oplus B \equiv B \oplus A,$ $A \oplus A \equiv 0,$ and $0 \oplus A \equiv A,$ we cancel out pairs of identical terms:

Therefore, the Boolean polynomial corresponding to $f$ is $1 \oplus x_2 \oplus x_1x_2.$ Notice that this polynomial isn't linear, so the function $f$ isn't affine.

### Example: Identifying Affine Boolean Functions of Two Variables

#### Question

Which of the following boolean functions of two variables are affine?

1. $f(x_1,x_2) \equiv x_2 \Rightarrow x_1$

2. $g(x_1,x_2) \equiv \overline{x_1} \land x_2$

3. $h(x_1,x_2) \equiv \overline{x_1}$

#### Explanation

A boolean function is affine if the corresponding Boolean polynomial for this function is linear (doesn't contain conjunctions).

With that in mind, let's examine our functions.

- The table corresponding to $f$ is the following: $x_1$ $x_2$ $f$ $0$ $0$ $1$ $\overline{x_1} \land \overline{x_2}$ $0$ $1$ $0$ $1$ $0$ $1$ ${x_1} \land \overline{x_2}$ $1$ $1$ $1$ $x_1 \land x_2$ Now, we can construct the corresponding polynomial: Since the polynomial contains a conjunction, $f$ is ** affine.

- Note that Since the polynomial contains a conjunction, $g$ is ** affine.

- Notice that Since the polynomial doesn't contain conjunctions, $h$ is affine.

Therefore, the correct answer is "III only."
