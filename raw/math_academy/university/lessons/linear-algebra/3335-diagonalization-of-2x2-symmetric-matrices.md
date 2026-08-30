# Diagonalization of 2x2 Symmetric Matrices

Source: https://www.mathacademy.com/topics/3335?courseId=55
Topic ID: 3335

## Prerequisites

- [Diagonalizing a 2x2 Matrix](./1968-diagonalizing-a-2x2-matrix.md)
- [Symmetric Matrices](./3118-symmetric-matrices.md)
- [Orthogonal Linear Transformations](./4319-orthogonal-linear-transformations.md)

## Lesson

### Introduction

A square matrix $A$ is **orthogonally diagonalizable** if there exists an orthogonal matrix $P$ such that

$$


A=PDP^T,


$$

where $D$ is a diagonal matrix. Note that this is equivalent to the equation

$$


D = P^TAP.


$$

So, to orthogonally diagonalize a matrix $A,$ we need to find a diagonal matrix $D$ and an orthogonal matrix $P$ that satisfies the above equations.

A helpful theorem allows us to determine whether a real matrix is orthogonally diagonalizable. It states the following:

*A matrix $A$ with real entries is orthogonally diagonalizable if and only if it is symmetric.*

Consequently, *every* symmetric matrix is orthogonally diagonalizable!

For example, the symmetric matrix

$$


[\begin{aligned}3 & 3 \\ 3 & −5\end{aligned}]


$$

has the orthogonal diagonalization

$$


\begin{aligned}𝐴 & =\underset{𝑃}{\underset{}\begin{aligned}\frac{3}{\sqrt{√10}} & \frac{1}{\sqrt{√10}} \\ \frac{1}{\sqrt{√10}} & −\frac{3}{\sqrt{√10}}\end{aligned}}}\underset{𝐷}{\underset{}\begin{aligned}4 & 0 \\ 0 & −6\end{aligned}}}\underset{𝑃^{𝑇}}{\underset{}\begin{aligned}\frac{3}{\sqrt{√10}} & \frac{1}{\sqrt{√10}} \\ \frac{1}{\sqrt{√10}} & −\frac{3}{\sqrt{√10}}\end{aligned}^{𝑇}}},\end{aligned}


$$

where $P$ is orthogonal, and $D$ is diagonal. As usual, the entries on the main diagonal of $D$ are the eigenvalues of $A.$ Also, the columns of $P$ are *orthonormal* eigenvectors corresponding to the eigenvalues of $A.$

The procedure of the orthogonal diagonalization of a $2 \times 2$ real symmetric matrix $A$ is almost the same as the diagonalization of a matrix:

- **Step 1**: Find the eigenvalues of the matrix $A$.

- **Step 2**: Find a basis of $\mathbb{R}^2$ consisting of *unit orthogonal* eigenvectors of $A.$

- **Step 3**: Construct the matrices $D$ and $P.$

In the case of symmetric matrices, the two eigenvectors we compute in step 2 will always be orthogonal, provided that they correspond to different eigenvalues. However, we must also ensure that we *normalize* those eigenvectors.

### Example: Identifying Parts of an Orthogonal Diagonalization

#### Question

$$


\begin{aligned}\,∗\, & −\frac{\sqrt{√10}}{10} \\ \,∗\, & −\frac{3\sqrt{√10}}{10}\end{aligned}


$$

Consider the matrix $P$ shown above. Given that $A=PDP^T$ is an orthogonal diagonalization of a $2\times 2$ symmetric matrix $A$ for some diagonal matrix $D,$ which of the following could be the first column of the matrix $P?$

$$


\begin{aligned}\frac{3\sqrt{√10}}{10} \\ −\frac{\sqrt{√10}}{10}\end{aligned}


$$

#### Explanation

Recall that a matrix $A$ is orthogonally diagonalizable if there exists an orthogonal matrix $P$ such that

$$


A=PDP^T,


$$

where $D$ is a diagonal matrix.

Moreover, a matrix $A$ is orthogonally diagonalizable if and only if it is symmetric.

Since $A=PDP^T$ is an orthogonal diagonalization of a $2\times 2$ symmetric matrix $A,$ the matrix $P$ must be a $2\times 2$ orthogonal matrix. This means that

- the first column must be orthogonal to the second column, and

- the norm of the first column must be equal to $1.$

Among the given options, only the vector $\begin{aligned}\frac{3\sqrt{√10}}{10} \\ −\frac{\sqrt{√10}}{10}\end{aligned}$ has both properties.

### Example: Orthogonally Diagonalizing a 2x2 Symmetric Matrix Given Part of the Diagonalization

#### Question

$$


[\begin{aligned}0 & −1 \\ −1 & 0\end{aligned}]


$$

Consider the matrices shown above. Given that $D=P^T \! AP,$ where $P$ is an orthogonal matrix, which of the following could be the first column of the matrix $P?$

$$


\begin{aligned}\frac{\sqrt{√2}}{2} \\ \frac{\sqrt{√2}}{2}\end{aligned}


$$

#### Explanation

Recall that a matrix $A$ is orthogonally diagonalizable if there exists an orthogonal matrix $P$ such that

$$


A=PDP^T,


$$

where $D$ is a diagonal matrix. Equivalently,

$$


D=P^TAP.


$$

Moreover, a matrix $A$ is orthogonally diagonalizable if and only if it is symmetric.

First, note that $A$ is symmetric and $D$ is diagonal. Therefore, $D=P^T \! AP$ gives an orthogonal diagonalization of $A.$

From the diagonal matrix $D$ we deduce that the eigenvalues of the matrix $A$ are $\lambda_1=-1$ and $\lambda_2=1.$ So, the first column of $P$ corresponds to the eigenvalue $\lambda_1=-1.$

Now, we need to find an eigenvector that corresponds to $\lambda_1=-1.$ Computing $A-(-1)I,$ we get

$$


\begin{aligned}𝐴+𝐼 & =[\begin{aligned}0 & −1 \\ −1 & 0\end{aligned}]+[\begin{aligned}1 & 0 \\ 0 & 1\end{aligned}] \\ & =[\begin{aligned}1 & −1 \\ −1 & 1\end{aligned}].\end{aligned}


$$

So, we have a system of linear equations with the augmented matrix $M$ which we reduce to row echelon form using Gaussian elimination, as follows:

$$


\begin{aligned}𝑀 & =[\begin{aligned}1 & −1 & 0 \\ −1 & 1 & 0\end{aligned}] & 𝑅_{2} & :=𝑅_{2}+𝑅_{1} \\ & ∼[\begin{aligned}1 & −1 & 0 \\ 0 & 0 & 0\end{aligned}] & & \end{aligned}


$$

The reduced matrix above has one pivot column (the $1$st one). Thus, $x_2$ is a free variable. From the first equation, we obtain $x_1=x_2.$ Hence, the general solution is

$$


[\begin{aligned}𝑥_{2} \\ 𝑥_{2}\end{aligned}]


$$

Therefore, setting $x_2=1,$ we get the eigenvector

$$


[\begin{aligned}1 \\ 1\end{aligned}]


$$

where $\| \mathbf{v}_1 \| = \sqrt{2}.$ Dividing $\mathbf{v}_1$ by its norm, we obtain the first column of $P\mathbin{:}$

$$


[\begin{aligned}1 \\ 1\end{aligned}]


$$

### Example: Orthogonally Diagonalizing a 2x2 Symmetric Matrix

#### Question

$$


[\begin{aligned}1 & 6 \\ 6 & −4\end{aligned}]


$$

The matrix $A$ above has eigenvalues $\lambda_1=5$ and $\lambda_2=-8.$ Find a diagonal matrix $D$ and an orthogonal matrix $P$ such that $D=P^T \! A P.$

#### Explanation

Recall that a matrix $A$ is orthogonally diagonalizable if there exists an orthogonal matrix $P$ such that

$$


A=PDP^T,


$$

where $D$ is a diagonal matrix. Equivalently,

$$


D=P^TAP.


$$

Moreover, a matrix $A$ is orthogonally diagonalizable if and only if it is symmetric.

Note that $A$ is symmetric. Therefore, it is orthogonally diagonalizable. Let's now go through the process.

**** Notice that we already have the eigenvalues of $A\mathbin{:}$

$\qquad$ $\lambda_1=5\quad$ and $\quad \lambda_2=-8$

**** Now, we need to find an eigenvector basis of $A.$

- For $\lambda_1=5,$ we have Seeking a non-zero solution of $(A-5I)\mathbf{x}=\mathbf{0}$ gives the eigenvector $[\begin{aligned}3 \\ 2\end{aligned}]$ Dividing $\mathbf{v}_1$ by its norm $\| \mathbf{v}_1 \| = \sqrt{13},$ we get

- For $\lambda_2=-8,$ we have Seeking a non-zero solution of $(A-(-8)I)\mathbf{x}=\mathbf{0}$ gives the eigenvector $[\begin{aligned}−2 \\ 3\end{aligned}]$ Dividing $\mathbf{v}_2$ by its norm $\| \mathbf{v}_2 \| = \sqrt{13},$ we get

**** We construct the diagonal matrix $D$ and the orthogonal matrix $P$ in the usual way, and this gives us the following:

$$


[\begin{aligned}5 & 0 \\ 0 & −8\end{aligned}]


$$
