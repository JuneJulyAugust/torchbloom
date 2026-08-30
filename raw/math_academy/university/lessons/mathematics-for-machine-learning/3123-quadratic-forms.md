# Quadratic Forms

Source: https://www.mathacademy.com/topics/3123?courseId=145
Topic ID: 3123

## Prerequisites

- [Symmetric Matrices](./3118-symmetric-matrices.md)
- [Bilinear Forms](./3121-bilinear-forms.md)

## Lesson

### Introduction

Given a bilinear form $B(\mathbf{x},\mathbf{y})$ such that

$$


B:\Bbb R^n \times \Bbb R^n \to \Bbb R


$$

and the corresponding $n \times n$ matrix is *symmetric*, we can define the so-called **quadratic form** by substituting $\mathbf{y}=\mathbf{x}$ as follows:

$$


Q(\mathbf{x})= B(\mathbf{x},\mathbf{x}).


$$

Notice that the new expression depends only on $\mathbf{x}.$ So, a quadratic form is a function

$$


Q:\Bbb R^n \to \Bbb R.


$$

In matrix notation, a quadratic form can be given as

$$


Q(\mathbf{x}) = \mathbf{x}^T \! A \mathbf{x},


$$

where $A$ is a symmetric matrix. It's called the **matrix of the quadratic form**.

**Watch out!** By definition, the matrix of a quadratic form must be *symmetric*.

For example, given the bilinear form

$$


[\begin{aligned}1 & 2 \\ 2 & 1\end{aligned}]


$$

the corresponding quadratic form is then $Q(\mathbf{x})=B(\mathbf{x}, \mathbf{x}).$ Explicitly, we have

$$


\begin{aligned}𝑄(𝑥_{1},𝑥_{2}) & =[\begin{matrix}𝑥_{1} & 𝑥_{2}\end{matrix}][\begin{matrix}1 & 2 \\ 2 & 1\end{matrix}][\begin{matrix}𝑥_{1} \\ 𝑥_{2}\end{matrix}] \\ & =[\begin{matrix}𝑥_{1} & 𝑥_{2}\end{matrix}][\begin{matrix}𝑥_{1}+2𝑥_{2} \\ 2𝑥_{1}+𝑥_{2}\end{matrix}] \\ & =𝑥_{21}+4𝑥_{1}𝑥_{2}+𝑥_{22}.\end{aligned}


$$

**Note**: In a quadratic form, all terms must be of degree two (considered as polynomials in the variables $x_1, x_2, \cdots, x_n$). That's the reason we call it *quadratic*.

### Example: Identifying Matrices of Quadratic Forms

#### Question

Which of the following could be matrices of quadratic forms defined on $\mathbb{R}^2?$

$$


\begin{aligned}4 & 1 & −2 \\ 1 & 4 & 5 \\ −2 & 5 & 4\end{aligned}


$$

#### Explanation

Recall that every quadratic form defined on $\mathbb{R}^2$ has an associated $2 \times 2$ symmetric matrix.

With that in mind, let's examine each matrix in turn.

- $L$ ** be a matrix of a quadratic form defined on $\mathbb{R}^2$ since it's a $3 \times 3$ matrix (not $2 \times 2$).

- $M$ ** be a matrix of a quadratic form defined on $\mathbb{R}^2.$ Although it's a $2 \times 2$ matrix, $M$ is not symmetric since $m_{12} \neq m_{21}.$

- $N$ could be a matrix of a quadratic form defined on $\mathbb{R}^2$ since it is a $2 \times 2$ symmetric matrix.

Therefore, the correct answer is "$N$ only."

### Example: Evaluating a Quadratic Form

#### Question

$$


[\begin{aligned}−2 & 1 \\ 1 & 5\end{aligned}]


$$

Given the matrix $A$ above, evaluate the quadratic form $Q(\mathbf{x}) = \mathbf{x}^T \! A \mathbf{x}$ when $[\begin{aligned}3 \\ 4\end{aligned}]$

#### Explanation

Substituting $[\begin{aligned}3 \\ 4\end{aligned}]$ into the expression for $Q(\mathbf{x}),$ we obtain

$$


\begin{aligned}𝑄(𝐱) & =𝐱^{𝑇}\,𝐴𝐱 \\ & =[\begin{matrix}3 & 4\end{matrix}][\begin{matrix}−2 & 1 \\ 1 & 5\end{matrix}][\begin{matrix}3 \\ 4\end{matrix}] \\ & =[\begin{matrix}−2 & 23\end{matrix}][\begin{matrix}3 \\ 4\end{matrix}] \\ & =86.\end{aligned}


$$

### Example: Writing Down a Quadratic Form Given Its Matrix

#### Question

$$


[\begin{aligned}−1 & 1 \\ 1 & −1\end{aligned}]


$$

Consider the matrix $A$ above. Which expression represents the corresponding quadratic form $\mathbf{x}^T \! A \mathbf{x}$ in terms of the components of $[\begin{aligned}𝑥_{1} \\ 𝑥_{2}\end{aligned}]$

#### Explanation

****

Each entry $a_{ij}$ of $A$ corresponds to the term $a_{ij}x_i x_j$ in the expression of the quadratic form:

$$


\begin{aligned}𝐱^{𝑇}\,𝐴𝐱 & =−1𝑥_{1}𝑥_{1}+(1)𝑥_{1}𝑥_{2}+(1)𝑥_{2}𝑥_{1}+−1𝑥_{2}𝑥_{2} \\ & =−𝑥_{21}+𝑥_{1}𝑥_{2}+𝑥_{2}𝑥_{1}−𝑥_{22} \\ & =−𝑥_{21}+2𝑥_{1}𝑥_{2}−𝑥_{22}\end{aligned}


$$

****

To write down a quadratic form in terms of vector components, we compute the following expression:

$$


\begin{aligned}𝐱^{𝑇}\,𝐴𝐱 & =[\begin{matrix}𝑥_{1} & 𝑥_{2}\end{matrix}][\begin{matrix}−1 & 1 \\ 1 & −1\end{matrix}][\begin{matrix}𝑥_{1} \\ 𝑥_{2}\end{matrix}] \\ & =[\begin{matrix}𝑥_{1} & 𝑥_{2}\end{matrix}][\begin{matrix}−𝑥_{1}+𝑥_{2} \\ 𝑥_{1}−𝑥_{2}\end{matrix}] \\ & =𝑥_{1}(−𝑥_{1}+𝑥_{2})+𝑥_{2}(𝑥_{1}−𝑥_{2}) \\ & =−𝑥_{21}+𝑥_{1}𝑥_{2}+𝑥_{2}𝑥_{1}−𝑥_{22} \\ & =−𝑥_{21}+2𝑥_{1}𝑥_{2}−𝑥_{22}\end{aligned}


$$

### Example: Finding the Matrix of a Quadratic Form

#### Question

The matrix of the quadratic form is given above. What is the value of

#### Explanation

Since the matrix of the quadratic form must be symmetric, we rewrite our expression as follows:

Notice that to get a symmetric matrix, we must do the following splits:

- we split the coefficient of between the entries and

- we split the coefficient of between the entries

So, the matrix corresponding to our quadratic form is

Therefore, and Finally,
