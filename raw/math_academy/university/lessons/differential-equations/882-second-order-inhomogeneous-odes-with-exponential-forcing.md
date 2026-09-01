# Second-Order Inhomogeneous ODEs With Exponential Forcing

Source: https://www.mathacademy.com/topics/882?courseId=61
Topic ID: 882

## Prerequisites

- [Second-Order Homogeneous Initial Value Problems](./2741-second-order-homogeneous-initial-value-problems.md)
- [Solving First-Order Linear ODEs With Exponential Forcing](./6679-solving-first-order-linear-odes-with-exponential-forcing.md)

## Lesson

### Introduction

Recall that a second-order inhomogeneous differential equation takes the form

$$


a(x)y'' + b(x)y' + c(x) y = f(x)


$$

where $a(x),$ $b(x),$ and $c(x)$ are functions of $x$ only and $f(x)$ is a nonzero function.

In general, we say that a second-order ODE has **exponential forcing** if $f(x)$ is an exponential function. For example, the ODE below has exponential forcing:

$$


\frac{\text{d}^2 y}{\text{d} x^2} + 5\frac{\text{d} y}{\text{d} x} + 6y =10 e ^ {2x}


$$

The method for solving a second-order ODE with exponential forcing is similar to the method for solving a second-order ODE with polynomial forcing. The general solution is still the sum of the complementary solution $y_c$ (i.e., the solution to the associated homogeneous ODE) and a particular solution $y_p\mathbin{:}$

$$


y = y_c + y_p


$$

The only difference is in how we find a particular solution. Given a second-order ODE with exponential forcing $f(x) = ae^{bx},$ provided that $e^{bx}$ is not a term in the complementary solution, we assume that a particular solution takes the form

$$


y_p = \alpha e^{bx}


$$

where $b$ is a known constant and $\alpha$ is an unknown constant to be determined.

### Solving a Second-Order ODE with Exponential Forcing

Let's solve the following second-order ODE with exponential forcing:

$$


\frac{\text{d}^2 y}{\text{d} x^2} + 5\frac{\text{d} y}{\text{d} x} + 6y =10 e ^ {2x}


$$

First, we find the complementary solution by solving the associated homogeneous ODE. The characteristic equation (or auxiliary equation) is

$$


\begin{aligned}𝜆^{2}+5𝜆+6 & =0 \\ (𝜆+3)(𝜆+2) & =0,\end{aligned}


$$

so $\lambda = -3$ or $\lambda = -2.$ Consequently, the complementary solution is

$$


y_c = Ae^{-2x} + Be^{-3x}.


$$

Second, we find a particular solution of the inhomogeneous ODE. We see that the right-hand side is $10e^{2x},$ and $e^{2x}$ is not a term in the complementary solution, so we assume that a particular solution takes the form

$$


y_p = \alpha e^{2x}


$$

where $\alpha$ is a constant to be determined.

Calculating the first and second derivatives of $y_p,$ we get

$$


\frac{\text{d}y_p}{\text{d}x} = 2 \alpha e ^{2x}, \quad \frac{\text{d}^2y_p}{\text{d}x^2} = 4 \alpha e ^{2x}.


$$

To find the value of $\alpha,$ we substitute the derivatives into the original ODE and get

$$


\begin{aligned}4𝛼𝑒^{2𝑥}+5(2𝛼𝑒^{2𝑥})+6𝛼𝑒^{2𝑥} & =10𝑒^{2𝑥} \\ 20𝛼𝑒^{2𝑥} & =10𝑒^{2𝑥} \\ 𝛼 & =\frac{1}{2}.\end{aligned}


$$

Therefore, the particular solution is

$$


y_p = \dfrac{1}{2}e^{2x}


$$

and the general solution is

$$


\begin{aligned}𝑦 & =𝑦_{𝑐}+𝑦_{𝑝} \\ & =𝐴𝑒^{−2𝑥}+𝐵𝑒^{−3𝑥}+\frac{1}{2}𝑒^{2𝑥}.\end{aligned}


$$

### Example: Solving a Second-Order ODE with Exponential Forcing

#### Question

Find the general solution to the equation

$$


\frac{\text{d}^2 y}{\text{d} x^2} + \frac{\text{d} y}{\text{d} x} - 2y = 20 e ^ {3x}.


$$

#### Explanation

First, we find the complementary solution by solving the associated homogeneous ODE. Since the roots of the characteristic equation are $\lambda = 1, -2,$ we get

$$


y_c = Ae^{x} + Be^{- 2 x}.


$$

Second, we find a particular solution of the inhomogeneous ODE. We see that the right-hand side is $20e^{3x},$ and $e^{3x}$ is not a term in the complementary solution, so we assume that a particular solution takes the form

$$


y_p = \alpha e^{3x},


$$

where $\alpha$ is a constant to be determined.

Calculating the first and second derivatives of $y_p,$ we get

$$


\frac{\text{d}y_p}{\text{d}x} = 3 \alpha e ^{3x}, \quad \frac{\text{d}^2y_p}{\text{d}x^2} = 9 \alpha e ^{3x}.


$$

To find the value of $\alpha,$ we substitute the derivatives into the original ODE and get

$$


\begin{aligned}9𝛼𝑒^{3𝑥}+3𝛼𝑒^{3𝑥}−2𝛼𝑒^{3𝑥} & =20𝑒^{3𝑥} \\ 𝛼(9+3−2)𝑒^{3𝑥} & =20𝑒^{3𝑥} \\ 10𝛼𝑒^{3𝑥} & =20𝑒^{3𝑥} \\ 10𝛼 & =20 \\ 𝛼 & =2.\end{aligned}


$$

Therefore, the particular solution is

$$


y_p = 2e^{3x}


$$

and the general solution is

$$


\begin{aligned}𝑦 & =𝑦_{𝑐}+𝑦_{𝑝} \\ & =𝐴𝑒^{𝑥}+𝐵𝑒^{−2𝑥}+2𝑒^{3𝑥}.\end{aligned}


$$

### The Case When the Right-Hand Side and the Complementary Solution are Linearly Dependent

Given a second-order ODE with exponential forcing $f(x) = ae^{bx},$ if $e^{bx}$ *is* a term in the complementary solution, then $\alpha e^{bx}$ *cannot* be a particular solution. Instead, we assume that a particular solution takes the form

$$


y_p = \alpha x e^{bx}


$$

For example, let's find the solution to the following ODE:

$$


\frac{\text{d}^2 y}{\text{d} x^2} + 5\frac{\text{d} y}{\text{d} x} + 6y =3 e ^ {-2x}


$$

First, we find the complementary solution by solving the associated homogeneous ODE. The characteristic equation is

$$


\begin{aligned}𝜆^{2}+5𝜆+6 & =0 \\ (𝜆+2)(𝜆+3) & =0,\end{aligned}


$$

so $\lambda = -2$ or $\lambda = - 3.$ Consequently, the complimentary solution is

$$


y_c = Ae^{-2x} + Be^{-3x}.


$$

Second, we find a particular solution to the inhomogeneous ODE. We see that the right-hand side is $3e^{-2x},$ and $e^{-2x}$ is a term in the complementary solution, so we assume that a particular solution takes the form

$$


y_p = \alpha x e^{-2x},


$$

where $\alpha$ is a constant to be determined.

Calculating the first and second derivatives of $y_p,$ we get

$$


\begin{aligned}\frac{d𝑦_{𝑝}}{d𝑥} & =−2𝛼𝑥𝑒^{−2𝑥}+𝛼𝑒^{−2𝑥}, \\ \,\frac{d^{2}𝑦_{𝑝}}{d𝑥^{2}} & =4𝛼𝑥𝑒^{−2𝑥}−2𝛼𝑒^{−2𝑥}−2𝛼𝑒^{−2𝑥} \\ & =4𝛼𝑥𝑒^{−2𝑥}−4𝛼𝑒^{−2𝑥}.\end{aligned}


$$

To find the value of $\alpha,$ we substitute the derivatives into the original ODE and get

$$


\begin{aligned}\underset{}{4𝛼𝑥𝑒^{−2𝑥}}−4𝛼𝑒^{−2𝑥}+5(\underset{}{−2𝛼𝑥𝑒^{−2𝑥}}+𝛼𝑒^{−2𝑥})+\underset{}{6𝛼𝑥𝑒^{−2𝑥}} & =3𝑒^{−2𝑥}.\end{aligned}


$$

Canceling the underlined terms, we get

$$


\begin{aligned}𝛼𝑒^{−2𝑥} & =3𝑒^{−2𝑥} \\ 𝛼 & =3.\end{aligned}


$$

Therefore, the particular solution is

$$


y_p = 3 x e^{-2x},


$$

and the general solution is

$$


\begin{aligned}𝑦 & =𝑦_{𝑐}+𝑦_{𝑝} \\ & =𝐴𝑒^{−2𝑥}+𝐵𝑒^{−3𝑥}+3𝑥𝑒^{−2𝑥}.\end{aligned}


$$

### Example: Solving a Second-Order ODE When the Right-Hand Side and the Complementary Solution are Linearly Dependent

#### Question

Find the general solution to the equation

#### Explanation

First, we find the complementary solution by solving the associated homogeneous ODE. Since the roots of the characteristic equation are we get

Second, we find a particular solution of the inhomogeneous ODE. We see that the right-hand side is and is a term in the complementary solution, so we assume that a particular solution takes the form

where is a constant to be determined.

Calculating the first and second derivatives of we get

To find the value of we substitute the derivatives into the original ODE and get

Therefore, the particular solution is

The general solution is given by

and the general solution is

### Second-Order ODEs With Exponential Forcing and Repeated Roots

Given a second-order ODE with exponential forcing $f(x) = ae^{bx},$ if $e^{bx}$ and $xe^{bx}$ are *both* terms in the complementary solution, then neither can be a particular solution. Instead, we assume that a particular solution takes the form

$$


y_p = \alpha x^2 e^{bx}.


$$

For example, let's find the solution to the following ODE:

$$


\frac{\text{d}^2 y}{\text{d} x^2} - 12\frac{\text{d} y}{\text{d} x} + 36y = e ^{6x}


$$

First, we find the complementary solution by solving the associated homogeneous ODE. The characteristic equation is

$$


\begin{aligned}𝜆^{2}−12𝜆+36 & =0 \\ (𝜆−6)(𝜆−6) & =0,\end{aligned}


$$

so $\lambda = 6$ is a repeated root. Consequently, the complementary solution is

$$


y = Ae^{6 x} + Bxe^{6 x}.


$$

Second, we find a particular solution of the inhomogeneous ODE. We see that the right-hand side is $e^{6x},$ and $e^{6x}$ and $xe^{6x}$ are both terms in the complementary solution, so we assume that a particular solution takes the form

$$


y_p = \alpha x^2 e^{6x},


$$

where $\alpha$ is a constant to be determined.

Calculating the first and second derivatives of $y_p,$ we get

$$


\begin{aligned}\frac{d𝑦_{𝑝}}{d𝑥} & =6𝛼𝑥^{2}𝑒^{6𝑥}+2𝛼𝑥𝑒^{6𝑥} \\ \,\frac{d^{2}𝑦_{𝑝}}{d𝑥^{2}} & =12𝑥𝛼𝑒^{6𝑥}+36𝛼𝑥^{2}𝑒^{6𝑥}+2𝛼𝑒^{6𝑥}+12𝛼𝑥𝑒^{6𝑥} \\ & =36𝛼𝑥^{2}𝑒^{6𝑥}+2𝛼𝑒^{6𝑥}+24𝛼𝑥𝑒^{6𝑥}.\end{aligned}


$$

To find the value of $\alpha,$ we substitute the derivatives into the original ODE and get

$$


\underline {36 \alpha x^2 e ^{6x}} +2 \alpha e ^{6x} +\underline{ 24 \alpha x e ^{6x} }-12(\underline{6 \alpha x^ 2e ^{6x} }+ \underline {2 \alpha x e^{6x}}) +\underline{36 \alpha x^2 e ^{6x}} = e^{6x}.


$$

Canceling the underlined terms, we get

$$


\begin{aligned}2𝛼𝑒^{6𝑥} & =𝑒^{6𝑥}\,⇒\,𝛼=\frac{1}{2}.\end{aligned}


$$

Therefore, the particular solution is

$$


y_p = \dfrac{1}{2} x^2 e^{6x},


$$

and the general solution is

$$


\begin{aligned}𝑦 & =𝑦_{𝑐}+𝑦_{𝑐} \\ & =𝐴𝑒^{6𝑥}+𝐵𝑥𝑒^{6𝑥}+\frac{1}{2}𝑥^{2}𝑒^{6𝑥}.\end{aligned}


$$

### Example: Solving a Second-Order ODE with Exponential Forcing and Repeated Roots

#### Question

Find the general solution to the equation

$$


\frac{\text{d}^2 y}{\text{d} x^2} - 6\frac{\text{d} y}{\text{d} x} + 9y = e ^{3x}.


$$

#### Explanation

First, we find the complementary solution by solving the associated homogeneous ODE. Since the characteristic equation has a single repeated root $\lambda = 3,$ the complementary solution is

$$


y_c(x) = Ae^{3x} + Bxe^{3x}.


$$

Second, we find a particular solution of the inhomogeneous ODE. We see that the right-hand side is $e^{3x},$ and $e^{3x}$ and $xe^{3x}$ are both terms in the complementary solution, so we assume that a particular solution takes the form

$$


y_p = \alpha x^2e ^ {3x},


$$

where $\alpha$ is a constant to be determined.

Calculating the first and second derivatives of $y_p,$ we get

$$


\begin{aligned}\frac{d𝑦_{𝑝}}{d𝑥} & =(3𝑥^{2}+2𝑥)𝛼𝑒^{3𝑥},\,\frac{d^{2}𝑦_{𝑝}}{d𝑥^{2}}=(9𝑥^{2}+12𝑥+2)𝛼𝑒^{3𝑥}.\end{aligned}


$$

We substitute $y_p$, $y'_p$ and $y_p''$ into the ODE and solve for $\alpha\mathbin{:}$

$$


\begin{aligned}(9𝑥^{2}+12𝑥+2)𝛼𝑒^{3𝑥}−6(3𝑥^{2}+2𝑥)𝛼𝑒^{3𝑥}+9𝛼𝑥^{2}𝑒^{3𝑥} & =𝑒^{3𝑥} \\ (9𝑥^{2}+12𝑥+2−18𝑥^{2}−12𝑥+9𝑥^{2})𝛼𝑒^{3𝑥} & =𝑒^{3𝑥} \\ 2𝛼𝑒^{3𝑥} & =𝑒^{3𝑥} \\ 2𝛼 & =1 \\ 𝛼 & =\frac{1}{2}\end{aligned}


$$

Therefore, the particular solution is

$$


y_p(x) = \dfrac 1 2x^2 e ^{3x},


$$

and the general solution is

$$


\begin{aligned}𝑦 & =𝑦_{𝑐}+𝑦_{𝑝} \\ & =𝐴𝑒^{3𝑥}+𝐵𝑥𝑒^{3𝑥}+\frac{1}{2}𝑥^{2}𝑒^{3𝑥}.\end{aligned}


$$

### Example: Solving an Initial Value Problem

#### Question

Given that the differential equation

$$


\frac{\text{d}^2 y}{\text{d} x^2} - 6\frac{\text{d} y}{\text{d} x} + 9y = e ^{3x}


$$

has the general solution

$$


Ae^{3 x} + Bxe^{3 x} + \dfrac 1 2 x ^2 e^{3 x},


$$

solve the initial value problem

$$


\frac{\text{d}^2 y}{\text{d} x^2} - 6\frac{\text{d} y}{\text{d} x} + 9y = e ^{3x}, \qquad y(0) = 2 , \ \ y'(0) = 1.


$$

#### Explanation

We find the constants $A$ and $B$ by substituting the initial conditions.

- Substituting $y(0)=2$ into the general solution gives

- Differentiating $y$ gives Substituting $y'(0)=1$ into the derivative gives

Finally, since $A=2$ and $B=-5,$ we have the following solution to the initial value problem:

$$


\begin{aligned}𝑦=2𝑒^{3𝑥}−5𝑥𝑒^{3𝑥}+\frac{1}{2}𝑥^{2}𝑒^{3𝑥}\end{aligned}


$$
