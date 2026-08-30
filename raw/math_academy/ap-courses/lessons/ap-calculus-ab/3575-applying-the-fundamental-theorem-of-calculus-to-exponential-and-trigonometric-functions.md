# Applying the Fundamental Theorem of Calculus to Exponential and Trigonometric Functions

Source: https://www.mathacademy.com/topics/3575?courseId=24
Topic ID: 3575

## Prerequisites

- [The Fundamental Theorem of Calculus](./283-the-fundamental-theorem-of-calculus.md)
- [Integrating Trigonometric Functions](./285-integrating-trigonometric-functions.md)
- [Integrating Exponential Functions](./312-integrating-exponential-functions.md)

## Lesson

### Introduction

Besides polynomials, exponential and trigonometric functions are perhaps the most efficient functions in terms of calculating their definite integrals. Indeed, recall that the fundamental theorem of calculus states the following:

*If $f(x)$ is a function that's continuous on an interval $[a,b]$, and there exists a function $F(x)$ such that $F'(x) = f(x)$ on $[a,b]$, then*

$$


\int_a^b f(x)\,\text{d}x = F(b) - F(a).


$$

To illustrate this, let's calculate

$$


\int_1^3 2^x \,\text{d}x.


$$

Recall that the antiderivative of $2^x$ is $\dfrac{2^x}{\ln{2}}.$ Therefore, evaluating the difference at the bounds, we get

$$


\begin{aligned}∫_{31}2^{𝑥}\,d𝑥 & =\frac{2^{𝑥}}{ln⁡2}_{31} \\ & =\frac{1}{ln⁡2}(2^{3}−2^{1}) \\ & =\frac{1}{ln⁡2}(8−2) \\ & =\frac{6}{ln⁡2}.\end{aligned}


$$

### Example: Evaluating the Definite Integral of an Exponential Function

#### Question

Calculate $\displaystyle \int_{0}^5 e^x \, \textrm d x.$

#### Explanation

Taking the antiderivative and evaluating the difference at the bounds, we get

$$


\begin{aligned}∫_{50}𝑒^{𝑥}\,d𝑥 & =𝑒^{𝑥}_{50} \\ & =𝑒^{5}−𝑒^{0} \\ & =𝑒^{5}−1.\end{aligned}


$$

### Example: Evaluating the Definite Integral of a Trigonometric Function

#### Question

Evaluate $\displaystyle \int_{0}^{\pi/2} \cos x \,\text{d} x.$

#### Explanation

Taking the antiderivative and evaluating the difference at the bounds, we get

$$


\begin{aligned}∫_{𝜋/20}cos⁡𝑥\,d𝑥 & =sin⁡𝑥\,_{𝜋/20} \\ & =sin⁡(\frac{𝜋}{2})−sin⁡(0) \\ & =1−0 \\ & =1.\end{aligned}


$$
