# Differentiating Hyperbolic Functions

Source: https://www.mathacademy.com/topics/1362?courseId=105
Topic ID: 1362

## Prerequisites

- [Selecting Procedures for Calculating Derivatives](./1115-selecting-procedures-for-calculating-derivatives.md)
- [The Reciprocal Hyperbolic Functions](./3265-the-reciprocal-hyperbolic-functions.md)

## Lesson

### Introduction

$$

Since the hyperbolic functions are defined in terms of exponential functions, we can easily calculate their derivatives.

The derivatives of the basic hyperbolic functions are as follows:

$$


\begin{aligned}\frac{d}{d𝑥}(sinh⁡𝑥) & =cosh⁡𝑥 \\ \frac{d}{d𝑥}(cosh⁡𝑥) & =sinh⁡𝑥 \\ \frac{d}{d𝑥}(tanh⁡𝑥) & =sech^{2}⁡𝑥\end{aligned}


$$

Let's use these results to find the derivative of the following function:

$$


y = \sinh{x} - 2\cosh{x}


$$

Using the usual properties of derivatives, we have

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =\frac{d}{d𝑥}(sinh⁡𝑥−2cosh⁡𝑥) \\ & =\frac{d}{d𝑥}(sinh⁡𝑥)+\frac{d}{d𝑥}(−2cosh⁡𝑥) \\ & =\frac{d}{d𝑥}(sinh⁡𝑥)−2\frac{d}{d𝑥}(cosh⁡𝑥) \\ & =cosh⁡𝑥−2sinh⁡𝑥.\end{aligned}


$$

### Example: Basic Derivatives of the Hyperbolic Functions

#### Question

$$

Find the derivative of $y = 3\tanh{x}- \sinh{x}.$

#### Explanation

$$

First, we recall the results for the derivatives of the basic hyperbolic functions:

$$


\dfrac{\text{d}}{\text{d}x} ( \sinh x ) = \cosh x, \quad \dfrac{\text{d}}{\text{d}x} ( \cosh x ) = \sinh x, \quad \dfrac{\text{d}}{\text{d}x} ( \tanh x ) = \operatorname{sech}^2 x


$$

Differentiating the given function using these results, we get

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =\frac{d}{d𝑥}(3tanh⁡𝑥−sinh⁡𝑥) \\ & =3\frac{d}{d𝑥}(tanh⁡𝑥)−\frac{d}{d𝑥}(sinh⁡𝑥) \\ & =3sech^{2}⁡𝑥−cosh⁡𝑥.\end{aligned}


$$

### Example: Differentiating Hyperbolic Functions Using the Chain Rule

#### Question

$$

Find the derivative of $f(x) = \cosh{\sqrt x}.$

#### Explanation

First, we express $f(x)$ as a composite function:

$$


f = \cosh g, \qquad g = \sqrt x


$$

The chain rule states that

$$


\dfrac {\text{d}f} {\text{d}x} = \dfrac {\text{d}f} {\text{d}g} \cdot \dfrac {\text{d}g} {\text{d}x}.


$$

Differentiating, we have

$$


\dfrac {\text{d}f} {\text{d}g} = \sinh g,


$$

and

$$


\dfrac {\text{d}g} {\text{d}x} = \dfrac{1}{2\sqrt x}.


$$

Finally, multiplying the two results together and substituting for $g$ gives

$$


\begin{aligned}\frac{d𝑓}{d𝑥} & =sinh⁡𝑔⋅\frac{1}{2\sqrt{𝑥}} \\ & =sinh⁡\sqrt{𝑥}⋅\frac{1}{2\sqrt{𝑥}} \\ & =\frac{sinh⁡\sqrt{𝑥}}{2\sqrt{𝑥}}.\end{aligned}


$$

### Example: Differentiating Hyperbolic Functions Using the Product Rule

#### Question

$$

Find the derivative of $f(x) = 2x\tanh{x}.$

#### Explanation

$$

Here, we have the product of two functions $u(x) = 2x$ and $v(x)=\tanh x.$ So, we apply the product rule:

$$


\begin{aligned}𝑓^{′}(𝑥) & =(2𝑥)^{′}⋅tanh⁡𝑥+2𝑥⋅(tanh⁡𝑥)^{′} \\ & =2⋅tanh⁡𝑥+2𝑥⋅sech^{2}⁡𝑥 \\ & =2tanh⁡𝑥+2𝑥sech^{2}⁡𝑥 \\ & =2(tanh⁡𝑥+𝑥sech^{2}⁡𝑥)\end{aligned}


$$

### Example: Differentiating Hyperbolic Functions Using the Quotient Rule

#### Question

$$

Find the derivative of $w(x) = \dfrac{x^3}{\cosh{x}}.$

#### Explanation

$$

In this case, the expression for $w(x)$ is a quotient $\dfrac{u(x)}{v(x)}$ with $u(x) = x^3$ and $v(x) = \cosh{x}.$

Therefore, we apply the quotient rule as follows:

$$


\begin{aligned}\begin{matrix}𝑤^{′}(𝑥) & =\frac{𝑢^{′}(𝑥)⋅𝑣(𝑥)−𝑢(𝑥)⋅𝑣^{′}(𝑥)}{[𝑣(𝑥)]^{2}} \\ & =\frac{(𝑥^{3})^{′}⋅cosh⁡𝑥−𝑥^{3}⋅(cosh⁡𝑥)^{′}}{(cosh⁡𝑥)^{2}} \\ & =\frac{3𝑥^{2}⋅cosh⁡𝑥−𝑥^{3}⋅sinh⁡𝑥}{cosh^{2}⁡𝑥} \\ & =\frac{𝑥^{2}(3cosh⁡𝑥−𝑥sinh⁡𝑥)}{cosh^{2}⁡𝑥}\end{matrix}\end{aligned}


$$

### Deriving the Formula for the Derivative of the Hyperbolic Sine

$\%$

We would like the prove the following result:

$$


\dfrac{\text{d}}{\text{d}x}(\sinh{x}) = \cosh x


$$

To do this, we revert to the definition of the hyperbolic sine:

$$


\sinh x = \dfrac{1}{2}(e^x-e^{-x}).


$$

Differentiating the above equation with respect to $x,$ we get

$$


\begin{aligned}\frac{d}{d𝑥}(sinh⁡𝑥) & =\frac{d}{d𝑥}(\frac{1}{2}(𝑒^{𝑥}−𝑒^{−𝑥})) \\ & =\frac{1}{2}⋅\frac{d}{d𝑥}(𝑒^{𝑥}−𝑒^{−𝑥}) \\ & =\frac{1}{2}(𝑒^{𝑥}+𝑒^{−𝑥}) \\ & =cosh⁡𝑥.\end{aligned}


$$

The proof for the derivative of the hyperbolic cosine is very similar. You may wish to try it for yourself.

### Deriving the Formula for the Derivative of the Hyperbolic Tangent

$$

We would like the prove the following result:

$$


\dfrac{\textrm d}{\textrm d x}(\tanh{x}) = \operatorname{sech}^2{x}


$$

We do this using the definition of the hyperbolic tangent. The most convenient definition to work with for this purpose is

$$


\tanh{x} = \dfrac{e^{2x}-1}{e^{2x}+1}.


$$

Differentiating the above equation with respect to $x$ using the quotient rule, we arrive at

$$


\begin{aligned}\frac{d}{d𝑥}(tanh⁡𝑥) & =\frac{d}{d𝑥}(\frac{𝑒^{2𝑥}−1}{𝑒^{2𝑥}+1}) \\ & =\frac{(𝑒^{2𝑥}−1)^{′}⋅(𝑒^{2𝑥}+1)−(𝑒^{2𝑥}−1)⋅(𝑒^{2𝑥}+1)^{′}}{(𝑒^{2𝑥}+1)^{2}} \\ & =\frac{(2𝑒^{2𝑥})(𝑒^{2𝑥}+1)−(𝑒^{2𝑥}−1)(2𝑒^{2𝑥})}{(𝑒^{2𝑥}+1)^{2}} \\ & =\frac{2𝑒^{4𝑥}+2𝑒^{2𝑥}−2𝑒^{4𝑥}+2𝑒^{2𝑥}}{(𝑒^{2𝑥}+1)^{2}} \\ & =\frac{4𝑒^{2𝑥}}{(𝑒^{2𝑥}+1)^{2}} \\ & =(\frac{2𝑒^{𝑥}}{𝑒^{2𝑥}+1})^{2} \\ & =(\frac{2}{𝑒^{𝑥}+𝑒^{−𝑥}})^{2} \\ & =sech^{2}⁡𝑥.\end{aligned}


$$
