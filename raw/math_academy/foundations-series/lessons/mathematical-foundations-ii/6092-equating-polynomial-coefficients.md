# Equating Polynomial Coefficients

Source: https://www.mathacademy.com/topics/6092?courseId=111
Topic ID: 6092

## Prerequisites

- [Factoring Polynomials Using GCFs](../../../high-school/traditional/lessons/algebra-i/353-factoring-polynomials-using-gcfs.md)
- [Multiplying Binomials](../../../high-school/traditional/lessons/algebra-i/371-multiplying-binomials.md)
- [Linear Equations With Infinitely Many Solutions](../../../middle-school/lessons/grade-8/1414-linear-equations-with-infinitely-many-solutions.md)
- [Linear Equations With No Solutions](../../../middle-school/lessons/grade-8/5572-linear-equations-with-no-solutions.md)

## Lesson

### Introduction

Let's recall what we learned in a previous lesson about linear equations with infinitely many solutions.

Suppose we have the linear equation

$$


2x + 5 = 2x + 5.


$$

Notice that

- the coefficient of $x$ on both sides of the equation is $2,$ and

- the constant term on both sides of the equation is $5.$

Since the coefficients of $x$ on both sides of the equation are equal, and the constants are also equal, it follows that this equation has *infinitely many solutions.* In fact, this equation is true for *any* value of $x.$

More generally, suppose we have the equation

$$


ax + b = cx + d.


$$

If $a = c$ and $b = d$ are *both* true, then the equation is true for any value of $x.$

The goal of this lesson is to extend this idea to quadratic polynomials.

### Equating Coefficients of Quadratic Polynomials

Suppose we have two quadratic polynomials $P$ and $Q,$ given by

$$


P(x) = ax^2 + bx + c \quad \text{and} \quad Q(x) = dx^2 + ex + f.


$$

If these polynomials are equal for *all* values of $x,$ we say that they're **identical.** This means their matching terms must be the same. In other words, we must have

$$


a = d, \qquad b = e, \qquad c = f.


$$

For example, suppose we are given the equation

$$


ax^2 + bx + c = x^2 + 5x + 4


$$

where $a, b,$ and $c$ are fixed numbers, and we're told that this equation is true for all values of $x.$

Since this polynomial equation is true for all values of $x$, we can match the coefficients.

- The coefficient of $x^2$ on the left-hand side is $a$, and on the right-hand side it is $1.$ So, we have

- The coefficient of $x$ on the left-hand side is $b$, and on the right-hand side it is $5.$ So, we have

- The constant on the left-hand side is $c$, and on the right-hand side it is $4.$ So, we have

This process is known as **equating coefficients.** It’s a useful tool whenever we know two polynomials are equal for all values of the variable.

This idea works for higher-degree polynomials too: when two polynomials are equal for all $x$, we can compare the coefficients of each power of $x$ and set them equal to each other.

### Example: Matching a Single Coefficient

#### Question

The following equation is true for all values of $x.$

$$


mx^2 + 5x + 4 = 2x^2 + 5x + 4


$$

What is the value of the constant $m?$

#### Explanation

Since the equation is true for all values of $x,$ the expressions on both sides must be exactly the same. That means the coefficients of the matching powers of $x$ must be equal.

We compare the quadratic terms on both sides. On the left-hand side, the coefficient of $x^2$ is $m.$ On the right-hand side, the coefficient of $x^2$ is $2.$

So, we set

$$


m = 2.


$$

### Example: Solving for Two Coefficients

#### Question

The equation

$$


ax^2 + bx + 12 = 7x^2 + 2x + 12


$$

is true for all values of $x,$ where $a$ and $b$ are constants. What is the value of $a + b?$

#### Explanation

Since the equation is true for all values of $x,$ the expressions on both sides must be exactly the same. That means the coefficients of the matching powers of $x$ must be equal.

Let's compare the coefficients:

- The coefficient of $x^2$ on the left-hand side is $a,$ and on the right-hand side it is $7.$ So, we have

- The coefficient of $x$ on the left-hand side is $b,$ and on the right-hand side it is $2.$ So, we have

Now, we compute the sum:

$$


\begin{aligned}𝑎+𝑏 & =7+2 \\ & =9\end{aligned}


$$

### Example: Comparing Factored Forms

#### Question

The equation

$$


x^2 + 9x + 18 = (x + 3)(x + k)


$$

is true for all values of $x,$ where $k$ is a constant. What is the value of $k?$

#### Explanation

Since the equation is true for all values of $x,$ the expressions on both sides must be exactly the same. That means the factored form on the right-hand side must expand to match the left-hand side.

Let's expand the right-hand side:

$$


\begin{aligned}(𝑥+3)(𝑥+𝑘) & =𝑥^{2}+𝑘𝑥+3𝑥+3𝑘 \\ & =𝑥^{2}+(𝑘+3)𝑥+3𝑘.\end{aligned}


$$

Now, we compare the expanded form to the left-hand side:

$$


x^2 + 9x + 18 = x^2 + (k + 3)x + 3k


$$

Equating the constant terms, we get

$$


\begin{aligned}18 & =3𝑘 \\ 6 & =𝑘 \\ 𝑘 & =6.\end{aligned}


$$

Let's verify that value $k = 6$ produces the correct linear coefficient:

$$


\begin{aligned}𝑘+3 & =6+3 \\ & =9\,✓\end{aligned}


$$

which matches the coefficient of $x$ on the left-hand side. So, our solution is valid.
