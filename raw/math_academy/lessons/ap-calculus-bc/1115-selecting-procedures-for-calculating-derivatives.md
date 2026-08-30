# Selecting Procedures for Calculating Derivatives

Source: https://www.mathacademy.com/topics/1115?courseId=21
Topic ID: 1115

## Prerequisites

- [The Chain Rule With Trigonometric Functions](../ap-calculus-ab/305-the-chain-rule-with-trigonometric-functions.md)
- [The Chain Rule With Exponential Functions](../ap-calculus-ab/1007-the-chain-rule-with-exponential-functions.md)
- [The Chain Rule With Logarithmic Functions](../ap-calculus-ab/1036-the-chain-rule-with-logarithmic-functions.md)

## Lesson

### Introduction

Sometimes, we need to combine multiple rules of differentiation to differentiate a given function. As a reminder, the product rule, quotient rule, and chain rule are stated below.

- Product rule: $\hspace{.5cm} \dfrac{\mathrm{d}}{\mathrm{d}x} \left[u(x) \cdot v(x) \right] = u'(x) \cdot v(x) + u(x) \cdot v'(x)$

- Quotient rule: $\hspace{.5cm} \dfrac{\mathrm{d}}{\mathrm{d}x} \left[\dfrac{u(x)}{v(x)} \right] = \dfrac{u'(x)\cdot v(x) - u(x)\cdot v'(x)}{[v(x)]^2}$

- Chain rule: $\hspace{.5cm} \dfrac{\mathrm{d}}{\mathrm{d}x} \left[u(v(x)) \right] = u'(v(x))\cdot v'(x)$

### Example: Calculating a Derivative Using Multiple Instances of the Chain Rule

#### Question

Differentiate $y = \cos^4{2x}.$

#### Explanation

First, we express $y$ as a composite function

$$


y = u^4, \qquad u = \cos{v}, \qquad v = 2x.


$$

Differentiating gives

$$


\dfrac{\textrm d y}{\textrm d u} = 4u^3,\qquad \dfrac{\textrm{d}u}{\textrm d v} = -\sin{v},\qquad \dfrac{\textrm{d}v}{\textrm d x} = 2.


$$

Applying now the chain rule twice, we get

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =\frac{d𝑦}{d𝑢}⋅\frac{d𝑢}{d𝑥} \\ & =\frac{d𝑦}{d𝑢}⋅\frac{d𝑢}{d𝑣}⋅\frac{d𝑣}{d𝑥} \\ & =4𝑢^{3}⋅(−sin⁡𝑣)⋅(2) \\ & =4(cos⁡2𝑥)^{3}⋅(−sin⁡2𝑥)⋅(2) \\ & =−8cos^{3}⁡2𝑥sin⁡2𝑥.\end{aligned}


$$

### Example: Calculating a Derivative Using the Chain and Product Rules

#### Question

If $f(x) = e^{-2x}\tan({x^2})$, then what is $f'(x)?$

#### Explanation

This question requires the product rule. Let $u(x) = e^{-2x}$ and $v(x)=\tan{(x^2)}.$ Then

$$


u'(x) = -2e^{-2x}, \qquad v'(x) = 2x\sec^2(x^2).


$$

Note that we used the chain rule to differentiate both $u$ and $v.$

Now, applying the product rule and simplifying, we have

$$


\begin{aligned}𝑓^{′}(𝑥) & =𝑢^{′}(𝑥)⋅𝑣(𝑥)+𝑢(𝑥)⋅𝑣^{′}(𝑥) \\ & =(−2𝑒^{−2𝑥})⋅tan⁡(𝑥^{2})+𝑒^{−2𝑥}⋅2𝑥sec^{2}⁡(𝑥^{2}) \\ & =2𝑒^{−2𝑥}(−tan⁡(𝑥^{2})+𝑥sec^{2}⁡(𝑥^{2})) \\ & =2𝑒^{−2𝑥}(𝑥sec^{2}⁡(𝑥^{2})−tan⁡(𝑥^{2})).\end{aligned}


$$

### Example: Calculating a Derivative Using the Chain and Quotient Rules

#### Question

Given that $y =\dfrac{e^{3x}}{2^{x}+1},$ find $\dfrac{\textrm{d}y}{\textrm{d}x}.$

#### Explanation

We use the quotient rule with the numerator $u(x)=e^{3x}$ and the denominator $v(x)=2^x +1.$

Differentiating $u(x)$ and $v(x),$ we have

$$


u'(x) = 3e^{3x}, \qquad v'(x) = 2^x \ln 2.


$$

Note that we used the chain rule to differentiate $u.$

Now, applying the quotient rule and simplifying, we have

$$


\begin{aligned} \dfrac{\textrm{d}y}{\textrm{d}x} &= \dfrac{u'(x)\cdot v(x) - u(x)\cdot v'(x)}{[v(x)]^2} \\\[5pt] &=\dfrac{3e^{3x} \cdot \left( 2^{x}+1\right) - e^{3x} \cdot \left(2^x \cdot \ln2\right)}{\left(2^{ x}+1 \right)^2}\\\[5pt] &=\dfrac{3e^{3x}2^{x} + 3e^{3x} - e^{3x}2^{x}\ln 2}{\left(2^{ x}+1 \right)^2}\\\[5pt] &=\dfrac{e^{3x} \left( 3(2^{x}) - 2^{x} \ln 2 +3\right)}{\left(2^{x}+1 \right)^2} \end{aligned}


$$
