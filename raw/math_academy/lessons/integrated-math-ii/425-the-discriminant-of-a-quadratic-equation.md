# The Discriminant of a Quadratic Equation

Source: https://www.mathacademy.com/topics/425?courseId=133
Topic ID: 425

## Prerequisites

- [The Quadratic Formula](../algebra-i/422-the-quadratic-formula.md)
- [Rational Numbers as Finite or Repeating Decimals](../grade-7/7011-rational-numbers-as-finite-or-repeating-decimals.md)

## Lesson

### Introduction

Given a quadratic equation in the form

$$


ax^2+bx+c=0,


$$

we can find its roots using the quadratic formula:

$$


x = \dfrac{-b \pm \sqrt{\color{blue}b^2 - 4ac}}{2a}


$$

In this formula, the expression under the square root is called the **discriminant**:

$$


\mathcal{D} = {\color{blue}b^2 - 4ac}


$$

The value of the discriminant $\mathcal{D}$ tells us a lot about the solutions of our quadratic equation.

- If $\mathcal{D}>0,$ then we get $2$ distinct real solutions: one with the positive square root and one with the negative square root.

- If $\mathcal{D}=0,$ then we get $1$ real solution because the square root vanishes. We sometimes say that the equation has two equal solutions.

- If $\mathcal{D}<0,$ then we get no real solutions.

Let's illustrate with some examples:

- If $x^2+3x+2=0,$ then we have a positive discriminant $\mathcal{D}=3^2-4(1)(2) = 1$ and $2$ distinct real solutions:

- If $x^2+2x+1=0,$ then we have a zero discriminant $\mathcal{D}=2^2-4(1)(1) = 0$ and $1$ distinct real solution:

- If $x^2+x+1=0,$ then we have a negative discriminant $\mathcal{D}=1^2-4(1)(1) = -3$ and no real solutions:

### Example: Calculating the Discriminant of a Quadratic Equation

#### Question

Calculate the discriminant of the quadratic equation $-2x^2+5x-1=0.$

#### Explanation

We have $a=-2,$ $b=5,$ and $c=-1.$ So, we calculate the discriminant as follows:

$$


\begin{aligned}D & =𝑏^{2}−4𝑎𝑐 \\ & =(5)^{2}−4(−2)(−1) \\ & =25−8 \\ & =17\end{aligned}


$$

### Example: Using the Discriminant to Determine the Number of Solutions to a Quadratic Equation

#### Question

Consider the equation $-x^2-x+1=0.$ How many distinct real solutions does it have?

#### Explanation

To quickly determine the number of solutions, we can compute the discriminant. We have $a=-1,$ $b=-1,$ and $c=1,$ so the discriminant is as follows:

$$


\begin{aligned}D & =𝑏^{2}−4𝑎𝑐 \\ & =(−1)^{2}−4(−1)(1) \\ & =1+4 \\ & =5\end{aligned}


$$

Since the discriminant is positive $(\mathcal{D}>0),$ the equation has two distinct solutions.

### Example: Choosing a Parameter to Force a Desired Number of Solutions to a Quadratic Equation

#### Question

Find the values of $k$ for which the quadratic equation $x^2+2x+k=0$ has no real solutions.

#### Explanation

The equation has no real solutions if its discriminant is negative. So, we need to find the values of $k$ so that the discriminant is negative.

First, we calculate the discriminant. We have $a=1,$ $b=2,$ and $c=k,$ so the discriminant is as follows:

$$


\begin{aligned}D & =𝑏^{2}−4𝑎𝑐 \\ & =(2)^{2}−4(1)(𝑘) \\ & =4−4𝑘\end{aligned}


$$

Now, we find the values of $k$ such that the discriminant is negative:

$$


\begin{aligned}D & <0 \\ 4−4𝑘 & <0 \\ 4 & <4𝑘 \\ 1 & <𝑘 \\ 𝑘 & >1\end{aligned}


$$

Therefore, the given equation will have no real solutions if $k>1.$

### Rational Solutions of Quadratic Equations

Suppose we have the quadratic equation

$$


ax^2+bx+c=0


$$

where

- the coefficients $a,$ $b,$ and $c$ are all *rational numbers,* and

- the discriminant is non-negative, i.e., $\mathcal D \geq 0.$

Then, we have the following possibilities:

- If $\mathcal{D}$ is a *perfect square*, then the equation has two *rational* solutions.

- If $\mathcal{D}$ is *not* a perfect square, then the equation has two *irrational* solutions.

Let's illustrate with some examples.

Consider the equation $x^2-x-6=0.$ Its discriminant is

$$


\begin{aligned}D & =(−1)^{2}−4(1)(−6) \\ & =1+24 \\ & =25 \\ & =5^{2}\end{aligned}


$$

which is a perfect square. Consequently, the corresponding solutions are both rational numbers:

$$


x = \dfrac{1 \pm \sqrt{5^2}}{2(1)} = 3, -2


$$

Now, consider the equation $x^2-x-5=0.$ Its discriminant is

$$


\begin{aligned}D & =(−1)^{2}−4(1)(−5) \\ & =1+20 \\ & =21,\end{aligned}


$$

which is *not* a perfect square. Consequently, the solutions are both irrational numbers:

$$


x = \dfrac{1 \pm \sqrt{21}}{2}


$$

### Example: Identifying Quadratic Equations With Rational Solutions

#### Question

Consider the quadratic equation $x^2+2x -2 = 0.$ Which of the following statements are true?

1. The discriminant of the equation is a perfect square.

2. The equation has only rational solutions.

3. The equation has only irrational solutions.

#### Explanation

Let's examine our statements in turn.

- Statement I is false. We have $a=1,$ $b=2,$ and $c=-2.$ So, we calculate the discriminant as follows: And $12$ is ** a perfect square.

- Statement II is false, while statement III is true. First, notice that our quadratic equation has rational coefficients. And, since the discriminant is not a perfect square, the equation must have two irrational solutions.

Therefore, the correct answer is "III only."
