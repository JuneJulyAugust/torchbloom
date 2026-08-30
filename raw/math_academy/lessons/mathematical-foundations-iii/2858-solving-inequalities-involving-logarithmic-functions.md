# Solving Inequalities Involving Logarithmic Functions

Source: https://www.mathacademy.com/topics/2858?courseId=136
Topic ID: 2858

## Prerequisites

- [Compound AND Inequalities](../algebra-i/350-compound-and-inequalities.md)
- [Properties of Transformed Logarithmic Functions](../algebra-ii/1610-properties-of-transformed-logarithmic-functions.md)
- [Solving Logarithmic Equations With Logarithms on Both Sides](../algebra-ii/1643-solving-logarithmic-equations-with-logarithms-on-both-sides.md)

## Lesson

### Introduction

When we have a logarithm in an inequality with base $n > 1,$ we can use each side of the inequality as an exponent of $n.$

However, there is a catch: when we solve the resulting inequality, we must remember to remove extraneous solutions. We can do this by keeping only the solutions that are in the domain of the original logarithm.

For example, to solve the inequality

$$


\log_2 (x-1) < 4,


$$

we write each side of the inequality as an exponent of $2,$ and we get

$$


\begin{aligned}2^{log_{2}⁡(𝑥−1)} & <2^{4} \\ 𝑥−1 & <16 \\ 𝑥 & <17.\end{aligned}


$$

Now, we must only keep the solutions that are in the domain of the logarithm in the original inequality. To find the domain of the logarithm, we recall that the argument of the logarithm must be positive:

$$


x-1 > 0 \quad \Rightarrow \quad x > 1


$$

Our solution is $x < 17,$ which can be expressed as $(-\infty, 17).$ But the domain of the logarithm is $x > 1,$ which can be expressed as $(1, \infty).$ To find the solutions that are in the domain of the logarithm, we take the intersection:

$$


(-\infty, 17) \cap (1, \infty) = (1, 17)


$$

Therefore, the solution is $x \in (1,17),$ which can also be written as $1 < x < 17.$

### The Reason Why We Can Use Each Side as an Exponent

We're allowed to use each side of an inequality as the exponent of a number $n>1.$ But why are we allowed to do this?

The reason is that this operation preserves the ordering of numbers. That is to say, if $a < b$ and $n>1,$ then $n^a < n^b.$

To see this concretely, consider the following order of numbers:

$$


-2 < -1 < 0 < 0.5 < 1 < 2 < 3


$$

If we raise $2$ to the power of these numbers, the results stay in the same order:

$$


\underbrace{0.25}_{ 2^{-2} } < \underbrace{0.5}_{ 2^{-1} } < \underbrace{1}_{ 2^0 } < \underbrace{\,\, 1.41\ldots \,\,}_{ 2^{0.5} } < \underbrace{2}_{ 2^1 } < \underbrace{4}_{ 2^2 } < \underbrace{8}_{ 2^3 }


$$

### Example: Solving an Inequality Involving One Logarithmic Function

#### Question

Solve the inequality $\dfrac{3}{5} \ln(x+2) +1 \leq 0.$

#### Explanation

First, we isolate the logarithm:

$$


\begin{aligned}\frac{3}{5}ln⁡(𝑥+2)+1 & ≤0 \\ \frac{3}{5}ln⁡(𝑥+2) & ≤−1 \\ ln⁡(𝑥+2) & ≤−\frac{5}{3}\end{aligned}


$$

Now, we use each side of the inequality as an exponent of $e.$ We get the following:

$$


\begin{aligned}𝑒^{ln⁡(𝑥+2)} & ≤𝑒^{−5/3} \\ 𝑥+2 & ≤𝑒^{−5/3} \\ 𝑥 & ≤𝑒^{−5/3}−2\end{aligned}


$$

Now, we must only keep the solutions that are in the domain of the logarithm in the original inequality. To find the domain of the logarithm, we recall that the argument of the logarithm must be positive:

$$


x+2> 0 \quad \Rightarrow \quad x > -2


$$

Our solution is $x \leq e^{-5/3}-2,$ which can be expressed as $\left(-\infty, e^{-5/3}-2\right].$ Additionally, the domain of the logarithm is $x > -2,$ which can be expressed as $(-2, \infty).$ To find the solutions that are in the domain of the logarithm, we take the intersection:

$$


\left(-\infty, e^{-5/3}-2\right] \cap (-2, \infty) = \left(-2,e^{-5/3}-2 \right]


$$

Therefore, the solution is $x \in \left(-2, e^{-5/3}-2\right],$ which can also be written as $-2< x \leq e^{-5/3}-2.$

### Inequalities with Two Logarithms

When we have two logarithms in an inequality, we can use the same solution procedure as before: we use each side of the inequality as an exponent of the base of the logarithm.

Just remember that we still need to remove extraneous solutions. We can do this by keeping only the solutions that are in the domains of *all* the logarithms in the original inequality.

### Example: Solving an Inequality Involving Two Logarithmic Functions

#### Question

Solve the inequality

#### Explanation

We use each side of the inequality as an exponent of This gives the following:

Now, we must only keep the solutions that are in the domain of the logarithms in the original inequality. To find the domain of the logarithms, we recall that the argument of the logarithm must be positive:

Our solution is which can be expressed as Additionally, the domains of the logarithms are and which can be expressed as and respectively. To find the solutions that are in the domains of the logarithms, we take the intersection:

Therefore, the solution is which can also be written as
