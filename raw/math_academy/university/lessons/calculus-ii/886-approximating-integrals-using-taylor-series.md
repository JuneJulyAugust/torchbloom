# Approximating Integrals Using Taylor Series

Source: https://www.mathacademy.com/topics/886?courseId=106
Topic ID: 886

## Prerequisites

- [Representing Functions as Power Series](./885-representing-functions-as-power-series.md)
- [The Sum and Constant Multiple Rules for Definite Integrals](../../../ap-courses/lessons/ap-calculus-ab/1685-the-sum-and-constant-multiple-rules-for-definite-integrals.md)

## Lesson

### Introduction

Consider the following integral:

$$


\int \cos \sqrt{x} \, \textrm dx\,


$$

Unfortunately, we cannot compute this integral using any of our standard methods. However, we *can* express this integral as an infinite series if we first write the integrand $\cos \sqrt{x}$ as a Maclaurin series.

Let's start with the Maclaurin series expansion of $\cos{x},$ valid for all $x\mathbin{:}$

$$


\cos{x} =1 - \frac{1}{2!}x^2 + \frac{1}{4!}x^4+\cdots \,.


$$

Replacing $x$ with $\sqrt{x}$ in the above equation, we find the series expansion for $\cos{\sqrt{x}}$ as follows:

$$


\begin{aligned}cos⁡\sqrt{√𝑥} & =1−\frac{1}{2!}(\sqrt{√𝑥})^{2}+\frac{1}{4!}(\sqrt{√𝑥})^{4}+⋯ \\ & =1−\frac{𝑥}{2}+\frac{𝑥^{2}}{24}+⋯\end{aligned}


$$

Integrating both sides of this equality, we get

$$


\begin{aligned}∫cos⁡\sqrt{√𝑥}\,d𝑥 & =∫(1−\frac{𝑥}{2}+\frac{𝑥^{2}}{24}+⋯)\,d𝑥 \\ & =∫1\,d𝑥−\frac{1}{2}∫𝑥\,d𝑥+\frac{1}{24}∫𝑥^{2}\,d𝑥+⋯ \\ & =𝐶+𝑥−\frac{1}{2}⋅\frac{𝑥^{2}}{2}+\frac{1}{24}⋅\frac{𝑥^{3}}{3}+⋯ \\ & =𝐶+𝑥−\frac{𝑥^{2}}{4}+\frac{𝑥^{3}}{72}+⋯\,.\end{aligned}


$$

And we're done! We've just found the Maclaurin series expression for $\displaystyle \int\cos{\sqrt{x}}\,\mathrm{d}x.$

We can apply the same method to any function $f(x)$ having a power series expansion of the form

$$


f(x)=a_0+a_1 x+a_2 x^2 + \cdots\,.


$$

Integrating the above, we get

$$


\begin{aligned}∫𝑓(𝑥)\,d𝑥 & =∫(𝑎_{0}+𝑎_{1}𝑥+𝑎_{2}𝑥^{2}+⋯)d𝑥 \\ & =𝑎_{0}∫\,d𝑥+𝑎_{1}∫𝑥\,d𝑥+𝑎_{2}∫𝑥^{2}\,d𝑥+⋯ \\ & =𝐶+𝑎_{0}𝑥+𝑎_{1}\frac{𝑥^{2}}{2}+𝑎_{2}\frac{𝑥^{3}}{3}+⋯.\end{aligned}


$$

This is valid for the same radius of convergence as the series expansion of $f(x).$

### Example: Computing Indefinite Integrals Using Taylor Series

#### Question

Starting with the standard Maclaurin result for $e^x,$ find the first three terms of the series expansion for $\displaystyle{\int e^{-x^2}\textrm{d}x}.$

#### Explanation

The series expansion of $e^{x}$ is

$$


\begin{aligned}𝑒^{𝑥} & =1+𝑥+\frac{1}{2!}𝑥^{2}+⋯.\end{aligned}


$$

Replacing $x$ with $-x^2$ in the above formula, we get

$$


\begin{aligned}𝑒^{−𝑥^{2}} & =1+(−𝑥^{2})+\frac{1}{2!}(−𝑥^{2})^{2}+⋯ \\ & =1−𝑥^{2}+\frac{1}{2}𝑥^{4}+⋯.\end{aligned}


$$

Finally, integrating with respect to $x,$ we get

$$


\begin{aligned}∫𝑒^{−𝑥^{2}}d𝑥 & =∫(1−𝑥^{2}+\frac{1}{2}𝑥^{4}+⋯)d𝑥 \\ & =𝐶+𝑥−\frac{1}{3}𝑥^{3}+\frac{1}{10}𝑥^{5}+⋯.\end{aligned}


$$

### Example: Computing Definite Integrals Using Taylor Series

#### Question

Using the standard form of the Maclaurin series of $\ln(1+x)$, find the first three non-zero terms of the series expansion of the definite integral

$$


\displaystyle{\int_0^{1/2}\ln(1-x^2)\text{d}x}.


$$

#### Explanation

The power series expansion of $\ln(1+x)$ is given by

$$


\begin{aligned}ln⁡(1+𝑥)=𝑥−\frac{1}{2}𝑥^{2}+\frac{1}{3}𝑥^{3}+⋯\,.\end{aligned}


$$

Replacing $x$ with $-x^2$ in the above, we get

$$


\begin{aligned}ln⁡(1−𝑥^{2}) & =(−𝑥^{2})−\frac{1}{2}(−𝑥^{2})^{2}+\frac{1}{3}(−𝑥^{2})^{3}+⋯ \\ & =−𝑥^{2}−\frac{1}{2}𝑥^{4}−\frac{1}{3}𝑥^{6}+⋯\,.\end{aligned}


$$

Finally, we calculate the definite integral, as follows:

$$


\begin{aligned}∫_{1/20}^{}ln⁡(1−𝑥^{2})d𝑥 & =∫(−𝑥^{2}−\frac{1}{2}𝑥^{4}−\frac{1}{3}𝑥^{6}+⋯)d𝑥 \\ & =(−\frac{𝑥^{3}}{3}−\frac{1}{2}⋅\frac{𝑥^{5}}{5}−\frac{1}{3}⋅\frac{𝑥^{7}}{7}+⋯)_{1/20}^{} \\ & =−\frac{1}{3⋅2^{3}}−\frac{1}{2⋅5⋅2^{5}}−\frac{1}{3⋅7⋅2^{7}} \\ & =−\frac{1}{24}−\frac{1}{320}−\frac{1}{2688}+⋯\,\end{aligned}


$$

**** We can get a numerical approximation by evaluating the first three terms. This gives

$$


\begin{aligned}∫_{1/20}^{}ln⁡(1−𝑥^{2})d𝑥 & ≈−\frac{1}{24}−\frac{1}{320}−\frac{1}{2688}=−0.04516\end{aligned}


$$

rounded to five decimal places.

The exact value of the integral, rounded to five decimal places, is

$$


\begin{aligned}∫_{1/20}^{}ln⁡(1−𝑥^{2})d𝑥 & =−0.04523\,.\end{aligned}


$$

So, our estimation was pretty good!
