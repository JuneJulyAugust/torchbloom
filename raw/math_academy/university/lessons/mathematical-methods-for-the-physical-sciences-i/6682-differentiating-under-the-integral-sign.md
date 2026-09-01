# Differentiating Under the Integral Sign

Source: https://www.mathacademy.com/topics/6682?courseId=154
Topic ID: 6682

## Prerequisites

- [The Sum and Constant Multiple Rules for Definite Integrals](../../../ap-courses/lessons/ap-calculus-ab/1685-the-sum-and-constant-multiple-rules-for-definite-integrals.md)
- [Partial Differentiability of Multivariable Functions](./1932-partial-differentiability-of-multivariable-functions.md)

## Lesson

### Introduction

Consider the integral

$$


I(t) = \int_{a}^{b} f(x,t)\,\mathrm{d}x,


$$

where $x$ is the integration variable and $t$ is a parameter. How do we compute $\dfrac{\mathrm{d} I}{\mathrm{d} t}$?

If $f(x,t)$ is continuous on $R = [a,b] \times [c,d]$ and $\dfrac{\partial f}{\partial t}$ exists and is continuous on $R,$ then the function

$$


I(t) = \int_{a}^b f(x,t)\,\mathrm{d} x


$$

is differentiable on $(c,d),$ and

$$


I'(t) = \dfrac{\mathrm{d}}{\mathrm{d} t}\int_{a}^b f(x,t)\,\mathrm{d} x = \int_{a}^b \dfrac{\partial f}{\partial t}(x,t)\,\mathrm{d} x.


$$

This is known as **differentiating under the integral sign**.

The integral represents the total area under the curve $y = f(x,t).$ Changing the parameter $t$ alters the height of the curve at each $x,$ but the interval $[a,b]$ remains fixed. Thus, the total change in area is obtained by summing (integrating) how each point changes.

For example, if

$$


I(t) = \int_{0}^{1} e^{-tx}\,\mathrm{d}x,


$$

then

$$


\begin{aligned}𝐼^{′}(𝑡) & =\frac{d}{d𝑡}∫_{10}𝑒^{−𝑡𝑥}\,d𝑥 \\ & =∫_{10}\frac{𝜕}{𝜕𝑡}(𝑒^{−𝑡𝑥})\,d𝑥 \\ & =∫_{10}−𝑥𝑒^{−𝑡𝑥}\,d𝑥.\end{aligned}


$$

We can then evaluate this integral using the usual methods. For the purposes of integration, we treat $t$ as a constant.

### A Worked Example

Now, given that

$$


\displaystyle I(t)=\int_{-1}^{1} (3x-t^2)^2\,\text{d}x,


$$

let's calculate $I'(t)$ for $t\in\mathbb{R}$ by *differentiating under the integral sign*.

Recall that if $f(x,t)$ is continuous on $R = [a,b]\times [c,d]$ and $\dfrac{\partial f}{\partial t}$ exists and is continuous on $R,$ then the function

$$


I(t) = \int_{a}^b f(x,t)\,\text{d} x


$$

is differentiable on $(c,d),$ and

$$


I'(t) = \dfrac{\textrm d}{\textrm d t}\int_{a}^b f(x,t)\,\text{d} x = \int_{a}^b \dfrac{\partial f}{\partial t}(x,t)\,\text{d} x.


$$

We wish to compute $I'(t),$ where

$$


I(t)=\int_{-1}^{1} (3x-t^2)^2\,\text{d}x.


$$

Differentiating under the integral sign, we get

$$


I'(t) = \int_{-1}^{1} \frac{\partial}{\partial t}\Bigl[(3x-t^2)^2\Bigr]\,\text{d}x.


$$

Next, let's compute the partial derivative with respect to $t$:

$$


\begin{aligned}\frac{𝜕}{𝜕𝑡}[(3𝑥−𝑡^{2})^{2}] & =2(3𝑥−𝑡^{2})⋅\frac{𝜕}{𝜕𝑡}(3𝑥−𝑡^{2}) \\ & =2(3𝑥−𝑡^{2})⋅(−2𝑡) \\ & =−4𝑡(3𝑥−𝑡^{2}).\end{aligned}


$$

Substituting this back into our integral, we get

$$


\begin{aligned}𝐼^{′}(𝑡) & =∫_{1−1}−4𝑡(3𝑥−𝑡^{2})\,d𝑥 \\ & =−4𝑡∫_{1−1}(3𝑥−𝑡^{2})\,d𝑥.\end{aligned}


$$

Finally, let's evaluate the remaining integral:

$$


\begin{aligned}∫_{1−1}(3𝑥−𝑡^{2})\,d𝑥 & =∫_{1−1}3𝑥\,d𝑥−∫_{1−1}𝑡^{2}\,d𝑥 \\ & =\frac{3𝑥^{2}}{2}_{1−1}−𝑡^{2}𝑥_{1−1} \\ & =0−2𝑡^{2} \\ & =−2𝑡^{2}.\end{aligned}


$$

Therefore,

$$


\begin{aligned}𝐼^{′}(𝑡) & =−4𝑡(−2𝑡^{2}) \\ & =8𝑡^{3}.\end{aligned}


$$

### Example: Differentiating Under the Integral Sign

#### Question

Given that $\displaystyle J(t)=\int_{0}^{1} (\cos t+2x)^2\, \text{d}x,$ calculate $J'(t)$ for $t\in\mathbb R$ by differentiating under the integral sign.

#### Explanation

Suppose $f(x,t)$ is continuous on $R = [a,b]\times [c,d]$ and $\dfrac{\partial f}{\partial t}$ exists and is continuous on $R.$ Then, the function

$$


F(t) = \int_{a}^b f(x,t)\,\text{d} x


$$

is differentiable on $(c,d),$ and

$$


F'(t) = \dfrac{\textrm d}{\textrm d t}\int_{a}^b f(x,t)\,\text{d} x = \int_{a}^b \dfrac{\partial f}{\partial t}(x,t)\,\text{d} x.


$$

This is known as differentiating under the integral sign.

We wish to compute $J'(t),$ where

$$


J(t)=\int_{0}^{1} (\cos t+2x)^2\, \text{d}x.


$$

Differentiating under the integral sign, we get

$$


J'(t) = \int_{0}^{1} \frac{\partial}{\partial t}\Bigl[(\cos t+2x)^2\Bigr]\,\text{d}x.


$$

Next, let's compute the partial derivative with respect to $t$:

$$


\begin{aligned}\frac{𝜕}{𝜕𝑡}[(cos⁡𝑡+2𝑥)^{2}] & =2(cos⁡𝑡+2𝑥)⋅\frac{𝜕}{𝜕𝑡}(cos⁡𝑡+2𝑥) \\ & =2(cos⁡𝑡+2𝑥)⋅(−sin⁡𝑡) \\ & =−2(cos⁡𝑡+2𝑥)sin⁡𝑡\end{aligned}


$$

Substituting this back into our integral, we get

$$


\begin{aligned}𝐽^{′}(𝑡) & =∫_{10}−2(cos⁡𝑡+2𝑥)sin⁡𝑡\,d𝑥 \\ & =−2sin⁡𝑡∫_{10}(cos⁡𝑡+2𝑥)\,d𝑥.\end{aligned}


$$

Finally, let's evaluate the remaining integral:

$$


\begin{aligned}∫_{10}(cos⁡𝑡+2𝑥)\,d𝑥 & =cos⁡𝑡⋅𝑥_{10}+𝑥^{2}_{10} \\ & =cos⁡𝑡+1\end{aligned}


$$

Therefore,

$$


J'(t) =-2\sin t\,(\cos t+1).


$$

### Checking the Conditions

Consider the function

$$


F(t) = \int_{a}^b f(x,t)\,\text{d} x, \qquad t \in [c,d].


$$

Then, *differentiation under the integral sign* applies, meaning

$$


F'(t) = \int_{a}^b \frac{\partial f}{\partial t}(x,t)\,\text{d} x,


$$

provided the following conditions are met:

- $f(x,t)$ is continuous on $R = [a,b] \times [c,d],$ and

- $\dfrac{\partial f}{\partial t}$ exists and is continuous on $R.$

For example, suppose we wish to compute $I'(t),$ where

$$


I(t)=\int_{0}^{1} (2x+t^3)^2 \, \text{d}x, \qquad t \in [0,5].


$$

We may differentiate under the integral sign provided that the function $f(x,t) = (2x+t^3)^2$ fits the necessary criteria. Let's check.

Fix $t_0 \in (0,5)$ and choose $c < t_0 < d$ such that $[c,d] \subseteq [0,5],$ so $R = [0,1] \times [c,d].$

- Notice that $f(x,t) = (2x+t^3)^2$ is continuous on $R.$

- Computing the partial derivative, we have which exists and is continuous on $R.$

Thus, the operation is valid. We obtain

$$


I'(t) = \int_{0}^{1} 6(2x+t^3)t^2 \, \text{d}x.


$$

### Example: Identifying Cases Where Differentiating Under the Integral Sign Applies

#### Question

For which of the following functions is it valid to differentiate under the integral sign?

1. $\displaystyle F_1(t) = \int_0^1 t\cos x\,\text{d} x, \quad t \in \mathbb R$

2. $\displaystyle F_2(t) = \int_0^1 \dfrac{1}{\sqrt{|x - t|}}\,\text{d} x, \quad t \in (0,1)$

3. $\displaystyle F_3(t) = \int_0^1 \dfrac{1}{1 + (x - t)^2}\,\text{d} x, \quad t \in [0,1]$

#### Explanation

Suppose $f(x,t)$ is continuous on $R = [a,b]\times [c,d]$ and $\dfrac{\partial f}{\partial t}$ exists and is continuous on $R.$ Then, the function

$$


F(t) = \int_{a}^b f(x,t)\,\text{d} x


$$

is differentiable on $(c,d),$ and

$$


F'(t) = \dfrac{\textrm d}{\textrm d t}\int_{a}^b f(x,t)\,\text{d} x = \int_{a}^b \dfrac{\partial f}{\partial t}(x,t)\,\text{d} x.


$$

This is known as **

With that in mind, let's check each function:

- For the first function, we have We fix $t_0 \in \mathbb R$ and choose $c < t_0 < d$ such that $[c,d] \subseteq \mathbb R,$ so $R = [0,1] \times [c,d].$ Note that $f_1$ is continuous on $R.$ Computing the partial derivative, we have which exists and is continuous on $R.$ Thus, differentiating under the integral sign is valid at $t_0.$ And since our choice of $t_0$ was arbitrary, we can compute $F'_1(t)$ for all real $t.$

- For the second function, we have We fix $t_0 \in (0,1)$ and choose $c < t_0 < d$ such that $[c,d] \subseteq (0,1),$ so $R = [0,1] \times [c,d].$ Note that $f_2$ is undefined when $x = t,$ since the denominator vanishes. Thus, $f_2$ is not continuous on $R,$ and differentiating under the integral sign is ** valid.

- For the third function, we have We fix $t_0 \in (0,1)$ and choose $c < t_0 < d$ such that $[c,d] \subseteq [0,1],$ so $R = [0,1] \times [c,d].$ Note that $f_3$ is continuous on $R.$ Computing the partial derivative, we have which exists and is continuous on $R.$ Thus, differentiating under the integral sign is valid at $t_0.$ And since our choice of $t_0$ was arbitrary, we can compute $F'_3(t)$ for all $t \in [0,1].$

Therefore, the correct answer is "I and III only."
