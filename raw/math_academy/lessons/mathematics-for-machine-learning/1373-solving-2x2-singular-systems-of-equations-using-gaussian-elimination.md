# Solving 2x2 Singular Systems of Equations Using Gaussian Elimination

Source: https://www.mathacademy.com/topics/1373?courseId=145
Topic ID: 1373

## Prerequisites

- [Solving 2x2 Systems of Equations Using Gaussian Elimination](./151-solving-2x2-systems-of-equations-using-gaussian-elimination.md)
- [Consistency and Dependency in Linear Systems](../algebra-i/4638-consistency-and-dependency-in-linear-systems.md)

## Lesson

### Introduction

Let's consider a system of linear equations where the corresponding coefficient matrix is singular. For example, consider the following system and its associated augmented matrix:

$$


\begin{aligned}𝑥−2𝑦=−5 \\ −3𝑥+6𝑦=15\end{aligned}


$$

To solve the system, we can reduce $M$ to row echelon form using Gaussian elimination, as usual. We have

$$


\begin{aligned}𝑀 & ∼[\begin{aligned}1 & −2 & −5 \\ −3 & 6 & 15\end{aligned}] & 𝑅_{2} & :=𝑅_{2}+3𝑅_{1} \\ & ∼[\begin{aligned}1 & −2 & −5 \\ 0 & 0 & 0\end{aligned}]. & & \end{aligned}


$$

The corresponding system is now

$$


\begin{aligned}𝑥−2𝑦=−5 \\ 0𝑥+0𝑦=0.\end{aligned}


$$

Since any pair of numbers $x,y$ is a solution of the final equation $0x+0y = 0,$ we can remove this equation from the system. So, our system now consists of a single equation

$$


x - 2y = -5.


$$

Finally, we describe the **general solution** of our system.

- The first variable in our equation, $x,$ is called a **basic variable**.

- The second variable in our equation, $y,$ is called a **free variable**.

Solving for the basic variable $(x)$ in terms of the free variable $(y),$ we get $x = -5+2y.$ So the general solution of the system is

$$


\begin{aligned}𝑥=−5+2𝑦 \\ 𝑦=𝑦\end{aligned}


$$

where the free variable $y$ is any number.

In vector form, this solution is written as

$$


\begin{aligned}[\begin{aligned}𝑥 \\ 𝑦\end{aligned}]=[\begin{aligned}−5+2𝑦 \\ 𝑦\end{aligned}]=[\begin{aligned}−5 \\ 0\end{aligned}]+𝑦[\begin{aligned}2 \\ 1\end{aligned}],\,𝑦∈(−∞,∞).\end{aligned}


$$

Notice that this is the equation of a straight line on a plane. Any point on this line satisfies our system of equations.

If we want to find some **particular solution** of the system, we simply choose some particular value of $y$ and find the corresponding value of $x$ on the line. For example, if we choose $y=0,$ then the corresponding value is $x=-5$ and the particular solution is $x=-5,$ $y=0.$

### Example: Reducing an Augmented Matrix for a Singular 2x2 System to REF and Solving the Resulting System

#### Question

Consider the augmented matrix $M$ given by

$$


\begin{aligned}1 & −3 & 1 \\ 4 & −12 & 4\end{aligned}


$$

Use the standard method of Gaussian elimination to reduce $M$ to row echelon form, and then find the general solution of the linear system represented by the matrix.

#### Explanation

Reducing $M$ to echelon form, we have

$$


\begin{aligned}𝑀 & ∼[\begin{aligned}1 & −3 & 1 \\ 4 & −12 & 4\end{aligned}] & 𝑅_{2} & :=𝑅_{2}+(−4)𝑅_{1} \\ & ∼[\begin{aligned}1 & −3 & 1 \\ 0 & 0 & 0\end{aligned}]. & & \end{aligned}


$$

The corresponding system is now

$$


\begin{aligned}𝑥−3𝑦=1 \\ 0𝑥+0𝑦=0.\end{aligned}


$$

Since any pair of numbers $x,y$ is a solution of the final equation $0x+0y = 0,$ we can remove this equation from the system. So, our system now consists of a single equation

$$


x - 3y = 1.


$$

The first variable $(x)$ is the basic variable, and the second variable $(y)$ is the free variable. Solving for the basic variable $(x)$ in terms of the free variable $(y),$ we get $x=1+3y,$ and the general solution is

$$


\begin{aligned}𝑥=1+3𝑦 \\ 𝑦=𝑦\end{aligned}


$$

where $y$ is an arbitrary number.

In vector form, the general solution can be written as

$$


\begin{aligned}[\begin{aligned}𝑥 \\ 𝑦\end{aligned}]=[\begin{aligned}1+3𝑦 \\ 𝑦\end{aligned}]=⟨1+3𝑦,\,𝑦⟩,\,𝑦∈(−∞,∞).\end{aligned}


$$

### Singular Systems with No Solution

Sometimes, a system of equations might not have any solutions. For example, consider the following augmented matrix:

$$


\begin{aligned}𝑀=[\begin{aligned}1 & −2 & 3 \\ 0 & 0 & 10\end{aligned}]\end{aligned}


$$

The corresponding system is

$$


\begin{aligned}𝑥−2𝑦=3 \\ 0𝑥+0𝑦=10.\end{aligned}


$$

The final equation, $0x+0y=10,$ has no solution. It simplifies to $0=10,$ which is a false statement.

So, there is no pair $x,y$ that satisfies both equations in the system. Consequently, the overall system has no solution.

### Example: Solving a Singular 2x2 System of Equations Using Gaussian Elimination

#### Question

Consider the system of linear equations

$$


\begin{aligned}2𝑥+5𝑦=4 \\ 4𝑥+10𝑦=0.\end{aligned}


$$

Use the standard method of Gaussian elimination to reduce the augmented matrix $M$ of the system to row echelon form, and then find the general solution of the linear system.

#### Explanation

First, we set up the augmented matrix for the system:

$$


\begin{aligned}2 & 5 & 4 \\ 4 & 10 & 0\end{aligned}


$$

Reducing $M$ to row echelon form, we have

$$


\begin{aligned}𝑀 & ∼[\begin{aligned}2 & 5 & 4 \\ 4 & 10 & 0\end{aligned}] & 𝑅_{1} & :=\frac{1}{2}𝑅_{1} \\ & ∼\begin{aligned}1 & \frac{5}{2} & 2 \\ 4 & 10 & 0\end{aligned} & 𝑅_{2} & :=𝑅_{2}+(−4)𝑅_{1} \\ & ∼\begin{aligned}1 & \frac{5}{2} & 2 \\ 0 & 0 & −8\end{aligned}. & & \end{aligned}


$$

The corresponding system is now

$$


\begin{aligned}𝑥+\frac{5}{2}𝑦=2 \\ 0𝑥+0𝑦=−8.\end{aligned}


$$

However, the final equation $0x+0y=-8$ has no solution. It simplifies to $0=-8,$ which is a false statement.

So, there is no pair $x,y$ that satisfies both equations in the system. Consequently, the overall system has no solution.

### The Number of Solutions of a 2x2 System

Given a $2 \times 2$ system of linear equations, we have the following possibilities for the number of solutions:

- The system has exactly *one solution* if and only if the respective coefficient matrix is non-singular (meaning that the determinant is not zero). Such systems are called **consistent independent**.

- The system has *infinitely many solutions* if the second row in the standard echelon form contains only $0$'s. These systems are called **consistent dependent**.

- The system has *no solution* if the second row in the standard echelon form contains only $0$'s on the left-hand side and a non-zero element on the right-hand side. These are called **inconsistent** systems.

![Instructional graphic](../../lesson-assets/mathematics-for-machine-learning/topic-1373/4936bfbe282f7c90.png)

**Note:** A system of linear equations of the form

$$


\begin{aligned}𝑎𝑥+𝑏𝑦=0 \\ 𝑐𝑥+𝑑𝑦=0,\end{aligned}


$$

where we have only $0$'s on the right-hand side, is called **homogeneous**. A homogeneous system always has at least one solution, namely, the solution $x=0$ and $y=0.$ Or, in vector form, $\langle 0,0 \rangle.$
