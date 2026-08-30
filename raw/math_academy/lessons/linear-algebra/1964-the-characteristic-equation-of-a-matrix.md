# The Characteristic Equation of a Matrix

Source: https://www.mathacademy.com/topics/1964?courseId=55
Topic ID: 1964

## Prerequisites

- [The Rational Roots Theorem](../algebra-ii/757-the-rational-roots-theorem.md)
- [Calculating the Eigenvalues of a 2x2 Matrix](./990-calculating-the-eigenvalues-of-a-2x2-matrix.md)
- [Basic Properties of Determinants](./1771-basic-properties-of-determinants.md)

## Lesson

### Introduction

We can find the eigenvalues of a $3\times 3$ matrix in much the same way as for $2\!\times\! 2$ matrices.

Remember, $\lambda$ is an eigenvalue of $A$ if $A\mathbf{v} = \lambda\mathbf{v}$ for some non-zero vector $\mathbf{v}$. This implies that the equation

$$


(A-\lambda I)\mathbf{v}=\mathbf{0}


$$

has a non-trivial solution, which means that the matrix $A-\lambda I$ is singular, and consequently $\textrm{det}(A-\lambda I)=0.$ Therefore, if we want to find the eigenvalues of a $n\!\times\! n$ matrix $A,$ we have to find the solutions of the characteristic equation

$$


\textrm{det}(A-\lambda I)=0.


$$

Let's go through this process in the case of the matrix $A,$ given by

$$


\begin{aligned}−2 & 0 & 0 \\ 0 & −8 & 0 \\ 0 & 0 & 5\end{aligned}


$$

First, we write down the matrix $A-\lambda I{:}$

$$


\begin{aligned}𝐴−𝜆𝐼 & =\begin{aligned}−2 & 0 & 0 \\ 0 & −8 & 0 \\ 0 & 0 & 5\end{aligned}−\begin{aligned}𝜆 & 0 & 0 \\ 0 & 𝜆 & 0 \\ 0 & 0 & 𝜆\end{aligned} \\ & =\begin{aligned}−2−𝜆 & 0 & 0 \\ 0 & −8−𝜆 & 0 \\ 0 & 0 & 5−𝜆\end{aligned}\end{aligned}


$$

Now, we set and solve the characteristic equation $\,\textrm{det}(A-\lambda I)=0.$ Using the fact that the determinant of a triangular (or diagonal) matrix is given by the product of the elements on the main diagonal, we get the following:

$$


\begin{aligned}det(𝐴−𝜆𝐼) & =0 \\ \begin{aligned}−2−𝜆 & 0 & 0 \\ 0 & −8−𝜆 & 0 \\ 0 & 0 & 5−𝜆\end{aligned} & =0 \\ (−2−𝜆)(−8−𝜆)(5−𝜆) & =0 \\ (𝜆+2)(𝜆+8)(𝜆−5) & =0\end{aligned}


$$

So, the eigenvalues of the matrix $A$ are $\lambda=-2,$ $\lambda=-8,$ and $\lambda=5.$

### Example: Calculating the Eigenvalues of a 3x3 Matrix Containing a Block of Zeros

#### Question

Determine all real eigenvalues $\lambda$ of the matrix $\begin{aligned}−9 & 4 & 8 \\ 0 & 9 & −7 \\ 0 & 0 & 6\end{aligned}$

#### Explanation

First, we find the matrix $\, A-\lambda I \mathbin{:}$

$$


\begin{aligned}−9−𝜆 & 4 & 8 \\ 0 & 9−𝜆 & −7 \\ 0 & 0 & 6−𝜆\end{aligned}


$$

The characteristic equation is $\det(A-\lambda I) = 0.$

Since the determinant of a triangular (or diagonal) matrix is given by the product of the entries on the main diagonal, we obtain the following:

$$


\begin{aligned}det(𝐴−𝜆𝐼) & =0 \\ \begin{aligned}−9−𝜆 & 4 & 8 \\ 0 & 9−𝜆 & −7 \\ 0 & 0 & 6−𝜆\end{aligned} & =0 \\ (−9−𝜆)(9−𝜆)(6−𝜆) & =0 \\ (𝜆+9)(𝜆−9)(𝜆−6) & =0\end{aligned}


$$

Therefore, the eigenvalues are $\lambda_1=-9,$ $\lambda_2=9,$ and $\lambda_3=6.$

**** The eigenvalues of a triangular (or diagonal) matrix are always the entries on the main diagonal.

### The Algebraic Multiplicity of an Eigenvalue

The **algebraic multiplicity** of an eigenvalue $\lambda$ is the number of times it is a solution of the characteristic equation.

For example, consider a $6\times 6$ matrix $A$ with the following characteristic equation:

$$


(\lambda-{\color{red}4})(\lambda-{\color{red}4})(\lambda-1)(\lambda+8)^{\color{blue}3} =0


$$

The eigenvalue $\lambda={\color{red}4}$ is a double root. Therefore, it has algebraic multiplicity $2.$

By the same reasoning, we say that

- $\lambda=1$ has algebraic multiplicity $1,$ and

- $\lambda=-8$ has algebraic multiplicity $\color{blue}3$.

### Example: Calculating the Eigenvalues of a 4x4 Matrix Containing a Block of Zeros

#### Question

$$


\begin{aligned}3 & 0 & −8 & −2 \\ 0 & −1 & 3 & 5 \\ 0 & 0 & 4 & 0 \\ 0 & 7 & −3 & 1\end{aligned}


$$

Consider the matrix $P$ given above. Which of the following statements are true?

1. $\lambda=4$ is an eigenvalue of $P$

2. $\lambda=-1$ is an eigenvalue of $P$

3. The eigenvalue $\lambda=6$ has algebraic multiplicity $2$

#### Explanation

First, we find the matrix $\, P-\lambda I \mathbin{:}$

$$


\begin{aligned}3−𝜆 & 0 & −8 & −2 \\ 0 & −1−𝜆 & 3 & 5 \\ 0 & 0 & 4−𝜆 & 0 \\ 0 & 7 & −3 & 1−𝜆\end{aligned}


$$

The characteristic equation is $\det(P-\lambda I) = 0.$

Notice that we can expand the $4 \times 4$ determinant across the $1$st column, as follows:

$$


\begin{aligned}det(𝑃−𝜆𝐼) & =0 \\ \begin{aligned}3−𝜆 & 0 & −8 & −2 \\ 0 & −1−𝜆 & 3 & 5 \\ 0 & 0 & 4−𝜆 & 0 \\ 0 & 7 & −3 & 1−𝜆\end{aligned} & =0 \\ (3−𝜆)\begin{aligned}−1−𝜆 & 3 & 5 \\ 0 & 4−𝜆 & 0 \\ 7 & −3 & 1−𝜆\end{aligned} & =0\end{aligned}


$$

Now, expanding the $3 \times 3$ determinant across the $2$nd row, we obtain the following:

$$


\begin{aligned}(3−𝜆)⋅(4−𝜆)\begin{aligned}−1−𝜆 & 5 \\ 7 & 1−𝜆\end{aligned} & =0 \\ (3−𝜆)(4−𝜆)((−1−𝜆)(1−𝜆)−35) & =0 \\ (3−𝜆)(4−𝜆)(𝜆^{2}−36) & =0 \\ (𝜆−3)(𝜆−4)(𝜆−6)(𝜆+6) & =0\end{aligned}


$$

So, the eigenvalues of $P$ are $\lambda=3,$ $\lambda=4,$ $\lambda=6,$ and $\lambda=-6$ (all with algebraic multiplicity $1$).

Therefore, the correct answer is "I only."

### Example: Finding the Eigenvalues of a General 3x3 Matrix

#### Question

Determine all real eigenvalues of the matrix

#### Explanation

First, we find the matrix

The characteristic equation is given by

Expanding the determinant across the st row, we get the following:

Now, we need to solve this equation. We find the first root by testing some values. According to the rational zeros theorem, a list of good first guesses consists of all divisors of

Let's pick Substituting to the characteristic equation gives So, is a root of the equation. This means we can factor out of using synthetic division:

So, we obtain the following factorization:

Therefore, the eigenvalues are and
