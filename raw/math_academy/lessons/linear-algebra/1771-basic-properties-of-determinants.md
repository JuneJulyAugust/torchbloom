# Basic Properties of Determinants

Source: https://www.mathacademy.com/topics/1771?courseId=55
Topic ID: 1771

## Prerequisites

- [The Geometric Interpretation of the 2x2 Determinant](../integrated-math-iii-honors/1169-the-geometric-interpretation-of-the-2x2-determinant.md)
- [Finding Determinants Using Laplace Expansions](./1770-finding-determinants-using-laplace-expansions.md)
- [Triangular Matrices](./1777-triangular-matrices.md)

## Lesson

### Introduction

There are some special matrices for which we can compute the determinants without doing so many computations. This is the case for triangular or diagonal matrices.

For example, let's consider the following matrices:

$$


\begin{aligned}1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1\end{aligned}


$$

To quickly compute the determinants of the matrices above, we can use the following three basic properties of determinants:

1. The determinant of an $n\!\times\!n$ identity matrix is equal to $1$. So,

2. The determinant of a triangular or diagonal matrix is equal to the product of the entries on the main diagonal. So,

3. The determinant of $A^T$, the transpose of $A$, is the same as the determinant of $A$:

### Example: Finding the Determinant of a Triangular Matrix

#### Question

Calculate $\begin{aligned}−2 & 0 & 0 & 0 \\ −4 & 1 & 0 & 0 \\ 1 & 10 & \sqrt{√3} & 0 \\ −3 & 0 & 6 & −2\end{aligned}$

#### Explanation

The determinant of a triangular matrix is equal to the product of the entries on the main diagonal. Therefore, we have

$$


\begin{aligned}\begin{aligned}−2 & 0 & 0 & 0 \\ −4 & 1 & 0 & 0 \\ 1 & 10 & \sqrt{√3} & 0 \\ −3 & 0 & 6 & −2\end{aligned} & =(−2)⋅1⋅\sqrt{√3}⋅(−2)=4\sqrt{√3}.\end{aligned}


$$

### Example: Calculating the Determinant of a Matrix With Many Zeros

#### Question

Find the determinant of the matrix $\begin{aligned}2 & 5 & 5 & 4 \\ 0 & 1 & 0 & 0 \\ 0 & 8 & 2 & 0 \\ 0 & 13 & 19 & −3\end{aligned}$

#### Explanation

Notice that the $1$st column contains three zeros. So, using Laplace expansion along the $1$st column, we have

$$


\begin{aligned}det(𝐴) & =\begin{aligned}2 & 5 & 5 & 4 \\ 0 & 1 & 0 & 0 \\ 0 & 8 & 2 & 0 \\ 0 & 13 & 19 & −3\end{aligned} \\ & =2⋅(−1)^{1+1}\begin{aligned}1 & 0 & 0 \\ 8 & 2 & 0 \\ 13 & 19 & −3\end{aligned} \\ & =2\begin{aligned}1 & 0 & 0 \\ 8 & 2 & 0 \\ 13 & 19 & −3\end{aligned}.\end{aligned}


$$

The determinant of a triangular matrix is equal to the product of the entries on the main diagonal. Therefore, we have

$$


\begin{aligned}\begin{aligned}1 & 0 & 0 \\ 8 & 2 & 0 \\ 13 & 19 & −3\end{aligned} & =1⋅2⋅(−3)=−6.\end{aligned}


$$

Finally, we obtain

$$


\det(A) = 2 \cdot (-6) = -12.


$$

### Determinants as Volumes

Geometrically, the absolute value of an $n \times n$ determinant can be interpreted as the volume of the $n$-dimensional parallelepiped spanned by the columns of the matrix. For example:

- The parallelogram (a.k.a. $2$-dimensional parallelepiped) spanned by the two-dimensional vectors $\mathbf{p}$ and $\mathbf{q}$ is depicted below: The volume of this parallelogram is

- The $3$-dimensional parallelepiped spanned by the three-dimensional vectors $\mathbf{a},$ $\mathbf{b},$ and $\mathbf{c}$ is depicted below: The volume of this parallelepiped is

It's much harder to draw a $4$-dimesional parallelepiped that is spanned by the four-dimensional vectors $\mathbf{a}_1,$ $\mathbf{a}_2,$ $\mathbf{a}_3,$ and $\mathbf{a}_4.$ However, we can define its volume similar to the ones above. It will be equal to the absolute value of the corresponding determinant:

$$


\begin{aligned}\,\,| & | & | & |\,\, \\ \,\,𝐚_{1} & 𝐚_{2} & 𝐚_{3} & 𝐚_{4}\,\, \\ \,\,| & | & | & |\,\,\end{aligned}


$$

Volumes for parallelepipeds of higher dimensions are defined analogously.

### Example: Computing the Volume of an N-Dimensional Parallelepiped

#### Question

Calculate the volume of the $4$-dimensional parallelepiped spanned by the vectors

$$


\begin{aligned}2 \\ 3 \\ −4 \\ 5\end{aligned}


$$

#### Explanation

First, let's construct the matrix $M,$ whose columns are the coordinates of our vectors $\mathbf{a},$ $\mathbf{b},$ $\mathbf{c},$ and $\mathbf{d}{:}$

$$


\begin{aligned}2 & 3 & −2 & 1 \\ 3 & 0 & 0 & 0 \\ −4 & 0 & 1 & 0 \\ 5 & −4 & 2 & 5\end{aligned}


$$

The volume of the parallelepiped spanned by these vectors equals the absolute value of the determinant of $M{:}$

$$


V = | \det(M) |


$$

Notice that the $2$nd row of the determinant contains three zeros. So, using Laplace expansion along the $2$nd row, we have

$$


\begin{aligned}det(𝑀) & =\begin{aligned}2 & 3 & −2 & 1 \\ 3 & 0 & 0 & 0 \\ −4 & 0 & 1 & 0 \\ 5 & −4 & 2 & 5\end{aligned} \\ & =3⋅(−1)^{2+1}\begin{aligned}3 & −2 & 1 \\ 0 & 1 & 0 \\ −4 & 2 & 5\end{aligned} \\ & =−3\begin{aligned}3 & −2 & 1 \\ 0 & 1 & 0 \\ −4 & 2 & 5\end{aligned}.\end{aligned}


$$

Now, notice that the $2$nd row of the $3 \times 3$ determinant contains two zeros. So, using Laplace expansion along the $2$nd row, we have

$$


\begin{aligned}det(𝑀) & =−3\begin{aligned}3 & −2 & 1 \\ 0 & 1 & 0 \\ −4 & 2 & 5\end{aligned} \\ & =−3⋅1⋅(−1)^{2+2}\begin{aligned}3 & 1 \\ −4 & 5\end{aligned} \\ & =−3\begin{aligned}3 & 1 \\ −4 & 5\end{aligned} \\ & =−3(15+4) \\ & =−57.\end{aligned}


$$

Therefore, the volume is

$$


V = | \det(M) | = |-57| = 57.


$$

### Example: Calculating an Expression Involving Given Determinants and Matrix Types

#### Question

Given that $\det(A)=4,$ which of the following statements are true?

1. $\textrm{det}(A^T)=16$

2. $3\textrm{det}(A^T)=12$

3. $\textrm{det}(A^T)+\textrm{det}(I)=17$

#### Explanation

From the properties of determinants, we know that

$$


\textrm{det}(A^T)=\textrm{det}(A)=4


$$

and

$$


\textrm{det}(I)=1.


$$

With that in mind, let's analyze each statement in turn.

- Statement I is false. Rather,

- Statement II is true. Indeed,

- Statement III is false. We have

In conclusion, the correct answer is "II only".
