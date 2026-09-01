# Conditions When a Determinant Equals Zero

Source: https://www.mathacademy.com/topics/2201?courseId=145
Topic ID: 2201

## Prerequisites

- [Volumes of Parallelepipeds](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/1287-volumes-of-parallelepipeds.md)
- [Row and Column Operations on Determinants](./1772-row-and-column-operations-on-determinants.md)

## Lesson

### Introduction

If an $n\!\times \!n$ matrix $A$ has an entire row or column of zeros, then its determinant is equal to zero.

For example, consider the matrix $A$ given below:

$$


\begin{aligned}∗ & ∗ & ∗ \\ 0 & 0 & 0 \\ ∗ & ∗ & ∗\end{aligned}


$$

The second row consists of all zeros, and the asterisks ($\ast$) may represent any number.

Let's compute the determinant using the Laplace expansion across the second row:

$$


\begin{aligned}det(𝐴) & =\begin{matrix}∗ & ∗ & ∗ \\ 0 & 0 & 0 \\ ∗ & ∗ & ∗\end{matrix} \\ & =(−1)^{2+1}(0)\begin{matrix}∗ & ∗ \\ ∗ & ∗\end{matrix}+(−1)^{2+2}(0)\begin{matrix}∗ & ∗ \\ ∗ & ∗\end{matrix}+(−1)^{2+3}(0)\begin{matrix}∗ & ∗ \\ ∗ & ∗\end{matrix} \\ & =0+0+0 \\ & =0\end{aligned}


$$

Notice that it doesn't matter what numbers are represented by the asterisks ($\ast$). Each cofactor is multiplied by zero, so the final result must be zero.

### Determinants with Identical Rows or Identical Columns

Now, suppose a matrix has no zero rows but it has two identical rows:

$$


\begin{aligned}1 & 2 & 1 \\ 1 & 2 & 3 \\ 1 & 2 & 1\end{aligned}


$$

We can subtract the $1$st row from the $3$rd row, as follows:

$$


\begin{aligned}𝐴 & =\begin{matrix}1 & 2 & 1 \\ 1 & 2 & 3 \\ 1 & 2 & 1\end{matrix} & 𝑅_{3} & :=𝑅_{3}+(−1)𝑅_{1} \\ & ∼\begin{matrix}1 & 2 & 1 \\ 1 & 2 & 3 \\ 0 & 0 & 0\end{matrix} & & \\ & =𝐵 & & \end{aligned}


$$

Since this operation does not change the determinant, we get $\det(A) = \det(B).$ Furthermore, as $B$ contains a zero row, we obtain

$$


\det(A) = \det(B) = 0.


$$

Notice that we can use this method with columns too. Therefore, we have the following property:

*If a square matrix has at least two identical rows/columns, its determinant equals zero.*

### Example: Calculating the Determinant of a Matrix With A Zero Row/Column or Two Identical Rows/Columns

#### Question

Find $5\det(A)-\det(B),$ where

$$


\begin{aligned}4 & \sqrt{13} & 4 \\ 4 & 11 & 4 \\ \sqrt{3} & 9 & \sqrt{3}\end{aligned}


$$

#### Explanation

Let's examine each matrix in turn.

- Since $A$ has two identical columns, we obtain

- Since $B$ is a diagonal matrix, its determinant is given by the product of the elements of the main diagonal:

Therefore, $5\det(A)-\det(B) = 5 \cdot 0 - 24 = -24.$

### Determinants with Proportional Rows/Columns

Now, suppose a matrix has no zero rows and no identical rows but it has two proportional rows:

$$


\begin{aligned}1 & 2 & 1 \\ 1 & 2 & 3 \\ −3 & −6 & −3\end{aligned}


$$

We can add three times the $1$st row to the $3$rd row, as follows:

$$


\begin{aligned}𝐴 & =\begin{matrix}1 & 2 & 1 \\ 1 & 2 & 3 \\ −3 & −6 & −3\end{matrix} & 𝑅_{3} & :=𝑅_{3}+3𝑅_{1} \\ & ∼\begin{matrix}1 & 2 & 1 \\ 1 & 2 & 3 \\ 0 & 0 & 0\end{matrix} & & \\ & =𝐵 & & \end{aligned}


$$

Since this operation does not change the determinant, we get $\det(A) = \det(B).$ Furthermore, as $B$ contains a zero row, we obtain

$$


\det(A) = \det(B) = 0.


$$

Notice that we can use this method with columns too. Therefore, we have the following property:

*If a square matrix has at least two proportional rows/columns, its determinant equals zero.*

### Example: Calculating the Determinant of a Matrix With Two Proportional Rows/Columns

#### Question

Which of the following determinants are equal to $0?$

$$


\begin{aligned}2 & \sqrt{3} & 1 \\ 1 & 1 & 2 \\ 3 & 3 & 6\end{aligned}


$$

#### Explanation

Let's examine each of the given determinants in turn.

- The matrix $A$ has proportional rows: As a result, $|A| = 0.$

- The matrix $B$ is a triangular matrix, so

- The matrix $C$ has a zero row: As a result, $|C| = 0.$

Therefore, only $|A|$ and $|C|$ are equal to $0.$

### Conditions When a Determinant Equals Zero

In conclusion, if an $n\!\times \!n$ matrix $A$ satisfies any one of the following conditions, then $\det(A)=0.$

1. $A$ has a zero row/column

2. $A$ has two identical rows/columns

3. $A$ has two proportional rows/columns

4. $A$ has a row/column that is a linear combination of other rows/columns

Notice that condition IV encompasses each of the conditions I, II, and III. If we have a zero row/column, two identical rows/columns, or proportional rows/columns, then the rows/columns form a linearly dependent set of vectors. In turn, this means that one of the rows/columns is a linear combination of other rows/columns.

**Watch out!** While all of the above conditions are *sufficient* to conclude that $\det(A)=0,$ only condition IV is *necessary* to conclude that $\det(A)=0.$ In other words, if we have a matrix $A$ with $\det(A)=0,$ then conditions I, II, and III may or may not be satisfied, while condition IV *must* be satisfied.

So, we have the following theorem:

*$\det(A)=0$ if and only if one of the rows/columns of $A$ is a linear combination of other rows/columns of $A.$*

Finally, note also that in the case of a $2\times 2$ matrix *only*, statements III and IV mean the same thing.

### Geometric Interpretation of a Zero Determinant

Geometrically, the absolute value of an $n \times n$ determinant can be interpreted as the volume of the $n$-dimensional parallelepiped spanned by the columns of the determinant.

For example:

- Suppose the columns of a $3\times 3$ matrix $A$ are ${\color{black}\mathbf{a}}, {\color{black}\mathbf{b}},$ and ${\color{black}\mathbf{c}}.$ The $3$-dimensional parallelepiped spanned by the columns of $A$ is depicted below: The volume $V$ of this parallelepiped equals the absolute value of the determinant of $A{:}$

- Now suppose the columns of a $2\times 2$ matrix $B$ are ${\color{black}\mathbf{p}}$ and ${\color{black}\mathbf{q}}.$ The $2$-dimensional parallelepiped (i.e., the parallelogram) spanned by vectors $\mathbf{p}$ and $\mathbf{q}$ is shown below: The two-dimensional volume $V$ (i.e., the area) of this parallelepiped equals the absolute value of the determinant of $B{:}$

- In general, the absolute value of the determinant of an $n\times n$ matrix $M$ gives the $n$-dimensional volume of the parallelepiped spanned by the columns of $M.$

In this lesson, we studied the following property:

*$\det(A) = 0$ if and only if one of the columns of $A$ is a linear combination of other columns of $A$.*

What does this property mean in geometric terms?

The component $\det(A) = 0$ implies that the $n$-dimensional parallelepiped formed by the columns of $A$ has zero volume. Conversely, when one of the columns of $A$ is a linear combination of other columns, it indicates that the corresponding parallelepiped possesses at most $n-1$ distinct dimensions.

Consider the following examples:

- In the case of a $3$-dimensional parallelepiped, if the vector $\mathbf{c}$ is a linear combination of the vectors $\mathbf{a}$ and $\mathbf{b}$, then $\mathbf{c}$ lies within the plane containing $\mathbf{a}$ and $\mathbf{b}$. In other words, the vectors $\mathbf{a}$, $\mathbf{b}$, and $\mathbf{c}$ are coplanar. Consequently, we obtain a "flat" ($2$-dimensional) figure with a volume of $0$.

- For the parallelogram example, if the vector $\mathbf{q}$ is a linear combination of the vector $\mathbf{p}$ (i.e., $\mathbf{p}$ and $\mathbf{q}$ are proportional), then $\mathbf{q}$ resides on the line containing vector $\mathbf{p}$. In other words, the vectors $\mathbf{p}$ and $\mathbf{q}$ are collinear. This results in a $1$-dimensional object with a $2$-dimensional volume (i.e., area) of $0$.

### Example: Identifying the Reasons Why a Determinant Equals Zero

#### Question

$$


\begin{aligned}1 & 2 & 0 & −1 \\ 3 & 6 & 0 & 1 \\ 2 & 4 & 0 & −2 \\ 6 & 8 & 0 & 2\end{aligned}


$$

Consider the matrix given above. Identify **** of the reasons why one can conclude that $|A|=0.$

1. $A$ has a zero column

2. $A$ has proportional rows

3. $A$ has identical columns

#### Explanation

Let's examine each of the statements in turn.

- $A$ has a zero column:

- $A$ has proportional rows:

- $A$ does ** have identical columns.

Therefore, the correct answer is "I and II only."
