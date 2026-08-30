# Calculating the Inverse of a 3x3 Matrix Using the Cofactor Method

Source: https://www.mathacademy.com/topics/154?courseId=101
Topic ID: 154

## Prerequisites

- [The Determinant of a 3x3 Matrix](./153-the-determinant-of-a-3x3-matrix.md)
- [The Transpose of a Matrix](./232-the-transpose-of-a-matrix.md)
- [Inverses of 2x2 Matrices](./864-inverses-of-2x2-matrices.md)

## Lesson

### Introduction

We can calculate the inverse of a $3\times 3$ matrix $A$ using the following five-step algorithm.

**Step 1:** Find the determinant $\det(A)$ of the matrix.

**Step 2:** Form the **matrix $M$ of the minors** of $A,$ where each entry $a_{ij}$ of $A$ is replaced by its minor $M_{ij}\mathbin{:}$

$$


\begin{aligned}𝑀_{11} & 𝑀_{12} & 𝑀_{13} \\ 𝑀_{21} & 𝑀_{22} & 𝑀_{23} \\ 𝑀_{31} & 𝑀_{32} & 𝑀_{33}\end{aligned}


$$

**Step 3:** Create the **matrix $C$ of cofactors** by changing the sign of some entries of the matrix of the minors according to the **rule of alternating signs**:

$$


\begin{aligned}+ & − & + \\ − & + & − \\ + & − & +\end{aligned}


$$

For each entry of $M$, we change the sign if the corresponding sign in the pattern is "$-$". Otherwise, if the corresponding sign in the pattern is "$+$", then we don't change the entry.

So, the matrix of cofactors is given by

$$


\begin{aligned}𝑀_{11} & −𝑀_{12} & 𝑀_{13} \\ −𝑀_{21} & 𝑀_{22} & −𝑀_{23} \\ 𝑀_{31} & −𝑀_{32} & 𝑀_{33}\end{aligned}


$$

**Step 4:** Write down the transpose of the matrix of cofactors, $C^T.$

$$


\begin{aligned}𝑀_{11} & −𝑀_{21} & 𝑀_{31} \\ −𝑀_{12} & 𝑀_{22} & −𝑀_{32} \\ 𝑀_{13} & −𝑀_{23} & 𝑀_{33}\end{aligned}


$$

**Step 5:** Use the formula for the inverse of a $3\times 3$ matrix:

$$


A^{-1} = \dfrac{1}{\det ( A)}C^{T}


$$

In other words, we divide each entry of the transpose of the matrix of cofactors by the determinant of the original matrix (which we computed in step 1).

Let's see this in practice, in the next example.

### Example: Calculating the Inverse of a 3x3 Matrix Using the Matrix of Cofactors

#### Question

Find the inverse of $\begin{aligned}0 & 1 & 2 \\ 1 & 0 & 3 \\ 4 & −3 & 8\end{aligned}$

#### Explanation

Let's follow the standard five-step procedure.

**** Find the determinant of $A.$

$$


\begin{aligned}det(𝐴)=\begin{aligned}0 & 1 & 2 \\ 1 & 0 & 3 \\ 4 & −3 & 8\end{aligned} & =0\begin{aligned}0 & 3 \\ −3 & 8\end{aligned}−1\begin{aligned}1 & 3 \\ 4 & 8\end{aligned}+2\begin{aligned}1 & 0 \\ 4 & −3\end{aligned} \\ & =0−(8−12)+2(−3−0) \\ & =−2\end{aligned}


$$

**** Form the matrix of the minors of $A.$ To make this matrix, we replace each entry of $A$ by its minor.

$$


\begin{aligned}𝑀 & =\begin{aligned}\begin{aligned}0 & 3 \\ −3 & 8\end{aligned} & \begin{aligned}1 & 3 \\ 4 & 8\end{aligned} & \begin{aligned}1 & 0 \\ 4 & −3\end{aligned} \\ \begin{aligned}1 & 2 \\ −3 & 8\end{aligned} & \begin{aligned}0 & 2 \\ 4 & 8\end{aligned} & \begin{aligned}0 & 1 \\ 4 & −3\end{aligned} \\ \begin{aligned}1 & 2 \\ 0 & 3\end{aligned} & \begin{aligned}0 & 2 \\ 1 & 3\end{aligned} & \begin{aligned}0 & 1 \\ 1 & 0\end{aligned}\end{aligned} \\ & =\begin{aligned}9 & −4 & −3 \\ 14 & −8 & −4 \\ 3 & −2 & −1\end{aligned}\end{aligned}


$$

**** Create the matrix of cofactors by changing the sign of some of the entries of $M$ according to the rule of alternating signs.

$$


\begin{aligned}9 & −(−4) & −3 \\ −(14) & −8 & −(−4) \\ 3 & −(−2) & −1\end{aligned}


$$

**** Write down the transpose of the matrix of cofactors.

$$


\begin{aligned}9 & −14 & 3 \\ 4 & −8 & 2 \\ −3 & 4 & −1\end{aligned}


$$

**** Use the formula for the inverse of a $3\times 3$ matrix.

$$


\begin{aligned}𝐴^{−1} & =\frac{1}{det(𝐴)}𝐶^{𝑇} \\ & =\frac{1}{−2}\begin{aligned}9 & −14 & 3 \\ 4 & −8 & 2 \\ −3 & 4 & −1\end{aligned} \\ & =−\frac{1}{2}\begin{aligned}9 & −14 & 3 \\ 4 & −8 & 2 \\ −3 & 4 & −1\end{aligned} \\ & =\begin{aligned}−\frac{9}{2} & 7 & −\frac{3}{2} \\ −2 & 4 & −1 \\ \frac{3}{2} & −2 & \frac{1}{2}\end{aligned}\end{aligned}


$$

### Calculating Individual Entries of the Matrix of Cofactors

We make the matrix $C$ of cofactors by changing the sign of alternate entries of the matrix $M$ of the minors. So, each entry $c_{ij}$ of $C$ equals

$$


c_{ij} = (-1)^{i+j} M_{ij},


$$

where $M_{ij}$ is the minor of the entry $a_{ij}$ in the matrix $A.$

With this and the formula for the inverse, we can write the formula for each entry $a'_{ij}$ of the inverse matrix $A^{-1}$ as follows:

$$


a'_{ij} = \dfrac{1}{\det(A)}c^t_{ij} = \dfrac{1}{\det(A)} c_{ji}


$$

Here, we used the fact that the entry $c^t_{ij}$ of $C^T$ is equal to the entry $c_{ji}$ of $C$ by the definition of the transpose.

### Example: Calculating an Element of the Inverse of a 3x3 Matrix

#### Question

Determine the entry $a'_{23}$ in the inverse of the matrix $\begin{aligned}−2 & 3 & −3 \\ 0 & 1 & 0 \\ 1 & −1 & 2\end{aligned}$

#### Explanation

First, we need to find the determinant of $A\mathbin{:}$

$$


\begin{aligned}det(𝐴)=\begin{aligned}−2 & 3 & −3 \\ 0 & 1 & 0 \\ 1 & −1 & 2\end{aligned} & =−2\begin{aligned}1 & 0 \\ −1 & 2\end{aligned}−3\begin{aligned}0 & 0 \\ 1 & 2\end{aligned}+(−3)\begin{aligned}0 & 1 \\ 1 & −1\end{aligned} \\ & =−2(2−0)−3(0−0)−3(0−1) \\ & =−1\end{aligned}


$$

Since we want the entry $a'_{23}$ in $A^{-1},$ we need to know the value of $c_{32}$ in the matrix of cofactors. For this, we use the formula to get

$$


\begin{aligned}𝑐_{32} & =(−1)^{3+2}𝑀_{32} \\ & =(−1)^{5}\begin{aligned}−2 & −3 \\ 0 & 0\end{aligned} \\ & =−1⋅(0) \\ & =0.\end{aligned}


$$

Then, since $A^{-1}=\dfrac{1}{\det (A)}C^{T},$ we have

$$


a'_{23} = \dfrac{1}{-1}c_{32} = -1\cdot 0 = 0.


$$

### Example: Calculating the Cofactor Method To Solve for an Unknown Quantity

#### Question

The entry $a'_{31}$ in the inverse of the matrix $\begin{aligned}3 & 2 & −2 \\ −2 & 𝑘 & 0 \\ −1 & −3 & 3\end{aligned}$ equals $1$. Find the value of $k$.

#### Explanation

First, we need to find the determinant of $A\mathbin{:}$

$$


\begin{aligned}det(𝐴)=\begin{aligned}3 & 2 & −2 \\ −2 & 𝑘 & 0 \\ −1 & −3 & 3\end{aligned} & =3\begin{aligned}𝑘 & 0 \\ −3 & 3\end{aligned}−2\begin{aligned}−2 & 0 \\ −1 & 3\end{aligned}+(−2)\begin{aligned}−2 & 𝑘 \\ −1 & −3\end{aligned} \\ & =3(3𝑘−0)−2(−6−0)−2(6+𝑘) \\ & =9𝑘+12−12−2𝑘 \\ & =7𝑘.\end{aligned}


$$

Since we want the entry $a'_{31}$ in $A^{-1},$ we need to know the value of $c_{13}$ in the matrix of cofactors. For this, we use the formula to get

$$


\begin{aligned}𝑐_{13} & =(−1)^{1+3}\begin{aligned}−2 & 𝑘 \\ −1 & −3\end{aligned} \\ & =\begin{aligned}−2 & 𝑘 \\ −1 & −3\end{aligned} \\ & =6+𝑘.\end{aligned}


$$

Then, since $A^{-1}=\dfrac{1}{\det (A)}C^{T},$ we have

$$


\begin{aligned}𝑎_{′31}^{} & =\frac{1}{det(𝐴)}𝑐_{13} \\ & =\frac{1}{7𝑘}⋅(6+𝑘) \\ & =\frac{6+𝑘}{7𝑘}.\end{aligned}


$$

Finally, since we are told that $a'_{31}=1$, we have

$$


\begin{aligned}\frac{6+𝑘}{7𝑘} & =1 \\ 6+𝑘 & =7𝑘 \\ 6 & =6𝑘 \\ 𝑘 & =1.\end{aligned}


$$
