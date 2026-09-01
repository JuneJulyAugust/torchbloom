# Introduction to Boundary Value Problems

Source: https://www.mathacademy.com/topics/2742?courseId=61
Topic ID: 2742

## Prerequisites

- [Introduction to Second-Order Linear ODEs](./2548-introduction-to-second-order-linear-odes.md)

## Lesson

### Introduction

A **boundary value problem** (BVP) specifies a differential equation for an unknown function $y(x)$ together with conditions on $y$ (or its derivatives) at *different* locations in the domain.

For example, the system

$$


y'' - y = x, \qquad y(a)=1, \qquad y(b)=0


$$

is a boundary value problem because the two conditions are specified at different points ($x=a$ and $x=b$).

Recall that an *initial value problem* (IVP) specifies both conditions at the *same* location in the domain. For instance,

$$


y'' - y = x, \qquad y(a)=1, \qquad y'(a)=0.


$$

Here, both conditions are specified at the same point $x=a.$

Let's see some more examples.

### Example: Identifying Boundary Value Problems

#### Question

Which of the following systems is a boundary value problem?

1. $y'' = x\cos(x), \quad y(2)=7$

2. $y'' + 3y = x^2+1, \quad y(0)=0, \quad y(5)=0$

3. $2y'' - y' = e^{2x}, \quad y(-1)=1, \quad y(1)=3$

#### Explanation

If a second-order differential equation for the function $y(x)$ is given with two conditions specified at ** locations in the domain of $y,$ then this is a ****.

Let's go through each equation in turn.

- The first system is not a boundary value problem. It consists of a differential equation combined with only one condition.

- The second system is a boundary value problem. It consists of a differential equation together with two conditions at different points in the domain of $y(x)$ (i.e., at $x=0$ and $x=5$).

- The third system is a boundary value problem. It consists of a differential equation together with two conditions at different points in the domain of $y(x)$ (i.e., at $x=-1$ and $x=1$).

### Dirichlet, Neumann, Robin, and Periodic Boundary Conditions

For a second-order **boundary value problem (BVP)**,

$$


y''(x) + P(x)y'(x) + Q(x)y(x) = f(x), \qquad a \leq x \leq b


$$

where $P(x), Q(x)$ and $f(x)$ are all continuous on $[a,b],$ the solution is constrained by **boundary conditions**. The most common types are:

- **Dirichlet** conditions: These specify the *value* of the function at the boundaries.

- **Neumann** conditions: These specify the *rate of change* (or slope) of the function at the boundaries.

- **Robin** (mixed) conditions: These specify a *linear combination* of the function's value and its rate of change.

- **Periodic** conditions: These require the function and its derivative to have the same value at both boundaries.

where $\gamma_i, \alpha_i,$ and $\beta_i$ are real numbers with $(\alpha_i, \beta_i) \neq (0,0).$

**Note:** Dirichlet and Neumann conditions are special cases of Robin conditions. However, we typically apply the most specific label possible. This is the convention we'll follow.

Next, we will look at a concrete example of a boundary value problem.

### Example: Classifying Boundary Conditions

#### Question

Consider the following boundary value problem.

$$


y''(x) + 2y(x) = x, \qquad y(0) - y'(0) = 4, \qquad y(2) = 1, \qquad 0\leq x \leq 2


$$

Which of the following best classifies the boundary conditions for this problem?

1. Robin

2. Dirichlet

3. Neumann

4. Periodic

#### Explanation

For a second-order boundary value problem,

$$


y''(x) + P(x)y'(x) + Q(x)y(x) = f(x), \qquad a \leq x \leq b


$$

where $P(x),Q(x)$ and $f(x)$ are all continuous on $[a,b],$ we have the following boundary condition classifications.

- Dirichlet:

- Neumann:

- Robin (mixed):

- Periodic:

where $\gamma_i, \alpha_i,$ and $\beta_i$ are real numbers with $(\alpha_i, \beta_i) \neq (0,0).$

In our case, we have the following boundary conditions, defined on $x = a = 0$ and $x = b = 2.$

$$


y(0) - y'(0) = 4, \qquad y(2) = 1


$$

These are Robin (mixed) boundary conditions.

### Homogeneous vs. Inhomogeneous Boundary Value Problems

We'll restrict our attention to Dirichlet, Neumann, and Robin (mixed) conditions. Recall that for a second-order boundary value problem,

$$


y''(x) + P(x)y'(x) + Q(x)y(x) = f(x), \qquad a \leq x \leq b


$$

where $P(x),$ $Q(x),$ and $f(x)$ are all continuous on $[a,b],$ we have the following boundary condition classifications:

- Dirichlet:

- Neumann:

- Robin (mixed):

A set of Dirichlet, Neumann, or Robin boundary conditions is **homogeneous** if both constants on the right-hand side are zero (i.e., $\gamma_1 = \gamma_2 = 0.$) Otherwise, it is **inhomogeneous.**

A boundary value problem is **homogeneous** if

- the differential equation is *homogeneous* $(f \equiv 0),$ and

- the corresponding boundary conditions are *homogeneous*.

Otherwise, the BVP is **inhomogeneous**.

*Note*: The notation $f \equiv 0$ means $f$ is identically zero (i.e., zero for all $x.$)

In the next slide, we will apply these definitions to a concrete example.

### Example: Identifying Homogeneous Boundary Value Problems

#### Question

Consider the following boundary value problem (BVP).

$$


y''(x) + e^x y'(x) - y(x) = 0, \qquad 1\leq x \leq 3


$$

$$


y(1) = 0, \qquad y(3) = -5


$$

Complete the missing information below:

$\quad$ The governing differential equation is $𝐴𝐴𝐴𝐴𝐴$.

$\quad$ For this BVP, the $𝐴𝐴𝐴𝐴𝐴$ boundary conditions are $𝐴𝐴𝐴𝐴𝐴$

$\quad$ The boundary value problem is $𝐴𝐴𝐴𝐴𝐴$.

#### Explanation

For a second-order boundary value problem,

$$


y''(x) + P(x)y'(x) + Q(x)y(x) = f(x), \qquad a \leq x \leq b


$$

where $P(x),Q(x)$ and $f(x)$ are all continuous on $[a,b],$ we have the following boundary condition classifications.

- Dirichlet:

- Neumann:

- Robin (mixed):

where $\gamma_i, \alpha_i,$ and $\beta_i$ are real numbers with $(\alpha_i, \beta_i) \neq (0,0).$

A set of Dirichlet, Neumann, or Robin boundary conditions is homogeneous if both right-hand sides are zero (i.e., $\gamma_1 = \gamma_2 = 0.)$ Otherwise, they are inhomogeneous.

A boundary value problem is homogeneous if the differential equation is homogeneous $(f \equiv 0)$ and the corresponding boundary conditions are homogeneous. Otherwise, the BVP is inhomogeneous.

With that in mind, let's consider each statement:

- The governing differential equation is Since the right-hand side $f(x) \equiv 0,$ the equation is $\text{homogeneous}.$

- The boundary conditions are These are $\text{Dirichlet}$ boundary conditions, and since the right-hand sides are not zero for both, they are $\text{inhomogeneous}.$

- Since the governing equation is homogeneous, yet the boundary conditions are inhomogeneous, the BVP is $\text{inhomogeneous}.$
