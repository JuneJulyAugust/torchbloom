# Integrating Trigonometric Functions Using Substitution

Source: https://www.mathacademy.com/topics/478?courseId=106
Topic ID: 478

## Prerequisites

- [Calculating Definite Integrals Using Substitution](./1159-calculating-definite-integrals-using-substitution.md)

## Lesson

### Introduction

We know how to integrate $\cos{x}.$ But how do we integrate $\cos{3x}?$

To compute

$$


\int \cos{3x} \, \textrm dx,


$$

we can use substitution. If we let $u=3x,$ then

$$


\dfrac{\textrm d u}{\textrm d x} = 3\quad\Longrightarrow\quad \textrm d x = \dfrac 1 3 \textrm d u.


$$

Finally, we can write the integral in terms of $u$ and evaluate:

$$


\begin{aligned}∫cos⁡3𝑥\,d𝑥 & =∫cos⁡𝑢⋅\frac{1}{3}\,d𝑢 \\ & =\frac{1}{3}∫cos⁡𝑢\,d𝑢 \\ & =\frac{1}{3}sin⁡𝑢+𝐶 \\ & =\frac{1}{3}sin⁡3𝑥+𝐶\end{aligned}


$$

**Note:** After solving an integral using substitution, we should always double-check that our result is correct. If we differentiate the result, then it should come out to the original integrand:

$$


\begin{aligned}\frac{d}{d𝑥}(\frac{1}{3}sin⁡3𝑥+𝐶) & =\frac{1}{3}⋅\frac{d}{d𝑥}(sin⁡3𝑥)+\frac{d}{d𝑥}(𝐶) \\ & =\frac{1}{3}⋅cos⁡3𝑥⋅\frac{d}{d𝑥}(3𝑥)+0 \\ & =\frac{1}{3}cos⁡3𝑥⋅3 \\ & =cos⁡3𝑥\,✓\end{aligned}


$$

### Example: Integrating Trigonometric Functions With Linear Arguments

#### Question

Calculate the integral $\displaystyle\int 2 \sin {\left(\dfrac x 3\right)} \, \textrm{d}x.$

#### Explanation

If we let $u=\dfrac x 3,$ then

$$


\dfrac{\textrm d u}{\textrm d x} = \dfrac 1 3\quad\Longrightarrow\quad \textrm d x =3\, \textrm d u.


$$

Using the above, we can write the integral in terms of $u$ and evaluate:

$$


\begin{aligned}∫2sin⁡(\frac{𝑥}{3})\,d𝑥 & =2∫sin⁡𝑢⋅3\,d𝑢 \\ & =2⋅3∫sin⁡𝑢\,d𝑢 \\ & =−6cos⁡𝑢+𝐶 \\ & =−6cos⁡(\frac{𝑥}{3})+𝐶\end{aligned}


$$

### Example: Integrating Reciprocal Trigonometric Functions With Linear Arguments

#### Question

Calculate the integral $\displaystyle\int 5 \csc {\left(6x+\dfrac \pi 3\right)} \cot {\left(6x+\dfrac \pi 3\right)} \, \textrm{d}x.$

#### Explanation

If we let $u=6x+\dfrac \pi 3,$ then

$$


\dfrac{\textrm d u}{\textrm d x} = 6\quad\Longrightarrow\quad \textrm d x =\dfrac 1 6\, \textrm d u.


$$

Using the above, we can write the integral in terms of $u$ and evaluate:

$$


\begin{aligned}∫5csc⁡(6𝑥+\frac{𝜋}{3})cot⁡(6𝑥+\frac{𝜋}{3})\,d𝑥 & =5∫csc⁡(6𝑥+\frac{𝜋}{3})cot⁡(6𝑥+\frac{𝜋}{3})\,d𝑥 \\ & =5∫csc⁡𝑢cot⁡𝑢⋅\frac{1}{6}\,d𝑢 \\ & =\frac{5}{6}∫csc⁡𝑢cot⁡𝑢\,d𝑢 \\ & =−\frac{5}{6}csc⁡𝑢+𝐶 \\ & =−\frac{5}{6}csc⁡(6𝑥+\frac{𝜋}{3})+𝐶\end{aligned}


$$

### Integrating Products Containing Trigonometric Functions Using Substitution

Suppose that we want to calculate $\displaystyle \int 2x \cos{(x^2)}\,\textrm d x.$

Notice that if we let $u = x^2,$ then we have

$$


\int \underbrace{2x}_{u'} \cos({\overbrace{x^2}^u})\,\textrm d x.


$$

In other words, the factor multiplying the trigonometric function is the derivative of the argument! Integrals like this can always be solved using substitution.

So, let $u=x^2.$ Differentiating gives

$$


\dfrac{\textrm{d} u}{\textrm{d}x } = 2x \quad\Longrightarrow\quad \textrm d u = 2x\,\textrm d x.


$$

Using the above, we now substitute and evaluate, as follows:

$$


\begin{aligned}∫2𝑥cos⁡(𝑥^{2})\,d𝑥 & =∫cos⁡(𝑥^{2})⋅2𝑥\,d𝑥 \\ & =∫cos⁡𝑢\,d𝑢 \\ & =sin⁡𝑢+𝐶 \\ & =sin⁡(𝑥^{2})+𝐶.\end{aligned}


$$

### Example: Integrating Products Containing Trigonometric Functions Using Substitution

#### Question

Calculate $\displaystyle \int x^2 \sec^2\left(x^3-\dfrac{\pi}{6}\right)\,\textrm d x.$

#### Explanation

Let $u = x^3 - \dfrac{\pi}{6}.$ Differentiating, we have

$$


\dfrac{\textrm{d} u}{\textrm{d}x } = 3x^2 \quad\Longrightarrow\quad \dfrac 1 3 \textrm d u = x^2\,\textrm d x.


$$

Using the above, we can write the integral in terms of $u$ and evaluate:

$$


\begin{aligned}∫𝑥^{2}sec^{2}⁡(𝑥^{3}−\frac{𝜋}{6})\,d𝑥 & =∫sec^{2}⁡(𝑥^{3}−\frac{𝜋}{6})⋅𝑥^{2}\,d𝑥 \\ & =∫sec^{2}⁡(𝑢)⋅\frac{1}{3}\,d𝑢 \\ & =\frac{1}{3}∫sec^{2}⁡(𝑢)\,d𝑢 \\ & =\frac{1}{3}tan⁡𝑢+𝐶 \\ & =\frac{1}{3}tan⁡(𝑥^{3}−\frac{𝜋}{6})+𝐶\end{aligned}


$$

### Example: Integrating Quotients Containing Trigonometric Functions Using Substitution

#### Question

Evaluate the integral $\displaystyle \int_0^{\pi/4} \dfrac{\tan x \sec^2 x}{1+\tan^2x}\,\textrm d x.$

#### Explanation

Notice that the numerator is proportional to the derivative of the denominator, because

$$


\dfrac{\textrm d}{\textrm d x}(1+\tan^2 x) = 2\tan{x}\sec^2 x.


$$

So, let $u = 1+\tan^2 x.$ Differentiating, we have

$$


\dfrac{\textrm{d} u}{\textrm{d}x } = 2\tan x\sec^2 x \quad\Longrightarrow\quad \dfrac 1 2 \textrm d u = \tan x\sec^2 x\,\textrm d x.


$$

Calculating the limits for $u$ gives

We now substitute and evaluate, as follows:

$$


\begin{aligned}∫_{𝜋/40}^{}\frac{tan⁡𝑥sec^{2}⁡𝑥}{1+tan^{2}⁡𝑥}\,d𝑥 & =∫_{𝜋/40}^{}\frac{1}{1+tan^{2}⁡𝑥}⋅tan⁡𝑥sec^{2}⁡𝑥\,d𝑥 \\ & =∫_{21}^{}\frac{1}{𝑢}⋅\frac{1}{2}\,d𝑢 \\ & =\frac{1}{2}∫_{21}^{}\frac{1}{𝑢}\,d𝑢 \\ & =\frac{1}{2}(ln⁡2−ln⁡1) \\ & =\frac{1}{2}ln⁡2\end{aligned}


$$
