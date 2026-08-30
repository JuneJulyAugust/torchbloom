# Cauchy-Euler Equations: Characteristic Equations With Repeated Roots

Source: https://www.mathacademy.com/topics/2544?courseId=61
Topic ID: 2544

## Prerequisites

- [Second-Order Homogeneous ODEs: Characteristic Equations With Repeated Roots](./879-second-order-homogeneous-odes-characteristic-equations-with-repeated-roots.md)
- [Cauchy-Euler Equations: Characteristic Equations With Distinct Real Roots](./2528-cauchy-euler-equations-characteristic-equations-with-distinct-real-roots.md)

## Lesson

### Introduction

When the characteristic equation of a Cauchy-Euler equation has a repeated root $\lambda = c,$ the general solution is

$$


y(x) = c_1 x^c + c_2 x^c \ln x.


$$

To illustrate, let's solve the following Cauchy-Euler equation:

$$


x^2y''-xy'+y=0


$$

Differentiating the trial solution $y = x^\lambda$ with respect to $x$ gives

$$


y' = \lambda x^{\lambda -1}, \qquad y'' = \lambda(\lambda-1)x^{\lambda-2}.


$$

Substituting the above to our differential equation gives

$$


\begin{aligned}𝑥^{2}𝜆(𝜆−1)𝑥^{𝜆−2}−𝑥𝜆𝑥^{𝜆−1}+𝑥^{𝜆} & =0 \\ 𝜆(𝜆−1)𝑥^{𝜆}−𝜆𝑥^{𝜆}+𝑥^{𝜆} & =0 \\ 𝑥^{𝜆}(𝜆(𝜆−1)−𝜆+1) & =0.\end{aligned}


$$

So, we have the following characteristic equation:

$$


\begin{aligned}𝜆(𝜆−1)−𝜆+1 & =0 \\ 𝜆^{2}−2𝜆+1 & =0 \\ (𝜆−1)^{2} & =0\end{aligned}


$$

The characteristic equation has a double root $\lambda = 1.$ Therefore, the general solution is

$$


\begin{aligned}𝑦(𝑥) & =𝑐_{1}𝑥^{1}+𝑐_{2}𝑥^{1}ln⁡𝑥 \\ & =𝑐_{1}𝑥+𝑐_{2}𝑥ln⁡𝑥.\end{aligned}


$$

### Example: Solving a Cauchy-Euler Equation with a Repeated Root

#### Question

Find the general solution to the equation

$$


2x^2 y'' + 6 xy' + 2y = 0, \qquad x>0.


$$

#### Explanation

This is an instance of the Cauchy-Euler equation. So, we assume the solutions take the form $y=x^\lambda.$ Differentiating $y$ with respect to $x$ gives

$$


y' = \lambda x^{\lambda -1}, \qquad y'' = \lambda(\lambda-1)x^{\lambda-2}.


$$

Substituting the above to our differential equation gives

$$


\begin{aligned}2𝑥^{2}⋅𝜆(𝜆−1)𝑥^{𝜆−2}+6𝑥⋅𝜆𝑥^{𝜆−1}+2𝑥^{𝜆} & =0 \\ 2𝜆(𝜆−1)𝑥^{𝜆}+6𝜆𝑥^{𝜆}+2𝑥^{𝜆} & =0 \\ 𝑥^{𝜆}[2𝜆(𝜆−1)+6𝜆+2] & =0.\end{aligned}


$$

So, we have the following characteristic equation:

$$


\begin{aligned}2𝜆(𝜆−1)+6𝜆+2 & =0 \\ 2𝜆^{2}+4𝜆+2 & =0 \\ 2(𝜆^{2}+2𝜆+1) & =0 \\ 2(𝜆+1)^{2} & =0\end{aligned}


$$

The characteristic equation has a double root $\lambda = -1.$ Therefore, the general solution is

$$


\begin{aligned}𝑦(𝑥) & =𝑐_{1}𝑥^{−1}+𝑐_{2}𝑥^{−1}ln⁡𝑥 \\ & =\frac{𝑐_{1}}{𝑥}+\frac{𝑐_{2}ln⁡𝑥}{𝑥}.\end{aligned}


$$

### Example: Solving an Initial Value Problem Involving a Cauchy-Euler Equation with a Repeated Root

#### Question

Given that the differential equation

$$


x^2 y'' - 19 xy' + 100y = 0


$$

has the general solution

$$


y =c_1 x^{10}+ c_2x ^{10}\ln x ,


$$

solve the initial value problem

$$


x^2 y'' - 19 xy' + 100y = 0, \quad y(1) = 0,\quad y'(1)=1, \quad x>0.


$$

#### Explanation

We find the constants $c_1$ and $c_2$ using the initial conditions.

- First, we apply the condition $y(1)=0.$ Substituting $y(1)= 0$ into the general solution gives

- Then, we apply the condition $y'(1) = 1.$ Differentiating $y,$ we get

Substituting $y'(1)=1$ and $c_1 = 0$ into the above gives

$$


\begin{aligned}1 & =10𝑐_{1}+𝑐_{2} \\ 1 & =0+𝑐_{2} \\ 𝑐_{2} & =1.\end{aligned}


$$

Therefore, the solution to the initial value problem is

$$


y(x) = x ^{10}\ln x .


$$
