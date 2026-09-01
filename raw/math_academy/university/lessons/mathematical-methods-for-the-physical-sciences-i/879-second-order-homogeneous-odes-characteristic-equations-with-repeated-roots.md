# Second-Order Homogeneous ODEs: Characteristic Equations With Repeated Roots

Source: https://www.mathacademy.com/topics/879?courseId=154
Topic ID: 879

## Prerequisites

- [Second-Order Homogeneous ODEs: Characteristic Equations With Distinct Real Roots](./614-second-order-homogeneous-odes-characteristic-equations-with-distinct-real-roots.md)

## Lesson

### Introduction

When the characteristic equation of a second-order homogeneous ODE has a **repeated root** $\lambda = c,$ the general solution is

$$


y(x) = Ae^{cx} + Bxe^{cx}.


$$

To illustrate, let's solve the following ODE:

$$


\frac{\text{d}^2 y}{\text{d} x^2} - 6\frac{\text{d} y}{\text{d} x} + 9y =0.


$$

Assuming a solution of the form $y=e^{\lambda x},$ we differentiate and substitute into the ODE:

$$


\begin{aligned}𝜆^{2}𝑒^{𝜆𝑥}−6𝜆𝑒^{𝜆𝑥}+9𝑒^{𝜆𝑥} & =0 \\ 𝑒^{𝜆𝑥}(𝜆^{2}−6𝜆+9) & =0.\end{aligned}


$$

Since $e^{\lambda x}$ is never zero, we can divide by it to get the **characteristic equation**:

$$


\begin{aligned}𝜆^{2}−6𝜆+9 & =0 \\ (𝜆−3)^{2} & =0,\end{aligned}


$$

so $\lambda = 3$ is a **repeated root**. Therefore, the general solution is

$$


y(x) = Ae^{3x} + Bxe^{3x}.


$$

### Example: Constructing and Solving a Characteristic Equation With Repeated Roots

#### Question

Consider the equation $y''-2y'+y = 0.$ If $y = e^{\lambda x}$ is a solution to the equation, then what is $\lambda?$

#### Explanation

Assuming $y=e^{\lambda x}$ and differentiating $y$ with respect to $x$ gives

$$


y'= \lambda e^{\lambda x},\qquad y''= \lambda^2 e^{\lambda x}.


$$

Substituting the above into our differential equation gives

$$


\begin{aligned}𝜆^{2}𝑒^{𝜆𝑥}−2𝜆𝑒^{𝜆𝑥}+𝑒^{𝜆𝑥} & =0 \\ 𝑒^{𝜆𝑥}(𝜆^{2}−2𝜆+1) & =0.\end{aligned}


$$

The characteristic equation is therefore

$$


\begin{aligned}𝜆^{2}−2𝜆+1 & =0.\end{aligned}


$$

Factoring the auxiliary equation results in

$$


\begin{aligned}(𝜆−1)^{2} & =0\end{aligned}


$$

and so $\lambda = 1$ is a repeated root of the auxiliary equation.

### Example: Finding General Solutions When the Characteristic Equation Has Repeated Roots

#### Question

Find the general solution to the equation

$$


\frac{\text{d}^2 y}{\text{d} t^2} - 12\frac{\text{d} y}{\text{d} t} + 36y =0.


$$

#### Explanation

Assuming $y=e^{\lambda t}$ and differentiating $y$ with respect to $t$ gives

$$


\frac{\text{d} y}{\text{d} t}= \lambda e^{\lambda t},\qquad \frac{\text{d}^2 y}{\text{d} t^2}= \lambda^2 e^{\lambda t}.


$$

Substituting the above into our differential equation gives

$$


\begin{aligned}𝜆^{2}𝑒^{𝜆𝑡}−12𝜆𝑒^{𝜆𝑡}+36𝑒^{𝜆𝑡} & =0 \\ 𝑒^{𝜆𝑡}(𝜆^{2}−12𝜆+36) & =0.\end{aligned}


$$

The characteristic equation is

$$


\begin{aligned}𝜆^{2}−12𝜆+36 & =0 \\ (𝜆−6)^{2} & =0,\end{aligned}


$$

and $\lambda = 6$ is a repeated root. Therefore, the general solution is

$$


y = Ae^{6 t} + Bte^{6t}.


$$

### Example: Identifying Non-Solutions of Second-Order Homogeneous ODEs

#### Question

Given the equation $y''+12y'+36y = 0$ for $y=y(x),$ which of the following is **** a solution to this equation?

1. $xe^{-6x}$

2. $4e^{-6x}-3xe^{-6x}$

3. $2e^{6x}$

#### Explanation

Assuming $y=e^{\lambda x}$ and differentiating $y$ with respect to $x$ gives

$$


y'= \lambda e^{\lambda x},\qquad y''= \lambda^2 e^{\lambda x}.


$$

Substituting the above into our differential equation gives

$$


\begin{aligned}𝜆^{2}𝑒^{𝜆𝑥}+12𝜆𝑒^{𝜆𝑥}+36𝑒^{𝜆𝑥} & =0 \\ 𝑒^{𝜆𝑥}(𝜆^{2}+12𝜆+36) & =0.\end{aligned}


$$

The characteristic equation is therefore

$$


\begin{aligned}𝜆^{2}+12𝜆+36 & =0 \\ (𝜆+6)^{2} & =0,\end{aligned}


$$

and $\lambda =-6$ is a repeated root. Therefore, the general solution is

$$


y = Ae^{-6 x} + Bxe^{-6x}.


$$

Finally, we need to determine whether each of the given functions takes the form shown above.

- Function I takes the above form with $A=0$ and $B=1.$ So, it is a solution to the given ODE.

- Function II takes the above form with $A=4$ and $B=-3.$ So, it is a solution to the given ODE.

- Function III does ** take the above form. It contains $e^{6x},$ which is not included in the above form. So, it is ** a solution to the given ODE.

Therefore, the correct answer is "III only".
