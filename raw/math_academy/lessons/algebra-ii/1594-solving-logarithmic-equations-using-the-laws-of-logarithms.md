# Solving Logarithmic Equations Using the Laws of Logarithms

Source: https://www.mathacademy.com/topics/1594?courseId=51
Topic ID: 1594

## Prerequisites

- [Solving Quadratic Equations by Factoring](../algebra-i/375-solving-quadratic-equations-by-factoring.md)
- [Solving Quadratic Equations with No Constant Term](../algebra-i/393-solving-quadratic-equations-with-no-constant-term.md)
- [Solving Equations Using the Square Root Method](../algebra-i/430-solving-equations-using-the-square-root-method.md)
- [Solving Rational Equations Containing One Fractional Term](../algebra-i/1415-solving-rational-equations-containing-one-fractional-term.md)
- [The Quotient Rule for Logarithms](./1474-the-quotient-rule-for-logarithms.md)
- [Solving Logarithmic Equations Containing the Natural Logarithm](./1551-solving-logarithmic-equations-containing-the-natural-logarithm.md)

## Lesson

### Introduction

We can use the laws of logarithms to solve equations containing logarithms. First, let's recall the laws of logarithms:

**Product Rule**:

$\log_b(xy) = \log_b(x) + \log_b(y)$

**Quotient Rule:**

$\log_b\left(\dfrac x y\right) = \log_b(x) - \log_b(y)$

**Power Rule**:

$\log_b\left(x^n\right) = n\log_b(x)$

As an example, let's solve the following equation:

$$


\ln \left( 2x\right) + \ln (2)=3


$$

Since the logarithms on the left-hand side share a common base, we can use the product rule to combine them:

$$


\begin{aligned}ln⁡(2𝑥)+ln⁡(2) & =3 \\ ln⁡(2𝑥⋅2) & =3 \\ ln⁡(4𝑥) & =3\end{aligned}


$$

Next, we exponentiate both sides of the equation, and we get

$$


\begin{aligned}𝑒^{ln⁡(4𝑥)} & =𝑒^{3} \\ 4𝑥 & =𝑒^{3} \\ 𝑥 & =\frac{𝑒^{3}}{4}\end{aligned}


$$

Therefore, the solution is $x=\dfrac{e^3}{4}.$

### Example: Solving Logarithmic Equations Using the Product Rule

#### Question

Find the exact solution to $2\log_2 (x-4) + 2\log _2 (3) =4.$

#### Explanation

The logarithms share the same base, and so we can combine them using the product rule, as follows:

$$


\begin{aligned}2log_{2}⁡(𝑥−4)+2log_{2}⁡(3) & =4 \\ 2[log_{2}⁡(𝑥−4)+log_{2}⁡(3)] & =4 \\ 2log_{2}⁡(3(𝑥−4)) & =4 \\ 2log_{2}⁡(3𝑥−12) & =4 \\ log_{2}⁡(3𝑥−12) & =\frac{4}{2} \\ log_{2}⁡(3𝑥−12) & =2\end{aligned}


$$

Now, we solve the equation for $x$ using the usual methods.

$$


\begin{aligned}2^{log_{2}⁡(3𝑥−12)} & =2^{2} \\ 3𝑥−12 & =4 \\ 3𝑥 & =16 \\ 𝑥 & =\frac{16}{3}\end{aligned}


$$

### Example: Solving Logarithmic Equations Using the Quotient Rule

#### Question

Find the solution to $\log\left(x \right) - \log \left(2 \right) = 1.$

#### Explanation

The logarithms share the same base, so we can combine them using the quotient rule, as follows:

$$


\begin{aligned}log⁡(𝑥)−log⁡(2) & =1 \\ log⁡(\frac{𝑥}{2}) & =1\end{aligned}


$$

Now, we solve the equation for $x$ using the usual methods.

$$


\begin{aligned}10^{log⁡(𝑥/2)} & =10^{1} \\ \frac{𝑥}{2} & =10 \\ 𝑥 & =20\end{aligned}


$$

### Extraneous Solutions

When solving logarithmic equations, it is sometimes possible to get **extraneous solutions** that do not satisfy the original equation. This often occurs when a logarithmic equation results in a quadratic equation.

As an example, let's consider the following equation:

$$


\ln \left( x\right) + \ln \left(4x\right)=0


$$

Since the logarithms on the left-hand side share a common base, we can use the product rule to combine them:

$$


\begin{aligned}ln⁡(𝑥)+ln⁡(4𝑥)=0 & \\ ln⁡(𝑥⋅4𝑥) & =0 \\ ln⁡(4𝑥^{2}) & =0\end{aligned}


$$

Next, we exponentiate both sides of the equation, and we get

$$


\begin{aligned}𝑒^{ln⁡(4𝑥^{2})} & =𝑒^{0} \\ 4𝑥^{2} & =1 \\ 𝑥^{2} & =\frac{1}{4} \\ 𝑥 & =±\sqrt{√\frac{1}{4}} \\ 𝑥 & =±\frac{1}{2}.\end{aligned}


$$

So, $x = \dfrac12$ or $x = -\dfrac12$ are *possible* solutions.

Let's now check for extraneous solutions by substituting them back into the original equation:

- Substituting $x=\dfrac12$ back into the original equation, we get Substituting $x=\dfrac12$ back into the original equation gave a true statement. Therefore, $x=\dfrac12$ is a valid solution.

- Substituting $x=-\dfrac12$ back into the original equation, we get This is not a true statement because $\ln\left(-\dfrac12\right)$ and $\ln\left(-2\right)$ are undefined. Therefore, $x=-\dfrac12$ is *not* a valid solution.

Therefore, the only solution is $x=\dfrac12.$

### Example: Solving Equations Resulting in Quadratic Equations Using the Product Rule

#### Question

Solve the equation $\log_2x + \log_2(x + 3) = 2.$

#### Explanation

The logarithms on the left-hand side share the same base, so we can combine them using the product rule as follows:

$$


\begin{aligned}log_{2}⁡𝑥+log_{2}⁡(𝑥+3) & =2 \\ log_{2}⁡[𝑥(𝑥+3)] & =2\end{aligned}


$$

Now, we solve the equation for $x$ using the usual methods.

$$


\begin{aligned}𝑥(𝑥+3) & =2^{2} \\ 𝑥^{2}+3𝑥 & =4 \\ 𝑥^{2}+3𝑥−4 & =0 \\ (𝑥+4)(𝑥−1) & =0.\end{aligned}


$$

So, $x = -4$ or $x = 1.$

Let's now check for extraneous solutions by substituting them back into the original equation:

- Substituting $x=1$ back into the original equation, we get Therefore, $x=1$ is a valid solution.

- Substituting $x=-4$ back into the original equation, we get because $\log_2 (-4)$ and $\log_2(-1)$ are undefined. Therefore, $x=-4$ is not a valid solution.

Therefore, the only solution is $x=1.$
