# Integration Using the Hyperbolic Double-Angle Formulas

Source: https://www.mathacademy.com/topics/3262?courseId=106
Topic ID: 3262

## Prerequisites

- [Integration Using the Double-Angle Formulas](./1038-integration-using-the-double-angle-formulas.md)
- [Integration Using Basic Hyperbolic Identities](./3260-integration-using-basic-hyperbolic-identities.md)

## Lesson

### Introduction

We can compute integrals containing hyperbolic functions using the hyperbolic counterparts of the trigonometric double-angle formulas. We use Osborn's rule to convert a trigonometric identity to a corresponding hyperbolic identity.

Osborn's rule states that to convert a trigonometric identity to a corresponding hyperbolic identity, we

- replace every trigonometric function with its corresponding hyperbolic function, and

- for any product of two trigonometric sines, change the sign of the corresponding product of hyperbolic sines.

$\newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\sinh}{\mathop{\rm sinh}\nolimits} \newcommand{\cosh}{\mathop{\rm cosh}\nolimits} \newcommand{\tanh}{\mathop{\rm tanh}\nolimits} \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits}$

For example, let's consider the following integral:

$$


\displaystyle{\int} \sinh x \cosh x \, \textrm{d}x


$$

Notice that the corresponding trigonometric integral is

$$


\displaystyle{\int} \sin x \cos x \, \textrm{d}x.


$$

One way of solving this trigonometric integral is to use the double-angle formula for sine:

$$


\sin 2x = 2\sin x \cos x


$$

Applying Osborn's rule, we get an equivalent hyperbolic identity:

$$


\sinh 2x = 2\sinh x \cosh x


$$

Rearranging the above formula, we get

$$


\dfrac{1}{2}\sinh {2x}= \sinh x \cosh x.


$$

Therefore, we can calculate our original integral as follows:

$$


\begin{aligned}∫sinh⁡𝑥cosh⁡𝑥\,d𝑥 & =∫\frac{1}{2}sinh⁡2𝑥\,d𝑥 \\ & =\frac{1}{2}∫sinh⁡2𝑥\,d𝑥 \\ & =\frac{1}{2}⋅\frac{1}{2}cosh⁡2𝑥+𝐶 \\ & =\frac{1}{4}cosh⁡2𝑥+𝐶\end{aligned}


$$

### Example: Integrating Expressions Using the Double-Angle Formula for Sine

#### Question

Calculate $\displaystyle \int 4\sinh 2x \cosh 2x \, \textrm{d}x.$

#### Explanation

First, we find the hyperbolic identity that corresponds to the double-angle formula for sine:

$$


\sin {2\theta}=2\sin \theta \cos \theta


$$

Using Osborn's rule, we get the double-angle formula for the hyperbolic sine:

$$


\sinh {2\theta} =2\sinh \theta \cosh \theta


$$

Letting $\theta= 2x,$ we get

$$


\sinh {4x} =2\sinh 2x \cosh 2x.


$$

Rearranging the above formula, we get

$$


\dfrac{1}{2}\sinh {4x}= \sinh 2x \cosh 2x.


$$

Therefore,

$$


\begin{aligned}∫4sinh⁡2𝑥cosh⁡2𝑥\,d𝑥 & =∫4⋅\frac{1}{2}sinh⁡4𝑥\,d𝑥 \\ & =∫2sinh⁡4𝑥\,d𝑥 \\ & =2∫sinh⁡4𝑥\,d𝑥 \\ & =2⋅\frac{1}{4}cosh⁡4𝑥+𝐶 \\ & =\frac{1}{2}cosh⁡4𝑥+𝐶.\end{aligned}


$$

### Example: Integrating Expressions Using the Double-Angle Formula for Cosine

#### Question

Calculate $\displaystyle \int \cosh^2{x} + \sinh^2{x}\ \, \textrm{d}x.$

#### Explanation

First, we find the hyperbolic identity that corresponds to the following double-angle formula for cosine:

$$


\cos{2x}= \cos^2{x}-\sin^2{x}


$$

Using Osborn's rule, we get the following double-angle formula for the hyperbolic cosine:

$$


\cosh 2x = \cosh^2{x} + \sinh^2{x}


$$

Therefore,

$$


\begin{aligned}∫cosh^{2}⁡𝑥+sinh^{2}⁡𝑥\,d𝑥 & =∫cosh⁡2𝑥\,d𝑥 \\ & =\frac{1}{2}sinh⁡2𝑥+𝐶.\end{aligned}


$$

### Example: Integrating Expressions Using the Squared Cosine Double-Angle Formula

#### Question

Calculate $\displaystyle \int 2\cosh^2 x \, \textrm{d}x.$

#### Explanation

First, we find the hyperbolic identity that corresponds to the following double-angle formula for cosine:

$$


\cos{2x} =2\cos^2 x -1.


$$

Using Osborn's rule, we get the following double-angle formula for the hyperbolic cosine:

$$


\cosh{2x} =2\cosh^2 x -1.


$$

Rearranging, we have

$$


\cosh^2 x = \dfrac{1}{2} \left(\cosh 2x +1 \right).


$$

Substituting this into our integral, we get

$$


\begin{aligned}∫2cosh^{2}⁡𝑥\,d𝑥 & =∫2⋅\frac{1}{2}(cosh⁡2𝑥+1)\,d𝑥 \\ & =∫(cosh⁡2𝑥+1)\,d𝑥 \\ & =\frac{1}{2}sinh⁡2𝑥+𝑥+𝐶.\end{aligned}


$$

### Example: Integrating Expressions Using the Squared Sine Double-Angle Formula

#### Question

Evaluate $\displaystyle \int_{0}^{\ln 2} 8\sinh^2{x} \, \textrm{d}x.$

#### Explanation

First, we find the hyperbolic identity that corresponds to the following double-angle formula for cosine:

$$


\cos {2x}=1-2\sin^2x.


$$

Using Osborn's rule, we get the following double-angle formula for the hyperbolic cosine:

$$


\cosh{2x} = 1+ 2\sinh^2{x}


$$

We can rearrange the above formula as

$$


\sinh^2x = \dfrac{1}{2}\left(\cosh {2x} -1\right ).


$$

We can now integrate as follows:

$$


\begin{aligned}∫_{ln⁡20}^{}8sinh^{2}⁡𝑥\,d𝑥 & =∫_{ln⁡20}^{}8⋅\frac{1}{2}(cosh⁡2𝑥−1)\,d𝑥 \\ & =∫_{ln⁡20}^{}4cosh⁡2𝑥−4\,d𝑥 \\ & =(2sinh⁡2𝑥−4𝑥)\,_{ln⁡20}^{} \\ & =(2sinh⁡(2ln⁡2)−4ln⁡2)−(2sinh⁡0−4⋅0) \\ & =2⋅\frac{𝑒^{2ln⁡2}−𝑒^{−2ln⁡2}}{2}−4ln⁡2 \\ & =(2^{2}−2^{−2})−4ln⁡2 \\ & =\frac{15}{4}−4ln⁡2\end{aligned}


$$
