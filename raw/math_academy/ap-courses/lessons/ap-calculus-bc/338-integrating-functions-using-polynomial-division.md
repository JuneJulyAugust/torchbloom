# Integrating Functions Using Polynomial Division

Source: https://www.mathacademy.com/topics/338?courseId=21
Topic ID: 338

## Prerequisites

- [Calculating Definite Integrals Using Substitution](../ap-calculus-ab/1159-calculating-definite-integrals-using-substitution.md)

## Lesson

### Introduction

How do we calculate $\displaystyle \int\dfrac{3x+2}{x+2}\,\textrm d x\,?$

We need to write the integrand so that it's something we can integrate. One way to do this is to divide $3x+2$ by $x+2$ using polynomial or synthetic division. We'll use synthetic division because it's faster.

To rewrite $\dfrac{3x+2}{x+2},$ we complete a synthetic division table.

This tells us that $\dfrac{3x+2}{x+2}$ can be decomposed into a quotient and remainder as

$$


\dfrac{3x+2}{x+2}= 3 - \dfrac{4}{x+2}.


$$

Now, we can integrate the function, which gives

$$


\begin{aligned}∫\frac{3𝑥+2}{𝑥+2}\,d𝑥 & =∫(3−\frac{4}{𝑥+2})\,d𝑥 \\ & =∫3\,d𝑥−4∫\frac{1}{𝑥+2}\,d𝑥 \\ & =3𝑥−4ln⁡|𝑥+2|+𝐶.\end{aligned}


$$

### Example: Integrating a Quotient of Linear Polynomials

#### Question

Calculate $\displaystyle\int_0^1 \dfrac{4x-1}{x+1}\,\textrm d x.$

#### Explanation

The denominator of the integrand doesn't divide the numerator exactly, so we need to decompose it into its quotient and remainder. For this, we can use synthetic division.

We start by drawing up our synthetic division table:

So, from the synthetic division, we get that

$$


\dfrac{4x-1}{x+1} = 4 -\dfrac{5}{x+1}.


$$

Therefore,

$$


\begin{aligned}∫_{10}^{}\frac{4𝑥−1}{𝑥+1}\,d𝑥 & =∫_{10}^{}(4−\frac{5}{𝑥+1})\,d𝑥 \\ & =∫_{10}^{}4\,d𝑥−5∫_{10}^{}\frac{1}{𝑥+1}\,d𝑥 \\ & =4𝑥_{10}^{}−5ln⁡|𝑥+1|_{10}^{} \\ & =[4−0]−5[ln⁡2−ln⁡1] \\ & =4−5ln⁡2.\end{aligned}


$$

### Example: Integrating a Rational Function Whose Denominator is Linear

#### Question

Calculate $\displaystyle\int \dfrac{2x^2-3x-4}{x-3}\,\textrm d x.$

#### Explanation

We first need to decompose the integrand into its quotient and remainder parts, which we can do using synthetic division.

We draw up a synthetic division table:

So, from the synthetic division, we get that

$$


\begin{aligned} \dfrac{ 2x^2-3x-4}{x-3} = 2x + 3 + \dfrac {5}{x-3} . \end{aligned}


$$

Therefore,

$$


\begin{aligned}∫\frac{2𝑥^{2}−3𝑥−4}{𝑥−3}\,d𝑥 & =∫(2𝑥+3+\frac{5}{𝑥−3})\,d𝑥 \\ & =𝑥^{2}+3𝑥+5ln⁡|𝑥−3|+𝐶.\end{aligned}


$$

### Example: Integrating a Rational Function Whose Denominator Contains a Leading Coefficient

#### Question

Evaluate $\displaystyle\int \dfrac{x-1}{2x-1}\,\textrm d x.$

#### Explanation

First, we pull out the factor of $2$ from the denominator:

$$


\begin{aligned}∫\frac{𝑥−1}{2𝑥−1}\,d𝑥 & =∫\frac{𝑥−1}{2(𝑥−\frac{1}{2})}\,d𝑥 \\ & =\frac{1}{2}∫\frac{𝑥−1}{(𝑥−\frac{1}{2})}\,d𝑥\end{aligned}


$$

Then, we draw up our synthetic division table to decompose the integrand into its quotient and remainder.

So, from the synthetic division, we get that

$$


\begin{aligned}\frac{𝑥−1}{(𝑥−\frac{1}{2})} & =1−\frac{(\frac{1}{2})}{2} \\ & =1−\frac{1}{2(𝑥−\frac{1}{2})} \\ & =1−\frac{1}{2𝑥−1}.\end{aligned}


$$

Therefore,

$$


\begin{aligned}∫\frac{𝑥−1}{2𝑥−1}\,d𝑥 & =\frac{1}{2}∫(1−\frac{1}{2𝑥−1})\,d𝑥 \\ & =\frac{1}{2}[𝑥−\frac{1}{2}ln⁡|2𝑥−1|]+𝐶 \\ & =\frac{1}{2}𝑥−\frac{1}{4}ln⁡|2𝑥−1|+𝐶.\end{aligned}


$$
