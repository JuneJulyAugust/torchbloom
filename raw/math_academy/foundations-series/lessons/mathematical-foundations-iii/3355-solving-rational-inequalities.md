# Solving Rational Inequalities

Source: https://www.mathacademy.com/topics/3355?courseId=136
Topic ID: 3355

## Prerequisites

- [Roots of Rational Functions](../mathematical-foundations-ii/133-roots-of-rational-functions.md)
- [Vertical Asymptotes of Rational Functions](../mathematical-foundations-ii/807-vertical-asymptotes-of-rational-functions.md)
- [Solving Polynomial Inequalities Using the Sign Table Method](./2162-solving-polynomial-inequalities-using-the-sign-table-method.md)

## Lesson

### Introduction

We can solve rational inequalities using the sign table method. As an example, let's solve the following inequality.

$$


\dfrac{x-2}{x} \geq 0


$$

Notice that we have zero on the right-hand side. We define the function $f(x)$ as

$$


f(x) = \dfrac{x-2}{x}.


$$

So now, we're solving $f(x)\geq 0.$ We proceed to solve this inequality in four steps:

**Step 1**: Solve $f(x) = 0.$

In our case, the equation is

$$


\dfrac{x-2}{x} = 0,


$$

which has the unique solution $x=2.$

**Step 2**: Find the vertical asymptotes of $f(x).$

To find the vertical asymptotes, we set the denominator of $f(x)$ equal to zero and solve for $x.$ This gives

$$


x = 0.


$$

Therefore, $x=0$ is the only vertical asymptote of $f(x).$

**Step 3**: Create a sign table.

The root and asymptote divide the number line into the following $3$ subintervals:

$$


(-\infty,0), \qquad (0,2), \qquad (2,\infty)


$$

We construct a sign table with the list of the intervals on the top and the list of factors on the left. Filling in the sign table using the usual method, we get the following:

**Step 4**: Find the solution to the inequality using the sign table.

To solve the inequality $f(x)\geq 0,$ we look at the bottom row to find out where the expression $f(x)$ is positive. From the table, we see that the expression is positive on the intervals $(-\infty,0)$ and $(2,\infty).$

Also, since $f(x) \geq 0$ is an "or equal to" inequality, the roots of $f(x)$ are also included in the solution. Therefore, we must include $x=2$ in our solution.

Finally, we conclude that $f(x) \geq 0$ for all $x \in (-\infty, 0) \cup [2,\infty).$

### Example: Solving a Rational Inequality With One Linear Factor in the Numerator and Denominator

#### Question

Solve the inequality $\dfrac{1-x}{x+2} < 0.$

#### Explanation

First, we define the function $f(x)$ as

$$


f(x) = \dfrac{1-x}{x+2}.


$$

So we're now solving the inequality $f(x) \lt 0.$

The solution to the equation $f(x) = 0$ is $x = 1.$ Also, $f(x)$ has a vertical asymptote at $x = -2.$ The root and asymptote divide the number line into $3$ subintervals:

$$


(-\infty,-2), \quad (-2,1), \quad (1,\infty)


$$

Now, we construct a sign table with the list of the intervals on the top and the list of factors on the left. Filling in the sign table using the usual method, we get the following result:

Finally, to solve the inequality $f(x) < 0,$ we look at the bottom row to find out where $f(x)$ is negative.

From the table, we see that $f(x)$ is negative on the intervals $(-\infty,-2)$ and $(1,\infty).$

Therefore, we conclude that $f(x) < 0$ for all $x \in (-\infty,-2) \cup (1,\infty).$

### Example: Solving a Factored Rational Inequality

#### Question

Solve the inequality $\dfrac{2x-1}{(x+2)(x-1)} \geq 0.$

#### Explanation

First, we define the function $f(x)$ as

$$


f(x) = \dfrac{2x-1}{(x+2)(x-1)}.


$$

So we're now solving the inequality $f(x) \geq 0.$

The solution to the equation $f(x) = 0$ is $x=\dfrac 12.$ Also, $f(x)$ has vertical asymptotes at $x = -2$ and $x=1.$ The root and asymptotes divide the number line into $4$ subintervals:

$$


\left(-\infty,-2\right), \quad \left(-2,\dfrac 12\right), \quad \left(\dfrac 12,1\right), \quad \left(1,\infty\right)


$$

Now, we construct a sign table with the list of the intervals on the top and the list of factors on the left. Filling in the sign table using the usual method, we get the following result:

Finally, to solve the inequality $f(x) \geq 0,$ we look at the bottom row to find out where $f(x)$ is positive.

From the table, we see that $f(x)$ is positive on the intervals $\left(-2,\dfrac12\right)$ and $(1,\infty).$

Therefore, remembering that the root of $f(x)$ is also a solution, we conclude that the solution to $f(x) \geq 0$ is

$$


x\in \left(-2,\dfrac12\right]\cup (1,\infty).


$$

### Example: Solving a Rational Inequality by Factoring

#### Question

Solve the inequality $\dfrac{x^2-1}{x-3} \leq 0.$

#### Explanation

First, we define the function $f(x)$ as

$$


f(x) = \dfrac{x^2-1}{x-3} .


$$

By factoring its numerator, the function $f(x)$ can be rewritten as

$$


f(x) = \dfrac{(x+1)(x-1)}{x-3}.


$$

So we're now solving the inequality $f(x) \leq 0.$

The solutions to the equation $f(x) = 0$ are $x = \pm 1.$ Also, $f(x)$ has a vertical asymptote at $x=3.$ The roots and asymptote divide the number line into $4$ subintervals:

$$


(-\infty,-1) \quad(-1,1) \quad (1,3) \quad (3,\infty)


$$

Now, we construct a sign table with the list of the intervals on the top and the list of factors on the left. Filling in the sign table using the usual method, we get the following result:

Finally, to solve the inequality $f(x) \leq 0,$ we look at the bottom row to find out where $f(x)$ is negative.

From the table, we see that $f(x)$ is negative on the intervals $(-\infty,-1)$ and $(1,3).$

Therefore, remembering that the roots of $f(x)$ are also solutions, we conclude that $f(x) \leq 0$ for all $x \in (-\infty,-1]\cup [1,3)$.
