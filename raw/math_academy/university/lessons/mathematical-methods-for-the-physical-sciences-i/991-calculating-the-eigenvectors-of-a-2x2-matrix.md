# Calculating the Eigenvectors of a 2x2 Matrix

Source: https://www.mathacademy.com/topics/991?courseId=154
Topic ID: 991

## Prerequisites

- [Calculating the Eigenvalues of a 2x2 Matrix](./990-calculating-the-eigenvalues-of-a-2x2-matrix.md)

## Lesson

### Introduction

Consider the matrix

$$


[\begin{aligned}2 & 6 \\ 0 & 3\end{aligned}]


$$

Given that $\lambda=3$ is an eigenvalue of $A,$ how can we find an eigenvector that corresponds to this eigenvalue?

Recall that a non-zero vector $\color{blue}\mathbf{v}$ is an eigenvector of $A$ with corresponding eigenvalue $\lambda$ if

$$


A{\color{blue}\mathbf{v}}={\color{red}\lambda}{\color{blue}\mathbf{v}}.


$$

We can rewrite this equation, substituting ${\color{red}{\lambda = 3}},$ as follows:

$$


\begin{aligned}𝐴𝐯 & =3𝐯 \\ 𝐴𝐯−3𝐯 & =𝟎 \\ 𝐴𝐯−3𝐼𝐯 & =𝟎 \\ (𝐴−3𝐼)𝐯 & =𝟎\end{aligned}


$$

So, to find an eigenvector of $A$ that corresponds to $\lambda = {\color{red}3},$ we need to find a non-zero solution of the equation

$$


(A- {\color{red}3} I){\color{blue}\mathbf{v}} = \mathbf{0}.


$$

In our case, we have

$$


\begin{aligned}𝐴−3𝐼 & =[\begin{matrix}2 & 6 \\ 0 & 3\end{matrix}]−3[\begin{matrix}1 & 0 \\ 0 & 1\end{matrix}] \\ & =[\begin{matrix}−1 & 6 \\ 0 & 0\end{matrix}].\end{aligned}


$$

Therefore, the equation $(A- {\color{red}3} I){\color{blue}\mathbf{v}} = \mathbf{0}$ corresponds to the following homogeneous system of linear equations:

$$


\begin{aligned}−𝑥_{1}+6𝑥_{2}=0 \\ 0=0.\end{aligned}


$$

Notice that $A-{\color{red}3}I$ is already in row echelon form, and it has one pivot column (the $1$st one). So, $x_2$ is a free variable. Moreover, from the first equation, we get $x_1=6x_2,$ which implies that the general solution is

$$


[\begin{aligned}6𝑥_{2} \\ 𝑥_{2}\end{aligned}]


$$

We only require one eigenvector corresponding to $\lambda={\color{red}3}.$ Setting $x_2=1,$ we obtain the eigenvector

$$


[\begin{aligned}6 \\ 1\end{aligned}]


$$

**Note:** If we set $x_2=2,$ we'll get a different eigenvector, namely

$$


[\begin{aligned}12 \\ 2\end{aligned}]


$$

Note that $\mathbf w$ is also an eigenvector that corresponds to $\lambda=3.$ In fact, we can choose any real $x_2 \neq 0$ to generate an eigenvector corresponding to $\lambda = 3.$

**Watch out!** In the case of $x_2=0,$ we get the zero vector, but this is not an eigenvector. Remember that eigenvectors must be non-zero vectors.

### Example: Calculating the Components of an Eigenvector Corresponding to an Eigenvalue

#### Question

If $[\begin{aligned}𝑎 \\ 𝑏\end{aligned}]$ is an eigenvector of $[\begin{aligned}2 & 5 \\ −1 & −4\end{aligned}]$ that corresponds to the eigenvalue $\,\lambda=1$, then what is the value of $\,\dfrac{b}{a}\,?$

#### Explanation

To compute the eigenvectors of a matrix, we need to find non-zero solutions of the matrix equation

$$


(A - \lambda I) \textbf{x}=\mathbf{0}.


$$

In our case, we have $\,\lambda =1.$ So, we have

$$


\begin{aligned}𝐴−𝜆𝐼 & =[\begin{matrix}2 & 5 \\ −1 & −4\end{matrix}]−[\begin{matrix}1 & 0 \\ 0 & 1\end{matrix}] \\ & =[\begin{matrix}1 & 5 \\ −1 & −5\end{matrix}].\end{aligned}


$$

We have to solve the corresponding homogeneous system of linear equations:

$$


\begin{aligned}𝑥_{1}+5𝑥_{2}=0 \\ −𝑥_{1}−5𝑥_{2}=0\end{aligned}


$$

So, we row-reduce the augmented matrix $M$ to row echelon form using Gaussian elimination, as follows:

$$


\begin{aligned}𝑀 & =[\begin{matrix}1 & 5 & 0 \\ −1 & −5 & 0\end{matrix}] & 𝑅_{2}:=𝑅_{2}+𝑅_{1} \\ & ∼[\begin{matrix}1 & 5 & 0 \\ 0 & 0 & 0\end{matrix}] & \end{aligned}


$$

In the reduced matrix above, there is one pivot column (the $1$st one). So, $x_2$ is a free variable.

From the first equation, we obtain

$$


x_1+5x_2=0 \qquad\Longrightarrow\qquad x_1=-5x_2.


$$

Therefore, the general solution is

$$


[\begin{aligned}−5𝑥_{2} \\ 𝑥_{2}\end{aligned}]


$$

Setting, for instance, $x_2=-1,$ we get the following eigenvector:

$$


[\begin{aligned}𝑎 \\ 𝑏\end{aligned}]


$$

Finally, $\dfrac{b}{a}=\dfrac{-1}{5}=-\dfrac{1}{5}.$

### Example: Calculating an Eigenvector Corresponding to an Eigenvalue

#### Question

Find an eigenvector of $[\begin{aligned}7 & −4 \\ 5 & −2\end{aligned}]$ that corresponds to the eigenvalue $\,\lambda=2.$

#### Explanation

To compute the eigenvectors of a matrix, we need to find non-zero solutions of the matrix equation

$$


(A - \lambda I) \textbf{x}=\mathbf{0}.


$$

In our case, we have $\,\lambda =2.$ So, we get

$$


\begin{aligned}𝐴−𝜆𝐼 & =[\begin{matrix}7 & −4 \\ 5 & −2\end{matrix}]−2[\begin{matrix}1 & 0 \\ 0 & 1\end{matrix}] \\ & =[\begin{matrix}5 & −4 \\ 5 & −4\end{matrix}].\end{aligned}


$$

We have to solve the corresponding homogeneous system of linear equations:

$$


\begin{aligned}5𝑥_{1}−4𝑥_{2}=0 \\ 5𝑥_{1}−4𝑥_{2}=0\end{aligned}


$$

So, we row-reduce the augmented matrix $M$ to row echelon form using Gaussian elimination, as follows:

$$


\begin{aligned}𝑀 & =[\begin{matrix}5 & −4 & 0 \\ 5 & −4 & 0\end{matrix}] & 𝑅_{2}:=𝑅_{2}+(−1)𝑅_{1} \\ & ∼[\begin{matrix}5 & −4 & 0 \\ 0 & 0 & 0\end{matrix}] & \end{aligned}


$$

In the reduced matrix above, there is one pivot column (the $1$st one). So, $x_2$ is a free variable.

From the first equation, we obtain

$$


5x_1-4x_2=0 \qquad\Longrightarrow\qquad x_1=\dfrac{4}{5}x_2.


$$

Therefore, the general solution is

$$


\begin{aligned}\frac{4}{5}𝑥_{2} \\ 𝑥_{2}\end{aligned}


$$

Finally, setting $x_2=5,$ we get the eigenvector

$$


[\begin{aligned}4 \\ 5\end{aligned}]


$$

### Connection Between Eigenspaces and Null Spaces

Given a matrix $A$ with an eigenvalue $\lambda$, the **eigenspace** $V_\lambda$ can be defined as the set of all possible eigenvectors corresponding to $\lambda$ plus the vector $\mathbf{0}{:}$

$$


eigenvectors


$$

Note that the eigenspace consists of *all* (not only non-zero) solutions of the equation $(A-\lambda I)\mathbf{x}=\mathbf{0}.$ So, the eigenspace can also be viewed as the *null space* of the matrix $A-\lambda I,$ as follows:

$$


V_{\color{red}\lambda} = \text{Null}(A - {\color{red}\lambda} I).


$$

We also have the following theorem:

*Eigenvectors that correspond to different eigenvalues are always linearly independent.*

For example, the matrix

$$


[\begin{aligned}1 & −2 \\ 3 & −4\end{aligned}]


$$

has eigenvalues $\lambda_1=-2$ and $\lambda_2=-1,$ for which the corresponding eigenvectors are

$$


[\begin{aligned}2 \\ 3\end{aligned}]


$$

Here, $\mathbf{v}_1$ and $\mathbf{v}_2$ are linearly independent (they are not collinear).

**Watch out!** Eigenvectors that correspond to the *same* eigenvalue *can be* (and very often *will* be) linearly dependent. For example, the vectors

$$


[\begin{aligned}1 \\ 1\end{aligned}]


$$

are collinear eigenvectors of the matrix $A$ above that correspond to $\lambda_2=-1.$

### Example: Finding Two Linearly Independent Eigenvectors of a 2x2 Matrix

#### Question

Given that $\lambda=1$ and $\lambda=-4$ are the eigenvalues of the matrix $[\begin{aligned}1 & −1 \\ 0 & −4\end{aligned}]$ find two linearly independent eigenvectors of $A.$

#### Explanation

We can get two linearly independent eigenvectors by simply finding eigenvectors corresponding to the different eigenvalues.

To compute the eigenvectors of a matrix, we need to find non-zero solutions of the matrix equation

$$


(A - \lambda I) \textbf{x}=\mathbf{0}.


$$

With that in mind, let's consider each of the eigenvalues separately.

- For $\lambda =1,$ we have We have to solve the corresponding system of linear equations: So, we row-reduce the augmented matrix $M$ to row echelon form using Gaussian elimination, as follows: In the reduced matrix above, there is one pivot column (the $2$nd one). So, $x_1$ is a free variable. From the first equation, we obtain $x_2=0.$ Therefore, the general solution is Setting, for instance, $x_1=1,$ we get the eigenvector $[\begin{aligned}1 \\ 0\end{aligned}]$

- For $\lambda =-4,$ we have We have to solve the corresponding system of linear equations: So, we row-reduce the augmented matrix $M$ to row echelon form using Gaussian elimination, as follows: In the matrix above, there is one pivot column (the $1$st one). So, $x_2$ is a free variable. From the first equation, we obtain $x_1=\dfrac{1}{5}x_2.$ Therefore, the general solution is Setting, for instance, $x_2=5,$ we get the eigenvector $[\begin{aligned}1 \\ 5\end{aligned}]$

Therefore, two linearly independent eigenvectors of the matrix $A$ are

$$


[\begin{aligned}1 \\ 0\end{aligned}]


$$
