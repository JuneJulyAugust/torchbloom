# Introduction to Recurrence Relations

Source: https://www.mathacademy.com/topics/1989?courseId=109
Topic ID: 1989

## Prerequisites

- [Fibonacci Sequences](../algebra-i/73-fibonacci-sequences.md)

## Lesson

### Introduction

A **recurrence relation** is an equation defining a sequence of values in terms of previous terms.

Let's consider the recurrence relation given by

$$



a_n = 2 a_{n-1} + 6, \qquad a_1=0, \quad n \geq 2.



$$

Here, the first term is $a_1=0.$ All the succeeding terms for $n \geq 2,$ are obtained using the main equation

$$



a_n = 2 a_{n-1} + 6.



$$

To find, for instance, the fourth term of the corresponding sequence, we start with the first term

$$



a_1 = 0.



$$

We compute the next terms using the recursive formula until we reach the fourth term.

- To get $a_2$, we substitute $a_1=0$ into the recurrence relation:

- To get $a_3$, we substitute $a_2=6$ into the recurrence relation:

- To get $a_4$, we substitute $a_3=18$ into the recurrence relation:

Therefore, the fourth term is $a_{4}= 42.$

### Example: Finding Elements of a Relation Using a Recursive Formula

#### Question

Find the fourth term of the sequence given by the recurrence relation

$$



a_n = 5a_{n-1}+a_{n-2}, \qquad a_1 = 2, \quad a_2 = 1, \quad n \geq 3.



$$

#### Explanation

Starting with the initial terms $a_1 = 2,$ and $a_2 = 1,$ we compute the next terms using the recursive formula until we reach the fourth term.

$$



\begin{aligned}𝑎_{1} & =2 \\ 𝑎_{2} & =1 \\ 𝑎_{3} & =5𝑎_{2}+𝑎_{1}=5⋅1+2=5+2=7 \\ 𝑎_{4} & =5𝑎_{3}+𝑎_{2}=5⋅7+1=35+1=36\end{aligned}



$$

Therefore, the fourth term is $a_4 = 36.$

### Orders of Recurrence Relations

The **order** of a recurrence relation is the largest index difference between $a_n$ and the preceding terms in the relation. We have a **first-order** recurrence relation if $a_n$ depends only on the immediately preceding term $a_{n-1}$ and on the index $n{:}$

$$



a_n = f(a_{n-1},n)



$$

For example,

$$



a_n = 2a_{n-1} + 6, \qquad a_1=0,\quad n \geq 2



$$

is a first-order recurrence relation since $a_n$ depends only on the term $a_{n-1}.$

Similarly, we have a **second-order** recurrence relation if $a_n$ depends only on the two previous terms $a_{n-1}, a_{n-2}$ and $n{:}$

$$



a_n = f(a_{n-1},a_{n-2},n)



$$

For instance,

$$



a_n = 3a_{n-1}-4a_{n-2}, \qquad a_1=2, \quad a_2=1,\quad n \geq 3



$$

is a second-order recurrence relation since $a_n$ depends on $a_{n-1}$ and $a_{n-2}.$

In general, a **$k$th-order** recurrence relation depends on the last $k$ terms and $n{:}$

$$



a_n = f(a_{n-1},\ldots,a_{n-k},n)



$$

### Linear and Nonlinear Recurrence Relations

A recurrence relation is **linear (with constant coefficients)** if it expresses $a_n$ as a sum of previous terms $a_{n-1}, \dots, a_{n-k}$ with constant coefficients, together with possibly a final term that depends only on $n{:}$

$$



a_n = s_{1}a_{n-1} + s_{2}a_{n-2} + \ldots + s_{k}a_{n-k} + g(n)



$$

where $s_1, s_2, \ldots, s_k$ are constants and $g(n)$ is a function, often called a **forcing function**, that does not involve $a_n$ or its preceding terms. We will not consider the case of non-constant coefficients, so we won't always be explicit about the "with constant coefficients" part.

For example,

$$



a_n = 5a_{n-1}+6a_{n-2}+7a_{n-3}+5, \qquad a_1=2, \quad a_2=3,\quad a_3 = 4, \quad n \geq 4



$$

is linear because the terms $a_{n-1}, a_{n-2},$ and $a_{n-3}$ occur in the first power with the respective constant coefficients of $5,$ $6,$ and $7$.

Similarly, a recurrence relation is not linear if the previous terms are raised to powers greater than one, multiplied together, or appear inside non-linear functions (such as exponentials, trigonometric functions, or logarithms).

For example,

$$



a_n = a_{n-1}^3 +1, \qquad a_1=2, \quad n \geq 2



$$

is not linear since the term $a_{n-1}$ is raised to the power of $3.$

### Homogeneous and Inhomogeneous Recurrence Relations

A *linear* recurrence relation (with constant coefficients) is **homogeneous** if the forcing function is zero.

In other words, the linear recurrence relation

$$



a_n = s_1a_{n-1} + s_2a_{n-2} + \ldots + s_ka_{n-k} + g(n),



$$

is homogeneous if $g(n) = 0$ for all $n,$ and $s_i$ is constant for each $i.$ For instance,

$$



a_n = 5a_{n-1}+ 2a_{n-2}+3a_{n-3}, \qquad a_1 = 2, \quad a_2=1,\quad a_3 = 6, \quad n\geq 4



$$

is homogeneous since it contains only the preceding terms $a_{n-1}, a_{n-2},$ and $a_{n-3}$ in the recurrence relation with their respect constant coefficients of $5,$ $2,$ and $3.$

On the other hand, a linear recurrence relation with $g(n) \neq 0$ is called **inhomogeneous**. For example,

$$



a_n = 2a_{n-1}-3a_{n-2} + 6n^2, \qquad a_1 = -2,\quad a_2=0, \quad n \geq 3



$$

is not homogeneous because of the term $g(n) = 6n^2.$

### Example: Classifying Recurrence Relations

#### Question

Which of the following linear recurrence relations are homogeneous?

1. $a_n = a_{n-1} + 5a_{n-2}+n$

2. $b_n = 3b_{n-1} -2b_{n-2}$

3. $c_n = 2c_{n-1} + 3c_{n-2}- c_{n-3}$

#### Explanation

A linear recurrence relation (with constant coefficients) is **** if the forcing function is zero.

In other words, the linear recurrence relation

$$



a_n = s_1a_{n-1} + s_2a_{n-2} + \ldots + s_ka_{n-k} + g(n),



$$

is homogeneous if $g(n) = 0$ for all $n,$ and $s_i$ is constant for each $i.$

Let's examine each recurrence relation in turn.

- $a_n$ is not homogeneous. The term $n$ of the expression doesn't contain preceding terms of the relation.

- $b_n$ is homogeneous. The terms of the expression each contain a preceding term, $b_{n-1}$ and $b_{n-2}.$

- $c_n$ is homogeneous. The terms of the expression each contain a preceding term, $c_{n-1},$ $c_{n-2},$ and $c_{n-3}.$

Therefore, the correct answer is "II and III only."

### Example: Fully Classifying Recurrence Relations

#### Question

Fully classify the following recurrence relation:

$$



a_n = a_{n-2} - \dfrac23 a_{n-1}, \qquad a_1 =0, \quad a_2 = 1, \quad n \geq 2.



$$

#### Explanation

Recall the following classifications of recurrence relations:

- The order of a relation $a_n$ is the largest index difference between $a_n$ and the preceding terms in the relation.

- A recurrence relation is ** if it expresses $a_n$ as a sum of previous terms $a_{n-1}, \dots, a_{n-k}$ with constant coefficients, together with possibly a final term that depends only on $n{:}$ where $s_1, s_2, \ldots, s_k$ are constants and $g(n)$ is a function, often called a **, that does not involve $a_n$ or its preceding terms.

- A linear recurrence relation (with constant coefficients) is ** if the forcing function is zero. Otherwise, it is **

Let's classify the relation $a_n = a_{n-2} - \dfrac23 a_{n-1}.$

- The largest index difference between $a_n$ and the preceding terms $a_{n-1}$ and $a_{n-2}$ in the relation is $2.$ So, the relation has order $2.$

- The previous terms $a_{n-1}$ and $a_{n-2}$ occur only in the first power and their coefficients are constants. So, the relation is linear.

- The terms of the expression each contain a preceding term, $a_{n-1}$ and $a_{n-2}.$ So, the relation is homogeneous.

Therefore, the recurrence relation $a_n$ has order $\boxed{\color{blue}2},$ is $\boxed{\color{blue}\text{linear}},$ and is $\boxed{\color{blue}\text{homogeneous}}.$
