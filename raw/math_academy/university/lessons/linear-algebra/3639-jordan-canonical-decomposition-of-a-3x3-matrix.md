# Jordan Canonical Decomposition of a 3x3 Matrix

Source: https://www.mathacademy.com/topics/3639?courseId=55
Topic ID: 3639

## Prerequisites

- [Jordan Canonical Form of a 3x3 Matrix](./3115-jordan-canonical-form-of-a-3x3-matrix.md)

## Lesson

### Introduction

Like the case of $2 \times 2$ matrices, every $3 \times 3$ matrix has a Jordan canonical decomposition. Recall that a Jordan canonical decomposition of a square matrix $A$ is given by

$$


A = PJP^{-1},


$$

where $J$ is a Jordan canonical form and $P$ is an invertible matrix. So, to find a Jordan canonical decomposition of a matrix $A,$ means to find both

- a Jordan canonical form $J,$ and

- an invertible matrix $P$ that satisfies the equation above.

For example, the matrix

$$


\begin{aligned}1 & 1 & 0 \\ −1 & 3 & 0 \\ 5 & −3 & 3\end{aligned}


$$

has the Jordan canonical decomposition $A = PJP^{-1},$ where

$$


\begin{aligned}2 & 1 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 3\end{aligned}


$$

Notice that the columns of $P$ form a basis of $\mathbb{R}^3$ that consists of the following chains:

$$


\begin{aligned}𝐽_{2}(2) & : & 𝐯_{2}\overset{}{𝐴−2𝐼\,}𝐯_{1}\overset{}{𝐴−2𝐼\,}𝟎 \\ 𝐽_{1}(3) & : & 𝐯_{3}\overset{}{𝐴−3𝐼\,}𝟎\end{aligned}


$$

- The vectors ${\color{blue}\mathbf{v}_1}, {\color{DarkBlue}\mathbf{v}_2}$ are generalized eigenvectors corresponding to $\lambda = {\color{blue}2}.$ Here, only ${\color{blue}\mathbf{v}_1}$ is an eigenvector, while ${\color{DarkBlue}\mathbf{v}_2}$ is a generalized eigenvector of rank $2$ (that is, ${\color{DarkBlue}\mathbf{v}_2}$ is mapped to ${\color{blue}\mathbf{v}_1}$ under the action of $A-{\color{blue}2}I$).

- The vector ${\color{red}\mathbf{v}_3}$ is an eigenvector corresponding to $\lambda = {\color{red}3}.$

In general, for any Jordan canonical decomposition, the matrix $P$ must satisfy the properties given below.

- The columns of $P$ associated with a Jordan block $J_k(\lambda)$ are generalized eigenvectors corresponding to the eigenvalue $\lambda.$

- Moreover, if $k>1,$ the respective columns must be in the following order: the first column must be an eigenvector, and the second column must be a generalized eigenvector of rank $2$ that is mapped to the first column under the action of $A-\lambda I$, and so on.

**Watch out!** The order of the columns of $P$ is important!

### Example: Identifying the Columns of a Transformation Matrix in a Jordan Decomposition

#### Question

Consider the matrices above. Given that is a Jordan canonical decomposition of which of the following could be the first column of the matrix

#### Explanation

First, notice that the Jordan matrix may be written as a composition of Jordan blocks, as follows:

So, we have

- one Jordan block corresponding to and

- one Jordan block corresponding to

Therefore, the columns of form the following chains:

As a result, the first column of is an eigenvector corresponding to

Now, computing we get

Among the given vectors, only is an eigenvector of since

and we can write The other vectors do not satisfy this condition.

### The Case of a Single 3x3 Jordan Block

In this section, we will learn how to calculate a Jordan canonical decomposition of a non-diagonalizable $3\times3$ matrix with eigenvalue $\lambda$ of algebraic multiplicity $3.$

Consider the matrix $A,$ given by

$$


\begin{aligned}4 & −3 & 4 \\ −5 & −2 & −4 \\ −5 & 4 & −5\end{aligned}


$$

To find a Jordan canonical decomposition of $A,$ we follow the algorithm given below.

**Step 1:** Find the eigenvalues of the matrix.

Solving the characteristic equation $\vert A - \lambda I \vert = 0,$ we get the eigenvalue $\lambda=-1$ of algebraic multiplicity $3.$

**Step 2.** Determine the corresponding Jordan canonical form.

Computing $A - \lambda I$ and reducing it to row echelon form using Gaussian elimination, we obtain that

$$


\dim(V_{\lambda}) = \text{nullity}(A-\lambda I) = 1.


$$

This means that there is only one eigenvector corresponding to this eigenvalue, and thus the Jordan canonical form of $A$ is

$$


\begin{aligned}−1 & 1 & 0 \\ 0 & −1 & 1 \\ 0 & 0 & −1\end{aligned}


$$

**Step 3:** Find a basis of $\mathbb{R}^3$ consisting of the generalized eigenvectors corresponding to each eigenvalue.

Applying the usual method for computing eigenvectors, we get only one eigenvector

$$


\begin{aligned}−4 \\ 0 \\ 5\end{aligned}


$$

corresponding to the eigenvalue $\lambda =-1.$

Since the algebraic multiplicity of $\lambda$ is $3$ yet $\dim(V_{\lambda}) = 1,$ we need to find $3-1 = 2$ more linearly independent generalized eigenvectors corresponding to this eigenvalue. These generalized eigenvectors make up the columns of $P$ and form the following chain:

$$


\begin{aligned}𝐯_{3}\overset{}{𝐴+𝐼\,}𝐯_{2}\overset{}{𝐴+𝐼\,}𝐯_{1}\overset{}{𝐴+𝐼\,}𝟎\end{aligned}


$$

As a result, we obtain that

- the first column of $P$ corresponds to the eigenvector ${\color{DodgerBlue}\mathbf{v}_1}$ associated to the eigenvalue $\lambda=-1,$

- the second column of $P$ corresponds to the vector ${\color{blue}\mathbf{v}_2}$ such that $(A+I){\color{blue}\mathbf{v}_2} = {\color{DodgerBlue}\mathbf{v}_1},$ and

- the third column of $P$ corresponds to the vector ${\color{DarkBlue}\mathbf{v}_3}$ such that $(A+I){\color{DarkBlue}\mathbf{v}_3} = {\color{blue}\mathbf{v}_2}.$

To find the second vector of our basis, we have to solve the equation $(A + I){\color{blue}\mathbf{v}_2} = {\color{DodgerBlue}\mathbf{v_1}}.$ Solving this equation gives us

$$


\begin{aligned}−1 \\ 1 \\ 1\end{aligned}


$$

Similarly, to find the third vector of our basis, we have to solve the equation $(A + I){\color{DarkBlue}\mathbf{v}_3} = {\color{blue}\mathbf{v_2}}.$ This gives us

$$


\begin{aligned}−9 \\ 0 \\ 11\end{aligned}


$$

The set $\left\{{\color{DodgerBlue}\mathbf{v_1}}, {\color{blue}\mathbf{v_2}}, {\color{DarkBlue}\mathbf{v_3}}\right\}$ indeed forms a basis of $\mathbb{R}^3$ since the vectors are linearly independent.

**Step 4:** Construct the matrix $P.$

The columns of $P$ are the vectors $\color{DodgerBlue}\mathbf{v}_1,$ $\color{blue}\mathbf{v}_2,$ and $\color{DarkBlue}\mathbf{v}_3,$ where

- the first column must be our eigenvector $\color{DodgerBlue}\mathbf{v}_1,$

- the second column must be the vector $\color{blue}\mathbf{v}_2$ that is mapped to $\color{DodgerBlue}\mathbf{v}_1$ under the action of $A+I,$ and

- the third column must be the vector $\color{DarkBlue}\mathbf{v}_3$ that is mapped to $\color{blue}\mathbf{v}_2$ under the action of $A+I.$

So, we get

$$


\begin{aligned}| & | & | \\ 𝐯_{1} & 𝐯_{2} & 𝐯_{3} \\ | & | & |\end{aligned}


$$

Finally, the Jordan canonical decomposition of $A$ is as follows:

$$


\begin{aligned}4 & −3 & 4 \\ −5 & −2 & −4 \\ −5 & 4 & −5\end{aligned}


$$

**Watch out!** As always in Jordan decomposition, the order in which we write our vectors into the matrix $P$ is important!

### Example: Finding a Jordan Decomposition of a 3x3 Matrix Given Its Single Eigenvalue

#### Question

$$


\begin{aligned}−5 & −1 & 0 \\ 2 & −3 & −1 \\ −1 & −1 & −4\end{aligned}


$$

Consider the matrices above. Given that $A = P J P^{-1}$ is a Jordan canonical decomposition of $A,$ find the value of $a+b.$

#### Explanation

Since the Jordan block $J$ has a single $3 \times 3$ Jordan block corresponding to $\lambda=-4,$ the columns of $P$ form the following chain:

$$


\begin{aligned}𝐯_{3}\overset{}{𝐴+4𝐼\,}𝐯_{2}\overset{}{𝐴+4𝐼\,}𝐯_{1}\overset{}{𝐴+4𝐼\,}𝟎\end{aligned}


$$

As a result, we obtain that

- the first column of $P$ corresponds to the eigenvector $\mathbf{v}_1$ of the eigenvalue $\lambda=-4,$

- the second column of $P$ corresponds to the vector $\begin{aligned}0 \\ 1 \\ 0\end{aligned}$ such that $(A+4I)\mathbf{v}_2 = \mathbf{v}_1,$

- the third column of $P$ corresponds to the vector $\mathbf{v}_3$ such that $(A+4I)\mathbf{v}_3 = \mathbf{v}_2.$

Now, computing $A+4I,$ we get

$$


\begin{aligned}𝐴+4𝐼 & =\begin{aligned}−5 & −1 & 0 \\ 2 & −3 & −1 \\ −1 & −1 & −4\end{aligned}+4\begin{aligned}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{aligned}=\begin{aligned}−1 & −1 & 0 \\ 2 & 1 & −1 \\ −1 & −1 & 0\end{aligned}.\end{aligned}


$$

So, the matrix equation $(A+4I)\mathbf{v}_3 = \mathbf{v}_2$ is equivalent to the system of linear equations with the augmented matrix $M$ which we reduce to row echelon form using Gaussian elimination, as follows:

$$


\begin{aligned}𝑀 & =\begin{aligned}−1 & −1 & 0 & 0 \\ 2 & 1 & −1 & 1 \\ −1 & −1 & 0 & 0\end{aligned} & & \begin{aligned}𝑅_{2}:=𝑅_{2}+2𝑅_{1} \\ 𝑅_{3}:=𝑅_{3}+(−1)𝑅_{1}\end{aligned} \\ & ∼\begin{aligned}−1 & −1 & 0 & 0 \\ 0 & −1 & −1 & 1 \\ 0 & 0 & 0 & 0\end{aligned} & & \end{aligned}


$$

The reduced matrix above has two pivot columns (the $1$st and $2$nd). Thus, $x_3$ is a free variable. From the second equation, we have $x_2=-x_3-1.$ Substituting this into the first equation, we obtain

$$


-x_1-(-x_3-1) = 0 \qquad \Longrightarrow \qquad x_1= x_3+1.


$$

Hence, the general solution is

$$


\begin{aligned}𝑥_{3}+1 \\ −𝑥_{3}−1 \\ 𝑥_{3}\end{aligned}


$$

Therefore, setting $x_3=0,$ we get

$$


\begin{aligned}𝑎 \\ 𝑏 \\ 𝑐\end{aligned}


$$

Finally, $a+b=1 + (-1) = 0.$

### The Case of Two Jordan Blocks Corresponding to Two Different Eigenvalues

In this section, we will learn how to calculate a Jordan canonical decomposition of a non-diagonalizable $3\times3$ matrix where one of its eigenvalues has algebraic multiplicity $2.$

Consider the matrix $A,$ given by

$$


\begin{aligned}1 & 1 & 0 \\ −1 & 3 & 0 \\ 5 & −3 & 3\end{aligned}


$$

To find a Jordan canonical decomposition of $A,$ we follow the algorithm given below.

**Step 1:** Find the eigenvalues of the matrix.

Solving the characteristic equation $\vert A - \lambda I \vert = 0,$ we get

- the eigenvalue ${\color{blue}{\lambda_1}}={\color{blue}{2}}$ of algebraic multiplicity $2,$ and

- the eigenvalue ${\color{red}{\lambda_2}}={\color{red}{3}}$ of algebraic multiplicity $1.$

**Step 2.** Determine the corresponding Jordan canonical form.

Computing $A - \lambda_1 I$ and reducing it to row echelon form using Gaussian elimination, we obtain that

$$


\dim(V_{\color{blue}\lambda_1}) = \text{nullity}(A-{\color{blue}{\lambda_1}}I) = 1.


$$

This means that there is only one eigenvector corresponding to this eigenvalue. Therefore, a Jordan canonical form of $A$ is

$$


\begin{aligned}2 & 1 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 3\end{aligned}


$$

**Step 3:** Find a basis of $\mathbb{R}^3$ consisting of the generalized eigenvectors corresponding to each eigenvalue.

Applying the usual method for computing eigenvectors, we get the following:

- One eigenvector corresponding to the eigenvalue ${\color{blue}{\lambda_1}}={\color{blue}{2}},$ namely

- One eigenvector corresponding to the eigenvalue ${\color{red}{\lambda_2}}={\color{red}{3}},$ namely

Since the algebraic multiplicity of ${\color{blue}{\lambda_1}}$ is $2$ yet $\dim(V_{\color{blue}{\lambda_1}}) = 1,$ we need to find $2-1 = 1$ more linearly independent generalized eigenvector corresponding to this eigenvalue.

The generalized eigenvectors make up the columns of $P$ and form the following chains:

$$


\begin{aligned}𝐽_{2}(2) & : & 𝐯_{2}\overset{}{𝐴−2𝐼\,}𝐯_{1}\overset{}{𝐴−2𝐼\,}𝟎 \\ 𝐽_{1}(3) & : & 𝐯_{3}\overset{}{𝐴−3𝐼\,}𝟎\end{aligned}


$$

As a result, we obtain that

- the first column of $P$ corresponds to the eigenvector ${\color{blue}\mathbf{v}_1}$ associated to the eigenvalue ${\color{blue}{\lambda_1}},$

- the second column of $P$ corresponds to the vector ${\color{DarkBlue}\mathbf{v}_2}$ such that $(A-2I){\color{DarkBlue}\mathbf{v}_2} = {\color{blue}\mathbf{v}_1}.$

- the third column of $P$ corresponds to the eigenvector ${\color{red}\mathbf{v}_3}$ associated to the eigenvalue ${\color{red}{\lambda_2}}={\color{red}{3}}.$

To find the second vector of our special basis, we have to solve the equation $(A -2 I){\color{DarkBlue}\mathbf{v}_2} = {\color{blue}\mathbf{v_1}},$ which gives us

$$


\begin{aligned}−1 \\ −2 \\ 1\end{aligned}


$$

The set $\left\{{\color{blue}\mathbf{v_1}}, {\color{DarkBlue}\mathbf{v_2}}, {\color{red}\mathbf{v_3}}\right\}$ indeed forms a basis of $\mathbb{R}^3$ since the vectors are linearly independent.

**Step 4:** Construct the matrix $P.$

The columns of $P$ are the vectors $\color{blue}\mathbf{v}_1,$ $\color{blue}\mathbf{v}_2,$ and $\color{red}\mathbf{v}_3,$ where

- the first column must be the eigenvector ${\color{blue}\mathbf{v}_1},$

- the second column must be the vector $\color{DarkBlue}\mathbf{v}_2$ that is mapped to ${\color{blue}\mathbf{v}_1}$ under the action of $A-2I,$ and

- the third column must be the eigenvector ${\color{red}\mathbf{v}_3}.$

So, we get

$$


\begin{aligned}| & | & | \\ 𝐯_{1} & 𝐯_{2} & 𝐯_{3} \\ | & | & |\end{aligned}


$$

Finally, the Jordan canonical decomposition of $A$ is as follows:

$$


\begin{aligned}1 & 1 & 0 \\ −1 & 3 & 0 \\ 5 & −3 & 3\end{aligned}


$$

### Example: Finding a Jordan Decomposition of a 3x3 Matrix Given Its Two Distinct Eigenvalues

#### Question

$$


\begin{aligned}3 & −11 & 10 \\ 0 & −3 & 1 \\ 0 & −1 & −5\end{aligned}


$$

Consider the matrices above. Given that $A = P J P^{-1}$ is a Jordan canonical decomposition of $A,$ find the value of $a-3b.$

#### Explanation

First, notice that the Jordan matrix $J$ may be written as a composition of Jordan blocks, as follows:

$$


J = J_2(-4) {\:\oplus\:} J_1(3)


$$

So, we have

- a single $2 \times 2$ Jordan block corresponding to $\lambda=-4,$ and

- a single $1 \times 1$ block corresponding to $\lambda=3.$

Therefore, the columns of $P$ form the following chains:

$$


\begin{aligned}𝐽_{2}(−4) & : & 𝐯_{2}\overset{}{𝐴+4𝐼\,}𝐯_{1}\overset{}{𝐴+4𝐼\,}𝟎 & \\ 𝐽_{1}(3) & : & 𝐯_{3}\overset{}{𝐴−3𝐼\,}𝟎 & \end{aligned}


$$

As a result, we obtain that

- the first column of $P$ corresponds to the eigenvector $\begin{aligned}3 \\ 1 \\ −1\end{aligned}$ of the eigenvalue $\lambda=-4,$

- the second column of $P$ corresponds to the vector $\mathbf{v}_2$ such that $(A+4I)\mathbf{v}_2 = \mathbf{v}_1.$

Now, computing $A+4I,$ we get

$$


\begin{aligned}𝐴+4𝐼 & =\begin{aligned}3 & −11 & 10 \\ 0 & −3 & 1 \\ 0 & −1 & −5\end{aligned}+4\begin{aligned}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{aligned}=\begin{aligned}7 & −11 & 10 \\ 0 & 1 & 1 \\ 0 & −1 & −1\end{aligned}.\end{aligned}


$$

So, the matrix equation $(A+4I)\mathbf{v}_2 = \mathbf{v}_1$ is equivalent to the system of linear equations with the augmented matrix $M$ which we reduce to row echelon form using Gaussian elimination, as follows:

$$


\begin{aligned}𝑀 & =\begin{aligned}7 & −11 & 10 & 3 \\ 0 & 1 & 1 & 1 \\ 0 & −1 & −1 & −1\end{aligned} & & \begin{aligned}𝑅_{3}:=𝑅_{3}+𝑅_{2}\end{aligned} \\ & ∼\begin{aligned}7 & −11 & 10 & 3 \\ 0 & 1 & 1 & 1 \\ 0 & 0 & 0 & 0\end{aligned} & & \end{aligned}


$$

The reduced matrix above has two pivot columns (the $1$st and $2$nd). Thus, $x_3$ is a free variable. From the second equation, we have $x_2=1-x_3.$ Substituting this into the first equation, we obtain

$$


7x_1-11(1-x_3)+10x_3 = 3 \qquad \Longrightarrow \qquad x_1= 2-3x_3.


$$

Hence, the general solution is

$$


\begin{aligned}2−3𝑥_{3} \\ 1−𝑥_{3} \\ 𝑥_{3}\end{aligned}


$$

Therefore, setting $x_3=0,$ we get

$$


\begin{aligned}𝑎 \\ 𝑏 \\ 𝑐\end{aligned}


$$

Finally, $a-3b=2-3\cdot 1 = -1.$
