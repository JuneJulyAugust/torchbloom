# Determining Polynomial Coefficients Using the Factor Theorem

Source: https://www.mathacademy.com/topics/3738?courseId=51
Topic ID: 3738

## Prerequisites

- [The Factor Theorem](./846-the-factor-theorem.md)

## Lesson

### Introduction

If we know a factor of a polynomial, then we can use the factor theorem to solve for an unknown coefficient in the polynomial.

For example, given that $(x+5)$ is a factor of $p(x) = 3x^2+19x+c,$ we can use the factor theorem to find the value of $c.$

According to the factor theorem, if $(x-r)$ is a factor of $p(x),$ then the root $x = r$ is a root of $p(x).$

Here, we are considering the factor $(x+5).$ The root of this factor can be found by setting the factor equal to $0$ and solving:

$$



\begin{aligned}𝑥+5 & =0 \\ 𝑥 & =−5\end{aligned}



$$

According to the factor theorem, since $(x+5)$ is a factor of $p(x),$ then the root $x=-5$ is a root of $p(x).$ This means $p(-5)=0,$ so we have

$$



\begin{aligned} p(-5) &= 0 \\3(-5)^2 + 19(-5) + c &= 0 \\75 - 95+ c &= 0 \\-20 + c &= 0 \\c &= 20. \end{aligned}



$$

### Example: Finding an Unknown Coefficient of a Polynomial Given a Factor

#### Question

Find $k$ for which $(3x+2)$ is a factor of $p(x)=3x^3-kx^2+4.$

#### Explanation

According to the factor theorem, if $(ax-b)$ is a factor of $p(x),$ then the root $x = \dfrac{b}{a}$ is also a root of $p(x).$

Here, we are considering the factor $(3x+2).$ The root of this factor can be found by setting the factor equal to $0$ and solving:

$$



\begin{aligned}3𝑥+2 & =0 \\ 3𝑥 & =−2 \\ 𝑥 & =−\frac{2}{3}\end{aligned}



$$

According to the factor theorem, then, since $(3x+2)$ is a factor of $p(x),$ the root $x=-\dfrac{2}{3}$ is also a root of $p(x).$ This means $p \left(-\dfrac{2}{3} \right)=0,$ so we have

$$



\begin{aligned} p\left(-\frac23\right) &= 0 \\[5pt] 3\left(-\frac23\right)^3-k\left(-\frac23\right)^2+4 &= 0 \\[5pt] -\frac89-\frac{4k}{9}+\frac{36}{9} &= 0 \\[5pt] -8 - 4k + 36 &= 0 \\[5pt] 28 &= 4k \\[5pt] k &= 7. \end{aligned}



$$

### Example: Finding Two Unknown Coefficients of a Polynomial Given Two Factors

#### Question

Given that $(x+1)$ and $(x-3)$ are factors of $f(x) = ax^3+bx^2-16x-15,$ determine the values of $a$ and $b.$

#### Explanation

According to the factor theorem, if $(x-r)$ is a factor of $f(x),$ then the root $x = r$ is also a root of $f(x).$

Here, we are considering the factors $(x+1)$ and $(x-3).$ The roots of these factors can be found by setting the factors equal to $0$ and solving:

$$



\begin{aligned}𝑥+1=0 & \,⇒\,𝑥=−1 \\ 𝑥−3=0 & \,⇒\,𝑥=3\end{aligned}



$$

According to the factor theorem, then, since $(x+1)$ and $(x-3)$ are factors of $p(x),$ the roots $x=-1$ and $x=3$ are also roots of $f(x).$ This means $f(-1)=0$ and $f(3)=0,$ so we have

$$



\begin{aligned}𝑓(−1) & =0 \\ 𝑎(−1)^{3}+𝑏(−1)^{2}−16(−1)−15 & =0 \\ −𝑎+𝑏+1 & =0 \\ 𝑎−𝑏 & =1, \\ & \\ 𝑓(3) & =0 \\ 𝑎(3)^{3}+𝑏(3)^{2}−16(3)−15 & =0 \\ 27𝑎+9𝑏−63 & =0 \\ 3𝑎+𝑏 & =7.\end{aligned}



$$

This gives a system of equations

$$



\begin{aligned}𝑎−𝑏=1 \\ 3𝑎+𝑏=7.\end{aligned}



$$

Adding the equations, we eliminate $b$ and get

$$



4a = 8\quad\Rightarrow\quad a=2.



$$

Finally, substituting $a=2$ in either equation gives $b=1.$ So our solutions are $a=2$ and $b=1.$
