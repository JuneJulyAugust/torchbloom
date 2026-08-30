# The Chain Rule With Exponential Functions

Source: https://www.mathacademy.com/topics/1007?courseId=21
Topic ID: 1007

## Prerequisites

- [The Chain Rule for Differentiation](../ap-calculus-ab/1108-the-chain-rule-for-differentiation.md)
- [Differentiating Exponential Functions](../ap-calculus-ab/1114-differentiating-exponential-functions.md)

## Lesson

### Introduction

The chain rule can be used to differentiate exponential functions like

$$


y = e^{3x}.


$$

First, notice that this function can be written as the composite function

$$


y = e^u, \qquad u = 3x.


$$

We can use the chain rule to compute the derivative of this composite function:

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =\frac{d𝑦}{d𝑢}⋅\frac{d𝑢}{d𝑥} \\ & =\frac{d}{d𝑢}(𝑒^{𝑢})⋅\frac{d}{d𝑥}(3𝑥) \\ & =𝑒^{𝑢}⋅3 \\ & =3𝑒^{𝑢}\end{aligned}


$$

Substituting $u=3x,$ we obtain the final result:

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =3𝑒^{3𝑥}\end{aligned}


$$

### Example: Differentiating an Exponential Function with a Linear Exponent

#### Question

Calculate $f'(x)$ if $f(x) = e^{5x +4}.$

#### Explanation

First, we express $f(x)$ as the composite function

$$


f = e^u, \qquad u=5x+4.


$$

Differentiating gives

$$


\dfrac{\textrm d f}{\textrm d u} = e^u,\qquad \dfrac{\textrm d u}{\textrm d x} =5.


$$

We now apply the chain rule, and get

$$


\begin{aligned}\frac{d𝑓}{d𝑥} & =\frac{d𝑓}{d𝑢}⋅\frac{d𝑢}{d𝑥} \\ & =𝑒^{𝑢}⋅5 \\ & =5𝑒^{𝑢} \\ & =5𝑒^{5𝑥+4}.\end{aligned}


$$

### Example: Differentiating an Exponential Function with a Nonlinear Exponent

#### Question

Given that $y=e^{-x^2},$ calculate $\dfrac{\textrm d y}{\textrm d x}.$

#### Explanation

First we express $y$ as the composite function

$$


y = e^u, \qquad u=-x^2.


$$

Differentiating gives

$$


\dfrac{\textrm d y}{\textrm d u} = e^u,\qquad \dfrac{\textrm d u}{\textrm d x} =-2x.


$$

We now apply the chain rule, and get

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =\frac{d𝑦}{d𝑢}⋅\frac{d𝑢}{d𝑥} \\ & =𝑒^{𝑢}⋅(−2𝑥) \\ & =−2𝑥𝑒^{𝑢} \\ & =−2𝑥𝑒^{−𝑥^{2}}.\end{aligned}


$$

### Example: Differentiating a General Exponential Function Using the Chain Rule

#### Question

Given that $y= 3\cdot 2^{1 - x},$ find $\dfrac{\textrm d y}{\textrm d x}.$

#### Explanation

First, we express $y$ as the composite function

$$


y = 3\cdot 2^u, \qquad u=1-x.


$$

Differentiating gives

$$


\dfrac{\textrm d y}{\textrm d u} = 3\cdot 2^u\ln(2),\qquad \dfrac{\textrm d u}{\textrm d x} =-1.


$$

We now apply the chain rule, and get

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =\frac{d𝑦}{d𝑢}⋅\frac{d𝑢}{d𝑥} \\ & =3⋅2^{𝑢}ln⁡(2)⋅(−1) \\ & =−3⋅2^{𝑢}ln⁡(2) \\ & =−3⋅2^{1−𝑥}ln⁡(2).\end{aligned}


$$
