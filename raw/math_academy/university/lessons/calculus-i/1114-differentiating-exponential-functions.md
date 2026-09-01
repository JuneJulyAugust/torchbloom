# Differentiating Exponential Functions

Source: https://www.mathacademy.com/topics/1114?courseId=105
Topic ID: 1114

## Prerequisites

- [Calculating the Slope of a Tangent Line Using Differentiation](./332-calculating-the-slope-of-a-tangent-line-using-differentiation.md)
- [The Natural Logarithm](../../../high-school/traditional/lessons/algebra-ii/818-the-natural-logarithm.md)
- [Graphing Exponential Growth Functions](../../../high-school/traditional/lessons/algebra-i/1530-graphing-exponential-growth-functions.md)

## Lesson

### Introduction

The exponential function $f(x) = e^x$ has the special property that its derivative is the function itself:

$$


\dfrac{\text{d}}{ \text{d} x}\left( e^x \right)= e^x


$$

So, taking the derivative of an exponential function does nothing to the exponential function. The exponential function remains exactly the same.

Note that the exponential function is the *only* function with this special property.

We'll justify this result at the end of the lesson. But for now, let's get some practice working with it.

### Example: Differentiating the Product of a Constant and the Exponential Function, Plus a Constant

#### Question

Given that $f(x)=3e^x + \ln 3$, find $f'(x).$

#### Explanation

The derivative of $e^x$ is just $e^x$ itself. On the other hand, $\ln 3$ is a constant, so its derivative is $0.$

Using the addition rule, then, we have

$$


\begin{aligned} f'(x) &= \dfrac{\text{d}}{\text{d}x}\left(3e^x + \ln 3\right)\\&= \dfrac{\text{d}}{\text{d}x}\left( 3e^x\right) + \dfrac{\text{d}}{\text{d}x}\left( \ln 3 \right)\\&= 3\dfrac{\text{d}}{\text{d}x}\left(e^x\right) + 0\\&= 3 e^x. \end{aligned}


$$

### Example: Differentiating the Product of a Constant and the Exponential Function, Plus a Polynomial

#### Question

Given that $f(x)=4e^x+ 3x^4 - x^2,$ find $f'(x).$

#### Explanation

Using the addition and the power rules, we get

$$


\begin{aligned} f'(x) &= \dfrac{\text{d}}{\text{d}x}\left(4e^x+3x^{4} - x^2 \right)\\&= \dfrac{\text{d}}{\text{d}x}\left(4e^x\right)+\dfrac{\text{d}}{\text{d}x}\left(3x^{4}\right) -\dfrac{\text{d}}{\text{d}x}\left(x^{2}\right) \\&= 4\dfrac{\text{d}}{\text{d}x}\left(e^x\right)+3\dfrac{\text{d}}{\text{d}x}\left(x^{4}\right) - 2x \\&= 4 e^x+ 3 \cdot 4x^{3} - 2x \\&= 4 e^x+ 12x^{3} - 2x. \end{aligned}


$$

### Differentiating an Exponential Function with a Base Other Than e

If we replace the base $e$ of an exponential function by any other positive number $a$, then the derivative is as follows:

$$


\dfrac{\text{d}}{ \text{d} x}\left( a^x \right)= a^x \ln a


$$

We just multiply the given exponential function by the natural logarithm of the base.

Note that since $\ln e =1$, our first formula is a particular case of this one!

$$


\dfrac{\text{d}}{ \text{d} x}\left( e^x \right)= e^x \ln e = e^x \cdot 1 = e^x


$$

### Example: Differentiating an Exponential Function with a Base Other Than e

#### Question

Given that $f(x)=3 \cdot 2^x$, find $f'(x).$

#### Explanation

Applying the formula, we get

$$


\begin{aligned} f'(x) &= \dfrac{\text{d}}{\text{d}x}\left(3 \cdot 2^x\right) \\&= 3 \cdot \dfrac{\text{d}}{\text{d}x}\left(2^x\right) \\&= 3 \cdot 2^{x}\ln(2) \\&= 3 \ln(2) \cdot 2^{x}. \end{aligned}


$$

### Justifying the Rule for the Derivative of the Exponential Function

To derive the identity

$$


\frac{\mathrm{d}}{\mathrm{d}x}(e^x) = e^x,


$$

we begin with the definition of the derivative:

where $f(x) = e^x$.

Substituting the function $f(x)$ into the definition of $f'(x),$ we get

$$


\begin{aligned}𝑓^{′}(𝑥) & =\underset{ℎ→0}{lim}\frac{𝑒^{𝑥+ℎ}−𝑒^{𝑥}}{ℎ} \\ & =\underset{ℎ→0}{lim}\frac{𝑒^{𝑥}⋅𝑒^{ℎ}−𝑒^{𝑥}}{ℎ} \\ & =\underset{ℎ→0}{lim}\frac{𝑒^{𝑥}⋅(𝑒^{ℎ}−1)}{ℎ} \\ & =𝑒^{𝑥}⋅\underset{ℎ→0}{lim}\frac{𝑒^{ℎ}−1}{ℎ}.\end{aligned}


$$

Now, it can be shown that

$$


\lim_{h \to 0} \frac{e^h - 1}{h} = 1,


$$

which gives

$$


f'(x) = e^x \cdot 1 = e^x.


$$

Therefore, we conclude that

$$


\frac{\mathrm{d}}{\mathrm{d}x}(e^x) = e^x.


$$

### Justifying the Second Rule

Now, let's derive the rule

The trick here is to write this in terms of

First, note that since the natural logarithm is the inverse of the exponential function, we have

and by the power rule for logarithms, we can write this as

Now, the following result can be used (we'll prove it in the subsequent topics):

Therefore, we conclude that

as required.
