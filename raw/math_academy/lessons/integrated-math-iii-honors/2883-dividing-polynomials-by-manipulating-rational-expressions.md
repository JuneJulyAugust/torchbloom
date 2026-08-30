# Dividing Polynomials by Manipulating Rational Expressions

Source: https://www.mathacademy.com/topics/2883?courseId=101
Topic ID: 2883

## Prerequisites

- [Splitting Rational Expressions Into Separate Terms](../algebra-ii/355-splitting-rational-expressions-into-separate-terms.md)
- [Dividing Polynomials Using Synthetic Division](./728-dividing-polynomials-using-synthetic-division.md)

## Lesson

### Introduction

Sometimes, we can divide polynomials quickly by cleverly manipulating a rational function.

For example, suppose we wish to divide $x$ by $x+2.$ Then we have the following rational expression:

$$


\dfrac{x}{x+2}


$$

The goal is to write this rational expression in the form

$$


\dfrac{x}{x+2} = a + \dfrac{b}{x+2}


$$

where $a$ and $b$ are both constants. Here, $a$ is the quotient of the division, and $b$ is the remainder.

To manipulate the rational function into this form, we can add and subtract $2$ in the numerator. This reveals a copy of the denominator without changing the value of the expression.

$$


\begin{aligned}\frac{𝑥}{𝑥+2}=\frac{𝑥+2−2}{𝑥+2}\end{aligned}


$$

Then, we expand and simplify the fraction:

$$


\begin{aligned}\frac{𝑥+2−2}{𝑥+2} & =\frac{𝑥+2}{𝑥+2}+\frac{−2}{𝑥+2} \\ & =1+\frac{−2}{𝑥+2}\end{aligned}


$$

So we have $a=1$ and $b=-2,$ and we've reached the desired result:

$$


\dfrac{x}{x+2} = 1 + \dfrac{-2}{x+2}


$$

### Example: Manipulating Rational Expressions With Single-Term Numerators

#### Question

Write $\dfrac{5x^2}{5x^2-2}$ in the form $a + \dfrac{b}{5x^2-2},$ where $a \neq 0.$ What is the value of $a+b?$

#### Explanation

First, we subtract and add $2$ in the numerator. This reveals a copy of the denominator without changing the value of the expression.

$$


\begin{aligned}\frac{5𝑥^{2}}{5𝑥^{2}−2}=\frac{5𝑥^{2}−2+2}{5𝑥^{2}−2}\end{aligned}


$$

Then, we split the fraction into two, and then simplify:

$$


\begin{aligned}\frac{5𝑥^{2}−2+2}{5𝑥^{2}−2} & =\frac{5𝑥^{2}−2}{5𝑥^{2}−2}+\frac{2}{5𝑥^{2}−2} \\ & =1+\frac{2}{5𝑥^{2}−2}\end{aligned}


$$

Therefore, we have $a=1$ and $b=2,$ and we get

$$


a + b = 1 + 2 = 3.


$$

### Manipulations With Two-Term Numerators

We can use the same method to manipulate rational expressions with two terms in the numerator. For example, consider the following rational expression:

$$


\dfrac{x+5}{x+2}


$$

In order to write this rational expression in the form

$$


\dfrac{x+5}{x+2} = a + \dfrac{b}{x+2}


$$

where $a$ and $b$ are constants, we can apply the same trick: add and subtract $2$ in the numerator. This reveals a copy of the denominator without changing the value of the expression.

$$


\begin{aligned}\frac{𝑥+5}{𝑥+2}=\frac{𝑥+2−2+5}{𝑥+2}\end{aligned}


$$

Then, we expand and simplify the fraction:

$$


\begin{aligned}\frac{𝑥+2−2+5}{𝑥+2} & =\frac{𝑥+2}{𝑥+2}+\frac{−2+5}{𝑥+2} \\ & =1+\frac{3}{𝑥+2}\end{aligned}


$$

So we have $a=1$ and $b=3,$ and we've reached the desired result:

$$


\dfrac{x+5}{x+2} = 1 + \dfrac{3}{x+2}


$$

### Example: Manipulating Rational Expressions With Two-Term Numerators

#### Question

Write $\dfrac{3x^2+5}{3x^2-2x}$ in the form $a + \dfrac{bx+c}{3x^2-2x},$ where $a \neq 0.$ What is the value of $a+b+c?$

#### Explanation

First, we subtract and add $2x$ in the numerator. This reveals a copy of the denominator without changing the value of the expression.

$$


\begin{aligned}\frac{3𝑥^{2}+5}{3𝑥^{2}−2𝑥}=\frac{3𝑥^{2}−2𝑥+2𝑥+5}{3𝑥^{2}−2𝑥}\end{aligned}


$$

Then, we split the fraction into two, and then simplify:

$$


\begin{aligned}\frac{3𝑥^{2}−2𝑥+2𝑥+5}{3𝑥^{2}−2𝑥} & =\frac{3𝑥^{2}−2𝑥}{3𝑥^{2}−2𝑥}+\frac{2𝑥+5}{3𝑥^{2}−2𝑥} \\ & =1+\frac{2𝑥+5}{3𝑥^{2}−2𝑥}\end{aligned}


$$

Therefore, we have $a=1,$ $b=2,$ and $c=5,$ and we get

$$


a + b + c = 1 + 2 + 5 = 8.


$$

### Manipulations Requiring Factoring

Sometimes, we have to factor the numerator of a rational expression in order to reveal a copy of the denominator. For example, consider the following rational expression:

$$


\dfrac{2x}{x+1}


$$

In order to write this rational expression in the form

$$


\dfrac{2x}{x+1} = a + \dfrac{b}{x+1},


$$

where $a$ and $b$ are constants, we can add and subtract $1$ in parentheses in the numerator. This will reveal a copy of the denominator without changing the value of the expression.

$$


\begin{aligned}\frac{2𝑥}{𝑥+1} & =\frac{2(𝑥+1−1)}{𝑥+1} \\ & =\frac{2(𝑥+1)+2(−1)}{𝑥+1} \\ & =\frac{2(𝑥+1)−2}{𝑥+1}\end{aligned}


$$

Then, we expand and simplify the fraction:

$$


\begin{aligned}\frac{2(𝑥+1)−2}{𝑥+1} & =\frac{2(𝑥+1)}{𝑥+1}+\frac{−2}{𝑥+1} \\ & =2+\frac{−2}{𝑥+1}\end{aligned}


$$

So we have $a=2$ and $b=-2,$ and we've reached the desired result:

$$


\dfrac{2x}{x+1} = 2 + \dfrac{-2}{x+1}


$$

### Example: Manipulating Rational Expressions With Single-Term Numerators When Factoring Is Required

#### Question

Write $\dfrac{3x^3}{x^3+4}$ in the form $a + \dfrac{b}{x^3+4},$ where $a \neq 0.$ What is the value of $a+b?$

#### Explanation

First, we add and subtract $4$ in parentheses in the numerator. This reveals a copy of the denominator without changing the value of the expression.

$$


\begin{aligned}\frac{3𝑥^{3}}{𝑥^{3}+4} & =\frac{3(𝑥^{3}+4−4)}{𝑥^{3}+4} \\ & =\frac{3(𝑥^{3}+4)+3(−4)}{𝑥^{3}+4} \\ & =\frac{3(𝑥^{3}+4)−12}{𝑥^{3}+4}\end{aligned}


$$

Then, we split the fraction into two, and then simplify:

$$


\begin{aligned}\frac{3(𝑥^{3}+4)−12}{𝑥^{3}+4} & =\frac{3(𝑥^{3}+4)}{𝑥^{3}+4}+\frac{−12}{𝑥^{3}+4} \\ & =3+\frac{−12}{𝑥^{3}+4}\end{aligned}


$$

Therefore, we have $a=3$ and $b=-12,$ and we get

$$


a + b = 3 + (-12) = -9.


$$
