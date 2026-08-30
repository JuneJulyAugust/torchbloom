# Solving Inhomogeneous Systems of ODEs Using Matrix Methods

Source: https://www.mathacademy.com/topics/6691?courseId=155
Topic ID: 6691

## Prerequisites

- [Integration Rules for Vector-Valued Functions](../mathematical-methods-for-the-physical-sciences-i/1744-integration-rules-for-vector-valued-functions.md)
- [Integrating Rates of Change](../../../ap-courses/lessons/ap-calculus-ab/2512-integrating-rates-of-change.md)
- [Solving Homogeneous Systems of ODEs Using Matrix Methods](./6690-solving-homogeneous-systems-of-odes-using-matrix-methods.md)

## Lesson

### Introduction

Matrix exponentials can be used for solving *inhomogeneous systems* of ODEs as well. Consider the system

$$


\mathbf{x}'(t)=A\mathbf{x}(t)+\mathbf{g}(t),


$$

where $A$ is a constant square matrix, and suppose we are given an initial condition $\mathbf{x}(t_0)$.

Our goal is to derive the formula for the solution $\mathbf{x}(t)$ of the system.

First, we eliminate the *inhomogeneous term* by a change of variables. We define

$$


\mathbf{y}(t)=e^{-A(t-t_0)}\mathbf{x}(t)


$$

and differentiate it using the product rule:

$$


\begin{aligned}𝐲^{′}(𝑡) & =(𝑒^{−𝐴(𝑡−𝑡_{0})})^{′}𝐱(𝑡)+𝑒^{−𝐴(𝑡−𝑡_{0})}𝐱^{′}(𝑡) \\ & =(−𝐴)𝑒^{−𝐴(𝑡−𝑡_{0})}𝐱(𝑡)+𝑒^{−𝐴(𝑡−𝑡_{0})}(𝐴𝐱(𝑡)+𝐠(𝑡)) \\ & =−𝐴𝑒^{−𝐴(𝑡−𝑡_{0})}𝐱(𝑡)+𝐴𝑒^{−𝐴(𝑡−𝑡_{0})}𝐱(𝑡)+𝑒^{−𝐴(𝑡−𝑡_{0})}𝐠(𝑡) \\ & =𝑒^{−𝐴(𝑡−𝑡_{0})}𝐠(𝑡).\end{aligned}


$$

Now, we integrate both sides from $t_0$ to $t$ and get

$$


\mathbf{y}(t)-\mathbf{y}(t_0)=\int_{t_0}^{t} e^{-A(s-t_0)}\mathbf{g}(s)\,\text{d}s.


$$

Next, since $\mathbf{y}(t_0)=e^{-A(t_0-t_0)}\mathbf{x}(t_0)=\mathbf{x}(t_0),$ we have

$$


\mathbf{y}(t)=\mathbf{x}(t_0)+\int_{t_0}^{t} e^{-A(s-t_0)}\mathbf{g}(s)\,\text{d}s.


$$

Finally, we convert back to the initial variable $\mathbf{x}(t).$ To do that we multiply both sides by $e^{A(t-t_0)}{:}$

$$


\begin{aligned}𝑒^{𝐴(𝑡−𝑡_{0})}𝐲(𝑡) & =𝑒^{𝐴(𝑡−𝑡_{0})}𝐱(𝑡_{0})+𝑒^{𝐴(𝑡−𝑡_{0})}∫_{𝑡𝑡_{0}}^{}𝑒^{−𝐴(𝑠−𝑡_{0})}𝐠(𝑠)\,d𝑠 \\ 𝐱(𝑡) & =𝑒^{𝐴(𝑡−𝑡_{0})}𝐱(𝑡_{0})+∫_{𝑡𝑡_{0}}^{}𝑒^{𝐴(𝑡−𝑡_{0})}𝑒^{−𝐴(𝑠−𝑡_{0})}𝐠(𝑠)\,d𝑠 \\ & =𝑒^{𝐴(𝑡−𝑡_{0})}𝐱(𝑡_{0})+∫_{𝑡𝑡_{0}}^{}𝑒^{𝐴(𝑡−𝑡_{0})−𝐴(𝑠−𝑡_{0})}𝐠(𝑠)\,d𝑠 \\ & =𝑒^{𝐴(𝑡−𝑡_{0})}𝐱(𝑡_{0})+∫_{𝑡𝑡_{0}}^{}𝑒^{𝐴(𝑡−𝑠)}𝐠(𝑠)\,d𝑠\end{aligned}


$$

Therefore, the solution to our IVP is

$$


\mathbf{x}(t) = \underbrace{e^{A(t-t_0)} \, \mathbf{x}(t_0)}_{\text{homogeneous part}} + \underbrace{\int_{t_0}^{t} e^{A(t-s)} \mathbf{g}(s) \, \text{d}s}_{\text{particular solution}},


$$

where the first term represents the solution of the corresponding *homogeneous system*, and the second term gives a particular solution of our *inhomogeneous system*.

Let's see some concrete examples.

### Example: Identifying the Matrix Exponential Formula for IVP Solution of an Inhomogeneous System

#### Question

$$


[\begin{aligned}4 & 1 \\ 0 & 4\end{aligned}]


$$

Fill in the blanks in the expression that gives the solution of the initial value problem above.

**

$$


\begin{aligned}𝐱(𝑡) & =[\begin{matrix}\,\,𝑋𝑋𝑋𝑋\, \\ 3𝑒^{4(𝑡−1)}\end{matrix}]+∫_{𝑡1}[\begin{matrix}𝑒^{4𝑡} \\ \,\,𝑋𝑋\,\end{matrix}]d𝑠.\end{aligned}


$$

#### Explanation

Given the system $\mathbf{x}'(t) = A \mathbf{x}(t)+\mathbf{g}(t),$ where $A$ is a constant square matrix, the solution of the initial value problem can be written as the sum of the homogeneous part and a particular solution:

$$


\mathbf{x}(t) = \underbrace{e^{A(t-t_0)} \, \mathbf{x}(t_0)}_{\text{homogeneous part}} + \underbrace{\int_{t_0}^{t} e^{A(t-s)} \mathbf{g}(s) \, \text{d}s}_{\text{particular solution}},


$$

where $\mathbf x(t_0)$ is the initial condition vector.

Let's evaluate each part separately:

- First, we find the homogeneous part. We are given that $[\begin{aligned}𝑒^{4𝑡} & 𝑡𝑒^{4𝑡} \\ 0 & 𝑒^{4𝑡}\end{aligned}]$ So,

- Next, we find the particular solution. Notice that So, we have

Therefore, we get

$$


\begin{aligned}𝐱(𝑡) & =\begin{matrix}3(𝑡−1)𝑒^{4(𝑡−1)} \\ 3𝑒^{4(𝑡−1)}\end{matrix}+∫_{𝑡1}[\begin{matrix}𝑒^{4𝑡} \\ 0\end{matrix}]d𝑠.\end{aligned}


$$

### Example: Solving an Inhomogeneous System Using a Given Matrix Exponential

#### Question

$$


\begin{aligned}𝑥^{′}(𝑡)=3𝑥(𝑡)+𝑦(𝑡)+1 \\ 𝑦^{′}(𝑡)=3𝑦(𝑡),\end{aligned}


$$

Find the solution to the initial value problem above.

**

#### Explanation

Writing our system in matrix form, we get

$$


[\begin{aligned}3 & 1 \\ 0 & 3\end{aligned}]


$$

where $[\begin{aligned}𝑥(𝑡) \\ 𝑦(𝑡)\end{aligned}]$ and $[\begin{aligned}1 \\ 0\end{aligned}]$ So, the matrix of the system is $[\begin{aligned}3 & 1 \\ 0 & 3\end{aligned}]$

Given the system $\mathbf{x}'(t) = A \mathbf{x}(t)+\mathbf{g}(t),$ where $A$ is a constant square matrix, the solution of the initial value problem can be written as the sum of the homogeneous part and a particular solution:

$$


\mathbf{x}(t) = \underbrace{e^{A(t-t_0)} \, \mathbf{x}(t_0)}_{\text{homogeneous part}} + \underbrace{\int_{t_0}^{t} e^{A(t-s)} \mathbf{g}(s) \, \text{d}s}_{\text{particular solution}},


$$

where $\mathbf x(t_0)$ is the initial condition vector.

Let's evaluate each part separately:

- First, we find the homogeneous part. We are given that Since the initial conditions are given at $t = t_0 = 0,$ we have

- Next, we find the particular solution. Notice that So, we have Thus, we obtain

Finally, we get

$$


\begin{aligned}𝐱(𝑡) & =[\begin{matrix}0 \\ 0\end{matrix}]+\begin{matrix}\frac{1}{3}𝑒^{3𝑡}−\frac{1}{3} \\ 0\end{matrix} \\ & =\begin{matrix}\frac{1}{3}𝑒^{3𝑡}−\frac{1}{3} \\ 0\end{matrix} \\ & =\frac{1}{3}[\begin{matrix}𝑒^{3𝑡}−1 \\ 0\end{matrix}].\end{aligned}


$$

Therefore, the solution to the initial value problem is

$$


[\begin{aligned}𝑥(𝑡) \\ 𝑦(𝑡)\end{aligned}]


$$

### Example: Proving the Matrix Exponential Formula for IVP Solution of an Inhomogeneous System

#### Question

Consider the inhomogeneous system $\mathbf{x}'(t)=A\mathbf{x}(t)+\mathbf{g}(t),$ where $A$ is a constant square matrix. A derivation of the formula for the solution $\mathbf{x}(t)$ passing through $\mathbf{x}(t_0)$ is presented below.

$\text{L1}{:}\;$ Let $\mathbf{y}(t)=e^{-A(t-t_0)}\mathbf{x}(t)$

$\text{L2}{:}\;$ $\mathbf{y}'(t) = -Ae^{-A(t-t_0)}\mathbf{x}(t) + e^{-A(t-t_0)}\mathbf{x}'(t)$

$\text{L3}{:}\;$ $\mathbf{y}'(t)=e^{-A(t-t_0)}\mathbf{g}(t)$

$\text{L4}{:}\;$ $\displaystyle\mathbf{y}(t)-\mathbf{y}(t_0) = \int_{t_0}^{t} e^{-A(s-t_0)}\mathbf{g}(s) \, \text{d}s$

$\text{L5}{:}\;$ $\mathbf{y}(t_0)=\mathbf{x}(t_0)$

$\text{L6}{:}\;$ $\displaystyle\mathbf{y}(t)=\mathbf{x}(t_0)+\int_{t_0}^{t} e^{-A(s-t_0)}\mathbf{g}(s) \, \text{d}s$

$\text{L7}{:}\;$ $\displaystyle e^{A(t-t_0)}\mathbf{y}(t)=e^{A(t-t_0)}\mathbf{x}(t_0)+\int_{t_0}^{t} e^{A(t-s)}\mathbf{g}(s) \, \text{d}s$

$\text{L8}{:}\;$ $e^{A(t-t_0)}\mathbf{y}(t)=\mathbf{x}(t)$

$\text{L9}{:}\;$ $\displaystyle\mathbf{x}(t)=e^{A(t-t_0)}\mathbf{x}(t_0)+\int_{t_0}^{t} e^{A(t-s)}\mathbf{g}(s) \, \text{d}s$

Fill in the blanks with the correct reasons to justify each step of the reasoning.

$\quad$ Line $\text{L3}$ follows from $\text{L2}$ by $𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴$.

$\quad$ Line $\text{L5}$ follows from line $\text{L1}$ by $𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴$.

$\quad$ Line $\text{L8}$ follows from line $\text{L1}$ by $𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴$.

#### Explanation

Let's justify each of the selected steps.

- We first consider lines $\text{L2}$ and $\text{L3}.$ Starting from in $\text{L2}$ and substituting $\mathbf{x}'(t)=A\mathbf{x}(t)+\mathbf{g}(t)$ from the original system gives Thus, $\text{L3}$ follows from $\text{L2}$ by $𝐱^{′}(𝑡)=𝐴𝐱(𝑡)+𝐠(𝑡)$

- Next, we consider lines $\text{L1}$ and $\text{L5}.$ Evaluating $\mathbf{y}(t)=e^{-A(t-t_0)}\mathbf{x}(t)$ at $t=t_0$ gives Therefore, $\text{L5}$ follows from line $\text{L1}$ by $𝑡=𝑡_{0}$

- Finally, we consider lines $\text{L1}$ and $\text{L8}.$ Multiplying both sides of from $\text{L1}$ by $e^{A(t-t_0)}$ gives Therefore, $\text{L8}$ follows from $\text{L1}$ by $𝑒^{𝐴(𝑡−𝑡_{0})}$
