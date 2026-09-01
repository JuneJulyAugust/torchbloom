# The Rational Roots Theorem

Source: https://www.mathacademy.com/topics/757?courseId=51
Topic ID: 757

## Prerequisites

- [Factoring Cubic Polynomials Using the Factor Theorem](./2119-factoring-cubic-polynomials-using-the-factor-theorem.md)

## Lesson

### Introduction

The **rational roots theorem** (or **rational zeros theorem**) describes the rational roots of a polynomial with integer coefficients. The statement of the theorem is as follows:

*Suppose that the rational number $\dfrac{{\color{blue}{p}}}{\color{red}{q}},$ in lowest terms, is a root of a polynomial with integer coefficients. Then $\color{blue}p$ must be a factor of the polynomial's constant term, and $\color{red}q$ must be a factor of its leading coefficient.*

In other words, given a polynomial with integer coefficients, any rational roots of the polynomial must take the form

$$



\pm \dfrac{\text{factor of the constant term}}{\text{factor of the leading coefficient}}.



$$

For example, consider the polynomial

$$



f(x) = {\color{red}{8}}x^3+12x^2+6x+{\color{blue}{2}}.



$$

According to the rational roots theorem, any rational root of $f(x)$ must have a numerator that is a factor of $\color{blue}{2}$ (that is, either $\color{blue} \pm1$ or $\color{blue} \pm2$) and a denominator that's a factor of $\color{red} 8$ (${\color{red} \pm1},$ ${\color{red} \pm2},$ ${\color{red} \pm4},$ or $\color{red} \pm8$).

At first glance, it may seem like we have $16$ possible rational roots:

$$



\begin{aligned}±\frac{1}{1}, & ±\frac{1}{2}, & ±\frac{1}{4}, & ±\frac{1}{8}, \\ ±\frac{2}{1}, & ±\frac{2}{2}, & ±\frac{2}{4}, & ±\frac{2}{8}.\end{aligned}



$$

However, if we reduce the above fractions to lowest form, we see that there are some duplicates, which we cancel out:

$$



\begin{aligned}±1, & ±\frac{1}{2}, & ±\frac{1}{4}, & ±\frac{1}{8}, \\ ±2, & ±1, & ±\frac{1}{2}, & ±\frac{1}{4}.\end{aligned}



$$

Removing the duplicates, we have ten *possible* rational roots. We list them from least to greatest in absolute value:

$$



\begin{aligned}±\frac{1}{8}, & ±\frac{1}{4}, & ±\frac{1}{2}, & ±1, & ±2.\end{aligned}



$$

**Watch out!** The above roots are only *possible* rational roots. They are *not* guaranteed to be roots of our polynomial $f(x).$ The only guarantee is that if $f(x)$ has any roots that are rational numbers, they are included in the list of numbers above. Here, it turns out that the only actual root among the possibilities is $-1.$

### Example: Identifying Possible Roots of a Polynomial Using the Rational Roots Theorem

#### Question

According to the rational roots theorem, which of the following could be a root of the polynomial $f(x) = 9x^4-3x^2-7x-6?$

1. $-\dfrac{2}{3}$

2. $\dfrac{3}{2}$

3. $-9$

#### Explanation

Given a polynomial with integer coefficients, the rational roots theorem states that any rational roots of the polynomial must take the form

$$



\pm \dfrac{\text{factor of the constant term}}{\text{factor of the leading coefficient}}.



$$

For the given polynomial $f(x),$ the constant term is $-6,$ and the leading coefficient is $9.$ So, any rational roots of $f(x)$ must take the form

$$



\pm \dfrac{\text{factor of }{-6}}{\text{factor of }9}.



$$

Of the given answer choices, only $-\dfrac{2}{3}$ takes the above form since the numerator $(2)$ is a factor of $-6$ and the denominator $(3)$ is a factor of $9.$

### Example: Identifying Non-Roots of a Polynomial Using the Rational Roots Theorem

#### Question

According to the rational roots theorem, which of the following **** be a root of the polynomial $f(x) = 12x^4+5x^3-6x+15?$

1. $\dfrac{2}{3}$

2. $\dfrac{1}{3}$

3. $-\dfrac{3}{4}$

#### Explanation

Given a polynomial with integer coefficients, the rational roots theorem states that any rational roots of the polynomial must take the form

$$



\pm \dfrac{\text{factor of the constant term}}{\text{factor of the leading coefficient}}.



$$

For the given polynomial $f(x),$ the constant term is $15$ and the leading coefficient is $12.$ So, any rational roots of $f(x)$ must take the form

$$



\pm \dfrac{\text{factor of }{15}}{\text{factor of }12}.



$$

Of the given answer choices, only $\dfrac 23$ does not take the above form. The numerator $(2)$ is not a factor of $15.$

### Example: Counting the Number of Possible Rational Roots of a Polynomial

#### Question

For the polynomial $f(x)=6x^4-7x^3+11x-9,$ how many ** roots are given by the rational roots theorem?

#### Explanation

Given a polynomial with integer coefficients, the rational roots theorem states that any rational roots of the polynomial must take the form

$$



\pm \dfrac{\text{factor of the constant term}}{\text{factor of the leading coefficient}}.



$$

For the given polynomial:

- The constant term is $-9,$ and its factors are $\pm1,$ $\pm3,$ and $\pm9.$

- The leading coefficient is $6,$ and its factors are $\pm 1,$ $\pm 2,$ $\pm 3,$ and $\pm 6.$

First, we list out all the possibilities for the numerator and denominator:

$$



\begin{aligned}±\frac{1}{1}, & ±\frac{1}{2}, & ±\frac{1}{3}, & ±\frac{1}{6}, \\ ±\frac{3}{1}, & ±\frac{3}{2}, & ±\frac{3}{3}, & ±\frac{3}{6}, \\ ±\frac{9}{1}, & ±\frac{9}{2}, & ±\frac{9}{3}, & ±\frac{9}{6}.\end{aligned}



$$

Next, we reduce the fractions to lowest terms:

$$



\begin{aligned}±1, & ±\frac{1}{2}, & ±\frac{1}{3}, & ±\frac{1}{6}, \\ ±3, & ±\frac{3}{2}, & ±1, & ±\frac{1}{2}, \\ ±9, & ±\frac{9}{2}, & ±3, & ±\frac{3}{2}.\end{aligned}



$$

Notice that several potential roots are duplicates (shown above in red). Removing these duplicates, and listing those remaining in order from least to greatest in absolute value, we have

$$



\pm \frac{1}{6}, \; \pm \frac13, \; \pm \frac12, \; \pm 1, \; \pm \frac32, \; \pm 3, \; \pm \frac{9}{2}, \; \pm 9.



$$

This makes a total of $16$ potential roots. (Remember that each $\pm$ sign accounts for $2$ roots, and $2 \cdot 8 = 16.$)

### Example: Factoring a Cubic Polynomial Using the Rational Roots Theorem

#### Question

Given that the polynomial $f(x) =x^3 - x^2 - 4x + 4$ has a root in the interval $(0,4),$ find the sum of the distinct real roots of $f(x).$

#### Explanation

Given a polynomial with integer coefficients, the rational roots theorem states that any rational roots of the polynomial must take the form

$$



\pm \dfrac{\text{factor of the constant term}}{\text{factor of the leading coefficient}}.



$$

For the given polynomial $f(x),$ the constant term is $4$ and the leading coefficient is $1.$ So, any rational roots of $f(x)$ must take the form

$$



\pm \dfrac{\text{factor of }{4}}{\text{factor of }1}.



$$

Therefore, the possible rational roots are as follows:

$$



\pm1, \pm 2, \pm 4



$$

Of these roots, the only roots in the interval $(0,4),$ are $1$ and $2.$

Now, let's use synthetic division to test whether $\left(x-1\right)$ is a factor of $f(x).$ We get the following:

Since the remainder is $0,$ we conclude that $\left(x-1\right)$ is indeed a factor of $f(x).$ Moreover, we have

$$



f(x) = \left( x - 1\right) (x^2 - 4).



$$

Since the highest-degree factor is now a quadratic, we can continue factoring using the usual methods:

$$



\begin{aligned}𝑓(𝑥) & =(𝑥−1)(𝑥^{2}−4) \\ & =(𝑥−1)(𝑥+2)(𝑥−2)\end{aligned}



$$

Setting the factors equal to $0,$ we find the roots $x=-2, 1, 2.$ Summing these roots, we get

$$



-2+1+2 =1.



$$
