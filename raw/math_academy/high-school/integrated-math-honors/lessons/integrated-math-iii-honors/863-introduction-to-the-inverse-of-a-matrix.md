# Introduction to the Inverse of a Matrix

Source: https://www.mathacademy.com/topics/863?courseId=101
Topic ID: 863

## Prerequisites

- [Multiplying Square Matrices](./147-multiplying-square-matrices.md)

## Lesson

### Introduction

Given the scalar $a,$ the **multiplicative inverse** of $a$ is defined as the scalar $a^{-1}$ such that

$$


a \cdot a^{-1} = a^{-1} \cdot a = 1.


$$

For example, the multiplicative inverse of $2$ is the number $2^{-1} = \dfrac{1}{2}$ because

$$


\dfrac{1}{2}\cdot 2 = 2\cdot \dfrac{1}{2} = 1.


$$

Similarly, given a square $n \times n$ matrix $A,$ the **inverse** of $A$ is defined as the $n \times n$ matrix $A^{-1}$ such that

$$


A \cdot A^{-1} = A^{-1} \cdot A = I_n,


$$

where $I_n$ is the $n\times n$ identity matrix.

For example, suppose we're given the following $2\times 2$ matrix:

$$


[\begin{aligned}−1 & −1 \\ 1 & 2\end{aligned}]


$$

The inverse of the above matrix is given by

$$


[\begin{aligned}−2 & −1 \\ 1 & 1\end{aligned}]


$$

To verify that the above matrix is in fact the inverse of $A,$ first observe that if we multiply $A$ by the above matrix $A^{-1},$ then we get the identity matrix $I_2\mathbin{:}$

$$


\begin{aligned}\underset{𝐴}{\underset{}{[\begin{aligned}−1 & −1 \\ 1 & 2\end{aligned}]}}\underset{𝐴^{−1}}{\underset{}{[\begin{aligned}−2 & −1 \\ 1 & 1\end{aligned}]}} & =[\begin{aligned}−1⋅(−2)+(−1)⋅1 & −1⋅(−1)+(−1)⋅1 \\ 1⋅(−2)+2⋅1 & 1⋅(−1)+2⋅1\end{aligned}] \\ & =[\begin{aligned}1 & 0 \\ 0 & 1\end{aligned}] \\ & =𝐼_{2}\,✓\end{aligned}


$$

Likewise, if we multiply $A^{-1}$ by $A,$ then we also get the identity matrix $I_2\mathbin{:}$

$$


\begin{aligned}[\begin{aligned}−2 & −1 \\ 1 & 1\end{aligned}]\underset{𝐴}{\underset{}{[\begin{aligned}−1 & −1 \\ 1 & 2\end{aligned}]}} & =𝐼_{2}\,✓\end{aligned}


$$

We do not yet know how to find the inverse of a matrix. However, we can verify that one matrix is the inverse of the other by carrying out the same procedure as we did here.

### Example: Determining the Inverse of a 2x2 Matrix

#### Question

Using the method of direct verification, determine whether the matrix $B$ is the inverse of $A,$ where

$$


[\begin{aligned}1 & 0 \\ −1 & 1\end{aligned}]


$$

#### Explanation

We must check whether $AB = BA = I_2.$

Computing $AB,$ we get

$$


\begin{aligned}𝐴𝐵 & =[\begin{aligned}1 & 0 \\ −1 & 1\end{aligned}][\begin{aligned}1 & 0 \\ 1 & 1\end{aligned}] \\ & =[\begin{aligned}1 & 0 \\ 0 & 1\end{aligned}] \\ & =𝐼_{2}.\,✓\end{aligned}


$$

Likewise, computing $BA,$ we get

$$


\begin{aligned}𝐵𝐴 & =[\begin{aligned}1 & 0 \\ 1 & 1\end{aligned}][\begin{aligned}1 & 0 \\ −1 & 1\end{aligned}] \\ & =[\begin{aligned}1 & 0 \\ 0 & 1\end{aligned}] \\ & =𝐼_{2}.\,✓\end{aligned}


$$

Therefore, $B = A^{-1}.$

### Example: Determining the Inverse of a Larger Matrix

#### Question

Using the method of direct verification, determine whether the matrix $B$ is the inverse of $A,$ where

$$


\begin{aligned}1 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1\end{aligned}


$$

#### Explanation

First, we check whether $AB = BA = I_3.$

Computing $AB,$ we get

$$


\begin{aligned}𝐴𝐵 & =\begin{aligned}1 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1\end{aligned}\begin{aligned}1 & −1 & 0 \\ 0 & 1 & −1 \\ 0 & 0 & 1\end{aligned} \\ & =\begin{aligned}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{aligned} \\ & =𝐼_{3}.\,✓\end{aligned}


$$

Likewise, computing $BA,$ we get

$$


\begin{aligned}𝐵𝐴 & =\begin{aligned}1 & −1 & 0 \\ 0 & 1 & −1 \\ 0 & 0 & 1\end{aligned}\begin{aligned}1 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1\end{aligned} \\ & =\begin{aligned}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{aligned} \\ & =𝐼_{3}.\,✓\end{aligned}


$$

Therefore, $B = A^{-1}.$

### Not Every Matrix Has an Inverse

The number $0$ does not have an inverse for multiplication over the real numbers, because there's no such number $a$ that $a \cdot 0 = 1.$ Instead, for every $a$ we have $a \cdot 0 = 0.$

Similarly, not every matrix has an inverse.

- If a matrix is not square, an inverse does not exist.

- Some square matrices do not have an inverse. If a square matrix does not have an inverse, then it is said to be **singular**. An example of a singular matrix is the zero matrix

We will soon learn how to calculate the inverse of a square matrix, and we'll also soon learn how to determine when a square matrix does not have an inverse.
