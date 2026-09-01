# Solving Systems of Equations Using Back Substitution

Source: https://www.mathacademy.com/topics/1047?courseId=145
Topic ID: 1047

## Prerequisites

- [Three-Dimensional Vectors in Component Form](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/1166-three-dimensional-vectors-in-component-form.md)
- [Row Echelon Form](./2083-row-echelon-form.md)

## Lesson

### Introduction

Suppose we want to solve the following system of linear equations:

$$


\begin{aligned}𝑥+2𝑦+𝑧=1 \\ 𝑦−𝑧=2 \\ 𝑧=3\end{aligned}


$$

The augmented matrix for this system can be written as

$$


\begin{aligned}1 & 2 & 1 & 1 \\ 0 & 1 & −1 & 2 \\ 0 & 0 & 1 & 3\end{aligned}


$$

Notice that the matrix is in *row echelon form* (or REF). Whenever the augmented matrix is in row echelon form, we can solve the system using a method called **back substitution**.

Back substitution involves

- starting with the lowest equation (which is already solved for one variable),

- substituting the result into the next-lowest equation to find the solution for another variable, and

- continuing to substitute the result into the next-lowest equation until the values of all the variables have been found.

Here, the third equation states that $z=3.$ Substituting this into the second equation, we get

$$


y -(3) = 2 \qquad\Longrightarrow\qquad y = 5.


$$

Now, we substitute both $y=5$ and $z=3$ into the first equation to get

$$


x + 2(5) + (3) = 1 \qquad\Longrightarrow\qquad x = -12.


$$

Therefore, the solution is $x=-12,$ $y=5,$ and $z=3.$ We can write it in vector form, as follows:

$$


\begin{aligned}−12 \\ 5 \\ 3\end{aligned}


$$

**Note:** The values $x=-12,$ $y=5,$ and $z=3$ together form *one* solution. We say that this system has *one* solution, *not* three solutions. A system with three solutions would have three different solution vectors, whereas here, we only have *one* solution vector.

### Example: Solving a System of Equations Using Back Substitution

#### Question

Solve the following system of equations:

$$


\begin{aligned}𝑥+𝑦+𝑧=3 \\ 𝑦+𝑧=2 \\ 𝑧=2\end{aligned}


$$

#### Explanation

The third equation states that $z=2.$ Substituting this into the second equation, we get

$$


y+(2)=2 \qquad\Longrightarrow\qquad y = 2-2 = 0.


$$

Now, we substitute both $z=2$ and $y=0$ into the first equation to get

$$


x+(0)+(2)=3 \qquad\Longrightarrow\qquad x = 3-2 = 1.


$$

Therefore, the solution is $x = 1,$ $y=0,$ and $z = 2.$ Or, in vector form, the solution is $\langle 1,0,2 \rangle.$

### Example: Solving a System of Equations Using Back Substitution Given an Augmented Matrix

#### Question

Solve the system of equations that is represented by the augmented matrix

$$


\begin{aligned}1 & 1 & −1 & 1 \\ 0 & 1 & 1 & −2 \\ 0 & 0 & 1 & 5\end{aligned}


$$

#### Explanation

The matrix represents a system of three linear equations in three variables, say, $x_1,$ $x_2,$ and $x_3.$ We obtain the following system of linear equations:

$$


\begin{aligned}𝑥_{1}+𝑥_{2}−𝑥_{3}=1 \\ 𝑥_{2}+𝑥_{3}=−2 \\ 𝑥_{3}=5\end{aligned}


$$

The third equation states that $x_3=5.$ Substituting this into the second equation, we get

$$


x_2+(5)=-2 \qquad\Longrightarrow\qquad x_2=-2-5=-7.


$$

Now, we substitute both $x_3 = 5$ and $x_2 = -7$ into the first equation to get

$$


x_1+(-7)-(5) = 1 \qquad\Longrightarrow\qquad x_1 = 1 + 7 + 5 = 13.


$$

Therefore, the solution is $x_1 = 13,$ $x_2=-7,$ and $x_3 = 5.$ Or, in vector form, the solution is $\langle 13,-7,5 \rangle.$

### Example: Solving a System of Equations Given an Augmented Matrix Containing Non-Unit Leading Entries

#### Question

Solve the system of equations that is represented by the augmented matrix

$$


\begin{aligned}2 & 1 & −1 & 0 \\ 0 & 1 & 1 & −2 \\ 0 & 0 & 3 & 3\end{aligned}


$$

#### Explanation

The matrix represents a system of three linear equations in three variables, say, $x_1,$ $x_2,$ and $x_3.$ We obtain the following system of linear equations:

$$


\begin{aligned}2𝑥_{1}+𝑥_{2}−𝑥_{3}=0 \\ 𝑥_{2}+𝑥_{3}=−2 \\ 3𝑥_{3}=3\end{aligned}


$$

The third equation states that

$$


3x_3=3 \qquad\Longrightarrow\qquad x_3=1.


$$

Substituting this into the second equation, we get

$$


x_2+(1)=-2 \qquad\Longrightarrow\qquad x_2=-2-1=-3.


$$

Now, we substitute both $x_3 = 1$ and $x_2 = -3$ into the first equation to get

$$


2x_1+(-3)-(1) = 0 \qquad\Longrightarrow\qquad x_1 = \dfrac{1}{2} (3 + 1) = 2.


$$

Therefore, the solution is $x_1 = 2,$ $x_2=-3,$ and $x_3 = 1.$ Or, in vector form, the solution is $\langle 2,-3,1 \rangle.$
