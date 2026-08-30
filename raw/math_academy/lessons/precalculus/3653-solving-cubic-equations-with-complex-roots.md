# Solving Cubic Equations With Complex Roots

Source: https://www.mathacademy.com/topics/3653?courseId=43
Topic ID: 3653

## Prerequisites

- [Dividing Polynomials Using Long Division](../algebra-ii/427-dividing-polynomials-using-long-division.md)
- [The Fundamental Theorem of Algebra with Cubic Equations](./896-the-fundamental-theorem-of-algebra-with-cubic-equations.md)

## Lesson

### Introduction

The fundamental theorem of algebra tells us that any cubic polynomial with real coefficients has precisely three roots.

Moreover, since complex roots always come in complex conjugate pairs, it follows that all cubic polynomials with real coefficients must have at least one *real* root.

Therefore, if $p(x)$ is a cubic polynomial with real coefficients, we must have one of the following two cases:

- $p(x)$ has $3$ real roots (some of which might be repeated).

- $p(x)$ has $1$ real root and $2$ complex conjugate roots.

We already know how to deal with the first case. In this lesson, we will focus on the second case.

### Example: Finding the Roots of a Cubic Equation With Complex Roots Given One Real Root

#### Question

Given that $x=-2$ is a solution to the equation $x^3+8 = 0,$ find the remaining solutions.

#### Explanation

Let $f(x) = x^3+8.$ Since $x=-2$ is a root of $f(x),$ then according to the factor theorem $(x+2)$ is a factor of $f(x).$

We find the quotient when $f(x)$ is divided by $(x+2)$ using synthetic division.

$$


\begin{aligned}−2 & 1 & 0 & 0 & 8 \\ & & −2 & 4 & −8 \\ & 1 & −2 & 4 & 0\end{aligned}


$$

Thus, $f(x) = (x+2)(x^2-2x+4).$

To find the remaining two roots, we solve $x^2-2x+4 = 0$ by completing the square:

$$


\begin{aligned}𝑥^{2}−2𝑥+4 & =0 \\ 𝑥^{2}−2𝑥+1+3 & =0 \\ (𝑥−1)^{2}+3 & =0 \\ (𝑥−1)^{2} & =−3 \\ (𝑥−1)^{2} & =(\sqrt{√3}i)^{2} \\ 𝑥−1 & =±\sqrt{√3}i \\ 𝑥 & =1±\sqrt{√3}i\end{aligned}


$$

Therefore, the solutions to our original equation are $x=-2, \, 1\pm \sqrt3\textrm{i}.$

### Example: Finding the Roots of a Cubic Equation With Complex Roots Given One Complex Root

#### Question

Find all of the solutions to $x^3-3x^2+12x-10 = 0$ given that $x=1+3\text{i}$ is a solution.

#### Explanation

First, we let $f(x) = x^3-3x^2+12x-10.$

Since $f(x)$ has real coefficients and $x_1=1+3\text{i}$ is a root of $f(x),$ the complex conjugate

$$


\overline{x_1}=\overline{1+3\textrm{i}}=1-3\text{i}


$$

must also be a root of $f(x).$

Now, according to the factor theorem, $\big(x-(1+3\text{i})\big)\big(x-(1-3\text{i})\big)$ is a factor of $f(x).$ Expanding the parentheses, we obtain

$$


\begin{aligned}(𝑥−(1+3i))(𝑥−(1−3i)) & = \\ 𝑥^{2}−(1+3i+1−3i)𝑥+(1+3i)(1−3i) & = \\ 𝑥^{2}−2𝑥+(1^{2}−(3i)^{2}) & = \\ 𝑥^{2}−2𝑥+10 & .\end{aligned}


$$

Next, we find the quotient when $f(x)$ is divided by $x^2 - 2x + 10$ using polynomial division.

$$


\begin{aligned} & 𝑥^{2}−2𝑥+10\,\,\,\,\,\,𝑥−1 \\ & 𝑥^{2}−2𝑥+10\,\,\,\,𝑥^{3}−3𝑥^{2}+12𝑥−10\,\, \\ & 𝑥^{2}−2𝑥+10\,\,\,\,\,\,\underset{}{𝑥^{3}−2𝑥^{2}+10𝑥} \\ & 𝑥^{2}−2𝑥+10\,\,\,\,\,\,𝑥^{3}−0𝑥^{2}+02𝑥−10 \\ & 𝑥^{2}−2𝑥+10\,\,\,\,\,\,𝑥^{3}\underset{}{\,−\,0𝑥^{2}+02𝑥−10} \\ & 𝑥^{2}−2𝑥+10\,\,\,\,\,\,𝑥^{3}−3𝑥^{2}+12𝑥−10\end{aligned}


$$

Thus, $f(x) = (x^2 - 2x + 10)(x-1).$

To find the remaining root, we set the linear factor equal to zero and solve for $x\mathbin{:}$

$$


\begin{aligned}𝑥−1=0\,⟹\,𝑥=1\end{aligned}


$$

Therefore, the roots are $x=1, 1 \pm 3\textrm{i}.$
