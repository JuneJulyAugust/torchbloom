# The Quotient Rule for Differentiation

Source: https://www.mathacademy.com/topics/1110?courseId=105
Topic ID: 1110

## Prerequisites

- [The Product Rule for Differentiation](./1109-the-product-rule-for-differentiation.md)

## Lesson

### Introduction

We know how to calculate the derivative of the product of two functions, but what if we have a quotient?

For that, we can use the **quotient rule**. The quotient rule is a formula to calculate the derivative of the ratio of two functions like

$$


f(x) = \dfrac {u(x)}{v(x)}.


$$

The quotient rule for differentiation states that the derivative of the function above is given by

$$


f'(x) = \dfrac {u'(x)\cdot v(x) - u(x) \cdot v'(x)} {[v(x)]^2}.


$$

For example, suppose that we have the function $f(x)$ given by

$$


f(x)= \dfrac{x}{x^2+1},


$$

and we want to find $f'(x).$

Here $u(x)=x$ and $v(x)=x^2+1.$ Their derivatives are given by

$$


\begin{aligned}𝑢^{′}(𝑥) & =(𝑥)^{′}=1, \\ 𝑣^{′}(𝑥) & =(𝑥^{2}+1)^{′}=2𝑥.\end{aligned}


$$

If we plug them in the formula, we get:

$$


\begin{aligned}𝑓^{′}(𝑥) & =\frac{𝑢^{′}(𝑥)⋅𝑣(𝑥)−𝑢(𝑥)⋅𝑣^{′}(𝑥)}{[𝑣(𝑥)]^{2}} \\ & =\frac{1⋅(𝑥^{2}+1)−𝑥⋅2𝑥}{(𝑥^{2}+1)^{2}} \\ & =\frac{𝑥^{2}+1−2𝑥^{2}}{(𝑥^{2}+1)^{2}} \\ & =\frac{1−𝑥^{2}}{(𝑥^{2}+1)^{2}}.\end{aligned}


$$

### Example: Differentiating a Quotient of Two Polynomials

#### Question

Given that $f(x) = \dfrac{x} {9x^2 + 5x},$ find $f'(x).$

#### Explanation

The numerator and denominator are $u(x) = x$ and $v(x) = 9x^2 + 5x,$ respectively. Their derivatives are given by

$$


\begin{aligned}𝑢^{′}(𝑥) & =1, \\ 𝑣^{′}(𝑥) & =18𝑥+5.\end{aligned}


$$

Applying the quotient rule, we have

$$


\begin{aligned} f'(x) & = \dfrac {u'(x)\cdot v(x) - u(x) v'(x)} {[v(x)]^2}\\& = \dfrac{\left( 9x^2+5x \right )\cdot 1 -x\cdot \left( 18x+5 \right)}{\left( 9x^2+5x\right)^2}\\& = \dfrac{\left( 9x^2+5x-18x^2-5x \right)}{\left( 9x^2+5x\right)^2}\\& = -\dfrac{9x^2}{\left( 9x^2+5x\right)^2}. \end{aligned}


$$

### Example: Differentiating a Quotient Containing Other Functions

#### Question

If $f(x)=\dfrac{1+\sin x}{x},$ find $f'(x).$

#### Explanation

In this case, the expression for $f(x)$ is a quotient $\dfrac{u(x)}{v(x)}$ with $u(x) = 1+\sin x$ and $v(x) = x.$

Therefore, we apply the quotient rule as follows:

$$


\begin{aligned} f'(x) & = \dfrac{u'(x)\cdot v(x) - u(x)\cdot v'(x)}{[v(x)]^2}\\& = \dfrac{(1+\sin x)'\cdot (x) -(1+\sin x)\cdot (x)'}{x^2}\\& = \dfrac{\cos x \cdot x- (1+\sin x)\cdot 1}{x^2}\\& = \dfrac{x \cos x -\sin x -1}{x^2} \end{aligned}


$$

### Leibniz Notation

Using Leibniz notation, the quotient rule is expressed as follows:

$$


\dfrac{\textrm{d}}{\textrm{d}x}\left (\dfrac u v\right) = \dfrac {v \dfrac {\textrm{d}u} {\textrm{d}x} - u \dfrac{\textrm{d}v}{\textrm{d}x}}{v^2}


$$

### Example: Differentiating a Quotient Using Leibniz Notation

#### Question

Given that $y=\dfrac{1}{3x+7},$ find $\dfrac{\textrm{d}y}{\textrm{d}x}.$

#### Explanation

Let $u=1$ and $v=3x+7.$ Then

$$


\begin{aligned}\frac{d𝑢}{d𝑥} & =0\,and\,\frac{d𝑣}{d𝑥}=3.\end{aligned}


$$

Using the quotient rule, we get

$$


\begin{aligned} \dfrac{\textrm{d}y}{\textrm{d}x} & = \dfrac{ v\dfrac{\textrm{d}u}{\textrm{d}x}-u\dfrac{\textrm{d}v}{\textrm{d}x}}{v^2}\\& = \dfrac{ \left( 3x+7 \right ) \cdot 0 -1\cdot 3}{\left( 3x+7\right)^2}\\& = -\dfrac{3}{\left( 3x+7\right)^2}. \end{aligned}


$$

### Justifying the Formula for the Derivative of Tangent

We can now prove that $(\tan x)' = \sec^2{x}$ using the quotient rule. Here's how!

$$


\begin{aligned}\frac{d}{d𝑥}(tan⁡𝑥) & =\frac{d}{d𝑥}(\frac{sin⁡𝑥}{cos⁡𝑥}) \\ & =\frac{(sin⁡𝑥)^{′}⋅(cos⁡𝑥)−(sin⁡𝑥)⋅(cos⁡𝑥)^{′}}{cos^{2}⁡𝑥} \\ & =\frac{(cos⁡𝑥)⋅(cos⁡𝑥)−(sin⁡𝑥)⋅(−sin⁡𝑥)}{cos^{2}⁡𝑥} \\ & =\frac{cos^{2}⁡𝑥+sin^{2}⁡𝑥}{cos^{2}⁡𝑥} \\ & =\frac{1}{cos^{2}⁡𝑥} \\ & =sec^{2}⁡𝑥.\end{aligned}


$$
