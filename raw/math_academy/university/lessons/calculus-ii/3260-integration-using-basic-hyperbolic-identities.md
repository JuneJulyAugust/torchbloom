# Integration Using Basic Hyperbolic Identities

Source: https://www.mathacademy.com/topics/3260?courseId=106
Topic ID: 3260

## Prerequisites

- [Integrating Hyperbolic Functions](../calculus-i/304-integrating-hyperbolic-functions.md)
- [Integrating Trigonometric Functions Using Substitution](./478-integrating-trigonometric-functions-using-substitution.md)
- [Simplifying Expressions Using the Secant-Tangent Identity](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/1454-simplifying-expressions-using-the-secant-tangent-identity.md)
- [Simplifying Trigonometric Expressions Using the Cotangent-Cosecant Identity](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/1455-simplifying-trigonometric-expressions-using-the-cotangent-cosecant-identity.md)

## Lesson

### Introduction

It's possible to convert every trigonometric identity to a corresponding *hyperbolic* identity using **Osborn's rule.**

To apply Osborn's rule, we follow two steps:

1. Replace every trigonometric function with its corresponding hyperbolic function.

2. For any product of *two trigonometric sines*, change the sign of the corresponding product of hyperbolic sines.

To demonstrate, consider the Pythagorean trigonometric identity:

$$


\newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits} \newcommand{\cosh}{\mathop{\rm cosh}\nolimits} \newcommand{\sinh}{\mathop{\rm sinh}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \cos^2 x \:{\color{blue}{\boldsymbol +}}\: \sin^2 x = 1


$$

Notice that this trigonometric identity contains a product of two sines. Therefore, to find the corresponding hyperbolic identity, we change each trigonometric function to its corresponding hyperbolic counterpart and change the sign in front of the corresponding product of sines.

Thus, the corresponding hyperbolic identity is

$$


\cosh^2 x \:{\color{red}{\boldsymbol -}}\: \sinh^2 x = 1.


$$

We can check that this identity is indeed true using the definitions of the hyperbolic sine and cosine:

$$


\begin{aligned}cosh^{2}⁡𝑥−sinh^{2}⁡𝑥 & =(\frac{1}{2}(𝑒^{𝑥}+𝑒^{−𝑥}))^{2}−(\frac{1}{2}(𝑒^{𝑥}−𝑒^{−𝑥}))^{2} \\ & =\frac{1}{4}(𝑒^{𝑥}+𝑒^{−𝑥})^{2}−\frac{1}{4}(𝑒^{𝑥}−𝑒^{−𝑥})^{2} \\ & =\frac{1}{4}((𝑒^{𝑥}+𝑒^{−𝑥})^{2}−(𝑒^{𝑥}−𝑒^{−𝑥})^{2}) \\ & =\frac{1}{4}(𝑒^{2𝑥}+2+𝑒^{−2𝑥}−(𝑒^{2𝑥}−2+𝑒^{−2𝑥})) \\ & =\frac{1}{4}(𝑒^{2𝑥}+2+𝑒^{−2𝑥}−(𝑒^{2𝑥}−2+𝑒^{−2𝑥})) \\ & =\frac{1}{4}⋅4 \\ & =1\,✓\end{aligned}


$$

### Osborn’s Rule in Cases Where a Product of Sines Is Hidden

When applying Osborn's rule, we must be aware that sometimes a product of two sines is "hidden."

To demonstrate, consider the following trigonometric identity:

$$


\newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits} \newcommand{\cosh}{\mathop{\rm cosh}\nolimits} \newcommand{\sinh}{\mathop{\rm sinh}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} 1 \:{\color{blue}{\boldsymbol +}}\: \tan^2 x = \sec^2 x


$$

At first glance, it may seem that there is no product of sines, and we do not need to change any signs in the corresponding hyperbolic identity.

However, recall that

$$


\tan x = \dfrac{\sin x}{\cos x}


$$

which implies that

$$


\tan^2 x = \dfrac{\sin^2 x}{\cos^2 x}.


$$

So, there is a hidden product of sines within the $\tan^2 x$ term, and we need to flip the sign in front of this term when writing down the corresponding hyperbolic identity.

Thus, the corresponding hyperbolic identity is

$$


1 \:{\color{red}{\boldsymbol -}}\: \tanh^2 x = \sech^2 x.


$$

### Example: Deriving a Hyperbolic Identity Using Osborn's Rule

#### Question

$\newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits} \newcommand{\cosh}{\mathop{\rm cosh}\nolimits} \newcommand{\sinh}{\mathop{\rm sinh}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits}$Find a hyperbolic identity that corresponds to the trigonometric identity $1 + \cot^2{x} = \csc^2{x}.$

#### Explanation

$\newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits} \newcommand{\cosh}{\mathop{\rm cosh}\nolimits} \newcommand{\sinh}{\mathop{\rm sinh}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits}$Osborn's rule allows us to construct a hyperbolic identity from a corresponding trigonometric identity.

To apply Osborn's rule, we follow two steps:

1. Replace every trigonometric function with its corresponding hyperbolic function.

2. For any product of two trigonometric sines, flip the sign of the corresponding product of hyperbolic sines.

We're given the following trigonometric identity:

$$


1 + \cot^2{x} = \csc^2{x}


$$

Notice that

$$


\cot^2{x} = \dfrac{\cos^2{x}}{\sin^2{x}} \qquad \textrm{and} \qquad \csc^2{x} = \dfrac{1}{\sin^2{x}}


$$

and thus, we have two products of sines. Therefore, the corresponding hyperbolic identity is

$$


1 \,{\mathbf{\color{red}{-}}}\, \coth^2{x} = {\mathbf{\color{red}{-}}}\,\csch^2{x}.


$$

### Integration Using Hyperbolic Identities

Suppose we want to calculate the integral

$$


\newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits} \int \dfrac{1}{\sinh^2 x}\,\textrm{d}x.


$$

First, we note the following hyperbolic identity:

$$


\csch{x} = \dfrac{1}{\sinh{x}}


$$

Therefore, we can write our integral as

$$


\int \dfrac{1}{\sinh^2{x}} \,\textrm{d}x = \int \left(\dfrac{1}{\sinh{x}}\right)^2 \,\textrm{d}x = \int \csch^2{x} \,\textrm{d}x.


$$

From here, we can see that this is just a standard hyperbolic integral:

$$


\int \dfrac{1}{\sinh^2{x}}\,\textrm{d}x = \int \csch^2{x}\,\textrm{d}x = -\coth{x} + C


$$

### Example: Integrating a Product of Hyperbolic Functions

#### Question

$\newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits} \newcommand{\cosh}{\mathop{\rm cosh}\nolimits} \newcommand{\sinh}{\mathop{\rm sinh}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits}$ Evaluate $\displaystyle \int _{-1}^{1} \coth{x}\sinh{x}\,\textrm d x.$

#### Explanation

$$


\newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits} \newcommand{\cosh}{\mathop{\rm cosh}\nolimits} \newcommand{\sinh}{\mathop{\rm sinh}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits}


$$

First, we find the hyperbolic identity that corresponds to the trigonometric identity

$$


\cot{x}=\dfrac{\cos{x}}{\sin{x}}.


$$

Using Osborn's rule, the corresponding hyperbolic identity is

$$


\coth{x}=\dfrac{\cosh{x}}{\sinh{x}}.


$$

Now, we rewrite the integral using the above identity, as follows:

$$


\begin{aligned}∫_{1−1}^{}coth⁡𝑥sinh⁡𝑥\,d𝑥 & =∫_{1−1}^{}\frac{cosh⁡𝑥}{sinh⁡𝑥}⋅sinh⁡𝑥\,d𝑥 \\ & =∫_{1−1}^{}cosh⁡𝑥\,d𝑥 \\ & =sinh⁡𝑥\,_{1−1}^{} \\ & =sinh⁡(1)−sinh⁡(−1) \\ & =\frac{𝑒^{1}−𝑒^{−1}}{2}−\frac{𝑒^{−1}−𝑒^{−(−1)}}{2} \\ & =\frac{𝑒^{1}−𝑒^{−1}−𝑒^{−1}+𝑒^{1}}{2} \\ & =\frac{2𝑒−2𝑒^{−1}}{2} \\ & =𝑒−𝑒^{−1}.\end{aligned}


$$

### Example: Integrating a Quotient of Hyperbolic Functions

#### Question

$\newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\sinh}{\mathop{\rm sinh}\nolimits} \newcommand{\cosh}{\mathop{\rm cosh}\nolimits} \newcommand{\tanh}{\mathop{\rm tanh}\nolimits} \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits}$Evaluate $\displaystyle \int _{-1}^{1} \dfrac{\tanh^2{x}}{2\sinh^2 x} \,\textrm d x.$

#### Explanation

$\newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\sinh}{\mathop{\rm sinh}\nolimits} \newcommand{\cosh}{\mathop{\rm cosh}\nolimits} \newcommand{\tanh}{\mathop{\rm tanh}\nolimits} \newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits}$First, we write our integral as

$$


\int _{-1}^{1} \dfrac{\tanh^2{x}}{2\sinh^2 x}\textrm{d}x = \dfrac{1}{2}\int _{-1}^{1} \dfrac{1}{\sinh^2{x}}\cdot \tanh^2{x} \, \textrm{d}x.


$$

Now we need to find the hyperbolic identity that corresponds to the trigonometric identity

$$


\tan{x}=\dfrac{\sin{x}}{\cos{x}}.


$$

Using Osborn's rule, the corresponding hyperbolic identity is

$$


\tanh{x} = \dfrac{\sinh{x}}{\cosh{x}}.


$$

Then, we use the above identity to write the integral as follows:

$$


\begin{aligned}\frac{1}{2}∫_{1−1}^{}\frac{1}{sinh^{2}⁡𝑥}⋅tanh^{2}⁡𝑥\,d𝑥 & =\frac{1}{2}∫_{1−1}^{}\frac{1}{sinh^{2}⁡𝑥}⋅\frac{sinh^{2}⁡𝑥}{cosh^{2}⁡𝑥}\,d𝑥 \\ & =\frac{1}{2}∫_{1−1}^{}\frac{sinh^{2}⁡𝑥}{sinh^{2}⁡𝑥}⋅\frac{1}{cosh^{2}⁡𝑥}\,d𝑥 \\ & =\frac{1}{2}∫_{1−1}^{}\frac{1}{cosh^{2}⁡𝑥}\,d𝑥 \\ & =\frac{1}{2}∫_{1−1}^{}sech^{2}⁡𝑥 \\ & =\frac{1}{2}tanh⁡𝑥_{1−1}^{} \\ & =\frac{1}{2}(tanh⁡(1)−tanh⁡(−1)) \\ & =\frac{1}{2}(\frac{𝑒−𝑒^{−1}}{𝑒+𝑒^{−1}}−\frac{𝑒^{−1}−𝑒}{𝑒^{−1}+𝑒}) \\ & =\frac{1}{2}(\frac{𝑒^{2}−1}{𝑒^{2}+1}−\frac{1−𝑒^{2}}{1+𝑒^{2}}) \\ & =\frac{1}{2}(2⋅\frac{𝑒^{2}−1}{𝑒^{2}+1}) \\ & =\frac{𝑒^{2}−1}{𝑒^{2}+1}\end{aligned}


$$

### Example: Computing a Hyperbolic Integral Using a Substitution

#### Question

Evaluate $\newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits} \displaystyle{\int_{0}^{\ln 3} \tanh x \, \textrm{d}x}.$

#### Explanation

First, we find the hyperbolic identity that corresponds to the following trigonometric identity:

$$


\newcommand{\sech}{\mathop{\rm sech}\nolimits} \newcommand{\csch}{\mathop{\rm csch}\nolimits} \newcommand{\coth}{\mathop{\rm coth}\nolimits} \newcommand{\arsinh}{\mathop{\rm arsinh}\nolimits} \newcommand{\arcosh}{\mathop{\rm arcosh}\nolimits} \newcommand{\artanh}{\mathop{\rm artanh}\nolimits} \newcommand{\arsech}{\mathop{\rm arsech}\nolimits} \newcommand{\arcsch}{\mathop{\rm arcsch}\nolimits} \newcommand{\arcoth}{\mathop{\rm arcoth}\nolimits} \tan{x} = \dfrac{\sin{x}}{\cos{x}}


$$

Using Osborn's rule, the corresponding hyperbolic identity is

$$


\tanh{x} = \dfrac{\sinh{x}}{\cosh{x}}.


$$

Now, we rewrite the integral as follows:

$$


\begin{aligned}∫_{ln⁡30}^{}tanh⁡𝑥\,d𝑥 & =∫_{ln⁡30}^{}\frac{sinh⁡𝑥}{cosh⁡𝑥}\,d𝑥\end{aligned}


$$

We can solve this by substitution. Let $u = \cosh{x}.$ Then,

$$


\dfrac{\textrm{d}u}{\textrm{d}x} = \sinh{x} \quad \Longrightarrow \quad \textrm{d}u = \sinh{x} \, \textrm d x.


$$

Now, we fill the table for the limits of integration according to the rule $u = \cosh{x}.$

Now, we evaluate the integral, as follows:

$$


\begin{aligned}∫_{ln⁡30}^{}\frac{sinh⁡𝑥}{cosh⁡𝑥}\,d𝑥 & =∫_{5/31}^{}\frac{1}{𝑢}\,d𝑢 \\ & =ln⁡|𝑢|_{5/31}^{} \\ & =ln⁡(\frac{5}{3})−ln⁡1 \\ & =ln⁡(\frac{5}{3})\end{aligned}


$$
