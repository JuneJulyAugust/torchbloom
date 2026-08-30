# Integration by Substitution With Inverse Reciprocal Hyperbolic Functions

Source: https://www.mathacademy.com/topics/3259?courseId=106
Topic ID: 3259

## Prerequisites

- [Integration Using Inverse Reciprocal Hyperbolic Functions](../calculus-i/3256-integration-using-inverse-reciprocal-hyperbolic-functions.md)
- [Integration by Substitution With Inverse Hyperbolic Functions](./3258-integration-by-substitution-with-inverse-hyperbolic-functions.md)

## Lesson

### Introduction

Consider the integral

$$


\displaystyle \int \dfrac{1}{6x\sqrt{1-36x^2}} \, \textrm{d}x


$$

As it is, this integral doesn't resemble any of the basic integrals we have encountered so far. However, we can rewrite our integral as

$$


\int \dfrac{1}{6x\sqrt{1-36x^2}}\,\textrm{d}x = \int \dfrac{1}{(6x)\sqrt{1-\left(6x\right)^2}}\textrm{d}x,


$$

which becomes very similar to the basic integral for the inverse hyperbolic secant, $\newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits}$

$$


\int \frac{1}{u\sqrt{1-u^2}}\,\textrm{d}u = -\arsech u+C.


$$

The only difference is that instead of $u$ as the variable, we have $6x.$

So, let's substitute $u =6x.$ Differentiating, we get

$$


\dfrac{\textrm{d}u}{\textrm{d}x}=6 \quad\Longrightarrow\quad \textrm{d}x = \dfrac{1}{6} \,\textrm{d}u.


$$

Using the above, we can write the integral in terms of $u$ and compute it, as follows:

$$


\begin{aligned}\begin{aligned}∫\frac{1}{6𝑥\sqrt{√1−36𝑥^{2}}}\,d𝑥 & =∫\frac{1}{6𝑥\sqrt{√1−(6𝑥)^{2}}}\,d𝑥 \\ & =∫\frac{1}{𝑢\sqrt{√1−𝑢^{2}}}\,⋅\frac{1}{6}d𝑢 \\ & =\frac{1}{6}∫\frac{1}{𝑢\sqrt{√1−𝑢^{2}}}\,d𝑢 \\ & =−\frac{1}{6}arsech⁡𝑢+𝐶 \\ & =−\frac{1}{6}arsech⁡(6𝑥)+𝐶\end{aligned}\end{aligned}


$$

### Example: Calculating Indefinite Integrals Using Substitution With Inverse Hyperbolic Cosecant

#### Question

$\newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits}$

$\displaystyle \int \dfrac{1}{|3x|\sqrt{1+9x^2}} \, \textrm{d}x =$

#### Explanation

$\newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits}$

This integral resembles the basic integral for inverse hyperbolic cosecant,

$$


\int \frac{1}{|u|\sqrt{1+u^2}}\,\textrm{d}u = -\arcsch u+C.


$$

The only difference is that instead of $u^2$ as the variable, we have $9x^2 = (3x)^2.$

So, let's substitute $u =3x.$ Differentiating, we get

$$


\dfrac{\textrm{d}u}{\textrm{d}x}=3 \quad\Longrightarrow\quad \textrm{d}x = \dfrac{1}{3} \,\textrm{d}u.


$$

Using the above, we can write the integral in terms of $u$ and compute it, as follows:

$$


\begin{aligned}\begin{aligned}∫\frac{1}{|3𝑥|\sqrt{√1+9𝑥^{2}}}\,d𝑥 & =∫\frac{1}{|3𝑥|\sqrt{√1+(3𝑥)^{2}}}\,d𝑥 \\ & =∫\frac{1}{|𝑢|\sqrt{√1+𝑢^{2}}}\,⋅\frac{1}{3}\,d𝑢 \\ & =\frac{1}{3}∫\frac{1}{|𝑢|\sqrt{√1+𝑢^{2}}}\,d𝑢 \\ & =−\frac{1}{3}arcsch⁡𝑢+𝐶 \\ & =−\frac{1}{3}arcsch⁡3𝑥+𝐶\end{aligned}\end{aligned}


$$

### Example: Calculating Indefinite Integrals Using Substitution With Inverse Hyperbolic Secant

#### Question

$\newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits}$

$\displaystyle \int \dfrac{1}{x\sqrt{4-x^2}} \,\textrm{d}x =$

#### Explanation

$\newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits}$

Let's rewrite our integral as

$$


\int \dfrac{1}{x\sqrt{4-x^2}}\,\textrm{d}x = \dfrac{1}{2} \int \dfrac{1}{x\sqrt{1-\left(\frac{x}{2}\right)^2}} \, \textrm{d}x=\dfrac{1}{4} \int \dfrac{1}{\frac{x}{2}\sqrt{1-\left(\frac{x}{2}\right)^2}} \, \textrm{d}x.


$$

This integral resembles the basic integral for the inverse hyperbolic secant,

$$


\int \frac{1}{u\sqrt{1-u^2}}\,\textrm{d}u = -\arsech u+C.


$$

The only difference is that instead of $u^2$ as the variable, we have $\left(\dfrac{x}{2}\right)^2.$

So, let's substitute $u = \dfrac x 2.$ Differentiating, we get

$$


\dfrac{\textrm{d}u}{\textrm{d}x}= \dfrac{1}{2} \quad\Longrightarrow\quad \textrm{d}x =2\,\textrm{d}u.


$$

Using the above, we can write the integral in terms of $u$ and compute it, as follows:

$$


\begin{aligned}\begin{aligned}∫\frac{1}{\sqrt{√4−𝑥^{2}}}\,d𝑥 & =\frac{1}{4}∫\frac{1}{\frac{𝑥}{2}\sqrt{√1−(\frac{𝑥}{2})^{2}}}\,d𝑥 \\ & =\frac{1}{4}∫\frac{1}{𝑢\sqrt{√1−𝑢^{2}}}⋅2\,d𝑢 \\ & =\frac{1}{2}∫\frac{d𝑢}{𝑢\sqrt{√1−𝑢^{2}}} \\ & =−\frac{1}{2}arsech⁡𝑢+𝐶 \\ & =−\frac{1}{2}arsech⁡(\frac{𝑥}{2})+𝐶\end{aligned}\end{aligned}


$$

### Example: Calculating Indefinite Integrals Using Substitution With Inverse Hyperbolic Cotangent

#### Question

$\newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits}$

$\displaystyle \int \dfrac{5}{1 - 4x^2} \, \textrm{d}x =$

#### Explanation

$\newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits}$

This integral resembles the basic integral for the inverse hyperbolic cotangent,

$$


\int \frac{1}{1-u^2}\, \textrm{d}u =\arcoth u +C.


$$

The only difference is that instead of $u^2$ as the variable, we have $4x^2 = \left(2x\right)^2.$

So, let's substitute $u=2x.$ Differentiating, we get

$$


\dfrac{\textrm{d}u}{\textrm{d}x}=2\quad\Longrightarrow\quad \dfrac 1 2\,\textrm d u = \textrm d x.


$$

Using the above, we can write the integral in terms of $u$ and compute, as follows:

$$


\begin{aligned}\begin{aligned}∫\frac{5}{1−4𝑥^{2}}\,d𝑥 & =5∫\frac{1}{1−(2𝑥)^{2}}\,d𝑥 \\ & =5∫\frac{1}{1−𝑢^{2}}\,⋅\frac{1}{2}\,d𝑢 \\ & =\frac{5}{2}∫\frac{1}{1−𝑢^{2}}\,d𝑢 \\ & =\frac{5}{2}arcoth⁡𝑢+𝐶 \\ & =\frac{5}{2}arcoth⁡2𝑥+𝐶\end{aligned}\end{aligned}


$$

Note that this result is subject to the condition $\left|2x \right| > 1.$

### Example: Calculating Definite Integrals Using Substitution With Inverse Reciprocal Hyperbolic Functions

#### Question

$\newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits}$

Evaluate the integral $\displaystyle{\int_{1/9}^{1/6} \dfrac{1}{x\sqrt{1-9x^2}}\, \textrm{d}x}.$

#### Explanation

$\newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits}$

Note that we can rewrite this integral as

$$


\int_{1/9}^{1/6} \dfrac{1}{x\sqrt{1-9x^2}} \, \textrm{d}x = 3\int_{1/9}^{1/6} \dfrac{1}{3x\sqrt{1-9x^2}}\, \textrm{d}x.


$$

This integral resembles the basic integral for the inverse hyperbolic secant,

$$


\int \frac{1}{u\sqrt{1-u^2}} \, \textrm{d}u =-\arsech u +C.


$$

The only difference is that instead of $u^2$ as the variable, we have $9x^2 = \left(3x\right)^2.$

So, let's substitute $u=3x.$ Differentiating, we get

$$


\dfrac{\textrm{d}u}{\textrm{d}x}= 3 \quad\Longrightarrow\quad \textrm{d}x =\dfrac{1}{3}\,\textrm{d}u.


$$

Before substituting, we use the table below to change the limits from $x$ to $u.$

Using the above, we can now write the integral in terms of $u$ and compute it, as follows:

$$


\begin{aligned} \int_{1/9}^{1/6} \dfrac{1}{x\sqrt{1 - 9x^2}}\, \textrm{d}x &= 3 \int_{1/9}^{1/6 } \dfrac{1}{3x\sqrt{1 - \left(3x\right)^2}}\, \textrm{d}x \\\[5pt] &= 3 \int_{1/3}^{1/2} \dfrac{1}{u\sqrt{1 - u^2}}\, \cdot \dfrac{1}{3}\,\textrm{d}u \\\[5pt] &= \int_{1/3}^{1/2} \dfrac{\textrm{d}u}{u \sqrt{1-u^2}} \\\[5pt] & = - \arsech{u}\Big|_{1/3}^{1/2}\\\[5pt] &= -\left(\arsech\left(\dfrac{1}{2}\right) - \arsech\left(\dfrac{1}{3}\right) \right)\\\[5pt] &= \arsech\left(\dfrac{1}{3}\right) - \arsech\left(\dfrac{1}{2}\right) \end{aligned}


$$
