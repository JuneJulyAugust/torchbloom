# Solving Radical Inequalities

Source: https://www.mathacademy.com/topics/2856?courseId=101
Topic ID: 2856

## Prerequisites

- [Solving Radical Equations](../algebra-i/116-solving-radical-equations.md)
- [Compound AND Inequalities](../algebra-i/350-compound-and-inequalities.md)

## Lesson

### Introduction

When we have a cube root in an inequality, we can cube both sides of the inequality.

For example, to solve the inequality

$$


\sqrt[3]{x-2} \leq 4,


$$

we can cube both sides and get

$$


\begin{aligned}(\sqrt[√𝑥−2]{3})^{3} & ≤4^{3} \\ 𝑥−2 & ≤64 \\ 𝑥 & ≤66.\end{aligned}


$$

The reason why we're allowed to cube both sides of an inequality is that cubing preserves the order of numbers. That is to say, if $a < b,$ then $a^3 < b^3.$

To see this concretely, consider the following order of numbers:

$$


-2 < -1 < 0 < 0.5 < 1 < 2 < 3


$$

If we take the cubes of all the numbers above, they stay in the same order:

$$


\underbrace{-8}_{ (-2)^3 } < \underbrace{-1}_{ (-1)^3 } < \underbrace{0}_{ 0^3 } < \underbrace{0.125}_{ (0.5)^3 } < \underbrace{1}_{ 1^3 } < \underbrace{8}_{ 2^3 } < \underbrace{27}_{ 3^3 }


$$

### Example: Solving an Inequality Involving a Cube Root

#### Question

Solve the inequality $\sqrt[3]{x+3} + 1 \geq 0.$

#### Explanation

Isolating the cubic term, we find

$$


\begin{aligned}\sqrt[√𝑥+3]{3}+1 & ≥0 \\ \sqrt[√𝑥+3]{3} & ≥−1.\end{aligned}


$$

Then, we cube both sides and get

$$


\begin{aligned}(\sqrt[√𝑥+3]{3})^{3} & ≥(−1)^{3} \\ 𝑥+3 & ≥−1 \\ 𝑥 & ≥−4.\end{aligned}


$$

### Comparing a Square Root to a Negative Number

When we have a square root in an inequality, we *can't* always square both sides. To see why not, consider the following inequality:

$$


-4 \lt 3


$$

If we square both sides, then we get a false statement:

$$


\begin{aligned}(−4)^{2} & ≮3^{2} \\ 16 & ≮9\end{aligned}


$$

However, if we're comparing a square root to a negative number, there's no need to take the square root. The key is to remember that the square root of a number is always positive.

- If a square root is less than (or equal to) a negative number, then there is no solution. For example, if then there is no solution because the square root $\sqrt{x+1}$ can never be negative.

- If a square root is greater than (or equal to) a negative number, then any number we can substitute into the square root will satisfy the inequality. So, the solution is the domain of the square root. For example, if then the solution consists of all $x$ in the domain of $\sqrt{x+1}$ because $\sqrt{x+1}$ is zero or positive for all $x$ in its domain. To find the domain, we recall that the inside of the square root must be greater than or equal to $0{:}$

### Example: Solving an Inequality Involving a Square Root Compared to a Negative Number

#### Question

Solve the inequality $3\sqrt{x-2} +7 \geq 4.$

#### Explanation

First, we isolate the square root:

$$


\begin{aligned}3\sqrt{√𝑥−2}+7 & ≥4 \\ 3\sqrt{√𝑥−2} & ≥−3 \\ \sqrt{√𝑥−2} & ≥−1\end{aligned}


$$

Here, the square root is greater than a negative number $(-1),$ so any number we can substitute into the square root will satisfy the inequality. So, the solution is the domain of the square root.

To find the domain, we recall that the expression under the square root must be greater than or equal to $0{:}$

$$


x-2 \geq 0 \quad \Rightarrow \quad x \geq 2


$$

Therefore, the solution is $x \geq 2.$

### Comparing a Square Root to a Positive Number

If we have an inequality that compares a square root to a non-negative number, we can square both sides of the equation.

However, there is a catch: when we solve the resulting inequality, we must remember to remove extraneous solutions. We can do this by keeping only the solutions that are in the domain of the square root.

For example, consider the following inequality:

$$


\sqrt{x+1} < 3


$$

In this inequality, the square root is being compared to a non-negative number $(3).$ So, we can square both sides of the inequality:

$$


\begin{aligned}(\sqrt{√𝑥+1})^{2} & <3^{2} \\ 𝑥+1 & <9 \\ 𝑥 & <8\end{aligned}


$$

Now, we must only keep the solutions that are in the domain of the square root. To find the domain of the square root, we recall that the argument of the square root must be greater than or equal to zero:

$$


x+1 \geq 0 \quad \Rightarrow \quad x \geq -1


$$

Our solution is $x < 8,$ which can be expressed as $(-\infty, 8).$ But the domain of the square root is $x \geq -1,$ which can be expressed as $[-1, \infty).$ To find the solutions that are in the domain of the square root, we take the intersection:

$$


(-\infty, 8) \cap [-1, \infty) = [-1, 8)


$$

Therefore, the solution is $x \in [-1,8),$ which can also be written as $-1 \leq x < 8.$

### Example: Solving an Inequality Involving a Square Root Compared to a Positive Number

#### Question

Solve the inequality $7-\sqrt{x+3} < 5.$

#### Explanation

First, we isolate the square root:

$$


\begin{aligned}7−\sqrt{√𝑥+3} & <5 \\ −\sqrt{√𝑥+3} & <−2 \\ \sqrt{√𝑥+3} & >2\end{aligned}


$$

In this inequality, the square root is being compared to a non-negative number $(2).$ So, we can square both sides of the inequality:

$$


\begin{aligned}(\sqrt{√𝑥+3})^{2} & >2^{2} \\ 𝑥+3 & >4 \\ 𝑥 & >1\end{aligned}


$$

Now, we must only keep the solutions that are in the domain of the square root. To find the domain of the square root, we recall that the argument of the square root must be greater than or equal to zero:

$$


\begin{aligned}𝑥+3 & ≥0 \\ 𝑥 & ≥−3\end{aligned}


$$

Our solution is $x > 1,$ which can be expressed as $\left(1,\infty \right).$ The domain of the square root is $x \geq -3,$ which can be expressed as $\left[-3,\infty \right).$ To find the solutions that are in the domain of the square root, we take the intersection:

$$


\left( 1,\infty \right) \cap \left[ -3,\infty \right) =\left( 1,\infty\right)


$$

Therefore, the solution is $x \in \left(1,\infty\right),$ which can also be written as $x > 1.$
