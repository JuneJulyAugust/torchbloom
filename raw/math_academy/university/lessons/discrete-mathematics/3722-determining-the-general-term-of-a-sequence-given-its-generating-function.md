# Determining the General Term of a Sequence Given Its Generating Function

Source: https://www.mathacademy.com/topics/3722?courseId=109
Topic ID: 3722

## Prerequisites

- [Expressing Rational Functions as Sums of Partial Fractions](../../../ap-courses/lessons/ap-calculus-bc/1060-expressing-rational-functions-as-sums-of-partial-fractions.md)
- [Generating Functions](./3083-generating-functions.md)

## Lesson

### Introduction

We can use well-known series to recover the sequence associated with a generating function.

One series that occurs regularly for this purpose is the geometric series

$$



\dfrac{1}{1-r} = 1+r+r^2+r^3+\cdots\,.



$$

For example, let's determine the general term $a_n$ for $n\geq 0$ of the sequence with generating function

$$



\dfrac{3}{5+2x}.



$$

First, we rewrite the generating function by factoring out the term of the form $\dfrac{1}{1-r}{:}$

$$



\begin{aligned}\frac{3}{5+2𝑥} & =\frac{3}{5}⋅\frac{1}{(1+\frac{2}{5}𝑥)} \\ & =\frac{3}{5}⋅\frac{1}{[1−(−\frac{2}{5}𝑥)]}\end{aligned}



$$

Then, we expand the right-hand side using the geometric series formula:

$$



\begin{aligned}\frac{3}{5}[1+(−\frac{2}{5}𝑥)+(−\frac{2}{5}𝑥)^{2}+(−\frac{2}{5}𝑥)^{3}+⋯]\end{aligned}



$$

This simplifies to

$$



\begin{aligned}\frac{3}{5}+\frac{3}{5}(−\frac{2}{5})𝑥+\frac{3}{5}(−\frac{2}{5})^{2}𝑥^{2}+\frac{3}{5}(−\frac{2}{5})^{3}𝑥^{3}+⋯\,.\end{aligned}



$$

Finally, we identify that the general term $a_n$ of our sequence is

$$



a_n = \dfrac{3}{5}\left(-\dfrac{2}{5}\right)^n.



$$

### Example: Determining the General Term of a Sequence Given Its Generating Function

#### Question

Find the expression for the general term $a_n$ for $n\geq 0$ of the sequence with the generating function $\dfrac{6}{5-4x}.$

#### Explanation

Let's rewrite the expression and expand it as a geometric series:

$$



\begin{aligned}\frac{6}{5−4𝑥} & =\frac{6}{5}⋅\frac{1}{1−(\frac{4}{5}𝑥)} \\ & =\frac{6}{5}[1+(\frac{4}{5}𝑥)+(\frac{4}{5}𝑥)^{2}+(\frac{4}{5}𝑥)^{3}+⋯] \\ & =\frac{6}{5}+\frac{6}{5}(\frac{4}{5})𝑥+\frac{6}{5}(\frac{4}{5})^{2}𝑥^{2}+\frac{6}{5}(\frac{4}{5})^{3}𝑥^{3}+⋯\end{aligned}



$$

Therefore, the general term $a_n$ of our sequence is

$$



a_n = \dfrac{6}{5}\left(\dfrac{4}{5}\right)^n.



$$

### Determining the General Term of a Sequence Using Partial Fractions

In some cases, a generating function can be written as a combination of simpler functions that, in turn, can be further reduced to geometric series.

For example, suppose we have the generating function

$$



\dfrac{2x+6}{2-x-6x^2}\,.



$$

To calculate the generating series, we first factor the denominator:

$$



\dfrac{2x+6}{2-x-6x^2} = \dfrac{2x+6}{(1-2x)(2+3x)}



$$

Then, we express the function as a sum of partial fractions:

$$



\dfrac{2x+6}{(1-2x)(2+3x)} = \dfrac{2}{1-2x} + \dfrac{2}{2+3x}



$$

Next, we expand each of the partial fractions as a geometric series:

For the first sequence, we have

$$



\begin{aligned}\frac{2}{1−2𝑥} & =2⋅\frac{1}{1−2𝑥} \\ & =2⋅(1+(2𝑥)+(2𝑥)^{2}+(2𝑥)^{3}) \\ & =(2)+(2)^{2}𝑥+(2)^{3}𝑥^{2}+(2)^{4}𝑥^{3}+⋯\,.\end{aligned}



$$

The general term of the sequence associated with this generating series is $b_n=2^{n+1}.$

For the second sequence, we have

$$



\begin{aligned}\frac{2}{2+3𝑥} & =\frac{2}{2}⋅\frac{1}{[1+(\frac{3}{2})]} \\ & =\frac{1}{[1+(\frac{3}{2})]} \\ & =1+(−\frac{3}{2}𝑥)+(−\frac{3}{2}𝑥)^{2}+(−\frac{3}{2}𝑥)^{3}+⋯\,.\end{aligned}



$$

The general term of the sequence associated with this generating series is $c_n=\left(-\dfrac{3}{2}\right)^n.$

Finally, the general term of the sequence associated with our original function is

$$



a_n = b_n + c_n = 2^{n+1} + \left(-\dfrac{3}{2}\right)^n\,.



$$

### Example: Determining the General Term of a Sequence Using a Sum of Partial Fractions

#### Question

Find an expression for the general term $a_n$ for $n\geq 0$ of the sequence with the generating function

$$



\dfrac{3x}{(2x+1)(x-1)}.



$$

#### Explanation

First, we rewrite our fraction as a sum of partial fractions:

$$



\begin{aligned}\frac{3𝑥}{(2𝑥+1)(𝑥−1)} & =\frac{𝐴}{(2𝑥+1)}+\frac{𝐵}{(𝑥−1)}\end{aligned}



$$

Multiplying both sides by $(2x+1)(x-1)$ gives

$$



\begin{aligned}3𝑥 & =𝐴(𝑥−1)+𝐵(2𝑥+1).\end{aligned}



$$

We now find the coefficients $A$ and $B\mathbin{:}$

- Substituting $x=-\dfrac{1}{2},$ we get $A = 1.$

- Substituting $x=1,$ we get $B =1.$

Hence,

$$



\dfrac{3x}{(2x+1)(x-1)} = \dfrac{1}{2x+1} + \dfrac{1}{x-1}.



$$

Next, we expand each of the partial fractions as a geometric series.

$$



\begin{aligned}\frac{1}{2𝑥+1} & =\frac{1}{1−(−2𝑥)} \\ & =1+(−2𝑥)+(−2𝑥)^{2}+(−2𝑥)^{3}+⋯ \\ & =1+(−2)𝑥+(−2)^{2}𝑥^{2}+(−2)^{3}𝑥^{3}+⋯ \\ \frac{1}{𝑥−1} & =(−1)\frac{1}{1−𝑥} \\ & =(−1)⋅(1+𝑥+𝑥^{2}+𝑥^{3}+⋯) \\ & =(−1)+(−1)𝑥+(−1)𝑥^{2}+(−1)𝑥^{3}+⋯\end{aligned}



$$

The general term of the first sequence is $b_n = \left(-2\right)^n,$ while the general term of the second sequence is $c_n = -1.$

Therefore, the general term of our original sequence is

$$



\begin{aligned}𝑎_{𝑛} & =𝑏_{𝑛}+𝑐_{𝑛} \\ & =(−2)^{𝑛}+(−1) \\ & =(−2)^{𝑛}−1.\end{aligned}



$$
