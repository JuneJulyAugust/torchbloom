# Integration Using Inverse Trigonometric Functions

Source: https://www.mathacademy.com/topics/342?courseId=136
Topic ID: 342

## Prerequisites

- [Differentiating Inverse Reciprocal Trigonometric Functions](./1721-differentiating-inverse-reciprocal-trigonometric-functions.md)
- [Dividing Polynomials by Manipulating Rational Expressions](../../../high-school/traditional/lessons/algebra-ii/2883-dividing-polynomials-by-manipulating-rational-expressions.md)
- [The Sum Rule for Indefinite Integrals](../../../ap-courses/lessons/ap-calculus-ab/3769-the-sum-rule-for-indefinite-integrals.md)

## Lesson

### Introduction

Recall the following derivatives of the inverse trigonometric functions:

$$


\begin{aligned}\frac{d}{d𝑥}(arcsin⁡𝑥) & =\frac{1}{\sqrt{√1−𝑥^{2}}} \\ \frac{d}{d𝑥}(arctan⁡𝑥) & =\frac{1}{1+𝑥^{2}} \\ \frac{d}{d𝑥}(arcsec\,𝑥) & =\frac{1}{|𝑥|\sqrt{√𝑥^{2}−1}}\end{aligned}


$$

Since integration is the opposite of differentiation, we arrive at the following results:

$$


\begin{aligned}∫\frac{1}{\sqrt{√1−𝑥^{2}}}d𝑥 & =arcsin⁡(𝑥)+𝐶 \\ ∫\frac{1}{1+𝑥^{2}}d𝑥 & =arctan⁡(𝑥)+𝐶 \\ ∫\frac{1}{|𝑥|\sqrt{√𝑥^{2}−1}}d𝑥 & =arcsec(𝑥)+𝐶\end{aligned}


$$

### Example: Integrating Using Arcsine

#### Question

Calculate the indefinite integral $\displaystyle \int \frac{3}{\sqrt{1-x^2}}\textrm{d}x.$

#### Explanation

Recall that

$$


\int \frac{1}{\sqrt{1-x^2}}\textrm{d}x = \arcsin (x) + C.


$$

Therefore, we have

$$


\begin{aligned}∫\frac{3}{\sqrt{√1−𝑥^{2}}}d𝑥 & =3∫\frac{1}{\sqrt{√1−𝑥^{2}}}d𝑥 \\ & =3arcsin⁡(𝑥)+𝐶.\end{aligned}


$$

### Example: Integrating Using Arctangent

#### Question

Calculate $\displaystyle \int \frac{2}{1+x^2}\textrm{d}x.$

#### Explanation

Recall that

$$


\int \frac{1}{1+x^2}\textrm{d}x = \arctan{x} + C.


$$

Therefore, we have

$$


\begin{aligned}∫\frac{2}{1+𝑥^{2}}d𝑥 & =2∫\frac{1}{1+𝑥^{2}}d𝑥 \\ & =2arctan⁡𝑥+𝐶.\end{aligned}


$$

### Example: Integrating Using Arcsecant

#### Question

If $f'(x) = \dfrac{5}{|x|\sqrt{x^2 - 1}} - 2x,$ then $f(x)=$

#### Explanation

Recall that

$$


\int \dfrac{1}{|x|\sqrt{x^2 - 1}} \, \textrm dx = \textrm{arcsec} \, x.


$$

Then we have

$$


\begin{aligned}\begin{aligned}𝑓(𝑥) & =∫𝑓^{′}(𝑥)\,d𝑥 \\ & =∫(\frac{5}{|𝑥|\sqrt{√𝑥^{2}−1}}−2𝑥)d𝑥 \\ & =∫\frac{5}{|𝑥|\sqrt{√𝑥^{2}−1}}\,d𝑥−∫2𝑥\,d𝑥 \\ & =5∫\frac{1}{|𝑥|\sqrt{√𝑥^{2}−1}}\,d𝑥−2∫𝑥\,d𝑥 \\ & =5arcsec\,(𝑥)−2⋅\frac{𝑥^{2}}{2}+𝐶 \\ & =5arcsec\,(𝑥)−𝑥^{2}+𝐶.\end{aligned}\end{aligned}


$$

### Example: Integrating Using Inverse Trigonometric Functions and Some Manipulations

#### Question

Evaluate the integral $\displaystyle \int \dfrac {x^2+2}{x^2 + 1}\, \textrm{d}x.$

#### Explanation

This integral doesn't look like one of the basic ones. However, we can manipulate the numerator a bit to make it look more like the denominator, which reveals a more familiar expression:

$$


\begin{aligned}\frac{𝑥^{2}+2}{𝑥^{2}+1} & =\frac{𝑥^{2}+1+1}{𝑥^{2}+1} \\ & =\frac{𝑥^{2}+1}{𝑥^{2}+1}+\frac{1}{𝑥^{2}+1} \\ & =1+\frac{1}{𝑥^{2}+1}.\end{aligned}


$$

Remembering that

$$


\int \dfrac{1}{x^2+1} \textrm dx = \arctan(x),


$$

we can now calculate the integral and get

$$


\begin{aligned}\begin{aligned}∫\frac{𝑥^{2}+2}{𝑥^{2}+1}\,d𝑥 & =∫(1+\frac{1}{𝑥^{2}+1})d𝑥 \\ & =∫1\,d𝑥+∫\frac{1}{𝑥^{2}+1}\,d𝑥 \\ & =𝑥+arctan⁡(𝑥)+𝐶.\end{aligned}\end{aligned}


$$
