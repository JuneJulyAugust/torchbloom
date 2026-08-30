# Calculating the Eigenvectors of a 3x3 Matrix in the General Case

Source: https://www.mathacademy.com/topics/1965?courseId=55
Topic ID: 1965

## Prerequisites

- [Calculating the Eigenvectors of a 3x3 Matrix With Distinct Eigenvalues](./1977-calculating-the-eigenvectors-of-a-3x3-matrix-with-distinct-eigenvalues.md)

## Lesson

### Introduction

Let's consider the matrix

$$


\begin{aligned}5 & 8 & 16 \\ 4 & 1 & 8 \\ −4 & −4 & −11\end{aligned}


$$

with the eigenvalue $\lambda=-3.$ Note that this eigenvalue has multiplicity two in the corresponding characteristic equation.

We know how to find eigenvectors when all eigenvalues are simple roots of the characteristic equation (i.e., all roots have multiplicity equal to one). But what can we say about the eigenspace $V_{-3}$ for this particular matrix?

Recall that given a matrix with eigenvalue $\lambda,$ the eigenspace $V_{\lambda}$ is

$$


eigenvectors


$$

To compute the eigenvectors of the matrix, we need to find non-zero solutions of the matrix equation

$$


(A - \lambda I) \textbf{x}=\mathbf{0}.


$$

In our case, we have $\lambda =-3.$ So, we get

$$


\begin{aligned}𝐴−𝜆𝐼 & =\begin{matrix}5 & 8 & 16 \\ 4 & 1 & 8 \\ −4 & −4 & −11\end{matrix}−(−3)\begin{matrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{matrix}=\begin{matrix}8 & 8 & 16 \\ 4 & 4 & 8 \\ −4 & −4 & −8\end{matrix}.\end{aligned}


$$

Now, we have to solve the corresponding homogeneous system of linear equations:

$$


\begin{aligned}8𝑥_{1}+8𝑥_{2}+16𝑥_{3}=0 \\ 4𝑥_{1}+4𝑥_{2}+8𝑥_{3}=0 \\ −4𝑥_{1}−4𝑥_{2}−8𝑥_{3}=0\end{aligned}


$$

Solving the system, we obtain the general solution

$$


\begin{aligned}−𝑥_{2}−2𝑥_{3} \\ 𝑥_{2} \\ 𝑥_{3}\end{aligned}


$$

Therefore, our eigenspace is

$$


\begin{aligned}−1 \\ 1 \\ 0\end{aligned}


$$

Notice that $s=t=0$ gives the zero vector. On the other hand, the vectors from the general solution form a basis $\mathcal B$ of our eigenspace:

$$


\begin{aligned}−1 \\ 1 \\ 0\end{aligned}


$$

In particular, we have $\dim(V_{-3}) =2.$

### Example: Finding a Basis of a One-Dimensional Eigenspace

#### Question

$$


\begin{aligned}−4 & −5 & 8 \\ 0 & −4 & 3 \\ 0 & 0 & −1\end{aligned}


$$

Consider the matrix $A$ shown above. Find a basis of the eigenspace corresponding to the eigenvalue $\lambda=-4.$

#### Explanation

To compute the eigenvectors of a matrix, we need to find non-zero solutions of the matrix equation

$$


(A - \lambda I) \textbf{x}=\mathbf{0}.


$$

In our case, we have $\lambda =-4.$ So, we get

$$


\begin{aligned}𝐴−𝜆𝐼 & =\begin{matrix}−4 & −5 & 8 \\ 0 & −4 & 3 \\ 0 & 0 & −1\end{matrix}−(−4)\begin{matrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{matrix}=\begin{matrix}0 & −5 & 8 \\ 0 & 0 & 3 \\ 0 & 0 & 3\end{matrix}.\end{aligned}


$$

To find the eigenvectors, we have to solve the corresponding homogeneous system of linear equations:

$$


\begin{aligned}−5𝑥_{2}+8𝑥_{3}=0 \\ 3𝑥_{3}=0 \\ 3𝑥_{3}=0\end{aligned}


$$

So, we row-reduce the augmented matrix $M$ to row echelon form using Gaussian elimination, as follows:

$$


\begin{aligned}𝑀 & =\begin{matrix}0 & −5 & 8 & 0 \\ 0 & 0 & 3 & 0 \\ 0 & 0 & 3 & 0\end{matrix} & & \begin{matrix}𝑅_{3}:=𝑅_{3}+(−1)𝑅_{2}\end{matrix} \\ & ∼\begin{matrix}0 & −5 & 8 & 0 \\ 0 & 0 & 3 & 0 \\ 0 & 0 & 0 & 0\end{matrix} & & \end{aligned}


$$

In the reduced matrix above, there are two pivot columns (the $2$nd and the $3$rd). Thus, $x_1$ is a free variable. From the second equation, we obtain $x_3=0.$ Substituting this into the first equation, we get $x_2=0.$

So, the general solution is

$$


\begin{aligned}𝑥_{1} \\ 0 \\ 0\end{aligned}


$$

Therefore, the required basis is

$$


\begin{aligned}1 \\ 0 \\ 0\end{aligned}


$$

### Example: Finding a Basis of a Two-Dimensional Eigenspace

#### Question

$$


\begin{aligned}−8 & 8 & −6 \\ −15 & 14 & −9 \\ −5 & 4 & −1\end{aligned}


$$

Consider the matrix $A$ shown above. Find a basis of the eigenspace corresponding to the eigenvalue $\lambda=2?$

#### Explanation

To compute the eigenvectors of a matrix, we need to find non-zero solutions of the matrix equation

$$


(A - \lambda I) \textbf{x}=\mathbf{0}.


$$

In our case, we have $\lambda =2.$ So, we get

$$


\begin{aligned}𝐴−𝜆𝐼 & =\begin{matrix}−8 & 8 & −6 \\ −15 & 14 & −9 \\ −5 & 4 & −1\end{matrix}−2\begin{matrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{matrix}=\begin{matrix}−10 & 8 & −6 \\ −15 & 12 & −9 \\ −5 & 4 & −3\end{matrix}.\end{aligned}


$$

To find the eigenvectors, we have to solve the corresponding homogeneous system of linear equations:

$$


\begin{aligned}−10𝑥_{1}+8𝑥_{2}−6𝑥_{3}=0 \\ −15𝑥_{1}+12𝑥_{2}−9𝑥_{3}=0 \\ −5𝑥_{1}+4𝑥_{2}−3𝑥_{3}=0\end{aligned}


$$

So, we row-reduce the augmented matrix $M$ to row echelon form using Gaussian elimination, as follows:

$$


\begin{aligned}𝑀 & =\begin{matrix}−10 & 8 & −6 & 0 \\ −15 & 12 & −9 & 0 \\ −5 & 4 & −3 & 0\end{matrix} & & \begin{matrix}𝑅_{1}:=−\frac{1}{2}𝑅_{1}\end{matrix} \\ & ∼\begin{matrix}5 & −4 & 3 & 0 \\ −15 & 12 & −9 & 0 \\ −5 & 4 & −3 & 0\end{matrix} & & \begin{matrix}𝑅_{2}:=𝑅_{2}+3𝑅_{1} \\ 𝑅_{3}:=𝑅_{3}+𝑅_{1}\end{matrix} \\ & ∼\begin{matrix}5 & −4 & 3 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0\end{matrix} & & \end{aligned}


$$

In the reduced matrix above, there is one pivot column (the $1$st one). Thus, $x_2$ and $x_3$ are free variables. From the first equation, we obtain $x_1=\dfrac 4 5x_2-\dfrac35x_3.$ So, the general solution is

$$


\begin{aligned}\frac{4}{5}𝑥_{2}−\frac{3}{5}𝑥_{3} \\ 𝑥_{2} \\ 𝑥_{3}\end{aligned}


$$

Therefore, the required basis is

$$


\begin{aligned}4 \\ 5 \\ 0\end{aligned}


$$

### Example: Finding Linearly Independent Eigenvectors of a 3x3 Matrix

#### Question

$$


\begin{aligned}7 & −6 & 5 \\ 6 & −8 & 10 \\ 0 & 0 & 4\end{aligned}


$$

Consider the matrix $A$ and vectors $\mathbf{v}_1,\mathbf{v}_2$ shown above. If $\mathbf{v}_1$ and $\mathbf{v}_2$ are two linearly independent eigenvectors corresponding to the eigenvalue $\lambda=4,$ what is the value of $a+b?$

#### Explanation

To compute the eigenvectors of a matrix, we need to find non-zero solutions of the matrix equation

$$


(A - \lambda I) \textbf{x}=\mathbf{0}.


$$

In our case, we have $\lambda =4.$ So, we get

$$


\begin{aligned}𝐴−𝜆𝐼 & =\begin{matrix}7 & −6 & 5 \\ 6 & −8 & 10 \\ 0 & 0 & 4\end{matrix}−4\begin{matrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{matrix}=\begin{matrix}3 & −6 & 5 \\ 6 & −12 & 10 \\ 0 & 0 & 0\end{matrix}.\end{aligned}


$$

To find the eigenvectors, we have to solve the corresponding homogeneous system of linear equations:

$$


\begin{aligned}3𝑥_{1}−6𝑥_{2}+5𝑥_{3}=0 \\ 6𝑥_{1}−12𝑥_{2}+10𝑥_{3}=0 \\ 0=0\end{aligned}


$$

So, we row-reduce the augmented matrix $M$ to row echelon form using Gaussian elimination, as follows:

$$


\begin{aligned}𝑀 & =\begin{matrix}3 & −6 & 5 & 0 \\ 6 & −12 & 10 & 0 \\ 0 & 0 & 0 & 0\end{matrix} & & 𝑅_{2}:=𝑅_{2}+(−2)𝑅_{1} \\ & ∼\begin{matrix}3 & −6 & 5 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0\end{matrix} & & \end{aligned}


$$

In the reduced matrix above, there is one pivot column (the $1$st one). Thus, $x_2$ and $x_3$ are free variables. On the other hand, from the first equation, we obtain $x_1=2x_2-\dfrac{5}{3}x_3.$

Hence, the general solution is

$$


\begin{aligned}2𝑥_{2}−\frac{5}{3}𝑥_{3} \\ 𝑥_{2} \\ 𝑥_{3}\end{aligned}


$$

We now deduce the eigenvectors $\mathbf v_1$ and $\mathbf v_2\mathbin:$

- Since $\begin{aligned}𝑎 \\ 1 \\ 0\end{aligned}$ we must have that $x_2=1$ and $x_3=0.$ As a result, $a=2(1)-\dfrac 53(0)=2.$

- Since $\begin{aligned}𝑏 \\ 0 \\ 3\end{aligned}$ we must have that $x_2=0$ and $x_3=3.$ As a result, $b=2(0)-\dfrac53(3)=-5.$

Therefore, $a+b=2+(-5)=-3.$

### Dimensions of Eigenspaces

In general, given an eigenvalue $\lambda$ of a matrix $A,$ we can have the following two situations:

- If $\lambda$ is a simple root of the characteristic equation, then the eigenspace $V_{\lambda}$ has dimension $1\mathbin{:}$

- If $\lambda$ is *not* a simple root of the characteristic equation (it's a double, triple, quadruple root, etc.), the dimension of the eigenspace $V_{\lambda}$ equals the number of free variables in the system of linear equations corresponding to

**Watch out!** The second rule does *not* claim that if an eigenvalue is, say, a double root, then $\text{dim}(V_{\lambda}) = 2.$ It says that we have to examine the corresponding linear system and only then make the conclusion depending on the number of free variables.

However, there is one thing we can determine about the dimension of the eigenspace, and it is given by the following theorem.

*If an eigenvalue $\lambda$ is a root of multiplicity $k$ in the corresponding characteristic equation, then the eigenspace $V_{\lambda}$ has dimension not greater than $k \mathbin{:}$*

Recall that the multiplicity of an eigenvalue as a root of the characteristic equation is called *algebraic multiplicity*. On the other hand, the dimension of the corresponding eigenspace is called the **geometric multiplicity** of the eigenvalue. Our theorem above states the following:

*The geometric multiplicity of an eigenvalue is always less than or equal to the algebraic multiplicity.*

### Example: Calculating the Dimension of an Eigenspace

#### Question

$$


\begin{aligned}1 & 6 & −3 \\ 0 & −2 & 0 \\ 1 & 2 & −3\end{aligned}


$$

Consider the matrix $A$ shown above. What are the dimensions of the eigenspaces $V_{0}$ and $V_{-2}$ corresponding to eigenvalues $\lambda=0$ and $\lambda=-2$ of $A$, respectively?

#### Explanation

First, we write down the characteristic equation $\text{det}(A-\lambda I)=0\mathbin{:}$

$$


\begin{aligned}det(𝐴−𝜆𝐼)=0 \\ \begin{matrix}1−𝜆 & 6 & −3 \\ 0 & −2−𝜆 & 0 \\ 1 & 2 & −3−𝜆\end{matrix}=0 \\ (−2−𝜆)\begin{matrix}1−𝜆 & −3 \\ 1 & −3−𝜆\end{matrix}=0 \\ (−2−𝜆)((1−𝜆)(−3−𝜆)+3)=0 \\ −(𝜆+2)(𝜆^{2}+2𝜆)=0 \\ 𝜆(𝜆+2)^{2}=0.\end{aligned}


$$

Hence, $\lambda_1=0$ (simple root) and $\lambda_2=\lambda_3=-2$ (double root).

Let's now consider the eigenspaces corresponding to each eigenvector:

- First, we consider $\lambda=0.$ Since $V_{0}$ corresponds to a simple root, we obtain

- Then, we consider $\lambda=-2,$ which is a repeated root of the characteristic equation. To find the dimension of $V_{-2},$ we row-reduce the matrix $(A - (-2) I) \textbf{x}=\mathbf{0}\mathbin{:}$ In the reduced matrix above, there is one pivot column (the $1$st one). This implies that we will have $3-1=2$ linearly independent eigenvectors corresponding to the eigenvalue $\lambda = -2.$ Therefore,
