# The Sum and Constant Multiple Rules for Definite Integrals

Source: https://www.mathacademy.com/topics/1685?courseId=24
Topic ID: 1685

## Prerequisites

- [Integration Using Inverse Trigonometric Functions](./342-integration-using-inverse-trigonometric-functions.md)
- [Applying the Fundamental Theorem of Calculus to Exponential and Trigonometric Functions](./3575-applying-the-fundamental-theorem-of-calculus-to-exponential-and-trigonometric-functions.md)

## Lesson

### Introduction

The properties of indefinite integrals also apply to definite integrals. For example, to evaluate the definite integral

$$


\displaystyle\int_{2}^{3} 4 x \, \textrm d x,


$$

we can use the constant multiple rule and factor the constant out of the integral:

$$


\begin{aligned}∫_{32}^{}4𝑥\,d𝑥 & =4∫_{32}^{}𝑥\,d𝑥 \\ & =4⋅\frac{𝑥^{2}}{2}_{32}^{} \\ & =2𝑥^{2}_{32}^{} \\ & =2(3^{2}−2^{2}) \\ & =2(9−4) \\ & =10.\end{aligned}


$$

In general, the constant multiple rule holds for any constant $k$ and any definite integral:

$$


\begin{aligned}∫_{𝑏𝑎}^{}𝑘𝑓(𝑥)\,d𝑥 & =𝑘∫_{𝑏𝑎}^{}𝑓(𝑥)\,d𝑥.\end{aligned}


$$

### Example: Evaluating a Definite Integral Using the Constant Multiple Rule

#### Question

Calculate $\displaystyle \int_{-1}^{2} 9 x^2 \, \textrm d x.$

#### Explanation

Factoring the constant out of the integral, we have

$$


\begin{aligned}∫_{2−1}^{}9𝑥^{2}\,d𝑥 & =9∫_{2−1}^{}𝑥^{2}\,d𝑥 \\ & =9⋅\frac{𝑥^{3}}{3}\,_{2−1}^{} \\ & =3𝑥^{3}\,_{2−1}^{} \\ & =3(2^{3}−(−1)^{3}) \\ & =3(8−(−1)) \\ & =3⋅9 \\ & =27.\end{aligned}


$$

### Integrating the Sum of Two Functions

We can also use the sum rule to compute the definite integral of the sum of two functions. For example, to evaluate the definite integral

$$


\displaystyle\int_{1}^{2} (x+x^2) \, \textrm d x,


$$

we can split up the integral into a sum of two integrals and evaluate each integral separately:

$$


\begin{aligned}∫_{21}^{}(𝑥+𝑥^{2})\,d𝑥 & =∫_{21}^{}𝑥\,d𝑥+∫_{21}^{}𝑥^{2}\,d𝑥 \\ & =\frac{𝑥^{2}}{2}_{21}^{}+\frac{𝑥^{3}}{3}_{21}^{} \\ & =\frac{4−1}{2}+\frac{8−1}{3} \\ & =\frac{3}{2}+\frac{7}{3} \\ & =\frac{23}{6}.\end{aligned}


$$

In general,

$$


\begin{aligned}∫_{𝑏𝑎}^{}(𝑓(𝑥)+𝑔(𝑥))\,d𝑥 & =∫_{𝑏𝑎}^{}𝑓(𝑥)\,d𝑥+∫_{𝑏𝑎}^{}𝑔(𝑥)\,d𝑥.\end{aligned}


$$

### Example: Evaluating the Integral of the Sum of Two Functions Using the Sum Rule

#### Question

Evaluate $\displaystyle \int_{0}^{\pi/4} (\sec x \tan x - \cos x)\, \textrm d x.$

#### Explanation

Splitting up the integral into the difference of two integrals and evaluating each integral separately, we get

$$


\begin{aligned}∫_{𝜋/40}^{}(sec⁡𝑥tan⁡𝑥−cos⁡𝑥)\,d𝑥 & =∫_{𝜋/40}^{}sec⁡𝑥tan⁡𝑥\,d𝑥−∫_{𝜋/40}^{}cos⁡𝑥\,d𝑥 \\ & =sec⁡𝑥\,_{𝜋/40}^{}−sin⁡𝑥\,_{𝜋/40}^{} \\ & =(sec⁡\frac{𝜋}{4}−sec⁡0)−(sin⁡\frac{𝜋}{4}−sin⁡0) \\ & =(\sqrt{√2}−1)−(\frac{\sqrt{√2}}{2}−0) \\ & =\sqrt{√2}−\frac{\sqrt{√2}}{2}−1 \\ & =\frac{2\sqrt{√2}−\sqrt{√2}}{2}−1 \\ & =\frac{\sqrt{√2}}{2}−1.\end{aligned}


$$

### Combining the Constant Multiple and Sum Rules

To compute the integral of the sum of two functions multiplied by constants, we can combine the addition rule and the constant multiple rule. For example, to compute the integral

$$


\int_{0}^1 (3x^2 + 6x)\,\textrm d x ,


$$

we can split up the sum and factor out the constants, as follows:

$$


\begin{aligned}∫_{10}^{}(3𝑥^{2}+6𝑥)\,d𝑥 & =∫_{10}^{}3𝑥^{2}\,d𝑥+∫_{10}^{}6𝑥\,d𝑥 \\ & =3∫_{10}^{}𝑥^{2}\,d𝑥+6∫_{10}^{}𝑥\,d𝑥.\end{aligned}


$$

Then, we can compute the two resulting integrals using the usual methods.

In general, for functions $f(x)$ and $g(x)$ and constants $c$ and $k$, we have

$$


\begin{aligned}∫_{𝑏𝑎}^{}(𝑐𝑓(𝑥)+𝑘𝑔(𝑥))\,d𝑥 & =𝑐∫_{𝑏𝑎}^{}𝑓(𝑥)\,d𝑥+𝑘∫_{𝑏𝑎}^{}𝑔(𝑥)\,d𝑥.\end{aligned}


$$

### Example: Evaluating the Integral of a Polynomial Function

#### Question

Evaluate $\displaystyle \int_{-2}^2(2x^3 - 5)\, \textrm d x.$

#### Explanation

Splitting up the sum and factoring out the constants, we have

$$


\begin{aligned}∫_{2−2}^{}(2𝑥^{3}−5)\,d𝑥 & =2∫_{2−2}^{}𝑥^{3}\,d𝑥−5∫_{2−2}^{}1\,d𝑥 \\ & =2⋅\frac{𝑥^{4}}{4}_{2−2}^{}−5𝑥_{2−2}^{} \\ & =\frac{1}{2}𝑥^{4}\,_{2−2}^{}−5𝑥\,_{2−2}^{} \\ & =\frac{1}{2}(2^{4}−(−2)^{4})−5(2−(−2)) \\ & =\frac{1}{2}(16−16)−5⋅4 \\ & =−20.\end{aligned}


$$

### Example: Evaluating the Integral of a Sum of Two Functions

#### Question

Calculate $\displaystyle \int_{1}^{4} \left(\sqrt x - \dfrac 2 {x^2}\right) \, \textrm d x.$

#### Explanation

First, we rewrite the integral as

$$


\int_1^4 \left( \sqrt x - \dfrac 2 {x^2} \right) \, \textrm dx = \int_1^4 \left( x^{1/2}-2x^{-2} \right) \, \textrm dx.


$$

Then, we split the integral into the difference of two integrals and factor out the constants. We get

$$


\begin{aligned}∫_{41}^{}(\sqrt{√𝑥}−\frac{2}{𝑥^{2}})\,d𝑥 & =∫_{41}^{}𝑥^{1/2}\,d𝑥−2∫_{41}^{}𝑥^{−2}\,d𝑥 \\ & =\frac{2}{3}𝑥^{3/2}\,_{41}^{}+2𝑥^{−1}\,_{41}^{} \\ & =\frac{2}{3}(4^{3/2}−1^{3/2})+2(4^{−1}−1^{−1}) \\ & =\frac{2}{3}(8−1)+2(\frac{1}{4}−1) \\ & =\frac{14}{3}+2⋅(−\frac{3}{4}) \\ & =\frac{14}{3}−\frac{3}{2} \\ & =\frac{19}{6}.\end{aligned}


$$
