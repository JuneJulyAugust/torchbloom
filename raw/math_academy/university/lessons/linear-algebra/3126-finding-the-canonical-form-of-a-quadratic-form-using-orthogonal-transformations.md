# Finding the Canonical Form of a Quadratic Form Using Orthogonal Transformations

Source: https://www.mathacademy.com/topics/3126?courseId=55
Topic ID: 3126

## Prerequisites

- [Diagonalization of 3x3 Symmetric Matrices](./3119-diagonalization-of-3x3-symmetric-matrices.md)
- [Change of Variables in Quadratic Forms](./3122-change-of-variables-in-quadratic-forms.md)

## Lesson

### Introduction

Consider a quadratic form

$$


\mathbf{x}^T \! A \mathbf{x},


$$

where $A$ is a symmetric matrix. As we know, any symmetric matrix can be orthogonally diagonalized as follows:

$$


D = P^T \! AP,


$$

where $P$ is an orthogonal matrix and $D$ is a diagonal matrix that contains eigenvalues of $A$ on the main diagonal.

Now, substituting the change of variable $\mathbf{x} = P \mathbf{y}$ into our quadratic form, we obtain

$$


\begin{aligned}𝐱^{𝑇}\,𝐴𝐱 & =(𝑃𝐲)^{𝑇}\,𝐴(𝑃𝐲) \\ & =𝐲^{𝑇}\,(𝑃^{𝑇}\,𝐴𝑃)𝐲 \\ & =𝐲^{𝑇}\,𝐷𝐲,\end{aligned}


$$

which gives us a canonical form.

As a result, using the orthogonal diagonalization of $A,$ we can find the canonical form of $\mathbf{x}^T \! A \mathbf{x}.$

For example, let's find the canonical form of

$$


Q(\mathbf{x})=x_1^2+4x_1x_2+x_2^2.


$$

First, we write down the matrix of our quadratic form:

$$


[\begin{aligned}1 & 2 \\ 2 & 1\end{aligned}]


$$

To find the coefficients of the canonical form, we need to calculate the eigenvalues of $A\mathbin{:}$

$$


\begin{aligned}|𝐴−𝜆𝐼| & =0 \\ \begin{matrix}1−𝜆 & 2 \\ 2 & 1−𝜆\end{matrix} & =0 \\ (1−𝜆)(1−𝜆)−4 & =0 \\ 𝜆^{2}−2𝜆−3 & =0 \\ (𝜆+1)(𝜆−3) & =0 \\ 𝜆 & =3,\,−1\end{aligned}


$$

So, writing the eigenvalues in descending order, we obtain the diagonal matrix

$$


[\begin{aligned}3 & 0 \\ 0 & −1\end{aligned}]


$$

The corresponding quadratic form after a change of variables is

$$


3y_1^2 - y_2^2.


$$

### Example: Finding the Canonical Form of a Quadratic Function by Finding Eigenvalues

#### Question

Using the method of orthogonal transformations, find the canonical form of $Q(\mathbf{x})=x_1^2+x_2^2+2x_3^2+4x_1x_2.$

#### Explanation

First, we write down the matrix of our quadratic form:

$$


\begin{aligned}1 & 2 & 0 \\ 2 & 1 & 0 \\ 0 & 0 & 2\end{aligned}


$$

Every quadratic form can be reduced to its canonical (diagonal) form using orthogonal transformations.

To find the coefficients of the canonical form, we need to calculate the eigenvalues of $A\mathbin{:}$

$$


\begin{aligned}|𝐴−𝜆𝐼| & =0 \\ \begin{matrix}1−𝜆 & 2 & 0 \\ 2 & 1−𝜆 & 0 \\ 0 & 0 & 2−𝜆\end{matrix} & =0 \\ (2−𝜆)\begin{matrix}1−𝜆 & 2 \\ 2 & 1−𝜆\end{matrix} & =0 \\ (2−𝜆)((1−𝜆)(1−𝜆)−4) & =0 \\ (2−𝜆)(𝜆^{2}−2𝜆−3) & =0 \\ (2−𝜆)(𝜆−3)(𝜆+1) & =0 \\ 𝜆 & =3,\,2,\,−1\end{aligned}


$$

So, writing the eigenvalues in descending order, we obtain the diagonal matrix

$$


\begin{aligned}3 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & −1\end{aligned}


$$

The corresponding quadratic form after a change of variables is

$$


3y_1^2 + 2y_2^2 - y_3^2.


$$

### Example: Reducing a Quadratic Function Over the 2D-Space to the Canonical Form Using Orthogonal Transformations

#### Question

Given the quadratic form $Q(\mathbf{x})=2x_1^2-2x_1x_2+2x_2^2,$ find its canonical (diagonal) form $\mathbf{y}^T \! D \mathbf{y}$ and an orthogonal matrix $P$ such that $\mathbf{x}=P\mathbf{y}$ defines the corresponding change of variables.

#### Explanation

First, we write down the matrix of our quadratic form:

$$


[\begin{aligned}2 & −1 \\ −1 & 2\end{aligned}]


$$

Every quadratic form can be reduced to its canonical (diagonal) form using orthogonal transformations.

To find the coefficients of the canonical form, we need to calculate the eigenvalues of $A\mathbin{:}$

$$


\begin{aligned}|𝐴−𝜆𝐼| & =0 \\ \begin{matrix}2−𝜆 & −1 \\ −1 & 2−𝜆\end{matrix} & =0 \\ 𝜆^{2}−4𝜆+3 & =0 \\ 𝜆 & =3,\,1\end{aligned}


$$

Now, we need to find an eigenvector basis of $A.$

- For $\lambda_1=3,$ we have Seeking a non-zero solution of $(A-3I)\mathbf{x}=\mathbf{0}$ gives the eigenvector $[\begin{aligned}−1 \\ 1\end{aligned}]$ Dividing $\mathbf{v}_1$ by its norm $\| \mathbf{v}_1 \| = \sqrt{2},$ we get

- For $\lambda_2=1,$ we have Seeking a non-zero solution of $(A-I)\mathbf{x}=\mathbf{0}$ gives the eigenvector $[\begin{aligned}1 \\ 1\end{aligned}]$ Dividing $\mathbf{v}_2$ by its norm $\| \mathbf{v}_2 \| = \sqrt{2},$ we get

Finally, we construct the diagonal matrix $D$ (writing the eigenvalues in descending order) and the orthogonal matrix $P$ in the usual way, and this gives us the following:

$$


[\begin{aligned}3 & 0 \\ 0 & 1\end{aligned}]


$$

### Example: Reducing a Quadratic Function Over the 3D-Space to the Canonical Form Using Orthogonal Transformations

#### Question

$$


\begin{aligned}1 & 0 & 0 \\ 0 & 3 & 1 \\ 0 & 1 & 3\end{aligned}


$$

Consider the matrices given above. Find an orthogonal matrix $P$ such that $\mathbf{x}=P\mathbf{y}$ defines the corresponding change of variables that reduces the quadratic form $Q(\mathbf{x}) = \mathbf{x}^T \! A \mathbf{x}$ to the canonical (diagonal) form $\mathbf{y}^T \! D \mathbf{y}.$

#### Explanation

Every quadratic form can be reduced to its canonical (diagonal) form using orthogonal transformations.

From the diagonal matrix $D,$ we deduce that the eigenvalues of the matrix $A$ are

$\qquad$ $\lambda_1=4, \quad$ $\lambda_2=2, \quad$ and $\quad\lambda_3=1.$

Now, we need to find an eigenvector basis of $A.$

- For $\lambda_1=4,$ we have Seeking a non-zero solution of $(A-4I)\mathbf{x}=\mathbf{0}$ gives the eigenvector $\begin{aligned}0 \\ 1 \\ 1\end{aligned}$ Dividing $\mathbf{v}_1$ by its norm $\| \mathbf{v}_1 \| = \sqrt{2},$ we get

- For $\lambda_2=2,$ we have Seeking a non-zero solution of $(A-2I)\mathbf{x}=\mathbf{0}$ gives the eigenvector $\begin{aligned}0 \\ −1 \\ 1\end{aligned}$ Dividing $\mathbf{v}_2$ by its norm $\| \mathbf{v}_2 \| = \sqrt{2},$ we get

- For $\lambda_3=1,$ we have Seeking a non-zero solution of $(A-I)\mathbf{x}=\mathbf{0}$ gives the eigenvector $\begin{aligned}1 \\ 0 \\ 0\end{aligned}$ Dividing $\mathbf{v}_3$ by its norm $\| \mathbf{v}_3 \| = 1,$ we get

Finally, we construct the orthogonal matrix $P$ in the usual way, and this gives us the following:

$$


\begin{aligned}0 & 0 & 1 \\ \frac{1}{\sqrt{2}} & −\frac{1}{\sqrt{2}} & 0 \\ \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} & 0\end{aligned}


$$
