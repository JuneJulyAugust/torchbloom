# Reasoning About Coefficients in Quadratic Equations Using the Factor Theorem

Source: https://www.mathacademy.com/topics/6267?courseId=120
Topic ID: 6267

## Prerequisites

- [Solving Quadratic Equations with No Constant Term](../../../high-school/traditional/lessons/algebra-i/393-solving-quadratic-equations-with-no-constant-term.md)
- [The Factor Theorem](../../../high-school/traditional/lessons/algebra-ii/846-the-factor-theorem.md)

## Lesson

### Introduction

In this lesson, we'll learn how to use the factor theorem to reason about unknown coefficients in polynomials:

First, recall that the factor theorem states the following:

- If $x=r$ is a root of the polynomial $p(x),$ then $(x-r)$ is a factor of a polynomial.

- If $x=\dfrac{r}{s}$ is a root of the polynomial $p(x),$ then $(sx-r)$ is a factor of a polynomial.

The **converse of the factor theorem** is similar, but the order of the statements is swapped. It states the following:

- If $(x-r)$ is a factor of a polynomial $p(x),$ then $x=r$ is a root of the polynomial.

- If $(sx-r)$ is a factor of a polynomial $p(x),$ then $x=\dfrac{r}{s}$ is a root of the polynomial.

The converse of the factor theorem means that if we know a factor of a quadratic polynomial, then we can use the factor theorem to solve for an unknown coefficient in the polynomial.

Let's see some examples.

### A Concrete Example

Let's consider the quadratic polynomial

$$


p(x) = x^{2} - 13x - 2c,


$$

where $c$ is an unknown constant. Suppose we know that the expression $(x-2c)$ is a factor of $p(x).$ We can use this information to determine the possible values of $c.$

Since $(x-2c)$ is a factor of the polynomial, this means that $x = 2c$ is a root, and we must have

$$


p(2c) = 0.


$$

Substituting $x=2c$ into the expression for $p(x),$ we get the following:

$$


\begin{aligned}𝑝(2𝑐) & =(2𝑐)^{2}−13(2𝑐)−2𝑐 \\ & =4𝑐^{2}−26𝑐−2𝑐 \\ & =4𝑐^{2}−28𝑐.\end{aligned}


$$

Since $p(2c) = 0,$ this gives the equation

$$


4c^{2} - 28c = 0


$$

and factoring the common factor of $4c,$ we have

$$


4c(c - 7) = 0.


$$

Now, by the zero product rule, we conclude that $4c(c - 7)=0$ if

$$


c=0 \qquad\text{or}\qquad c-7=0,


$$

which gives $c=0$ or $c=7.$

### Example: Applying the Factor Theorem to Quadratic Polynomials

#### Question

The expression $x + 2k$ is a factor of $2x^{2} + 15x + 6k.$ Which of the following could be the value of $k?$

1. $k=3$ or $k=5$

2. $k=0$ only

3. $k=0$ or $k=3$

4. $k=5$ only

#### Explanation

Recall that by the factor theorem, if $(x-r)$ is a factor of a polynomial $p(x),$ then $x=r$ is a root of the polynomial.

Now, since $x + 2k$ is a factor of the polynomial $p(x)=2x^{2} + 15x + 6k,$ we must have

$$


p(-2k) = 0.


$$

So, substituting $x=-2k$ into the expression for $p(x),$ we get the following:

$$


\begin{aligned}𝑝(−2𝑘) & =2(−2𝑘)^{2}+15(−2𝑘)+6𝑘 \\ & =8𝑘^{2}−30𝑘+6𝑘 \\ & =8𝑘^{2}−24𝑘 \\ & =8𝑘(𝑘−3)\end{aligned}


$$

Using the zero product rule, we conclude that $8k(k-3)=0$ if

$$


k=0 \qquad\text{or}\qquad k-3=0.


$$

Therefore, the correct answer is "III only"

### Example: Applying the Factor Theorem to Quadratic Polynomials With Leading Coefficients

#### Question

The expression $4x - g$ is a factor of $16x^{2} + 12x - 7g.$ Which of the following could be the value of $g?$

1. $g=0$ or $g=4$

2. $g=4$ only

3. $g=-1$ or $g=0$

4. $g=0$ only

#### Explanation

Recall that by the factor theorem, if $(sx-r)$ is a factor of a polynomial $p(x),$ then $x=\dfrac{r}{s}$ is a root of the polynomial.

Now, since $4x - g$ is a factor of the polynomial $p(x)=16x^{2} + 12x - 7g,$ we must have

$$


p\left(\dfrac{g}{4}\right) = 0.


$$

So, substituting $x=\dfrac{g}{4}$ into the expression for $p(x),$ we get the following:

$$


\begin{aligned}𝑝(\frac{𝑔}{4}) & =16(\frac{𝑔}{4})^{2}+12(\frac{𝑔}{4})−7𝑔 \\ & =𝑔^{2}+3𝑔−7𝑔 \\ & =𝑔^{2}−4𝑔 \\ & =𝑔(𝑔−4)\end{aligned}


$$

Using the zero product rule, we conclude that $g(g - 4)=0$ if

$$


g=0 \qquad\text{or}\qquad g-4=0,


$$

which gives $g=0$ or $g=4.$

Therefore, the correct answer is "I only"

### Example: Identifying Polynomials Corresponding to a Given Factor

#### Question

Which of the following expressions has a factor of $2x - 5m$, where $m$ is a **** constant?

1. $4x^{2} + 2x + 18m$

2. $4x^{2} + 2x + 10m$

3. $4x^{2} + 2x + 20m$

#### Explanation

Recall that by the factor theorem, if $(sx-r)$ is a factor of a polynomial $p(x),$ then $x=\dfrac{r}{s}$ is a root of the polynomial. Thus, since $2x -5m$ is a factor of our polynomial $p(x),$ we must have

$$


p\left(\dfrac{5m}{2}\right) = 0.


$$

With that in mind, let's examine the given options in turn.

- Option I, $p(x) = 4x^{2}+2x+18m,$ is not valid. Here, we have This equals zero only at $m=0$ or $m=-\dfrac{23}{25},$ neither of which is a negative integer. ${\color{red}\times}$

** $p(x)=4x^{2}+2x+10m,$ is not valid. Here, we have

$$


\begin{aligned}𝑝(\frac{3𝑐}{2}) & =4(\frac{5𝑚}{2})^{2}+2\,(\frac{5𝑚}{2})+10𝑚 \\ & =25𝑚^{2}+5𝑚+10𝑚 \\ & =25𝑚^{2}+15𝑚 \\ & =5𝑚(5𝑚+3).\end{aligned}


$$

This equals zero only at $m=0$ or $m=-\dfrac{3}{5},$ neither of which is a negative integer. ${\color{red}\times}$

** $p(x)=4x^{2}+2x+20m,$ is valid. Indeed,

$$


\begin{aligned}𝑝(\frac{3𝑐}{2}) & =4(\frac{5𝑚}{2})^{2}+2\,(\frac{5𝑚}{2})+20𝑚 \\ & =25𝑚^{2}+5𝑚+20𝑚 \\ & =25𝑚^{2}+25𝑚 \\ & =25𝑚(𝑚+1).\end{aligned}


$$

This equals zero only at $m=0$ or $m=-1,$ and $m=-1$ is a negative integer. ${\color{darkgreen}\checkmark}$

Therefore, the correct answer is "III only".
