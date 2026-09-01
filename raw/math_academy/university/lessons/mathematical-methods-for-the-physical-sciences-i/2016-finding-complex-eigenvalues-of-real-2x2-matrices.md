# Finding Complex Eigenvalues of Real 2x2 Matrices

Source: https://www.mathacademy.com/topics/2016?courseId=154
Topic ID: 2016

## Prerequisites

- [Calculating the Eigenvectors of a 2x2 Matrix](./991-calculating-the-eigenvectors-of-a-2x2-matrix.md)
- [Matrices Over the Complex Numbers](./2015-matrices-over-the-complex-numbers.md)

## Lesson

### Introduction

Let's compute the eigenvalues of the following matrix:

$$


[\begin{aligned}1 & −1 \\ 2 & −1\end{aligned}]


$$

The characteristic equation of $A$ is

$$


\lambda^2 +1 = 0.


$$

The eigenvalues are the roots of the characteristic equation. However, the discriminant of this equation is

$$


\mathcal{D}=-4<0,


$$

so $A$ doesn't have any real eigenvalues!

Nonetheless, we can still compute the eigenvalues of $A.$ The difference here is that they will be complex numbers. Let's solve the characteristic equation using the square root method:

$$


\begin{aligned}𝜆^{2}+1=0 \\ 𝜆^{2}=−1 \\ 𝜆=±i\end{aligned}


$$

Therefore, we conclude that the eigenvalues of $A$ are $\lambda = \pm\text{i}.$

### Example: Computing the Complex Eigenvalues of a Matrix

#### Question

Compute the eigenvalues of the matrix $[\begin{aligned}1 & −2 \\ 2 & 1\end{aligned}]$

#### Explanation

First, we find the matrix $\, A-\lambda I \mathbin{:}$

$$


[\begin{aligned}1−𝜆 & −2 \\ 2 & 1−𝜆\end{aligned}]


$$

Then, we compute the characteristic equation, as follows:

$$


\begin{aligned}det(𝐴−𝜆𝐼) & =0 \\ \begin{matrix}1−𝜆 & −2 \\ 2 & 1−𝜆\end{matrix} & =0 \\ (1−𝜆)(1−𝜆)−2(−2) & =0 \\ 1−2𝜆+𝜆^{2}+4 & =0 \\ 𝜆^{2}−2𝜆+5 & =0\end{aligned}


$$

Using the quadratic formula, we get

$$


\begin{aligned}𝜆 & =\frac{−𝑏±\sqrt{𝑏^{2}−4𝑎𝑐}}{2𝑎} \\ & =\frac{−(−2)±\sqrt{(−2)^{2}−4(1)(5)}}{2(1)} \\ & =\frac{2±\sqrt{−16}}{2} \\ & =\frac{2±4i}{2} \\ & =1±2i.\end{aligned}


$$

Therefore, the eigenvalues are $\lambda=1\pm 2\text{i}.$

### Complex Eigenvalues and Eigenvectors Come in Conjugate Pairs

You may have noticed that if $\lambda$ is a complex eigenvalue of a real matrix $A,$ then the complex conjugate $\overline{\lambda}$ also appears to be an eigenvalue.

Moreover, if the eigenvalue $\lambda$ corresponds to an eigenvector $\mathbb{v},$ then the eigenvalue $\overline{\lambda}$ corresponds to an eigenvector $\overline{\mathbb v}.$

As a matter of fact, this is true for all matrices with real entries:

Let $A$ be a matrix with real entries. If $A$ has an eigenvector $\mathbb v$ with eigenvalue $\lambda,$ then $A$ also has an eigenvector $\overline{\mathbb v}$ with eigenvalue $\overline{\lambda}.$

Let's prove this. If a real matrix $A$ has an eigenvalue $\lambda$ with corresponding eigenvector $\mathbf{v},$ then

$$


A\mathbf{v} = \lambda\mathbf{v}.


$$

Taking the complex conjugate of both sides, we get

$$


\begin{aligned}\overset{𝐴𝐯}{} & =\overset{𝜆𝐯}{} \\ \overset{𝐴}{}\overset{𝐯}{} & =\overset{𝜆}{}\overset{𝐯}{}.\end{aligned}


$$

But since $A$ is a matrix with real entries, we have that $\overline{A} = A.$ So, we have

$$


A\overline{\mathbf{v}} = \overline{\lambda}\overline{\mathbf{v}}.


$$

Therefore, $\overline{\lambda}$ is also an eigenvalue of $A$ and its corresponding eigenvector is $\overline{\mathbf{v}}.$

### Example: Finding a Complex Eigenvalue of a 2x2 Matrix Given Another Eigenvalue

#### Question

Given that $\lambda_1=-2+3\text{i}$ and $\lambda_2$ are eigenvalues of a real $2 \times 2$ matrix $A,$ find $2(\lambda_1+\lambda_2).$

#### Explanation

Since $\lambda_1=-2+3\text{i}$ is a complex eigenvalue of $A,$ the second eigenvalue of $A$ must be the complex conjugate of $\lambda_1.$ Therefore,

$$


\lambda_2=\overline{\lambda}_1=-2-3\text{i}.


$$

Finally, we have

$$


\begin{aligned}2(𝜆_{1}+𝜆_{2}) & =2(−2+3i+(−2−3i)) \\ & =2(−4) \\ & =−8.\end{aligned}


$$
