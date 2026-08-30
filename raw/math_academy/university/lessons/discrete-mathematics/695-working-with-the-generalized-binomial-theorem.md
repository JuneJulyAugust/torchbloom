# Working With the Generalized Binomial Theorem

Source: https://www.mathacademy.com/topics/695?courseId=109
Topic ID: 695

## Prerequisites

- [The Generalized Binomial Theorem](./1189-the-generalized-binomial-theorem.md)

## Lesson

### Introduction

If $n$ is any rational number, then we can expand the expression $(1+x)^n$ using the generalized binomial theorem:

$$



(1+x)^n = 1 + nx + \dfrac{n(n-1)x^2}{2!} + \dfrac{n(n-1)(n-2)x^3}{3!}+\cdots.



$$

This series is convergent whenever $|x| < 1.$

It's important to note that the constant term in our binomial must equal $1$ for these formulas to apply.

Now, suppose that we want to find a binomial expansion of the following expression:

$$



\sqrt{2+4x}.



$$

First, let's rewrite our expression as

$$



(2+4x)^{1/2}.



$$

Notice that the constant term in this binomial is $2,$ not $1.$ So, to apply the generalized binomial theorem, we must rewrite our expression to make the constant term inside the parentheses equal to $1.$

To do this, we first take out a factor of $2$ and apply the power of product rule:

$$



\begin{aligned} (2+4x)^{1/2} &= (2(1+2x))^{1/2}\\\[5pt] &= 2^{1/2} (1+2x)^{1/2} \end{aligned}



$$

Then, we apply our generalized binomial formula with $n=\dfrac{1}{2}$ and $2x$ instead of $x{:}$

$$



\begin{aligned} 2^{1/2} (1+2x)^{1/2} &= 2^{1/2} \left[1 + {\left(\dfrac{1}{2}\right)}(2x) + \dfrac{{\left(\dfrac{1}{2}\right)}{\left(\dfrac{1}{2}-1\right)}(2x)^2}{2!}+ \cdots \right]\\&= \sqrt{2} \left[1 + x + \dfrac{{\left(\dfrac{1}{2}\right)}{\left(-\dfrac{1}{2}\right)} 4x^2}{2}+ \cdots \right]\\&= \sqrt{2} \left[1 + x - \dfrac{x^2}{2} + \cdots \right]. \end{aligned}



$$

This series converges if $|2x|< 1,$ or equivalently, $|x| < \dfrac{1}{2}.$

### Example: Finding the Binomial Expansion of a Reciprocal Expression

#### Question

What is the binomial expansion of $\dfrac{6}{3-x}$ up to the third term for $|x|< 3?$

#### Explanation

The generalized binomial formula states that

$$



(1+x)^n = 1 + nx + \dfrac{n(n-1)x^2}{2!} + \dfrac{n(n-1)(n-2)x^3}{3!}+\cdots.



$$

Factoring $3$ out of the binomial, we rewrite the given expression as

$$



\begin{aligned}6(3−𝑥)^{−1} & =6(3(1−\frac{1}{3}𝑥))^{−1} \\ & =6(3)^{−1}(1−\frac{1}{3}𝑥)^{−1} \\ & =2(1−\frac{1}{3}𝑥)^{−1}.\end{aligned}



$$

Now, applying the generalized binomial formula with $n=-1$ and $-\dfrac{1}{3}x$ instead of $x,$ we obtain

$$



\begin{aligned}\frac{6}{3−𝑥} & =2(1−\frac{1}{3}𝑥)^{−1} \\ & =21+(−1)(−\frac{1}{3}𝑥)+\frac{(−1)(−1−1)(−\frac{1}{3}𝑥)^{2}}{3}+⋯ \\ & =21+\frac{1}{3}𝑥+\frac{(−1)(−2)(\frac{1}{9})𝑥^{2}}{9}+⋯ \\ & =2[1+\frac{1}{3}𝑥+\frac{1}{9}𝑥^{2}+⋯] \\ & =2+\frac{2}{3}𝑥+\frac{2}{9}𝑥^{2}+⋯.\end{aligned}



$$

### Example: Finding the Binomial Expansion of a Reciprocal Expression Raised to a Power

#### Question

What is the binomial expansion of $\dfrac{9}{(3+x)^3}$ up to the third term for $|x|< 3?$

#### Explanation

The generalized binomial formula states that

$$



(1+x)^n = 1 + nx + \dfrac{n(n-1)x^2}{2!} + \dfrac{n(n-1)(n-2)x^3}{3!}+\cdots.



$$

Factoring $3$ out of the binomial, we rewrite the given expression as

$$



\begin{aligned}\frac{9}{(3+𝑥)^{3}} & =9(3+𝑥)^{−3} \\ & =9(3(1+\frac{1}{3}𝑥))^{−3} \\ & =9(3)^{−3}(1+\frac{1}{3}𝑥)^{−3} \\ & =\frac{1}{3}(1+\frac{1}{3}𝑥)^{−3}.\end{aligned}



$$

Now, applying the generalized binomial formula with $n=-3$ and $\dfrac13x$ instead of $x,$ we obtain

$$



\begin{aligned}\frac{9}{(3+𝑥)^{3}} & =\frac{1}{3}(1+\frac{1}{3}𝑥)^{−3} \\ & =\frac{1}{3}1+(−3)(\frac{1}{3}𝑥)+\frac{(−3)(−3−1)(\frac{1}{3}𝑥)^{2}}{3}+⋯ \\ & =\frac{1}{3}1−𝑥+\frac{(−3)(−4)(\frac{1}{9})𝑥^{2}}{9}+⋯ \\ & =\frac{1}{3}[1−𝑥+\frac{2}{3}𝑥^{2}+⋯] \\ & =\frac{1}{3}−\frac{1}{3}𝑥+\frac{2}{9}𝑥^{2}+…\end{aligned}



$$

### Example: Finding the Binomial Expansion of a Radical Reciprocal Expression

#### Question

What is the binomial expansion of $\dfrac{\sqrt{2}}{\sqrt{2-x}}$ up to the third term for $|x|< 2?$

#### Explanation

The generalized binomial formula states that

$$



(1+x)^n = 1 + nx + \dfrac{n(n-1)x^2}{2!} + \dfrac{n(n-1)(n-2)x^3}{3!}+\cdots.



$$

Factoring $2$ out of the binomial, we rewrite the given expression as

$$



\begin{aligned} \sqrt{2}(2-x)^{-{1}/{2}} & = \sqrt{2}\left(2\left(1-\frac{1}{2}x\right)\right)^{-{1}/{2}} \\\[5pt] & = (2)^{{1}/{2}}(2)^{-{1}/{2}}\left(1-\frac{1}{2}x\right)^{-{1}/{2}} \\\[5pt] & = \left(1-\frac{1}{2}x\right)^{-{1}/{2}}. \end{aligned}



$$

Now, applying the generalized binomial formula with $n=-\dfrac12$ and $-\dfrac12x$ instead of $x,$ we obtain

$$



\begin{aligned} \dfrac{\sqrt{2}}{\sqrt{2-x}} & = \left(1-\dfrac{1}{2}x\right)^{-1/2} \\\[5pt] & = 1+\left(-\dfrac{1}{2}\right)\left(-\dfrac{1}{2}x\right)+\dfrac{\left(-\dfrac{1}{2}\right)\left(-\dfrac{1}{2}-1\right)\left(-\dfrac{1}{2}x\right)^2 }{2!}+ \cdots \\\[5pt] & = 1 + \dfrac{1}{4}x +\dfrac{\left(-\dfrac{1}{2}\right)\left(-\dfrac{3}{2}\right)\left(\dfrac{1}{4}\right)x^2}{2} + \cdots \\\[5pt] & = 1 + \dfrac{1}{4}x + \dfrac{3}{32}x^2+ \cdots . \end{aligned}



$$
