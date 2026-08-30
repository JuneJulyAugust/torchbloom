# The Null Space of a Matrix

Source: https://www.mathacademy.com/topics/1854?courseId=145
Topic ID: 1854

## Prerequisites

- [Representing 3x3 Systems of Equations Using a Matrix Product](../integrated-math-iii-honors/155-representing-3x3-systems-of-equations-using-a-matrix-product.md)
- [Gaussian Elimination For NxM Systems of Equations](./1733-gaussian-elimination-for-nxm-systems-of-equations.md)
- [Subspaces of N-Dimensional Space: Geometric Interpretation](./4077-subspaces-of-n-dimensional-space-geometric-interpretation.md)

## Lesson

### Introduction

The **null space** of a matrix $A$ is the set of all the solutions of the equation $A\mathbf{x}= \mathbf{0},$ and is denoted by $\textrm{Null}(A).$

To illustrate, let's consider the following matrix:

$$


[\begin{aligned}2 & 6 \\ 1 & 3\end{aligned}]


$$

The null space consists of all the solutions of $A\mathbf{x}=\mathbf{0}.$ For example, the vectors $[\begin{aligned}−3 \\ 1\end{aligned}]$ $[\begin{aligned}6 \\ −2\end{aligned}]$ and $[\begin{aligned}−9 \\ 3\end{aligned}]$ all satisfy the equation $A\mathbf{x}=\mathbf{0},$ so they are all elements of the null space:

$$


[\begin{aligned}−3 \\ 1\end{aligned}]


$$

### Example: Identifying Whether a Vector Lies in the Null Space of a Given Matrix

#### Question

The matrix $A$ and vectors $\mathbf{b}_1$, $\mathbf{b}_2$, $\mathbf{b}_3$ are given below. Which of the vectors lie in $\textrm{Null}(A)?$

$$


\begin{aligned}3 & −6 \\ −5 & 10 \\ −8 & 16\end{aligned}


$$

#### Explanation

A vector $\mathbf{b}$ lies in $\textrm{Null}(A)$ if $A\mathbf{b}=\mathbf{0}.$ So, we need to compute the product of $A$ and each of the given vectors and check whether it is equal to $\mathbf{0}\mathbin{:}$

$$


\begin{aligned}𝐴𝐛_{1} & =\begin{aligned}3 & −6 \\ −5 & 10 \\ −8 & 16\end{aligned}[\begin{aligned}3 \\ 6\end{aligned}]=\begin{aligned}−27 \\ 45 \\ 72\end{aligned}≠𝟎\,× \\ 𝐴𝐛_{2} & =\begin{aligned}3 & −6 \\ −5 & 10 \\ −8 & 16\end{aligned}[\begin{aligned}6 \\ 3\end{aligned}]=\begin{aligned}0 \\ 0 \\ 0\end{aligned}=𝟎\,✓ \\ 𝐴𝐛_{3} & =\begin{aligned}3 & −6 \\ −5 & 10 \\ −8 & 16\end{aligned}[\begin{aligned}1 \\ 3\end{aligned}]=\begin{aligned}−15 \\ 25 \\ 40\end{aligned}≠𝟎\,×\end{aligned}


$$

Therefore, only $\mathbf{b}_2$ lies in $\textrm{Null}(A).$

### Example: Solve a Variable in a Vector Lying in the Null Space of a Given Matrix

#### Question

Consider the matrix $\begin{aligned}3 & 2 & −4 \\ −3 & 3 & −1 \\ 6 & −6 & 2\end{aligned}$ and the vector $\begin{aligned}2 \\ 𝑘 \\ 3\end{aligned}$ Find the value of $k$ such that $\mathbf{b}\in\textrm{Null}(A).$

#### Explanation

If $\mathbf{b} \in \textrm{Null}(A),$ then we must have $A\mathbf{b} = \mathbf{0}.$ Substituting the given information, we get

$$


\begin{aligned}𝐴𝐛 & =𝟎 \\ \begin{aligned}3 & 2 & −4 \\ −3 & 3 & −1 \\ 6 & −6 & 2\end{aligned}\begin{aligned}2 \\ 𝑘 \\ 3\end{aligned} & =\begin{aligned}0 \\ 0 \\ 0\end{aligned} \\ \begin{aligned}6+2𝑘−12 \\ −6+3𝑘−3 \\ 12−6𝑘+6\end{aligned} & =\begin{aligned}0 \\ 0 \\ 0\end{aligned}.\end{aligned}


$$

This corresponds to the system

$$


\begin{aligned}2𝑘−6=0 \\ 3𝑘−9=0 \\ −6𝑘+18=0\end{aligned}


$$

and for each of these equations, we obtain $k=3.$

### Writing the Null Space using Set-Builder Notation

Let's again consider the following matrix:

$$


[\begin{aligned}2 & 6 \\ 1 & 3\end{aligned}]


$$

To find an expression for the null space using set-builder notation, we need to find all the solutions of $A\mathbf{x}=\mathbf{0}.$ Let's start by considering the augmented matrix $[A\,|\, \mathbf{0}]$ and finding its reduced row echelon form as follows:

$$


\begin{aligned}[𝐴\,|\,𝟎] & =[\begin{aligned}2 & 6 & 0 \\ 1 & 3 & 0\end{aligned}] & 𝑅_{1} & :=\frac{1}{2}𝑅_{1} \\ & ∼[\begin{aligned}1 & 3 & 0 \\ 1 & 3 & 0\end{aligned}] & 𝑅_{2} & :=𝑅_{2}+(−1)𝑅_{1} \\ & ∼[\begin{aligned}1 & 3 & 0 \\ 0 & 0 & 0\end{aligned}] & & \end{aligned}


$$

Note that the reduced matrix above has one pivot column (the $1$st column). The second column is not a pivot column.

Now, we convert the reduced matrix back into a system, as follows:

$$


\begin{aligned}𝑥_{1}+3𝑥_{2}=0 \\ 0=0\end{aligned}


$$

Here, $\color{blue}x_1$ is a basic variable (it corresponds to the pivot column), while $\color{red}x_2$ is a free variable (it corresponds to the non-pivot column). Because there is a free variable, the system $A\mathbf{x}=\mathbf{0}$ has infinitely many solutions.

From the first equation we get ${\color{blue}x_1}=-3{\color{red}x_2},$ so the set of all the solutions of $A\mathbf{x}=\mathbf{0}$ is

$$


[\begin{aligned}−3𝑥_{2} \\ 𝑥_{2}\end{aligned}]


$$

**Note:** It is not necessary to consider the full augmented matrix $[A \,|\, \mathbf{0}]$ since the last column won't be changed during the process of reduction. Really, we just need to find the reduced row echelon form of the matrix $A$ and then set up the corresponding system.

### Example: Finding the Null Space of a Given Matrix

#### Question

Consider the matrix $[\begin{aligned}4 & −12 \\ 3 & −8\end{aligned}]$ Find $\textrm{Null}(A).$

#### Explanation

We need to solve the equation $A\mathbf{x}=\mathbf{0}.$ First, we find the row echelon form of $A$ as follows:

$$


\begin{aligned}𝐴 & =[\begin{aligned}4 & −12 \\ 3 & −8\end{aligned}] & 𝑅_{1} & :=\frac{1}{4}𝑅_{1} \\ & ∼[\begin{aligned}1 & −3 \\ 3 & −8\end{aligned}] & 𝑅_{2} & :=𝑅_{2}+(−3)𝑅_{1} \\ & ∼[\begin{aligned}1 & −3 \\ 0 & 1\end{aligned}] & & \end{aligned}


$$

This corresponds to the following system:

$$


\begin{aligned}𝑥_{1}−3𝑥_{2}=0 \\ 𝑥_{2}=0\end{aligned}


$$

The second equation tells us that $x_2=0.$ Substituting this into the first equation, we get

$$


\begin{aligned}𝑥_{1}−3𝑥_{2} & =0 \\ 𝑥_{1}−3(0) & =0 \\ 𝑥_{1} & =0.\end{aligned}


$$

So, we conclude that $[\begin{aligned}0 \\ 0\end{aligned}]$ is the only solution to this system.

Therefore, $\textrm{Null}(A) = \left\{\mathbf{0} \right\}.$
