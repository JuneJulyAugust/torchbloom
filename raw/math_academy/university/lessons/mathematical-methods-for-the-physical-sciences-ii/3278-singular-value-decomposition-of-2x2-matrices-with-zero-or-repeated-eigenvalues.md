# Singular Value Decomposition of 2x2 Matrices With Zero or Repeated Eigenvalues

Source: https://www.mathacademy.com/topics/3278?courseId=155
Topic ID: 3278

## Prerequisites

- [Singular Value Decomposition of 2x2 Matrices](./3132-singular-value-decomposition-of-2x2-matrices.md)

## Lesson

### Introduction

Suppose that $A$ is a $m\times n$ matrix, and

$$


A=U \Sigma V^T


$$

is a singular value decomposition of $A.$ If the $i$th singular value of $A$ is nonzero, then the $i$th column of the orthogonal matrix $U$ can be found using the formula

$$


\mathbf{u}_i = \dfrac{1}{\sigma_i} A\mathbf{v}_i,


$$

where $\mathbf u_i$ and $\mathbf v_i$ are the $i$th columns of the orthogonal matrices $U$ and $V,$ respectively.

The formula above works whenever $\sigma_i\neq 0.$ But how do we find the $i$th column of $U$ in cases where $\sigma_i = 0?$ It turns out that we can find the corresponding left singular vector using the geometric properties of singular values.

For example, suppose that

$$


[\begin{aligned}\sqrt{√3} & 1 \\ 3 & \sqrt{√3}\end{aligned}]


$$

and $A=U \Sigma V^T$ is a singular value decomposition of $A,$ where

$$


[\begin{aligned}4 & 0 \\ 0 & 0\end{aligned}]


$$

The matrices $\Sigma$ and $V$ can be found using the methods we've seen before. So, our task now is to find the matrix $U.$

From $\Sigma,$ we deduce that the singular values of $A$ are $\sigma_1=4$ and $\sigma_2=0.$ Therefore, the first column of $U$ is

$$


\begin{aligned}𝐮_{1} & =\frac{1}{𝜎_{1}}𝐴𝐯_{1} \\ & =\frac{1}{4}[\begin{aligned}\sqrt{√3} & 1 \\ 3 & \sqrt{√3}\end{aligned}]\begin{aligned}\frac{\sqrt{√3}}{2} \\ \frac{1}{2}\end{aligned} \\ & =\begin{aligned}\frac{1}{2} \\ \frac{\sqrt{√3}}{2}\end{aligned}\end{aligned}


$$

Since the second singular value is $\sigma_2=0$, we can't use the same formula to find the second column of $U.$ However, we know that $U$ is an orthogonal matrix. Hence, we must find a vector

$$


[\begin{aligned}𝑥_{1} \\ 𝑥_{2}\end{aligned}]


$$

such that

$$


\mathbf{u}_1 \cdot \mathbf{u}_2 = 0 \qquad \textrm{and} \qquad \|\mathbf{u}_2\|=1.


$$

Let's consider each condition in turn:

- The equation $\mathbf{u}_1 \cdot \mathbf{u}_2 = 0$ is equivalent to Seeking a nonzero solution to this equation, we get the vector

- Normalizing the vector we just found, we get

Therefore, our orthogonal matrix $U$ is given by

$$


\begin{aligned}\frac{1}{2} & −\frac{\sqrt{√3}}{2} \\ \frac{\sqrt{√3}}{2} & \frac{1}{2}\end{aligned}


$$

### Example: Finding the Columns of the First Matrix Given Part of an SVD With a Zero Eigenvalue

#### Question

$$


[\begin{aligned}\sqrt{√3} & −1 \\ −\sqrt{√3} & 1\end{aligned}]


$$

Consider the matrices shown above. Given that $A=U \Sigma V^T$ is a singular value decomposition of $A,$ what is the second column of $U?$

#### Explanation

Recall that if $A=U \Sigma V^T$ is a singular value decomposition of $A,$ and $\sigma_i \neq 0,$ then the $i$th column of $U$ can be found as

$$


\mathbf{u}_i = \dfrac{1}{\sigma_i} A\mathbf{v}_i,


$$

where $\mathbf u_i$ and $\mathbf v_i$ are the $i$th columns of the orthogonal matrices $U$ and $V,$ respectively.

From the matrix $\Sigma,$ we deduce that the singular values are $\sigma_1=2\sqrt{2}$ and $\sigma_2=0.$ Therefore, the first column of $U$ is

$$


\begin{aligned}𝐮_{1} & =\frac{1}{𝜎_{1}}𝐴𝐯_{1} \\ & =\frac{1}{2\sqrt{√2}}[\begin{aligned}\sqrt{√3} & −1 \\ −\sqrt{√3} & 1\end{aligned}]\begin{aligned}−\frac{\sqrt{√3}}{2} \\ \frac{1}{2}\end{aligned} \\ & =\frac{1}{2\sqrt{√2}}[\begin{aligned}−2 \\ 2\end{aligned}] \\ & =\begin{aligned}−\frac{1}{\sqrt{√2}} \\ \frac{1}{\sqrt{√2}}\end{aligned}.\end{aligned}


$$

Since the second singular value is $\sigma_2=0$, we can't use the same formula to find the second column of $U.$ But we know that $U$ must be orthogonal. Hence, we must find a vector

$$


[\begin{aligned}𝑥_{1} \\ 𝑥_{2}\end{aligned}]


$$

such that

$$


\mathbf{u}_1 \cdot \mathbf{u}_2 = 0 \qquad \textrm{and} \qquad \|\mathbf{u}_2\|=1.


$$

Solving $\mathbf{u}_1 \cdot \mathbf{u}_2 = 0,$ which is equivalent to

$$


-\dfrac{1}{\sqrt{2}} x_1 + \dfrac{1}{\sqrt{2}} x_2 = 0,


$$

we get a nonzero solution $[\begin{aligned}1 \\ 1\end{aligned}]$ Normalizing this vector, we finally obtain the second column of $U\mathbin{:}$

$$


[\begin{aligned}1 \\ 1\end{aligned}]


$$

### Example: The Singular Value Decomposition of a 2x2 Matrix With a Zero Eigenvalue

#### Question

$$


[\begin{aligned}4 & −2 \\ −4 & 2\end{aligned}]


$$

Consider the matrices $A$ and $\Sigma$ shown above. Given that $A=U \Sigma V^T$ is a singular value decomposition of $A,$ find the matrices $U$ and $V.$

#### Explanation

Let's find the singular value decomposition of $A$ using the usual algorithm.

- **** Compute $A^T \! A\mathbin{:}$

- **** Find the singular values: From the matrix $\Sigma,$ we deduce that $\sigma_1=2\sqrt{10}$ and $\sigma_2=0.$

- **** Find the right singular vectors of $A$ (i.e., the unit eigenvectors of $A^T \! A$): For $\lambda_1=\sigma_1^2=40,$ we have Seeking a non-zero solution of $(A^T \! A - 40I)\mathbf{v}=\mathbf{0}$ gives a unit eigenvector For $\lambda_2=\sigma_2^2=0,$ we have Seeking a non-zero solution of $(A^T \! A - 0I)\mathbf{v}=\mathbf{0}$ gives a unit eigenvector

- **** Find the left singular vectors of $A$: Since the first singular value is not zero, and we know the corresponding singular right vector, we can compute the first column of $U$ as follows: Since the second singular value is $\sigma_2=0$, we can't use the same formula to find the second column of $U.$ But we know that $U$ must be orthogonal. Hence, we must find a vector such that Solving $\mathbf{u}_1 \cdot \mathbf{u}_2 = 0,$ which is equivalent to we get a nonzero solution $[\begin{aligned}1 \\ 1\end{aligned}]$ Normalizing this vector, we finally obtain the second column of $U\mathbin{:}$

Finally, we construct the matrices $U$ and $V\mathbin{:}$

$$


\begin{aligned}−\frac{1}{\sqrt{√2}} & \frac{1}{\sqrt{√2}} \\ \frac{1}{\sqrt{√2}} & \frac{1}{\sqrt{√2}}\end{aligned}


$$

### Singular Value Decomposition of 2x2 Matrices With Repeated Eigenvalues

It follows from the definitions that a $2\times 2$ matrix $A$ has two repeated singular values $\sigma_1= \sigma_2= \sigma$ if and only if the matrix $A^TA$ has two repeated eigenvalues $\lambda_1=\lambda_2 = \sigma^2.$ Thus, since $A^TA$ is diagonalizable (because it is symmetric), the eigenspace corresponding to $\sigma^2$ must be two-dimensional. Therefore,

$$


[\begin{aligned}𝜎^{2} & 0 \\ 0 & 𝜎^{2}\end{aligned}]


$$

Consequently, we can use any pair of unit orthogonal vectors as a basis for the eigenspace corresponding to $\sigma^2.$

Let's illustrate this with an example. Consider the following matrix:

$$


[\begin{aligned}2 & 3 \\ −3 & 2\end{aligned}]


$$

Let's find a singular value decomposition of $A$ using the usual algorithm.

- **Step 1.** Compute $A^T \! A\mathbin{:}$

- **Step 2.** Find the singular values: Notice that since $A^T \! A$ is diagonal, the singular values of $A$ are

- **Step 3.** Find the right singular vectors of $A$ (i.e., the unit eigenvectors of $A^T \! A$): Since the singular values are equal, we can always take as solutions of $(A^T\!A-13I)\mathbf{v}=\mathbf{0}$ the unit eigenvectors

- **Step 4.** Find the left singular vectors of $A$: Since we know the singular values and right singular vectors, we can compute the columns of $U$ as follows: First, we compute $\mathbf u_1\mathbin{:}$ Then, we compute $\mathbf u_2\mathbin{:}$

Finally, we construct the matrices $U,$ $\Sigma,$ and $V\mathbin{:}$

$$


\begin{aligned}\frac{2}{\sqrt{√13}} & \frac{3}{\sqrt{√13}} \\ −\frac{3}{\sqrt{√13}} & \frac{2}{\sqrt{√13}}\end{aligned}


$$

**Note:** By swapping the order of eigenvectors in step 3, we swap the vectors $\mathbf{u}_1$ and $\mathbf{u}_2$ in step 4. However, the resulting matrices (with swapped columns) will give us a valid singular decomposition too.

### Example: The Singular Value Decomposition of a 2x2 Matrix With Repeated Eigenvalues

#### Question

$$


[\begin{aligned}1 & 1 \\ −1 & 1\end{aligned}]


$$

Consider the matrix shown above. Given that $A=U \Sigma V^T$ is a singular value decomposition of $A,$ find the matrices $U$ and $V.$

#### Explanation

Let's find the singular value decomposition of $A$ using the usual algorithm.

- **** Compute $A^T \! A\mathbin{:}$

- **** Find the singular values: Notice that since $A^T \! A$ is diagonal, the singular values of $A$ are $\qquad$ $\sigma_1 = \sigma_2 = \sqrt{2}.$

- **** Find the right singular vectors of $A$: Seeking non-zero solutions of $(A^T\!A-2I)\mathbf{v}=\mathbf{0},$ we obtain the unit eigenvectors $\qquad$ $[\begin{aligned}1 \\ 0\end{aligned}]$ and $[\begin{aligned}0 \\ 1\end{aligned}]$

- **** Find the left singular vectors of $A$: Since we know the singular values and right singular vectors, we can compute the columns of $U$ as follows: First, we compute $\mathbf u_1\mathbin{:}$ Then, we compute $\mathbf u_2\mathbin{:}$

Finally, we construct the matrices $U,$ $\Sigma,$ and $V\mathbin{:}$

$$


\begin{aligned}\frac{1}{\sqrt{√2}} & \frac{1}{\sqrt{√2}} \\ −\frac{1}{\sqrt{√2}} & \frac{1}{\sqrt{√2}}\end{aligned}


$$
