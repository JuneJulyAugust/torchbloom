# Further Logarithmic Differentiation

Source: https://www.mathacademy.com/topics/344?courseId=105
Topic ID: 344

## Prerequisites

- [Logarithmic Differentiation](./294-logarithmic-differentiation.md)
- [The Power Rule for Exponents With Algebraic Expressions](../algebra-i/362-the-power-rule-for-exponents-with-algebraic-expressions.md)
- [Simplifying Square Root Expressions Using the Quotient Rule](../algebra-i/390-simplifying-square-root-expressions-using-the-quotient-rule.md)
- [The Quotient Rule for Logarithms](../algebra-ii/1474-the-quotient-rule-for-logarithms.md)

## Lesson

### Introduction

When a function $y=y(x)$ contains complex products, quotients, or radicals, we can use logarithmic differentiation to find the derivative $y'(x).$

For example, consider the following function:

$$


y = x^2 \cdot 2^x


$$

Our goal is to find $y'(x).$ To do this, we will use the product rule for logarithms, namely

$$


\ln(a b)= \ln a + \ln b.


$$

We differentiate our function by following four steps.

**Step 1.** We take the natural logarithm of both sides and apply the product and power rules:

$$


\begin{aligned}ln⁡𝑦 & =ln⁡(𝑥^{2}⋅2^{𝑥}) \\ ln⁡𝑦 & =ln⁡(𝑥^{2})+ln⁡(2^{𝑥}) \\ ln⁡𝑦 & =2ln⁡𝑥+𝑥ln⁡2\end{aligned}


$$

**Step 2.** Next, we differentiate both sides of our equation using implicit differentiation:

$$


\begin{aligned}\frac{d}{d𝑥}(ln⁡𝑦) & =\frac{d}{d𝑥}(2ln⁡𝑥+𝑥ln⁡2) \\ \frac{1}{𝑦}⋅𝑦^{′} & =2⋅(ln⁡𝑥)^{′}+(𝑥)^{′}⋅ln⁡(2) \\ \frac{1}{𝑦}⋅𝑦^{′} & =2⋅\frac{1}{𝑥}+1⋅ln⁡(2) \\ \frac{𝑦^{′}}{𝑦} & =\frac{2}{𝑥}+ln⁡2\end{aligned}


$$

**Step 3.** Then, we solve for $y'{:}$

$$


\begin{aligned}𝑦^{′} & =𝑦(\frac{2}{𝑥}+ln⁡2)\end{aligned}


$$

**Step 4.** Finally, we substitute back our original expression for $y =x^2\cdot 2^x{:}$

$$


\begin{aligned}𝑦^{′} & =𝑥^{2}⋅2^{𝑥}(\frac{2}{𝑥}+ln⁡2) \\ & =𝑥⋅2^{𝑥+1}+𝑥^{2}⋅2^{𝑥}ln⁡2\end{aligned}


$$

### Example: Differentiating a Product

#### Question

Consider the function $y = x^5 (\cos x)^x.$ Its derivative is given by

$$


y'(x) = x^4 (\cos x)^x \left( 5 + g(x) \right).


$$

Find the function $g(x).$

#### Explanation

We have the function

$$


y = x^5 (\cos x)^x.


$$

First, we find the natural logarithm of both sides and use the product rule for logarithms:

$$


\begin{aligned}ln⁡𝑦 & =ln⁡(𝑥^{5}(cos⁡𝑥)^{𝑥}) \\ ln⁡𝑦 & =ln⁡(𝑥^{5})+ln⁡((cos⁡𝑥)^{𝑥}) \\ ln⁡𝑦 & =5ln⁡𝑥+𝑥ln⁡(cos⁡𝑥)\end{aligned}


$$

Next, we differentiate both sides with respect to $x{:}$

$$


\begin{aligned}\frac{d}{d𝑥}(ln⁡𝑦) & =\frac{d}{d𝑥}(5ln⁡𝑥+𝑥ln⁡(cos⁡𝑥)) \\ \frac{1}{𝑦}⋅𝑦^{′} & =\frac{5}{𝑥}+(𝑥)^{′}⋅ln⁡(cos⁡𝑥)+𝑥⋅(ln⁡(cos⁡𝑥))^{′} \\ \frac{𝑦^{′}}{𝑦} & =\frac{5}{𝑥}+ln⁡(cos⁡𝑥)+𝑥⋅\frac{1}{cos⁡𝑥}⋅(−sin⁡𝑥) \\ \frac{𝑦^{′}}{𝑦} & =\frac{5}{𝑥}+ln⁡(cos⁡𝑥)−𝑥tan⁡𝑥\end{aligned}


$$

Now, we solve for $y'{:}$

$$


\begin{aligned}𝑦^{′} & =𝑦(\frac{5}{𝑥}+ln⁡(cos⁡𝑥)−𝑥tan⁡𝑥)\end{aligned}


$$

Finally, we substitute $y = x^5 (\cos x)^x {:}$

$$


\begin{aligned}𝑦^{′} & =𝑥^{5}(cos⁡𝑥)^{𝑥}(\frac{5}{𝑥}+ln⁡(cos⁡𝑥)−𝑥tan⁡𝑥) \\ & =𝑥^{5}(cos⁡𝑥)^{𝑥}(\frac{5}{𝑥}+\frac{𝑥ln⁡(cos⁡𝑥)}{𝑥}−\frac{𝑥^{2}tan⁡𝑥}{𝑥}) \\ & =𝑥^{4}(cos⁡𝑥)^{𝑥}(5+𝑥ln⁡(cos⁡𝑥)−𝑥^{2}tan⁡𝑥)\end{aligned}


$$

Therefore,

$$


g(x) = x \ln ( \cos x ) - x^2 \tan x.


$$

### Using Logarithms to Differentiate a Quotient

In cases where we wish to differentiate a quotient of functions

$$


y = f(x) = \dfrac{g(x)}{h(x)},


$$

we can apply the quotient rule for logarithms:

$$


\ln \left(\dfrac{a}{b}\right) = \ln a - \ln b


$$

For example, let's compute $y',$ where the function $y$ is given by

$$


y = \dfrac {e^{x^2}}{(1-2x)^2(x-1)^3}.


$$

First, we find the natural logarithm of both sides and use the quotient and power rules for logarithms:

$$


\begin{aligned}ln⁡𝑦 & =ln⁡(\frac{𝑒^{𝑥^{2}}}{(1−2𝑥)^{2}(𝑥−1)^{3}}) \\ ln⁡𝑦 & =ln⁡(𝑒^{𝑥^{2}})−ln⁡((1−2𝑥)^{2})−ln⁡((𝑥−1)^{3}) \\ ln⁡𝑦 & =𝑥^{2}−2ln⁡(1−2𝑥)−3ln⁡(𝑥−1)\end{aligned}


$$

Next, we differentiate both sides with respect to $x{:}$

$$


\begin{aligned}\frac{d}{d𝑥}(ln⁡𝑦) & =\frac{d}{d𝑥}(𝑥^{2}−2ln⁡(1−2𝑥)−3ln⁡(𝑥−1)) \\ \frac{1}{𝑦}⋅𝑦^{′} & =2𝑥−2⋅\frac{1}{1−2𝑥}⋅(−2)−3⋅\frac{1}{𝑥−1} \\ \frac{𝑦^{′}}{𝑦} & =2𝑥+\frac{4}{1−2𝑥}−\frac{3}{𝑥−1}\end{aligned}


$$

Now, we solve for $y'{:}$

$$


\begin{aligned}𝑦^{′} & =𝑦(2𝑥+\frac{4}{1−2𝑥}−\frac{3}{𝑥−1})\end{aligned}


$$

Finally, we substitute our expression for $y,$ and simplify:

$$


\begin{aligned}𝑦^{′} & =\frac{𝑒^{𝑥^{2}}}{(1−2𝑥)^{2}(𝑥−1)^{3}}(2𝑥+\frac{4}{1−2𝑥}−\frac{3}{𝑥−1}) \\ & =\frac{𝑒^{𝑥^{2}}}{(1−2𝑥)^{2}(𝑥−1)^{3}}(\frac{2𝑥(1−2𝑥)(𝑥−1)+4(𝑥−1)−3(1−2𝑥)}{(1−2𝑥)(𝑥−1)}) \\ & =\frac{𝑒^{𝑥^{2}}}{(1−2𝑥)^{3}(𝑥−1)^{4}}(2𝑥(1−2𝑥)(𝑥−1)+4(𝑥−1)−3(1−2𝑥)) \\ & =\frac{𝑒^{𝑥^{2}}}{(1−2𝑥)^{3}(𝑥−1)^{4}}(−4𝑥^{3}+6𝑥^{2}+8𝑥−7) \\ & =−\frac{𝑒^{𝑥^{2}}}{(1−2𝑥)^{3}(𝑥−1)^{4}}(4𝑥^{3}−6𝑥^{2}−8𝑥+7) \\ & =−\frac{𝑒^{𝑥^{2}}(4𝑥^{3}−6𝑥^{2}−8𝑥+7)}{(1−2𝑥)^{3}(𝑥−1)^{4}}\end{aligned}


$$

### Example: Differentiating a Quotient

#### Question

Consider the function $y = \dfrac{(x+3)^3}{(x+5)^6}.$ The derivative of this function is given by

$$


y' = -\dfrac{g(x)(x+3)^2}{(x+5)^7}.


$$

Find the function $g(x).$

#### Explanation

We have the function

$$


y = \dfrac{(x+3)^3}{(x+5)^6}.


$$

First, we take the natural logarithm of both sides and use the quotient and power rules for logarithms:

$$


\begin{aligned}ln⁡𝑦 & =ln⁡(\frac{(𝑥+3)^{3}}{(𝑥+5)^{6}}) \\ ln⁡𝑦 & =ln⁡((𝑥+3)^{3})−ln⁡((𝑥+5)^{6}) \\ ln⁡𝑦 & =3ln⁡(𝑥+3)−6ln⁡(𝑥+5)\end{aligned}


$$

Next, we differentiate both sides with respect to $x{:}$

$$


\begin{aligned}\frac{d}{d𝑥}(ln⁡𝑦) & =\frac{d}{d𝑥}(3ln⁡(𝑥+3)−6ln⁡(𝑥+5)) \\ \frac{1}{𝑦}⋅𝑦^{′} & =3⋅\frac{1}{𝑥+3}−6⋅\frac{1}{𝑥+5} \\ \frac{𝑦^{′}}{𝑦} & =\frac{3}{𝑥+3}−\frac{6}{𝑥+5}\end{aligned}


$$

Now, we solve for $y'{:}$

$$


\begin{aligned}𝑦^{′} & =𝑦(\frac{3}{𝑥+3}−\frac{6}{𝑥+5})\end{aligned}


$$

Finally, we substitute $y = \dfrac{(x+3)^3}{(x+5)^6}{:}$

$$


\begin{aligned}𝑦^{′} & =\frac{(𝑥+3)^{3}}{(𝑥+5)^{6}}(\frac{3}{𝑥+3}−\frac{6}{𝑥+5}) \\ & =\frac{(𝑥+3)^{3}}{(𝑥+5)^{6}}(\frac{3(𝑥+5)−6(𝑥+3)}{(𝑥+3)(𝑥+5)}) \\ & =\frac{(𝑥+3)^{3}}{(𝑥+5)^{6}}(\frac{−3𝑥−3}{(𝑥+3)(𝑥+5)}) \\ & =−\frac{3(𝑥+1)(𝑥+3)^{2}}{(𝑥+5)^{7}}\end{aligned}


$$

Therefore,

$$


g(x) = \boxed{3(x+1)}.


$$

### Example: Differentiating a Radical Expression

#### Question

Consider the function $y = \sqrt[3]{\dfrac{x^2}{x^5+ 1}}.$ The derivative of this function is given by

$$


y' = \dfrac{g(x)}{3\sqrt[3]{x(x^5+1)^4}}.


$$

Find the function $g(x).$

#### Explanation

Our function can be written as

$$


\begin{aligned}𝑦 & =\sqrt[√\frac{𝑥^{2}}{𝑥^{5}+1}]{3} \\ & =\frac{\sqrt[√𝑥^{2}]{3}}{\sqrt[√𝑥^{5}+1]{3}} \\ & =\frac{𝑥^{2/3}}{(𝑥^{5}+1)^{1/3}}.\end{aligned}


$$

First, we take the natural logarithm of both sides and use the quotient and power rules for logarithms:

$$


\begin{aligned}ln⁡𝑦 & =ln⁡(\frac{𝑥^{2/3}}{(𝑥^{5}+1)^{1/3}}) \\ ln⁡𝑦 & =ln⁡(𝑥^{2/3})−ln⁡((𝑥^{5}+1)^{1/3}) \\ ln⁡𝑦 & =\frac{2}{3}ln⁡𝑥−\frac{1}{3}ln⁡(𝑥^{5}+1)\end{aligned}


$$

Next, we differentiate both sides with respect to $x{:}$

$$


\begin{aligned}\frac{d}{d𝑥}(ln⁡𝑦) & =\frac{d}{d𝑥}(\frac{2}{3}ln⁡𝑥−\frac{1}{3}ln⁡(𝑥^{5}+1)) \\ \frac{1}{𝑦}⋅𝑦^{′} & =\frac{2}{3}⋅\frac{1}{𝑥}−\frac{1}{3}⋅\frac{1}{𝑥^{5}+1}⋅(5𝑥^{4}) \\ \frac{𝑦^{′}}{𝑦} & =\frac{1}{3}(\frac{2}{𝑥}−\frac{5𝑥^{4}}{𝑥^{5}+1})\end{aligned}


$$

Now, we solve for $y'{:}$

$$


\begin{aligned}𝑦^{′} & =𝑦(\frac{1}{3}(\frac{2}{𝑥}−\frac{5𝑥^{4}}{𝑥^{5}+1}))\end{aligned}


$$

Finally, we substitute $y = \sqrt[3]{\dfrac{x^2}{x^5+ 1}}{:}$

$$


\begin{aligned}𝑦^{′} & =\frac{1}{3}\sqrt[√\frac{𝑥^{2}}{𝑥^{5}+1}]{3}(\frac{2}{𝑥}−\frac{5𝑥^{4}}{𝑥^{5}+1}) \\ & =\frac{1}{3}\sqrt[√\frac{𝑥^{2}}{𝑥^{5}+1}]{3}(\frac{2(𝑥^{5}+1)−5𝑥^{5}}{𝑥(𝑥^{5}+1)}) \\ & =\frac{1}{3}\sqrt[√\frac{𝑥^{2}}{𝑥^{5}+1}]{3}(\frac{−3𝑥^{5}+2}{𝑥(𝑥^{5}+1)}) \\ & =\frac{1}{3}\sqrt[√\frac{𝑥^{2}}{𝑥^{5}+1}]{3}(\frac{−3𝑥^{5}+2}{\sqrt[√𝑥^{3}(𝑥^{5}+1)^{3}]{3}}) \\ & =\frac{−3𝑥^{5}+2}{3\sqrt[√𝑥(𝑥^{5}+1)^{4}]{3}}\end{aligned}


$$

Therefore,

$$


g(x) = \boxed{-3x^5+2}.


$$
