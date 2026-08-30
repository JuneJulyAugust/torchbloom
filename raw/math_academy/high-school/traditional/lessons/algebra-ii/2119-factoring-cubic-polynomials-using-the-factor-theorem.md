# Factoring Cubic Polynomials Using the Factor Theorem

Source: https://www.mathacademy.com/topics/2119?courseId=51
Topic ID: 2119

## Prerequisites

- [Solving Quadratic Equations Using a Difference of Squares](../algebra-i/394-solving-quadratic-equations-using-a-difference-of-squares.md)
- [The Discriminant of a Quadratic Equation](../algebra-i/425-the-discriminant-of-a-quadratic-equation.md)
- [The Factor Theorem](./846-the-factor-theorem.md)
- [Solving Quadratic Equations with Leading Coefficients by Factoring](../algebra-i/1422-solving-quadratic-equations-with-leading-coefficients-by-factoring.md)

## Lesson

### Introduction

If we're given a root $r$ of a polynomial $p(x),$ then the factor theorem tells us that $(x-r)$ is a factor of $p(x).$

For example, if we're given that $x=2$ is a root of the polynomial $p(x)=x^3-2x^2-x+2,$ then the factor theorem tells us that $(x-2)$ is a factor of $p(x).$

But what if we want to factor the polynomial completely? How can we find the other factors?

The trick is to use division. Because $(x-2)$ is a factor of $p(x),$ we know that $(x-2)$ divides $p(x).$ So, to begin factoring $p(x),$ we can divide it by $(x-2)$ using synthetic division:

Notice that the remainder turned out to be zero. Whenever we divide a polynomial by one of its factors, we *always* get a remainder of zero.

Therefore,

$$



\dfrac{x^3-2x^2-x+2}{x-2}=x^2-1,



$$

which means that

$$



x^3-2x^2-x+2 = (x-2) (x^2-1).



$$

We can factor the quadratic factor even further, and get

$$



x^3-2x^2-x+2 = (x-2) (x-1) (x+1).



$$

Now that our polynomial is fully factored, we can see that the three roots of the polynomial are

$$



x=2, \qquad x=1, \qquad x=-1.



$$

We can use this method and the factor theorem to factor polynomials and solve polynomial equations. Let's try a few more examples!

### Example: Factoring a Cubic Polynomial Given a Factor or a Root

#### Question

Given that $(x+2)$ is a factor of the polynomial $f(x)=x^3+2x^2-x-2,$ factor $f(x)$ completely.

#### Explanation

To find the remaining roots, we need to find the other factors of $f(x).$

Because $(x+2)$ is a factor of $f(x),$ we know that $(x+2)$ divides $f(x).$ So, to begin factoring $f(x),$ we can divide it by $(x+2)$ using synthetic division:

Therefore,

$$



\dfrac{x^3+2x^2-x-2}{x+2} = x^2-1,



$$

which means

$$



x^3+2x^2-x-2 = (x+2) (x^2-1).



$$

We can factor the quadratic factor even further, and get

$$



x^3+2x^2-x-2 = (x+2) (x+1)(x-1).



$$

### Example: Finding the Roots of a Cubic Polynomial Given a Factor or a Root

#### Question

Let $q(x)=2x^3+3x^2-18x+8.$ Given that $q(2) = 0$, factor $q(x)$ completely and identify all three of its roots.

#### Explanation

If $q(2) = 0$, then by the factor theorem $(x-2)$ is a factor of $q(x).$ To find the remaining zeros, we need to find the other factors of $q(x).$

So $(x-2)$ is a factor of $q(x),$ we know that $(x-2)$ divides $q(x)$ with no remainder. So, to begin factoring $q(x),$ we can divide it by $(x-2)$ using synthetic division:

Therefore,

$$



\dfrac{2x^3+3x^2-18x+8}{x-2} = 2x^2+7x-4,



$$

which means

$$



2x^3+3x^2-18x+8 = (x-2)(2x^2+7x-4).



$$

We can factor the quadratic factor even further, and get

$$



2x^3+3x^2-18x+8 = (x-2)(2x-1)(x+4).



$$

We can now equate each factor to $0$ and solve for $x$ to find the three roots:

$$



\begin{aligned}𝑥+4 & =0\, & 2𝑥−1 & =0\, & 𝑥−2 & =0 \\ 𝑥 & =−4\, & 𝑥 & =\frac{1}{2}\, & 𝑥 & =2\end{aligned}



$$

### Example: Factoring a Cubic Polynomial With Only One Real Factor

#### Question

Given that $(x+2)$ is a factor of the polynomial $f(x) = x^3 - 4x^2 - 2x + 20,$ factor $f(x)$ over the real numbers.

#### Explanation

To factor $f(x)$ we need to find its other factors.

Because $(x+2)$ is a factor of $f(x),$ we know that $(x+2)$ divides $f(x)$ with no remainder. So, to begin factoring $f(x),$ we can divide it by $(x+2)$ using synthetic division:

Therefore,

$$



\dfrac{x^3 - 4x^2 - 2x + 20}{x+2} = x^2 - 6x + 10,



$$

which means that

$$



x^3 - 4x^2 - 2x + 20 = (x+2)(x^2 - 6x + 10).



$$

To see whether the quadratic polynomial $x^2 - 6x + 10$ can be factored any further, we calculate its discriminant:

$$



b^2 - 4ac = (-6)^2 - 4(1)(10) = -4 < 0



$$

So, the quadratic polynomial $x^2 - 6x + 10$ cannot be factored over the real numbers since its discriminant is negative.

Therefore, the full factorization of $f(x)$ over the real numbers is given by

$$



x^3 - 4x^2 - 2x + 20 = (x+2)(x^2 - 6x + 10).



$$

### Example: Factoring a Cubic Polynomial That Factors Over the Reals But Not the Rationals

#### Question

Given that $(x+1)$ is a factor of the polynomial $f(x) = x^3 - x^2 - 4x - 2,$ factor $f(x)$ over the rational numbers.

#### Explanation

To factor $f(x)$ we need to find its other factors.

Because $(x+1)$ is a factor of $f(x),$ we know that $(x+1)$ divides $f(x)$ with no remainder. So, to begin factoring $f(x),$ we can divide it by $(x+1)$ using synthetic division:

Therefore,

$$



\dfrac{x^3 - x^2 - 4x - 2}{x+1} = x^2 - 2x - 2,



$$

which means that

$$



x^3 - x^2 - 4x - 2 = (x+1) (x^2 - 2x -2).



$$

To see whether the quadratic polynomial $x^2 - 2x - 2$ can be factored any further, we calculate its discriminant:

$$



\mathcal D = b^2 - 4ac = (-2)^2 - 4(1)(-2) = 12 > 0



$$

So, the quadratic polynomial $x^2 - 2x - 2$ cannot be factored over the rational numbers since its discriminant is not a perfect square.

Therefore, the full factorization of $f(x)$ (over the rational numbers) is given by

$$



x^3 - x^2 - 4x - 2 = (x+1)(x^2 - 2x - 2).



$$

****: Although the quadratic polynomial $(x^2 - 2x - 2)$ does not factor over the rational numbers, it ** have real roots, because $\mathcal D > 0.$ Therefore, if we were asked to find all of the real roots of $f(x),$ we would need to solve the equations

$$



x+1 = 0\qquad \text{and}\qquad x^2 - 2x - 2 = 0.



$$

The quadratic equation could be solved using the quadratic formula or by completing the square.
