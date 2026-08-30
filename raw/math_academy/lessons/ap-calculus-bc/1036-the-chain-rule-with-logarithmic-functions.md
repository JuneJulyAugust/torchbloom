# The Chain Rule With Logarithmic Functions

Source: https://www.mathacademy.com/topics/1036?courseId=21
Topic ID: 1036

## Prerequisites

- [The Chain Rule for Differentiation](../ap-calculus-ab/1108-the-chain-rule-for-differentiation.md)
- [Differentiating Logarithmic Functions](../ap-calculus-ab/1116-differentiating-logarithmic-functions.md)

## Lesson

### Introduction

The chain rule can be used to differentiate logarithmic functions like

$$


y = \ln (2x+1).


$$

First notice that this function can be written as the composite function

$$


y = \ln u, \qquad u = 2x+1.


$$

We can use the chain rule to compute the derivative of this composite function:

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =\frac{d𝑦}{d𝑢}⋅\frac{d𝑢}{d𝑥} \\ & =\frac{d}{d𝑢}(ln⁡𝑢)⋅\frac{d}{d𝑥}(2𝑥+1) \\ & =\frac{1}{𝑢}⋅2 \\ & =\frac{2}{𝑢}\end{aligned}


$$

Substituting $u=2x+1,$ we obtain the final result:

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =\frac{2}{2𝑥+1}\end{aligned}


$$

### Example: Differentiating a Natural Logarithm Function Using the Chain Rule

#### Question

Find the derivative of $f(x) = \ln(x^2-4).$

#### Explanation

First, we express $f(x)$ as the composite function

$$


f = \ln u, \qquad u = x^2-4.


$$

Differentiating gives

$$


\dfrac{\textrm d f}{\textrm d u} = \dfrac{1}{u},\qquad \dfrac{\textrm{d}u}{\textrm d x} = 2x.


$$

We now apply the chain rule, and we get

$$


\begin{aligned}\frac{d𝑓}{d𝑥} & =\frac{d𝑓}{d𝑢}⋅\frac{d𝑢}{d𝑥} \\ & =\frac{1}{𝑢}⋅2𝑥 \\ & =\frac{1}{𝑥^{2}−4}⋅2𝑥 \\ & =\frac{2𝑥}{𝑥^{2}−4}.\end{aligned}


$$

### Example: Differentiating a General Logarithm Function Using the Chain Rule

#### Question

If what is

#### Explanation

First, we express as the composite function

Differentiating gives

We now apply the chain rule, and get
