# The Sum and Constant Multiple Rules for Differentiation

Source: https://www.mathacademy.com/topics/278?courseId=105
Topic ID: 278

## Prerequisites

- [The Power Rule for Differentiation](./35-the-power-rule-for-differentiation.md)

## Lesson

### Introduction

The **constant multiple rule** states that if a function $f(x)$ is multiplied by a *constant* factor $k,$ then in order to differentiate $kf(x)$ we can take the derivative of $f(x)$ and then multiply by $k$ afterwards:

$$


\dfrac{\textrm d}{\textrm d x}\left(k f(x)\right) = k \dfrac{\textrm d}{\textrm d x}\left(f(x)\right)


$$

For example, to differentiate $y=6x^2$, we compute

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =\frac{d}{d𝑥}(6𝑥^{2}) \\ & =6⋅\frac{d}{d𝑥}(𝑥^{2}) \\ & =6⋅2𝑥 \\ & =12𝑥.\end{aligned}


$$

### Example: Differentiating a Power Function Using the Constant Multiple Rule

#### Question

Find the derivative of $f(x) = 6x^3.$

#### Explanation

We apply the constant multiple and power rules, as follows:

$$


\begin{aligned}𝑓^{′}(𝑥) & =\frac{d}{d𝑥}(6𝑥^{3}) \\ & =6⋅\frac{d}{d𝑥}(𝑥^{3}) \\ & =6⋅3𝑥^{2} \\ & =18𝑥^{2}\end{aligned}


$$

### Example: Differentiating a Negative Power Function Using the Constant Multiple Rule

#### Question

If $y=-\dfrac{3}{\sqrt{x}}$, find $\dfrac{\textrm d y}{\textrm d x}.$

#### Explanation

We first rewrite the function as

$$


y = -\dfrac{3}{\sqrt{x}} = -\dfrac{3}{x^{1/2}} = -3x^{-1/2}.


$$

Then, we apply the constant multiple and power rules:

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =\frac{d}{d𝑥}(−3𝑥^{−1/2}) \\ & =−3⋅\frac{d}{d𝑥}(𝑥^{−1/2}) \\ & =−3⋅(−\frac{1}{2})𝑥^{−3/2} \\ & =\frac{3}{2}𝑥^{−3/2} \\ & =\frac{3}{2\sqrt{𝑥^{3}}}\end{aligned}


$$

### The Sum Rule for Differentiation

The **sum rule** states that to differentiate the sum of two functions, we can take the sum of their respective derivatives:

$$


\dfrac{\textrm d }{\textrm d x}( u(x) + v(x) ) = \dfrac{\textrm d u}{\textrm d x} + \dfrac{\textrm d v}{\textrm d x}


$$

The sum rule also applies to differences:

$$


\dfrac{\textrm d }{\textrm d x}( u(x) - v(x) ) = \dfrac{\textrm d u}{\textrm d x} - \dfrac{\textrm d v}{\textrm d x}


$$

As an example, let's calculate the derivative of the function $y = x^2 + x.$ We can apply the sum rule to find $\dfrac{\textrm d y}{\textrm d x}$ as follows:

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =\frac{d}{d𝑥}(𝑥^{2}+𝑥) \\ & =\frac{d}{d𝑥}(𝑥^{2})+\frac{d}{d𝑥}(𝑥) \\ & =2𝑥+1.\end{aligned}


$$

### Example: Differentiating a Sum of Functions Without Constant Factors Using the Sum Rule

#### Question

Find $f'(x)$ for $f(x) = x^4 -\dfrac{1}{x^2} + x.$

#### Explanation

The function $f(x)$ is the sum of three power functions. So, we apply the sum rule, and we get

$$


\begin{aligned}𝑓^{′}(𝑥) & =\frac{d}{d𝑥}(𝑥^{4}−\frac{1}{𝑥^{2}}+𝑥) \\ & =\frac{d}{d𝑥}(𝑥^{4}−𝑥^{−2}+𝑥) \\ & =\frac{d}{d𝑥}(𝑥^{4})−\frac{d}{d𝑥}(𝑥^{−2})+\frac{d}{d𝑥}(𝑥) \\ & =4𝑥^{3}−(−2)𝑥^{−3}+1 \\ & =4𝑥^{3}+2𝑥^{−3}+1 \\ & =4𝑥^{3}+\frac{2}{𝑥^{3}}+1.\end{aligned}


$$

### Example: Differentiating a Sum of Functions With Constant Factors

#### Question

Calculate $\dfrac {\text{d}y} {\text{d}x}$ for $y= 2x^3 + 6\sqrt x.$

#### Explanation

Here, we convert the radical into a rational exponent, and we apply the addition, constant multiple, and power rules:

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =\frac{d}{d𝑥}(2𝑥^{3}+6𝑥^{1/2}) \\ & =\frac{d}{d𝑥}(2𝑥^{3})+\frac{d}{d𝑥}(6𝑥^{1/2}) \\ & =2⋅\frac{d}{d𝑥}(𝑥^{3})+6⋅\frac{d}{d𝑥}(𝑥^{1/2}) \\ & =2⋅3𝑥^{(3−1)}+6⋅\frac{1}{2}⋅𝑥^{(1/2−1)} \\ & =6𝑥^{2}+3⋅𝑥^{−1/2} \\ & =6𝑥^{2}+\frac{3}{\sqrt{𝑥}}\end{aligned}


$$
