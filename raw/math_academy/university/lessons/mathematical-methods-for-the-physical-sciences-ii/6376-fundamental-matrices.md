# Fundamental Matrices

Source: https://www.mathacademy.com/topics/6376?courseId=155
Topic ID: 6376

## Prerequisites

- [Solving Homogeneous Systems of ODEs With Distinct Eigenvalues and Initial Conditions](./2088-solving-homogeneous-systems-of-odes-with-distinct-eigenvalues-and-initial-conditions.md)
- [Matrix Exponentials](./6375-matrix-exponentials.md)

## Lesson

### Introduction

Consider the homogeneous linear system

$$


\mathbf{x}' = A\mathbf{x},


$$

where $A$ is an $n\times n$ matrix.

A **fundamental matrix** for this system is an $n\times n$ matrix $\Phi(t)$ whose columns are $n$ linearly independent solutions of the system.

If $\mathbf{x}_1(t),\dots,\mathbf{x}_n(t)$ are linearly independent solutions, then one fundamental matrix is

$$


\Phi(t)=\big[\mathbf{x}_1(t),\dots,\mathbf{x}_n(t)\big].


$$

**Note:** The columns of $\Phi(t)$ can be written in any order.

Let's see an example.

### Example: Constructing a Fundamental Matrix

#### Question

$$


[\begin{aligned}5 & 1 \\ 0 & 5\end{aligned}]


$$

Consider the system of linear ODEs and two of its linearly independent solutions $\mathbf x_1$ and $\mathbf x_2,$ shown above. Find the fundamental matrix for the system.

#### Explanation

Given a linear system $\mathbf{x}' = A \mathbf{x},$ where $A$ is an $n \times n$ matrix, a ** $\Phi(t)$ of the system is an $n \times n$ matrix whose columns are linearly independent solutions of the system.

In our cases, we have a $2 \times 2$ system. We are also given that the two linearly independent solutions of the system are the following:

$$


\begin{aligned}𝐱_{1}(𝑡) & =[\begin{aligned}4 \\ 0\end{aligned}]𝑒^{5𝑡}=[\begin{aligned}4𝑒^{5𝑡} \\ 0\end{aligned}] \\ 𝐱_{2}(𝑡) & =[\begin{aligned}4𝑡 \\ 4\end{aligned}]𝑒^{5𝑡}=[\begin{aligned}4𝑡𝑒^{5𝑡} \\ 4𝑒^{5𝑡}\end{aligned}]\end{aligned}


$$

Therefore, our fundamental could be written as

$$


[\begin{aligned}4𝑒^{5𝑡} & 4𝑡𝑒^{5𝑡} \\ 0 & 4𝑒^{5𝑡}\end{aligned}]


$$

**** The columns of $\Phi$ can be written in any order.

### Properties of the Fundamental Matrix

Again, let $\Phi(t)$ be a fundamental matrix for the linear system

$$


\mathbf{x}' = A\mathbf{x},


$$

where $A$ is an $n\times n$ matrix. The fundamental matrices have the following important properties.

1. *Satisfies the underlying system*. Indeed, since each column of $\Phi(t)$ is a solution of the system, we have

2. *Invertibility*. The columns of $\Phi(t)$ are linearly independent for all $t,$ so for all $t.$ In particular, $\Phi(t)$ is invertible for all $t.$

3. *Representation of solutions*. Every solution $\mathbf{x}(t)$ of the system can be written in the form where $\mathbf{c}$ is a constant vector.

4. *Non-uniqueness*. If $C$ is any invertible constant matrix, then is also a fundamental matrix for the same system.

We'll now get some practice.

### Example: Proving Properties of a Fundamental Matrix

#### Question

Consider the system $\mathbf{x}'(t) = A \mathbf{x}(t),$ where $A$ is a constant $2 \times 2$ matrix. Let $\Phi(t)$ be a fundamental matrix for this system. A derivation showing that $\Phi(t)$ satisfies the matrix differential equation $\Phi'(t) = A \, \Phi(t)$ is given below.

**

$\textrm{L1}{:}\;$ Let $\Phi(t) = \big[\mathbf{x}_1(t), \: \mathbf{x}_2(t) \big]$

$\textrm{L2}{:}\;$ $\mathbf{x}_1'(t) = A \mathbf{x}_1(t)$

$\textrm{L3}{:}\;$ $\mathbf{x}_2'(t) = A \mathbf{x}_2(t)$

$\textrm{L4}{:}\;$ $\Phi'(t) = \big[\mathbf{x}_1'(t), \: \mathbf{x}_2'(t) \big]$

$\textrm{L5}{:}\;$ $\Phi'(t) = \big[A \mathbf{x}_1(t), \: A \mathbf{x}_2(t) \big]$

$\textrm{L6}{:}\;$ $\Phi'(t) = A \big[\mathbf{x}_1(t), \: \mathbf{x}_2(t) \big]$

$\textrm{L7}{:}\;$ $\Phi'(t) = A \Phi(t)$

Select the correct options in the following reasoning.

$\quad$ Line $\textrm{L2}$ follows from the fact that $𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴$.

$\quad$ Line $\textrm{L6}$ follows from line $\textrm{L5}$ by $𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴$.

$\quad$ Line $\textrm{L7}$ follows from line $\textrm{L6}$ and substitution from line $𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴$.

#### Explanation

Let's justify each of the selected steps.

- We first consider line $\textrm{L2}.$ Since $\Phi(t)$ is a fundamental matrix, its columns $\mathbf{x}_1(t)$ and $\mathbf{x}_2(t)$ are linearly independent solutions of the homogeneous system $\mathbf{x}'(t) = A \mathbf{x}(t).$ This means that each column satisfies the differential equation. In particular, Therefore, $\textrm{L2}$ follows from the fact that $\mathbf{x}_1$ is a solution of the system.

- Next, we consider lines $\textrm{L5}$ and $\textrm{L6}.$ We now factor the matrix $A$ on the left: Therefore, $\textrm{L6}$ follows from $\textrm{L5}$ by factoring out $A$ on the left.

- Finally, we consider lines $\textrm{L6}$ and $\textrm{L7}.$ From $\textrm{L6}$ we have $\Phi'(t)=A\big[\mathbf{x}_1(t),\:\mathbf{x}_2(t)\big].$ Using $\Phi(t)=\big[\mathbf{x}_1(t),\:\mathbf{x}_2(t)\big]$ from $\textrm{L1},$ we substitute to obtain $\Phi'(t)=A\Phi(t).$ Thus, $\textrm{L7}$ follows from $\textrm{L6}$ by substitution from $L1.$

### Fundamental Matrices and Matrix Exponentials

For a linear system $\mathbf{x}' = A\mathbf{x}$ with constant $n\times n$ matrix $A,$ the **standard fundamental matrix** is the unique fundamental matrix $\Phi_0(t)$ that satisfies the initial condition

$$


\Phi_0(0)=I_n,


$$

where $I_n$ is the $n \times n$ identity matrix.

For constant matrices $A,$ the standard fundamental matrix is given by

$$


\Phi_0(t)=e^{At}.


$$

This matrix satisfies

$$


\Phi_0'(t)=A\,\Phi_0(t) \qquad\text{and}\qquad \Phi_0(0)=I_n.


$$

**Note:** Any other fundamental matrix $\Phi(t)$ for the same system can be written in the form

$$


\Phi(t)=\Phi_0(t)\,C,


$$

where $C$ is an invertible constant matrix.

In the next slide, we will compute the standard fundamental matrix for a specific example.

### Example: Computing Fundamental Matrices Using Matrix Exponentials

#### Question

$$


[\begin{aligned}0 & −7 \\ 7 & 0\end{aligned}]


$$

Consider the system of linear ODEs $\mathbf{x}' = A\mathbf{x}$ with the matrix $A$ shown above. Compute the **** fundamental matrix $\Phi(t)$ for this system.

#### Explanation

Suppose $A$ is a constant $n\times n$ matrix and $\mathbf x(t)$ is an $n\times 1$ column vector. The standard fundamental matrix of the linear system $\mathbf x'(t) = A\mathbf x(t),$ denoted $\Phi_0(t),$ is the unique matrix solution of the initial value problem

$$


\Phi_0'(t) = A\Phi_0(t), \quad \Phi_0(0) = I_n,


$$

where $I_n$ is the identity matrix.

Furthermore, it can be shown that $\Phi_0(t) = e^{At}.$

We have a square matrix of dimension $n=2.$ Thus,

$$


\begin{aligned}𝑒^{𝐴𝑡} & =𝛼_{1}𝐴𝑡+𝛼_{0}𝐼 \\ & =𝛼_{1}[\begin{aligned}0 & −7 \\ 7 & 0\end{aligned}]𝑡+𝛼_{0}[\begin{aligned}1 & 0 \\ 0 & 1\end{aligned}] \\ & =[\begin{aligned}𝛼_{0} & −7𝛼_{1}𝑡 \\ 7𝛼_{1}𝑡 & 𝛼_{0}\end{aligned}].\end{aligned}


$$

where $\alpha_1$ and $\alpha_0$ are constants to be determined.

Consider the polynomial $r(\lambda) = \alpha_1 \lambda + \alpha_0.$ The eigenvalues of $At$ are

$$


\lambda_1 = 7\textrm{i}t, \qquad \lambda_2 = -7\textrm{i}t,


$$

which are complex conjugates. Thus, we have the following:

$$


\begin{aligned}𝑟((7i)𝑡) & =𝑒^{(7i)𝑡} \\ 𝛼_{1}(7i)𝑡+𝛼_{0} & =cos⁡(7𝑡)+isin⁡(7𝑡) \\ 𝛼_{0}+7i𝛼_{1}𝑡 & =cos⁡(7𝑡)+isin⁡(7𝑡)\end{aligned}


$$

Now, we equate the real and imaginary parts, and solve for $\alpha_1$ and $\alpha_0{:}$

$$


\begin{aligned}\begin{aligned}𝛼_{0}=cos⁡(7𝑡) \\ 7𝛼_{1}𝑡=sin⁡(7𝑡)\end{aligned}\,⇒\,\begin{aligned}𝛼_{0}=cos⁡(7𝑡) \\ 𝛼_{1}=\frac{1}{7𝑡}sin⁡(7𝑡)\end{aligned}\end{aligned}


$$

Substituting $\alpha_1$ and $\alpha_0$ into the expressions for the required entries of $e^{At},$ we get the following:

$$


\begin{aligned}𝛼_{0} & =cos⁡(7𝑡) \\ 7𝛼_{1}𝑡 & =7⋅\frac{1}{7𝑡}sin⁡(7𝑡)⋅𝑡 \\ & =sin⁡(7𝑡)\end{aligned}


$$

Therefore,

$$


[\begin{aligned}cos⁡(7𝑡) & −sin⁡(7𝑡) \\ sin⁡(7𝑡) & cos⁡(7𝑡)\end{aligned}]


$$
