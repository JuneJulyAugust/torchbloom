# Jordan Canonical Form of a 3x3 Matrix

Source: https://www.mathacademy.com/topics/3115?courseId=55
Topic ID: 3115

## Prerequisites

- [Diagonalizing a 3x3 Matrix in the General Case](./1971-diagonalizing-a-3x3-matrix-in-the-general-case.md)
- [Jordan Canonical Decomposition of a 2x2 Matrix](./3652-jordan-canonical-decomposition-of-a-2x2-matrix.md)

## Lesson

### Introduction

Let's now consider Jordan canonical forms of $3 \times 3$ matrices.

Let $A$ be a $3\times 3$ matrix. The simplest case is when $A$ has three distinct eigenvalues, say $\lambda_1, \lambda_2,$ and $\lambda_3.$ In this case, $A$ must be diagonalizable. Therefore, the Jordan canonical form of $A$ is

$$


\begin{aligned}𝜆_{1} & 0 & 0 \\ 0 & 𝜆_{2} & 0 \\ 0 & 0 & 𝜆_{3}\end{aligned}


$$

For example, consider the matrix

$$


\begin{aligned}7 & 1 & −4 \\ 8 & 0 & 2 \\ 4 & −4 & 9\end{aligned}


$$

This matrix has eigenvalues $\lambda_1=8,$ $\lambda_2=5,$ and $\lambda_3=3.$ Therefore, its Jordan canonical form is

$$


\begin{aligned}8 & 0 & 0 \\ 0 & 5 & 0 \\ 0 & 0 & 3\end{aligned}


$$

Remember that a Jordan canonical form of a matrix is unique up to the order of the Jordan blocks.

### Example: Finding a Jordan Canonical Form of a 3x3 Matrix With Three Distinct Eigenvalues

#### Question

$$


\begin{aligned}8 & 2 & 1 \\ 8 & 8 & 8 \\ −4 & −2 & 3\end{aligned}


$$

The matrix above has eigenvalues $\lambda_1=8,$ $\lambda_2=7,$ and $\lambda_3=4.$ Find a Jordan canonical form of the matrix.

#### Explanation

Notice that we are given a $3 \times 3$ matrix that has precisely $3$ distinct eigenvalues.

Therefore, $A$ is diagonalizable, and its Jordan canonical form is

$$


\begin{aligned}8 & 0 & 0 \\ 0 & 7 & 0 \\ 0 & 0 & 4\end{aligned}


$$

A Jordan canonical form is unique up to the order of the Jordan blocks. So, another Jordan canonical form of $A$ is

$$


\begin{aligned}4 & 0 & 0 \\ 0 & 7 & 0 \\ 0 & 0 & 8\end{aligned}


$$

### Jordan Canonical Forms of 3x3 Matrices That Have Two Distinct Eigenvalues

Let's now consider the matrix $A,$ given by

$$


\begin{aligned}4 & 3 & 1 \\ 1 & 6 & 1 \\ 6 & −7 & 9\end{aligned}


$$

The characteristic equation of $A$ is given by

$$


(\lambda-8)^2(\lambda - 3) = 0.


$$

Therefore, this matrix has only two distinct eigenvalues, namely,

- $\lambda=8$ of algebraic multiplicity $2,$ and

- $\lambda=3$ of algebraic multiplicity $1.$

How can we find its Jordan canonical form?

In this example, we have one $1 \times 1$ Jordan block $J_1(3)$ corresponding to $\lambda=3.$ However, there are two possibilities for the Jordan blocks corresponding to $\lambda=8{:}$

- *Case I.* We may get the single $2 \times 2$ Jordan block $J_2(8).$ This happens when the generalized eigenvectors $\mathbf v_1$ and $\mathbf v_2$ corresponding to the eigenvalue $\lambda=8$ form the following chain:

- *Case II.* We may get a composition of two $1 \times 1$ Jordan blocks, namely $J_1(8) {\:\oplus\:} J_1(8).$ This happens when the generalized eigenvectors $\mathbf v_1$ and $\mathbf v_2$ corresponding to the eigenvalue $\lambda=8$ form the following chains:

To figure out which of the cases we obtain in this situation, let's find the number of linearly independent eigenvectors corresponding to $\lambda=8.$

Computing $A-8I,$ we get

$$


\begin{aligned}𝐴−8𝐼 & =\begin{aligned}4 & 3 & 1 \\ 1 & 6 & 1 \\ 6 & −7 & 9\end{aligned}−8\begin{aligned}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{aligned}=\begin{aligned}−4 & 3 & 1 \\ 1 & −2 & 1 \\ 6 & −7 & 1\end{aligned}.\end{aligned}


$$

Now, we reduce this matrix to row echelon form using Gaussian elimination, as follows:

$$


\begin{aligned}𝐴−8𝐼 & =\begin{aligned}−4 & 3 & 1 \\ 1 & −2 & 1 \\ 6 & −7 & 1\end{aligned} & & \begin{aligned}𝑅_{1}↔𝑅_{2}\end{aligned} \\ & ∼\begin{aligned}1 & −2 & 1 \\ −4 & 3 & 1 \\ 6 & −7 & 1\end{aligned} & & \begin{aligned}𝑅_{2}:=𝑅_{2}+4𝑅_{1} \\ 𝑅_{3}:=𝑅_{3}+(−6)𝑅_{1}\end{aligned} \\ & ∼\begin{aligned}1 & −2 & 1 \\ 0 & −5 & 5 \\ 0 & 5 & −5\end{aligned} & & \begin{aligned}𝑅_{3}:=𝑅_{3}+𝑅_{2}\end{aligned} \\ & ∼\begin{aligned}1 & −2 & 1 \\ 0 & −5 & 5 \\ 0 & 0 & 0\end{aligned} & & \end{aligned}


$$

Since $\text{nullity}(A-8I)=1,$ there will be only one eigenvector that corresponds to the eigenvalue $\lambda=8,$ say, $\mathbf{v}_1.$ So, the generalized eigenvectors corresponding to the eigenvalue $\lambda=8$ form the following chain:

$$


\mathbf{v}_2 \xrightarrow{A-8I} \mathbf{v}_1 \xrightarrow{A-8I} \mathbf{0}


$$

Therefore, we have *case I*, and $A$ has the following Jordan canonical form:

$$


\begin{aligned}8 & 1 & 0 \\ 0 & 8 & 0 \\ 0 & 0 & 3\end{aligned}


$$

As always, the Jordan canonical form is unique up to the order of the Jordan blocks.

### Example: Finding a Jordan Canonical Form of a 3x3 Matrix With Two Distinct Eigenvalues

#### Question

$$


\begin{aligned}3 & 8 & 8 \\ 4 & 7 & 8 \\ −4 & −8 & −9\end{aligned}


$$

The matrix above has eigenvalues $\lambda_1=\lambda_2=-1,$ and $\lambda_3=3.$ Find a Jordan canonical form of the matrix.

#### Explanation

Notice that we are given a $3 \times 3$ matrix with the following eigenvalues:

- $\lambda=-1$ of algebraic multiplicity $2$

- $\lambda=3$ of algebraic multiplicity $1$

As a result, we have one $1 \times 1$ Jordan block $J_1(3)$ corresponding to $\lambda=3.$ However, there are two possibilities for the Jordan blocks corresponding to $\lambda=-1{:}$

- ** We may get the single $2 \times 2$ Jordan block $J_2(-1).$ This happens when the generalized eigenvectors $\mathbf v_1$ and $\mathbf v_2$ corresponding to the eigenvalue $\lambda=-1$ form the following chain:

- ** We may get a composition of two $1 \times 1$ Jordan blocks, namely $J_1(-1) {\:\oplus\:} J_1(-1).$ This happens when the generalized eigenvectors $\mathbf v_1$ and $\mathbf v_2$ corresponding to the eigenvalue $\lambda=-1$ form the following chains:

To figure out which of the cases we obtain in this situation, let's find the number of linearly independent eigenvectors corresponding to $\lambda=-1.$

Computing $A+I,$ we get

$$


\begin{aligned}𝐴+𝐼 & =\begin{aligned}3 & 8 & 8 \\ 4 & 7 & 8 \\ −4 & −8 & −9\end{aligned}+\begin{aligned}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{aligned}=\begin{aligned}4 & 8 & 8 \\ 4 & 8 & 8 \\ −4 & −8 & −8\end{aligned}.\end{aligned}


$$

Now, we reduce this matrix to row echelon form using Gaussian elimination, as follows:

$$


\begin{aligned}𝐴+𝐼 & =\begin{aligned}4 & 8 & 8 \\ 4 & 8 & 8 \\ −4 & −8 & −8\end{aligned} & & \begin{aligned}𝑅_{2}:=𝑅_{2}+(−1)𝑅_{1}\end{aligned} \\ & ∼\begin{aligned}4 & 8 & 8 \\ 0 & 0 & 0 \\ −4 & −8 & −8\end{aligned} & & \begin{aligned}𝑅_{3}:=𝑅_{3}+𝑅_{1}\end{aligned} \\ & ∼\begin{aligned}4 & 8 & 8 \\ 0 & 0 & 0 \\ 0 & 0 & 0\end{aligned} & & \end{aligned}


$$

Since $\text{nullity}(A+I)=2,$ there will be two eigenvectors that correspond to the eigenvalue $\lambda=-1,$ say, $\mathbf{v}_1$ and $\mathbf{v}_2.$ So, the generalized eigenvectors corresponding to the eigenvalue $\lambda=-1$ form the following chains:

$$


\mathbf{v}_1 \xrightarrow{A+I} \mathbf{0} \\[5pt] \mathbf{v}_2 \xrightarrow{A+I} \mathbf{0}


$$

Therefore, we have **, and $A$ has the following Jordan canonical form:

$$


\begin{aligned}3 & 0 & 0 \\ 0 & −1 & 0 \\ 0 & 0 & −1\end{aligned}


$$

**** The Jordan canonical form is unique up to the order of the Jordan blocks.

### Jordan Canonical Forms of 3x3 Matrices That Have Only One Eigenvalue

Now, suppose we are given a non-scalar $3 \times 3$ matrix that has only one eigenvalue $\lambda$ of algebraic multiplicity $3.$

Then, there are two possibilities for the Jordan blocks corresponding to $\lambda{:}$

- *Case I.* We may have the single $3 \times 3$ Jordan block $J_3(\lambda).$ This happens when the generalized eigenvectors $\mathbf v_1, \mathbf v_2$ and $\mathbf v_3$ corresponding to $\lambda$ form the following chain:

- *Case II.* We may have a composition of one $2 \times 2$ and one $1 \times 1$ Jordan block, say $J_2(\lambda) {\:\oplus\:} J_1(\lambda).$ This happens when the generalized eigenvectors $\mathbf v_1, \mathbf v_2$ and $\mathbf v_3$ corresponding to $\lambda$ form the following chains:

To illustrate this situation, let's consider the matrix

$$


\begin{aligned}2 & −3 & 3 \\ 1 & −2 & 1 \\ −2 & 2 & −3\end{aligned}


$$

which has eigenvalues $\lambda_1=\lambda_2=\lambda_3=-1.$

To determine which of the above cases applies to this example, we now find the number of linearly independent eigenvectors corresponding to $\lambda=-1.$

Computing $A-(-1)I=A+I,$ we get

$$


\begin{aligned}𝐴+𝐼 & =\begin{aligned}2 & −3 & 3 \\ 1 & −2 & 1 \\ −2 & 2 & −3\end{aligned}+\begin{aligned}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{aligned}=\begin{aligned}3 & −3 & 3 \\ 1 & −1 & 1 \\ −2 & 2 & −2\end{aligned}.\end{aligned}


$$

Now, we reduce this matrix to row echelon form using Gaussian elimination, as follows:

$$


\begin{aligned}𝐴+𝐼 & =\begin{aligned}3 & −3 & 3 \\ 1 & −1 & 1 \\ −2 & 2 & −2\end{aligned} & & \begin{aligned}𝑅_{1}↔𝑅_{2}\end{aligned} \\ & ∼\begin{aligned}1 & −1 & 1 \\ 3 & −3 & 3 \\ −2 & 2 & −2\end{aligned} & & \begin{aligned}𝑅_{2}:=𝑅_{2}+(−3)𝑅_{1} \\ 𝑅_{3}:=𝑅_{3}+2𝑅_{1}\end{aligned} \\ & ∼\begin{aligned}1 & −1 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0\end{aligned} & & \end{aligned}


$$

In the matrix above, there is only one pivot column (the $1$st one). So, the rank of $A+I$ is $1.$ Using the rank-nullity theorem, we have that

$$


\begin{aligned}nullity(𝐴−𝐼) & =3−rank(𝐴−𝐼) \\ & =3−1 \\ & =2.\end{aligned}


$$

Recall that the nullity of $A-I$ gives the number of eigenvectors corresponding to $\lambda=-1.$ Therefore, there must be two such eigenvectors, say, $\mathbf{v}_1$ and $\mathbf{v}_3.$ So, the generalized eigenvectors corresponding to the eigenvalue $\lambda=-1$ form the following chains:

$$


\begin{aligned}𝐯_{2}\overset{}{𝐴+𝐼\,}𝐯_{1}\overset{}{𝐴+𝐼\,}𝟎 & \\ 𝐯_{3}\overset{}{𝐴+𝐼\,}𝟎 & \end{aligned}


$$

Therefore, we have *case II*, and $A$ has the following Jordan canonical decomposition:

$$


\begin{aligned}−1 & 1 & 0 \\ 0 & −1 & 0 \\ 0 & 0 & −1\end{aligned}


$$

which, as we know, is unique up to the order of the Jordan blocks.

### Example: Finding a Jordan Canonical Form of a 3x3 Matrix With Only One Eigenvalue

#### Question

$$


\begin{aligned}4 & −1 & 3 \\ 1 & 1 & 1 \\ −1 & 1 & 1\end{aligned}


$$

The matrix above has eigenvalues $\lambda_1=\lambda_2=\lambda_3=2.$ Find a Jordan canonical form of the matrix.

#### Explanation

Notice that we are given a non-scalar $3 \times 3$ matrix that has the eigenvalue $\lambda=2$ of algebraic multiplicity $3.$

As a result, there are two possibilities for the Jordan blocks corresponding to $\lambda=2{:}$

- ** We may get the single $3 \times 3$ Jordan block $J_3(2).$ This happens when the generalized eigenvectors $\mathbf v_1, \mathbf v_2$ and $\mathbf v_3$ corresponding to $\lambda=2$ form the following chain:

- ** We may get a composition of one $2 \times 2$ and one $1 \times 1$ Jordan block, say $J_2(2) {\:\oplus\:} J_1(2).$ This happens when the generalized eigenvectors $\mathbf v_1, \mathbf v_2$ and $\mathbf v_3$ corresponding to $\lambda=2$ form the following chains:

To figure out which of the cases we obtain in this situation, let's find the number of linearly independent eigenvectors corresponding to $\lambda=2.$

Computing $A-2I,$ we get

$$


\begin{aligned}𝐴−2𝐼 & =\begin{aligned}4 & −1 & 3 \\ 1 & 1 & 1 \\ −1 & 1 & 1\end{aligned}−2\begin{aligned}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{aligned}=\begin{aligned}2 & −1 & 3 \\ 1 & −1 & 1 \\ −1 & 1 & −1\end{aligned}.\end{aligned}


$$

Now, we reduce this matrix to row echelon form using Gaussian elimination, as follows:

$$


\begin{aligned}𝐴−2𝐼 & =\begin{aligned}2 & −1 & 3 \\ 1 & −1 & 1 \\ −1 & 1 & −1\end{aligned} & & \begin{aligned}𝑅_{1}↔𝑅_{2}\end{aligned} \\ & ∼\begin{aligned}1 & −1 & 1 \\ 2 & −1 & 3 \\ −1 & 1 & −1\end{aligned} & & \begin{aligned}𝑅_{2}:=𝑅_{2}+(−2)𝑅_{1} \\ 𝑅_{3}:=𝑅_{3}+𝑅_{1}\end{aligned} \\ & ∼\begin{aligned}1 & −1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 0\end{aligned} & & \end{aligned}


$$

Since $\text{nullity}(A-2I)=1,$ there will be only one eigenvector that corresponds to the eigenvalue $\lambda=2,$ say, $\mathbf{v}_1.$ So, the generalized eigenvectors corresponding to the eigenvalue $\lambda=2$ form the following chain:

$$


\mathbf{v}_3 \xrightarrow{A-2 I} \mathbf{v}_2 \xrightarrow{A-2 I} \mathbf{v}_1 \xrightarrow{A-2 I} \mathbf{0}


$$

Therefore, we have **, and $A$ has the following Jordan canonical form:

$$


\begin{aligned}2 & 1 & 0 \\ 0 & 2 & 1 \\ 0 & 0 & 2\end{aligned}


$$

**** The Jordan canonical form is unique up to the order of the Jordan blocks.

### Overview of All Possible Jordan Canonical Forms of 3x3 Matrices

In general, there are possible Jordan canonical forms for matrices up to permutations of its Jordan blocks.

- If has *three* distinct eigenvalues and then is diagonalizable, and its corresponding Jordan canonical form is simply the diagonal form of the matrix. In this case, is a composition of three distinct Jordan blocks:

- If has *two* distinct eigenvalues and where has algebraic multiplicity, then there are two possible Jordan canonical forms for If there are two linearly independent eigenvectors corresponding to, then is the composition of two Jordan blocks corresponding to and a Jordan block corresponding to If there is only one linearly independent eigenvector corresponding to the eigenvalue, then is the composition of a Jordan block corresponding to and a Jordan block corresponding to

- If has only *one* eigenvalue then there are three possible Jordan canonical forms for If there are three linearly independent eigenvectors corresponding to, then must be a scalar matrix (meaning that it's already diagonalized), and is a composition of three identical Jordan blocks: If there are only two linearly independent eigenvectors corresponding to, then is the composition of a Jordan block corresponding to and a Jordan block also corresponding to Finally, if there is just one linearly independent eigenvector corresponding to, then is a single Jordan block corresponding to
