# The Superposition Principle

Source: https://www.mathacademy.com/topics/2549?courseId=61
Topic ID: 2549

## Prerequisites

- [Verifying Solutions of Differential Equations](../ap-calculus-ab/1181-verifying-solutions-of-differential-equations.md)
- [Introduction to Second-Order Linear ODEs](./2548-introduction-to-second-order-linear-odes.md)

## Lesson

### Introduction

Recall that a second-order linear ODE can always be expressed in the form

$$


a(x)y'' + b(x)y' + c(x) y = f(x).


$$

Also, recall that the equation is *homogeneous* if $f(x) = 0$ for all $x{:}$

$$


a(x)y'' + b(x)y' + c(x) y =0


$$

The **superposition principle** states that if the functions $y_1(x)$ and $y_2(x)$ are solutions to a linear homogeneous differential equation, then the function

$$


y(x) = y_1(x) + y_2(x)


$$

is also a solution to the equation.

To illustrate, consider the following homogeneous differential equation:

$$


y'' + 16y = 0


$$

Two solutions of this equation are

$$


y_1(x) = \cos 4x, \qquad y_2(x) = \sin 4x.


$$

We can easily check that these are solutions by substituting them into the equation and verifying that they result in true statements:

$$


\begin{aligned}𝑦_{″1}^{}+16𝑦_{1} & =0 \\ (cos⁡4𝑥)^{″}+16cos⁡4𝑥 & =0 \\ (−4sin⁡4𝑥)^{′}+16cos⁡4𝑥 & =0 \\ −16cos⁡4𝑥+16cos⁡4𝑥 & =0 \\ 0 & =0\,✓ \\ 𝑦_{″2}^{}+16𝑦_{2} & =0 \\ (sin⁡4𝑥)^{″}+16sin⁡4𝑥 & =0 \\ (4cos⁡4𝑥)^{′}+16sin⁡4𝑥 & =0 \\ −16sin⁡4𝑥+16sin⁡4𝑥 & =0 \\ 0 & =0\,✓\end{aligned}


$$

Because the equation is linear and homogeneous, the superposition principle guarantees that the sum

$$


\begin{aligned}𝑦 & =𝑦_{1}+𝑦_{2}=cos⁡4𝑥+sin⁡4𝑥\end{aligned}


$$

is also a solution to the differential equation.

We can check that this is a solution to the equation by substituting (keeping the order consistent with our definition):

$$


\begin{aligned}𝑦^{″}+16𝑦 & =0 \\ (cos⁡4𝑥+sin⁡4𝑥)^{″}+16(cos⁡4𝑥+sin⁡4𝑥) & =0 \\ (−4sin⁡4𝑥+4cos⁡4𝑥)^{′}+16(cos⁡4𝑥+sin⁡4𝑥) & =0 \\ (−16cos⁡4𝑥−16sin⁡4𝑥)+16cos⁡4𝑥+16sin⁡4𝑥 & =0 \\ 0=0\,✓ & \end{aligned}


$$

**Watch out!** The superposition principle does *not* extend to the products or quotients of the known solutions. For example, the functions

$$


\cos4x\sin4x, \quad \sin^24x, \quad \dfrac{\sin4x}{\cos 4x},


$$

are *not* solutions to our original differential equation.

### Example: Identifying Solutions of Linear ODEs Using the Sum Rule

#### Question

Given that $y_1(x) = e^{-2x}$ and $y_2(x) = e^x$ are solutions to the equation $y''+y'-2y=0,$ then according to the superposition principle which of the following must also be a solution to the equation?

1. $y(x) = \dfrac{e^{-2x}}{e^{x}}$

2. $y(x) = e^{-2x}\cdot e^{x}$

3. $y(x) = e^{-2x} +e^{x}$

#### Explanation

According to the superposition principle, if the functions $y_1(x)$ and $y_2(x)$ are solutions to a homogeneous differential equation, then $y(x) = y_1(x) + y_2(x)$ is also a solution to the equation.

Let's consider each option:

- The function $y(x) = \dfrac{e^{-2x}}{e^{x}}$ is **** guaranteed to be a solution of the equation by the superposition principle. The superposition principle does not extend to the quotients of the known solutions.

- The function $y(x) = e^{-2x}\cdot e^{x}$ is **** guaranteed to be a solution of the equation by the superposition principle. The superposition principle does not extend to the products of the known solutions.

- The function $y(x) = e^{-2x} +e^{x}$ is a solution of the equation by the superposition principle.

Therefore, the correct answer is "III only."

### Constant Multiples of Solutions

Suppose we have the second-order homogeneous ODE

$$


a(x)y'' + b(x)y' + c(x) y = 0.


$$

The superposition principle also states that if $y_1(x)$ is a solution to the equation, then the function

$$


y(x) = cy_1(x)


$$

is also a solution to the equation, where $c$ is a constant.

To illustrate, let's once again consider the following linear differential equation:

$$


y'' + 16y = 0


$$

Recall that

$$


y_1(x) = \cos 4x, \qquad y_2(x) = \sin 4x


$$

are solutions to this equation. So, according to the superposition principle, the functions

$$


6\cos 4x, \quad -\sin 4x, \qquad \dfrac{\pi}{e}\cos 4x


$$

are all solutions to the ODE.

We can check that these are indeed solutions to the equation by substituting. To illustrate, let's verify the solution $6\cos 4x = 6y_1(x)$ by evaluating the left-hand side of this equation:

$$


\begin{aligned}𝑦^{″}+16𝑦 & =(6cos⁡4𝑥)^{″}+16(6cos⁡4𝑥) \\ & =6⋅(cos⁡4𝑥)^{″}+6⋅16(cos⁡4𝑥) \\ & =6⋅((cos⁡4𝑥)^{″}+16cos⁡4𝑥) \\ & =6⋅((−4sin⁡4𝑥)^{′}+16cos⁡4𝑥) \\ & =6⋅(−16cos⁡4𝑥+16cos⁡4𝑥) \\ & =6⋅0 \\ & =0\,✓\end{aligned}


$$

**Watch out!** This idea extends to *scalar* (or constant) multiples only. For example, the function $x\cos 4x$ is *not* a solution to our ODE.

### Example: Identifying Solutions of Linear ODEs Using the Constant Multiple Rule

#### Question

Given that $y_1(x) = e^{2x}$ is a solution to the equation $y'' - 4y = 0,$ then according to the superposition principle which of the following must also be a solution to the equation?

1. $y(x) = 2xe^{2x}$

2. $y(x) = 3e^{2x}$

3. $y(x) = -e^{2x}$

#### Explanation

According to the superposition principle, if the function $y_1(x)$ is a solution to a homogeneous, linear differential equation, and $c$ is a constant, then $y(x) = c y_1(x)$ is also a solution to the equation.

Let's consider each option:

- The function $y(x) = 2xe^{2x}$ is **** guaranteed to be a solution of the equation by the superposition principle. The superposition principle does not extend to the product of a non-constant function and a known solution.

- The function $y(x) = 3e^{2x}$ is a solution of the equation by the superposition principle. In this case, $c=3.$

- The function $y(x) = -e^{2x}$ is a solution of the equation by the superposition principle. In this case, $c=-1.$

Therefore, the correct answer is "II and III only."

### The Superposition Principle in Its Most General Form

In its most general form, the **superposition principle** states that any linear combination (or "superposition") of solutions to a homogeneous, linear differential equation is also a solution. More precisely:

*If the functions $y_1(x)$ and $y_2(x)$ are solutions to a homogeneous, linear differential equation, and $c_1$ and $c_2$ are constants, then $y(x) = c_1 y_1(x) + c_2 y_2(x)$ is also a solution to the equation.*

Note that the superposition principle follows immediately from the definition of a linear differential operator $L.$ Recall that every homogeneous equation can be written as

$$


L(y) = 0.


$$

Now, let $y = c_1 y_1(x) + c_2y_2(x).$ Then, by the linearity of $L,$ we have

$$


\begin{aligned}𝐿(𝑦) & =𝐿(𝑐_{1}𝑦_{1}(𝑥)+𝑐_{2}𝑦_{2}(𝑥)) \\ & =𝐿(𝑐_{1}𝑦_{1}(𝑥))+𝐿(𝑐_{2}𝑦_{2}(𝑥)) \\ & =𝑐_{1}𝐿(𝑦_{1}(𝑥))+𝑐_{2}𝐿(𝑦_{2}(𝑥)) \\ & =𝑐_{1}⋅0+𝑐_{2}⋅0 \\ & =0+0 \\ & =0.\end{aligned}


$$

For example, suppose we're told that the differential equation

$$


y'' - y = 0


$$

has two solutions

$$


y_1(x) = e^x \quad \textrm{and} \quad y_2(x) = e^{-x}.


$$

Then, according to the superposition principle, any linear combination

$$


y(x) = c_1 e^x + c_2 e^{-x}


$$

is also a solution.

- For instance, we can conclude that is also a solution because it takes the form $c_1 e^x + c_2 e^{-x}$ with $c_1 = 2$ and $c_2 = -\dfrac{1}{3}.$ $\quad \color{green}\checkmark$

- However, we *cannot* conclude that is a solution because $x^2$ and $\sin(x)$ are not constants. $\quad \color{red}\times$

### Example: Identifying Solutions to Linear ODEs Using the Superposition Principle

#### Question

Given that $y_1(x) = e^{-x}$ and $y_2(x) = e^{3x}$ are solutions to the equation $y'' - 2y - 3y = 0,$ which of the following must also be a solution to the equation?

1. $y(x) = 7e^{-x} - 6e^{3x}$

2. $y(x) = \dfrac{e^{3x}}{e^{-x}}$

3. $y(x) =- e^{x} + e^{3x}$

#### Explanation

According to the superposition principle, if the functions $y_1(x)$ and $y_2(x)$ are solutions to a homogeneous, linear differential equation, and $c_1$ and $c_2$ are constants, then $y(x) = c_1 y_1(x) + c_2 y_2(x)$ is also a solution to the equation.

We're given that $y_1(x) = e^{-x}$ and $y_2(x) =e^{3x}.$ Therefore, the following function is also a solution:

$$


y(t) = c_1 e^{-x} + c_2 e^{3x}


$$

Let's consider each option:

- The function $y(x) = 7e^{-x} - 6e^{3x}$ is a solution of the given equation. Here, $c_1 = 7$ and $c_2 = -6.$

- The function $y(x) = \dfrac{e^{3x}}{e^{-x}}$ is **** guaranteed to be a solution of the given equation. The superposition principle only applies to linear combinations of known solutions. It does not extend to the divisions of the known solutions.

- The function $y(x) = - e^{x} + e^{3x}$ is **** guaranteed to be a solution of the given equation because $e^x$ is not a solution.

Therefore, the correct answer is "I only".
