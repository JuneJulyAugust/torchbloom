# Translating Between Explicit and Recursive Formulas for Geometric Sequences

Source: https://www.mathacademy.com/topics/2215?courseId=111
Topic ID: 2215

## Prerequisites

- [The Nth Term of a Geometric Sequence](./680-the-nth-term-of-a-geometric-sequence.md)

## Lesson

### Introduction

Suppose that we're given the following **explicit formula** for a geometric sequence:

$$


a_n = 2\cdot 5^{n-1}, \qquad n\geq 1


$$

We can write this geometric sequence using a recursive formula. Recall that the recursive formula for *any* geometric sequence is

$$


a_{n+1} = r\cdot a_n.


$$

To convert from the explicit formula to the recursive formula, we just need to work out the first term and common ratio. The first two terms are

$$


\begin{aligned}𝑎_{1} & =2⋅5^{0}=2⋅1=2 \\ 𝑎_{2} & =2⋅5^{1}=2⋅5=10,\end{aligned}


$$

and the common ratio is

$$


\begin{aligned}𝑟=\frac{𝑎_{2}}{𝑎_{1}}=\frac{10}{2}=5.\end{aligned}


$$

So, the first term is $a_1={\color{blue}2}$ and the common ratio is $r={\color{red}5}.$ Therefore, the recursive formula is as follows:

$$


a_{n+1} = {\color{red}5} \cdot a_n, \qquad a_1 = {\color{blue}2}, \qquad n \geq 1


$$

### Example: Translating From the Explicit to the Recursive Formula

#### Question

The formula for the $n$th term of a geometric sequence is $a_n = 8 \cdot 3^n$ for $n\geq 1.$ What is the recursive formula for this sequence?

#### Explanation

The recursive formula for a geometric sequence is

$$


a_{n+1} = r \cdot a_n.


$$

To complete the formula, we must determine the common ratio $r$ and state the first term $a_1.$ The first two terms are

$$


\begin{aligned}𝑎_{1} & =8⋅3^{1}=8⋅3=24, \\ 𝑎_{2} & =8⋅3^{2}=8⋅9=72.\end{aligned}


$$

Hence, the common ratio is

$$


\begin{aligned}𝑟=\frac{𝑎_{2}}{𝑎_{1}}=\frac{72}{24}=3.\end{aligned}


$$

Therefore, the recursive formula for the geometric sequence is

$$


a_{n+1} = 3 a_n, \quad a_1 = 24, \quad n \geq 1.


$$

### Example: Translating From the Explicit to the Recursive Formula Using Function Notation

#### Question

The formula for the $n$th term of a geometric sequence is $f(n) =\dfrac{6}{(-2)^n}$ for $n\geq 1.$ What is the recursive formula for this sequence?

#### Explanation

The recursive formula for a geometric sequence is

$$


f(n+1) = r \cdot f(n).


$$

To complete the formula, we must determine the common ratio $r$ and state the first term $a_1.$ The first two terms are

$$


\begin{aligned}𝑓(1) & =\frac{6}{(−2)^{1}}=\frac{6}{(−2)}=−3, \\ 𝑓(2) & =\frac{6}{(−2)^{2}}=\frac{6}{4}=\frac{3}{2}.\end{aligned}


$$

Hence, the common ratio is

$$


\begin{aligned}𝑟=\frac{𝑓(2)}{𝑓(1)}=\frac{(\frac{3}{2})}{2}=−\frac{1}{2}.\end{aligned}


$$

Therefore, the recursive formula for the geometric sequence is

$$


f(n+1) = -\dfrac{1}{2} f(n), \qquad f(1) = -3, \qquad n \geq 1.


$$

### Translating From the Recursive to the Explicit Formula

It's often more useful to translate from the recursive formula to an explicit one. So how do we find the explicit formula for the geometric sequence defined recursively as

$$


a_{n+1} ={\color{red}\dfrac 1 4} a_n,\, \qquad a_1 = {\color{blue}2},\, \qquad n\geq 1?


$$

The explicit formula for a geometric sequence is

$$


a_n = a_1 \cdot r^{n-1}, \quad n \geq 1,


$$

so we just need to determine the first term $a_1$ and the common ratio $r.$

We are given that the first term is $a_1={\color{blue}2}.$ To find the common ratio, we compare the given sequence with the general recursive formula for a geometric sequence:

$$


\begin{aligned}𝑎_{𝑛+1} & =𝑟⋅𝑎_{𝑛} \\ 𝑎_{𝑛+1} & =\frac{1}{4}𝑎_{𝑛}\end{aligned}


$$

From the above, we see that ${\color{red}r} = {\color{red}\dfrac 1 4}.$

Now we substitute $a_1={\color{blue}2}$ and $r={\color{red}\dfrac{1}{4}}$ into the formula for the $n$th term:

$$


\begin{aligned} a_n &= a_1 \cdot r^{n-1} \\&= {\color{blue}2} \cdot \left( {\color{red}\dfrac{1}{4}} \right)^{n-1} \end{aligned}


$$

Therefore, the formula for the $n$th term is

$$


a_n=2 \cdot \left( \dfrac{1}{4} \right)^{n-1}, \quad n \geq 1.


$$

### Example: Translating From the Recursive to the Explicit Formula

#### Question

What is the explicit formula for the $n$th term of the geometric sequence

$$


a_{n+1} = 3a_n,\, \qquad a_1 = 1,\, \qquad n\geq 1?


$$

#### Explanation

The explicit formula for the $n$th term of a geometric sequence is

$$


a_n = a_1 \cdot r^{n-1}, \qquad n \geq 1.


$$

So, we must determine the first term $a_1$ and the common ratio $r.$

We are given that the first term is $a_1=1.$ To find the common ratio, we compare the given sequence with the general recursive formula for a geometric sequence:

$$


a_{n+1} = r \cdot a_n


$$

From the above, we see that $r = 3.$

Substituting $a_1 = 1$ and $r = 3$ into the formula for the $n$th term, we obtain

$$


\begin{aligned} a_n &= a_1 \cdot r^{n-1} \\\[5pt] &= 1 \cdot 3^{n-1} \\\[5pt] &= 3^{n-1}. \end{aligned}


$$

Therefore, the formula for the $n$th term is

$$


a_n=3^{n-1}, \quad n \geq 1.


$$

### Example: Translating From the Recursive to the Explicit Formula Using Function Notation

#### Question

What is the explicit formula for the $n$th term of the sequence

$$


f(n+1) =-\dfrac{f(n)}{3},\, \quad f(1) = {\color{blue}9},\, \quad n\geq 1?


$$

#### Explanation

First, let's rewrite our recursive formula as follows:

$$


\begin{aligned}𝑓(𝑛+1)=−\frac{𝑓(𝑛)}{3}=−\frac{1}{3}𝑓(𝑛)\end{aligned}


$$

The explicit formula for the $n$th term of a geometric sequence is

$$


f(n) =f(1) \cdot r^{n-1}, \quad n \geq 1.


$$

So, we must determine the first term $f(1)$ and the common ratio $r.$

We are given that the first term is $f(1)=9.$ To find the common ratio, we compare the given sequence with the general recursive formula for a geometric sequence:

$$


f(n+1) = {\color{red}r} \cdot f(n)


$$

From the above, we see that $r = -\dfrac{1}{3}.$

Substituting $f(1) = 9$ and $r = -\dfrac{1}{3}$ into the formula for the $n$th term, we obtain

$$


\begin{aligned} f(n) &= f(1) \cdot r^{n-1} \\\[5pt] &= 9 \cdot \left( -\dfrac{1}{3}\right)^{n-1}. \end{aligned}


$$

We can simplify further by manipulating the exponents as follows:

$$


\begin{aligned}𝑓(𝑛) & =9⋅(−\frac{1}{3})^{𝑛−1} \\ & =9⋅(−\frac{1}{3})^{−1}⋅(−\frac{1}{3})^{𝑛} \\ & =9⋅(−\frac{3}{1})⋅(−\frac{1}{3})^{𝑛} \\ & =−27⋅\frac{1}{(−3)^{𝑛}} \\ & =−\frac{27}{(−3)^{𝑛}}\end{aligned}


$$

Therefore, the formula for the $n$th term is

$$


f(n)=-\dfrac{27}{(-3)^n} ,\quad n\geq 1.


$$
