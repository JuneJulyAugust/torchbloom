# The Chain Rule With Trigonometric Functions

Source: https://www.mathacademy.com/topics/305?courseId=105
Topic ID: 305

## Prerequisites

- [The Chain Rule for Differentiation](./1108-the-chain-rule-for-differentiation.md)
- [Differentiating Reciprocal Trigonometric Functions](./1686-differentiating-reciprocal-trigonometric-functions.md)

## Lesson

### Introduction

The chain rule can be used to differentiate trigonometric functions like

$$


y = \sin (2x).


$$

First, notice that this function can be written as the composite function

$$


y = \sin u, \qquad u = 2x.


$$

We can use the chain rule to compute the derivative of this composite function:

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =\frac{d𝑦}{d𝑢}⋅\frac{d𝑢}{d𝑥} \\ & =\frac{d}{d𝑢}(sin⁡𝑢)⋅\frac{d}{d𝑥}(2𝑥) \\ & =cos⁡𝑢⋅2 \\ & =2cos⁡𝑢\end{aligned}


$$

Substituting $u=2x,$ we obtain the final result:

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =2cos⁡(2𝑥)\end{aligned}


$$

### Example: Differentiating a Trigonometric Function Using the Chain Rule

#### Question

Calculate $f'(x)$ if $f(x) = 2\sin (3x - 1).$

#### Explanation

First, we express $f(x)$ as a composite function

$$


f = 2\sin u, \qquad u=3x-1.


$$

Differentiating gives

$$


\dfrac{\textrm d f}{\textrm d u} = 2\cos u, \qquad\dfrac{\textrm d u}{\textrm d x} = 3.


$$

We now apply the chain rule, and get

$$


\begin{aligned}\frac{d𝑓}{d𝑥} & =\frac{d𝑓}{d𝑢}⋅\frac{d𝑢}{d𝑥} \\ & =2cos⁡𝑢⋅3 \\ & =6cos⁡𝑢 \\ & =6cos⁡(3𝑥−1).\end{aligned}


$$

### Example: Differentiating a Reciprocal Trigonometric Function Using the Chain Rule

#### Question

Calculate $\dfrac{\textrm d y}{\textrm d x}$ if $y = 4\csc (5x + 3).$

#### Explanation

First, we express $y$ as the composite function

$$


y = 4 \csc u, \qquad u = 5x+3.


$$

Differentiating gives

$$


\dfrac{\textrm d y}{\textrm d u} = -4\csc u\cot u, \qquad\dfrac{\textrm d u}{\textrm d x} = 5.


$$

We now apply the chain rule, and get

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =\frac{d𝑦}{d𝑢}⋅\frac{d𝑢}{d𝑥} \\ & =−4csc⁡𝑢cot⁡𝑢⋅5 \\ & =−20csc⁡𝑢cot⁡𝑢 \\ & =−20csc⁡(5𝑥+3)cot⁡(5𝑥+3).\end{aligned}


$$

### Example: Differentiating a Power of a Trigonometric Function Using the Chain Rule

#### Question

Given that $f(x) = \sin^3{x}$, calculate $f'(x).$

#### Explanation

First, we write

$$


f(x) = (\sin{x})^3.


$$

Now, we see that $f(x)$ can be expressed as the composite function

$$


f = u^3, \qquad u=\sin x.


$$

Differentiating, we get

$$


\dfrac{\textrm d f}{\textrm d u} = 3u^2, \qquad \dfrac{\textrm d u}{\textrm d x} = \cos{x}.


$$

We now apply the chain rule, and get

$$


\begin{aligned}𝑓^{′}(𝑥) & =\frac{d𝑓}{d𝑢}⋅\frac{d𝑢}{d𝑥} \\ & =3𝑢^{2}⋅(cos⁡𝑥) \\ & =3(sin⁡𝑥)^{2}cos⁡𝑥 \\ & =3sin^{2}⁡𝑥cos⁡𝑥.\end{aligned}


$$

### Example: Differentiating a Composition of Trigonometric Functions Using the Chain Rule

#### Question

Find the derivative of $y = \tan{\left(\sin(x)\right)}.$

#### Explanation

First, we express $y$ as the composite function

$$


y = \tan u, \qquad u = \sin x.


$$

Differentiating gives

$$


\dfrac{\textrm d y}{\textrm d u} = \sec^2 u,\qquad \dfrac{\textrm{d}u}{\textrm d x} = \cos x.


$$

We now apply the chain rule, and get

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =\frac{d𝑦}{d𝑢}⋅\frac{d𝑢}{d𝑥} \\ & =sec^{2}⁡𝑢⋅cos⁡𝑥 \\ & =sec^{2}⁡(sin⁡𝑥)cos⁡𝑥.\end{aligned}


$$
