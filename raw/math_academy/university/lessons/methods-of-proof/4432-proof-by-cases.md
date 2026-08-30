# Proof by Cases

Source: https://www.mathacademy.com/topics/4432?courseId=76
Topic ID: 4432

## Prerequisites

- [Proving Parity](./4429-proving-parity.md)

## Lesson

### Introduction

To show that a statement is true, we might need to break the proof up into several cases. This method is sometimes called **proof by cases**.

To demonstrate, let's prove the following proposition:

$$


\begin{aligned}𝑛 is an integer \,⇒\,𝑛^{2}−3𝑛 is even \end{aligned}


$$

The integers partition naturally into even and odd numbers, and these two cases cover all possible integers.

$$


\mathbb Z = \big\{0, \pm 2, \pm 4, \ldots\big\} \cup \big\{\pm 1, \pm 3, \pm 5, \ldots\big\}


$$

Therefore, it suffices to prove the following:

$$


\begin{aligned}(𝑛 is even )∨(𝑛 is odd )\,⇒\,𝑛^{2}−3𝑛 is even \end{aligned}


$$

We begin our proof by assuming $n$ is an integer and state that we'll proceed using cases.

*Let $n$ be an integer. We consider the following cases:*

First, we consider the case when $n$ is even.

****** *If $n$ is even, then $n = 2a$ for some integer $a.$*

The idea is to substitute $n=2a$ into our expression $n^2-3n$ and show it is even by writing it as a multiple of $2.$

*As a result, we obtain*

$$


\begin{aligned}𝑛^{2}−3𝑛 & =(2𝑎)^{2}−3(2𝑎) \\ & =4𝑎^{2}−6𝑎 \\ & =2(2𝑎^{2}−3𝑎).\end{aligned}


$$

*Let $b = 2a^2 - 3a.$ Since $a$ is an integer, we have that $b$ is an integer.*

*So, $n^2-3n = 2b,$ which means that it is even.*

Now, we consider the case when $n$ is odd.

****** *If $n$ is odd, then $n = 2a+1$ for some integer $a.$*

The idea is to substitute $n = 2a + 1$ into our expression $n^2-3n$ and show it is even by writing it as a multiple of $2.$

*As a result, we obtain*

$$


\begin{aligned}𝑛^{2}−3𝑛 & =(2𝑎+1)^{2}−3(2𝑎+1) \\ & =(4𝑎^{2}+4𝑎+1)−3(2𝑎+1) \\ & =4𝑎^{2}−2𝑎−2 \\ & =2(2𝑎^{2}−𝑎−1).\end{aligned}


$$

*Let $b = 2a^2 - a - 1.$ Since $a$ is an integer, we have that $b$ is an integer.*

*So, $n^2-3n = 2b,$ which means it is even*

Finally, we combine both cases:

*Combining the cases above, we can conclude that $n^2-3n$ is even for any integer $n.$*

For clarity, let's restate the proposition and full proof.

### Stating the Full Proof

Proposition:

$$


\begin{aligned}𝑛 is an integer \,⇒\,𝑛^{2}−3𝑛 is even\end{aligned}


$$

Proof:

*Let $n$ be an integer. We consider the following cases:*

****** *If $n$ is even, then $n = 2a$ for some integer $a.$*

*As a result, we obtain*

$$


\begin{aligned}𝑛^{2}−3𝑛 & =(2𝑎)^{2}−3(2𝑎) \\ & =4𝑎^{2}−6𝑎 \\ & =2(2𝑎^{2}−3𝑎).\end{aligned}


$$

*Let $b = 2a^2 - 3a.$ Since $a$ is an integer, we have that $b$ is an integer.*

*So, $n^2-3n = 2b,$ which means that it is even.*

****** *If $n$ is odd, then $n = 2a+1$ for some integer $a.$*

*As a result, we obtain*

$$


\begin{aligned}𝑛^{2}−3𝑛 & =(2𝑎+1)^{2}−3(2𝑎+1) \\ & =4𝑎^{2}−2𝑎−2 \\ & =2(2𝑎^{2}−𝑎−1).\end{aligned}


$$

*Let $b = 2a^2 - a - 1.$ Since $a$ is an integer, we have that $b$ is an integer.*

*So, $n^2-3n = 2b,$ which means it is even.*

*Combining the cases above, we can conclude that $n^2-3n$ is even for any integer $n.$*

### Example: Completing a Schema

#### Question

Suppose we wish to construct a direct proof of the following statement:

$m^2 + n + 1$ is odd if $m$ and $n$ have the same parity.

What are the missing entries in the proof template below?

Let $m$ and $n$ be integers. We consider the following cases:

****. If $m$ is even and $n$ is even, then

$$


m = \boxed{\phantom{WXYZ} } {\phantom{}} \quad\text{and}\quad n = \boxed{\phantom{WXYZ} } {\phantom{}}


$$

for some $\boxed{\phantom{WXYZ}} {\phantom{}}.$

By substituting the above into $\boxed{\phantom{WXYZ}} {\phantom{}}$, we can show that

$$


m^2 + n + 1 = \boxed{\phantom{WXYZ} } {\phantom{}}


$$

where $c$ is $\boxed{\phantom{WXYZ}} {\phantom{}}$.

Since $m^2 + n + 1$ $\boxed{\phantom{WXYZ}} {\phantom{}}$ a multiple of $2,$ we conclude that $m^2 + n + 1$ is $\boxed{\phantom{WXYZ}} {\phantom{}}$.

****. If $m$ is odd and $n$ is odd, then

$$


m = \boxed{\phantom{WXYZ} } {\phantom{}} \quad\text{and}\quad n = \boxed{\phantom{WXYZ} } {\phantom{}}


$$

for some $\boxed{\phantom{WXYZ}} {\phantom{}}$.

By substituting the above into $\boxed{\phantom{WXYZ}} {\phantom{}}$, we can show that

$$


m^2 + n + 1 = \boxed{\phantom{WXYZ} } {\phantom{}}


$$

where $c$ is $\boxed{\phantom{WXYZ}} {\phantom{}}$.

Since $m^2 + n + 1$ $\boxed{\phantom{WXYZ}} {\phantom{}}$ a multiple of $2,$ we conclude that $m^2 + n + 1$ is $\boxed{\phantom{WXYZ}} {\phantom{}}$.

Therefore, combining the cases above, we conclude that $m^2 + n + 1$ is $\boxed{\phantom{WXYZ}} {\phantom{}}$ for any integers $m$ and $n$ that have the same parity.

#### Explanation

Recall the following:

- An integer is ** if it can be written as $2p,$ where $p$ is an integer.

- An integer is ** if it can be written as $2q + 1,$ where $q$ is an integer.

In this case, we need to show the following:

$$


m \text{ and } n \text{ have the same parity} \quad\Rightarrow\quad m^2 + n + 1 \text{ is odd}


$$

We will assume that $m$ and $n$ have the same parity. Therefore, they are both even, or they are both odd. Hence, it suffices to show the following:

$$


(m \text{ and } n \text{ are both even}) \lor (m \text{ and } n \text{ are both odd}) \quad\Rightarrow\quad m^2 + n + 1 \text{ is odd}


$$

We begin our proof with the assumption that $m$ and $n$ are integers and state that we will prove our result using cases.

Let $m$ and $n$ be integers. We consider the following cases:

First, we consider the case when $m$ and $n$ are even.

****. If $m$ and $n$ are even, then

$$


m = \boxed{\color{blue}2a} \quad\text{and}\quad n = \boxed{\color{blue}2b}


$$

for some $𝑎$

The idea is to substitute $m=2a$ and $n=2b$ into our expression $m^2 + n + 1$ and show it is odd by writing it as $1$ more than a multiple of $2.$

By substituting the above into $\boxed{\color{blue}m^2 + n + 1}$, we can show that

$$


m^2 + n + 1 = \boxed{\color{blue}2c+1}


$$

where $c$ is $\boxed{\color{blue}\text{an integer}}.$

We then make our conclusion for this case:

Since $m^2 + n + 1$ $1$ a multiple of $2,$ we conclude that $m^2 + n + 1$ is $\boxed{\color{blue}\text{odd}}.$

Now, we consider the case when $m$ and $n$ are odd.

****. If $m$ and $n$ are odd, then

$$


m = \boxed{\color{blue}2a+1} \quad\text{and}\quad n = \boxed{\color{blue}2b+1}


$$

for some $𝑎$

The idea is to substitute $m=2a+1$ and $n=2b+1$ into our expression $m^2 + n + 1$ and show it is odd by writing it as $1$ more than a multiple of $2.$

By substituting the above into $\boxed{\color{blue}m^2 + n + 1}$, we can show that

$$


m^2 + n + 1 = \boxed{\color{blue}2c+1}


$$

where $c$ is $\boxed{\color{blue}\text{an integer}}.$

We then make our conclusion for this case:

Since $m^2 + n + 1$ $1$ a multiple of $2,$ we conclude that $m^2 + n + 1$ is $\boxed{\color{blue}\text{odd}}.$

We've proven that our statement is true for all possible cases. So, the proof is complete, and we can state our conclusion.

Therefore, combining the cases above, we conclude that $m^2 + n + 1$ is $\boxed{\color{blue}\text{odd}}$ for any integers $m$ and $n$ that have the same parity.

### Example: Proving Single-Variable Parity Statements by Cases

#### Question

Prove that if $n$ is an integer, then $n^2-n+7$ is odd.

#### Explanation

Recall the following:

- An integer is ** if it can be written as $2p,$ where $p$ is an integer.

- An integer is ** if it can be written as $2q + 1,$ where $q$ is an integer.

In this case, we need to show the following:

$$


\begin{aligned}𝑛 is an integer \,⇒\,𝑛^{2}−𝑛+7 is odd. \end{aligned}


$$

The integers split naturally into even and odd numbers, and these two cases cover all possible integers. Therefore, it suffices to prove the following:

$$


\begin{aligned}(𝑛 is even )∨(𝑛 is odd )\,⇒\,𝑛^{2}−𝑛+7 is odd. \end{aligned}


$$

We begin our proof by assuming $n$ is an integer and state that we'll proceed using cases.

Let $n$ be an integer. We consider the following cases:

First, we consider the case when $n$ is even.

****. If $n$ is even, then $n = 2a$ for some integer $a.$

The idea is to substitute $n=2a$ into our expression $n^2-n+7$ and show it is odd by writing it as $1$ more than a multiple of $2.$

As a result, we obtain

$$


\begin{aligned}𝑛^{2}−𝑛+7 & =(2𝑎)^{2}−(2𝑎)+7 \\ & =4𝑎^{2}−2𝑎+7 \\ & =(4𝑎^{2}−2𝑎+6)+1 \\ & =2(2𝑎^{2}−𝑎+3)+1.\end{aligned}


$$

Let $b = 2a^2 - a + 3.$ Since $a$ is an integer, we have that $b$ is an integer.

So, $n^2-n+7 = 2b+1,$ which means that it is odd.

Now, we consider the case when $n$ is odd.

****. If $n$ is odd, then $n = 2a+1$ for some integer $a.$

The idea is to substitute $n = 2a + 1$ into our expression $n^2-n+7$ and show it is odd by writing it as $1$ more than a multiple of $2.$

As a result, we obtain

$$


\begin{aligned}𝑛^{2}−𝑛+7 & =(2𝑎+1)^{2}−(2𝑎+1)+7 \\ & =(4𝑎^{2}+4𝑎+1)−(2𝑎+1)+7 \\ & =4𝑎^{2}+2𝑎+7 \\ & =(4𝑎^{2}+2𝑎+6)+1 \\ & =2(2𝑎^{2}+𝑎+3)+1.\end{aligned}


$$

Let $b = 2a^2 + a + 3.$ Since $a$ is an integer, we have that $b$ is an integer.

So, $n^2-n+7 = 2b+1,$ which means it is odd.

Finally, we combine both cases:

Combining the cases above, we can conclude that $n^2-n+7$ is odd for any integer $n.$

### Example: Proving Multivariable Parity Statements by Cases

#### Question

Prove that if $m$ and $n$ are of the same parity, then $3m-7n+2$ is even.

#### Explanation

Recall the following:

- An integer is ** if it can be written as $2p,$ where $p$ is an integer.

- An integer is ** if it can be written as $2q + 1,$ where $q$ is an integer.

In this case, we need to show the following:

$$


\begin{aligned}𝑚 and 𝑛 have the same parity \,⇒\,3𝑚−7𝑛+2 is even. \end{aligned}


$$

If $m$ and $n$ are of the same parity, then either both are even, or both are odd. Thus, it suffices to prove the following:

$$


\begin{aligned}(𝑚,𝑛 are both even)∨(𝑚,𝑛 are both odd)\,⇒\,3𝑚−7𝑛+2 is even. \end{aligned}


$$

We begin our proof by assuming $m$ and $n$ are integers of the same parity and state that we'll proceed using cases.

Let $m$ and $n$ be integers of the same parity. We consider the following cases:

First, we consider the case when $m$ and $n$ are both even.

Case 1. If $m$ and $n$ are even, then $m=2a$ and $n=2b$ for some integers $a$ and $b.$

As a result, we obtain

$$


\begin{aligned}3𝑚−7𝑛+2 & =3(2𝑎)−7(2𝑏)+2 \\ & =6𝑎−14𝑏+2 \\ & =2(3𝑎−7𝑏+1).\end{aligned}


$$

Let $c=3a-7b+1.$ Since $a$ and $b$ are integers, we have that $c$ is an integer.

So, $3m-7n+2 = 2c,$ which means that it is even.

Now, we consider the case when $m$ and $n$ are both odd.

Case 2. If $m$ and $n$ are odd, then $m=2a+1$ and $n=2b+1$ for some integers $a$ and $b.$

As a result, we obtain

$$


\begin{aligned}3𝑚−7𝑛+2 & =3(2𝑎+1)−7(2𝑏+1)+2 \\ & =6𝑎+3−14𝑏−7+2 \\ & =6𝑎−14𝑏−2 \\ & =2(3𝑎−7𝑏−1).\end{aligned}


$$

Let $c=3a-7b-1.$ Since $a$ and $b$ are integers, we have that $c$ is an integer.

So, $3m-7n+2 = 2c,$ which means that it is even.

Finally, we combine both cases:

Combining the cases above, we can conclude that $3m-7n+2$ is even for any integers $m$ and $n$ of the same parity.
