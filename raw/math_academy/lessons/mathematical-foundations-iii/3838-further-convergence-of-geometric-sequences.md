# Further Convergence of Geometric Sequences

Source: https://www.mathacademy.com/topics/3838?courseId=136
Topic ID: 3838

## Prerequisites

- [Convergence of Geometric Sequences](./1088-convergence-of-geometric-sequences.md)
- [Combining the Rules of Exponents With Algebraic Expressions](../algebra-i/1417-combining-the-rules-of-exponents-with-algebraic-expressions.md)
- [Solving Elementary Quadratic Inequalities](./1495-solving-elementary-quadratic-inequalities.md)
- [Solving Inequalities Involving Positive and Negative Factors](./2982-solving-inequalities-involving-positive-and-negative-factors.md)

## Lesson

### Introduction

For a geometric sequence with the first term $a_1$ and common ratio $r,$ we have the following convergence properties:

- If $|r| < 1,$ the sequence is convergent and converges to $0.$

- If $|r| > 1,$ the sequence is divergent.

Moreover, we have the following edge cases:

- If $r=1,$ the sequence is convergent and converges to $a_1.$

- If $r = -1,$ the sequence is divergent.

With that in mind, let's determine whether the following geometric sequence is convergent or divergent:

$$


a_n=\dfrac {3 (-5)^{n }}{2 ^ {n}}, \qquad n\geq 1


$$

To determine whether the sequence is convergent or divergent, we first write the sequence in the form $a_n = a \cdot r^{n},$ as follows:

$$


\begin{aligned}𝑎_{𝑛} & =\frac{3⋅(−5)^{𝑛}}{2^{𝑛}} \\ & =3⋅\frac{(−5)^{𝑛}}{2^{𝑛}} \\ & =\underset{𝑎}{\underset{}{3}}⋅(\,\underset{𝑟}{\underset{}{−\frac{5}{2}}}\,)^{𝑛}\end{aligned}


$$

We can now see that this is the geometric sequence with common ratio $r= -\dfrac 5 2.$

Since $|r| > 1,$ the sequence is divergent.

### Example: Determining Whether a Geometric Sequence Converges Given the General Term

#### Question

Does the sequence $a_n = \dfrac {2 \cdot (-3) ^ n}{5 ^ {n + 1}}$ for $n\geq 1$ converge or diverge? If it converges, what is its limit?

#### Explanation

Suppose we have a geometric sequence with the first term $a_1$ and common ratio $r.$ Then, we have the following convergence properties:

- if $|r| < 1,$ the sequence is convergent and converges to $0$

- if $|r| > 1,$ the sequence is divergent

Moreover, we have the following edge cases:

- if $r=1,$ the sequence is convergent and converges to $a_1$

- if $r = -1,$ the sequence is divergent

First, we rewrite the sequence in the form $a_n = a \cdot r^{n},$ as follows:

$$


\begin{aligned}𝑎_{𝑛} & =\frac{2⋅(−3)^{𝑛}}{5^{𝑛+1}} \\ & =\frac{2⋅(−3)^{𝑛}}{5⋅5^{𝑛}} \\ & =\frac{2}{5}⋅\frac{(−3)^{𝑛}}{5^{𝑛}} \\ & =\frac{2}{5}(−\frac{3}{5})^{𝑛}.\end{aligned}


$$

We can now see that this is the geometric sequence with $r=-\dfrac{3}{5}.$

Since $|r| < 1,$ the sequence converges to $0.$

### Example: Determining Values for Which a Geometric Sequence Converges

#### Question

Consider the geometric sequence

$$


a_n =\dfrac{x^2}{2}\left(\dfrac{16}{x^2}\right)^{n}, \qquad n\geq 1


$$

where $x$ is a positive real number. For which values of $x$ is the sequence convergent?

#### Explanation

Suppose we have a geometric sequence with the first term $a_1$ and common ratio $r.$ Then, we have the following convergence properties:

- if $|r| < 1,$ the sequence is convergent and converges to $0$

- if $|r| > 1,$ the sequence is divergent

Moreover, we have the following edge cases:

- if $r=1,$ the sequence is convergent and converges to $a_1$

- if $r = -1,$ the sequence is divergent

The given sequence is a geometric sequence with the common ratio $r = \dfrac{16}{x^2}.$ Since $x^2$ is positive, $r$ is also positive, So, the convergence condition is $0 \lt r\leq 1.$

Therefore, the sequence converges for

$$


0 \lt\dfrac{16}{x^2}\leq 1 \qquad \Longrightarrow \qquad x^2 \geq 16.


$$

Taking into account the fact that $x$ is positive, we get

$$


x \geq 4.


$$

### Example: Determining Values for Which a Geometric Sequence Converges: Rearrangement Required

#### Question

Consider the sequence $a_n = \dfrac{x^{2n+1}}{x^{n-2}},$ where $x$ is a real positive number and $n\geq 1.$ What are the values of $x$ for which the sequence converges?

#### Explanation

Suppose we have a geometric sequence with the first term $a_1$ and common ratio $r.$ Then, we have the following convergence properties:

- if $|r| < 1,$ the sequence is convergent and converges to $0$

- if $|r| > 1,$ the sequence is divergent

Moreover, we have the following edge cases:

- if $r=1,$ the sequence is convergent and converges to $a_1$

- if $r = -1,$ the sequence is divergent

First, we rewrite the sequence in the form $a_n = a \cdot r^{n},$ as follows:

$$


\begin{aligned}𝑎_{𝑛} & =\frac{𝑥^{2𝑛+1}}{𝑥^{𝑛−2}} \\ & =𝑥^{2𝑛+1−𝑛+2} \\ & =𝑥^{𝑛+3} \\ & =𝑥^{3}⋅𝑥^{𝑛}.\end{aligned}


$$

We see that this is a geometric sequence with common ratio $r = x.$ Since $x$ is positive, $r$ is also positive. So, the convergence condition is $0 \lt r \leq 1.$

Therefore, the sequence converges for

$$


0 \lt x \leq 1 .


$$
