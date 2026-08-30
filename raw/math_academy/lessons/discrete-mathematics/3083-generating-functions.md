# Generating Functions

Source: https://www.mathacademy.com/topics/3083?courseId=109
Topic ID: 3083

## Prerequisites

- [Multiplying Polynomials](../algebra-i/361-multiplying-polynomials.md)
- [Dividing Rational Expressions](../algebra-ii/436-dividing-rational-expressions.md)
- [Finding the Sum of an Infinite Geometric Series](./691-finding-the-sum-of-an-infinite-geometric-series.md)

## Lesson

### Introduction

Given a sequence $a_n$ for $n\geq 0,$ the corresponding **generating series** is an infinite power series such that the coefficient of $x^i$ is equal to $a_i$ for all $i\geq 0.$

For example, suppose that we have the following sequence of numbers:

$$



1,\quad -2,\quad 4,\quad -8, \quad\ldots



$$

The corresponding generating series for this sequence is

$$



1-2x+4x^2-8x^3+\cdots.



$$

A generating series is simply an alternative way of representing a sequence.

### Example: Identifying the Generating Series of a Given Sequence

#### Question

Find the sequence represented by the following generating series:

$$



-1+2x - 3x^2 + 4x^3 + \cdots



$$

#### Explanation

First, we re-write our series as follows:

$$



\begin{aligned}(−1)𝑥^{0}+2𝑥^{1}+(−3)𝑥^{2}+4𝑥^{3}+⋯ & \end{aligned}



$$

Now, we write down the $i$th coefficient of the series (for $i=0,1,2,\ldots$), which gives the following sequence:

$$



-1, \: 2, \: -3, \: 4, \: \ldots



$$

### Generating Functions

Given the sequence $a_n$ for $n\geq 0,$ a function $f(x)$ is called the **generating function** of the sequence if the corresponding generating series can be represented by the function $f(x).$ That is,

$$



f(x) = a_0 + a_1x + a_2x^2 + a_3x^3 + \cdots .



$$

Generating functions are a useful way to manipulate sequences because every term of the sequence is encoded in the function $f(x).$

For example, let consider the sequence $a_n = 1$ for $n\geq 0.$ Writing out the terms of this sequence explicitly, we have

$$



1, \quad 1,\quad 1, \quad 1,\quad \ldots.



$$

The corresponding generating series is

$$



1+x+x^2 + x^3 + \cdots



$$

Notice that this is a geometric series. The first term is equal to $1$ and the common ratio is $x.$ Using the formula for the sum of an infinite geometric series, we have

$$



\dfrac{1}{1-x} = 1+x+x^2 + x^3 + \cdots .



$$

Therefore, we conclude that the generating function for the sequence $a_n$ is $f(x) = \dfrac{1}{1-x}.$

**Watch out!** Strictly speaking, the identity

$$



1+x+x^2+x^3+\cdots = \frac{1}{1-x}



$$

is true as an equality of functions only when $|x|<1,$ since the infinite geometric series converges only in that interval. In generating functions, however, we usually view this as a *formal power series* identity rather than a statement about numerical values of $x.$ In that setting, we do not substitute particular values of $x.$ Instead, we focus on the coefficients of the powers of $x.$ So,

$$



\dfrac{1}{1-x}



$$

is the generating function for the sequence $1, \: 1, \: 1, \: 1, \: \ldots$ because its power series expansion has coefficient $1$ on every power of $x.$

### Example: Building Generating Functions in Some Simple Cases

#### Question

What generating function is defined by the following sequence?

$$



3, \quad 3\cdot 2, \quad 3 \cdot 4, \quad 3 \cdot 8, \quad \ldots



$$

#### Explanation

First, recall that the sequence $1, \: 1, \: 1, \: \ldots$ defines the series

$$



1+x+x^2+x^3+\cdots = \dfrac{1}{1-x}.



$$

By writing $2x$ in place of $x,$ we get the following:

$$



\begin{aligned}1+(2𝑥)+(2𝑥)^{2}+(2𝑥)^{3}+⋯ & =\frac{1}{1−(2𝑥)} \\ 1+2𝑥+4𝑥^{2}+8𝑥^{3}+⋯ & =\frac{1}{1−2𝑥}\end{aligned}



$$

Finally, we multiply both sides by $3\mathbin{:}$

$$



\begin{aligned}3⋅(1+2𝑥+4𝑥^{2}+8𝑥^{3}+⋯) & =3⋅\frac{1}{1−2𝑥} \\ 3+3⋅2𝑥+3⋅4𝑥^{2}+3⋅8𝑥^{3}+⋯ & =\frac{3}{1−2𝑥}\end{aligned}



$$

The left-hand side corresponds to the given sequence. Therefore, the sequence defines the generating function $f(x) = \dfrac{3}{1-2x}.$

### Building Generating Functions Using Differences

Let's calculate the generating function for the following sequence:

$$



1, \quad 2, \quad 3, \quad 4, \quad \ldots



$$

Our sequence is arithmetic since there is a common difference of $1$ between any two successive terms.

First, we let $A$ denote the generating function of our sequence:

$$



A = 1+2x+3x^2+4x^3+\cdots



$$

To find a closed form for $A,$ we need to do a clever trick. First, we multiply both sides of this equation by $(-x)\mathbin{:}$

$$



\begin{aligned}(−𝑥)⋅𝐴 & =(−𝑥)⋅(1+2𝑥+3𝑥^{2}+4𝑥^{3}+⋯) \\ −𝑥𝐴 & =−𝑥−2𝑥^{2}−3𝑥^{3}−4𝑥^{4}+⋯\end{aligned}



$$

Then, adding $-xA$ to $A,$ we obtain the following:

$$



\begin{aligned}𝐴 & =1+2𝑥+3𝑥^{2}+4𝑥^{3}+⋯ \\ −𝑥𝐴 & =0−2𝑥−2𝑥^{2}−3𝑥^{3}+⋯ \\ 𝐴−𝑥𝐴 & =1+2𝑥+2𝑥^{2}+3𝑥^{3}+⋯\end{aligned}



$$

Finally, since $1+x+x^2+\cdots = \dfrac{1}{1-x},$ we can solve for $A$ as follows:

$$



\begin{aligned}(1−𝑥)𝐴 & =1+𝑥+𝑥^{2}+𝑥^{3}+⋯ \\ (1−𝑥)𝐴 & =\frac{1}{1−𝑥} \\ 𝐴 & =\frac{1}{(1−𝑥)^{2}}\end{aligned}



$$

We can use the same technique to find the generating function of any arithmetic sequence. Let's see another example.

### Example: Building Generating Functions Using Differences

#### Question

Find the generating function for the sequence $-1, \: 2, \: 5, \: 8, \: \ldots \:.$

#### Explanation

Notice that our sequence has a common difference of $3$ between any two successive terms.

Let $A$ denote the generating function of our sequence:

$$



A = -1+2x+5x^2+8x^3+\cdots



$$

Now, we multiply both sides of this equation by $(-x)\mathbin{:}$

$$



\begin{aligned}(−𝑥)⋅𝐴 & =(−𝑥)⋅(−1+2𝑥+5𝑥^{2}+8𝑥^{3}+⋯) \\ −𝑥𝐴 & =𝑥−2𝑥^{2}−5𝑥^{3}−8𝑥^{4}+⋯\end{aligned}



$$

Adding $-xA$ to $A,$ we obtain the following:

$$



\begin{aligned}𝐴 & =−1+2𝑥+5𝑥^{2}+8𝑥^{3}+⋯ \\ −𝑥𝐴 & =−0+2𝑥−2𝑥^{2}−5𝑥^{3}+⋯ \\ 𝐴−𝑥𝐴 & =−1+3𝑥+3𝑥^{2}+3𝑥^{3}+⋯ \\ (1−𝑥)𝐴 & =−1+3𝑥⋅(1+𝑥+𝑥^{2}+⋯)\end{aligned}



$$

Since $1+x+x^2+\cdots = \dfrac{1}{1-x},$ we can solve for $A$ as follows:

$$



\begin{aligned}(1−𝑥)𝐴 & =−1+3𝑥⋅(1+𝑥+𝑥^{2}+⋯) \\ (1−𝑥)𝐴 & =−1+3𝑥⋅\frac{1}{1−𝑥} \\ (1−𝑥)𝐴 & =\frac{4𝑥−1}{1−𝑥} \\ 𝐴 & =\frac{4𝑥−1}{(1−𝑥)^{2}}\end{aligned}



$$
