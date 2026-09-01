# Second Derivatives of Parametric Equations

Source: https://www.mathacademy.com/topics/431?courseId=136
Topic ID: 431

## Prerequisites

- [Implicit Differentiation](./57-implicit-differentiation.md)
- [Second and Higher-Order Derivatives](../../../ap-courses/lessons/ap-calculus-ab/281-second-and-higher-order-derivatives.md)
- [Differentiating Parametric Curves](./798-differentiating-parametric-curves.md)

## Lesson

### Introduction

For a parametrically defined function we know that the derivative is given by

where denotes and denotes

To calculate the second derivative we differentiate with respect to and use the chain rule, as follows:

For example, let's calculate for the curve defined by the parametric equations

To calculate we first need to compute the derivatives of and We get

So, we have

Now, computing the second derivative, we get

### Example: Finding the Second Derivative of a Parametric Curve Given the First Derivative

#### Question

A curve is defined by the parametric equations $x =e^{t}, \, y= e^{2t}+1.$ Given that $\dfrac{\mathrm{d}y}{\mathrm{d}x}= 2e^t,$ calculate $\dfrac{\textrm d^2 y}{\textrm d x^2}.$

#### Explanation

To compute the second derivative, we can use the formula

$$


\begin{aligned}\frac{d^{2}𝑦}{d𝑥^{2}} & =\frac{\frac{d}{d𝑡}(\frac{d𝑦}{d𝑥})}{d𝑡}.\end{aligned}


$$

We're given that $\dfrac{\mathrm{d}y}{\mathrm{d}x}= 2e^t,$ and we can calculate $\dfrac{\mathrm dx}{\mathrm dt}$ as follows:

$$


\dfrac{\mathrm dx}{\mathrm dt} = \dfrac{\mathrm d}{\mathrm dt} (e^t) = e^t


$$

Substituting into the formula, we get

$$


\begin{aligned}\frac{d^{2}𝑦}{d𝑥^{2}} & =\frac{\frac{d}{d𝑡}(2𝑒^{𝑡})}{d𝑡} \\ & =\frac{2𝑒^{𝑡}}{𝑒^{𝑡}} \\ & =2.\end{aligned}


$$

### Example: Finding the Second Derivative of a Parametric Curve

#### Question

A curve is defined by the parametric equations $x=e^t, y=2e^{2t}.$ Calculate $\dfrac{\textrm d^2 y}{\textrm d x^2}.$

#### Explanation

To find the first derivative, we will use the formula

$$


\frac{\mathrm{d}y}{\mathrm{d}x} = \dfrac{y'(t)}{x'(t)}.


$$

Differentiating $x$ and $y,$ we get

$$


x'(t) = e^t, \qquad y'(t)=4e^{2t}.


$$

Therefore,

$$


\frac{\mathrm{d}y}{\mathrm{d}x} = \dfrac{4e^{2t}}{e^t} = 4e^t.


$$

To compute the second derivative, we can use the formula

$$


\begin{aligned}\frac{d^{2}𝑦}{d𝑥^{2}} & =\frac{\frac{d}{d𝑡}(\frac{d𝑦}{d𝑥})}{d𝑡}.\end{aligned}


$$

Substituting into the formula, we get

$$


\begin{aligned}\frac{d^{2}𝑦}{d𝑥^{2}} & =\frac{\frac{d}{d𝑡}(4𝑒^{𝑡})}{d𝑡} \\ & =\frac{4𝑒^{𝑡}}{𝑒^{𝑡}} \\ & =4.\end{aligned}


$$

### Example: Calculating the Derivative of a Parametric Curve at a Given Point

#### Question

A curve is defined by the parametric equations

$$


x = \sin(2t), \qquad y= 2\cos (2t) \qquad 0 \leq t \lt \pi.


$$

Given that $\dfrac{\textrm d y}{\textrm d x} = -2 \tan(2t),$ calculate $\dfrac{\textrm d^2 y}{\textrm d x^2}$ at the point where $t=\dfrac\pi 8.$

#### Explanation

To compute $\dfrac{\textrm d^2 y}{\textrm d x^2},$ we can use the formula

$$


\begin{aligned}\frac{d^{2}𝑦}{d𝑥^{2}} & =\frac{\frac{d}{d𝑡}(\frac{d𝑦}{d𝑥})}{d𝑡}.\end{aligned}


$$

We're given that $\dfrac{\mathrm{d}y}{\mathrm{d}x}= -2 \tan(2t),$ and we can calculate $\dfrac{\mathrm dx}{\mathrm dt}$ as follows:

$$


\dfrac{\mathrm dx}{\mathrm dt} = \dfrac{\mathrm d}{\mathrm dt} ( \sin 2t ) = 2 \cos(2t).


$$

Substituting into the formula, we get

$$


\begin{aligned}\frac{d^{2}𝑦}{d𝑥^{2}} & =\frac{\frac{d}{d𝑡}(−2tan⁡2𝑡)}{d𝑡} \\ & =\frac{−4sec^{2}⁡(2𝑡)}{2cos⁡(2𝑡)} \\ & =−4sec^{2}⁡(2𝑡)⋅\frac{1}{2}sec⁡(2𝑡) \\ & =−2sec^{3}⁡(2𝑡).\end{aligned}


$$

Finally, we evaluate at $t=\dfrac{\pi}{8},$ and we get

$$


\begin{aligned}\frac{d^{2}𝑦}{d𝑥^{2}}_{𝑡=𝜋/8} & =−2sec^{3}⁡(2⋅\frac{𝜋}{8}) \\ & =−2sec^{3}⁡(\frac{𝜋}{4}) \\ & =−2(\sqrt{2})^{3} \\ & =−4\sqrt{2}.\end{aligned}


$$
