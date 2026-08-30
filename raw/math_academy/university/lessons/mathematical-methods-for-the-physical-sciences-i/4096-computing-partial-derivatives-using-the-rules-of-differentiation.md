# Computing Partial Derivatives Using the Rules of Differentiation

Source: https://www.mathacademy.com/topics/4096?courseId=154
Topic ID: 4096

## Prerequisites

- [Introduction to Partial Derivatives](./1929-introduction-to-partial-derivatives.md)

## Lesson

### Introduction

We can use the chain, product, and quotient rules to find partial derivatives of multivariable functions.

For example, consider the following function:

$$


f(x,y) = \cos(xy^2) + 3x


$$

To compute the partial derivative of $f$ with respect to $x,$ we "fix" the variable ${\color{blue}y}$ (in other words, we treat ${\color{blue}y}$ as if it were constant). Then, we take the derivative with respect to $x,$ as usual.

First, we use the sum rule for differentiation:

$$


\begin{aligned}\frac{𝜕𝑓}{𝜕𝑥} & =\frac{𝜕}{𝜕𝑥}(cos⁡(𝑥𝑦^{2})+3𝑥) \\ & =\frac{𝜕}{𝜕𝑥}(cos⁡(𝑥𝑦^{2}))+\frac{𝜕}{𝜕𝑥}(3𝑥)\end{aligned}


$$

Now, we use the chain rule and the constant multiple rules for differentiation:

$$


\begin{aligned}\frac{𝜕}{𝜕𝑥}(cos⁡(𝑥𝑦^{2}))+\frac{𝜕}{𝜕𝑥}(3𝑥) & =−sin⁡(𝑥𝑦^{2})⋅\frac{𝜕}{𝜕𝑥}(𝑥𝑦^{2})+\frac{𝜕}{𝜕𝑥}(3𝑥) \\ & =−sin⁡(𝑥𝑦^{2})⋅𝑦^{2}⋅\frac{𝜕}{𝜕𝑥}(𝑥)+3⋅\frac{𝜕}{𝜕𝑥}(𝑥) \\ & =−sin⁡(𝑥𝑦^{2})⋅𝑦^{2}⋅1+3⋅1 \\ & =3−𝑦^{2}sin⁡(𝑥𝑦^{2})\end{aligned}


$$

To compute the partial derivative of $f$ with respect to $y,$ we "fix" the variable ${\color{blue}x}$ (in other words, we treat ${\color{blue}x}$ as if it were constant). Then, we take the derivative with respect to $y,$ as usual.

First, we use the sum rule for differentiation:

$$


\begin{aligned}\frac{𝜕𝑓}{𝜕𝑦} & =\frac{𝜕}{𝜕𝑦}(cos⁡(𝑥𝑦^{2})+3𝑥) \\ & =\frac{𝜕}{𝜕𝑦}(cos⁡(𝑥𝑦^{2}))+\frac{𝜕}{𝜕𝑦}(3𝑥)\end{aligned}


$$

Now, we use the chain rule and the constant multiple rules for differentiation:

$$


\begin{aligned}\frac{𝜕}{𝜕𝑦}(cos⁡(𝑥𝑦^{2}))+\frac{𝜕}{𝜕𝑦}(3𝑥) & =−sin⁡(𝑥𝑦^{2})⋅\frac{𝜕}{𝜕𝑦}(𝑥𝑦^{2})+\frac{𝜕}{𝜕𝑦}(3𝑥) \\ & =−sin⁡(𝑥𝑦^{2})⋅𝑥⋅\frac{𝜕}{𝜕𝑦}(𝑦^{2})+0 \\ & =−sin⁡(𝑥𝑦^{2})⋅𝑥⋅2𝑦 \\ & =−2𝑥𝑦sin⁡(𝑥𝑦^{2})\end{aligned}


$$

### Example: Applying the Chain Rule

#### Question

For the function $f(x,y) =\ln(y-x^2),$ evaluate $f_x(1,9).$

#### Explanation

We differentiate the given function with respect to $x,$ treating all other variables as constants.

First, we use the chain rule:

$$


\begin{aligned}𝑓_{𝑥}(𝑥,𝑦) & =\frac{𝜕}{𝜕𝑥}(ln⁡(𝑦−𝑥^{2})) \\ & =\frac{1}{𝑦−𝑥^{2}}⋅\frac{𝜕}{𝜕𝑥}(𝑦−𝑥^{2})\end{aligned}


$$

Now, we use the sum and constant multiple rules:

$$


\begin{aligned}\frac{1}{𝑦−𝑥^{2}}⋅\frac{𝜕}{𝜕𝑥}(𝑦−𝑥^{2}) & =\frac{1}{𝑦−𝑥^{2}}⋅(𝑦⋅\frac{𝜕}{𝜕𝑥}(1)−\frac{𝜕}{𝜕𝑥}(𝑥^{2})) \\ & =\frac{1}{𝑦−𝑥^{2}}⋅(𝑦⋅0−2𝑥) \\ & =−\frac{2𝑥}{𝑦−𝑥^{2}}\end{aligned}


$$

Finally, we evaluate the partial derivative at the point $(1,9)\mathbin{:}$

$$


\begin{aligned}𝑓_{𝑥}(1,9) & =−\frac{2⋅1}{9−1^{2}} \\ & =−\frac{2}{8} \\ & =−\frac{1}{4}\end{aligned}


$$

### Example: Applying the Product Rule

#### Question

Find $\dfrac{\partial f}{\partial x}$ for $f(x,y) =x^2y\ln{x}.$

#### Explanation

We differentiate the given function with respect to $x,$ treating all other variables as constants.

First, we use the constant multiple rule:

$$


\begin{aligned}\frac{𝜕𝑓}{𝜕𝑥} & =\frac{𝜕}{𝜕𝑥}(𝑥^{2}𝑦ln⁡𝑥) \\ & =𝑦⋅\frac{𝜕}{𝜕𝑥}(𝑥^{2}ln⁡𝑥)\end{aligned}


$$

Then, we use the product rule:

$$


\begin{aligned}𝑦⋅\frac{𝜕}{𝜕𝑥}(𝑥^{2}ln⁡𝑥) & =𝑦⋅(\frac{𝜕}{𝜕𝑥}(𝑥^{2})⋅ln⁡𝑥+𝑥^{2}⋅\frac{𝜕}{𝜕𝑥}(ln⁡𝑥)) \\ & =𝑦⋅((2𝑥)⋅ln⁡𝑥+𝑥^{2}⋅(\frac{1}{𝑥})) \\ & =𝑦(2𝑥ln⁡𝑥+𝑥) \\ & =𝑥𝑦(2ln⁡𝑥+1)\end{aligned}


$$

### Example: Applying the Quotient Rule

#### Question

For the function $f(x,y) = \dfrac{4x-y}{x+y^2},$ evaluate $\dfrac{\partial f}{\partial x}$ at the point $(2,-1).$

#### Explanation

We differentiate the given function with respect to $x,$ treating all other variables as constants.

First, we use the quotient rule:

$$


\begin{aligned}\frac{𝜕}{𝜕𝑥}(\frac{4𝑥−𝑦}{𝑥+𝑦^{2}}) & =\frac{\frac{𝜕}{𝜕𝑥}(4𝑥−𝑦)⋅(𝑥+𝑦^{2})−(4𝑥−𝑦)⋅\frac{𝜕}{𝜕𝑥}(𝑥+𝑦^{2})}{𝜕𝑥} \\ & =\frac{4⋅(𝑥+𝑦^{2})−(4𝑥−𝑦)⋅1}{(𝑥+𝑦^{2})^{2}} \\ & =\frac{4𝑥+4𝑦^{2}−4𝑥+𝑦}{(𝑥+𝑦^{2})^{2}} \\ & =\frac{4𝑦^{2}+𝑦}{(𝑥+𝑦^{2})^{2}}\end{aligned}


$$

Then, we evaluate the partial derivative at the point $(2,-1)\mathbin{:}$

$$


\begin{aligned}\frac{𝜕𝑓}{𝜕𝑥}_{(2,−1)} & =\frac{4(−1)^{2}+(−1)}{(2+(−1)^{2})^{2}} \\ & =\frac{4−1}{3^{2}} \\ & =\frac{1}{3}\end{aligned}


$$

### Partial Derivatives of Three-Variable Functions

We can also compute partial derivatives of functions with three or even more variables.

For example, suppose we have the function $f(x,y,z).$ We find its partial derivatives as follows:

- To compute $\dfrac{\partial f}{\partial x},$ we differentiate with respect to $x,$ treating $y$ *and* $z$ as constants.

- To compute $\dfrac{\partial f}{\partial y},$ we differentiate with respect to $y,$ treating $x$ *and* $z$ as constants.

- To compute $\dfrac{\partial f}{\partial z},$ we differentiate with respect to $z,$ treating $x$ *and* $y$ as constants.

Let's see an example.

### Example: Finding Partial Derivatives of Three-Variable Functions

#### Question

For the function $g(x,y,z) = 2 (x + 1)e^z+ yz,$ evaluate $\dfrac{\partial g}{\partial z}$ at $(1,1,1).$

#### Explanation

We differentiate the given function with respect to $z,$ treating all other variables as constants.

First, we use the sum and constant multiple rules:

$$


\begin{aligned}\frac{𝜕𝑔}{𝜕𝑧} & =\frac{𝜕}{𝜕𝑧}(2(𝑥+1)𝑒^{𝑧}+𝑦𝑧) \\ & =\frac{𝜕}{𝜕𝑧}(2(𝑥+1)𝑒^{𝑧})+\frac{𝜕}{𝜕𝑧}(𝑦𝑧) \\ & =2(𝑥+1)\frac{𝜕}{𝜕𝑧}(𝑒^{𝑧})+\frac{𝜕}{𝜕𝑧}(𝑦𝑧) \\ & =2(𝑥+1)𝑒^{𝑧}+𝑦\end{aligned}


$$

Finally, we evaluate the partial derivative at the point $(1,1,1)\mathbin{:}$

$$


\begin{aligned}\frac{𝜕𝑔}{𝜕𝑧}_{(1,1,1)} & =2(1+1)𝑒^{1}+1 \\ & =4𝑒+1\end{aligned}


$$
