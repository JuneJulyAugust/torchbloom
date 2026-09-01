# Solving First-Order IVPs Using Separation of Variables

Source: https://www.mathacademy.com/topics/1179?courseId=154
Topic ID: 1179

## Prerequisites

- [Solving First-Order ODEs Using Separation of Variables](./466-solving-first-order-odes-using-separation-of-variables.md)

## Lesson

### Introduction

Suppose we want to find a solution to the differential equation

$$


y' = (1-2x)y^2 \,,


$$

satisfying the additional condition $y(0)=1.$ This additional condition $y(0)=1$ is called an **initial condition** or sometimes a **boundary condition** of the differential equation.

First of all, we note that the given differential equation is separable, so we can separate variables and integrate both sides with respect to $x\mathbin{:}$

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =(1−2𝑥)𝑦^{2} \\ \frac{1}{𝑦^{2}}⋅\frac{d𝑦}{d𝑥} & =1−2𝑥 \\ ∫\frac{1}{𝑦^{2}}⋅\frac{d𝑦}{d𝑥}\,d𝑥 & =∫(1−2𝑥)\,d𝑥 \\ ∫\frac{d𝑦}{𝑦^{2}}\, & =∫(1−2𝑥)\,d𝑥 \\ −\frac{1}{𝑦} & =𝑥−𝑥^{2}+𝐶 \\ \frac{1}{𝑦} & =𝑥^{2}−𝑥−𝐶 \\ 𝑦 & =\frac{1}{𝑥^{2}−𝑥−𝐶}\,.\end{aligned}


$$

We conclude that the general solution is

$$


y = \dfrac {1} {x^2 - x - C} \,,


$$

where $C$ is an arbitrary constant.

Now we choose the constant $C$ such that the condition $y(0)=1$ is satisfied. Substituting $x=0$ and $y=1$ into the general solution and solving for $C,$ we get

$$


\begin{aligned}𝑦(0)=\frac{1}{0−0−𝐶}=1\,⇒\,𝐶=−1\,.\end{aligned}


$$

Therefore, the particular solution of $y' = (1-2x)y^2$ that satisfies the condition $y(0)=1$ is

$$


y = \dfrac {1} {x^2 - x - (-1)} = \dfrac {1} {x^2 - x + 1}\,.


$$

To recap: the solution of a first-order separable ordinary differential equation (ODE) with an initial condition is obtained by

1. separating the variables,

2. integrating the equation, and then

3. substituting the condition into the solution to solve for the constant of integration.

### Example: Finding Particular Solutions of Differential Equations by Separating the Variables

#### Question

Find the particular solution to the differential equation $y' = 5y$ that satisfies $y(0)=3.$

#### Explanation

We first find the general solution, and then apply the given initial condition to find a particular solution.

Separating variables and integrating both sides with respect to $x,$ we get

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =5𝑦 \\ \frac{1}{𝑦}\frac{d𝑦}{d𝑥} & =5 \\ ∫\frac{1}{𝑦}\frac{d𝑦}{d𝑥}\,d𝑥 & =5∫\,d𝑥 \\ ∫\frac{1}{𝑦}\,d𝑦 & =5∫\,d𝑥 \\ ln⁡|𝑦| & =5𝑥+𝐶\,.\end{aligned}


$$

Applying the exponential function to both sides, we find the general solution:

$$


\begin{aligned}𝑦 & =±𝑒^{5𝑥+𝐶} \\ & =±𝑒^{𝐶}𝑒^{5𝑥} \\ & =𝐾𝑒^{5𝑥}\,,\end{aligned}


$$

where $K=\pm e^{C}$ is an arbitrary constant.

Now we apply the condition $y(0) = 3$ to find $K\mathbin{:}$

$$


\begin{aligned}𝑦(0) & =3 \\ 𝐾𝑒^{5⋅0} & =3 \\ 𝐾 & =3\,.\end{aligned}


$$

Thus the particular solution of $y' = 5y$ that satisfies the condition $y(0)=3$ is

$$


y = 3 e^{5x} \,.


$$

### Example: Finding Particular Solutions of Differential Equations by First Rearranging and Then Separating

#### Question

Find the particular solution to the differential equation $\cos(3y)\dfrac {\text{d}y} {\text{d}x} + \sin(2x) = 0$ given that $y\left(\dfrac{\pi}{4}\right) = 0.$ Assume that $-\dfrac{\pi}{6} < y < \dfrac{\pi}{6}.$

#### Explanation

We first find the general solution, and then apply the given initial condition to find a particular solution.

Separating variables and integrating both sides with respect to $x,$ we get

$$


\begin{aligned}cos⁡(3𝑦)\frac{d𝑦}{d𝑥} & =−sin⁡(2𝑥) \\ ∫cos⁡(3𝑦)\frac{d𝑦}{d𝑥}\,d𝑥 & =−∫sin⁡(2𝑥)\,d𝑥 \\ ∫cos⁡(3𝑦)\,d𝑦 & =−∫sin⁡(2𝑥)\,d𝑥 \\ \frac{1}{3}sin⁡(3𝑦) & =\frac{1}{2}cos⁡(2𝑥)+𝐶 \\ sin⁡(3𝑦) & =\frac{3}{2}cos⁡(2𝑥)+𝐶_{1}\,,\end{aligned}


$$

where $C_1=3C.$

Now let's apply the condition $y\left(\dfrac{\pi}{4}\right) = 0$ to find $C_1\mathbin{:}$

$$


\begin{aligned}𝑦(\frac{𝜋}{4}) & =0 \\ sin⁡(3⋅0) & =\frac{3}{2}cos⁡(2⋅\frac{𝜋}{4})+𝐶_{1} \\ sin⁡(0) & =\frac{3}{2}cos⁡(\frac{𝜋}{2})+𝐶_{1} \\ 0 & =0+𝐶_{1} \\ 𝐶_{1} & =0\end{aligned}


$$

So we get the particular solution in implicit form:

$$


\sin(3y) = \dfrac {3} {2} \cos(2x)


$$
