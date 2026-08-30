# Monotonic Boolean Functions

Source: https://www.mathacademy.com/topics/3786?courseId=109
Topic ID: 3786

## Prerequisites

- [Boolean Functions And Logical Operations](./3779-boolean-functions-and-logical-operations.md)
- [Conditional Statements With Predicates](../methods-of-proof/4257-conditional-statements-with-predicates.md)

## Lesson

### Introduction

For two binary tuples $(x_1,x_2,\ldots,x_n)$ and $(y_1,y_2,\ldots,y_n),$ we say that

$$



(x_1,x_2,\ldots,x_n) \leq (y_1,y_2,\ldots,y_n)



$$

if $x_i \leq y_i$ for all $i=1,2\ldots,n.$ Similarly, we say

$$



(x_1,x_2,\ldots,x_n) \geq (y_1,y_2,\ldots,y_n)



$$

if $x_i \geq y_i$ for all $i=1,2\ldots,n.$ If neither of these conditions is satisfied, we say that the tuples are **not comparable**.

Let's compare the binary tuple $(0,1)$ to $(1,1),$ $(0,0),$ and $(1,0).$

- We have that $(0,1) \leq (1,1)$ since the components of the first tuple are less than or equal to the corresponding components of the second tuple: $1$st components: $0 \leq 1$ $2$nd components: $1 \leq 1$

- We have that $(0,1) \geq (0,0)$ since the components of the first tuple are greater than or equal to the corresponding components of the second tuple: $1$st components: $0 \geq 0$ $2$nd components: $1 \geq 0$

- The tuples $(0,1)$ and $(1,0)$ are not comparable since, for the $1$st components, we have $0 \leq 1,$ while for the $2$nd components, we have $1 \geq 0$ (the inequalities are opposite).

### Example: Comparing Binary Tuples

#### Question

Compare the binary tuples below.

- $(0,0,0)$ and $(1,0,1)$

- $(1,0,0)$ and $(0,1,1)$

- $(1,1,1)$ and $(0,0,1)$

#### Explanation

We say that

$$



(x_1,x_2,\ldots,x_n) \leq (y_1,y_2,\ldots,y_n)



$$

if $x_i \leq y_i$ for all $i=1,2,\ldots,n.$ Similarly,

$$



(x_1,x_2,\ldots,x_n) \geq (y_1,y_2,\ldots,y_n)



$$

if $x_i \geq y_i$ for all $i=1,2,\ldots,n.$ If neither of these conditions is satisfied, we say that the tuples are **.

With that in mind, let's examine our tuples.

- We have that $(0,0,0) \boxed{\color{blue}\leq} (1,0,1)$ since the components of the first tuple are smaller than or equal to the corresponding components of the second tuple: $1$st components: $0 \leq 1$ $2$nd components: $0 \leq 0$ $3$rd components: $0 \leq 1$

- The tuples $(1,0,0)$ and $(0,1,1)$ are not comparable since, for the $1$st components, we have $1 \geq 0,$ while for the $2$nd components, we have $0 \leq 1$ (the inequalities are opposite).

- We have that $(1,1,1) \boxed{\color{blue}\geq} (0,0,1)$ since the components of the first tuple are greater than or equal to the corresponding components of the second tuple: $1$st components: $1 \geq 0$ $2$nd components: $1 \geq 0$ $3$rd components: $1 \geq 1$

### Monotonic Boolean Functions

A boolean function $f$ is called **monotonic** if, for any comparable pair of binary tuples, we have

$$



(x_1,x_2,\ldots,x_n) \leq (y_1,y_2,\ldots,y_n) \quad \Rightarrow \quad f(x_1,x_2,\ldots,x_n) \leq f(y_1,y_2,\ldots,y_n).



$$

Consider the Boolean function $f$ given below.

In this case, the function is not monotonic. To demonstrate this, consider the tuples $(0,0)$ and $(1,0).$

Notice that

$$



(0,0) \boxed{\leq} (1,0),



$$

but for the corresponding outputs, we have

$$



f(0,0) = 1 \boxed{>} 0 = f(1,0).



$$

This contradicts the definition of monotonic functions.

### Example: Identifying Monotonic Boolean Functions From Tables

#### Question

Which of the Boolean functions $f_1,f_2,f_3$ given below are monotonic?

#### Explanation

A boolean function is monotonic if, for any comparable pair of binary tuples, we have

$$



(x_1,x_2,\ldots,x_n) \leq (y_1,y_2,\ldots,y_n) \quad \Rightarrow \quad f(x_1,x_2,\ldots,x_n) \leq f(y_1,y_2,\ldots,y_n).



$$

With that in mind, let's examine our functions.

- Function $f_1$ is not monotonic. Notice that $(1,1,0) \leq (1,1,1)$ but $f_1(1,1,0) > f_1(1,1,1).$

- Function $f_2$ is monotonic. Indeed, for any comparable pair of binary tuples, we have

- Function $f_3$ is not monotonic. Notice that $(0,1,0) \leq (0,1,1)$ but $f_3(0,1,0) \gt f_3(0,1,1).$

Therefore, the correct answer is "$f_2$ only."

### Example: Identifying Monotonic Boolean Functions of Two Variables

#### Question

Which of the following boolean functions of two variables are monotonic?

1. $f(x_1,x_2) \equiv \lnot x_1$

2. $g(x_1,x_2) \equiv x_1 \land x_2$

3. $h(x_1,x_2) \equiv x_1 \downarrow x_2$

#### Explanation

A boolean function is monotonic if, for any comparable pair of binary tuples, we have

$$



(x_1,x_2,\ldots,x_n) \leq (y_1,y_2,\ldots,y_n) \quad \Rightarrow \quad f(x_1,x_2,\ldots,x_n) \leq f(y_1,y_2,\ldots,y_n).



$$

The tables corresponding to our functions are the following:

With that in mind, let's examine our functions.

- Function I is ** monotonic since $(0,0) \leq (1,0)$ but $f(0,0) > f(1,0).$

- Function II is monotonic. Indeed, for any comparable pair of binary tuples, we have Namely: $(0,0) \leq (0,1)$ and $g(0,0) \leq g(0,1)$ $(0,0) \leq (1,0)$ and $g(0,0) \leq g(1,0)$ $(0,0) \leq (1,1)$ and $g(0,0) \leq g(1,1)$ $(0,1)$ and $(1,0)$ are not comparable $(0,1) \leq (1,1)$ and $g(0,1) \leq g(1,1)$ $(1,0) \leq (1,1)$ and $g(1,0) \leq g(1,1)$

- Function III is ** monotonic since $(0,0) \leq (0,1)$ but $h(0,0) > h(0,1).$

Therefore, the correct answer is "II only."
