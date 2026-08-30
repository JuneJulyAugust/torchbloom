# Indicator Functions for Predicates

Source: https://www.mathacademy.com/topics/3218?courseId=145
Topic ID: 3218

## Prerequisites

- [Indicator Functions](./948-indicator-functions.md)

## Lesson

### Introduction

Recall that the indicator function $\mathbf{1}_A(x)$ of a set $A$ equals $1$ if $x \in A$ and $0$ if $x \notin A.$

$$


\begin{aligned}1, & if x \in A, \\ 0, & if x \notin A.\end{aligned}


$$

In this lesson, we introduce a more general notation that allows us to write indicator functions for any condition, not just set membership.

The **Iverson bracket notation** $\mathbf{1}[P]$ takes a predicate $P$ and returns

$$


\begin{aligned}1, & if P is true, \\ 0, & if P is false.\end{aligned}


$$

For example:

- $\mathbf{1}[3 > 2] = 1$ because $3 > 2$ is true.

- $\mathbf{1}[5 \leq 4] = 0$ because $5 \leq 4$ is false.

- $\mathbf{1}[7 \in \{2, 5, 7\}] = 1$ because $7$ is an element of $\{2, 5, 7\}.$

### Example: Using Indicator Functions to Check Predicates

#### Question

Evaluate the indicator function $\mathbf{1}[9 > 7].$

#### Explanation

The indicator function $\mathbf{1}[P]$ equals $1$ if the predicate $P$ is true and $0$ if $P$ is false.

$$


\begin{aligned}1, & if P is true, \\ 0, & if P is false.\end{aligned}


$$

Here, the predicate is $9 > 7.$ Since $9$ is greater than $7,$ the predicate is true. Therefore,

$$


\mathbf{1}[9 > 7] = 1.


$$

### Set Notation and Bracket Notation

The set-based notation from the previous lesson is a special case of Iverson bracket notation. Specifically,

$$


\mathbf{1}_A(x) = \mathbf{1}[x \in A].


$$

Both expressions equal $1$ when $x \in A$ and $0$ when $x \notin A.$

The Iverson bracket is more flexible because it works with any predicate, such as inequalities. For example:

$$


\begin{aligned}1 & if \,𝑥<0 \\ 0 & if \,𝑥≥0.\end{aligned}


$$

### Example: Converting Indicator Notations

#### Question

Let $H = \{-5, -3, -1, 1\}.$ Which of the following is equivalent to $\mathbf{1}_H(0)?$

1. $\mathbf{1}[0 \in \{-5, -3, -1, 1\}]$

2. $\mathbf{1}[0 \notin \{-5, -3, -1, 1\}]$

3. $\mathbf{1}[H \in \{-5, -3, -1, 1\}]$

4. $\mathbf{1}[\{-5, -3, -1, 1\} \in 0]$

5. $\mathbf{1}[0 = H]$

#### Explanation

The indicator function $\mathbf{1}[P]$ equals $1$ if the predicate $P$ is true and $0$ if $P$ is false.

$$


\begin{aligned}1, & if P is true, \\ 0, & if P is false.\end{aligned}


$$

Recall that the indicator function $\mathbf{1}_H(x)$ of a set $H$ equals $1$ if $x \in H$ and $0$ if $x \notin H.$ This can be written using Iverson bracket notation as

$$


\mathbf{1}_H(x) = \mathbf{1}[x \in H].


$$

Therefore, we have

$$


\mathbf{1}_H(0) = \mathbf{1}[0 \in H] = \mathbf{1}[0 \in \{-5, -3, -1, 1\}].


$$

### Using Indicator Functions in Expressions: Sums

Indicator functions are useful for writing expressions that behave differently depending on whether a condition is met.

**Sums with indicator functions.** When we multiply a term by an indicator function inside a sum, the indicator acts as a filter. For example, given values $x_1, x_2, \ldots, x_n,$ the sum

$$


\sum_{i=1}^{n} \mathbf{1}[x_i > 0] \cdot x_i


$$

adds up only the positive values. If $x_i > 0,$ the indicator equals $1$ and the term contributes $x_i.$ If $x_i \leq 0,$ the indicator equals $0$ and the term contributes nothing.

Consider the values $x_1 = 5, x_2 = -3, x_3 = 2.$ Using the formula:

$$


\begin{aligned}\underset{\underset{𝑖=1}{∑}}{\overset{}{3}}𝟏[𝑥_{𝑖}>0]⋅𝑥_{𝑖} & =𝟏[5>0]⋅5+𝟏[−3>0]⋅(−3)+𝟏[2>0]⋅2 \\ & =1⋅5+0⋅(−3)+1⋅2 \\ & =5+0+2 \\ & =7.\end{aligned}


$$

Similarly, $\sum_{i=1}^{n} \mathbf{1}[x_i > 0]$ counts the positive values. For this data, the count is $1 + 0 + 1 = 2.$

### Using Indicator Functions in Expressions: Piecewise Functions

Indicator functions can also express piecewise functions compactly. Consider the absolute value function:

$$


\begin{aligned}𝑥, & if x \geq 0, \\ −𝑥, & if x < 0.\end{aligned}


$$

We can write this as a single expression using indicator functions:

$$


|x| = \mathbf{1}[x \geq 0] \cdot x + \mathbf{1}[x < 0] \cdot (-x).


$$

Since the conditions $x \geq 0$ and $x < 0$ are mutually exclusive, exactly one indicator equals $1$ and the other equals $0.$ This "switch" mechanism selects the appropriate term automatically.

Let's verify this expression for a negative number, say $x = -4{:}$

$$


\begin{aligned}|−4| & =𝟏[−4≥0]⋅(−4)+𝟏[−4<0]⋅(−(−4)) \\ & =0⋅(−4)+1⋅4 \\ & =4.\end{aligned}


$$

### Example: Using Indicator Functions in Expressions

#### Question

Consider the function

$$


f(x) = \mathbf{1}[x \geq 1] \cdot x^2 + \mathbf{1}[x < 1] \cdot (-x).


$$

What is $f(-2)?$

#### Explanation

The indicator function $\mathbf{1}[P]$ equals $1$ if the predicate $P$ is true and $0$ if $P$ is false.

$$


\begin{aligned}1, & if P is true, \\ 0, & if P is false.\end{aligned}


$$

For $x = -2,$ we evaluate each indicator function:

- $\mathbf{1}[x \geq 1] = \mathbf{1}[-2 \geq 1] = 0$ (since $-2 \geq 1$ is false)

- $\mathbf{1}[x < 1] = \mathbf{1}[-2 < 1] = 1$ (since $-2 < 1$ is true)

Substituting into the expression for $f(x),$ we get

$$


\begin{aligned}𝑓(−2) & =𝟏[−2≥1]⋅(−2)^{2}+𝟏[−2<1]⋅(−(−2)) \\ & =0⋅4+1⋅2 \\ & =2.\end{aligned}


$$

Note that the indicator functions act as a "switch": since $x = -2 < 1,$ the first term vanishes and only the second term contributes to the result.
