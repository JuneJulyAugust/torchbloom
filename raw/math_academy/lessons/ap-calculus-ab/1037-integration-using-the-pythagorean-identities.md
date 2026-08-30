# Integration Using the Pythagorean Identities

Source: https://www.mathacademy.com/topics/1037?courseId=24
Topic ID: 1037

## Prerequisites

- [Integration Using Basic Trigonometric Identities](./282-integration-using-basic-trigonometric-identities.md)
- [Simplifying Trigonometric Expressions Using the Cotangent-Cosecant Identity](../precalculus/1455-simplifying-trigonometric-expressions-using-the-cotangent-cosecant-identity.md)
- [Alternate Forms of the Secant-Tangent Identity](../precalculus/3857-alternate-forms-of-the-secant-tangent-identity.md)

## Lesson

### Introduction

How can we calculate $\displaystyle{\int} \left(3\sin^2 x + 3\cos^2 x\right) \, \textrm{d}x?$

We can compute integrals like this using the Pythagorean trigonometric identity,

$$


\sin^2 x + \cos^2 x=1.


$$

So, we evaluate our integral as follows:

$$


\begin{aligned} \int \left(3\sin^2 x+ 3\cos^2 x\right ) \, \textrm{d}x &= \int 3(\underbrace{\sin^2 x +\cos^2 x }_1 )\, \textrm{d}x\\&=\int 3(1) \, \textrm{d}x\\&=\int 3 \, \textrm{d}x\\&=3x+C \end{aligned}


$$

Let's look at some more examples.

### Example: Integrating Using the Pythagorean Trigonometric Identity

#### Question

Calculate the integral $\displaystyle\int \dfrac{1}{1-\sin^2 x}\,\textrm{d}x.$

#### Explanation

We use a variation of the Pythagorean identity:

$$


\sin^2 x + \cos^2 x = 1\quad\Longrightarrow\quad \cos^2 x = 1-\sin^2 x.


$$

Using the above, we rewrite the denominator and calculate the resulting integral:

$$


\begin{aligned}∫\frac{1}{1−sin^{2}⁡𝑥}\,d𝑥 & =∫\frac{1}{cos^{2}⁡𝑥}\,d𝑥 \\ & =∫(\frac{1}{cos⁡𝑥})^{2}\,d𝑥 \\ & =∫sec^{2}⁡𝑥\,d𝑥 \\ & =tan⁡𝑥+𝐶.\end{aligned}


$$

### Calculating Integrals Using Related Identities

The identities

$$


1+\tan ^{2}x =\sec ^{2}x


$$

and

$$


1+\cot ^{2}x =\csc ^{2}x


$$

are also called Pythagorean trigonometric identities. They can be used to solve certain integrals involving the expressions $\tan^2 x$ or $\csc^2 x.$ Let's see their application in action!

### Example: Integrating Using the Secant-Tangent Identity

#### Question

Calculate $\, \displaystyle{\int} \tan^2 x \, \textrm{d}x.$

#### Explanation

First, we select the identity that contains a $\tan^2{x}$ term. So we can use the identity

$$


1+\tan^2x =\sec^2x.


$$

Rearranging the above identity gives

$$


\tan^2 x =\sec^2 x -1.


$$

Using the above, we compute the given integral as follows:

$$


\begin{aligned} \int \tan^2 x \, \textrm{d}x&=\int \left(\sec^2 x -1\right ) \, \textrm{d}x\\&=\tan x -x+C. \end{aligned}


$$

### Example: Integrating Using the Cosecant-Cotangent Identity

#### Question

Calculate the integral $\displaystyle{\int} \left(5\cot^2 x -x^2\right) \, \textrm{d}x.$

#### Explanation

In this case, we have to use the identity $1+\cot^2x =\csc^2 x.$ Rearranging this gives

$$


\begin{aligned} \cot^2 x &=\csc^2 x -1. \end{aligned}


$$

Substituting this into our integral gives

$$


\begin{aligned} \int \left(5\cot^2 x -x^2\right) \, \textrm{d}x&=\int \bigg(5\left(\csc^2 x -1 \right) -x^2\bigg) \, \textrm{d}x\\&=\int \left(5\csc^2 x -5 -x^2\right ) \, \textrm{d}x\\&=-5\cot x -5x-\dfrac{x^3}{3}+C. \end{aligned}


$$

### Example: Integrating Trigonometric Expressions With Linear Arguments Using the Pythagorean Identities

#### Question

Calculate $\displaystyle{\int} 2\tan^2 (3x) \, \textrm{d} x.$

#### Explanation

From the identity $1+\tan^2 \theta =\sec^2 \theta$ with $\theta = 3x,$ we get

$$


\begin{aligned} 1+\tan^2 (3x) &=\sec^2 (3x)\\\tan^2 (3x) &=\sec^2 (3x) -1. \end{aligned}


$$

Substituting the above into our integral gives

$$


\begin{aligned} \int 2\tan^2 (3x) \, \textrm{d}x&= 2\int \tan^2 (3x) \, \textrm{d}x\\&= 2\int \left(\sec^2 (3x) -1\right ) \, \textrm{d}x\\&= 2\left(\int \sec^2 (3x)\, \textrm{d}x -\int1 \, \textrm{d}x\right)\\&= 2\left( \dfrac{1}{3}\tan (3x) -x\right)+C\\&= \dfrac{2}{3}\tan (3x) -2x+C. \end{aligned}


$$
