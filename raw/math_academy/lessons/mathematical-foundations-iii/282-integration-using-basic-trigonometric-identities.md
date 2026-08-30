# Integration Using Basic Trigonometric Identities

Source: https://www.mathacademy.com/topics/282?courseId=136
Topic ID: 282

## Prerequisites

- [Simplifying Expressions Using Basic Trigonometric Identities](./203-simplifying-expressions-using-basic-trigonometric-identities.md)
- [Integrating Trigonometric Functions Using Substitution](./478-integrating-trigonometric-functions-using-substitution.md)

## Lesson

### Introduction

Suppose we want to calculate the integral

$$


\displaystyle \int\dfrac{1}{\sin^2x}\,\textrm d x.


$$

At first glance, this looks kind of tricky. However, if we use the identity $\dfrac{1}{\sin x} = \csc x,$ we can rewrite the integral as

$$


\begin{aligned}∫\frac{1}{sin^{2}⁡𝑥}\,d𝑥=∫(\frac{1}{sin⁡𝑥})^{2}\,d𝑥=∫csc^{2}⁡𝑥\,d𝑥,\end{aligned}


$$

and we see that this is just a standard trigonometric integral:

$$


\int\dfrac{1}{\sin^2x}\,\textrm d x = \int\csc^2 x\,\textrm d x =-\cot x + C


$$

When confronted with a tricky-looking trigonometric integral, we can often reduce it to a standard integral using a trigonometric identity.

### Example: Integrating a Product of Trigonometric Functions Using Trigonometric Identities

#### Question

Calculate $\displaystyle \int \dfrac{1}{\sin x}\left(\cot x + \sin^2 x\right)\,\textrm d x.$

#### Explanation

We multiply out the parentheses and then use the identity $\dfrac{1}{\sin x} = \csc x,$ as follows:

$$


\begin{aligned}∫\frac{1}{sin⁡𝑥}(cot⁡𝑥+sin^{2}⁡𝑥)\,d𝑥 & =∫(\frac{1}{sin⁡𝑥}⋅cot⁡𝑥+\frac{1}{sin⁡𝑥}⋅sin^{2}⁡𝑥)\,d𝑥 \\ & =∫(csc⁡𝑥⋅cot⁡𝑥+sin⁡𝑥)\,d𝑥 \\ & =∫csc⁡𝑥cot⁡𝑥\,d𝑥+∫sin⁡𝑥\,d𝑥 \\ & =−csc⁡𝑥−cos⁡𝑥+𝐶\end{aligned}


$$

### Example: Integrating a Quotient of Trigonometric Functions Using Trigonometric Identities

#### Question

Calculate $\displaystyle \int_0^{\pi/3} \dfrac{\sin x}{\cos^2 x}\,\textrm d x.$

#### Explanation

We can write the integral as

$$


\int_0^{\pi/3} \dfrac{\sin x}{\cos^2 x}\,\textrm d x = \int_0^{\pi/3} \dfrac{1}{\cos x}\cdot \dfrac{\sin x}{\cos x}\,\textrm d x.


$$

We then use the fact that $\dfrac{\sin x}{\cos x} = \tan x$ and $\dfrac{1}{\cos x} = \sec x$ to express this as

$$


\int_0^{\pi/3} \sec x\tan x\,\textrm d x,


$$

which is a standard trigonometric integral. Therefore,

$$


\begin{aligned}∫_{𝜋/30}^{}\frac{sin⁡𝑥}{cos^{2}⁡𝑥}\,d𝑥 & =∫_{𝜋/30}^{}sec⁡𝑥tan⁡𝑥\,d𝑥 \\ & =sec⁡𝑥_{𝜋/30}^{} \\ & =sec⁡(\frac{𝜋}{3})−sec⁡(0) \\ & =2−1 \\ & =1.\end{aligned}


$$

### Example: Integrating a Trigonometric Expression Using Identities and Substitution

#### Question

Calculate $\displaystyle \int \tan{2x}\,\textrm d x.$

#### Explanation

We use the identity $\tan 2x = \dfrac{\sin 2x}{\cos 2x}$ and rewrite the integral as

$$


\int \tan{2x}\,\textrm d x = \int \dfrac{\sin{2x}}{\cos 2x}\,\textrm d x.


$$

Notice that the numerator of the integrand is proportional to the derivative of the denominator. So, we can solve this by substitution.

Let $u=\cos 2x.$ Then

$$


\dfrac{\textrm{d}u}{\textrm{d}x}=-2 \sin 2x \quad\Longrightarrow\quad -\dfrac 1 2 \,\textrm d u= \sin 2x \, \textrm d x.


$$

Using the above, we can write the integral in terms of $u$ and evaluate:

$$


\begin{aligned}∫\frac{sin⁡2𝑥}{cos⁡2𝑥}\,d𝑥 & =−\frac{1}{2}∫\frac{1}{𝑢}\,d𝑢 \\ & =−\frac{1}{2}ln⁡|𝑢|+𝐶 \\ & =−\frac{1}{2}ln⁡|cos⁡2𝑥|+𝐶 \\ & =\frac{1}{2}ln⁡|(cos⁡2𝑥)^{−1}|+𝐶 \\ & =\frac{1}{2}ln⁡|sec⁡2𝑥|+𝐶\end{aligned}


$$
