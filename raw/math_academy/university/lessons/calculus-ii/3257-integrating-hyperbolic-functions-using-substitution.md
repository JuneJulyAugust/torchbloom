# Integrating Hyperbolic Functions Using Substitution

Source: https://www.mathacademy.com/topics/3257?courseId=106
Topic ID: 3257

## Prerequisites

- [Integrating Hyperbolic Functions](../calculus-i/304-integrating-hyperbolic-functions.md)
- [Integrating Trigonometric Functions Using Substitution](./478-integrating-trigonometric-functions-using-substitution.md)

## Lesson

### Introduction

Consider the integral $$

$$


\int \operatorname{csch}^2(2x+3) \, \text{d}x.


$$

As it is, this integral doesn't resemble any of the basic integrals we have encountered so far. However, it is very similar to the basic integral for the hyperbolic cotangent,

$$


\int \operatorname{csch}^2 u \, \text{d}u = -\coth u+C.


$$

The only difference is that instead of $u$ as the variable, we have $2x+3.$

So, let $u=2x+3.$ Differentiating, we have

$$


\dfrac{\textrm d u}{\textrm d x} = 2\quad\Longrightarrow\quad \text{d}x = \dfrac{1}{2} \, \text{d}u.


$$

Using the above, we can write the integral in terms of $u$ and compute it, as follows:

$$


\begin{aligned}∫csch^{2}⁡(2𝑥+3)\,d𝑥 & =∫csch^{2}⁡𝑢⋅\frac{1}{2}\,d𝑢 \\ & =\frac{1}{2}∫csch^{2}⁡𝑢\,d𝑢 \\ & =\frac{1}{2}(−coth⁡𝑢)+𝐶 \\ & =−\frac{1}{2}coth⁡(2𝑥+3)+𝐶\end{aligned}


$$

### Example: Integrating Hyperbolic Functions With Linear Arguments

#### Question

Evaluate the integral $\displaystyle \int_{-2}^{1} \sinh {\left(2x+1\right)} \, \text{d}x.$

#### Explanation

Let $u=2x+1.$ Differentiating, we have

$$


\dfrac{\text{d}u}{\text{d}x} = 2 \quad\Longrightarrow\quad \textrm d x=\dfrac 1 2 \, \textrm d u.


$$

Before substituting, we use the table below to change the limits from $x$ to $u.$

Using the above, we can write the integral in terms of $u$ and evaluate:

$$


\begin{aligned}∫_{1−2}sinh⁡(2𝑥+1)\,d𝑥 & =∫_{3−3}sinh⁡𝑢⋅\frac{1}{2}\,d𝑢 \\ & =\frac{1}{2}∫_{3−3}sinh⁡𝑢\,d𝑢 \\ & =\frac{1}{2}cosh⁡𝑢_{3−3} \\ & =\frac{1}{2}(cosh⁡3−cosh⁡(−3)) \\ & =\frac{1}{2}(cosh⁡3−cosh⁡3) \\ & =0\end{aligned}


$$

### Example: Integrating Reciprocal Hyperbolic Functions With Linear Arguments

#### Question

Calculate the integral $\displaystyle \int \operatorname{csch}(3x+1)\coth(3x+1) \, \text{d}x.$

#### Explanation

Let $u=3x+1.$ Differentiating, we have

$$


\dfrac{\textrm d u}{\textrm d x} = 3\quad\Longrightarrow\quad \text{d}x =\dfrac{1}{3} \, \text{d}u.


$$

Using the above, we can write the integral in terms of $u$ and compute it, as follows:

$$


\begin{aligned}∫csch⁡(3𝑥+1)coth⁡(3𝑥+1)\,d𝑥 & =∫csch⁡𝑢coth⁡𝑢⋅\frac{1}{3}\,d𝑢 \\ & =\frac{1}{3}∫csch⁡𝑢coth⁡𝑢\,d𝑢 \\ & =\frac{1}{3}(−csch⁡𝑢)+𝐶 \\ & =−\frac{1}{3}csch⁡(3𝑥+1)+𝐶\end{aligned}


$$

### Example: Integrating Products Containing Hyperbolic Functions Using Substitution

#### Question

Evaluate the integral $\displaystyle {\int_{-2}^{2} x^2\sinh{x^3}}\, \text{d}x.$

#### Explanation

Let $u=x^3.$ Differentiating, we have

$$


\dfrac{\text{d}u}{\text{d}x}=3x^2\quad\Longrightarrow\quad \dfrac{1}{3}\text{d} u = x^2\, \textrm d x.


$$

Before substituting, we use the table below to change the limits from $x$ to $u.$

Using the above, we can write the integral in terms of $u$ and evaluate:

$$


\begin{aligned} \int_{-2}^{2} x^2\sinh{x^3}\, \text{d}x &=\int_{-2}^{2} \sinh{x^3}\cdot x^2\,\text{d}x\\[5pt] &=\int_{-8}^{8} \sinh{u}\cdot\dfrac{1}{3}\, \text{d}u\\[5pt] &=\dfrac{1}{3}\cosh u\Big|_{-8}^{8}\\[5pt] &=\dfrac{1}{3}\left(\cosh{8} - \cosh{(-8)}\right)\\[5pt] &=\dfrac{1}{3}\left(\cosh{8} - \cosh{8}\right)\\[5pt] &=\dfrac{1}{3}\cdot 0\\[5pt] &=0 \end{aligned}


$$

### Example: Integrating Quotients Containing Hyperbolic Functions Using Substitution

#### Question

Calculate $\displaystyle \int \dfrac{x\sinh{x^2}}{\cosh{x^2}}\, \text{d}x.$

#### Explanation

$$

Let $u= \cosh{x^2}.$ Differentiating, we have

$$


\dfrac{\text{d}u}{\text{d}x} = 2x\sinh{x^2} \quad\Longrightarrow\quad \dfrac{1}{2} \, \text{d}u = x\sinh{x^2} \,\text{d}x.


$$

Using the above, we can write the integral in terms of $u$ and compute it, as follows:

$$


\begin{aligned} \displaystyle \int \dfrac{x\sinh{x^2}}{\cosh{x^2}}\, \text{d}x &= \int \dfrac{1}{\cosh{x^2}}\cdot x\sinh{x^2}\, \text{d}x\\[5pt] &= \int \dfrac{1}{u}\cdot \dfrac{1}{2} \, \textrm d u \\[5pt] &= \dfrac{1}{2}\int \dfrac{1}{u}\, \text{d}u\\[5pt] &= \dfrac{1}{2}\ln|u|+C\\[5pt] &= \dfrac{1}{2}\ln\left(\cosh{x^2}\right)+ C \end{aligned}


$$
