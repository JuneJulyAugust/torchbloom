# Solving Quartic Equations With Complex Roots

Source: https://www.mathacademy.com/topics/3657?courseId=101
Topic ID: 3657

## Prerequisites

- [The Fundamental Theorem of Algebra with Quartic Equations](./897-the-fundamental-theorem-of-algebra-with-quartic-equations.md)
- [Solving Cubic Equations With Complex Roots](./3653-solving-cubic-equations-with-complex-roots.md)

## Lesson

### Introduction

The fundamental theorem of algebra tells us that any quartic polynomial with real coefficients has precisely four roots.

Moreover, since complex roots always come in complex conjugate pairs, if $p(x)$ is a quartic polynomial with real coefficients, we must have one of the following cases:

- $p(x)$ has $4$ real roots (some of which might be repeated).

- $p(x)$ has $2$ (possibly repeated) real roots and $2$ complex conjugate roots. For example, In this case, the real roots are $x=\pm 1,$ and the complex conjugate roots are $x=\pm\textrm i.$

- $p(x)$ has two pairs of complex conjugate roots. For example, In this case, the complex conjugate pairs of roots are $x=\pm\textrm i$ and $x=\pm 2\textrm i.$ Also, notice that it's possible for the complex conjugate pairs of roots to be repeated. For example, In this case, the roots are $x=\pm\textrm i.$ Each of these roots is a double root.

### Example: Finding All the Roots of a Quartic Equation Given Two Real Roots

#### Question

Given that $x=-1$ and $x=1$ are solutions to the equation $x^4 - 6 x^3 + 12 x^2 + 6 x - 13 = 0,$ find the remaining solutions.

#### Explanation

Let $f(x)=x^4 - 6 x^3 + 12 x^2 + 6 x - 13.$ Since $x_1=-1$ and $x_2=1$ are roots of $f(x),$ then according to the factor theorem,

$$


(x+1)(x-1) = x^2-1


$$

is a factor of $f(x).$

Next, we find the quotient when $f(x)$ is divided by $x^2-1$ using polynomial division.

$$


\begin{aligned} & \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,𝑥^{2}−6𝑥+13 \\ & 𝑥^{2}−1\,\,\,𝑥^{4}−6𝑥^{3}+12𝑥^{2}+6𝑥−13\,\, \\ & \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\underset{}{𝑥^{4}\,\,\,−\,\,\,𝑥^{2}} \\ & \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,−6𝑥^{3}+13𝑥^{2}+6𝑥 \\ & \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\underset{}{−6𝑥^{3}\,\,\,\,\,+6𝑥} \\ & \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,𝑥^{4}+3\,13𝑥^{2}\,\,\,\,−13 \\ & \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,𝑥^{4}+3\underset{}{\,13𝑥^{2}\,\,\,\,−13} \\ & \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,𝑥^{4}+3𝑥^{3}−5𝑥^{2}+15\,0\end{aligned}


$$

Thus, $f(x) = (x^2-1)(x^2-6x+13).$

To find the remaining two roots, we solve $x^2-6x+13=0$ by completing the square:

$$


\begin{aligned}𝑥^{2}−6𝑥+13 & =0 \\ (𝑥^{2}−6𝑥+3^{2})−3^{2}+13 & =0 \\ (𝑥−3)^{2}+4 & =0 \\ (𝑥−3)^{2} & =−4 \\ 𝑥−3 & =±2i \\ 𝑥 & =3±2i\end{aligned}


$$

Therefore, the solutions to our original equation are $x=\pm 1$ and $x=3\pm 2\text{i}.$

### Example: Finding All the Roots of a Quartic Equation Given One Complex Root

#### Question

Given that $x=2\text{i}$ is a solution to the quartic equation $x^4 + 13 x^2 + 36 = 0$, find all of the solutions.

#### Explanation

First, we let $f(x) = x^4 + 13 x^2 + 36.$

Since $f(x)$ has real coefficients and $x_1=2\text{i}$ is a root of $f(x),$ the complex conjugate

$$


\overline{x_1}=\overline{2\text{i}}=-2\text{i}


$$

must also be a root of $f(x).$

Now, according to the factor theorem, $\big(x-2\text{i}\big)\big(x-(-2\text{i})\big)$ is a factor of $f(x).$ Expanding the parentheses, we obtain

$$


\begin{aligned}(𝑥−2i)(𝑥−(−2i)) & =(𝑥−2i)(𝑥+2i) \\ & =(𝑥^{2}−(2i)^{2}) \\ & =𝑥^{2}+4.\end{aligned}


$$

Next, we find the quotient when $f(x)$ is divided by $x^2+4$ using long division.

$$


\begin{aligned} & \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,𝑥^{2}+9 \\ & 𝑥^{2}+4\,\,\,𝑥^{4}+13𝑥^{2}+36\,\, \\ & \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\underset{}{𝑥^{4}+4𝑥^{2}} \\ & \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,2𝑥^{4}+9𝑥^{2}+36 \\ & \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,2𝑥^{4}+\underset{}{9𝑥^{2}+36} \\ & \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,2𝑥^{4}+2𝑥^{2}+00\end{aligned}


$$

Thus, $f(x) = (x^2+4)(x^2+9).$

To find the other two roots, we solve $x^2+9 = 0{:}$

$$


\begin{aligned}𝑥^{2}+9 & =0 \\ 𝑥^{2} & =−9 \\ 𝑥 & =±3i\end{aligned}


$$

Therefore, the roots of our quartic equation are $x=\pm 2\text{i}, \, \pm 3 \text{i}.$
