# Differentiating Reciprocal Hyperbolic Functions

Source: https://www.mathacademy.com/topics/3251?courseId=105
Topic ID: 3251

## Prerequisites

- [Differentiating Hyperbolic Functions](./1362-differentiating-hyperbolic-functions.md)

## Lesson

### Introduction

$\newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits}$

The derivatives of the reciprocal hyperbolic functions are as follows:

$$


\begin{aligned}\frac{d}{d𝑥}(sech⁡𝑥) & =−sech⁡𝑥tanh⁡𝑥 \\ \frac{d}{d𝑥}(csch⁡𝑥) & =−csch⁡𝑥coth⁡𝑥 \\ \frac{d}{d𝑥}(coth⁡𝑥) & =−csch^{2}⁡𝑥\end{aligned}


$$

Let's use these results to find the derivative of

$$


y= \sech x - 2\csch x.


$$

Differentiating term-by-term, we get

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =\frac{d}{d𝑥}(sech⁡𝑥−2csch⁡𝑥) \\ & =\frac{d}{d𝑥}(sech⁡𝑥)+\frac{d}{d𝑥}(−2csch⁡𝑥) \\ & =\frac{d}{d𝑥}(sech⁡𝑥)−2\frac{d}{d𝑥}(csch⁡𝑥) \\ & =−sech⁡𝑥tanh⁡𝑥−2(−csch⁡𝑥coth⁡𝑥) \\ & =−sech⁡𝑥tanh⁡𝑥+2csch⁡𝑥coth⁡𝑥.\end{aligned}


$$

### Example: Basic Derivatives of the Reciprocal Hyperbolic Functions

#### Question

$\newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits}$

Find the derivative of $y = 3\sech{x}+\coth{x}.$

#### Explanation

$\newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits}$

First, we recall the results for the derivatives of the basic reciprocal hyperbolic functions:

$$


( \sech x )' = -\sech x\tanh x, \quad ( \csch x )' = -\csch x \coth x, \quad ( \coth x )' = -\csch^2 x


$$

Differentiating the given function using these results and the rules of differentiation, we get

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =\frac{d}{d𝑥}(3sech⁡𝑥+coth⁡𝑥) \\ & =3\frac{d}{d𝑥}(sech⁡𝑥)+\frac{d}{d𝑥}(coth⁡𝑥) \\ & =3(−sech⁡𝑥tanh⁡𝑥)+(−csch^{2}⁡𝑥) \\ & =−3sech⁡𝑥tanh⁡𝑥−csch^{2}⁡𝑥.\end{aligned}


$$

### Example: Differentiating Reciprocal Hyperbolic Functions Using the Chain Rule

#### Question

$\newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits}$

Find the derivative of $f(x) =\coth(5x - 2).$

#### Explanation

$\newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits}$

First, we express $f(x)$ as a composite function:

$$


f =\coth{g}, \qquad g = 5x - 2


$$

The chain rule states that

$$


\dfrac {\textrm{d}f} {\textrm{d}x} = \dfrac {\textrm{d}f} {\textrm{d}g} \cdot \dfrac {\textrm{d}g} {\textrm{d}x}.


$$

Differentiating, we have

$$


\dfrac {\textrm{d}f} {\textrm{d}g} = -\csch^2{g},


$$

and

$$


\dfrac {\textrm{d}g} {\textrm{d}x} = 5.


$$

Finally, multiplying the two results together and substituting for $g$ gives

$$


\begin{aligned}\frac{d𝑓}{d𝑥} & =−csch^{2}⁡𝑔⋅5 \\ & =−5csch^{2}⁡𝑔 \\ & =−5csch^{2}⁡(5𝑥−2).\end{aligned}


$$

### Example: Differentiating Reciprocal Hyperbolic Functions Using the Product Rule

#### Question

$\newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits}$

Find the derivative of $f(x) = x^2\coth{x}.$

#### Explanation

$\newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits}$

Here, we have the product of two functions $u(x) = x^2$ and $v(x) = \coth{x}.$ So, we apply the product rule:

$$


\begin{aligned}𝑓^{′}(𝑥) & =(𝑥^{2})^{′}⋅coth⁡𝑥+𝑥^{2}⋅(coth⁡𝑥)^{′} \\ & =2𝑥⋅coth⁡𝑥+𝑥^{2}⋅(−csch^{2}⁡𝑥) \\ & =𝑥(2coth⁡𝑥−𝑥csch^{2}⁡𝑥)\end{aligned}


$$

### Example: Differentiating Reciprocal Hyperbolic Functions Using the Quotient Rule

#### Question

$\newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits}$

Find the derivative of $f(x) = \dfrac{\sech{x}}{4x}.$

#### Explanation

$\newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits}$

In this case, the expression for $f(x)$ is a quotient $\dfrac{u(x)}{v(x)}$ with $u(x) = \sech{x}$ and $v(x) = 4x.$

Therefore, we apply the quotient rule as follows:

$$


\begin{aligned}\begin{aligned}𝑓^{′}(𝑥) & =\frac{𝑢^{′}(𝑥)⋅𝑣(𝑥)−𝑢(𝑥)⋅𝑣^{′}(𝑥)}{[𝑣(𝑥)]^{2}} \\ & =\frac{(sech⁡𝑥)^{′}⋅(4𝑥)−sech⁡𝑥⋅(4𝑥)^{′}}{(4𝑥)^{2}} \\ & =\frac{(−sech⁡𝑥tanh⁡𝑥)⋅(4𝑥)−sech⁡𝑥⋅4}{16𝑥^{2}} \\ & =−\frac{4sech⁡𝑥(𝑥tanh⁡𝑥+1)}{16𝑥^{2}} \\ & =−\frac{sech⁡𝑥(𝑥tanh⁡𝑥+1)}{4𝑥^{2}}\end{aligned}\end{aligned}


$$

### Deriving the Result for the Derivative of the Hyperbolic Secant

$\newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits}$

We wish to prove the following result:

$$


\dfrac{\textrm{d}}{\textrm{d}x}(\sech{x}) = -\sech{x} \tanh{x}.


$$

To do this, we can use the fact that

$$


\sech x = \dfrac{1}{\cosh x}.


$$

Differentiating the above equation using the chain rule, we arrive at

$$


\begin{aligned}\frac{d}{d𝑥}(sech⁡𝑥) & =\frac{d}{d𝑥}(\frac{1}{cosh⁡𝑥}) \\ & =\frac{d}{d𝑥}(cosh⁡𝑥)^{−1} \\ & =−(cosh⁡𝑥)^{−2}⋅(cosh⁡𝑥)^{′} \\ & =−\frac{1}{cosh^{2}⁡𝑥}⋅sinh⁡𝑥 \\ & =−\frac{1}{cosh⁡𝑥}⋅\frac{sinh⁡𝑥}{cosh⁡𝑥} \\ & =−sech⁡𝑥tanh⁡𝑥\end{aligned}


$$

We can prove the results for the derivatives of the hyperbolic cosecant and cotangent in a similar way.
