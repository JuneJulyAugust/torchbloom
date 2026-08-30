# Differentiating Inverse Reciprocal Hyperbolic Functions

Source: https://www.mathacademy.com/topics/3255?courseId=105
Topic ID: 3255

## Prerequisites

- [Differentiating Inverse Reciprocal Trigonometric Functions](./1721-differentiating-inverse-reciprocal-trigonometric-functions.md)
- [Differentiating Inverse Hyperbolic Functions](./3252-differentiating-inverse-hyperbolic-functions.md)

## Lesson

### Introduction

The derivatives of the inverse reciprocal hyperbolic functions are shown below: $$

$$


\begin{aligned}\frac{d}{d𝑥}(arcsch⁡𝑥) & =−\frac{1}{|𝑥|\sqrt{1+𝑥^{2}}}, & & 𝑥∈(−∞,0)∪(0,∞) \\ \frac{d}{d𝑥}(arsech⁡𝑥) & =−\frac{1}{𝑥\sqrt{1−𝑥^{2}}}, & & 𝑥∈(0,1) \\ \frac{d}{d𝑥}(arcoth⁡𝑥) & =\frac{1}{1−𝑥^{2}}, & & 𝑥∈(−∞,−1)∪(1,∞)\end{aligned}


$$

Now that we know the derivative of the base inverse reciprocal hyperbolic functions, we can differentiate combinations of these functions, by using the properties of differentiation.

For example, let's find the derivative of

$$


y = \operatorname{arsech}{(-x^2)}


$$

Using the formulas above together with the chain rule, we get

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =\frac{d}{d𝑥}(arsech⁡(−𝑥^{2})) \\ & =−\frac{1}{(−𝑥^{2})\sqrt{1−(−𝑥^{2})^{2}}}⋅(−𝑥^{2})^{′} \\ & =−\frac{1}{−𝑥^{2}\sqrt{1−𝑥^{4}}}⋅(−2𝑥) \\ & =−\frac{2}{𝑥\sqrt{1−𝑥^{4}}}.\end{aligned}


$$

### Example: Differentiating an Inverse Csch Function

#### Question

$$

If $y =7\operatorname{arcsch}(1-x),$ then $\dfrac {\text{d}y}{\text{d}x}=$

#### Explanation

$$

The formula for the derivative of the inverse hyperbolic cosecant function is

$$


\dfrac{\text{d}}{\text{d}x}(\operatorname{arcsch} x) = -\dfrac{1}{|x|\sqrt{1+x^2}}.


$$

Using the formula above with the chain rule, we get

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =\frac{d}{d𝑥}(7arcsch⁡(1−𝑥)) \\ & =7\frac{d}{d𝑥}(arcsch⁡(1−𝑥)) \\ & =7(−\frac{1}{|1−𝑥|\sqrt{1+(1−𝑥)^{2}}})⋅(1−𝑥)^{′} \\ & =7(−\frac{1}{|𝑥−1|\sqrt{1+1−2𝑥+𝑥^{2}}})⋅(−1) \\ & =\frac{7}{|𝑥−1|\sqrt{𝑥^{2}−2𝑥+2}}.\end{aligned}


$$

### Example: Differentiating an Inverse Sech Function

#### Question

$$

If $y = 5\operatorname{arsech}{2x},$ then $\dfrac {\text{d}y}{\text{d}x}=$

#### Explanation

$$

The formula for the derivative of the inverse hyperbolic secant function is

$$


\dfrac{\text{d}}{\text{d}x}(\operatorname{arsech} x) = -\dfrac{1}{x\sqrt{1-x^2}}.


$$

Using the formula above with the chain rule, we get

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =\frac{d}{d𝑥}(5arsech⁡2𝑥) \\ & =5\frac{d}{d𝑥}(arsech⁡2𝑥) \\ & =5(−\frac{1}{(2𝑥)\sqrt{1−(2𝑥)^{2}}})⋅(2𝑥)^{′} \\ & =−\frac{5}{2𝑥\sqrt{1−4𝑥^{2}}}⋅2 \\ & =−\frac{5}{𝑥\sqrt{1−4𝑥^{2}}}.\end{aligned}


$$

### Example: Differentiating an Inverse Coth Function

#### Question

$$

If $y = \operatorname{arcoth}{e^x},$ then $\dfrac {\text{d}y}{\text{d}x}=$

#### Explanation

$$

The formula for the derivative of the inverse hyperbolic cotangent function is

$$


\dfrac{\text{d}}{\text{d}x}(\operatorname{arcoth} x) = \dfrac{1}{1-x^2}.


$$

Using the formula above with the chain rule, we get

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =\frac{d}{d𝑥}(arcoth⁡𝑒^{𝑥}) \\ & =\frac{1}{1−(𝑒^{𝑥})^{2}}⋅(𝑒^{𝑥})^{′} \\ & =\frac{1}{1−𝑒^{2𝑥}}⋅𝑒^{𝑥} \\ & =\frac{𝑒^{𝑥}}{1−𝑒^{2𝑥}}.\end{aligned}


$$

### Example: Differentiating Inverse Reciprocal Hyperbolic Functions Using the Product and Quotient Rules

#### Question

$$

If $f(x) = \sin{x} \cdot \operatorname{arcsch}{x},$ then $f'(x) = \cos{x} \operatorname{arcsch}{x} + g(x).$ What is $g(x)?$

#### Explanation

$$

In this case, the expression for $f(x)$ is a product $u(x) \cdot v(x)$ with $u(x) = \sin{x}$ and $v(x) = \operatorname{arcsch}{x}.$

Therefore, we apply the product rule as follows:

$$


\begin{aligned}𝑓^{′}(𝑥) & =𝑢^{′}(𝑥)⋅𝑣(𝑥)+𝑢(𝑥)⋅𝑣^{′}(𝑥) \\ & =(sin⁡𝑥)^{′}⋅arcsch⁡𝑥+sin⁡𝑥⋅(arcsch⁡𝑥)^{′} \\ & =cos⁡𝑥⋅arcsch⁡𝑥+sin⁡𝑥⋅(−\frac{1}{|𝑥|\sqrt{1+𝑥^{2}}}) \\ & =cos⁡𝑥arcsch⁡𝑥+\underset{𝑔(𝑥)}{\underset{}{(−\frac{sin⁡𝑥}{|𝑥|\sqrt{1+𝑥^{2}}})}}\end{aligned}


$$

Therefore, $g(x) = -\dfrac{\sin{x}}{|x|\sqrt{1+x^2}}.$
