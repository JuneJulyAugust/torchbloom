# Integration Using Inverse Reciprocal Hyperbolic Functions and Completing the Square

Source: https://www.mathacademy.com/topics/3264?courseId=106
Topic ID: 3264

## Prerequisites

- [Integration by Substitution With Inverse Reciprocal Hyperbolic Functions](./3259-integration-by-substitution-with-inverse-reciprocal-hyperbolic-functions.md)
- [Integration Using Hyperbolic Functions and Completing the Square](./3263-integration-using-hyperbolic-functions-and-completing-the-square.md)

## Lesson

### Introduction

We can also complete the square to integrate hyperbolic *arcsecant*, *arccosecant*, and *arccotangent*.

For example, let's consider the integral

$$


\int \dfrac{1}{\left(x+3\right)\sqrt{-x^2-6x}} \text{d}x.


$$

As it is, this integral doesn't resemble any of the basic integrals we have encountered so far. However, we can complete the square for the argument of the square root in the denominator, as follows:

$$


\begin{aligned}−𝑥^{2}−6𝑥 & =−(𝑥^{2}+6𝑥) \\ & =−(𝑥^{2}+2⋅3𝑥+3^{2}−3^{2}) \\ & =−((𝑥+3)^{2}−9) \\ & =9−(𝑥+3)^{2}\end{aligned}


$$

If we plug the above into our integral and collect a factor of $9$ under the square root, we get

$$


\begin{aligned}∫\frac{1}{(𝑥+3)\sqrt{−𝑥^{2}−6𝑥}}d𝑥 & =∫\frac{1}{(𝑥+3)\sqrt{9−(𝑥+3)^{2}}}\,d𝑥 \\ & =∫\frac{1}{3(𝑥+3)\sqrt{1−(\frac{𝑥+3}{3})^{2}}}\,d𝑥 \\ & =\frac{1}{9}∫\frac{1}{(\frac{𝑥+3}{3})\sqrt{1−(\frac{𝑥+3}{3})^{2}}}\,d𝑥.\end{aligned}


$$

This now looks more familiar! Let $u = \dfrac {x+3}{3}.$ Then

$$


\dfrac{\text{d}u}{\text{d}x}=\dfrac{1}{3} \quad\Longrightarrow\quad \text{d}x = 3\,\text{d}u.


$$

We can now write the integral as

$$


\begin{aligned}∫\frac{1}{(𝑥+3)\sqrt{−𝑥^{2}−6𝑥}}d𝑥 & =\frac{1}{9}∫\frac{1}{(\frac{𝑥+3}{3})\sqrt{1−(\frac{𝑥+3}{3})^{2}}}\,d𝑥 \\ & =\frac{1}{9}∫\frac{1}{𝑢\sqrt{1−𝑢^{2}}}⋅(3\,d𝑢) \\ & =\frac{1}{3}∫\frac{1}{𝑢\sqrt{1−𝑢^{2}}}\,d𝑢.\end{aligned}


$$

This is a basic integral for an inverse reciprocal hyperbolic function, and we can solve it in one step: $$

$$


\begin{aligned}\frac{1}{3}∫\frac{1}{𝑢\sqrt{1−𝑢^{2}}}\,d𝑢 & =−\frac{1}{3}arsech⁡𝑢+𝐶 \\ & =−\frac{1}{3}arsech⁡(\frac{𝑥+3}{3})+𝐶.\end{aligned}


$$

### Example: Computing an Inverse Reciprocal Hyperbolic Integral Containing a Completed Square

#### Question

Calculate $\displaystyle \int \dfrac{1}{4-(2x-2)^2} \text{d}x.$

#### Explanation

First, we note that

$$


\int \dfrac{1}{4-(2x-2)^2}\text{d}x = \int \dfrac{1}{4-4(x-1)^2}\text{d}x = \dfrac{1}{4} {\int}\dfrac{1}{ 1 - (x-1)^2 }\text{d}x.


$$

Let $u = x-1.$ Then, we have

$$


\dfrac{\text{d}u}{\text{d}x}=1 \quad\Longrightarrow\quad \text{d}x = \text{d}u.


$$

Therefore,

$$


\begin{aligned}\frac{1}{4}∫\frac{1}{1−(𝑥−1)^{2}}d𝑥 & =\frac{1}{4}∫\frac{1}{1−𝑢^{2}}⋅d𝑢 \\ & =\frac{1}{4}⋅arcoth⁡𝑢+𝐶 \\ & =\frac{1}{4}arcoth⁡(𝑥−1)+𝐶.\end{aligned}


$$

Note that this result is subject to the condition $\left|{x-1} \right| > 1.$

### Example: Completing the Square to Compute a Hyperbolic Arsecant Integral

#### Question

${\displaystyle \int \dfrac{1}{(x-1)\sqrt{2x-x^2}} \text{d}x=}$

#### Explanation

First, we complete the square for the argument of the square root in the denominator:

$$


\begin{aligned} 2x-x^2 & = -(x^2 - 2x)\\[5pt] & = -(x^2 - 2\cdot x + 1^2-1^2)\\[5pt] & = -((x-1)^2 - 1) \\[5pt] &= 1 - (x-1)^2 \end{aligned}


$$

Substituting the above into the given integral, we get

$$


\int \dfrac{1}{(x-1)\sqrt{2x-x^2}} \text{d}x = \int \dfrac{1}{(x-1)\sqrt { 1-(x-1)^2 } } \, \text{d}x.


$$

Let $u = x-1.$ Then, we have

$$


\dfrac{\text{d}u}{\text{d}x}=1 \quad\Longrightarrow\quad \text{d}x = \text{d}u.


$$

Therefore,

$$


\begin{aligned}\begin{matrix}∫\frac{1}{(𝑥−1)\sqrt{2𝑥−𝑥^{2}}}d𝑥 & =∫\frac{1}{(𝑥−1)\sqrt{1−(𝑥−1)^{2}}}\,d𝑥 \\ & =∫\frac{1}{𝑢\sqrt{1−𝑢^{2}}}d𝑢 \\ & =−arsech⁡𝑢+𝐶 \\ & =−arsech⁡(𝑥−1)+𝐶.\end{matrix}\end{aligned}


$$

### Example: Completing the Square to Compute a Hyperbolic Arcosecant Integral

#### Question

${\displaystyle \int \dfrac{6}{|3x+9|\sqrt{x^2+6x+10}} \text{d}x=}$

#### Explanation

First, we complete the square for the argument of the square root in the denominator:

$$


\begin{aligned}𝑥^{2}+6𝑥+10 & =𝑥^{2}+2⋅3𝑥+3^{2}−3^{2}+10 \\ & =(𝑥+3)^{2}+1\end{aligned}


$$

Substituting the above into the given integral, we get

$$


\int \dfrac{6}{|3x\!+\!9|\sqrt{x^2\!+\!6x\!+\!10}} \,\text{d}x = \int \dfrac{6}{3|x\!+\!3|\sqrt {1\!+\!(x\!+\!3)^2} } \, \text{d}x = {2} \int \dfrac{1}{|x\!+\!3|\sqrt{1\!+\!(x\!+\!3)^2}} \, \text{d}x.


$$

Let $u = x+3.$ Then, we have

$$


\dfrac{\text{d}u}{\text{d}x}=1 \quad\Longrightarrow\quad \text{d}x = \text{d}u.


$$

Therefore,

$$


\begin{aligned}\begin{matrix}2∫\frac{1}{|𝑥+3|\sqrt{1+(𝑥+3)^{2}}}d𝑥 & =2∫\frac{1}{|𝑢|\sqrt{1+𝑢^{2}}}\,d𝑢 \\ & =−2arcsch⁡𝑢+𝐶 \\ & =−2arcsch⁡(𝑥+3)+𝐶.\end{matrix}\end{aligned}


$$

### Example: Completing the Square to Compute a Hyperbolic Arcotangent Integral

#### Question

$\displaystyle \int \dfrac{1}{3-2x-x^2} \text{d}x=$

#### Explanation

First, we complete the square for the denominator:

$$


\begin{aligned} 3-2x-x^2 & = -(x^2 + 2x - 3)\\[5pt] & = -(x^2 + 2\cdot x +1^2 - 1^2 - 3)\\[5pt] & = -((x+1)^2 - 4) \\[5pt] &= 4 - (x+1)^2 \end{aligned}


$$

Substituting the above into the denominator of our integral, we get

$$


\int \dfrac{1}{3-2x-x^2}\text{d}x = \int \dfrac{1}{4-(x+1)^2}\text{d}x = \dfrac{1}{4} {\int}\dfrac{1}{ 1 - \left( \frac{1}{2}(x+1)\right)^2 }\text{d}x.


$$

Let $u = \dfrac{1}{2}(x+1).$ Then, we have

$$


\dfrac{\text{d}u}{\text{d}x}=\dfrac{1}{2} \quad\Longrightarrow\quad \text{d}x = 2\,\text{d}u.


$$

Therefore,

$$


\begin{aligned}\frac{1}{4}∫\frac{1}{1−(\frac{1}{2}(𝑥+1))^{2}}d𝑥 & =\frac{1}{4}∫\frac{1}{1−𝑢^{2}}⋅2\,d𝑢 \\ & =\frac{1}{2}∫\frac{1}{1−𝑢^{2}}\,d𝑢 \\ & =\frac{1}{2}⋅arcoth⁡𝑢+𝐶 \\ & =\frac{1}{2}⋅arcoth⁡(\frac{1}{2}(𝑥+1))+𝐶 \\ & =\frac{1}{2}arcoth⁡(\frac{𝑥+1}{2})+𝐶.\end{aligned}


$$

Note that this result is subject to the condition $\left|\dfrac {x+1} {2} \right| > 1.$
