# Solving Systems of Equations by Substitution

Source: https://www.mathacademy.com/topics/487?courseId=113
Topic ID: 487

## Prerequisites

- [Solving Two-Variable Equations](./356-solving-two-variable-equations.md)
- [Introduction to Systems of Linear Equations](./2225-introduction-to-systems-of-linear-equations.md)

## Lesson

### Introduction

Suppose that we want to solve, *without* using graphs, the following system of linear equations:

$$


\begin{aligned}𝑥+𝑦=4 \\ 𝑥−2=𝑦\,\end{aligned}


$$

In order to solve the system without a graph, we will need to combine the equations into a single equation that can be solved using algebraic manipulation.

One way to combine the equations is called the **substitution method.** To use the substitution method, we substitute for one variable in terms of the other.

For instance, notice that we can make $y$ the subject of the second equation:

$$


\color{red}y=x - 2


$$

Substituting this expression for $y$ into the first equation, we get an equation that we can solve for $x\mathbin{:}$

$$


\begin{aligned}𝑥+𝑦 & =4 \\ 𝑥+(𝑥−2) & =4 \\ 2𝑥−2 & =4 \\ 2𝑥 & =6 \\ 𝑥 & =3\end{aligned}


$$

So, the solution must have $x=3.$ But we also need to figure out what $y$ is. We can do this by substituting $x=3$ back into the second equation:

$$


\begin{aligned}𝑦 & =𝑥−2 \\ 𝑦 & =3−2 \\ 𝑦 & =1\end{aligned}


$$

Therefore, the solution to the system of equations is $x = 3$ and $y = 1$, which can be written as $\left(3, 1\right).$

**Note:** Whenever we isolate the variable in one equation, we have to substitute it into the *other* equation. We cannot substitute a variable into the same equation it came from, because this will not give us any more information about the variable.

### Example: Solving a System of Linear Equations Using Substitution

#### Question

Solve the following system of equations:

$$


\begin{aligned}𝑥−𝑦=4 \\ 𝑥+2𝑦=16\end{aligned}


$$

#### Explanation

We will isolate a variable in one of the equations and then substitute it into the other equation. It doesn't matter which equation we pick first, so we choose the easiest one. In this case, the first equation looks like the easiest.

Using the first equation, we can isolate $x$ by adding $y$ to both sides of the equation:

$$


\begin{aligned}𝑥−𝑦 & =4 \\ 𝑥 & =4+𝑦\end{aligned}


$$

Then, we replace $x$ with $4+y$ in the second equation and solve for $y\mathbin{:}$

$$


\begin{aligned} x+2y &=16 \\(4+y) + 2y &=16\\4+3y &=16\\3y &=12\\y &=4 \end{aligned}


$$

If we now substitute $y=4$ into $x=4+y$, then we can find the value of $x\mathbin{:}$

$$


\begin{aligned} x &= 4 + y \\&= 4 + (4) \\&=8 \end{aligned}


$$

Therefore, the solution to the system of equations is $x = 8$ and $y = 4$, which can be written as $(8, 4).$

### Example: Solving a Challenging System of Linear Equations Using Substitution

#### Question

Solve the following system of equations:

$$


\begin{aligned}2𝑢+9𝑣−6=0 \\ 2𝑢+6𝑣−8=0\end{aligned}


$$

#### Explanation

Sometimes, it's handy to assign a number to each equation in a system, so that we can refer to them more easily:

$$


\begin{aligned}2𝑢+9𝑣−6=0\,(1) \\ 2𝑢+6𝑣−8=0\,(2)\end{aligned}


$$

We will isolate a variable in one of the equations and then substitute it into the other equation. Using equation $\color{blue}(2)$, we can solve for $u$ as follows:

$$


\begin{aligned} 2u+6v-8 &= 0 \\2u+6v &= 8 \\2u &= 8 - 6v \\u &= \dfrac{8-6v}{2} \\u &= 4 - 3v \end{aligned}


$$

Then, we substitute $u=4-3v$ into equation $\color{red}(1)$ and solve for $v\mathbin{:}$

$$


\begin{aligned} 2u+9v-6 &= 0 \\2(4-3v)+9v-6 &= 0 \\8-6v+9v-6 &= 0 \\2+3v &= 0 \\3v &= -2 \\v &= -\dfrac{2}{3} \end{aligned}


$$

If we now substitute $v=-\dfrac{2}{3}$ into equation $\color{red}(1)$, then we can find the value of $u\mathbin{:}$

$$


\begin{aligned} 2u+9v-6 &= 0 \\2u+9\left(-\dfrac{2}{3}\right) -6 &= 0 \\2u-6-6 &= 0 \\2u-12 &= 0 \\2u &= 12 \\u &= 6 \end{aligned}


$$

Therefore, the solution to the system of equations is $u=6$ and $v=-\dfrac{2}{3}$, which can be written as $\left(6,-\dfrac{2}{3}\right).$
