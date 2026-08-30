# Differentiating Reciprocal Trigonometric Functions

Source: https://www.mathacademy.com/topics/1686?courseId=105
Topic ID: 1686

## Prerequisites

- [The Quotient Rule for Differentiation](./1110-the-quotient-rule-for-differentiation.md)

## Lesson

### Introduction

The derivatives of the reciprocal trigonometric functions are shown in the table below:

As with the standard trigonometric functions, we can now differentiate any combination of the above functions using the rules of differentiation.

For example, let's find the derivative of

$$


y= \sec x + \csc x.


$$

We can take the derivative of each term and then add them, as follows:

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =\frac{d}{d𝑥}(sec⁡𝑥+csc⁡𝑥) \\ & =\frac{d}{d𝑥}(sec⁡𝑥)+\frac{d}{d𝑥}(csc⁡𝑥) \\ & =sec⁡𝑥tan⁡𝑥−csc⁡𝑥cot⁡𝑥\end{aligned}


$$

**Note:** We could have computed the derivative of the above function by rewriting it as

$$


y= \dfrac{1}{\cos x} + \dfrac{1}{\sin x}


$$

and applying the appropriate derivative rules. However, this would have taken significantly more work! You can save a lot of time by memorizing the derivatives of the reciprocal trigonometric functions.

### Mnemonic Tricks

Trigonometric functions appear very frequently in calculus, so it's extremely important to commit their derivatives to memory.

Conveniently, there are some mnemonic tricks that we can use to more easily remember the derivatives of trigonometric functions.

$$


\begin{aligned}\frac{d}{d𝑥}(sin⁡𝑥) & =cos⁡𝑥\, & \,\frac{d}{d𝑥}(cos⁡𝑥) & =−sin⁡𝑥 \\ \frac{d}{d𝑥}(tan⁡𝑥) & =sec^{2}⁡𝑥\, & \,\frac{d}{d𝑥}(sec⁡𝑥) & =sec⁡𝑥tan⁡𝑥 \\ \frac{d}{d𝑥}(cot⁡𝑥) & =−csc^{2}⁡𝑥\, & \,\frac{d}{d𝑥}(csc⁡𝑥) & =−csc⁡𝑥cot⁡𝑥\end{aligned}


$$

It's helpful to notice that the "co"-functions (cosine, cosecant, and cotangent) all have negative signs in their derivatives, while the other trigonometric functions (sine, secant, and tangent) do not.

It's also helpful to realize that functions come in pairs.

- Sine and cosine are a pair because each appears in the other's derivative.

- Tangent and secant are a pair because each appears in the other's derivative.

- Cotangent and cosecant are a pair because each appears in the other's derivative.

Lastly, it's helpful to realize the following:

- Ignoring the positive or negative sign, tangent and cotangent have a similar format for their derivatives: the square of the function they're paired with.

- Ignoring the positive or negative sign, secant and cosecant have a similar format for their derivatives: the product of themself and the function they're paired with.

### Example: Differentiating Expressions Involving the Cosecant Function

#### Question

Find $f'(x)$ if $f(x) = 2 \csc x.$

#### Explanation

Here, we just take the constant out of the derivative and use the result for the derivative of $\csc x,$ as follows:

$$


\begin{aligned}𝑓^{′}(𝑥) & =\frac{d}{d𝑥}(2csc⁡𝑥) \\ & =2\frac{d}{d𝑥}(csc⁡𝑥) \\ & =2(−csc⁡𝑥cot⁡𝑥) \\ & =−2csc⁡𝑥cot⁡𝑥\end{aligned}


$$

### Example: Differentiating Expressions Involving the Cotangent Function

#### Question

Find $\dfrac {\textrm d y} {\textrm d x}$ if $y = 2x - 3\cot x.$

#### Explanation

We take the derivative of each term and then add them, as follows:

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =\frac{d}{d𝑥}(2𝑥−3cot⁡𝑥) \\ & =2−3(−csc^{2}⁡𝑥) \\ & =2+3csc^{2}⁡𝑥\end{aligned}


$$

### Example: Differentiating Expressions Involving the Secant Function

#### Question

Calculate $f'(x)$ if $f(x) = x\sec x.$

#### Explanation

We use the product rule, as follows:

$$


\begin{aligned}𝑓^{′}(𝑥) & =\frac{d}{d𝑥}(𝑥sec⁡𝑥) \\ & =\frac{d}{d𝑥}(𝑥)⋅sec⁡𝑥+𝑥⋅\frac{d}{d𝑥}(sec⁡𝑥) \\ & =(1)⋅sec⁡𝑥+𝑥⋅(sec⁡𝑥tan⁡𝑥) \\ & =sec⁡𝑥(1+𝑥tan⁡𝑥)\end{aligned}


$$

### Example: Finding the Slope of the Tangent at a Point of a Function Involving Reciprocal Trigonometric Functions

#### Question

Find the slope of $y=f(x)$ at $x=\dfrac{\pi}{4}$ if $f(x) = \dfrac{-2\cot x}{\sin x}.$

#### Explanation

First, we calculate the derivative using the quotient rule:

$$


\begin{aligned}𝑓^{′}(𝑥) & =\frac{d}{d𝑥}(\frac{−2cot⁡𝑥}{sin⁡𝑥}) \\ & =\frac{\frac{d}{d𝑥}(−2cot⁡𝑥)⋅sin⁡𝑥−(−2cot⁡𝑥)⋅\frac{d}{d𝑥}(sin⁡𝑥)}{d𝑥} \\ & =\frac{−2(−csc^{2}⁡𝑥)⋅sin⁡𝑥+2cot⁡𝑥⋅(cos⁡𝑥)}{sin^{2}⁡𝑥} \\ & =\frac{2csc⁡𝑥+2cot⁡𝑥cos⁡𝑥}{sin^{2}⁡𝑥}\end{aligned}


$$

Then, we substitute $x=\dfrac{\pi}{4}$ in the derivative and get

$$


\begin{aligned}𝑓^{′}(\frac{𝜋}{4}) & =\frac{2csc⁡(\frac{𝜋}{4})+2cot⁡(\frac{𝜋}{4})cos⁡(\frac{𝜋}{4})}{4} \\ & =\frac{2⋅(\sqrt{2})+2⋅(1)⋅(\frac{\sqrt{2}}{2})}{2} \\ & =\frac{3\sqrt{2}}{(\frac{1}{2})} \\ & =6\sqrt{2}.\end{aligned}


$$

### Justifying the Derivatives of Reciprocal Trigonometric Functions

To see why the derivative of $\sec x$ is $\sec x \tan x,$ we start by remembering that

$$


\sec x = \dfrac{1}{\cos x}.


$$

If we now differentiate the above relation using the quotient rule, we get

$$


\begin{aligned}\frac{d}{d𝑥}(sec⁡𝑥) & =\frac{d}{d𝑥}(\frac{1}{cos⁡𝑥}) \\ & =\frac{\frac{d}{d𝑥}(1)⋅cos⁡𝑥−1⋅\frac{d}{d𝑥}(cos⁡𝑥)}{d𝑥} \\ & =\frac{(0)⋅cos⁡𝑥−1⋅(−sin⁡𝑥)}{cos^{2}⁡𝑥} \\ & =\frac{sin⁡𝑥}{cos^{2}⁡𝑥} \\ & =\underset{sec⁡𝑥}{\underset{}{\frac{1}{cos⁡𝑥}}}\underset{tan⁡𝑥}{\underset{}{\frac{sin⁡𝑥}{cos⁡𝑥}}} \\ & =sec⁡𝑥tan⁡𝑥.\end{aligned}


$$

We can use the same method to find the derivative of the other two reciprocal trigonometric functions,

$$


\csc x = \dfrac{1}{\sin x} \qquad \text{and} \qquad \cot x = \dfrac{1}{\tan x}.


$$
