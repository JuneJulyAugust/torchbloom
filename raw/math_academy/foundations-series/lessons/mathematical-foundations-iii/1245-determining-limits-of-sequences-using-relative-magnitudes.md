# Determining Limits of Sequences Using Relative Magnitudes

Source: https://www.mathacademy.com/topics/1245?courseId=136
Topic ID: 1245

## Prerequisites

- [Evaluating Limits at Infinity by Comparing Relative Magnitudes of Functions](./607-evaluating-limits-at-infinity-by-comparing-relative-magnitudes-of-functions.md)
- [Limits of Sequences](./1087-limits-of-sequences.md)

## Lesson

### Introduction

What is the limit of the sequence $a_n$ given by

$$


a_n = \dfrac{n}{2^n}, \qquad n\geq 1\, ?


$$

Both the numerator and denominator grow without bound as $n\to\infty.$ However, we notice that for large values of $n,$ we get

$$


a_n = \dfrac{n}{2^n} = \dfrac{\textrm{a fairly big number}}{\textrm{an enormous number}}.


$$

The gap between the numerator and denominator continues to grow as $n\to\infty.$ So, the limit of the sequence is

$$


\lim_{n\to\infty} a_n = 0.


$$

In other words, the sequence converges to zero.

While this is not a rigorous argument, it's a handy technique that can help us to identify whether specific sequences converge or diverge.

Recall that for large values of $n,$ we have

$$


n! \gg e^{n} \gg n^m \gg \ln(n),


$$

where $\gg$ means **much greater than**, and $m\gt 0.$ We can use this to solve a variety of problems involving limits at infinity.

### Example: Determining the Convergence of Sequences Containing Power and Exponential Functions

#### Question

What is the limit of the sequence $a_n = \dfrac{n^{100}}{e^n}$ for $n\geq 1?$

#### Explanation

Recall that for large values of $n,$ we have

$$


n! \gg e^{n} \gg n^m \gg \ln(n),


$$

where $\gg$ means "much greater than," and $m \gt 0.$

We calculate the limit of the sequence as $n$ approaches infinity:

$$


\lim_{n\to \infty} a_n = \lim_{n\to \infty}\dfrac{n^{100}}{e^n}


$$

Both the numerator and denominator approach infinity as $n\to\infty.$ However, the denominator is growing much faster than the numerator, and we conclude that

$$


\lim_{n\to \infty}\dfrac{n^{100}}{e^n} = 0.


$$

Therefore, the sequence converges, and its limit is $0.$

### Example: Determining the Convergence Sequences Containing Power and Logarithmic Functions

#### Question

Does the sequence $a_n = \dfrac{n}{\ln{n}}$ for $n\gt 1$ converge or diverge? If the sequence converges, what is its limit?

#### Explanation

Recall that for large values of $n,$ we have

$$


n! \gg e^{n} \gg n^m \gg \ln(n),


$$

where $\gg$ means "much greater than," and $m \gt 0.$

We calculate the limit of the sequence as $n$ approaches infinity:

$$


\lim_{n\to \infty} a_n = \lim_{n\to \infty}\dfrac{n}{\ln{n}}


$$

Both the numerator and denominator approach infinity as $n\to\infty.$ However, the numerator is growing much faster than the denominator, and we conclude that

$$


\lim_{n\to \infty}\dfrac{n}{\ln{n}} = \infty.


$$

The limit does not exist. Therefore, the sequence diverges.

### Example: Determining the Convergence of Sequences Containing Exponential Logarithmic Function

#### Question

What is the limit of the sequence $a_n = \dfrac{e^{2n}}{\ln{n}}$ for $n\geq 1?$

#### Explanation

Recall that for large values of $n,$ we have

$$


n! \gg e^{n} \gg n^m \gg \ln(n),


$$

where $\gg$ means "much greater than," and $m \gt 0.$

To find the limit, we calculate

$$


\lim_{n\to \infty} a_n = \lim_{n\to \infty}\dfrac{e^{2n}}{\ln{n}}.


$$

Both the numerator and denominator approach infinity as $x\to\infty.$ However, the numerator is growing much faster than the denominator, and we conclude that

$$


\lim_{n\to \infty}\dfrac{e^{2n}}{\ln{n}} = \infty.


$$

The limit does not exist. Therefore, the sequence diverges.
