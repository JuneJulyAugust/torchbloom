# Integration Using Inverse Hyperbolic Functions

Source: https://www.mathacademy.com/topics/3253?courseId=105
Topic ID: 3253

## Prerequisites

- [Integrating Hyperbolic Functions](./304-integrating-hyperbolic-functions.md)
- [Integration Using Inverse Trigonometric Functions](./342-integration-using-inverse-trigonometric-functions.md)
- [Differentiating Inverse Hyperbolic Functions](./3252-differentiating-inverse-hyperbolic-functions.md)

## Lesson

### Introduction

Recall the following derivatives of the inverse hyperbolic functions: $$

$$


\begin{aligned}\frac{d}{d𝑥}(arsinh⁡𝑥) & =\frac{1}{\sqrt{𝑥^{2}+1}}, & & \,𝑥∈(−∞,∞) \\ \frac{d}{d𝑥}(arcosh⁡𝑥) & =\frac{1}{\sqrt{𝑥^{2}−1}}, & & \,𝑥∈(1,∞) \\ \frac{d}{d𝑥}(artanh⁡𝑥) & =\frac{1}{1−𝑥^{2}}, & & \,𝑥∈(−1,1)\end{aligned}


$$

Since integration is the reverse of differentiation, we arrive at the following basic integrals:

$$


\begin{aligned}∫\frac{1}{\sqrt{𝑥^{2}+1}}\,d𝑥 & =arsinh⁡𝑥+𝐶, & & \,𝑥∈(−∞,∞) \\ ∫\frac{1}{\sqrt{𝑥^{2}−1}}\,d𝑥 & =arcosh⁡𝑥+𝐶, & & \,𝑥∈(1,∞) \\ ∫\frac{1}{1−𝑥^{2}}\,d𝑥 & =artanh⁡𝑥+𝐶, & & \,𝑥∈(−1,1)\end{aligned}


$$

We can now use these formulas for finding integrals. For example, let's find the integral

$$


\int \left(\dfrac{5}{2\sqrt{x^2-1}} + 2x \right) \textrm d x


$$

Using the properties of integration and the formulas above, we obtain

$$


\begin{aligned}∫(\frac{5}{2\sqrt{𝑥^{2}−1}}+2𝑥)d𝑥 & =\frac{5}{2}∫\frac{1}{\sqrt{𝑥^{2}−1}}\,d𝑥+∫2𝑥\,d𝑥 \\ & =\frac{5}{2}arcosh⁡𝑥+𝑥^{2}+𝐶.\end{aligned}


$$

### Example: Integrating Using Arcsinh

#### Question

$$

$\displaystyle \int \dfrac{-3}{\sqrt{x^2+1}}\,\textrm d x=$

#### Explanation

$$

The derivative of the inverse hyperbolic sine function is given by

$$


\dfrac{\text{d}}{\text{d}x}(\operatorname{arsinh} x) = \dfrac{1}{\sqrt{x^2+1}}.


$$

Therefore, we have

$$


\begin{aligned}∫\frac{−3}{\sqrt{𝑥^{2}+1}}\,d𝑥=−3∫\frac{1}{\sqrt{𝑥^{2}+1}}\,d𝑥=−3arsinh⁡𝑥+𝐶.\end{aligned}


$$

### Example: Integrating Using Arcosh

#### Question

$$

$\displaystyle \int \dfrac{\ln{\pi}}{\sqrt{x^2-1}}\,\textrm d x=$

#### Explanation

$$

The derivative of the inverse hyperbolic cosine function is given by

$$


\dfrac{\text{d}}{\text{d}x}(\operatorname{arcosh} x) = \dfrac{1}{\sqrt{x^2-1}}.


$$

Therefore, we have

$$


\begin{aligned}∫\frac{ln⁡𝜋}{\sqrt{𝑥^{2}−1}}\,d𝑥=ln⁡𝜋∫\frac{1}{\sqrt{𝑥^{2}−1}}\,d𝑥=ln⁡𝜋arcosh⁡𝑥+𝐶.\end{aligned}


$$

### Example: Integrating Using Artanh

#### Question

$$

Calculate $\displaystyle \int \dfrac{1}{2(1-x^2)}\,\textrm d x$ for $|x|< 1.$

#### Explanation

$$

The derivative of the inverse hyperbolic tangent function is given by

$$


\dfrac{\text{d}}{\text{d}x}(\operatorname{artanh} x) = \dfrac{1}{1-x^2}.


$$

Therefore, we have

$$


\begin{aligned}∫\frac{1}{2(1−𝑥^{2})}\,d𝑥=\frac{1}{2}∫\frac{1}{1−𝑥^{2}}\,d𝑥=\frac{1}{2}\,artanh⁡𝑥+𝐶.\end{aligned}


$$
