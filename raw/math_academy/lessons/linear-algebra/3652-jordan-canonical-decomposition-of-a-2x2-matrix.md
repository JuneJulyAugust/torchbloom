# Jordan Canonical Decomposition of a 2x2 Matrix

Source: https://www.mathacademy.com/topics/3652?courseId=55
Topic ID: 3652

## Prerequisites

- [Jordan Canonical Form of a 2x2 Matrix](./3629-jordan-canonical-form-of-a-2x2-matrix.md)

## Lesson

### Introduction

Every square matrix $A$ can be written as

$$


A = PJP^{-1},


$$

where $J$ is a Jordan canonical form and $P$ is an invertible matrix.

Expressing $A$ in the above form is called a **Jordan canonical decomposition** of $A,$ and is an extension of diagonalization that works for all square matrices.

So, to find a Jordan canonical decomposition of $A$ means to find both

- a Jordan canonical form $J,$ and

- an invertible matrix $P$ that satisfies the equation $A = PJP^{-1}$.

If $A$ is diagonalizable, finding a Jordan canonical decomposition is the same as diagonalizing. In this lesson, we will focus on non-diagonalizable matrices.

### An Introductory Example

As an example, consider the following matrix:

$$


[\begin{aligned}0 & 1 \\ −4 & 4\end{aligned}]


$$

This matrix has a single eigenvalue $\lambda = {\color{red}2}$ and, since $A$ is not scalar, it is not diagonalizable. Thus, the Jordan canonical form of $A$ is

$$


[\begin{aligned}2 & 1 \\ 0 & 2\end{aligned}]


$$

We can show that $A$ has the Jordan canonical decomposition $A = PJP^{-1},$ where

$$


[\begin{aligned}1 & 0 \\ 2 & 1\end{aligned}]


$$

Notice that the columns of $P$ form a basis of $\mathbb{R}^2$ that generates the following chains:

$$


\begin{aligned}𝐯_{2}\overset{}{𝐴−2𝐼\,}𝐯_{1}\overset{}{𝐴−2𝐼\,}𝟎\end{aligned}


$$

The vectors ${\color{blue}\mathbf{v}_1}$ and ${\color{DarkBlue}\mathbf{v}_2}$ are generalized eigenvectors corresponding to $\lambda = {\color{red}2}.$ Here, ${\color{blue}\mathbf{v}_1}$ is an eigenvector of $A,$ while ${\color{DarkBlue}\mathbf{v}_2}$ is a generalized eigenvector of rank $2.$

In general, the matrix $P$ of any Jordan canonical decomposition of a non-diagonalizable $2\times 2$ matrix $A$ with eigenvalue $\lambda$ must satisfy the following property:

- The columns of $P$ associated with a Jordan block $J_2(\lambda)$ are generalized eigenvectors that correspond to the eigenvalue $\lambda,$ where the first column of $P$ is an eigenvector, and the second column of $P$ is a generalized eigenvector of rank $2$ that is mapped to the first column under the action of $A-\lambda I.$

**Watch out!** The order of the columns of $P$ is important! The first column should *always* be an eigenvector.

### Example: Identifying Columns of a Transformation Matrix in a Jordan Decomposition

#### Question

$$


[\begin{aligned}3 & −4 \\ 1 & −1\end{aligned}]


$$

Consider the matrices above. Given that $A = P J P^{-1}$ is a Jordan canonical decomposition of $A,$ which of the following could be the second column of the matrix $P?$

$$


[\begin{aligned}1 \\ 0\end{aligned}]


$$

#### Explanation

First, notice that the Jordan matrix $J$ consists of one Jordan block $J = J_2(1).$

Therefore, the columns of $P$ form the following chain:

$$


\begin{aligned}𝐽_{2}(1) & : & 𝐯_{2}\overset{}{𝐴−1𝐼\,}𝐯_{1}\overset{}{𝐴−1𝐼\,}𝟎 & \end{aligned}


$$

As a result, the second column of $P$ is a generalized eigenvector of rank $2$ corresponding to $\lambda=1.$

Now, computing $A-1I,$ we get

$$


\begin{aligned}𝐴−1𝐼 & =[\begin{aligned}3 & −4 \\ 1 & −1\end{aligned}]−1[\begin{aligned}1 & 0 \\ 0 & 1\end{aligned}]=[\begin{aligned}2 & −4 \\ 1 & −2\end{aligned}].\end{aligned}


$$

Among the given vectors, only $\mathbf x$ is a generalized eigenvector of rank $2,$ since

$$


[\begin{aligned}2 & −4 \\ 1 & −2\end{aligned}]


$$

and

$$


[\begin{aligned}2 & −4 \\ 1 & −2\end{aligned}]


$$

Therefore, we can write

$$


\begin{aligned}[\begin{aligned}1 \\ 0\end{aligned}]\overset{}{𝐴−1𝐼\,}[\begin{aligned}2 \\ 1\end{aligned}]\overset{}{𝐴−1𝐼\,}𝟎.\end{aligned}


$$

The other vectors do not satisfy this condition.

### Finding the Jordan Decomposition of a Non-Diagonalizable 2x2 Matrix

Let's find the Jordan canonical decomposition of the matrix $A,$ given by

$$


[\begin{aligned}−4 & 4 \\ −1 & 0\end{aligned}]


$$

To find a Jordan canonical decomposition of a $2\times 2$ matrix, we follow a three-step **Jordan decomposition algorithm:**

**Step 1:** Find the eigenvalues of the matrix.

We solve the characteristic equation $\vert A - \lambda I \vert = 0.$ For the given matrix, there is only one eigenvalue, namely $\lambda = -2.$

**Step 2:** Find a basis of $\mathbb{R}^2$ consisting of the generalized eigenvectors corresponding to each eigenvalue.

Applying the usual method for computing eigenvectors, we get an eigenvector

$$


[\begin{aligned}2 \\ 1\end{aligned}]


$$

corresponding to the eigenvalue $\lambda = -2.$ This is the first vector of our basis.

To find the second vector of our basis, we have to find a generalized eigenvector ${\color{blue}\mathbf{v_2}}$ of $A$ corresponding to $\lambda = -2.$ So, our vectors ${\color{red}\mathbf{v_1}}$ and ${\color{blue}\mathbf{v_2}}$ must form the following chain:

$$


{\color{blue}\mathbf{v_2}} \xrightarrow{A+2I} {\color{red}\mathbf{v_1}} \xrightarrow{A+2I} \mathbf{0}


$$

Therefore, to find ${\color{blue}\mathbf{v}_2}$ we must solve the equation

$$


(A +2I ){\color{blue}\mathbf{v}_2} = {\color{red}\mathbf{v_1}}.


$$

Solving this equation using our usual methods gives us the solution

$$


[\begin{aligned}−1 \\ 0\end{aligned}]


$$

Notice that the set $\left\{{\color{red}\mathbf{v_1}}, {\color{blue}\mathbf{v_2}}\right\}$ is linearly independent and thus forms a basis of $\mathbb{R}^2.$

**Step 3:** Construct the matrices $J$ and $P.$

Now that we have our special basis, we can construct a Jordan canonical form $J$ and invertible matrix $P.$ The matrix $J$ is represented by a single $2 \times 2$ Jordan block:

$$


[\begin{aligned}−2 & 1 \\ 0 & −2\end{aligned}]


$$

Then, the columns of $P$ are the vectors $\color{red}\mathbf{v}_1$ and $\color{blue}\mathbf{v}_2,$ where the first column *must* be the eigenvector ${\color{red}\mathbf{v_1}}.$ So, we get

$$


\begin{aligned}| & | \\ 𝐯_{1} & 𝐯_{2} \\ | & |\end{aligned}


$$

Finally, the Jordan canonical decomposition of $A$ is as follows:

$$


[\begin{aligned}−4 & 4 \\ −1 & 0\end{aligned}]


$$

**Watch out!** In Jordan decomposition, the order in which we write our vectors in the matrix $P$ is important! The first column of $P$ must *always* be the eigenvector.

### Example: Finding Elements of a Jordan Canonical Decomposition for a 2x2 Matrix: The First Column Case

#### Question

$$


[\begin{aligned}8 & 4 \\ −4 & 0\end{aligned}]


$$

Consider the matrices above. Given that $A = P J P^{-1}$ is a Jordan canonical decomposition of $A,$ find the value of $\dfrac{a}{b}.$

#### Explanation

From the Jordan matrix $J,$ we deduce that the eigenvalues of $A$ are

$$


\lambda_1=\lambda_2=4.


$$

As a result, the first column of $P$ corresponds to an eigenvector of the eigenvalue $\lambda=4.$

Now, computing $A-4I,$ we get

$$


\begin{aligned}𝐴−4𝐼 & =[\begin{aligned}8 & 4 \\ −4 & 0\end{aligned}]−(4)[\begin{aligned}1 & 0 \\ 0 & 1\end{aligned}] \\ & =[\begin{aligned}4 & 4 \\ −4 & −4\end{aligned}].\end{aligned}


$$

So, we have a system of linear equations with the augmented matrix $M,$ which we reduce to row echelon form using Gaussian elimination, as follows:

$$


\begin{aligned}𝑀 & =[\begin{aligned}4 & 4 & 0 \\ −4 & −4 & 0\end{aligned}] & 𝑅_{2} & :=𝑅_{2}+𝑅_{1} \\ & ∼[\begin{aligned}4 & 4 & 0 \\ 0 & 0 & 0\end{aligned}] & & \end{aligned}


$$

The reduced matrix above has one pivot column (the $1$st one). Thus, $x_2$ is a free variable. From the first equation, we obtain $x_1=-x_2.$ Hence, the general solution is

$$


[\begin{aligned}−𝑥_{2} \\ 𝑥_{2}\end{aligned}]


$$

Therefore, setting $x_2=1,$ we get the eigenvector

$$


[\begin{aligned}𝑎 \\ 𝑏\end{aligned}]


$$

Finally, $\dfrac{a}{b}=\dfrac{-1}{1} = -1.$

### Example: Finding Elements of a Jordan Canonical Decomposition for a 2x2 Matrix: The Second Column Case

#### Question

$$


[\begin{aligned}9 & 5 \\ −5 & −1\end{aligned}]


$$

Consider the matrices above. Given that $A = P J P^{-1}$ is a Jordan canonical decomposition of $A,$ find the second column of the matrix $P.$

#### Explanation

From the Jordan matrix $J,$ we deduce that the eigenvalues of $A$ are

$$


\lambda_1=\lambda_2=4.


$$

As a result, we obtain that

- the first column of $P$ corresponds to the eigenvector $[\begin{aligned}−1 \\ 1\end{aligned}]$ of the eigenvalue $\lambda=4,$

- the second column of $P$ corresponds to the vector $\mathbf{v}_2$ such that $(A-4I)\mathbf{v}_2 = \mathbf{v}_1.$

Now, computing $A-4I,$ we get

$$


\begin{aligned}𝐴−4𝐼 & =[\begin{aligned}9 & 5 \\ −5 & −1\end{aligned}]−(4)[\begin{aligned}1 & 0 \\ 0 & 1\end{aligned}] \\ & =[\begin{aligned}5 & 5 \\ −5 & −5\end{aligned}].\end{aligned}


$$

So, the matrix equation $(A - 4I)\mathbf{v}_2 = \mathbf{v}_1$ is equivalent to the system of linear equations with the augmented matrix $M$ which we reduce to row echelon form using Gaussian elimination, as follows:

$$


\begin{aligned}𝑀 & =[\begin{aligned}5 & 5 & −1 \\ −5 & −5 & 1\end{aligned}] & 𝑅_{2} & :=𝑅_{2}+𝑅_{1} \\ & ∼[\begin{aligned}5 & 5 & −1 \\ 0 & 0 & 0\end{aligned}] & & \end{aligned}


$$

The reduced matrix above has one pivot column (the $1$st one). Thus, $x_2$ is a free variable. From the first equation, we obtain $x_1=-\dfrac 15 - x_2.$ Hence, the general solution is

$$


\begin{aligned}−\frac{1}{5}−𝑥_{2} \\ 𝑥_{2}\end{aligned}


$$

Therefore, setting $x_2=0,$ we get

$$


[\begin{aligned}𝑎 \\ 𝑏\end{aligned}]


$$
