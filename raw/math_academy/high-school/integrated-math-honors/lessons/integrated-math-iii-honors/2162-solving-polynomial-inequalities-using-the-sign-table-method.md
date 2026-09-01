# Solving Polynomial Inequalities Using the Sign Table Method

Source: https://www.mathacademy.com/topics/2162?courseId=101
Topic ID: 2162

## Prerequisites

- [Solving Quadratic Inequalities Using the Sign Table Method](./118-solving-quadratic-inequalities-using-the-sign-table-method.md)
- [Factoring Higher-Order Polynomials as a Difference of Squares](../../../traditional/lessons/algebra-ii/660-factoring-higher-order-polynomials-as-a-difference-of-squares.md)
- [Solving Cubic Equations by Grouping](../../../traditional/lessons/algebra-ii/727-solving-cubic-equations-by-grouping.md)

## Lesson

### Introduction

Let's use the sign table method to solve the inequality

$$


(x+2)(x-2)(x-3) \leq 0.


$$

First, we define the function $f(x)$ as

$$


f(x) =(x+2)(x-2)(x-3).


$$

So we're now solving the inequality $f(x) \leq 0.$

Next, we find the solutions to the equation $f(x) = 0,$ which are $x=-2, x=2,$ and $x=3.$ Since the inequality is not strict, these values *are* solutions to the inequality. Moreover, these roots divide the number line into $4$ subintervals:

$$


\left( -\infty,-2 \right), \qquad (-2,2), \qquad (2,3), \qquad (3,\infty)


$$

On each of these intervals, the factors of the polynomial are either always positive or always negative. We can find out which by filling a sign table:

To fill out the sign table, we have to figure out the sign of each factor on each of the intervals. We can do this by finding the sign of each factor at a chosen test point in each of the intervals:

In the interval $(-\infty, -2),$ we can choose the test point $x_1=-3.$ Then, we have

$$


\begin{aligned}𝑥+2 & =−3+2=−1<0, \\ 𝑥−2 & =−3−2=−5<0, \\ 𝑥−3 & =−3−3=−6<0,\end{aligned}


$$

so all three factors are negative $({\color{red}-})$ on the interval $(-\infty, -2).$

By applying the same method for the other intervals and placing the signs in the sign table, we get the following table.

To fill in the final row, we compute the product of the signs in each of the columns. This gives the following:

To solve the inequality $f(x)\leq 0,$ we look at the bottom row to find out where $f(x)$ is negative.

From the table, we see that $f(x)$ is negative on the intervals $(-\infty, -2)$ and $(2,3).$

Finally, since this is an "or equal to" inequality, the roots of $f(x),$ namely $x=-2, x=2,$ and $x=3$ are also solutions to the inequality. Therefore, we have that $f(x) \leq 0$ for all $x \in (-\infty, -2] \cup [2,3].$

### Example: Solving a Factored Cubic Polynomial Inequality

#### Question

Solve the inequality $(2x+1)(x-2)(x-7) > 0.$

#### Explanation

First, we define the function $f(x)$ as

$$


f(x) = (2x+1)(x-2)(x-7).


$$

So we're now solving the inequality $f(x) > 0.$

The solutions to the equation $f(x) = 0$ are $x=-\dfrac{1}{2},$ $x=2,$ and $x=7.$ These roots divide the number line into $4$ subintervals:

$$


\left( -\infty,-\dfrac{1}{2} \right), \quad \left( -\dfrac{1}{2},2 \right), \quad (2,7), \quad (7, \infty)


$$

Now, we construct a sign table with the list of the intervals on the top and the list of factors on the left. Filling in the sign table using the usual method, we get the following result:

Finally, to solve the inequality $f(x)> 0,$ we look at the bottom row to determine where $f(x)$ is positive.

From the table, we see that $f(x)$ is positive on the intervals $\left(-\dfrac12, 2\right)$ and $(7,\infty).$

Therefore, we conclude that $f(x) > 0$ for all $x \in \left(-\dfrac12, 2\right) \cup (7,\infty).$

### Example: Solving a Factored Higher-Order Polynomial Inequality

#### Question

Solve the inequality $x(x+2)^2(x-1) \leq 0.$

#### Explanation

First, we define the function $f(x)$ as

$$


f(x) = x(x+2)^2(x-1).


$$

So we're now solving the inequality $f(x) \leq 0.$

The solutions to the equation $f(x) = 0$ are $x=-2,$ $x=0,$ and $x=1.$ These roots divide the number line into $4$ subintervals:

$$


(-\infty,-2), \quad (-2,0), \quad (0,1), \quad (1,\infty)


$$

Now, we construct a sign table with the list of the intervals on the top and the list of factors on the left. Filling in the sign table using the usual method, we get the following result:

Finally, to solve the inequality $f(x) \leq 0,$ we look at the bottom row to determine where $f(x)$ is negative.

From the table, we see that $f(x)$ is negative on the interval $(0,1)$ only.

Therefore, remembering that the roots are also solutions, we conclude that $f(x)\leq 0$ for all $x \in \{-2\} \cup[0, 1].$

### Example: Solving an Expanded Polynomial Inequality

#### Question

Solve the inequality $x^4 + 2x^3 - 3x^2 \leq 0.$

#### Explanation

First, we factor the polynomial on the left-hand side of the inequality:

$$


\begin{aligned}𝑥^{4}+2𝑥^{3}−3𝑥^{2} & =𝑥^{2}(𝑥^{2}+2𝑥−3) \\ & =𝑥^{2}(𝑥^{2}+3𝑥−𝑥−3) \\ & =𝑥^{2}(𝑥(𝑥+3)−(𝑥+3)) \\ & =𝑥^{2}(𝑥+3)(𝑥−1)\end{aligned}


$$

Then, we define the function $f(x)$ as

$$


f(x) = x^2(x+3)(x-1).


$$

So we're now solving the inequality $f(x) \leq 0.$

The roots of the polynomial are $x=-3,$ $x=0$ and $x=1.$ These roots divide the number line into $4$ subintervals:

$$


( -\infty,-3 ), \quad ( -3,0 ), \quad (0,1), \quad (1,\infty)


$$

Now, we construct a sign table with the list of the intervals on the top and the list of factors on the left. Filling in the sign table using the usual method, we get the following result:

Finally, to solve the inequality $f(x)\leq 0,$ we look at the bottom row to determine where $f(x)$ is negative.

From the table, we see that $f(x)$ is negative on the intervals $(-3, 0)$ and $(0,1).$

Therefore, remembering that the roots are also solutions, we conclude that the solution to $f(x) \leq 0$ is

$$


x \in [-3,0]\cup [0,1] = [-3,1].


$$

### Example: Solving a Polynomial Inequality when the Right-Hand Side is Nonzero

#### Question

Solve the inequality $x(2x^2-3) < 5x.$

#### Explanation

Moving all the terms to the left-hand side and factoring the resulting polynomial, we get

$$


\begin{aligned}𝑥(2𝑥^{2}−3) & <5𝑥 \\ 𝑥(2𝑥^{2}−3)−5𝑥 & <0 \\ 𝑥(2𝑥^{2}−3−5) & <0 \\ 𝑥(2𝑥^{2}−8) & <0 \\ 2𝑥(𝑥^{2}−4) & <0 \\ 2𝑥(𝑥+2)(𝑥−2) & <0 \\ 𝑥(𝑥+2)(𝑥−2) & <0.\end{aligned}


$$

Then, we define the function $f(x)$ as

$$


f(x) = x(x+2)(x-2).


$$

So we're now solving the inequality $f(x) < 0.$

The solutions to the equation $f(x) = 0$ are $x=-2,$ $x = 0,$ and $x = 2.$ These roots divide the number line into $4$ subintervals:

$$


(-\infty,-2), \quad (-2,0),\quad (0,2),\quad (2,\infty)


$$

Now, we construct a sign table with the list of the intervals on the top and the list of factors on the left. Filling in the sign table using the usual method, we get the following result:

Finally, to solve the inequality $f(x) < 0,$ we look at the bottom row to determine where $f(x)$ is negative.

From the table, we see that $f(x)$ is negative on the intervals $(-\infty, -2)$ and $(0,2).$

Therefore, we conclude that $f(x) < 0$ for all $x \in (-\infty, -2) \cup (0,2).$
