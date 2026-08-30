# Solving Logarithmic Equations With Logarithms on Both Sides

Source: https://www.mathacademy.com/topics/1643?courseId=51
Topic ID: 1643

## Prerequisites

- [Solving Quadratic Equations by Factoring](../algebra-i/375-solving-quadratic-equations-by-factoring.md)
- [Solving Quadratic Equations with No Constant Term](../algebra-i/393-solving-quadratic-equations-with-no-constant-term.md)
- [The Discriminant of a Quadratic Equation](../algebra-i/425-the-discriminant-of-a-quadratic-equation.md)
- [The Power Rule for Logarithms](./1475-the-power-rule-for-logarithms.md)

## Lesson

### Introduction

To solve an equation that has logarithms with the same base on both sides, we can exponentiate both sides of the equation by the base. For example, consider the equation

$$


\log_3(2x-4)=\log_3(x+3).


$$

Since both sides of the equation are represented as logarithms of the same base ($3$), we can exponentiate both sides of the equation by $3.$ This gives

$$


\begin{aligned}3^{log_{3}⁡(2𝑥−4)} & =3^{log_{3}⁡(𝑥+3)} \\ 2𝑥−4 & =𝑥+3.\end{aligned}


$$

Now, we solve for $x\mathbin{:}$

$$


\begin{aligned}2𝑥−4 & =𝑥+3 \\ 𝑥 & =7\end{aligned}


$$

Therefore, $x=7$ is the solution.

**Caution:** Remember that, when solving logarithmic equations, it is sometimes possible to get *extraneous* solutions that don't actually satisfy the original equation. We can't take a logarithm of zero or a negative number.

So, once we've found the solutions, we need to substitute them back into the original equation and check that the arguments of the logarithms are positive. Substituting $x=7$ back into the original equation, we get

$$


\begin{aligned}log_{3}⁡(2𝑥−4) & \overset{=}{?}log_{3}⁡(𝑥+3) \\ log_{3}⁡(2⋅7−4) & \overset{=}{?}log_{3}⁡(7+3) \\ log_{3}⁡(10) & =log_{3}⁡(10).\,✓\end{aligned}


$$

Therefore, $x=7$ is a valid solution.

### Equating Arguments in a Logarithmic Equation

In the previous example, you may have noticed that for the logarithmic equation

$$


\log_3 (2x-4) = \log_3 (x+3),


$$

we were able to "cancel out" the logarithms and equate the arguments:

$$


2x-4 = x+3


$$

This result holds in general. Whenever the logarithms on both sides of the equation have the same base, we can equate the arguments.

**Caution:** This trick only works when the logarithms have the same base. The equation must take the form

$$


\log_n f(x) = \log_n g(x)


$$

where $n$ is the base of *both* logarithms and $f(x)$ and $g(x)$ are the arguments of the logarithms.

### Example: Solving Logarithmic Equations Containing a Constant on One Side

#### Question

If $\log_2(x^2-6)=\log_2(10),$ then what is the value of $x?$

#### Explanation

Since the logarithms on both sides of the equation have the same base, we can equate the arguments. This gives

$$


\begin{aligned}log_{2}⁡(𝑥^{2}−6) & =log_{2}⁡(10) \\ 𝑥^{2}−6 & =10 \\ 𝑥^{2} & =16 \\ 𝑥 & =±4.\end{aligned}


$$

Let's now check for extraneous solutions by substituting back into the original equation:

- Substituting $x=4$ back into the original equation, we get Therefore, $x=4$ is a valid solution.

- Substituting $x=-4$ back into the original equation, we get Therefore, $x=-4$ is a valid solution.

So, we conclude that the solutions are $x = \pm 4.$

### Example: Solving Logarithmic Equations Containing Linear Arguments on Both Sides

#### Question

Solve $\log (x-1)=\log (2x+1)$ for $x.$

#### Explanation

Since the logarithms on both sides of the equation have the same base, we can equate the arguments. This gives

$$


\begin{aligned}log⁡(𝑥−1) & =log⁡(2𝑥+1) \\ 𝑥−1 & =2𝑥+1 \\ 𝑥 & =−2.\end{aligned}


$$

Let's now check for extraneous solutions by substituting back into the original equation:

- Substituting $x=-2$ back into the original equation, we get However, $\log (-3)$ is not a real number.

Therefore, we conclude that the equation has no real solutions.

### Example: Solving Logarithmic Equations Containing Nonlinear Arguments

#### Question

Solve the equation $\ln (2x^2)=\ln (3x).$

#### Explanation

Since the logarithms on both sides of the equation have the same base, we can equate the arguments. This gives

$$


\begin{aligned}ln⁡(2𝑥^{2}) & =ln⁡(3𝑥) \\ 2𝑥^{2} & =3𝑥 \\ 2𝑥^{2}−3𝑥 & =0 \\ 𝑥(2𝑥−3) & =0 \\ 𝑥 & =0,\,\frac{3}{2}.\end{aligned}


$$

Let's now check for extraneous solutions by substituting back into the original equation:

- Substituting $x=0$ back into the original equation, we get which is not valid because $\ln \left(0\right)$ is undefined. Therefore, $x=0$ is not a valid solution.

- Substituting $x=\dfrac{3}{2}$ back into the original equation, we get Therefore, $x=\dfrac{3}{2}$ is a valid solution.

Therefore, the only solution is $x =\dfrac{3}{2}.$
