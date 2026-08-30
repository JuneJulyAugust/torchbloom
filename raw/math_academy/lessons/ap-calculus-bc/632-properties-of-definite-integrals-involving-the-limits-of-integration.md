# Properties of Definite Integrals Involving the Limits of Integration

Source: https://www.mathacademy.com/topics/632?courseId=21
Topic ID: 632

## Prerequisites

- [The Sum and Constant Multiple Rules for Definite Integrals](../ap-calculus-ab/1685-the-sum-and-constant-multiple-rules-for-definite-integrals.md)

## Lesson

### Introduction

In addition to the properties that we've already discussed, there are several more properties that we can use to calculate definite integrals.

The first property states that if the lower and upper limits of a definite integral are the same, then the integral evaluates to zero:

$$


\displaystyle\int_{\color{blue}a}^{\color{blue}a} f(x) \, \textrm d x = 0.


$$

For example, in the definite integral

$$


\displaystyle\int_{\color{blue}3}^{\color{blue}3} x \, \textrm d x ,


$$

the upper and lower limits of integration are the same. If we evaluate the integral, we get

$$


\begin{aligned}∫_{33}^{}𝑥\,d𝑥 & =\frac{𝑥^{2}}{2}_{33}^{} \\ & =\frac{(3)^{2}}{2}−\frac{(3)^{2}}{2} \\ & =0.\end{aligned}


$$

There's an intuitive explanation for this result. The integral $\displaystyle\int_3^3 x \, \textrm d x$ can be thought of as the area under the graph of $y = x$ between $x=3$ and $x=3$, which is a rectangle of zero width. A rectangle of zero width has no area!

### Example: Evaluating an Integral Over an Interval of Length Zero

#### Question

Calculate $\displaystyle \int_\pi^\pi \sqrt{\sin x}\,\textrm d x.$

#### Explanation

Notice that the lower and upper limits are the same. So, the integral evaluates to zero:

$$


\int_\pi^\pi \sqrt{\sin x}\,\textrm d x = 0


$$

### Reversing the Limits of Integration

The second property states that reversing the limits of integration changes the sign of the definite integral:

$$


\displaystyle\int_{\color{red}a}^{\color{blue}b} f(x)\, \textrm d x = - \int_{\color{blue}b}^{\color{red}a} f(x)\, \textrm d x.


$$

So, for example, if we know that

$$


\displaystyle\int_{\color{red}1}^{\color{blue}2} 2x\, \textrm d x =3,


$$

then we can immediately conclude that

$$


\displaystyle\int_{\color{blue}2}^{\color{red}1} 2x\, \textrm d x = -3.


$$

### Example: Evaluating an Integral Given Another Integral With Reversed Limits of Integration

#### Question

Given that ${\displaystyle \int_{0}^{6} \, f(x) \; \textrm d x = -54},$ what is the value of ${\displaystyle \int_{6}^{0} \bigg(\dfrac 1 3 f(x) + 1 \bigg) \; \textrm d x}?$

#### Explanation

Let's reverse the limits of integration on the known result:

$$


\begin{aligned}∫_{06}^{}\,𝑓(𝑥)\,d𝑥=−∫_{60}^{}\,𝑓(𝑥)\,d𝑥=54\end{aligned}


$$

Now, we can split up the given integral using the sum rule and factor out the constants. We get

$$


\begin{aligned}∫_{06}^{}(\frac{1}{3}𝑓(𝑥)+1)\,d𝑥 & =\frac{1}{3}∫_{06}^{}𝑓(𝑥)\,d𝑥+∫_{06}^{}1\,d𝑥 \\ & =\frac{1}{3}⋅54+𝑥\,_{06}^{} \\ & =18+(0−6) \\ & =12.\end{aligned}


$$

### The Integral of a Function Over Adjacent Intervals

The last property states that if we have the sum of two integrals with the same integrand, and where the lower bound of one integral matches the upper bound of the other integral, such as

$$


\displaystyle \int_{-3}^{\color{blue}0} 4x^2\, \textrm d x + \int_{\color{blue}0}^{5} 4x^2\, \textrm d x,


$$

then we can combine the two integrals into a single integral as follows:

$$


\int_{-3}^{\color{blue}0} 4x^2\, \textrm d x + \int_{\color{blue}0}^{5} 4x^2\, \textrm d x = \int_{-3}^{5} 4x^2\, \textrm d x


$$

In general,

$$


\int_a^c f(x) \, \textrm d x + \int_c^b f(x) \, \textrm d x = \int_a^b f(x)\, \textrm d x.


$$

To understand the reasoning behind this rule, remember that the integrals represent area. So, the rule states that the area bounded by a function on the interval $[a,b]$ is equal to the sum of areas on the adjacent intervals $[a,c]$ and $[c,b].$

### Example: Evaluating a Definite Integral Given Integrals Over Adjacent Intervals

#### Question

If $\displaystyle \int_7^{10}f(x)\,\textrm d x = 18$ and $\displaystyle \int_0^{7}f(x)\,\textrm d x = -6$ then what is $\displaystyle \int_0^{10} \big(2f(x)+1 \big) \,\textrm d x?$

#### Explanation

From the adjacent intervals rule, we know that

$$


\int_0^{7}f(x)\,\textrm d x + \displaystyle \int_7^{10}f(x)\,\textrm d x = \displaystyle \int_0^{10}f(x)\,\textrm d x.


$$

Plugging in the known information into the above gives the following:

$$


\begin{aligned}−6+18=∫_{100}^{}𝑓(𝑥)\,d𝑥 \\ 12=∫_{100}^{}𝑓(𝑥)\,d𝑥\end{aligned}


$$

Finally, we compute the desired integral and get

$$


\begin{aligned}∫_{100}^{}(2𝑓(𝑥)+1)\,d𝑥 & =2∫_{100}^{}𝑓(𝑥)\,d𝑥+∫_{100}^{}d𝑥 \\ & =2(12)+𝑥\,_{100}^{} \\ & =24+(10−0) \\ & =34.\end{aligned}


$$

### Example: Evaluating a Definite Integral Using Multiple Properties of Definite Integrals

#### Question

Suppose that $f(x)$ is a function such that ${\displaystyle \int_4^1 2 \, f(x) \, \textrm dx = -1}$ and ${\displaystyle \int_{1}^{-1} f(x) \, \textrm dx = 2}.$ What is the value of ${\displaystyle \int_{-1}^4 f(x) \, \textrm dx}?$

#### Explanation

Let's simplify the first given integral:

$$


\begin{aligned}∫_{14}^{}2\,𝑓(𝑥)\,d𝑥 & =−1 \\ 2∫_{14}^{}\,𝑓(𝑥)\,d𝑥 & =−1 \\ −2∫_{41}^{}\,𝑓(𝑥)\,d𝑥 & =−1 \\ ∫_{41}^{}\,𝑓(𝑥)\,d𝑥 & =\frac{1}{2}.\end{aligned}


$$

The second integral can be rewritten as follows:

$$


\begin{aligned}∫_{−11}^{}𝑓(𝑥)\,d𝑥 & =2 \\ −∫_{1−1}^{}𝑓(𝑥)\,d𝑥 & =2 \\ ∫_{1−1}^{}𝑓(𝑥)\,d𝑥 & =−2.\end{aligned}


$$

Then, from the adjacent intervals rule, we get

$$


\begin{aligned}∫_{4−1}^{}𝑓(𝑥)\,d𝑥 & =∫_{1−1}^{}𝑓(𝑥)\,d𝑥+∫_{41}^{}𝑓(𝑥)\,d𝑥 \\ & =−2+\frac{1}{2} \\ & =−\frac{3}{2}.\end{aligned}


$$
