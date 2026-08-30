# Finding a Basis of a Span

Source: https://www.mathacademy.com/topics/1855?courseId=154
Topic ID: 1855

## Prerequisites

- [Linear Dependence and Independence](./1861-linear-dependence-and-independence.md)
- [Subspaces of N-Dimensional Space: Geometric Interpretation](./4077-subspaces-of-n-dimensional-space-geometric-interpretation.md)

## Lesson

### Introduction

A **basis** of a subspace $U$ (in $\mathbb{R}^n$) is a set of vectors in $\mathbb{R}^n$ that is linearly independent and spans $U.$

For example, consider the following subspace consisting of the span of three vectors:

$$


[\begin{aligned}1 \\ 0\end{aligned}]


$$

To find a basis of $U,$ we need to find a set of linearly independent vectors that spans $U.$

**Watch out!** The set $[\begin{aligned}1 \\ 0\end{aligned}]$ is *not* a basis of $U.$ It's true that this set *spans* $U,$ but the vectors in this set are *not* linearly independent. In particular, the vector $\color{red}\mathbf{a}_3$ can be written as a linear combination of $\color{blue}\mathbf{a}_1$ and $\color{blue}\mathbf{a}_2$ as follows:

$$


[\begin{aligned}−1 \\ 3\end{aligned}]


$$

To find a basis of $U = \textrm{Span} \{{\color{blue}\mathbf{a}_1}, {\color{blue}\mathbf{a}_2}, {\color{red}\mathbf{a}_3} \},$ we can start with $\{{\color{blue}\mathbf{a}_1}, {\color{blue}\mathbf{a}_2}, {\color{red}\mathbf{a}_3} \},$ but we need to remove any "redundant" vectors that can be written as a linear combination of other vectors in the set. In this case, we remove ${\color{red}\mathbf{a}_3}$ because it can be written as a linear combination of $\color{blue}\mathbf{a}_1$ and ${\color{blue}\mathbf{a}_2}.$

We are left with the set

$$


[\begin{aligned}1 \\ 0\end{aligned}]


$$

These two vectors are linearly independent (since they are not parallel), and removing a redundant vector does not change the span, so these vectors still span $U.$ That is to say,

$$


U = \textrm{Span} \{ {\color{blue}\mathbf{a}_1}, {\color{blue}\mathbf{a}_2}, {\color{red}\mathbf{a}_3} \} = \textrm{Span} \{ {\color{blue}\mathbf{a}_1}, {\color{blue}\mathbf{a}_2} \}.


$$

Therefore, the set $\mathcal{B} = \{{\color{blue}\mathbf{a}_1}, {\color{blue}\mathbf{a}_2} \}$ is a basis of $U.$

**Note:** To see that the vectors $\{{\color{blue}\mathbf{a}_1}, {\color{blue}\mathbf{a}_2} \}$ still span $U,$ first note that any vector $\mathbf{b} \in U$ can be written as a linear combination of the three original vectors:

$$


\mathbf{b} = x_1 {\color{blue}\mathbf{a}_1} + x_2 {\color{blue}\mathbf{a}_2} + x_3 {\color{red}\mathbf{a}_3}


$$

Since ${\color{red}\mathbf{a}_3} = -{\color{blue}\mathbf{a}_1}+3{\color{blue}\mathbf{a}_2},$ then we must have

$$


\begin{aligned}𝐛 & =𝑥_{1}𝐚_{1}+𝑥_{2}𝐚_{2}+𝑥_{3}(−𝐚_{1}+3𝐚_{2}) \\ & =(𝑥_{1}−𝑥_{3})𝐚_{1}+(𝑥_{2}+3𝑥_{3})𝐚_{2},\end{aligned}


$$

which shows that $\mathbf{b}$ can actually be written as a linear combination of only two vectors, ${\color{blue}\mathbf{a}_1}$ and ${\color{blue}\mathbf{a}_2}.$

Therefore, we can conclude that the set $\{{\color{blue}\mathbf{a}_1}, {\color{blue}\mathbf{a}_2} \}$ spans the subspace $U = \textrm{Span} \{{\color{blue}\mathbf{a}_1}, {\color{blue}\mathbf{a}_2}, {\color{red}\mathbf{a}_3} \}.$

### Example: Finding a Basis of the Space Spanned by a Set of Vectors Using Inspection

#### Question

Consider the vectors $[\begin{aligned}2 \\ 3\end{aligned}]$ and $[\begin{aligned}1 \\ 1\end{aligned}]$ Find a basis of $S=\textrm{Span}\{\mathbf{a}_1,\mathbf{a}_2,\mathbf{a}_3 \}$ by inspection.

#### Explanation

Remember that a basis of $S$ is a set of linearly independent vectors that spans $S.$

From the given vectors, we can see that $\mathbf{a}_2$ is a linear combination of vectors $\mathbf{a}_1$ and $\mathbf{a}_3\mathbin{:}$

$$


\mathbf{a}_2=1\cdot \mathbf{a}_1+1\cdot \mathbf{a}_3


$$

Consequently, the vector $\mathbf{a}_2$ can be removed from $\textrm{Span}\{\mathbf{a}_1,\mathbf{a}_2,\mathbf{a}_3 \}$ without changing the span. So $S = \textrm{Span}\{\mathbf{a}_1,\mathbf{a}_2,\mathbf{a}_3 \}$ is spanned by just $\{\mathbf{a}_1,\mathbf{a}_3\}.$

Lastly, note that $\mathbf{a}_1$ and $\mathbf{a}_3$ are linearly independent since they are not parallel. So the set $\{\mathbf{a}_1,\mathbf{a}_3\}$ is a linearly independent set that spans $S.$

Therefore, a basis of $S$ is $\{\mathbf{a}_1,\mathbf{a}_3\},$ that is to say,

$$


[\begin{aligned}2 \\ 3\end{aligned}]


$$

### Finding a Basis by Identifying Pivot Columns

In the previous example, it was easy to see that one vector was a linear combination of the others. But what can we do when it's not so easy to tell? For example, consider the subspace

$$


[\begin{aligned}1 \\ −2\end{aligned}]


$$

To find a subset of linearly independent vectors, we can put the vectors in a matrix and compute the reduced row echelon form:

$$


\begin{aligned} & =\,\,[\begin{aligned}1 & −1 & −1 \\ −2 & 3 & 7\end{aligned}] & 𝑅_{2} & :=𝑅_{2}+2𝑅_{1} \\ & ∼[\begin{aligned}1 & −1 & −1 \\ 0 & 1 & 5\end{aligned}] & 𝑅_{1} & :=𝑅_{1}+𝑅_{2} \\ & ∼[\begin{aligned}1 & 0 & 4 \\ 0 & 1 & 5\end{aligned}] & & \end{aligned}


$$

The pivot columns correspond to linearly independent vectors, while the non-pivot columns correspond to linearly dependent (or redundant) vectors that can be removed. Here, the $1$st and $2$nd columns are pivot columns, while the $3$rd column is a non-pivot column.

**But watch out!** We need to pick the pivot columns from the *original matrix*, not from the reduced one.

The $1$st and $2$nd columns from the original matrix are $\mathbf{a}_1$ and $\mathbf{a}_2.$ So, a basis of $U$ is $\{\mathbf{a}_1, \mathbf{a}_2 \},$ that is to say,

$$


[\begin{aligned}1 \\ −2\end{aligned}]


$$

### Example: Finding a Basis of the Space Spanned by a Set of Vectors by Identifying Pivot Columns

#### Question

Consider the vectors $[\begin{aligned}5 \\ 2\end{aligned}]$ $[\begin{aligned}10 \\ 4\end{aligned}]$ and $[\begin{aligned}15 \\ 5\end{aligned}]$ Find a basis of $S=\textrm{Span}\{\mathbf{a}_1,\mathbf{a}_2,\mathbf{a}_3 \}.$

#### Explanation

We need to find a subset of linearly independent vectors. So, we start by creating a matrix whose columns are made up of our vectors, and then we reduce the matrix to row echelon form:

$$


\begin{aligned}𝑀 & =\,\,[\begin{aligned}5 & 10 & 15 \\ 2 & 4 & 5\end{aligned}] & 𝑅_{1} & :=\frac{1}{5}𝑅_{1} \\ & ∼[\begin{aligned}1 & 2 & 3 \\ 2 & 4 & 5\end{aligned}] & 𝑅_{2} & :=𝑅_{2}+(−2)𝑅_{1} \\ & ∼[\begin{aligned}1 & 2 & 3 \\ 0 & 0 & −1\end{aligned}] & & \end{aligned}


$$

The pivot columns correspond to linearly independent vectors, while the non-pivot columns correspond to linearly dependent vectors that can be removed. Here, the $1$st and $3$rd columns are pivot columns, while the $2$nd column is a non-pivot column.

Remember that we need to pick the pivot columns from the **, not from the reduced one.

The $1$st and $3$rd columns from the original matrix are $\mathbf{a}_1$ and $\mathbf{a}_3.$ So, a basis of $S$ is $\{\mathbf{a}_1, \mathbf{a}_3 \},$ that is to say,

$$


[\begin{aligned}5 \\ 2\end{aligned}]


$$

### Finding a Particular Linear Combination of Vectors

Earlier, we computed a basis of

$$


[\begin{aligned}1 \\ −2\end{aligned}]


$$

The basis that we found was

$$


[\begin{aligned}1 \\ −2\end{aligned}]


$$

The vector $\mathbf{a}_3$ was not included in the basis. This means that $\mathbf{a}_3$ can be written as a linear combination of $\mathbf{a}_1$ and $\mathbf{a}_2.$

Now, what if we want to find the exact linear combination of $\mathbf{a}_1$ and $\mathbf{a}_2$ that yields $\mathbf{a}_3?$ That is to say, we want to find $x_1, x_2 \in \mathbb{R}$ such that

$$


[\begin{aligned}1 \\ −2\end{aligned}]


$$

This is equivalent to a system with the augmented matrix

$$


\begin{aligned}1 & −1 & −1 \\ −2 & 3 & 7\end{aligned}


$$

If we reduced this matrix to the *reduced* row echelon form, we get

$$


\begin{aligned}1 & 0 & 4 \\ 0 & 1 & 5\end{aligned}


$$

Finally, the third column of the *reduced* matrix tells us that $x_1=4$ and $x_2=5,$ meaning that

$$


[\begin{aligned}−1 \\ 7\end{aligned}]


$$

**Watch out!** The matrix must be written in *reduced* row echelon form (with $1$'s for pivots and $0$'s above and below the pivots), not just row echelon form.

### Example: Determining Whether a Given Set Is a Basis of a Span

#### Question

The vectors $\mathbf{a}_1,$ $\mathbf{a}_2,$ $\mathbf{a}_3,$ and $\mathbf{a}_4$ are given below. Determine whether $\mathcal{B} = \{\mathbf{a}_1, \mathbf{a}_2, \mathbf{a}_3 \}$ is a basis of $\textrm{Span}\{\mathbf{a}_1,\mathbf{a}_2,\mathbf{a}_3, \mathbf{a}_4 \}.$ If that is the case, find $x_1 + x_2 + x_3,$ where $\mathbf{a}_4=x_1\mathbf{a}_1+x_2\mathbf{a}_2+x_3\mathbf{a}_3.$

$$


\begin{aligned}1 \\ −1 \\ −3\end{aligned}


$$

#### Explanation

We want to determine if $\mathcal{B}$ is indeed a basis of $\textrm{Span}\{\mathbf{a}_1,\mathbf{a}_2,\mathbf{a}_3,\mathbf{a}_4 \}.$ So, we want to find $x_1, x_2, x_3 \in \mathbb{R}$ such that

$$


\begin{aligned}1 \\ −1 \\ −3\end{aligned}


$$

This equation is equivalent to the system

$$


\begin{aligned}𝑥_{1}+𝑥_{3}=2 \\ −𝑥_{1}+𝑥_{2}−𝑥_{3}=−2 \\ −3𝑥_{1}−2𝑥_{3}=1\end{aligned}


$$

Now, we reduce the augmented matrix of the system to reduced row echelon form (RREF):

$$


\begin{aligned}𝐴 & =\,\,\begin{aligned}1 & 0 & 1 & 2 \\ −1 & 1 & −1 & −2 \\ −3 & 0 & −2 & 1\end{aligned} & 𝑅_{2} & :=𝑅_{2}+𝑅_{1} \\ & ∼\begin{aligned}1 & 0 & 1 & 2 \\ 0 & 1 & 0 & 0 \\ −3 & 0 & −2 & 1\end{aligned} & 𝑅_{3} & :=𝑅_{3}+3𝑅_{1} \\ & ∼\begin{aligned}1 & 0 & 1 & 2 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 7\end{aligned} & 𝑅_{1} & :=𝑅_{1}+(−1)𝑅_{3} \\ & ∼\begin{aligned}1 & 0 & 0 & −5 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 7\end{aligned} & & \end{aligned}


$$

From the reduced matrix above, we see that the pivot columns are the $1$st, $2$nd, and $3$rd columns. So, $\mathcal{B}$ is indeed a basis of $\textrm{Span}\{\mathbf{a}_1,\mathbf{a}_2,\mathbf{a}_3,\mathbf{a}_4 \}.$ Also, the matrix tells us that $x_1=-5,$ $x_2=0,$ and $x_3=7,$ meaning that

$$


\begin{aligned}1 \\ −1 \\ −3\end{aligned}


$$

Therefore, $x_1 + x_2 + x_3 = (-5) + 0 + 7 = 2.$
