# Dividing Polynomials Using Synthetic Division

Source: https://www.mathacademy.com/topics/728?courseId=134
Topic ID: 728

## Prerequisites

- [Multiplying Polynomials](../algebra-i/361-multiplying-polynomials.md)
- [Multiplying Rational Expressions](../algebra-ii/435-multiplying-rational-expressions.md)

## Lesson

### Introduction

Suppose that we want to divide two polynomials, such as

$$


\dfrac{2x^3-5x^2-7x+11}{x-3}.


$$

First, let's get familiar with some terminology:

- The **dividend** is the polynomial that we want to divide, so $2x^3-5x^2-7x+11$ in this case.

- The **divisor** is the polynomial that we want to divide the dividend by, so $x-3$ in this case.

- The result of the division, which will be a polynomial, is called the **quotient**.

- The **remainder** is what is left after the division.

Before we start, we need to check that the polynomials are written in standard form. In our case, the terms in both the numerator and denominator are in descending order of their degree, so we're ready to go!

### Dividing a Polynomial Using Synthetic Division

Our goal is to find the quotient and remainder of the following division problem.

$$


\dfrac{2x^3-5x^2-7x+11}{x-3}


$$

To do this, we can use **synthetic division**. Synthetic division allows us to divide a polynomial by a factor of the form $(x-c).$ Here's how we do it.

The numbers $2,$ $1$ and $-4$ in the bottom row are the coefficients of the **quotient**. So from left to right, the quotient is

$$


2x^2+1x-4.


$$

The **remainder** is the value in the box, so ${\color{blue}-1}$ in this case.

Finally, we can write the full result of the division as

$$


\dfrac{2x^3-5x^2-7x+11}{x-3}=2x^2+x-4+\dfrac{\color{blue}-1}{x-3} ,


$$

which simplifies to

$$


\dfrac{2x^3-5x^2-7x+11}{x-3}=2x^2+x-4-\dfrac{1}{x-3}.


$$

### Checking the Division

Dividing $2x^3-5x^2-7x+11$ by $x-3,$ we obtained that

$$


\dfrac{2x^3-5x^2-7x+11}{x-3}=2x^2+x-4-\dfrac{1}{x-3}.


$$

Now, multiplying both sides by $x-3,$ we get

$$


{\color{blue}2x^3-5x^2-7x+11}=(x-3)(2x^2+x-4)-1.


$$

Therefore, to check if we have done the division correctly, we can simply multiply the polynomials on the right-hand side and simplify:

$$


\begin{aligned}(𝑥−3)(2𝑥^{2}+𝑥−4)−1 & =𝑥(2𝑥^{2}+𝑥−4)−3(2𝑥^{2}+𝑥−4)−1 \\ & =2𝑥^{3}+𝑥^{2}−4𝑥−6𝑥^{2}−3𝑥+12−1 \\ & =2𝑥^{3}−5𝑥^{2}−7𝑥+11\,✓\end{aligned}


$$

### Example: Dividing a Polynomial by a Linear Binomial Using Synthetic Division

#### Question

Use synthetic division to divide $5x^4+x^3+6x+2$ by $x+1.$

#### Explanation

Notice that the dividend is missing an $x^2$ term, so we insert a $0x^2$ in its place and carry out the process in the same way.

$$


\begin{aligned}−1 & 5 & 1 & 0 & 6 & 2 \\ & & −5 & 4 & −4 & −2 \\ & 5 & −4 & 4 & 2 & 0\end{aligned}


$$

Since the remainder is $0,$ it means that $x+1$ divides $5x^4+x^3+6x+2$ exactly and gives a quotient of $5x^3-4x^2+4x+2.$

So, we have

$$


\dfrac{5x^4+x^3+6x+2}{x+1} = 5x^3-4x^2+4x+2 .


$$

### Dividing By a General Linear Factor

We have already seen how synthetic division can be used to quickly divide a polynomial by a linear binomial with a leading coefficient of $1.$

In fact, synthetic division can be used when the divisor is *any* linear binomial, like $(ax+b).$ We just factor out the leading coefficient $a,$ carry out the division in the standard way, and then include the leading coefficient in the final result.

Let's see an example.

### Example: Dividing a Polynomial by a Linear Binomial With Leading Coefficients

#### Question

Find the quotient and remainder of $\dfrac{3x^4+7x^3-10x+8}{2-3x}.$

#### Explanation

First, we write the divisor in standard form as $-3x+2.$ Then, we factor out the leading coefficient. This gives

$$


\begin{aligned}\frac{3𝑥^{4}+7𝑥^{3}−10𝑥+8}{−3𝑥+2} & =\frac{3𝑥^{4}+7𝑥^{3}−10𝑥+8}{−3(𝑥−\frac{2}{3})} \\ & =−\frac{1}{3}(\frac{3𝑥^{4}+7𝑥^{3}−10𝑥+8}{(𝑥−\frac{2}{3})}).\end{aligned}


$$

Carrying out the synthetic division process on $\dfrac{3x^4+7x^3-10x+8}{\left(x-\frac23\right)},$ remembering to include a coefficient of zero for the $x^2$ term, we arrive at the following:

$$


\begin{aligned}\frac{2}{3} & 3 & 7 & 0 & −10 & 8 \\ & & 2 & 6 & 4 & −4 \\ & 3 & 9 & 6 & −6 & 4\end{aligned}


$$

Reading off the bottom row, we get

$$


\frac{3x^4+7x^3-10x+8}{\left(x-\frac23\right)} = 3x^3+9x^2+6x-6+\frac{4}{\left(x-\frac23\right)}.


$$

Finally, we multiply by the original $-\dfrac 1 3$ factor to get

$$


\begin{aligned}\frac{3𝑥^{4}+7𝑥^{3}−10𝑥+8}{2−3𝑥} & =−\frac{1}{3}(3𝑥^{3}+9𝑥^{2}+6𝑥−6+\frac{4}{(𝑥−\frac{2}{3})}) \\ & =−𝑥^{3}−3𝑥^{2}−2𝑥+2+\frac{4}{2−3𝑥}.\end{aligned}


$$
