# Integrating Algebraic Functions Using Substitution

Source: https://www.mathacademy.com/topics/334?courseId=21
Topic ID: 334

## Prerequisites

- [The Chain Rule for Differentiation](../ap-calculus-ab/1108-the-chain-rule-for-differentiation.md)
- [The Sum Rule for Indefinite Integrals](../ap-calculus-ab/3769-the-sum-rule-for-indefinite-integrals.md)

## Lesson

### Introduction

We know how to calculate $\displaystyle\int x^5 \, \textrm{d}x.$ But suppose that we want to calculate an integral like

$$


\int (2x+1)^5 \, \textrm{d}x.


$$

The integral above is different from what we've seen previously because now it's a whole function $(2x+1)$ that is being raised to the power of $5.$ So what do we do?

In this case, the answer is to introduce a new variable. Our goal is to replace all of the $x$'s in the integral, *including* the $\textrm d x$, with this new variable which we'll call $u.$

First, we let $u=2x+1.$ Differentiating both sides with respect to $x$ gives

$$


\dfrac{\textrm{d}u}{\textrm{d}x} = 2,


$$

and if we treat $\dfrac{\textrm d u}{\textrm d x}$ like a fraction, we can get the $\textrm d x$ on its own as

$$


\textrm{d} x = \dfrac 1 2 \textrm d u.


$$

We're now in a position to write our integral in terms of the new variable $u,$ which we do as follows:

$$


\begin{aligned}∫(2𝑥+1)^{5}\,d𝑥 & =∫𝑢^{5}⋅\frac{1}{2}d𝑢 \\ & =\frac{1}{2}∫𝑢^{5}d𝑢.\end{aligned}


$$

We now calculate our integral as normal, and write the final answer in terms of $x$ at the very end:

$$


\begin{aligned}\frac{1}{2}∫𝑢^{5}d𝑢 & =\frac{1}{2}⋅\frac{𝑢^{6}}{6}+𝐶 \\ & =\frac{1}{12}𝑢^{6}+𝐶 \\ & =\frac{1}{12}(2𝑥+1)^{6}+𝐶.\end{aligned}


$$

**Note:** After solving an integral using substitution, we should always double-check that our result is correct. If we differentiate the result, then it should come out to the original integrand:

$$


\begin{aligned}\frac{d}{d𝑥}[\frac{1}{12}(2𝑥+1)^{6}+𝐶] & =\frac{1}{12}⋅\frac{d}{d𝑥}[(2𝑥+1)^{6}]+\frac{d}{d𝑥}(𝐶) \\ & =\frac{1}{12}⋅6(2𝑥+1)^{5}⋅\frac{d}{d𝑥}(2𝑥+1)+0 \\ & =\frac{1}{2}(2𝑥+1)^{5}⋅2 \\ & =(2𝑥+1)^{5}\,✓\end{aligned}


$$

### Example: Integrating an Algebraic Function With Positive Integer Exponent

#### Question

Calculate $\displaystyle\int (3x+1)^3 \, \textrm{d}x.$

#### Explanation

Let $u=3x+1.$ Then differentiating with respect to $x$ gives

$$


\dfrac{\textrm d u}{\textrm d x} = 3\quad\Longrightarrow\quad \textrm d x = \dfrac 1 3 \textrm d u.


$$

We now write our integral in terms of $u,$ calculate the integral as normal, and write the final answer in terms of $x$ at the very end:

$$


\begin{aligned}∫(3𝑥+1)^{3}\,d𝑥 & =∫𝑢^{3}⋅\frac{1}{3}d𝑢 \\ & =\frac{1}{3}∫𝑢^{3}d𝑢 \\ & =\frac{1}{3}⋅\frac{𝑢^{4}}{4}+𝐶 \\ & =\frac{1}{12}𝑢^{4}+𝐶 \\ & =\frac{1}{12}(3𝑥+1)^{4}+𝐶\end{aligned}


$$

Let's double-check that our result is correct. If we differentiate the result, then it should come out to the original integrand:

$$


\begin{aligned}\frac{d}{d𝑥}[\frac{1}{12}(3𝑥+1)^{4}+𝐶] & =\frac{1}{12}⋅\frac{d}{d𝑥}[(3𝑥+1)^{4}]+\frac{d}{d𝑥}(𝐶) \\ & =\frac{1}{12}⋅4(3𝑥+1)^{3}⋅\frac{d}{d𝑥}(3𝑥+1)+0 \\ & =\frac{1}{3}(3𝑥+1)^{3}⋅3 \\ & =(3𝑥+1)^{3}\,✓\end{aligned}


$$

### Example: Integrating an Algebraic Function With Negative Integer Exponent

#### Question

Calculate $\displaystyle\int \dfrac{2}{(1-x)^3} \, \textrm{d}x.$

#### Explanation

First, we rewrite the integral as

$$


\displaystyle\int 2(1-x)^{-3} \, \textrm{d}x .


$$

Let $u=1-x.$ Then differentiating with respect to $x$ gives

$$


\dfrac{\textrm d u}{\textrm d x} = -1\quad\Longrightarrow\quad \textrm d x = -\textrm d u.


$$

We now write our integral in terms of $u,$ calculate the integral as normal, and write the final answer in terms of $x$ at the very end:

$$


\begin{aligned}∫2(1−𝑥)^{−3}\,d𝑥 & =∫2𝑢^{−3}⋅(−1)d𝑢 \\ & =−2∫𝑢^{−3}d𝑢 \\ & =−2⋅\frac{𝑢^{−2}}{−2}+𝐶 \\ & =𝑢^{−2}+𝐶 \\ & =(1−𝑥)^{−2}+𝐶 \\ & =\frac{1}{(1−𝑥)^{2}}+𝐶.\end{aligned}


$$

Let's double-check that our result is correct. If we differentiate the result, then it should come out to the original integrand:

$$


\begin{aligned}\frac{d}{d𝑥}[\frac{1}{(1−𝑥)^{2}}+𝐶] & =\frac{d}{d𝑥}[\frac{1}{(1−𝑥)^{2}}]+\frac{d}{d𝑥}(𝐶) \\ & =\frac{d}{d𝑥}[(1−𝑥)^{−2}]+\frac{d}{d𝑥}(𝐶) \\ & =−2(1−𝑥)^{−3}⋅\frac{d}{d𝑥}(1−𝑥)+0 \\ & =−\frac{2}{(1−𝑥)^{3}}⋅(−1) \\ & =\frac{2}{(1−𝑥)^{3}}\,✓\end{aligned}


$$

### Example: Integrating an Algebraic Function With Fractional Exponent

#### Question

Calculate $\displaystyle\int\sqrt{1-5x}\,\textrm d x.$

#### Explanation

First, we rewrite the integral as

$$


\displaystyle\int(1-5x)^{1/2}\,\textrm d x.


$$

Now, we let $u=1-5x.$ Then differentiating with respect to $x$ gives

$$


\dfrac{\textrm d u}{\textrm d x} = -5\quad\Longrightarrow\quad \textrm d x = -\dfrac 1 5 \textrm d u.


$$

We now write our integral in terms of $u,$ calculate the integral as normal, and write the final answer in terms of $x$ at the very end:

$$


\begin{aligned}∫(1−5𝑥)^{1/2}\,d𝑥 & =∫𝑢^{1/2}⋅(−\frac{1}{5})\,d𝑢 \\ & =−\frac{1}{5}∫𝑢^{1/2}\,d𝑢 \\ & =−\frac{1}{5}⋅\frac{2}{3}𝑢^{3/2}+𝐶 \\ & =−\frac{2}{15}𝑢^{3/2}+𝐶 \\ & =−\frac{2}{15}(1−5𝑥)^{3/2}+𝐶 \\ & =−\frac{2}{15}\sqrt{√(1−5𝑥)^{3}}+𝐶\end{aligned}


$$

Let's double-check that our result is correct. If we differentiate the result, then it should come out to the original integrand:

$$


\begin{aligned}\frac{d}{d𝑥}[−\frac{2}{15}\sqrt{√(1−5𝑥)^{3}}+𝐶] & =−\frac{2}{15}⋅\frac{d}{d𝑥}[\sqrt{√(1−5𝑥)^{3}}]+\frac{d}{d𝑥}(𝐶) \\ & =−\frac{2}{15}⋅\frac{d}{d𝑥}[(1−5𝑥)^{3/2}]+\frac{d}{d𝑥}(𝐶) \\ & =−\frac{2}{15}⋅\frac{3}{2}(1−5𝑥)^{1/2}⋅\frac{d}{d𝑥}(1−5𝑥)+0 \\ & =−\frac{1}{5}(1−5𝑥)^{1/2}⋅(−5) \\ & =(1−5𝑥)^{1/2}\,✓\end{aligned}


$$

### The General Formula

By using the substitution $u=ax+b$, it's straightforward to show that

$$


\int (ax+b)^n\,\textrm d x = \dfrac{1}{a(n+1)}(ax+b)^{n+1} + C, \qquad n\neq -1.


$$

If you can remember the formula, great! You'll save yourself some time. If you don't like memorizing formulas, you can always solve these integrals using the substitution method described in this lesson.
