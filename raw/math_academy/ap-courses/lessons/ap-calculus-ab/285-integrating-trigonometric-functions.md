# Integrating Trigonometric Functions

Source: https://www.mathacademy.com/topics/285?courseId=24
Topic ID: 285

## Prerequisites

- [Differentiating Reciprocal Trigonometric Functions](./1686-differentiating-reciprocal-trigonometric-functions.md)
- [The Sum Rule for Indefinite Integrals](./3769-the-sum-rule-for-indefinite-integrals.md)

## Lesson

### Introduction

We know that the derivative of sine is cosine:

$$


\dfrac{\textrm d }{\textrm d x}(\sin{x}) = \cos{x}


$$

Since integration is the reverse of differentiation, we see that the integral of cosine is sine:

$$


\int \cos{x}\,\textrm d x = \sin{x} + C


$$

We can discover two other integrals by considering the derivatives of cosine and tangent:

$$


\begin{aligned}∫sin⁡𝑥 d𝑥 & =−cos⁡𝑥+𝐶 \\ ∫sec^{2}⁡𝑥 d𝑥 & =tan⁡𝑥+𝐶.\end{aligned}


$$

Similarly, by considering the derivatives of secant, cosecant, and cotangent, we arrive at

$$


\begin{aligned}∫sec⁡𝑥tan⁡𝑥 d𝑥 & =sec⁡𝑥+𝐶 \\ ∫csc⁡𝑥cot⁡𝑥 d𝑥 & =−csc⁡𝑥+𝐶 \\ ∫csc^{2}⁡𝑥 d𝑥 & =−cot⁡𝑥+𝐶.\end{aligned}


$$

With these six formulas, we can integrate many different trigonometric functions.

### Example: Integrating Sine and Cosine

#### Question

Calculate $\displaystyle \int 3\sin{x}\,\textrm d x.$

#### Explanation

Recall that

$$


\int \sin x \, \textrm dx = -\cos x + C.


$$

Therefore, we have

$$


\begin{aligned}∫3sin⁡𝑥\,d𝑥 & =3∫sin⁡𝑥\,d𝑥 \\ & =3(−cos⁡𝑥)+𝐶 \\ & =−3cos⁡𝑥+𝐶.\end{aligned}


$$

### Example: Integrating Secant-Tangent and Cosecant-Cotangent

#### Question

Calculate $\displaystyle \int (-\csc x\cot x)\,\textrm d x.$

#### Explanation

Recall that

$$


\int \csc x \cot x \, \textrm dx = - \csc x + C.


$$

Therefore, we have

$$


\begin{aligned}∫(−csc⁡𝑥cot⁡𝑥)\,d𝑥 & =−∫(csc⁡𝑥cot⁡𝑥)\,d𝑥 \\ & =−(−csc⁡𝑥)+𝐶 \\ & =csc⁡𝑥+𝐶.\end{aligned}


$$

### Example: Integrating Secant Squared

#### Question

Calculate the integral $\displaystyle{\int} (2\sec^2 x + \sec x \tan x)\, \text{d}x.$

#### Explanation

Recall that

$$


\int \sec^2 x \, \textrm dx = \tan x + C


$$

and

$$


\int \sec x \tan x \, \textrm dx = \sec x + C.


$$

Therefore, we get

$$


\begin{aligned} \int (2\sec^2 x + \sec x \tan x )\, \text{d}x& = 2 \int \sec^2 x \, \text{d}x+ \int \sec x \tan x \, \text{d}x \\&=2\tan x + \sec x + C. \end{aligned}


$$

### Example: Integrating Cosecant Squared

#### Question

Calculate the integral $\displaystyle{\int} \csc{x}(\csc{x}+3\cot{x})\, \text{d}x.$

#### Explanation

Recall that

$$


\int \csc^2 x \, \textrm dx = -\cot x + C


$$

and

$$


\int \csc x \cot x \, \textrm dx = -\csc x + C.


$$

Therefore, we get

$$


\begin{aligned}∫csc⁡𝑥(csc⁡𝑥+3cot⁡𝑥)\,d𝑥 & =∫csc^{2}⁡𝑥+3csc⁡𝑥cot⁡𝑥\,d𝑥 \\ & =∫csc^{2}⁡𝑥\,d𝑥+3∫csc⁡𝑥cot⁡𝑥\,d𝑥 \\ & =−cot⁡𝑥−3csc⁡𝑥+𝐶.\end{aligned}


$$
