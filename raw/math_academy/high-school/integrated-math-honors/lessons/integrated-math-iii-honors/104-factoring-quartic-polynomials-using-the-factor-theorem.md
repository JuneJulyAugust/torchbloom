# Factoring Quartic Polynomials Using the Factor Theorem

Source: https://www.mathacademy.com/topics/104?courseId=101
Topic ID: 104

## Prerequisites

- [Factoring Cubic Polynomials Using the Factor Theorem](./2119-factoring-cubic-polynomials-using-the-factor-theorem.md)

## Lesson

### Introduction

If we are given one or more factors of a polynomial, we can use these factors to continue factoring the polynomial completely. We just need to divide the polynomial by the known factors, and then continue factoring the quotient.

For example, suppose we know that $(x+2)$ is a factor of $f(x) = x^4+4x^3+x^2-6x.$ Then $(x+2)$ divides $f(x)$ with no remainder. So, to begin factoring $f(x),$ we can divide it by $(x+2)$ using synthetic division:

$$


\begin{aligned}−2 & 1 & 4 & 1 & −6 & 0 \\ & & −2 & −4 & 6 & 0 \\ & 1 & 2 & −3 & 0 & 0\end{aligned}


$$

Therefore,

$$


\dfrac{x^4+4x^3+x^2-6x}{x+2} = x^3+2x^2-3x,


$$

which means that

$$


x^4+4x^3+x^2-6x = (x+2) (x^3+2x^2-3x).


$$

We can factor the cubic factor even further, and get

$$


\begin{aligned}(𝑥+2)(𝑥^{3}+2𝑥^{2}−3𝑥) & =(𝑥+2)(𝑥)(𝑥^{2}+2𝑥−3) \\ & =(𝑥+2)(𝑥)(𝑥+3)(𝑥−1) \\ & =𝑥(𝑥+2)(𝑥+3)(𝑥−1).\end{aligned}


$$

### Example: Factoring a Quartic Polynomial Given Two Factors

#### Question

Given that $(x-1)$ and $(x-3)$ are factors of the polynomial $f(x)= x^4 - x^3 - 7 x^2 + x + 6,$ factor $f(x)$ completely.

#### Explanation

To factor $f(x)$ completely, we need to find its other factors.

Because $(x-1)$ is a factor of $f(x),$ we know that $(x-1)$ divides $f(x)$ with no remainder. So, to begin factoring $f(x),$ we can divide it by $(x-1)$ using synthetic division:

Therefore,

$$


\dfrac{x^3-7x-6}{x-3} = x^2+3x +2,


$$

which means that

$$


x^4 - x^3 - 7 x^2 + x + 6 = (x-1) (x-3) (x^2+3x +2).


$$

We can factor the quadratic factor even further, and get

$$


x^4 - x^3 - 7 x^2 + x + 6 = (x-1) (x-3) (x+2)(x+1).


$$

### Example: Factoring a Quartic Polynomial Given Two Roots

#### Question

Let $p(x) = x^4 - x^3 - 9 x^2 - 11 x - 4.$ Knowing that $p(4) = p(-1) = 0,$ factor the polynomial $p(x)$ completely.

#### Explanation

Since $p(4) = p(-1) = 0,$ the factor theorem guarantees that $(x - 4)$ and $(x + 1)$ are both factors of $p(x).$ To factor $p(x)$ completely, we need to find its other factors.

Since $(x - 4)$ is a factor of $p(x),$ we know that $(x - 4)$ divides $p(x)$ with no remainder. So, to begin factoring $p(x),$ we can divide it by $(x - 4)$ using synthetic division:

Therefore,

$$


\dfrac{x^4 - x^3 - 9 x^2 - 11 x - 4}{x-4} = x^3+3x^2+3x+1,


$$

which means that

$$


x^4 - x^3 - 9 x^2 - 11 x - 4 = (x-4) ( x^3+3x^2+3x+1).


$$

Now, because $(x+1)$ is also a factor of $p(x),$ it must be a factor of the quotient $(x^3+3x^2+3x+1).$ So, we divide this quotient by $(x+1)$ using synthetic division once more:

Therefore,

$$


\dfrac{ x^3+3x^2+3x-1}{x+1} = x^2+2x+1,


$$

which means that

$$


x^4 - x^3 - 9 x^2 - 11 x - 4 = (x-4)(x+1)(x^2+2x+1).


$$

We can factor the quadratic factor even further, and get

$$


\begin{aligned}𝑥^{4}−𝑥^{3}−9𝑥^{2}−11𝑥−4 & =(𝑥−4)(𝑥+1)(𝑥+1)^{2} \\ & =(𝑥−4)(𝑥+1)^{3}.\end{aligned}


$$

### Example: Factoring a Quartic Polynomial With Only Two Real Factors

#### Question

Let $f(x) = 3 x^4 - 5 x^3 - 3 x^2 + 6 x - 8.$ If $x=2$ and $x=-\dfrac{4}{3}$ are zeros of $f(x),$ factor $f(x)$ completely.

#### Explanation

Because $x=2$ and $x=-\dfrac{4}{3}$ are both zeros of $f(x),$ the factor theorem guarantees that $(x-2)$ and $\left(x + \dfrac{4}{3} \right)$ are both factors of $f(x).$ So, $(x-2)$ and $\left(x + \dfrac{4}{3} \right)$ both divide $f(x).$

To begin factoring $f(x),$ we can divide it by one of these factors (it doesn't matter which one we divide first). Let's divide $f(x)$ by $(x-2)$ using synthetic division:

Therefore,

$$


\begin{aligned}𝑓(𝑥) & =3𝑥^{4}−5𝑥^{3}−3𝑥^{2}+6𝑥−8 \\ & =(𝑥−2)(3𝑥^{3}+𝑥^{2}−𝑥+4).\end{aligned}


$$

Now, because $\left(x+\dfrac{4}{3} \right)$ is also a factor of $f(x),$ it must be a factor of the quotient $3x^3 + x^2 - x +4.$ So, we divide this quotient by $\left(x+\dfrac{4}{3} \right)$ using synthetic division once more:

$$


\begin{aligned}3𝑥^{3}+𝑥^{2}−𝑥+4 & =(𝑥+\frac{4}{3})(3𝑥^{2}−3𝑥+3) \\ & =(𝑥+\frac{4}{3})(3)(𝑥^{2}−𝑥+1) \\ & =(3𝑥+4)(𝑥^{2}−𝑥+1),\end{aligned}


$$

which means that

$$


\begin{aligned}3𝑥^{4}−5𝑥^{3}−3𝑥^{2}+6𝑥−8 & =(𝑥−2)(3𝑥+4)(𝑥^{2}−𝑥+1).\end{aligned}


$$

The quadratic polynomial $x^2-x+1$ does not appear to factor over the real numbers. We can make sure of this by verifying that its discriminant is negative:

$$


\begin{aligned}D=𝑏^{2}−4𝑎𝑐=(−1)^{2}−4(1)(1)=−3<0\end{aligned}


$$

Therefore, the full factorization of $f(x)$ over the real numbers is given by

$$


f(x) = (x-2)(3x+4)(x^2-x+1).


$$
