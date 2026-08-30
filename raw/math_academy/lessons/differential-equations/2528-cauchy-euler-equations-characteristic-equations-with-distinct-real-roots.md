# Cauchy-Euler Equations: Characteristic Equations With Distinct Real Roots

Source: https://www.mathacademy.com/topics/2528?courseId=61
Topic ID: 2528

## Prerequisites

- [Second-Order Homogeneous ODEs: Characteristic Equations With Distinct Real Roots](./614-second-order-homogeneous-odes-characteristic-equations-with-distinct-real-roots.md)

## Lesson

### Introduction

The second-order Cauchy-Euler equation has the form

$$


ax^2y''+bxy'+cy=f(x),


$$

where $a,b,$ and $c$ are constants.

Cauchy-Euler equations can be solved using a trial solution $y=x^\lambda,$ where $\lambda$ is a constant to be found. To illustrate, let's solve the following Cauchy-Euler equation:

$$


x^2y''+xy'-9y=0


$$

Differentiating the trial solution $y = x^\lambda$ with respect to $x$ gives

$$


y' = \lambda x^{\lambda -1}, \qquad y'' = \lambda(\lambda-1)x^{\lambda-2}.


$$

Substituting the above to our differential equation gives

$$


\begin{aligned}𝑥^{2}𝜆(𝜆−1)𝑥^{𝜆−2}+𝑥𝜆𝑥^{𝜆−1}−9𝑥^{𝜆} & =0 \\ 𝜆(𝜆−1)𝑥^{𝜆}+𝜆𝑥^{𝜆}−9𝑥^{𝜆} & =0 \\ 𝑥^{𝜆}(𝜆(𝜆−1)+𝜆−9) & =0.\end{aligned}


$$

So, we have the following characteristic equation:

$$


\begin{aligned}𝜆(𝜆−1)+𝜆−9 & =0 \\ 𝜆^{2}−9 & =0 \\ 𝜆 & =±3\end{aligned}


$$

Therefore, the general solution is

$$


\begin{aligned}𝑦(𝑥) & =𝑐_{1}𝑥^{3}+𝑐_{2}𝑥^{−3} \\ & =𝑐_{1}𝑥^{3}+\frac{𝑐_{2}}{𝑥^{3}}.\end{aligned}


$$

### Example: Identifying Instances of the Cauchy-Euler Equation

#### Question

Which of the following equations is an instance of the Cauchy-Euler equation?

1. $-2x^2y''+6xy'-5y=0$

2. $xy''+2y'-3xy=0$

3. $y''-3x^2y=\sqrt{x}$

#### Explanation

The second-order Cauchy-Euler equation has the form

$$


ax^2y''+bxy'+cy=f(x),


$$

where $a,b,$ and $c$ are constants. With that in mind, let's inspect each of the given equations.

- Equation I is a Cauchy-Euler equation with $a=-2,$ $b=6,$ $c=-5,$ and $f(x)=0.$

- Equation II is ** a Cauchy-Euler equation because the $y''$ is not multiplied by an $x^2.$ Instead, it is multiplied by an $x.$

- Equation III is ** a Cauchy-Euler equation because the $y''$ term is not multiplied by an $x^2.$

Therefore, the correct answer is "I only".

### Example: Solving an Instance of the Cauchy-Euler Equation

#### Question

Find the general solution to the equation

$$


3t^2 y''+8ty' -2y = 0, \quad t\gt 0.


$$

#### Explanation

This is an instance of the Cauchy-Euler equation. So, we assume the solutions take the form $y=t^\lambda.$ Differentiating $y$ with respect to $t$ gives

$$


y' = \lambda t^{\lambda -1}, \qquad y'' = \lambda(\lambda-1)t^{\lambda-2}.


$$

Substituting the above into our differential equation gives

$$


\begin{aligned}3𝑡^{2}⋅𝜆(𝜆−1)𝑡^{𝜆−2}+8𝑡⋅𝜆𝑡^{𝜆−1}−2𝑡^{𝜆} & =0 \\ 3𝜆(𝜆−1)𝑡^{𝜆}+8𝜆𝑡^{𝜆}−2𝑡^{𝜆} & =0 \\ 𝑡^{𝜆}[3𝜆(𝜆−1)+8𝜆−2] & =0.\end{aligned}


$$

So, we have the following characteristic equation:

$$


\begin{aligned}3𝜆(𝜆−1)+8𝜆−2 & =0 \\ 3𝜆^{2}+5𝜆−2 & =0 \\ (𝜆+2)(3𝜆−1) & =0\end{aligned}


$$

The roots of the characteristic equation are $\lambda = -2$ and $\lambda = \dfrac{1}{3}.$ Therefore, the general solution is

$$


\begin{aligned}𝑦(𝑡) & =𝑐_{1}𝑡^{−2}+𝑐_{2}𝑡^{1/3} \\ & =\frac{𝑐_{1}}{𝑡^{2}}+𝑐_{2}𝑡^{1/3}.\end{aligned}


$$

### Example: Solving an Initial Value Problem Involving a Cauchy-Euler Equation

#### Question

Given that the differential equation

$$


x^2 y'' +2 xy' -6 y= 0


$$

has the general solution

$$


y=\dfrac{c_1}{x^3}+ c_2x^{2},


$$

find the solution to the initial value problem

$$


x^2 y'' +2 xy' -6 y= 0, \quad y(1)= 0, \quad y'(1) = 5, \quad x \gt 0.


$$

#### Explanation

We find the constants $c_1$ and $c_2$ using the initial conditions.

- First, we apply the condition $y(1)=0.$ Substituting $y(1)= 0$ into the general solution gives

- Then, we apply the condition $y'(1) = 5.$ Differentiating $y,$ we get Substituting $y'(1)=5$ and $c_2=-c_1$ into the above gives

Therefore, the solution to the initial value problem is

$$


y(x)=x^{2}-\dfrac{1}{x^3}.


$$
