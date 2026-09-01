# The Spectral Theorem

Source: https://www.mathacademy.com/topics/3120?courseId=155
Topic ID: 3120

## Prerequisites

- [Projection Matrices, Linear Transformations and Their Properties](./2125-projection-matrices-linear-transformations-and-their-properties.md)
- [Diagonalization of 3x3 Symmetric Matrices](./3119-diagonalization-of-3x3-symmetric-matrices.md)

## Lesson

### Introduction

Suppose that $A$ is an $n\times n$ symmetric matrix over $\mathbb{R}.$ The **spectral theorem** states the following:

- The eigenvalues of $A$ are all real.

- The eigenvectors corresponding to *different* eigenvalues are orthogonal.

- The dimension of the eigenspace for each eigenvalue equals the multiplicity of that eigenvalue as a root of the characteristic polynomial.

- $A$ is orthogonally diagonalizable.

### Example: Identifying True Statements Regarding the Spectral Theorem

#### Question

Given that $A$ is a real symmetric matrix, which of the following statements are true?

1. $A$ must have all real eigenvalues

2. $A$ is diagonalizable

3. If $\mathbf{u}$ and $\mathbf{v}$ are two eigenvectors, then $\mathbf{u} \perp \mathbf{v}$

#### Explanation

Given that $A$ is an $n \times n$ symmetric matrix over $\mathbb{R}$, the spectral theorem states the following:

- The eigenvalues of $A$ are all real.

- Eigenvectors corresponding to different eigenvalues are orthogonal.

- $A$ is orthogonally diagonalizable.

With that in mind, let's examine our statements in turn.

- Statement I is true. Indeed, the eigenvalues of a symmetric matrix are real.

- Statement II is true. Indeed, any symmetric matrix with real entries is orthogonally diagonalizable. Hence, it is diagonalizable.

- Statement III is false. According to the theorem, eigenvectors corresponding to ** eigenvalues must be orthogonal, but two eigenvectors corresponding to the ** eigenvalue may not be orthogonal.

Therefore, the correct answer is "I and II only."

### The Spectral Decomposition of a Symmetric Matrix

We can write an $n\times n$ symmetric matrix $A$ in terms of a sum of products of its eigenvalues and eigenvectors.

Specifically, if $\mathbf{u}_i$ denotes an orthonormal eigenvector of $A$ corresponding to the eigenvalue $\lambda_i$ for $i=1,\ldots, n$, then

$$


A=\sum_{i=1}^n \lambda_i \mathbf{u}_i \mathbf{u}_i^T.


$$

Expressing a symmetric matrix $A$ in this way is called the **spectral decomposition** of $A.$

To demonstrate, let's find the spectral decomposition of the $2\times 2$ symmetric matrix $A,$ given by

$$


[\begin{aligned}−3 & 3 \\ 3 & 5\end{aligned}]


$$

The eigenvalues of $A$ are $\lambda_1 = 6$ and $\lambda_2 = -4,$ and the corresponding eigenvectors are

$$


[\begin{aligned}1 \\ 3\end{aligned}]


$$

The spectral decomposition of $A$ is given by

$$


A =\sum_{i=1}^2 \lambda_i \mathbf{u}_i \mathbf{u}_i^T = \lambda_1 \mathbf u_1 \mathbf u_1^T + \lambda_2 \mathbf u_2 \mathbf u_2^T,


$$

where $\mathbf u_1$ and $\mathbf u_2$ are orthonormal eigenvectors of $A$ corresponding to $\lambda_1$ and $\lambda_2,$ respectively.

First, let's normalize our eigenvectors:

$$


\begin{aligned}𝐮_{1} & =\frac{𝐯_{1}}{‖𝐯_{1}‖}=\frac{1}{\sqrt{10}}[\begin{matrix}1 \\ 3\end{matrix}] \\ 𝐮_{2} & =\frac{𝐯_{2}}{‖𝐯_{2}‖}=\frac{1}{\sqrt{10}}[\begin{matrix}3 \\ −1\end{matrix}]\end{aligned}


$$

Therefore, the spectral decomposition of $A$ is

$$


\begin{aligned}𝐴 & =𝜆_{1}𝐮_{1}𝐮_{𝑇1}+𝜆_{2}𝐮_{2}𝐮_{𝑇2} \\ & =6⋅\frac{1}{\sqrt{10}}[\begin{matrix}1 \\ 3\end{matrix}]⋅\frac{1}{\sqrt{10}}[\begin{matrix}1 & 3\end{matrix}]+(−4)⋅\frac{1}{\sqrt{10}}[\begin{matrix}3 \\ −1\end{matrix}]⋅\frac{1}{\sqrt{10}}[\begin{matrix}3 & −1\end{matrix}] \\ & =6⋅\frac{1}{10}[\begin{matrix}1 \\ 3\end{matrix}]⋅[\begin{matrix}1 & 3\end{matrix}]+(−4)⋅\frac{1}{10}[\begin{matrix}3 \\ −1\end{matrix}]⋅[\begin{matrix}3 & −1\end{matrix}] \\ & =\underset{𝜆_{1}}{\underset{}{6}}⋅\underset{𝐮_{1}𝐮_{𝑇1}}{\begin{matrix}\frac{1}{10} & \frac{3}{10} \\ \frac{3}{10} & \frac{9}{10}\end{matrix}}+\underset{𝜆_{2}}{\underset{}{(−4)}}⋅\underset{𝐮_{2}𝐮_{𝑇2}}{\begin{matrix}\frac{9}{10} & −\frac{3}{10} \\ −\frac{3}{10} & \frac{1}{10}\end{matrix}}.\end{aligned}


$$

In this decomposition, the matrix $\mathbf{u}_i \mathbf{u}_i^T$ is the orthogonal projection matrix that maps any $\mathbf x \in \mathbb R^2$ onto the subspace spanned by $\mathbf u_i.$

### Example: Finding the Spectral Decomposition of a Symmetric Matrix

#### Question

Suppose that

$\qquad$ $[\begin{aligned}2 \\ 3\end{aligned}]$ and $[\begin{aligned}−3 \\ 2\end{aligned}]$

are eigenvectors of a $2 \times 2$ symmetric matrix $A$ that correspond to the eigenvalues $\lambda_1=6$ and $\lambda_2=-7,$ respectively. Find the matrix $A.$

#### Explanation

The spectral decomposition of a $2\times 2$ symmetric matrix $A$ is given by

$$


A = \lambda_1 \mathbf u_1\cdot \mathbf u_1^T + \lambda_2 \mathbf u_2\cdot \mathbf u_2^T,


$$

where $\mathbf u_1$ and $\mathbf u_2$ are orthonormal eigenvectors of $A$ corresponding to the eigenvalues $\lambda_1$ and $\lambda_2,$ respectively.

First, let's normalize our eigenvectors:

$$


\begin{aligned}𝐮_{1} & =\frac{𝐯_{1}}{‖𝐯_{1}‖}=\frac{1}{\sqrt{13}}[\begin{matrix}2 \\ 3\end{matrix}] \\ 𝐮_{2} & =\frac{𝐯_{2}}{‖𝐯_{2}‖}=\frac{1}{\sqrt{13}}[\begin{matrix}−3 \\ 2\end{matrix}]\end{aligned}


$$

Therefore, we have

$$


\begin{aligned}𝐴 & =𝜆_{1}𝐮_{1}𝐮_{𝑇1}+𝜆_{2}𝐮_{2}𝐮_{𝑇2} \\ & =6⋅\frac{1}{\sqrt{13}}[\begin{matrix}2 \\ 3\end{matrix}]⋅\frac{1}{\sqrt{13}}[\begin{matrix}2 & 3\end{matrix}]+(−7)⋅\frac{1}{\sqrt{13}}[\begin{matrix}−3 \\ 2\end{matrix}]⋅\frac{1}{\sqrt{13}}[\begin{matrix}−3 & 2\end{matrix}] \\ & =6⋅\frac{1}{13}[\begin{matrix}2 \\ 3\end{matrix}][\begin{matrix}2 & 3\end{matrix}]+(−7)⋅\frac{1}{13}[\begin{matrix}−3 \\ 2\end{matrix}][\begin{matrix}−3 & 2\end{matrix}] \\ & =\frac{1}{13}(6⋅[\begin{matrix}2 \\ 3\end{matrix}][\begin{matrix}2 & 3\end{matrix}]+(−7)⋅[\begin{matrix}−3 \\ 2\end{matrix}][\begin{matrix}−3 & 2\end{matrix}]) \\ & =\frac{1}{13}(6⋅[\begin{matrix}4 & 6 \\ 6 & 9\end{matrix}]+(−7)⋅[\begin{matrix}9 & −6 \\ −6 & 4\end{matrix}]) \\ & =\frac{1}{13}[\begin{matrix}−39 & 78 \\ 78 & 26\end{matrix}] \\ & =[\begin{matrix}−3 & 6 \\ 6 & 2\end{matrix}].\end{aligned}


$$

### Example: Finding a Projection Matrix That Orthogonally Projects a Vector to the Subspace Spanned by an Eigenvector

#### Question

Find the orthogonal projection matrix that maps $\mathbf x\in \mathbb R^2$ onto the subspace spanned by an eigenvector corresponding to the eigenvalue $\lambda=-1$ of the matrix $[\begin{aligned}3 & −2 \\ −2 & 0\end{aligned}]$

#### Explanation

The spectral decomposition of a $2\times 2$ symmetric matrix $A$ is given by

$$


A = \lambda_1 \mathbf u_1\cdot \mathbf u_1^T + \lambda_2 \mathbf u_2\cdot \mathbf u_2^T,


$$

where $\mathbf u_1$ and $\mathbf u_2$ are orthonormal eigenvectors of $A$ corresponding to the eigenvalues $\lambda_1$ and $\lambda_2,$ respectively.

Moreover, $\mathbf u_i\cdot \mathbf u_i^T$ is the projection matrix corresponding to $\mathbf u_i.$

First, we need to find an eigenvector that corresponds to $\lambda=-1.$ Computing $A-(-1)I,$ we get

$$


\begin{aligned}𝐴−(−1)𝐼 & =[\begin{matrix}3 & −2 \\ −2 & 0\end{matrix}]−(−1)[\begin{matrix}1 & 0 \\ 0 & 1\end{matrix}]=[\begin{matrix}4 & −2 \\ −2 & 1\end{matrix}].\end{aligned}


$$

So, we have a system of linear equations with the augmented matrix $M$ which we reduce to row echelon form using Gaussian elimination, as follows:

$$


\begin{aligned}𝑀 & =[\begin{matrix}4 & −2 & 0 \\ −2 & 1 & 0\end{matrix}] & 𝑅_{2} & :=𝑅_{2}+\frac{1}{2}𝑅_{1} \\ & ∼[\begin{matrix}4 & −2 & 0 \\ 0 & 0 & 0\end{matrix}] & & \end{aligned}


$$

The reduced matrix above has one pivot column (the $1$st one). Thus, $x_2$ is a free variable. From the first equation, we obtain $x_1=\dfrac12x_2.$ Hence, the general solution is

$$


\begin{aligned}\frac{1}{2}𝑥_{2} \\ 𝑥_{2}\end{aligned}


$$

Therefore, setting $x_2=2,$ we get the eigenvector

$$


[\begin{aligned}1 \\ 2\end{aligned}]


$$

where $\| \mathbf{v} \| = \sqrt{5}.$ Dividing $\mathbf{v}$ by its norm, we obtain the normalized eigenvector:

$$


[\begin{aligned}1 \\ 2\end{aligned}]


$$

Finally, the required orthogonal projection matrix is given by

$$


\begin{aligned}𝐮⋅𝐮^{𝑇} & =\frac{1}{\sqrt{5}}[\begin{matrix}1 \\ 2\end{matrix}]⋅\frac{1}{\sqrt{5}}[\begin{matrix}1 & 2\end{matrix}] \\ & =\frac{1}{5}[\begin{matrix}1 \\ 2\end{matrix}]⋅[\begin{matrix}1 & 2\end{matrix}] \\ & =\frac{1}{5}[\begin{matrix}1 & 2 \\ 2 & 4\end{matrix}].\end{aligned}


$$
