# The Invertible Matrix Theorem in Terms of Dimension, Rank and Nullity

Source: https://www.mathacademy.com/topics/1869?courseId=55
Topic ID: 1869

## Prerequisites

- [The Invertible Matrix Theorem in Terms of 2x2 Systems of Equations](./1730-the-invertible-matrix-theorem-in-terms-of-2x2-systems-of-equations.md)
- [The Dimension of the Null Space of a Matrix](./1868-the-dimension-of-the-null-space-of-a-matrix.md)

## Lesson

### Introduction

Suppose we are given an $n \!\times\! n$ invertible matrix $A.$ Remember that if $A$ is invertible, then the equation $A\mathbf{x}=\mathbf{0}$ has only the trivial solution $\mathbf{x}=\mathbf{0}.$

Let's extract all possible information from this fact using the vector spaces related to the matrix, namely, the *column space* and the *null space*.

- The fact that the unique solution to $A\mathbf{x}=\mathbf{0}$ is $\mathbf{x}=\mathbf{0}$ tells us that or alternatively,

- Furthermore, if $\textrm{dim(Null}(A))=0$ then $A$ has no *non-pivot* columns, or equivalently, all the columns of $A$ are *pivot columns*. So

- Finally, since $\textrm{Col}(A)$ is a subspace of $\mathbb{R}^n$ and its basis has $n$ linearly independent vectors, we can conclude that

All the results mentioned above can be summarized in the following theorem, called the **invertible matrix theorem**:

*Let $A$ be an $n \!\times\! n$ matrix. Then we have the following equivalence:*

$$


\begin{aligned} & Col(𝐴)=ℝ^{𝑛} \\ & dim(Col(𝐴))=𝑛=rank(𝐴) \\ & Null(𝐴)={𝟎} \\ & dim(Null(𝐴))=0=nullity(𝐴)\end{aligned}


$$

### Example: Recognizing Parts of the Invertible Matrix Theorem

#### Question

$$


\begin{aligned} & Col(𝐴)=ℝ^{𝑛} \\ & dim(Col(𝐴))=𝑛=rank(𝐴) \\ & Null(𝐴)={𝟎} \\ & 𝑊𝑊𝑊=0=nullity(𝐴)\end{aligned}


$$

Consider the equivalence above, where $A$ is an $n \!\times\! n$ matrix. What should be placed into the blank space to make a true statement?

#### Explanation

Recall that the ** states the following:

**

$$


\begin{aligned} & Col(𝐴)=ℝ^{𝑛} \\ & dim(Col(𝐴))=𝑛=rank(𝐴) \\ & Null(𝐴)={𝟎} \\ & dim(Null(𝐴))=0=nullity(𝐴)\end{aligned}


$$

The missing expression is $\textrm{dim(Null}(A)).$

### Example: Identifying True Statements Using the Invertible Matrix Theorem

#### Question

Which of the following statements are true, given that $A$ is a $4 \times 4$ matrix, and

$$


\begin{aligned}𝑥_{1} \\ 2𝑥_{1} \\ 0 \\ −𝑥_{1}\end{aligned}


$$

1. $A$ is not invertible

2. $\textrm{Col}(A)=\mathbb{R}^4$

3. $\textrm{rank}(A)=4$

#### Explanation

Since $A$ is a $4 \times 4$ matrix, the invertible matrix theorem states the following:

$$


\begin{aligned} & Col(𝐴)=ℝ^{4} \\ & dim(Col(𝐴))=4=rank(𝐴) \\ & Null(𝐴)={𝟎} \\ & dim(Null(𝐴))=0=nullity(𝐴)\end{aligned}


$$

With that in mind, let's examine each statement in turn.

- Statement I is true. Since we conclude that So, according to the invertible matrix theorem, the matrix $A$ is not invertible.

- Statement II is false. Since the matrix $A$ is not invertible, then by the invertible matrix theorem, we must have $\textrm{Col}(A) \neq \mathbb{R}^4.$

- Statement III is false. Since $A$ is not invertible, then by the invertible matrix theorem, we must have $\textrm{rank}(A) \neq 4.$

Therefore, the correct answer is "I only."

### Example: Сompleting a Sentence Using the Invertible Matrix Theorem

#### Question

Consider the following sentence:

**

Which of the following can be placed into the blank space to make a true statement?

1. $\det(A) = 0$

2. $\textrm{rank}(A) = n$

3. $A$ has $n$ pivot columns

#### Explanation

The invertible matrix theorem states the following:

$A$ is invertible $\begin{aligned} & Col(𝐴)=ℝ^{𝑛} \\ & dim(Col(𝐴))=𝑛=rank(𝐴) \\ & Null(𝐴)={𝟎} \\ & dim(Null(𝐴))=0=nullity(𝐴)\end{aligned}$

With that in mind, let's examine each of the options separately.

- The following statement is false: $\qquad$ ** $\:{\color{red}\times}$ Since $\textrm{Null}(A) = \{\mathbf{0}\},$ then according to the invertible matrix theorem, the matrix $A$ must be invertible, which means $\det(A) \ne 0.$

- The following statement is true: $\qquad$ ** $\:{\color{green}\checkmark}$ Indeed, since $A$ is invertible, then according to the invertible matrix theorem, we have $\textrm{rank}(A)=n.$

- The following statement is true: $\qquad$ ** $\:{\color{green}\checkmark}$ Indeed, since $A$ is invertible, then according to the invertible matrix theorem, we have $\textrm{dim(Col}(A))=n,$ which means that $A$ has exactly $n$ pivot columns.

Therefore, the correct answer is "II and III only."
