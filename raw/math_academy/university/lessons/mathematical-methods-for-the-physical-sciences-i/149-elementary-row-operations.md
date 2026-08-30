# Elementary Row Operations

Source: https://www.mathacademy.com/topics/149?courseId=154
Topic ID: 149

## Prerequisites

- [Systems of Equations as Augmented Matrices](./148-systems-of-equations-as-augmented-matrices.md)
- [Index Notation for Matrices](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/1167-index-notation-for-matrices.md)

## Lesson

### Introduction

Suppose we are given a system of linear equations and its respective augmented matrix:

$$


\begin{aligned}𝑥_{1}+3𝑥_{2}−𝑥_{3}=0 \\ 2𝑥_{1}−𝑥_{2}+4𝑥_{3}=−2 \\ 5𝑥_{1}+𝑥_{2}+𝑥_{3}=1\end{aligned}


$$

We can apply some operations to the augmented matrix that do not change the set of solutions for the corresponding system. These operations are called **elementary row operations**.

After applying an **elementary row operation** to the augmented matrix, the new corresponding system will have the same solutions.

There are three types of elementary row operations:

- switching any two rows:

- multiplying (each element of) a row by a non-zero number:

- adding a multiple of one row to another row:

In the notations above, the "$:=$" symbol is called the **assignment operator.** We use this to assign new values to every element of a given row.

For example, the row operation $R_1:= 2 R_1$ means, "create a new row $1$ by taking the old row $1$ and multiplying it by $2.$" When we do this, we get the following:

$$


\begin{aligned}𝑀 & ∼\begin{aligned}1 & 3 & −1 & 0 \\ 2 & −1 & 4 & −2 \\ 5 & 1 & 1 & 1\end{aligned}\,𝑅_{1}:=2𝑅_{1} \\ & ∼\begin{aligned}2⋅1 & 2⋅3 & 2⋅(−1) & 2⋅0 \\ 2 & −1 & 4 & −2 \\ 5 & 1 & 1 & 1\end{aligned} \\ & ∼\begin{aligned}2 & 6 & −2 & 0 \\ 2 & −1 & 4 & −2 \\ 5 & 1 & 1 & 1\end{aligned}\end{aligned}


$$

A few final points on notation.

- We use the similarity symbol ($\sim$) to indicate when one matrix is transformed into another matrix using elementary row operations.

- The assignment operator $:=$ is sometimes called the "walrus operator" because it looks like a walrus on its side!

### Example: Applying Row Operations To a Coefficients Matrix

#### Question

Consider the matrix $A,$ given by

$$


\begin{aligned}1 & 2 & 3 \\ 4 & 2 & −1 \\ 7 & 12 & 13\end{aligned}


$$

What matrix results from carrying out the row operation $R_2:= R_2 +(- 4) \cdot R_1$ on $A?$

#### Explanation

The operation $R_2:=R_2 + (-4) R_1$ means that we need to add $-4$ times the first row to the second row.

Carrying out this row operation, we get the following:

$$


\begin{aligned}𝐴 & =\begin{aligned}1 & 2 & 3 \\ 4 & 2 & −1 \\ 7 & 12 & 13\end{aligned}\,𝑅_{2}:=𝑅_{2}+(−4)⋅𝑅_{1} \\ & ∼\begin{aligned}1 & 2 & 3 \\ 4+(−4)(1) & 2+(−4)(2) & −1+(−4)(3) \\ 7 & 12 & 13\end{aligned} \\ & ∼\begin{aligned}1 & 2 & 3 \\ 0 & −6 & −13 \\ 7 & 12 & 13\end{aligned}\end{aligned}


$$

### Example: Applying Row Operations To an Augmented Matrix

#### Question

Consider the augmented matrix $A,$ given by

$$


\begin{aligned}−1 & 5 & 4 & 1 \\ 1 & 0 & 5 & 2 \\ 3 & 7 & 1 & 9\end{aligned}


$$

What matrix results from carrying out the row operation $R_1 \leftrightarrow R_2$ on $A?$

#### Explanation

The operation $R_1 \leftrightarrow R_2$ means that we need to swap the first and second rows.

Applying this row operation, we obtain the following:

$$


\begin{aligned}𝐴 & =\begin{aligned}−1 & 5 & 4 & 1 \\ 1 & 0 & 5 & 2 \\ 3 & 7 & 1 & 9\end{aligned}\,𝑅_{1}↔𝑅_{2} \\ & ∼\begin{aligned}1 & 0 & 5 & 2 \\ −1 & 5 & 4 & 1 \\ 3 & 7 & 1 & 9\end{aligned}\end{aligned}


$$

### Example: Identifying the Appropriate Row Operation To Transform One Matrix Into Another

#### Question

Which elementary row operation could transform the matrix $A$ into the matrix $B$, where

$$


\begin{aligned}−4 & −2 & 4 \\ 4 & 1 & 2 \\ 1 & 2 & 3\end{aligned}


$$

#### Explanation

First, notice that the $1$st and the $3$rd rows are the same in both matrices. The only row that has been changed is the $2$nd row.

Now, applying the operation $R_2:=R_2+1 \cdot R_1,$ we get the following:

$$


\begin{aligned}𝐴 & =\begin{aligned}−4 & −2 & 4 \\ 4 & 1 & 2 \\ 1 & 2 & 3\end{aligned}\,𝑅_{2}:=𝑅_{2}+1⋅𝑅_{1} \\ & ∼\begin{aligned}−4 & −2 & 4 \\ 4+1⋅(−4) & 1+1⋅(−2) & 2+1⋅4 \\ 1 & 2 & 3\end{aligned} \\ & ∼\begin{aligned}−4 & −2 & 4 \\ 0 & −1 & 6 \\ 1 & 2 & 3\end{aligned} \\ & =𝐵\end{aligned}


$$

Therefore, the transformation could be done by the operation

$$


R_2:=R_2+1\cdot R_1


$$

or simply

$$


R_2:=R_2+R_1.


$$

### Example: Identifying the Appropriate Row Operation To Transform a Given Entry to a Desired Value

#### Question

Given that $\begin{aligned}3 & 1 & −2 \\ −1 & 5 & 6 \\ 0 & 2 & 4\end{aligned}$ which elementary row operation could make $a_{22}=0?$

#### Explanation

In the given matrix, we have $a_{22}=5$ and we want to perform an elementary row operation that makes $a_{22}=0.$

- We ** make $a_{22}=0$ by switching two rows, because there are no rows with $0$ as the second entry.

- We ** multiply the second row by $0,$ because we are only allowed to multiply rows by ** constants.

- However, we ** add a multiple of another row to the $2$nd row to make $a_{22}=0.$

Looking at the first row, we see that $a_{12}=1.$ If we add $-5$ times this entry to $a_{22},$ we will get $a_{22}=0$ as desired. So, the elementary row operation that we need to use is

$$


R_2 := R_2 + (-5) \cdot R_1.


$$

Applying this operation, we obtain the following:

$$


\begin{aligned}𝐴 & =\begin{aligned}3 & 1 & −2 \\ −1 & 5 & 6 \\ 0 & 2 & 4\end{aligned}\,𝑅_{2}:=𝑅_{2}+(−5)⋅𝑅_{1} \\ & ∼\begin{aligned}3 & 1 & −2 \\ −1+(−5)⋅3 & 5+(−5)⋅1 & 6+(−5)⋅(−2) \\ 0 & 2 & 4\end{aligned} \\ & ∼\begin{aligned}3 & 1 & −2 \\ −16 & 0 & 16 \\ 0 & 2 & 4\end{aligned}\end{aligned}


$$

Therefore, the desired elemetary row operation is

$$


R_2 := R_2 + (-5) \cdot R_1,


$$

or simply

$$


R_2 := R_2 -5 R_1.


$$
