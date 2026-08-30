# The Invertible Matrix Theorem in Terms of Eigenvalues

Source: https://www.mathacademy.com/topics/1966?courseId=154
Topic ID: 1966

## Prerequisites

- [The Characteristic Equation of a Matrix](./1964-the-characteristic-equation-of-a-matrix.md)

## Lesson

### Introduction

The **invertible matrix theorem in terms of eigenvalues** states the following:

*An $n \times n$ matrix $A$ is invertible if and only if $0$ is not an eigenvalue of $A.$*

As a result, $\lambda=0$ should not be a solution to the corresponding characteristic equation.

For example, if we are given that

$$


\lambda^3-\lambda^2-2\lambda=0


$$

is the characteristic equation of a $3 \times 3$ matrix $A,$ then $A$ must be singular (not invertible) since $\lambda=0$ is a root of the equation.

### Example: Identifying True Statements Using the Invertible Matrix Theorem in Terms of Eigenvalues

#### Question

If $A$ is a $3 \times 3$ invertible matrix, then which of the following could be the characteristic equation of $A?$

1. $(\lambda-2)^2(\lambda-3)=0$

2. $\lambda^3-2\lambda^2+3\lambda=0$

3. $\lambda^3-4\lambda + 7=0$

#### Explanation

According to the invertible matrix theorem, if $A$ is invertible, then $0$ can't be an eigenvalue of $A.$ As a result, $\lambda=0$ should not be a solution to the corresponding characteristic equation.

With that in mind, let's examine the given equations in turn.

- Equation I could be the characteristic equation of $A.$ Indeed, $\lambda=0$ is not a root of the equation.

- Equation II **** be the characteristic equation of $A$ since $\lambda=0$ is a root of the equation.

- Equation III could be the characteristic equation of $A.$ Indeed, $\lambda=0$ is not a root of the equation.

Therefore, the correct answer is "I and III only."

### Example: Identifying True Statements Using the Invertible Matrix Theorem

#### Question

If $A$ is a $3 \times 3$ matrix and $\lambda=7$ is an eigenvalue of $A,$ which of the following statements are true?

1. $(A-7I)\mathbf{x} = \mathbf{0}$ has a nonzero solution

2. $\textrm{rank}(A-7I) = 3$

3. $\textrm{Null}(A-7I) \ne\{\mathbf{0}\}$

#### Explanation

Given a $3 \times 3$ matrix $M,$ we have the following by the invertible matrix theorem:

$M$ is invertible $\begin{aligned} & Col(𝑀)=ℝ^{3} \\ & dim(Col(𝑀))=3=rank(𝑀) \\ & Null(𝑀)={𝟎} \\ & dim(Null(𝑀))=0=nullity(𝑀)\end{aligned}$

Let's now apply the theorem to the matrix $M = A- 7I.$

- Statement I is true. Notice that if $\lambda=7$ is an eigenvalue of $A,$ then the nonzero solutions of $(A-7I)\mathbf{x} = \mathbf{0}$ are eigenvectors of $A,$ which are nonzero by definition. As a result, the matrix $M=A-7 I$ must be singular.

- Statement II is false. Since $M=A-7I$ is singular, by the invertible matrix theorem, we obtain that

- Statement III is true. Since $M=A-7I$ is singular, by the invertible matrix theorem, we obtain that

Therefore, the correct answer is "I and III only."

### Example: Identifying True Statements Using the Invertible Matrix and Rank-Nullity Theorems

#### Question

If $B$ is a $4 \times 4$ matrix and $\textrm{rank}(B+4I) = 3,$ which of the following statements are true?

1. $\textrm{Null}(B+4I) = \{\mathbf{0} \}$

2. $B +4I$ is singular

3. $\lambda = -4$ is an eigenvalue of $B$

#### Explanation

Given a $4 \times 4$ matrix $M,$ we have the following by the invertible matrix theorem:

$M$ is invertible $\begin{aligned} & Col(𝑀)=ℝ^{4} \\ & dim(Col(𝑀))=4=rank(𝑀) \\ & Null(𝑀)={𝟎} \\ & dim(Null(𝑀))=0=nullity(𝑀)\end{aligned}$

Also, according to the rank-nullity theorem, if $M$ has $4$ columns, then

$$


\textrm{rank}(M) + \textrm{nullity}(M) = 4.


$$

With that in mind, let's examine our statements in turn.

- Statement I is false. According to the rank-nullity theorem, As a result, $\textrm{Null}(B+4I) \ne \{\mathbf{0} \}.$

- Statements II is true. By the invertible matrix theorem, since $\textrm{nullity}(B+4I) \neq 0,$ we obtain that $B +4I$ must be singular.

- Statement III is true. Notice that if $M=B +4 I$ is singular, then $(B +4 I)\mathbf{x} = \mathbf{0}$ has nonzero solutions which will be eigenvectors of $B.$ As a result, $\lambda=-4$ is an eigenvalue of $B.$

Therefore, the correct answer is "II and III only."
