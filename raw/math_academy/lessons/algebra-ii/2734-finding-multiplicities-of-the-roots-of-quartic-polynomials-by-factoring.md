# Finding Multiplicities of the Roots of Quartic Polynomials by Factoring

Source: https://www.mathacademy.com/topics/2734?courseId=51
Topic ID: 2734

## Prerequisites

- [Multiplicities of the Roots of Polynomials](./88-multiplicities-of-the-roots-of-polynomials.md)
- [Factoring Quartic Polynomials Using the Factor Theorem](./104-factoring-quartic-polynomials-using-the-factor-theorem.md)
- [Factoring Biquadratic Expressions](./2336-factoring-biquadratic-expressions.md)

## Lesson

### Introduction

To find the multiplicity of a root of a quartic polynomial, we can divide the polynomial by the corresponding factor as many times as possible.

For example, suppose we want to find the multiplicity of the root $x=-2$ of the polynomial

$$


p(x) = x^4+2x^3-3x^2-8x-4.


$$

Because $x=-2$ is a root of $p(x),$ we know that $(x+2)$ is a factor of $p(x),$ which means $(x+2)$ divides $p(x)$ with no remainder. So, to find the multiplicity of $x=-2,$ we will divide $p(x)$ by $(x+2)$ as many times as possible. Proceeding with synthetic division, we get

$$


\begin{aligned}−2 & 1 & 2 & −3 & −8 & −4 \\ & 0 & −2 & 0 & 6 & 4 \\ & 1 & 0 & −3 & −2 & 0\end{aligned}


$$

Therefore,

$$


\dfrac{p(x)}{x+2} = x^3-3x-2,


$$

which means that

$$


p(x) = (x+2) (x^3-3x-2).


$$

Now, let's see if $x=-2$ is also a root of the cubic factor $(x^3-3x-2).$ If it is, then $(x+2)$ is a factor of the cubic, and we'll keep on dividing by $(x+2).$ If it isn't, then we're done.

Substituting $x=-2$ into the cubic factor $(x^3-3x-2),$ we get

$$


(-2)^3-3(-2)-2 = -8+6-2 = -4 \neq 0. \quad \color{red}\times


$$

So, we are done. The factor of $(x+2)$ has an exponent of $1$ in the factored form of $p(x).$ Therefore, the root $x=-2$ has multiplicity $1.$

### Example: Determining the Multiplicity of a Root of a Quartic Polynomial Using the Factor Theorem

#### Question

What is the multiplicity of the root $x=3$ of $p(x) = x^4 - 3 x^3 - 7 x^2 + 15 x + 18?$

#### Explanation

Since $x=3$ is a root of $p(x),$ the factor theorem tells us that $(x-3)$ is a factor of $p(x).$

Because $(x-3)$ is a factor of $p(x),$ we know that $(x-3)$ divides $p(x).$ So, to begin factoring $p(x),$ we can divide it by $(x-3)$ using synthetic division:

Therefore,

$$


\dfrac{p(x)}{x-3} = x^3 - 7x - 6


$$

which means that

$$


p(x) = (x-3) (x^3 - 7x - 6).


$$

Let's check if $x=3$ is also a root of $(x^3-7x-6).$ Substituting, we get

$$


3^3 - 7(3) - 6 = 27 - 21 - 6 = 0. \quad \color{green}\checkmark


$$

So $x=3$ is indeed a root of $(x^3-7x-6),$ we have that $(x-3)$ is a factor of $(x^3-7x-6),$ and we can continue factoring using synthetic division:

Therefore,

$$


\dfrac{x^3-7x-6}{x-3} = x^2 + 3x + 2 ,


$$

which means that

$$


x^3-7x-6 = (x-3)(x^2 + 3x + 2).


$$

So we have

$$


\begin{aligned}𝑝(𝑥) & =(𝑥−3)(𝑥^{3}−7𝑥−6) \\ & =(𝑥−3)(𝑥−3)(𝑥^{2}+3𝑥+2) \\ & =(𝑥−3)^{2}(𝑥+1)(𝑥+2).\end{aligned}


$$

The factor $(x-3)$ has an exponent of $2$ in the factored form of $p(x).$ So the root $x=3$ has multiplicity $2.$

### Factoring Using Other Techniques

To find the multiplicity of a root, we have been using synthetic division. However, there are sometimes other ways to factor polynomials besides synthetic division. For example, remember that when a polynomial is a *biquadratic*, we can factor it as though it were a quadratic.

For example, consider the polynomial $p(x) = x^4 - 3x^2 - 4.$ To factor this polynomial, we can let $u=x^2,$ and factor the polynomial in terms of $u\mathbin{:}$

$$


\begin{aligned}𝑝(𝑥) & =𝑥^{4}−3𝑥^{2}−4 \\ & =(𝑥^{2})^{2}−3(𝑥^{2})−4 \\ & =𝑢^{2}−3𝑢−4 \\ & =(𝑢−4)(𝑢+1)\end{aligned}


$$

Now, we substitute $x^2$ back in for $u$ and continue factoring:

$$


\begin{aligned}𝑝(𝑥) & =(𝑥^{2}−4)(𝑥^{2}+1) \\ & =(𝑥+2)(𝑥−2)(𝑥^{2}+1)\end{aligned}


$$

### Example: Determining the Multiplicity of a Root of a Biquadratic Polynomial

#### Question

Which root(s) of the polynomial $p(x) = x^4 - 6x^2 - 27$ have multiplicity $1?$

#### Explanation

First, we need to factor the polynomial. This polynomial is a biquadratic since all of the powers are even. So, we can let $u=x^2,$ and factor the polynomial in terms of $u\mathbin{:}$

$$


\begin{aligned}𝑝(𝑥) & =𝑥^{4}−6𝑥^{2}−27 \\ & =(𝑥^{2})^{2}−6(𝑥^{2})−27 \\ & =𝑢^{2}−6𝑢−27 \\ & =(𝑢−9)(𝑢+3)\end{aligned}


$$

Now, we substitute $x^2$ back in for $u$ and continue factoring:

$$


\begin{aligned}𝑝(𝑥) & =(𝑥^{2}−9)(𝑥^{2}+3) \\ & =(𝑥+3)(𝑥−3)(𝑥^{2}+3)\end{aligned}


$$

Note that the factor $(x^2+3)$ cannot be factored any further, and it does not have any real roots.

The real roots of $p(x)$ come from the factors $(x+3)$ and $(x-3).$ We find their multiplicities as follows:

- The factor $(x+3)$ has an exponent of $1$ in the factored form of $p(x).$ So the root $x=-3$ has multiplicity $1.$

- The factor $(x-3)$ has an exponent of $1$ in the factored form of $p(x).$ So the root $x=3$ has multiplicity $1.$

In conclusion, the roots $x=3,-3$ both have multiplicity $1.$

### Example: Determining the Multiplicity of a Root of a Quartic Polynomial Using the GCF and Grouping

#### Question

Which real root(s) of the polynomial $f(x) = x^4+2x^3+x^2+2x$ have multiplicity $1?$

#### Explanation

First, we need to factor the polynomial. Notice that all of the terms have a common factor of $x.$ So, we can immediately factor out a $x$ from all the terms:

$$


\begin{aligned}𝑓(𝑥) & =𝑥^{4}+2𝑥^{3}+𝑥^{2}+2𝑥 \\ & =𝑥(𝑥^{3}+2𝑥^{2}+𝑥+2)\end{aligned}


$$

Now, we factor the cubic by grouping, and simplify until the polynomial is fully factored:

$$


\begin{aligned}𝑓(𝑥) & =𝑥(𝑥^{3}+2𝑥^{2}+𝑥+2) \\ & =𝑥[𝑥^{2}(𝑥+2)+(𝑥+2)] \\ & =𝑥(𝑥^{2}+1)(𝑥+2)\end{aligned}


$$

Note that the factor $(x^2+1)$ cannot be factored any further, and it does not have any real roots.

The real roots of $f(x)$ come from the factors $x$ and $(x+2).$ We find their multiplicities as follows:

- The factor $x$ has an exponent of $1$ in the factored form of $f(x).$ So the root $x=0$ has multiplicity $1.$

- The factor $(x+2)$ has an exponent of $1$ in the factored form of $f(x).$ So the root $x=-2$ has multiplicity $1.$

In conclusion, the roots $x = 0, \, -2$ both have multiplicity $1.$
