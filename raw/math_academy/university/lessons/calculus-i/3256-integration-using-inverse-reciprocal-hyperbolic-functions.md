# Integration Using Inverse Reciprocal Hyperbolic Functions

Source: https://www.mathacademy.com/topics/3256?courseId=105
Topic ID: 3256

## Prerequisites

- [Integration Using Inverse Hyperbolic Functions](./3253-integration-using-inverse-hyperbolic-functions.md)
- [Differentiating Inverse Reciprocal Hyperbolic Functions](./3255-differentiating-inverse-reciprocal-hyperbolic-functions.md)

## Lesson

### Introduction

Recall the following derivatives of the inverse reciprocal hyperbolic functions: $$

$$


\begin{aligned}\frac{d}{d𝑥}(arcsch⁡𝑥) & =−\frac{1}{|𝑥|\sqrt{1+𝑥^{2}}}, & & \,𝑥∈(−∞,0)∪(0,∞) \\ \frac{d}{d𝑥}(arsech⁡𝑥) & =−\frac{1}{𝑥\sqrt{1−𝑥^{2}}}, & & \,𝑥∈(0,1) \\ \frac{d}{d𝑥}(arcoth⁡𝑥) & =\frac{1}{1−𝑥^{2}}, & & \,𝑥∈(−∞,−1)∪(1,∞)\end{aligned}


$$

Since integration is the reverse of differentiation, we arrive at the following basic integrals:

$$


\begin{aligned}∫\frac{1}{|𝑥|\sqrt{1+𝑥^{2}}}\,d𝑥 & =−arcsch⁡𝑥+𝐶, & & \,𝑥∈(−∞,0)∪(0,∞) \\ ∫\frac{1}{𝑥\sqrt{1−𝑥^{2}}}\,d𝑥 & =−arsech⁡𝑥+𝐶, & & \,𝑥∈(0,1) \\ ∫\frac{1}{1−𝑥^{2}}\,d𝑥 & =arcoth⁡𝑥+𝐶, & & \,𝑥∈(−∞,−1)∪(1,∞)\end{aligned}


$$

We can now use these formulas for finding integrals. For example, let's find the integral

$$


\int \left(\dfrac{2}{3x\sqrt{1-x^2}} + \cos x \right) \textrm d x.


$$

Using the properties of integration and the formulas above, we obtain

$$


\begin{aligned}∫(\frac{2}{3𝑥\sqrt{1−𝑥^{2}}}+cos⁡𝑥)d𝑥 & =\frac{2}{3}∫\frac{1}{𝑥\sqrt{1−𝑥^{2}}}\,d𝑥+∫cos⁡𝑥\,d𝑥 \\ & =−\frac{2}{3}arsech⁡𝑥+sin⁡𝑥+𝐶.\end{aligned}


$$

### Example: Integrating Using Arcsch

#### Question

$$

$\displaystyle \int \dfrac{1}{3|x|\sqrt{x^2+1}}\,\textrm d x=$

#### Explanation

$$

The formula for the derivative of the inverse hyperbolic cosecant function is

$$


\dfrac{\text{d}}{\text{d}x}(\operatorname{arcsch} x) = -\dfrac{1}{|x|\sqrt{1+ x^2}}.


$$

Therefore, we have

$$


\begin{aligned}∫\frac{1}{3|𝑥|\sqrt{𝑥^{2}+1}}\,d𝑥=−\frac{1}{3}∫−\frac{1}{|𝑥|\sqrt{1+𝑥^{2}}}\,d𝑥=−\frac{1}{3}arcsch⁡𝑥+𝐶.\end{aligned}


$$

### Example: Integrating Using Arsech

#### Question

$$

$\displaystyle \int \dfrac{3}{x\sqrt{1-x^2}}\,\textrm d x=$

#### Explanation

$$

The formula for the derivative of the inverse hyperbolic secant function is

$$


\dfrac{\text{d}}{\text{d}x}(\operatorname{arsech} x) = -\dfrac{1}{x\sqrt{1-x^2}}.


$$

Therefore, we have

$$


\begin{aligned}∫\frac{3}{𝑥\sqrt{1−𝑥^{2}}}\,d𝑥=−3∫−\frac{1}{𝑥\sqrt{1−𝑥^{2}}}\,d𝑥=−3arsech⁡𝑥+𝐶.\end{aligned}


$$

### Example: Integrating Using Arcoth

#### Question

$$

Calculate $\displaystyle \int \dfrac{8}{1-x^2}\,\textrm d x$ for $|x|>1.$

#### Explanation

$$

The formula for the derivative of the inverse hyperbolic cotangent function is

$$


\dfrac{\text{d}}{\text{d}x}(\operatorname{arcoth} x) = \dfrac{1}{1-x^2}.


$$

Therefore, we have

$$


\begin{aligned}∫\frac{8}{1−𝑥^{2}}\,d𝑥=8∫\frac{1}{1−𝑥^{2}}\,d𝑥=8arcoth⁡𝑥+𝐶.\end{aligned}


$$

### The Importance of the Domain When Integrating Using Inverse Reciprocal Hyperbolic Functions

Recall that $$

$$


\int \dfrac{1}{1-x^2} \,\text{d}x = {\color{blue}\operatorname{artanh}{x}} + C, \qquad {\color{blue}x\in(-1,1)}.


$$

But we have just seen that

$$


\int \dfrac{1}{1-x^2} \,\text{d}x = {\color{red}\operatorname{arcoth}{x}} + C, \qquad {\color{red}x\in(-\infty,-1) \cup (1,\infty)}.


$$

Notice that the integral on the left-hand side is the same but we used different functions on the right. What is the difference, and how do we know which hyperbolic function to use?

The difference is the domain of the variable $x.$ When the $|x| < 1,$ we use the antiderivative $\operatorname{artanh}{x},$ otherwise we use the antiderivative $\operatorname{arcoth}{x}.$

For instance, we have that

$$


\begin{aligned}∫_{1/2−1/2}\frac{1}{1−𝑥^{2}}\,d𝑥 & =artanh⁡𝑥\,_{1/2−1/2} \\ & =artanh⁡(\frac{1}{2})−artanh⁡(−\frac{1}{2}).\end{aligned}


$$

Note that since the limits of integration lie in the interval $(-1,1),$ we used the antiderivative $\operatorname{artanh}{x}.$

While, on the other hand, we have that

$$


\begin{aligned}∫_{32}\frac{1}{1−𝑥^{2}}\,d𝑥 & =arcoth⁡𝑥\,_{32} \\ & =arcoth⁡(3)−arcoth⁡(2).\end{aligned}


$$

Note that since the limits of integration lie in the interval $(1,\infty),$ we used the antiderivative $\operatorname{arcoth}{x}.$
