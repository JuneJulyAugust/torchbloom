# The Generalized Binomial Theorem

Source: https://www.mathacademy.com/topics/1189?courseId=109
Topic ID: 1189

## Prerequisites

- [Convergent and Divergent Infinite Series](./982-convergent-and-divergent-infinite-series.md)
- [The Special Case of the Binomial Theorem](../../../high-school/integrated-math-honors/lessons/integrated-math-ii-honors/3764-the-special-case-of-the-binomial-theorem.md)

## Lesson

### Introduction

Suppose we have the following binomial, where $n$ is a positive integer.

$$



(1+x)^n



$$

We can use the binomial theorem to expand this binomial into a finite series containing ascending powers of $x$ as follows:

$$



\begin{aligned}(1+𝑥)^{𝑛} & =1+𝑛𝑥+(\frac{𝑛}{2})𝑥^{2}+(\frac{𝑛}{3})𝑥^{3}+⋯+𝑥^{𝑛}\end{aligned}



$$

We derived this result in a previous lesson. This series is finite whenever $n$ is a positive integer.

However, suppose we want to expand $(1+x)^n$ where $n$ is some other rational number (i.e., not a positive integer)? In such cases, we can apply the **generalized binomial theorem**, which states that

$$



(1+x)^n = 1 + nx + \dfrac{n(n-1)}{2!}x^2 + \dfrac{n(n-1)(n-2)}{3!}x^3 + \cdots.



$$

In general, this is an *infinite series*. The series is *convergent* for $|x| < 1$ and *divergent* for $|x| \geq 1.$

More generally, if $a$ is a real number, then we can expand the binomial $(1+ax)^n$ similarly as follows:

$$



(1+ax)^n = 1 + nax + \dfrac{n(n-1)}{2!}(ax)^2 + \dfrac{n(n-1)(n-2)}{3!}(ax)^3 + \cdots



$$

which is convergent whenever $|ax| < 1,$ which we usually write as $|x| < \dfrac{1}{|a|}.$

Let's use this to find the first few terms of the binomial expansion of

$$



\dfrac{1}{(1+x)^2}.



$$

Applying the generalized binomial formula with $n=-2,$ we obtain

$$



\begin{aligned}\frac{1}{(1+𝑥)^{2}} & =(1+𝑥)^{−2} \\ & =1+(−2)𝑥+\frac{(−2)(−2−1)𝑥^{2}}{2!}+\frac{(−2)(−2−1)(−2−2)𝑥^{3}}{3!}+⋯ \\ & =1−2𝑥+\frac{(−2)(−3)𝑥^{2}}{2}+\frac{(−2)(−3)(−4)𝑥^{3}}{6}+⋯ \\ & =1−2𝑥+\frac{6⋅𝑥^{2}}{2}−\frac{24⋅𝑥^{3}}{6}+⋯ \\ & =1−2𝑥+3𝑥^{2}−4𝑥^{3}+⋯.\end{aligned}



$$

Finally, the generalized binomial theorem also works when $n$ *is* a positive integer. In this case, all terms after the $(n+1)$th term equal zero. In this case, we can relax the condition $|x| < 1.$

### Example: Finding the Binomial Expansion of a Reciprocal Expression

#### Question

Given that $|x| < \dfrac{1}{3},$ find the first three terms in the binomial expansion of $\dfrac{1}{1 + 3x}.$

#### Explanation

The generalized binomial formula states that

$$



(1+x)^n = 1 + nx + \dfrac{n(n-1)x^2}{2!} + \dfrac{n(n-1)(n-2)x^3}{3!}+\cdots.



$$

We rewrite the given expression as

$$



\dfrac{1}{1 + 3x} = (1+3x)^{-1}.



$$

Now, applying the generalized binomial formula with $n=-1$ and $3x$ instead of $x,$ we obtain

$$



\begin{aligned}\frac{1}{1+3𝑥} & =(1+3𝑥)^{−1} \\ & =1+(−1)(3𝑥)+\frac{(−1)(−1−1)(3𝑥)^{2}}{2!}+⋯ \\ & =1−3𝑥+\frac{(−1)(−2)(9𝑥^{2})}{2}+⋯ \\ & =1−3𝑥+9𝑥^{2}+⋯.\end{aligned}



$$

### Example: Finding the Binomial Expansion of a Reciprocal Expression Raised to a Power

#### Question

Given that $|x| < \dfrac{1}{2},$ find the first three terms in the binomial expansion of $\dfrac{5}{(1+2x)^2}.$

#### Explanation

The generalized binomial formula states that

$$



(1+x)^n = 1 + nx + \dfrac{n(n-1)x^2}{2!} + \dfrac{n(n-1)(n-2)x^3}{3!}+\cdots.



$$

We rewrite the given expression as

$$



\dfrac{5}{(1+2x)^2} = 5(1+2x)^{-2}.



$$

Now, applying the generalized binomial formula with $n=-2$ and $2x$ instead of $x,$ we obtain

$$



\begin{aligned} \dfrac{5}{(1+2x)^2} & = 5\left[ 1+(-2)(2x)+\dfrac{(-2)(-2-1)(2x)^2}{2!} + \cdots \right] \\\[5pt] & = 5\left[ 1 - 4x +\dfrac{(-2)(-3)(4)x^2}{2} + \cdots \right] \\\[5pt] & = 5\left[ 1 - 4x + 12x^2 + \cdots \right] \\\[5pt] & = 5 - 20x + 60x^2 + \cdots . \end{aligned}



$$

### Example: Finding the Binomial Expansion of a Radical Expression

#### Question

Find the binomial expansion of $\dfrac{1}{\sqrt{1+4x}}$ up to the third term. Assume that $|x|<\dfrac{1}{4}.$

#### Explanation

The generalized binomial formula states that

$$



(1+x)^n = 1 + nx + \dfrac{n(n-1)x^2}{2!} + \dfrac{n(n-1)(n-2)x^3}{3!}+\cdots.



$$

We rewrite the given expression as

$$



\dfrac{1}{\sqrt{1+4x}} =(1+4x)^{-1/2}



$$

Now, applying the generalized binomial formula with $n=-\dfrac12$ and $4x$ instead of $x,$ we obtain

$$



\begin{aligned} \dfrac{1}{\sqrt{1+4x}} & = 1+\left(-\dfrac{1}{2}\right)(4x)+\dfrac{\left(-\dfrac{1}{2}\right)\left(-\dfrac{1}{2}-1\right)(4x)^2}{2!} + \cdots \\\[5pt] & = 1 - 2x +\dfrac{\left(-\dfrac{1}{2}\right)\left(-\dfrac{3}{2}\right)16x^2}{2} + \cdots \\\[5pt] & = 1 - 2x + 6x^2 + \cdots . \end{aligned}



$$
