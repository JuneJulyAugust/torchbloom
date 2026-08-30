# The Constructive Definition of a Set

Source: https://www.mathacademy.com/topics/46?courseId=55
Topic ID: 46

## Prerequisites

- [Fibonacci Sequences](../algebra-i/73-fibonacci-sequences.md)
- [Solving Elementary Quadratic Inequalities](../integrated-math-iii-honors/1495-solving-elementary-quadratic-inequalities.md)
- [Equivalent Sets](./1976-equivalent-sets.md)

## Lesson

### Introduction

Let's consider the set $E$ containing all positive even numbers.

$$


E = \big\{2,4,6,8,\ldots \big\}


$$

The elements of our set can be generated using the arithmetic sequence

$$


a_n = 2n, \qquad n\in \{1,2,3,4,\ldots\}.


$$

Since $n=\{1,2,3,4,\ldots\}$ is simply the set of natural numbers $\mathbb N,$ we can write our sequence as

$$


a_n = 2n, \qquad n\in \mathbb N.


$$

We can express our original set $E$ using a **constructive definition**, as follows:

$$


E = \big\{ 2n\, : \, n\in\mathbb N \big \}


$$

This notation tells us that to generate the elements of $E,$ we run through all elements of $\mathbb N$ and substitute them into the formula $2n.$

$$


\begin{aligned}𝐸 & ={2𝑛\,:\,𝑛∈ℕ} \\ & ={2(1),\,2(2),\,2(3),\,2(4),\,…} \\ & ={2,4,6,8,…}\end{aligned}


$$

Note the following:

- Under this definition, $2n$ describes a formula or algorithm used to generate all elements of the set.

- When a set is defined constructively, the symbol "$:$" reads as the word "where". So, in words, we can describe the set $E$ as follows: $\qquad$ *$E$ contains all numbers of the form $2n,$ **** $n$ is a natural number.*

- In our definition, $n$ is a **dummy variable**. Its purpose is to describe the logic behind the set's definition and can be replaced with any other variable. For example, we can describe $E$ similarly as follows:

- An alternative to the "constructive definition of a set" terminology is to say the set is written using **set-builder notation**.

- Instead of using a "$:$" symbol to denote the word "where", it's common to use the "$|$" symbol, as follows:

### Example: Listing the Elements of a Set Defined Over a Special Set

#### Question

Consider the set $A,$ defined as

$$


A = \{ (-1)^n \, n : n \in \mathbb{N} \}.


$$

Write down a set that's equivalent to $A$ using ellipsis notation.

#### Explanation

The elements of $A$ are all the terms of the sequence $a_n,$ given by

$$


a_n = (-1)^n \,n, \qquad n \in \mathbb N = \{1,2,3,4,\ldots\}.


$$

Let's write down the first few terms of our sequence:

$$


\begin{aligned}𝑎_{1} & =(−1)^{1}(1)=−1 \\ 𝑎_{2} & =(−1)^{2}(2)=2 \\ 𝑎_{3} & =(−1)^{3}(3)=−3 \\ 𝑎_{4} & =(−1)^{4}(4)=4 \\ & ⋮\end{aligned}


$$

Therefore,

$$


A = \{ -1, 2, -3, 4, \ldots \}.


$$

### Sets Defined Using Indexing Sets

Let's consider the following set:

$$


S = \big\{ 2n+1\, : n\in\{0,1,2,3\} \big \}


$$

The elements of $S$ are all terms of the sequence $a_n,$ given by

$$


a_n = 2n+1, \qquad n\in\{0,1,2,3\}.


$$

Here, the set $n=\{0,1,2,3\}$ is called an **indexing set.**

To write down the elements of $S,$ we first list the terms of our sequence:

$$


\begin{aligned}𝑎_{0} & =2(0)+1=1 \\ 𝑎_{1} & =2(1)+1=3 \\ 𝑎_{2} & =2(2)+1=5 \\ 𝑎_{3} & =2(3)+1=7\end{aligned}


$$

Therefore, we can express the set $S$ equivalently as

$$


S = \{1,3,5,7\}.


$$

### Sets Defined Using Multiple Conditions

Now consider the following set:

$$


A= \big\{ 2n-3\, : \, n\in\mathbb Z,\, -1\leq n\lt 2 \big\}


$$

The conditions after the "$:$" symbol

$$


n \in \mathbb Z,\, -1\leq n\lt 2


$$

state that $n$ is an integer, *and* it must satisfy the inequality $-1\leq n\lt 2$ (in this context, the comma after the first condition represents the word "and").

Therefore, since the only integers that satisfy $-1\leq n\lt 2$ are $-1,0,$ and $1,$ we have

$$


n \in \{-1,0,1\}.


$$

Therefore, the elements of $A$ are all the terms of the sequence $a_n$ given by

$$


a_n = 2n-3, \qquad n \in \{-1,0, 1\}.


$$

Let's write down all the terms of our sequence:

$$


\begin{aligned}𝑎_{−1} & =2(−1)−3=−5 \\ 𝑎_{0} & =2(0)−3=−3 \\ 𝑎_{1} & =2(1)−3=−1\end{aligned}


$$

Therefore, writing out all the elements of $A,$ we get

$$


A = \left\{-5,-3,-1 \right\}.


$$

### Example: Listing the Elements of a Set Defined Over a Finite or Infinite Set

#### Question

Consider the set $A,$ defined as

$$


A = \left \{ 4^n : n \in \mathbb Z,\, -2\leq n\leq 2 \right \}.


$$

Describe $A$ by listing all of its elements.

#### Explanation

The condition after the "$:$" symbol,

$$


n \in \mathbb Z,\, -2\leq n\leq 2


$$

states that $n$ can be any integer that satisfies the inequality $-2\leq n\leq 2.$

Therefore, the elements of $A$ are all the terms of the sequence $a_n,$ given by

$$


a_n = 4^n, \qquad n \in \{0, \pm 1, \pm 2\}.


$$

Let's write down all the terms of our sequence:

$$


\begin{aligned}𝑎_{−2} & =4^{−2}=\frac{1}{16} \\ 𝑎_{−1} & =4^{−1}=\frac{1}{4} \\ 𝑎_{0} & =4^{0}=1 \\ 𝑎_{1} & =4^{1}=4 \\ 𝑎_{2} & =4^{2}=16\end{aligned}


$$

Therefore,

$$


A = \left\{\dfrac{1}{16},\,\dfrac{1}{4},\,1,\,4,\,16 \right\}.


$$

### Example: Listing the Elements of a Set Defined Using a Recursive Sequence

#### Question

Consider the set $A,$ defined as

$$


A = \big \{ a_n \,:\,a_{n+1} = 2a_{n} - 1, \, a_1 = 2,\, n \in \mathbb N \big\}.


$$

Write down a set that's equivalent to $A$ using ellipsis notation.

#### Explanation

The elements of $A$ are all the terms of the ** sequence $a_n,$ given by

$$


a_{n+1} =2a_{n} - 1, \quad a_1 =2,\qquad n \in \mathbb N.


$$

Let's write down the first few terms of our sequence:

$$


\begin{aligned}𝑎_{1} & =2 \\ 𝑎_{2} & =2𝑎_{1}−1 \\ & =2(2)−1 \\ & =3 \\ 𝑎_{3} & =2𝑎_{2}−1 \\ & =2(3)−1 \\ & =5 \\ 𝑎_{4} & =2𝑎_{3}−1 \\ & =2(5)−1 \\ & =9 \\ 𝑎_{5} & =2𝑎_{4}−1 \\ & =2(9)−1 \\ & =17 \\ & ⋮\end{aligned}


$$

Therefore,

$$


A = \left\{2,3,5,9,17,\ldots \right\}.


$$
