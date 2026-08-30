# Determining Unknown Parameters in Quadratic Equations With No Real Solutions

Source: https://www.mathacademy.com/topics/6289?courseId=120
Topic ID: 6289

## Prerequisites

- [Determining Unknown Parameters in Quadratic Equations With Real Solutions](../../../high-school/traditional/lessons/precalculus/100-determining-unknown-parameters-in-quadratic-equations-with-real-solutions.md)

## Lesson

### Introduction

Recall that for a quadratic equation

$$


ax^2 + bx + c = 0,


$$

with $a\neq 0,$ the discriminant is defined as

$$


\mathcal{D} = b^2 - 4ac.


$$

A quadratic equation has no real solutions if the discriminant is negative: $\mathcal{D} < 0.$

If a quadratic equation contains an unknown parameter and we know the equation has no real solutions, we can use the condition $\mathcal D < 0$ to place conditions on the unknown parameter.

To demonstrate, let's consider the equation

$$


2x^2-5kx+10 = 0


$$

where $k$ is a real parameter. We wish to find *all* the values of $k$ for which the quadratic equation has no real solutions.

To compute the discriminant, we first note that the coefficients are

$$


a=2,\quad b=-5k,\quad c=10.


$$

So, we require

$$


\begin{aligned}D & <0 \\ 𝑏^{2}−4𝑎𝑐 & <0 \\ (−5𝑘)^{2}−4(2)(10) & <0 \\ 25𝑘^{2}−80 & <0\end{aligned}


$$

This is a quadratic inequality in the variable $k.$ Solving this equation for $k,$ we get the following:

$$


\begin{aligned}25𝑘^{2}−80 & <0 \\ 25𝑘^{2} & <80 \\ 𝑘^{2} & <\frac{16}{5} \\ \sqrt{√𝑘^{2}} & <\sqrt{√\frac{16}{5}} \\ |𝑘| & <\frac{4}{\sqrt{√5}} \\ |𝑘| & <\frac{4\sqrt{√5}}{5}.\end{aligned}


$$

Therefore, our solution is

$$


-\dfrac{4\sqrt{5}}{5} < k < \dfrac{4\sqrt{5}}{5}.


$$

We can also express this solution using interval notation:

$$


k \in \left(-\dfrac{4\sqrt{5}}{5},\dfrac{4\sqrt{5}}{5}\right)


$$

Any value of $k$ in this interval will give a quadratic equation with no real solutions.

### Example: Determining Ranges of Parameter Values in Quadratic Equations With No Real Solutions

#### Question

Given that $kx^2 + 6x + k=0,$ where $k$ is a non-zero real number, find the values of $k$ for which the equation has no real solutions.

#### Explanation

A quadratic equation has no real solutions if the discriminant is negative: $\mathcal{D} < 0.$

To compute the discriminant, note the following coefficients: $a = k,$ $b = 6$ and $c = k.$

So, we require

$$


\begin{aligned}D & <0 \\ 𝑏^{2}−4𝑎𝑐 & <0 \\ (6)^{2}−4(𝑘)(𝑘) & <0 \\ 36−4𝑘^{2} & <0 \\ 36 & <4𝑘^{2} \\ 𝑘^{2} & >9 \\ \sqrt{√𝑘^{2}} & >\sqrt{√9} \\ |𝑘| & >3.\end{aligned}


$$

If $|k| > 3,$ then $k \lt -3$ or $k \gt 3.$ Using interval notation, then, our solution is $k \in (-\infty, -3) \cup (3, \infty).$

### Example: Determining Extreme Parameter Values in Quadratic Equations With No Real Solutions

#### Question

Given that $x(px - 24) = -9,$ where $p$ is an **** constant, has no real solutions, what is the least possible value of $p?$

#### Explanation

A quadratic equation has no real solutions if the discriminant is negative: $\mathcal{D} < 0.$

First, rewrite the equation in standard quadratic form:

$$


\begin{aligned}𝑥(𝑝𝑥−24) & =−9 \\ 𝑝𝑥^{2}−24𝑥 & =−9 \\ 𝑝𝑥^{2}−24𝑥+9 & =0\end{aligned}


$$

The coefficients of our quadratic equation are the following:

$$


a = p, \qquad b = -24, \qquad c = 9


$$

So, computing the discriminant, we get

$$


\begin{aligned}D & =𝑏^{2}−4𝑎𝑐 \\ & =(−24)^{2}−4(𝑝)(9) \\ & =576−36𝑝.\end{aligned}


$$

To have no real solutions, we need $\mathcal{D} < 0{:}$

$$


\begin{aligned}576−36𝑝 & <0 \\ −36𝑝 & <−576 \\ 𝑝 & >\frac{−576}{−36} \\ 𝑝 & >16\end{aligned}


$$

Since $p$ must be an integer, we conclude that the least possible value is $17.$
