# Introduction to Partial Derivatives

Source: https://www.mathacademy.com/topics/1929?courseId=154
Topic ID: 1929

## Prerequisites

- [Differentiating Inverse Trigonometric Functions](../ap-calculus-ab/303-differentiating-inverse-trigonometric-functions.md)
- [Limits and Continuity of Multivariable Functions](./1931-limits-and-continuity-of-multivariable-functions.md)

## Lesson

### Introduction

Let $f(x,y)$ be a function of two variables. The **partial derivative of** $\boldsymbol{f}$ **with respect to** $\boldsymbol x$ is computed by taking the derivative of $f$ with respect to $x$ using the usual methods, *while treating $y$ as a constant.*

The partial derivative of $f$ with respect to $x$ has the following notation:

$$


\dfrac {\partial f} {\partial x}


$$

This partial derivative is defined as the following limit:

$$


\begin{aligned}\frac{𝜕𝑓}{𝜕𝑥} & =\underset{ℎ→0}{lim}(\frac{𝑓(𝑥+ℎ,𝑦)−𝑓(𝑥,𝑦)}{ℎ})\end{aligned}


$$

It's worth taking a moment to compare this to the derivative of a single-variable function $f(x){:}$

$$


\begin{aligned}\frac{d𝑓}{d𝑥} & =\underset{ℎ→0}{lim}(\frac{𝑓(𝑥+ℎ)−𝑓(𝑥)}{ℎ})\end{aligned}


$$

We can also define the partial derivative of $f$ with respect to $y,$ defined as follows:

$$


\dfrac {\partial f} {\partial y} = \lim_{h \to 0}\left(\dfrac {f (x ,y + h) - f(x, y)} {h}\right)


$$

In this case, we'd differentiate $f$ with respect to $y,$ treating $x$ as a constant.

We also have the following notations for partial derivatives:

$$


f_x = \dfrac {\partial f} {\partial x}, \qquad f_y = \dfrac {\partial f} {\partial y}


$$

### Example: Partial Derivatives as Limits of Difference Quotients

#### Question

Given that $f(x,y) = y^2\ln{x},$ express $\dfrac{\partial f}{\partial x}$ as the limit of a difference quotient.

#### Explanation

The partial derivative of $f$ with respect to $x$ is given by the limit

$$


\dfrac{\partial f}{\partial x} = \lim_{h \to 0} \left(\dfrac{f(x+h,y)-f(x,y)}{h}\right).


$$

Since $f(x) = y^2 \ln{x},$ we have that

$$


f(x+h,y) = y^2\ln(x+h).


$$

Therefore,

$$


\displaystyle \dfrac{\partial f}{\partial x} = \lim_{h \to 0}\left( \dfrac{y^2\ln(x+h) -y^2\ln{x} }{h}\right).


$$

### Computing Partial Derivatives

Consider the multivariable function $f(x,y),$ given by

$$


f (x, y)= x y^2 + e^{y}.


$$

To compute the partial derivative of $f$ with respect to ${\color{blue}x},$ we "fix" the variable $y$ (in other words, treat $y$ as if it were a constant). Then, we take the derivative with respect to ${\color{blue}x},$ as we usually would:

$$


\begin{aligned}\frac{𝜕𝑓}{𝜕𝑥} & =\frac{𝜕}{𝜕𝑥}(𝑥𝑦^{2}+𝑒^{𝑦}) \\ & =𝑦^{2}⋅\frac{𝜕}{𝜕𝑥}(𝑥)+\frac{𝜕}{𝜕𝑥}(𝑒^{𝑦}) \\ & =𝑦^{2}⋅(1)+0 \\ & =𝑦^{2}\end{aligned}


$$

Notice that the term $e^{y}$ vanished when taking the derivative with respect to $x.$ This is because $e^y$ is a function of $y$ only, and since we're treating $y$ as a constant, this entire term is treated as a constant and therefore differentiates to zero (just as a constant would).

Similarly, to compute the partial derivative of $f$ with respect to ${\color{blue}y},$ we fix the variable $x$ and then take the derivative with respect to ${\color{blue}y},$ as we usually would:

$$


\begin{aligned}\frac{𝜕𝑓}{𝜕𝑦} & =\frac{𝜕}{𝜕𝑦}(𝑥𝑦^{2}+𝑒^{𝑦}) \\ & =𝑥⋅\frac{𝜕}{𝜕𝑦}(𝑦^{2})+\frac{𝜕}{𝜕𝑦}(𝑒^{𝑦}) \\ & =𝑥⋅(2𝑦)+(𝑒^{𝑦}) \\ & =2𝑥𝑦+𝑒^{𝑦}\end{aligned}


$$

When we wish to evaluate a partial derivative at a point $(x_0, y_0),$ we can use any of the following notations:

$$


\dfrac {\partial f(x_0,y_0)} {\partial x} = \dfrac {\partial f} {\partial x}\Bigg|_{(x_0,y_0)} = f_x(x_0,y_0)


$$

The notations for $f_y(x_0,y_0)$ follow the same patterns.

### Example: Finding Partial Derivatives of Two-Variable Functions

#### Question

Find $\dfrac{\partial f}{\partial y}$ given that $f(x,y) = 3x\ln y + 2ye^x.$

#### Explanation

We differentiate the given function with respect to $y,$ treating all other variables as constants.

Additionally, we use the sum and constant multiple rules for differentiation, as follows:

$$


\begin{aligned}\frac{𝜕𝑓}{𝜕𝑦} & =\frac{𝜕}{𝜕𝑦}(3𝑥ln⁡𝑦+2𝑦𝑒^{𝑥}) \\ & =\frac{𝜕}{𝜕𝑦}(3𝑥ln⁡𝑦)+\frac{𝜕}{𝜕𝑦}(2𝑦𝑒^{𝑥}) \\ & =3𝑥⋅\frac{𝜕}{𝜕𝑦}(ln⁡𝑦)+2𝑒^{𝑥}⋅\frac{𝜕}{𝜕𝑦}(𝑦) \\ & =3𝑥⋅\frac{1}{𝑦}+2𝑒^{𝑥}⋅1 \\ & =\frac{3𝑥}{𝑦}+2𝑒^{𝑥}\end{aligned}


$$

### Example: Evaluating a Partial Derivative at a Point

#### Question

For the function $f(x,y) = x^2y^2+\sin{x}\cos{y},$ evaluate $\dfrac{\partial f}{\partial x}$ at the point $(\pi,2\pi).$

#### Explanation

We differentiate the given function with respect to $x,$ treating all other variables as constants:

Additionally, we use the sum and constant multiple rules for differentiation, as follows:

$$


\begin{aligned}\frac{𝜕𝑓}{𝜕𝑥} & =\frac{𝜕}{𝜕𝑥}(𝑥^{2}𝑦^{2}+sin⁡𝑥cos⁡𝑦) \\ & =\frac{𝜕}{𝜕𝑥}(𝑥^{2}𝑦^{2})+\frac{𝜕}{𝜕𝑥}(sin⁡𝑥cos⁡𝑦) \\ & =𝑦^{2}⋅\frac{𝜕}{𝜕𝑥}(𝑥^{2})+cos⁡𝑦⋅\frac{𝜕}{𝜕𝑥}(sin⁡𝑥) \\ & =𝑦^{2}⋅(2𝑥)+cos⁡𝑦⋅(cos⁡𝑥) \\ & =2𝑥𝑦^{2}+cos⁡𝑥cos⁡𝑦\end{aligned}


$$

Finally, we evaluate the partial derivative at the point $(\pi,2\pi)\mathbin{:}$

$$


\begin{aligned}\frac{𝜕𝑓}{𝜕𝑥}_{(𝜋,2𝜋)} & =2⋅𝜋⋅(2𝜋)^{2}+cos⁡𝜋⋅cos⁡2𝜋 \\ & =2𝜋⋅4𝜋^{2}+(−1)⋅1 \\ & =8𝜋^{3}−1\end{aligned}


$$
