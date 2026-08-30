# The Factor Theorem

Source: https://www.mathacademy.com/topics/846?courseId=134
Topic ID: 846

## Prerequisites

- [Determining the Roots of Polynomials](../algebra-ii/469-determining-the-roots-of-polynomials.md)
- [Dividing Polynomials Using Synthetic Division](../algebra-ii/728-dividing-polynomials-using-synthetic-division.md)
- [Solving Systems of Linear Equations Using Elimination: Two Transformations](../algebra-i/4236-solving-systems-of-linear-equations-using-elimination-two-transformations.md)

## Lesson

### Introduction

If we know a *root* of a polynomial, we can immediately determine a *factor* of the polynomial using the **factor theorem**.

The factor theorem states that if $p(x)$ is a polynomial and $x={\color{blue}{r}}$ is a *root* of $p(x),$ meaning that

$$


p({\color{blue}{r}})=0


$$

then $(x-{\color{blue}{r}})$ is a *factor* of $p(x).$

The converse of the factor theorem is also true. In other words, if $(x-{\color{blue}{r}})$ is a factor of $p(x),$ then $x={\color{blue}{r}}$ is a root of the polynomial.

For example, consider the polynomial $p(x),$ defined as

$$


p(x)=x^3-2x^2-x+2.


$$

Note that $x = {\color{blue}2}$ is a root of this polynomial:

$$


\begin{aligned}𝑝(2) & =2^{3}−2(2)^{2}−2+2 \\ & =8−8−2+2 \\ & =0\end{aligned}


$$

Therefore, according to the factor theorem, $(x-{\color{blue}2})$ is a *factor* of the polynomial. Indeed, it can be shown that this polynomial can be factored as follows:

$$


\begin{aligned}𝑥^{3}−2𝑥^{2}−𝑥+2 & =(𝑥−2)(𝑥^{2}−1)\end{aligned}


$$

We'll learn more about factoring polynomials using the factor theorem in future lessons. But for now, we can check that this is correct by multiplying the parentheses.

### Connection With Polynomial Division

So, we know that the polynomial $p(x) = x^3-2x^2-x+2$ can be factored as follows:

$$


\begin{aligned}𝑥^{3}−2𝑥^{2}−𝑥+2 & =(𝑥−2)(𝑥^{2}−1)\end{aligned}


$$

By dividing both sides by $(x-2),$ we can rewrite this equation as

$$


\dfrac{x^3-2x^2-x+2}{x-2} = x^2-1.


$$

Since the result of dividing the polynomial $p(x)$ by the factor $({x-{\color{black}2}})$ gives *another* polynomial, namely $x^2-1,$ we say that $({x-{\color{black}2}})$ divides $p(x)$ *with no remainder*.

We can confirm that we get a remainder of zero when $p(x)$ is divided by $({x-{\color{blue}2}})$ using synthetic division:

### Example: Applying the Factor Theorem

#### Question

Determine if $x+3$ is a factor of $p(x)=x^3+3x^2-3x-9.$

#### Explanation

According to the factor theorem, $(x-r)$ is a factor of $p(x)$ if the root $x = r$ is also a root of $p(x).$

Here, we are considering $(x+3).$ The root of this expression can be found by setting the expression equal to $0$ and solving:

$$


\begin{aligned}𝑥+3 & =0 \\ 𝑥 & =−3\end{aligned}


$$

According to the factor theorem, then, $(x+3)$ is a factor of $p(x)$ if the root $x = -3$ is a root of $p(x).$

So, we just need to check if $x=-3$ is a root of $p(x).$ In other words, we need to check if $p(-3)=0\mathbin{:}$

$$


\begin{aligned}𝑝(−3) & =(−3)^{3}+3(−3)^{2}−3(−3)−9 \\ & =−27+27+9−9 \\ & =0\end{aligned}


$$

Indeed, $p(-3)=0,$ so $x = -3$ is a root of the polynomial. Consequently, by the factor theorem, we conclude that $(x+3)$ is indeed a factor of $p(x).$

### The Factor Theorem for General Linear Factors

We can also apply the factor theorem to factors of the form $(ax-b).$

For example, suppose that $(2x-3)$ is a factor of a polynomial $p(x).$ Then, we can immediately obtain a root of $p(x)$ by setting the factor equal to $0$ and solving for $x,$ as follows:

$$


\begin{aligned}2𝑥−3 & =0 \\ 2𝑥 & =3 \\ 𝑥 & =\frac{3}{2}\end{aligned}


$$

Therefore, by the factor theorem, it follows that

$$


p\left(\dfrac32\right) = 0.


$$

We can summarize this more general form of the factor theorem as follows:

- If $({\color{red}a}x-{\color{blue}b})$ is a factor of a polynomial $p(x),$ then $x=\dfrac{{\color{blue}b}}{{\color{red}a}}$ is a root of $p(x).$

- Conversely, if $x=\dfrac{{\color{blue}b}}{{\color{red}a}}$ is a root of $p(x),$ then $({\color{red}a}x-{\color{blue}b})$ is a factor of $p(x).$

### Example: Applying the Factor Theorem to Factors With Leading Coefficients

#### Question

Determine if $(4-3x)$ is a factor of $p(x)=-6x^2+11x-4.$

#### Explanation

According to the factor theorem, $(ax-b)$ is a factor of $p(x)$ if the root $x = \dfrac{b}{a}$ is also a root of $p(x).$

Here, we are considering $(4-3x).$ The root of this expression can be found by setting the expression equal to $0$ and solving:

$$


\begin{aligned}4−3𝑥 & =0 \\ 4 & =3𝑥 \\ 𝑥 & =\frac{4}{3}\end{aligned}


$$

According to the factor theorem, then, $(4-3x)$ is a factor of $p(x)$ if the root $x=\dfrac{4}{3}$ is also a root of $p(x).$

So, we just need to check if $x=\dfrac{4}{3}$ is a root of $p(x).$ In other words, we need to check if $p\left(\dfrac{4}{3} \right) =0\mathbin{:}$

$$


\begin{aligned}𝑝(\frac{4}{3}) & =−6(\frac{4}{3})^{2}+11(\frac{4}{3})−4 \\ & =−6⋅\frac{16}{9}+\frac{44}{3}−4 \\ & =\frac{−32+44−12}{3} \\ & =0\end{aligned}


$$

Indeed, $p \left(\dfrac{4}{3} \right)=0,$ so $x=\dfrac{4}{3}$ is a root of the polynomial. Consequently, by the factor theorem, we conclude that $(4-3x)$ is indeed a factor of $p(x).$
