# Diagonalizing a 3x3 Matrix in the General Case

Source: https://www.mathacademy.com/topics/1971?courseId=154
Topic ID: 1971

## Prerequisites

- [Calculating the Eigenvectors of a 3x3 Matrix in the General Case](./1965-calculating-the-eigenvectors-of-a-3x3-matrix-in-the-general-case.md)
- [Diagonalizing a 3x3 Matrix With Distinct Eigenvalues](./1970-diagonalizing-a-3x3-matrix-with-distinct-eigenvalues.md)

## Lesson

### Introduction

Let's consider the following matrix:

$$


\begin{aligned}1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 0\end{aligned}


$$

This is a $3\times 3$ matrix, yet it has only *two* distinct eigenvalues, namely $\lambda_1 = 0$ and $\lambda_2 = 1.$ Note that $\lambda_1$ is a simple root of the characteristic polynomial and $\lambda_2$ is a double root.

To diagonalize a $3\times 3$ matrix, we need to find a basis of $\mathbb R^3$ consisting of linearly independent eigenvectors of $A.$ So the question is, can we diagonalize this matrix even though it does not have three distinct eigenvalues?

Let's start by computing the eigenvectors of $A\mathbin{:}$

- First, we consider the simple root $\lambda_1 = 0.$ Solving the equation $A \mathbf x = \lambda_1 \mathbf x$ in the usual way, we obtain a single linearly independent eigenvector:

- Next, we consider the double root $\lambda_2 = 1.$ Let's solve the equation $A \mathbf x = \lambda_2 \mathbf x$ by reducing $(A - \lambda_2 I)$ to row-echelon form: There is one pivot column in the reduced matrix above (the $3$rd one). Thus, $x_1$ and $x_2$ are free variables. From the first equation, we obtain the solution $x_3 = 0.$ Therefore, the general solution is where $x_1, x_2\in \mathbb R.$ Thus, we have obtained *two* linearly independent eigenvectors:

So $A$ has three linearly independent eigenvectors that form a basis of $\mathbb R^3.$ Therefore, $A$ is diagonalizable!

In terms of eigenspaces, $A$ is diagonalizable because the sum of the dimensions of the eigenspaces equals the number of rows/columns of $A.$ The eigenspaces corresponding to $\lambda_1 = 0$ and $\lambda_2 = 1$ are given by

$$


\begin{aligned}1 \\ 1 \\ −1\end{aligned}


$$

If we sum the dimensions of $V_0$ and $V_1,$ we get precisely $3\mathbin{:}$

$$


\dim(V_{0}) + \dim(V_{1}) = 1 + 2 = 3 \quad {\color{green}\checkmark}


$$

which means that $A$ is diagonalizable.

It's important to realize that not all matrices are diagonalizable! Let's see an example.

### An Example of a Non-Diagonalizable 3x3 Matrix

Let's now consider the following matrix:

$$


\begin{aligned}1 & 0 & 0 \\ −3 & 2 & 1 \\ −2 & 0 & 2\end{aligned}


$$

Its eigenvalues are $\lambda_1=1$ (simple root) and $\lambda_2=2$ (double root).

Let's see how many linearly independent eigenvectors we can find for this matrix.

- First, we consider the simple root $\lambda_1 = 1.$ Solving the equation $A \mathbf x = \lambda_1 \mathbf x$ in the usual way, we obtain a single linearly independent eigenvector:

- Next, we consider the double root $\lambda_2 = 2.$ Let's solve the equation $A \mathbf x = \lambda_2 \mathbf x$ by reducing $(A - \lambda_2 I)$ to row-echelon form: In the reduced matrix above, there are two pivot columns (the $1$st and the $3$rd). Thus, $x_2$ is a free variable. From the first and second equations, we have Therefore, the general solution is where $x_2\in\mathbb R.$ Thus, we have obtained *only one* linearly independent eigenvector:

So $A$ has *only two* linearly independent eigenvectors, and these cannot form a basis of $\mathbb R^3.$ Therefore, $A$ is *not* diagonalizable.

In terms of eigenspaces, the matrix $A$ is not diagonalizable because the sum of the dimensions of the eigenspaces is *smaller* than the number of rows/columns of $A.$ The eigenspaces corresponding to $\lambda_1 = 1$ and $\lambda_2 = 2$ are given by

$$


\begin{aligned}1 \\ 1 \\ 2\end{aligned}


$$

If we sum the dimensions of $V_1$ and $V_2,$ we get

$$


\dim(V_{1}) + \dim(V_{2}) = 1 + 1 = 2 \neq 3 \quad {\color{red}{\boldsymbol\times}}


$$

which means that $A$ is *not* diagonalizable.

### Determining Whether an NxN Matrix Is Diagonalizable

To check whether diagonalization is possible, we can use the following theorem:

*An $n \times n$ matrix is diagonalizable if and only if the sum of the dimensions of the eigenspaces equals $n$.*

That is, if

$$


\lambda_1, \: \lambda_2, \: \ldots, \: \lambda_k


$$

are the distinct eigenvalues of an $n \times n$ matrix, and the corresponding eigenspaces are

$$


V_{\lambda_1}, \: V_{\lambda_2}, \: \ldots, \: V_{\lambda_k}


$$

then the matrix is diagonalizable if and only if

$$


\dim(V_{\lambda_1}) + \dim(V_{\lambda_2}) + \cdots + \dim(V_{\lambda_k}) = n.


$$

### Example: Finding a Diagonal Matrix Corresponding to a Given Matrix

#### Question

$$


\begin{aligned}4 & 3 & 0 \\ 0 & 1 & 0 \\ 0 & 3 & 4\end{aligned}


$$

If the matrix $A$ above is diagonalizable, find a corresponding diagonal matrix $D.$

#### Explanation

First, we find the eigenvalues of the matrix $A$ by solving $\det(A-\lambda I)=0\mathbin{:}$

$$


\begin{aligned}\begin{matrix}4−𝜆 & 3 & 0 \\ 0 & 1−𝜆 & 0 \\ 0 & 3 & 4−𝜆\end{matrix} & =0 \\ (1−𝜆)\begin{matrix}4−𝜆 & 0 \\ 0 & 4−𝜆\end{matrix} & =0 \\ (1−𝜆)((4−𝜆)(4−𝜆)−0) & =0 \\ (𝜆−1)(𝜆−4)^{2} & =0\end{aligned}


$$

Therefore, the eigenvalues are $\lambda_1=1$ (simple root) and $\lambda_2=4$ (double root).

Let's now find the dimension of the eigenspace corresponding to each eigenvalue.

- First, we consider the simple root $\lambda_1 = 1.$ Since the root is simple, the dimension of the eigenspace $V_{1}$ corresponding to $\lambda_1 = 1$ is

- Next, we consider the double root $\lambda_2 = 4.$ Let's find the dimension of the eigenspace $V_{4}$ corresponding to this eigenvalue. To do this, we row-reduce the matrix $A-4I \mathbin{:}$ In the reduced matrix above, there is one pivot column (the $2$nd one). This implies that we will have $3-1=2$ linearly independent eigenvectors corresponding to $\lambda_2 = 4.$ So,

Therefore, $A$ is diagonalizable, since

$$


\text{dim}(V_{1}) + \text{dim}(V_{4}) = 1+2 = 3. \quad {\color{green}\checkmark}


$$

Finally, a corresponding diagonal matrix is

$$


\begin{aligned}4 & 0 & 0 \\ 0 & 4 & 0 \\ 0 & 0 & 1\end{aligned}


$$

### The Diagonalization Algorithm

A square matrix $A$ is diagonalizable if there exists a diagonal matrix $D$ and an invertible matrix $P$ such that

$$


A = PDP^{-1}.


$$

So, diagonalizing $A$ means finding matrices $D$ and $P$ that satisfy this equation.

For example, let's diagonalize the matrix $A,$ given by

$$


\begin{aligned}−1 & −3 & 6 \\ 0 & 2 & 0 \\ −1 & −1 & 4\end{aligned}


$$

To diagonalize a $3 \times 3$ matrix, we follow a three-step **diagonalization algorithm.**

**Step 1:** Find the eigenvalues of the matrix.

We solve the characteristic equation $\vert A - \lambda I \vert = 0.$ For the given matrix, the eigenvalues are

$$


{\color{red}{\lambda_1}} = {\color{red}{\lambda_2}} = {\color{red}2}\qquad \text{and} \qquad{\color{blue}\lambda_3 =1}.


$$

**Step 2:** Find a basis (if it exists) consisting of eigenvectors of the matrix.

Following the usual method for computing eigenvectors, we get

$$


\begin{aligned}2 \\ 0 \\ 1\end{aligned}


$$

corresponding to the eigenvalues ${\color{red}{\lambda_1}} = {\color{red}{\lambda_2}} = {\color{red}2}$ and ${\color{blue}\lambda_3 =1},$ respectively.

**Watch out!** In this example, the total number of linearly independent eigenvectors equals the number of rows/columns of the matrix. If we obtain fewer eigenvectors at this step, then the matrix is *not* diagonalizable.

**Step 3:** Construct the matrices $D$ and $P.$

Now that we have our eigenvalues and corresponding eigenvectors, we can construct the diagonal matrix $D$ and invertible matrix $P.$

The matrix $D$ has the eigenvalues of the matrix as its entries on the main diagonal. We can write them in any order, so we let

$$


\begin{aligned}2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1\end{aligned}


$$

Then, the columns of $P$ are the corresponding eigenvectors. We must write each eigenvector in the *same* column as its respective eigenvalue in the matrix $D.$ So, we get

$$


\begin{aligned}2 & −1 & 3 \\ 0 & 1 & 0 \\ 1 & 0 & 1\end{aligned}


$$

Finally, we obtain

$$


\begin{aligned}𝐴=𝑃𝐷𝑃^{−1} & =\begin{matrix}2 & −1 & 3 \\ 0 & 1 & 0 \\ 1 & 0 & 1\end{matrix}\begin{matrix}2 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 1\end{matrix}\begin{matrix}2 & −1 & 3 \\ 0 & 1 & 0 \\ 1 & 0 & 1\end{matrix}^{−1}.\end{aligned}


$$

**Note:** When diagonalizing a diagonalizable matrix, we can place the eigenvalues into the matrix $P$ in any order. We just need to be sure that the diagonal entries in the matrix $D$ correspond to the columns of $P.$

For example:

- Swapping the columns $\mathbf{v}_1$ and $\mathbf{v}_2,$ we get another valid diagonalization:

- Swapping the columns $\mathbf{v}_2$ and $\mathbf{v}_3$ above gives another valid diagonalization:

### Example: Diagonalizing a 3x3 Matrix Given Part of the Diagonalization

#### Question

$$


\begin{aligned}−1 & 1 & −2 \\ −2 & −4 & 4 \\ 3 & 3 & −8\end{aligned}


$$

Consider the matrices shown above. Given that $A=PDP^{-1},$ find the value of $\dfrac{a}{b}.$

#### Explanation

Notice that $D=P^{-1}AP$ is a diagonalization of the matrix $A.$

From the diagonal matrix $D,$ we find that the eigenvalues of $A$ are

$\qquad$ $\lambda_1=\lambda_3=-2 \quad$ and $\quad \lambda_2=-9.$

The second column of $P$ corresponds to $\lambda=-2.$ Computing $A-\lambda I,$ we have

$$


\begin{aligned}𝐴−(−2)𝐼 & =\begin{matrix}−1 & 1 & −2 \\ −2 & −4 & 4 \\ 3 & 3 & −8\end{matrix}−(−2)\begin{matrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{matrix} \\ & =\begin{matrix}1 & 1 & −2 \\ −2 & −2 & 4 \\ 3 & 3 & −6\end{matrix}.\end{aligned}


$$

So, we have a system of linear equations with the augmented matrix $M$ which we reduce to row echelon form using Gaussian elimination:

$$


\begin{aligned}𝑀 & =\begin{matrix}1 & 1 & −2 & 0 \\ −2 & −2 & 4 & 0 \\ 3 & 3 & −6 & 0\end{matrix} & & \begin{matrix}𝑅_{2}:=𝑅_{2}+2𝑅_{1} \\ 𝑅_{3}:=𝑅_{3}+(−3)𝑅_{1}\end{matrix} \\ & ∼\begin{matrix}1 & 1 & −2 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0\end{matrix} & & \end{aligned}


$$

In the reduced matrix above, there is one pivot column (the $1$st one). Thus, $x_2$ and $x_3$ are free variables. From the first equation, we obtain

$$


x_1 = -x_2+2x_3.


$$

Therefore, the general solution is

$$


\begin{aligned}−𝑥_{2}+2𝑥_{3} \\ 𝑥_{2} \\ 𝑥_{3}\end{aligned}


$$

Comparing this with the second column of $P,$ we deduce that $x_2=0.$ Now, setting $x_3=1$ and substituting our values for $x_2$ and $x_3$ into the general solution, we obtain the following:

$$


\begin{aligned}2 \\ 0 \\ 1\end{aligned}


$$

Finally, $\dfrac{a}{b}=\dfrac{2}{1}=2.$

### Example: Diagonalizing a 3x3 Matrix

#### Question

$$


\begin{aligned}2 & 2 & 6 \\ −1 & 5 & 3 \\ 1 & −1 & 1\end{aligned}


$$

Consider the matrices shown above. Given that $A=PDP^{-1},$ what is the matrix $P?$

#### Explanation

Notice that $A=PDP^{-1}$ is a diagonalization of the matrix $A.$ So let's apply the diagonalization algorithm to $A.$

**** From the diagonal matrix $D,$ we deduce that the eigenvalues of $A$ are

$\qquad$ $\lambda_1=\lambda_2=4 \quad$ and $\quad \lambda_3=0.$

**** Now, we need to find an eigenvector basis of $A.$

- Consider $\lambda=4.$ Then, So, we have a system of linear equations with the augmented matrix $M$ which we reduce to row echelon form using Gaussian elimination: In the reduced matrix above, there is one pivot column (the $1$st one). Thus, $x_2$ and $x_3$ are free variables. From the first equation, we obtain $x_1=x_2+3x_3.$ Hence, the general solution is As a result, we have two linearly independent eigenvectors $\qquad$ $\begin{aligned}1 \\ 1 \\ 0\end{aligned}$ and $\begin{aligned}3 \\ 0 \\ 1\end{aligned}$

- Consider $\lambda=0.$ Then, Seeking for nonzero solutions of $(A-0I)\mathbf{x}=\mathbf{0},$ we obtain the eigenvector $\qquad$ $\begin{aligned}−2 \\ −1 \\ 1\end{aligned}$

**** We construct the invertible matrix $P$ using our eigenvectors, as follows:

$$


\begin{aligned}−2 & 1 & 3 \\ −1 & 1 & 0 \\ 1 & 0 & 1\end{aligned}


$$
