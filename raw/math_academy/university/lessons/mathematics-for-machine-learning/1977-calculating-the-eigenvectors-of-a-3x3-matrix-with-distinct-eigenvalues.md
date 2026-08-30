# Calculating the Eigenvectors of a 3x3 Matrix With Distinct Eigenvalues

Source: https://www.mathacademy.com/topics/1977?courseId=145
Topic ID: 1977

## Prerequisites

- [Calculating the Eigenvectors of a 2x2 Matrix](./991-calculating-the-eigenvectors-of-a-2x2-matrix.md)
- [The Characteristic Equation of a Matrix](./1964-the-characteristic-equation-of-a-matrix.md)

## Lesson

### Introduction

Consider the following $3\times 3$ matrix:

$$


\begin{aligned}3 & 6 & −8 \\ 0 & 0 & 6 \\ 0 & 3 & −4\end{aligned}


$$

If we are told that one of the eigenvalues of this matrix is $\lambda = 3,$ how do we calculate the corresponding eigenvector?

To compute the eigenvectors of a matrix, we need to find non-zero solutions of the matrix equation

$$


(A - \lambda I) \textbf{x}=\mathbf{0}.


$$

In our case, we have $\lambda =3.$ So, we get

$$


\begin{aligned}𝐴−𝜆𝐼 & =\begin{matrix}3 & 6 & −8 \\ 0 & 0 & 6 \\ 0 & 3 & −4\end{matrix}−3\begin{matrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{matrix} \\ & =\begin{matrix}0 & 6 & −8 \\ 0 & −3 & 6 \\ 0 & 3 & −7\end{matrix}.\end{aligned}


$$

Next, to find the eigenvectors, we have to solve the corresponding homogeneous system of linear equations:

$$


\begin{aligned}6𝑥_{2}−8𝑥_{3}=0 \\ −3𝑥_{2}+6𝑥_{3}=0 \\ 3𝑥_{2}−7𝑥_{3}=0\end{aligned}


$$

So, we row-reduce the augmented matrix $M$ to row echelon form using Gaussian elimination, as follows:

$$


\begin{aligned}𝑀 & =\begin{matrix}0 & 6 & −8 & 0 \\ 0 & −3 & 6 & 0 \\ 0 & 3 & −7 & 0\end{matrix} & & \begin{matrix}𝑅_{2}:=𝑅_{2}+\frac{1}{2}𝑅_{1} \\ 𝑅_{3}:=𝑅_{3}+(−\frac{1}{2})𝑅_{1}\end{matrix} \\ & ∼\begin{matrix}0 & 6 & −8 & 0 \\ 0 & 0 & 2 & 0 \\ 0 & 0 & −3 & 0\end{matrix} & & \begin{matrix}𝑅_{3}:=𝑅_{3}+\frac{3}{2}𝑅_{2}\end{matrix} \\ & ∼\begin{matrix}0 & 6 & −8 & 0 \\ 0 & 0 & 2 & 0 \\ 0 & 0 & 0 & 0\end{matrix} & & \end{aligned}


$$

In this reduced matrix, there are two pivot columns (the $2$nd and $3$rd). Thus, $x_1$ is a free variable. From the second equation, we have $x_3 = 0.$ Substituting this into the first equation, we obtain $x_2 = 0.$ Therefore, the general solution is

$$


\begin{aligned}𝑥_{1} \\ 0 \\ 0\end{aligned}


$$

Setting $x_1=1,$ we get the following eigenvector:

$$


\begin{aligned}𝑎 \\ 𝑏 \\ 𝑐\end{aligned}


$$

### Example: Calculating the Components of an Eigenvector Corresponding to a Given Eigenvalue

#### Question

The vector $\mathbf{v}$ and the matrix $A$ are given below. If $\mathbf{v}$ is an eigenvector of $A$ that corresponds to the eigenvalue $\lambda=3,$ then what is the value of $\dfrac{b}{c}?$

$$


\begin{aligned}𝑎 \\ 𝑏 \\ 𝑐\end{aligned}


$$

#### Explanation

To compute the eigenvectors of a matrix, we need to find non-zero solutions of the matrix equation

$$


(A - \lambda I) \textbf{x}=\mathbf{0}.


$$

In our case, we have $\lambda =3.$ So, we get

$$


\begin{aligned}𝐴−𝜆𝐼 & =\begin{matrix}5 & 0 & −6 \\ 2 & 1 & −4 \\ 1 & 0 & 0\end{matrix}−3\begin{matrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{matrix} \\ & =\begin{matrix}2 & 0 & −6 \\ 2 & −2 & −4 \\ 1 & 0 & −3\end{matrix}.\end{aligned}


$$

To find the eigenvectors, we have to solve the corresponding homogeneous system of linear equations:

$$


\begin{aligned}2𝑥_{1}−6𝑥_{3}=0 \\ 2𝑥_{1}−2𝑥_{2}−4𝑥_{3}=0 \\ 𝑥_{1}−3𝑥_{3}=0\end{aligned}


$$

So, we row-reduce the augmented matrix $M$ to row echelon form using Gaussian elimination, as follows:

$$


\begin{aligned}𝑀 & =\begin{matrix}2 & 0 & −6 & 0 \\ 2 & −2 & −4 & 0 \\ 1 & 0 & −3 & 0\end{matrix} & & 𝑅_{1}:=\frac{1}{2}𝑅_{1} \\ & ∼\begin{matrix}1 & 0 & −3 & 0 \\ 2 & −2 & −4 & 0 \\ 1 & 0 & −3 & 0\end{matrix} & & \begin{matrix}𝑅_{2}:=𝑅_{2}+(−2)𝑅_{1} \\ 𝑅_{3}:=𝑅_{3}+(−1)𝑅_{1}\end{matrix} \\ & ∼\begin{matrix}1 & 0 & −3 & 0 \\ 0 & −2 & 2 & 0 \\ 0 & 0 & 0 & 0\end{matrix} & & \end{aligned}


$$

In the reduced matrix above, there are two pivot columns (the $1$st and the $2$nd). Thus, $x_3$ is a free variable. From the second equation, we obtain $x_2=x_3.$ From the first equation, we get $x_1=3x_3.$ Therefore, the general solution is

$$


\begin{aligned}3𝑥_{3} \\ 𝑥_{3} \\ 𝑥_{3}\end{aligned}


$$

Setting, for instance, $x_3=1,$ we get the following eigenvector:

$$


\begin{aligned}𝑎 \\ 𝑏 \\ 𝑐\end{aligned}


$$

Finally, $\dfrac{b}{c}=\dfrac{1}{1}=1.$

### Example: Calculating an Eigenvector Corresponding to a Given Eigenvalue

#### Question

Find an eigenvector of $\begin{aligned}1 & 3 & 4 \\ 0 & −2 & 0 \\ 0 & 0 & −1\end{aligned}$ that corresponds to the eigenvalue $\lambda=-2.$

#### Explanation

To compute the eigenvectors of a matrix, we need to find non-zero solutions of the matrix equation

$$


(A - \lambda I) \textbf{x}=\mathbf{0}.


$$

In our case, we have $\lambda =-2.$ So, we obtain

$$


\begin{aligned}𝐴−𝜆𝐼 & =\begin{matrix}1 & 3 & 4 \\ 0 & −2 & 0 \\ 0 & 0 & −1\end{matrix}−(−2)\begin{matrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{matrix} \\ & =\begin{matrix}3 & 3 & 4 \\ 0 & 0 & 0 \\ 0 & 0 & 1\end{matrix}.\end{aligned}


$$

To find the eigenvectors corresponding to this eigenvalue, we have to solve the corresponding homogeneous system of linear equations:

$$


\begin{aligned}3𝑥_{1}+3𝑥_{2}+4𝑥_{3}=0 \\ 0=0 \\ 𝑥_{3}=0\end{aligned}


$$

So, we row-reduce the augmented matrix $M$ to row echelon form using Gaussian elimination, as follows:

$$


\begin{aligned}𝑀 & =\begin{matrix}3 & 3 & 4 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0\end{matrix} & & \begin{matrix}𝑅_{2}↔𝑅_{3}\end{matrix} \\ & ∼\begin{matrix}3 & 3 & 4 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0\end{matrix} & & \end{aligned}


$$

In the reduced matrix above, there are two pivot columns (the $1$st and the $3$rd). Thus, $x_2$ is a free variable. From the second equation, we obtain $x_3=0.$ Substituting this in the first equation, we get $x_1=-x_2.$ Therefore, the general solution is

$$


\begin{aligned}−𝑥_{2} \\ 𝑥_{2} \\ 0\end{aligned}


$$

Setting, for instance, $x_2=1,$ we get the eigenvector $\begin{aligned}−1 \\ 1 \\ 0\end{aligned}$

### Eigenvectors That Correspond to Different Eigenvalues

Note the following important theorem.

*The set of eigenvectors $\{\mathbf{v}_1,\mathbf{v}_2, \ldots, \mathbf{v}_k \}$ of a matrix $A,$ where each vector $\mathbf v_i$ corresponds to a different eigenvalue, is linearly independent.*

**Watch out!** Eigenvectors that correspond to the *same* eigenvalue *can* be (and very often *will* be) linearly dependent.

### Example: Finding the Eigenvectors of a 3x3 Matrix

#### Question

$$


\begin{aligned}1 & 0 & 0 \\ 0 & −1 & 0 \\ 0 & 0 & 4\end{aligned}


$$

The vectors $\mathbf{v}_1$ and $\mathbf{v}_2$ are eigenvectors that correspond to the eigenvalues $\lambda_1=1$ and $\lambda_2=-1$ of the matrix $A,$ given above. Find the third eigenvector $\mathbf{v}_3=\big[a, \, b, \, c \big]^T$ such that the set $\{\mathbf{v}_1,\mathbf{v}_2, \mathbf{v}_3 \}$ is linearly independent. What is the value of $\dfrac{a}{c}?$

#### Explanation

Since $A$ is a diagonal matrix, we have that its eigenvalues are the entries in the main diagonal, that is, $\lambda_1=1,$ $\lambda_2=-1$ and $\lambda_3=4.$

Also, since we obtained three distinct eigenvalues, the set of eigenvectors $\{\mathbf{v}_1,\mathbf{v}_2, \mathbf{v}_3 \},$ where each vector corresponds to different eigenvalue, will be linearly independent.

Now, recall that $\mathbf{v}_1$ and $\mathbf{v}_2$ correspond to the eigenvalues $\lambda_1=1$ and $\lambda_2=-1.$ Thus, the third eigenvector $\mathbf{v}_3$ must correspond to $\lambda_3=4.$

To compute the eigenvectors of a matrix, we need to find non-zero solutions of the matrix equation

$$


(A - \lambda I) \textbf{x}=\mathbf{0}.


$$

In our case, we have $\lambda =4.$ So, we obtain

$$


\begin{aligned}𝐴−𝜆𝐼 & =\begin{matrix}1 & 0 & 0 \\ 0 & −1 & 0 \\ 0 & 0 & 4\end{matrix}−4\begin{matrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{matrix} \\ & =\begin{matrix}−3 & 0 & 0 \\ 0 & −5 & 0 \\ 0 & 0 & 0\end{matrix}.\end{aligned}


$$

To find the eigenvectors corresponding to this eigenvalue, we have to solve the corresponding homogeneous system of linear equations:

$$


\begin{aligned}−3𝑥_{1}=0 \\ −5𝑥_{2}=0 \\ 0=0\end{aligned}


$$

Notice that the augmented matrix $M$ is already in its row echelon form:

$$


\begin{aligned}𝑀 & =\begin{matrix}−3 & 0 & 0 & 0 \\ 0 & −5 & 0 & 0 \\ 0 & 0 & 0 & 0\end{matrix}\end{aligned}


$$

In this matrix, there are two pivot columns (the $1$st and the $2$nd). Thus, $x_3$ is a free variable. From the first and second equations, we obtain $x_1=x_2=0.$ Therefore, the general solution is

$$


\begin{aligned}0 \\ 0 \\ 𝑥_{3}\end{aligned}


$$

Setting, for instance, $x_3=1,$ we get the following eigenvector:

$$


\begin{aligned}𝑎 \\ 𝑏 \\ 𝑐\end{aligned}


$$

Finally, $\dfrac{a}{c}=\dfrac{0}{1}=0.$
