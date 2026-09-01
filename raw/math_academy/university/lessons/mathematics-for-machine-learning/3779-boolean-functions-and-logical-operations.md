# Boolean Functions And Logical Operations

Source: https://www.mathacademy.com/topics/3779?courseId=145
Topic ID: 3779

## Prerequisites

- [Biconditional Statements](./248-biconditional-statements.md)
- [Boolean Functions](./3778-boolean-functions.md)

## Lesson

### Introduction

We can associate any logical operation (or expression) with a corresponding Boolean function. In this correspondence, the value $1$ is equivalent to "True," and the value $0$ is equivalent to "False."

For example, consider the logical operation of conjunction (the "and" connective). The corresponding truth table is shown below. Remember, conjunction is true if and only if both arguments are true.

Now, substituting $0$ for "False" and $1$ for "True" in the table, we get the following:

The obtained table defines the Boolean function **associated with** the logical operation of conjunction.

### Example: Identifying Boolean Functions Given Logical Operations

#### Question

Complete the missing values in the truth table below.

#### Explanation

Recall that $\text{True}=1$ and $\text{False}=0.$

Also, the implication $x_1 \Rightarrow x_2$ is false if and only if $x_1$ is true ($1$) and $x_2$ is false ($0$).

Therefore, the corresponding Boolean function is the following:

### Peirce Arrow, Sheffer Stroke, and XOR

Remember that we equate $0$ to "False" and $1$ to "True." As well as conjunction, disjunction, negation, implication, and equivalence, there are a few more logical operations we should know:

- The **exclusive disjunction** (**EXCLUSIVE OR** or **XOR**) $x_1 \oplus x_2$ is false $(0)$ if and only if both $x_1$ and $x_2$ are false $(0),$ or both $x_1$ and $x_2$ are true $(1).$ The corresponding Boolean function is the following: $x_1$ $x_2$ $x_1 \oplus x_2$ $0$ $0$ $0$ $0$ $1$ $1$ $1$ $0$ $1$ $1$ $1$ $0$ The key difference between XOR and $x_1\lor x_2$ is that XOR returns zero when $x_1 = x_2 = 1.$ Hence, it is called the exclusive OR since it returns $1$ if $x_1$ or $x_2$ equal $1,$ but not both.

- The **Peirce arrow** (**NOT OR** or **NOR**) $x_1 \downarrow x_2$ is true $(1)$ if and only if both $x_1$ and $x_2$ are false $(0).$ The corresponding Boolean function is the following: $x_1$ $x_2$ $x_1 \downarrow x_2$ $0$ $0$ $1$ $0$ $1$ $0$ $1$ $0$ $0$ $1$ $1$ $0$ Note that the Peirce arrow is the negation of the Boolean OR operator:

- The **Sheffer stroke** (**NOT AND** or **NAND**) $x_1 \mid x_2$ is false $(0)$ if and only if both $x_1$ and $x_2$ are true $(1).$ The corresponding Boolean function is the following: $x_1$ $x_2$ $x_1 \mid x_2$ $0$ $0$ $1$ $0$ $1$ $1$ $1$ $0$ $1$ $1$ $1$ $0$ The Sheffer stroke is the negation of the Boolean AND operator:

### Example: Identifying Peirce Arrow, Sheffer Stroke, and XOR

#### Question

Complete the missing values in the truth table below.

#### Explanation

Recall that $\text{True}=1$ and $\text{False}=0.$

Also, the Peirce arrow $x_1 \downarrow x_2$ is true if and only if both $x_1$ and $x_2$ are false ($0$).

Therefore, the corresponding Boolean function is the following:

### Classifying Unary Logical Operations

There are $2^{2^n}$ distinct Boolean functions of $n$ variables; therefore, there are $2^{2^1}=4$ distinct Boolean functions of one variable. These functions can be summarized in the following table:

Each of these functions corresponds to an **unary** logical operation, an operation that operates on only one operand. Let's examine each function in turn.

- The function $f_0$ always returns $0.$ This is the constant zero operation $f_0 \equiv 0.$

- The function $f_1$ returns the same value as $x.$ This is the the identity $f_1 \equiv x.$

- The function $f_2$ returns the opposite value to $x.$ This is the negation $f_2 \equiv \lnot \, x.$

- The function $f_3$ always returns $1.$ This is the constant one operation $f_3 \equiv 1.$

### Classifying Binary Logical Operations

If we have two variables, the situation is a bit more complicated. There are $2^{2^2}=16$ distinct Boolean functions of two variables. These functions can be summarized in the following table:

Each of these functions corresponds to a **binary** logical function, an operation that operates on two operands. Let's examine each function in turn.

- The following functions involve conjunction, disjunction, negation, implication, and equivalence. The function $f_0$ always returns $0.$ This is the constant zero operation $f_0 \equiv 0.$ The function $f_1$ returns $1$ if and only if both $x_1$ and $x_2$ equal $1.$ This is the conjunction $f_1 \equiv x_1 \land x_2.$ The function $f_3$ returns the same value as $x_1.$ This is the identity applied to the first input $f_3 \equiv x_1.$ The function $f_5$ returns the same value as $x_2.$ This is the identity applied to the second input $f_5 \equiv x_2.$ The function $f_7$ returns $0$ if and only if both $x_1$ and $x_2$ equal $0.$ This is the disjunction $f_7 \equiv x_1 \lor x_2.$ The function $f_9$ returns $1$ if and only if both $x_1=x_2.$ This is the equivalence $f_9 \equiv x_1 \Leftrightarrow x_2.$ The function $f_{10}$ returns the value opposite to $x_2.$ This is the negation of the second input $f_{10} \equiv \lnot \, x_2.$ The function $f_{11}$ returns $0$ if and only if $x_2=1$ and $x_1=0.$ This is the implication $f_{11}\equiv x_2 \Rightarrow x_1.$ The function $f_{12}$ returns the value opposite to $x_1.$ This is the negation of the first input $f_{12} \equiv \lnot \, x_1.$ The function $f_{13}$ returns $0$ if and only if $x_1=1$ and $x_2=0.$ This is the implication $f_{13}\equiv x_1 \Rightarrow x_2.$ The function $f_{15}$ always returns $1.$ This is the constant one operation $f_{15} \equiv 1.$

- The following involve exclusive disjunction, Peirce arrow, and Sheffer Stroke. The function $f_6$ returns $0$ if and only if both $x_1$ and $x_2$ are $0$ or both are $1.$ This is the exclusive disjunction $f_6 \equiv x_1 \oplus x_2.$ Notice that it's opposite to the function $f_9 \equiv x_1 \Leftrightarrow x_2,$ hence, $f_6 \equiv \lnot\, (x_1 \Leftrightarrow x_2).$ The function $f_8$ returns $1$ if and only if both $x_1$ and $x_2$ equal $0.$ This is the Peirce arrow $f_8 \equiv x_1 \downarrow x_2.$ Notice that it's opposite to the function $f_7 \equiv x_1 \lor x_2,$ hence, $f_8 \equiv \lnot\, (x_1 \lor x_2).$ The function $f_{14}$ returns $0$ if and only if both $x_1$ and $x_2$ equal $1.$ This is the Sheffer stroke $f_{14} \equiv x_1 \mid x_2.$ Notice that it's opposite to the function $f_1 \equiv x_1 \land x_2,$ hence, $f_{14} \equiv \lnot\, (x_1 \land x_2).$

- Finally, we have two other functions. The function $f_2$ returns $1$ if and only if $x_1=1$ and $x_2=0.$ Notice that it's opposite to the function $f_{13}\equiv x_1 \Rightarrow x_2.$ Hence, $f_2 \equiv \lnot (x_1 \Rightarrow x_2).$ The function $f_4$ returns $1$ if and only if $x_1=0$ and $x_2=1.$ Notice that it's opposite to the function $f_{11}\equiv x_2 \Rightarrow x_1.$ Hence, $f_4 \equiv \lnot (x_2 \Rightarrow x_1).$

### Example: Identifying Logical Operations Given Boolean Functions

#### Question

Find the logical operations that have the corresponding Boolean function shown above?

#### Explanation

The function corresponding to the given table returns $0$ if and only if $x_1=1$ and $x_2=0.$ This is the implication. Therefore,

$$


f \equiv (x_1 \Rightarrow x_2).


$$

### Example: Building Truth Tables for Boolean Functions With Three Variables

#### Question

Complete the missing values in the truth table below.

#### Explanation

First, we fill out the column corresponding to $x_1 \lor x_2{:}$

Finally, we fill in the column for $x_3 \land (x_1 \lor x_2){:}$
