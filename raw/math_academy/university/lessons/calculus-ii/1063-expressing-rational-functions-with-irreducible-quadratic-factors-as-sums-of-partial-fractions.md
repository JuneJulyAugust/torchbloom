# Expressing Rational Functions with Irreducible Quadratic Factors as Sums of Partial Fractions

Source: https://www.mathacademy.com/topics/1063?courseId=106
Topic ID: 1063

## Prerequisites

- [Expressing Rational Functions as Sums of Partial Fractions](./1060-expressing-rational-functions-as-sums-of-partial-fractions.md)

## Lesson

### Introduction

Let's consider the following fraction:

$$


\dfrac{3x^2-x+1}{(x^2+2)(x-1)}


$$

How can we rewrite it as a sum of partial fractions?

First, we note the following:

- The degree of the polynomial in the numerator (quadratic) is *smaller than* that of the denominator (cubic). This means we can find a partial fraction representation.

- The factor $(x^2+2$) cannot be written as a product of linear factors with real coefficients. We call this an **irreducible quadratic factor.**

In such cases, our decomposition will be of the form

$$


\dfrac{3x^2-x+1}{(x^2+2)(x-1)} = \dfrac{?}{x^2+2} + \dfrac{?}{x-1}.


$$

Now, since the degree of the numerator on the left-hand side is *smaller than* the degree of the denominator, we must have the same property for the fractions on the right-hand side. Otherwise, our rational expression will contain a nonzero integer part. Therefore, we have

- a first-degree polynomial $Ax+B$ over $x^2+2,$ and

- a zero-degree polynomial $C$ over $x-1.$

Therefore, we seek a partial fraction decomposition of the form

$$


\dfrac{3x^2-x+1}{(x^2+2)(x-1)} = \dfrac{Ax+B}{x^2+2} + \dfrac{C}{x-1}.


$$

To find the coefficients $A, B,$ and $C,$ we multiply both sides by $(x^2+2)(x-1)$ and get

$$


3x^2-x+1 = (Ax+B)(x-1) + C(x^2+2).


$$

By expanding the right-hand side and combining the like terms, we have

$$


\begin{aligned}3𝑥^{2}−𝑥+1 & =(𝐴+𝐶)𝑥^{2}+(𝐵−𝐴)𝑥+(2𝐶−𝐵).\end{aligned}


$$

Comparing the coefficients of polynomials on the left-hand side and the right-hand side, we get the following system of linear equations:

$$


\begin{aligned}𝐴+𝐶=3 \\ 𝐵−𝐴=−1 \\ 2𝐶−𝐵=1\end{aligned}


$$

Notice that we have three equations and three unknowns. An equal number of equations and unknowns is generally a *good thing* when solving equations, as it makes a solution more likely to exist.

Solving the system, we obtain $A=2,$ $B=1,$ and $C=1.$ Therefore, our final result is

$$


\dfrac{3x^2-x+1}{(x^2+2)(x-1)} = \dfrac{2x+1}{x^2+2} + \dfrac{1}{x-1}.


$$

Solving a system of three linear equations is cumbersome. Let's discuss a faster method.

### Finding the Coefficients

In practice, it's often easier and faster to substitute some nice values of $x$ to determine the unknown coefficients.

Let's go back to the following equation:

$$


3x^2-x+1 = (Ax+B)(x-1) + C(x^2+2),


$$

If we carefully select values of $x$ to substitute into the above, we can make light work of finding the coefficients:

- Plugging in $x=1$ eliminates the $A$ and $B$ terms and allows us to solve for $C.$ We get

- Plugging in $x=0$ eliminates the $A$ term, and using our result for $C$ allows us to solve for $B.$ We get

- We still need to solve for $A.$ To do this, we can substitute our results for $B$ and $C$ and plug in any value of $x$ we haven't already used. We've already used $x=0$ and $x=1,$ so we'll plug in a different simple value of $x,$ say $x=-1.$ Doing this, we get

So, we have $A=2, B=1, C=1,$ the same as before.

### Example: Computing Coefficients in a Partial Fractions Decomposition

#### Question

Given that

$$


\dfrac{7 x^2 - 2x - 13 }{(x^2+1)(x+1) } = \dfrac{9x+B}{ x^2 +1} - \dfrac{2}{x+1} ,


$$

what is the value of $B?$

#### Explanation

Multiplying both sides of the given equality by $(x^2+1)(x+1)$ gives

$$


\begin{aligned}7𝑥^{2}−2𝑥−13 & =(9𝑥+𝐵)(𝑥+1)−2(𝑥^{2}+1).\end{aligned}


$$

Letting $x=0$ gives

$$


\begin{aligned}7(0)^{2}−2(0)−13 & =(9⋅(0)+𝐵)(0+1)−2((0)^{2}+1) \\ −13 & =𝐵−2 \\ 𝐵 & =−11.\end{aligned}


$$

### Example: Expressing Rational Functions as a Sum of Partial Fractions

#### Question

Express $\dfrac{2x+3}{(x^2+4)(x-1)}$ as a sum of partial fractions.

#### Explanation

Our task is to find $A,$ $B$ and $C$ such that

$$


\begin{aligned}\frac{2𝑥+3}{(𝑥^{2}+4)(𝑥−1)} & =\frac{𝐴𝑥+𝐵}{𝑥^{2}+4}+\frac{𝐶}{𝑥−1}.\end{aligned}


$$

Note that since $x^2+4$ is an irreducible quadratic factor, we must use a linear term $Ax+B$ in the numerator.

We multiply both sides by $(x^2+4)(x-1)$ and get

$$


\begin{aligned}2𝑥+3 & =(𝐴𝑥+𝐵)(𝑥−1)+𝐶(𝑥^{2}+4).\end{aligned}


$$

Plugging in $x=1$ eliminates the $A$ and $B$ terms and allows us to solve for $C.$ We get

$$


\begin{aligned}2(1)+3 & =(𝐴(1)+𝐵)(1−1)+𝐶(1^{2}+4) \\ 5 & =5𝐶 \\ 𝐶 & =1.\end{aligned}


$$

Plugging in $x=0$ eliminates the $A$ term, and using our result for $C$ allows us to solve for $B.$ We get

$$


\begin{aligned}2(0)+3 & =(𝐴(0)+𝐵)(0−1)+𝐶(0^{2}+4) \\ 3 & =−𝐵+4𝐶 \\ 3 & =−𝐵+4(1) \\ 𝐵 & =1.\end{aligned}


$$

Finally, to solve for $A,$ we choose $x=2$ and use our results for $B$ and $C.$ We get

$$


\begin{aligned}2(2)+3 & =(𝐴(2)+𝐵)(2−1)+𝐶(2^{2}+4) \\ 7 & =2𝐴+𝐵+8𝐶 \\ 7 & =2𝐴+1+8(1) \\ 2𝐴 & =−2 \\ 𝐴 & =−1.\end{aligned}


$$

So we have $A=-1,$ $B=1,$ and $C=1.$ Therefore, our final result is

$$


\dfrac{2x+3}{(x^2+4)(x-1)} = \dfrac{1-x}{x^2+4} +\dfrac{1}{x-1}.


$$
