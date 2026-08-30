# Finding Complex Eigenvectors of Real 2x2 Matrices

Source: https://www.mathacademy.com/topics/3574?courseId=55
Topic ID: 3574

## Prerequisites

- [Finding Complex Eigenvalues of Real 2x2 Matrices](./2016-finding-complex-eigenvalues-of-real-2x2-matrices.md)

## Lesson

### Introduction

Let's find the eigenvector corresponding to the eigenvalue $\lambda=-\textrm{i}$ of the matrix $[\begin{aligned}1 & −1 \\ 2 & −1\end{aligned}]$

To compute the eigenvectors of a matrix, we need to find non-zero solutions of the matrix equation

$$


(A - \lambda I) \textbf{x}=\mathbf{0}.


$$

In our case, we have $\,\lambda =-\textrm{i},$ and

$$


\begin{aligned}𝐴−𝜆𝐼 & =[\begin{aligned}1 & −1 \\ 2 & −1\end{aligned}]−[\begin{aligned}−i & 0 \\ 0 & −i\end{aligned}] \\ & =[\begin{aligned}1+i & −1 \\ 2 & −1+i\end{aligned}].\end{aligned}


$$

So, we have the homogeneous system of linear equations

$$


\begin{aligned}(1+i)𝑥_{1}−𝑥_{2}=0 \\ 2𝑥_{1}+(−1+i)𝑥_{2}=0.\end{aligned}


$$

Now, since the matrix $A-(-\textrm{i})I$ is singular, the system above must have a non-zero solution. This means that one equation of the system is a multiple of another.

As a result, we can drop one of the rows and take one of the variables as the free variable. For example, from the first equation, we get

$$


x_2 = (1+\textrm{i})x_1.


$$

Therefore, by setting $x_1\in\mathbb C$ to be the free variable, we find that the general solution to our system is given by

$$


[\begin{aligned}𝑥_{1} \\ (1+i)𝑥_{1}\end{aligned}]


$$

Setting $x_1=1,$ we get the eigenvector

$$


[\begin{aligned}1 \\ 1+i\end{aligned}]


$$

Notice that our eigenvector has complex-valued entries.

**Note:** To check our result, we can show that $A\mathbf v = \lambda \mathbf v.$ Computing $A\mathbf v,$ we get

$$


\begin{aligned}𝐴𝐯 & =[\begin{aligned}1 & −1 \\ 2 & −1\end{aligned}][\begin{aligned}1 \\ 1+i\end{aligned}]=[\begin{aligned}−i \\ 1−i\end{aligned}],\end{aligned}


$$

and computing $\lambda \mathbf v$ gives

$$


[\begin{aligned}1 \\ 1+i\end{aligned}]


$$

So $A\mathbf v = \lambda \mathbf v,$ as required.

### Example: Finding a Complex Eigenvalue of a Matrix Given a Complex Eigenvector

#### Question

Determine whether $[\begin{aligned}1+3i \\ 4\end{aligned}]$ is an eigenvector of the matrix $[\begin{aligned}2 & −5 \\ 8 & −2\end{aligned}]$ If so, then what is the corresponding eigenvalue?

#### Explanation

The eigenvectors of $A$ are the non-zero vectors $\mathbf{v}$ such that $A\mathbf{v}=\lambda \mathbf{v}.$ So, we have

$$


\begin{aligned}𝐴𝐯 & =[\begin{aligned}2 & −5 \\ 8 & −2\end{aligned}][\begin{aligned}1+3i \\ 4\end{aligned}] \\ & =[\begin{aligned}−18+6i \\ 24i\end{aligned}] \\ & =[\begin{aligned}18i^{2}+6i \\ 24i\end{aligned}] \\ & =6i[\begin{aligned}1+3i \\ 4\end{aligned}] \\ & =6i𝐯.\end{aligned}


$$

Since $A\mathbf{v} = 6\textrm{i} \mathbf{v},$ we conclude that $\mathbf{v}$ is an eigenvector of $A$ and the corresponding eigenvalue is $\lambda=6\textrm{i}.$

### Example: Finding a Complex Eigenvector of a Matrix Given a Complex Eigenvalue

#### Question

Find an eigenvector of $[\begin{aligned}−3 & 4 \\ −4 & −3\end{aligned}]$ that corresponds to the eigenvalue $\lambda=-3+4\textrm{i}.$

#### Explanation

To compute the eigenvectors of a matrix, we need to find non-zero solutions of the matrix equation

$$


(A - \lambda I) \textbf{x}=\mathbf{0}.


$$

In our case, we have $\,\lambda =-3+4\textrm{i},$ and

$$


\begin{aligned}𝐴−𝜆𝐼 & =[\begin{aligned}−3 & 4 \\ −4 & −3\end{aligned}]−[\begin{aligned}−3+4i & 0 \\ 0 & −3+4i\end{aligned}] \\ & =[\begin{aligned}−4i & 4 \\ −4 & −4i\end{aligned}].\end{aligned}


$$

So, we have the homogeneous system of linear equations

$$


\begin{aligned}−4i𝑥_{1}+4𝑥_{2}=0 \\ −4𝑥_{1}−4i𝑥_{2}=0.\end{aligned}


$$

Now, since the matrix $A-(-3+4\textrm{i})I$ is singular, the system above must have a non-zero solution. This means that one equation of the system is a multiple of another.

As a result, we can drop one of the rows and take one of the variables to be the free variable. For example, from the second equation, we get

$$


x_1 = -\textrm{i}x_2.


$$

Therefore, the general solution is given by

$$


[\begin{aligned}−i𝑥_{2} \\ 𝑥_{2}\end{aligned}]


$$

Setting $x_2=1,$ we get the eigenvector $[\begin{aligned}−i \\ 1\end{aligned}]$

### Example: Finding Two Linearly Independent Complex Eigenvectors of a 2x2 Matrix

#### Question

Let $[\begin{aligned}𝑎_{1} \\ 𝑏_{1}\end{aligned}]$ and $[\begin{aligned}𝑎_{2} \\ 𝑏_{2}\end{aligned}]$ be linearly independent eigenvectors of the matrix $[\begin{aligned}4 & 5 \\ −5 & 4\end{aligned}]$ Given that $\lambda_1=4+5\textrm{i}$ is an eigenvalue of $A,$ find the value of ${\dfrac{a_1a_2}{b_1b_2}}.$

#### Explanation

To compute the eigenvectors of a matrix, we need to find non-zero solutions of the matrix equation

$$


(A - \lambda I) \textbf{x}=\mathbf{0}.


$$

In our case, we have $\,\lambda_1 =4+5\textrm{i}$ and

$$


\begin{aligned}𝐴−𝜆_{1}𝐼 & =[\begin{aligned}4 & 5 \\ −5 & 4\end{aligned}]−[\begin{aligned}4+5i & 0 \\ 0 & 4+5i\end{aligned}] \\ & =[\begin{aligned}−5i & 5 \\ −5 & −5i\end{aligned}].\end{aligned}


$$

So, we have the homogeneous system of linear equations

$$


\begin{aligned}−5i𝑥_{1}+5𝑥_{2}=0 \\ −5𝑥_{1}−5i𝑥_{2}=0.\end{aligned}


$$

Now, since the matrix $A-(4+5\textrm{i})I$ is singular, the system above must have a non-zero solution. This means that one equation of the system is a multiple of another.

As a result, we can drop one of the rows and take one of the variables as the free variable. For example, from the first equation, we get

$$


x_2 = \textrm{i}x_1.


$$

So, the general solution is given by

$$


[\begin{aligned}𝑥_{1} \\ i𝑥_{1}\end{aligned}]


$$

Setting $x_1=1,$ we get the eigenvector

$$


[\begin{aligned}1 \\ i\end{aligned}]


$$

Now, since $\lambda_1=4+5\textrm{i}$ is a complex eigenvalue of $A,$ the second eigenvalue of $A$ must be the complex conjugate of $\lambda_1.$ Therefore, we have

$$


\lambda_2=\overline{\lambda_1}=4-5\textrm{i}.


$$

Moreover, the corresponding eigenvector must be the complex conjugate of $\mathbf v_1.$ Therefore, we have

$$


[\begin{aligned}1 \\ −i\end{aligned}]


$$

Finally, we obtain

$$


{\dfrac{a_1a_2}{b_1b_2}} = {\dfrac{(1)(1)}{(\textrm{i})(-\textrm{i})}} = 1.


$$
