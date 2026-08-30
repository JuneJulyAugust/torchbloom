# Solving First-Order Linear ODEs With Sinusoidal Forcing

Source: https://www.mathacademy.com/topics/6680?courseId=154
Topic ID: 6680

## Prerequisites

- [General Solutions of First-Order Linear ODEs](./6678-general-solutions-of-first-order-linear-odes.md)

## Lesson

### Introduction

Consider the first-order inhomogeneous ODE with **constant coefficients**

$$


a y' + b y = f(x),


$$

where $a$ and $b$ are constants ($a \neq 0$).

As we know, the method of finding the general solution is to find the sum of the complementary solution $y_c(x)$ and a particular solution $y_p(x).$

$$


y(x) = y_c(x) + y_p(x)


$$

To find the particular solution $y_p(x),$ we examine the functional form of the forcing term $f(x)$ and guess a form for $y_p(x)$ that matches it.

An ODE exhibits **sinusoidal forcing** if the forcing term $f(x)$ is a sine or cosine function, or a combination of both. It is typically written as

$$


f(x) = C \cos(\omega x) + D \sin(\omega x)


$$

where $C$ and $D$ are constants (not both zero).

Now, if we choose only a sine or only a cosine as a trial function for the particular solution, differentiation will introduce the other sinusoidal term, since the derivative of a sinusoid is another sinusoid. Substituting such a trial solution into the ODE therefore produces both sine and cosine terms.

To ensure that this combination can match the forcing term $f(x),$ the trial guess *must* include both sine and cosine terms of the same frequency $\omega,$ even when $f(x)$ itself contains only one of them.

Therefore, our trial guess for the particular solution is

$$


y_p(x) = \alpha \cos(\omega x) + \beta \sin(\omega x),


$$

where $\alpha$ and $\beta$ are to be determined.

In this lesson, we focus on solving first-order inhomogeneous ODEs with sinusoidal forcing. Let's look at a concrete example.

### A Worked Example

Consider the differential equation

$$


\frac {\textrm {d} y} {\textrm {d} x} + 2 y = 10\sin x.


$$

The associated homogeneous equation is

$$


\frac {\textrm {d} y} {\textrm {d} x} + 2 y = 0


$$

and therefore, the complementary solution is

$$


y_c(x) = Ae^{-2x}


$$

where $A$ is an arbitrary constant. Let's find the particular solution $y_p(x)$ to this equation.

Since the right-hand side of the inhomogeneous equation is the sinusoidal function $f(x) = 10\sin x,$ we assume a particular solution of the form

$$


y_p(x) = \alpha \cos x + \beta \sin x,


$$

where $\alpha$ and $\beta$ are constants to be determined.

Calculating the first derivative of $y_p$ gives

$$


\frac{\textrm{d}y_p}{\textrm{d}x} = - \alpha \sin x + \beta \cos x.


$$

To find the values of $\alpha$ and $\beta,$ we substitute $y_p$ and its derivative into the differential equation:

$$


( - \alpha \sin x + \beta \cos x) + 2(\alpha \cos x + \beta \sin x) = 10\sin x.


$$

Grouping the terms on the left-hand side gives

$$


(2\alpha+\beta)\cos x + (-\alpha + 2\beta) \sin x = 10\sin x + 0\cos x.


$$

Equating the coefficients of $\sin x$ and $\cos x$ on both sides of the equation, we get the following system of equations:

$$


\begin{aligned}\begin{aligned}2𝛼+𝛽=0\, & (equating the coefficients of\,cos⁡𝑥) \\ −𝛼+2𝛽=10\, & (equating the coefficients of\,sin⁡𝑥)\end{aligned}\end{aligned}


$$

Solving this system gives $\alpha=-2, \beta=4.$

Therefore, the particular solution $y_p(x)$ is

$$


y_p(x) = -2\cos x + 4\sin x


$$

and the general solution to the equation is

$$


y(x) = y_c(x) + y_p(x) = Ae^{-2x} -2\cos x + 4\sin x.


$$

### Example: Finding a Particular Solution to a First-Order Inhomogeneous ODE With Sinusoidal Forcing

#### Question

Given that the differential equation

$$


\frac {\textrm {d} y} {\textrm {d} x} + 3 y = 2\cos{x}


$$

has the complementary solution $y_c(x) = A e ^ {-3x}$, find the particular solution $y_p(x)$ to this equation.

#### Explanation

To find the general solution of an inhomogeneous first-order linear equation with constant coefficients on the left-hand side, we must find the sum of the complementary and particular solutions.

The right-hand side of the inhomogeneous equation is $2\cos{x}.$ So, we assume the particular solution to be

$$


y_p(x) = \alpha \cos x + \beta \sin x,


$$

where $\alpha$ and $\beta$ are constants to be determined.

Calculating the first derivative of $y_p$ gives

$$


\frac{\textrm{d}y_p}{\textrm{d}x} = - \alpha \sin {x} + \beta \cos {x}.


$$

To find the values of $\alpha$ and $\beta,$ we substitute $y_p$ and $y_p'$ into the differential equation:

$$


( - \alpha \sin {x} + \beta \cos {x}) + 3(\alpha \cos x + \beta \sin x) = 2\cos{x}.


$$

Grouping the terms on the left-hand side gives

$$


(3\alpha+\beta)\cos x + (-\alpha + 3\beta) \sin x = 2\cos{x}.


$$

Equating the coefficients, we get the following system of equations:

$$


\begin{aligned}\begin{aligned}3𝛼+𝛽=2\, & (equating the coefficients of\,cos⁡𝑥) \\ −𝛼+3𝛽=0\, & (equating the coefficients of\,sin⁡𝑥)\end{aligned}\end{aligned}


$$

Solving this system gives $\alpha = \dfrac 3 5,$ $\beta = \dfrac 1 5.$

Therefore, the particular solution $y_p(x)$ is

$$


y_p(x) = \dfrac{3}{5} \cos(x) + \dfrac{1}{5} \sin(x).


$$

### Example: Finding the General Solution to a First-Order Inhomogeneous ODE With Sinusoidal Forcing

#### Question

Consider the differential equation

$$


2\frac{\textrm{d} y}{\textrm{d} x} + 4 y = 8 \cos(3x) - 2 \sin(3x).


$$

Find the general solution to this equation given that the complementary solution is $y_c(x) = Ae^{-2x},$ where $A$ is an arbitrary constant.

#### Explanation

To find the general solution of an inhomogeneous first-order linear equation with constant coefficients on the left-hand side, we must find the sum of the complementary and particular solutions.

To find the complementary solution $y_c$ we solve the corresponding homogeneous equation, given by

$$


2\frac{\textrm{d} y_c}{\textrm{d} x} + 4 y_c = 0.


$$

Solving this equation, we find that the complementary solution is

$$


y_c = Ae^{-2x}


$$

where $A$ is an arbitrary constant.

We now need to find the particular solution $y_p(x).$

The right-hand side of the inhomogeneous equation is $8\cos(3x) - 2\sin(3x).$ So, we assume the particular solution to be

$$


y_p(x) = \alpha \cos(3x) + \beta \sin(3x),


$$

where $\alpha$ and $\beta$ are constants that are to be determined.

Calculating the first derivative of $y_p$ gives

$$


\frac{\textrm{d}y_p}{\textrm{d}x} = - 3\alpha \sin(3x) + 3\beta \cos(3x).


$$

To find the values of $\alpha$ and $\beta,$ we substitute $y_p$ and $y_p'$ into the differential equation:

$$


2 ( - 3\alpha \sin(3x) + 3\beta \cos(3x)) + 4(\alpha \cos(3x)+ \beta \sin(3x)) = 8 \cos(3x) - 2\sin(3x).


$$

Grouping the terms on the left-hand side gives

$$


(6\beta + 4\alpha)\cos(3x) + (-6\alpha + 4 \beta) \sin(3x) = 8 \cos(3x) - 2\sin(3x).


$$

Equating the coefficients, we get the following system of equations:

$$


\begin{aligned}\begin{aligned}6𝛽+4𝛼=8\, & (equating the coefficients of\,cos⁡(3𝑥)) \\ −6𝛼+4𝛽=−2\, & (equating the coefficients of\,sin⁡(3𝑥))\end{aligned}\end{aligned}


$$

Solving this system gives $\alpha=\dfrac{11}{13}, \beta=\dfrac{10}{13}.$

Therefore,

$$


y_p(x) = \dfrac{11}{13}\cos(3x) + \dfrac{10}{13} \sin(3x).


$$

The general solution is given by

$$


y(x) = y_c(x)+y_p(x),


$$

and therefore, the general solution in our case is

$$


y = A e^{-2x} + \left(\boxed{\dfrac{11}{13} }\right)\cos(3x) + \left(\boxed{\dfrac{10}{13} }\right) \sin(3x).


$$

### Example: Solving an Initial Value Problem

#### Question

Consider the following initial value problem:

$$


y' + 3y = 26 \sin(2x), \qquad y(0) = 1


$$

Given that the differential equation

$$


y' + 3y = 26 \sin(2x)


$$

has the complementary solution $y_c = Ae^{-3x},$ solve the initial value problem.

#### Explanation

To find the general solution of an inhomogeneous first-order linear equation with constant coefficients on the left-hand side, we must find the sum of the complementary and particular solutions.

To find the complementary solution $y_c$ we solve the corresponding homogeneous equation, given by

$$


y_c' + 3y_c = 0.


$$

Solving this equation, we find that the complementary solution is

$$


y_c = Ae^{-3x}


$$

where $A$ is an arbitrary constant.

We now need to find the particular solution $y_p(x).$

The right-hand side of the inhomogeneous equation is $26 \sin(2x).$ So, we assume the particular solution to be

$$


y_p(x) = \alpha \cos(2x) + \beta \sin(2x).


$$

where $\alpha$ and $\beta$ are constants to be determined.

Calculating the first derivative of $y_p$ gives

$$


y_p' = - 2\alpha \sin(2x) + 2\beta \cos(2x)


$$

To find the values of $\alpha,$ and $\beta,$ we substitute $y_p$ and $y_p'$ into the differential equation:

$$


( - 2\alpha \sin(2x) + 2\beta \cos(2x)) + 3 (\alpha \cos(2x)+ \beta \sin(2x)) = 26 \sin(2x)


$$

Grouping the terms on the left-hand side gives

$$


(2\beta+3\alpha)\cos(2x) + (-2\alpha +3 \beta) \sin(2x) = 26 \sin(2x).


$$

Equating the coefficients, we get the following system of equations:

$$


\begin{aligned}\begin{aligned}2𝛽+3𝛼=0\, & (equating the coefficients of\,cos⁡(2𝑥)) \\ −2𝛼+3𝛽=26\, & (equating the coefficients of\,sin⁡(2𝑥))\end{aligned}\end{aligned}


$$

Solving this system gives $\alpha=-4, \beta=6.$

Therefore, the particular solution $y_p(x)$ is

$$


y_p(x) = - 4\cos(2x) + 6\sin(2x).


$$

The general solution is given by

$$


y(x) = y_c(x)+y_p(x),


$$

and therefore, the general solution in our case is

$$


y = Ae^{-3x} - 4\cos(2x) + 6\sin(2x).


$$

Now, we can find the constant $A$ using the initial conditions.

Substituting $y(0) =1$ into the general solution gives

$$


\begin{aligned}𝐴𝑒^{−3⋅0}−4cos⁡(2⋅0)+6sin⁡(2⋅0) & =1 \\ 𝐴−4+0 & =1 \\ 𝐴 & =5.\end{aligned}


$$

Therefore, the solution to the initial value problem is

$$


y = 5e^{-3x} - 4\cos(2x) + 6\sin(2x).


$$
