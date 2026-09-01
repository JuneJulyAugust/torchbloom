# Recursive Sequences

Source: https://www.mathacademy.com/topics/1226?courseId=44
Topic ID: 1226

## Prerequisites

- [Introduction to Sequences](./2271-introduction-to-sequences.md)
- [Identifying Patterns](../../../../elementary-school/lessons/grade-4/2431-identifying-patterns.md)

## Lesson

### Introduction

Some sequences are defined **recursively**, which means that there is a formula to get from one term to the next.

For example, suppose that we have the following formula:

$$


a_{n+1}=a_n+{\color{blue}{2}}, \quad a_1 = {\color{red}{3}}


$$

In this formula,

- the statement $a_{n+1} = a_n + {\color{blue}{2}}$ means "to get to the next term, we add ${\color{blue}{2}}$ to the previous term," and

- the statement $a_1 = {\color{red}{3}}$ tells us that the first term is ${\color{red}{3}}.$

So how do we calculate $a_2$, the next term in the sequence? Easy! We plug $n=1$ into the formula:

$$


\begin{aligned}𝑎_{𝑛+1} & =𝑎_{𝑛}+2 \\ 𝑎_{1+1} & =𝑎_{1}+2 \\ 𝑎_{2} & =𝑎_{1}+2 \\ 𝑎_{2} & =3+2 \\ 𝑎_{2} & =5\end{aligned}


$$

Now that we know $a_2,$ we can find $a_3$ by plugging in $n=2$ into the formula:

$$


\begin{aligned}𝑎_{𝑛+1} & =𝑎_{𝑛}+2 \\ 𝑎_{2+1} & =𝑎_{2}+2 \\ 𝑎_{3} & =𝑎_{2}+2 \\ 𝑎_{3} & =5+2 \\ 𝑎_{3} & =7\end{aligned}


$$

We can keep going by substituting $n=3,4,5,$ and so on. The resulting terms of the sequence are as follows:

$$


3,\qquad 5,\qquad 7,\qquad 9,\qquad 11,\ldots


$$

### Example: Computing the Second Term of a Sequence

#### Question

If $a_{n+1}=2a_n-3$ with $a_1=4,$ then find the value of $a_2.$

#### Explanation

The recursive formula is

$$


a_{n+1}=2a_n - 3


$$

where $a_1={\color{blue}4}.$

We compute $a_2$ by substituting $n=1$ into the recursive formula:

$$


\begin{aligned}𝑎_{𝑛+1} & =2𝑎_{𝑛}−3 \\ 𝑎_{1+1} & =2𝑎_{1}−3 \\ 𝑎_{2} & =2𝑎_{1}−3 \\ 𝑎_{2} & =2(4)−3 \\ 𝑎_{2} & =5\end{aligned}


$$

Therefore, $a_2=5.$

### Example: Computing the Third Term of a Sequence

#### Question

Given the recursive sequence $a_{n+1} = 3a_n-2$ with $a_1=2,$ what is the value of $a_3?$

#### Explanation

The recursive formula is

$$


a_{n+1} = 3a_n-2,


$$

where $a_1={\color{blue}2}.$

We use this formula to compute the terms $a_2$ and $a_3$ as follows:

- We first compute $a_2$ by substituting $n=1$ into the recursive formula:

- Then, we compute $a_3$ by substituting $n=2$ into the recursive formula:

Therefore, $a_3=10.$

### Example: Recursive Sequences in Function Notation

#### Question

If $f(n+1) = 2f(n) + 1$ with $f(1) = 3,$ then what is $f(4)?$

#### Explanation

The recursive formula is

$$


f(n+1) = 2f(n) + 1,


$$

where $f(1) = {\color{blue}3}.$

We use this formula to compute the terms $f(2), f(3),$ and $f(4)$ as follows:

- To compute $f(2),$ we substitute $n = 1$ into the recursive formula:

- To compute $f(3),$ we substitute $n=2$ into the recursive formula:

- To compute $f(4),$ we substitute $n=3$ into the recursive formula:

Therefore, the fourth term of the sequence is $f(4) = 31.$

### Example: Writing a Recursive Formula for a Sequence

#### Question

Consider the following sequence:

$$


1, \quad 6, \quad 11, \quad 16, \quad 21, \quad 26, \quad \dots


$$

The recursive formula for this sequence is given by

$$


f(n+1) = f(n) + \boxed{\phantom{A}}\,, \qquad f(1) = \boxed{\phantom{A}}\,.


$$

From left to right, what are the missing values?

#### Explanation

Notice that the first term of the sequence is $f(1) = {\color{blue}1}.$

Inspecting the terms of the sequence, we see that we always get the next term by adding ${\color{red}5}.$

Therefore, the recursive rule must be the following:

$$


f(n+1) = f(n) + \boxed{{\color{red}5}}\,, \qquad f(1) = \boxed{{\color{blue}1}}


$$

So, the missing values are $5$ and $1.$
