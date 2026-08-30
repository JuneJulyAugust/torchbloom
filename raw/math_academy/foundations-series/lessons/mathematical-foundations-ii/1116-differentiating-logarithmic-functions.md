# Differentiating Logarithmic Functions

Source: https://www.mathacademy.com/topics/1116?courseId=111
Topic ID: 1116

## Prerequisites

- [Differentiating Exponential Functions](./1114-differentiating-exponential-functions.md)

## Lesson

### Introduction

The derivative of the natural logarithm is the reciprocal function:

$$


\dfrac{\textrm{d}}{ \textrm{d} x}\left( \ln x \right)= \dfrac{1}{x}


$$

We'll prove this result in a future lesson.

### Example: Differentiating the Product of a Constant and the Natural Logarithm Function

#### Question

Given that $y=5\ln x$, find $\dfrac{\textrm{d}y}{\textrm{d}x}.$

#### Explanation

The derivative of the natural logarithm is the reciprocal function:

$$


\dfrac{\textrm{d}}{ \textrm{d} x}\left( \ln x \right)= \dfrac{1}{x}


$$

We apply our formula and get

$$


\begin{aligned} \dfrac{\textrm{d}y}{\textrm{d}x} & = \left(5\ln x\right)'\\& = 5 (\ln x)'\\&=5\cdot \dfrac{1}{x}\\&= \dfrac{5}{x}. \end{aligned}


$$

### Example: Differentiating a Sum Containing a Natural Logarithm Function

#### Question

Given that $f(x)=2\ln x+x^2-1$, find $f'(x).$

#### Explanation

Taking the derivative, we have

$$


\begin{aligned} f'(x) &= \left(2\ln x+x^2-1\right)'\\&=2 \cdot \dfrac{1}{x}+2x-0\\&=\dfrac{2}{x}+2x. \end{aligned}


$$

### Differentiating a Logarithmic Function with a General Base

For a general logarithm of base $a,$ the derivative is given by

$$


\dfrac{\textrm{d}}{ \textrm{d} x}\left( \log_a x \right)= \dfrac{1}{x\ln a}.


$$

Also, recall that whenever $\log$ is written without a base, we can assume that it represents the base $10.$ So, we have

$$


\log x = \log_{10} x.


$$

Therefore,

$$


\begin{aligned}\frac{d}{d𝑥}(log⁡𝑥) & =\frac{d}{d𝑥}(log_{10}⁡𝑥)=\frac{1}{𝑥ln⁡10}.\end{aligned}


$$

**Note:** To see where this rule comes from, we can use the change-of-base formula as shown below.

$$


\log_a x = \dfrac{\ln x}{\ln a}


$$

Taking the derivative and using the fact that $\ln a$ is a constant, then, we have

$$


\begin{aligned}\frac{d}{d𝑥}(log_{𝑎}⁡𝑥) & =\frac{d}{d𝑥}(\frac{ln⁡𝑥}{ln⁡𝑎}) \\ & =\frac{1}{ln⁡𝑎}⋅\frac{d}{d𝑥}(ln⁡𝑥) \\ & =\frac{1}{ln⁡𝑎}⋅\frac{1}{𝑥} \\ & =\frac{1}{𝑥ln⁡𝑎}.\end{aligned}


$$

### Example: Differentiating a Logarithmic Function With a General Base

#### Question

Given that $y=4\log_3 x,$ find $\dfrac{\textrm{d}y}{\textrm{d}x}.$

#### Explanation

Here, we apply our formula for the derivative when the base of the logarithm is a number other than $e.$ By doing so, we obtain

$$


\begin{aligned} \dfrac{\textrm{d}y}{\textrm{d}x}&=\dfrac{\textrm{d}}{\textrm{d}x}\left(4\log_3 x\right)\\&=4\dfrac{\textrm{d}}{\textrm{d}x}\left(\log_3 x\right)\\&=4\cdot\dfrac{1}{x \ln 3}\\&=\dfrac{4}{x \ln 3}. \end{aligned}


$$

### Example: Calculating the Slope of the Tangent Line of a Logarithmic Function at a Point

#### Question

Given that $y= \log_4 x + \ln x$, find the slope of the tangent at $x=1.$

#### Explanation

To find the slope of the tangent at a given point, we have to find $\dfrac {\textrm{d}y} {\textrm{d}x}$ at that point.

Taking the derivative, we have

$$


\begin{aligned} \dfrac{\textrm{d}y}{\textrm{d}x} &= \dfrac{\textrm{d}}{\textrm{d}x}\left( \log_4 x + \ln x \right)\\&= \dfrac{\textrm{d}}{\textrm{d}x}(\log_4 x) + \dfrac{\textrm{d}}{\textrm{d}x}(\ln x )\\&= \dfrac{1}{x\ln 4} + \dfrac{1}{x}. \end{aligned}


$$

Therefore, the slope of the tangent at $x=1$ is

$$


\begin{aligned}\frac{d𝑦}{d𝑥}_{𝑥=1} & =(\frac{1}{𝑥ln⁡4}+\frac{1}{𝑥})_{𝑥=1} \\ & =\frac{1}{ln⁡4}+1.\end{aligned}


$$
