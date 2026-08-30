# Integrating Functions by Completing the Square

Source: https://www.mathacademy.com/topics/444?courseId=106
Topic ID: 444

## Prerequisites

- [Integration by Substitution With Inverse Trigonometric Functions](./315-integration-by-substitution-with-inverse-trigonometric-functions.md)
- [Completing the Square With Leading Coefficients](../../../high-school/traditional/lessons/algebra-i/3824-completing-the-square-with-leading-coefficients.md)

## Lesson

### Introduction

Consider the following integral:

$$


\int \dfrac{1}{x^2+2x+5}\, \text{d}x


$$

This integral doesn't resemble any of the standard integrals we have encountered so far.

However, notice that we can complete the square in the denominator as follows:

$$


\begin{aligned}𝑥^{2}+2𝑥+5 & =𝑥^{2}+2⋅1⋅𝑥+5 \\ & =𝑥^{2}+2⋅1⋅𝑥+(1^{2}−1^{2})+5 \\ & =(𝑥^{2}+2⋅1⋅𝑥+1^{2})−1^{2}+5 \\ & =(𝑥+1)^{2}+4\end{aligned}


$$

If we plug the above into our integral and collect a factor of ${\color{red}{4}}$, we get

$$


\begin{aligned}∫\frac{1}{𝑥^{2}+2𝑥+5}\,d𝑥 & =∫\frac{1}{(𝑥+1)^{2}+4}\,d𝑥 \\ & =∫\frac{1}{4[(𝑥+1)^{2}/4+1]}\,d𝑥 \\ & =\frac{1}{4}∫\frac{1}{(𝑥+1)^{2}/4+1}\,d𝑥 \\ & =\frac{1}{4}∫\frac{1}{1+(𝑥+1)^{2}/4}\,d𝑥 \\ & =\frac{1}{4}∫\frac{1}{1+((𝑥+1)/2)^{2}}\,d𝑥.\end{aligned}


$$

Notice that this now resembles the basic integral for inverse tangent:

$$


\int \dfrac{1}{1+u^2} \, \text{d}u = \arctan u + C


$$

The only difference is that instead of $u$ as the variable, we have $\left(\dfrac{x+1}{2}\right).$

So, let's perform the substitution

$$


u=\dfrac{x+1}{2}.


$$

Differentiating, we get

$$


\dfrac{\text{d}u}{\text{d}x}=\dfrac{1}{2} \quad\Longrightarrow\quad \text{d}x = 2\,\text{d}u.


$$

Finally, we write the integral in terms of $u,$ and evaluate:

$$


\begin{aligned}∫\frac{1}{𝑥^{2}+2𝑥+5}\,d𝑥 & =\frac{1}{4}∫\frac{1}{1+((𝑥+1)/2)^{2}}\,d𝑥 \\ & =\frac{1}{4}∫\frac{1}{1+𝑢^{2}}⋅2\,d𝑢 \\ & =\frac{1}{2}∫\frac{1}{1+𝑢^{2}}\,d𝑢 \\ & =\frac{1}{2}arctan⁡𝑢+𝐶 \\ & =\frac{1}{2}arctan⁡(\frac{𝑥+1}{2})+𝐶\end{aligned}


$$

And we're done!

### Example: Calculating Inverse Trigonometric Function Integrals Using Substitution

#### Question

Calculate $\displaystyle \int \dfrac{1}{\sqrt{36 -(3x - 2)^2}} \, \text{d}x.$

#### Explanation

Let's rewrite our integral as follows:

$$


\begin{aligned}∫\frac{1}{\sqrt{36−(3𝑥−2)^{2}}}\,d𝑥 & =∫\frac{1}{\sqrt{36(1−(3𝑥−2)^{2}/36)}}\,d𝑥 \\ & =∫\frac{1}{\sqrt{36}⋅\sqrt{1−(3𝑥−2)^{2}/36}}\,d𝑥 \\ & =∫\frac{1}{6\sqrt{1−(3𝑥−2)^{2}/36}}\,d𝑥 \\ & =\frac{1}{6}∫\frac{1}{\sqrt{1−(3𝑥−2)^{2}/36}}\,d𝑥 \\ & =\frac{1}{6}∫\frac{1}{\sqrt{1−((3𝑥−2)/6)^{2}}}\,d𝑥\end{aligned}


$$

This resembles the basic integral for inverse sine:

$$


\int \dfrac{1}{\sqrt{1-u^2}}\,\text{d}u = \arcsin u + C


$$

The only difference is that instead of $u$ as the variable, we have $\left(\dfrac{3x-2}{6}\right).$

So, let's perform the substitution

$$


u=\dfrac{3x-2}{6}.


$$

Differentiating, we get

$$


\dfrac{\text{d}u}{\text{d}x} = \dfrac{1}{2} \quad \Longrightarrow \quad \text{d}x = 2\,\text{d}u.


$$

Finally, we write the integral in terms of $u,$ and evaluate:

$$


\begin{aligned}∫\frac{1}{\sqrt{36−(3𝑥−2)^{2}}}\,d𝑥 & =\frac{1}{6}∫\frac{1}{\sqrt{1−((3𝑥−2)/6)^{2}}}\,d𝑥 \\ & =\frac{1}{6}∫\frac{1}{\sqrt{1−𝑢^{2}}}⋅2\,d𝑢 \\ & =\frac{1}{3}arcsin⁡𝑢+𝐶 \\ & =\frac{1}{3}arcsin⁡(\frac{3𝑥−2}{6})+𝐶\end{aligned}


$$

### Example: Computing an Arctangent Integral by Completing the Square

#### Question

Calculate $\displaystyle \int \dfrac{1}{x^2-2x + 3}\, \text{d}x.$

#### Explanation

First, we complete the square in the denominator:

$$


\begin{aligned} x^2-2x + 3 & = x^2 - 2 \cdot x+ (1^2 - 1^2) + 3 \\[3pt] & = (x^2 - 2 \cdot x+ 1^2) - 1 + 3 \\[3pt] & = (x-1)^2+2 \end{aligned}


$$

Substituting the above into the denominator, we get

$$


\begin{aligned}∫\frac{1}{𝑥^{2}−2𝑥+3}\,d𝑥 & =∫\frac{1}{(𝑥−1)^{2}+2}\,d𝑥 \\ & =\frac{1}{2}∫\frac{1}{1+((𝑥−1)/\sqrt{2})^{2}}\,d𝑥.\end{aligned}


$$

This resembles the basic integral for inverse tangent:

$$


\int \dfrac{1}{1+u^2} \, \text{d}u = \arctan u + C.


$$

The only difference is that instead of $u$ as the variable, we have $\left(\dfrac{x-1}{\sqrt{2}}\right).$

So, let's perform the substitution

$$


u=\dfrac{x-1}{\sqrt{2}}.


$$

Differentiating, we get

$$


\dfrac{\text{d}u}{\text{d}x}=\dfrac{1}{\sqrt{2}} \quad\Longrightarrow\quad \text{d}x = \sqrt{2}\,\text{d}u.


$$

Finally, we write the integral in terms of $u,$ and evaluate:

$$


\begin{aligned}\begin{matrix}∫\frac{1}{𝑥^{2}−2𝑥+3}\,d𝑥 & =\frac{1}{2}∫\frac{1}{1+((𝑥−1)/\sqrt{2})^{2}}\,d𝑥 \\ & =\frac{1}{2}∫\frac{1}{1+𝑢^{2}}⋅\sqrt{2}\,d𝑢 \\ & =\frac{\sqrt{2}}{2}∫\frac{1}{1+𝑢^{2}}\,d𝑢 \\ & =\frac{\sqrt{2}}{2}arctan⁡𝑢+𝐶 \\ & =\frac{\sqrt{2}}{2}arctan⁡(\frac{𝑥−1}{\sqrt{2}})+𝐶\end{matrix}\end{aligned}


$$

### Example: Computing an Arcsine Integral by Completing the Square

#### Question

Calculate ${\displaystyle \int \dfrac{1}{\sqrt{4x - 4x^2}} \, \text{d}x}.$

#### Explanation

First, we complete the square for the argument of the square root in the denominator:

$$


\begin{aligned}4𝑥−4𝑥^{2} & =−(4𝑥^{2}−4𝑥) \\ & =−((2𝑥)^{2}−2⋅2𝑥+1−1) \\ & =−((2𝑥−1)^{2}−1) \\ & =1−(2𝑥−1)^{2}\end{aligned}


$$

Substituting the above in the given integral, we get

$$


\begin{aligned}∫\frac{1}{\sqrt{4𝑥−4𝑥^{2}}}\,d𝑥 & =∫\frac{1}{\sqrt{1−(2𝑥−1)^{2}}}\,d𝑥.\end{aligned}


$$

This resembles the basic integral for inverse sine:

$$


\int \frac{1}{\sqrt{1-u^2}}\,\text{d}u = \arcsin u+C


$$

The only difference is that instead of $u$ as the variable, we have $(2x - 1).$

So, let's perform the substitution

$$


u =2x - 1.


$$

Differentiating, we get

$$


\dfrac{\text{d}u}{\text{d}x}=2 \quad\Longrightarrow\quad \text{d}x = \dfrac12\text{d}u.


$$

Finally, we write the integral in terms of $u,$ and evaluate:

$$


\begin{aligned}∫\frac{1}{\sqrt{4𝑥−4𝑥^{2}}}\,d𝑥 & =∫\frac{1}{\sqrt{1−(2𝑥−1)^{2}}}\,d𝑥 \\ & =∫\frac{1}{\sqrt{1−𝑢^{2}}}⋅\frac{1}{2}d𝑢 \\ & =\frac{1}{2}∫\frac{1}{\sqrt{1−𝑢^{2}}}\,d𝑢 \\ & =\frac{1}{2}arcsin⁡𝑢+𝐶 \\ & =\frac{1}{2}arcsin⁡(2𝑥−1)+𝐶.\end{aligned}


$$

### Example: Computing an Arcsecant Integral by Completing the Square

#### Question

Evaluate the integral $\displaystyle{\int_{1+2/\sqrt{3}}^{3} \dfrac{1}{|x-1|\sqrt{x^2-2x}}\, \text{d}x}.$

#### Explanation

First, we complete the square for the expression inside the square root:

$$


\begin{aligned} x^2-2x&= x^2 -2x +(1-1)\\[3pt] &= (x^2 -2x +1)-1\\[3pt] &= (x-1)^2-1 \end{aligned}


$$

Substituting the above in the given integral, we get

$$


\int_{1+2/\sqrt{3}}^{3} \dfrac{1}{|x-1|\sqrt{x^2-2x}}\, \text{d}x = \int_{1+2/\sqrt{3}}^{3} \dfrac{1}{|x-1|\sqrt{(x-1)^2-1}}\, \text{d}x.


$$

This resembles the basic integral for inverse secant:

$$


\int \frac{1}{|u|\sqrt{u^2-1}} \, \text{d}u = \text{arcsec} \, u +C


$$

The only difference is that instead of $u$ as the variable, we have $x-1.$

So, let's perform the substitution

$$


u=x-1.


$$

Differentiating, we get

$$


\dfrac{\text{d}u}{\text{d}x}=1 \quad\Longrightarrow\quad \text{d}x = \text{d}u.


$$

Let's use the table below to change the limits from $x$ to $u.$

Therefore,

$$


\begin{aligned} \int_{1+2/\sqrt{3}}^{3} \dfrac{1}{|x-1|\sqrt{x^2-2x}}\, \text{d}x &= \int_{1+2/\sqrt{3}}^{3}\dfrac{1}{|x-1|\sqrt{(x-1)^2-1}}\,\text{d}x \\[5pt] &=\int_{2/\sqrt{3}}^{2} \dfrac{1}{|u|\sqrt{u^2-1}}\, \text{d}u\\[5pt] &= \text{arcsec}\, {u}\Big|_{2/\sqrt{3}}^{2}\\[5pt] &= \text{arcsec} \left(2\right) - \text{arcsec}\left(\dfrac{2}{\sqrt{3}} \right)\\[5pt] &=\left(\dfrac{\pi}{3}-\dfrac{\pi}{6}\right)\\[5pt] &=\dfrac{\pi}{6}. \end{aligned}


$$
