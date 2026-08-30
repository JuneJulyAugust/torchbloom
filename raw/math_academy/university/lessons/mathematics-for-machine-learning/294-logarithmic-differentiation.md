# Logarithmic Differentiation

Source: https://www.mathacademy.com/topics/294?courseId=145
Topic ID: 294

## Prerequisites

- [Implicit Differentiation](../../../ap-courses/lessons/ap-calculus-ab/57-implicit-differentiation.md)
- [Simplifying Expressions Using Basic Trigonometric Identities](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/203-simplifying-expressions-using-basic-trigonometric-identities.md)
- [The Power Rule for Logarithms](../../../high-school/traditional/lessons/algebra-ii/1475-the-power-rule-for-logarithms.md)

## Lesson

### Introduction

**Logarithmic differentiation** is a technique to compute derivatives that are difficult to find using the usual rules of differentiation, such as the product, quotient, and chain rules.

Let's consider the following function.

$$


y = x^x


$$

We aim to compute $\dfrac{\textrm d y}{\textrm d x}.$ However, in this case, we note the following:

- Both the base and the exponent are functions of $x.$

- This means we cannot apply the power rule since the exponent is not a fixed number.

- We also cannot apply the rules for differentiating exponentials since the base is not a fixed number.

So instead, we'll use logarithmic differentiation. We proceed as follows:

**Step 1.** We take the natural logarithm of both sides and apply the power rule for logarithms:

$$


\begin{aligned}𝑦 & =𝑥^{𝑥} \\ ln⁡𝑦 & =ln⁡𝑥^{𝑥} \\ ln⁡𝑦 & =𝑥ln⁡𝑥\end{aligned}


$$

**Step 2.** We differentiate both sides of the above equation with respect to $x$ using implicit differentiation and the product rule:

$$


\begin{aligned}\frac{d}{d𝑥}(ln⁡𝑦) & =\frac{d}{d𝑥}(𝑥ln⁡𝑥) \\ \frac{1}{𝑦}⋅\frac{d𝑦}{d𝑥} & =\frac{d}{d𝑥}(𝑥)⋅ln⁡𝑥+𝑥⋅\frac{d}{d𝑥}(ln⁡𝑥) \\ \frac{1}{𝑦}⋅\frac{d𝑦}{d𝑥} & =1⋅ln⁡𝑥+𝑥⋅(\frac{1}{𝑥}) \\ \frac{1}{𝑦}⋅\frac{d𝑦}{d𝑥} & =ln⁡𝑥+1\end{aligned}


$$

**Step 3.** Now, we solve for $\dfrac {\textrm{d}y}{\textrm{d}x}.$ This gives

$$


\dfrac {\textrm{d}y}{\textrm{d}x} = y\left( \ln x + 1 \right).


$$

**Step 4.** Finally, we substitute back our original expression for $y=x^x{:}$

$$


\dfrac {\textrm{d}y}{\textrm{d}x} = x^x \left( \ln x + 1 \right)


$$

Let's see another example.

### Example: Differentiating X Raised to the Power of a Function

#### Question

Find the derivative of the function $y = x^{x^3}.$

#### Explanation

We have the function

$$


y = x^{x^3}.


$$

First, we take the natural logarithm of both sides:

$$


\begin{aligned}ln⁡𝑦 & =ln⁡(𝑥^{𝑥^{3}}) \\ ln⁡𝑦 & =𝑥^{3}ln⁡𝑥\end{aligned}


$$

Next, we differentiate both sides with respect to $x{:}$

$$


\begin{aligned}\frac{d}{d𝑥}(ln⁡𝑦) & =\frac{d}{d𝑥}(𝑥^{3}ln⁡𝑥) \\ \frac{1}{𝑦}⋅𝑦^{′} & =(𝑥^{3})^{′}⋅(ln⁡𝑥)+(𝑥^{3})⋅(ln⁡𝑥)^{′} \\ \frac{1}{𝑦}⋅𝑦^{′} & =3𝑥^{2}⋅ln⁡𝑥+𝑥^{3}⋅\frac{1}{𝑥} \\ \frac{𝑦^{′}}{𝑦} & =3𝑥^{2}ln⁡𝑥+𝑥^{2}\end{aligned}


$$

Now, we solve for $y'{:}$

$$


\begin{aligned}𝑦^{′} & =𝑦(3𝑥^{2}ln⁡𝑥+𝑥^{2})\end{aligned}


$$

Finally, we substitute $y=x^{x^3}{:}$

$$


\begin{aligned}𝑦^{′} & =𝑥^{𝑥^{3}}(3𝑥^{2}ln⁡𝑥+𝑥^{2}) \\ & =𝑥^{𝑥^{3}}(𝑥^{2}(3ln⁡𝑥+1)) \\ & =𝑥^{𝑥^{3}+2}(3ln⁡𝑥+1)\end{aligned}


$$

### Example: Differentiating a Function Raised to the Power of X

#### Question

Find the derivative of the function $y = (x^2-1)^x.$

#### Explanation

We have the function

$$


y = (x^2-1)^x.


$$

First, we take the natural logarithm of both sides:

$$


\begin{aligned}ln⁡𝑦 & =ln⁡((𝑥^{2}−1)^{𝑥}) \\ ln⁡𝑦 & =𝑥ln⁡(𝑥^{2}−1)\end{aligned}


$$

Next, we differentiate both sides with respect to $x{:}$

$$


\begin{aligned}\frac{d}{d𝑥}(ln⁡𝑦) & =\frac{d}{d𝑥}(𝑥ln⁡(𝑥^{2}−1)) \\ \frac{1}{𝑦}⋅\frac{d𝑦}{d𝑥} & =\frac{d}{d𝑥}(𝑥)⋅ln⁡(𝑥^{2}−1)+𝑥⋅\frac{d}{d𝑥}(ln⁡(𝑥^{2}−1)) \\ \frac{1}{𝑦}⋅\frac{d𝑦}{d𝑥} & =1⋅ln⁡(𝑥^{2}−1)+𝑥⋅(\frac{1}{𝑥^{2}−1}⋅2𝑥) \\ \frac{1}{𝑦}⋅\frac{d𝑦}{d𝑥} & =ln⁡(𝑥^{2}−1)+\frac{2𝑥^{2}}{𝑥^{2}−1}\end{aligned}


$$

Now, we solve for $\dfrac {\textrm{d}y}{\textrm{d}x}{:}$

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =𝑦(ln⁡(𝑥^{2}−1)+\frac{2𝑥^{2}}{𝑥^{2}−1})\end{aligned}


$$

Finally, we substitute $y = (x^2-1)^x{:}$

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =(𝑥^{2}−1)^{𝑥}(ln⁡(𝑥^{2}−1)+\frac{2𝑥^{2}}{𝑥^{2}−1}) \\ & =(𝑥^{2}−1)^{𝑥}(\frac{(𝑥^{2}−1)ln⁡(𝑥^{2}−1)}{𝑥^{2}−1}+\frac{2𝑥^{2}}{𝑥^{2}−1}) \\ & =(𝑥^{2}−1)^{𝑥−1}((𝑥^{2}−1)ln⁡(𝑥^{2}−1)+2𝑥^{2})\end{aligned}


$$

### Example: Differentiating a Function Raised to the Power of a Function

#### Question

Find the derivative of the function $y = (\sin x)^{\cos x}.$

#### Explanation

We have the function

$$


y = (\sin x)^{\cos x}.


$$

First, we take the natural logarithm of both sides:

$$


\begin{aligned}ln⁡𝑦 & =ln⁡((sin⁡𝑥)^{cos⁡𝑥}) \\ ln⁡𝑦 & =cos⁡𝑥\,ln⁡(sin⁡𝑥)\end{aligned}


$$

Next, we differentiate both sides with respect to $x{:}$

$$


\begin{aligned}\frac{d}{d𝑥}(ln⁡𝑦) & =\frac{d}{d𝑥}(cos⁡𝑥ln⁡(sin⁡𝑥)) \\ \frac{1}{𝑦}⋅𝑦^{′} & =(cos⁡𝑥)^{′}⋅(ln⁡(sin⁡𝑥))+(cos⁡𝑥)⋅(ln⁡(sin⁡𝑥))^{′} \\ \frac{1}{𝑦}⋅𝑦^{′} & =(−sin⁡𝑥)⋅ln⁡(sin⁡𝑥)+cos⁡𝑥⋅(\frac{1}{sin⁡𝑥}⋅cos⁡𝑥) \\ \frac{𝑦^{′}}{𝑦} & =cos⁡𝑥\,cot⁡𝑥−sin⁡𝑥\,ln⁡(sin⁡𝑥)\end{aligned}


$$

Now, we solve for $y'{:}$

$$


\begin{aligned}𝑦^{′} & =𝑦(cos⁡𝑥\,cot⁡𝑥−sin⁡𝑥\,ln⁡(sin⁡𝑥))\end{aligned}


$$

Finally, we substitute $y = (\sin x)^{\cos x}{:}$

$$


\begin{aligned}𝑦^{′} & =(sin⁡𝑥)^{cos⁡𝑥}(cos⁡𝑥\,cot⁡𝑥−sin⁡𝑥\,ln⁡(sin⁡𝑥))\end{aligned}


$$
