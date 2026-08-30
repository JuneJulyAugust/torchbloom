# Solving Homogeneous Systems of ODEs With Complex Eigenvalues

Source: https://www.mathacademy.com/topics/2819?courseId=61
Topic ID: 2819

## Prerequisites

- [Euler's Formula](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/898-euler-s-formula.md)
- [Solving Homogeneous Systems of ODEs With Distinct Eigenvalues and Initial Conditions](./2088-solving-homogeneous-systems-of-odes-with-distinct-eigenvalues-and-initial-conditions.md)
- [Finding Complex Eigenvectors of Real 2x2 Matrices](../linear-algebra/3574-finding-complex-eigenvectors-of-real-2x2-matrices.md)

## Lesson

### Introduction

For a $2 \times 2$ matrix differential equation

$$


\mathbf{x}'(t) = A \mathbf{x}(t),


$$

we know that if $A$ has distinct eigenvalues, the general solution is

$$


\mathbf{x}(t) = c_1{\color{black}\mathbf{v}_1} e^{{\color{black}\lambda_1} t} + c_2{\color{black}\mathbf{v}_2} e^{{\color{black}\lambda_2} t}.


$$

This formula works even when the eigenvalues $\lambda_1, \lambda_2$ are complex. However, using it directly requires working with complex exponentials, which can be cumbersome.

A more direct method is to find just *one* of the complex solutions, say $\mathbf x_1(t) = \mathbf{v}_1 e^{{\color{black}\lambda_1} t},$ and separate it into its *real and imaginary parts*.

$$


\begin{aligned}𝐱_{1}(𝑡) & =𝐯_{1}𝑒^{𝜆_{1}𝑡} \\ & =\underset{Real Part}{\underset{}{𝐰_{1}(𝑡)}}\,+\,i\,\,\,\underset{Imaginary Part}{\underset{}{𝐰_{2}(𝑡)}}\end{aligned}


$$

The general *real-valued* solution is then a linear combination of these two parts:

$$


\mathbf x(t) = c_1 \mathbf w_1(t) + c_2 \mathbf w_2(t)


$$

**Note:** This method may seem surprising. Why can we construct the general solution using only *one* of the complex solutions, $\mathbf x_1(t)?$

The reason is that the second solution, $\mathbf x_2(t),$ doesn't provide any new information. For a real matrix $A,$ the complex eigenvalues and eigenvectors come in *conjugate pairs*, which means $\mathbf x_2(t)$ is simply the complex conjugate of $\mathbf x_1(t).$

Since $\mathbf x_2(t) = \mathbf w_1 (t) - \textrm{i} \, \mathbf w_2(t),$ it is also a linear combination of the real and imaginary parts of $\mathbf x_1(t).$

To build our general solution, we just need two *linearly independent* real solutions. The key facts are the following:

- For a system with complex eigenvalues, the real part $\mathbf w_1(t)$ and the imaginary part $\mathbf w_2(t)$ are *always* linearly independent.

- Since they are two linearly independent solutions, they can form the basis for the general solution.

So, we can use them directly and bypass the need to work with $\mathbf x_2(t)$ at all.

Let's see a concrete example.

### Example: Finding the General Solution to a System of Linear Equations: Purely Imaginary Eigenvalues

#### Question

$$


[\begin{aligned}1 & −1 \\ 2 & −1\end{aligned}]


$$

Consider the system of linear differential equations above. Find the unknown function $f(t)$ in the general solution to the system, shown below.

$$


[\begin{aligned}cos⁡𝑡−sin⁡𝑡 \\ 2cos⁡𝑡\end{aligned}]


$$

**

#### Explanation

We need to find the eigenvalues and associated eigenvectors of the matrix $[\begin{aligned}1 & −1 \\ 2 & −1\end{aligned}]$

We are given the eigenvalue $\lambda_1 = \textrm{i}$ and the corresponding eigenvector $[\begin{aligned}1+i \\ 2\end{aligned}]$

**** The eigenvector corresponding to the second eigenvalue $\lambda_2 = \overline{\lambda}_1$ is $\mathbf{v}_2 = \overline{\mathbf{v}}_1.$ But we do not require this eigenvector for solving our system.

The solution that we obtain for the eigenvalue $\lambda_1 = \textrm{i}$ and its associated eigenvector is

$$


[\begin{aligned}1+i \\ 2\end{aligned}]


$$

We now express this as a real function. Using Euler's formula, we obtain

$$


\begin{aligned}𝐱_{1}(𝑡) & =[\begin{aligned}1+i \\ 2\end{aligned}]𝑒^{i𝑡} \\ & =[\begin{aligned}1+i \\ 2\end{aligned}]⋅(cos⁡𝑡+isin⁡𝑡) \\ & =[\begin{aligned}cos⁡𝑡+isin⁡𝑡+icos⁡𝑡−sin⁡𝑡 \\ 2cos⁡𝑡+2isin⁡𝑡\end{aligned}] \\ & =[\begin{aligned}(cos⁡𝑡−sin⁡𝑡)+i(cos⁡𝑡+sin⁡𝑡) \\ 2cos⁡𝑡+2isin⁡𝑡\end{aligned}] \\ & =[\begin{aligned}cos⁡𝑡−sin⁡𝑡 \\ 2cos⁡𝑡\end{aligned}]+i[\begin{aligned}cos⁡𝑡+sin⁡𝑡 \\ 2sin⁡𝑡\end{aligned}] \\ & =𝐰_{1}(𝑡)+i𝐰_{2}(𝑡).\end{aligned}


$$

The vectors $\mathbf w_1$ and $\mathbf w_2$ are linearly independent. Therefore, the general solution of the system is

$$


\begin{aligned}𝐱(𝑡) & =𝑐_{1}𝐰_{1}(𝑡)+𝑐_{2}𝐰_{2}(𝑡) \\ & =𝑐_{1}[\begin{aligned}cos⁡𝑡−sin⁡𝑡 \\ 2cos⁡𝑡\end{aligned}]+𝑐_{2}[\begin{aligned}cos⁡𝑡+sin⁡𝑡 \\ 2sin⁡𝑡\end{aligned}].\end{aligned}


$$

Finally, $f(t) = \cos{t} + \sin{t}.$

### Example: Solving an Initial Value Problem: Purely Imaginary Eigenvalues

#### Question

Solve the initial value problem

$$


[\begin{aligned}2 & −4 \\ 2 & −2\end{aligned}]


$$

**

#### Explanation

We need to find the eigenvalues and associated eigenvectors of the matrix $[\begin{aligned}2 & −4 \\ 2 & −2\end{aligned}]$

We are given the eigenvalue $\lambda_1 = 2\textrm{i}$ and the corresponding eigenvector $[\begin{aligned}1+i \\ 1\end{aligned}]$

**** The eigenvector corresponding to the second eigenvalue $\lambda_2 = \overline{\lambda}_1$ is $\mathbf{v}_2 = \overline{\mathbf{v}}_1.$ But we do not require this eigenvector for solving our system.

The solution that we obtain for the eigenvalue $\lambda_1 = 2\textrm{i}$ and its associated eigenvector is

$$


[\begin{aligned}1+i \\ 1\end{aligned}]


$$

We now express this as a real function. Using Euler's formula, we obtain

$$


\begin{aligned}𝐱_{1}(𝑡) & =[\begin{aligned}1+i \\ 1\end{aligned}]𝑒^{2i𝑡} \\ & =[\begin{aligned}1+i \\ 1\end{aligned}](cos⁡(2𝑡)+isin⁡(2𝑡)) \\ & =[\begin{aligned}cos⁡(2𝑡)+isin⁡(2𝑡)+icos⁡(2𝑡)−sin⁡(2𝑡) \\ cos⁡(2𝑡)+isin⁡(2𝑡)\end{aligned}] \\ & =[\begin{aligned}(cos⁡(2𝑡)−sin⁡(2𝑡))+i(cos⁡(2𝑡)+sin⁡(2𝑡)) \\ cos⁡(2𝑡)+isin⁡(2𝑡)\end{aligned}] \\ & =[\begin{aligned}cos⁡(2𝑡)−sin⁡(2𝑡) \\ cos⁡(2𝑡)\end{aligned}]+i[\begin{aligned}cos⁡(2𝑡)+sin⁡(2𝑡) \\ sin⁡(2𝑡)\end{aligned}] \\ & =𝐰_{1}(𝑡)+i𝐰_{2}(𝑡).\end{aligned}


$$

The vectors $\mathbf w_1$ and $\mathbf w_2$ are linearly independent. Therefore, the general solution of the system is

$$


\begin{aligned}𝐱(𝑡) & =𝑐_{1}𝐰_{1}(𝑡)+𝑐_{2}𝐰_{2}(𝑡) \\ & =𝑐_{1}[\begin{aligned}cos⁡(2𝑡)−sin⁡(2𝑡) \\ cos⁡(2𝑡)\end{aligned}]+𝑐_{2}[\begin{aligned}cos⁡(2𝑡)+sin⁡(2𝑡) \\ sin⁡(2𝑡)\end{aligned}].\end{aligned}


$$

Now, we need to find the values of $c_1$ and $c_2$ using the initial condition $[\begin{aligned}−1 \\ 1\end{aligned}]$ Substituting $t=0$ into the general solution gives

$$


\begin{aligned}𝐱(0) & =𝑐_{1}[\begin{aligned}1 \\ 1\end{aligned}]+𝑐_{2}[\begin{aligned}1 \\ 0\end{aligned}] \\ [\begin{aligned}−1 \\ 1\end{aligned}] & =[\begin{aligned}𝑐_{1}+𝑐_{2} \\ 𝑐_{1}\end{aligned}] \\ [\begin{aligned}𝑐_{1} \\ 𝑐_{2}\end{aligned}] & =[\begin{aligned}1 \\ −2\end{aligned}].\end{aligned}


$$

Finally, the solution to our initial value problem is given by

$$


\begin{aligned}𝐱(𝑡) & =1[\begin{aligned}cos⁡(2𝑡)−sin⁡(2𝑡) \\ cos⁡(2𝑡)\end{aligned}]−2[\begin{aligned}cos⁡(2𝑡)+sin⁡(2𝑡) \\ sin⁡(2𝑡)\end{aligned}] \\ & =[\begin{aligned}−cos⁡(2𝑡)−3sin⁡(2𝑡) \\ cos⁡(2𝑡)−2sin⁡(2𝑡)\end{aligned}].\end{aligned}


$$

### Example: Finding the General Solution to a System of Linear Equations: Complex Eigenvalues

#### Question

$$


[\begin{aligned}1 & −1 \\ 1 & 1\end{aligned}]


$$

Consider the system of linear differential equations above. Find the unknown function $f(t)$ in the general solution to the system, shown below.

$$


[\begin{aligned}−sin⁡𝑡 \\ cos⁡𝑡\end{aligned}]


$$

**

#### Explanation

We need to find the eigenvalues and associated eigenvectors of the matrix $[\begin{aligned}1 & −1 \\ 1 & 1\end{aligned}]$

We are given that the eigenvalue is $\lambda_1=1+\textrm{i}.$

Let's go through the process of finding the eigenvectors. For $\lambda_1 =1+\textrm{i},$ we get

$$


[\begin{aligned}−i & −1 \\ 1 & −i\end{aligned}]


$$

So, we get an eigenvector $[\begin{aligned}i \\ 1\end{aligned}]$

**** The eigenvector corresponding to the second eigenvalue $\lambda_2 = \overline{\lambda}_1$ is $\mathbf{v}_2 = \overline{\mathbf{v}}_1.$ But we do not require this eigenvector for solving our system.

The solution that we obtain for the eigenvalue $\lambda_1 = 1+\textrm{i}$ and its associated eigenvector is

$$


[\begin{aligned}i \\ 1\end{aligned}]


$$

We now separate this solution into its real and imaginary parts. Using Euler's formula, we obtain

$$


\begin{aligned}𝐱_{1}(𝑡) & =[\begin{aligned}i \\ 1\end{aligned}]𝑒^{(1+i)𝑡} \\ & =[\begin{aligned}i \\ 1\end{aligned}]𝑒^{𝑡}(cos⁡𝑡+isin⁡𝑡) \\ & =[\begin{aligned}i(𝑒^{𝑡}cos⁡𝑡)−𝑒^{𝑡}sin⁡𝑡 \\ 𝑒^{𝑡}cos⁡𝑡+i(𝑒^{𝑡}sin⁡𝑡)\end{aligned}] \\ & =[\begin{aligned}−sin⁡𝑡 \\ cos⁡𝑡\end{aligned}]𝑒^{𝑡}+i[\begin{aligned}cos⁡𝑡 \\ sin⁡𝑡\end{aligned}]𝑒^{𝑡} \\ & =𝐰_{1}(𝑡)+i𝐰_{2}(𝑡).\end{aligned}


$$

The vectors $\mathbf w_1$ and $\mathbf w_2$ are linearly independent. Therefore, the general solution of the system is

$$


\begin{aligned}𝐱(𝑡) & =𝑐_{1}𝐰_{1}(𝑡)+𝑐_{2}𝐰_{2}(𝑡) \\ & =𝑐_{1}[\begin{aligned}−sin⁡𝑡 \\ cos⁡𝑡\end{aligned}]𝑒^{𝑡}+𝑐_{2}[\begin{aligned}cos⁡𝑡 \\ sin⁡𝑡\end{aligned}]𝑒^{𝑡}.\end{aligned}


$$

Finally, $f(t) = \cos{t}.$

### Example: Solving an Initial Value Problem: Complex Eigenvalues

#### Question

Solve the initial value problem

$$


[\begin{aligned}3 & −1 \\ 1 & 3\end{aligned}]


$$

**

#### Explanation

We need to find the eigenvalues and associated eigenvectors of the matrix $[\begin{aligned}3 & −1 \\ 1 & 3\end{aligned}]$

We are given that the eigenvalue is $\lambda_1=3+\textrm{i}.$

Let's go through the process of finding the eigenvectors. For $\lambda_1 =3+\textrm{i},$ we get

$$


[\begin{aligned}−i & −1 \\ 1 & −i\end{aligned}]


$$

So, we get an eigenvector $[\begin{aligned}i \\ 1\end{aligned}]$

**** The eigenvector corresponding to the second eigenvalue $\lambda_2 = \overline{\lambda}_1$ is $\mathbf{v}_2 = \overline{\mathbf{v}}_1.$ But we do not require this eigenvector for solving our system.

The solution that we obtain for the eigenvalue $\lambda_1 = 3 + \textrm{i}$ and its associated eigenvector is

$$


[\begin{aligned}i \\ 1\end{aligned}]


$$

We now express this as a real function. Using Euler's formula, we obtain

$$


\begin{aligned}𝐱_{1}(𝑡) & =[\begin{aligned}i \\ 1\end{aligned}]𝑒^{(3+i)𝑡} \\ & =[\begin{aligned}i \\ 1\end{aligned}]𝑒^{3𝑡}(cos⁡𝑡+isin⁡𝑡) \\ & =[\begin{aligned}i(𝑒^{3𝑡}cos⁡𝑡)−𝑒^{3𝑡}sin⁡𝑡 \\ 𝑒^{3𝑡}cos⁡𝑡+i(𝑒^{3𝑡}sin⁡𝑡)\end{aligned}] \\ & =[\begin{aligned}−sin⁡𝑡 \\ cos⁡𝑡\end{aligned}]𝑒^{3𝑡}+i[\begin{aligned}cos⁡𝑡 \\ sin⁡𝑡\end{aligned}]𝑒^{3𝑡} \\ & =𝐰_{1}(𝑡)+i𝐰_{2}(𝑡).\end{aligned}


$$

The vectors $\mathbf w_1$ and $\mathbf w_2$ are linearly independent. Therefore, the general solution of the system is

$$


\begin{aligned}𝐱(𝑡) & =𝑐_{1}𝐰_{1}(𝑡)+𝑐_{2}𝐰_{2}(𝑡) \\ & =𝑐_{1}[\begin{aligned}−sin⁡𝑡 \\ cos⁡𝑡\end{aligned}]𝑒^{3𝑡}+𝑐_{2}[\begin{aligned}cos⁡𝑡 \\ sin⁡𝑡\end{aligned}]𝑒^{3𝑡}.\end{aligned}


$$

Now, we need to find the values of $c_1$ and $c_2$ using the initial condition $[\begin{aligned}−3 \\ 1\end{aligned}]$ Substituting $t=0$ into the general solution gives

$$


\begin{aligned}𝐱(0) & =𝑐_{1}[\begin{aligned}0 \\ 1\end{aligned}]+𝑐_{2}[\begin{aligned}1 \\ 0\end{aligned}] \\ [\begin{aligned}−3 \\ 1\end{aligned}] & =[\begin{aligned}𝑐_{2} \\ 𝑐_{1}\end{aligned}].\end{aligned}


$$

Finally, the solution to our initial value problem is given by

$$


\begin{aligned}𝐱(𝑡) & =1[\begin{aligned}−sin⁡𝑡 \\ cos⁡𝑡\end{aligned}]𝑒^{3𝑡}−3[\begin{aligned}cos⁡𝑡 \\ sin⁡𝑡\end{aligned}]𝑒^{3𝑡} \\ & =[\begin{aligned}−sin⁡𝑡−3cos⁡𝑡 \\ cos⁡𝑡−3sin⁡𝑡\end{aligned}]𝑒^{3𝑡}.\end{aligned}


$$
