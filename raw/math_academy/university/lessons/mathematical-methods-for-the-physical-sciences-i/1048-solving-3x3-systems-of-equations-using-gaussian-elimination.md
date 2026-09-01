# Solving 3x3 Systems of Equations Using Gaussian Elimination

Source: https://www.mathacademy.com/topics/1048?courseId=154
Topic ID: 1048

## Prerequisites

- [Solving 2x2 Systems of Equations Using Gaussian Elimination](./151-solving-2x2-systems-of-equations-using-gaussian-elimination.md)

## Lesson

### Introduction

Consider a system of linear equations and its respective augmented matrix $M\mathbin{:}$

$$


\begin{aligned}𝑥−𝑦+𝑧=6 \\ 𝑦−3𝑧=−13 \\ −𝑥−𝑦−𝑧=−4\end{aligned}


$$

We can reduce $M$ to row echelon form using the standard Gaussian elimination algorithm. The algorithm that we use is very similar to the case of $2 \times 2$ systems.

Our goal is to create a descending "staircase" of $1$'s with $0$'s below, and we achieve this using elementary row operations. So, we have

$$


\begin{aligned}𝑀 & ∼\begin{matrix}1 & −1 & 1 & 6 \\ 0 & 1 & −3 & −13 \\ −1 & −1 & −1 & −4\end{matrix} & 𝑅_{3} & :=𝑅_{3}+𝑅_{1} \\ & ∼\begin{matrix}1 & −1 & 1 & 6 \\ 0 & 1 & −3 & −13 \\ 0 & −2 & 0 & 2\end{matrix} & 𝑅_{3} & :=𝑅_{3}+2𝑅_{2} \\ & ∼\begin{matrix}1 & −1 & 1 & 6 \\ 0 & 1 & −3 & −13 \\ 0 & 0 & −6 & −24\end{matrix} & 𝑅_{3} & :=−\frac{1}{6}𝑅_{3} \\ & ∼\begin{matrix}1 & −1 & 1 & 6 \\ 0 & 1 & −3 & −13 \\ 0 & 0 & 1 & 4\end{matrix}. & & \end{aligned}


$$

The matrix is now in row echelon form, and we can apply back substitution to solve the original system of equations.

**Note:** The row echelon form of a matrix is *not* unique. In the previous example, after the second row operation we arrived at

$$


\begin{aligned}1 & −1 & 1 & 6 \\ 0 & 1 & −3 & −13 \\ 0 & 0 & −6 & −24\end{aligned}


$$

This augmented matrix is already in row echelon form! However, it is always useful to do an extra step and obtain $1$'s along the main diagonal, like we did previously:

$$


\begin{aligned}1 & −1 & 1 & 6 \\ 0 & 1 & −3 & −13 \\ 0 & 0 & 1 & 4\end{aligned}


$$

Having $1$'s along the main diagonal makes the final back substitution process a little easier.

### General Algorithm

The **standard Gaussian elimination** for a $3 \times 3$ system can be described as follows:

1. If $a_{11} \neq 0$ and $a_{11} \neq 1,$ then we use the row operation $R_1:=R_1/a_{11}.$

2. We use first row and the necessary row operations to make the remaining entries of the first column below $a_{11}$ equal to $0.$ Namely, if $a_{21} \neq 0,$ then we use the row operation $R_2:=R_2 + (-a_{21})R_1;$ if $a_{31} \neq 0,$ then we use the row operation $R_3:=R_3 + (-a_{31})R_1.$

3. If $a_{22} \neq 1,$ then we use the row operation $R_2:=R_2/a_{22}.$

4. We use the second row and the necessary row operation to make the entry below $a_{22}$ equal to $0.$ Namely, if $a_{32} \neq 0,$ then we use the row operation $R_3:=R_3 + (-a_{32})R_2.$

1. If $a_{33} \neq 1,$ then we use the row operation $R_3:=R_3/a_{33}.$

2. In some exceptional cases, such as when the element on the diagonal is equal to $0,$ we first need to exchange rows. Then proceed using the same steps as above.

Carrying out the above algorithm will convert the matrix to row echelon form.

### Example: Solving a 3x3 System of Equations Using Standard Gaussian Elimination

#### Question

Consider the system of linear equations

$$


\begin{aligned}𝑥−𝑦+𝑧=1 \\ 𝑦+𝑧=−2 \\ −𝑥+2𝑦+𝑧=−1.\end{aligned}


$$

Use the standard method of Gaussian elimination to reduce the augmented matrix $M$ of the system to row echelon form, and then solve the linear system.

#### Explanation

Reducing $M$ to row echelon form, we have

$$


\begin{aligned}𝑀 & ∼\begin{matrix}1 & −1 & 1 & 1 \\ 0 & 1 & 1 & −2 \\ −1 & 2 & 1 & −1\end{matrix} & 𝑅_{3} & :=𝑅_{3}+𝑅_{1} \\ & ∼\begin{matrix}1 & −1 & 1 & 1 \\ 0 & 1 & 1 & −2 \\ 0 & 1 & 2 & 0\end{matrix} & 𝑅_{3} & :=𝑅_{3}+(−1)𝑅_{2} \\ & ∼\begin{matrix}1 & −1 & 1 & 1 \\ 0 & 1 & 1 & −2 \\ 0 & 0 & 1 & 2\end{matrix}. & & \end{aligned}


$$

The system is now

$$


\begin{aligned}𝑥−𝑦+𝑧=1 \\ 𝑦+𝑧=−2 \\ 𝑧=2,\end{aligned}


$$

and we can apply back substitution. The final equation $z=2$ tells us the value of $z.$ Substituting this value into the second equation, we get

$$


\begin{aligned}𝑦+(2)=−2\,⟹\,𝑦=−4.\end{aligned}


$$

Finally, substituting both $y=-4$ and $z=2$ into the first equation, we get

$$


\begin{aligned}𝑥−(−4)+(2)=1\,⟹\,𝑥=−5.\end{aligned}


$$

Therefore, the solution is $x=-5,$ $y=-4,$ and $z=2.$ Or, in vector form, $\langle -5,-4,2 \rangle.$

### Example: Solving a 3x3 System of Equations Using Standard Gaussian Elimination with Row Exchanges

#### Question

Consider the system of linear equations

$$


\begin{aligned} & 𝑥+𝑦+𝑧=−2 \\ & 𝑥+𝑦+2𝑧=−1 \\ & 𝑥+2𝑦+𝑧=1.\end{aligned}


$$

Use the standard method of Gaussian elimination to reduce the augmented matrix $M$ of the system to row echelon form, and then solve the linear system.

#### Explanation

The augmented matrix for this system is

$$


\begin{aligned}1 & 1 & 1 & −2 \\ 1 & 1 & 2 & −1 \\ 1 & 2 & 1 & 1\end{aligned}


$$

Reducing $M$ to row echelon form, we have

$$


\begin{aligned}𝑀 & ∼\begin{matrix}1 & 1 & 1 & −2 \\ 1 & 1 & 2 & −1 \\ 1 & 2 & 1 & 1\end{matrix} & 𝑅_{2} & :=𝑅_{2}+(−1)𝑅_{1} \\ & ∼\begin{matrix}1 & 1 & 1 & −2 \\ 0 & 0 & 1 & 1 \\ 1 & 2 & 1 & 1\end{matrix} & 𝑅_{3} & :=𝑅_{3}+(−1)𝑅_{1} \\ & ∼\begin{matrix}1 & 1 & 1 & −2 \\ 0 & 0 & 1 & 1 \\ 0 & 1 & 0 & 3\end{matrix}. & & \end{aligned}


$$

Note that we get $a_{22}=0.$ Therefore, we swap the $2$nd and $3$rd rows:

$$


\begin{aligned}𝑀 & ∼\begin{matrix}1 & 1 & 1 & −2 \\ 0 & 0 & 1 & 1 \\ 0 & 1 & 0 & 3\end{matrix} & 𝑅_{2} & ↔𝑅_{3} \\ & ∼\begin{matrix}1 & 1 & 1 & −2 \\ 0 & 1 & 0 & 3 \\ 0 & 0 & 1 & 1\end{matrix} & & \end{aligned}


$$

The system is now

$$


\begin{aligned}𝑥+𝑦+𝑧=−2 \\ 𝑦=3 \\ 𝑧=1,\end{aligned}


$$

and we can apply back substitution. The third equation $z=1$ tells us the value of $z,$ and the second equation $y=3$ tells us the value of $y.$ Substituting these values into the first equation, we get

$$


\begin{aligned}𝑥+(3)+(1)=−2\,⟹\,𝑥=−6.\end{aligned}


$$

Therefore, the solution is $x=-6,$ $y=3,$ and $z=1.$ Or, in vector form, $\langle -6,3,1 \rangle.$
