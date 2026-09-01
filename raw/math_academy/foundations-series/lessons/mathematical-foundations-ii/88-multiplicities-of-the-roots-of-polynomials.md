# Multiplicities of the Roots of Polynomials

Source: https://www.mathacademy.com/topics/88?courseId=111
Topic ID: 88

## Prerequisites

- [Factoring Cubic Expressions by Grouping](./428-factoring-cubic-expressions-by-grouping.md)
- [Factoring Cubic Polynomials Using the Factor Theorem](./2119-factoring-cubic-polynomials-using-the-factor-theorem.md)

## Lesson

### Introduction

Suppose we have the factored polynomial

$$


p(x)= (x-5)^2(x+8).


$$

By the factor theorem, we know the roots of the polynomial are $x=5$ and $x=-8.$

The **multiplicity** of a root of a polynomial equals the number of times the corresponding factor appears in the fully factored form of the polynomial.

For the polynomial $p(x)$ above, we have the following:

- The factor $(x-5)$ has an exponent of $2$ in the factored form of $p(x).$ Therefore, it appears *twice*, and the multiplicity of the root $x=5$ is $2.$

- In contrast, the factor $(x+8)$ has an exponent of $1$ in the factored form of $p(x).$ Therefore, it appears only once, and the multiplicity of the root $x=-8$ is $1.$

If the multiplicity of a root is $1,$ like $x=-8$ in the example above, then the root is called a **simple root**. Otherwise, the root is called a **multiple root**. In the example above, $x=5$ is a multiple root.

Additionally, roots that have multiplicity $2$ are often referred to as **double roots.**

### Example: Identifying the Multiplicity of a Root of a Polynomial

#### Question

Which root of the polynomial $P(x)=(x+1)^2(x^2 -x -2)(x-2)(x+3)$ has multiplicity $3?$

#### Explanation

The multiplicity of a root of a polynomial equals the exponent of its corresponding factor in the factorization of the polynomial.

First, let's completely factor $P(x)\mathbin{:}$

$$


\begin{aligned}𝑃(𝑥) & =(𝑥+1)^{2}(𝑥^{2}−𝑥−2)(𝑥−2)(𝑥+3) \\ & =(𝑥+1)^{2}((𝑥+1)(𝑥−2))(𝑥−2)(𝑥+3) \\ & =(𝑥+1)^{2}(𝑥+1)(𝑥−2)(𝑥−2)(𝑥+3) \\ & =(𝑥+1)^{3}(𝑥−2)^{2}(𝑥+3)\end{aligned}


$$

From the factored form, we can tell that the roots of $P(x)$ are $x=-1,$ $x=2,$ and $x=-3.$

- The factor $(x+1)$ has an exponent of $3$ in the factored form of $P(x).$ So the root $x=-1$ has multiplicity $3.$

- The factor $(x-2)$ has an exponent of $2$ in the factored form of $P(x).$ So the root $x=2$ has multiplicity $2.$

- The factor $(x+3)$ has an exponent of $1$ in the factored form of $P(x).$ So the root $x=-3$ has multiplicity $1$ (and it is a simple root).

Therefore, the root with multiplicity $3$ is $x=-1.$

### Example: Determining the Multiplicity of a Root of a Cubic Polynomial Using Synthetic Division

#### Question

What is the multiplicity of the root $x=-3$ in the polynomial $p(x) = 2x^3 + 13x^2 + 24x + 9?$

#### Explanation

Since $x=-3$ is a root of $p(x),$ the factor theorem tells us that $(x+3)$ is a factor of $p(x).$

Because $(x+3)$ is a factor of $p(x),$ we know that $(x+3)$ divides $p(x)$ with no remainder. So, to begin factoring $p(x),$ we can divide it by $(x+3)$ using synthetic division:

Therefore,

$$


\dfrac{p(x)}{x+3} = 2x^2 + 7x + 3


$$

which means that

$$


p(x) = (x+3) (2x^2 + 7x + 3).


$$

We can factor the quadratic factor even further, and get

$$


\begin{aligned}𝑝(𝑥) & =(𝑥+3)(2𝑥+1)(𝑥+3) \\ & =(𝑥+3)^{2}(2𝑥+1).\end{aligned}


$$

The factor $(x+3)$ has an exponent of $2$ in the factored form of $p(x).$ So the root $x=-3$ has multiplicity $2.$

### Example: Determining the Multiplicity of a Root of a Cubic Polynomial Using the GCF

#### Question

Which root(s) of the polynomial $p(x) = x^3-5x^2$ have multiplicity $1?$

#### Explanation

First, we need to factor the polynomial.

For this polynomial, we can factor by noting that the greatest common factor of $x^3$ and $-5x^2$ is $x^2{:}$

$$


\begin{aligned}𝑝(𝑥) & =𝑥^{3}−5𝑥^{2} \\ & =𝑥^{2}(𝑥−5)\end{aligned}


$$

To find the roots and their multiplicities, we look at the factors:

- The factor $x^2$ has an exponent of $2$ in the factored form of $p(x).$ So the root $x=0$ has multiplicity $2.$

- The factor $(x-5)$ has an exponent of $1$ in the factored form of $p(x).$ So the root $x=5$ has multiplicity $1.$

In conclusion, only the root $x=5$ has multiplicity $1.$

### Example: Determining the Multiplicity of a Root of a Cubic Polynomial Using Grouping

#### Question

Which root(s) of the polynomial $p(x) = x^3 + 3x^2 - 4x - 12$ have multiplicity $1?$

#### Explanation

First, we need to factor the polynomial. For this polynomial, we can factor by grouping:

$$


\begin{aligned}𝑝(𝑥) & =𝑥^{3}+3𝑥^{2}−4𝑥−12 \\ & =𝑥^{2}(𝑥+3)−4(𝑥+3) \\ & =(𝑥^{2}−4)(𝑥+3) \\ & =(𝑥−2)(𝑥+2)(𝑥+3)\end{aligned}


$$

To find the roots and their multiplicities, we look at the factors:

- The factor $(x-2)$ has an exponent of $1$ in the factored form of $p(x).$ So the root $x=2$ has multiplicity $1.$

- The factor $(x+2)$ has an exponent of $1$ in the factored form of $p(x).$ So the root $x=-2$ has multiplicity $1.$

- The factor $(x+3)$ has an exponent of $1$ in the factored form of $p(x).$ So the root $x=-3$ has multiplicity $1.$

In conclusion, the roots $x=2,-2,-3$ all have multiplicity $1.$
