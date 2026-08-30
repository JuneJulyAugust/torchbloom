# Completing the Square With Odd Linear Terms

Source: https://www.mathacademy.com/topics/3842?courseId=111
Topic ID: 3842

## Prerequisites

- [Completing the Square](./450-completing-the-square.md)

## Lesson

### Introduction

Let's recall the formula for factoring a perfect square:

$$


x^2 + {\color{red}{2}}{\color{blue}{a}}x + a^2 = (x + {\color{blue}{a}})^2


$$

As we've seen, **completing the square** on a quadratic expression means expressing it as the sum of a perfect square and a constant.

In this lesson, we'll learn how to complete the square on a quadratic expression when the coefficient of the linear term is odd. In these cases, we get a fraction in the final expression.

As an example, let's consider the following quadratic expression:

$$


\left(x^2 + 5x + \left(\dfrac 52\right)^2\right) + 1


$$

Notice that we have a perfect square in the large parentheses that we can factor as follows:

$$


\begin{aligned}𝑥^{2}+5𝑥+(\frac{5}{2})^{2} & = \\ 𝑥^{2}+2⋅\frac{5}{2}𝑥+(\frac{5}{2})^{2} & = \\ (𝑥+\frac{5}{2})^{2} & \end{aligned}


$$

Therefore, our original expression can be written as

$$


\begin{aligned}(𝑥+\frac{5}{2})^{2}+1.\end{aligned}


$$

Let's see another example.

### Example: Completing the Square When the Perfect Square Is Isolated

#### Question

Rewrite the expression

$$


\left(x^2 + 7x + \dfrac{49}{4}\right) + 3


$$

as the sum of a perfect square and a constant.

#### Explanation

First, we recall the following formula:

$$


x^2 + {\color{red}{2}}{\color{blue}{a}}x + a^2 = (x + {\color{blue}{a}})^2


$$

Notice that we have a perfect square in the parentheses that we can factor as follows:

$$


\begin{aligned}𝑥^{2}+7𝑥+\frac{49}{4} & = \\ 𝑥^{2}+7𝑥+(\frac{7}{2})^{2} & = \\ 𝑥^{2}+2⋅\frac{7}{2}𝑥+(\frac{7}{2})^{2} & = \\ (𝑥+\frac{7}{2})^{2} & \end{aligned}


$$

Therefore, we obtain

$$


\begin{aligned}(𝑥^{2}+7𝑥+\frac{49}{4})+3 & = \\ (𝑥+\frac{7}{2})^{2}+3 & .\end{aligned}


$$

### Completing the Square

Let's complete the square on the following expression:

$$


x^2 + 3x + 4


$$

The procedure is very similar to the one we encountered when the coefficient of the linear term was even.

First, we rewrite the coefficient of the linear term as a product with ${\color{red}{2}}$ as a factor:

$$


x^2 + {\color{red}{2}}\cdot {\color{blue}{\dfrac{3}{2}}}x + {\color{purple}{4}}


$$

Now, here's the trick. We *add* and *then subtract* $\left({\color{blue}{\dfrac{3}{2}}}\right)^2,$ writing the constant term ${\color{purple}{4}}$ last:

$$


x^2 + {\color{red}{2}}\cdot {\color{blue}{\dfrac{3}{2}}}x + \left({\color{blue}{\dfrac{3}{2}}}\right)^2 - \left({\color{blue}{\dfrac{3}{2}}}\right)^2 + {\color{purple}{4}}


$$

As a result, the first three terms now form a perfect square!

$$


\underbrace{x^2 + {\color{red}{2}}\cdot {\color{blue}{\dfrac{3}{2}}}x + \left({\color{blue}{\dfrac{3}{2}}}\right)^2} - \left({\color{blue}{\dfrac{3}{2}}}\right)^2 + {\color{purple}{4}}


$$

Factoring the perfect square, we get

$$


\left(x + {\color{blue}{\dfrac{3}{2}}}\right)^2 - \left({\color{blue}{\dfrac{3}{2}}}\right)^2 + {\color{purple}{4}}.


$$

Finally, evaluating the last two terms, we get

$$


\begin{aligned}(𝑥+\frac{3}{2})^{2}−(\frac{3}{2})^{2}+4 & = \\ (𝑥+\frac{3}{2})^{2}−\frac{9}{4}+4 & = \\ (𝑥+\frac{3}{2})^{2}−\frac{9}{4}+\frac{16}{4} & = \\ (𝑥+\frac{3}{2})^{2}+\frac{7}{4} & .\end{aligned}


$$

### Example: Completing the Square on a Quadratic Expression

#### Question

Complete the square on the quadratic expression $x^2 + 7x - 1.$

#### Explanation

First, we rewrite the coefficient of the linear term as a product with ${\color{red}{2}}$ as a factor:

$$


x^2 + {\color{red}{2}}\cdot {\color{blue}{\dfrac{7}{2}}}x - {\color{purple}{1}}


$$

Now, here's the trick. We ** and ** $\left({\color{blue}{\dfrac{7}{2}}}\right)^2,$ writing the constant term ${\color{purple}{-1}}$ last:

$$


\underbrace{x^2 + {\color{red}{2}}\cdot {\color{blue}{\dfrac{7}{2}}}x + \left({\color{blue}{\dfrac{7}{2}}}\right)^2} - \left({\color{blue}{\dfrac{7}{2}}}\right)^2 - {\color{purple}{1}}


$$

The first three terms form a perfect square, which we factor as follows:

$$


\left(x + {\color{blue}{\dfrac{7}{2}}}\right)^2 - \left({\color{blue}{\dfrac{7}{2}}}\right)^2 - {\color{purple}{1}}


$$

Finally, evaluating the last two terms, we get

$$


\left(x + {\color{blue}{\dfrac{7}{2}}}\right)^2 - \dfrac{53}{4}.


$$

### Example: Expressions Containing a Negative Linear Term

#### Question

Complete the square on the quadratic expression $x^2 - 7x.$

#### Explanation

First, we rewrite the coefficient of the linear term as a product with ${\color{red}{2}}$ as a factor:

$$


x^2 - {\color{red}{2}}\cdot {\color{blue}{\dfrac{7}{2}}}x


$$

Now, here's the trick. We ** and ** $\left({\color{blue}{\dfrac{7}{2}}}\right)^2{:}$

$$


\underbrace{x^2 - {\color{red}{2}}\cdot {\color{blue}{\dfrac{7}{2}}}x + \left({\color{blue}{\dfrac{7}{2}}}\right)^2} - \left({\color{blue}{\dfrac{7}{2}}}\right)^2


$$

The first three terms form a perfect square, which we factor as follows:

$$


\left(x - {\color{blue}{\dfrac{7}{2}}}\right)^2 - \left({\color{blue}{\dfrac{7}{2}}}\right)^2


$$

Finally, evaluating the last term, we get

$$


\left(x - {\color{blue}{\dfrac{7}{2}}}\right)^2 - \dfrac{49}{4}.


$$
