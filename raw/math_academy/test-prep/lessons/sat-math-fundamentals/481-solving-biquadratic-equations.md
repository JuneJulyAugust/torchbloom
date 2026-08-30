# Solving Biquadratic Equations

Source: https://www.mathacademy.com/topics/481?courseId=120
Topic ID: 481

## Prerequisites

- [Solving Quadratic Equations Using a Difference of Squares](../../../high-school/traditional/lessons/algebra-i/394-solving-quadratic-equations-using-a-difference-of-squares.md)
- [Solving Quadratic Equations with Leading Coefficients by Factoring](../../../high-school/traditional/lessons/algebra-i/1422-solving-quadratic-equations-with-leading-coefficients-by-factoring.md)
- [Factoring Biquadratic Expressions](../../../high-school/traditional/lessons/algebra-ii/2336-factoring-biquadratic-expressions.md)

## Lesson

### Introduction

A **biquadratic equation** is a polynomial of degree $4$ that has only even powers of the variable. For example,

- the equation $a^{\color{blue}4}-3a^{\color{blue}2}+2=0$ is a biquadratic equation because the exponents $\color{blue}4$ and $\color{blue}2$ are both even, while

- the equation $a^{\color{blue}4}+3a^{\color{blue}1}+2=0$ is *not* a biquadratic equation because the exponents $\color{blue}4$ and $\color{blue}1$ are *not* both even.

Solving a biquadratic may seem daunting because of the higher powers, but there is a trick! We just substitute a new variable in the place of the original variable squared.

For example, to solve the equation $a^4-3a^2+2=0$, just let $b = a^2$ and substitute $b$ in the place of $a^2.$ Then, we can solve for $b$ as follows:

Let's work it out:

$$


\begin{aligned} a^4-3a^2+2 &= 0 \\\left(a^2\right)^2 - 3\left(a^2\right) +2 &= 0 \\(b)^2 - 3(b) + 2 &= 0 \\b^2 - 3b + 2&= 0 \\(b-1)(b - 2) &= 0 \\b &= 1,2 \end{aligned}


$$

We have the solutions $b=1,2.$ However, the original equation was given in terms of $a,$ so we need to find the corresponding values of $a.$ To do this, we substitute $a^2$ back in for $b$ and solve for $a\mathbin{:}$

$$


\begin{aligned}𝑎^{2} & =1 & \, & ⇒ & \,𝑎 & =±1 \\ 𝑎^{2} & =2 & \, & ⇒ & \,𝑎 & =±\sqrt{√2}\end{aligned}


$$

Therefore, the solutions are $a = \pm 1, \pm \sqrt{2}.$

### Example: Solving Biquadratic Equations When the Right-Hand Side is Zero

#### Question

Solve the equation $4x^4-4x^2+1 = 0.$

#### Explanation

We let $y = x^2$ and substitute $y$ in the place of $x^2.$ Then, we can solve for $y$ as follows:

$$


\begin{aligned} 4x^4-4x^2+1 &= 0 \\4\left(x^2\right)^2 - 4\left(x^2\right) +1 &= 0 \\4(y)^2 - 4(y) + 1 &= 0 \\4y^2 - 4y + 1 &= 0 \\(2y-1)^2 &= 0 \\2y-1 &= 0 \\y &= \dfrac{1}{2} \end{aligned}


$$

Plugging $x^2$ back in for $y,$ we get

$$


\begin{aligned} x^2 &= \dfrac 1 2 \\\sqrt{x^2} &= \sqrt{\dfrac 1 2} \\\vert x \vert &= \dfrac {\sqrt{1}} {\sqrt{2}} \\\vert x \vert &= \dfrac 1 {\sqrt{2}} \\x &= \pm \dfrac 1 {\sqrt{2}} . \end{aligned}


$$

Therefore, the solutions are $x = \pm \dfrac 1 {\sqrt{2}}.$

### Example: Solving Biquadratic Equations When the Right-Hand Side is Not Zero when Both Factors Have Roots

#### Question

Solve for $n$ where $3n^4 - 6n^2 = n^2 - 2.$

#### Explanation

First, we move all of the terms to the left-hand side so that the right-hand side becomes zero:

$$


\begin{aligned} 3n^4 - 6n^2 &= n^2 - 2 \\3n^4 - 7n^2 + 2 &= 0 \end{aligned}


$$

We let $m = n^2$ and substitute $m$ in the place of $n^2.$ Then, we can solve for $m$ as follows:

$$


\begin{aligned} 3n^4 - 7n^2 + 2 &= 0 \\3\left(n^2\right)^2 - 7\left(n^2\right) + 2 &= 0 \\3m^2 - 7m + 2 &= 0 \\(3m - 1)(m - 2) &= 0 \\m &= \dfrac 1 3, 2 \\\end{aligned}


$$

Plugging $n^2$ back in for $m$ we get

$$


\begin{aligned} n^2 &= \dfrac 1 3 \\\sqrt{n^2} &= \sqrt{\dfrac 1 3} \\\vert n \vert &= \dfrac {\sqrt{1}} {\sqrt{3}} \\\vert n \vert &= \dfrac 1 {\sqrt{3}} \\n &= \pm \dfrac 1 {\sqrt{3}}, \\\\n^2 &= 2 \\\sqrt{n^2} &= \sqrt{2} \\\vert n \vert &= \sqrt{2} \\n &= \pm \sqrt{2}. \\\end{aligned}


$$

Therefore, the solutions are $n = \pm \dfrac 1 {\sqrt{3}}, \pm \sqrt{2}.$

### Example: Solving Biquadratic Equations When the Right-Hand Side is Not Zero

#### Question

Find all real solutions of $x^4 - 2x^2 =8.$

#### Explanation

We let $t = x^2$ and substitute $t$ in the place of $x^2.$ Then, we can solve for $t$ as follows:

$$


\begin{aligned}𝑥^{4}−2𝑥^{2} & =8 \\ 𝑥^{4}−2𝑥^{2}−8 & =0 \\ (𝑥^{2})^{2}−2(𝑥^{2})−8 & =0 \\ 𝑡^{2}−2𝑡−8 & =0 \\ (𝑡+2)(𝑡−4) & =0 \\ 𝑡 & =−2,4\end{aligned}


$$

Plugging $x^2$ back in for $t$ we get two equations:

$$


\begin{aligned}𝑥^{2}=−2,\,𝑥^{2}=4.\end{aligned}


$$

The first equation $x^2 = -2$ has no real roots. However, the second equation can be solved:

$$


\begin{aligned}𝑥^{2} & =4 \\ \sqrt{√𝑥^{2}} & =\sqrt{√4} \\ |𝑥| & =2 \\ 𝑥 & =±2\end{aligned}


$$

Therefore, the real solutions are $x = \pm 2.$
