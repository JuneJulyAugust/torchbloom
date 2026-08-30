# Solving Homogeneous Recurrence Relations Using Generating Functions

Source: https://www.mathacademy.com/topics/3726?courseId=109
Topic ID: 3726

## Prerequisites

- [Generating Functions of Homogeneous Recurrence Relations](./3140-generating-functions-of-homogeneous-recurrence-relations.md)
- [Determining the General Term of a Sequence Given Its Generating Function](./3722-determining-the-general-term-of-a-sequence-given-its-generating-function.md)

## Lesson

### Introduction

Recall that a relation $a_n$ is **homogeneous** if the corresponding expression contains only preceding terms of the relation.

In other words, the linear recurrence relation

$$



a_n = s_1a_{n-1} + s_2a_{n-2} + \ldots + s_ka_{n-k} + g(n),



$$

is homogeneous if $g(n) = 0$ for all $n,$ and $s_i$ is constant for each $i.$

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

### Homogeneous Recurrence Relations Using Generating Functions

Suppose the general term $a_n$ for $n\geq 0$ of the sequence $1, \: -1, \: -1, \: 11, \: \ldots$ satisfies the recurrence relation

$$



a_n=-5a_{n−1}-6a_{n−2}.



$$

We can use generating functions to find the explicit expression for $a_n.$ Let's see how.

Notice that for $n \geq 2,$ our sequence satisfies the recurrence relation

$$



a_n + 5a_{n−1} + 6a_{n−2} = 0.



$$

Let $A$ denote the generating function of our sequence:

$$



A = 1-x-x^2+11x^3+\cdots



$$

Adding $A,$ $5xA,$ and $6x^2A,$ we obtain the following:

$$



\begin{aligned}𝐴 & =1−0𝑥−0𝑥^{2}+11𝑥^{3}+⋯ \\ 5𝑥𝐴 & =0+5𝑥−5𝑥^{2}−05𝑥^{3}+⋯ \\ 6𝑥^{2}𝐴 & =0+0𝑥+6𝑥^{2}−06𝑥^{3}+⋯ \\ 𝐴+5𝑥𝐴+6𝑥^{2}𝐴 & =1+4𝑥+0𝑥^{2}+00𝑥^{3}+⋯ \\ (1+5𝑥+6𝑥^{2})𝐴 & =1+4𝑥 \\ 𝐴 & =\frac{1+4𝑥}{1+5𝑥+6𝑥^{2}} \\ & =\frac{1+4𝑥}{(3𝑥+1)(2𝑥+1)}\end{aligned}



$$

Now, we re-write our fraction as a sum of partial fractions:

$$



\begin{aligned}\frac{1+4𝑥}{(3𝑥+1)(2𝑥+1)} & =−\frac{1}{(3𝑥+1)}+\frac{2}{(2𝑥+1)}\end{aligned}



$$

Next, we expand each of the partial fractions as a geometric series.

$$



\begin{aligned}\frac{1}{3𝑥+1} & =1+(−3)𝑥+(−3)^{2}𝑥^{2}+(−3)^{3}𝑥^{3}+⋯ \\ \frac{2}{2𝑥+1} & =2+2(−2)𝑥+2(−2)^{2}𝑥^{2}+2(−2)^{3}𝑥^{3}+⋯\end{aligned}



$$

The general term of the first sequence is $b_n = \left(-3\right)^n,$ while the general term of the second sequence is $c_n = 2 \cdot (-2)^n.$

Therefore, the general term of our original sequence is

$$



\begin{aligned}𝑎_{𝑛} & =−𝑏_{𝑛}+𝑐_{𝑛} \\ & =−(−3)^{𝑛}+2⋅(−2)^{𝑛} \\ & =(−1)^{𝑛}(2^{𝑛+1}−3^{𝑛}).\end{aligned}



$$

### Example: Completing a Solution Template

#### Question

Suppose we wish to determine the general term $a_n$ for $n \geq 0$ of the sequence

$$



3, \: -9, \: 21, \: -45, \: \ldots



$$

that satisfies the recurrence relation $a_n=-3a_{n−1}-2a_{n−2}.$

Fill the blanks in the template for the solution below.

**** Let $A$ denote the generating function of our sequence:

$$



A = \boxed{\phantom{\textrm{3-9x+21x^2-45x^3+...}}}



$$

**** Find a closed expression for $A$ by adding $\boxed{\phantom{\textrm{odd}}}$, $\boxed{\phantom{\textrm{odd}}}$, and $\boxed{\phantom{\textrm{odd}}}$:

$$



A = \dfrac{3}{(1+3x+2x^2)}



$$

**** We express $A$ as a $\boxed{\phantom{\textrm{sum of partial fractions}}}$:

$$



A = \dfrac{6}{1+2x} - \dfrac{3}{1+x}



$$

**** We determine the general terms for the coefficients $b_n$ and $c_n$ in the $\boxed{\phantom{\textrm{geometric}}}$ series corresponding to the first and the second partial fractions:

$$



b_n = 6 \cdot \big( \boxed{\phantom{\textrm{odd}}}] \big)^n \qquad\text{and}\qquad c_n = 3 \cdot \big( \boxed{\phantom{\textrm{odd}}}\big)^n



$$

**** We write down the general term of our original sequence:

$$



a_n = \boxed{\phantom{\textrm{b_n-c_n}}} =6 \cdot (-2)^n - 3\cdot (-1)^{n}



$$

#### Explanation

The correct solution is the following:

**** Let $A$ denote the generating function of our sequence:

$$



A = \boxed{\color{blue}3 - 9x + 21x^2 - 45x^3+\cdots}



$$

**** Find a closed expression for $A$ by adding $\boxed{\color{blue}A},$ $\boxed{\color{blue}3xA},$ and $\boxed{\color{blue}2x^2A}{:}$

$$



A = \dfrac{3}{(1+3x+2x^2)}



$$

**** We express $A$ as a $\boxed{\color{blue}\textrm{sum of partial fractions}}{:}$

$$



A = \dfrac{6}{1+2x} - \dfrac{3}{1+x}



$$

**** We determine the general terms for the coefficients $b_n$ and $c_n$ in the $\boxed{\color{blue}\textrm{geometric}}$ series corresponding to the first and the second partial fractions:

$$



b_n =6 \cdot \big( \boxed{\color{blue}-2} \big)^n \qquad\text{and}\qquad c_n =3 \cdot \big( \boxed{\color{blue}{-1}} \big)^n



$$

Indeed, notice the following:

$$



\begin{aligned}\frac{6}{1+2𝑥} & =6⋅\frac{1}{1−(−2𝑥)} \\ & =6[1+(−2𝑥)+(−2𝑥)^{2}+(−2𝑥)^{3}+⋯] \\ & =\underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}[6⋅(−2)^{𝑛}𝑥^{𝑛}] \\ \frac{3}{1+𝑥} & =3⋅\frac{1}{1−(−𝑥)} \\ & =3[1+(−𝑥)+(−𝑥)^{2}+(−𝑥)^{3}+⋯] \\ & =\underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}[3⋅(−1)^{𝑛}𝑥^{𝑛}]\end{aligned}



$$

**** We write down the general term of our original sequence:

$$



a_n = \boxed{\color{blue}b_n-c_n} = 6 \cdot (-2)^n - 3\cdot (-1)^{n}



$$

### Example: Second-Order Homogeneous Recurrence Relations: Finding Partial Solutions Using Generating Functions

#### Question

The general term $a_n$ for $n\geq 0$ of the sequence

$$



1, \: -4, \: 10, \: -22, \: \ldots



$$

that satisfies the recurrence relation $a_n=-3a_{n−1}-2a_{n−2}$ is given by

$$



a_n = 3\cdot (-2)^{n} - 2 \cdot (-1)^n.



$$

Fill in the blanks below to obtain the correct reasoning.

Let $A$ denote the generating function of our sequence:

$$



A =\boxed{\phantom{\textrm{1-4x +10x^2-22x^3}}}



$$

First, we find a closed expression for $A$ by adding $\boxed{\phantom{\textrm{A}}}$, $\boxed{\phantom{\textrm{3xA}}}$, and $\boxed{\phantom{\textrm{2x^2A}}}$.

By doing so, we obtain

Now, we rewrite our fraction as the sum of the partial fractions:

The general terms for the coefficients in the geometric series corresponding to the first and second partial fractions, respectively, are

$$



b_n = \boxed{\phantom{\textrm{3*(-2)^n}}} \qquad\text{and}\qquad c_n = \boxed{\phantom{\textrm{(-1)^n}}}.



$$

Therefore, the general term of our original sequence is

$$



a_n = \boxed{\phantom{\textrm{b_n-c_n}}} = 3\cdot (-2)^{n} - 2\cdot (-1)^n.



$$

#### Explanation

Notice that for $n \geq 2,$ our sequence satisfies the recurrence relation

$$



a_n + 3a_{n−1} + 2a_{n−2} = 0.



$$

Let $A$ denote the generating function of our sequence:

$$



A = \boxed{\color{blue}1-4x+10x^2-22x^3+\cdots}



$$

Adding $\boxed{\color{blue}A},$ $\boxed{\color{blue}3xA},$ and $\boxed{\color{blue}2x^2A},$ we obtain the following:

$$



\begin{aligned}𝐴 & =1−4𝑥+10𝑥^{2}−22𝑥^{3}+⋯ \\ 3𝑥𝐴 & =0+3𝑥−12𝑥^{2}+30𝑥^{3}+⋯ \\ 2𝑥^{2}𝐴 & =0+0𝑥+02𝑥^{2}−08𝑥^{3}+⋯ \\ 𝐴+3𝑥𝐴+2𝑥^{2}𝐴 & =1−0𝑥+00𝑥^{2}+00𝑥^{3}+⋯ \\ 𝐴+3𝑥𝐴+2𝑥^{2}𝐴 & =1−𝑥 \\ (1+3𝑥+2𝑥^{2})𝐴 & =1−𝑥 \\ 𝐴 & =\frac{1−𝑥}{1+3𝑥+2𝑥^{2}} \\ & =\frac{1−𝑥}{(1+2𝑥)(1+𝑥)}\end{aligned}



$$

Now, we rewrite our fraction as a sum of partial fractions:

$$



\begin{aligned}\frac{1−𝑥}{(1+2𝑥)(1+𝑥)} & =\frac{𝐵}{(1+2𝑥)}+\frac{𝐶}{(1+𝑥)}\end{aligned}



$$

Multiplying both sides by $(1+2x)(1+x)$ gives

$$



\begin{aligned}1−𝑥 & =𝐵(1+𝑥)+𝐶(1+2𝑥).\end{aligned}



$$

- Substituting $x=-\dfrac12,$ we get $B = 3.$

- Substituting $x=-1,$ we get $C = -2.$

Hence,

$$



\dfrac{1-x}{(1+2x)(1+x)} = \dfrac{3}{1+2x} + \dfrac{-2}{1+x} = \dfrac{\boxed{\color{blue}3}}{1+2x} - \dfrac{\boxed{\color{blue}2}}{1+x}.



$$

Next, we expand each of the partial fractions as a geometric series.

$$



\begin{aligned}\frac{3}{1+2𝑥} & =3⋅\frac{1}{1−(−2𝑥)} \\ & =3[1+(−2𝑥)+(−2𝑥)^{2}+(−2𝑥)^{3}+⋯] \\ & =3+3(−2)𝑥+3(−2)^{2}𝑥^{2}+3(−2)^{3}𝑥^{3}+⋯ \\ \frac{2}{1+𝑥} & =2⋅\frac{1}{1−(−𝑥)} \\ & =2[1+(−𝑥)+(−𝑥)^{2}+(−𝑥)^{3}+⋯] \\ & =2+2(−1)𝑥+2(−1)^{2}𝑥^{2}+2(−1)^{3}𝑥^{3}+⋯\end{aligned}



$$

The general term for the coefficients in the first series is $b_n = \boxed{\color{blue}3 \cdot (-2)^n},$ while the general term for the coefficients in the second series is $c_n = \boxed{\color{blue}2 \cdot (-1)^n}.$

Therefore, the general term of our original sequence is

$$



\begin{aligned}𝑎_{𝑛} & =𝑏_{𝑛}−𝑐_{𝑛} \\ & =3⋅(−2)^{𝑛}−2⋅(−1)^{𝑛}.\end{aligned}



$$

### Example: Solving Second-Order Homogeneous Recurrence Relation Using Generating Functions

#### Question

Find the general term $a_n$ for $n\geq 0$ of the sequence

$$



2, \: 2, \: -2, \: -22, \: \ldots



$$

that satisfies the recurrence relation $a_n=5a_{n−1}-6a_{n−2}.$

#### Explanation

Notice that for $n \geq 2,$ our sequence satisfies the recurrence relation

$$



a_n - 5a_{n−1} + 6a_{n−2} = 0.



$$

Let $A$ denote the generating function of our sequence:

$$



A = 2+2x-2x^2-22x^3+\cdots



$$

Adding $A,$ $-5xA,$ and $6x^2A,$ we obtain the following:

$$



\begin{aligned}𝐴 & =2+02𝑥−02𝑥^{2}−22𝑥^{3}+⋯ \\ −5𝑥𝐴 & =0−10𝑥−10𝑥^{2}+10𝑥^{3}+⋯ \\ 6𝑥^{2}𝐴 & =0+00𝑥+12𝑥^{2}+12𝑥^{3}+⋯ \\ 𝐴−5𝑥𝐴+6𝑥^{2}𝐴 & =2−08𝑥+00𝑥^{2}+00𝑥^{3}+⋯ \\ 𝐴−5𝑥𝐴+6𝑥^{2}𝐴 & =2−8𝑥 \\ (1−5𝑥+6𝑥^{2})𝐴 & =2−8𝑥 \\ 𝐴 & =\frac{2−8𝑥}{1−5𝑥+6𝑥^{2}} \\ & =\frac{2−8𝑥}{(1−3𝑥)(1−2𝑥)}\end{aligned}



$$

Now, we re-write our fraction as a sum of partial fractions:

$$



\begin{aligned}\frac{2−8𝑥}{(1−3𝑥)(1−2𝑥)} & =\frac{𝐵}{(1−3𝑥)}+\frac{𝐶}{(1−2𝑥)}\end{aligned}



$$

Multiplying both sides by $(1-3x)(1-2x)$ gives

$$



\begin{aligned}2−8𝑥 & =𝐵(1−2𝑥)+𝐶(1−3𝑥).\end{aligned}



$$

- Substituting $x=\dfrac 1 3,$ we get $B =-2.$

- Substituting $x=\dfrac{1}{2},$ we get $C = 4.$

Hence,

$$



\dfrac{2-8x}{(1-3x)(1-2x)} = \dfrac{4}{1-2x}-\dfrac{2}{1-3x}.



$$

Next, we expand each of the partial fractions as a geometric series.

$$



\begin{aligned}\frac{4}{1−2𝑥} & =4⋅\frac{1}{1−(2𝑥)} \\ & =4[1+(2𝑥)+(2𝑥)^{2}+(2𝑥)^{3}+⋯] \\ & =4+4(2)𝑥+4(2)^{2}𝑥^{2}+4(2)^{3}𝑥^{3}+⋯ \\ \frac{2}{1−3𝑥} & =2⋅\frac{1}{1−(3𝑥)} \\ & =2[1+(3𝑥)+(3𝑥)^{2}+(3𝑥)^{3}+⋯] \\ & =2+2(3)𝑥+2(3)^{2}𝑥^{2}+2(3)^{3}𝑥^{3}+⋯\end{aligned}



$$

The general term for the coefficients in the first series is $b_n = 4 \cdot 2^n,$ while the general term for the coefficients in the second series is $c_n = 2 \cdot 3^n.$

Therefore, the general term of our original sequence is

$$



\begin{aligned}𝑎_{𝑛} & =𝑏_{𝑛}−𝑐_{𝑛} \\ & =4⋅2^{𝑛}−2⋅3^{𝑛}.\end{aligned}



$$
