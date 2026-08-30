# Singular Value Decomposition of Larger Matrices

Source: https://www.mathacademy.com/topics/3133?courseId=155
Topic ID: 3133

## Prerequisites

- [Singular Value Decomposition of 2x2 Matrices With Zero or Repeated Eigenvalues](./3278-singular-value-decomposition-of-2x2-matrices-with-zero-or-repeated-eigenvalues.md)

## Lesson

### Introduction

We can compute a singular value decomposition (SVD) of any matrix! The algorithm for computing an SVD of a rectangular $m\times n$ matrix $(m\neq n)$ is similar to the algorithm for square matrices.

As an example, let's consider the matrix $A,$ given by

$$


\begin{aligned}1 & 1 \\ −1 & 1 \\ 1 & 1\end{aligned}


$$

Notice that $A$ is a ${\color{blue}{3}}\times {\color{red}{2}}$ matrix. So, to compute the SVD of $A,$ we must write

$$


A=U \Sigma V^T,


$$

where

- $\Sigma$ is a ${\color{blue}{3}}\times {\color{red}{2}}$ matrix with the singular values of $A$ (ordered from largest to smallest) on the main diagonal and zeroes outside the main diagonal,

- $U$ is an orthogonal ${\color{blue}{3}} \times {\color{blue}{3}}$ matrix,

- $V$ is an orthogonal ${\color{red}{2}} \times {\color{red}{2}}$ matrix.

We proceed as follows:

- **Step 1.** Compute $A^T \! A\mathbin{:}$

- **Step 2.** Find the singular values of $A.$ Computing the eigenvalues of $A^TA,$ we get Therefore, the singular values of $A$ are

- **Step 3.** Find the right singular vectors of $A$ (i.e., the unit eigenvectors of $A^T A$). Seeking non-zero solutions of $(A^T \! A - \lambda_1 I)\mathbf{v}=\mathbf{0}$ and $(A^T \! A - \lambda_2 I)\mathbf{v}=\mathbf{0}$ gives the unit eigenvectors

- **Step 4.** Find the left singular vectors of $A.$ Since we know the singular values and right singular vectors, we can compute the first two columns of $U$ as follows: First, we compute $\mathbf u_1\mathbin{:}$ Then, we compute $\mathbf u_2\mathbin{:}$

- The matrix $U$ is a $3\times 3$ matrix. However, we do not have the third singular value, so we can't use the same formula to find the third column of $U.$ But we know that $U$ must be orthogonal. Hence, we must find a vector such that Solving this system, we get the following nonzero normalized solution:

Finally, we construct the matrices $U,$ $\Sigma,$ and $V\mathbin{:}$

$$


\begin{aligned}\frac{1}{\sqrt{√2}} & 0 & −\frac{1}{\sqrt{√2}} \\ 0 & 1 & 0 \\ \frac{1}{\sqrt{√2}} & 0 & \frac{1}{\sqrt{√2}}\end{aligned}


$$

### Example: Finding the Third Factor in the SVD of a Rectangular Matrix

#### Question

$$


\begin{aligned}3 & 1 \\ −1 & −3 \\ −4 & 4\end{aligned}


$$

Consider the matrices $A$ and $\Sigma$ shown above. Given that $A=U \Sigma V^T$ is a singular value decomposition of $A,$ find a $2\times 2$ matrix that could be the matrix $V.$

#### Explanation

Recall that if $A=U \Sigma V^T$ is a singular value decomposition of a $3 \times 2$ matrix $A,$ then

- $\Sigma$ is a $3 \times 2$ matrix with nonnegative elements on the main diagonal and zeroes outside the main diagonal,

- $U$ is an orthogonal $3 \times 3$ matrix,

- $V$ is an orthogonal $2 \times 2$ matrix.

Let's find the singular value decomposition of $A$ using the usual algorithm.

- **** Compute $A^T \! A\mathbin{:}$

- **** Find the singular values. From the matrix $\Sigma,$ we deduce that $\sigma_1=6$ and $\sigma_2=4.$

- **** Find the right singular vectors of $A$ (i.e., the unit eigenvectors of $A^T \! A$): For $\lambda_1=\sigma_1^2=36,$ we have Seeking a non-zero solution of $(A^T \! A - 36I)\mathbf{v}=\mathbf{0}$ gives the unit eigenvector For $\lambda_2=\sigma_2^2=16,$ we have Seeking a non-zero solution of $(A^T \! A - 16I)\mathbf{v}=\mathbf{0}$ gives the unit eigenvector

Finally, we construct the matrix $V\mathbin{:}$

$$


\begin{aligned}−\frac{1}{\sqrt{√2}} & \frac{1}{\sqrt{√2}} \\ \frac{1}{\sqrt{√2}} & \frac{1}{\sqrt{√2}}\end{aligned}


$$

### Example: Finding the First Factor in the SVD of a Rectangular Matrix

#### Question

$$


\begin{aligned}2 & −2 \\ −4 & −3 \\ 3 & 4\end{aligned}


$$

Consider the matrices shown above. Given that $A=U \Sigma V^T$ is a singular value decomposition of $A,$ find a vector whose components correspond to the $3$rd column of the matrix $U.$

#### Explanation

Recall that if $A=U \Sigma V^T$ is a singular value decomposition of an $3 \times 2$ matrix $A,$ then

- $\Sigma$ is a $3 \times 2$ matrix with nonnegative elements on the main diagonal and zeroes outside the main diagonal,

- $U$ is an orthogonal $3 \times 3$ matrix,

- $V$ is an orthogonal $2 \times 2$ matrix.

From the matrix $\Sigma,$ we deduce that $\sigma_1=7$ and $\sigma_2=3.$ Also, the columns $\mathbf{v}_1$ and $\mathbf{v}_2$ of $V$ give us the right singular vectors of $A.$

Therefore, we can compute the $1$st and $2$nd columns of $U$ as follows:

- First, we compute $\mathbf u_1\mathbin{:}$

- Then, we compute $\mathbf u_2\mathbin{:}$

Since we do not have the third singular value, we can't use the same formula to find the third column of $U.$ But we know that $U$ must be orthogonal. Hence, we must find a vector

$$


\begin{aligned}𝑥_{1} \\ 𝑥_{2} \\ 𝑥_{3}\end{aligned}


$$

such that

$$


\begin{aligned}𝐮_{1}⋅𝐮_{3}=0 \\ 𝐮_{2}⋅𝐮_{3}=0,\end{aligned}


$$

Solving this system, which is equivalent to

$$


\begin{aligned}−\frac{1}{\sqrt{√2}}𝑥_{2}+\frac{1}{\sqrt{√2}}𝑥_{3}=0 \\ −\frac{4}{3\sqrt{√2}}𝑥_{1}+\frac{1}{3\sqrt{√2}}𝑥_{2}+\frac{1}{3\sqrt{√2}}𝑥_{3}=0\end{aligned}


$$

we get the nonzero normalized solution

$$


\begin{aligned}\frac{1}{3} \\ \frac{2}{3} \\ \frac{2}{3}\end{aligned}


$$

Finally, we construct the matrix $U \mathbin{:}$

$$


\begin{aligned}0 & −\frac{4}{3\sqrt{√2}} & \frac{1}{3} \\ −\frac{1}{\sqrt{√2}} & \frac{1}{3\sqrt{√2}} & \frac{2}{3} \\ \frac{1}{\sqrt{√2}} & \frac{1}{3\sqrt{√2}} & \frac{2}{3}\end{aligned}


$$

### Choosing Eigenvectors When Eigenvalues Repeat or Are Missing

In some singular value decomposition problems, we do not get all of the needed vectors from the usual formulas right away.

This happens, for example, when:

- an eigenvalue is repeated, or

- a singular value is zero, so the corresponding vector is not determined uniquely.

In these cases, we proceed as follows:

- **Step 1.** Solve the system that defines the eigenspace (or orthogonal complement). For example, we solve an equation of the form or, when finding missing columns of $U,$ we solve orthogonality conditions such as

- **Step 2.** Write the general solution using free variables. This shows that there are infinitely many solutions. For example, the solution might look like where $x$ and $y$ are free variables.

- **Step 3.** Choose convenient vectors from the solution space. We usually choose simple values for the free variables to get easy vectors. These vectors should be linearly independent and, if possible, already orthogonal.

- **Step 4.** Orthogonalize the chosen vectors if necessary. If the vectors are not mutually orthogonal, we apply the Gram–Schmidt process.

- **Step 5.** Normalize the vectors. After that, we divide each vector by its norm to obtain unit vectors. These unit vectors form an orthonormal basis for the solution space, and they can be used as the needed columns of $V$ or $U.$

**Note:** In these situations, there is usually *more than one correct answer*. Different choices of free variables can produce different orthonormal bases, so the resulting SVD is not necessarily unique. What matters is that the chosen vectors:

- belong to the correct solution space,

- are mutually orthogonal, and

- have norm $1.$

Let's see a concrete example.

### Example: Finding the First Factor in the SVD of a Rectangular Matrix: Advanced Cases

#### Question

$$


\begin{aligned}1 & 0 \\ 2 & 0 \\ 0 & 0\end{aligned}


$$

Consider the matrices shown above. Given that $A=U \Sigma V^T$ is a singular value decomposition of $A,$ find a $3\times 3$ matrix that could be the matrix $U.$

#### Explanation

Recall that if $A=U \Sigma V^T$ is a singular value decomposition of a $3 \times 2$ matrix $A,$ then

- $\Sigma$ is a $3 \times 2$ matrix with nonnegative elements on the main diagonal and zeroes outside the main diagonal,

- $U$ is an orthogonal $3 \times 3$ matrix,

- $V$ is an orthogonal $2 \times 2$ matrix.

From the matrix $\Sigma,$ we deduce that $\sigma_1=\sqrt5$ and $\sigma_2=0.$ Also, the columns $\mathbf{v}_1$ and $\mathbf{v}_2$ of $V$ give us the right singular vectors of $A.$

Therefore, we can compute the $1$st column of $U$ as follows:

$$


\begin{aligned}𝐮_{1} & =\frac{1}{𝜎_{1}}𝐴𝐯_{1} \\ & =\frac{1}{\sqrt{√5}}\begin{aligned}1 & 0 \\ 2 & 0 \\ 0 & 0\end{aligned}[\begin{aligned}1 \\ 0\end{aligned}] \\ & =\frac{1}{\sqrt{√5}}\begin{aligned}1 \\ 2 \\ 0\end{aligned} \\ & =\begin{aligned}\frac{1}{\sqrt{√5}} \\ \frac{2}{\sqrt{√5}} \\ 0\end{aligned}\end{aligned}


$$

Since the second singular value is $\sigma_2=0$, and we do not have a third singular value, we can't use the same formula to find the second and third columns of $U.$ But we know that $U$ must be orthogonal. Hence, we must find vectors

$$


\begin{aligned}𝑥_{1} \\ 𝑥_{2} \\ 𝑥_{3}\end{aligned}


$$

such that $\mathbf{u}_1 \cdot \mathbf{u} = 0$ and $\|\mathbf{u}\|=1.$

Solving $\mathbf{u}_1 \cdot \mathbf{u} = 0,$ which is equivalent to

$$


\dfrac{1}{\sqrt{5}} x_1 + \dfrac{2}{\sqrt{5}} x_2 = 0 \qquad\Longrightarrow\qquad x_1 + 2x_2 = 0,


$$

we get the general solution

$$


\begin{aligned}−2𝑥_{2} \\ 𝑥_{2} \\ 𝑥_{3}\end{aligned}


$$

where $x_2$ and $x_3$ are free variables. Notice that the two linearly independent solutions are mutually orthogonal. Normalizing these vectors, we get

$$


\begin{aligned}−\frac{2}{\sqrt{√5}} \\ \frac{1}{\sqrt{√5}} \\ 0\end{aligned}


$$

Finally, we construct the matrix $U \mathbin{:}$

$$


\begin{aligned}\frac{1}{\sqrt{√5}} & −\frac{2}{\sqrt{√5}} & 0 \\ \frac{2}{\sqrt{√5}} & \frac{1}{\sqrt{√5}} & 0 \\ 0 & 0 & 1\end{aligned}


$$

### Example: Finding the First Factor in the SVD of a Rectangular Matrix: Cases Requiring Orthogonalization

#### Question

$$


\begin{aligned}\sqrt{√2} & 0 \\ 1 & 0 \\ −1 & 0\end{aligned}


$$

Consider the matrices shown above. Given that $A=U \Sigma V^T$ is a singular value decomposition of $A,$ find a $3\times 3$ matrix that could be the matrix $U.$

#### Explanation

Recall that if $A=U \Sigma V^T$ is a singular value decomposition of a $3 \times 2$ matrix $A,$ then

- $\Sigma$ is a $3 \times 2$ matrix with nonnegative elements on the main diagonal and zeroes outside the main diagonal,

- $U$ is an orthogonal $3 \times 3$ matrix,

- $V$ is an orthogonal $2 \times 2$ matrix.

From the matrix $\Sigma,$ we deduce that $\sigma_1=2$ and $\sigma_2=0.$ Also, the columns $\mathbf{v}_1$ and $\mathbf{v}_2$ of $V$ give us the right singular vectors of $A.$

Therefore, we can compute the $1$st column of $U$ as follows:

$$


\begin{aligned}𝐮_{1} & =\frac{1}{𝜎_{1}}𝐴𝐯_{1} \\ & =\frac{1}{2}\begin{aligned}\sqrt{√2} & 0 \\ 1 & 0 \\ −1 & 0\end{aligned}[\begin{aligned}1 \\ 0\end{aligned}] \\ & =\frac{1}{2}\begin{aligned}\sqrt{√2} \\ 1 \\ −1\end{aligned} \\ & =\begin{aligned}\frac{\sqrt{√2}}{2} \\ \frac{1}{2} \\ −\frac{1}{2}\end{aligned}\end{aligned}


$$

Since the second singular value is $\sigma_2=0$, and we do not have the third singular value, we can't use the same formula to find the second and third columns of $U.$ But we know that $U$ must be orthogonal. Hence, we must find vectors

$$


\begin{aligned}𝑢_{1} \\ 𝑢_{2} \\ 𝑢_{3}\end{aligned}


$$

such that $\mathbf{u}_1 \cdot \mathbf{u} = 0$ and $\|\mathbf{u}\|=1.$

Solving $\mathbf{u}_1 \cdot \mathbf{u} = 0,$ which is equivalent to

$$


\dfrac{\sqrt2}{2} x_1 + \dfrac{1}{2} x_2- \dfrac{1}{2} x_3 = 0 \qquad\Longrightarrow\qquad \sqrt2x_1 + x_2-x_3 = 0,


$$

we get the general solution

$$


\begin{aligned}𝑥_{1} \\ 𝑥_{2} \\ \sqrt{√2}𝑥_{1}+𝑥_{2}\end{aligned}


$$

where $x_1$ and $x_2$ are free variables.

Notice that the two linearly independent solutions $\mathbf{b}_1$ and $\mathbf{b}_2$ are ** mutually orthogonal. Therefore, we have to orthogonalize them using the Gram-Schmidt process. So, let

$$


\begin{aligned}1 \\ 0 \\ \sqrt{√2}\end{aligned}


$$

Then,

$$


\begin{aligned}𝐜_{2} & =𝐛_{2}−\frac{𝐛_{2}⋅𝐜_{1}}{𝐜_{1}⋅𝐜_{1}}𝐜_{1} \\ & =\begin{aligned}0 \\ 1 \\ 1\end{aligned}−\frac{\sqrt{√2}}{3}\begin{aligned}1 \\ 0 \\ \sqrt{√2}\end{aligned} \\ & =\frac{1}{3}\begin{aligned}−\sqrt{√2} \\ 3 \\ 1\end{aligned}.\end{aligned}


$$

Finally, normalizing the orthogonal vectors $\mathbf{c}_1$ and $\mathbf{c}_2,$ we obtain the second and third columns of $U{:}$

$$


\begin{aligned}\frac{1}{\sqrt{√3}} \\ 0 \\ \frac{\sqrt{√2}}{\sqrt{√3}}\end{aligned}


$$

So, the matrix $U$ could be the following:

$$


\begin{aligned}\frac{\sqrt{√2}}{2} & \frac{1}{\sqrt{√3}} & −\frac{\sqrt{√2}}{2\sqrt{√3}} \\ \frac{1}{2} & 0 & \frac{3}{2\sqrt{√3}} \\ −\frac{1}{2} & \frac{\sqrt{√2}}{\sqrt{√3}} & \frac{1}{2\sqrt{√3}}\end{aligned}


$$

### The Singular Value Decomposition of a Transposed Matrix

Suppose we want to find an SVD for the $2\times 4$ matrix $A,$ given by

$$


[\begin{aligned}1 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0\end{aligned}]


$$

Directly applying the standard approach to $A$ could be problematic because it requires finding the eigenvalues of the $4\times 4$ matrix $A^T \! A.$

In such cases, it's usually more convenient to find an SVD of the transposed matrix $A^T$ and then take the transpose of the resulting SVD. In this case, we would only have to find the eigenvalues of a $2 \times 2$ matrix.

For example, if

$$


A^T = U \Sigma V^T


$$

is an SVD for $A^T,$ then

$$


A= \left(A^T\right)^T= \left(U \Sigma V^T\right)^T=V\Sigma^T U^T


$$

is an SVD for $A.$

Going through our usual process, we find that an SVD for $A^T$ is

$$


\begin{aligned}\frac{1}{\sqrt{√2}} & 0 & −\frac{1}{\sqrt{√2}} & 0 \\ 0 & 0 & 0 & 1 \\ \frac{1}{\sqrt{√2}} & 0 & \frac{1}{\sqrt{√2}} & 0 \\ 0 & 1 & 0 & 0\end{aligned}


$$

Taking the transpose of the above equation. we find that an SVD for $A$ is

$$


[\begin{aligned}1 & 0 \\ 0 & 1\end{aligned}]


$$
