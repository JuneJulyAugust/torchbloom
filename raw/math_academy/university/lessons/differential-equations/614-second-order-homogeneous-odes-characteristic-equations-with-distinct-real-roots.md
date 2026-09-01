# Second-Order Homogeneous ODEs: Characteristic Equations With Distinct Real Roots

Source: https://www.mathacademy.com/topics/614?courseId=61
Topic ID: 614

## Prerequisites

- [General Solutions of Linear ODEs](./2740-general-solutions-of-linear-odes.md)

## Lesson

### Introduction

A second-order, linear, homogeneous ordinary differential equation with constant coefficients has the general form

$$


a\frac{\text{d}^2 y}{\text{d} x^2} + b\frac{\text{d} y}{\text{d} x} + cy =0,


$$

where $a, b,$ and $c$ are constants.

To find solutions, we can propose a trial solution of the form $y=e^{\lambda x},$ where $\lambda$ is a constant to be determined. Differentiating this gives:

$$


\dfrac{\text{d}y}{\text{d}x} = \lambda e^{\lambda x}, \qquad \dfrac{\text{d}^2y}{\text{d}x^2} = \lambda^2 e^{\lambda x}.


$$

Substituting these into the general ODE, we get:

$$


\begin{aligned}𝑎(𝜆^{2}𝑒^{𝜆𝑥})+𝑏(𝜆𝑒^{𝜆𝑥})+𝑐(𝑒^{𝜆𝑥}) & =0 \\ 𝑒^{𝜆𝑥}(𝑎𝜆^{2}+𝑏𝜆+𝑐) & =0.\end{aligned}


$$

Since $e^{\lambda x}$ can never be zero, the expression in the parentheses must be zero:

$$


a\lambda^2+b\lambda + c =0 .


$$

This is called the **characteristic equation** (or **auxiliary equation**). The roots of this quadratic equation for $\lambda$ give us the solutions to the original differential equation.

Next, we'll use the characteristic equation to solve a specific example.

### A Worked Example

Let's solve the following differential equation:

$$


\frac{\mathrm{d}^2 y}{\mathrm{d} x^2} + 5\frac{\mathrm{d} y}{\mathrm{d} x} + 6y =0


$$

From the previous slide, we know this ODE has a characteristic equation of the form $a\lambda^2 + b\lambda + c=0.$ Here, $a=1, b=5,$ and $c=6,$ so the characteristic equation is:

$$


\begin{aligned}𝜆^{2}+5𝜆+6 & =0 \\ (𝜆+3)(𝜆+2) & =0.\end{aligned}


$$

The roots are $\lambda_1 = -2$ and $\lambda_2 = -3.$ Each root gives a particular solution to the ODE: $y_1=e^{-2x}$ and $y_2=e^{-3x}.$

The **general solution** is a linear combination of these particular solutions:

$$


y(x) = Ae^{-2x} + Be^{-3x},


$$

where $A$ and $B$ are arbitrary constants.

### Example: Constructing and Solving a Characteristic Equation

#### Question

Consider the equation $y''-3y'-4y = 0$ where $y=y(t).$ If $y = e^{\lambda t}$ is a solution, then what is $\lambda?$

#### Explanation

Assuming $y=e^{\lambda t}$ and differentiating $y$ with respect to $t$ gives

$$


y'= \lambda e^{\lambda t},\qquad y''= \lambda^2 e^{\lambda t}.


$$

Substituting the above into our differential equation gives

$$


\begin{aligned}𝜆^{2}𝑒^{𝜆𝑡}−3𝜆𝑒^{𝜆𝑡}−4𝑒^{𝜆𝑡} & =0 \\ 𝑒^{𝜆𝑡}(𝜆^{2}−3𝜆−4) & =0.\end{aligned}


$$

So, we have the following characteristic equation:

$$


\lambda^2 - 3\lambda - 4 = 0


$$

Factoring, we get

$$


(\lambda -4) (\lambda +1) = 0.


$$

Therefore, the roots of the characteristic equation are $\lambda = 4$ and $\lambda = -1.$

### Example: Finding General Solutions of Second-Order Homogeneous ODEs

#### Question

Find the general solution to the equation

$$


\frac{\text{d}^2 y}{\text{d} x^2} + \frac{\text{d} y}{\text{d} x} - 2y =0.


$$

#### Explanation

This is a second-order homogeneous ODE. So, we assume the solutions take the form $y=e^{\lambda x}.$ Differentiating $y$ with respect to $x$ gives

$$


\dfrac{\text{d}y}{\text{d}x} = \lambda e^{\lambda x}, \qquad \dfrac{\text{d}^2y}{\text{d}x^2} = \lambda^2 e^{\lambda x}.


$$

Substituting the above into our differential equation gives

$$


\begin{aligned}𝜆^{2}𝑒^{𝜆𝑥}+𝜆𝑒^{𝜆𝑥}−2𝑒^{𝜆𝑥} & =0 \\ 𝑒^{𝜆𝑥}(𝜆^{2}+𝜆−2) & =0.\end{aligned}


$$

So, we have the following characteristic equation:

$$


\begin{aligned}𝜆^{2}+𝜆−2 & =0 \\ (𝜆−1)(𝜆+2) & =0\end{aligned}


$$

The roots of the characteristic equation are $\lambda = 1$ and $\lambda = -2.$ Therefore, the general solution is

$$


y = Ae^{x} + Be^{- 2 x}.


$$

### Example: Identifying Non-Solutions of Second-Order Homogeneous ODEs

#### Question

Given that $y = y(x)$ satisfies the equation $y''+7y'+6y = 0,$ which of the following could **** be $y(x)?$

1. $-3e^{-6x}$

2. $2e^{-6x}-4e^{-x}$

3. $e^{-6x}+2e^{x}$

#### Explanation

This is a second-order homogeneous ODE. So, we assume the solutions take the form $y=e^{\lambda x}.$ Differentiating $y$ with respect to $x$ gives

$$


y'= \lambda e^{\lambda x},\qquad y''= \lambda^2 e^{\lambda x}.


$$

Substituting the above into our differential equation gives

$$


\begin{aligned}𝜆^{2}𝑒^{𝜆𝑥}+7𝜆𝑒^{𝜆𝑥}+6𝑒^{𝜆𝑥} & =0 \\ 𝑒^{𝜆𝑥}(𝜆^{2}+7𝜆+6) & =0.\end{aligned}


$$

So, we have the following characteristic equation:

$$


\begin{aligned}𝜆^{2}+7𝜆+6 & =0 \\ (𝜆+6)(𝜆+1) & =0\end{aligned}


$$

The roots of the characteristic equation are $\lambda = -6$ and $\lambda = - 1.$

Therefore, the general solution is

$$


y = Ae^{-6x} + Be^{- x}.


$$

Finally, we need to determine whether each of the given functions takes the form shown above.

- Function I takes the above form with $A=-3$ and $B=0.$ So, it is a solution to the given ODE.

- Function II takes the above form with $A=2$ and $B=-1.$ So, it is a solution to the given ODE.

- Function III does ** take the above form. It contains $e^x,$ which is not included in the above form. So, it is ** a solution to the given ODE.

Therefore, the correct answer is "III only".
