# Orthogonal Matrices

Source: https://www.mathacademy.com/topics/2105?courseId=155
Topic ID: 2105

## Prerequisites

- [Solving Systems of Equations Using Inverse Matrices](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/1023-solving-systems-of-equations-using-inverse-matrices.md)
- [Further Properties of Determinants](../linear-algebra/1774-further-properties-of-determinants.md)
- [The Characteristic Equation of a Matrix](../linear-algebra/1964-the-characteristic-equation-of-a-matrix.md)
- [Orthogonal Sets in Euclidean Spaces](./2103-orthogonal-sets-in-euclidean-spaces.md)

## Lesson

### Introduction

Suppose we have a square $n\times n$ matrix $Q$ with columns $\mathbf{q}_1, \mathbf{q}_2, \ldots, \mathbf{q}_n{:}$

$$


\begin{aligned}| & | & & | \\ 𝐪_{1} & 𝐪_{2} & ⋯ & 𝐪_{𝑛} \\ | & | & & |\end{aligned}


$$

The matrix $Q$ is said to be **orthogonal** if its columns $\mathbf{q}_1, \mathbf{q}_2, \dots, \mathbf{q}_n$ form an *orthonormal* set. In other words,

- the columns of $Q$ must be *mutually orthogonal*, and

- they must all be *unit* vectors.

For instance, the matrix

$$


\begin{aligned}\frac{\sqrt{√3}}{2} & −\frac{1}{2} \\ \frac{1}{2} & \frac{\sqrt{√3}}{2}\end{aligned}


$$

is orthogonal since its columns

$$


\begin{aligned}\frac{\sqrt{√3}}{2} \\ \frac{1}{2}\end{aligned}


$$

form an orthonormal set $\left\{{\color{black}\mathbf{q}_1}, {\color{black}\mathbf{q}_2} \right\}.$ To see this, note the following:

- The vectors $\mathbf q_1$ and $\mathbf q_2$ are orthogonal, since

- Both $\mathbf q_1$ and $\mathbf q_2$ are unit vectors, since and

### A Straightforward Test of Orthogonality

Checking that the columns of $Q$ form an orthonormal set is a fair amount of work. Thankfully, we have the following theorem to make our lives easier:

*A matrix $Q$ is orthogonal if and only if*

$$


Q \cdot Q^T = Q^T \cdot Q = I


$$

Note the following:

- $Q^T$ denotes the transpose of $Q.$ It's the matrix we get when we interchange the rows and columns of $Q.$

- To verify that a matrix is orthogonal in practice, we only need to check that $Q \, Q^T = I.$

Let's see an example of applying this theorem.

### Example: Identifying Orthogonal Matrices

#### Question

$$


\begin{aligned}\frac{1}{\sqrt{√2}} & −\frac{1}{\sqrt{√2}} \\ \frac{1}{\sqrt{√2}} & \frac{1}{\sqrt{√2}}\end{aligned}


$$

Consider the matrix $A$ above. Which of the following statements are true?

1. $A$ is a square matrix

2. $A \cdot A^T = I$

3. $A$ is an orthogonal matrix

#### Explanation

Recall that a square matrix $A$ is **** if and only if

$$


A \cdot A^T = A^T\cdot A = I


$$

where $I$ is the identity matrix.

With that in mind, let's examine the given statements.

- Statement I is true. The number of rows in $A$ is the same as the number of columns. So, it's a square matrix.

- Statement II is true. Indeed,

- Statement III is true. Since $A\cdot A^T = I,$ our matrix is orthogonal.

Therefore, the correct answer is "I, II, and III."

### The Inverse of an Orthogonal Matrix

Recall the following theorem:

*A matrix $Q$ is orthogonal if and only if*

$$


Q \cdot {\color{blue}{Q^T}} = {\color{blue}{Q^T}} \cdot Q = I.


$$

Now, recall that for $Q$ to be invertible, there must exist a matrix $Q^{-1}$ such that

$$


Q \cdot {\color{blue}{Q^{-1}}} = {\color{blue}{Q^{-1}}} \cdot Q = I.


$$

By comparing the two equations above, we can deduce the following:

- Every orthogonal matrix $Q$ is invertible, and

- the inverse of an orthogonal matrix $Q$ is ${\color{blue}{Q^T}},$ that is

These properties explain why orthogonal matrices are desirable. We can always find the inverse of an orthogonal matrix, and we can quickly compute the inverse by simply transposing the original matrix.

### Example: Calculating the Inverse of an Orthogonal Matrix

#### Question

Find the inverse of the orthogonal matrix $\begin{aligned}\frac{1}{\sqrt{√2}} & \frac{1}{\sqrt{√2}} \\ −\frac{1}{\sqrt{√2}} & \frac{1}{\sqrt{√2}}\end{aligned}$

#### Explanation

The inverse of an orthogonal matrix is equal to its transpose.

Therefore, since $D$ is orthogonal, we have

$$


\begin{aligned}𝐷^{−1} & =𝐷^{𝑇}=\begin{aligned}\frac{1}{\sqrt{√2}} & −\frac{1}{\sqrt{√2}} \\ \frac{1}{\sqrt{√2}} & \frac{1}{\sqrt{√2}}\end{aligned}.\end{aligned}


$$

### Properties of Orthogonal Matrices

Orthogonal matrices also have the following important properties:

- $\det(Q)=\pm1$ (the determinant of an orthogonal matrix is either $1$ or $-1$)

- If $\lambda$ is an eigenvalue of an orthogonal matrix $Q,$ then $| \lambda |= 1.$

**Watch out!** These properties are necessary *but not sufficient* conditions:

- Every orthogonal matrix has determinant equal to $\pm 1$, but not every matrix with determinant $\pm 1$ is orthogonal!

- Similarly, every orthogonal matrix has eigenvalues $1$ or $-1$ only, but not every matrix with eigenvalues $1$ or $-1$ is orthogonal.

### Example: Calculating the Determinant of a Product of Matrices

#### Question

$$


\begin{aligned}\frac{2}{\sqrt{√13}} & −\frac{3}{\sqrt{√13}} \\ \frac{3}{\sqrt{√13}} & \frac{2}{\sqrt{√13}}\end{aligned}


$$

Find $|\textrm{det}(PQ)|$ given that $P$ is an orthogonal matrix.

#### Explanation

We use the following facts:

- The determinant of a product is equal to the product of the determinants.

- The determinant of an orthogonal matrix $P$ is equal to $\pm1.$

Applying these ideas, we get the following:

$$


\begin{aligned}|det(𝑃𝑄)| & =|det(𝑃)⋅det(𝑄)| \\ & =|(±1)⋅det(𝑄)| \\ & =|±1|⋅|det(𝑄)| \\ & =|det(𝑄)| \\ & =|(−2\sqrt{√3})⋅3\sqrt{√3}−2⋅1| \\ & =|−18−2| \\ & =|−20| \\ & =20\end{aligned}


$$

### Example: Identifying True Statements About Orthogonal Matrices

#### Question

Which of the following statements are true regarding the $n\times n$ orthogonal matrices $P$ and $Q?$

1. $2Q$ is orthogonal

2. $P^{-1}Q$ is orthogonal

3. $PQ^T$ is orthogonal

#### Explanation

Recall that a matrix $Q$ is orthogonal if and only if

$$


Q Q^T = Q^T Q = I.


$$

To check that a matrix is orthogonal, it is sufficient to check that the above equation is satisfied.

Moreover, we have the following properties:

- For any orthogonal matrix $Q,$ we have $Q^{-1} = Q^T.$

- $(AB)^T = B^TA^T$ for conformable matrices $A$ and $B.$

With that in mind, let's inspect each statement in turn.

- Statement I is false. Computing the product $2Q \cdot (2Q)^T,$ we obtain

- Statement II is true. Computing the product $(P^{-1}Q)\cdot (P^{-1}Q)^T,$ we obtain

- Statement III is true. Computing the product $(PQ^T)\cdot(PQ^T)^T,$ we obtain

Therefore, the correct answer is "II and III only."
