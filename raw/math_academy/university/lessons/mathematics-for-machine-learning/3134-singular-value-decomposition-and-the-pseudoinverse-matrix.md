# Singular Value Decomposition and the Pseudoinverse Matrix

Source: https://www.mathacademy.com/topics/3134?courseId=145
Topic ID: 3134

## Prerequisites

- [The Least-Squares Solution of a Linear System (With Collinearity)](./2167-the-least-squares-solution-of-a-linear-system-with-collinearity.md)
- [Singular Value Decomposition of Larger Matrices](./3133-singular-value-decomposition-of-larger-matrices.md)

## Lesson

### Introduction

The invertible matrix theorem tells us that if $A$ is an $n \times n$ matrix with full rank (i.e., $\mathrm{rank}(A)=n$), then there exists a unique inverse matrix $A^{-1}$ such that

$$


AA^{-1}=A^{-1}\!A=I_n,


$$

where $I_n$ denotes the $n \times n$ identity matrix.

There are two questions that we can ask:

- Can we extend the notion of an inverse matrix to one that works for $n\times n$ matrices $A$ where $\mathrm{rank}(A) < n?$

- Is it possible to generalize the concept of an inverse to non-square matrices?

The answer to both questions is yes! This generalization of the inverse of $A$ is called the **pseudoinverse** of $A,$ and is denoted $A^+.$ The dimensions of $A^+$ are the same as $A^T.$

As an example, let's consider the ${\color{red}{3}}\times {\color{blue}{2}}$ matrix $A$ and its corresponding pseudoinverse, given below:

$$


\begin{aligned}5 & 0 \\ 0 & 1 \\ 0 & 0\end{aligned}


$$

- Computing $A^{+}\!A,$ we have which is the identity matrix $I_{\color{blue}{2}}.$

- Computing $A\!A^{+},$ we have which is *almost* the identity matrix $I_{\color{red}{3}}.$

We can explain this result using the following properties of the pseudoinverse:

- *If the columns of an $m\times {\color{blue}{n}}$ matrix $A$ are linearly independent, then $A^+A = I_{\color{blue}{n}}.$*

- *If the rows of an ${\color{red}{m}}\times n$ matrix $A$ are linearly independent, then $AA^+ = I_{\color{red}{m}}.$*

In the example above, the columns of $A$ are linearly independent, but the rows are not.

Moreover, the notion of a pseudoinverse is consistent with inverse matrices. In particular,

*If $A$ is an invertible square matrix, then $A^{+} = A^{-1}.$*

This lesson will discuss how to compute the pseudoinverse for any matrix, starting with an important special case.

### The Pseudoinverse of an Almost Diagonal Matrix

For an *almost* zero ${\color{red}{m}}\times {\color{blue}{n}}$ matrix with non-zero entries

$$


\sigma_1, \: \sigma_2, \: \ldots, \: \sigma_r


$$

on the main diagonal only, the corresponding pseudoinverse is the *almost* zero ${\color{blue}{n}}\times {\color{red}{m}}$ matrix with non-zero entries

$$


{\sigma_1^{-1}}, \, {\sigma_2^{-1}}, \, \ldots, \, {\sigma_r^{-1}}


$$

on the main diagonal only.

For example, for the matrix $A,$ given by

$$


[\begin{aligned}3 & 0 & 0 \\ 0 & 4 & 0\end{aligned}]


$$

we calculate its pseudoinverse as follows:

- **Step 1:** Replace the non-zero elements on the main diagonal with their multiplicative inverses.

- **Step 2:** Transpose the resulting matrix.

$$


\begin{aligned}𝐴^{+} & =[\begin{matrix}3 & 0 & 0 \\ 0 & 4 & 0\end{matrix}]^{+} \\ & =\begin{matrix}3^{−1} & 0 \\ 0 & 4^{−1} \\ 0 & 0\end{matrix} \\ & =\begin{matrix}1/3 & 0 \\ 0 & 1/4 \\ 0 & 0\end{matrix} \\ & =\frac{1}{12}\begin{matrix}4 & 0 \\ 0 & 3 \\ 0 & 0\end{matrix}\end{aligned}


$$

### Example: Finding the Pseudoinverse of a Diagonal Matrix

#### Question

For the matrix $\begin{aligned}6 & 0 \\ 0 & 4 \\ 0 & 0\end{aligned}$ find the pseudoinverse $A^+.$

#### Explanation

For an "almost" zero $m \times n$ matrix with non-zero entries

$$


\sigma_1, \: \sigma_2, \: \ldots, \: \sigma_r


$$

on the main diagonal, the corresponding pseudoinverse is the "almost" zero $n \times m$ matrix with entries

$$


{\sigma_1^{-1}}, \, {\sigma_2^{-1}}, \, \ldots, \, {\sigma_r^{-1}}


$$

on the main diagonal.

Therefore, we obtain

$$


\begin{aligned}𝐴^{+} & =\begin{matrix}6 & 0 \\ 0 & 4 \\ 0 & 0\end{matrix}^{+} \\ & =[\begin{matrix}6^{−1} & \,\,\,0 & 0 \\ \,\,0 & \,4^{−1} & 0\end{matrix}] \\ & =\frac{1}{12}[\begin{matrix}2 & 0 & 0 \\ 0 & 3 & 0\end{matrix}].\end{aligned}


$$

### Finding the Pseudoinverse Using Singular Value Decomposition

There are many ways to find the pseudoinverse of a given matrix $A.$ One way is to use the singular value decomposition of $A{:}$

Specifically, if

$$


A=U \Sigma V ^T


$$

is a singular value decomposition of $A,$ then the pseudoinverse of $A$ is given by

$$


A^+ = V \, \Sigma^+ \, U^T,


$$

where $\Sigma^+$ is the pseudoinverse of $\Sigma.$

### Example: Finding the Pseudoinverse of a Matrix Given Its Singular Value Decomposition

#### Question

$$


\begin{aligned}\frac{4}{5} & −\frac{3}{5} & 0 \\ \frac{3}{5} & \frac{4}{5} & 0 \\ 0 & 0 & 1\end{aligned}


$$

Consider the matrices shown above. Given that $A=U \Sigma V^T$ is a singular value decomposition of $A,$ find the pseudoinverse $A^+.$

#### Explanation

If $A=U \Sigma V ^T$ is a singular value decomposition of $A,$ then the pseudoinverse of $A$ is given by

$$


V \, \Sigma^+ \, U^T,


$$

where $\Sigma^+$ is the pseudoinverse of $\Sigma.$

First, notice that

$$


[\begin{aligned}1 & 0 \\ 0 & 1\end{aligned}]


$$

Therefore, we have

$$


\begin{aligned}𝐴^{+} & =𝑉\,Σ^{+}\,𝑈^{𝑇} \\ & =[\begin{matrix}1 & 0 \\ 0 & 1\end{matrix}]⋅\frac{1}{5}[\begin{matrix}1 & 0 & 0 \\ 0 & 0 & 0\end{matrix}]⋅\frac{1}{5}\begin{matrix}4 & 3 & 0 \\ −3 & 4 & 0 \\ 0 & 0 & 5\end{matrix} \\ & =\frac{1}{25}[\begin{matrix}1 & 0 \\ 0 & 1\end{matrix}]⋅[\begin{matrix}1 & 0 & 0 \\ 0 & 0 & 0\end{matrix}]⋅\begin{matrix}4 & 3 & 0 \\ −3 & 4 & 0 \\ 0 & 0 & 5\end{matrix} \\ & =\frac{1}{25}[\begin{matrix}1 & 0 & 0 \\ 0 & 0 & 0\end{matrix}]⋅\begin{matrix}4 & 3 & 0 \\ −3 & 4 & 0 \\ 0 & 0 & 5\end{matrix} \\ & =\frac{1}{25}[\begin{matrix}4 & 3 & 0 \\ 0 & 0 & 0\end{matrix}].\end{aligned}


$$

### Reduced Singular Value Decomposition

Consider the matrix

$$


\begin{aligned}4 & 0 \\ 3 & 0 \\ 0 & 2\end{aligned}


$$

and its singular value decomposition $A=U \Sigma V ^T,$ where

$$


\begin{aligned}\frac{4}{5} & 0 & −\frac{3}{5} \\ \frac{3}{5} & 0 & \frac{4}{5} \\ 0 & 1 & 0\end{aligned}


$$

Notice that $\Sigma$ contains a row of zeros. In these situations, it's possible to simplify the decomposition of $A.$ This simplified decomposition is called the **reduced singular value decomposition** of $A.$

First, we note that $A$ is a $3 \times 2$ matrix. In addition, the matrix $\Sigma$ has two non-zero singular values on its main diagonal, so the rank of $A$ is $\color{blue}r=2.$

To find our reduced SVD, we proceed as follows:

- First, we remove all zero rows and columns from $\Sigma.$ In our example, we should delete the $3$rd row since it contains only zeros. Notice that we obtain a square invertible matrix of rank ${\color{blue}2}{:}$

- Next, we remove all extra columns of $U$ starting from the right, keeping only $\color{blue}2$ columns. In our example, we should delete the $3$rd column:

- Finally, we remove all extra columns of $V$ starting from the right, keeping only $\color{blue}2$ columns. In our example, we should keep $V$ as it is since it already has only $2$ columns:

The reduced singular value decomposition of $A$ is then given by

$$


A = U_r \Sigma_r V_r^T.


$$

So, in our example, we have

$$


\begin{aligned}\frac{4}{5} & 0 \\ \frac{3}{5} & 0 \\ 0 & 1\end{aligned}


$$

In general, a singular value decomposition

$$


A=U \Sigma V^T


$$

of an $m \times n$ matrix $A$ is not unique. However, we can always simplify it to the corresponding reduced singular value decomposition

$$


A=U_r \Sigma_r V_r^T


$$

with the following properties:

- $\Sigma_r$ is a square diagonal matrix of size $r\times r,$ where $r\leq \min\{m,n\}$ is the rank of $A.$ The main diagonal of $\Sigma_r$ contains the non-zero singular values $\sigma_1, \sigma_2, \ldots, \sigma_r$ of $A$ in descending order.

- $U_r$ is a $m\times r$ matrix obtained by keeping only the first $r$ columns of $U.$

- $V_r$ is a $n \times r$ matrix obtained by keeping only the first $r$ columns of $V.$

### Example: Finding the Pseudoinverse of a Matrix Given Its Reduced Singular Value Decomposition

#### Question

$$


\begin{aligned}\frac{3}{5} \\ \frac{4}{5} \\ 0\end{aligned}


$$

Consider the matrices shown above. Given that $A=U_r \Sigma_r V_r^T$ is a reduced singular value decomposition of $A,$ find the pseudoinverse $A^+.$

#### Explanation

If $A=U_r \Sigma_r V_r ^T$ is a reduced singular value decomposition of $A,$ then the pseudoinverse of $A$ is given by

$$


V_r \, \Sigma_r^+ \, U_r^T,


$$

where $\Sigma_r^+$ is the pseudoinverse of $\Sigma_r.$

First, notice that

$$


[\begin{aligned}4 \\ 3\end{aligned}]


$$

Therefore, we have

$$


\begin{aligned}𝐴^{+} & =𝑉_{𝑟}\,Σ_{+𝑟}\,𝑈_{𝑇𝑟} \\ & =\frac{1}{5}[\begin{matrix}4 \\ 3\end{matrix}]⋅\frac{1}{2}[\begin{matrix}1\end{matrix}]⋅\frac{1}{5}[\begin{matrix}3 & 4 & 0\end{matrix}] \\ & =\frac{1}{50}[\begin{matrix}4 \\ 3\end{matrix}]⋅[\begin{matrix}1\end{matrix}]⋅[\begin{matrix}3 & 4 & 0\end{matrix}] \\ & =\frac{1}{50}[\begin{matrix}4 \\ 3\end{matrix}]⋅[\begin{matrix}3 & 4 & 0\end{matrix}] \\ & =\frac{1}{50}[\begin{matrix}12 & 16 & 0 \\ 9 & 12 & 0\end{matrix}].\end{aligned}


$$

### The Optimal Least-Squares Solution

Recall that the least-squares solution of the system

$$


A\mathbf x=\mathbf{b},


$$

is a vector ${\hat{\mathbf{x}}}$ such that $\| A{\hat{\mathbf{x}}} - \mathbf{b} \|$ is minimized.

The least-squares solution is not unique when $A$ has linearly dependent columns. However, it can be shown that a so-called **optimal least-squares solution** $\mathbf{x^\ast}$ always exists. The optimal least-squares solution is the solution to the least squares problem with the shortest possible length.

It turns out that the optimal least-squares solution can be found using the pseudoinverse of $A,$ as follows:

$$


\mathbf{x^\ast} = A^{+} \mathbf{b}


$$
