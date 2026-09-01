# Differentiating Inverse Reciprocal Trigonometric Functions

Source: https://www.mathacademy.com/topics/1721?courseId=24
Topic ID: 1721

## Prerequisites

- [Differentiating Inverse Trigonometric Functions](./303-differentiating-inverse-trigonometric-functions.md)

## Lesson

### Introduction

We can calculate the derivatives of the inverse reciprocal trigonometric functions by using their definition and the chain rule, similar to how we did for the inverse trigonometric functions. When we do so, we get the following results:

$$


\begin{aligned}\frac{d}{d𝑥}(arcsec 𝑥) & =\frac{1}{|𝑥|\sqrt{𝑥^{2}−1}} \\ \frac{d}{d𝑥}(arccsc 𝑥) & =−\frac{1}{|𝑥|\sqrt{𝑥^{2}−1}} \\ \frac{d}{d𝑥}(arccot 𝑥) & =−\frac{1}{1+𝑥^{2}}\end{aligned}


$$

### Example: Differentiating Inverse Reciprocal Trigonometric Functions

#### Question

Calculate $\dfrac {\text{d}y}{\text{d}x}$ if $y = 2 \,\textrm {arccot} x.$

#### Explanation

The formula for the derivative of $\text{arccot}$ is

$$


\dfrac{\textrm d}{\textrm d x}(\textrm {arccot } x) = -\dfrac 1 {1+x^2}.


$$

Using the formula above, we obtain

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =\frac{d}{d𝑥}(2\,arccot 𝑥) \\ & =2⋅\frac{d}{d𝑥}(arccot 𝑥) \\ & =2⋅(−\frac{1}{1+𝑥^{2}}) \\ & =−\frac{2}{1+𝑥^{2}}.\end{aligned}


$$

### Example: Differentiating Inverse Reciprocal Trigonometric Functions Using the Chain Rule

#### Question

Find $f'(x)$ if $f(x) =2 \, \textrm {arccot} (x^2 + 5).$

#### Explanation

The formula for the derivative of $\text{arccot}$ is

$$


\dfrac{\textrm d}{\textrm d x}(\textrm {arccot } x) = -\dfrac 1 {1+x^2}.


$$

Using the chain rule and the formula above, we obtain

$$


\begin{aligned}𝑓^{′}(𝑥) & =\frac{d}{d𝑥}(2\,arccot (𝑥^{2}+5)) \\ & =2⋅(−\frac{1}{1+(𝑥^{2}+5)^{2}})⋅\frac{d}{d𝑥}(𝑥^{2}+5) \\ & =−\frac{2}{1+(𝑥^{2}+5)^{2}}⋅2𝑥 \\ & =−\frac{4𝑥}{1+(𝑥^{2}+5)^{2}} \\ & =−\frac{4𝑥}{𝑥^{4}+10𝑥^{2}+26}\,.\end{aligned}


$$

### Example: Differentiating Inverse Reciprocal Trigonometric Functions Using the Product Rule

#### Question

If $f(x) =3 x\, \textrm {arccsc}x,$ calculate $f'(x).$

#### Explanation

The formula for the derivative of $\text{arccsc}$ is

$$


\dfrac{\textrm d}{\textrm d x}(\textrm {arccsc } x) = -\dfrac 1 {|x| \sqrt {x^2 - 1}} \, .


$$

Using the product rule and the formula above, we obtain

$$


\begin{aligned}𝑓^{′}(𝑥) & =\frac{d}{d𝑥}(3𝑥\,arccsc 𝑥) \\ & =3\frac{d}{d𝑥}(𝑥\,arccsc 𝑥) \\ & =3(𝑥⋅\frac{d}{d𝑥}(arccsc 𝑥)+arccsc 𝑥⋅\frac{d}{d𝑥}(𝑥)) \\ & =3𝑥(−\frac{1}{|𝑥|\sqrt{𝑥^{2}−1}})+3\,arccsc 𝑥⋅1 \\ & =−\frac{3𝑥}{|𝑥|\sqrt{𝑥^{2}−1}}+3\,arccsc 𝑥.\end{aligned}


$$

### Example: Differentiating Inverse Reciprocal Trigonometric Functions Using the Quotient Rule

#### Question

If $f(x) = \dfrac{\text{arcsec} x}{\text{arccsc} x},$ calculate $f'(x).$

#### Explanation

Here, we let $u(x) = \text{arcsec} x$ and $v(x) = \text{arccsc} x$, and apply the quotient rule.

We use the formulae

$$


u'(x) = \dfrac 1 {|x| \sqrt {x^2 - 1}} \quad \text{and} \quad v'(x) = -\dfrac 1 {|x| \sqrt {x^2 - 1}}.


$$

Therefore,

$$


\begin{aligned}𝑓^{′}(𝑥) & =\frac{𝑢^{′}(𝑥)⋅𝑣(𝑥)−𝑢(𝑥)⋅𝑣^{′}(𝑥)}{[𝑣(𝑥)]^{2}} \\ & =\frac{\frac{1}{|𝑥|\sqrt{𝑥^{2}−1}}⋅arccsc 𝑥−arcsec 𝑥⋅(−\frac{1}{|𝑥|\sqrt{𝑥^{2}−1}})}{|𝑥|\sqrt{𝑥^{2}−1}} \\ & =(\frac{1}{|𝑥|\sqrt{𝑥^{2}−1}})\frac{arccsc 𝑥+arcsec 𝑥}{arccsc ^{2}𝑥} \\ & =\frac{arccsc 𝑥+arcsec 𝑥}{|𝑥|\sqrt{𝑥^{2}−1} arccsc ^{2}𝑥}.\end{aligned}


$$
