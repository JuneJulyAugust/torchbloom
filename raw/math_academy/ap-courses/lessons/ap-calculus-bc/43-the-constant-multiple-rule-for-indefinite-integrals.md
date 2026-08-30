# The Constant Multiple Rule for Indefinite Integrals

Source: https://www.mathacademy.com/topics/43?courseId=21
Topic ID: 43

## Prerequisites

- [The Sum and Constant Multiple Rules for Differentiation](../ap-calculus-ab/278-the-sum-and-constant-multiple-rules-for-differentiation.md)
- [The Antiderivative](../ap-calculus-ab/308-the-antiderivative.md)

## Lesson

### Introduction

Suppose we want to find the integral of a power function multiplied by a constant, like $5x^2.$ How do we proceed?

According to the **constant factor rule**, we can just take the constant factor out of the integral, like this:

$$


\int 5 x^2\, \text{d}x = 5\cdot \int x^2 \,\text{d}x


$$

Then, we solve the integral using the power rule:

$$


\begin{aligned}5⋅∫𝑥^{2}\,d𝑥 & =5⋅(\frac{𝑥^{2+1}}{2+1})+𝐶 \\ & =\frac{5}{3}𝑥^{3}+𝐶\end{aligned}


$$

We can use this trick in general. Whenever the integrand is a function $f(x)$ multiplied by a constant $k,$ we can simplify as

$$


\int k f(x)\, \text{d}x = k \int f(x) \,\text{d}x.


$$

**Watch out!** We can only take *constant factors* out of integrals. We *cannot* take any variables out of integrals.

### Example: Using the Constant Factor Rule to Integrate a Power Function

#### Question

Calculate $\displaystyle \int \dfrac{2}{3} x \,\textrm d x.$

#### Explanation

We can just take the constant factor out of the integral, and then apply the power rule:

$$


\begin{aligned}∫\frac{2}{3}𝑥\,d𝑥 & =\frac{2}{3}∫𝑥\,d𝑥 \\ & =\frac{2}{3}(\frac{𝑥^{1+1}}{1+1})+𝐶 \\ & =\frac{2}{3}⋅\frac{𝑥^{2}}{2}+𝐶 \\ & =\frac{1}{3}𝑥^{2}+𝐶\end{aligned}


$$

### Example: Using the Constant Factor Rule to Integrate a Constant Function

#### Question

Calculate $\displaystyle \int 6 \,\textrm d x.$

#### Explanation

We can just take the constant factor out of the integral, and then apply the power rule:

$$


\begin{aligned}∫6\,d𝑥 & =6∫1\,d𝑥 \\ & =6∫𝑥^{0}\,d𝑥 \\ & =6⋅\frac{𝑥^{0+1}}{0+1}+𝐶 \\ & =6⋅𝑥+𝐶 \\ & =6𝑥+𝐶\end{aligned}


$$

In general, we can see that for any constant $k,$ we have $\displaystyle \int k \,\textrm d x = kx + C.$
