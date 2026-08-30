# Generating Functions of Homogeneous Recurrence Relations

Source: https://www.mathacademy.com/topics/3140?courseId=109
Topic ID: 3140

## Prerequisites

- [Fibonacci Sequences](../algebra-i/73-fibonacci-sequences.md)
- [Generating Functions](./3083-generating-functions.md)

## Lesson

### Introduction

Suppose we want to find a generating function for the sequence defined by the rule

$$



a_n=-2a_{n−1}, \qquad a_0 = 2.



$$

We call this rule a **recurrence relation.** The first few terms of the sequence defined by this relation are

$$



2, \quad -4, \quad 8, \quad -16, \quad \ldots



$$

Let $A$ denote the generating function of our sequence:

$$



A = 2-4x+8x^2-16x^3+\cdots



$$

To find the generating function, we manipulate the expression for $A$ to obtain a closed expression instead of an infinite series.

In this case, since the coefficients of the sequence form a geometric series, we obtain

$$



\begin{aligned}𝐴 & =2−4𝑥+8𝑥^{2}−16𝑥^{3}+⋯ \\ & =2(1−2𝑥+4𝑥^{2}−8𝑥^{3}+⋯) \\ & =2(1+(−2𝑥)+(−2𝑥)^{2}+(−2𝑥)^{3}+⋯) \\ & =2⋅\frac{1}{1−(−2𝑥)} \\ & =\frac{2}{1+2𝑥}.\end{aligned}



$$

### Example: Determining the Generating Function of a First-Order Homogeneous Recurrence Relation

#### Question

Find the generating function for the sequence that satisfies the recurrence relation $a_n=3a_{n−1}$ with $a_0=1.$

#### Explanation

Let $A$ denote the generating function of our sequence:

$$



A = 1 + 3x + 9x^2 + 27x^3 + \cdots



$$

Since the coefficients of the sequence form a geometric series, we obtain

$$



\begin{aligned}𝐴 & =1+3𝑥+9𝑥^{2}+27𝑥^{3}+⋯ \\ & =1+(3𝑥)+(3𝑥)^{2}+(3𝑥)^{3}+⋯ \\ & =\frac{1}{1−(3𝑥)} \\ & =\frac{1}{1−3𝑥}.\end{aligned}



$$

### Generating Functions of Second-Order Homogeneous Recurrence Relations

Let's consider the recurrence relation

$$



a_n-a_{n−1}-a_{n−2} = 0, \quad (\ast)



$$

with $a_0=a_1=1.$ The first few terms of the sequence defined by this recurrence relation are

$$



1, \quad 1, \quad 2, \quad 3, \quad 5, \quad \ldots\,.



$$

You might recognize this as the Fibonacci sequence. Let's find a generating function for this sequence.

First, let $A$ denote the generating function of our sequence:

$$



A = 1+x+2x^2+3x^3+\cdots



$$

The idea is to manipulate the above expression for $A$ so that we obtain a closed expression instead of an infinite series. We can do this using the recurrence relation $(\ast).$

The coefficient of the second term in $(\ast)$ is $-1.$ So first, we multiply both sides of the equation for $A$ by $(-x)\mathbin{:}$

$$



\begin{aligned}−𝑥𝐴 & =−𝑥−𝑥^{2}−2𝑥^{3}−3𝑥^{4}+⋯\end{aligned}



$$

The coefficient of the third term in $(\ast)$ is $-1$ too. So, we multiply both sides of the equation for $A$ by $(-x^2)\mathbin{:}$

$$



\begin{aligned}−𝑥^{2}𝐴 & =−𝑥^{2}−𝑥^{3}−2𝑥^{4}−3𝑥^{5}+⋯\end{aligned}



$$

Adding $A,$ $-xA,$ and $-x^2A,$ we obtain the following:

$$



\begin{aligned}𝐴 & =1+0𝑥+2𝑥^{2}+3𝑥^{3}+⋯ \\ −𝑥𝐴 & =0−0𝑥−0𝑥^{2}−2𝑥^{3}+⋯ \\ −𝑥^{2}𝐴 & =0−0𝑥−0𝑥^{2}−0𝑥^{3}+⋯ \\ 𝐴−𝑥𝐴−𝑥^{2}𝐴 & =1−0𝑥+0𝑥^{2}+0𝑥^{3}+⋯\end{aligned}



$$

Notice that the coefficients from the $x^2$ term onward on the right-hand side are constructed from a sum that satisfies the recurrence relation and, therefore, must all be zero. Consequently, we are left with

$$



A-xA-x^2A = 1.



$$

Finally, we can solve for $A,$ as follows:

$$



\begin{aligned}(1−𝑥−𝑥^{2})𝐴=1\,⟹\,𝐴=\frac{1}{1−𝑥−𝑥^{2}}\end{aligned}



$$

Therefore, the generating function for the Fibonacci sequence is

$$



A = \dfrac{1}{1-x-x^2}.



$$

### Example: Determining the Generating Function of a Second-Order Homogeneous Recurrence Relation

#### Question

Find the generating function for the sequence $2, \: 1, \: -2, \: -26, \: \ldots$ that satisfies the recurrence relation $a_n=10a_{n−1}-6a_{n−2}.$

#### Explanation

For $n \geq 2,$ our sequence satisfies the equation

$$



a_n - 10a_{n−1} + 6a_{n−2} = 0.\qquad (\ast)



$$

Let $A$ denote the generating function of our sequence:

$$



A = 2+x-2x^2-26x^3+\cdots



$$

The idea is to manipulate the above expression for $A$ so that we obtain a closed expression instead of an infinite series. We can do this using the recurrence relation $(\ast).$

The coefficient of the second term in $(\ast)$ is $-10.$ So first, we multiply both sides of the equation for $A$ by $(-10x)\mathbin{:}$

$$



\begin{aligned}−10𝑥𝐴 & =−20𝑥−10𝑥^{2}+20𝑥^{3}+260𝑥^{4}+⋯\end{aligned}



$$

The coefficient of the third term in $(\ast)$ is $6.$ So next, we multiply both sides of the equation for $A$ by $(6x^2)\mathbin{:}$

$$



\begin{aligned}6𝑥^{2}𝐴 & =12𝑥^{2}+6𝑥^{3}−12𝑥^{4}−156𝑥^{5}+⋯\end{aligned}



$$

Adding $A,$ $-10xA,$ and $6x^2A,$ we obtain the following:

$$



\begin{aligned}𝐴 & =2+00𝑥−02𝑥^{2}−26𝑥^{3}+⋯ \\ −10𝑥𝐴 & =0−20𝑥−10𝑥^{2}+20𝑥^{3}+⋯ \\ 6𝑥^{2}𝐴 & =0+00𝑥+12𝑥^{2}+06𝑥^{3}+⋯ \\ 𝐴−10𝑥𝐴+6𝑥^{2}𝐴 & =2−19𝑥+00𝑥^{2}+00𝑥^{3}+⋯\end{aligned}



$$

Notice that the coefficients from the $x^2$ term onward on the right-hand side are constructed from a sum that satisfies the recurrence relation and, therefore, must all be zero. Consequently, we are left with

$$



A-10xA+6x^2A = 2-19x.



$$

Finally, we can solve for $A,$ as follows:

$$



\begin{aligned}𝐴−10𝑥𝐴+6𝑥^{2}𝐴 & =2−19𝑥 \\ (1−10𝑥+6𝑥^{2})𝐴 & =2−19𝑥 \\ 𝐴 & =\frac{2−19𝑥}{1−10𝑥+6𝑥^{2}}\end{aligned}



$$

### Example: Determining the Generating Function of a Second-Order Homogeneous Degenerate Recurrence Relation

#### Question

Find the generating function for the sequence $3, \: -1, \: -6, \: 2 \: \ldots$ that satisfies the recurrence relation $a_n=-2a_{n−2}.$

#### Explanation

For $n \geq 2,$ our sequence satisfies the relation

$$



a_n +2a_{n−2} = 0.\qquad (\ast)



$$

Let $A$ denote the generating function of our sequence:

$$



A = 3-x-6x^2+2x^3+\cdots



$$

The idea is to manipulate the above expression for $A$ so that we obtain a closed expression instead of an infinite series. We can do this using the recurrence relation $(\ast).$

Notice that the coefficient of the term $a_{n-1}$ in $(\ast)$ is $0.$ The coefficient of the term $a_{n-2}$ in $(\ast)$ is $2.$ So, we multiply both sides of the equation for $A$ by $2x^2\mathbin{:}$

$$



\begin{aligned}2𝑥^{2}𝐴 & =6𝑥^{2}−2𝑥^{3}−12𝑥^{4}+4𝑥^{5}+⋯\end{aligned}



$$

Adding $A$ and $2x^2A,$ we obtain the following:

$$



\begin{aligned}𝐴 & =3−0𝑥−6𝑥^{2}+2𝑥^{3}+⋯ \\ 2𝑥^{2}𝐴 & =0−0𝑥+6𝑥^{2}−2𝑥^{3}+⋯ \\ 𝐴+2𝑥^{2}𝐴 & =3−0𝑥+0𝑥^{2}+0𝑥^{3}+⋯\end{aligned}



$$

Notice that the coefficients from the $x^2$ term onward on the right-hand side are constructed from a sum that satisfies the recurrence relation and, therefore, must all be zero. Consequently, we are left with

$$



A+2x^2A = 3-x.



$$

Finally, we can solve for $A,$ as follows:

$$



\begin{aligned}𝐴+2𝑥^{2}𝐴 & =3−𝑥 \\ (1+2𝑥^{2})𝐴 & =3−𝑥 \\ 𝐴 & =\frac{3−𝑥}{1+2𝑥^{2}}\end{aligned}



$$
