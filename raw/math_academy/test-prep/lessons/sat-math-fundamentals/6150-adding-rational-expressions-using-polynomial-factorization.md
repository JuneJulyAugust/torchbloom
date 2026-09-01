# Adding Rational Expressions Using Polynomial Factorization

Source: https://www.mathacademy.com/topics/6150?courseId=120
Topic ID: 6150

## Prerequisites

- [Factoring Trinomials With Leading Coefficients](../../../high-school/traditional/lessons/algebra-i/372-factoring-trinomials-with-leading-coefficients.md)
- [Adding and Subtracting Rational Expressions](../../../high-school/traditional/lessons/algebra-ii/437-adding-and-subtracting-rational-expressions.md)
- [The Least Common Multiple of Two Polynomials](../../../high-school/traditional/lessons/algebra-ii/2626-the-least-common-multiple-of-two-polynomials.md)

## Lesson

### Introduction

We can add two rational expressions by expressing each fraction using a common denominator before performing the addition. In this lesson, we'll discuss how factoring the denominators first can make this process easier.

Let's consider the following addition problem:

$$


\dfrac{3+6x}{x^2+xy}+\dfrac{1-y}{y+x}


$$

We can write these two over a common denominator by

- multiplying the numerator and denominator of the first fraction by $y+x,$ and

- multiplying the numerator and denominator of the second fraction by $x^2+xy.$

This will lead to the common denominator $(y+x)(x^2+xy){:}$

$$


\dfrac{y+x}{y+x} \cdot \dfrac{3+6x}{x^2+xy} + \dfrac{x^2+xy}{x^2+xy} \cdot \dfrac{1-y}{y+x}


$$

This is a fairly complex-looking expression that will take some effort to simplify.

However, in this case, it turns out that we can simplify the computations by forming a simpler common denominator. Let's see how.

### Adding Rational Expressions by Factoring

Let's consider our rational expression once more.

$$


\dfrac{3+6x}{x^2+xy}+\dfrac{1-y}{y+x}


$$

Notice that we can factor the polynomial in the first denominator as

$$


x^2+xy = x(x+y).


$$

Therefore, can rewrite our expression as follows:

$$


\dfrac{3+6x}{x(x+y)}+\dfrac{1-y}{x+y}


$$

Notice that

- the denominator of the first term is $x(x+y),$

- the denominator of the second term is $(x+y),$ and

- the least common multiple of the two denominators is $x(x+y).$

Therefore, we can put these two expressions over a common denominator of $x(x+y)$ by multiplying the numerator and denominator of the *second* term by ${\color{blue}{x}},$ as follows:

$$


\begin{aligned}\frac{3+6𝑥}{𝑥(𝑥+𝑦)}+\frac{1−𝑦}{𝑥+𝑦} & =\frac{3+6𝑥}{𝑥(𝑥+𝑦)}+\frac{𝑥}{𝑥}⋅\frac{1−𝑦}{𝑥+𝑦} \\ & =\frac{3+6𝑥}{𝑥(𝑥+𝑦)}+\frac{𝑥(1−𝑦)}{𝑥(𝑥+𝑦)}\end{aligned}


$$

Notice that we obtained a much simpler expression than we did previously!

Finally, we add our expressions:

$$


\begin{aligned}\frac{3+6𝑥}{𝑥(𝑥+𝑦)}+\frac{𝑥(1−𝑦)}{𝑥(𝑥+𝑦)} & =\frac{3+6𝑥+𝑥(1−𝑦)}{𝑥(𝑥+𝑦)} \\ & =\frac{3+6𝑥+𝑥−𝑥𝑦}{𝑥(𝑥+𝑦)} \\ & =\frac{3+7𝑥−𝑥𝑦}{𝑥(𝑥+𝑦)}\end{aligned}


$$

### Example: Adding Rational Expressions by Factoring Binomials

#### Question

Simplify the following expression:

$$


\dfrac{5-q}{3p+4q}-\dfrac{6p+8pq}{18p^2+24pq}


$$

#### Explanation

Notice that we can factor the polynomial in the second denominator as

$$


18p^2+24pq = 6p(3p+4q).


$$

With that in mind, we can rewrite our expression as follows:

$$


\dfrac{5-q}{3p+4q}-\dfrac{6p+8pq}{18p^2+24pq} = \dfrac{5-q}{3p+4q}-\dfrac{6p+8pq}{6p(3p+4q)}


$$

Now, we can put each rational expression over a common denominator by multiplying the numerator and denominator of the first fraction by $6p,$ as follows:

$$


\begin{aligned}\frac{5−𝑞}{3𝑝+4𝑞}−\frac{6𝑝+8𝑝𝑞}{6𝑝(3𝑝+4𝑞)} & =\frac{6𝑝}{6𝑝}⋅\frac{5−𝑞}{3𝑝+4𝑞}−\frac{6𝑝+8𝑝𝑞}{6𝑝(3𝑝+4𝑞)} \\ & =\frac{6𝑝(5−𝑞)}{6𝑝(3𝑝+4𝑞)}−\frac{6𝑝+8𝑝𝑞}{6𝑝(3𝑝+4𝑞)}\end{aligned}


$$

Finally, we subtract the rational expressions:

$$


\begin{aligned}\frac{6𝑝(5−𝑞)}{6𝑝(3𝑝+4𝑞)}−\frac{6𝑝+8𝑝𝑞}{6𝑝(3𝑝+4𝑞)} & =\frac{6𝑝(5−𝑞)−(6𝑝+8𝑝𝑞)}{6𝑝(3𝑝+4𝑞)} \\ & =\frac{30𝑝−6𝑝𝑞−6𝑝−8𝑝𝑞}{6𝑝(3𝑝+4𝑞)} \\ & =\frac{24𝑝−14𝑝𝑞}{6𝑝(3𝑝+4𝑞)} \\ & =\frac{2𝑝(12−7𝑞)}{6𝑝(3𝑝+4𝑞)} \\ & =\frac{12−7𝑞}{3(3𝑝+4𝑞)}\end{aligned}


$$

### Example: Adding Rational Expressions by Factoring Trinomials

#### Question

Simplify the following expression:

$$


\dfrac{5}{2x^2-11x+5}+\dfrac{7x}{x-5}


$$

#### Explanation

First, we factor the denominator in the first term, $2x^2-11x+5.$

To factor this quadratic expression, we need to find two numbers that multiply to $2\cdot 5=10$ and add to $-11.$ These are $-10$ and $-1{:}$

$$


\begin{aligned}2𝑥^{2}−11𝑥+5 & =2𝑥^{2}\underset{−11𝑥}{\underset{}{−10𝑥−𝑥}}+5 \\ & =(2𝑥^{2}−10𝑥)+(−𝑥+5) \\ & =2𝑥(𝑥−5)−1(𝑥−5) \\ & =(𝑥−5)(2𝑥−1)\end{aligned}


$$

With that in mind, we can rewrite our expression as follows:

$$


\dfrac{5}{2x^2-11x+5}+\dfrac{7x}{x-5} = \dfrac{5}{(x-5)(2x-1)}+\dfrac{7x}{x-5}


$$

Now, we can put each rational expression over a common denominator by multiplying the numerator and denominator of the second fraction by $(2x-1),$ as follows:

$$


\begin{aligned}\frac{5}{(𝑥−5)(2𝑥−1)}+\frac{7𝑥}{𝑥−5} & =\frac{5}{(𝑥−5)(2𝑥−1)}+\frac{2𝑥−1}{2𝑥−1}⋅\frac{7𝑥}{𝑥−5} \\ & =\frac{5}{(𝑥−5)(2𝑥−1)}+\frac{7𝑥(2𝑥−1)}{(𝑥−5)(2𝑥−1)}\end{aligned}


$$

Finally, we add the rational expressions:

$$


\begin{aligned}\frac{5}{(𝑥−5)(2𝑥−1)}+\frac{7𝑥(2𝑥−1)}{(𝑥−5)(2𝑥−1)} & =\frac{5+7𝑥(2𝑥−1)}{(𝑥−5)(2𝑥−1)} \\ & =\frac{5+14𝑥^{2}−7𝑥}{(𝑥−5)(2𝑥−1)} \\ & =\frac{14𝑥^{2}−7𝑥+5}{(𝑥−5)(2𝑥−1)}\end{aligned}


$$

### Factoring Rational Expressions Using a Sign Change

We sometimes encounter situations where common factors in the denominator are somewhat obscured. A common example is when one factor differs from another by sign only. Here, we'll learn how to deal with this kind of problem.

For example, consider the following subtraction problem:

$$


\dfrac{5}{\color{blue}1-x}-\dfrac{2}{x^2-x}


$$

We start by factoring the polynomial in the second denominator, which yields

$$


\dfrac{5}{\color{blue}1-x}-\dfrac{2}{x(x-1)}.


$$

Note the following:

- The denominator of the first term is ${\color{blue}{1-x}}.$

- The second factor in the denominator of the second term is $x - 1,$ which differs from the denominator of the first term by a factor of $({\color{red}{-1}}){:}$

$$


x-1 = ({\color{red}{-1}})({\color{blue}1-x})


$$

We can simplify our subtraction problem by introducing a negative sign in the denominator of the second term, as follows:

$$


\begin{aligned}\frac{5}{1−𝑥}−\frac{2}{𝑥(𝑥−1)} & =\frac{5}{1−𝑥}−\frac{2}{𝑥(−1)(1−𝑥)} \\ & =\frac{5}{1−𝑥}−\frac{2}{−𝑥(1−𝑥)}\end{aligned}


$$

To get rid of the minus sign in the second denominator, we multiply the numerator and denominator of the second fraction by $-1,$ as shown below:

$$


\begin{aligned}\frac{5}{1−𝑥}−\frac{2}{−𝑥(1−𝑥)} & =\frac{5}{1−𝑥}−\frac{(−1)⋅2}{(−\,1)⋅(−\,𝑥(1−𝑥))} \\ & =\frac{5}{1−𝑥}−(−1)⋅\frac{2}{𝑥(1−𝑥)} \\ & =\frac{5}{1−𝑥}+\frac{2}{𝑥(1−𝑥)}\end{aligned}


$$

This shows that we can pull out the minus sign from the denominator (or numerator) of a fraction and write it before the fraction. Notice that this has turned our subtraction problem into one involving addition.

Now, we can put each rational expression over a common denominator by multiplying the numerator and denominator of the first fraction by $x,$ as follows:

$$


\begin{aligned}\frac{5}{1−𝑥}+\frac{2}{𝑥(1−𝑥)} & =\frac{𝑥}{𝑥}⋅\frac{5}{1−𝑥}+\frac{2}{𝑥(1−𝑥)} \\ & =\frac{5𝑥}{𝑥(1−𝑥)}+\frac{2}{𝑥(1−𝑥)}\end{aligned}


$$

Finally, we combine the rational expressions:

$$


\begin{aligned}\frac{5𝑥}{𝑥(1−𝑥)}+\frac{2}{𝑥(1−𝑥)} & =\frac{5𝑥+2}{𝑥(1−𝑥)}\end{aligned}


$$

### Example: Simplifying Rational Expressions by Factoring Binomials and Changing Signs

#### Question

Simplify the following expression:

$$


\dfrac{2y-5}{4-x}-\dfrac{3}{x^2-4x}


$$

#### Explanation

Notice that we can factor the polynomial in the second denominator as

$$


\begin{aligned}𝑥^{2}−4𝑥 & =𝑥(𝑥−4) \\ & =−𝑥(4−𝑥).\end{aligned}


$$

With that in mind, we can rewrite our expression as follows:

$$


\begin{aligned}\frac{2𝑦−5}{4−𝑥}−\frac{3}{𝑥^{2}−4𝑥} & =\frac{2𝑦−5}{4−𝑥}−\frac{3}{−𝑥(4−𝑥)} \\ & =\frac{2𝑦−5}{4−𝑥}+\frac{3}{𝑥(4−𝑥)}\end{aligned}


$$

Now, we can put each rational expression over a common denominator by multiplying the numerator and denominator of the first fraction by $x,$ as follows:

$$


\begin{aligned}\frac{2𝑦−5}{4−𝑥}+\frac{3}{𝑥(4−𝑥)} & =\frac{𝑥}{𝑥}⋅\frac{2𝑦−5}{4−𝑥}+\frac{3}{𝑥(4−𝑥)} \\ & =\frac{𝑥(2𝑦−5)}{𝑥(4−𝑥)}+\frac{3}{𝑥(4−𝑥)}\end{aligned}


$$

Finally, we combine the rational expressions:

$$


\begin{aligned}\frac{𝑥(2𝑦−5)}{𝑥(4−𝑥)}+\frac{3}{𝑥(4−𝑥)} & =\frac{𝑥(2𝑦−5)+3}{𝑥(4−𝑥)} \\ & =\frac{2𝑥𝑦−5𝑥+3}{𝑥(4−𝑥)}\end{aligned}


$$
