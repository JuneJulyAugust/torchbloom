# Differentiating Inverse Hyperbolic Functions

Source: https://www.mathacademy.com/topics/3252?courseId=105
Topic ID: 3252

## Prerequisites

- [Differentiating Inverse Trigonometric Functions](./303-differentiating-inverse-trigonometric-functions.md)
- [The Inverse Hyperbolic Functions](./969-the-inverse-hyperbolic-functions.md)
- [Differentiating Hyperbolic Functions](./1362-differentiating-hyperbolic-functions.md)

## Lesson

### Introduction

The derivatives of the base inverse hyperbolic functions are shown below: $\newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits}$

$$


\begin{aligned}\frac{d}{d𝑥}(arsinh⁡𝑥) & =\frac{1}{\sqrt{√𝑥^{2}+1}}, & & \,𝑥∈(−∞,∞) \\ \frac{d}{d𝑥}(arcosh⁡𝑥) & =\frac{1}{\sqrt{√𝑥^{2}−1}}, & & \,𝑥∈(1,∞) \\ \frac{d}{d𝑥}(artanh⁡𝑥) & =\frac{1}{1−𝑥^{2}}, & & \,𝑥∈(−1,1)\end{aligned}


$$

Now that we know the derivative of the base inverse hyperbolic functions, we can differentiate combinations of these functions, by using the properties of differentiation.

For example, let's find the derivative of

$$


y = \arcosh(x^2).


$$

Using the formula above with the chain rule, we get

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =\frac{d}{d𝑥}(arcosh⁡(𝑥^{2})) \\ & =\frac{1}{\sqrt{√(𝑥^{2})^{2}−1}}⋅(𝑥^{2})^{′} \\ & =\frac{1}{\sqrt{√𝑥^{4}−1}}⋅2𝑥 \\ & =\frac{2𝑥}{\sqrt{√𝑥^{4}−1}}.\end{aligned}


$$

### Example: Differentiating an Inverse Sinh Function

#### Question

$\newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits}$

If $y = 2\arsinh{x^2},$ then find $\dfrac {\textrm{d}y}{\textrm{d}x}.$

#### Explanation

$\newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits}$

The formula for the derivative of the inverse hyperbolic sine function is

$$


\dfrac{\textrm{d}}{\textrm{d}x}(\arsinh x) = \dfrac{1}{\sqrt{x^2+1}}.


$$

Using the formula above with the chain rule, we get

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =\frac{d}{d𝑥}(2arsinh⁡𝑥^{2}) \\ & =2⋅\frac{d}{d𝑥}(arsinh⁡𝑥^{2}) \\ & =2⋅\frac{1}{\sqrt{√(𝑥^{2})^{2}+1}}⋅(𝑥^{2})^{′} \\ & =2⋅\frac{1}{\sqrt{√𝑥^{4}+1}}⋅2𝑥 \\ & =\frac{4𝑥}{\sqrt{√𝑥^{4}+1}}.\end{aligned}


$$

### Example: Differentiating an Inverse Cosh Function

#### Question

$\newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits}$

If $y =\arcosh(x+1),$ then find $\dfrac {\textrm{d}y}{\textrm{d}x}.$

#### Explanation

$\newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits}$

The formula for the derivative of the inverse hyperbolic cosine function is

$$


\dfrac{\textrm{d}}{\textrm{d}x}(\arcosh x) = \dfrac{1}{\sqrt{x^2-1}}.


$$

Using the formula above with the chain rule, we get

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =\frac{d}{d𝑥}(arcosh⁡(𝑥+1)) \\ & =\frac{1}{\sqrt{√(𝑥+1)^{2}−1}}⋅(𝑥+1)^{′} \\ & =\frac{1}{\sqrt{√(𝑥^{2}+2𝑥+1)−1}}⋅1 \\ & =\frac{1}{\sqrt{√𝑥^{2}+2𝑥}} \\ & =\frac{1}{\sqrt{√𝑥(𝑥+2)}}.\end{aligned}


$$

### Example: Differentiating an Inverse Tanh Function

#### Question

$\newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits}$

If $y = \artanh{4x},$ then find $\dfrac {\textrm{d}y}{\textrm{d}x}.$

#### Explanation

$\newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits}$

The formula for the derivative of the inverse hyperbolic tangent function is

$$


\dfrac{\textrm{d}}{\textrm{d}x}(\artanh x) = \dfrac{1}{1-x^2}.


$$

Using the formula above with the chain rule, we get

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =\frac{d}{d𝑥}(artanh⁡4𝑥) \\ & =\frac{1}{1−(4𝑥)^{2}}⋅(4𝑥)^{′} \\ & =\frac{1}{1−16𝑥^{2}}⋅4 \\ & =\frac{4}{1−16𝑥^{2}}.\end{aligned}


$$

### Example: Differentiating Inverse Hyperbolic Functions Using the Product and Quotient Rules

#### Question

$\newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits}$

If $w(x) = e^{2x}\artanh{x},$ then $w'(x)=2e^{2x}\artanh{x} + y(x).$ What is $y(x)?$

#### Explanation

$\newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits}$

Here, we have the product of two functions $u(x) = e^{2x}$ and $v(x)=\artanh{x}.$ So, we apply the product rule:

$$


\begin{aligned}𝑤^{′}(𝑥) & =(𝑒^{2𝑥})^{′}⋅artanh⁡𝑥+𝑒^{2𝑥}⋅(artanh⁡𝑥)^{′} \\ & =2𝑒^{2𝑥}⋅artanh⁡𝑥+𝑒^{2𝑥}⋅\frac{1}{1−𝑥^{2}} \\ & =2𝑒^{2𝑥}artanh⁡𝑥+\underset{𝑦(𝑥)}{\underset{}{\frac{𝑒^{2𝑥}}{1−𝑥^{2}}}}\end{aligned}


$$

Therefore, $y(x) = \dfrac{e^{2x}}{1 - x^2}.$

### Deriving the Derivatives of Inverse Hyperbolic Functions

We derive formulas for the derivatives of the inverse hyperbolic functions from the functions' definitions. $\newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits}$

For instance, let's show that

$$


\dfrac{\textrm{d}}{\textrm{d}x}(\arsinh{x}) = \dfrac{1}{\sqrt{x^2+1}}.


$$

Recall that

$$


\arsinh{x} = \ln\big(x+\sqrt{x^2+1}\big).


$$

Differentiating using the chain rule, we get

$$


\begin{aligned}\frac{d}{d𝑥}(arsinh⁡𝑥) & =\frac{d}{d𝑥}(ln⁡(𝑥+\sqrt{√𝑥^{2}+1})) \\ & =\frac{1}{𝑥+\sqrt{√𝑥^{2}+1}}⋅(𝑥+\sqrt{√𝑥^{2}+1})^{′} \\ & =\frac{(1+\frac{𝑥}{\sqrt{√𝑥^{2}+1}})}{\sqrt{√𝑥^{2}+1}} \\ & =\frac{\sqrt{√𝑥^{2}+1}+𝑥}{\sqrt{√𝑥^{2}+1}(𝑥+\sqrt{√𝑥^{2}+1})} \\ & =\frac{𝑥+\sqrt{√𝑥^{2}+1}}{\sqrt{√𝑥^{2}+1}(𝑥+\sqrt{√𝑥^{2}+1})} \\ & =\frac{1}{\sqrt{√𝑥^{2}+1}}.\end{aligned}


$$

Similarly, we can obtain the other formulas.
