# Jordan Canonical Form of a 2x2 Matrix

Source: https://www.mathacademy.com/topics/3629?courseId=55
Topic ID: 3629

## Prerequisites

- [Properties of Diagonalization](./1969-properties-of-diagonalization.md)
- [Generalized Eigenvectors](./2738-generalized-eigenvectors.md)
- [Jordan Blocks and Jordan Matrices](./3114-jordan-blocks-and-jordan-matrices.md)

## Lesson

### Introduction

Not every square matrix is diagonalizable. However, if a square matrix is not diagonalizable, it is "almost" diagonalizable.

More precisely, every $n\times n$ matrix $A$ can be written in the form

$$


A = PJP^{-1},


$$

where $J$ is a Jordan matrix, and $P$ is an invertible matrix. We say that $J$ is a **Jordan canonical form** (or **Jordan normal form**) of $A.$

Not all square matrices have corresponding diagonal matrices. However, *all* square matrices have Jordan canonical forms. A Jordan canonical form is either diagonal or "almost" diagonal.

Our goal in this lesson is to find a Jordan canonical form of any $2\times 2$ matrix.

If a matrix is diagonalizable, then finding its Jordan canonical form is equivalent to finding its diagonal form.

For diagonalizable $2\times 2$ matrices, we have two separate cases:

- $A$ has two distinct eigenvalues.

- $A$ is a **scalar matrix**. A diagonal matrix is scalar if every value on the leading diagonal is the same.

Let's discuss these two cases first. Then, we will discuss the final case, which is when $A$ is not diagonalizable.

### Example: Finding a Jordan Canonical Form of a 2x2 Matrix With Two Distinct Eigenvalues

#### Question

Find a Jordan canonical form of the matrix $[\begin{aligned}5 & 4 \\ 2 & −2\end{aligned}]$

#### Explanation

Every $n\times n$ matrix $A$ can be written in the form

$$


A = PJP^{-1},


$$

where $J$ is a Jordan canonical form (or Jordan normal form) of $A,$ and $P$ is an invertible matrix.

To find the matrix $J,$ we first find the eigenvalues of the matrix $A$ by solving $\det(A-\lambda I)=0{:}$

$$


\begin{aligned}\begin{matrix}5−𝜆 & 4 \\ 2 & −2−𝜆\end{matrix} & =0 \\ (5−𝜆)(−2−𝜆)−4⋅2 & =0 \\ 𝜆^{2}−3𝜆−18 & =0 \\ (𝜆−6)(𝜆+3) & =0\end{aligned}


$$

So, the eigenvalues are $\lambda_1=-3$ and $\lambda_2=6.$ Since we get two distinct eigenvalues, the matrix $A$ is diagonalizable, and a Jordan canonical form is

$$


[\begin{aligned}−3 & 0 \\ 0 & 6\end{aligned}]


$$

****: A Jordan canonical form is unique up to permutations of its Jordan blocks. Therefore, another Jordan canonical form for this matrix is

$$


[\begin{aligned}6 & 0 \\ 0 & −3\end{aligned}]


$$

### Example: Finding a Jordan Canonical Form of a 2x2 Scalar Matrix

#### Question

Find the Jordan canonical form of the matrix $[\begin{aligned}−3 & 0 \\ 0 & −3\end{aligned}]$

#### Explanation

Every $n\times n$ matrix $A$ can be written in the form

$$


A = PJP^{-1},


$$

where $J$ is a Jordan canonical form (or Jordan normal form) of $A,$ and $P$ is an invertible matrix.

Notice that $A$ is a scalar matrix, which means that it is already in Jordan canonical form. Therefore, it has a single (repeated) eigenvalue $\lambda = -3,$ and

$$


[\begin{aligned}−3 & 0 \\ 0 & −3\end{aligned}]


$$

### Finding a Jordan Canonical Form of a Non-Diagonalizable 2x2 Matrix

When a $2\times 2$ matrix with repeated eigenvalue $\lambda$ is not diagonalizable, its Jordan canonical form is given by

$$


J = J_2(\lambda).


$$

As an example, let's find a Jordan canonical form of the matrix

$$


[\begin{aligned}5 & 4 \\ −1 & 1\end{aligned}]


$$

We first find the eigenvalues of $A$ by solving $\det(A-\lambda I)=0{:}$

$$


\begin{aligned}\begin{matrix}5−𝜆 & 4 \\ −1 & 1−𝜆\end{matrix} & =0 \\ (5−𝜆)(1−𝜆)−4⋅(−1) & =0 \\ 𝜆^{2}−6𝜆+9 & =0 \\ (𝜆−3)(𝜆−3) & =0\end{aligned}


$$

Therefore, the eigenvalues are $\lambda_1=\lambda_2=3.$

Since $A$ has a repeated eigenvalue and is not a scalar matrix, we conclude that $A$ is not diagonalizable.

Therefore, in this case, the Jordan canonical form of $A$ is

$$


[\begin{aligned}3 & 1 \\ 0 & 3\end{aligned}]


$$

Note that $J$ is "almost" diagonal.

### Example: Finding a Jordan Canonical Form of a 2x2 Matrix With Only One Eigenvalue

#### Question

Find the Jordan canonical form of the matrix $[\begin{aligned}2 & 3 \\ −3 & −4\end{aligned}]$

#### Explanation

Every $n\times n$ matrix $A$ can be written in the form

$$


A = PJP^{-1},


$$

where $J$ is a Jordan canonical form (or Jordan normal form) of $A,$ and $P$ is an invertible matrix.

To find the matrix $J,$ we first find the eigenvalues of the matrix $A$ by solving $\det(A-\lambda I)=0{:}$

$$


\begin{aligned}\begin{matrix}2−𝜆 & 3 \\ −3 & −4−𝜆\end{matrix} & =0 \\ (2−𝜆)(−4−𝜆)−3⋅(−3) & =0 \\ 𝜆^{2}+2𝜆+1 & =0 \\ (𝜆+1)(𝜆+1) & =0\end{aligned}


$$

Therefore, the eigenvalues are $\lambda_1=\lambda_2=-1.$

Since $A$ is not a scalar matrix, we conclude that $A$ is not diagonalizable, and its Jordan canonical form is

$$


[\begin{aligned}−1 & 1 \\ 0 & −1\end{aligned}]


$$

### Overview of All Possible Jordan Canonical Forms of 2x2 Matrices

Given a $2 \times 2$ matrix $A,$ we have $3$ possible cases:

- If $A$ has two distinct eigenvalues $\lambda_1 \neq \lambda_2,$ then $A$ is diagonalizable, and $J$ is a diagonal matrix. In this case, $J$ is a composition of two distinct $1 \times 1$ Jordan blocks:

- If $A$ has only one eigenvalue $\lambda$ of algebraic multiplicity $2$ and there exist two linearly independent eigenvectors corresponding to this eigenvalue, then $A$ must be a scalar matrix. This situation corresponds to the case where $A$ is already diagonalized, and $J$ is a composition of two identical $1 \times 1$ Jordan blocks:

- If $A$ has only one eigenvalue $\lambda$ of algebraic multiplicity $2$ and only one linearly independent eigenvector exists that corresponds to this eigenvalue, then $A$ is not diagonalizable. In this case, $J$ is a single $2 \times 2$ Jordan block:

So, in two out of three cases, our matrix is diagonalizable. But in the third case, the closest we can get to a diagonal matrix is a Jordan block with a $1$ on the superdiagonal.
