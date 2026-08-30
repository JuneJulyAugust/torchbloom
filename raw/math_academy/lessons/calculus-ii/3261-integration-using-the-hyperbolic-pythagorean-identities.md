# Integration Using the Hyperbolic Pythagorean Identities

Source: https://www.mathacademy.com/topics/3261?courseId=106
Topic ID: 3261

## Prerequisites

- [Integration Using the Pythagorean Identities](./1037-integration-using-the-pythagorean-identities.md)
- [Integration Using Basic Hyperbolic Identities](./3260-integration-using-basic-hyperbolic-identities.md)

## Lesson

### Introduction

We can compute integrals containing hyperbolic functions using the hyperbolic counterparts of the Pythagorean identity. We use Osborn's rule to convert a trigonometric identity to a corresponding hyperbolic identity.

Osborn's rule states that to convert a trigonometric identity to a corresponding hyperbolic identity, we

- replace every trigonometric function with its corresponding hyperbolic function, and

- for any product of two trigonometric sines, change the sign of the corresponding product of hyperbolic sines.

$\displaystyle \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits}$

For example, suppose we want to calculate the following integral:

$$


\int \cosh^2{x} - \sinh^2{x} \: \textrm{d}x


$$

First, we recall the Pythagorean identity

$$


\cos^2{x} + \sin^2{x} = 1.


$$

Using Osborn's rule, we get the corresponding hyperbolic identity

$$


\cosh^2{x} - \sinh^2{x} = 1.


$$

Therefore, we evaluate our integral as follows:

$$


\begin{aligned}∫\underset{1}{\underset{}{cosh^{2}⁡𝑥−sinh^{2}⁡𝑥}}\,d𝑥=∫1\,d𝑥=𝑥+𝐶\end{aligned}


$$

Let's see another example.

### Example: Integrating a Function Using the Hyperbolic Pythagorean Identity

#### Question

$\newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits}$

Calculate $\displaystyle{\int} \dfrac{1}{1+\sinh^2 x} \, \textrm{d}x.$

#### Explanation

$\newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits}$First, we find the hyperbolic identity that corresponds to the Pythagorean identity

$$


\cos^2 x + \sin^2 x= 1.


$$

Using Osborn's rule, we get the hyperbolic Pythagorean identity

$$


\cosh^2x -\sinh^2x=1


$$

which we can write as

$$


1+\sinh^2x=\cosh^2x.


$$

Additionally, we have

$$


\sech x = \dfrac{1}{\cosh x}.


$$

Using the above, we rewrite the denominator and calculate the integral as follows:

$$


\begin{aligned}∫\frac{1}{1+sinh^{2}⁡𝑥}\,d𝑥 & =∫\frac{1}{cosh^{2}⁡𝑥}\,d𝑥 \\ & =∫(\frac{1}{cosh⁡𝑥})^{2}\,d𝑥 \\ & =∫sech^{2}⁡𝑥\,d𝑥 \\ & =tanh⁡𝑥+𝐶\end{aligned}


$$

### Calculating Integrals Using Related Hyperbolic Identities

$\newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits}$We can use Osborn's rule to write down the hyperbolic equivalents of the sectant-tangent and cotangent-cosecant identities.

From the secant-tangent identity

$$


1 + \tan^2 x = \sec^2 x


$$

we have the equivalent hyperbolic identity

$$


1 - \tanh^2 x = \sech^2 x.


$$

Similarly, from the cotangent-cosecant identity

$$


1+\cot^2 x = \csc^2 x


$$

we have the equivalent hyperbolic identity

$$


1-\coth^2 x = -\csch^2 x


$$

which we can rewrite as

$$


\coth^2 x - 1 = \csch^2 x.


$$

These identities can be used to solve certain integrals involving the expressions $\tanh^2{x},$ $\coth^2 x,$ $\sech^2 x,$ or $\csch^2{x}.$

### Example: Integrating a Function Using the Hyperbolic Secant-Tangent Identity

#### Question

$\newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits}$Evaluate $\displaystyle \int_{0}^{\ln 2} \dfrac{\tanh{x}-\tanh^3{x}}{\sech{x}} \, \textrm{d}x.$

#### Explanation

$\newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits}$First, we find the hyperbolic identity that corresponds to the secant-tangent identity

$$


1 + \tan^2 x= \sec^2{x}.


$$

Using Osborn's rule, we get the hyperbolic secant-tangent identity

$$


1-\tanh^2x=\sech^2{x}.


$$

Using the above, we rewrite the integral and evaluate it as follows:

$$


\begin{aligned}∫_{ln⁡20}^{}\frac{tanh⁡𝑥−tanh^{3}⁡𝑥}{sech⁡𝑥}\,d𝑥 & =∫_{ln⁡20}^{}\frac{(1−tanh^{2}⁡𝑥)tanh⁡𝑥}{sech⁡𝑥}\,d𝑥 \\ & =∫_{ln⁡20}^{}\frac{sech^{2}⁡𝑥tanh⁡𝑥}{sech⁡𝑥}\,d𝑥 \\ & =∫_{ln⁡20}^{}sech⁡𝑥tanh⁡𝑥\,d𝑥 \\ & =−sech⁡𝑥\,_{ln⁡20}^{} \\ & =−sech⁡(ln⁡2)+sech⁡0 \\ & =−\frac{2}{𝑒^{ln⁡2}+𝑒^{−ln⁡2}}+\frac{2}{𝑒^{0}+𝑒^{0}} \\ & =−\frac{2}{(2+\frac{1}{2})}+1 \\ & =−\frac{2}{(\frac{5}{2})}+1 \\ & =−\frac{4}{5}+1 \\ & =\frac{1}{5}\end{aligned}


$$

### Example: Integrating a Function Using the Hyperbolic Cosecant-Cotangent Identity

#### Question

$\newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits}$Evaluate $\displaystyle \int_{\ln 3}^{\ln 6} \dfrac{\csch{x}}{\coth^2{x} - 1} \, \textrm{d}x.$

#### Explanation

First, we find the hyperbolic identity that corresponds to the cosecant-cotangent identity

$$


\newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits} 1 + \cot^2 x= \csc^2{x}.


$$

Using Osborn's rule, we get the hyperbolic cosecant-cotangent identity

$$


\coth^2x - 1=\csch^2{x}.


$$

Using the above, we rewrite the integral and evaluate it, as follows:

$$


\begin{aligned} \int_{\ln 3}^{\ln 6} \dfrac{\csch{x}}{\coth^2{x} - 1} \, \textrm{d}x &= \int_{\ln 3}^{\ln 6} \dfrac{\csch{x}}{\csch^2{x}} \, \textrm{d}x \\\[5pt] &= \int_{\ln 3}^{\ln 6} \sinh{x} \, \textrm{d}x \\\[5pt] &= \cosh{x} \Big|_{\ln 3}^{\ln 6}\\\[5pt] &= \cosh(\ln 6) - \cosh(\ln 3)\\\[5pt] &= \left(\dfrac{e^{\ln 6}+e^{-\ln 6}}{2}\right) - \left(\dfrac{e^{\ln 3}+e^{-\ln 3}}{2}\right)\\\[5pt] &= \left(\dfrac{6 + \dfrac{1}{6}}{2}\right) - \left(\dfrac{3 + \dfrac{1}{3}}{2}\right)\\\[5pt] &= \dfrac{37}{12} - \dfrac{5}{3}\\\[5pt] &= \dfrac{37}{12} - \dfrac{20}{12} \\\[5pt] &= \dfrac{17}{12} \end{aligned}


$$

### Example: Integrating Hyperbolic Functions With Linear Arguments

#### Question

$\newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits}$Calculate $\displaystyle{\int \dfrac{2}{\cosh^2(2x+1)-1} \, \textrm{d}x}.$

#### Explanation

$\newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits}$First, we find the hyperbolic identity that corresponds to the Pythagorean identity

$$


\cos^2 \theta + \sin^2 \theta = 1.


$$

Using Osborn's rule, we get the hyperbolic Pythagorean identity

$$


\cosh^2 \theta - \sinh^2 \theta = 1.


$$

Setting $\theta = 2x + 1,$ we get

$$


\cosh^2 (2x+1) - \sinh^2(2x+1) = 1


$$

which can be written as

$$


\cosh^2 (2x+1) -1 = \sinh^2(2x+1).


$$

Substituting the above into our integral gives

$$


\begin{aligned}∫\frac{2}{cosh^{2}⁡(2𝑥+1)−1}\,d𝑥 & =2∫\frac{1}{sinh^{2}⁡(2𝑥+1)}\,d𝑥 \\ & =2∫csch^{2}⁡(2𝑥+1)\,d𝑥 \\ & =−coth⁡(2𝑥+1)+𝐶.\end{aligned}


$$
