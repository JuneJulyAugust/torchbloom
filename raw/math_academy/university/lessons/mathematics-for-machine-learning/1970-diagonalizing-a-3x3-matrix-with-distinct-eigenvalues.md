# Diagonalizing a 3x3 Matrix With Distinct Eigenvalues

Source: https://www.mathacademy.com/topics/1970?courseId=145
Topic ID: 1970

## Prerequisites

- [Diagonalizing a 2x2 Matrix](./1968-diagonalizing-a-2x2-matrix.md)
- [Calculating the Eigenvectors of a 3x3 Matrix With Distinct Eigenvalues](./1977-calculating-the-eigenvectors-of-a-3x3-matrix-with-distinct-eigenvalues.md)

## Lesson

### Introduction

An $n\times n$ matrix $A$ is said to be diagonalizable if there exists a diagonal matrix $D$ and an invertible matrix $P$ such that

$$


A=PDP^{-1}.


$$

For example, the matrix $[\begin{aligned}3 & −4 \\ 2 & −3\end{aligned}]$ is diagonalizable because

$$


[\begin{aligned}3 & −4 \\ 2 & −3\end{aligned}]


$$

In general, we have the following theorem:

*An $n\times n$ matrix $A$ is diagonalizable if and only if there exists a basis of $\mathbb{R}^n$ that consists of eigenvectors of $A$.*

Since eigenvectors corresponding to different eigenvalues are linearly independent, we can also conclude the following fact:

*If an $n\times n$ matrix $A$ has $n$*distinct*eigenvalues (that is, $n$ simple roots of the corresponding characteristic equation), then there exists a basis of eigenvectors. Thus, the matrix is diagonalizable.*

Let's show you how to use the diagonalization theorem with an example.

Suppose that $\lambda_1={\color{blue}-2},$ $\lambda_2={\color{red}1},$ $\lambda_3=-3$ are eigenvalues of a $3\times 3$ matrix $A$, and that

$$


\begin{aligned}−3 \\ 0 \\ −1\end{aligned}


$$

are the respective eigenvectors. To find an invertible matrix $P$ and a diagonal matrix $D$ such that $PDP^{-1} = A,$ we do the following:.

First, we construct the diagonal matrix $D$ by writing the eigenvalues in the main diagonal:

$$


\begin{aligned}−2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & −3\end{aligned}


$$

Now, to construct the matrix $P,$ we simply write the respective eigenvectors as columns:

- the $1$st column is the eigenvector corresponding to $\lambda_1={\color{blue}-2},$

- the $2$nd column is the eigenvector corresponding to $\lambda_2={\color{red}1},$ and

- the $3$rd column is the eigenvector corresponding to $\lambda_3=-3.$

Therefore, we get

$$


\begin{aligned}−3 & 1 & 1 \\ 0 & 1 & 0 \\ −1 & 0 & 2\end{aligned}


$$

**Note:** If the matrix $A$ does not have $n$ distinct eigenvalues, it is not always possible to diagonalize it. However, the algorithm to diagonalize any diagonalizable $n\!\times\! n$ matrix is the same as the $3\!\times\! 3$ case!

### Example: Diagonalizing a Matrix Given Its Eigenvalues and Corresponding Eigenvectors

#### Question

Consider the matrix $A$ for which $\lambda_1=-1,$ $\lambda_2=1,$ $\lambda_3=0$ are eigenvalues, and

$$


\begin{aligned}1 \\ 0 \\ 0\end{aligned}


$$

are the respective eigenvectors. What are the values of $a,b,c$ given that

$$


\begin{aligned}1 & 1 & 0 \\ 0 & 𝑏 & 0 \\ 𝑎 & 0 & 1\end{aligned}


$$

#### Explanation

Since the eigenvalues of the matrix are $\lambda_1={\color{blue}-1},$ $\lambda_2={\color{red}1},$ $\lambda_3=0,$ we construct the diagonal matrix $D$ by writing the eigenvalues in the main diagonal:

$$


\begin{aligned}−1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0\end{aligned}


$$

Now, to construct the matrix $P,$ we simply write the respective eigenvectors as columns:

- the $1$st column is the eigenvector corresponding to $\lambda_1={\color{blue}-1},$

- the $2$nd column is the eigenvector corresponding to $\lambda_2={\color{red}1},$ and

- the $3$rd column is the eigenvector corresponding to $\lambda_3=0.$

Therefore, we get

$$


\begin{aligned}1 & 1 & 0 \\ 0 & −1 & 0 \\ 0 & 0 & 1\end{aligned}


$$

Finally, we obtain

$$


\begin{aligned}1 & 1 & 0 \\ 0 & −1 & 0 \\ 0 & 0 & 1\end{aligned}


$$

In conclusion, we get $a=0,$ $b=-1,$ and $c=-1.$

### Example: Identifying Whether a Given Matrix Is Diagonalizable Over the Real Numbers

#### Question

Consider the matrix $A,$ given by

$$


\begin{aligned}2 & 6 & 0 \\ 2 & 1 & 0 \\ 1 & −4 & 4\end{aligned}


$$

Determine whether $A=PDP^{-1}$ for some invertible matrix $P$ and a diagonal matrix $D,$ where $P$ and $D$ are both real. In the affirmative case, find a possible diagonal matrix $D.$

#### Explanation

First, we need to determine whether $D$ is diagonalizable over $\mathbb R.$

We start by computing the eigenvalues of $A.$ To do that, we solve the characteristic equation, as follows:

$$


\begin{aligned}det(𝐴−𝜆𝐼) & =0 \\ \begin{matrix}2−𝜆 & 6 & 0 \\ 2 & 1−𝜆 & 0 \\ 1 & −4 & 4−𝜆\end{matrix} & =0 \\ (4−𝜆)\begin{matrix}2−𝜆 & 6 \\ 2 & 1−𝜆\end{matrix} & =0 \\ (4−𝜆)([𝜆^{2}−3𝜆+2]−12) & =0 \\ (4−𝜆)(𝜆^{2}−3𝜆−10) & =0 \\ (4−𝜆)(𝜆−5)(𝜆+2) & =0\end{aligned}


$$

Therefore, the eigenvalues of $A$ are $\lambda_1=4,$ $\lambda_2=5,$ and $\lambda_3=-2.$ Since all of the eigenvalues are simple roots of the characteristic polynomial, $A$ is diagonalizable.

We construct a diagonal matrix $D$ by writing the eigenvalues in the main diagonal. Therefore, one possible matrix $D$ is

$$


\begin{aligned}4 & 0 & 0 \\ 0 & 5 & 0 \\ 0 & 0 & −2\end{aligned}


$$

Note that the diagonal matrix $D$ is unique up to the ordering of the eigenvalues. Therefore, another possible diagonal matrix is

$$


\begin{aligned}5 & 0 & 0 \\ 0 & 4 & 0 \\ 0 & 0 & −2\end{aligned}


$$

### Example: Diagonalizing a Matrix Given Part of the Diagonalization

#### Question

Consider the following matrices:

$$


\begin{aligned}−8 & −4 & 6 \\ −9 & −7 & 9 \\ −16 & −10 & 14\end{aligned}


$$

Given that $D=P^{-1}AP,$ find the first column of the matrix $P.$

#### Explanation

From the diagonal matrix $D$, we deduce that the eigenvalues of $A$ are

$\qquad$ $\lambda_1=-2, \quad$ $\lambda_2=-1, \quad$ $\lambda_3=2.$

So, the first column of $P$ corresponds to the eigenvalue $\lambda_1=-2.$

Now, we need to find an eigenvector that corresponds to $\lambda_1=-2.$ Computing $A-(-2)I,$ we get

$$


\begin{aligned}𝐴−𝜆_{1}𝐼 & =\begin{matrix}−8 & −4 & 6 \\ −9 & −7 & 9 \\ −16 & −10 & 14\end{matrix}−(−2)\begin{matrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{matrix} \\ & =\begin{matrix}−6 & −4 & 6 \\ −9 & −5 & 9 \\ −16 & −10 & 16\end{matrix}.\end{aligned}


$$

So, we have a system of linear equations with the augmented matrix $M$ that we reduce to row echelon form using Gaussian elimination, as follows:

$$


\begin{aligned}𝑀 & =\begin{matrix}−6 & −4 & 6 & 0 \\ −9 & −5 & 9 & 0 \\ −16 & −10 & 16 & 0\end{matrix} & & \begin{matrix}𝑅_{2}:=𝑅_{2}+(−\frac{3}{2})𝑅_{1} \\ 𝑅_{3}:=𝑅_{3}+(−\frac{8}{3})𝑅_{1}\end{matrix} \\ & ∼\begin{matrix}−6 & −4 & 6 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & \frac{2}{3} & 0 & 0\end{matrix} & & \begin{matrix}𝑅_{3}:=𝑅_{3}+(−\frac{2}{3})𝑅_{2}\end{matrix} \\ & ∼\begin{matrix}−6 & −4 & 6 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0\end{matrix}. & & \end{aligned}


$$

The reduced matrix above has two pivot columns ($1$st and $2$nd). Thus, $x_3$ is a free variable. From the second equation, we obtain $x_2=0.$ Substituting this into the first equation, we get $x_1=x_3.$ Hence, the general solution is

$$


\begin{aligned}𝑥_{3} \\ 0 \\ 𝑥_{3}\end{aligned}


$$

Therefore, setting $x_3=1,$ we get the eigenvector

$$


\begin{aligned}1 \\ 0 \\ 1\end{aligned}


$$

Finally, $\begin{aligned}1 & 0 & 1 \\ 0 & 3 & 2 \\ 1 & 2 & 3\end{aligned}$

### Example: Diagonalizing a Matrix

#### Question

$$


\begin{aligned}0 & −2 & 0 \\ 0 & 2 & 0 \\ 1 & 0 & 1\end{aligned}


$$

The matrix $A$ has eigenvalues $\lambda_1=2,$ $\lambda_2=1,$ and $\lambda_3=0.$ Find a diagonal matrix $D$ and an invertible matrix $P$ such that $D=P^{-1}AP.$

#### Explanation

We apply the diagonalization algorithm.

**** Notice that we are already given the eigenvalues of the matrix:

$\qquad$ $\lambda_1=2,\quad$ $\lambda_2=1, \quad$ $\lambda_3=0.$

**** Now, we need to find an eigenvector basis of $A.$ Applying our usual method, we get the following.

- For $\lambda_1=2,$ we get Seeking a non-zero solution of $(A-2I)\mathbf{x}=\mathbf{0}$ gives us the eigenvector $\begin{aligned}1 \\ −1 \\ 1\end{aligned}$

- For $\lambda_2=1,$ we get Seeking a non-zero solution of $(A-I)\mathbf{x}=\mathbf{0}$ gives us the eigenvector $\begin{aligned}0 \\ 0 \\ 1\end{aligned}$

- For $\lambda_3=0,$ we get Seeking a non-zero solution of $(A-0I)\mathbf{x}=\mathbf{0}$ gives us the eigenvector $\begin{aligned}1 \\ 0 \\ −1\end{aligned}$

**** We construct the diagonal matrix $D$ and the invertible matrix $P$ in the usual way, and this gives us the following:

$$


\begin{aligned}2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0\end{aligned}


$$
