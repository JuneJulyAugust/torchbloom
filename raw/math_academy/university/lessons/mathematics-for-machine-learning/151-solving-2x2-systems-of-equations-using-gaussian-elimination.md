# Solving 2x2 Systems of Equations Using Gaussian Elimination

Source: https://www.mathacademy.com/topics/151?courseId=145
Topic ID: 151

## Prerequisites

- [Solving Systems of Equations Using Back Substitution](./1047-solving-systems-of-equations-using-back-substitution.md)
- [Creating Rows or Columns Containing Zeros Using Gaussian Elimination](./3029-creating-rows-or-columns-containing-zeros-using-gaussian-elimination.md)

## Lesson

### Introduction

Consider the following system of linear equations and its respective **augmented matrix**:

$$


\begin{aligned}2𝑥+6𝑦=−2 \\ 3𝑥−𝑦=2\end{aligned}


$$

If we can convert the augmented matrix $M$ to row echelon form, then we can solve the system using back substitution.

The procedure for reducing $M$ to row echelon form using elementary row operations is called **Gaussian elimination**. To perform Gaussian elimination on a $2 \times 2$ matrix, we use the following procedure.

**Step 1:** Consider the entry $a_{11}=2$ of the coefficient matrix. This entry is called a **pivot element**. We want to make this entry equal to $1$. So, the first elementary row operation will be

$$


R_1 := \dfrac{1}{2}R_1


$$

and we have

$$


\begin{aligned}𝑀 & ∼[\begin{matrix}2 & 6 & −2 \\ 3 & −1 & 2\end{matrix}] & 𝑅_{1}:=\frac{1}{2}𝑅_{1} \\ & ∼[\begin{matrix}1 & 3 & −1 \\ 3 & −1 & 2\end{matrix}]. & \end{aligned}


$$

**Step 2:** Consider the entry $a_{21}=3$ below the first pivot element. We want to make this entry equal to $0$. So, the second elementary row operation will be

$$


R_2 :=R_2+(-3)R_1


$$

and we have

$$


\begin{aligned}𝑀 & ∼[\begin{matrix}1 & 3 & −1 \\ 3 & −1 & 2\end{matrix}] & 𝑅_{2}:=𝑅_{2}+(−3)𝑅_{1} \\ & ∼[\begin{matrix}1 & 3 & −1 \\ 0 & −10 & 5\end{matrix}]. & \end{aligned}


$$

**Step 3:** Finally, consider the entry $a_{22}=-10$. This entry is the second pivot element, and we would like to make it equal to $1$. So, the third elementary row operation will be

$$


R_2 :=\dfrac{1}{-10}R_2


$$

and we get $M$ in row echelon form:

$$


\begin{aligned}𝑀 & ∼[\begin{matrix}1 & 3 & −1 \\ 0 & −10 & 5\end{matrix}] & 𝑅_{2}:=\frac{1}{−10}𝑅_{2} \\ & ∼\begin{matrix}1 & 3 & −1 \\ 0 & 1 & −\frac{1}{2}\end{matrix}. & \end{aligned}


$$

The system is now

$$


\begin{aligned}𝑥+3𝑦=−1 \\ 𝑦=−\frac{1}{2},\end{aligned}


$$

and we can apply back substitution. The final equation $y=-\dfrac{1}{2}$ tells us the value of $y.$ Substituting this value into the first equation, we get

$$


x+3 \left( -\dfrac{1}{2} \right) = -1 \qquad\Rightarrow\qquad x=\dfrac{1}{2}.


$$

Therefore, the solution is $x=\dfrac{1}{2}$ and $y=-\dfrac{1}{2}.$ Or, in vector form, $\left< \dfrac{1}{2}, -\dfrac{1}{2} \right>.$

### The Uniqueness of the Row Echelon Form Matrix

The row echelon form of a matrix is *not* unique. In the previous example, after the first row operation we arrived at

$$


\begin{aligned}1 & 3 & −1 \\ 0 & −10 & 5\end{aligned}


$$

This augmented matrix is already in row echelon form! However, it is always useful to do an extra step and obtain $1$'s along the main diagonal, like we did previously:

$$


\begin{aligned}1 & 3 & −1 \\ 0 & 1 & −\frac{1}{2}\end{aligned}


$$

Having $1$'s along the main diagonal makes the final back substitution process a little easier.

### Example: Reducing a 2x2 Augmented Matrix to REF Using Gaussian Elimination

#### Question

Consider the augmented matrix $M$ given by

$$


\begin{aligned}1 & 2 & 0 \\ 3 & −2 & −8\end{aligned}


$$

Use the standard method of Gaussian elimination to reduce $M$ to row echelon form, and then solve the linear system represented by the matrix.

#### Explanation

Reducing $M$ to row echelon form, we have

$$


\begin{aligned}𝑀 & ∼[\begin{matrix}1 & 2 & 0 \\ 3 & −2 & −8\end{matrix}] & 𝑅_{2} & :=𝑅_{2}+(−3)𝑅_{1} \\ & ∼[\begin{matrix}1 & 2 & 0 \\ 0 & −8 & −8\end{matrix}] & 𝑅_{2} & :=−\frac{1}{8}𝑅_{2} \\ & ∼[\begin{matrix}1 & 2 & 0 \\ 0 & 1 & 1\end{matrix}]. & & \end{aligned}


$$

The system is now

$$


\begin{aligned}𝑥+2𝑦=0 \\ 𝑦=1,\end{aligned}


$$

and we can apply back substitution. The final equation $y=1$ tells us the value of $y.$ Substituting this value into the first equation, we get

$$


x+2(1)=0 \quad\Rightarrow\quad x=-2.


$$

Therefore, the solution is $x=-2$ and $y=1.$ Or, in vector form, $\left< -2,1 \right>.$

### Example: Solving a 2x2 System of Equations Using Gaussian Elimination

#### Question

Consider the system of linear equations

$$


\begin{aligned}−𝑥+5𝑦=5 \\ 𝑥−6𝑦=5.\end{aligned}


$$

Use the standard method of Gaussian elimination to reduce the augmented matrix $M$ of the system to row echelon form, and then solve the linear system.

#### Explanation

The augmented matrix for this system is

$$


\begin{aligned}−1 & 5 & 5 \\ 1 & −6 & 5\end{aligned}


$$

Reducing $M$ to row echelon form, we have

$$


\begin{aligned}𝑀 & ∼[\begin{matrix}−1 & 5 & 5 \\ 1 & −6 & 5\end{matrix}] & 𝑅_{1} & :=−𝑅_{1} \\ & ∼[\begin{matrix}1 & −5 & −5 \\ 1 & −6 & 5\end{matrix}] & 𝑅_{2} & :=𝑅_{2}+(−1)𝑅_{1} \\ & ∼[\begin{matrix}1 & −5 & −5 \\ 0 & −1 & 10\end{matrix}] & 𝑅_{2} & :=−𝑅_{2} \\ & ∼[\begin{matrix}1 & −5 & −5 \\ 0 & 1 & −10\end{matrix}]. & & \end{aligned}


$$

The system is now

$$


\begin{aligned}𝑥−5𝑦=−5 \\ 𝑦=−10,\end{aligned}


$$

and we can apply back substitution. The final equation $y=-10$ tells us the value of $y.$ Substituting this value into the first equation, we get

$$


x-5(-10)=-5 \quad\Rightarrow\quad x=-55.


$$

Therefore, the solution is $x=-55$ and $y=-10.$ Or, in vector form, $\langle -55,-10 \rangle.$
