# Block Diagonalization of NxN Matrices

Source: https://www.mathacademy.com/topics/2019?courseId=55
Topic ID: 2019

## Prerequisites

- [Partitioned and Block Matrices](./1735-partitioned-and-block-matrices.md)
- [Diagonalizing a 3x3 Matrix in the General Case](./1971-diagonalizing-a-3x3-matrix-in-the-general-case.md)
- [Reducing Real 2x2 Matrices to Rotation-Scaling Form](./2018-reducing-real-2x2-matrices-to-rotation-scaling-form.md)

## Lesson

### Introduction

A square matrix $A$ is **block diagonalizable** if it is similar to a block diagonal matrix $B.$ That is, there exists a block diagonal matrix $B$ and an invertible matrix $P$ such that

$$


A=PBP^{-1}.


$$

For example, the matrix

$$


\begin{aligned}2 & 0 & 0 \\ −2 & 3 & 2 \\ −1 & −2 & 3\end{aligned}


$$

is block diagonalizable because it can be factored as follows:

$$


\begin{aligned}2 & 0 & 0 \\ −2 & 3 & 2 \\ −1 & −2 & 3\end{aligned}


$$

Here, the matrix $A$ has eigenvalues

$$


{\color{red}\lambda_1 = 2},\qquad {\color{blue}\lambda_2=3-2\textrm i},\qquad {\color{blue}\lambda_3=3+2\textrm i}.


$$

Notice that $\lambda_2 = \overline{\lambda_3}.$ The eigenvectors of ${\color{red}\lambda_1}, {\color{blue}\lambda_2},$ and ${\color{blue}\lambda_3},$ respectively, are

$$


\begin{aligned}1 \\ 0 \\ 1\end{aligned}


$$

Again, notice that $\mathbf{v}_2 = \overline{\mathbf{v}_3}.$ The first column of $P$ corresponds to the eigenvector ${\color{red}\mathbf{v}_1},$ and the second and third columns correspond to the real and the imaginary parts of ${\color{blue}\mathbf{v}_2}.$

### The Block Diagonalization Theorem for a 3x3 Matrix

We have the following theorem regarding the block diagonalization of a real $3\!\times\! 3$ matrix:

*If $A$ is a real $3\times 3$ matrix with one real eigenvalue ${\color{red}\lambda_1}$ with corresponding eigenvector ${\color{red}{\mathbf{v}_1}},$ and two complex eigenvalues ${\color{blue}\lambda_2} = \overline{\color{blue}\lambda}_{\color{blue}3}$ with corresponding eigenvectors ${\color{blue}\mathbf{v}_2} = \overline{\color{blue}\mathbf{v}}_{\color{blue}3},$ then*

$$


A=PBP^{-1},


$$

*where the matrices $B$ and $P$ are given by*

$$


\begin{aligned}𝜆_{1} & 0 & 0 \\ 0 & Re(𝜆_{2}) & Im(𝜆_{2}) \\ 0 & −Im(𝜆_{2}) & Re(𝜆_{2})\end{aligned}


$$

In other words, if $A$ is a real $3\!\times\! 3$ matrix with one real eigenvalue and two complex eigenvalues, then $A$ is block diagonalizable.

Note the following:

- The block of $B$ constructed from the real and imaginary parts of $\color{blue}\lambda_2$ is a rotation-scaling matrix.

- We can write the blocks of $B$ in either order. However, the order of the columns of $P$ *must* correspond to the order of the blocks.

### Example: Finding the Eigenvalues and Corresponding Eigenvectors of a Matrix in Block Diagonal Form

#### Question

$$


\begin{aligned}4 & −1 & 1 \\ 1 & 1 & 3 \\ 1 & 2 & 1\end{aligned}


$$

Consider the nonsingular matrix $P$ and the block diagonal matrix $B$ shown above, where the $2 \times 2$ block of $B$ is a rotation-scaling matrix. Given that $A=PBP^{-1},$ what are the complex (not real) eigenvalues and the corresponding eigenvectors of $A?$

#### Explanation

Recall that if $A$ is a $3\times 3$ real matrix that has one real eigenvalue ${\color{red}\lambda_1}$ with corresponding eigenvector ${\color{red}{\mathbf{v}_1}},$ and two complex eigenvalues ${\color{blue}\lambda_2} = \overline{\color{blue}\lambda}_{\color{blue}3}$ with corresponding eigenvectors ${\color{blue}\mathbf{v}_2} = \overline{\color{blue}\mathbf{v}}_{\color{blue}3},$ then $A=PBP^{-1},$ where

$$


\begin{aligned}𝜆_{1} & 0 & 0 \\ 0 & Re(𝜆_{2}) & Im(𝜆_{2}) \\ 0 & −Im(𝜆_{2}) & Re(𝜆_{2})\end{aligned}


$$

Notice that swapping the blocks on the main diagonal of $B$ will result in switching the corresponding columns in $P.$

- From our block diagonal matrix we deduce the complex eigenvalues are ${\color{blue}\lambda_{1,2}=1 \pm 3\text{i}}$ and the real eigenvalue is ${\color{red}\lambda_3=-3}.$

- From our matrix we deduce that the complex and real eigenvectors are

### Example: Finding a Block Diagonalization of a 3x3 Matrix

#### Question

$$


\begin{aligned}−2 & 0 & 1 \\ 3 & −1 & 5 \\ −1 & 0 & −2\end{aligned}


$$

Consider the matrix $A$ shown above. Find a block diagonal matrix $B,$ where the $2 \times 2$ block represents a rotation-scaling matrix, such that $A=PBP^{-1}.$

#### Explanation

Recall that if $A$ is a real $3\times 3$ matrix that has one real eigenvalue ${\color{red}\lambda_1}$ with corresponding eigenvector ${\color{red}{\mathbf{v}_1}},$ and two complex eigenvalues ${\color{blue}\lambda_2} = \overline{\color{blue}\lambda}_{\color{blue}3}$ with corresponding eigenvectors ${\color{blue}\mathbf{v}_2} = \overline{\color{blue}\mathbf{v}}_{\color{blue}3},$ then $A=PBP^{-1},$ where

$$


\begin{aligned}𝜆_{1} & 0 & 0 \\ 0 & Re(𝜆_{2}) & Im(𝜆_{2}) \\ 0 & −Im(𝜆_{2}) & Re(𝜆_{2})\end{aligned}


$$

Swapping the blocks on the main diagonal of $B$ will result in switching the corresponding columns in $P.$

To compute the eigenvalues of $A,$ we solve the characteristic equation as follows:

$$


\begin{aligned}det(𝐴−𝜆𝐼) & =0 \\ \begin{matrix}−2−𝜆 & 0 & 1 \\ 3 & −1−𝜆 & 5 \\ −1 & 0 & −2−𝜆\end{matrix} & =0 \\ (−1−𝜆)((−2−𝜆)^{2}−1(−1)) & =0 \\ (−1−𝜆)(𝜆^{2}+4𝜆+5) & =0\end{aligned}


$$

So, the real eigenvalue is $\lambda_1={\color{red}-1}.$ Now, using the quadratic formula, we get

$$


\begin{aligned}𝜆_{2,3} & =\frac{−4±\sqrt{(4)^{2}−4⋅1⋅5}}{2} \\ & =\frac{−4±\sqrt{−4}}{2} \\ & =\frac{−4±2i}{2} \\ & =−2±i.\end{aligned}


$$

Therefore, the block diagonal matrix is

$$


\begin{aligned}−1 & 0 & 0 \\ 0 & −2 & 1 \\ 0 & −1 & −2\end{aligned}


$$

### Example: Calculating the Invertible Matrix in Block Diagonal Form of a 3x3 Matrix

#### Question

Consider the vectors $\mathbf{v}_1$ and $\mathbf{v}_2$ and the block diagonal matrix $B$ shown below, where the $2 \times 2$ block of $B$ represents a rotation-scaling matrix:

$$


\begin{aligned}2 \\ −1 \\ 5\end{aligned}


$$

The vectors $\mathbf{v}_1$ and $\mathbf{v}_2$ are the eigenvectors of a matrix $A$ corresponding to the eigenvalues $\lambda_1=2$ and $\lambda_2=1-\text{i},$ respectively. Given that $A=PBP^{-1},$ find the matrix $P.$

#### Explanation

Recall that if $A$ is a real $3\times 3$ matrix that has one real eigenvalue ${\color{red}\lambda_1}$ with corresponding eigenvector ${\color{red}{\mathbf{v}_1}},$ and two complex eigenvalues ${\color{blue}\lambda_2} = \overline{\color{blue}\lambda}_{\color{blue}3}$ with corresponding eigenvectors ${\color{blue}\mathbf{v}_2} = \overline{\color{blue}\mathbf{v}}_{\color{blue}3},$ then $A=PBP^{-1},$ where

$$


\begin{aligned}𝜆_{1} & 0 & 0 \\ 0 & Re(𝜆_{2}) & Im(𝜆_{2}) \\ 0 & −Im(𝜆_{2}) & Re(𝜆_{2})\end{aligned}


$$

Swapping the blocks on the main diagonal of $B$ will result in switching the corresponding columns in $P.$

From our block diagonal matrix

$$


\begin{aligned}2 & 0 & 0 \\ 0 & 1 & −1 \\ 0 & 1 & 1\end{aligned}


$$

we deduce that the first column of $P$ will correspond to the real eigenvector ${{\color{red}{\mathbf{v}_1}}},$ and the second and third columns of $P$ will correspond to the complex eigenvector ${\color{blue}\mathbf{v}_2}.$ Therefore,

$$


\begin{aligned}2 & 7 & −2 \\ −1 & 0 & −3 \\ 5 & −2 & −1\end{aligned}


$$

### Generalization of Block Diagonalization to NxN Matrices

We can find a block diagonalization for any real $n\!\times\! n$ matrix $A.$ This means that for any square matrix $A,$ we can construct a block diagonal matrix $B$ and invertible matrix $P$ such that

$$


A=PBP^{-1},


$$

where the blocks of $B$ are either:

- $1\!\times\! 1$ blocks containing the real eigenvalues of $A,$ or

- $2\!\times\! 2$ blocks containing the rotation-scaling matrices corresponding to the complex (not real) eigenvalues of $A.$

The columns of $P$ form bases of the eigenspaces for the real eigenvectors, or come in the pairs $\left(\text{Re}(\mathbf{v}), \text{Im}(\mathbf{v})\right)$ for the non-real eigenvectors.

Let's see an example of block diagonalization for higher-dimensional matrices.

### Example: Calculating the Invertible Matrix in Block Diagonal Form of an NxN Matrix

#### Question

Consider the vectors $\mathbf{v}_1$ and $\mathbf{v}_3$ and the block diagonal matrix $B$ shown below, where both $2 \times 2$ blocks of $B$ represent rotation-scaling matrices:

$$


\begin{aligned}−3+2i \\ −1+3i \\ 4+i \\ −i\end{aligned}


$$

The vectors $\mathbf{v}_1$ and $\mathbf{v}_3$ are the eigenvectors of a matrix $A$ corresponding to the eigenvalues $\lambda_1=7 + 4\text{i}$ and $\lambda_3=-3 + 2\text{i},$ respectively. Given that $A=PBP^{-1},$ find a possible matrix $P.$

#### Explanation

Recall that if $A$ is a $4\times 4$ real matrix that has complex eigenvalues

$\qquad$ ${\color{red}\lambda_1}=\overline{\color{red}\lambda}_{\color{red}2} \quad$ and $\quad {\color{blue}\lambda_3}=\overline{\color{blue}\lambda}_{\color{blue}4}$

with corresponding eigenvectors

$\qquad$ ${\color{red}\mathbf{v}_1} = \overline{\color{red}\mathbf{v}}_{\color{red}2} \quad$ and $\quad {\color{blue}\mathbf{v}_3} = \overline{\color{blue}\mathbf{v}}_{\color{blue}4},$

then $A=PBP^{-1},$ where

$$


\begin{aligned}Re(𝜆_{1}) & Im(𝜆_{1}) & 0 & 0 \\ −Im(𝜆_{1}) & Re(𝜆_{1}) & 0 & 0 \\ 0 & 0 & Re(𝜆_{3}) & Im(𝜆_{3}) \\ 0 & 0 & −Im(𝜆_{3}) & Re(𝜆_{3})\end{aligned}


$$

and

$$


\begin{aligned}| & | & | & | \\ Re(𝐯_{1}) & Im(𝐯_{1}) & Re(𝐯_{3}) & Im(𝐯_{3}) \\ | & | & | & |\end{aligned}


$$

Swapping the blocks on the main diagonal of $B$ will result in switching the corresponding columns in $P.$

From our block diagonal matrix

$$


\begin{aligned}7 & 4 & 0 & 0 \\ −4 & 7 & 0 & 0 \\ 0 & 0 & −3 & 2 \\ 0 & 0 & −2 & −3\end{aligned}


$$

we deduce that the first and second columns of $P$ will correspond to the complex eigenvector ${\color{red}{\mathbf{v}_1}},$ and the third and forth columns of $P$ will correspond to the complex eigenvector ${\color{blue}\mathbf{v}_3}.$ Therefore,

$$


\begin{aligned}−3 & 2 & 0 & 1 \\ −1 & 3 & 7 & 0 \\ 4 & 1 & 1 & −2 \\ 0 & −1 & 1 & −1\end{aligned}


$$
