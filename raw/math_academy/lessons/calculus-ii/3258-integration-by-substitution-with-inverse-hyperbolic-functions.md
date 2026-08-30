# Integration by Substitution With Inverse Hyperbolic Functions

Source: https://www.mathacademy.com/topics/3258?courseId=106
Topic ID: 3258

## Prerequisites

- [Integration by Substitution With Inverse Trigonometric Functions](./315-integration-by-substitution-with-inverse-trigonometric-functions.md)
- [Integration Using Inverse Hyperbolic Functions](../calculus-i/3253-integration-using-inverse-hyperbolic-functions.md)

## Lesson

### Introduction

Consider the integral $\newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits}$

$$


\displaystyle \int \dfrac{2}{\sqrt{4x^2-1}} \, \textrm{d}x.


$$

As it is, this integral doesn't resemble any of the basic integrals we have encountered so far. However, we can rewrite our integral as

$$


\int \dfrac{2}{\sqrt{4x^2-1}}\,\textrm{d}x = 2 \int \dfrac{1}{\sqrt{\left(2x\right)^2-1}}\textrm{d}x,


$$

which becomes very similar to the basic integral for the inverse hyperbolic cosine,

$$


\int \frac{1}{\sqrt{u^2-1}}\,\textrm{d}u = \arcosh u+C.


$$

The only difference is that instead of $u$ as the variable, we have $2x.$

So, let $u=2x.$ Differentiating, we have

$$


\dfrac{\textrm{d}u}{\textrm{d}x}=2 \quad\Longrightarrow\quad \textrm{d}x = \dfrac{1}{2} \,\textrm{d}u.


$$

Using the above, we can write the integral in terms of $u$ and compute it, as follows:

$$


\begin{aligned}\begin{aligned}∫\frac{2}{\sqrt{√4𝑥^{2}−1}}\,d𝑥 & =2∫\frac{1}{\sqrt{√(2𝑥)^{2}−1}}\,d𝑥 \\ & =2∫\frac{1}{\sqrt{√𝑢^{2}−1}}\,⋅\frac{1}{2}\,d𝑢 \\ & =∫\frac{1}{\sqrt{√𝑢^{2}−1}}\,d𝑢 \\ & =arcosh⁡𝑢+𝐶 \\ & =arcosh⁡(2𝑥)+𝐶\end{aligned}\end{aligned}


$$

### Example: Calculating Indefinite Integrals Using Substitution With Inverse Hyperbolic Sine

#### Question

$\newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits} \displaystyle \int \dfrac{\pi}{\sqrt{2x^2+1}} \, \textrm{d}x=$

#### Explanation

$\newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits}$

This integral resembles the basic integral for the inverse hyperbolic sine,

$$


\int \frac{1}{\sqrt{u^2+1}}\,\textrm{d}u = \arsinh u+C.


$$

The only difference is that instead of $u^2$ as the variable, we have $2x^2 = \left(\sqrt{2}\,x\right)^2.$

So, let's substitute $u =\sqrt{2}\,x.$ Differentiating, we get

$$


\dfrac{\textrm{d}u}{\textrm{d}x}=\sqrt{2} \quad\Longrightarrow\quad \textrm{d}x = \dfrac{1}{\sqrt{2}} \,\textrm{d}u.


$$

Using the above, we can write the integral in terms of $u$ and compute it, as follows:

$$


\begin{aligned}\begin{aligned}∫\frac{𝜋}{\sqrt{√2𝑥^{2}+1}}\,d𝑥 & =∫\frac{𝜋}{\sqrt{√(\sqrt{√2}\,𝑥)^{2}+1}}\,d𝑥 \\ & =𝜋∫\frac{1}{\sqrt{√𝑢^{2}+1}}\,⋅(\frac{1}{\sqrt{√2}}\,d𝑢) \\ & =\frac{𝜋}{\sqrt{√2}}∫\frac{1}{\sqrt{√𝑢^{2}+1}}\,d𝑢 \\ & =\frac{𝜋}{\sqrt{√2}}arsinh⁡𝑢+𝐶 \\ & =\frac{𝜋}{\sqrt{√2}}arsinh⁡(\sqrt{√2}\,𝑥)+𝐶\end{aligned}\end{aligned}


$$

### Example: Calculating Indefinite Integrals Using Substitution With Inverse Hyperbolic Cosine

#### Question

$\newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits}$

$\displaystyle \int \dfrac{3}{\sqrt{x^2-4}} \,\textrm{d}x =$

#### Explanation

$\newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits}$

Let's rewrite our integral as

$$


\int \dfrac{3}{\sqrt{x^2-4}}\,\textrm{d}x = \dfrac{3}{2} \int \dfrac{1}{\sqrt{\left(\frac{x}{2}\right)^2-1}} \, \textrm{d}x.


$$

This integral resembles the basic integral for the inverse hyperbolic cosine,

$$


\int \frac{1}{\sqrt{u^2-1}}\,\textrm{d}u = \arcosh u+C.


$$

The only difference is that instead of $u^2$ as the variable, we have $\left(\dfrac{x}{2}\right)^2.$

So, let's substitute $u = \dfrac x 2.$ Differentiating, we get

$$


\dfrac{\textrm{d}u}{\textrm{d}x}= \dfrac{1}{2} \quad\Longrightarrow\quad \textrm{d}x =2\,\textrm{d}u.


$$

Using the above, we can write the integral in terms of $u$ and evaluate it, as follows:

$$


\begin{aligned}\begin{aligned}∫\frac{3}{\sqrt{√𝑥^{2}−4}}\,d𝑥 & =\frac{3}{2}∫\frac{1}{\sqrt{√(\frac{𝑥}{2})^{2}−1}}\,d𝑥 \\ & =\frac{3}{2}∫\frac{1}{\sqrt{√𝑢^{2}−1}}⋅2\,d𝑢 \\ & =3∫\frac{d𝑢}{\sqrt{√𝑢^{2}−1}} \\ & =3arcosh⁡𝑢+𝐶 \\ & =3arcosh⁡(\frac{𝑥}{2})+𝐶\end{aligned}\end{aligned}


$$

### Example: Calculating Indefinite Integrals Using Substitution With Inverse Hyperbolic Tangent

#### Question

$\newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits}$

$\displaystyle \int \dfrac{10}{1 - 4x^2} \, \textrm{d}x =$

#### Explanation

$\newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits}$

This integral resembles the basic integral for the inverse hyperbolic tangent,

$$


\int \frac{1}{1-u^2} \, \textrm{d}u =\artanh u +C.


$$

The only difference is that instead of $u^2$ as the variable, we have $4x^2 = \left(2x\right)^2.$

So, let's substitute $u=2x.$ Differentiating, we get

$$


\dfrac{\textrm{d}u}{\textrm{d}x}=2\quad\Longrightarrow\quad \dfrac 1 2\,\textrm d u = \textrm d x.


$$

Using the above, we can write the integral in terms of $u$ and evaluate it, as follows:

$$


\begin{aligned}\begin{aligned}∫\frac{10}{1−4𝑥^{2}}\,d𝑥 & =10∫\frac{1}{1−(2𝑥)^{2}}\,d𝑥 \\ & =10∫\frac{1}{1−𝑢^{2}}\,⋅\frac{1}{2}\,d𝑢 \\ & =5∫\frac{1}{1−𝑢^{2}}\,d𝑢 \\ & =5artanh⁡𝑢+𝐶 \\ & =5artanh⁡2𝑥+𝐶\end{aligned}\end{aligned}


$$

Note that this result is subject to the condition $\left|2x \right| < 1.$

### Example: Calculating Definite Integrals Using Substitution With Inverse Hyperbolic Functions

#### Question

$\newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits}$

Evaluate the integral $\displaystyle{\int_{4}^{2\sqrt{5}} \dfrac{1}{\sqrt{x^2 - 4}}\, \textrm{d}x}.$

#### Explanation

$\newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits}$

Note that we can rewrite this integral as

$$


\int_{4}^{2\sqrt{5}} \dfrac{1}{\sqrt{x^2 - 4}}\, \textrm{d}x = \dfrac{1}{2}\int_{4}^{2\sqrt{5}} \dfrac{1}{\sqrt{\left(\frac {x}{2} \right)^2 - 1}} \, \textrm{d}x.


$$

This integral resembles the basic integral for inverse hyperbolic cosine,

$$


\int \frac{1}{\sqrt{u^2-1}}\, \textrm{d}u = \arcosh{u}+C.


$$

The only difference is that instead of $u^2$ as the variable, we have $\left(\dfrac {x}{2} \right)^2.$

So, let's substitute $u = \dfrac {x}{2}.$ Differentiating, we get

$$


\dfrac{\textrm{d}u}{\textrm{d}x} = \dfrac{1}{2} \quad\Longrightarrow\quad \textrm{d}x = 2\,\textrm{d}u.


$$

Before substituting, we use the table below to change the limits from $x$ to $u.$
