# Properties of Diagonalization

Source: https://www.mathacademy.com/topics/1969?courseId=154
Topic ID: 1969

## Prerequisites

- [Powers of Matrices](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/1725-powers-of-matrices.md)
- [Diagonalizing a 2x2 Matrix](./1968-diagonalizing-a-2x2-matrix.md)

## Lesson

### Introduction

Remember that the diagonalization of a $2\times 2$ matrix $A$ with eigenvalues $\lambda_1$ and $\lambda_2$ and corresponding linearly independent eigenvectors $\mathbf{v_1}$ and $\mathbf{v_2}$ is

$$


\begin{aligned}| & | \\ 𝐯_{1} & 𝐯_{2} \\ | & |\end{aligned}


$$

This idea also works in reverse. Given a diagonalization $A$ in the form

$$


A=PDP^{-1},


$$

we can immediately deduce that the eigenvalues of $A$ are the diagonal entries of $D,$ and the corresponding eigenvectors are the columns of $P.$ This is because the diagonalization of a matrix is (almost) unique.

**Note:** The diagonalization is "almost" unique because the order of the eigenvalue-eigenvector pairs may vary, and the eigenvectors may be replaced with scalar multiples of themselves. However, none of these variations change the actual outcome regarding the eigenvalue-eigenvector pairs that we deduce.

### Example: Restoring a Matrix Given Its Eigenvalues and Eigenvectors

#### Question

Find a $2 \times 2$ matrix $C$ that has eigenvalues $\lambda_1=1$ and $\lambda_2=-4,$ and corresponding eigenvectors

$$


[\begin{aligned}2 \\ −2\end{aligned}]


$$

#### Explanation

Since $\mathcal{B}= \{\mathbf{v}_1,\mathbf{v}_2\}$ is a basis of $\mathbb{R}^2$ consisting of the eigenvectors of $C,$ then $C$ must be diagonalizable.

So, we can write $C=PDP^{-1},$ where $P$ is a matrix whose columns are the eigenvectors of $C,$ and $D$ is a diagonal matrix whose entries are the eigenvalues in the corresponding order:

$$


\begin{aligned}| & | \\ 𝐯_{1} & 𝐯_{2} \\ | & |\end{aligned}


$$

Let $[\begin{aligned}2 & 1 \\ −2 & 1\end{aligned}]$ Then

$$


\begin{aligned}𝑃^{−1} & =[\begin{matrix}2 & 1 \\ −2 & 1\end{matrix}]^{−1}=\frac{1}{4}[\begin{matrix}1 & −1 \\ 2 & 2\end{matrix}].\end{aligned}


$$

Therefore, carrying out the necessary matrix multiplication, we obtain

$$


\begin{aligned}𝐶 & =\frac{1}{4}[\begin{matrix}2 & 1 \\ −2 & 1\end{matrix}][\begin{matrix}1 & 0 \\ 0 & −4\end{matrix}][\begin{matrix}1 & −1 \\ 2 & 2\end{matrix}] \\ & =\frac{1}{4}[\begin{matrix}2 & −4 \\ −2 & −4\end{matrix}][\begin{matrix}1 & −1 \\ 2 & 2\end{matrix}] \\ & =\begin{matrix}−\frac{3}{2} & −\frac{5}{2} \\ −\frac{5}{2} & −\frac{3}{2}\end{matrix}.\end{aligned}


$$

### Raising a Diagonalizable Matrix to a Power

One useful property of diagonalization is that it allows us to easily determine the power of a matrix.

As an example, we consider the $2\times 2$ matrix $[\begin{aligned}1 & −2 \\ 0 & −1\end{aligned}]$ with the diagonalization

$$


[\begin{aligned}5 & 1 \\ 0 & 1\end{aligned}]


$$

We will use the diagonalization of $A$ to compute $A^{55}.$

Let's start by computing $A^2.$ Using the properties of matrix multiplication, we have

$$


\begin{aligned}𝐴^{2} & =𝑃𝐷𝑃^{−1}⋅𝑃𝐷𝑃^{−1} \\ & =𝑃𝐷𝑃^{−1}⋅𝑃𝐷𝑃^{−1} \\ & =𝑃(𝐷𝐷)𝑃^{−1} \\ & =𝑃𝐷^{2}𝑃^{−1}.\end{aligned}


$$

Computing $A^3,$ we get

$$


\begin{aligned}𝐴^{3} & =𝐴^{2}⋅𝐴 \\ & =𝑃𝐷^{2}𝑃^{−1}⋅𝑃𝐷𝑃^{−1} \\ & =𝑃𝐷^{2}𝑃^{−1}⋅𝑃𝐷𝑃^{−1} \\ & =𝑃(𝐷^{2}𝐷)𝑃^{−1} \\ & =𝑃𝐷^{3}𝑃^{−1}.\end{aligned}


$$

We see that the matrix $P$ and its inverse $P^{-1}$ will always cancel each other out in the middle of the multiplication! So by induction, we have that

$$


A^{\color{blue}55}=P \cdot D^{\color{blue}55} \cdot P^{-1}.


$$

Now, we only need to find $D^{\color{blue}55}.$

Since $D$ is a diagonal matrix, we have the following:

$$


\begin{aligned}𝐷^{2} & =[\begin{matrix}1 & 0 \\ 0 & −1\end{matrix}][\begin{matrix}1 & 0 \\ 0 & −1\end{matrix}]=[\begin{matrix}1^{2} & 0 \\ 0 & (−1)^{2}\end{matrix}] \\ 𝐷^{3} & =𝐷^{2}𝐷=[\begin{matrix}1^{2} & 0 \\ 0 & (−1)^{2}\end{matrix}][\begin{matrix}1 & 0 \\ 0 & −1\end{matrix}]=[\begin{matrix}1^{3} & 0 \\ 0 & (−1)^{3}\end{matrix}]\end{aligned}


$$

Following this pattern, we get

$$


[\begin{aligned}1^{55} & 0 \\ 0 & (−1)^{55}\end{aligned}]


$$

Therefore, we can conclude that

$$


\begin{aligned}𝐴^{55} & =[\begin{matrix}5 & 1 \\ 0 & 1\end{matrix}][\begin{matrix}1 & 0 \\ 0 & −1\end{matrix}]^{55}\begin{matrix}\frac{1}{5} & −\frac{1}{5} \\ 0 & 1\end{matrix} \\ & =[\begin{matrix}5 & 1 \\ 0 & 1\end{matrix}][\begin{matrix}1 & 0 \\ 0 & −1\end{matrix}]\begin{matrix}\frac{1}{5} & −\frac{1}{5} \\ 0 & 1\end{matrix} \\ & =[\begin{matrix}5 & −1 \\ 0 & −1\end{matrix}]\begin{matrix}\frac{1}{5} & −\frac{1}{5} \\ 0 & 1\end{matrix} \\ & =[\begin{matrix}1 & −2 \\ 0 & −1\end{matrix}].\end{aligned}


$$

In general, given that $A = PDP^{-1},$ for any non-negative integer ${\color{blue}k},$ we obtain

$$


A^{\color{blue}k} = P \cdot D^{\color{blue}k} \cdot P^{-1}.


$$

### Example: Raising a Matrix to a Large Power Using the Properties of Diagonalization

#### Question

Find $A^{100},$ where

$$


[\begin{aligned}2 & −1 \\ −1 & 1\end{aligned}]


$$

#### Explanation

First, notice that

$$


[\begin{aligned}2 & −1 \\ −1 & 1\end{aligned}]


$$

So, we have been given the following diagonalization of $A\mathbin{:}$

$$


[\begin{aligned}2 & −1 \\ −1 & 1\end{aligned}]


$$

Since $A=PDP^{-1},$ we can compute $A^k$ by using the formula

$$


A^{k} = PD^{k}P^{-1}.


$$

Carrying out the necessary multiplication, we obtain the following:

$$


\begin{aligned}𝐴^{100} & =𝑃𝐷^{100}𝑃^{−1} \\ & =[\begin{matrix}2 & −1 \\ −1 & 1\end{matrix}][\begin{matrix}1 & 0 \\ 0 & 0\end{matrix}]^{100}[\begin{matrix}1 & 1 \\ 1 & 2\end{matrix}] \\ & =[\begin{matrix}2 & −1 \\ −1 & 1\end{matrix}][\begin{matrix}1^{100} & 0 \\ 0 & 0^{100}\end{matrix}][\begin{matrix}1 & 1 \\ 1 & 2\end{matrix}] \\ & =[\begin{matrix}2 & −1 \\ −1 & 1\end{matrix}][\begin{matrix}1 & 0 \\ 0 & 0\end{matrix}][\begin{matrix}1 & 1 \\ 1 & 2\end{matrix}] \\ & =[\begin{matrix}2 & 0 \\ −1 & 0\end{matrix}][\begin{matrix}1 & 1 \\ 1 & 2\end{matrix}] \\ & =[\begin{matrix}2 & 2 \\ −1 & −1\end{matrix}].\end{aligned}


$$

### Example: Finding the Eigenvalues and Eigenvectors of a Matrix Using the Properties of Diagonalization

#### Question

Find the eigenvectors of the $2 \times 2$ matrix $E,$ given that

$$


[\begin{aligned}3 & 6 \\ 1 & 1\end{aligned}]


$$

#### Explanation

Notice that the matrix $[\begin{aligned}3 & 6 \\ 1 & 1\end{aligned}]$ appears on both sides of the equation. Since this matrix is invertible (its determinant is not zero), left-multiplying the equation by the inverse gives the following expression for $E\mathbin{:}$

$$


[\begin{aligned}3 & 6 \\ 1 & 1\end{aligned}]


$$

Therefore, $E$ is diagonalizable. The eigenvalues of $E$ are $\lambda_1=3$ and $\lambda_2=6$ and the corresponding eigenvectors are the columns of the matrix $P.$ Computing $P,$ we obtain

$$


\begin{aligned}𝑃=[\begin{matrix}3 & 6 \\ 1 & 1\end{matrix}]^{−1}=\frac{1}{−3}[\begin{matrix}1 & −6 \\ −1 & 3\end{matrix}]=\begin{matrix}−\frac{1}{3} & 2 \\ \frac{1}{3} & −1\end{matrix}.\end{aligned}


$$

In conclusion, the corresponding eigenvectors are

$$


\begin{aligned}−\frac{1}{3} \\ \frac{1}{3}\end{aligned}


$$
