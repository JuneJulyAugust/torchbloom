# Integration Using Hyperbolic Functions and Completing the Square

Source: https://www.mathacademy.com/topics/3263?courseId=106
Topic ID: 3263

## Prerequisites

- [Integrating Functions by Completing the Square](./444-integrating-functions-by-completing-the-square.md)
- [Integration by Substitution With Inverse Hyperbolic Functions](./3258-integration-by-substitution-with-inverse-hyperbolic-functions.md)

## Lesson

### Introduction

Consider the integral

$$


\int \dfrac{1}{\sqrt{x^2-10x+34}}\, \textrm{d}x.


$$

As it is, this integral doesn't resemble any of the basic integrals we have encountered so far. However, we can complete the square for the denominator, as follows:

$$


\begin{aligned}𝑥^{2}−10𝑥+34 & =𝑥^{2}−10𝑥+(25−25)+34 \\ & =(𝑥^{2}−10𝑥+25)−25+34 \\ & =(𝑥−5)^{2}+9\end{aligned}


$$

If we plug the above into our integral and collect a factor of $9$ in the denominator, we get

$$


\begin{aligned}∫\frac{1}{\sqrt{√𝑥^{2}−10𝑥+34}}\,d𝑥 & =∫\frac{1}{\sqrt{√(𝑥−5)^{2}+9}}\,d𝑥 \\ & =∫\frac{1}{\sqrt{√9[\frac{(𝑥−5)^{2}}{9}+1]}}\,d𝑥 \\ & =\frac{1}{3}∫\frac{1}{\sqrt{√(\frac{𝑥−5}{3})^{2}+1}}\,d𝑥.\end{aligned}


$$

This now looks more familiar! Let $u = \dfrac {x-5}{3}.$ Then

$$


\dfrac{\textrm{d}u}{\textrm{d}x}=\dfrac{1}{3} \quad\Longrightarrow\quad \textrm{d}x = 3\,\textrm{d}u.


$$

We can now write the integral as

$$


\begin{aligned}∫\frac{1}{\sqrt{√𝑥^{2}−10𝑥+34}}\,d𝑥 & =\frac{1}{3}∫\frac{1}{\sqrt{√(\frac{𝑥−5}{3})^{2}+1}}\,d𝑥 \\ & =\frac{1}{3}∫\frac{1}{\sqrt{√𝑢^{2}+1}}\,⋅(3\,d𝑢) \\ & =∫\frac{1}{\sqrt{√𝑢^{2}+1}}\,d𝑢.\end{aligned}


$$

This is a basic integral for an inverse hyperbolic function, and we can solve it in one step:

$$


\begin{aligned}∫\frac{1}{\sqrt{√𝑢^{2}+1}}\,d𝑢 & =arsinh⁡𝑢+𝐶 \\ & =arsinh⁡(\frac{𝑥−5}{3})+𝐶\end{aligned}


$$

### Example: Computing an Inverse Hyperbolic Integral Containing a Completed Square

#### Question

Calculate $\displaystyle \int \dfrac{\textrm{d}x}{\sqrt{\left(x - 1\right)^2-9}}.$

#### Explanation

First, we note that

$$


\int \dfrac{\textrm{d}x}{\sqrt{\left(x - 1\right)^2-9}} = \int \dfrac{\textrm{d}x}{\sqrt{9\left(\dfrac{x - 1}{3}\right)^2-9}} = \dfrac{1}{3} \int \dfrac{1}{\sqrt{\left( \dfrac{x-1}{3}\right)^2-1}} \textrm{d}x.


$$

Let $u =\dfrac{x-1}{3}.$ Then, we have

$$


\dfrac{\textrm{d}u}{\textrm{d}x}=\dfrac{1}{3} \quad\Longrightarrow\quad \textrm{d}x = 3\,\textrm{d}u.


$$

Therefore,

$$


\begin{aligned}\frac{1}{3}∫\frac{1}{\sqrt{√(\frac{𝑥−1}{3})^{2}−1}}d𝑥 & =\frac{1}{3}∫\frac{1}{\sqrt{√𝑢^{2}−1}}⋅3\,d𝑢 \\ & =arcosh⁡𝑢+𝐶 \\ & =arcosh⁡(\frac{𝑥−1}{3})+𝐶.\end{aligned}


$$

### Example: Completing the Square to Compute a Hyperbolic Arcsine Integral

#### Question

${\displaystyle \int \dfrac{\textrm{d}x}{\sqrt{x^2-2x+2}} =}$

#### Explanation

First, we complete the square for the argument of the square root in the denominator:

$$


\begin{aligned} x^2-2x+2 & = x^2 - 2\cdot x +1^2 - 1^2 + 2 \\[3pt] &= (x-1)^2 -1+2 \\[3pt] &= (x-1)^2 + 1 \end{aligned}


$$

Substituting the above into the given integral, we get

$$


\int \dfrac{\textrm{d}x}{\sqrt{x^2-2x+2}} = \int \dfrac{\textrm{d}x}{\sqrt { (x-1)^2 + 1}}.


$$

Let $u = x-1.$ Then, we have

$$


\dfrac{\textrm{d}u}{\textrm{d}x}=1 \quad\Longrightarrow\quad \textrm{d}x = \textrm{d}u.


$$

Therefore,

$$


\begin{aligned}\begin{aligned}∫\frac{d𝑥}{\sqrt{√𝑥^{2}−2𝑥+2}} & =∫\frac{d𝑥}{\sqrt{√(𝑥−1)^{2}+1}} \\ & =∫\frac{d𝑢}{\sqrt{√𝑢^{2}+1}} \\ & =arsinh⁡𝑢+𝐶 \\ & =arsinh⁡(𝑥−1)+𝐶.\end{aligned}\end{aligned}


$$

### Example: Completing the Square to Compute a Hyperbolic Arccosine Integral

#### Question

${\displaystyle \int \dfrac{2}{\sqrt{x^2-4x+3}} \textrm{d}x=}$

#### Explanation

First, we complete the square for the argument of the square root in the denominator:

$$


\begin{aligned}𝑥^{2}−4𝑥+3 & =𝑥^{2}−2⋅2𝑥+2^{2}−2^{2}+3 \\ & =(𝑥−2)^{2}−1\end{aligned}


$$

Substituting the above into the given integral, we get

$$


\int \dfrac{2}{\sqrt{x^2-4x+3}} \textrm{d}x = \int \dfrac{2}{\sqrt {(x-2)^2-1} } \, \textrm{d}x.


$$

Let $u = x-2.$ Then, we have

$$


\dfrac{\textrm{d}u}{\textrm{d}x}=1 \quad\Longrightarrow\quad \textrm{d}x = \textrm{d}u.


$$

Therefore,

$$


\begin{aligned}\begin{aligned}∫\frac{2}{\sqrt{√𝑥^{2}−4𝑥+3}}d𝑥 & =∫\frac{2}{\sqrt{√(𝑥−2)^{2}−1}}\,d𝑥 \\ & =2∫\frac{1}{\sqrt{√𝑢^{2}−1}}d𝑢 \\ & =2arcosh⁡𝑢+𝐶 \\ & =2arcosh⁡(𝑥−2)+𝐶.\end{aligned}\end{aligned}


$$

### Example: Completing the Square to Compute a Hyperbolic Arctangent Integral

#### Question

$\displaystyle \int \dfrac{1}{4x-x^2} \textrm{d}x=$

#### Explanation

First, we complete the square for the denominator:

$$


\begin{aligned} 4x-x^2 & = -(x^2 - 4x)\\\[5pt] & = -(x^2 - 2\cdot 2x + 2^2-2^2)\\\[5pt] & = -((x-2)^2 - 4) \\\[5pt] &= 4 - (x-2)^2 \end{aligned}


$$

Substituting the above into the denominator of our integral, we get

$$


\int \dfrac{1}{4x-x^2}\textrm{d}x = \int \dfrac{1}{4-(x-2)^2}\textrm{d}x = \dfrac{1}{4} {\int}\dfrac{1}{ 1 - \left( \frac{1}{2}(x-2)\right)^2 }\textrm{d}x.


$$

Let $u = \dfrac{1}{2}(x-2).$ Then, we have

$$


\dfrac{\textrm{d}u}{\textrm{d}x}=\dfrac{1}{2} \quad\Longrightarrow\quad \textrm{d}x = 2\,\textrm{d}u.


$$

Therefore,

$$


\begin{aligned}\frac{1}{4}∫\frac{1}{1−(\frac{1}{2}(𝑥−2))^{2}}d𝑥 & =\frac{1}{4}∫\frac{1}{1−𝑢^{2}}⋅2\,d𝑢 \\ & =\frac{1}{2}∫\frac{1}{1−𝑢^{2}}\,d𝑢 \\ & =\frac{1}{2}⋅artanh⁡𝑢+𝐶 \\ & =\frac{1}{2}artanh⁡(\frac{𝑥−2}{2})+𝐶.\end{aligned}


$$

Note that this result is subject to the condition $\left|\dfrac {x-2} {2} \right| < 1.$
