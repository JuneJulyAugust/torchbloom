# Multiplying a Matrix by the Identity Matrix

Source: https://www.mathacademy.com/topics/1171?courseId=136
Topic ID: 1171

## Prerequisites

- [Multiplying Square Matrices](./147-multiplying-square-matrices.md)
- [Multiplying a Matrix by a Column Vector](./1195-multiplying-a-matrix-by-a-column-vector.md)

## Lesson

### Introduction

Remember that the **identity matrix** $I_n$ is an $n \times n$ square matrix with $1$'s on the diagonal, and where all other elements are $0.$ For example, the $3 \times 3$ identity matrix $I_3$ is given below:

$$


\begin{aligned}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{aligned}


$$

The identity matrix gets its name from the fact that whenever we multiply a matrix by the corresponding identity matrix, the matrix remains unchanged.

For example, let's consider the matrix

$$


\begin{aligned}−2 & 3 & 10 \\ 6 & −2 & 2 \\ 23 & 4 & 8\end{aligned}


$$

Multiplying the matrix $A$ by the identity matrix $I_3,$ we find that the result is just $A$ itself:

$$


\begin{aligned}𝐴⋅𝐼_{3} & =\begin{matrix}−2 & 3 & 10 \\ 6 & −2 & 2 \\ 23 & 4 & 8\end{matrix}\begin{matrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{matrix} \\ & =\begin{matrix}(−2)⋅1+3⋅0+10⋅0 & (−2)⋅0+3⋅1+10⋅0 & (−2)⋅0+3⋅0+10⋅1 \\ 6⋅1+(−2)⋅0+2⋅0 & 6⋅0+(−2)⋅1+2⋅0 & 6⋅0+(−2)⋅0+2⋅1 \\ 23⋅1+4⋅0+8⋅0 & 23⋅0+4⋅1+8⋅0 & 23⋅0+4⋅0+8⋅1\end{matrix} \\ & =\begin{matrix}−2 & 3 & 10 \\ 6 & −2 & 2 \\ 23 & 4 & 8\end{matrix} \\ & =𝐴\end{aligned}


$$

Therefore, $A \cdot I_3 = A.$ You can check that $I_3 \cdot A = A$ using the same method.

This result holds in general:

For *any* square $n \times n$ matrix $A,$ we have

$$


A \cdot I_n = I_n \cdot A = A.


$$

In other words, the $n \times n$ identity matrix $I_n$ has a similar property to the number $1,$ namely that

$$


a\cdot 1 = 1\cdot a = a


$$

for any real number $a.$

### Example: Multiplying a Matrix by the Identity Matrix

#### Question

Calculate the product $I_3 B$ given that $I_3$ is the $3 \times 3$ identity matrix and $\begin{aligned}2 & 3 & −1 \\ 5 & 2 & 7 \\ 0 & 4 & 6\end{aligned}$

#### Explanation

Any matrix, when multiplied by an identity matrix, remains unchanged (assuming that the multiplication is well defined).

The matrix $I_3$ is a $3 \times 3$ matrix and $B$ is a $3 \times 3$ matrix too.

Therefore, the multiplication is well defined and

$$


\begin{aligned}2 & 3 & −1 \\ 5 & 2 & 7 \\ 0 & 4 & 6\end{aligned}


$$

### Multiplying a Matrix by a Column of the Identity Matrix

Whenever we multiply a matrix $A$ by the $n$th column of the identity matrix, the result is the $n$th column of $A.$

For example, consider the matrix

$$


[\begin{aligned}3 & −1 \\ 1 & 2\end{aligned}]


$$

The first column of the identity matrix $I_2$ is given by

$$


[\begin{aligned}1 \\ 0\end{aligned}]


$$

If we multiply $A$ by the column on the *right*, we get

$$


\begin{aligned}[\begin{matrix}3 & −1 \\ 1 & 2\end{matrix}][\begin{matrix}1 \\ 0\end{matrix}] & =[\begin{matrix}3⋅1+(−1)⋅0 \\ 1⋅1+2⋅0\end{matrix}] \\ & =[\begin{matrix}3 \\ 1\end{matrix}].\end{aligned}


$$

The product is just the first column of the matrix $A.$

Using the same method, you can check for yourself that when we multiply $A$ by the second column of $I_2,$ the result is the second column of $A.$

On the other hand, if we multiply $A$ by the first *row* of the identity matrix $I_2$ on the *left*, we will obtain the first row of $A$. Indeed,

$$


\begin{aligned}[\begin{matrix}1 & 0\end{matrix}][\begin{matrix}3 & −1 \\ 1 & 2\end{matrix}] & =[\begin{matrix}3⋅1+1⋅0 & (−1)⋅1+2⋅0\end{matrix}] \\ & =[\begin{matrix}3 & −1\end{matrix}].\end{aligned}


$$

### Example: Multiplying a Matrix by a Column or Row of the Identity Matrix

#### Question

Calculate the product $C D,$ if $\begin{aligned}2 & 1 & 0 \\ −1 & 1 & −4 \\ 5 & 4 & −2\end{aligned}$ and $\begin{aligned}0 \\ 1 \\ 0\end{aligned}$

#### Explanation

Notice that $D$ is the $2$nd ** of the identity matrix $I_3.$

Since we're multiplying the $3\times 3$ matrix $C$ by the $2$nd ** of the identity matrix $I_3,$ the result must be the $2$nd ** of $C.$ Therefore,

$$


\begin{aligned}1 \\ 1 \\ 4\end{aligned}


$$

Don't believe it? Let's check the long way:

$$


\begin{aligned}𝐶𝐷 & =\begin{matrix}2 & 1 & 0 \\ −1 & 1 & −4 \\ 5 & 4 & −2\end{matrix}\begin{matrix}0 \\ 1 \\ 0\end{matrix} \\ & =\begin{matrix}2⋅0+1⋅1+0⋅0 \\ −1⋅0+1⋅1+(−4)⋅0 \\ 5⋅0+4⋅1+(−2)⋅0\end{matrix} \\ & =\begin{matrix}1 \\ 1 \\ 4\end{matrix}\end{aligned}


$$

### Proving Properties Related to the Identity Matrix

We've been using the fact that $AI_n = I_n A = A$ for any $n \times n$ matrix $A.$ But how do we know for sure?

Let's prove the case of $n=2.$ That is, let's prove that $AI_2=I_2A = A,$ where $A$ is any $2\times2$ matrix.

Any general $2 \times 2$ matrix can be written as $[\begin{aligned}𝑎_{11} & 𝑎_{12} \\ 𝑎_{21} & 𝑎_{22}\end{aligned}]$

Then, multiplying by $I_2,$ we have

$$


\begin{aligned}𝐴𝐼_{2} & =[\begin{matrix}𝑎_{11} & 𝑎_{12} \\ 𝑎_{21} & 𝑎_{22}\end{matrix}][\begin{matrix}1 & 0 \\ 0 & 1\end{matrix}] \\ & =[\begin{matrix}𝑎_{11}⋅1+𝑎_{12}⋅0 & 𝑎_{11}⋅0+𝑎_{12}⋅1 \\ 𝑎_{21}⋅1+𝑎_{22}⋅0 & 𝑎_{21}⋅0+𝑎_{22}⋅1\end{matrix}] \\ & =[\begin{matrix}𝑎_{11} & 𝑎_{12} \\ 𝑎_{21} & 𝑎_{22}\end{matrix}] \\ & =𝐴.\end{aligned}


$$

Similarly,

$$


\begin{aligned}𝐼_{2}𝐴 & =[\begin{matrix}1 & 0 \\ 0 & 1\end{matrix}][\begin{matrix}𝑎_{11} & 𝑎_{12} \\ 𝑎_{21} & 𝑎_{22}\end{matrix}] \\ & =[\begin{matrix}𝑎_{11} & 𝑎_{12} \\ 𝑎_{21} & 𝑎_{22}\end{matrix}] \\ & =𝐴.\end{aligned}


$$

The above proof shows that the property $A I_2 = I_2 A = A$ holds for all $2\times2$ matrices $A.$

In general, to prove that the property $AI_n = I_n A = A$ holds for all $n \times n$ matrices $A,$ we can use the same method.
