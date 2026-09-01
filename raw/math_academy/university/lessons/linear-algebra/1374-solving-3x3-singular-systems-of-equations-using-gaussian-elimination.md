# Solving 3x3 Singular Systems of Equations Using Gaussian Elimination

Source: https://www.mathacademy.com/topics/1374?courseId=55
Topic ID: 1374

## Prerequisites

- [Solving 2x2 Singular Systems of Equations Using Gaussian Elimination](./1373-solving-2x2-singular-systems-of-equations-using-gaussian-elimination.md)
- [The Parametric Equations of a Plane](./1806-the-parametric-equations-of-a-plane.md)
- [Identifying the Pivot Columns of a Matrix](./1904-identifying-the-pivot-columns-of-a-matrix.md)

## Lesson

### Introduction

Let's consider a system of linear equations where the corresponding coefficient matrix is singular. For example, consider the following system and its associated augmented matrix:

$$


\begin{aligned}𝑥−𝑦+𝑧=2 \\ 2𝑥−𝑦−𝑧=−1 \\ 2𝑦−6𝑧=−10\end{aligned}


$$

To solve the system, we can reduce $M$ to row echelon form using Gaussian elimination, as usual. We have

$$


\begin{aligned}𝑀 & ∼\begin{matrix}1 & −1 & 1 & 2 \\ 2 & −1 & −1 & −1 \\ 0 & 2 & −6 & −10\end{matrix} & 𝑅_{2} & :=𝑅_{2}+(−2)𝑅_{1} \\ & ∼\begin{matrix}1 & −1 & 1 & 2 \\ 0 & 1 & −3 & −5 \\ 0 & 2 & −6 & −10\end{matrix} & 𝑅_{3} & :=𝑅_{3}+(−2)𝑅_{2} \\ & ∼\begin{matrix}1 & −1 & 1 & 2 \\ 0 & 1 & −3 & −5 \\ 0 & 0 & 0 & 0\end{matrix}. & & \end{aligned}


$$

The corresponding system is now

$$


\begin{aligned}𝑥−𝑦+𝑧=2 \\ 0𝑥+𝑦−3𝑧=−5 \\ 0𝑥+0𝑦+0𝑧=0.\end{aligned}


$$

Since any numbers $x,y,z$ form a solution of the final equation $0x+0y+0z = 0,$ we can remove this equation from the system. So, our system now consists of just two equations:

$$


\begin{aligned}𝑥−𝑦+𝑧=2 \\ 𝑦−3𝑧=−5\end{aligned}


$$

The **basic variables** are the variables of our system whose coefficients are the pivots of the row echelon form matrix. Let's illustrate the pivots of $M\mathbin{:}$

$$


\begin{aligned}1 & −1 & 1 & 2 \\ 0 & 1 & −3 & −5 \\ 0 & 0 & 0 & 0\end{aligned}


$$

The pivots are

- $m_{11}=1,$ which is the coefficient of $x,$ and

- $m_{22}=1,$ which is the coefficient of $y.$

Therefore, the basic variables are $x$ and $y.$

The remaining variables are called the **free variables**. We have only one free variable in our system, which is $z$.

Finally, we can describe the **general solution** by finding equations for the basic variables in terms of the free variables. In our case, this means we need to find $x$ and $y$ in terms of $z$.

To do this, we apply the back substitution. From the second equation, we obtain

$$


y - 3z = -5 \qquad\Longrightarrow\qquad y = -5+3z.


$$

Substituting this into the first equation, we get

$$


\begin{aligned}𝑥−(−5+3𝑧)+𝑧=2\,⟹\, & 𝑥=−3+2𝑧.\end{aligned}


$$

Therefore, the general solution is

$$


\begin{aligned}𝑥=−3+2𝑧 \\ 𝑦=−5+3𝑧 \\ 𝑧=𝑧\end{aligned}


$$

where $z$ (the free variable) is an arbitrary number.

In vector form, the solution can be written as

$$


\begin{aligned}𝑥 \\ 𝑦 \\ 𝑧\end{aligned}


$$

Geometrically, this is the vector equation of a line, and any point on the line is a solution to our original system.

If we want to find some **particular solution** of the system, we simply choose some particular value of $z$ and find the corresponding values of $x$ and $y$ on the line. For example, if we choose $z=0,$ then the corresponding values are $x=-3$ and $y=-5$ and the particular solution is $x=-3,$ $y=-5,$ $z=0.$

### Example: Finding the General Solution of a Singular 3x3 System of Equations with Two Pivots

#### Question

Consider the augmented matrix $M$ given by

$$


\begin{aligned}1 & 1 & 3 & 1 \\ 1 & 1 & 1 & −1 \\ 1 & 1 & 5 & 3\end{aligned}


$$

Use the standard method of Gaussian elimination to reduce $M$ to row echelon form, and then find the general solution of the linear system represented by the matrix.

#### Explanation

Reducing $M$ to echelon form, we have

$$


\begin{aligned}𝑀 & ∼\begin{matrix}1 & 1 & 3 & 1 \\ 1 & 1 & 1 & −1 \\ 1 & 1 & 5 & 3\end{matrix} & 𝑅_{2} & :=𝑅_{2}+(−1)𝑅_{1} \\ & ∼\begin{matrix}1 & 1 & 3 & 1 \\ 0 & 0 & −2 & −2 \\ 1 & 1 & 5 & 3\end{matrix} & 𝑅_{3} & :=𝑅_{3}+(−1)𝑅_{1} \\ & ∼\begin{matrix}1 & 1 & 3 & 1 \\ 0 & 0 & −2 & −2 \\ 0 & 0 & 2 & 2\end{matrix} & 𝑅_{3} & :=𝑅_{3}+𝑅_{2} \\ & ∼\begin{matrix}1 & 1 & 3 & 1 \\ 0 & 0 & −2 & −2 \\ 0 & 0 & 0 & 0\end{matrix} & 𝑅_{2} & :=−\frac{1}{2}𝑅_{2} \\ & ∼\begin{matrix}1 & 1 & 3 & 1 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0\end{matrix}. & & \end{aligned}


$$

The corresponding system is now

$$


\begin{aligned}𝑥+𝑦+3𝑧=1 \\ 0𝑥+0𝑦+𝑧=1 \\ 0𝑥+0𝑦+0𝑧=0.\end{aligned}


$$

Since any numbers $x,y,z$ form a solution of the final equation $0x+0y+0z = 0,$ we can remove this equation from the system. So, our system now consists of just two equations:

$$


\begin{aligned}𝑥+𝑦+3𝑧=1 \\ 𝑧=1\end{aligned}


$$

The basic variables are the variables whose coefficients are pivots. In this case, the basic variables are $x$ and $z,$ and we have one free variable, $y.$ That means we need to find $x$ and $z$ in terms of $y.$ To do this, we apply the back substitution.

Starting with the second equation $z=1,$ we substitute into the first equation and get

$$


\begin{aligned}𝑥+𝑦+3(1)=1\,⇒\,𝑥=−2−𝑦.\end{aligned}


$$

Therefore, the general solution is

$$


\begin{aligned}𝑥=−2−𝑦 \\ 𝑦=𝑦 \\ 𝑧=1,\end{aligned}


$$

where $y$ (the free variable) is an arbitrary number.

In vector form, the solution can be written as

$$


\begin{aligned}\begin{matrix}𝑥 \\ 𝑦 \\ 𝑧\end{matrix}=\begin{matrix}−2−𝑦 \\ 𝑦 \\ 1\end{matrix}=\begin{matrix}−2 \\ 0 \\ 1\end{matrix}+𝑦\begin{matrix}−1 \\ 1 \\ 0\end{matrix},\,𝑦∈(−∞,∞).\end{aligned}


$$

### Example: Finding the General Solution of a Singular 3x3 System of Equations with One Pivot

#### Question

Consider the augmented matrix $M$ given by

$$


\begin{aligned}1 & 1 & 3 & 1 \\ −2 & −2 & −6 & −2 \\ 3 & 3 & 9 & 3\end{aligned}


$$

Use the standard method of Gaussian elimination to reduce $M$ to row echelon form, and then find the general solution of the linear system represented by the matrix.

#### Explanation

Reducing $M$ to echelon form, we have

$$


\begin{aligned}𝑀 & ∼\begin{matrix}1 & 1 & 3 & 1 \\ −2 & −2 & −6 & −2 \\ 3 & 3 & 9 & 3\end{matrix} & 𝑅_{2} & :=𝑅_{2}+2𝑅_{1} \\ & ∼\begin{matrix}1 & 1 & 3 & 1 \\ 0 & 0 & 0 & 0 \\ 3 & 3 & 9 & 3\end{matrix} & 𝑅_{3} & :=𝑅_{3}+(−3)𝑅_{1} \\ & ∼\begin{matrix}1 & 1 & 3 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0\end{matrix}. & & \end{aligned}


$$

The corresponding system is now

$$


\begin{aligned}𝑥+𝑦+3𝑧=1 \\ 0𝑥+0𝑦+0𝑧=0 \\ 0𝑥+0𝑦+0𝑧=0.\end{aligned}


$$

Since any numbers $x,y,z$ form a solution of the final two equations $0x+0y+0z = 0,$ we can remove these equations from the system. So, our system now consists of just a single equation:

$$


x + y + 3z = 1


$$

The basic variable is $x$, and we have two free variables $y$ and $z$. That means we need to find $x$ in terms of $y,z.$ Doing this, we get

$$


x = 1-y-3z.


$$

Therefore, the general solution is

$$


\begin{aligned}𝑥=1−𝑦−3𝑧 \\ 𝑦=𝑦 \\ 𝑧=𝑧\end{aligned}


$$

where $y,z$ (the free variables) are arbitrary numbers.

In vector form, the solution can be written as

$$


\begin{aligned}\begin{matrix}𝑥 \\ 𝑦 \\ 𝑧\end{matrix}=\begin{matrix}1−𝑦−3𝑧 \\ 𝑦 \\ 𝑧\end{matrix}=\begin{matrix}1 \\ 0 \\ 0\end{matrix}+𝑦\begin{matrix}−1 \\ 1 \\ 0\end{matrix}+𝑧\begin{matrix}−3 \\ 0 \\ 1\end{matrix},\,𝑦,𝑧∈(−∞,∞).\end{aligned}


$$

Geometrically, this is the equation of a plane in $\mathbb R^3$, and any point on the plane is a solution to the system.

### Example: Identifying a Singular 3x3 System of Equations That Has No Solution

#### Question

Consider the augmented matrix $M$ given by

$$


\begin{aligned}1 & −2 & −6 & 7 \\ 1 & 1 & 0 & 19 \\ 1 & −3 & −8 & 6\end{aligned}


$$

Use the standard method of Gaussian elimination to reduce $M$ to row echelon form, and then find the general solution of the linear system represented by the matrix.

#### Explanation

Reducing $M$ to echelon form, we have

$$


\begin{aligned}𝑀 & ∼\begin{matrix}1 & −2 & −6 & 7 \\ 1 & 1 & 0 & 19 \\ 1 & −3 & −8 & 6\end{matrix} & 𝑅_{2} & :=𝑅_{2}−𝑅_{1} \\ & ∼\begin{matrix}1 & −2 & −6 & 7 \\ 0 & 3 & 6 & 12 \\ 1 & −3 & −8 & 6\end{matrix} & 𝑅_{3} & :=𝑅_{3}−𝑅_{1} \\ & ∼\begin{matrix}1 & −2 & −6 & 7 \\ 0 & 3 & 6 & 12 \\ 0 & −1 & −2 & −1\end{matrix} & 𝑅_{2} & :=\frac{1}{3}𝑅_{2} \\ & ∼\begin{matrix}1 & −2 & −6 & 7 \\ 0 & 1 & 2 & 4 \\ 0 & −1 & −2 & −1\end{matrix} & 𝑅_{3} & :=𝑅_{3}+𝑅_{2} \\ & ∼\begin{matrix}1 & −2 & −6 & 7 \\ 0 & 1 & 2 & 4 \\ 0 & 0 & 0 & 3\end{matrix}. & & \end{aligned}


$$

The corresponding system is now

$$


\begin{aligned}𝑥−2𝑦−6𝑧=7 \\ 0𝑥+𝑦+2𝑧=4 \\ 0𝑥+0𝑦+0𝑧=3\end{aligned}


$$

Since there are no such numbers $x,y,z$ that form a solution of the final equation $0x+0y+0z = 3,$ we can conclude that our system has no solution.
