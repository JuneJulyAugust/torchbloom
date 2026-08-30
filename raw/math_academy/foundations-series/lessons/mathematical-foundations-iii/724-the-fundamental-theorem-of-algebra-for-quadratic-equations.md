# The Fundamental Theorem of Algebra for Quadratic Equations

Source: https://www.mathacademy.com/topics/724?courseId=136
Topic ID: 724

## Prerequisites

- [Multiplicities of the Roots of Polynomials](../../../high-school/traditional/lessons/algebra-ii/88-multiplicities-of-the-roots-of-polynomials.md)
- [Extending Polynomial Identities to the Complex Numbers](./696-extending-polynomial-identities-to-the-complex-numbers.md)
- [The Complex Conjugate and the Roots of a Quadratic Equation](./1647-the-complex-conjugate-and-the-roots-of-a-quadratic-equation.md)

## Lesson

### Introduction

The **fundamental theorem of algebra** tells us that any quadratic polynomial with real coefficients has precisely two roots.

Furthermore, any such polynomial can be factored as

$$


ax^2+bx+c = a(x-x_1)(x-x_2),


$$

where $x_1$ and $x_2$ are the roots of the polynomial.

When counting the roots of a quadratic polynomial, we need to bear in mind the following important points:

- If a root has multiplicity $2,$ we count that root twice.

- We also include any imaginary or complex roots.

Also, remember that in the case of imaginary or complex roots, the roots always come in complex conjugate pairs.

Let's consider some examples.

- Let $f(x) = 2x^2 +x -1.$ This polynomial has two distinct real roots, $x = \dfrac12$ and $x = -1.$ Therefore, it can be factored as follows:

$$


\begin{aligned}𝑓(𝑥) & =2(𝑥−\frac{1}{2})(𝑥−(−1)) \\ & =2(𝑥−\frac{1}{2})(𝑥+1)\end{aligned}


$$

- Let $g(x) = 9x^2-6x+1.$ This polynomial has a single repeated root, $x = \dfrac13.$ Therefore, it can be factored as follows:

$$


\begin{aligned}𝑔(𝑥) & =9(𝑥−\frac{1}{3})(𝑥−\frac{1}{3}) \\ & =9(𝑥−\frac{1}{3})^{2}\end{aligned}


$$

- Let $h(x) = x^2+4.$ This polynomial has two purely imaginary roots, $x = \pm 2\textrm i.$ Therefore, it can be factored as follows:

$$


\begin{aligned}ℎ(𝑥) & =(𝑥−2i)(𝑥−(−2i)) \\ & =(𝑥−2i)(𝑥+2i)\end{aligned}


$$

- Let $k(x) = x^2-4x+5.$ This polynomial has two complex roots, $x = 2\pm \textrm i.$ Therefore, it can be factored as follows:

$$


\begin{aligned}𝑘(𝑥) & =(𝑥−(2+i))(𝑥−(2−i)) \\ & =(𝑥−2−i)(𝑥−2+i)\end{aligned}


$$

### Example: Finding a Quadratic Polynomial Given Two Real Roots and a Leading Coefficient

#### Question

The quadratic polynomial $P(x)$ has roots $x_1=2, x_2=5,$ and the coefficient of the quadratic term is $3.$ Find $P(x).$

#### Explanation

Since our quadratic polynomial has roots ${\color{black}x_1=2}$ and ${\color{black}x_2=5},$ and the coefficient of the quadratic term is ${\color{black}a=3},$ we can write the polynomial as follows:

$$


\begin{aligned}𝑎(𝑥−𝑥_{1})(𝑥−𝑥_{2}) & =3(𝑥−2)(𝑥−5) \\ & =3(𝑥−2)(𝑥−5)\end{aligned}


$$

Expanding the parentheses, we obtain

$$


\begin{aligned}3(𝑥−2)(𝑥−5) & =3(𝑥^{2}−7𝑥+10) \\ & =3𝑥^{2}−21𝑥+30.\end{aligned}


$$

Therefore, $P(x) = 3x^2-21x+30.$

### Example: Finding a Quadratic Polynomial Given a Double Root and a Leading Coefficient

#### Question

The quadratic polynomial $P(x)$ has the double root $x_1=x_2=5,$ and the coefficient of the quadratic term is $a=1.$ Find $P(x).$

#### Explanation

Since our quadratic polynomial has the double root ${\color{black}x_1=x_2=5},$ and the coefficient of the quadratic term is ${\color{black}a=1},$ we can write the polynomial as follows:

$$


\begin{aligned}𝑎(𝑥−𝑥_{1})^{2} & =1⋅(𝑥−5)^{2} \\ & =(𝑥−5)^{2}\end{aligned}


$$

Expanding the parentheses, we obtain

$$


\begin{aligned}(𝑥−5)^{2} & =𝑥^{2}−10𝑥+25.\end{aligned}


$$

Therefore, $P(x) = x^2 - 10x+25.$

### Example: Finding a Quadratic Polynomial Given Two Imaginary or Complex Roots

#### Question

The quadratic polynomial $f(z)$ with real coefficients has roots $z_1=3+\textrm{i}$ and $z_2=3-\textrm{i},$ and the coefficient of the quadratic term is $2.$ Find $f(z).$

#### Explanation

Since our quadratic polynomial has roots ${\color{black}z_1=3+\textrm{i}}$ and ${\color{black}z_2=3-\textrm{i}},$ and the coefficient of the quadratic term is ${\color{black}a=2},$ we can write the polynomial as follows:

$$


\begin{aligned}𝑎(𝑧−𝑧_{1})(𝑧−𝑧_{2}) & =2(𝑧−(3+i))(𝑧−(3−i))\end{aligned}


$$

Expanding the parentheses, we obtain

$$


\begin{aligned}2(𝑧−(3+i))(𝑧−(3−i)) & =2(𝑧^{2}−(3+i)𝑧−(3−i)𝑧+(3+i)(3−i)) \\ & =2(𝑧^{2}−(3+i+3−i)𝑧+(3^{2}−i^{2})) \\ & =2(𝑧^{2}−6𝑧+(9+1)) \\ & =2(𝑧^{2}−6𝑧+10) \\ & =2𝑧^{2}−12𝑧+20.\end{aligned}


$$

Therefore, $f(z) = 2z^2-12z+20.$

### Example: Factoring a Quadratic Polynomial With Complex Roots

#### Question

Factor $u^2-2u+10.$

#### Explanation

First, we let $f(u) = u^2-2u+10.$

Next, we solve $f(u) = 0$ by completing the square, as follows:

$$


\begin{aligned}𝑓(𝑢) & =0 \\ 𝑢^{2}−2𝑢+10 & =0 \\ (𝑢^{2}−2𝑢+1^{2})−1^{2}+10 & =0 \\ (𝑢−1)^{2}−1+10 & =0 \\ (𝑢−1)^{2}+9 & =0 \\ (𝑢−1)^{2} & =−9 \\ (𝑢−1)^{2} & =9i^{2} \\ (𝑢−1)^{2} & =(3i)^{2} \\ 𝑢−1 & =±3i \\ 𝑢 & =1±3i\end{aligned}


$$

Now, since our quadratic equation has roots $u_1=1+ 3\textrm{i}$ and $u_2=1- 3\textrm{i},$ and the coefficient of the quadratic term is $a=1,$ the expression $u^2-2u+10$ can be written as

$$


\begin{aligned}𝑢^{2}−2𝑢+10 & =𝑎(𝑢−𝑢_{1})(𝑢−𝑢_{2}) \\ & =(𝑢−(1+3i))(𝑢−(1−3i)).\end{aligned}


$$

### General Statement of the Fundamental Theorem of Algebra

In this lesson, we have considered the fundamental theorem of algebra applied to quadratic polynomials. As it turns out, we can apply the fundamental theorem of algebra to *any* polynomial with real coefficients.

Consider a general polynomial $p(x)$ of degree $n$ with real coefficients, given by

$$


p(x) = a_nx^n+\ldots+a_1x+a_0, \qquad a_n\neq 0.


$$

The fundamental theorem of algebra tells us that $p(x)$ will always have precisely $n$ roots.

Furthermore, $p(x)$ can be factored as follows:

$$


p(x) = a_n(x-x_1)(x-x_2)(x-x_3)\cdots (x-x_{n})


$$

where $x_1, x_2, x_3,\ldots, x_n$ are the roots of the polynomial.

As with the quadratic case, we need to bear the following important points in mind when counting the roots of a polynomial:

- If a root has multiplicity $m,$ we count that root $m$ times.

- We also include any imaginary or complex roots.

As with the quadratic case, imaginary and complex roots always come in complex conjugate pairs.

In future lessons, we will learn more about the fundamental theorem of algebra applied to higher-degree polynomials.
