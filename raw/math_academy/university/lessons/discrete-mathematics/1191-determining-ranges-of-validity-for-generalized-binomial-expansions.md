# Determining Ranges of Validity for Generalized Binomial Expansions

Source: https://www.mathacademy.com/topics/1191?courseId=109
Topic ID: 1191

## Prerequisites

- [Working With the Generalized Binomial Theorem](./695-working-with-the-generalized-binomial-theorem.md)

## Lesson

### Introduction

The **range of validity** of a binomial expansion is an expression describing all $x$-values for which the binomial expansion converges. The range of validity of a binomial expansion is also known as its **interval of convergence.**

Recall that the generalized binomial expansion of $(1+x)^n$ for rational $n$ is given by

$$



(1+x)^n = 1 + nx + \dfrac{n(n-1)x^2}{2!} + \dfrac{n(n-1)(n-2)x^3}{3!}+\cdots.



$$

For this binomial expansion, the range of validity is $|x| < 1.$ This means the following:

- If $|x|< 1,$ the infinite series converges, and the left-hand side equals the right-hand side.

- If $|x|\geq1,$ the infinite series diverges, and consequently, the left-hand side does *not* equal the right-hand side.

How can we find the range of validity of the following binomial expansion?

$$



\dfrac{1}{5-3x} = \dfrac{1}{5} + \dfrac{3}{25}x + \dfrac{9}{125}x^2 + \dfrac{27}{625}x^3 + \cdots



$$

To determine the range of validity in this case, we apply the following steps:

- First, rewrite the given expression in the form $a(1+bx)^n.$

- Then, we solve the absolute value equation $|bx|<1$ for the variable $x$.

Therefore, in our case we have

$$



\begin{aligned} \dfrac{1}{5-3x} & = (5-3x)^{-1} \\[5pt] & = \left(5\left(1-\dfrac{3}{5}x\right)\right)^{-1} \\[5pt] & = (5)^{-1}\left(1-\dfrac{3}{5}x\right)^{-1} \\[5pt] & = \dfrac{1}{5}\left(1-\dfrac{3}{5}x\right)^{-1}. \end{aligned}



$$

Therefore, we conclude that the given expansion is convergent if

$$



\left| - \dfrac{3}{5}x \right| < 1.



$$

Let's solve this absolute value equation for the variable $x.$

$$



\begin{aligned}−\frac{3}{5}𝑥 & <1 \\ −\frac{3}{5}⋅|𝑥| & <1 \\ \frac{3}{5}⋅|𝑥| & <1 \\ |𝑥| & <\frac{5}{3}\end{aligned}



$$

Therefore, the range of validity is $|x| < \dfrac53.$

### Example: Determining Ranges of Validity for Binomial Expansions of Powers

#### Question

Calculate the range of validity of the binomial expansion

$$



\dfrac{128}{(4+x)^3} = 2 - \dfrac{3}{2}x + \dfrac{3}{4}x^2 - \cdots .



$$

#### Explanation

First, we write the expression $\dfrac{128}{(4+x)^3}$ in the form $a(1+bx)^n{:}$

$$



\begin{aligned} \dfrac{128}{(4+x)^3} & = 128(4+x)^{-3} \\[5pt] & = 128\left(4\left(1+\dfrac{1}{4}x\right)\right)^{-3} \\[5pt] & = 128(4)^{-3}\left(1+\dfrac{1}{4}x\right)^{-3} \\[5pt] & = \dfrac{128}{64}\left(1+\dfrac{1}{4}x\right)^{-3} \\[5pt] & = 2\left(1+\dfrac{1}{4}x\right)^{-3} \end{aligned}



$$

Recall that the series on the right-hand side of

$$



(1+x)^{n}= 1 + {n}x + {n}({n-1}) \dfrac{x^2}{2!}+ {n}({n-1})( {n-2 })\dfrac{x^3}{3!} + \cdots



$$

converges only when $|x|< 1.$

Therefore,

$$



\dfrac{128}{(4+x)^3} = 2\left(1+\dfrac{1}{4}x\right)^{-3} = 2 - \dfrac{3}{2}x + \dfrac{3}{4}x^2 - \cdots



$$

is valid only for $\left| \dfrac{1}{4}x \right| < 1,$ or equivalently, for $|x| < 4.$

### Example: Determining Ranges of Validity for Binomial Expansions of Radicals

#### Question

Calculate the range of validity of the binomial expansion

$$



\dfrac{20}{\sqrt{16+64x}} = 5 - 10x + 30x^2 - \cdots .



$$

#### Explanation

First, we write the expression $\dfrac{20}{\sqrt{16+64x}}$ in the form $a(1+bx)^n{:}$

$$



\begin{aligned} \dfrac{20}{\sqrt{16+64x}} & = \dfrac{20}{(16+64x)^{{1}/{2}}} \\[5pt] & = 20(16+64x)^{-{1}/{2}} \\[5pt] & = 20\left(16\left(1+4x\right)\right)^{-{1}/{2}} \\[5pt] & = 20(16)^{-{1}/{2}}\left(1+4x\right)^{-{1}/{2}} \\[5pt] & = \dfrac{20}{(16)^{{1}/{2}}}\left(1+4x\right)^{-{1}/{2}} \\[5pt] & = \dfrac{20}{4}\left(1+4x\right)^{-{1}/{2}} \\[5pt] & = 5\left(1+4x\right)^{-{1}/{2}} \end{aligned}



$$

Recall that the series on the right-hand side of

$$



(1+x)^{n}= 1 + {n}x + {n}({n-1}) \dfrac{x^2}{2!}+ {n}({n-1})( {n-2 })\dfrac{x^3}{3!} + \cdots



$$

converges only when $|x|< 1.$

Therefore,

$$



\dfrac{20}{\sqrt{16+64x}} = 5\left(1+4x\right)^{-{1}/{2}} = 5 - 10x + 30x^2 - \cdots



$$

is valid only for $\left| 4x \right| < 1$ or, equivalently, for $|x| < \dfrac{1}{4}.$
