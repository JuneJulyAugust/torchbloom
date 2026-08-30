# Finding General Solutions Using the Method of Frobenius

Source: https://www.mathacademy.com/topics/6719?courseId=61
Topic ID: 6719

## Prerequisites

- [General Solutions of Linear ODEs](./2740-general-solutions-of-linear-odes.md)
- [Finding Recurrence Relations for the Coefficients of a Frobenius Solution](./6727-finding-recurrence-relations-for-the-coefficients-of-a-frobenius-solution.md)

## Lesson

### Introduction

Suppose $x=0$ is a regular singular point of a second-order homogeneous linear differential equation, and the indicial equation has roots $\lambda_1$ and $\lambda_2$ with $\lambda_1 \geq \lambda_2.$

Near $x=0,$ the general solution has the form

$$


y=c_1y_1(x)+c_2y_2(x),


$$

where $c_1$ and $c_2$ are arbitrary constants and $y_1(x)$ and $y_2(x)$ are linearly independent solutions.

Taking $\lambda$ to be the larger indicial root, $\lambda=\lambda_1,$ the method of Frobenius always yields a solution of the form

$$


y_1(x)=x^{\lambda_1}\sum_{n=0}^\infty a_n(\lambda_1)x^n.


$$

Here, we write $a_n=a_n(\lambda_1)$ since these are the coefficients produced by the method when $\lambda=\lambda_1.$

We take the solution corresponding to $\lambda_1$ as $y_1,$ because it typically has the “less singular” behavior at $x=0.$

For example, suppose the indicial equation is

$$


2\lambda^2 - 5\lambda - 3 = 0.


$$

Solving for the roots, we get

$$


\begin{aligned}2𝜆^{2}−5𝜆−3 & =0 \\ (2𝜆+1)(𝜆−3) & =0 \\ 𝜆 & =−\frac{1}{2},3.\end{aligned}


$$

The larger root is $\lambda_1=3,$ so the first Frobenius solution is

$$


y_1(x)=x^3\sum_{n=0}^\infty a_n(3)x^n.


$$

### Example: Determining the First Solution in the General Solution Using the Method of Frobenius

#### Question

Consider the following differential equation.

$$


x^2y'' + x(x-4)y' - 4y = 0


$$

The general solution near $x=0$ of the differential equation is given by

$$


y = c_1y_1(x) + c_2y_2(x),


$$

where $c_1$ and $c_2$ are arbitrary constants and $y_1(x)$ and $y_2(x)$ are linearly independent solutions. According to the Frobenius method, what is the best choice for the first solution $y_1,$ where $a_n$ for $n=0,1,2,\ldots$ are constants determined by substitution?

**

#### Explanation

The general solution near a regular singular point $x=0$ of a second-order homogeneous linear differential equation with indicial roots $\lambda_1 \geq \lambda_2$ is given by

$$


y = c_1y_1(x) + c_2y_2(x),


$$

where

- $\displaystyle y_1(x) = x^{\lambda_1} \sum_{n=0}^\infty a_n(\lambda_1)x^n$ is the first Frobenius solution corresponding to the larger root of the indicial equation, and

- $a_n(\lambda_1)$ are the coefficients produced by the method when $\lambda = \lambda_1.$

We are given that the indicial equation is $\lambda^2-5\lambda+4=0.$ Solving for the roots, we get

$$


\begin{aligned}𝜆^{2}−5𝜆+4 & =0 \\ (𝜆−1)(𝜆−4) & =0 \\ 𝜆 & =1,4\end{aligned}


$$

The larger solution is $\lambda_1 = 4.$ Therefore, the first Frobenius series solution we take is

$$


y_1(x) = x^4\sum_{n=0}^\infty a_nx^n.


$$

### Example: Determining the Coefficients of the First Solution Given the Recurrence Relation

#### Question

Consider the following differential equation.

$$


5xy'' + 2y' - 6y = 0


$$

The general solution near $x=0$ of the differential equation is given by

$$


y = c_1y_1(x) + c_2y_2(x),


$$

where $c_1$ and $c_2$ are arbitrary constants and $y_1(x)$ and $y_2(x)$ are linearly independent solutions. According to the Frobenius method, what is the first solution $y_1?$

**

#### Explanation

The general solution near a regular singular point $x=0$ of a second-order homogeneous linear differential equation with indicial roots $\lambda_1 \geq \lambda_2$ is given by

$$


y = c_1y_1(x) + c_2y_2(x),


$$

where

- $\displaystyle y_1(x) = x^{\lambda_1} \sum_{n=0}^\infty a_n(\lambda_1)x^n$ is the first Frobenius solution corresponding to the larger root of the indicial equation, and

- $a_n(\lambda_1)$ are the coefficients produced by the method when $\lambda = \lambda_1.$

We are given that the indicial equation is $5\lambda^2-3\lambda=0.$ Solving for the roots, we get

$$


\begin{aligned}5𝜆^{2}−3𝜆 & =0 \\ 𝜆(5𝜆−3) & =0 \\ 𝜆 & =0,\frac{3}{5}\end{aligned}


$$

The larger solution is $\lambda_1 = \dfrac35.$ Therefore, the first Frobenius series solution we take is

$$


y_1(x) = x^{3/5}\sum_{n=0}^\infty a_nx^n.


$$

With $\lambda = \dfrac35,$ the recurrence relation is given by

$$


\begin{aligned}𝑎_{𝑛} & =\frac{6}{(\frac{3}{5}+𝑛)(5(\frac{3}{5}+𝑛)−3)}\,𝑎_{𝑛−1} \\ & =\frac{6}{5𝑛(𝑛+\frac{3}{5})}\,𝑎_{𝑛−1} \\ & =\frac{6}{𝑛(5𝑛+3)}\,𝑎_{𝑛−1}.\end{aligned}


$$

Now, with $a_0\neq0$ arbitrary, we evaluate the first three coefficients using the given recurrence relation as follows:

$$


\begin{aligned}𝑎_{0} & ≠0, \\ 𝑎_{1} & =\frac{6}{1(5⋅1+3)}\,𝑎_{0}=\frac{6}{8}𝑎_{0}=\frac{3}{4}𝑎_{0}, \\ 𝑎_{2} & =\frac{6}{2(5⋅2+3)}\,𝑎_{1}=\frac{6}{26}⋅\frac{3}{4}𝑎_{0}=\frac{9}{52}𝑎_{0},\end{aligned}


$$

Therefore, the first Frobenius solution is

$$


\begin{aligned}𝑦_{1}(𝑥) & =𝑥^{3/5}\underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}𝑎_{𝑛}𝑥^{𝑛} \\ & =𝑥^{3/5}(𝑎_{0}+\frac{3}{4}𝑎_{0}𝑥+\frac{9}{52}𝑎_{0}𝑥^{2}+⋯) \\ & =𝑎_{0}(𝑥^{3/5}+\frac{3}{4}𝑥^{8/5}+\frac{9}{52}𝑥^{13/5}+⋯).\end{aligned}


$$

### Finding the Second Linearly Independent Solution Using the Method of Frobenius

The general solution of a second-order homogeneous linear differential equation with indicial roots $\lambda_1 \geq \lambda_2$ near a regular singular point $x=0$ is

$$


y=c_1y_1(x)+c_2y_2(x),


$$

where the first Frobenius solution is

$$


y_1(x)=x^{\lambda_1}\sum_{n=0}^\infty a_n(\lambda_1)x^n.


$$

The form of the second linearly independent solution $y_2$ depends on the relationship between the indicial roots:

- **Case 1**: If $\lambda_1 - \lambda_2 \not\in \mathbb{Z},$ then the second Frobenius solution is

- **Case 2**: If $\lambda_1 = \lambda_2,$ then the second Frobenius solution is

- **Case 3**: If $\lambda_1 - \lambda_2 \in \mathbb{N},$ then the second Frobenius solution is

For example, from our previous example we found $\lambda_1=3$ and $\lambda_2=-\dfrac12.$ Then

$$


\lambda_1-\lambda_2 = 3 - \left(-\dfrac12\right)=\dfrac72,


$$

so $\lambda_1-\lambda_2\not\in\mathbb{Z},$ and we are in **Case 1**. Therefore,

$$


y_2(x)=x^{-1/2}\sum_{n=0}^\infty a_n\!\left(-\dfrac12\right)x^n.


$$

### Example: Determining the Second Linearly Independent Solution Using the Method of Frobenius

#### Question

Consider the following differential equation.

$$


x^2y'' - 5xy' + (3x+9)y = 0


$$

The general solution near $x=0$ of the differential equation above is given by

$$


y = c_1x^3\sum_{n=0}^\infty a_nx^n + c_2y_2(x),


$$

where $c_1$ and $c_2$ are arbitrary constants and $a_n$ are constants. What is the form of the second Frobenius solution $y_2,$ where $b_n$ for $n \geq 0$ are the constant coefficients of the $n$th term determined by substitution?

**

#### Explanation

The general solution near a regular singular point $x=0$ of a second-order homogeneous linear differential equation with indicial roots $\lambda_1 \geq \lambda_2$ is given by

$$


y = c_1y_1(x) + c_2y_2(x),


$$

where

$$


\displaystyle y_1(x) = x^{\lambda_1} \sum_{n=0}^\infty a_n(\lambda_1)x^n


$$

is the first Frobenius solution, and the second Frobenius solution is determined as follows:

- ****: If $\lambda_1 - \lambda_2 \not\in \mathbb{Z},$ then $\displaystyle y_2(x) = x^{\lambda_2} \sum_{n=0}^\infty a_n(\lambda_2)x^n.$

- ****: If $\lambda_1 = \lambda_2,$ then $\displaystyle y_2(x) = y_1(x)\ln x + x^{\lambda_1} \sum_{n=0}^\infty b_nx^n.$

- ****: If $\lambda_1 - \lambda_2 \in \mathbb{N},$ then $\displaystyle y_2(x) = b_{-1}y_1(x)\ln x + x^{\lambda_2}\sum_{n=0}^\infty b_nx^n.$

We are given that the indicial equation is $\lambda^2 - 6\lambda + 9 = 0.$ Solving for the roots, we get

$$


\begin{aligned}𝜆^{2}−6𝜆+9 & =0 \\ (𝜆−3)^{2} & =0 \\ 𝜆 & =3\end{aligned}


$$

The solution $\lambda=3$ is a double root. So, the indicial roots are equal $\lambda_1 = \lambda_2 = 3.$ Therefore, the first Frobenius series solution we take is

$$


y_1(x) = x^3\sum_{n=0}^\infty a_nx^n.


$$

Now, since the roots are equal, the second solution is given by

$$


y_2(x) = y_1(x)\ln x + x^3 \sum_{n=0}^\infty b_nx^n,


$$

where the constants $b_n$ are found by substitution.
