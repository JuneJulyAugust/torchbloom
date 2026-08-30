# The Sum Rule for Indefinite Integrals

Source: https://www.mathacademy.com/topics/3769?courseId=24
Topic ID: 3769

## Prerequisites

- [The Constant Multiple Rule for Indefinite Integrals](./43-the-constant-multiple-rule-for-indefinite-integrals.md)

## Lesson

### Introduction

How can we calculate the integral of a sum of functions, like $\displaystyle \int (x+x^3)\,\textrm d x?$

According to the **sum rule**, the integral of the sum of functions is equal to the sum of the integrals of each function:

$$


\int (f(x) \pm g(x))\,\textrm d x = \int f(x) \,\textrm d x \pm \int g(x) \,\textrm d x.


$$

In our case, we have

$$


\begin{aligned}∫(𝑥+𝑥^{3})\,d𝑥 & =∫𝑥\,d𝑥+∫𝑥^{3}\,d𝑥 \\ & =(\frac{𝑥^{2}}{2}+𝑐_{1})+(\frac{𝑥^{4}}{4}+𝑐_{2}) \\ & =\frac{1}{2}𝑥^{2}+\frac{1}{4}𝑥^{4}+(𝑐_{1}+𝑐_{2}) \\ & =\frac{1}{2}𝑥^{2}+\frac{1}{4}𝑥^{4}+𝐶,\end{aligned}


$$

where we renamed $c_1+c_2=C.$ (The sum of two arbitrary constants is itself an arbitrary constant.)

### Example: Computing an Integral Using the Sum Rule

#### Question

Find the integral of $x^2 + 1.$

#### Explanation

Applying the sum rule, we compute the sum of the integrals of each function:

$$


\begin{aligned}∫𝑥^{2}+1\,d𝑥 & =∫𝑥^{2}\,d𝑥+∫1\,d𝑥 \\ & =∫𝑥^{2}\,d𝑥+∫𝑥^{0}\,d𝑥 \\ & =(\frac{𝑥^{2+1}}{2+1})+𝑥+𝐶 \\ & =\frac{1}{3}𝑥^{3}+𝑥+𝐶\end{aligned}


$$

### Combining the Constant Factor and Sum Rules

For more complicated functions consisting of the sum of functions multiplied by constants, we can combine the constant factor and sum rules as follows:

$$


\int k_1 f(x) \pm k_2 g(x)\,\textrm d x = k_1\int f(x) \,\textrm d x \pm k_2\int g(x) \,\textrm d x


$$

### Example: Computing an Integral Using the Sum and Constant Factor Rules

#### Question

Calculate $\displaystyle \int 2 x^3 - x \,\textrm d x.$

#### Explanation

Using the sum and constant factor rules, we get

$$


\begin{aligned}∫2𝑥^{3}−𝑥\,d𝑥 & =2∫𝑥^{3}\,d𝑥−∫𝑥\,d𝑥 \\ & =2(\frac{𝑥^{3+1}}{3+1})−(\frac{𝑥^{1+1}}{1+1})+𝐶 \\ & =2(\frac{𝑥^{4}}{4})−(\frac{𝑥^{2}}{2})+𝐶 \\ & =\frac{𝑥^{4}}{2}−\frac{𝑥^{2}}{2}+𝐶.\end{aligned}


$$

### Example: Integrating Sums of Power Functions

#### Question

Calculate $\displaystyle \int \left(5(\sqrt{x})^{3} - 4 x^2 + 5\right) \,\textrm d x.$

#### Explanation

Using the sum and constant factor rules, we get

$$


\begin{aligned}∫(5(\sqrt{√𝑥})^{3}−4𝑥^{2}+5)\,d𝑥 & =∫(5𝑥^{3/2}−4𝑥^{2}+5)\,d𝑥 \\ & =5∫𝑥^{3/2}\,d𝑥−4∫𝑥^{2}d𝑥+5∫1\,d𝑥 \\ & =5\frac{𝑥^{5/2}}{\frac{5}{2}}−4(\frac{𝑥^{3}}{3})+5(𝑥)+𝐶 \\ & =5⋅\frac{2}{5}𝑥^{5/2}−\frac{4}{3}𝑥^{3}+5𝑥+𝐶 \\ & =2\sqrt{√𝑥^{5}}−\frac{4}{3}𝑥^{3}+5𝑥+𝐶.\end{aligned}


$$
