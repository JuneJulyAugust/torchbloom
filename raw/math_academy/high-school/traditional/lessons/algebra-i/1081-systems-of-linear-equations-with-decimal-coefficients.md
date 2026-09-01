# Systems of Linear Equations With Decimal Coefficients

Source: https://www.mathacademy.com/topics/1081?courseId=44
Topic ID: 1081

## Prerequisites

- [Solving Systems of Equations by Substitution](../../../../middle-school/lessons/prealgebra/487-solving-systems-of-equations-by-substitution.md)
- [Solving Systems of Linear Equations Using Elimination: Two Transformations](./4236-solving-systems-of-linear-equations-using-elimination-two-transformations.md)

## Lesson

### Introduction

Sometimes, we might have a system of equations with decimal coefficients, such as the following:

$$


\begin{aligned}0.2𝑥+𝑦=1 \\ 0.15𝑥−0.04𝑦=0.2\end{aligned}


$$

To make the system easier to solve, we turn it into a system involving integer coefficients only.

In general, we multiply each equation by $10,$ or $100,$ or $1000,$ etc. depending on how many decimal places we need to eliminate. In this particular instance:

- We need to eliminate one decimal place in the top equation, so we multiply by $10.$

- We need to eliminate two decimal places in the bottom equation, so we multiply by $100.$

So, we multiply the first equation by $10$ and the second equation by $100,$ as follows:

$$


\begin{aligned}0.2𝑥+𝑦=1 & ×10 \\ 0.15𝑥−0.04𝑦=0.2 & ×100\end{aligned}


$$

From here, we can solve the system of equations using either substitution or elimination.

### Example: Solving a System Containing Decimals in One Equation

#### Question

Solve the following system of equations:

$$


\begin{aligned}0.5𝑥+3𝑦+4=0 \\ 4𝑥=−20𝑦−20\end{aligned}


$$

#### Explanation

To get rid of the decimals, we multiply the first equation by $10,$ as follows:

$$


\begin{aligned}0.5𝑥+3𝑦+4=0 & \,×10 \\ 4𝑥=−20𝑦−20 & \end{aligned}


$$

We also notice that each equation can be simplified by dividing by a common factor. In the first equation, the common factor is $5,$ while in the second equation, the common factor is $4.$

$$


\begin{aligned}5𝑥+30𝑦+40=0 & \,÷5 \\ 4𝑥=−20𝑦−20 & \,÷4\end{aligned}


$$

Notice that the second equation is already solved for $x.$ So, we can substitute $x = -5y-5$ into the first equation and then solve for $y\mathbin{:}$

$$


\begin{aligned}𝑥+6𝑦+8 & =0 \\ (−5𝑦−5)+6𝑦+8 & =0 \\ 𝑦+3 & =0 \\ 𝑦 & =−3\end{aligned}


$$

Finally, to find the value of $x,$ we substitute $y=-3$ back into $x=-5y-5,$ as follows:

$$


\begin{aligned}𝑥 & =−5𝑦−5 \\ & =−5(−3)−5 \\ & =15−5 \\ & =10\end{aligned}


$$

Therefore, the solution is $x = 10$ and $y = -3,$ which can be expressed as $(10, -3).$

### Example: Solving a System Containing Decimals in Both Equations

#### Question

Solve the following system of equations:

$$


\begin{aligned}1.4𝑥+2.8𝑦=1.4 \\ 0.02𝑥+0.01𝑦=0.05\end{aligned}


$$

#### Explanation

To get rid of the decimals, we multiply the first equation by $10$ and the second equation by $100,$ as follows:

$$


\begin{aligned}1.4𝑥+2.8𝑦=1.4 & ×10 \\ 0.02𝑥+0.01𝑦=0.05 & ×100\end{aligned}


$$

To simplify the first equation, we divide by $14\mathbin{:}$

$$


\begin{aligned}14𝑥+28𝑦=14 & ÷14 \\ 2𝑥+𝑦=5 & \end{aligned}


$$

We will use the substitution method to solve the system. Notice that the first equation can easily be solved for $x\mathbin{:}$

$$


\begin{aligned}𝑥+2𝑦 & =1 \\ 𝑥 & =1−2𝑦\end{aligned}


$$

So, we can substitute $x=1-2y$ into the second equation and then solve for $y\mathbin{:}$

$$


\begin{aligned}2𝑥+𝑦 & =5 \\ 2(1−2𝑦)+𝑦 & =5 \\ 2−4𝑦+𝑦 & =5 \\ 2−3𝑦 & =5 \\ −3𝑦 & =3 \\ 𝑦 & =−1\end{aligned}


$$

Finally, to find the value of $x,$ we substitute $y=-1$ back into $x=1-2y,$ as follows:

$$


\begin{aligned}𝑥 & =1−2𝑦 \\ & =1−2(−1) \\ & =1+2 \\ & =3\end{aligned}


$$

Therefore, the solution to the system of equations is $x =3$ and $y =-1$, which can be expressed as $(3, -1).$
