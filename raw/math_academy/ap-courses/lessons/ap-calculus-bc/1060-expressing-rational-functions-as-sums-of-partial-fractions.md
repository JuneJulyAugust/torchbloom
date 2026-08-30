# Expressing Rational Functions as Sums of Partial Fractions

Source: https://www.mathacademy.com/topics/1060?courseId=21
Topic ID: 1060

## Prerequisites

- [Advanced Rational Equations](../../../high-school/traditional/lessons/precalculus/708-advanced-rational-equations.md)

## Lesson

### Introduction

Adding and subtracting fractions is usually straightforward. For example, suppose that we wanted to calculate

$$


\dfrac{1}{x-1}-\dfrac{3}{3x-2}.


$$

We can do this easily by putting each fraction over a common denominator, as follows:

$$


\begin{aligned}\frac{1}{𝑥−1}−\frac{3}{3𝑥−2} & =\frac{(3𝑥−2)−3(𝑥−1)}{(𝑥−1)(3𝑥−2)} \\ & =\frac{3𝑥−2−3𝑥+3}{(𝑥−1)(3𝑥−2)} \\ & =\frac{1}{(𝑥−1)(3𝑥−2)}.\end{aligned}


$$

But what about if we wanted to go the other way? How do we get from

$$


\dfrac{1}{(x-1)(3x-2)}


$$

to

$$


\dfrac{1}{x-1}-\dfrac{3}{3x-2}\,?


$$

Rephrasing the problem, our task is to find $A$ and $B$ so that

$$


\begin{aligned}\frac{1}{(𝑥−1)(3𝑥−2)}=\frac{𝐴}{𝑥−1}+\frac{𝐵}{3𝑥−2}.\end{aligned}


$$

Let's go through the process. First, we multiply the expression above by $(x-1)(3x-2)$ to clear out the fractions.

$$


1={A(3x-2)+B(x-1)}


$$

The equation above should be true for all $x.$ So let's plug in $x=1,$ which gets rid of the $B$ term and allows us to solve for $A.$ We get

$$


\begin{aligned}1 & =𝐴(3−2)+𝐵(1−1) \\ 1 & =𝐴.\end{aligned}


$$

On the other hand, to solve for $B,$ we substitute $x=\dfrac 2 3$, which gets rid of the $A$ term. We get

$$


\begin{aligned}1 & =𝐴(3⋅\frac{2}{3}−2)+𝐵(\frac{2}{3}−1) \\ 1 & =𝐴(2−2)+𝐵(−\frac{1}{3}) \\ 1 & =−\frac{1}{3}𝐵 \\ 𝐵 & =−3.\end{aligned}


$$

Knowing that $A=1$ and $B=-3,$ we have

$$


\dfrac{1}{(x-1)(3x-2)} = \dfrac{1}{x-1}-\dfrac{3}{3x-2},


$$

and we're done! This process is called **partial fractions decomposition**. In this case, the **partial fractions** are $\dfrac{1}{x-1}$ and $-\dfrac{3}{3x-2}.$

### Example: Expressing a Rational Function With Two Linear Factors as a Sum of Partial Fractions

#### Question

Express $\dfrac{2x-1}{(x+2)(x-3)}$ as a sum of partial fractions.

#### Explanation

Our task is to find $A$ and $B$ such that

$$


\dfrac{2x-1}{(x+2)(x-3)} = \dfrac{A}{(x+2)} +\dfrac{B}{(x-3)}.


$$

Multiplying the above expression through by $(x+2)(x-3)$ gives

$$


2x-1= A(x-3)+B(x+2).


$$

Plugging in $x=-2$ gets rid of the $B$ term and allows us to solve for $A.$ We get

$$


\begin{aligned}2(−2)−1 & =𝐴(−2−3)+𝐵(−2+2) \\ −5 & =𝐴(−5)+𝐵(0) \\ 𝐴 & =1.\end{aligned}


$$

On the other hand, plugging in $x=3$ gets rid of the $A$ term and allows us to solve for $B.$ We get

$$


\begin{aligned}2(3)−1 & =𝐴(3−3)+𝐵(3+2) \\ 5 & =𝐴(0)+𝐵(5) \\ 𝐵 & =1.\end{aligned}


$$

Knowing that $A=1$ and $B=1,$ we have

$$


\dfrac{2x-1}{(x+2)(x-3)} = \dfrac{1}{(x+2)} +\dfrac{1}{(x-3)}.


$$

### Example: Expressing a Rational Function With Three Linear Factors as a Sum of Partial Fractions

#### Question

Express $\dfrac{2x^2+5x+7}{(x+2)(x-3)(x+1)}$ as a sum of partial fractions.

#### Explanation

Our task is to find $A,$ $B,$ and $C$ such that

$$


\dfrac{2x^2+5x+7}{(x+2)(x-3)(x+1)} = \dfrac{A}{x+2} + \dfrac{B}{x-3} + \dfrac{C}{x+1}.


$$

First, we multiply both sides of the equation by $(x+2)(x-3)(x+1)$ to clear the fractions:

$$


2x^2+5x+7= A(x-3)(x+1)+B(x+2)(x+1)+C(x+2)(x-3)


$$

Plugging in $x=-2$ gets rid of the $B$ and $C$ terms and allows us to solve for $A.$ We get

$$


\begin{aligned}2(−2)^{2}+5(−2)+7 & =𝐴(−2−3)(−2+1) \\ 5 & =𝐴(5) \\ 𝐴 & =1.\end{aligned}


$$

On the other hand, plugging in $x=3$ gets rid of the $A$ and $C$ terms and allows us to solve for $B.$ We get

$$


\begin{aligned}2(3)^{2}+5(3)+7 & =𝐵(3+2)(3+1) \\ 40 & =𝐵(20) \\ 𝐵 & =2.\end{aligned}


$$

Finally, plugging in $x=-1$ gets rid of the $A$ and $B$ terms and allows us to solve for $C.$ We get

$$


\begin{aligned}2(−1)^{2}+5(−1)+7 & =𝐶(−1+2)(−1−3) \\ 4 & =𝐶(−4) \\ 𝐶 & =−1.\end{aligned}


$$

Knowing that $A=1,$ $B=2,$ and $C=-1,$ we have

$$


\dfrac{2x^2+5x+7}{(x+2)(x-3)(x+1)} = \dfrac{1}{x+2} +\dfrac{2}{x-3} -\dfrac{1}{x+1}.


$$
