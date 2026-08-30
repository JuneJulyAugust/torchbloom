# Solving Homogeneous Systems of ODEs With Repeated Eigenvalues

Source: https://www.mathacademy.com/topics/2818?courseId=155
Topic ID: 2818

## Prerequisites

- [Differentiation Rules for Vector-Valued Functions](../mathematical-methods-for-the-physical-sciences-i/1738-differentiation-rules-for-vector-valued-functions.md)
- [Solving Homogeneous Systems of ODEs With Distinct Eigenvalues and Initial Conditions](./2088-solving-homogeneous-systems-of-odes-with-distinct-eigenvalues-and-initial-conditions.md)
- [Generalized Eigenvectors](../linear-algebra/2738-generalized-eigenvectors.md)

## Lesson

### Introduction

For a $2 \times 2$ system of linear differential equations

$$


\mathbf{x}'(t) = A \mathbf{x}(t),


$$

we know that if $A$ is diagonalizable and has eigenvectors ${\color{black}\mathbf{v}_1}$ and ${\color{black}\mathbf{v}_2}$ with the corresponding eigenvalues ${\color{black}\lambda_1}$ and ${\color{black}\lambda_2},$ respectively, then the general solution formula is

$$


\mathbf{x}(t) = c_1{\color{black}\mathbf{v}_1} e^{{\color{black}\lambda_1} t} + c_2{\color{black}\mathbf{v}_2} e^{{\color{black}\lambda_2} t}.


$$

But what happens if $A$ has a single repeated eigenvalue, $\lambda?$ It depends on the number of linearly independent eigenvectors corresponding to $\lambda.$

- We say that $\lambda$ is a **complete** eigenvalue if there are two linearly independent eigenvectors $\mathbf v_1$ and $\mathbf v_2$ corresponding to $\lambda.$

- We say that $\lambda$ is a **defective** (or **incomplete**) eigenvalue if there is only one linearly independent eigenvector $\mathbf v$ corresponding to $\lambda.$

This leads to two distinct cases:

- *The Complete Case.* If $\lambda$ is a *complete* eigenvalue, then there are two linearly independent eigenvectors $\mathbf v_1$ and $\mathbf v_2$ corresponding to $\lambda,$ and we can use the usual formula:

- *The Defective Case.* If $\lambda$ is a *defective* eigenvalue, there is only one linearly independent eigenvector $\mathbf v.$ We cannot use the usual formula because there are not enough eigenvectors. Instead, we must find a *generalized eigenvector* $\mathbf w,$ which is a vector that satisfies the equation The general solution is then given by the formula:

We'll explain how and why this solution comes about at the end of the lesson.

Now, let's see some concrete examples.

### Example: Finding the General Solution to a System of Linear Equations in a Complete Case

#### Question

Find the general solution to the matrix differential equation $[\begin{aligned}4 & 0 \\ 0 & 4\end{aligned}]$

#### Explanation

Given a decoupled system of first-order linear ODEs in the form

$$


[\begin{aligned}𝑥_{′1}^{}(𝑡) \\ 𝑥_{′2}^{}(𝑡)\end{aligned}]


$$

the formula for the general solution is

$$


[\begin{aligned}1 \\ 0\end{aligned}]


$$

Since the matrix of our differential equation is diagonal, the system is decoupled.

Therefore, the general solution is given by

$$


[\begin{aligned}1 \\ 0\end{aligned}]


$$

### Example: Finding the General Solution to a System of Linear Equations in a Defective Case

#### Question

Consider the system of linear differential equations given by

$$


[\begin{aligned}−4 & 1 \\ 0 & −4\end{aligned}]


$$

Given that the solution to the system can be written as

$$


[\begin{aligned}1 \\ 𝑎\end{aligned}]


$$

what is the value of $a+b?$

#### Explanation

We need to find the eigenvalues and the eigenvectors of the matrix $[\begin{aligned}−4 & 1 \\ 0 & −4\end{aligned}]$

Since $A$ is upper-triangular, the repeated eigenvalue is $\lambda=-4$ (of multiplicity two). For this eigenvalue, we get

$$


[\begin{aligned}0 & 1 \\ 0 & 0\end{aligned}]


$$

So, we get an eigenvector $[\begin{aligned}1 \\ 0\end{aligned}]$

Since we have a repeated eigenvalue $\lambda$ and only one linearly independent eigenvector $\mathbf v,$ the solution of the system of differential equations is given by

$$


\mathbf{x}(t) = c_1\mathbf{v} e^{\lambda t} + c_2 (\mathbf{v} te^{\lambda t} + \mathbf{w}e^{\lambda t} \, ),


$$

where $\mathbf{w}$ is a solution to the equation $(A - \lambda I)\mathbf{w}= \mathbf{v}.$

To find $\mathbf{w},$ we solve the equation $(A - \lambda I)\mathbf{w} = \mathbf{v}$ as follows:

$$


\begin{aligned}(𝐴−𝜆𝐼)𝐰 & =𝐯 \\ [\begin{aligned}−4+4 & 1 \\ 0 & −4+4\end{aligned}][\begin{aligned}𝑤_{1} \\ 𝑤_{2}\end{aligned}] & =[\begin{aligned}1 \\ 0\end{aligned}] \\ [\begin{aligned}0 & 1 \\ 0 & 0\end{aligned}][\begin{aligned}𝑤_{1} \\ 𝑤_{2}\end{aligned}] & =[\begin{aligned}1 \\ 0\end{aligned}]\end{aligned}


$$

The last equality allows us to form the following system of equations:

$$


\begin{aligned}0𝑤_{1}+1𝑤_{2}=1 \\ 0𝑤_{1}+0𝑤_{2}=0\end{aligned}


$$

So, we obtain

$$


w_2 = 1.


$$

The variable $w_1$ is a free variable. Setting $w_1 = 0,$ we get

$$


[\begin{aligned}0 \\ 1\end{aligned}]


$$

Therefore, the general solution is given by

$$


[\begin{aligned}1 \\ 0\end{aligned}]


$$

Finally, we see that $a=0, b=1,$ and $a+b=1.$

### Example: Solving an Initial Value Problem in a Defective Case

#### Question

Solve the initial value problem

$$


[\begin{aligned}−1 & −8 \\ 2 & 7\end{aligned}]


$$

**

#### Explanation

We need to find the eigenvalues and the eigenvectors of the matrix $[\begin{aligned}−1 & −8 \\ 2 & 7\end{aligned}]$

We are given that the eigenvalue is $\lambda=3$ (of multiplicity two). For this eigenvalue, we get

$$


[\begin{aligned}−4 & −8 \\ 2 & 4\end{aligned}]


$$

So, we get an eigenvector $[\begin{aligned}−2 \\ 1\end{aligned}]$

Since we have a repeated eigenvalue $\lambda$ and only one linearly independent eigenvector $\mathbf v,$ the solution to the system of differential equations is given by

$$


\mathbf{x}(t) = c_1 \mathbf{v}e^{\lambda t} + c_2 (\mathbf{v}t e^{\lambda t} + \mathbf{w}e^{\lambda t}),


$$

where $\mathbf{w}$ is a solution to the equation $(A - \lambda I)\mathbf{w}= \mathbf{v}.$

To find $\mathbf{w},$ we solve the equation $(A - \lambda I)\mathbf{w} = \mathbf{v}$ as follows:

$$


\begin{aligned}(𝐴−𝜆𝐼)𝐰 & =𝐯 \\ [\begin{aligned}−1−3 & −8 \\ 2 & 7−3\end{aligned}][\begin{aligned}𝑤_{1} \\ 𝑤_{2}\end{aligned}] & =[\begin{aligned}−2 \\ 1\end{aligned}] \\ [\begin{aligned}−4 & −8 \\ 2 & 4\end{aligned}][\begin{aligned}𝑤_{1} \\ 𝑤_{2}\end{aligned}] & =[\begin{aligned}−2 \\ 1\end{aligned}]\end{aligned}


$$

The last equality allows us to form the following system of equations:

$$


\begin{aligned}−4𝑤_{1}−8𝑤_{2}=−2 \\ 2𝑤_{1}+4𝑤_{2}=1\end{aligned}


$$

Note that the first equation is a constant multiple of the second. So, we obtain

$$


w_1 =\dfrac{1}{2} - 2 w_2 .


$$

The variable $w_2$ is a free variable. Setting $w_2 = 0,$ we get $w_1 = \dfrac{1}{2},$ and therefore

$$


[\begin{aligned}\frac{1}{2} \\ 0\end{aligned}]


$$

Therefore, the general solution is given by

$$


[\begin{aligned}−2 \\ 1\end{aligned}]


$$

Now, we need to find the values of $c_1$ and $c_2$ using the initial condition $[\begin{aligned}−3 \\ 1\end{aligned}]$ Substituting $t=0$ into the general solution gives

$$


\begin{aligned}𝐱(0) & =[\begin{aligned}−2𝑐_{1}+\frac{1}{2}𝑐_{2} \\ 𝑐_{1}\end{aligned}] \\ [\begin{aligned}−3 \\ 1\end{aligned}] & =[\begin{aligned}−2𝑐_{1}+\frac{1}{2}𝑐_{2} \\ 𝑐_{1}\end{aligned}] \\ [\begin{aligned}𝑐_{1} \\ 𝑐_{2}\end{aligned}] & =[\begin{aligned}1 \\ −2\end{aligned}].\end{aligned}


$$

Finally, the solution to our initial value problem is given by

$$


\begin{aligned}𝐱(𝑡) & =[\begin{aligned}−2 \\ 1\end{aligned}]𝑒^{3𝑡}−2([\begin{aligned}−2 \\ 1\end{aligned}]𝑡𝑒^{3𝑡}+[\begin{aligned}\frac{1}{2} \\ 0\end{aligned}]𝑒^{3𝑡}) \\ & =[\begin{aligned}−3 \\ 1\end{aligned}]𝑒^{3𝑡}+[\begin{aligned}4 \\ −2\end{aligned}]𝑡𝑒^{3𝑡} \\ & =[\begin{aligned}(4𝑡−3)𝑒^{3𝑡} \\ (1−2𝑡)𝑒^{3𝑡}\end{aligned}].\end{aligned}


$$

### Justification for the Solution Formula in the Defective Case

When solving the $2\times 2$ matrix differential equation

$$


\mathbf{x}'(t) = A \mathbf{x}(t),


$$

in the case where $A$ has a single, defective eigenvalue $\lambda$ with the corresponding eigenvector $\mathbf v,$ the first fundamental solution takes the form

$$


\mathbf{x}_1(t) = \mathbf{v} e^{\lambda t},


$$

as usual, and the second fundamental solution takes the form

$$


\mathbf x_2(t) = \mathbf{v} te^{\lambda t} + \mathbf{w}e^{\lambda t}


$$

where $\mathbf{v}$ is an eigenvector of $A$ and $\mathbf w$ is a vector that satisfies $(A - \lambda I)\mathbf{w}= \mathbf{v}.$

We can see that the second fundamental solution works by substituting $\mathbf x_2(t) = \mathbf{v} te^{\lambda t} + \mathbf{w}e^{\lambda t}$ into the differential equation, as follows:

$$


\begin{aligned}𝐱_{′2}^{}(𝑡) & =𝐴𝐱_{2}(𝑡) \\ \frac{d}{d𝑡}[𝐯𝑡𝑒^{𝜆𝑡}+𝐰𝑒^{𝜆𝑡}] & =𝐴(𝐯𝑡𝑒^{𝜆𝑡}+𝐰𝑒^{𝜆𝑡}) \\ 𝐯𝑒^{𝜆𝑡}+𝜆𝐯𝑡𝑒^{𝜆𝑡}+𝜆𝐰𝑒^{𝜆𝑡} & =𝐴𝐯𝑡𝑒^{𝜆𝑡}+𝐴𝐰𝑒^{𝜆𝑡} \\ 𝐯𝑒^{𝜆𝑡}+𝜆𝐯𝑡𝑒^{𝜆𝑡}+𝜆𝐰𝑒^{𝜆𝑡} & =𝜆𝐯𝑡𝑒^{𝜆𝑡}+𝐴𝐰𝑒^{𝜆𝑡} \\ 𝐯𝑒^{𝜆𝑡}+𝜆𝐰𝑒^{𝜆𝑡} & =𝐴𝐰𝑒^{𝜆𝑡} \\ 𝐯+𝜆𝐰 & =𝐴𝐰 \\ 𝐯 & =𝐴𝐰−𝜆𝐰 \\ 𝐯 & =(𝐴−𝜆𝐼)𝐰.\end{aligned}


$$

So we conclude that $\mathbf x_2(t) = \mathbf{v} te^{\lambda t} + \mathbf{w}e^{\lambda t}$ works as a second fundamental solution provided that $\mathbf w$ is a solution to $\mathbf{v} = (A - \lambda I) \mathbf{w}.$

**Note:** By linearity, any linear combination of $\mathbf{x}_1(t)$ and $\mathbf{x}_2(t)$ is also a solution of the system. Moreover, it turns out, every solution can be written as a linear combination of $\mathbf{x}_1(t)$ and $\mathbf{x}_2(t).$ Later in the course, we’ll see why certain particular solutions can generate the entire solution set.
