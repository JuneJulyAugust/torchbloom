# Integrating Products of Trigonometric Functions

Source: https://www.mathacademy.com/topics/3224?courseId=106
Topic ID: 3224

## Prerequisites

- [The Sum and Difference Formulas for Sine](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/270-the-sum-and-difference-formulas-for-sine.md)
- [The Sum and Difference Formulas for Cosine](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/274-the-sum-and-difference-formulas-for-cosine.md)
- [Integration Using Basic Trigonometric Identities](./282-integration-using-basic-trigonometric-identities.md)

## Lesson

### Introduction

When an integrand contains a product of trigonometric functions, we can often rewrite that product as a sum using the sum and difference formulas. Then, the integral becomes a sum of simpler integrals.

First, let's recall the sum and difference formulas for cosine:

$$


\begin{aligned}cos⁡(𝛼−𝛽) & =cos⁡𝛼cos⁡𝛽+sin⁡𝛼sin⁡𝛽 \\ cos⁡(𝛼+𝛽) & =cos⁡𝛼cos⁡𝛽−sin⁡𝛼sin⁡𝛽\end{aligned}


$$

Adding these equations, we get

$$


\cos(\alpha-\beta) + \cos(\alpha+\beta) = 2 \cos \alpha \cos \beta.


$$

Now, solving for $\cos \alpha \cos \beta,$ we obtain the following **product-to-sum identity**:

$$


\cos \alpha \cos \beta = \dfrac{1}{2}\left(\cos(\alpha-\beta)+\cos(\alpha+\beta)\right)


$$

For example, consider the integral

$$


\displaystyle \int \cos(5x)\cos(3x)\,\text{d}x.


$$

Using the identity above,

$$


\begin{aligned}cos⁡(5𝑥)cos⁡(3𝑥) & =\frac{1}{2}(cos⁡(5𝑥−3𝑥)+cos⁡(5𝑥+3𝑥)) \\ & =\frac{1}{2}(cos⁡(2𝑥)+cos⁡(8𝑥)).\end{aligned}


$$

Therefore,

$$


\begin{aligned}∫cos⁡(5𝑥)cos⁡(3𝑥)\,d𝑥 & =∫\frac{1}{2}cos⁡(2𝑥)+\frac{1}{2}cos⁡(8𝑥)\,d𝑥 \\ & =\frac{1}{4}sin⁡(2𝑥)+\frac{1}{16}sin⁡(8𝑥)+𝐶,\end{aligned}


$$

where $C$ is an arbitrary constant.

### Example: Integrating a Product of Cosines

#### Question

Evaluate the integral $\displaystyle \int_{\pi/4}^{\pi/2} \cos(9x)\cos(x)\,\text{d}x.$

#### Explanation

First, let's recall the sum and difference formulas for cosine:

$$


\begin{aligned}cos⁡(𝛼−𝛽) & =cos⁡𝛼cos⁡𝛽+sin⁡𝛼sin⁡𝛽 \\ cos⁡(𝛼+𝛽) & =cos⁡𝛼cos⁡𝛽−sin⁡𝛼sin⁡𝛽\end{aligned}


$$

Adding these equations, we get the following product-to-sum identity:

$$


\begin{aligned}cos⁡(𝛼−𝛽)+cos⁡(𝛼+𝛽) & =2cos⁡𝛼cos⁡𝛽 \\ cos⁡𝛼cos⁡𝛽 & =\frac{1}{2}(cos⁡(𝛼−𝛽)+cos⁡(𝛼+𝛽))\end{aligned}


$$

Thus, we have

$$


\begin{aligned}cos⁡(9𝑥)cos⁡(𝑥) & =\frac{1}{2}(cos⁡(9𝑥−𝑥)+cos⁡(9𝑥+𝑥)) \\ & =\frac{1}{2}(cos⁡(8𝑥)+cos⁡(10𝑥)).\end{aligned}


$$

Substituting this into the integral gives

$$


\begin{aligned}∫_{𝜋/2𝜋/4}cos⁡(9𝑥)cos⁡(𝑥)\,d𝑥 & =∫_{𝜋/2𝜋/4}\frac{1}{2}cos⁡(8𝑥)+\frac{1}{2}cos⁡(10𝑥)\,d𝑥 \\ & =[\frac{1}{16}sin⁡(8𝑥)+\frac{1}{20}sin⁡(10𝑥)]_{𝜋/2𝜋/4} \\ & =\frac{1}{16}(sin⁡(4𝜋)−sin⁡(2𝜋))+\frac{1}{20}(sin⁡(5𝜋)−sin⁡(\frac{5𝜋}{2})) \\ & =\frac{1}{16}(0−0)+\frac{1}{20}(0−1) \\ & =−\frac{1}{20}.\end{aligned}


$$

### Integrating a Product of Sines

Similar to the above, when an integrand contains a product of sines, we can rewrite that product as a sum of cosines using the sum and difference formulas for cosine. Then, the integral becomes a sum of simpler integrals.

First, let's recall the sum and difference formulas for cosine:

$$


\begin{aligned}cos⁡(𝛼−𝛽) & =cos⁡𝛼cos⁡𝛽+sin⁡𝛼sin⁡𝛽 \\ cos⁡(𝛼+𝛽) & =cos⁡𝛼cos⁡𝛽−sin⁡𝛼sin⁡𝛽\end{aligned}


$$

Subtracting the second equation from the first, we get

$$


\cos(\alpha-\beta) - \cos(\alpha+\beta) = 2 \sin \alpha \sin \beta.


$$

Now, solving for $\sin \alpha \sin \beta,$ we obtain the following *product-to-sum identity*:

$$


\sin \alpha \sin \beta = \dfrac{1}{2}\left(\cos(\alpha-\beta)-\cos(\alpha+\beta)\right)


$$

For example, consider the integral

$$


\displaystyle \int \sin(7x)\sin(4x)\,\text{d}x.


$$

Using the identity above,

$$


\begin{aligned}sin⁡(7𝑥)sin⁡(4𝑥) & =\frac{1}{2}(cos⁡(7𝑥−4𝑥)−cos⁡(7𝑥+4𝑥)) \\ & =\frac{1}{2}(cos⁡(3𝑥)−cos⁡(11𝑥)).\end{aligned}


$$

Therefore,

$$


\begin{aligned}∫sin⁡(7𝑥)sin⁡(4𝑥)\,d𝑥 & =∫\frac{1}{2}cos⁡(3𝑥)−\frac{1}{2}cos⁡(11𝑥)\,d𝑥 \\ & =\frac{1}{6}sin⁡(3𝑥)−\frac{1}{22}sin⁡(11𝑥)+𝐶,\end{aligned}


$$

where $C$ is an arbitrary constant.

### Example: Integrating a Product of Sines

#### Question

Evaluate the integral $\displaystyle \int \sin(12x)\sin(5x)\,\text{d}x.$

#### Explanation

First, let's recall the sum and difference formulas for cosine:

$$


\begin{aligned}cos⁡(𝛼−𝛽) & =cos⁡𝛼cos⁡𝛽+sin⁡𝛼sin⁡𝛽 \\ cos⁡(𝛼+𝛽) & =cos⁡𝛼cos⁡𝛽−sin⁡𝛼sin⁡𝛽\end{aligned}


$$

Subtracting the second equation from the first, we get the following product-to-sum identity:

$$


\begin{aligned}cos⁡(𝛼−𝛽)−cos⁡(𝛼+𝛽) & =2sin⁡𝛼sin⁡𝛽 \\ sin⁡𝛼sin⁡𝛽 & =\frac{1}{2}(cos⁡(𝛼−𝛽)−cos⁡(𝛼+𝛽))\end{aligned}


$$

Thus, we have

$$


\begin{aligned}sin⁡(12𝑥)sin⁡(5𝑥) & =\frac{1}{2}(cos⁡(12𝑥−5𝑥)−cos⁡(12𝑥+5𝑥)) \\ & =\frac{1}{2}(cos⁡(7𝑥)−cos⁡(17𝑥)).\end{aligned}


$$

Substituting this into the integral gives

$$


\begin{aligned}∫sin⁡(12𝑥)sin⁡(5𝑥)\,d𝑥 & =∫\frac{1}{2}cos⁡(7𝑥)−\frac{1}{2}cos⁡(17𝑥)\,d𝑥 \\ & =\frac{1}{14}sin⁡(7𝑥)−\frac{1}{34}sin⁡(17𝑥)+𝐶,\end{aligned}


$$

where $C$ is an arbitrary constant.

### Integrating a Product of Sine and Cosine

Next, when an integrand contains a product of sine and cosine, we can rewrite that product as a sum of sines using the sum and difference formulas for sine. Then, the integral becomes a sum of simpler integrals.

First, let's recall the sum and difference formulas for sine:

$$


\begin{aligned}sin⁡(𝛼+𝛽) & =sin⁡𝛼cos⁡𝛽+cos⁡𝛼sin⁡𝛽 \\ sin⁡(𝛼−𝛽) & =sin⁡𝛼cos⁡𝛽−cos⁡𝛼sin⁡𝛽\end{aligned}


$$

Adding these equations, we get

$$


\sin(\alpha+\beta) + \sin(\alpha-\beta) = 2 \sin \alpha \cos \beta.


$$

Now, solving for $\sin \alpha \cos \beta,$ we obtain the following *product-to-sum identity*:

$$


\sin \alpha \cos \beta = \dfrac{1}{2}\left(\sin(\alpha+\beta)+\sin(\alpha-\beta)\right)


$$

For example, consider the integral

$$


\displaystyle \int \sin(8x)\cos(2x)\,\text{d}x.


$$

Using the identity above,

$$


\begin{aligned}sin⁡(8𝑥)cos⁡(2𝑥) & =\frac{1}{2}(sin⁡(8𝑥+2𝑥)+sin⁡(8𝑥−2𝑥)) \\ & =\frac{1}{2}(sin⁡(10𝑥)+sin⁡(6𝑥)).\end{aligned}


$$

Therefore,

$$


\begin{aligned}∫sin⁡(8𝑥)cos⁡(2𝑥)\,d𝑥 & =∫\frac{1}{2}sin⁡(10𝑥)+\frac{1}{2}sin⁡(6𝑥)\,d𝑥 \\ & =−\frac{1}{20}cos⁡(10𝑥)−\frac{1}{12}cos⁡(6𝑥)+𝐶,\end{aligned}


$$

where $C$ is an arbitrary constant.

### Example: Integrating a Product of Sine and Cosine

#### Question

Evaluate the integral $\displaystyle \int_{0}^{\pi/2} \sin(2x)\cos(4x)\,\text{d}x.$

#### Explanation

First, let's recall the sum and difference formulas for sine:

$$


\begin{aligned}sin⁡(𝛼+𝛽) & =sin⁡𝛼cos⁡𝛽+cos⁡𝛼sin⁡𝛽 \\ sin⁡(𝛼−𝛽) & =sin⁡𝛼cos⁡𝛽−cos⁡𝛼sin⁡𝛽\end{aligned}


$$

Adding these equations, we get the following product-to-sum identity:

$$


\begin{aligned}sin⁡(𝛼+𝛽)+sin⁡(𝛼−𝛽) & =2sin⁡𝛼cos⁡𝛽 \\ sin⁡𝛼cos⁡𝛽 & =\frac{1}{2}(sin⁡(𝛼+𝛽)+sin⁡(𝛼−𝛽))\end{aligned}


$$

Thus, we have

$$


\begin{aligned}sin⁡(2𝑥)cos⁡(4𝑥) & =\frac{1}{2}(sin⁡(2𝑥+4𝑥)+sin⁡(2𝑥−4𝑥)) \\ & =\frac{1}{2}(sin⁡(6𝑥)+sin⁡(−2𝑥)) \\ & =\frac{1}{2}(sin⁡(6𝑥)−sin⁡(2𝑥)).\end{aligned}


$$

Substituting this into the integral gives

$$


\begin{aligned}∫_{𝜋/20}sin⁡(2𝑥)cos⁡(4𝑥)\,d𝑥 & =∫_{𝜋/20}\frac{1}{2}sin⁡(6𝑥)−\frac{1}{2}sin⁡(2𝑥)\,d𝑥 \\ & =[−\frac{1}{12}cos⁡(6𝑥)+\frac{1}{4}cos⁡(2𝑥)]_{𝜋/20} \\ & =−\frac{1}{12}(cos⁡(3𝜋)−cos⁡(0))+\frac{1}{4}(cos⁡(𝜋)−cos⁡(0)) \\ & =−\frac{1}{12}(−1−1)+\frac{1}{4}(−1−1) \\ & =−\frac{1}{3}.\end{aligned}


$$
