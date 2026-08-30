# Boolean Polynomials

Source: https://www.mathacademy.com/topics/3782?courseId=109
Topic ID: 3782

## Prerequisites

- [Direct Proof](../methods-of-proof/2801-direct-proof.md)
- [Principal Disjunctive Normal Forms](./5396-principal-disjunctive-normal-forms.md)

## Lesson

### Introduction

A **Boolean polynomial** is an expression that consists exclusively of variables, the operations $\land$ and $\oplus,$ and the constants $0$ and $1.$ For example,

$$



x_1 \oplus (x_2 \land x_3) \oplus 1



$$

is a Boolean polynomial, but $\overline{x_1} \land x_2 \lor 1$ is not, since it contains a negation and the operation $\lor.$

For simplicity, we can omit the $\land$-signs in Boolean polynomials, similar to omitting the multiplication signs in algebraic expressions. So, we can write the Boolean polynomial above as follows:

$$



x_1 \oplus x_2x_3 \oplus 1



$$

Just like algebraic polynomials, Boolean polynomials are sums of products of variables and constants.

According to this definition, the constants $0$ and $1$ are also considered Boolean polynomials.

### Example: Identifying Boolean Polynomials

#### Question

Which of the following are Boolean polynomials?

1. $A \oplus B \lor C$

2. $A \land B \oplus C$

3. $0AB$

#### Explanation

A Boolean polynomial is an expression that can contain only variables, operations $\land$ and $\oplus,$ and constants $0$ and $1.$

With that in mind, let's examine our formulas.

- Expression I is **** a Boolean polynomial since it contains the operation $\lor.$

- Expression II is a Boolean polynomial since it contains only variables $A,\ B,\ C$ and operations $\land,\ \oplus.$

- Expression III is a Boolean polynomial representing $0\land A \land B,$ which contains the variables $A,\, B,$ constant $0,$ and operation $\land.$

Therefore, the correct answer is "II and III only."

### Properties of Boolean Polynomials

Just like in regular algebra, some laws govern Boolean algebra.

Let $A$ be a Boolean variable. Then, we have the following laws:

- The **identity law** states that

- The **negation law** states that

- The **annulment law** states that

- The **commutative law** states that

These four laws directly result from the definition of the XOR $(\oplus)$ Boolean operator.

Additionally, we have the **distributive law.** Suppose that which states that

$$



A (B \oplus C) \equiv AB \oplus AC.



$$

This can be proved using a table of values.

Notice that the two rightmost columns are identical. Thus, $A (B \oplus C) \equiv AB \oplus AC.$

Finally, for any distinct minterms $K$ and $M$ in a principal disjunctive normal form, we have

$$



K \lor M \equiv K \oplus M.



$$

This is only true for minterms in a PDNF because each gives $1$ on distinct combinations of the variables' values.

### Example: Finding the Boolean Polynomial of Boolean Functions With Two Variables

#### Question

Find the Boolean polynomial corresponding to the function $f(x_1,x_2)=x_1x_2 \lor x_1,$ whose truth table is shown above.

#### Explanation

First, we construct the principal disjunctive normal form corresponding to $f.$ The rows containing ones of the function and their corresponding minterms are shown below.

So, the corresponding PDNF is

$$



f \equiv \left(x_1 \land \overline{x_2}\right) \lor \left(x_1 \land x_2\right)



$$

Now, we substitute $\overline{x} = x \oplus 1$ for the negation.

$$



\begin{aligned}𝑓≡(𝑥_{1}∧(𝑥_{2}⊕1))∨(𝑥_{1}∧𝑥_{2})\end{aligned}



$$

Also, since the minterms in our PDNF each give $1$ on distinct combinations of the variables' values, we can change all instances of $\lor$ to $\oplus.$

$$



\begin{aligned}𝑓 & ≡(𝑥_{1}∧(𝑥_{2}⊕1))⊕(𝑥_{1}∧𝑥_{2})\end{aligned}



$$

Finally, we simplify the expression:

- Drop the $\land$-sign as we do with multiplication in algebraic expression to make the expressions shorter:

- Using logical equivalences $(A \oplus B)C \equiv C(A \oplus B) \equiv A C \oplus B C\$ and $1 \land A \equiv A \land 1 \equiv A,$ we expand the parentheses:

- Using the fact that $A \oplus B \equiv B \oplus A,$ we rearrange to pair up identical terms:

- Using the fact that $A \oplus A \equiv 0$ and $0 \oplus A \equiv A,$ we cancel out the pair of identical terms:

### Example: Finding the Boolean Polynomial Given a Table

#### Question

Find the Boolean polynomial corresponding to the truth table above.

#### Explanation

First, we construct the principal disjunctive normal form corresponding to $f.$ The rows containing ones of the function and their corresponding minterms are shown below.

So, the corresponding PDNF is

$$



f \equiv (x_1 \land \overline{x_2} \land x_3) \lor (x_1 \land x_2 \land \overline{x_3}) \lor (x_1 \land x_2 \land x_3).



$$

Now, we substitute $\overline{x} = x \oplus 1$ for each negation.

$$



\begin{aligned}𝑓 & ≡(𝑥_{1}∧(𝑥_{2}⊕1)∧𝑥_{3})∨(𝑥_{1}∧𝑥_{2}∧(𝑥_{3}⊕1))∨(𝑥_{1}∧𝑥_{2}∧𝑥_{3})\end{aligned}



$$

Also, since the minterms in our PDNF each give $1$ on distinct combinations of the variables' values, we can change all instances of $\lor$ to $\oplus.$

$$



\begin{aligned}𝑓 & ≡(𝑥_{1}∧(𝑥_{2}⊕1)∧𝑥_{3})⊕(𝑥_{1}∧𝑥_{2}∧(𝑥_{3}⊕1))⊕(𝑥_{1}∧𝑥_{2}∧𝑥_{3})\end{aligned}



$$

Finally, we simplify the expression:

- Drop the $\land$-sign as we do with multiplication in algebraic expression to make the expressions shorter:

- Using logical equivalences $(A \oplus B)C \equiv C(A \oplus B) \equiv A C \oplus B C\$ and $1 \land A \equiv A \land 1 \equiv A,$ we expand the parentheses:

- Using the fact that $A \oplus B \equiv B \oplus A,$ we rearrange to pair up identical terms:

- Using logical equivalences $A \oplus A \equiv 0$ and $0 \oplus A \equiv A,$ we cancel out the pair of identical terms:

### Example: Proving Properties of Boolean Polynomials

#### Question

Prove the following statement:

**

#### Explanation

First, let's consider the truth tables for $\lor$ and $\oplus{:}$

Notice that the table's $3$rd and $4$th columns are the same. The only difference is in the $4$th row.

We established that $\lor$ and $\oplus$ are almost equivalent. So, we could use these symbols interchangeably if our expression does not allow the disjunction of two $1$'s. But this is precisely the case for any principal disjunctive normal form (PDNF): since each conjunction of literals in a PDNF equals $1$ only on one combination of Boolean variables, in a PDNF, we will never have a disjunction of $1$'s.

Finally, we conclude that we can change any occurrence of $\lor$ to $\oplus$ in any PDNF.

**** We can't swap $\lor$ and $\oplus$ in an arbitrary expression; here, we only proved this could be done in PDNFs.
