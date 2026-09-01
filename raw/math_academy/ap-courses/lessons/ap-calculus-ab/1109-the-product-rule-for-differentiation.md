# The Product Rule for Differentiation

Source: https://www.mathacademy.com/topics/1109?courseId=24
Topic ID: 1109

## Prerequisites

- [Differentiating Trigonometric Functions](./280-differentiating-trigonometric-functions.md)
- [Differentiating Logarithmic Functions](./1116-differentiating-logarithmic-functions.md)

## Lesson

### Introduction

Suppose that we have the two functions $u(x)=2x^3$ and $v(x)=x^2.$ How do we calculate the derivative of their product $(u(x) \cdot v(x))'?$

To do that, we can use the **product rule**, which states that the derivative of the product of two functions is given by the formula

$$


\left(u(x) \cdot v(x)\right)' = u'(x) \cdot v(x) + u(x) \cdot v'(x).


$$

In our case, the derivatives of the two functions are given by

$$


\begin{aligned}𝑢^{′}(𝑥) & =(2𝑥^{3})^{′}=6𝑥^{2}, \\ 𝑣^{′}(𝑥) & =(𝑥^{2})^{′}=2𝑥.\end{aligned}


$$

If we plug all of this into the product rule formula, we get

$$


\begin{aligned}(𝑢(𝑥)⋅𝑣(𝑥))^{′} & =(6𝑥^{2})(𝑥^{2})+(2𝑥^{3})(2𝑥) \\ & =6𝑥^{4}+4𝑥^{4} \\ & =10𝑥^{4}.\end{aligned}


$$

This example was quite simple, and we could have solved it by calculating the product first and then taking the derivative. We can do it now to double check our result:

$$


\begin{aligned}(𝑢(𝑥)⋅𝑣(𝑥))^{′} & =(2𝑥^{3}⋅𝑥^{2})^{′} \\ & =(2𝑥^{5})^{′} \\ & =10𝑥^{4}\,✓\end{aligned}


$$

Sometimes, however, we cannot calculate the product algebraically, or it can be tedious to do it. In those cases, the product rule will turn out to be very useful!

### Example: Differentiating a Product Containing a Trigonometric Function

#### Question

Differentiate $x\cos x.$

#### Explanation

Here, we have the product of the two functions $u(x)=x$ and $v(x)=\cos x.$ So, we apply the product rule:

$$


\begin{aligned} (x\cos x)' &= u'(x) \cdot v(x) + u(x) \cdot v'(x)\\&= (x)'\cdot \cos x + x\cdot (\cos x)'\\& = 1 \cdot \cos x + x (-\sin x)\\& = \cos x - x \sin x \end{aligned}


$$

### Example: Differentiating a Product Containing an Exponential or Logarithmic Function

#### Question

Given that $f(x)=x^2\ln x,$ find $f'(x).$

#### Explanation

Here, we have the product of two functions $u(x) = x^2$ and $v(x)=\ln x.$ So, we apply the product rule:

$$


\begin{aligned}𝑓^{′}(𝑥) & =(𝑥^{2})^{′}ln⁡𝑥+𝑥^{2}(ln⁡𝑥)^{′} \\ & =2𝑥⋅ln⁡𝑥+𝑥^{2}(\frac{1}{𝑥}) \\ & =2𝑥ln⁡𝑥+𝑥 \\ & =𝑥(2ln⁡𝑥+1)\end{aligned}


$$

### Leibniz Notation

The product rule can also be written using *Leibniz notation*:

If $y = u(x) \cdot v(x),$ then

$$


\dfrac{\text{d}y}{\text{d}x} = \dfrac{\text{d}u}{\text{d}x} \cdot v + u \cdot \dfrac{\text{d}v}{\text{d}x}


$$

### Example: Finding the Slope of the Tangent Line to a Product at a Given Point

#### Question

If a curve $\mathcal C$ is given by $y=e^x\sin x,$ calculate the slope of the tangent line to the curve at the point where $x=\dfrac \pi 2.$

#### Explanation

We differentiate using the product rule. Let $u(x) = e^x$ and $v(x)=\sin{x}.$ Then, we have

$$


\dfrac{\textrm d u}{\textrm d x} = e^x,\qquad \dfrac{\textrm d v}{\textrm d x} = \cos x.


$$

Applying the product rule gives

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =𝑢\frac{d𝑣}{d𝑥}+𝑣\frac{d𝑢}{d𝑥} \\ & =𝑒^{𝑥}⋅cos⁡𝑥+sin⁡𝑥⋅𝑒^{𝑥} \\ & =𝑒^{𝑥}(cos⁡𝑥+sin⁡𝑥).\end{aligned}


$$

To find the slope of the tangent line, we now substitute $x=\dfrac\pi 2$ into the formula and get

$$


\begin{aligned}\frac{d𝑦}{d𝑥}_{𝑥=𝜋/2} & =𝑒^{𝜋/2}(cos⁡(\frac{𝜋}{2})+sin⁡(\frac{𝜋}{2})) \\ & =𝑒^{𝜋/2}(0+1) \\ & =𝑒^{𝜋/2}.\end{aligned}


$$

Therefore, the slope of the tangent line is $e^{\pi/2}.$
