# Second-Order Homogeneous Recurrence Relations: Characteristic Equations with Repeated Roots

Source: https://www.mathacademy.com/topics/1916?courseId=109
Topic ID: 1916

## Prerequisites

- [Second-Order Homogeneous Recurrence Relations: Characteristic Equations with Distinct Real Roots](./2007-second-order-homogeneous-recurrence-relations-characteristic-equations-with-distinct-real-roots.md)

## Lesson

### Introduction

Recall that when the characteristic equation of a second-order linear homogeneous recurrence relation has two distinct real roots $\lambda_1$ and $\lambda_2,$ the general solution is

$$



a_n = A \cdot \lambda_1^n + B \cdot \lambda_2^n.



$$

However, if the characteristic equation has a *repeated* root $\lambda,$ the general solution is

$$



a_n = A \cdot \lambda^n + Bn \cdot \lambda^n.



$$

To illustrate, let's solve the following recurrence relation:

$$



a_n = 6a_{n-1} -9a_{n-2}



$$

Assuming $a_n = \lambda^n,$ we have that

$$



a_{n-1} = \lambda^{n-1}, \qquad a_{n-2} = \lambda^{n-2}.



$$

Substituting the above into our relation gives

$$



\lambda^n = 6\lambda^{n-1} - 9\lambda^{n-2}



$$

which can be written as follows:

$$



\begin{aligned}𝜆^{𝑛}−6𝜆^{𝑛−1}+9𝜆^{𝑛−2} & =0 \\ 𝜆^{𝑛−2}(𝜆^{2}−6𝜆+9) & =0\end{aligned}



$$

So, the characteristic equation is

$$



\lambda^2 - 6\lambda + 9 = 0.



$$

Factoring, we get

$$



(\lambda - 3)^2 = 0.



$$

Therefore, $\lambda = 3$ is a repeated root, and the general solution is

$$



a_n = A \cdot 3^n + Bn \cdot 3^n.



$$

### Example: Finding and Solving a Characteristic Equation

#### Question

Consider the recurrence relation $a_n = -2a_{n-1} - a_{n-2}.$ If $a_n=\lambda^n$ is a nonzero solution, then find the value of $\lambda.$

#### Explanation

Assuming $a_n=\lambda^n,$ we have that

$$



a_{n-1} = \lambda^{n-1}, \qquad a_{n-2} = \lambda^{n-2}.



$$

Substituting the above into our relation gives

$$



\begin{aligned}𝜆^{𝑛} & =−2𝜆^{𝑛−1}−𝜆^{𝑛−2}\end{aligned}



$$

which can be written as follows:

$$



\begin{aligned}𝜆^{𝑛}+2𝜆^{𝑛−1}+𝜆^{𝑛−2} & =0 \\ 𝜆^{𝑛−2}(𝜆^{2}+2𝜆+1) & =0\end{aligned}



$$

So, the characteristic equation is

$$



\lambda^2 + 2\lambda + 1 = 0.



$$

Factoring, we get

$$



(\lambda + 1)^2 = 0.



$$

Therefore, $\lambda = -1$ is a repeated root of the characteristic equation.

### Example: Finding the General Solution to a Second-Order Recurrence Relation

#### Question

Find the general solution to the recurrence relation $a_n = 4a_{n-1} - 4a_{n-2}.$

#### Explanation

Let $a_n=\lambda^n.$ Then, we have that

$$



a_{n-1} = \lambda^{n-1}, \qquad a_{n-2} = \lambda^{n-2}.



$$

Substituting the above into our relation gives

$$



\lambda^n = 4\lambda^{n-1} - 4\lambda^{n-2}



$$

which can be written as follows:

$$



\begin{aligned}𝜆^{𝑛}−4𝜆^{𝑛−1}+4𝜆^{𝑛−2} & =0 \\ 𝜆^{𝑛−2}(𝜆^{2}−4𝜆+4) & =0\end{aligned}



$$

So, the characteristic equation is

$$



\lambda^2 - 4\lambda + 4 = 0.



$$

Factoring, we get

$$



(\lambda - 2)^2 = 0.



$$

Therefore, $\lambda = 2$ is a repeated root.

So, the general solution to the recurrence relation is

$$



a_n = A \cdot 2^n + Bn \cdot 2^n.



$$

### Example: Solving Second-Order Recurrence Relations With Initial Conditions

#### Question

Solve the recurrence relation

$$



a_n = 8a_{n-1} - 16a_{n-2}, \quad a_0 = 1, \quad a_1 = -8.



$$

#### Explanation

Let $a_n=\lambda^n.$ Then, we have that

$$



a_{n-1} = \lambda^{n-1}, \qquad a_{n-2} = \lambda^{n-2}.



$$

Substituting the above into our relation gives

$$



\lambda^n = 8\lambda^{n-1} - 16\lambda^{n-2}



$$

which can be written as follows:

$$



\begin{aligned}𝜆^{𝑛}−8𝜆^{𝑛−1}+16𝜆^{𝑛−2} & =0 \\ 𝜆^{𝑛−2}(𝜆^{2}−8𝜆+16) & =0\end{aligned}



$$

The characteristic equation is

$$



\lambda^2 - 8\lambda + 16 = 0.



$$

Factoring, we get

$$



(\lambda - 4)^2 = 0.



$$

Therefore, $\lambda = 4$ is a repeated root.

So, the general solution to the recurrence relation is

$$



a_n = A \cdot 4^n + Bn \cdot 4^n.



$$

We find the constants $A$ and $B$ using the initial conditions:

- Substituting $a_0 = 1$ into the general solution gives

- Substituting $a_1 = -8$ into the general solution gives Using the fact that $A=1,$ we get

Therefore, the solution to the recurrence relation is

$$



\begin{aligned}𝑎_{𝑛} & =1⋅4^{𝑛}−3𝑛⋅4^{𝑛} \\ & =4^{𝑛}−3𝑛⋅4^{𝑛} \\ & =4^{𝑛}(1−3𝑛).\end{aligned}



$$
