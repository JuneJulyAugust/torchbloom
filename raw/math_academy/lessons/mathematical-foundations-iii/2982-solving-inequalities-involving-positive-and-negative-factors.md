# Solving Inequalities Involving Positive and Negative Factors

Source: https://www.mathacademy.com/topics/2982?courseId=136
Topic ID: 2982

## Prerequisites

- [Compound AND Inequalities](../algebra-i/350-compound-and-inequalities.md)
- [Properties of Transformed Exponential Functions](../algebra-ii/1609-properties-of-transformed-exponential-functions.md)
- [Properties of Transformed Logarithmic Functions](../algebra-ii/1610-properties-of-transformed-logarithmic-functions.md)
- [Properties of Transformed Sine and Cosine Functions](../algebra-ii/2062-properties-of-transformed-sine-and-cosine-functions.md)

## Lesson

### Introduction

Given an inequality, we're allowed to multiply or divide both sides by an expression if we know that the expression is always positive.

For example, suppose we want to solve the inequality

$$


\dfrac{x}{1+x^2} < 0.


$$

We know that the denominator $1+x^2$ is positive for all values of $x.$ So, we can multiply both sides of the inequality by $1+x^2$ as follows:

$$


\begin{aligned}\frac{𝑥}{1+𝑥^{2}} & <0 \\ (1+𝑥^{2})⋅\frac{𝑥}{1+𝑥^{2}} & <(1+𝑥^{2})⋅0 \\ (1+𝑥^{2})⋅\frac{𝑥}{1+𝑥^{2}} & <0 \\ 𝑥 & <0\end{aligned}


$$

Therefore, the solution to the inequality is $x<0.$

### Example: Solving Inequalities Requiring Multiplication by a Positive Factor

#### Question

Solve the inequality

$$


\dfrac{2}{5x^4 +2} \lt \dfrac{5-2x}{5x^4+2}.


$$

#### Explanation

We know that the denominator $5x^4+ 2$ is positive for all values of $x.$ So, we can multiply both sides of the inequality by $5x^4+2$ and solve the resulting inequality as follows:

$$


\begin{aligned}\frac{2}{5𝑥^{4}+2} & <\frac{5−2𝑥}{5𝑥^{4}+2} \\ (5𝑥^{4}+2)⋅\frac{2}{5𝑥^{4}+2} & <(5𝑥^{4}+2)⋅\frac{5−2𝑥}{5𝑥^{4}+2} \\ 2 & <5−2𝑥 \\ 2𝑥 & <3 \\ 𝑥 & <\frac{3}{2}\end{aligned}


$$

### Example: Solving Inequalities Requiring Division by a Positive Factor

#### Question

Solve the inequality

$$


6x^3 + 3x \lt 0.


$$

#### Explanation

First, we factor:

$$


\begin{aligned}6𝑥^{3}+3𝑥 & <0. \\ 3𝑥(2𝑥^{2}+1) & <0\end{aligned}


$$

Since $2x^2 + 1$ is always positive, we can divide both sides of the inequality by this quantity. By doing this, we get

$$


\begin{aligned}\frac{3𝑥(2𝑥^{2}+1)}{2𝑥^{2}+1} & <\frac{0}{2𝑥^{2}+1} \\ 3𝑥 & <0 \\ 𝑥 & <0.\end{aligned}


$$

### Multiplying or Dividing by a Negative Factor

Given an inequality, we're also allowed to multiply or divide both sides by an expression if we know that the expression is always *negative*.

The only catch is that we have to remember to flip the sign of the inequality, like we normally do when multiplying or dividing both sides by a negative number.

For example, suppose that we have the inequality

$$


\dfrac{x}{-2-x^2} > 0.


$$

We know that the denominator $-2-x^2$ is negative for all values of $x.$ So, we can multiply both sides of the inequality by $-2-x^2,$ provided that we flip the sign of the inequality:

$$


\begin{aligned}\frac{𝑥}{−2−𝑥^{2}} & >0 \\ (−2−𝑥^{2})⋅\frac{𝑥}{−2−𝑥^{2}} & <(−2−𝑥^{2})⋅0 \\ (−2−𝑥^{2})⋅\frac{𝑥}{−2−𝑥^{2}} & <(−2−𝑥^{2})⋅0 \\ 𝑥 & <0\end{aligned}


$$

### Example: Solving Inequalities Requiring Multiplication or Division by a Negative Factor

#### Question

Solve the inequality

$$


(2\sin{x}-9)(2x) \leq 0.


$$

#### Explanation

Note that the factor $2\sin{x}-9$ is always negative. We know this because

$$


-1 \leq \sin x \leq 1 \quad \Rightarrow \quad -11 \leq 2\sin x - 9 \leq -7.


$$

Because $2\sin{x}-9$ is always negative, we can divide both sides of the inequality by this quantity, but we have to remember to flip the sign of the inequality. By doing this, we get

$$


\begin{aligned}(2sin⁡𝑥−9)(2𝑥) & ≤0 \\ \frac{(2sin⁡𝑥−9)(2𝑥)}{2sin⁡𝑥−9} & ≥\frac{0}{2sin⁡𝑥−9} \\ 2𝑥 & ≥0 \\ 𝑥 & ≥0.\end{aligned}


$$

### Example: Solving Inequalities Involving Domain Restrictions

#### Question

Solve the inequality

$$


\dfrac{x+5}{1-3x} \lt 2, \quad x \lt 0.


$$

#### Explanation

Since $x\lt 0,$ we have that

$$


\begin{aligned}𝑥 & <0 \\ −𝑥 & >0 \\ −3𝑥 & >0 \\ 1−3𝑥 & >1.\end{aligned}


$$

This means that $1-3x$ is positive for all the values of $x$ that we are considering $(x\lt 0).$ So, we can multiply both sides by $1-3x,$ and solve the resulting inequality as follows:

$$


\begin{aligned}\frac{𝑥+5}{1−3𝑥} & <2 \\ (1−3𝑥)⋅\frac{𝑥+5}{1−3𝑥} & <(1−3𝑥)⋅2 \\ 𝑥+5 & <2−6𝑥 \\ 7𝑥 & <−3 \\ 𝑥 & <−\frac{3}{7}\end{aligned}


$$

Therefore, the solution to the inequality will be the numbers that satisfy both $x \lt 0$ and $x \lt -\dfrac{3}{7}.$ So, the solution to our inequality is $x \lt -\dfrac{3}{7}.$
