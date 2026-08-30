# Integrating Exponential Functions Using Substitution

Source: https://www.mathacademy.com/topics/3770?courseId=136
Topic ID: 3770

## Prerequisites

- [Integrating Exponential Functions Using Linear Substitution](./1112-integrating-exponential-functions-using-linear-substitution.md)

## Lesson

### Introduction

Suppose that we want to calculate $\displaystyle \int 2x e^{x^2}\,\textrm d x.$

Notice that if we let $u = x^2,$ then both $u$ and its derivative $u'=2x$ appear in the integrand:

$$


\int \underbrace{2x}_{u'} e^{\overbrace{x^2}^u}\,\textrm d x


$$

Integrals like this can always be solved using substitution.

Let $u=x^2.$ Differentiating gives

$$


\dfrac{\text{d} u}{\text{d}x } = 2x \quad\Longrightarrow\quad \textrm d u = 2x\,\textrm d x.


$$

We now substitute our expressions into the integral and evaluate it as follows:

$$


\begin{aligned}∫2𝑥𝑒^{𝑥^{2}}\,d𝑥 & =∫𝑒^{𝑥^{2}}\,\underset{d𝑢}{\underset{}{2𝑥\,d𝑥}} \\ & =∫𝑒^{𝑢}\,d𝑢 \\ & =𝑒^{𝑢}+𝐶 \\ & =𝑒^{𝑥^{2}}+𝐶\end{aligned}


$$

### Example: Integrating Products Containing the Exponential Function

#### Question

Calculate $\displaystyle{\int x^2 e^{x^3+1}\, \text{d}x}.$

#### Explanation

Let's introduce the new variable $u = x^3+1.$ Differentiating gives

$$


\dfrac{\text{d}u}{\text{d}x}= 3x^2\quad\Longrightarrow\quad\dfrac 1 3 \text{d}u = x^2 \, \text{d}x.


$$

Therefore,

$$


\begin{aligned}∫𝑥^{2}𝑒^{𝑥^{3}+1}\,d𝑥 & =∫𝑒^{𝑥^{3}+1}⋅\,𝑥^{2}\,d𝑥 \\ & =∫𝑒^{𝑢}⋅\frac{1}{3}\,d𝑢 \\ & =\frac{1}{3}∫𝑒^{𝑢}\,d𝑢 \\ & =\frac{1}{3}𝑒^{𝑢}+𝐶 \\ & =\frac{1}{3}𝑒^{𝑥^{3}+1}+𝐶.\end{aligned}


$$

### Example: Integrating Products Containing Other Exponential Functions

#### Question

Calculate $\displaystyle \int x^3\,{3^{1-x^4}} \, \text{d}x.$

#### Explanation

Let's introduce the new variable $u= 1-x^4.$ Differentiating gives

$$


\dfrac{ \text{d}u}{ \text{d}x} = -4x^3\quad\Longrightarrow\quad x^3 \, \text{d}x = -\dfrac{1}{4} \text{d}u.


$$

Therefore,

$$


\begin{aligned} \int {x^3\,{3^{1-x^4}} }\, \text{d}x &=\int {{3^{1-x^4}}\cdot x^3 }\, \text{d}x \\[5pt] &= \int {3^{u}} \cdot \left(-\dfrac{1}{4}\right) \text{d}u\\[5pt] &= -\dfrac{1}{4}\int {3^{u}} \text{d}u\\[5pt] &= -\dfrac{1}{4}\cdot\dfrac{3^{u}}{\ln 3} + C\\[5pt] &= -\dfrac{3^{1-x^4}}{4\ln 3}+ C. \end{aligned}


$$

### Example: More Complex Cases

#### Question

Calculate $\displaystyle \int \dfrac {e^{2x}} {e^{2x} + 1} \, \text{d}x.$

#### Explanation

Notice that the numerator is proportional to the derivative of the denominator. So, we introduce the new variable $u = e^{2x}+1.$ Differentiating gives

$$


\dfrac{\text{d}u}{\text{d}x}= 2e^{2x}\quad\Longrightarrow\quad \dfrac{1}{2}\, \text{d}u = e^{2x} \, \text{d}x.


$$

Therefore,

$$


\begin{aligned}∫\frac{𝑒^{2𝑥}}{𝑒^{2𝑥}+1}\,d𝑥 & =∫\frac{1}{𝑒^{2𝑥}+1}⋅𝑒^{2𝑥}\,d𝑥 \\ & =∫\frac{1}{𝑢}⋅\frac{1}{2}\,d𝑢 \\ & =\frac{1}{2}∫\frac{1}{𝑢}\,d𝑢 \\ & =\frac{1}{2}ln⁡|𝑢|+𝐶 \\ & =\frac{1}{2}ln⁡|𝑒^{2𝑥}+1|+𝐶 \\ & =\frac{1}{2}ln⁡(𝑒^{2𝑥}+1)+𝐶.\end{aligned}


$$

Notice that, in the last step, we used the fact that $e^{2x} + 1 > 0$ for all $x.$

### Definite Integrals

Let's evaluate the following definite integral:

$$


\displaystyle{\int_{0}^{3} xe^{x^{2}}\, \text{d}x}


$$

We'll use the change of variable method, which comprises three steps:

**Step1:** Change of variable in the integrand.

Let's introduce the new variable $u = x^2.$ Differentiating gives

$$


\dfrac{\text{d}u}{ \text{d}x} = 2x \qquad\Longrightarrow\qquad \dfrac{1}{2}\text{d}u = x \, \text{d}x.


$$

**Step 2:** Find the new limits of integration.

We create a table below to change our limits of integration from $x$ to $u{:}$

**Step 3:** Evaluate the integral in the new variable $u.$

$$


\begin{aligned}∫_{30}𝑥𝑒^{𝑥^{2}}\,d𝑥 & =∫_{30}𝑒^{𝑥^{2}}⋅𝑥\,d𝑥 \\ & =∫_{90}𝑒^{𝑢}⋅\frac{1}{2}\,d𝑢 \\ & =\frac{1}{2}∫_{90}𝑒^{𝑢}\,d𝑢 \\ & =\frac{1}{2}𝑒^{𝑢}\,_{90} \\ & =\frac{1}{2}(𝑒^{9}−𝑒^{0}) \\ & =\frac{𝑒^{9}−1}{2}.\end{aligned}


$$

### Example: Evaluating Definite Integrals

#### Question

Evaluate the integral $\displaystyle{\int_{0}^{\sqrt {\ln 4}} 16xe^{-2x^2}\, \text{d}x}$.

#### Explanation

Let's introduce the new variable $u=-2x^2.$ Differentiating gives

$$


\dfrac{\text{d}u}{\text{d}x}=-4x \qquad\Longrightarrow\qquad -4 \, \text{d}u=16x \, \text{d}x.


$$

Next, we determine the new limits of integration:

Therefore, we get

$$


\begin{aligned}∫_{\sqrt{ln⁡4}0}^{}16𝑥𝑒^{−2𝑥^{2}}\,d𝑥 & =∫_{\sqrt{ln⁡4}0}^{}𝑒^{−2𝑥^{2}}⋅16𝑥\,d𝑥 \\ & =∫_{−2ln⁡40}𝑒^{𝑢}⋅(−4\,d𝑢) \\ & =−4∫_{−2ln⁡40}𝑒^{𝑢}\,d𝑢 \\ & =−4𝑒^{𝑢}\,_{−2ln⁡40} \\ & =−4(𝑒^{−2ln⁡4}−𝑒^{0}) \\ & =−4(\frac{1}{16}−1) \\ & =4(\frac{15}{16}) \\ & =\frac{15}{4}.\end{aligned}


$$
