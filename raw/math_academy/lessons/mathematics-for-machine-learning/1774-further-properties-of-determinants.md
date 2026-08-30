# Further Properties of Determinants

Source: https://www.mathacademy.com/topics/1774?courseId=145
Topic ID: 1774

## Prerequisites

- [Conditions When a Determinant Equals Zero](./2201-conditions-when-a-determinant-equals-zero.md)

## Lesson

### Introduction

In this topic, we will consider a few more properties of determinants. Let's start with the following important property.

*The determinant of the product of two square matrices is equal to the product of the determinants.*

Symbolically, if and are both square matrices, then

For instance, suppose that we want to find the determinant of the matrix that is defined as follows:

To easily compute, we first compute the determinants of the two matrices and then multiply the results. Also, notice that both matrices in our product are triangular, so their determinants are given by the product of the diagonal entries:

### Example: Calculating the Determinant of a Product

#### Question

Given that find

#### Explanation

Given two matrices and we have

In our case, this gives

We can compute the required determinants as follows:

- For the first determinant, we notice that it's upper triangular. Therefore, the determinant is simply the product of the diagonal entries.

- For the second determinant, we can compute it using a Laplace expansion down the st column.

Therefore, we obtain

### The Determinant of an Inverse Matrix

Another useful property of determinants is that, for any invertible matrix $A,$ we have

$$


\det(A^{-1}) = \dfrac{1}{\det(A)}.


$$

To understand why the above property is true, remember that $A \cdot A^{-1} = I$ for any invertible matrix $A.$ So, we have

$$


\begin{aligned}𝐴⋅𝐴^{−1} & =𝐼 \\ det(𝐴⋅𝐴^{−1}) & =det(𝐼) \\ det(𝐴)⋅det(𝐴^{−1}) & =1 \\ det(𝐴^{−1}) & =\frac{1}{det(𝐴)}.\end{aligned}


$$

**Important:** We can only apply the formula $\det(A^{-1}) = \dfrac{1}{\det(A)}$ if $A$ is invertible, meaning that $\det(A) \neq 0.$

### Example: Calculating the Determinant of the Inverse of a Matrix

#### Question

Find $|A^{-1}|,$ if $\begin{aligned}2 & 14 & −1 \\ 7 & −6 & −6 \\ 0 & −3 & 0\end{aligned}$

#### Explanation

Given an invertible $n\times n$ matrix $A,$ we have

$$


|A^{-1}| = \dfrac{1}{|A|}.


$$

First, we find $|A|$ using a Laplace expansion across the $3$rd row:

$$


\begin{aligned}|𝐴| & =\begin{aligned}2 & 14 & −1 \\ 7 & −6 & −6 \\ 0 & −3 & 0\end{aligned} \\ & =−3(−1)^{3+2}\begin{aligned}2 & −1 \\ 7 & −6\end{aligned} \\ & =3⋅(−12+7) \\ & =−15\end{aligned}


$$

Therefore, we obtain

$$


\det(A^{-1}) = \dfrac{1}{|A|} = -\dfrac{1}{15}.


$$

### The Linearity of the Determinant

One final important property of the determinant is that it is **linear in each row and column**. For rows, for example, this means

$$


\begin{aligned} & det\begin{aligned}⋮ & ⋮ & … & ⋮ \\ ◻_{1}+△_{1} & ◻_{2}+△_{2} & … & ◻_{𝑛}+△_{𝑛} \\ ⋮ & ⋮ & … & ⋮\end{aligned} \\ & \,\,=det\begin{aligned}⋮ & ⋮ & … & ⋮ \\ ◻_{1} & ◻_{2} & … & ◻_{𝑛} \\ ⋮ & ⋮ & … & ⋮\end{aligned}+det\begin{aligned}⋮ & ⋮ & … & ⋮ \\ △_{1} & △_{2} & … & △_{𝑛} \\ ⋮ & ⋮ & … & ⋮\end{aligned}.\end{aligned}


$$

For instance, it's easy to check that

$$


\begin{aligned}\overset{\overset{det[\begin{aligned}1 & 2 \\ 3 & 4\end{aligned}]}{}}{−2} & =det[\begin{aligned}1 & 2 \\ 0+3 & 4+0\end{aligned}] \\ & =\underset{4}{\underset{}{det[\begin{aligned}1 & 2 \\ 0 & 4\end{aligned}]}}+\underset{−6}{\underset{}{det[\begin{aligned}1 & 2 \\ 3 & 0\end{aligned}]}}.\end{aligned}


$$

Note that this property also holds for columns:

$$


\begin{aligned}det\begin{aligned}⋯ & ◻_{1}+△_{1} & ⋯ \\ ⋯ & ◻_{2}+△_{2} & ⋯ \\ ⋮ & ⋮ & ⋮ \\ ⋯ & ◻_{𝑛}+△_{𝑛} & ⋯\end{aligned}=det\begin{aligned}⋯ & ◻_{1} & ⋯ \\ ⋯ & ◻_{2} & ⋯ \\ ⋮ & ⋮ & ⋮ \\ ⋯ & ◻_{𝑛} & ⋯\end{aligned}+det\begin{aligned}⋯ & △_{1} & ⋯ \\ ⋯ & △_{2} & ⋯ \\ ⋮ & ⋮ & ⋮ \\ ⋯ & △_{𝑛} & ⋯\end{aligned}\end{aligned}


$$

For example, we have that

$$


\begin{aligned}\overset{\overset{det[\begin{aligned}1 & 2 \\ 3 & 4\end{aligned}]}{}}{−2} & =det[\begin{aligned}1+0 & 2 \\ 0+3 & 4\end{aligned}] \\ & =\underset{4}{\underset{}{det[\begin{aligned}1 & 2 \\ 0 & 4\end{aligned}]}}+\underset{−6}{\underset{}{det[\begin{aligned}0 & 2 \\ 3 & 4\end{aligned}]}}.\end{aligned}


$$

### Example: Calculating a Determinant Using the Linearity of the Determinant

#### Question

Given that $\begin{aligned}𝑎 & 𝑏 & 𝑐 \\ 1 & 2 & 3 \\ 1 & 1 & 2\end{aligned}$ find $\begin{aligned}𝑎 & 𝑏 & 𝑐+1 \\ 1 & 2 & 3 \\ 1 & 1 & 2\end{aligned}$

#### Explanation

We "factor out" the given determinant from the determinant we would like to find:

$$


\begin{aligned}\begin{aligned}𝑎 & 𝑏 & 𝑐+1 \\ 1 & 2 & 3 \\ 1 & 1 & 2\end{aligned} & =\begin{aligned}𝑎+0 & 𝑏+0 & 𝑐+1 \\ 1 & 2 & 3 \\ 1 & 1 & 2\end{aligned}\end{aligned}


$$

Now, using the linearity property of determinants and expanding the second determinant across the $1$st row, we obtain

$$


\begin{aligned}\begin{aligned}𝑎+0 & 𝑏+0 & 𝑐+1 \\ 1 & 2 & 3 \\ 1 & 1 & 2\end{aligned} & =\underset{−10}{\underset{}\begin{aligned}𝑎 & 𝑏 & 𝑐 \\ 1 & 2 & 3 \\ 1 & 1 & 2\end{aligned}}}+\begin{aligned}0 & 0 & 1 \\ 1 & 2 & 3 \\ 1 & 1 & 2\end{aligned} \\ & =−10+1(−1)^{1+3}\begin{aligned}1 & 2 \\ 1 & 1\end{aligned} \\ & =−10−1 \\ & =−11.\end{aligned}


$$
