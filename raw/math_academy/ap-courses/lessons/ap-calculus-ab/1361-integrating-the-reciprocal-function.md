# Integrating the Reciprocal Function

Source: https://www.mathacademy.com/topics/1361?courseId=24
Topic ID: 1361

## Prerequisites

- [Combining the Laws of Logarithms](../../../high-school/traditional/lessons/algebra-ii/30-combining-the-laws-of-logarithms.md)
- [Differentiating Logarithmic Functions](./1116-differentiating-logarithmic-functions.md)
- [The Sum Rule for Indefinite Integrals](./3769-the-sum-rule-for-indefinite-integrals.md)

## Lesson

### Introduction

Recall that for $x >0,$ we have

$$


\dfrac{\textrm d }{\textrm d x}(\ln{x}) = \dfrac 1 x.


$$

We can generalize this to all values $x\neq 0$ by including an absolute value inside the natural logarithm:

$$


\dfrac{\textrm d }{\textrm d x}(\ln{|x|}) = \dfrac 1 x.


$$

Therefore, the integral of the reciprocal function is

$$


\int \dfrac 1 x \,\textrm{d}x = \ln |x| + C.


$$

### Example: Integrating a Reciprocal Function

#### Question

Calculate $\displaystyle\int \left(\dfrac 2 x\right)\, \textrm{d} x.$

#### Explanation

First, we apply the constant factor rule and take the coefficient $2$ out of the integral. Then we compute the integral of $\dfrac 1 x,$ and get

$$


\begin{aligned}∫(\frac{2}{𝑥})\,d𝑥 & =2∫\frac{1}{𝑥}\,d𝑥 \\ & =2ln⁡|𝑥|+𝐶.\end{aligned}


$$

### Example: Integrating the Sum of a Reciprocal Function and a Power Function

#### Question

Find the integral of $\dfrac 1 {2x} + 3x$ with respect to $x.$

#### Explanation

Applying the sum and constant factor rules, we get

$$


\begin{aligned}∫(\frac{1}{2𝑥}+3𝑥)\,d𝑥 & =∫\frac{1}{2𝑥}\,d𝑥+∫3𝑥\,d𝑥 \\ & =\frac{1}{2}∫\frac{1}{𝑥}\,d𝑥+3∫𝑥\,d𝑥 \\ & =\frac{1}{2}ln⁡|𝑥|+3⋅\frac{𝑥^{1+1}}{1+1}+𝐶 \\ & =\frac{ln⁡|𝑥|}{2}+\frac{3𝑥^{2}}{2}+𝐶.\end{aligned}


$$

### Simplifying the Arbitrary Constant Using the Laws of Logarithms

For any constant $C,$ we can always write $C = \ln K,$ where $K>0$ is some other constant. Then, using the laws of logarithms, we can write

$$


\begin{aligned}∫\frac{1}{𝑥}\,d𝑥 & =ln⁡|𝑥|+𝐶 \\ & =ln⁡|𝑥|+ln⁡𝐾 \\ & =ln⁡(𝐾|𝑥|).\end{aligned}


$$

### Example: Integrating a Reciprocal Function and Simplifying the Arbitrary Constant Using the Laws of Logarithms

#### Question

What is the antiderivative of $\dfrac {3+2x} {x}?$

#### Explanation

We separate the integrand into the sum of two fractions so that we can simplify each term. So, we get

$$


\begin{aligned}∫\frac{3+2𝑥}{𝑥}\,d𝑥 & =∫(\frac{3}{𝑥}+\frac{2𝑥}{𝑥})\,d𝑥 \\ & =∫(\frac{3}{𝑥}+2)\,d𝑥 \\ & =3∫\frac{1}{𝑥}\,d𝑥+2∫\,d𝑥 \\ & =3ln⁡|𝑥|+2𝑥+𝐶.\end{aligned}


$$

Lastly, let's rewrite the constant so that we can combine it with the natural logarithm. For any constant $C,$ we can always write $C =3 \ln K$ where $K$ is some other constant. Doing this allows us to combine the constant with $3\ln|x|$ term, and we get

$$


\begin{aligned}∫\frac{3+2𝑥}{𝑥}\,d𝑥 & =3ln⁡|𝑥|+2𝑥+𝐶 \\ & =3ln⁡|𝑥|+2𝑥+3ln⁡𝐾 \\ & =3ln⁡(𝐾|𝑥|)+2𝑥.\end{aligned}


$$
