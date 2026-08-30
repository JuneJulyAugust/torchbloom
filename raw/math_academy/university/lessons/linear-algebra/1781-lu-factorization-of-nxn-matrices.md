# LU Factorization of NxN Matrices

Source: https://www.mathacademy.com/topics/1781?courseId=55
Topic ID: 1781

## Prerequisites

- [LU Factorization of 3x3 Matrices](./1780-lu-factorization-of-3x3-matrices.md)

## Lesson

### Introduction

In general, the LU factorization $A=LU$ of an $n\times n$ matrix $A$ is the product of two matrices $L$ and $U,$ where

$$


\begin{aligned}1 & 0 & ⋯ & 0 \\ ∗ & 1 & & 0 \\ ⋮ & & ⋱ & ⋮ \\ ∗ & ∗ & ⋯ & 1\end{aligned}


$$

is a *unit* lower triangular matrix, and

$$


\begin{aligned}∗ & ∗ & ⋯ & ∗ \\ 0 & ∗ & & ∗ \\ ⋮ & & ⋱ & ⋮ \\ 0 & 0 & ⋯ & ∗\end{aligned}


$$

is an upper triangular matrix.

As it turns out, there is a quick way of finding a matrix's LU factorization, which is particularly helpful when factoring large matrices.

Let's see a concrete example of how this works.

### A Worked Example

Suppose we want to find the LU factorization $A=LU$ of the matrix

$$


\begin{aligned}2 & 1 & 1 \\ 6 & 1 & 1 \\ 4 & 6 & 0\end{aligned}


$$

We proceed by reducing $A$ to row echelon form using Gaussian elimination.

To start, we want to make $0$ at the position $a_{{\color{blue}2}{\color{red}1}}.$ To do this, we take the ${\color{blue}2}$nd row of $A,$ and we add the ${\color{red}1}$st row of $A$ multiplied by ${\color{purple}-3}{:}$

$$


\begin{aligned}𝐴 & =\begin{matrix}2 & 1 & 1 \\ 6 & 1 & 1 \\ 4 & 6 & 0\end{matrix} & 𝑅_{2} & :=𝑅_{2}+(−3)𝑅_{1} \\ & ∼\begin{matrix}2 & 1 & 1 \\ 0 & −2 & −2 \\ 4 & 6 & 0\end{matrix} & & \end{aligned}


$$

Now, here's the trick. We take the factor $\color{purple}-3$ that we multiplied $R_{\color{red}1}$ by, change its sign, and write it as the entry $a_{{\color{blue}2}{\color{red}1}}$ with a box around it. This gives

$$


\begin{aligned}𝐴 & ∼\begin{matrix}2 & 1 & 1 \\ \,3\, & −2 & −2 \\ 4 & 6 & 0\end{matrix}.\,\,(∗)\end{aligned}


$$

**Important**:

- You can think of the box $\boxed{\color{purple}\:\phantom{3}\:}$ as representing the original zero.

- In addition, we store the value $\color{purple}3$ to use later.

- When doing this in practice, you might find it helpful to write a large zero with a small $\color{purple}3$ inside it. This is represented by $\boxed{\color{purple}\:3\:}$ in our matrix above.

Let's now continue with our Gaussian elimination.

We want to make $0$ at the position $a_{{\color{blue}3}{\color{red}1}}.$ To do this, we take the ${\color{blue}3}$rd row of $(\ast)$ and we add the ${\color{red}1}$st row multiplied by ${\color{purple}-2}.$ Then, we place $-({\color{purple}-2})={\color{purple}2}$ with a box around it at the position $a_{{\color{blue}3}{\color{red}1}}{:}$

$$


\begin{aligned}𝐴 & ∼\begin{matrix}2 & 1 & 1 \\ \,3\, & −2 & −2 \\ 4 & 6 & 0\end{matrix} & 𝑅_{3} & :=𝑅_{3}+(−2)𝑅_{1} \\ & ∼\begin{matrix}2 & 1 & 1 \\ \,3\, & −2 & −2 \\ \,2\, & 4 & −2\end{matrix} & & \end{aligned}


$$

Finally, we want to make $0$ at the position $a_{{\color{blue}3}{\color{red}2}}.$ To do this, we take the ${\color{blue}3}$rd row and we add the ${\color{red}2}$nd row multiplied by ${\color{purple}2}.$ Then, we place $-({\color{purple}2})={\color{purple}-2}$ with a box around it at the position $a_{{\color{blue}3}{\color{red}2}}{:}$

$$


\begin{aligned}𝐴 & =\begin{matrix}2 & 1 & 1 \\ \,3\, & −2 & −2 \\ \,2\, & 4 & −2\end{matrix} & 𝑅_{3} & :=𝑅_{3}+2𝑅_{2} \\ & ∼\begin{matrix}2 & 1 & 1 \\ \,3\, & −2 & −2 \\ \,2\, & −2 & −6\end{matrix} & & \end{aligned}


$$

The matrix is now in row echelon form (remember that the boxes each represent zero), and we're almost done.

Now, here's the neat bit. Both $L$ and $U$ can be extracted from the matrix above:

- The matrix $L$ takes all elements that lie *below* the main diagonal: Remember that $L$ must be *unit* lower triangular.

- The matrix $U$ takes the remaining elements: Remember that $U$ must be upper triangular.

### Example: Finding Missing Numbers in the Matrix U of an LU Factorization

#### Question

$$


\begin{aligned}1 & −5 & 6 \\ 4 & −9 & 8 \\ 6 & −8 & 10\end{aligned}


$$

Consider the LU factorization of the matrix $A$ above. What is the value of $u_{33}$ in the matrix $U?$

#### Explanation

The matrix $U$ in the LU decomposition is obtained from the original matrix $A$ by row-reducing using Gaussian elementation. In particular, to make zeros below the main diagonal, we proceed as follows:

$$


\begin{aligned}𝐴 & =\begin{matrix}1 & −5 & 6 \\ 4 & −9 & 8 \\ 6 & −8 & 10\end{matrix} & 𝑅_{2} & :=𝑅_{2}+(−4)𝑅_{1} \\ & ∼\begin{matrix}1 & −5 & 6 \\ 0 & 11 & −16 \\ 6 & −8 & 10\end{matrix} & 𝑅_{3} & :=𝑅_{3}+(−6)𝑅_{1} \\ & ∼\begin{matrix}1 & −5 & 6 \\ 0 & 11 & −16 \\ 0 & 22 & −26\end{matrix} & 𝑅_{3} & :=𝑅_{3}+(−2)𝑅_{2} \\ & ∼\begin{matrix}1 & −5 & 6 \\ 0 & 11 & −16 \\ 0 & 0 & 6\end{matrix} & & \end{aligned}


$$

Therefore, $u_{33}=6.$

### Example: Finding Missing Numbers in the Matrix L of an LU Factorization

#### Question

$$


\begin{aligned}1 & 2 & −3 \\ 2 & −6 & 1 \\ 4 & 8 & −10\end{aligned}


$$

Consider the LU factorization of the matrix $A$ above. What is the value of the entry $l_{31}$ in the matrix $L?$

#### Explanation

We want to make $0$ at the position $a_{{\color{blue}3}{\color{red}1}}$ using Gaussian elimination. To do this, we take the ${\color{blue}3}$rd row of $A,$ and we add the ${\color{red}1}$st row of $A$ multiplied by ${\color{purple}-4}{:}$

$$


\begin{aligned}𝐴 & =\begin{matrix}1 & 2 & −3 \\ 2 & −6 & 1 \\ 4 & 8 & −10\end{matrix} & 𝑅_{3} & :=𝑅_{3}+(−4)𝑅_{1} \\ & ∼\begin{matrix}1 & 2 & −3 \\ 2 & −6 & 1 \\ 0 & 0 & 2\end{matrix} & & \end{aligned}


$$

The entry $l_{{\color{blue}3}{\color{red}1}}$ of the matrix $L$ is the factor next to $R_1,$ taken with the opposite sign:

$$


l_{31}=-({\color{purple}-4})=4


$$

### Example: Finding the LU Factorization of a 3x3 Matrix

#### Question

$$


\begin{aligned}2 & 7 & 1 \\ −6 & 3 & −12 \\ −4 & 10 & 1\end{aligned}


$$

If $A=LU$ is the LU decomposition of the matrix $A$ given above, what is the value of $l_{31} \cdot u_{23}?$

#### Explanation

Let's apply our standard LU factorization algorithm.

We reduce the matrix $A$ to row echelon form to obtain the matrix $U,$ as usual. However, instead of writing zeros below the main diagonal, we will instead write down the entries of the matrix $L.$

$$


\begin{aligned}𝐴 & =\begin{matrix}2 & 7 & 1 \\ −6 & 3 & −12 \\ −4 & 10 & 1\end{matrix} & 𝑅_{2} & :=𝑅_{2}+3𝑅_{1} \\ & ∼\begin{matrix}2 & 7 & 1 \\ −3 & 24 & −9 \\ −4 & 10 & 1\end{matrix} & 𝑅_{3} & :=𝑅_{3}+2𝑅_{1} \\ & ∼\begin{matrix}2 & 7 & 1 \\ −3 & 24 & −9 \\ −2 & 24 & 3\end{matrix} & 𝑅_{3} & :=𝑅_{3}+(−1)𝑅_{2} \\ & ∼\begin{matrix}2 & 7 & 1 \\ −3 & 24 & −9 \\ −2 & \,1\, & 12\end{matrix} & & \end{aligned}


$$

Therefore, we obtain

$$


\begin{aligned}1 & 0 & 0 \\ −3 & 1 & 0 \\ −2 & 1 & 1\end{aligned}


$$

Finally, since $l_{31}=-2$ and $u_{23}=-9,$ we get

$$


l_{31} \cdot u_{23} = (-2) \cdot (-9) =18.


$$

### Example: Finding the LU Factorization of a 4x4 Matrix

#### Question

$$


\begin{aligned}6 & 6 & −6 & 8 \\ 0 & −2 & 0 & −3 \\ −6 & −6 & 9 & −7 \\ 0 & 4 & 6 & 9\end{aligned}


$$

If $A=LU$ is the LU decomposition of the matrix $A$ given above, what is the value of $l_{42} \cdot u_{24}?$

#### Explanation

Let's apply our standard LU factorization algorithm.

We reduce the matrix $A$ to row echelon form to obtain the matrix $U,$ as usual. However, instead of writing zeros below the main diagonal, we will instead write down the entries of the matrix $L.$

$$


\begin{aligned}𝐴 & =\begin{matrix}6 & 6 & −6 & 8 \\ 0 & −2 & 0 & −3 \\ −6 & −6 & 9 & −7 \\ 0 & 4 & 6 & 9\end{matrix} & 𝑅_{3} & :=𝑅_{3}+1𝑅_{1} \\ & ∼\begin{matrix}6 & 6 & −6 & 8 \\ 0 & −2 & 0 & −3 \\ −1 & 0 & 3 & 1 \\ 0 & 4 & 6 & 9\end{matrix} & 𝑅_{4} & :=𝑅_{4}+2𝑅_{2} \\ & ∼\begin{matrix}6 & 6 & −6 & 8 \\ 0 & −2 & 0 & −3 \\ −1 & 0 & 3 & 1 \\ 0 & −2 & 6 & 3\end{matrix} & 𝑅_{4} & :=𝑅_{4}+(−2)𝑅_{3} \\ & ∼\begin{matrix}6 & 6 & −6 & 8 \\ 0 & −2 & 0 & −3 \\ −1 & 0 & 3 & 1 \\ 0 & −2 & \,2\, & 1\end{matrix} & & \end{aligned}


$$

Therefore, we obtain

$$


\begin{aligned}1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ −1 & 0 & 1 & 0 \\ 0 & −2 & 2 & 1\end{aligned}


$$

Finally, since $l_{42}=-2$ and $u_{24}=-3,$ we get

$$


l_{42} \cdot u_{24} = (-2) \cdot (-3) =6.


$$
