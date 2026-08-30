# Finding Determinants Using Laplace Expansions

Source: https://www.mathacademy.com/topics/1770?courseId=145
Topic ID: 1770

## Prerequisites

- [The Determinant of an NxN Matrix](./1769-the-determinant-of-an-nxn-matrix.md)

## Lesson

### Introduction

Sometimes there are lots of calculations involved in finding the determinant of a matrix using a cofactor expansion across the first row.

Fortunately, however, we don't always have to use the first row! We can use *any* row we like. A cofactor expansion across any general row is known as a **Laplace expansion**.

Across the row $i,$ the Laplace expansion of an $n\!\times\! n$ matrix $A$ is given by the formula

$$


\begin{aligned}det(𝐴) & =\underset{\underset{𝑗=1}{∑}}{\overset{}{𝑛}}𝑎_{𝑖𝑗}𝐶_{𝑖𝑗} \\ & =𝑎_{𝑖1}𝐶_{𝑖1}+𝑎_{𝑖2}𝐶_{𝑖2}+⋯+𝑎_{𝑖𝑛}𝐶_{𝑖𝑛},\end{aligned}


$$

where ${\color{blue}C_{ij}}$ is the cofactor of the entry $\color{red}a_{ij}$ in $A.$ Remember the cofactor of the entry $\color{red}a_{ij}$ is

$$


{\color{black}C_{ij}}=(-1)^{i+j}{\color{black}M_{ij}},


$$

where ${\color{black}M_{ij}}$ is the minor of the entry.

For example, consider the following matrix:

$$


\begin{aligned}−1 & 2 & 1 & 1 \\ 0 & −1 & 1 & 1 \\ 0 & 2 & 0 & 0 \\ 0 & 1 & 0 & −3\end{aligned}


$$

To compute the determinant of the matrix above, it is most convenient to use a Laplace expansion along the row with the most zeros. So, let's use Laplace expansion across the third row ($i=3$) as follows:

$$


\begin{aligned}det\begin{aligned}−1 & 2 & 1 & 1 \\ 0 & −1 & 1 & 1 \\ 0 & 2 & 0 & 0 \\ 0 & 1 & 0 & −3\end{aligned} & =\underset{\underset{𝑗=1}{∑}}{\overset{}{𝑛}}𝑎_{3𝑗}𝐶_{3𝑗} \\ & =0⋅𝐶_{31}+2⋅𝐶_{32}+0⋅𝐶_{33}+0⋅𝐶_{34} \\ & =2⋅(−1)^{3+2}⋅\begin{aligned}−1 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & −3\end{aligned} \\ & =−2⋅\begin{aligned}−1 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & −3\end{aligned}\end{aligned}


$$

So, we reduced a $4 \times 4$ determinant to a $3 \times 3$ determinant.

### Example: Applying a Laplace Expansion Across a Row

#### Question

Using a cofactor expansion along the $4$th row, write the following determinant as a combination of $3 \times 3$ determinants:

$$


\begin{aligned}10 & 2 & −2 & −1 \\ 1 & −2 & 7 & 9 \\ −2 & 1 & −2 & 3 \\ −6 & 0 & 0 & 1\end{aligned}


$$

#### Explanation

Using a Laplace expansion along the $4$th row, we have

$$


\begin{aligned}\begin{aligned}10 & 2 & −2 & −1 \\ 1 & −2 & 7 & 9 \\ −2 & 1 & −2 & 3 \\ −6 & 0 & 0 & 1\end{aligned} & =(−6)⋅𝐶_{41}+0⋅𝐶_{42}+0⋅𝐶_{43}+1⋅𝐶_{44} \\ & =(−6)⋅(−1)^{4+1}⋅\begin{aligned}2 & −2 & −1 \\ −2 & 7 & 9 \\ 1 & −2 & 3\end{aligned}+1⋅(−1)^{4+4}⋅\begin{aligned}10 & 2 & −2 \\ 1 & −2 & 7 \\ −2 & 1 & −2\end{aligned} \\ & =6⋅\begin{aligned}2 & −2 & −1 \\ −2 & 7 & 9 \\ 1 & −2 & 3\end{aligned}+\begin{aligned}10 & 2 & −2 \\ 1 & −2 & 7 \\ −2 & 1 & −2\end{aligned}.\end{aligned}


$$

Therefore,

$$


\begin{aligned}10 & 2 & −2 & −1 \\ 1 & −2 & 7 & 9 \\ −2 & 1 & −2 & 3 \\ −6 & 0 & 0 & 1\end{aligned}


$$

### Example: Calculating a Determinant Using a Laplace Expansion Across a Row

#### Question

Calculate $\begin{aligned}1 & −1 & 0 & 2 \\ 0 & 1 & −4 & 2 \\ 0 & −2 & 3 & 1 \\ 0 & 0 & 0 & −1\end{aligned}$

#### Explanation

The $4$th row of the matrix contains three zeros, more than any other row. So using a Laplace expansion along the $4$th row, we have

$$


\begin{aligned}\begin{aligned}1 & −1 & 0 & 2 \\ 0 & 1 & −4 & 2 \\ 0 & −2 & 3 & 1 \\ 0 & 0 & 0 & −1\end{aligned} & =0⋅𝐶_{41}+0⋅𝐶_{42}+0⋅𝐶_{43}+(−1)⋅𝐶_{44} \\ & =(−1)⋅(−1)^{4+4}⋅\begin{aligned}1 & −1 & 0 \\ 0 & 1 & −4 \\ 0 & −2 & 3\end{aligned} \\ & =−\begin{aligned}1 & −1 & 0 \\ 0 & 1 & −4 \\ 0 & −2 & 3\end{aligned}.\end{aligned}


$$

Now, computing the $3 \times 3$ determinant by applying a Laplace expansion along the $1$st row, we obtain:

$$


\begin{aligned}\begin{aligned}1 & −1 & 0 \\ 0 & 1 & −4 \\ 0 & −2 & 3\end{aligned} & =1⋅\begin{aligned}1 & −4 \\ −2 & 3\end{aligned}−(−1)⋅\begin{aligned}0 & −4 \\ 0 & 3\end{aligned}+0⋅\begin{aligned}0 & 1 \\ 0 & −2\end{aligned} \\ & =\begin{aligned}1 & −4 \\ −2 & 3\end{aligned}+\begin{aligned}0 & −4 \\ 0 & 3\end{aligned} \\ & =(3−8)+(0−0) \\ & =−5\end{aligned}


$$

Therefore,

$$


\begin{aligned}1 & −1 & 0 & 2 \\ 0 & 1 & −4 & 2 \\ 0 & −2 & 3 & 1 \\ 0 & 0 & 0 & −1\end{aligned}


$$

### Laplace Expansion Across a Column

We can also use the Laplace expansion across any *column* to find the determinant. Across the column $j,$ the Laplace expansion is given by the formula

$$


\begin{aligned}det(𝐴) & =\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}𝑎_{𝑖𝑗}𝐶_{𝑖𝑗} \\ & =𝑎_{1𝑗}𝐶_{1𝑗}+𝑎_{2𝑗}𝐶_{2𝑗}+⋯+𝑎_{𝑛𝑗}𝐶_{𝑛𝑗},\end{aligned}


$$

where $\color{blue}C_{ij}$ is the cofactor of the entry ${\color{red}a_{ij}}.$

In other words, the Laplace expansion across a row or column is the sum of the entries in the row or column multiplied by their respective cofactors.

To find the determinant of a matrix, we can choose to use the Laplace expansion across any row or column, so choose the row or column that has the most zeros, to cut down on the calculations!

### Example: Calculating a Determinant Using a Laplace Expansion Across a Column

#### Question

Using a cofactor expansion along the $2$nd column, write the following determinant as a combination of $3 \times 3$ determinants:

$$


\begin{aligned}1 & 0 & −3 & −2 \\ 2 & 3 & −1 & 5 \\ 1 & 0 & 8 & 9 \\ 2 & 0 & 3 & −1\end{aligned}


$$

#### Explanation

Using a Laplace expansion along the $2$nd column, we have

$$


\begin{aligned}\begin{aligned}1 & 0 & −3 & −2 \\ 2 & 3 & −1 & 5 \\ 1 & 0 & 8 & 9 \\ 2 & 0 & 3 & −1\end{aligned} & =0⋅𝐶_{12}+3⋅𝐶_{22}+0⋅𝐶_{32}+0⋅𝐶_{42} \\ & =3⋅(−1)^{2+2}⋅\begin{aligned}1 & −3 & −2 \\ 1 & 8 & 9 \\ 2 & 3 & −1\end{aligned} \\ & =3⋅\begin{aligned}1 & −3 & −2 \\ 1 & 8 & 9 \\ 2 & 3 & −1\end{aligned}.\end{aligned}


$$

Therefore,

$$


\begin{aligned}1 & 0 & −3 & −2 \\ 2 & 3 & −1 & 5 \\ 1 & 0 & 8 & 9 \\ 2 & 0 & 3 & −1\end{aligned}


$$
