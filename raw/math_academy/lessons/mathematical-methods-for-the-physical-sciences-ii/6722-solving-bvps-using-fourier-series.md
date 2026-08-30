# Solving BVPs Using Fourier Series

Source: https://www.mathacademy.com/topics/6722?courseId=155
Topic ID: 6722

## Prerequisites

- [Introduction to Boundary Value Problems](./2742-introduction-to-boundary-value-problems.md)
- [Solving IVPs Using Fourier Series](./6721-solving-ivps-using-fourier-series.md)

## Lesson

### Introduction

In this topic, we will use Fourier series to solve boundary value problems with periodic forcing functions.

As before, we consider a second-order linear differential equation with constant coefficients and forcing function $f(x)$, for which the general solution can be written as

$$


y=y_c+y_p,


$$

where $y_c$ solves the homogeneous equation and $y_p$ is a particular solution.

The main ideas are similar to those of solving IVPs:

- we choose the correct form of the series for the particular solution $y_p$, and then

- use boundary conditions at the endpoints to determine the constants in the homogeneous part $y_c$ of the solution.

When $f(x)$ is periodic, we often look for $y_p$ as a Fourier series on a symmetric interval $[-L,L].$

Recall that for an equation of the form $y''+\omega^2 y=f(x)$ with no (damping) $y'$ term, the particular solution inherits the parity of $f(x)$:

- If $f$ is *even*, then its Fourier series contains only cosine terms.

- If $f$ is *odd*, then its Fourier series contains only sine terms.

For example, consider the boundary value problem

$$


y''+5y=f(x)


$$

on $[-2,2]$, where $f$ is $4$-periodic and odd. We want the appropriate Fourier series form for a particular solution $y_p$.

Because $f$ is $4$-periodic on $[-2,2]$, we have $L=2$, so the Fourier basis on this interval is

$$


\cos\left(\dfrac{n\pi x}{2}\right) \qquad\text{and}\qquad \sin\left(\dfrac{n\pi x}{2}\right).


$$

Next, since $f$ is odd, its Fourier series contains only sine terms. Since the equation has no $y'$ term, the particular solution inherits the same parity and is also odd.

Therefore, the appropriate form for $y_p$ is a sine series:

$$


y_p(x)=\sum_{n=1}^{\infty} b_n\sin\left(\dfrac{n\pi x}{2}\right).


$$

Let's see more examples.

### Example: Identifying the Form of the Fourier Series For the Solution

#### Question

Consider the boundary value problem

$$


y''+8y=f(x)


$$

on $[-3,3]$, where $f$ is $6$-periodic and even. What Fourier-series form is appropriate for a particular solution $y_p?$

#### Explanation

Because $f$ is $6$-periodic on $[-3,3]$, we have $L=3$, so Fourier series on this interval use the basis

$$


\cos\left(\dfrac{n\pi x}{3}\right) \qquad\text{and}\qquad \sin\left(\dfrac{n\pi x}{3}\right).


$$

Next, since $f$ is even, its Fourier series contains only cosine terms. For a second-order equation with no $y'$ (damping) term, the particular solution inherits this property and is also an even function.

Therefore, the appropriate form for $y_p$ is a cosine series:

$$


y_p(x)=\sum_{n=0}^{\infty} a_n\cos\left(\dfrac{n\pi x}{3}\right)


$$

### Using Boundary Conditions

Recall that we are considering a second-order linear differential equation with constant coefficients and forcing function $f(x)$, for which the general solution can be written as

$$


y=y_c+y_p,


$$

where $y_c$ solves the homogeneous equation and $y_p$ is a particular solution.

There are many types of boundary conditions (including mixed or Robin-type conditions), but in this lesson, we will focus on the two simplest cases:

- *Dirichlet conditions* (values of $y$ are specified):

- *Neumann conditions* (values of $y'$ are specified):

A key simplification is possible if we choose our particular solution $y_p$ to satisfy the corresponding *homogeneous* boundary conditions. For any given $f(x),$ it is always possible to find such a $y_p$. This drastically simplifies the computations, as the boundary conditions then determine the constants in $y_c$ directly.

- *Dirichlet-type simplification:* If we choose the forcing so that then so we can solve for the constants in $y_c$ using only the homogeneous solution.

- *Neumann-type simplification:* If we choose the forcing so that then so the derivative conditions determine the constants in $y_c$ directly.

Let's see how this works in practice.

### Example: Solving BVPs Using Fourier Series

#### Question

Consider the boundary value problem

$$


y''+2y=f(x), \qquad y'(0)=0,\quad y'(1)=-5


$$

where $f(x)$ is $2$-periodic and even. Fill in the missing part in the solution of the BVP, where the infinite sum on the right-hand side below represents a particular solution $y_p$ of the differential equation.

**

$$


\frac{1}{𝑥𝑥𝑥}?\frac{1}{𝑥𝑥𝑥}


$$

#### Explanation

We write the solution as $y=y_c+y_p$, where $y_c$ solves the homogeneous equation and $y_p$ is a particular solution.

First, solve the homogeneous equation $y''+2y=0.$ Its general solution is

$$


y_c(x)=A\cos(\sqrt{2}x)+B\sin(\sqrt{2}x).


$$

Computing the derivative, we get

$$


y'(x)=-A\sqrt{2}\sin(\sqrt{2}x)+B\sqrt{2}\cos(\sqrt{2}x)+y_p'(x).


$$

Now, we use the hint. Since $y_p'(0)=0$ and $y_p'(1)=0$, we have

$$


y'(0)=y_c'(0)\qquad\text{and}\qquad y'(1)=y_c'(1).


$$

Next, we apply the boundary conditions.

- Use $y'(0)=0{:}$ So, $y_c(x)=A\cos(\sqrt{2}x).$

- Use $y'(1)=-5$ with $B=0{:}$

Therefore, the solution is

$$


y(x)\sim \boxed{\dfrac{5}{\sqrt{2}\sin(\sqrt{2})}\cos(\sqrt{2}x)} +\sum_{n=0}^\infty a_n\cos(n\pi x).


$$
