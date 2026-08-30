# General Solutions of Linear ODEs

Source: https://www.mathacademy.com/topics/2740?courseId=154
Topic ID: 2740

## Prerequisites

- [Reduction of Order](./1925-reduction-of-order.md)
- [Linear Independence of Solutions to Homogeneous ODEs](./2547-linear-independence-of-solutions-to-homogeneous-odes.md)
- [The Superposition Principle](./2549-the-superposition-principle.md)
- [General Solutions of First-Order Linear ODEs](./6678-general-solutions-of-first-order-linear-odes.md)

## Lesson

### Introduction

Consider the second-order linear homogeneous differential equation

$$


y'' - 5y' + 6y = 0.


$$

It can be shown that a fundamental set of solutions is given by

$$


y_1(x) = e^{3x}, \qquad y_2(x) = e^{2x}.


$$

The superposition principle tells us that any linear combination of solutions to a linear, homogeneous differential equation is also a solution to the equation. Therefore, the **general solution** to this differential equation is

$$


y(x) = Ae^{3x} + Be^{2x}


$$

where $A$ and $B$ are **arbitrary constants.**

In general, if an $n$th order homogeneous, linear ODE has a fundamental set of solutions given by

$$


y_1(x), \quad y_2(x),\quad \ldots, \quad y_n(x),


$$

then the general solution to the equation is

$$


\boxed{y(x) = C_1y_1(x)+C_2y_2(x)+\cdots+C_ny_n(x)}


$$

for arbitrary constants $C_1, C_2,\ldots C_n.$

**Note:** Using sigma notation, we can write the general solution more compactly as

$$


y(x) = \sum_{i=1}^n C_i y_i(x).


$$

### Example: Identifying True Statements About General Solutions of Second-Order Linear ODEs

#### Question

Consider the differential equation $y'' - 3y'+ 2y=0.$ Which of the following statements are true?

1. $y_1(x) = e^{x}$ is a solution to the equation.

2. $y_2(x) = e^{2x}$ is a solution to the equation.

3. The general solution of the equation is $y=Ae^{x} + Be^{2x}.$

#### Explanation

Let's check each statement.

- To determine whether $y_1(x)$ is a solution to the differential equation, we substitute $y_1$ and its derivatives into the equation. Computing the first and second derivatives, we get and substituting into the equation, we get So $y_1$ is a solution to the equation, and therefore statement I is true.

- Similarly, we compute the derivatives of $y_2$ and substitute to the equation. Computing the derivatives, we get and substituting into the equation, we get So $y_2$ is a solution to the equation, and therefore statement II is true.

- Both $y_1=e^x$ and $y_2=e^{2x}$ are solutions of the equation. So, the general solution is $y=Ae^{x} + Be^{2x}$ if $y_1$ and $y_2$ are linearly independent. To check if they are linearly independent, we compute the Wronskian: Since the Wronskian does not equal $0,$ the functions are linearly independent. Therefore, statement III is true.

In conclusion, the correct statements are I, II, and III.

### Example: Finding General Solutions to Second-Order Homogeneous ODEs Using Reduction of Order

#### Question

Given that $y_1(x) = e^{5x}$ is a solution to the equation $y'' - 10y' + 25y = 0,$ use reduction of order to find a second solution $y_2(x)$ to the equation, and write down the general solution.

#### Explanation

According to the reduction of order method, we let $y_{2}=u(x) e^{5x}.$

Differentiating the above with respect to $x$ gives

$$


\begin{aligned}𝑦_{′2}^{} & =𝑢^{′}𝑒^{5𝑥}+5𝑢𝑒^{5𝑥}=𝑒^{5𝑥}(𝑢^{′}+5𝑢) \\ 𝑦_{″2}^{} & =𝑒^{5𝑥}(𝑢^{″}+10𝑢^{′}+25𝑢).\end{aligned}


$$

Substituting the above into the differential equation gives

$$


\begin{aligned}𝑒^{5𝑥}(𝑢^{″}+10𝑢^{′}+25𝑢)−10𝑒^{5𝑥}(𝑢^{′}+5𝑢)+25𝑒^{5𝑥}𝑢 & =0 \\ 𝑒^{5𝑥}(𝑢^{″}+10𝑢^{′}+25𝑢−10𝑢^{′}−50𝑢+25𝑢) & =0 \\ 𝑒^{5𝑥}(𝑢^{″}) & =0.\end{aligned}


$$

Since $e^{5x}\neq 0$ we must have

$$


u'' = 0.


$$

Integrating the equation twice gives

$$


u(x) = c_1x+c_2.


$$

Therefore, our expression for $y_2(x) = ue^{5x}$ becomes

$$


y_2(x) = e^{5x}\left(c_1 x + c_2\right).


$$

Setting $c_1 = 1$ and $c_2 = 0,$ we get

$$


y_2(x) = e^{5x}\cdot x = xe^{5x}.


$$

Finally, because $W(y_1, y_2) = e^{10x} \neq 0,$ we know that $y_1$ and $y_2$ are independent (you should verify this calculation yourself).

Therefore, the general solution to the equation is

$$


y=Ae^{5x}+Bxe^{5x}.


$$

### Example: Finding General Solutions to Second-Order Homogeneous ODEs With Variable Coefficients

#### Question

Given that $y_1(x) = \dfrac{1}{x}$ is a solution to the equation $x^2 y'' + 3xy' + y = 0$ for $x>0,$ use reduction of order to find a second solution $y_2(x)$ to the equation, and write down the general solution.

#### Explanation

According to the reduction of order method, we let

$$


\begin{aligned}𝑦_{2}(𝑥) & =𝑢(𝑥)𝑦_{1}(𝑥) \\ & =𝑢(𝑥)⋅\frac{1}{𝑥} \\ & =\frac{𝑢(𝑥)}{𝑥}.\end{aligned}


$$

Differentiating $y_{2} = \dfrac{u(x)}{x}$ with respect to $x$ gives

$$


\begin{aligned}𝑦_{2} & =\frac{𝑢}{𝑥} \\ 𝑦_{′2}^{} & =\frac{𝑢^{′}𝑥−𝑢}{𝑥^{2}} \\ 𝑦_{″2}^{} & =\frac{𝑢^{″}𝑥^{2}−2𝑢^{′}𝑥+2𝑢}{𝑥^{3}}.\end{aligned}


$$

Substituting the above into the differential equation gives

$$


\begin{aligned}𝑥^{2}𝑦^{″}+3𝑥𝑦^{′}+𝑦 & =0 \\ 𝑥^{2}(\frac{𝑢^{″}𝑥^{2}−2𝑢^{′}𝑥+2𝑢}{𝑥^{3}})+3𝑥(\frac{𝑢^{′}𝑥−𝑢}{𝑥^{2}})+\frac{𝑢}{𝑥} & =0 \\ \frac{𝑢^{″}𝑥^{2}−2𝑢^{′}𝑥+2𝑢+3𝑢^{′}𝑥−3𝑢+𝑢}{𝑥} & =0 \\ \frac{𝑢^{″}𝑥^{2}+𝑢^{′}𝑥}{𝑥} & =0 \\ 𝑢^{″}𝑥+𝑢^{′} & =0.\end{aligned}


$$

Now, let $w = u'.$ Then our equation becomes a first-order equation:

$$


w' x + w = 0


$$

This is a separable equation that has the solution

$$


w = \dfrac{c_1}{x}.


$$

Since $w = u',$ we have

$$


u' = \dfrac{c_1}{x} \quad\Longrightarrow\quad u = c_1\ln{x} + c_2.


$$

Therefore, our expression for $y_2(x) = \dfrac{u}{x}$ becomes

$$


y_2(x) = \dfrac{c_1\ln{x} + c_2}{x}.


$$

Setting $c_1 = 1$ and $c_2 = 0,$ we get

$$


y_2(x) = \dfrac{\ln{x}}{x}.


$$

Finally, because $W(y_1, y_2) = \dfrac{1}{x^3} \neq 0,$ we know that $y_1$ and $y_2$ are independent (you should verify this calculation yourself).

Therefore, the general solution is

$$


y = \dfrac{A}{x} + \dfrac{B\ln{x}}{x} = \dfrac{A + B\ln{x}}{x}.


$$

### General Solutions of Inhomogeneous ODEs

Similar to first-order linear ODEs, for inhomogeneous differential equations, the **general solution** is given by

$$


y(x) = y_c(x) + y_p(x),


$$

where

- $y_c(x)$ is the **complementary solution** (the general solution of the corresponding homogeneous equation), and

- $y_p(x)$ is a **particular solution** of the original inhomogeneous equation.

We will apply this structure to a specific differential equation in the next slide.

### Example: Constructing General Solutions of Inhomogeneous ODEs

#### Question

Consider the differential equation below, for which the corresponding complementary solution is $y_c(x)=Ax^6+Bx^2,$ where $A$ and $B$ are arbitrary constants.

$$


x^2y'' - 7xy' + 12y = -3x^3


$$

Determine whether $y_p(x)=x$ or $y_p(x)=x^3$ is a particular solution of the differential equation, and then write the general solution.

#### Explanation

For an inhomogeneous differential equation, the general solution is given by

$$


y(x) = y_c(x) + y_p(x),


$$

where

- $y_c(x)$ is the complementary solution (the general solution of the corresponding homogeneous equation), and

- $y_p(x)$ is a particular solution of the original inhomogeneous equation.

With this in mind, let's check which of the two given functions is a particular solution of our inhomogeneous equation:

- For $y_p(x)=x,$ we have Substituting this into the equation, we have So, $y_p(x)=x$ isn't a particular solution of the differential equation.

- For $y_p(x)=x^3,$ we have Substituting this into the equation, we have So, $y_p(x)=x^3$ is a particular solution of the differential equation.

We are told that the complementary solution of our equation is $y_c(x)=Ax^6+Bx^2.$ Therefore, the general solution is

$$


\begin{aligned}𝑦(𝑥) & =𝑦_{𝑐}(𝑥)+𝑦_{𝑝}(𝑥) \\ & =𝐴𝑥^{6}+𝐵𝑥^{2}+𝑥^{3}\end{aligned}


$$

where $A$ and $B$ are arbitrary constants.
