# Finding Generalized Eigenvectors of Specific Ranks

Source: https://www.mathacademy.com/topics/3634?courseId=55
Topic ID: 3634

## Prerequisites

- [Ranks of Generalized Eigenvectors](./3633-ranks-of-generalized-eigenvectors.md)

## Lesson

### Introduction

Given a matrix $A$ with eigenvalue $\lambda,$ a generalized eigenvector of rank $k$ is a vector $\mathbf{v}$ that satisfies

$$


(A - \lambda I)^k \mathbf{v} = \mathbf{0} \quad \textrm{and} \quad (A - \lambda I)^{k-1} \mathbf{v} \neq \mathbf{0}.


$$

In this lesson, we'll learn how to calculate generalized eigenvectors of a specific rank for a given matrix $A.$

As an example, consider the matrix $A,$ given by

$$


[\begin{aligned}−3 & 8 \\ 0 & −3\end{aligned}]


$$

Suppose we're given that $\lambda = -3$ is an eigenvalue of $A,$ and that this eigenvalue has corresponding generalized eigenvectors of rank $2.$ How do we find one of these generalized eigenvectors?

To find a generalized eigenvector of rank $2$ corresponding to $\lambda = -3,$ we need to find a vector $\mathbf v$ that satisfies

$$


(A + 3I)^2 \mathbf{v} = \mathbf{0} \quad \textrm{and} \quad (A +3I)^{} \mathbf{v} \neq \mathbf{0}.


$$

Let's consider each condition:

- We start by solving $(A + 3I)^2 \mathbf{v} = \mathbf{0}.$ First, we have Computing its square, we see that this matrix is nilpotent: This means that *any* vector in $\mathbb R^2$ is a solution to $(A + 3I)^2 \mathbf{v} = \mathbf{0}.$ Therefore, the solution to $(A + 3I)^2 \mathbf{v} = \mathbf{0}$ can be written as

- Next, we solve $(A +3I) \mathbf{v} = \mathbf{0}.$ We have Converting this matrix to reduced row echelon form, we get This means the solution to $(A +3I) \mathbf{v} = \mathbf{0}$ is $v_2 = 0$, where $v_1$ is a free variable. Therefore, the solution to $(A + 3I) \mathbf{v} = \mathbf{0}$ can be written as

Comparing our two solutions, we see that the vector

$$


[\begin{aligned}0 \\ 1\end{aligned}]


$$

satisfies $(A +3I)^2 \mathbf{v} = \mathbf{0}$ but does *not* satisfy $(A +3 I) \mathbf{v} = \mathbf{0}.$

Hence, $[\begin{aligned}0 \\ 1\end{aligned}]$ is a generalized eigenvector of rank $2$ of $A.$

### Example: Computing a Generalized Eigenvector of a 2x2 Matrix

#### Question

Consider the matrix $A,$ given by

$$


[\begin{aligned}4 & 0 \\ 5 & 4\end{aligned}]


$$

Given that $\lambda = 4$ is an eigenvalue of $A,$ and that this eigenvalue has corresponding generalized eigenvectors of rank $2,$ calculate one of these generalized eigenvectors.

#### Explanation

Given a matrix $A$ with eigenvalue $\lambda,$ a generalized eigenvector of rank $k$ is a vector $\mathbf{v}$ that satisfies

$$


(A - \lambda I)^k \mathbf{v} = \mathbf{0} \quad \textrm{and} \quad (A - \lambda I)^{k-1} \mathbf{v} \neq \mathbf{0}.


$$

To find a generalized eigenvector of rank $2$ corresponding to $\lambda = 4,$ we need to find a vector $\mathbf v$ that satisfies

$$


(A -4I)^2 \mathbf{v} = \mathbf{0} \quad \textrm{and} \quad (A -4I) \mathbf{v} \neq \mathbf{0}.


$$

Let's consider each condition:

- We start by solving $(A -4I)^2 \mathbf{v} = \mathbf{0}.$ First, we have Computing its square, we see that this matrix is nilpotent: This means that ** vector in $\mathbb R^2$ is a solution to $(A -4I)^2 \mathbf{v} = \mathbf{0}.$ Therefore, the solution to $(A -4I)^2 \mathbf{v} = \mathbf{0}$ can be written as

- Next, we solve $(A -4I) \mathbf{v} = \mathbf{0}.$ We have Converting this matrix to reduced row echelon form, we get This means that the solution to $(A -4I) \mathbf{v} = \mathbf{0}$ is $v_1 = 0,$ where $v_2$ is a free variable. Therefore, the solution to $(A -4I) \mathbf{v} = \mathbf{0}$ can be written as

Comparing our two solutions, we see that the vector $[\begin{aligned}1 \\ 0\end{aligned}]$satisfies $(A -4I)^2 \mathbf{v} = \mathbf{0}$ but does ** satisfy $(A -4 I) \mathbf{v} = \mathbf{0}.$

Hence, $[\begin{aligned}1 \\ 0\end{aligned}]$ is a generalized eigenvector of rank $2$ of $A.$

### Example: Computing a Generalized Eigenvector of a 3x3 Matrix

#### Question

Consider the matrix $A,$ given by

$$


\begin{aligned}3 & 0 & 4 \\ 0 & 1 & 0 \\ 0 & 0 & 3\end{aligned}


$$

Given that $\lambda = 3$ is an eigenvalue of $A,$ and that this eigenvalue has corresponding generalized eigenvectors of rank $2,$ calculate one of these generalized eigenvectors.

**

$$


\begin{aligned}(𝐴−3𝐼)^{2}=\begin{aligned}0 & 0 & 0 \\ 0 & 4 & 0 \\ 0 & 0 & 0\end{aligned}\end{aligned}


$$

#### Explanation

Given a matrix $A$ with eigenvalue $\lambda,$ a generalized eigenvector of rank $k$ is a vector $\mathbf{v}$ that satisfies

$$


(A - \lambda I)^k \mathbf{v} = \mathbf{0} \quad \textrm{and} \quad (A - \lambda I)^{k-1} \mathbf{v} \neq \mathbf{0}.


$$

To find a generalized eigenvector of rank $2$ corresponding to $\lambda = 3,$ we need to find a vector $\mathbf v$ that satisfies

$$


(A -3I)^2 \mathbf{v} = \mathbf{0} \quad \textrm{and} \quad (A -3I) \mathbf{v} \neq \mathbf{0}.


$$

Let's consider each condition:

- We start by solving $(A -3I)^2 \mathbf{v} = \mathbf{0}.$ We're given that Converting this matrix to reduced row echelon form, we get This means that the solution to $(A-3I)^2 \mathbf{v} = \mathbf{0}$ is $v_2 = 0,$ where $v_1$ and $v_3$ are free variables. Therefore, the solution to $(A -3I)^2 \mathbf{v} = \mathbf{0}$ can be written as

- Next, we solve $(A -3I) \mathbf{v} = \mathbf{0}.$ We have Converting this matrix to reduced row echelon form, we get This means that the solution to $(A -3I) \mathbf{v} = \mathbf{0}$ is $v_2 = v_3 = 0,$ where $v_1$ is a free variable. Therefore, the solution to $(A -3I) \mathbf{v} = \mathbf{0}$ can be written as

Comparing our two solutions, we see that the vector $\begin{aligned}0 \\ 0 \\ 1\end{aligned}$ satisfies $(A -3I)^2 \mathbf{v} = \mathbf{0}$ but does ** satisfy $(A -3 I) \mathbf{v} = \mathbf{0}.$

Hence, $\begin{aligned}0 \\ 0 \\ 1\end{aligned}$ is a generalized eigenvector of rank $2$ of $A.$

### Example: Computing a Generalized Eigenvector of a 4x4 Matrix

#### Question

Consider the matrix $A,$ given by

$$


\begin{aligned}3 & 3 & −3 & 2 \\ 0 & 3 & 2 & 4 \\ 0 & 0 & 3 & 2 \\ 0 & 0 & 0 & 2\end{aligned}


$$

Given that $\lambda = 3$ is an eigenvalue of $A,$ and that this eigenvalue has corresponding generalized eigenvectors of rank $3,$ calculate one of these eigenvectors.

**

$$


\begin{aligned}(𝐴−3𝐼)^{2}=\begin{aligned}0 & 0 & 6 & 4 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & −2 \\ 0 & 0 & 0 & 1\end{aligned},\,(𝐴−3𝐼)^{3}=\begin{aligned}0 & 0 & 0 & 8 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 2 \\ 0 & 0 & 0 & −1\end{aligned}\end{aligned}


$$

#### Explanation

Given a matrix $A$ with eigenvalue $\lambda,$ a generalized eigenvector of rank $k$ is a vector $\mathbf{v}$ that satisfies

$$


(A - \lambda I)^k \mathbf{v} = \mathbf{0} \quad \textrm{and} \quad (A - \lambda I)^{k-1} \mathbf{v} \neq \mathbf{0}.


$$

To find a generalized eigenvector of rank $3$ corresponding to $\lambda = 3,$ we need to find a vector $\mathbf v$ that satisfies

$$


(A - 3I)^3 \mathbf{v} = \mathbf{0} \quad \textrm{and} \quad (A - 3I)^2 \mathbf{v} \neq \mathbf{0}.


$$

Let's consider each condition:

- We start by solving $(A -3I)^3 \mathbf{v} = \mathbf{0}.$ We're given that Converting this matrix to reduced row echelon form, we get This means the solution to $(A -3I)^3 \mathbf{v} = \mathbf{0}$ is $v_4 = 0,$ where $v_1,v_2,$ and $v_3$ are free variables. Therefore, the solution to $(A-3I)^3 \mathbf{v} = \mathbf{0}$ can be written as

- Next, we solve $(A -3I)^2 \mathbf{v} = \mathbf{0}.$ We're given that Converting this matrix to reduced row echelon form, we get This means the solution to $(A -3I)^2 \mathbf{v} = \mathbf{0}$ is $v_3 = v_4 = 0,$ where $v_1$ and $v_2$ are free variables. So, the solution to $(A-3I)^2 \mathbf{v} = \mathbf{0}$ can be written as

Comparing our two solutions, we see that the vector

$$


\begin{aligned}0 \\ 0 \\ 1 \\ 0\end{aligned}


$$

satisfies $(A -3I)^3 \mathbf{v} = \mathbf{0}$ but does ** satisfy $(A -3 I)^2 \mathbf{v} = \mathbf{0}.$

Hence, $\begin{aligned}0 \\ 0 \\ 1 \\ 0\end{aligned}$ is a generalized eigenvector of rank $3$ of $A.$
