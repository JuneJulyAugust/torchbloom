# Completing the Square

Source: https://www.mathacademy.com/topics/450?courseId=111
Topic ID: 450

## Prerequisites

- [Factoring Perfect Square Trinomials](../../../high-school/traditional/lessons/algebra-i/352-factoring-perfect-square-trinomials.md)

## Lesson

### Introduction

Let's recall the formula for factoring a perfect square:

$$


x^2 + {\color{red}{2}}{\color{blue}{a}}x + {\color{blue}{a}}^2 = (x + {\color{blue}{a}})^2


$$

Not all quadratic expressions are perfect squares. However, every quadratic expression can be expressed as a perfect square *plus a constant*. In this lesson, we'll learn how to write quadratic expressions in this form.

As an example, let's consider the following quadratic expression:

$$


\left(x^2 + 6x + 3^2\right) + 4


$$

Notice that we have a perfect square in the parentheses that we can factor as follows:

$$


\begin{aligned}𝑥^{2}+6𝑥+3^{2} & = \\ 𝑥^{2}+2⋅3𝑥+3^{2} & = \\ (𝑥+3)^{2} & \end{aligned}


$$

Therefore, our original expression can be written as

$$


\begin{aligned}(𝑥+3)^{2}+4.\end{aligned}


$$

And that's it! We have successfully written the original expression as a perfect square $(x + {\color{blue}3})^2$ plus a constant $(4).$

Writing a quadratic expression as a perfect square plus a constant is called **completing the square.** Completing the square is a valuable technique for solving many problems.

Let's see another example.

### Example: Completing the Square When the Perfect Square is Isolated

#### Question

Rewrite the expression $(x^2 + 14x + 49) - 8$ as the difference between a perfect square and a constant.

#### Explanation

First, we recall the following formula:

$$


x^2 + {\color{red}{2}}{\color{blue}{a}}x + a^2 = (x + {\color{blue}{a}})^2


$$

Notice that we have a perfect square in the parentheses that we can factor as follows:

$$


\begin{aligned}𝑥^{2}+14𝑥+49 & = \\ 𝑥^{2}+14𝑥+7^{2} & = \\ 𝑥^{2}+2⋅7𝑥+7^{2} & = \\ (𝑥+7)^{2} & \end{aligned}


$$

Therefore, we obtain

$$


\begin{aligned}(𝑥^{2}+14𝑥+49)−8 & = \\ (𝑥+7)^{2}−8 & .\end{aligned}


$$

### Example: Completing the Square When the Perfect Square is Isolated: Negative Linear Term

#### Question

Rewrite the expression $(x^2 - 12x + 36) -5$ as the difference between a perfect square and a constant.

#### Explanation

First, we recall the following formula:

$$


x^2 - {\color{red}{2}}{\color{blue}{a}}x + a^2 = (x - {\color{blue}{a}})^2


$$

Notice that we have a perfect square in the parentheses that we can factor as follows:

$$


\begin{aligned}𝑥^{2}−12𝑥+36 & = \\ 𝑥^{2}−12𝑥+6^{2} & = \\ 𝑥^{2}−2⋅6𝑥+6^{2} & = \\ (𝑥−6)^{2} & \end{aligned}


$$

Therefore, we obtain

$$


\begin{aligned}(𝑥^{2}−12𝑥+36)−5 & = \\ (𝑥−6)^{2}−5 & .\end{aligned}


$$

### Completing the Square

Up to now, we've completed the square on quadratic expressions whose perfect square is already isolated.

In general, isolating the perfect square in a quadratic expression requires a trick. We'll now learn how this works.

As an example, let's complete the square on the following expression:

$$


x^2+10x+{\color{purple}{15}}


$$

First, we rewrite the coefficient of the linear term ($10$) as a product with ${\color{red}{2}}$ as a factor:

$$


x^2+{\color{red}{2}}\cdot {\color{blue}{5}}x+{\color{purple}{15}}


$$

So, the linear coefficient is now decomposed into two factors, $\color{red}2$ and ${\color{blue}{5}}.$

Now, here's the trick. We *add* and then *subtract* the square of the second factor ${\color{blue}{5}},$ writing the constant term ${\color{purple}{15}}$ last:

$$


x^2+{\color{red}{2}}\cdot {\color{blue}{5}}x + {\color{blue}{5}}^2 - {\color{blue}{5}}^2 + {\color{purple}{15}}


$$

As a result, the first three terms now form a perfect square!

$$


\underbrace{x^2+{\color{red}{2}}\cdot {\color{blue}{5}}x + {\color{blue}{5}}^2} - {\color{blue}{5}}^2 + {\color{purple}{15}}


$$

Factoring the perfect square, we get

$$


(x+{\color{blue}{5}})^2 - {\color{blue}{5}}^2 + {\color{purple}{15}}


$$

Finally, we evaluate the last two terms as follows:

$$


\begin{aligned}(𝑥+5)^{2}−5^{2}+15 & = \\ (𝑥+5)^{2}−25+15 & = \\ (𝑥+5)^{2}−10 & .\end{aligned}


$$

And we're done!

We can easily check that our answer is correct by expanding the parentheses and simplifying:

$$


\begin{aligned}(𝑥+5)^{2}−10 & = \\ 𝑥^{2}+2⋅5⋅𝑥+5^{2}−10 & = \\ 𝑥^{2}+10𝑥+25−10 & = \\ 𝑥^{2}+10𝑥+15 & \,✓\end{aligned}


$$

### Example: Completing the Square on a Quadratic Expression

#### Question

Complete the square on the quadratic expression $x^2 + 2x + 3.$

#### Explanation

First, we rewrite the coefficient of the linear term as a product with ${\color{red}{2}}$ as a factor:

$$


x^2 + {\color{red}{2}}\cdot {\color{blue}{1}}x + {\color{purple}{3}}


$$

Now, here's the trick. We ** and ** ${\color{blue}{1}}^2,$ writing the constant term ${\color{purple}{3}}$ last:

$$


\underbrace{x^2 + {\color{red}{2}}\cdot {\color{blue}{1}}x + {\color{blue}{1}}^2} - \, {\color{blue}{1}}^2 + {\color{purple}{3}}


$$

The first three terms form a perfect square, which we factor as follows:

$$


(x + {\color{blue}{1}})^2 - {\color{blue}{1}}^2 + {\color{purple}{3}}


$$

Finally, evaluating the last two terms, we get

$$


(x + {\color{blue}{1}})^2 + 2.


$$

### Example: Completing the Square on a Quadratic Expression with a Negative Linear Term

#### Question

Complete the square on the quadratic expression $x^2 - 12x + 40.$

#### Explanation

First, we rewrite the coefficient of the linear term as a product with ${\color{red}{2}}$ as a factor:

$$


x^2 - {\color{red}{2}}\cdot {\color{blue}{6}}x + {\color{purple}{40}}


$$

Now, here's the trick. We ** and ** ${\color{blue}{6}}^2,$ writing the constant term ${\color{purple}{40}}$ last:

$$


\underbrace{x^2 - {\color{red}{2}}\cdot {\color{blue}{6}}x + {\color{blue}{6}}^2} - \, {\color{blue}{6}}^2 + {\color{purple}{40}}


$$

The first three terms form a perfect square, which we factor as follows:

$$


(x - {\color{blue}{6}})^2 - {\color{blue}{6}}^2 + {\color{purple}{40}}


$$

Finally, evaluating the last two terms, we get

$$


(x - {\color{blue}{6}})^2 +4.


$$
