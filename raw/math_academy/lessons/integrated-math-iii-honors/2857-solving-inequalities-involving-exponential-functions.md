# Solving Inequalities Involving Exponential Functions

Source: https://www.mathacademy.com/topics/2857?courseId=101
Topic ID: 2857

## Prerequisites

- [Combining the Laws of Logarithms](../algebra-ii/30-combining-the-laws-of-logarithms.md)
- [Solving Exponential Equations With Different Bases Using Logarithms](../algebra-ii/3737-solving-exponential-equations-with-different-bases-using-logarithms.md)
- [Further Solving Linear Inequalities](../grade-7/4034-further-solving-linear-inequalities.md)

## Lesson

### Introduction

When we have an exponential function in an inequality and the base of the exponential is greater than $1,$ we can take the logarithm of both sides of the inequality.

For example, to solve the inequality

$$


2^x < 3,


$$

we can take the logarithm (base $2$) of both sides and get

$$


\begin{aligned}log_{2}⁡(2^{𝑥}) & <log_{2}⁡(3) \\ 𝑥 & <log_{2}⁡(3).\end{aligned}


$$

The reason why we're allowed to take a logarithm of both sides of an inequality is that taking a logarithm preserves the order of numbers. That is to say, if $a < b,$ then $\log_n (a) < \log_n (b),$ provided that $n > 1$ and $a,b>0.$

To see this concretely, consider the following order of numbers:

$$


0.5 < 1 < 2 < 3


$$

If we take the logarithm (base $2$) of all the numbers above, they stay in the same order:

$$


\underbrace{-1}_{ \log_2(0.5) } < \underbrace{0}_{ \log_2(1) } < \underbrace{1}_{ \log_2(2) } < \underbrace{ \,\, 1.585 \,\, }_{ \log_2(3) }


$$

### Example: Solving an Inequality When the Base of the Exponential is Greater Than One

#### Question

Solve the inequality $4e^x - 5 > 0.$

#### Explanation

Isolating the exponential term, we find

$$


\begin{aligned}4𝑒^{𝑥}−5 & >0 \\ 4𝑒^{𝑥} & >5 \\ 𝑒^{𝑥} & >\frac{5}{4}.\end{aligned}


$$

Then, taking the natural logarithm of both sides and applying the laws of logarithms, we get

$$


\begin{aligned}ln⁡(𝑒^{𝑥}) & >ln⁡(\frac{5}{4}) \\ 𝑥 & >ln⁡5−ln⁡4.\end{aligned}


$$

### The Case When the Base of the Exponential is Between Zero and One

When we have an exponential function in an inequality and the base of the exponential is *less* than $1,$ we can't take a logarithm of both sides using that same base. To see why not, consider the following inequality:

$$


\dfrac{1}{2} \lt 1


$$

If we take a logarithm with base $\dfrac{1}{2}$ of both sides, then we get a false statement:

$$


\begin{aligned}log_{\frac{1}{2}}⁡(\frac{1}{2}) & ≮log_{\frac{1}{2}}⁡(1) \\ 1 & ≮0\end{aligned}


$$

However, we can get around this problem by always taking a logarithm with a base that's *greater* than $1,$ such as the natural logarithm $\ln,$ which has base $e \approx 2.71 \,.$ Then we can use the laws of logarithms to simplify the result.

For example, consider the following inequality:

$$


\left( \dfrac{2}{3} \right)^x < 5


$$

We can't take $\log_\frac{2}{3}$ of both sides, but we can take the natural logarithm of both sides and simplify the result using the laws of logarithms:

$$


\begin{aligned}ln⁡[(\frac{2}{3})^{𝑥}] & <ln⁡5 \\ 𝑥ln⁡(\frac{2}{3}) & <ln⁡5 \\ 𝑥(ln⁡2−ln⁡3) & <ln⁡5\end{aligned}


$$

Lastly, note that $\ln 2 - \ln 3$ is a negative quantity, so when we divide both sides by it, we need to flip the inequality:

$$


\begin{aligned}𝑥 & >\frac{ln⁡5}{ln⁡2−ln⁡3}\end{aligned}


$$

### Example: Solving an Inequality When the Base of the Exponential is Between Zero and One

#### Question

Solve the inequality $5 \cdot \left(\dfrac{3}{4} \right)^x + 2 \geq 12.$

#### Explanation

Isolating the exponential term, we find

$$


\begin{aligned}5⋅(\frac{3}{4})^{𝑥}+2 & ≥12 \\ 5⋅(\frac{3}{4})^{𝑥} & ≥10 \\ (\frac{3}{4})^{𝑥} & ≥2.\end{aligned}


$$

Then, taking the natural logarithm of both sides and applying the laws of logarithms, we get

$$


\begin{aligned}ln⁡[(\frac{3}{4})^{𝑥}] & ≥ln⁡2 \\ 𝑥ln⁡(\frac{3}{4}) & ≥ln⁡2 \\ 𝑥(ln⁡3−ln⁡4) & ≥ln⁡2.\end{aligned}


$$

Lastly, note that $\ln 3 - \ln 4$ is a negative quantity, so when we divide both sides by it, we need to flip the inequality:

$$


\begin{aligned}𝑥 & ≤\frac{ln⁡2}{ln⁡3−ln⁡4}\end{aligned}


$$

### Comparing an Exponential to Zero or a Negative Number

Sometimes we might not be able to find the logarithm of both sides of inequality due to a negative number. For example, this happens in the following inequality:

$$


3^{x-1} \geq -5


$$

We can't take the logarithm of both sides because $\ln (-5)$ is not a real number. In general, a logarithm of a negative number is not a real number.

What we can do instead, though, is realize that a power of a positive number is always greater than $0.$ In particular, in our situation, we have

$$


3^{x-1} > 0


$$

for all values of $x$ because any power of $3$ is positive.

So, because $3^{x-1} > 0$ for all values of $x,$ we have $3^{x-1} \geq -5$ for all values of $x,$ and we conclude that the solution consists of all real numbers.

**Note:** If the inequality were flipped, i.e., $3^{x-1} \leq -5,$ then the inequality would have no real solution. The reasoning is the same: because any power of $3$ is positive, we must have $3^{x-1} > 0$ for all values of $x,$ so we can never have $3^{x-1} \leq -5.$

In general, if we have an inequality that compares a power of a positive number to zero or a negative number, it will always be the case that either the solution consists of all real numbers, or there is no real solution.

### Example: Solving an Inequality When the Exponential is Compared to Zero or a Negative Number

#### Question

Solve the inequality $4 \cdot 3^{8-x} + 12 > 0.$

#### Explanation

Isolating the exponential term, we find

$$


\begin{aligned}4⋅3^{8−𝑥}+12 & >0 \\ 4⋅3^{8−𝑥} & >−12 \\ 3^{8−𝑥} & >−3.\end{aligned}


$$

Because a power of a positive number is always greater than $0,$ we must have

$$


3^{8-x} > 0


$$

for all values of $x.$

Therefore, the inequality $3^{8-x} > -3$ is satisfied for all real values of $x.$

### Equations with Exponential Functions on Both Sides

When an inequality has exponential functions on both sides, we can often solve it by taking a logarithm of both sides and applying the laws of logarithms.

For example, consider the inequality

$$


2^{x} < 3^{1-x}.


$$

Taking the natural logarithm of both sides and applying the laws of logarithms, we solve the equation as follows:

$$


\begin{aligned}ln⁡(2^{𝑥}) & <ln⁡(3^{1−𝑥}) \\ 𝑥ln⁡2 & <(1−𝑥)ln⁡3 \\ 𝑥ln⁡2 & <ln⁡3−𝑥ln⁡3 \\ 𝑥ln⁡2+𝑥ln⁡3 & <ln⁡3 \\ 𝑥(ln⁡2+ln⁡3) & <ln⁡3 \\ 𝑥 & <\frac{ln⁡3}{ln⁡2+ln⁡3}\end{aligned}


$$

**Note:** Other times, it's possible to run into cases where there is no real solution, or where the solution is all real numbers. For example, consider the following equation:

$$


2^{x} < -3^{1-x}


$$

Since $2^x$ is always positive and $-3^{1-x}$ is always negative, we always have $2^x > -3^{1-x}.$ This means the above inequality has no real solutions.

### Example: Solving an Inequality with Exponential Functions on Both Sides

#### Question

Solve the inequality $3 \cdot 5^x < 7^{3-x}.$

#### Explanation

Taking the natural logarithm of both sides and applying the laws of logarithms, we get the following:

$$


\begin{aligned}3⋅5^{𝑥} & <7^{3−𝑥} \\ ln⁡(3⋅5^{𝑥}) & <ln⁡(7^{3−𝑥}) \\ ln⁡3+ln⁡(5^{𝑥}) & <ln⁡(7^{3−𝑥}) \\ ln⁡3+𝑥ln⁡5 & <(3−𝑥)ln⁡7 \\ ln⁡3+𝑥ln⁡5 & <3ln⁡7−𝑥ln⁡7 \\ 𝑥ln⁡5+𝑥ln⁡7 & <3ln⁡7−ln⁡3 \\ 𝑥(ln⁡5+ln⁡7) & <3ln⁡7−ln⁡3 \\ 𝑥 & <\frac{3ln⁡7−ln⁡3}{ln⁡5+ln⁡7}\end{aligned}


$$
