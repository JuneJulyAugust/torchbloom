# The Rank-Nullity Theorem

Source: https://www.mathacademy.com/topics/3836?courseId=55
Topic ID: 3836

## Prerequisites

- [The Invertible Matrix Theorem in Terms of Dimension, Rank and Nullity](./1869-the-invertible-matrix-theorem-in-terms-of-dimension-rank-and-nullity.md)

## Lesson

### Introduction

When we reduce a matrix to row echelon form, the number of *pivot* columns plus the number of *non-pivot* columns always equals the total number of columns of the matrix.

By translating this into the language of vector spaces, we get the **rank-nullity theorem**. The rank-nullity theorem relates the rank of a matrix to the dimension of its null space:

*Let $A$ be a matrix (not necessarily square) with $n$ columns. Then,*

$$


\textrm{dim(Col}(A)) + \textrm{dim(Null}(A)) = \textrm{dim}(\mathbb{R}^n),


$$

*or, equivalently,*

$$


\textrm{rank}(A) + \textrm{nullity}(A) = n.


$$

For example, suppose that for some matrix $A,$ we have

$$


\begin{aligned}−2𝑥_{2} \\ 𝑥_{2} \\ 2𝑥_{3} \\ 𝑥_{2}−𝑥_{3}\end{aligned}


$$

We can use the rank-nullity theorem to calculate $\textrm{rank}(A).$

In this case, we must have $n=4,$ since this is the number of components in each of the vectors of the null space.

Also, we must have $\textrm{nullity}(A)=2,$ since

$$


\begin{aligned}−2 \\ 1 \\ 0 \\ 1\end{aligned}


$$

Therefore, using the rank-nullity theorem, we have

$$


\begin{aligned}rank(𝐴)+nullity(𝐴) & =𝑛 \\ rank(𝐴)+2 & =4 \\ rank(𝐴) & =4−2 \\ & =2.\end{aligned}


$$

### Example: Finding the Rank or Nullity of a Matrix Using the Rank-Nullity Theorem

#### Question

Consider a $8 \times 6$ matrix $A.$ If $\textrm{rank}(A)=5$ then what is $\textrm{nullity}(A)?$

#### Explanation

According to the rank-nullity theorem, if $A$ is a matrix with $n$ columns, then

$$


\textrm{rank}(A) + \textrm{nullity}(A) = n.


$$

For the given matrix, we have $n=6.$ Therefore,

$$


\begin{aligned}rank(𝐴)+nullity(𝐴) & =𝑛 \\ 5+nullity(𝐴) & =6 \\ nullity(𝐴) & =6−5 \\ & =1.\end{aligned}


$$

### Example: Finding the Rank or Nullity of a Matrix Given a Description of the Column or Null Space

#### Question

Let $A$ be a $3\times 5$ matrix. If $\mathcal{B}= \{\mathbf{b_1}, \mathbf{b_2}, \mathbf{b_3}\}$ is a basis of $\textrm{Col}(A)$, find $\textrm{dim(Null}(A)).$

#### Explanation

According to the rank-nullity theorem, if $A$ is a matrix with $n$ columns, then

$$


\textrm{rank}(A) + \textrm{nullity}(A) = n.


$$

For the given matrix, we have $n=5,$ and since $\mathcal{B}$ is formed by $3$ vectors, $\textrm{rank}(A) = 3.$ Therefore,

$$


\begin{aligned}rank(𝐴)+nullity(𝐴) & =𝑛 \\ 3+nullity(𝐴) & =5 \\ nullity(𝐴) & =5−3 \\ dim(Null(𝐴)) & =2.\end{aligned}


$$

### Example: Identifying True Statements Using the Invertible Matrix Theorem and the Rank-Nullity Theorem

#### Question

Which of the following statements are true given that $A$ is a $3 \times 3$ matrix, and

$$


\begin{aligned}𝑥_{1} \\ 0 \\ −2𝑥_{3}\end{aligned}


$$

1. $\textrm{rank}(A)=1$

2. $A$ is invertible

3. $\textrm{Col}(A)$ is a $2$-dimensional subspace of $\Bbb R^3$

#### Explanation

Since $A$ is a $3 \times 3$ matrix, the invertible matrix theorem states the following:

$$


\begin{aligned} & Col(𝐴)=ℝ^{3} \\ & dim(Col(𝐴))=3=rank(𝐴) \\ & Null(𝐴)={𝟎} \\ & dim(Null(𝐴))=0=nullity(𝐴)\end{aligned}


$$

Also, according to the rank-nullity theorem, if $A$ is a matrix with $n$ columns, then

$$


\textrm{rank}(A) + \textrm{nullity}(A) = n.


$$

With that in mind, let's examine each statement in turn.

- Statement I is true. Indeed, we have that which means that $\textrm{nullity}(A) =2.$ Now, for the matrix $A,$ the number of columns is $n = 3,$ so according to the rank-nullity theorem, we obtain

- Statement II is false. Since $\textrm{nullity}(A) = 2 \neq 0,$ then by the invertible matrix theorem, $A$ cannot be an invertible matrix.

- Statement III is false. Since $\textrm{rank}(A) = 1,$ we have that $\textrm{Col}(A)$ is a $1$-dimensional subspace of $\Bbb R^3.$

Therefore, the correct answer is "I only."
