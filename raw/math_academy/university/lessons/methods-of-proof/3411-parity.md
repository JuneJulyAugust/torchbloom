# Parity

Source: https://www.mathacademy.com/topics/3411?courseId=76
Topic ID: 3411

## Prerequisites

- [Formal and Informal Language](./2798-formal-and-informal-language.md)

## Lesson

### Introduction

In this lesson, we'll learn how to prove universal statements that involve the evenness and oddness of simple expressions.

First, we have the following definitions:

- Two integers have the **same parity** if they're *both* even or *both* odd.

- Two integers have **opposite parity** if *one* of them is even and the *other* is odd.

For example:

- The integers $2$ and $4$ have the *same* parity because they're both even.

- The integers $1$ and $7$ have the *same* parity because they're both odd.

- On the other hand, the integers $1$ and $6$ have *opposite* parity because $1$ is odd and $6$ is even.

### Representing Even Integers

The list below gives the first few even integers:

$$


0, \quad \pm 2, \quad \pm 4, \quad \pm 6, \quad \pm 8, \quad \ldots


$$

An integer is even if it is a multiple of $2.$ And, since every integer is a multiple of its factors, every even integer can be written as

$$


{\color{red}{2}}\times {\color{blue}{\text{some other integer}}}.


$$

For example:

$$


\begin{aligned}0 & =2×0 \\ 2 & =2×1 \\ 4 & =2×2 \\ 12 & =2×6 \\ −24 & =2×(−12)\end{aligned}


$$

Suppose we know that an integer $n$ is even. Then, we can rewrite $n$ as follows:

$$


n={\color{red}{2}}{\color{blue}{a}}


$$

where ${\color{blue}{a}}$ is an integer.

This choice of letter for the second factor is arbitrary: we chose ${\color{blue}{a}}$ here, but we can use any letter we like! However, the following variables are commonly used to denote integers:

$$


a, \quad b, \quad c, \quad k, \quad l, \quad m, \quad n, \quad p, \quad q, \quad r, \quad x, \quad y, \quad z


$$

### Showing an Expression Is Even

Consider the following statement:

$\qquad$ $P:\: \forall n\in\mathbb Z,\, 8n-4$ *is even.*

To prove this statement, we need to show that $8n-4$ can be written as $2{\color{blue}{a}},$ where ${\color{blue}{a}}$ is an integer.

The first step is to factor out $2$ from the expression.

$$


8n-4 = 2(4n-2)


$$

Next, we introduce a new variable ${\color{blue}{a}},$ where

$$


{\color{blue}{a}} = 4n-2.


$$

Notice that since $n\in\mathbb Z,$ we have that $4n-2\in\mathbb Z.$ In other words, ${\color{blue}{a}}\in\mathbb Z.$ It's essential to state this since the whole argument breaks down if the second factor is sometimes not an integer.

Now, our expression can be written as

$$


2(4n-2) = 2{\color{blue}{a}}.


$$

So, since $8n-4$ can be written in the form $2{\color{blue}{a}}$ where ${\color{blue}{a}}$ is an integer, we conclude that $8n-4$ is even *for all* $n\in\mathbb Z.$

Let's take a look at another example. Before we do, note that statements about parity are often written informally, and so the universal quantifier $\forall$ is usually hidden.

### Example: Showing a Linear Expression Is Even

#### Question

Suppose $n=10-30p,$ where $p \in \mathbb{Z}.$ Construct an argument that explains why $n$ is even.

#### Explanation

An integer is ** if it can be written as $2a,$ where $a$ is an integer.

Therefore, we complete our argument as follows:

The number $n$ is even since

$$


\begin{aligned}𝑛 & =10−30𝑝 \\ & =2(\underset{𝑎}{\underset{}{5−15𝑝}}) \\ & =2𝑎,\end{aligned}


$$

where we have defined $a=\boxed{\color{blue}5-15p},$ which is an integer.

### Representing Odd Integers

Recall that an integer is *odd* if it is not even. The list below gives the first few odd integers:

$$


\pm 1, \quad \pm 3, \quad \pm 5, \quad \pm 7, \quad \ldots


$$

Notice that every odd integer can be expressed as

$$


{\color{red}{2}}\times {\color{blue}{\text{some other integer}}} + 1.


$$

For example:

$$


\begin{aligned}1 & =2×0+1 \\ 3 & =2×1+1 \\ 5 & =2×2+1 \\ 19 & =2×9+1 \\ −17 & =2×(−9)+1\end{aligned}


$$

In general, an integer $n$ is odd if it can be written as

$$


n={\color{red}{2}}{\color{blue}{a}}+1


$$

where $\color{blue}a$ is an integer.

### Showing a Statement Is Odd

Consider the following statement:

$\qquad$ $P:\: \forall n\in\mathbb Z,\, 4n+7$ *is odd.*

To prove this statement, we need to show that it can be written as $2{\color{blue}{a}}+1,$ where ${\color{blue}{a}}$ is an integer.

The first step is to rewrite the expression by isolating $+1.$ We can do this by decomposing $7$ into $6+1,$ as follows:

$$


4n+7 = 4n+6+1 = (4n+6)+1


$$

Next, we factor out $2$ from the expression in parentheses:

$$


(4n+6)+1 = 2(2n+3) + 1


$$

Then, we introduce a new variable ${\color{blue}{a}},$ where

$$


{\color{blue}{a}} = 2n+3.


$$

Notice that since $n\in\mathbb Z,$ we have that $2n+3\in\mathbb Z.$ In other words, ${\color{blue}{a}}\in\mathbb Z.$

This means our original expression can be written as

$$


2(2n+3) + 1= 2{\color{blue}{a}} + 1.


$$

So, since $4n+7$ can be written in the form $2{\color{blue}{a}}+1$ where ${\color{blue}{a}}$ is an integer, we conclude that $4n+7$ is odd *for all* $n\in\mathbb Z.$

### Example: Showing a Linear Expression Is Odd

#### Question

Suppose $n=3-4m,$ where $m \in \mathbb{Z}.$ Construct an argument that explains why $n$ is odd.

#### Explanation

An integer is ** if it can be written as $2a + 1,$ where $a$ is an integer.

Therefore, we complete our argument as follows:

The number $n$ is ** since

$$


\begin{aligned}𝑛 & =3−4𝑚 \\ & =(−4𝑚+2)+1 \\ & =2(\underset{𝑎}{\underset{}{−2𝑚+1}})+1 \\ & =2𝑎+1,\end{aligned}


$$

where we have defined $a=\boxed{\color{blue}-2m+1},$ which is an integer.

### Example: Proving Parity of Non-Linear Expressions

#### Question

Suppose $n=4m^2+2m-1,$ where $m \in \mathbb{Z}.$ Construct an argument that explains why $n$ is odd.

#### Explanation

An integer is ** if it can be written as $2a + 1,$ where $a$ is an integer.

Now, note the following regarding the expression $4m^2+2m-1{:}$

- All terms, apart from the constant term, have a common factor of $2.$

- The constant term can be written as $-1 = -2+1.$

Therefore, we complete our argument as follows:

The number $n$ is $\boxed{\color{blue}\text{odd}}$ since

$$


\begin{aligned}𝑛 & =4𝑚^{2}+2𝑚−1 \\ & =(4𝑚^{2}+2𝑚−2)+1 \\ & =2(\underset{𝑎}{\underset{}{2𝑚^{2}+𝑚−1}})+1 \\ & =2𝑎+1,\end{aligned}


$$

where $a=\boxed{\color{blue}2m^2+m-1}$ is an integer.

### Example: Proving Parity of Non-Linear Expressions With Multiple Variables

#### Question

Suppose $n=2pq - 4q + 5,$ where $p,q \in \mathbb{Z}.$ Construct an argument that explains why $n$ is odd.

#### Explanation

An integer is ** if it can be written as $2a + 1,$ where $a$ is an integer.

Now, note the following regarding the expression $2pq - 4q + 5 {:}$

- All terms, apart from the constant term, have a common factor of $2.$

- The constant term can be written as $5 = 4+1.$

Therefore, we complete our argument as follows:

The number $n$ is $\boxed{\color{blue}\text{odd}}$ since

$$


\begin{aligned}𝑛 & =2𝑝𝑞−4𝑞+5 \\ & =(2𝑝𝑞−4𝑞+4)+1 \\ & =2(\underset{𝑎}{\underset{}{𝑝𝑞−2𝑞+2}})+1 \\ & =2𝑎+1,\end{aligned}


$$

where $a= \boxed{\color{blue} pq - 2q + 2\in \mathbb Z}.$
