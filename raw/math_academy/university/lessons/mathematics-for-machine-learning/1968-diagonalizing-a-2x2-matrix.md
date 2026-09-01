# Diagonalizing a 2x2 Matrix

Source: https://www.mathacademy.com/topics/1968?courseId=145
Topic ID: 1968

## Prerequisites

- [Calculating the Eigenvectors of a 2x2 Matrix](./991-calculating-the-eigenvectors-of-a-2x2-matrix.md)
- [Changing a Basis Using the Change-of-Coordinates Matrix](./1910-changing-a-basis-using-the-change-of-coordinates-matrix.md)

## Lesson

### Introduction

A square matrix $A$ is called **diagonalizable** if there exists a diagonal matrix $D$ and an invertible matrix $P$ such that

$$


A = PDP^{-1}.


$$

So, to **diagonalize** a matrix $A,$ we need to find a diagonal matrix $D$ and an invertible matrix $P$ that satisfy the equation above.

For example, let's diagonalize the matrix $A,$ given by

$$


[\begin{aligned}0 & −6 \\ 1 & 5\end{aligned}]


$$

To diagonalize a $2\times 2$ matrix, we follow a three-step **diagonalization algorithm.**

**Step 1:** Find the eigenvalues of the matrix.

We solve the characteristic equation $\vert A - \lambda I \vert = 0.$ For the given matrix, the eigenvalues are $\color{red}\lambda_1 =2$ and $\color{blue}\lambda_2 =3.$

**Step 2:** Find a basis of $\mathbb{R}^2$ consisting of eigenvectors of the matrix.

Following the usual method for computing eigenvectors, we get

$$


[\begin{aligned}3 \\ −1\end{aligned}]


$$

corresponding to the eigenvalues $\color{red}\lambda_1 =2$ and $\color{blue}\lambda_2 =3,$ respectively.

Note that $\left\{{\color{red}\mathbf{v_1}}, {\color{blue}\mathbf{v_2}}\right\}$ is a basis of $\mathbb{R}^2$ since eigenvectors corresponding to distinct eigenvalues are linearly independent. This becomes important later.

**Step 3:** Construct the matrices $D$ and $P.$

Now that we have our eigenvalues and corresponding eigenvectors, we can construct the diagonal matrix $D$ and invertible matrix $P.$

The matrix $D$ has the eigenvalues of the matrix as its entries on the diagonal. For now, we can write them in any order. So, we let

$$


[\begin{aligned}2 & 0 \\ 0 & 3\end{aligned}]


$$

Then, the columns of $P$ are the corresponding eigenvectors. We need to write each eigenvector in the *same* column as its respective eigenvalue in the matrix $D.$ So, we get

$$


[\begin{aligned}3 & −2 \\ −1 & 1\end{aligned}]


$$

Finally, we obtain

$$


\begin{aligned}𝐴=𝑃𝐷𝑃^{−1} & =[\begin{matrix}3 & −2 \\ −1 & 1\end{matrix}][\begin{matrix}2 & 0 \\ 0 & 3\end{matrix}][\begin{matrix}3 & −2 \\ −1 & 1\end{matrix}]^{−1}.\end{aligned}


$$

We can check our solution by computing the product on the right-hand side:

$$


\begin{aligned}[\begin{matrix}3 & −2 \\ −1 & 1\end{matrix}][\begin{matrix}2 & 0 \\ 0 & 3\end{matrix}][\begin{matrix}3 & −2 \\ −1 & 1\end{matrix}]^{−1} & =[\begin{matrix}6 & −6 \\ −2 & 3\end{matrix}][\begin{matrix}1 & 2 \\ 1 & 3\end{matrix}] \\ & =[\begin{matrix}0 & −6 \\ 1 & 5\end{matrix}] \\ & =𝐴\,✓\end{aligned}


$$

### Example: Diagonalizing a 2x2 Matrix Given Its Eigenvalues

#### Question

Consider the matrix $[\begin{aligned}3 & 0 \\ −5 & 4\end{aligned}]$ You're given that $\lambda_1=4$ and $\lambda_2=3$ are the eigenvalues of $A,$ and $[\begin{aligned}0 \\ 1\end{aligned}]$ $[\begin{aligned}1 \\ 5\end{aligned}]$ are the respective eigenvectors. Find the matrices $P$ and $D$ such that $PDP^{-1} = A,$ where $D$ is a diagonal matrix.

#### Explanation

Since the eigenvalues of the matrix are $\lambda_1={\color{blue}4}$ and $\lambda_2={\color{red}3},$ we construct the diagonal matrix $D$ by writing the eigenvalues in the main diagonal:

$$


[\begin{aligned}4 & 0 \\ 0 & 3\end{aligned}]


$$

Now, to construct the matrix $P,$ we simply write the respective eigenvectors as columns:

- the $1$st column is the eigenvector corresponding to $\lambda_1={\color{blue}4},$ and

- the $2$nd column is the eigenvector corresponding to $\lambda_2={\color{red}3}.$

Therefore, we get

$$


[\begin{aligned}0 & 1 \\ 1 & 5\end{aligned}]


$$

### Diagonalizable vs. Non-Diagonalizable Matrices

There is a theorem that states the following:

*If $A$ is a $2 \times 2$ matrix, then it is diagonalizable if and only if there exists a basis of $\mathbb{R}^2$ that consists of eigenvectors of $A.$*

We can break this down into two possible cases:

- If $A$ has two distinct eigenvalues, then it is indeed diagonalizable. This is because two distinct eigenvalues will give rise to two linearly independent eigenvectors (one for each eigenvalue). So, for a matrix $A$ with eigenvalues $\color{red}\lambda_1$ and $\color{blue}\lambda_2$ and corresponding eigenvectors $\color{red}\mathbf{v_1}$ and $\color{blue}\mathbf{v_2},$ we have

- If we get a double root $\lambda$ of the characteristic equation, the matrix will be diagonalizable *only if* we can find exactly two linearly independent eigenvectors corresponding to $\lambda,$ which may or may not be possible. Another way of saying this is that the corresponding eigenspace $V_\lambda$ must be of dimension $2.$

### Example: Identifying Whether a Given 2x2 Matrix Is Diagonalizable

#### Question

Determine if the matrix $[\begin{aligned}3 & −5 \\ 0 & 3\end{aligned}]$ is diagonalizable or not, and if it is diagonalizable, find a corresponding diagonal matrix $D.$

#### Explanation

Since $A$ is triangular, the eigenvalues are the entries on the main diagonal.

So, the eigenvalues are $\lambda_1=\lambda_2=3.$ Since we get one repeated eigenvalue, the matrix might not be diagonalizable. To check this, we row-reduce the matrix $A-3I\mathbin{:}$

$$


\begin{aligned}𝐴−3𝐼 & =[\begin{matrix}3 & −5 \\ 0 & 3\end{matrix}]−3[\begin{matrix}1 & 0 \\ 0 & 1\end{matrix}] \\ & =[\begin{matrix}0 & −5 \\ 0 & 0\end{matrix}].\end{aligned}


$$

The reduced matrix above has only $1$ pivot column. This implies that we will have only $2-1=1$ linearly independent eigenvector corresponding to the current eigenvalue. Therefore, $A$ is not diagonalizable.

### The Connection Between a Matrix and Its Diagonal Form

If $A$ is a diagonalizable matrix, then we can write

$$


A=PDP^{-1}.


$$

We can write this equation in an equivalent form, making $D$ the subject.

First, we left-multiply both sides of the equation by $P^{-1}\mathbin{:}$

$$


\begin{aligned}𝐴 & =𝑃𝐷𝑃^{−1} \\ 𝑃^{−1}⋅𝐴 & =𝑃^{−1}⋅𝑃𝐷𝑃^{−1} \\ 𝑃^{−1}𝐴 & =𝐼_{2}𝐷𝑃^{−1} \\ 𝑃^{−1}𝐴 & =𝐷𝑃^{−1}\end{aligned}


$$

Then, we right-multiply both sides of the equation by $P{:}$

$$


\begin{aligned}𝑃^{−1}𝐴⋅𝑃 & =𝐷𝑃^{−1}⋅𝑃 \\ 𝑃^{−1}𝐴𝑃 & =𝐷𝐼_{2} \\ 𝑃^{−1}𝐴𝑃 & =𝐷\end{aligned}


$$

Therefore,

$$


A=PDP^{-1} \qquad\Longleftrightarrow\qquad D = P^{-1}A P.


$$

### Example: Diagonalizing a 2x2 Matrix Given Part of the Diagonalization

#### Question

Consider the following matrices:

$$


[\begin{aligned}1 & 4 \\ 2 & 3\end{aligned}]


$$

Given that $D=P^{-1}AP,$ find the value of $\dfrac{a}{b}.$

#### Explanation

From the diagonal matrix $[\begin{aligned}5 & 0 \\ 0 & −1\end{aligned}]$ we deduce that the eigenvalues of $A$ are $\lambda_1=5$ and $\lambda_2=-1.$

So, the second column of $P$ corresponds to the eigenvalue $\lambda_2=-1.$

Now, we simply need to find an eigenvector that corresponds to $\lambda_2=-1.$ Computing $A-(-1)I,$ we get

$$


\begin{aligned}𝐴−(−1)𝐼 & =[\begin{matrix}1 & 4 \\ 2 & 3\end{matrix}]+[\begin{matrix}1 & 0 \\ 0 & 1\end{matrix}] \\ & =[\begin{matrix}2 & 4 \\ 2 & 4\end{matrix}].\end{aligned}


$$

To solve the corresponding system of linear equations, we construct the augmented matrix $M$ and reduce it to its row echelon form using Gaussian elimination:

$$


\begin{aligned}𝑀 & =[\begin{matrix}2 & 4 & 0 \\ 2 & 4 & 0\end{matrix}] & 𝑅_{2}=𝑅_{2}+(−1)𝑅_{1} \\ & ∼[\begin{matrix}2 & 4 & 0 \\ 0 & 0 & 0\end{matrix}] & \end{aligned}


$$

The reduced matrix above has one pivot column (the $1$st one). So, $x_2$ is a free variable. From the first equation, we obtain $x_1= -{2}x_2.$ Therefore, the general solution is

$$


[\begin{aligned}−2𝑥_{2} \\ 𝑥_{2}\end{aligned}]


$$

By setting $x_2=1,$ we get the eigenvector

$$


[\begin{aligned}𝑎 \\ 𝑏\end{aligned}]


$$

Finally, $\dfrac{a}{b}=\dfrac{-2}{1} = -2.$

### Example: Diagonalizing a 2x2 Matrix

#### Question

Given the matrix $[\begin{aligned}3 & −8 \\ 0 & −2\end{aligned}]$ find a diagonal matrix $D$ and an invertible matrix $P$ such that $D=P^{-1}AP.$

#### Explanation

We apply the diagonalization algorithm.

**** We need to find the eigenvalues of the matrix. Since matrix $A$ is triangular, its eigenvalues are the entries on the main diagonal:

$$


\lambda_1=3, \quad\quad\lambda_2=-2.


$$

**** Now, we need to find an eigenvector basis of $A.$

- For $\lambda_1=3,$ we have To solve the corresponding system of linear equations, we construct the augmented matrix $M$ and reduce it to its row echelon form using Gaussian elimination: The reduced matrix above has one pivot column (the $2$nd one). So, $x_1$ is a free variable. From the first equation, we obtain $x_2=0.$ Therefore, the general solution is Setting $x_1=1,$ we get the eigenvector $[\begin{aligned}1 \\ 0\end{aligned}]$

- For $\lambda_2=-2,$ we have The above matrix corresponds to a homogeneous system of linear equations. Note, the matrix is already in row echelon form. There is one pivot column (the $1$st one). So, $x_2$ is a free variable. From the first equation, we obtain $x_1=\dfrac{8}{5}x_2.$ Therefore, the general solution is Setting $x_2=5,$ we get the eigenvector $[\begin{aligned}8 \\ 5\end{aligned}]$

**** We construct the diagonal matrix $D$ and the invertible matrix $P$ as follows:

$$


[\begin{aligned}3 & 0 \\ 0 & −2\end{aligned}]


$$

### Uniqueness of the Diagonalization

Given a matrix $A,$ the diagonalization

$$


\begin{aligned}| & | \\ 𝐯_{𝟏} & 𝐯_{𝟐} \\ | & |\end{aligned}


$$

is almost unique, but not quite.

When we construct the diagonal matrix $D,$ we can put the eigenvalues in any order. So this matrix is unique up to permutations of the order of the eigenvalues. Note that by swapping the eigenvalues in $D,$ we then have to swap the corresponding eigenvectors (columns) in $P{:}$

$$


\begin{aligned}| & | \\ 𝐯_{𝟐} & 𝐯_{𝟏} \\ | & |\end{aligned}


$$

Also, since any non-zero multiple of an eigenvector is an eigenvector as well, the eigenvector basis of $\mathbb{R}^2$ can consist of these multiples instead. So the invertible matrix $P$ is unique up to multiples of its columns.

### Diagonalization as a Change of Coordinates

Let be a diagonalizable matrix. Then we can write where

- is an invertible matrix whose columns are eigenvectors and of and

- is a diagonal matrix whose diagonal entries are the corresponding eigenvalues and

To understand this better, we need to distinguish between two coordinate systems.

In the **standard basis** is

So, if a vector is written as then The numbers and are the *standard coordinates* of

Now let

Since the columns of are and written in standard coordinates, the matrix converts coordinates from the basis to the standard basis.

So, for any vector

Here, denotes the standard-coordinate column of the vector, while denotes the coordinate column of the same vector in the eigenvector basis

Also, in the basis the eigenvectors have especially simple coordinate columns:

This is because

So, in the basis the matrix acts by scaling the first coordinate by and the second coordinate by

We can summarize this process for any vector as a sequence of three steps:

- first, rewrite in the eigenvector basis

- then, apply the diagonal matrix in that basis,

- finally, convert the result back to standard coordinates.

The diagram below shows this sequence.
