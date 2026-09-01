# Computing Principal Components

Source: https://www.mathacademy.com/topics/3945?courseId=145
Topic ID: 3945

## Prerequisites

- [Calculating the Eigenvectors of a 3x3 Matrix With Distinct Eigenvalues](./1977-calculating-the-eigenvectors-of-a-3x3-matrix-with-distinct-eigenvalues.md)
- [Introduction to Principal Component Analysis](./3775-introduction-to-principal-component-analysis.md)

## Lesson

### Introduction

Recall that the principal components of a standardized observation matrix $X$ are the unit eigenvectors of the covariance matrix $C.$ If

$$


\lambda_1 \gt \lambda_2 \gt \cdots\gt \lambda_n


$$

are the eigenvalues of $C$ written in descending order, then:

- the $1$st principal component is the unit eigenvector $\mathbf u_1$ corresponding to the $1$st eigenvalue $\lambda_1,$

- the $2$nd principal component is the unit eigenvector $\mathbf u_2$ corresponding to the $2$nd eigenvalue $\lambda_2,$

- $\cdots$

and so on.

For example, suppose that the covariance matrix $C$ of some particular observations is

$$


[\begin{aligned}9 & 1 \\ 1 & 9\end{aligned}]


$$

It's easy to show that the eigenvalues of the covariance matrix $C,$ in descending order, are

$$


\lambda_1=10, \qquad \lambda_2=8.


$$

To find the first principal component of the data, we need the unit eigenvector corresponding to the eigenvalue $\lambda_1=10.$

Applying our usual algorithm for finding eigenvectors, we have

$$


\begin{aligned}𝐶−10𝐼 & =[\begin{matrix}9 & 1 \\ 1 & 9\end{matrix}]−10[\begin{matrix}1 & 0 \\ 0 & 1\end{matrix}]=[\begin{matrix}−1 & 1 \\ 1 & −1\end{matrix}].\end{aligned}


$$

Now, seeking a non-zero solution of $(C-10I)\mathbf{x}=\mathbf{0}$ gives the eigenvector

$$


[\begin{aligned}1 \\ 1\end{aligned}]


$$

Finally, dividing $\mathbf{v}_1$ by its norm $\| \mathbf{v}_1 \| = \sqrt{2},$ we get

$$


[\begin{aligned}1 \\ 1\end{aligned}]


$$

Therefore, the $1$st principal component of the data is $[\begin{aligned}1 \\ 1\end{aligned}]$

**Note:** The opposite vector $[\begin{aligned}1 \\ 1\end{aligned}]$ also works in the example above.

### Example: Finding a Principal Component Given a 2x2 Covariance Matrix

#### Question

The covariance matrix $C$ of some particular observations is shown below.

$$


[\begin{aligned}7 & 3 \\ 3 & 15\end{aligned}]


$$

Find the second principal component of the data, given that the eigenvalues of $C$ are $16$ and $6.$

#### Explanation

Recall that the unit eigenvectors of the covariance matrix $C$ are called the principal components of the data. If

$$


\lambda_1 \gt \lambda_2 \gt \cdots\gt \lambda_n


$$

are the eigenvalues of $C$ written in descending order, then:

- the $1$st principal component is the unit eigenvector $\mathbf u_1$ corresponding to the $1$st eigenvalue $\lambda_1,$

- the $2$nd principal component is the unit eigenvector $\mathbf u_2$ corresponding to the $2$nd eigenvalue $\lambda_2,$

- $\cdots$

and so on.

In our case, the eigenvalues of the covariance matrix $C,$ in descending order, are $\lambda_1=16$ and $\lambda_2=6.$ So, we need the unit eigenvector that corresponds to the eigenvalue $\lambda_2=6{:}$

Applying our usual algorithm for finding eigenvectors, we have

$$


\begin{aligned}𝐶−6𝐼 & =[\begin{matrix}7 & 3 \\ 3 & 15\end{matrix}]−6[\begin{matrix}1 & 0 \\ 0 & 1\end{matrix}]=[\begin{matrix}1 & 3 \\ 3 & 9\end{matrix}].\end{aligned}


$$

Seeking a non-zero solution of $(C-6I)\mathbf{x}=\mathbf{0}$ gives the eigenvector $[\begin{aligned}−3 \\ 1\end{aligned}]$

Finally, dividing $\mathbf{v}_2$ by its norm $\| \mathbf{v}_2 \| = \sqrt{10},$ we get

$$


[\begin{aligned}−3 \\ 1\end{aligned}]


$$

Therefore, the second principal component of the data is $[\begin{aligned}−3 \\ 1\end{aligned}]$

### Example: Finding a Principal Component Given a 3x3 Covariance Matrix

#### Question

The covariance matrix $C$ of some particular observations is shown below.

$$


\begin{aligned}5 & 2 & 2 \\ 2 & 6 & 0 \\ 2 & 0 & 4\end{aligned}


$$

Find the first principal component of the data, given that the eigenvalues of $S$ are $8,$ $5,$ and $2.$

#### Explanation

Recall that the unit eigenvectors of the covariance matrix $C$ are called the principal components of the data. If

$$


\lambda_1 \gt \lambda_2 \gt \cdots\gt \lambda_n


$$

are the eigenvalues of $C$ written in descending order, then:

- the $1$st principal component is the unit eigenvector $u_1$ corresponding to the $1$st eigenvalue $\lambda_1,$

- the $2$nd principal component is the unit eigenvector $u_2$ corresponding to the $2$nd eigenvalue $\lambda_2,$

- $\cdots$

and so on.

In our case, the eigenvalues of the covariance matrix $C,$ in descending order, are

$$


\lambda_1=8,\qquad \lambda_2=5,\qquad \lambda_3=2.


$$

So, we need the unit eigenvector that corresponds to the eigenvalue $\lambda_1=8{:}$

Applying our usual algorithm for finding eigenvectors, we have

$$


\begin{aligned}𝐶−8𝐼 & =\begin{matrix}5 & 2 & 2 \\ 2 & 6 & 0 \\ 2 & 0 & 4\end{matrix}−8\begin{matrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{matrix}=\begin{matrix}−3 & 2 & 2 \\ 2 & −2 & 0 \\ 2 & 0 & −4\end{matrix}.\end{aligned}


$$

Seeking a non-zero solution of $(C-8I)\mathbf{x}=\mathbf{0}$ gives the eigenvector $\begin{aligned}2 \\ 2 \\ 1\end{aligned}$

Finally, dividing $\mathbf{v}_1$ by its norm $\| \mathbf{v}_1 \| =3,$ we get

$$


\begin{aligned}2 \\ 2 \\ 1\end{aligned}


$$

Therefore, the first principal component of the data is $\begin{aligned}2 \\ 2 \\ 1\end{aligned}$
