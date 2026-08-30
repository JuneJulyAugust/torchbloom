# Further Solving of Rational Inequalities

Source: https://www.mathacademy.com/topics/2044?courseId=43
Topic ID: 2044

## Prerequisites

- [Solving Rational Inequalities](./3355-solving-rational-inequalities.md)
- [Adding Rational Expressions With No Common Factors in the Denominator](../algebra-ii/3739-adding-rational-expressions-with-no-common-factors-in-the-denominator.md)

## Lesson

### Introduction

We can use the sign table method to solve rational inequalities with zero on one side. For example, the inequality

$$


\dfrac{x+1}{x+2} > 0


$$

can be solved using the sign table method.

Sometimes, rational inequalities require some rearrangement before we can apply the sign table method.

As an example, let's consider the inequality

$$


\dfrac{x+1}{x+2} > x.


$$

To solve this inequality, we first subtract $x$ from both sides of the inequality to get zero on one side:

$$


\dfrac{x+1}{x+2} - x > 0


$$

Then, we put all of the terms on the left-hand side over a common denominator and simplify.

$$


\begin{aligned}\frac{𝑥+1}{𝑥+2}−𝑥 & >0 \\ \frac{𝑥+1}{𝑥+2}−\frac{𝑥(𝑥+2)}{𝑥+2} & >0 \\ \frac{𝑥+1−𝑥(𝑥+2)}{𝑥+2} & >0 \\ \frac{𝑥+1−𝑥^{2}−2𝑥}{𝑥+2} & >0 \\ \frac{1−𝑥−𝑥^{2}}{𝑥+2} & >0\end{aligned}


$$

We can solve this inequality using the sign table method.

### Example: Solving a Rational Inequality With a Constant on One Side

#### Question

Solve the inequality $\dfrac{x}{x+1} \leq 3.$

#### Explanation

Here, we have a rational inequality that is non-zero on one side. So, we rewrite the inequality to give zero on one side:

$$


\begin{aligned}\frac{𝑥}{𝑥+1} & ≤3 \\ \frac{𝑥}{𝑥+1}−3 & ≤0 \\ \frac{𝑥}{𝑥+1}−\frac{3(𝑥+1)}{𝑥+1} & ≤0 \\ \frac{𝑥−3(𝑥+1)}{𝑥+1} & ≤0 \\ \frac{𝑥−3𝑥−3}{𝑥+1} & ≤0 \\ \frac{−2𝑥−3}{𝑥+1} & ≤0 \\ −\frac{2𝑥+3}{𝑥+1} & ≤0 \\ \frac{2𝑥+3}{𝑥+1} & ≥0\end{aligned}


$$

We now proceed using the sign table method. First, we define the function $f(x)$ as

$$


f(x) = \dfrac{2x+3}{x+1}.


$$

So, we're now solving the inequality $f(x) \geq 0.$

The solution to the equation $f(x)=0$ is $x=-\dfrac32.$ Also, $f(x)$ has a vertical asymptote at $x=-1.$ The root and asymptote divide the number line into $3$ subintervals:

$$


\left(-\infty, -\dfrac32\right), \quad \left(-\dfrac32, -1\right), \quad (-1, \infty).


$$

Now, we construct a sign table with the list of the intervals on the top and the list of factors on the left. Filling in the sign table using the usual method, we get the following result:

To solve the inequality $f(x) \geq 0,$ we look at the bottom row to find out where $f(x)$ is positive.

From the table, we see that $f(x)$ is positive on the intervals $\left(-\infty, -\dfrac32\right)$ and $(-1, \infty).$

Since our inequality is non-strict, we must remember that the root of $f(x)$ is also a solution. Therefore, we conclude that the solution to $f(x) \geq 0$ is

$$


x\in \left( -\infty, -\dfrac32 \right] \cup (-1, \infty).


$$

### Example: Solving a Rational Inequality With a Linear Expression on One Side

#### Question

Solve the inequality $\dfrac{2x}{x-4} < x.$

#### Explanation

Here, we have a rational inequality that is non-zero on one side. So, we rewrite the inequality to give zero on one side:

$$


\begin{aligned}\frac{2𝑥}{𝑥−4} & <𝑥 \\ \frac{2𝑥}{𝑥−4}−𝑥 & <0 \\ \frac{2𝑥−𝑥(𝑥−4)}{𝑥−4} & <0 \\ \frac{−𝑥^{2}+6𝑥}{𝑥−4} & <0 \\ \frac{𝑥(6−𝑥)}{𝑥−4} & <0.\end{aligned}


$$

We now proceed using the sign table method. First, we define the function $f(x)$ as

$$


f(x) = \dfrac{x(6-x)}{x-4}.


$$

So, we're solving the inequality $f(x) < 0.$

The solutions to the equation $f(x) = 0$ are $x=0$ and $x=6.$ Also, $f(x)$ has a vertical asymptote at $x=4.$ The roots and asymptote divide the number line into $4$ subintervals:

$$


(-\infty,0), \quad (0,4), \quad (4,6), \quad (6, \infty)


$$

Now, we construct a sign table with the list of the intervals on the top and the list of factors on the left. Filling in the sign table using the usual method, we get the following result:

To solve the inequality $f(x) < 0,$ we look at the bottom row to find out where $f(x)$ is negative.

From the table, we see that $f(x)$ is negative on the intervals $(0, 4)$ and $(6,\infty).$

Therefore, we conclude that the solution to $f(x) < 0$ is

$$


x \in (0,4) \cup (6, \infty).


$$

### Example: Solving a Rational Inequality Involving Two Rational Expressions

#### Question

Solve the inequality $\dfrac{x-2}{x+2} > \dfrac{x}{x-2}.$

#### Explanation

Here, we have a rational inequality that is non-zero on one side. So, we rewrite the inequality to give zero on one side:

$$


\begin{aligned}\frac{𝑥−2}{𝑥+2} & >\frac{𝑥}{𝑥−2} \\ \frac{𝑥−2}{𝑥+2}−\frac{𝑥}{𝑥−2} & >0 \\ \frac{(𝑥−2)^{2}−𝑥(𝑥+2)}{(𝑥+2)(𝑥−2)} & >0 \\ \frac{𝑥^{2}−4𝑥+4−𝑥^{2}−2𝑥}{(𝑥+2)(𝑥−2)} & >0 \\ \frac{4−6𝑥}{(𝑥+2)(𝑥−2)} & >0 \\ \frac{2(2−3𝑥)}{(𝑥+2)(𝑥−2)} & >0.\end{aligned}


$$

We now proceed using the sign table method. First, we define the function $f(x)$ as

$$


f(x) = \dfrac{2(2-3x)}{(x+2)(x-2)}.


$$

So, we're now solving the inequality $f(x) > 0.$

The solution to the equation $f(x) = 0$ is $x=\dfrac{2}{3}.$ Also, $f(x)$ has vertical asymptotes at $x=-2$ and $x=2.$ The root and asymptotes divide the number line into $4$ subintervals:

$$


(-\infty,-2), \quad \left(-2,\frac{2}{3}\right), \quad \left(\frac{2}{3},2\right), \quad (2,\infty)


$$

Now, we construct a sign table with the list of the intervals on the top and the list of factors on the left. Filling in the sign table using the usual method, we get the following result:

To solve the inequality $f(x) > 0,$ we look at the bottom row to find out where $f(x)$ is negative.

From the table, we see that $f(x)$ is negative on the intervals $\left(-2,\dfrac{2}{3}\right)$ and $\left(\dfrac{2}{3},2\right).$

Therefore, we conclude that the solution to $f(x) > 0$ is

$$


x \in (-\infty,-2)\cup\left(\dfrac{2}{3},2\right).


$$
