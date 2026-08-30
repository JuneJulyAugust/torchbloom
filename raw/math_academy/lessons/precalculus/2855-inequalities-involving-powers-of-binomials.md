# Inequalities Involving Powers of Binomials

Source: https://www.mathacademy.com/topics/2855?courseId=43
Topic ID: 2855

## Prerequisites

- [Solving Elementary Quadratic Inequalities](./1495-solving-elementary-quadratic-inequalities.md)
- [Solving Equations With Even Exponents Using the Nth Root Method](../algebra-i/1587-solving-equations-with-even-exponents-using-the-nth-root-method.md)
- [Solving Equations With Odd Exponents Using the Nth Root Method](../algebra-i/3748-solving-equations-with-odd-exponents-using-the-nth-root-method.md)

## Lesson

### Introduction

When we have a power of a binomial in an inequality, we can apply a root to both sides of the inequality.

For example, to solve the inequality

$$


(x-2)^3 \leq 4,


$$

we can apply the cube root and get

$$


\begin{aligned}\sqrt[√(𝑥−2)^{3}]{3} & ≤\sqrt[√4]{3} \\ 𝑥−2 & ≤\sqrt[√4]{3} \\ 𝑥 & ≤2+\sqrt[√4]{3}\end{aligned}


$$

Note that this technique works for all roots, not just cube roots.

We're allowed to apply a root to both sides of an inequality because taking the root preserves the order of numbers. That is to say, if $a < b,$ then $\sqrt[3]{a} < \sqrt[3]{b}.$

To see this concretely, consider the following order of numbers:

$$


-2 < -1 < 0 < 0.5 < 1 < 2 < 3


$$

If we take the cube roots of all the numbers above, they stay in the same order:

$$


\underbrace{-1.26}_{ \sqrt[3]{-2} } < \underbrace{-1}_{ \sqrt[3]{-1} } < \underbrace{0}_{ \sqrt[3]{0} } < \underbrace{0.79}_{ \sqrt[3]{0.5} } < \underbrace{1}_{ \sqrt[3]{1} } < \underbrace{1.26}_{ \sqrt[3]{2} } < \underbrace{1.44}_{ \sqrt[3]{3} }


$$

### Example: Solving an Inequality Involving an Odd Power

#### Question

Solve the inequality $2(x - 2)^3 - 5 \gt 11.$

#### Explanation

Isolating the cubic term, we find

$$


\begin{aligned}2(𝑥−2)^{3}−5 & >11 \\ 2(𝑥−2)^{3} & >16 \\ (𝑥−2)^{3} & >8.\end{aligned}


$$

Then, we take the cube root of both sides and get

$$


\begin{aligned}\sqrt[√(𝑥−2)^{3}]{3} & >\sqrt[√8]{3} \\ 𝑥−2 & >2 \\ 𝑥 & >4.\end{aligned}


$$

### Simplifying Roots of Even Powers

Remember that when we take an even root of an even power, the result simplifies to an absolute value. For example, to solve the inequality

$$


(x-2)^4 \leq 5,


$$

we can start by taking the fourth root of both sides:

$$


\sqrt[4]{(x-2)^4} \leq \sqrt[4]{5}


$$

Now, here is where it's important to be careful. The expression $\sqrt[4]{(x-2)^4}$ does *not* simplify to $x-2.$ Rather, it simplifies to the absolute value, $|x-2|.$ So, it becomes

$$


|x-2| \leq \sqrt[4]{5}.


$$

This corresponds to the following compound inequality:

$$


-\sqrt[4]{5} \leq x-2 \leq \sqrt[4]{5}


$$

So, the final solution is

$$


2-\sqrt[4]{5} \leq x \leq 2+\sqrt[4]{5}.


$$

**Caution:** It's only for *even* roots that we need to use the absolute value.

- If $n$ is odd, then $\sqrt[n]{x^n} = x.$ For example, $\sqrt[3]{x^3} = x.$

- If $n$ is even, then $\sqrt[n]{x^n} = |x|.$ For example, $\sqrt[4]{x^4} = |x|.$

### Example: Solving an Inequality Involving an Even Power

#### Question

Solve the inequality $\dfrac{(5x + 2)^4}{9} - 3 \gt 6.$

#### Explanation

Isolating the quartic term, we find

$$


\begin{aligned}\frac{(5𝑥+2)^{4}}{9}−3 & >6 \\ \frac{(5𝑥+2)^{4}}{9} & >9 \\ (5𝑥+2)^{4} & >81.\end{aligned}


$$

Now, we take the fourth root of both sides and get

$$


\begin{aligned}\sqrt[√(5𝑥+2)^{4}]{4} & >\sqrt[√81]{4} \\ |5𝑥+2| & >3.\end{aligned}


$$

This corresponds to the following compound inequality:

$$


5x + 2 \lt -3 \qquad \textrm{or} \qquad 5x + 2 \gt 3


$$

We can solve each inequality using the usual methods.

$$


\begin{aligned}5𝑥+2 & <−3 & & & 5𝑥+2 & >3 \\ 5𝑥 & <−5 & & & 5𝑥 & >1 \\ 𝑥 & <−1 & & & 𝑥 & >\frac{1}{5}\end{aligned}


$$

Therefore, the solution is

$$


x \lt -1 \quad \textrm{or} \quad x \gt \dfrac{1}{5}.


$$

### Comparing an Even Power to a Negative Number

Sometimes we might not be able to find an even root of both sides of inequality due to a negative number. For example, this happens in the following inequality:

$$


(x-2)^4 \geq -5


$$

We can't take the fourth root of both sides because $\sqrt[4]{-5}$ is not a real number. In general, an even root of a negative number is not a real number.

What we can do instead, though, is realize that an even power of a number is always greater than or equal to $0.$ In particular, in our situation, we have

$$


(x-2)^4 \geq 0


$$

for all values of $x$ because the power $(4)$ is even.

So, because $(x-2)^4 \geq 0$ for all values of $x,$ we have $(x-2)^4 \geq -5$ for all values of $x,$ and we conclude that the solution consists of all real numbers.

**Note:** If the inequality were flipped, i.e., $(x-2)^4 \leq -5,$ then the inequality would have no real solution. The reasoning is the same: because $4$ is an even power, we must have $(x-2)^4 \geq 0$ for all values of $x,$ so we can never have $(x-2)^4 \leq -5.$

In general, if we have an inequality that compares an even power to a negative number, it will always be the case that either the solution consists of all real numbers, or there is no real solution.

### Example: Solving an Inequality Involving an Even Power Compared To a Negative Number

#### Question

Solve $(5x-1)^6 + 5 \geq -4.$

#### Explanation

Isolating the sixth-degree term, we find

$$


\begin{aligned}(5𝑥−1)^{6}+5 & ≥−4 \\ (5𝑥−1)^{6} & ≥−9.\end{aligned}


$$

Note that $(5x - 1)^{6} \geq 0$ for all values of $x$ because the power $(6)$ is even.

Therefore, the solution to the given inequality is all real numbers.
