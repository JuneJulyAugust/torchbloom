# Solving First-Order Linear ODEs With Exponential Forcing

Source: https://www.mathacademy.com/topics/6679?courseId=154
Topic ID: 6679

## Prerequisites

- [General Solutions of First-Order Linear ODEs](./6678-general-solutions-of-first-order-linear-odes.md)

## Lesson

### Introduction

Consider the first-order inhomogeneous ODE with constant coefficients given by

$$


ay' + by = f(x),


$$

where $a$ and $b$ are constants.

As we know, the method of finding the general solution is to find the sum of the complementary solution $y_c(x)$ and a particular solution $y_p(x).$

$$


y(x) = y_c(x) + y_p(x)


$$

To find the particular solution $y_p(x),$ we examine the functional form of the forcing term $f(x)$ and guess a form for $y_p(x)$ that matches it.

An ODE exhibits **exponential forcing** if the forcing term $f(x)$ is an exponential function

$$


f(x) = Ke^{k x},


$$

where $K$ is a constant.

Provided that the forcing function $e^{kx}$ is not a term in the complementary solution, our trial guess for the particular solution is an exponential function with the same exponent. That is

$$


y_p(x) = \alpha\,e^{k x},


$$

where $\alpha$ is a constant to be determined.

In this lesson, we focus on solving first-order inhomogeneous ODEs with **exponential forcing**. Let's look at a concrete example.

### A Worked Example

Consider the differential equation

$$


\frac {\text{d} y} {\text{d} x} + 3 y = 4 e ^ {2x}.


$$

The associated homogeneous equation is

$$


\frac {\text{d} y} {\text{d} x} + 3 y = 0


$$

and therefore, the complementary solution is

$$


y_c(x) = A e^{-3x},


$$

where $A$ is an arbitrary constant. Let's now find the **particular solution** $y_p(x)$ to this equation.

Since the right-hand side of the inhomogeneous equation is the exponential function $f(x) = 4 e^{2x},$ and this is not incorporated within the complementary solution, we assume a particular solution of the form

$$


y_p(x) = \alpha e^{2x},


$$

where $\alpha$ is a constant to be determined.

Calculating the first derivative of $y_p$ gives

$$


\frac{\text{d}y_p}{\text{d}x} = 2\alpha e ^{2x}.


$$

To find the value of $\alpha,$ we substitute $y_p$ and $y_p'$ into the differential equation and solve for $\alpha{:}$

$$


\begin{aligned}(2𝛼𝑒^{2𝑥})+3(𝛼𝑒^{2𝑥}) & =4𝑒^{2𝑥} \\ (2+3)𝛼𝑒^{2𝑥} & =4𝑒^{2𝑥} \\ 5𝛼𝑒^{2𝑥} & =4𝑒^{2𝑥} \\ 𝛼 & =\frac{4}{5}\end{aligned}


$$

Therefore, the particular solution $y_p(x)$ is

$$


y_p(x) = \dfrac{4}{5} e ^{2x}.


$$

Finally, the **general solution** is given by

$$


y = y_c + y_p = A e^{-3x} + \dfrac{4}{5} e ^{2x}.


$$

We can employ a similar strategy when the forcing function is a sum of exponential functions. Let's see an example.

### Example: Finding a Particular Solution to a First-Order Inhomogeneous ODE With Exponential Forcing

#### Question

Given that the differential equation

$$


\frac {\textrm {d} y} {\textrm {d} x} - 2 y = e ^ {x} - 2 e^{3x}


$$

has the complementary solution $y_c(x) = A e ^ {2x}$, find the particular solution $y_p(x)$ to this equation.

#### Explanation

To find the general solution of an inhomogeneous first-order linear equation with constant coefficients on the left-hand side, we must find the sum of the complementary and particular solutions.

We see that the right-hand side is $e ^ {x} - 2 e^{3x},$ and neither $e^{x}$ nor $e^{3x}$ is a term in the complementary solution, so we assume a particular solution of the form

$$


y_p = \alpha e^{x} + \beta e^{3x},


$$

where $\alpha$ and $\beta$ are constants that are to be determined.

Calculating the first derivative of $y_p$ gives

$$


\frac{\text{d}y_p}{\text{d}x} = \alpha e^{x} + 3\beta e^{3x}.


$$

To find the values of $\alpha$ and $\beta,$ we substitute $y_p$ and $y_p'$ into the differential equation:

$$


\begin{aligned}(𝛼𝑒^{𝑥}+3𝛽𝑒^{3𝑥})−2(𝛼𝑒^{𝑥}+𝛽𝑒^{3𝑥}) & =𝑒^{𝑥}−2𝑒^{3𝑥} \\ (𝛼−2𝛼)𝑒^{𝑥}+(3𝛽−2𝛽)𝑒^{3𝑥} & =𝑒^{𝑥}−2𝑒^{3𝑥} \\ −𝛼𝑒^{𝑥}+𝛽𝑒^{3𝑥} & =𝑒^{𝑥}−2𝑒^{3𝑥}\end{aligned}


$$

Equating coefficients of $e^{x}$ and $e^{3x},$ respectively, gives

$$


-\alpha = 1, \quad \quad \beta = -2.


$$

So, we have

$$


\alpha = -1, \quad \quad \beta = -2.


$$

Therefore, the particular solution $y_p(x)$ is

$$


y_p(x) = - e ^{x} - 2 e^{3x}.


$$

### Cases When the Forcing Term is Part of the Complementary Solution

So far, our guesses for the particular solution have worked because the forcing term did not already appear in the complementary solution.

Sometimes, however, the right-hand side of the differential equation has the same form as a term that appears in the complementary solution $y_c(x).$ When this happens, our usual guess for $y_p(x)$ fails because it duplicates part of the complementary solution and cannot produce a new solution.

In this situation, we must modify our guess by *multiplying it by $x.$* Specifically, if the forcing term has the form $K e^{kx}$ and the complementary solution contains a term like $Ae^{kx},$ then instead of guessing

$$


y_p(x) = \alpha e^{kx},


$$

we try

$$


y_p(x) = \alpha \boldsymbol{x} e^{kx}.


$$

This works because multiplying by $x$ creates a new function that is *linearly independent* of the complementary solution. As a result, our guess no longer overlaps with $y_c(x)$ and can serve as a valid particular solution. We'll discuss linear independence of functions in more detail in future lessons.

Let’s see how this works in practice using a concrete example.

### A Worked Example

Consider the differential equation

$$


y' + 5y = 10e^{-5x}.


$$

The associated homogeneous equation is

$$


y' + 5y = 0


$$

and so the complementary solution is

$$


y_c(x) = Ae^{-5x},


$$

where $A$ is an arbitrary constant.

Notice that the forcing term is $f(x) = 10 e^{-5x},$ and yet $e^{-5x}$ is a term in the complementary solution. So, in this case, we assume a particular solution that takes the form

$$


y_p(x) = \alpha x e ^ {-5 x} ,


$$

where $\alpha$ is a constant to be determined.

We calculate the first derivative of $y_p$ using the product rule for differentiation:

$$


\begin{aligned}𝑦_{′𝑝} & =(𝛼𝑥𝑒^{−5𝑥})^{′} \\ & =𝛼(𝑥𝑒^{−5𝑥})^{′} \\ & =𝛼(𝑒^{−5𝑥}−5𝑥𝑒^{−5𝑥}) \\ & =𝛼(1−5𝑥)𝑒^{−5𝑥}\end{aligned}


$$

To find the value of $\alpha,$ we substitute $y_p$ and $y_p'$ into the differential equation and solve for $\alpha.$

$$


\begin{aligned}(𝛼(1−5𝑥)𝑒^{−5𝑥})+5𝛼𝑥𝑒^{−5𝑥} & =10𝑒^{−5𝑥} \\ (1−5𝑥+5𝑥)𝛼𝑒^{−5𝑥} & =10𝑒^{−5𝑥} \\ 𝛼𝑒^{−5𝑥} & =10𝑒^{−5𝑥} \\ 𝛼 & =10\end{aligned}


$$

Therefore, the particular solution $y_p(x)$ is

$$


y_p(x) = 10x e ^ {-5x}


$$

and thus the general solution to the equation is

$$


y(x) = y_c(x) + y_p(x) = Ae^{-5x} + 10xe^{-5x}.


$$

### Example: Finding a Particular Solution When the Forcing Term is Part of the Complementary Solution

#### Question

Given that the differential equation

$$


y' + 5y = 15e^{-5x} + 12e^{x},


$$

has the complementary solution $y_c(x) = Ae^{-5x}$, find the particular solution to the equation.

#### Explanation

To find the general solution of an inhomogeneous first-order linear equation with constant coefficients on the left-hand side, we must find the sum of the complementary and particular solutions.

We see that the right-hand side is $15 e^{-5x} + 12 e^{x},$ and $e^{-5x}$ is a term in the complementary solution, while $e^{x}$ is not, so we assume that a particular solution takes the form

$$


y_p = \alpha x e ^ {-5 x} + \beta e^{x},


$$

where $\alpha$ and $\beta$ are constants that are to be determined.

Calculating the first derivative of $y_p$ gives

$$


\begin{aligned}𝑦_{′𝑝} & =(𝛼𝑥𝑒^{−5𝑥}+𝛽𝑒^{𝑥})^{′} \\ & =𝛼(𝑥𝑒^{−5𝑥})^{′}+𝛽(𝑒^{𝑥})^{′} \\ & =𝛼(𝑒^{−5𝑥}−5𝑥𝑒^{−5𝑥})+𝛽𝑒^{𝑥} \\ & =𝛼(1−5𝑥)𝑒^{−5𝑥}+𝛽𝑒^{𝑥}.\end{aligned}


$$

To find the values of $\alpha$ and $\beta,$ we substitute $y_p$ and $y_p'$ into the differential equation:

$$


\begin{aligned}(𝛼(1−5𝑥)𝑒^{−5𝑥}+𝛽𝑒^{𝑥})+5(𝛼𝑥𝑒^{−5𝑥}+𝛽𝑒^{𝑥}) & =15𝑒^{−5𝑥}+12𝑒^{𝑥} \\ (1−5𝑥+5𝑥)𝛼𝑒^{−5𝑥}+(𝛽+5𝛽)𝑒^{𝑥} & =15𝑒^{−5𝑥}+12𝑒^{𝑥} \\ 𝛼𝑒^{−5𝑥}+6𝛽𝑒^{𝑥} & =15𝑒^{−5𝑥}+12𝑒^{𝑥}.\end{aligned}


$$

Equating coefficients of $e^{-5x}$ and $e^{x}$ gives

$$


\alpha = 15 \quad \text{and} \quad 6\beta = 12,


$$

so, we have

$$


\alpha = 15 \quad \text{and} \quad \beta = 2.


$$

Therefore, the particular solution $y_p(x)$ is

$$


y_p(x) = 15x e ^ {-5x} + 2 e^{x}.


$$

### Example: Finding the General Solution to a First-Order Inhomogeneous ODE With Exponential Forcing

#### Question

Consider the differential equation

$$


y' - 6 y = 9 e ^ {6 x}.


$$

Find the general solution to this equation given that the complementary solution is $y_c(x) = Ae^{6x},$ where $A$ is an arbitrary constant.

#### Explanation

To find the general solution of an inhomogeneous first-order linear equation with constant coefficients on the left-hand side, we must find the sum of the complementary and particular solutions.

To find the complementary solution $y_c,$ we solve the corresponding homogeneous equation, given by

$$


y_c' - 6 y_c=0.


$$

Solving this equation, we find that the complementary solution is

$$


y_c = A e^{6x}.


$$

where $A$ is an arbitrary constant.

We now need to find the particular solution $y_p(x).$

We see that the right-hand side is $9 e ^ {6 x},$ and $e^{6x}$ is a term in the complementary solution, so we assume that a particular solution takes the form

$$


y_p = \alpha x e ^ {6x} ,


$$

where $\alpha$ is a constant to be determined.

We calculate the first derivative of $y_p$ using the product rule for differentiation:

$$


\begin{aligned}𝑦_{′𝑝} & =(𝛼𝑥𝑒^{6𝑥})^{′} \\ & =𝛼(𝑥𝑒^{6𝑥})^{′} \\ & =𝛼(𝑒^{6𝑥}+6𝑥𝑒^{6𝑥}) \\ & =𝛼(1+6𝑥)𝑒^{6𝑥}\end{aligned}


$$

To find the value of $\alpha,$ we substitute $y_p$ and $y_p'$ into the differential equation:

$$


\begin{aligned}(𝛼(1+6𝑥)𝑒^{6𝑥})−6𝛼𝑥𝑒^{6𝑥} & =9𝑒^{6𝑥} \\ (1+6𝑥−6𝑥)𝛼𝑒^{6𝑥} & =9𝑒^{6𝑥} \\ 𝛼𝑒^{6𝑥} & =9𝑒^{6𝑥} \\ 𝛼 & =9\end{aligned}


$$

Therefore, the particular solution $y_p(x)$ is

$$


y_p(x) = 9x e ^ {6 x} .


$$

Now, since the general solution is given by

$$


y(x) = y_c(x)+y_p(x),


$$

the general solution in our case is

$$


y = Ae^{6x} + 9xe^{6x}.


$$

### Example: Solving an Initial Value Problem

#### Question

Consider the following initial value problem:

$$


y' - 2y = 4e^{3x}, \qquad y(0) = 1


$$

Given that the differential equation

$$


y' - 2y = 4e^{3x}


$$

has the complementary solution $y_c = Ae^{2x},$ solve the initial value problem.

#### Explanation

To find the general solution of an inhomogeneous first-order linear equation with constant coefficients on the left-hand side, we must find the sum of the complementary and particular solutions.

To find the complementary solution $y_c,$ we solve the corresponding homogeneous equation, given by

$$


y_c' - 2y_c = 0.


$$

Solving this equation, we find that the complementary solution is

$$


y_c = Ae^{2x}


$$

where $A$ is an arbitrary constant.

We now need to find the particular solution $y_p(x).$

We see that the right-hand side is $4e^{3x},$ and $e^{3x}$ is not a term in the complementary solution, so we assume a particular solution of the form

$$


y_p = \alpha e^{3x},


$$

where $\alpha$ is a constant to be determined.

Calculating the first derivative of $y_p$ gives

$$


y_p' = 3\alpha e ^{3x}.


$$

To find the value of $\alpha,$ we substitute $y_p$ and $y_p'$ into the differential equation:

$$


\begin{aligned}(3𝛼𝑒^{3𝑥})−2(𝛼𝑒^{3𝑥}) & =4𝑒^{3𝑥} \\ (3−2)𝛼𝑒^{3𝑥} & =4𝑒^{3𝑥} \\ 𝛼𝑒^{3𝑥} & =4𝑒^{3𝑥} \\ 𝛼 & =4.\end{aligned}


$$

Therefore, the particular solution $y_p(x)$ is

$$


y_p(x) = 4e^{3x}.


$$

Now, since the general solution is given by

$$


y(x) = y_c(x)+y_p(x),


$$

the general solution in our case is

$$


y = Ae^{2x} + 4e ^{3x}.


$$

We can find the constant $A$ using the initial conditions.

Substituting $y(0) =1$ into the general solution gives

$$


\begin{aligned}𝐴+4 & =1 \\ 𝐴 & =−3.\end{aligned}


$$

Therefore, the solution to the initial value problem is

$$


y = -3e^{2x} + 4e ^{3x}.


$$
