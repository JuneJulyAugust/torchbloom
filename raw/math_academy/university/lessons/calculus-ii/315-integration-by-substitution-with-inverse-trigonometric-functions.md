# Integration by Substitution With Inverse Trigonometric Functions

Source: https://www.mathacademy.com/topics/315?courseId=106
Topic ID: 315

## Prerequisites

- [Evaluating Expressions Containing Inverse Trigonometric Functions](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/209-evaluating-expressions-containing-inverse-trigonometric-functions.md)
- [Calculating Definite Integrals Using Substitution](./1159-calculating-definite-integrals-using-substitution.md)

## Lesson

### Introduction

Consider the integral

$$


\int \dfrac{1}{\sqrt{1-4x^2}} \, \text{d}x.


$$

This integral, apart from the coefficient of $4$ in the denominator, resembles the basic integral

$$


\int \frac{1}{\sqrt{1-u^2}}\text{d}u = \arcsin(u)+C.


$$

In fact, they look almost the same, but instead of $u^2$ as the variable, we have $4x^2 = (2x)^2.$

So, let's substitute $u=2x.$ Differentiating, we get

$$


\dfrac{\text{d}u}{\text{d}x}=2\quad\Longrightarrow\quad \dfrac 1 2 \textrm d u = \textrm d x.


$$

We can now write the integral in terms of $u,$ and evaluate:

$$


\begin{aligned}∫\frac{1}{\sqrt{1−4𝑥^{2}}}\,d𝑥 & =∫\frac{1}{\sqrt{1−(2𝑥)^{2}}}\,d𝑥 \\ & =∫\frac{1}{\sqrt{1−𝑢^{2}}}⋅\frac{1}{2}\,d𝑢 \\ & =\frac{1}{2}∫\frac{1}{\sqrt{1−𝑢^{2}}}\,d𝑢 \\ & =\frac{1}{2}arcsin⁡(𝑢)+𝐶 \\ & =\frac{1}{2}arcsin⁡(2𝑥)+𝐶.\end{aligned}


$$

We can often use this trick whenever we see an integral that closely resembles an integral for an inverse trigonometric function.

**Note:** As always, after solving an integral using substitution, we should always double-check that our result is correct. If we differentiate the result, then it should come out to the original integrand:

$$


\begin{aligned}\frac{d}{d𝑥}[\frac{1}{2}arcsin⁡(2𝑥)+𝐶] & =\frac{1}{2}⋅\frac{d}{d𝑥}[arcsin⁡(2𝑥)]+\frac{d}{d𝑥}(𝐶) \\ & =\frac{1}{2}⋅\frac{1}{\sqrt{1−(2𝑥)^{2}}}⋅\frac{d}{d𝑥}(2𝑥)+0 \\ & =\frac{1}{2}⋅\frac{1}{\sqrt{1−4𝑥^{2}}}⋅2 \\ & =\frac{1}{\sqrt{1−4𝑥^{2}}}\,✓\end{aligned}


$$

### Example: Calculating Indefinite Integrals Using Substitution with Inverse Sine

#### Question

Calculate the integral $\displaystyle \int \dfrac{9}{4\sqrt{1-9x^2}} \, \text{d}x.$

#### Explanation

This integral resembles the basic integral for inverse sine,

$$


\int \frac{1}{\sqrt{1-u^2}}\text{d}u = \arcsin(u)+C.


$$

The only difference is that instead of $u^2$ as the variable, we have $9x^2 = (3x)^2.$

So, let's substitute $u=3x.$ Differentiating, we get

$$


\dfrac{\text{d}u}{\text{d}x}=3\quad\Longrightarrow\quad \dfrac 1 3 \,\textrm d u=\textrm d x.


$$

We can now write the integral in terms of $u,$ and evaluate:

$$


\begin{aligned}\begin{matrix}∫\frac{9}{4\sqrt{1−9𝑥^{2}}}\,d𝑥 & =\frac{9}{4}∫\frac{1}{\sqrt{1−(3𝑥)^{2}}}\,\,d𝑥 \\ & =\frac{9}{4}∫\frac{1}{\sqrt{1−𝑢^{2}}}⋅\frac{1}{3}d𝑢 \\ & =\frac{9}{12}∫\frac{1}{\sqrt{1−𝑢^{2}}}\,d𝑢 \\ & =\frac{3}{4}⋅arcsin⁡𝑢+𝐶 \\ & =\frac{3}{4}arcsin⁡3𝑥+𝐶\end{matrix}\end{aligned}


$$

### Example: Calculating Indefinite Integrals Using Substitution with Inverse Tangent

#### Question

Calculate the integral $\displaystyle{\int \dfrac{3}{2 + 50x^2} \, \text{d}x}.$

#### Explanation

Note that we can rewrite this integral as

$$


\int \dfrac{3}{2 + 50x^2} \, \text{d}x = \int \dfrac{3}{2(1 + 25x^2)} = \dfrac 3 2 \int \dfrac{1}{1+25x^2}\,\textrm d x.


$$

This integral resembles the basic integral for inverse tangent,

$$


\int \frac{1}{1+u^2}\text{d}u =\arctan u +C.


$$

The only difference is that instead of $u^2$ as the variable, we have $25x^2 = (5x)^2.$

So, let's substitute $u=5x.$ Differentiating, we get

$$


\dfrac{\text{d}u}{\text{d}x}=5\quad\Longrightarrow\quad \dfrac 1 5\,\textrm d u = \textrm d x.


$$

We can now write the integral in terms of $u,$ and evaluate:

$$


\begin{aligned}\begin{matrix}∫\frac{3}{2+50𝑥^{2}}\,d𝑥 & =\frac{3}{2}∫\frac{1}{1+25𝑥^{2}}\,d𝑥 \\ & =\frac{3}{2}∫\frac{1}{1+(5𝑥)^{2}}\,d𝑥 \\ & =\frac{3}{2}∫\frac{1}{1+𝑢^{2}}\,\,⋅\frac{1}{5}\,d𝑢 \\ & =\frac{3}{10}∫\frac{1}{1+𝑢^{2}}\,d𝑢 \\ & =\frac{3}{10}⋅arctan⁡𝑢+𝐶 \\ & =\frac{3}{10}arctan⁡5𝑥+𝐶\end{matrix}\end{aligned}


$$

### Example: Calculating Indefinite Integrals Using Substitution with Inverse Secant

#### Question

${\displaystyle \int \dfrac{5\, \text{d}x}{|5x|\sqrt{(5x)^2-1}} =}$

#### Explanation

This resembles the basic integral for $\text{arcsec},$

$$


\int \frac{1}{|u|\sqrt{u^2-1}} \text{d}u = \text{arcsec}(u)+C.


$$

Let $u = 5x.$ Then

$$


\dfrac{\text{d}u}{\text{d}x}=5 \quad\Longrightarrow\quad 5\,\text{d}x = \text{d}u.


$$

Therefore,

$$


\begin{aligned}\begin{matrix}∫\frac{5\,d𝑥}{|5𝑥|\sqrt{(5𝑥)^{2}−1}} & =∫\frac{d𝑢}{|𝑢|\sqrt{𝑢^{2}−1}} \\ & =arcsec(𝑢)+𝐶 \\ & =arcsec(5𝑥)+𝐶.\end{matrix}\end{aligned}


$$

### Example: Calculating Definite Integrals Using Substitution with Inverse Trigonometric Functions

#### Question

Evaluate the integral $\displaystyle{\int_{0}^{\sqrt 2} \dfrac{1}{2+x^2}\, \text{d}x}.$

#### Explanation

First, we rewrite the integral as

$$


\begin{aligned}∫_{\sqrt{2}0}^{}\frac{1}{2+𝑥^{2}}\,d𝑥 & =∫_{\sqrt{2}0}^{}\frac{1}{2(1+𝑥^{2}/2)}\,d𝑥 \\ & =∫_{\sqrt{2}0}^{}\frac{1}{2(1+(𝑥/\sqrt{2})^{2})}\,d𝑥 \\ & =\frac{1}{2}∫_{\sqrt{2}0}^{}\frac{1}{1+(𝑥/\sqrt{2})^{2}}\,d𝑥.\end{aligned}


$$

We see that this integral now resembles the basic integral for the inverse tangent,

$$


\int\dfrac{1}{1+u^2}\,\textrm d u = \arctan{u} + C.


$$

We make the substitution $u=\dfrac{x}{\sqrt 2}.$ Differentiating, we get

$$


\dfrac{\textrm d u}{\textrm d x} = \dfrac{1}{\sqrt 2}\quad\Longrightarrow\quad \sqrt 2 \,\textrm d u = \textrm d x.


$$

Before substituting, we use the table below to change the limits from $x$ to $u.$

Using the above, we can now write the integral in terms of $u,$ and evaluate:

$$


\begin{aligned}∫_{\sqrt{2}0}^{}\frac{1}{2+𝑥^{2}}\,d𝑥 & =\frac{1}{2}∫_{10}\frac{1}{1+𝑢^{2}}\,⋅\sqrt{2}\,d𝑢 \\ & =\frac{\sqrt{2}}{2}∫_{10}\frac{1}{1+𝑢^{2}}\,d𝑢 \\ & =\frac{\sqrt{2}}{2}arctan⁡𝑢|_{10} \\ & =\frac{\sqrt{2}}{2}(arctan⁡1−arctan⁡0) \\ & =\frac{\sqrt{2}}{2}(\frac{𝜋}{4}−0) \\ & =\frac{𝜋\sqrt{2}}{8}\end{aligned}


$$

### Summary of Key Results

In this lesson, we learned how to use substitution to evaluate integrals that give rise to inverse trigonometric functions.

Although you can always solve these integrals by going through the substitution process, it is convenient to remember the following key results:

$$


\begin{aligned}∫\frac{1}{\sqrt{1−(𝑎𝑥)^{2}}}\,d𝑥 & =\frac{1}{𝑎}arcsin⁡(𝑎𝑥)+𝐶 \\ ∫\frac{1}{\sqrt{𝑎^{2}−𝑥^{2}}}\,d𝑥 & =arcsin⁡(\frac{𝑥}{𝑎})+𝐶 \\ ∫\frac{1}{1+(𝑎𝑥)^{2}}\,d𝑥 & =\frac{1}{𝑎}arctan⁡(𝑎𝑥)+𝐶 \\ ∫\frac{1}{𝑎^{2}+𝑥^{2}}\,d𝑥 & =\frac{1}{𝑎}arctan⁡(\frac{𝑥}{𝑎})+𝐶 \\ ∫\frac{1}{|𝑎𝑥|\sqrt{(𝑎𝑥)^{2}−1}}\,d𝑥 & =\frac{1}{𝑎}arcsec(𝑎𝑥)+𝐶\end{aligned}


$$

To remember the results above, note the following:

- Whenever the integrand has an $ax$ term, the argument of the resulting inverse trigonometric function is $ax.$

- Otherwise, if the $a$ and $x$ are separated, then the argument of the resulting inverse trigonometric function is $\dfrac{x}{a}.$

- All the results are multiplied by $\dfrac{1}{a},$ except for $\arcsin \left(\dfrac{x}{a} \right) + C.$
