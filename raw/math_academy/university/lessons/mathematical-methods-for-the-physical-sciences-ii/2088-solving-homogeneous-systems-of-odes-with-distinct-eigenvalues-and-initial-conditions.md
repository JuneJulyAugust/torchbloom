# Solving Homogeneous Systems of ODEs With Distinct Eigenvalues and Initial Conditions

Source: https://www.mathacademy.com/topics/2088?courseId=155
Topic ID: 2088

## Prerequisites

- [Solving Homogeneous Systems of ODEs With Distinct Eigenvalues](./2087-solving-homogeneous-systems-of-odes-with-distinct-eigenvalues.md)

## Lesson

### Introduction

An **initial value problem (IVP)** for a homogeneous linear system has the form

$$


\mathbf{x}'(t)=A\mathbf{x}(t), \qquad \mathbf{x}(t_0)=\mathbf{x}_0,


$$

where $A$ is a constant $2 \times 2$ matrix and $\mathbf{x}_0\in\mathbb{R}^2$ is the given initial state at $t=t_0.$ In other words, in an IVP we seek the solution of $\mathbf{x}'(t)=A\mathbf{x}(t)$ that passes through the point $\mathbf{x}_0$ at $t=t_0.$

To solve an IVP, we proceed as follows:

1. Find the general solution of the system $\mathbf{x}'(t)=A\mathbf{x}(t){:}$

2. Substitute $t=t_0$ into the general solution and use the initial condition $\mathbf{x}(t_0)=\mathbf{x}_0{:}$

3. Solve the resulting linear system for $c_1$ and $c_2,$ then substitute those values back into $\mathbf{x}(t).$

The definition (and the procedure) above generalizes directly to the $n\times n$ case.

Let's see some concrete examples of solving an IVP.

### Example: Solving an Initial Value Problem Given the General Solution

#### Question

Solve the initial value problem

$$


[\begin{aligned}7 \\ −1\end{aligned}]


$$

given that the general solution to our differential equation is

$$


[\begin{aligned}3 \\ 1\end{aligned}]


$$

The solution to the initial value problem is

$$


\begin{aligned}\phantom{X|} \\ \phantom{X|}\end{aligned}


$$

#### Explanation

To find the values of $c_1$ and $c_2$, we substitute $t=0$ in the general solution:

$$


\begin{aligned}𝐱(0) & =[\begin{matrix}7 \\ −1\end{matrix}] \\ 𝑐_{1}[\begin{matrix}3 \\ 1\end{matrix}]𝑒^{0}+𝑐_{2}[\begin{matrix}2 \\ −1\end{matrix}]𝑒^{0} & =[\begin{matrix}7 \\ −1\end{matrix}] \\ [\begin{matrix}3𝑐_{1}+2𝑐_{2} \\ 𝑐_{1}−𝑐_{2}\end{matrix}] & =[\begin{matrix}7 \\ −1\end{matrix}]\end{aligned}


$$

So, we have a system of linear equations

$$


\begin{aligned}3𝑐_{1}+2𝑐_{2}=7 \\ 𝑐_{1}−𝑐_{2}=−1.\end{aligned}


$$

Multiplying the second equation by $2$ and adding the result to the first equation, we get

$$


5c_1= 5 \qquad\Longrightarrow\qquad c_1 = 1.


$$

Substituting this into the second equation, we obtain

$$


1 - c_2 = -1 \qquad\Longrightarrow\qquad c_2 = 2.


$$

Therefore, the solution to the initial value problem is

$$


\begin{aligned}𝐱(𝑡) & =1⋅[\begin{matrix}3 \\ 1\end{matrix}]𝑒^{𝑡}+2⋅[\begin{matrix}2 \\ −1\end{matrix}]𝑒^{−𝑡} \\ & =\begin{matrix}3 \\ 1\end{matrix}𝑒^{𝑡}+\begin{matrix}4 \\ −2\end{matrix}𝑒^{−𝑡}.\end{aligned}


$$

### Example: Solving an Initial Value Problem Given the Eigenvectors and Eigenvalues of the Corresponding Matrix

#### Question

Let $\lambda_1=3$ and $\lambda_2=-2$ be eigenvalues of the $2\times 2$ matrix $A$ that correspond to eigenvectors

$$


[\begin{aligned}6 \\ −2\end{aligned}]


$$

Given that the position of a particle at time $t$ seconds is given by the vector $\mathbf{x}(t)$ and that $\mathbf{x}(t)$ is the solution to the initial value problem

$$


[\begin{aligned}−11 \\ 1\end{aligned}]


$$

find the position of the particle after $2$ seconds.

#### Explanation

Given a system of first-order linear ODEs in the form

$$


\mathbf{x}'(t)=A\mathbf{x}(t)


$$

where $A$ has two distinct eigenvalues ${\color{red}\lambda_1}, {\color{blue}\lambda_2}$ with corresponding eigenvectors ${\color{red}\mathbf{v}_1}$ and ${\color{blue}\mathbf{v}_2},$ the formula for the general solution is

$$


\mathbf{x}(t) = c_1{\color{red}\mathbf{v}_1} e^{{\color{red}\lambda_1} t} + c_2{\color{blue}\mathbf{v}_2} e^{{\color{blue}\lambda_2} t}, \qquad c_1,c_2 \in \mathbb{R}.


$$

Therefore, the general solution to our matrix differential equation is

$$


\begin{aligned}𝐱(𝑡)=𝑐_{1}[\begin{matrix}6 \\ −2\end{matrix}]𝑒^{3𝑡}+𝑐_{2}[\begin{matrix}1 \\ −3\end{matrix}]𝑒^{−2𝑡},\,𝑐_{1},𝑐_{2}∈ℝ.\end{aligned}


$$

Now, to find the values of $c_1$ and $c_2,$ we substitute $t=0$ into the general solution:

$$


\begin{aligned}𝐱(0) & =[\begin{matrix}−11 \\ 1\end{matrix}] \\ 𝑐_{1}[\begin{matrix}6 \\ −2\end{matrix}]𝑒^{0}+𝑐_{2}[\begin{matrix}1 \\ −3\end{matrix}]𝑒^{0} & =[\begin{matrix}−11 \\ 1\end{matrix}] \\ [\begin{matrix}6𝑐_{1}+𝑐_{2} \\ −2𝑐_{1}−3𝑐_{2}\end{matrix}] & =[\begin{matrix}−11 \\ 1\end{matrix}]\end{aligned}


$$

So, we have a system of linear equations

$$


\begin{aligned}6𝑐_{1}+𝑐_{2}=−11 \\ −2𝑐_{1}−3𝑐_{2}=1.\end{aligned}


$$

Multiplying the first equation by $3$ and adding the result to the second equation, we get

$$


16c_1 = -32 \qquad\Longrightarrow\qquad c_1=-2.


$$

Substituting this into the second equation, we obtain

$$


-2\cdot(-2) -3c_2 = 1 \qquad\Longrightarrow\qquad c_2=1.


$$

Therefore, the solution for the initial value problem is

$$


\begin{aligned}𝐱(𝑡) & =−2⋅[\begin{matrix}6 \\ −2\end{matrix}]𝑒^{3𝑡}+1⋅[\begin{matrix}1 \\ −3\end{matrix}]𝑒^{−2𝑡} \\ & =[\begin{matrix}−12 \\ 4\end{matrix}]𝑒^{3𝑡}+[\begin{matrix}1 \\ −3\end{matrix}]𝑒^{−2𝑡}.\end{aligned}


$$

Finally, we calculate $\mathbf x(2)\mathbin{:}$

$$


\begin{aligned}𝐱(2) & =[\begin{matrix}−12 \\ 4\end{matrix}]𝑒^{3⋅2}+[\begin{matrix}1 \\ −3\end{matrix}]𝑒^{−2⋅2} \\ & =[\begin{matrix}−12𝑒^{6}+𝑒^{−4} \\ 4𝑒^{6}−3𝑒^{−4}\end{matrix}]\end{aligned}


$$

### Example: Solving an Initial Value Problem for a Linear System of Differential Equations

#### Question

Find the solution to the initial value problem

$$


\begin{aligned}𝑥_{′1}(𝑡)=3𝑥_{1}(𝑡)−𝑥_{2}(𝑡) \\ 𝑥_{′2}(𝑡)=6𝑥_{1}(𝑡)−4𝑥_{2}(𝑡)\end{aligned}


$$

**

#### Explanation

Let's construct the matrix differential equation $\mathbf{x}'(t)=A\mathbf{x}(t)$ for the given system

$$


[\begin{aligned}𝑥_{′1}(𝑡) \\ 𝑥_{′2}(𝑡)\end{aligned}]


$$

- We are given that the eigenvalues are

- Let's go through the process of finding the eigenvectors. For $\lambda_1 =2,$ we get So, we get an eigenvector $[\begin{aligned}1 \\ 1\end{aligned}]$ For $\lambda_2 =-3,$ we get So, we get an eigenvector $[\begin{aligned}1 \\ 6\end{aligned}]$

Now, we write down the general solution to the given linear system of differential equations:

$$


\begin{aligned}𝐱(𝑡) & =𝑐_{1}𝐯_{1}𝑒^{𝜆_{1}𝑡}+𝑐_{2}𝐯_{2}𝑒^{𝜆_{2}𝑡} \\ & =𝑐_{1}[\begin{matrix}1 \\ 1\end{matrix}]𝑒^{2𝑡}+𝑐_{2}[\begin{matrix}1 \\ 6\end{matrix}]𝑒^{−3𝑡},\,𝑐_{1},𝑐_{2}∈ℝ\end{aligned}


$$

Now, to find the values of $c_1$ and $c_2,$ we substitute $t=0$ in the general solution and use the initial values:

$$


\begin{aligned}𝐱(0) & =[\begin{matrix}5 \\ 0\end{matrix}] \\ 𝑐_{1}[\begin{matrix}1 \\ 1\end{matrix}]𝑒^{0}+𝑐_{2}[\begin{matrix}1 \\ 6\end{matrix}]𝑒^{0} & =[\begin{matrix}5 \\ 0\end{matrix}] \\ [\begin{matrix}𝑐_{1}+𝑐_{2} \\ 𝑐_{1}+6𝑐_{2}\end{matrix}] & =[\begin{matrix}5 \\ 0\end{matrix}]\end{aligned}


$$

So, we have a system of linear equations

$$


\begin{aligned}𝑐_{1}+𝑐_{2}=5 \\ 𝑐_{1}+6𝑐_{2}=0\end{aligned}


$$

Subtracting the first equation from the second equation, we get

$$


\begin{aligned}5𝑐_{2}=−5\,⟹\,𝑐_{2}=−1.\end{aligned}


$$

Substituting $c_2 = -1$ into the first equation, we obtain

$$


\begin{aligned}𝑐_{1}−1=5\,⟹\,𝑐_{1}=6.\end{aligned}


$$

Finally, we write down the solution to the initial value problem:

$$


\begin{aligned}𝐱(𝑡) & =6[\begin{matrix}1 \\ 1\end{matrix}]𝑒^{2𝑡}−[\begin{matrix}1 \\ 6\end{matrix}]𝑒^{−3𝑡}.\end{aligned}


$$
