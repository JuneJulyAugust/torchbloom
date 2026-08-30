# Solving Homogeneous Systems of ODEs With Distinct Eigenvalues

Source: https://www.mathacademy.com/topics/2087?courseId=155
Topic ID: 2087

## Prerequisites

- [Properties of Diagonalization](../linear-algebra/1969-properties-of-diagonalization.md)
- [Solving Decoupled Homogeneous Systems of ODEs](./3238-solving-decoupled-homogeneous-systems-of-odes.md)

## Lesson

### Introduction

We know how to solve a system of differential equations when they're decoupled. However, most systems are not decoupled. So, how do we solve them?

Let's consider a general linear system of two differential equations:

$$


\begin{aligned}𝑥_{′1}^{}(𝑡)=𝑎\,𝑥_{1}(𝑡)+𝑏\,𝑥_{2}(𝑡) \\ 𝑥_{′2}^{}(𝑡)=𝑐\,𝑥_{1}(𝑡)+𝑑\,𝑥_{2}(𝑡)\end{aligned}


$$

It turns out that if the matrix $A$ has two *distinct real eigenvalues* $\lambda_1$ and $\lambda_2$, then $A$ is diagonalizable and we can solve the system.

If the eigenvectors corresponding to $\color{red}\lambda_1$ and $\color{blue}\lambda_2$ are ${\color{red}\mathbf{v}_1}$ and ${\color{blue}\mathbf{v}_2},$ respectively, then the general solution to our original system can be written as

$$


\mathbf{x}(t) = c_1{\color{red}\mathbf{v}_1} e^{{\color{red}\lambda_1} t} + c_2{\color{blue}\mathbf{v}_2} e^{{\color{blue}\lambda_2} t}, \qquad c_1,c_2 \in \mathbb{R}.


$$

This result is true for any $n \times n$ system with $n$ distinct eigenvalues. We'll prove this result for a $2\times 2$ system at the end of the lesson.

Now, let's see some concrete examples.

### Example: Finding the General Solution Given the Eigenvalues and Eigenvectors of the Corresponding Matrix

#### Question

Let $[\begin{aligned}1 \\ −2\end{aligned}]$ and $[\begin{aligned}2 \\ 5\end{aligned}]$ be eigenvectors of a matrix $A$ that correspond to eigenvalues $\lambda_1=-1$ and $\lambda_2=2,$ respectively. What is the general solution of the matrix differential equation $\mathbf{x}'(t)=A\mathbf{x}(t)?$

#### Explanation

Given a system of first-order linear ODEs in the form

$$


\mathbf{x}'(t)=A\mathbf{x}(t),


$$

where $A$ has two distinct eigenvalues ${\color{red}\lambda_1}, {\color{blue}\lambda_2}$ with corresponding eigenvectors ${\color{red}\mathbf{v}_1}$ and ${\color{blue}\mathbf{v}_2},$ the formula for the general solution is

$$


\mathbf{x}(t) = c_1{\color{red}\mathbf{v}_1} e^{{\color{red}\lambda_1} t} + c_2{\color{blue}\mathbf{v}_2} e^{{\color{blue}\lambda_2} t}, \qquad c_1,c_2 \in \mathbb{R}.


$$

Therefore, the general solution of our matrix differential equation is

$$


\begin{aligned}𝐱(𝑡) & =𝑐_{1}[\begin{aligned}1 \\ −2\end{aligned}]𝑒^{−𝑡}+𝑐_{2}[\begin{aligned}2 \\ 5\end{aligned}]𝑒^{2𝑡},\,𝑐_{1},𝑐_{2}∈ℝ.\end{aligned}


$$

### Example: Finding the General Solution to a Linear System of Differential Equations

#### Question

Find the general solution to the system of differential equations

$$


\begin{aligned}𝑥_{′1}^{}(𝑡)=6𝑥_{1}(𝑡)+7𝑥_{2}(𝑡) \\ 𝑥_{′2}^{}(𝑡)=−3𝑥_{1}(𝑡)−4𝑥_{2}(𝑡).\end{aligned}


$$

**

#### Explanation

First, we write down the matrix differential equation $\mathbf{x}'(t)=A\mathbf{x}(t)$ for the given system:

$$


[\begin{aligned}𝑥_{′1}^{}(𝑡) \\ 𝑥_{′2}^{}(𝑡)\end{aligned}]


$$

We need to find the eigenvalues and the eigenvectors of the matrix $A.$

- We are given that the eigenvalues are

- Let's go through the process of finding the eigenvectors. For $\lambda_1 =-1,$ we get So, we get an eigenvector $[\begin{aligned}−1 \\ 1\end{aligned}]$ For $\lambda_2 =3,$ we get So, we get an eigenvector $[\begin{aligned}7 \\ −3\end{aligned}]$

Thus, the general solution to the given system is

$$


\begin{aligned}𝐱(𝑡) & =𝑐_{1}𝐯_{1}𝑒^{𝜆_{1}𝑡}+𝑐_{2}𝐯_{2}𝑒^{𝜆_{2}𝑡} \\ & =𝑐_{1}[\begin{aligned}−1 \\ 1\end{aligned}]𝑒^{−𝑡}+𝑐_{2}[\begin{aligned}7 \\ −3\end{aligned}]𝑒^{3𝑡},\,𝑐_{1},𝑐_{2}∈ℝ.\end{aligned}


$$

### Decoupling a Linear System of Differential Equations

We've seen how to solve a decoupled system of differential equations. Our goal now is to understand in more detail why this method works.

Let's consider our general linear system of two differential equations once again:

We will show that if the matrix $A$ is diagonalizable, we can convert it into an equivalent decoupled system.

If $A$ is diagonalizable, it has $2$ linearly independent eigenvectors ${\color{red}\mathbf{v}_1}$ and ${\color{blue}\mathbf{v}_2}.$ We use these to form the *change of variables matrix* $E,$ given by

$$


\begin{aligned}| & | \\ 𝐯_{1} & 𝐯_{2} \\ | & |\end{aligned}


$$

Because the columns are linearly independent, $E$ is invertible. Then, the substitution

$$


\mathbf{x}(t) = E\mathbf{u}(t)


$$

will transform our original system of differential equations into a decoupled one, as follows:

$$


\begin{aligned}𝐱^{′}(𝑡) & =𝐴𝐱(𝑡) \\ \frac{d}{d𝑡}(𝐸𝐮(𝑡)) & =𝐴(𝐸𝐮(𝑡)) \\ 𝐸𝐮^{′}(𝑡) & =𝐴𝐸𝐮(𝑡) \\ 𝐮^{′}(𝑡) & =𝐸^{−1}𝐴𝐸\,𝐮(𝑡)\end{aligned}


$$

Note that

$$


[\begin{aligned}𝜆_{1} & 0 \\ 0 & 𝜆_{2}\end{aligned}]


$$

is a diagonal matrix, and ${\color{red}\lambda_1},$ ${\color{blue}\lambda_2}$ are the eigenvalues of $A$ corresponding to ${\color{red}\mathbf{v}_1}$ and ${\color{blue}\mathbf{v}_2}.$

Following these steps, we now have the *decoupled system*

Here, the matrix $D = E^{-1}$ is sometimes called the **decoupling matrix**.

Let's see a concrete example.

### Example: Determining the Decoupling Substitution of a Linear System of Differential Equations

#### Question

Find the substitution that will decouple the following system of differential equations:

$$


\begin{aligned}𝑥_{′1}^{}(𝑡)=−3𝑥_{1}(𝑡) \\ 𝑥_{′2}^{}(𝑡)=−3𝑥_{1}(𝑡)+𝑥_{2}(𝑡)\end{aligned}


$$

#### Explanation

Let's construct the matrix differential equation $\mathbf{x}'(t)=A\mathbf{x}(t)$ for the given system:

$$


[\begin{aligned}𝑥_{′1}^{}(𝑡) \\ 𝑥_{′2}^{}(𝑡)\end{aligned}]


$$

We need to find the eigenvalues and the eigenvectors of the matrix $A.$

- Since $A$ is lower-triangular, the eigenvalues are

- Let's go through the process of finding the eigenvectors. For $\lambda_1 =-3,$ we get So, we get an eigenvector $[\begin{aligned}4 \\ 3\end{aligned}]$ For $\lambda_2 =1,$ we get So, we get an eigenvector $[\begin{aligned}0 \\ 1\end{aligned}]$

Therefore, we have $[\begin{aligned}4 & 0 \\ 3 & 1\end{aligned}]$

Finally, the change of variables that decouples the system is given by $\mathbf{x}(t) = E\mathbf{u}(t),$ or equivalently,

$$


\begin{aligned}𝑥_{1}(𝑡)=4𝑢_{1}(𝑡) \\ 𝑥_{2}(𝑡)=3𝑢_{1}(𝑡)+𝑢_{2}(𝑡).\end{aligned}


$$

### The Proof of the Formula For a General System

Consider the $2\times 2$ matrix differential equation

$$


\mathbf{x}'(t) = A \mathbf{x}(t).


$$

Assume that $A$ is diagonalizable and has eigenvectors ${\color{red}\mathbf{v}_1}$ and ${\color{blue}\mathbf{v}_2}$ with corresponding eigenvalues ${\color{red}\lambda_1}$ and ${\color{blue}\lambda_2},$ respectively.

We've been using the general solution formula

$$


\mathbf{x}(t) = c_1{\color{red}\mathbf{v}_1} e^{{\color{red}\lambda_1} t} + c_2{\color{blue}\mathbf{v}_2} e^{{\color{blue}\lambda_2} t}.


$$

But where does this formula come from? First, remember that the substitution

$$


\begin{aligned}| & | \\ 𝐯_{1} & 𝐯_{2} \\ | & |\end{aligned}


$$

transforms the matrix differential equation into the equivalent decoupled system

$$


[\begin{aligned}𝜆_{1} & 0 \\ 0 & 𝜆_{2}\end{aligned}]


$$

We can solve this new decoupled system using the formula

$$


\begin{aligned}𝐮(𝑡) & =𝑐_{1}[\begin{aligned}1 \\ 0\end{aligned}]𝑒^{𝜆_{1}𝑡}+𝑐_{2}[\begin{aligned}0 \\ 1\end{aligned}]𝑒^{𝜆_{2}𝑡},\,𝑐_{1},𝑐_{2}∈ℝ.\end{aligned}


$$

Using the substitution $\mathbf{x}(t)=E\mathbf{u}(t)$, we can transform the system back to the variable $\mathbf x(t),$ as follows:

$$


\begin{aligned}𝐱(𝑡) & =𝐸𝐮(𝑡) \\ & =𝐸(𝑐_{1}[\begin{aligned}1 \\ 0\end{aligned}]𝑒^{𝜆_{1}𝑡}+𝑐_{2}[\begin{aligned}0 \\ 1\end{aligned}]𝑒^{𝜆_{2}𝑡}) \\ & =𝑐_{1}𝐸[\begin{aligned}1 \\ 0\end{aligned}]𝑒^{𝜆_{1}𝑡}+𝑐_{2}𝐸[\begin{aligned}0 \\ 1\end{aligned}]𝑒^{𝜆_{2}𝑡} \\ & =𝑐_{1}𝐯_{1}𝑒^{𝜆_{1}𝑡}+𝑐_{2}𝐯_{2}𝑒^{𝜆_{2}𝑡}\end{aligned}


$$

Therefore, the general solution to our original system is given by

$$


\mathbf{x}(t) = c_1{\color{red}\mathbf{v}_1} e^{{\color{red}\lambda_1} t} + c_2{\color{blue}\mathbf{v}_2} e^{{\color{blue}\lambda_2} t}.


$$
