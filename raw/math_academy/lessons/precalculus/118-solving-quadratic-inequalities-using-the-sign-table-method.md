# Solving Quadratic Inequalities Using the Sign Table Method

Source: https://www.mathacademy.com/topics/118?courseId=43
Topic ID: 118

## Prerequisites

- [Solving Elementary Quadratic Inequalities](./1495-solving-elementary-quadratic-inequalities.md)

## Lesson

### Introduction

A **quadratic inequality** is an inequality that involves the square of a variable. For example, the inequality

$$


x^2 +x-2 \geq 0


$$

is a quadratic inequality.

One way of solving a quadratic inequality is to use a **sign table.** A sign table is just a way of keeping track of the sign (positive or negative) of various expressions for various values of $x.$

For example, suppose we want to keep track of the sign of the expression $x+2.$ First, we identify where the expression is zero:

$$


\begin{aligned}𝑥+2 & =0 \\ 𝑥 & =−2\end{aligned}


$$

Now, we split up the number line across the zero of the expression. So we have two intervals, $(-\infty, -2)$ and $(-2,\infty).$

On each of these intervals, the expression $x+2$ is either always positive or always negative. To keep track of this, we can set up a sign table as follows:

To fill out the sign table, we have to figure out the sign of $x+2$ on each of the intervals provided. We can do this by choosing test points:

- In the interval $(-\infty, -2),$ we can choose a test point of $x_1 = -3.$ Substituting this test point into the expression, we get which means that the expression $x+2$ is negative $({\color{red}-})$ for all values of $x$ in the interval $(-\infty, -2).$

- In the interval $(-2, \infty),$ we can choose a test point of $x_2 = 0.$ Substituting this test point into the expression, we get which means that the expression is positive $({\color{blue}+})$ for all values of $x$ in the interval $(-2, \infty).$

Filling out our sign table, then, we have

For now, let's focus on learning how to set up and fill out a sign table. Then, we'll learn how to use them to solve quadratic inequalities.

### Example: Completing a Table of Signs

#### Question

Complete the following sign table:

#### Explanation

We need to fill in each box with the sign of the corresponding expression on the corresponding interval.

Let's start down the first column. In the interval $(-\infty, -1),$ we choose a test point $x_1=-2.$ Then, we have

$$


\begin{aligned}𝑥−2 & =−2−2=−4<0, \\ 𝑥+1 & =−2+1=−1<0,\end{aligned}


$$

so both the expressions $x-2$ and $x+1$ are negative $({\color{red}-})$ on the interval $(-\infty,-1).$

To find the sign of $(x-2)(x+1)$ on this interval, we can just multiply the corresponding signs of $x-2$ and $x+1\mathbin{:}$

$$


({\color{red}-}) \times ({\color{red}-}) = ({\color{blue}+})


$$

So $(x-2)(x+1)$ is positive $({\color{blue}+})$ on this interval, and we can complete the first column of the table:

To find the entries in the other columns, we use the same procedure.

- In the interval $(-1,2),$ we can choose a test point $x_2=0.$ Then we have and we fill in the table as follows:

- In the interval $(2,\infty),$ we can choose a test point $x_3=3.$ Then we have and we fill in the table as follows:

### Solving a Quadratic Inequality Using the Sign Table Method

Given a quadratic inequality like $(x+1)(x-1) > 0$, let's see how to find the solution set using the **sign table method**.

First, we find the roots of the corresponding equation $(x+1)(x-1)=0.$ The two roots are $x=-1$ and $x=1,$ and they split the number line into the $3$ subintervals $(-\infty, -1),$ $(-1,1),$ and $(1,\infty).$

Now, we construct a sign table with the list of the intervals on the top and the list of factors on the left.

Filling in the sign table using the usual method, we get the following result:

Finally, to solve the quadratic inequality $(x+1)(x-1) > 0,$ we look at the bottom row to find out where the expression $(x+1)(x-1)$ is positive $({\color{blue}+}).$

We see that the expression is positive on the intervals $(-\infty,-1)$ and $(1,\infty).$

Therefore, we conclude that $(x+1)(x-1) > 0$ for all $x \in (-\infty, -1) \cup (1, \infty).$

### Example: Solving a Quadratic Inequality With No Constant Term Using the Sign Table Method

#### Question

Find the solution of $x^2-3x \lt 0.$

#### Explanation

First, let's factor the left-hand side of the inequality:

$$


\begin{aligned}𝑥^{2}−3𝑥 & <0 \\ 𝑥(𝑥−3) & <0\end{aligned}


$$

Next, we find the roots of the corresponding equation $x(x-3)=0.$ The roots are $x=0$ and $x=3,$ and they split the number line into the $3$ intervals $(-\infty,0),$ $(0,3),$ and $(3,\infty).$

Now, we construct a sign table with the list of the intervals on the top and the list of factors on the left. Filling in the sign table using the usual method, we get the following result:

Finally, to solve the quadratic inequality $x(x-3) \lt 0,$ we look at the bottom row to find out where the expression $x(x-3)$ is negative.

We see that the expression is negative on the interval $(0, 3).$

Therefore, we conclude that $x^2-3x \lt 0$ for all $x\in (0,3).$

### Example: Solving a Quadratic Inequality Using the Sign Table Method

#### Question

Find the solution of $x^2-3x +2\geq 0.$

#### Explanation

First, let's factor the left-hand side of the inequality:

$$


\begin{aligned}𝑥^{2}−3𝑥+2 & ≥0 \\ (𝑥−1)(𝑥−2) & ≥0\end{aligned}


$$

Next, we find the roots of the corresponding equation $(x-1)(x-2)=0.$ The roots are $x = 1$ and $x=2,$ and they split the number line into the $3$ subintervals $(-\infty,1),$ $(1,2),$ and $(2,\infty).$

Now, we construct a sign table with the list of the intervals on the top and the list of factors on the left. Filling in the sign table using the usual method, we get the following result:

Finally, to solve the quadratic inequality $(x-1)(x-2) \geq 0,$ we look at the bottom row to find out where the expression $(x-1)(x-2)$ is zero or positive.

We see that the expression is positive on the intervals $(-\infty, 1)$ and $(2,\infty).$ Also, we know that the expression equals $0$ at the points $x=1$ and $x=2.$

Therefore, we conclude that $(x-1)(x-2) \geq 0$ for all $x\in (-\infty, 1] \cup [2, \infty).$

### Example: Solving an Inequality by Rearranging Terms and Using the Sign Table Method

#### Question

Find the solution of $x^2+x \leq 6.$

#### Explanation

First, we rewrite the given inequality so that the right-hand side equals zero. Then, we factor the left-hand side:

$$


\begin{aligned}𝑥^{2}+𝑥 & ≤6 \\ 𝑥^{2}+𝑥−6 & ≤0 \\ (𝑥−2)(𝑥+3) & ≤0\end{aligned}


$$

Next, we find the roots of the corresponding equation $(x-2)(x+3) = 0.$ The roots are $x=2$ and $x=-3,$ and they split the number line into $3$ subintervals $(-\infty, -3),$ $(-3,2),$ and $(2,\infty).$

Now, we construct a sign table with the list of the intervals on the top and the list of factors on the left. Filling in the sign table using the usual method, we get the following result:

Finally, to solve the quadratic inequality $(x-2)(x+3) \leq 0,$ we look at the bottom row to find out where the expression $(x-2)(x+3)$ is zero or negative.

We see that the expression is negative on the interval $(-3,2).$ Also, we know that the expression equals zero at the points $x=-3$ and $x=2.$

Therefore, we conclude that $(x-2)(x+3) \leq 0$ for all $x\in[-3,2].$
