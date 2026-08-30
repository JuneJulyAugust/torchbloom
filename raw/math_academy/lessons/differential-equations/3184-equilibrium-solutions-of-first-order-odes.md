# Equilibrium Solutions of First-Order ODEs

Source: https://www.mathacademy.com/topics/3184?courseId=61
Topic ID: 3184

## Prerequisites

- [Qualitative Analysis of First-Order ODEs](./2976-qualitative-analysis-of-first-order-odes.md)

## Lesson

### Introduction

Given an autonomous differential equation

$$


y'(t) = f(y),


$$

we have that $y(t)=c$ is an **equilibrium solution** of the equation if

$$


f(c)=0.


$$

For instance, consider the differential equation

$$


\dfrac{\textrm d y}{\textrm d t}= \underbrace{y^3 + y}_{\large f(y)}.


$$

Then, $y=0$ is an equilibrium solution of the equation. Indeed, we have that

$$


f(0) = (0)^3 + (0) = 0.


$$

Now, notice that

$$


f(y) = y^3 + y = y(y^2+1),


$$

where $y^2 + 1 > 0$ for all $y.$ This means that we will not have any other zeros of $f(y).$ Therefore, the only equilibrium solution of our equation is

$$


y(t) =0.


$$

### Example: Identifying Equilibrium Solutions of a Differential Equation

#### Question

Consider the differential equation $\dfrac{\textrm d y}{\textrm d t} + y + 6 = y^2.$ Which of the following is an equilibrium solution of this equation?

1. $y=-3$

2. $y=-2$

3. $y=-1$

#### Explanation

Given an autonomous differential equation $y'(t) = f(y),$ if there exists a constant $c$ such that $f(c)=0,$ then $y=c$ is an equilibrium solution of the equation.

First, we write the given equation as

$$


\dfrac{\textrm d y}{\textrm d t} = y^2 - y - 6,


$$

and we get that $f(y) = y^2 - y - 6.$

Now, let's check each proposed solution by substituting them into $f(y).$

- $y=-3$ is ** an equilibrium point. We have $f(-3) = (-3)^2 - (-3) - 6 = 6 \neq 0.$ $\quad \color{red}{\times}$

- $y = -2$ is an equilibrium point. We have $f(-2) = (-2)^2 - (-2) - 6 = 0.$$\quad \color{green}{\checkmark}$

- $y= -1$ is ** an equilibrium point. We have $f(-1) = (-1)^2 - (-1) - 6 = -4 \neq 0.$ $\quad \color{red}{\times}$

Therefore, the correct answer is "II only."

### Example: Finding Equilibrium Solutions of a Differential Equation

#### Question

Find the equilibrium solutions of the differential equation $\dfrac{\textrm d y}{\textrm d x}= y^2+4y.$

#### Explanation

Given an autonomous differential equation $y'(x) = f(y),$ if there exists a constant $c$ such that $f(c)=0,$ then $y=c$ is an equilibrium solution of the equation.

So, to find the equilibrium solutions of a differential equation, we must find all values of $c$ such that $f(c)=0.$

In our case, we have that $f(y)= y^2+4y,$ so we solve the equation $f(c)=0,$ as follows:

$$


\begin{aligned}𝑓(𝑐) & =0 \\ 𝑐^{2}+4𝑐 & =0 \\ 𝑐(𝑐+4) & =0 \\ 𝑐 & =−4,0\end{aligned}


$$

Therefore, $y_1(x)=-4$ and $y_2(x)=0$ are the equilibrium solutions of the given differential equation.

### Example: Identifying True Statements About Equilibrium Solutions

#### Question

Consider the differential equation $\dfrac{\textrm d y}{\textrm d x}= y^3-3y^2-6y+8.$ Which of the following statements are true?

1. $y_1(x)=4$ is an equilibrium solution of the equation

2. The equation has $3$ distinct equilibrium solutions, $y_1(x), y_2(x),$ and $y_3(x)$

3. $y_1(x) + y_2(x)+y_3(x) =-3$

#### Explanation

Given an autonomous differential equation $y'(x) = f(y),$ if there exists a constant $c$ such that $f(c)=0,$ then $y=c$ is an equilibrium solution of the equation.

In our case, we have that $f(y)=y^3-3y^2-6y+8.$

Let's examine the statement one-by-one.

- Statement I is true. We have that $f(4)=4^3-3(4)^2-6(4)+8 = 0.$

- Statement II is true. We know that $y=4$ is a solution to $f(y) = 0,$ and so $(y-4)$ is a factor of the polynomial $f(y).$ Dividing $f(y)$ by $(y-4)$ using synthetic division, we get $y^3$ $y^2$ $y^1$ $y^0$ $4$ $1$ $-3$ $-6$ $8$ $\color{lightgray}\downarrow$ $4$ $4$ $-8$ $1$ $1$ $-2$ $0$ Therefore, Hence, $f(y)$ has three distinct equilibrium solutions,

- Statement III is false. We have $y_1(x)+y_2(x) + y_3(x) = 4+1+(-2) = 3.$

Therefore, the correct answer is "I and II only."
