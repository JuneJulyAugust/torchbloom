# Second-Order Homogeneous Initial Value Problems

Source: https://www.mathacademy.com/topics/2741?courseId=154
Topic ID: 2741

## Prerequisites

- [Second-Order Homogeneous ODEs: Characteristic Equations With Repeated Roots](./879-second-order-homogeneous-odes-characteristic-equations-with-repeated-roots.md)
- [Second-Order Homogeneous ODEs: Characteristic Equations With Complex Roots](./880-second-order-homogeneous-odes-characteristic-equations-with-complex-roots.md)

## Lesson

### Introduction

Remember that the general solution of the ODE

$$


y'' + 5y' + 6y = 0,


$$

is given by

$$


y = Ae^{-2x} + Be^{-3x}


$$

where $A$ and $B$ are arbitrary constants.

Now, let's consider the same ODE with some additional conditions imposed:

$$


y'' + 5y' + 6y = 0, \quad y(0) = 1, \quad y'(0) = 1.


$$

This is called an **initial value problem (IVP)**. In addition to the differential equation, we are given two **initial conditions**:

$$


y(0) = 1 \quad \text{and} \quad y'(0) = 1.


$$

The goal of an IVP is to use these initial conditions to find specific values for the arbitrary constants $A$ and $B,$ which gives us a unique *particular solution*.

In the next slide, we will use the initial conditions to solve for $A$ and $B.$

### Solving the Initial Value Problem

Let's find the particular solution for the **initial value problem**:

$$


y'' + 5y' + 6y =0, \ \ y(0) = 1, \ \ y' (0) = 1.


$$

We start with the general solution:

$$


y(x) = Ae^{-2x} + Be^{-3x}.


$$

**Step 1: Apply the first initial condition, $y(0)=1.$** Substituting $x=0$ and $y=1$ into the general solution gives our first equation:

$$


\begin{aligned}1 & =𝐴𝑒^{−2(0)}+𝐵𝑒^{−3(0)} \\ 1 & =𝐴𝑒^{0}+𝐵𝑒^{0} \\ 1 & =𝐴+𝐵.\end{aligned}


$$

**Step 2: Apply the second initial condition, $y'(0)=1.$** First, we need to find the derivative, $y'(x){:}$

$$


y'(x) = -2 A e ^ { -2 x} -3 B e ^ {-3 x}.


$$

Now, substituting $x=0$ and $y'=1$ gives our second equation:

$$


\begin{aligned}1 & =−2𝐴𝑒^{−2(0)}−3𝐵𝑒^{−3(0)} \\ 1 & =−2𝐴𝑒^{0}−3𝐵𝑒^{0} \\ 1 & =−2𝐴−3𝐵.\end{aligned}


$$

**Step 3: Solve the system of equations for $A$ and $B.$** We have a system of two linear equations:

$$


\begin{aligned}1=𝐴+𝐵 \\ 1=−2𝐴−3𝐵\end{aligned}


$$

From the first equation, we can write $A=1-B.$ Substituting this into the second equation:

$$


\begin{aligned}1 & =−2(1−𝐵)−3𝐵 \\ 1 & =−2+2𝐵−3𝐵 \\ 3 & =−𝐵 \\ 𝐵 & =−3.\end{aligned}


$$

Now, find $A{:}$

$$


A = 1-B = 1 - (-3) = 4.


$$

**Step 4: Write the particular solution.** Substituting $A=4$ and $B=-3$ back into the general solution gives the unique solution to the IVP:

$$


y(x) = 4e^{-2x} - 3 e^{-3x}.


$$

### Example: Solving Second-Order IVPs When the Characteristic Equation Has Distinct Real Roots

#### Question

Given that the differential equation

$$


y'' + y - 2y =0


$$

has the general solution

$$


y = Ae^{x} + Be^{- 2 x},


$$

solve the initial value problem

$$


y'' + y - 2y =0, \ \ y(1) = e, \ \ y'(1) = e ^{-2}.


$$

#### Explanation

We find the constants $A$ and $B$ using the initial conditions.

- Substituting $y(1)=e$ into our general solution gives

- To apply the condition $y'(1) = e^{-2},$ we first differentiate $y$ to get Then, we substitute $y'(1)=e^{-2}$ into the above to get

Putting the two equations from above together, we have the following system:

$$


\begin{aligned}𝐴=1−𝐵𝑒^{−3} \\ 𝑒^{−2}=𝐴𝑒−2𝐵𝑒^{−2}\end{aligned}


$$

Substituting $A = 1 - B e ^{-3}$ in the second equation gives

$$


\begin{aligned}𝑒^{−2} & =(1−𝐵𝑒^{−3})𝑒−2𝐵𝑒^{−2} \\ 1 & =𝑒^{3}−𝐵−2𝐵 \\ 𝐵 & =\frac{𝑒^{3}−1}{3}.\end{aligned}


$$

Then, substituting $B= \dfrac {e ^ 3 - 1} 3$ back into the equation $A = 1-Be^{-3}$ gives

$$


A = 1 - \dfrac {(e ^ 3 - 1) e ^ {-3}} 3 = \dfrac {2 + e ^ {-3}} 3.


$$

Therefore, the particular solution of the initial value problem is

$$


y = \dfrac { e ^ {-3} + 2} 3 e^{x} + \dfrac {e ^ 3 - 1} 3 e^{-2x}.


$$

### Example: Solving Second-Order IVPs When the Characteristic Equation Has Repeated Roots

#### Question

Solve the initial value problem

$$


y'' - 4 y' + 4y =0, \qquad y(0) = 3, \qquad y'(0) = 2.


$$

#### Explanation

First, we find the roots of the characteristic polynomial:

$$


\begin{aligned}𝜆^{2}−4𝜆+4 & =0 \\ (𝜆−2)^{2} & =0\end{aligned}


$$

We have a repeated root $\lambda = 2,$ so we have the following general solution:

$$


y = A e ^ { 2 x} + B x e ^ {2 x}


$$

We find the constants $A$ and $B$ using the initial conditions.

- Substituting $y(0)=3$ into our general solution gives

- To apply the condition $y' (0) = 2,$ we first differentiate $y$ to get Then, we substitute $y'(0)=2$ into the above to get

Putting the two equations from above together, we have the following system:

$$


\begin{aligned}3=𝐴 \\ 2=2𝐴+𝐵\end{aligned}


$$

Substituting $A=3$ into the second equation gives

$$


\begin{aligned}2 & =6+𝐵 \\ 𝐵 & =−4\end{aligned}


$$

So we have $A=3$ and $B=-4,$ and therefore the solution is

$$


y = 3 e ^ { 2 x } - 4 x e ^ { 2 x}.


$$

### Example: Solving Second-Order IVPs When the Characteristic Equation Has Imaginary Roots

#### Question

Solve the following initial value problem:

$$


y'' + y = 0, \quad y(\pi) = 2, \quad y'(\pi) = -1


$$

#### Explanation

First, we find the roots of the characteristic polynomial:

$$


\begin{aligned}𝜆^{2}+1 & =0 \\ 𝜆^{2} & =−1 \\ 𝜆 & =±i\end{aligned}


$$

So, we have the following general solution:

$$


y = A \cos x + B \sin x


$$

Now, we need to find constants $A$ and $B.$ To do this, we apply the initial conditions $y(\pi)=2,$ $y'(\pi)=-1.$

- Substituting $y(\pi) = 2$ into the general solution gives

- Computing $y'(x),$ we get and substituting $y'(\pi)=-1,$ we get

Therefore, the solution to the initial value problem is

$$


y = -2\cos{x} + \sin{x}.


$$

### Example: Solving Second-Order IVPs When the Characteristic Equation Has Complex Roots

#### Question

Solve the initial value problem

$$


y'' - 6y' + 25y=0, \quad y(0)= 2, \quad y'(0) = 5, \quad t\gt 0.


$$

#### Explanation

First, we find the roots of the characteristic polynomial by completing the square:

$$


\begin{aligned}𝜆^{2}−6𝜆+25 & =0 \\ (𝜆^{2}−6𝜆+9)−9+25 & =0 \\ (𝜆^{2}−3)^{2}+16 & =0 \\ (𝜆−3)^{2} & =−16 \\ 𝜆−3 & =4i \\ 𝜆 & =3±4i\end{aligned}


$$

So, we have the following general solution:

$$


y = e^{3x} \left( P \cos 4x + Q \sin 4x \right)


$$

We find the constants $P$ and $Q$ using the initial conditions.

- Substituting $y(0) = 2$ into the general solution gives

- To apply the condition $y'(0) = 5,$ we first differentiate $y$ to get Then, we substitute $y'(0) = 5$ and $P=2$ into the above to get

Therefore, the solution to the initial value problem is

$$


y = e^{3x} \left( 2 \cos 4x - \dfrac{1}{4} \sin 4x \right).


$$
