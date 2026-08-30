# Diagonalization of 3x3 Symmetric Matrices

Source: https://www.mathacademy.com/topics/3119?courseId=55
Topic ID: 3119

## Prerequisites

- [Diagonalizing a 3x3 Matrix in the General Case](./1971-diagonalizing-a-3x3-matrix-in-the-general-case.md)
- [The Gram-Schmidt Process for Two Vectors](./2127-the-gram-schmidt-process-for-two-vectors.md)
- [Diagonalization of 2x2 Symmetric Matrices](./3335-diagonalization-of-2x2-symmetric-matrices.md)

## Lesson

### Introduction

Recall that a matrix $A$ is orthogonally diagonalizable if there exists an orthogonal matrix $P$ such that

$$


A=PDP^T,


$$

where $D$ is a diagonal matrix.

Moreover, a real matrix $A$ is orthogonally diagonalizable if and only if it is symmetric.

The procedure for finding an orthogonal diagonalization of a $3 \times 3$ symmetric matrix $A$ is similar to diagonalizing a regular (diagonalizable) $3\times 3$ matrix:

- **Step 1**: Find the eigenvalues of $A.$

- **Step 2**: Find a basis of $\mathbb{R}^3$ consisting of *unit orthogonal* eigenvectors of $A.$

- **Step 3**: Construct the matrices $D$ and $P.$

As an example, consider the matrix

$$


\begin{aligned}−2 & −5 & 1 \\ −5 & −2 & 1 \\ 1 & 1 & −8\end{aligned}


$$

This matrix is symmetric. So let's apply our diagonalization algorithm.

- **Step 1.** We find the eigenvalues of $A$ by solving $\det(A-\lambda I)=0.$ This gives

- **Step 2.** We need to find an eigenvector basis of $\mathbb R^3.$ Seeking a nonzero solution of $|A-\lambda_i I| = 0$ for $i=1,2,3,$ we get the corresponding eigenvectors Notice that the eigenvectors are mutually orthogonal. Now, an orthogonal diagonalization requires each eigenvector to be normalized. So, dividing each eigenvector by its norm, we obtain the following unit orthogonal eigenvectors:

- **Step 3.** We construct the diagonal matrix $D$ and the orthogonal matrix $P$ as follows:

**Watch out!** In this example, we automatically get orthogonal eigenvectors because $A$ has three *distinct* eigenvalues. However, in the case of repeated eigenvalues, the corresponding eigenvectors might not be orthogonal.

### Example: Identifying Parts of an Orthogonal Diagonalization

#### Question

$$


\begin{aligned}\frac{\sqrt{√3}}{3} & \frac{\sqrt{√2}}{2} & \,∗\, \\ \frac{\sqrt{√3}}{3} & 0 & \,∗\, \\ \frac{\sqrt{√3}}{3} & −\frac{\sqrt{√2}}{2} & \,∗\,\end{aligned}


$$

Consider the matrix $P$ shown above. Given that $A=PDP^T$ is an orthogonal diagonalization of a $3 \times 3$ symmetric matrix $A$ for some diagonal matrix $D,$ which of the following could be the third column of the matrix $P?$

$$


\begin{aligned}0 \\ −1 \\ 0\end{aligned}


$$

#### Explanation

Recall that a matrix $A$ is orthogonally diagonalizable if there exists an orthogonal matrix $P$ such that

$$


A=PDP^T,


$$

where $D$ is a diagonal matrix.

Moreover, a matrix $A$ is orthogonally diagonalizable if and only if it is symmetric.

Since $A=PDP^T$ is an orthogonal diagonalization of a $3\times 3$ symmetric matrix $A,$ the matrix $P$ must be a $3\times 3$ orthogonal matrix. This means that

- the third column must be orthogonal to the first and second columns, and

- the norm of the third column must be equal to $1.$

Among the given options, only the vector $\begin{aligned}\frac{\sqrt{√6}}{6} \\ −\frac{\sqrt{√6}}{3} \\ \frac{\sqrt{√6}}{6}\end{aligned}$ has both properties.

### Example: Orthogonally Diagonalizing a 3x3 Matrix With Distinct Eigenvalues

#### Question

$$


\begin{aligned}1 & 1 & −1 \\ 1 & 1 & −1 \\ −1 & −1 & 3\end{aligned}


$$

Consider the matrices shown above. Given that $D=P^T \! AP,$ where $P$ is an orthogonal matrix, find the third column of the matrix $P.$

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

From the diagonal matrix $D$ we deduce that the eigenvalues of the matrix $A$ are $\lambda_1=0,$ $\lambda_2=1,$ and $\lambda_3=4.$ So, the third column of $P$ corresponds to the eigenvalue $\lambda_3=4.$

Now, we need to find an eigenvector that corresponds to $\lambda_3=4.$ Computing $A-4I,$ we get

$$


\begin{aligned}𝐴−4𝐼 & =\begin{aligned}1 & 1 & −1 \\ 1 & 1 & −1 \\ −1 & −1 & 3\end{aligned}−4\begin{aligned}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{aligned}=\begin{aligned}−3 & 1 & −1 \\ 1 & −3 & −1 \\ −1 & −1 & −1\end{aligned}.\end{aligned}


$$

Seeking a non-zero solution of $(A-4I)\mathbf{x}=\mathbf{0}$ gives the eigenvector

$$


\begin{aligned}−1 \\ −1 \\ 2\end{aligned}


$$

where $\| \mathbf{v}_3 \| = \sqrt{6}.$ Dividing $\mathbf{v}_3$ by its norm, we obtain the third column of $P\mathbin{:}$

$$


\begin{aligned}−1 \\ −1 \\ 2\end{aligned}


$$

### Symmetric Matrices With Repeated Eigenvalues

Let's recall the algorithm for diagonalizing a $3\times 3$ symmetric matrix $A.$

- **Step 1**: Find the eigenvalues of $A.$

- **Step 2**: Find a basis of $\mathbb{R}^3$ consisting of unit orthogonal eigenvectors of $A.$

- **Step 3**: Construct the matrices $D$ and $P.$

Note the following important points regarding step 2 of this process:

- If $A$ has mutually distinct eigenvalues, the eigenvectors will automatically be orthogonal, so we only need to normalize them.

- If $A$ has *repeated* eigenvalues, then the eigenvectors corresponding to these repeated eigenvalues *may not* be orthogonal. Therefore, we have to apply the Gram-Schmidt process to obtain orthogonal vectors.

For example, consider the following matrix:

$$


\begin{aligned}2 & −2 & 2 \\ −2 & 2 & 2 \\ 2 & 2 & 2\end{aligned}


$$

This matrix is symmetric. Let's apply our diagonalization algorithm.

- **Step 1.** We find the eigenvalues of $A$ by solving $\det(A-\lambda I)=0\mathbin{:}$

- **Step 2.** Now, we need to find an eigenvector basis of $\mathbb R^3.$ Seeking a nonzero solution of $|A-\lambda_i I| = 0$ for $i=1,2,3,$ we get the corresponding eigenvectors Notice that $\mathbf{v}_1$ and $\mathbf{v}_2$ are not orthogonal. So, we proceed using the Gram-Schmidt process. We set and we find $\mathbf{e}_2$ as follows: So, the vectors $\mathbf e_1, \mathbf e_2$ and $\mathbf v_3$ form an *orthogonal* basis of $\mathbb R^3.$ Dividing each eigenvector by its norm, we obtain the unit orthogonal eigenvectors:

- **Step 3.** We construct the diagonal matrix $D$ and the invertible matrix $P$ as follows:

### Example: Orthogonally Diagonalizing a 3x3 Matrix With Repeated Eigenvalues

#### Question

$$


\begin{aligned}3 & 2 & 4 \\ 2 & 0 & 2 \\ 4 & 2 & 3\end{aligned}


$$

Consider the matrices shown above. Given that $D=P^T \! AP,$ where $P$ is an orthogonal matrix, find the first and second columns of the matrix $P.$

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

From the diagonal matrix $D$ we deduce that the eigenvalues of the matrix $A$ are $\lambda_1=-1,$ $\lambda_2=-1,$ and $\lambda_3=8.$ So, the first and second columns of $P$ correspond to the eigenvalue $\lambda=-1.$

Now, we need to find eigenvectors that correspond to $\lambda_1=\lambda_2=-1.$ Computing $A-(-1)I,$ we get

$$


\begin{aligned}𝐴−(−1)𝐼 & =\begin{aligned}3 & 2 & 4 \\ 2 & 0 & 2 \\ 4 & 2 & 3\end{aligned}+\begin{aligned}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{aligned}=\begin{aligned}4 & 2 & 4 \\ 2 & 1 & 2 \\ 4 & 2 & 4\end{aligned}.\end{aligned}


$$

Seeking a non-zero solution of $(A-(-1)I)\mathbf{x}=\mathbf{0}$ gives two eigenvectors:

$\qquad$ $\begin{aligned}−1 \\ 2 \\ 0\end{aligned}$ and $\begin{aligned}−1 \\ 0 \\ 1\end{aligned}$

Notice that eigenvectors $\mathbf{v}_1$ and $\mathbf{v}_2$ are not orthogonal. So, we proceed using the Gram-Schmidt process. We set

$$


\begin{aligned}−1 \\ 2 \\ 0\end{aligned}


$$

and we find $\mathbf{e}_2$ as follows:

$$


\begin{aligned}𝐞_{2} & =𝐯_{2}−\frac{𝐯_{2}⋅𝐞_{1}}{𝐞_{1}⋅𝐞_{1}}𝐞_{1} \\ & =𝐯_{2}−\frac{1}{5}𝐞_{1} \\ & =\begin{aligned}−1 \\ 0 \\ 1\end{aligned}−\frac{1}{5}\begin{aligned}−1 \\ 2 \\ 0\end{aligned} \\ & =\begin{aligned}−\frac{4}{5} \\ −\frac{2}{5} \\ 1\end{aligned}\end{aligned}


$$

Finally, dividing $\mathbf{e}_1$ and $\mathbf{e}_2$ by their respective norms, we obtain the first and second columns of $P\mathbin{:}$

$$


\begin{aligned}\frac{𝐞_{1}}{‖𝐞_{1}‖} & =\frac{1}{\sqrt{√5}}\begin{aligned}−1 \\ 2 \\ 0\end{aligned}=\begin{aligned}−\frac{\sqrt{√5}}{5} \\ \frac{2\sqrt{√5}}{5} \\ 0\end{aligned} \\ \frac{𝐞_{2}}{‖𝐞_{2}‖} & =\frac{\sqrt{√5}}{3}\begin{aligned}−\frac{4}{5} \\ −\frac{2}{5} \\ 1\end{aligned}=\begin{aligned}−\frac{4\sqrt{√5}}{15} \\ −\frac{2\sqrt{√5}}{15} \\ \frac{\sqrt{√5}}{3}\end{aligned}\end{aligned}


$$
