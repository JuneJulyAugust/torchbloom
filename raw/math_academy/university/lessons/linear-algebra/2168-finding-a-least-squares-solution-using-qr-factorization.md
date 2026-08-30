# Finding a Least-Squares Solution Using QR Factorization

Source: https://www.mathacademy.com/topics/2168?courseId=55
Topic ID: 2168

## Prerequisites

- [QR Factorization](./2129-qr-factorization.md)
- [The Least-Squares Solution of a Linear System (With Collinearity)](./2167-the-least-squares-solution-of-a-linear-system-with-collinearity.md)

## Lesson

### Introduction

Let's consider the least-squares problem for the system

$$


A\mathbf{x} = \mathbf{b}.


$$

We can use QR factorization to construct the least-squares solution of this system. Recall that finding the QR factorization of $A$ means expressing $A$ in the form

$$


A = QR,


$$

where

- $Q$ has orthonormal columns, and

- $R$ is an upper triangular matrix with positive entries on its main diagonal.

To see how QR factorization can be used to solve a least-squares problem, we first recall that the least-squares solution satisfies the normal equation

$$


A^T A \mathbf{x} = A^T \mathbf{b}.


$$

Substituting $A = QR,$ we obtain

$$


\begin{aligned}𝐴^{𝑇}𝐴𝐱 & =𝐴^{𝑇}𝐛 \\ (𝑄𝑅)^{𝑇}𝑄𝑅𝐱 & =(𝑄𝑅)^{𝑇}𝐛 \\ 𝑅^{𝑇}(𝑄^{𝑇}𝑄)𝑅𝐱 & =𝑅^{𝑇}𝑄^{𝑇}𝐛.\end{aligned}


$$

Since $Q$ has orthonormal columns, we have $Q^T Q = I.$ Therefore, the above equation becomes

$$


R^TR\mathbf{x} = R^TQ^T\mathbf{b}.


$$

Since $R^T$ is invertible, pre-multiplying our equation by $(R^T)^{-1}$ gives

$$


\begin{aligned}(𝑅^{𝑇})^{−1}⋅𝑅^{𝑇}𝑅𝐱 & =(𝑅^{𝑇})^{−1}⋅𝑅^{𝑇}𝑄^{𝑇}𝐛\end{aligned}


$$

which simplifies as

$$


R \mathbf{x} = Q^T \mathbf{b}. \qquad\qquad (\ast)


$$

The least-squares solution $\hat{\mathbf x}$ can now be found by solving this equation using back-substitution or row operations. This is usually the fastest way.

If we want an explicit formula for the least-squares solution, then we note that since $R$ is invertible, pre-multiplying $(\ast)$ by $R^{-1}$ gives

$$


\begin{aligned}𝑅^{−1}⋅𝑅𝐱 & =𝑅^{−1}⋅𝑄^{𝑇}𝐛\end{aligned}


$$

which simplifies as

$$


\mathbf{x} = R^{-1} Q^T \mathbf{b}.


$$

The least-squares solution is unique if $A$ has linearly independent columns.

### Example: Identifying an Expression for a Least-Squares Solution in Terms of the Matrices Q and R

#### Question

$$


\boxed{\phantom{A}} \, \mathbf{x} = \boxed{\phantom{A}} \, \mathbf{b}


$$

Let $A=QR$ be a QR decomposition of an $m \times n$ matrix $A$ with linearly independent columns, and the matrix equation above gives the least-squares solution of $A\mathbf{x}=\mathbf{b}.$ From left to right, what are the missing parts of the equation?

#### Explanation

The least-squares solution of $A\mathbf{x}=\mathbf{b}$ satisfies the normal equation

$$


A^T A\mathbf{x} = A^T\mathbf{b}.


$$

Substituting $A=QR,$ we obtain

$$


\begin{aligned}𝐴^{𝑇}𝐴𝐱 & =𝐴^{𝑇}𝐛 \\ (𝑄𝑅)^{𝑇}𝑄𝑅𝐱 & =(𝑄𝑅)^{𝑇}𝐛 \\ 𝑅^{𝑇}(𝑄^{𝑇}𝑄)𝑅𝐱 & =𝑅^{𝑇}𝑄^{𝑇}𝐛.\end{aligned}


$$

Since $Q$ has orthonormal columns, it satisfies $Q^T Q = I,$ and we get

$$


R^T R \mathbf{x} = R^T \! Q^T \mathbf{b}.


$$

Finally, since $R^T$ is invertible, pre-multiplying by $(R^T)^{-1}$ gives

$$


\begin{aligned}(𝑅^{𝑇})^{−1}⋅𝑅^{𝑇}𝑅𝐱 & =(𝑅^{𝑇})^{−1}⋅𝑅^{𝑇}𝑄^{𝑇}𝐛 \\ \,𝑅|\,\,𝐱 & =𝑄^{𝑇}\,𝐛.\end{aligned}


$$

Therefore, the missing parts of the equation are $R$ and $Q^T.$

### Using QR Factorization to Solve a Least-Squares Problem

Let's find the least-squares solution to $A\mathbf{x} = \mathbf{b},$ where $A = QR,$ and

$$


[\begin{aligned}−1 & 1 \\ 1 & 1\end{aligned}]


$$

Previously, we showed that the normal equation corresponding to $A\mathbf{x}=\mathbf{b},$ where $A=QR,$ can be reduced to

$$


R \mathbf{x} = Q^T \mathbf{b}.


$$

Substituting our matrices into this equation, we have

$$


\begin{aligned}\overset{\overset{\frac{1}{\sqrt{√2}}[\begin{aligned}2 & −4 \\ 0 & 3\end{aligned}]}{}}{𝑅}𝐱 & =\overset{\overset{\frac{1}{\sqrt{√2}}[\begin{aligned}−1 & 1 \\ 1 & 1\end{aligned}]}{}}{𝑄^{𝑇}}\overset{\overset{[\begin{aligned}2 \\ 4\end{aligned}]}{}}{𝐛} \\ [\begin{aligned}2 & −4 \\ 0 & 3\end{aligned}]𝐱 & =[\begin{aligned}2 \\ 6\end{aligned}],\end{aligned}


$$

which gives the system

$$


\begin{aligned}2𝑥_{1}−4𝑥_{2}=2 \\ 3𝑥_{2}=6.\end{aligned}


$$

From the second equation, we get $x_2=2.$ Substituting this into the first equation, we obtain

$$


\begin{aligned}2𝑥_{1}−4(2) & =2 \\ 2𝑥_{1} & =10 \\ 𝑥_{1} & =5.\end{aligned}


$$

Therefore, the least-squares solution to $A\mathbf{x} = \mathbf{b}$ is $[\begin{aligned}5 \\ 2\end{aligned}]$

### Example: Finding the Least-Squares Solution of a Linear System Given a QR Factorization

#### Question

Given the QR decomposition $A=QR,$ find the least-squares solution to $A\mathbf{x}=\mathbf{b},$ where

$$


\begin{aligned}3 & −6 \\ 6 & 2 \\ 2 & 3\end{aligned}


$$

#### Explanation

The least-squares solution of $A\mathbf{x}=\mathbf{b}$ satisfies the corresponding normal equation:

$$


A^T A\mathbf{x} = A^T\mathbf{b}


$$

Substituting $A=QR,$ we obtain

$$


\begin{aligned}𝐴^{𝑇}𝐴𝐱 & =𝐴^{𝑇}𝐛 \\ (𝑄𝑅)^{𝑇}𝑄𝑅𝐱 & =(𝑄𝑅)^{𝑇}𝐛 \\ 𝑅^{𝑇}(𝑄^{𝑇}𝑄)𝑅𝐱 & =𝑅^{𝑇}𝑄^{𝑇}𝐛.\end{aligned}


$$

Since $Q$ has orthonormal columns, it satisfies $Q^T Q = I,$ and we get

$$


R^T R \mathbf{x} = R^T \! Q^T \mathbf{b}.


$$

Finally, since $R^T$ is invertible, pre-multiplying by $(R^T)^{-1}$ gives

$$


\begin{aligned}(𝑅^{𝑇})^{−1}⋅𝑅^{𝑇}𝑅𝐱 & =(𝑅^{𝑇})^{−1}⋅𝑅^{𝑇}𝑄^{𝑇}𝐛 \\ 𝑅𝐱 & =𝑄^{𝑇}𝐛.\end{aligned}


$$

Now, substituting our matrices, we have

$$


\begin{aligned}\overset{\overset{\frac{1}{7}[\begin{aligned}7 & −3 \\ 0 & 2\end{aligned}]}{}}{𝑅}𝐱 & =\overset{\overset{\frac{1}{7}[\begin{aligned}3 & 6 & 2 \\ −6 & 2 & 3\end{aligned}]}{}}{𝑄^{𝑇}}\overset{\overset\begin{aligned}0 \\ 4 \\ 2\end{aligned}}{}}{𝐛} \\ [\begin{aligned}7 & −3 \\ 0 & 2\end{aligned}]𝐱 & =[\begin{aligned}28 \\ 14\end{aligned}],\end{aligned}


$$

which gives the system

$$


\begin{aligned}7𝑥_{1}−3𝑥_{2}=28 \\ 2𝑥_{2}=14.\end{aligned}


$$

From the second equation, we get $x_2=7.$ Substituting this into the first equation, we obtain

$$


\begin{aligned}7𝑥_{1}−3(7) & =28 \\ 7𝑥_{1} & =49 \\ 𝑥_{1} & =7.\end{aligned}


$$

Therefore, the least-squares solution to $A\mathbf{x}=\mathbf{b}$ is $[\begin{aligned}7 \\ 7\end{aligned}]$
