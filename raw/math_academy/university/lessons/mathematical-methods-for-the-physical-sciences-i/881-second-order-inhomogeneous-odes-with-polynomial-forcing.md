# Second-Order Inhomogeneous ODEs With Polynomial Forcing

Source: https://www.mathacademy.com/topics/881?courseId=154
Topic ID: 881

## Prerequisites

- [Second-Order Homogeneous Initial Value Problems](./2741-second-order-homogeneous-initial-value-problems.md)

## Lesson

### Introduction

Recall that a second-order homogeneous differential equation takes the form

$$


a(x)y'' + b(x)y' + c(x) y = 0


$$

where $a(x),$ $b(x),$ and $c(x)$ are functions of $x$ only.

A **second-order inhomogeneous** differential equation is similar, except the right-hand side does *not* equal zero. So, a second-order inhomogeneous differential equation can be written as

$$


a(x)y'' + b(x)y' + c(x) y = f(x)


$$

where $a(x),$ $b(x),$ and $c(x)$ are functions of $x$ only and $f(x)$ is a nonzero function.

For example, the following equation is a second-order inhomogeneous ODE because the right-hand side is $3$ instead of $0\mathbin{:}$

$$


\frac{\text{d}^2 y}{\text{d} x^2} + 5\frac{\text{d} y}{\text{d} x} + 6y =3


$$

In general, we say that a second-order ODE has **polynomial forcing** if $f(x)$ is a polynomial.

### Solving Second-Order Inhomogeneous ODEs

To find the general solution to an inhomogeneous ODE, we perform the following steps:

- **Step 1:** Find the solution $y_c$ of the associated homogeneous ODE. This solution is called the **complementary solution** (or the **homogeneous solution**).

- **Step 2:** Find a **particular solution** $y_p$ (also known as the **particular integral**) of the inhomogeneous ODE. If $f(x)$ is an $n$th degree polynomial, then so is a particular solution.

- **Step 3:** Write the general solution as the sum of the complementary solution and the particular solution: $y = y_c + y_p.$

To illustrate, let's find the general solution to the following inhomogeneous ODE:

$$


\frac{\text{d}^2 y}{\text{d} x^2} + 5\frac{\text{d} y}{\text{d} x} + 6y =3


$$

- **Step 1:** First we find the complementary solution $y_c$ by solving the homogeneous ODE: The characteristic equation (or auxiliary equation) is so $\lambda=-3$ or $\lambda=-2.$ Consequently, the complementary solution is

- **Step 2:** Second, we find a particular solution $y_p$ of the inhomogeneous ODE. Since the right-hand side is a constant, it is a polynomial of degree $0,$ which means a particular solution will also be a polynomial of degree $0,$ or a constant. So we assume where $\alpha$ is a constant to be found. Calculating the first and second derivatives of $y_p,$ we get To find the value of $\alpha,$ we substitute the derivatives into the original ODE and get Therefore, the particular solution is

- **Step 3:** Finally, we write the general solution as the sum of the complementary solution and the particular solution and get

### Example: Solving a Second-Order Inhomogeneous ODE with Constant Forcing

#### Question

Find the general solution to the equation

$$


\dfrac {\textrm {d} ^ 2 y} {\textrm {d} x ^ 2} - \dfrac {\textrm {d} y} {\textrm {d} x} - 2 y = 6.


$$

#### Explanation

**** First we find the complementary solution $y_c$ by solving the homogeneous ODE. The characteristic equation

$$


\lambda^2 - \lambda - 2 = 0


$$

has roots $\lambda = -1, 2,$ so the complementary solution is

$$


y_c = A e ^ {- x} + B e ^ {2 x}.


$$

**** Second, we find a particular solution $y_p$ of the inhomogeneous ODE. Since the right hand side is a constant, it is a polynomial of degree $0,$ which means a particular solution will also be a polynomial of degree $0,$ or a constant. So we assume

$$


y_p =\alpha,


$$

where $\alpha$ is a constant to be found. Calculating the first and second derivatives of $y_p,$ we get

$$


\frac{\text{d}y_p}{\text{d}x} = 0,\qquad \frac{\text{d}^2y_p}{\text{d}x^2} = 0.


$$

To find the value of $\alpha,$ we substitute the derivatives into the original ODE and get

$$


\begin{aligned}0−0−2𝛼=6\,⟹\,𝛼=−3.\end{aligned}


$$

Therefore, the particular solution is

$$


y_p = -3.


$$

**** Finally, we write the general solution as the sum of the complementary solution and the particular solution, and get

$$


\begin{aligned}𝑦 & =𝑦_{𝑐}+𝑦_{𝑝} \\ & =𝐴𝑒^{−𝑥}+𝐵𝑒^{2𝑥}−3.\end{aligned}


$$

### Example: Solving a Second-Order Inhomogeneous ODE with Affine Forcing

#### Question

Find the general solution to the equation

$$


\dfrac {\textrm {d} ^ 2 y} {\textrm {d} x ^ 2} -4 \dfrac {\textrm {d} y} {\textrm {d} x} +4 y = 8x + 4.


$$

#### Explanation

**** First we find the complementary solution $y_c$ by solving the homogeneous ODE. The characteristic equation

$$


\lambda^2 - 4\lambda + 4 = 0


$$

has a repeated root $\lambda = 2,$ so the complementary solution is

$$


y_c = A e ^ { 2 x} + B x e ^ {2 x}.


$$

**** Second, we find a particular solution $y_p$ of the inhomogeneous ODE. Since the right hand side is a polynomial of degree $1,$ a particular solution will also be a polynomial of degree $1.$ So we assume

$$


y_p=\alpha x + \beta


$$

where $\alpha$ and $\beta$ are constants that are to be determined.

Calculating the first and second derivatives of $y_p,$ we get

$$


\frac{\text{d}y_p}{\text{d}x} = \alpha,\qquad \frac{\text{d}^2y_p}{\text{d}x^2} = 0.


$$

To find the values of $\alpha$ and $\beta,$ we substitute the derivatives into the original ODE and get

$$


\begin{aligned}0−4𝛼+4(𝛼𝑥+𝛽) & =8𝑥+4 \\ 4𝛼𝑥+(4𝛽−4𝛼) & =8𝑥+4.\end{aligned}


$$

Equating the coefficients, we get the following system of equations:

$$


\begin{aligned}\begin{matrix}4𝛼=8\, & (equating the coefficients of\,\,𝑥) \\ 4𝛽−4𝛼=4\, & (equating the constants)\end{matrix}\end{aligned}


$$

Solving this system gives $\alpha=2, \beta=3.$

Therefore, the particular solution $y_p$ is

$$


y_p =2x+3.


$$

**** Finally, we write the general solution as the sum of the complementary solution and the particular solution, and get

$$


\begin{aligned}𝑦 & =𝑦_{𝑐}+𝑦_{𝑝} \\ & =𝐴𝑒^{2𝑥}+𝐵𝑥𝑒^{2𝑥}+2𝑥+3.\end{aligned}


$$

### Example: Solving a Second-Order Inhomogeneous ODE with Quadratic Forcing

#### Question

Find the general solution to the equation

$$


y'' +y' -2y = x ^ 2 + 5 x - 3.


$$

#### Explanation

**** First we find the complementary solution $y_c$ by solving the homogeneous ODE. The characteristic equation

$$


\lambda^2 + \lambda - 2 = 0


$$

has roots $\lambda = 1,-2,$ so the complementary solution is

$$


y_c = Ae^{x} + Be^{- 2 x}.


$$

**** Second, we find a particular solution $y_p$ of the inhomogeneous ODE. Since the right hand side is a polynomial of degree $2,$ a particular solution will also be a polynomial of degree $2.$ So we assume

$$


y_p =\alpha x^2 + \beta x + \gamma


$$

where $\alpha,$ $\beta,$ and $\gamma$ are constants that are to be determined.

Calculating the first and second derivatives of $y_p,$ we get

$$


y_p' = 2\alpha x +\beta,\qquad y_p'' = 2\alpha.


$$

To find the values of $\alpha,$ $\beta,$ and $\gamma,$ we substitute the derivatives into the original ODE and get

$$


\begin{aligned}2𝛼+(2𝛼𝑥+𝛽)−2(𝛼𝑥^{2}+𝛽𝑥+𝛾) & =𝑥^{2}+5𝑥−3 \\ −2𝛼𝑥^{2}+(2𝛼−2𝛽)𝑥+(2𝛼+𝛽−2𝛾) & =𝑥^{2}+5𝑥−3\end{aligned}


$$

Equating the coefficients, we get the following system of equations:

$$


\begin{aligned}\begin{matrix}−2𝛼=1\, & (equating the coefficients of\,\,𝑥^{2}) \\ 2𝛼−2𝛽=5\, & (equating the coefficients of\,\,𝑥) \\ 2𝛼+𝛽−2𝛾=−3\, & (equating the constants)\end{matrix}\end{aligned}


$$

Solving this system gives $\alpha=-\dfrac{1}{2}, \beta=-3, \gamma=-\dfrac{1}{2}.$

Therefore, the particular solution is

$$


y_p =- \frac{x^2}{2} - 3 x - \dfrac 1 2.


$$

**** We write the general solution as the sum of the complementary solution and the particular solution, and get

$$


\begin{aligned}𝑦 & =𝑦_{𝑐}+𝑦_{𝑝} \\ & =𝐴𝑒^{𝑥}+𝐵𝑒^{−2𝑥}−\frac{𝑥^{2}}{2}−3𝑥−\frac{1}{2}.\end{aligned}


$$

### Example: Solving an Initial Value Problem

#### Question

Given that the differential equation

$$


y'' +y' -2y = x ^ 2 + 5 x - 3


$$

has the general solution

$$


y = Ae^{x} + Be^{- 2 x} - \frac{x^2}{2} - 3 x - \dfrac 1 2,


$$

solve the initial value problem

$$


y'' +y' -2y = x ^ 2 + 5 x - 3, \qquad y(0) = -\dfrac{1}{2}, \ \ y'(0) = 0.


$$

#### Explanation

We find the constants $A$ and $B$ using the initial conditions.

- Substituting $y(0) = -\dfrac{1}{2}$ into the general solution gives

- To apply the condition $y'(0) = 0,$ we first differentiate $y$ to get and then we substitute $y'(0)=0$ into the above to get

So we have the following system of equations for $A$ and $B\mathbin{:}$

$$


\begin{aligned}𝐴+𝐵=0 \\ 𝐴−2𝐵=3\end{aligned}


$$

Solving this system gives $A=1, B=-1.$

Therefore, the solution to the initial value problem is

$$


y = e^{x} -e^{-2 x} - \frac{x^2}{2} - 3 x - \dfrac 1 2.


$$
