# Eigenvalues and Eigenfunctions of Homogeneous BVPs

Source: https://www.mathacademy.com/topics/3211?courseId=61
Topic ID: 3211

## Prerequisites

- [Second-Order Homogeneous ODEs: Characteristic Equations With Repeated Roots](./879-second-order-homogeneous-odes-characteristic-equations-with-repeated-roots.md)
- [General Solutions of Trigonometric Equations With Transformed Functions](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/1259-general-solutions-of-trigonometric-equations-with-transformed-functions.md)
- [Second-Order Homogeneous Boundary Value Problems](./6711-second-order-homogeneous-boundary-value-problems.md)

## Lesson

### Introduction

In a homogeneous boundary value problem (BVP) that depends on a parameter $\lambda$, most values of $\lambda$ lead only to the trivial solution $y\equiv 0$.

The special values of $\lambda$ that produce *nontrivial* solutions are called **eigenvalues**, and the corresponding nontrivial solutions are called **eigenfunctions**.

For example, consider the boundary value problem

$$


y'' - 18\lambda y' + 81\lambda^2y = 0, \quad y(0) = 0, \quad 4y(3) + 5y'(3) = 0, \quad 0 \leq x \leq 3, \quad \lambda \in\mathbb R.


$$

Let's find the eigenvalues and eigenfunctions of this problem.

The method for solving the differential equation depends on whether $\lambda = 0$ or $\lambda \neq 0.$ To find the eigenvalues, we must therefore investigate these two possibilities as separate cases.

On the next slide, we will analyze the case where $\lambda = 0.$

### Trivial Solution of the Eigenvalue Problem

We begin by considering the case $\lambda = 0.$

Setting $\lambda = 0$ in the original equation, $y'' - 18\lambda y' + 81\lambda^2y = 0,$ gives a much simpler equation:

$$


y'' = 0.


$$

Integrating this equation twice with respect to $x$ gives the general solution

$$


y = Ax + B.


$$

Now we apply the boundary conditions.

- The first condition, $y(0) = 0,$ implies: So the solution must be of the form $y = Ax.$

- For the second condition, we first find the derivative, $y' = A.$ Applying the condition $4y(3) + 5y'(3) = 0$ yields

Since both $A=0$ and $B=0,$ we are left with the trivial solution $y \equiv 0.$ By definition, an eigenfunction must be a *nontrivial* solution.

Therefore, $\lambda = 0$ is *not* an eigenvalue.

Next, we will check the case where $\lambda \neq 0.$

### Non-Trivial Solution of the Eigenvalue Problem

Next, we consider the case $\lambda \neq 0.$

To find the fundamental solutions of

$$


y'' - 18\lambda y' + 81\lambda^2y = 0,


$$

for $\lambda \neq 0,$ we set $y = e^{m x}.$ The auxiliary equation is

$$


\begin{aligned}𝑚^{2}−18𝜆𝑚+81𝜆^{2} & =0 \\ (𝑚−9𝜆)(𝑚−9𝜆) & =0.\end{aligned}


$$

This gives a repeated root $m = 9\lambda.$ The general solution is

$$


y = Ae^{9\lambda x} + Bxe^{9\lambda x}.


$$

Now we apply the boundary conditions.

- Applying the first boundary condition, $y(0) = 0,$ yields So, the solution simplifies to $y = Bxe^{9\lambda x}.$ Its derivative is

- Applying the second boundary condition, $4y(3) + 5y'(3) = 0,$ yields

For a nontrivial solution (an eigenfunction), we require $B\neq 0.$ Since $e^{27\lambda}$ is never zero, we must have

$$


17+135\lambda = 0 \quad \implies \quad \lambda = -\dfrac{17}{135}.


$$

This is our **eigenvalue**. The corresponding **eigenfunction** is

$$


y(x) = Bxe^{9(-17/135) x} = Bxe^{-17x/15}.


$$

Note that any nonzero constant multiple of this function is also an eigenfunction.

### Example: Exponential Eigenfunctions

#### Question

Consider the boundary value problem

$$


y'' - 18\lambda y' + 81\lambda^2y = 0, \quad y'(1) = 0, \quad y(2) + 2y'(2) = 0, \quad 1 \leq x \leq 2, \quad \lambda \in\mathbb R.


$$

Find the eigenvalues and eigenfunctions of this problem. Assume that $B$ and $C$ are constants.

#### Explanation

We consider the cases $\lambda = 0$ and $\lambda \neq 0$ separately, since they correspond to different solutions.

****: First, we consider $\lambda = 0.$

Setting $\lambda = 0$ gives the equation

$$


y'' = 0.


$$

Integrating this equation gives

$$


y = Ax + B.


$$

Applying the conditions $y'(1) =0$ and $y(2) + 2y'(2) = 0$ yields the trivial solution $y\equiv 0.$ Since the zero solution is not an eigenfunction, $\lambda = 0$ is not an eigenvalue.

****: Next, we consider $\lambda \neq 0.$

To find the fundamental solutions, we set $y = e^{m x}.$ The auxiliary equation is

$$


\begin{aligned}𝑚^{2}−18𝜆𝑚+81𝜆^{2} & =0 \\ (𝑚−9𝜆)(𝑚−9𝜆) & =0.\end{aligned}


$$

So, we have the double root $m = 9\lambda.$ So, the fundamental solutions are

$$


y_1(x) = e^{9\lambda x}, \qquad y_2(x) = xe^{9\lambda x}


$$

and the general solution is

$$


y = Ae^{9\lambda x} + Bxe^{9\lambda x}.


$$

Differentiating gives

$$


\begin{aligned}𝑦^{′} & =9𝐴𝜆𝑒^{9𝜆𝑥}+𝐵𝑒^{9𝜆𝑥}+9𝐵𝜆𝑥𝑒^{9𝜆𝑥}.\end{aligned}


$$

Applying the boundary condition $y'(1) = 0$ yields

$$


\begin{aligned}9𝐴𝜆𝑒^{9𝜆}+𝐵𝑒^{9𝜆}+9𝐵𝜆𝑒^{9𝜆} & =0 \\ 9𝐴𝜆+𝐵+9𝐵𝜆 & =0 \\ (9𝜆)𝐴+(1+9𝜆)𝐵 & =0.\end{aligned}


$$

Applying the boundary condition $y(2) + 2y'(2) = 0$ yields

$$


\begin{aligned}𝐴𝑒^{18𝜆}+2𝐵𝑒^{18𝜆}+2(9𝐴𝜆𝑒^{18𝜆}+𝐵𝑒^{18𝜆}+18𝐵𝜆𝑒^{18𝜆}) & =0 \\ 𝐴+2𝐵+2(9𝐴𝜆+𝐵+18𝐵𝜆) & =0 \\ 𝐴+2𝐵+18𝐴𝜆+2𝐵+36𝐵𝜆 & =0 \\ (1+18𝜆)𝐴+(4+36𝜆)𝐵 & =0 \\ (1+18𝜆)𝐴+4(1+9𝜆)𝐵 & =0.\end{aligned}


$$

So, we have the following systems of equations for $A$ and $B{:}$

$$


\begin{aligned}(9𝜆)𝐴+(1+9𝜆)𝐵=0 \\ (1+18𝜆)𝐴+4(1+9𝜆)𝐵=0\end{aligned}


$$

This homogeneous linear system has a nontrivial solution if and only if the determinant is zero. This gives

$$


\begin{aligned}9𝜆 & 1+9𝜆 \\ 1+18𝜆 & 4(1+9𝜆)\end{aligned}


$$

So, we get

$$


\begin{aligned}9𝜆⋅4(1+9𝜆)−(1+9𝜆)(1+18𝜆) & =0 \\ (1+9𝜆)[36𝜆−(1+18𝜆)] & =0 \\ (1+9𝜆)[36𝜆−1−18𝜆] & =0 \\ (1+9𝜆)(18𝜆−1) & =0.\end{aligned}


$$

Thus, we have the eigenvalues $\lambda_1 = -\dfrac19 \textrm{and} \lambda_2 = \dfrac1{18}.$

Finally, we find the eigenfunction corresponding to each eigenvalue:

- Consider $\lambda_1 = -\dfrac19.$ Then, we have the solution and substituting $\lambda_1$ into we get which gives $A = 0,$ and where $B$ is a free parameter. Thus, the eigenfunction corresponding to this eigenvalue is

- For $\lambda_2 = \dfrac1{18},$ we have and substituting $\lambda_2$ into we get where $B$ is a free parameter. Thus, the eigenfunction corresponding to this eigenvalue is where we have set $C = B.$

So, the eigenfunctions corresponding to $\lambda_1$ and $\lambda_2,$ respectively, are $Bxe^{-x} \textrm{and} Ce^{x/2}(x-3).$

### Trigonometric Eigenfunctions

When the auxiliary equation has purely imaginary roots, the solutions are trigonometric, and the boundary conditions usually force $\lambda$ to take on a discrete set of values. So, we again look for values of $\lambda$ that allow a nontrivial solution.

We will now find the **eigenvalues** and **eigenfunctions** for the boundary value problem:

$$


y'' + 9\lambda^2 y = 0, \qquad y'(0) = 0, \quad y(4) = 0, \quad 0 \leq x \leq 4, \quad \lambda \geq 0.


$$

We consider two cases based on the value of $\lambda,$ since they correspond to different forms of the general solution.

**Case 1: $\lambda = 0$**

Setting $\lambda = 0$ gives the equation $y'' = 0.$ Integrating this equation twice gives the general solution:

$$


y = Ax + B.


$$

To apply the boundary conditions, we first find the derivative, $y' = A.$

- Applying $y'(0) = 0$ gives $A = 0.$ The solution becomes $y = B.$

- Applying $y(4) = 0$ then gives $B = 0.$

This yields the trivial solution $y \equiv 0.$ Since an eigenfunction must be nontrivial, $\lambda = 0$ is *not* an eigenvalue.

**Case 2: $\lambda > 0$**

The auxiliary equation is $m^2 + 9\lambda^2 = 0,$ which has roots $m = \pm 3i\lambda.$ The general solution is therefore

$$


y = A\cos (3\lambda x) + B\sin (3\lambda x).


$$

Now we apply the boundary conditions. First, we find the derivative:

$$


y' = -3A\lambda\sin(3\lambda x) + 3B\lambda\cos(3\lambda x).


$$

- Applying the condition $y'(0) = 0$ yields: Since we are in the case where $\lambda > 0,$ this requires $B = 0.$ The solution simplifies to:

- Next, applying the condition $y(4) = 0$ yields: For a nontrivial solution, we must have $A \neq 0,$ which means we require This condition is met when $12\lambda$ is an odd multiple of $\pi/2:$

Solving for $\lambda$ gives the set of **eigenvalues**:

$$


\lambda_n = \dfrac{(2n+1)\pi}{24}.


$$

The corresponding **eigenfunctions** are

$$


y_n(x) = A_n \cos(3\lambda_n x) , \quad A_n \in \mathbb{R}.


$$

### Example: Trigonometric Eigenfunctions

#### Question

Consider the boundary value problem

$$


y'' + 9\lambda y = 0, \qquad y(0) = y(\pi) = 0, \quad 0 \leq x \leq \pi, \quad \lambda \geq 0.


$$

Find the eigenvalues and eigenfunctions of this problem.

#### Explanation

We consider the cases $\lambda = 0$ and $\lambda > 0$ separately, since they correspond to different solutions.

****: First, we consider $\lambda = 0.$

Setting $\lambda = 0$ gives the equation

$$


y'' = 0.


$$

Integrating this equation gives

$$


y = Ax + B.


$$

Applying the conditions $y(0) = y(\pi) = 0$ yields the trivial solution $y\equiv 0.$ Since the zero solution is not an eigenfunction, $\lambda = 0$ is not an eigenvalue.

****: Next, we consider $\lambda > 0.$

To find the fundamental solutions, we set $y = e^{m x}.$ The auxiliary equation is

$$


\begin{aligned}𝑚^{2}+9𝜆 & =0.\end{aligned}


$$

So, we have $m = \pm 3\textrm i\sqrt{\lambda}.$ So, the fundamental solutions are

$$


y_1(x) = \cos (3x\sqrt{\lambda}), \qquad y_2(x) = \sin (3x\sqrt{\lambda})


$$

and the general solution is

$$


y = A\cos (3x\sqrt{\lambda}) + B\sin (3x\sqrt{\lambda}).


$$

Applying the boundary condition $y(0) = 0$ yields

$$


A\cos (0) + B\sin (0) = 0


$$

which gives $A = 0.$ So, we have

$$


y = B\sin (3x\sqrt{\lambda}).


$$

Applying the boundary condition $y(\pi) = 0$ yields

$$


B\sin (3\pi\sqrt{\lambda}) = 0.


$$

For nontrivial solutions, we require

$$


3\pi\sqrt{\lambda} = n\pi


$$

for $n\in \mathbb N.$ This gives the set of eigenvalues

$$


\lambda_n = \dfrac{n^2}{9}.


$$

The corresponding eigenfunctions are

$$


y_n(x) = B_n \sin(3x\sqrt{\lambda_n}), \qquad B_n \in\mathbb R.


$$
