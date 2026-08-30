# Second-Order Inhomogeneous ODEs With Sinusoidal Forcing

Source: https://www.mathacademy.com/topics/883?courseId=61
Topic ID: 883

## Prerequisites

- [Second-Order Homogeneous Initial Value Problems](./2741-second-order-homogeneous-initial-value-problems.md)
- [Solving First-Order Linear ODEs With Sinusoidal Forcing](./6680-solving-first-order-linear-odes-with-sinusoidal-forcing.md)

## Lesson

### Introduction

Recall that second-order inhomogeneous differential equation takes the form

$$


a(x)y'' + b(x)y' + c(x) y = f(x)


$$

where $a(x),$ $b(x),$ and $c(x)$ are functions of $x$ only and $f(x)$ is a nonzero function.

In general, we say that a second-order ODE has **sinusoidal forcing** if $f(x)$ is a sinusoidal function of the form

$$


f(x) = a \cos \omega x + b \sin \omega x,


$$

where $\omega$ is a constant.

For example, the ODE below has sinusoidal forcing:

$$


\frac{\text{d}^2 y}{\text{d} x^2} + \frac{\text{d} y}{\text{d} x} - 2y= 2 \cos 2 x


$$

Solving a second-order ODE with sinusoidal forcing is similar to the method for solving a second-order ODE with polynomial forcing. The general solution is still the sum of the complementary solution $y_c$ (i.e., the solution to the associated homogeneous ODE) and a particular solution $y_p\mathbin{:}$

$$


y = y_c + y_p


$$

The only difference is in how we find a particular solution. Given a second-order ODE with sinusoidal forcing $f(x) = a \cos \omega x + b \sin \omega x,$ provided that $\sin \omega x$ and $\cos \omega x$ do not feature in the complementary solution, then we assume that a particular solution takes the form

$$


y_p =\alpha \cos \omega x + \beta \sin \omega x.


$$

where $\alpha$ and $\beta$ are unknown constants to be determined.

### Solving a Second-Order ODE with Sinusoidal Forcing

Let's solve the following second-order ODE with sinusoidal forcing:

$$


\frac{\text{d}^2 y}{\text{d} x^2} + \frac{\text{d} y}{\text{d} x} - 2y= 2 \cos 2 x


$$

First, we find the complementary solution by solving the associated homogeneous ODE. The characteristic equation (or auxiliary equation) is

$$


\begin{aligned}𝜆^{2}+𝜆−2 & =0 \\ (𝜆−1)(𝜆+2) & =0,\end{aligned}


$$

so $\lambda = 1$ or $\lambda = -2.$ Consequently, the complementary solution is

$$


y_c = Ae^{x} + Be^{- 2 x}.


$$

Second, we find a particular solution of the inhomogeneous ODE. We see that the right-hand side is $2 \cos 2x,$ and $\cos 2x$ does not appear as a term in the complementary solution, so we assume that a particular solution takes the form

$$


y_p =\alpha \cos 2x + \beta \sin 2x


$$

where $\alpha$ and $\beta$ are constants to be determined.

Calculating the first and second derivatives of $y_p,$ we get

$$


\begin{aligned}\frac{d𝑦_{𝑝}}{d𝑥} & =−2𝛼sin⁡2𝑥+2𝛽cos⁡2𝑥 \\ \,\frac{d^{2}𝑦_{𝑝}}{d𝑥^{2}} & =−4𝛼cos⁡2𝑥−4𝛽sin⁡2𝑥.\end{aligned}


$$

To find the values of $\alpha$ and $\beta,$ we substitute the derivatives into the original ODE and get

$$


\begin{aligned}−4𝛼cos⁡2𝑥−4𝛽sin⁡2𝑥−2𝛼sin⁡2𝑥+2𝛽cos⁡2𝑥−2(𝛼cos⁡2𝑥+𝛽sin⁡2𝑥) & =2cos⁡2𝑥 \\ (2𝛽−6𝛼)cos⁡2𝑥+(−6𝛽−2𝛼)sin⁡2𝑥 & =2cos⁡2𝑥.\end{aligned}


$$

The corresponding terms on both sides should have the same coefficients. Equating the coefficients of like terms, we get the following system:

$$


\begin{aligned}\begin{matrix}2𝛽−6𝛼=2 \\ −6𝛽−2𝛼=0\end{matrix}\end{aligned}


$$

From the second equation, it follows that

$$


- 6 \beta - 2 \alpha = 0 \quad \Rightarrow \quad \alpha = - 3 \beta.


$$

Substituting $\alpha=-3\beta$ into the first equation gives

$$


\begin{aligned}2𝛽−6(−3)𝛽 & =2 \\ 20𝛽 & =2 \\ 𝛽 & =0.1.\end{aligned}


$$

Back-substituting into $\alpha = -3\beta,$ we get

$$


\alpha = -3(0.1) = -0.3.


$$

Therefore, the particular solution is

$$


y_p = - 0.3 \cos 2x + 0.1 \sin 2x,


$$

and the general solution is

$$


\begin{aligned}𝑦 & =𝑦_{𝑐}+𝑦_{𝑝} \\ & =𝐴𝑒^{𝑥}+𝐵𝑒^{−2𝑥}−0.3cos⁡2𝑥+0.1sin⁡2𝑥.\end{aligned}


$$

### Example: Solving a Second-Order Differential Equation Using Sinusoidal Forcing

#### Question

Find the general solution to the equation

#### Explanation

First, we find the complementary solution by solving the associated homogeneous ODE. The characteristic equation has roots so the complementary solution is

Second, we find a particular solution of the inhomogeneous ODE. We see that the right-hand side is and is not a term in the complementary solution, so we assume that a particular solution takes the form where and are constants to be determined.

**** The terms of the complementary solution are and Although appears, is not itself a term because it is multiplied by

Calculating the first and second derivatives of we get

To find the values of and we substitute the derivatives into the original ODE and get

The corresponding terms on both sides should have the same coefficients. Equating the coefficients of like terms, we get the following system:

Solving this system gives

Therefore, the particular solution is and the general solution is

### The Case When the Right-Hand Side and the Complementary Solution Have the Same Term

Given a second-order ODE with sinusoidal forcing $f(x) = a \cos \omega x + b \sin \omega x,$ if $\cos \omega x$ or $\sin \omega x$ *is* a term in the complementary solution, then $a \cos \omega x + b \sin \omega x$ *cannot* be a particular solution. Instead, we assume that a particular solution takes the form

$$


y_p = x(\alpha \cos \omega x + \beta \sin \omega x).


$$

For example, let's find the solution to the following ODE:

$$


\frac{\text{d}^2 y}{\text{d} x^2} + y= 4 \cos x.


$$

First, we find the complementary solution by solving the associated homogeneous ODE. The characteristic equation is

$$


\begin{aligned}𝜆^{2}+1 & =0 \\ 𝜆 & =±i,\end{aligned}


$$

so $\lambda = \text{i}$ or $\lambda = -\text{i}.$ Consequently, the complimentary solution is

$$


y_c = A\cos x + B \sin x.


$$

Second, we find a particular solution of the inhomogeneous ODE. We see that the right-hand side is $4 \cos x$ and $\cos x$ is a term in the complementary solution, so we assume that a particular solution takes the form

$$


y_p = x (\alpha \cos x + \beta \sin x),


$$

where $\alpha$ and $\beta$ are constants that are to be determined.

Calculating the first and second derivatives of $y_p,$ we get

$$


\begin{aligned}\frac{d𝑦_{𝑝}}{d𝑥} & =(𝛼cos⁡𝑥+𝛽sin⁡𝑥)+𝑥(−𝛼sin⁡𝑥+𝛽cos⁡𝑥), \\ \frac{d^{2}𝑦_{𝑝}}{d𝑥^{2}} & =2(−𝛼sin⁡𝑥+𝛽cos⁡𝑥)+𝑥(−𝛼cos⁡𝑥−𝛽sin⁡𝑥).\end{aligned}


$$

To find the values of $\alpha$ and $\beta,$ we substitute the derivatives into the original ODE and get

$$


\begin{aligned}2(−𝛼sin⁡𝑥+𝛽cos⁡𝑥)+𝑥(−𝛼cos⁡𝑥−𝛽sin⁡𝑥)+𝑥(𝛼cos⁡𝑥+𝛽sin⁡𝑥) & =4cos⁡𝑥 \\ −2𝛼sin⁡𝑥+2𝛽cos⁡𝑥 & =4cos⁡𝑥.\end{aligned}


$$

Equating the coefficients, we get the following system of equations:

$$


\begin{aligned}\begin{matrix}2𝛽=4\, & (equating the coefficients of\,\,cos⁡𝑥) \\ −2𝛼=0\, & (equating the coefficients of\,\,sin⁡𝑥)\end{matrix}\end{aligned}


$$

Solving this system gives $\alpha = 0$ and $\beta = 2.$

Therefore, the particular solution is

$$


y_p = 2x \sin{x}


$$

and the general solution is

$$


\begin{aligned}𝑦(𝑥) & =𝑦_{𝑐}(𝑥)+𝑦_{𝑝}(𝑥)=𝐴cos⁡𝑥+𝐵sin⁡𝑥+2𝑥sin⁡𝑥.\end{aligned}


$$

### Example: Solving a Second-Order ODE When the Right-Hand Side and the Complementary Solution are Dependent

#### Question

Find the general solution to the equation

$$


\frac{\text{d}^2 y}{\text{d} x^2} + 4y = 4\sin 2x.


$$

#### Explanation

First, we find the complementary solution by solving the associated homogeneous ODE. The characteristic equation has roots $\lambda = \pm 2 \text{i},$ so the complementary solution is

$$


y_c = A\cos{2x} + B \sin{2x}.


$$

We now need to find the particular solution $y_p(x).$

Second, we find a particular solution of the inhomogeneous ODE. We see that the right-hand side is $4 \sin 2x,$ and $\sin 2x$ is a term in the complementary solution. So, we assume a particular solution of the form

$$


y_p = x (\alpha \cos{2x} + \beta \sin{2x}),


$$

where $\alpha$ and $\beta$ are constants that are to be determined.

Calculating the first and second derivatives of $y_p,$ we get

$$


\begin{aligned}\frac{d𝑦_{𝑝}}{d𝑥} & =(𝛼cos⁡2𝑥+𝛽sin⁡2𝑥)+2𝑥(−𝛼sin⁡2𝑥+𝛽cos⁡2𝑥), \\ \frac{d^{2}𝑦_{𝑝}}{d𝑥^{2}} & =4(−𝛼sin⁡2𝑥+𝛽cos⁡2𝑥)+4𝑥(−𝛼cos⁡2𝑥−𝛽sin⁡2𝑥).\end{aligned}


$$

To find the values of $\alpha$ and $\beta,$ we substitute the derivatives into the original ODE and get

$$


\begin{aligned}4(−𝛼sin⁡2𝑥+𝛽cos⁡2𝑥)+4𝑥(−𝛼cos⁡2𝑥−𝛽sin⁡2𝑥)+4𝑥(𝛼cos⁡2𝑥+𝛽sin⁡2𝑥) & =4sin⁡2𝑥 \\ −4𝛼sin⁡2𝑥+4𝛽cos⁡2𝑥 & =4sin⁡2𝑥.\end{aligned}


$$

Equating the coefficients, we get the following system of equations:

$$


\begin{aligned}\begin{matrix}4𝛽=0\, & (equating the coefficients of\,\,cos⁡2𝑥) \\ −4𝛼=4\, & (equating the coefficients of\,\,sin⁡2𝑥)\end{matrix}\end{aligned}


$$

Solving this system gives $\alpha = -1$ and $\beta = 0.$

Therefore, the particular solution is

$$


y_p(x) = -x \cos{2x},


$$

and the general solution is

$$


\begin{aligned}𝑦 & =𝑦_{𝑐}+𝑦_{𝑝} \\ & =𝐴cos⁡2𝑥+𝐵sin⁡2𝑥−𝑥cos⁡2𝑥.\end{aligned}


$$

### Example: Solving an Initial Value Problem

#### Question

Given that the differential equation

$$


\frac{\text{d}^2 y}{\text{d} x^2} + 4y = 4\sin 2x


$$

has the general solution

$$


y(x) = A \cos{2x} + B \sin{2x} - x \cos{2x},


$$

solve the initial value problem

$$


\frac{\text{d}^2 y}{\text{d} x^2} + 4y = 4\sin 2x, \qquad y(0) = 2 , \ \ y'(0) = -3.


$$

#### Explanation

We find the constants $A$ and $B$ by substituting the initial conditions.

- Substituting $y(0)=2$ into the general solution gives

- Differentiating $y$ gives Substituting $y'(0)=-3$ into the derivative gives

Finally, since $A=2$ and $B=-1,$ we have the following solution to the initial value problem:

$$


\begin{aligned}𝑦=2cos⁡2𝑥−sin⁡2𝑥−𝑥cos⁡2𝑥\end{aligned}


$$
