# Self-Dual Boolean Functions

Source: https://www.mathacademy.com/topics/3785?courseId=109
Topic ID: 3785

## Prerequisites

- [Boolean Functions And Logical Operations](./3779-boolean-functions-and-logical-operations.md)

## Lesson

### Introduction

The **dual Boolean function** $f^d$ of a Boolean function $f$ is defined as

$$



f^d(x_1,x_2,\ldots,x_n) = \lnot f(\lnot x_1, \lnot x_2,\ldots, \lnot x_n).



$$

To demonstrate, let's find the dual Boolean function of $f(x_1,x_2) \equiv x_1 \lor x_2.$ In this case, we have

$$



\begin{aligned}𝑓^{𝑑}(𝑥_{1},𝑥_{2}) & ≡¬𝑓(¬𝑥_{1},¬𝑥_{2}) \\ & ≡¬(¬𝑥_{1}∨¬𝑥_{2}) \\ & ≡¬(¬𝑥_{1})∧¬(¬𝑥_{2}) \\ & ≡𝑥_{1}∧𝑥_{2}.\end{aligned}



$$

### Example: Constructing a Dual Function

#### Question

Find the dual Boolean function of $f(x_1,x_2,x_3) \equiv (x_1 \mid x_2) \lor x_3.$

#### Explanation

The dual Boolean function of $f$ is the function $f^d$ defined by

$$



f^d(x_1,x_2,x_3, \ldots,x_n) = \lnot f(\lnot x_1, \lnot x_2,\lnot x_3,\ldots, \lnot x_n).



$$

In our case, we have

$$



\begin{aligned}𝑓^{𝑑}(𝑥_{1},𝑥_{2},𝑥_{3}) & ≡¬𝑓(¬𝑥_{1},¬𝑥_{2},¬𝑥_{3}) \\ & ≡¬((¬𝑥_{1}∣¬𝑥_{2})∨¬𝑥_{3}) \\ & ≡¬(¬(¬𝑥_{1}∧¬𝑥_{2})∨¬𝑥_{3}) \\ & ≡¬(¬(¬𝑥_{1}∧¬𝑥_{2}))∧¬(¬𝑥_{3}) \\ & ≡(¬𝑥_{1}∧¬𝑥_{2})∧𝑥_{3} \\ & ≡¬𝑥_{1}∧¬𝑥_{2}∧𝑥_{3}.\end{aligned}



$$

### Example: Constructing a Dual Function From a Table

#### Question

In the table below, fill the corresponding dual value of Boolean function $f^d$ of $f.$

#### Explanation

The dual Boolean function of $f$ is the function $f^d$ defined by

$$



f^d(x_1,x_2,\ldots,x_n) = \lnot f(\lnot x_1, \lnot x_2,\ldots, \lnot x_n).



$$

Therefore, we have the following:

- $f^d(0,0) = \lnot f(\lnot \, 0, \lnot \, 0) = \lnot f(1, 1) = \lnot \, 1 = \boxed{\color{blue}0}$

- $f^d(0,1) = \lnot f(\lnot \, 0, \lnot \, 1) = \lnot f(1, 0) = \lnot \, 1 = \boxed{\color{blue}0}$

- $f^d(1,0) = \lnot f(\lnot \, 1, \lnot \, 0) = \lnot f(0, 1) = \lnot \, 0 = \boxed{\color{blue}1}$

- $f^d(1,1) = \lnot f(\lnot \, 1, \lnot \, 1) = \lnot f(0, 0) = \lnot \, 1 = \boxed{\color{blue}0}$

Now, the completed table is presented below

### Self-Dual Functions

A Boolean function is **self-dual** if it is negated by negating all inputs:

$$



f(\lnot x_1, \lnot x_2, \ldots, \lnot x_n) = \lnot f(x_1,x_2,\ldots,x_n)



$$

In other words, a self-dual function has opposite values on opposite binary tuples of variable values.

A self-dual Boolean function is equivalent to its dual, $f\equiv f^d.$

Consider the Boolean function $f$ given by its table below. Let's determine whether $f$ is self-dual.

In this case, the function isn't self-dual. Indeed, for the tuple $(0,0,1),$ we have

$$



f(0,0,1)=0.



$$

But for the opposite tuple $(1,1,0),$ we have

$$



f(1,1, 0) = 0 \neq 1.



$$

So, our function doesn't have opposite values on opposite tuples:

$$



f(0,0,1) \neq \neg f(1,1,0)



$$

Therefore, the function is not self-dual.

### Example: Identifying Self-Dual Functions Using Tables

#### Question

Which of the Boolean functions $f_1,f_2,f_3$ are self-dual?

#### Explanation

A Boolean function is self-dual if it is negated by negating all inputs:

$$



f(\lnot x_1, \lnot x_2, \ldots, \lnot x_n) = \lnot f(x_1,x_2,\ldots,x_n)



$$

This is equivalent to $f\equiv f^d,$ where $f^d$ is the dual Boolean function of $f.$

In other words, a self-dual function has opposite values on opposite binary tuples of variable values.

With that in mind, let's examine our functions.

- Function $f_1$ is ** self-dual. Notice that $f_1(0,1,1)=1$ but $f_1(1,0,0) \neq 0.$

- Function $f_2$ is self-dual. Indeed, it has opposite values on opposite tuples of variables' values. $f_2(0,0,0) = 1$ and $f_2(1,1,1)=0,$ $f_2(0,0,1) = 0$ and $f_2(1,1,0)=1,$ $f_2(0,1,0) = 0$ and $f_2(1,0,1)=1,$ $f_2(0,1,1) = 1$ and $f_2(1,0,0)=0.$

- Function $f_3$ is ** self-dual. Notice that $f_3(0,0,1)=1$ but $f_3(1,1,0) \neq 0.$

Therefore, the correct answer is "$f_2$ only."

### Example: Identifying Self-Dual Functions

#### Question

Which of the following Boolean functions of two variables are self-dual?

1. $f(x_1,x_2,x_3) \equiv (x_1 \oplus x_2) \oplus x_3$

2. $g(x_1,x_2,x_3) \equiv x_1 \Leftrightarrow (x_2\lor x_3)$

3. $h(x_1,x_2,x_3)\equiv x_1\land x_2$

#### Explanation

A Boolean function is self-dual if it is negated by negating all inputs:

$$



f(\lnot x_1, \lnot x_2, \ldots, \lnot x_n) = \lnot f(x_1,x_2,\ldots,x_n)



$$

This is equivalent to $f\equiv f^d,$ where $f^d$ is the dual Boolean function of $f.$

In other words, a self-dual function has opposite values on opposite binary tuples of the variables' values.

The tables corresponding to our functions are the following:

With that in mind, let's examine our functions.

- Function I is self-dual. Indeed, it has opposite values on opposite tuples of variables' values. $f(0,0,0) = 0$ and $f(1,1,1)=1,$ $f(0,0,1) = 1$ and $f(1,1,0)=0,$ $f(0,1,0) = 1$ and $f(1,0,1)=0,$ $f(0,1,1) = 0$ and $f(1,0,0)=1.$

- Function II is ** self-dual. Notice that $g(0,0,0)=1$ but $g(1,1,1) \neq 0.$

- Function III is ** self-dual. Notice that $h(0,1,1)=0$ but $h(1,0,0) \neq 1.$

Therefore, the correct answer is "I only."
