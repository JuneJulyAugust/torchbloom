# Equality of Mixed Partial Derivatives

Source: https://www.mathacademy.com/topics/1957?courseId=154
Topic ID: 1957

## Prerequisites

- [Higher-Order Partial Derivatives](./1933-higher-order-partial-derivatives.md)

## Lesson

### Introduction

Suppose that $f(x,y) = x y^2 - x^3 y.$ Then the first-order partial derivatives are

$$


\dfrac{\partial f}{\partial x} (x,y) = y^2 -3x^2y \quad \mathrm{and} \quad \dfrac{\partial f}{\partial y}(x,y) = 2xy -x^3,


$$

and the second-order **mixed partial derivatives** are

$$


\dfrac{\partial^2 f}{\partial y\, \partial x}(x,y) = 2y -3x^2 \quad \mathrm{and} \quad \dfrac{\partial^2 f}{\partial x\, \partial y}(x,y) = 2y-3x^2.


$$

Notice that these two mixed partial derivatives are equal, i.e.,

$$


\dfrac{\partial^2 f}{\partial y\, \partial x}=\dfrac{\partial^2 f}{\partial x\, \partial y}.


$$

In general, if a function $f(x,y)$ has continuous first-order partial derivatives on an open set $U,$ and the second-order mixed partial derivatives exist and are continuous on $U,$ then the mixed partial derivatives are equal everywhere on $U.$

### Example: Finding Missing Constants in First-Order Partial Derivative Expressions

#### Question

Suppose that the function $f(x,y)$ and all of its first and second-order partial derivatives are continuous on an open set $U.$ Find the values of $a$ and $b,$ if

$$


f_x(x,y) = 6xy+axy^3-5, \qquad f_y(x,y) = 3x^2+bx^2y^2, \qquad f_y(2,-1) = -24.


$$

#### Explanation

First, we compute the mixed partial derivatives:

$$


\begin{aligned}𝑓_{𝑥𝑦}(𝑥,𝑦) & =\frac{𝜕}{𝜕𝑦}(𝑓_{𝑥}(𝑥,𝑦)) \\ & =\frac{𝜕}{𝜕𝑦}(6𝑥𝑦+𝑎𝑥𝑦^{3}−5) \\ & =6𝑥+3𝑎𝑥𝑦^{2}−0 \\ & =6𝑥+3𝑎𝑥𝑦^{2} \\ 𝑓_{𝑦𝑥}(𝑥,𝑦) & =\frac{𝜕}{𝜕𝑥}(𝑓_{𝑦}(𝑥,𝑦)) \\ & =\frac{𝜕}{𝜕𝑥}(3𝑥^{2}+𝑏𝑥^{2}𝑦^{2}) \\ & =6𝑥+2𝑏𝑥𝑦^{2}\end{aligned}


$$

Since the function and its first and second-order partial derivatives are continuous on an open set $U,$ the mixed partial derivatives must be equal. So, we have the identity

$$


\begin{aligned}𝑓_{𝑥𝑦}(𝑥,𝑦) & =𝑓_{𝑦𝑥}(𝑥,𝑦) \\ 6𝑥+3𝑎𝑥𝑦^{2} & =6𝑥+2𝑏𝑥𝑦^{2}.\end{aligned}


$$

Equating the coefficients of $xy^2,$ we see that $3a=2b.$

Now, since $f_y(2,-1)=-24,$ we get

$$


\begin{aligned}𝑓_{𝑦}(2,−1) & =−24 \\ 3(2)^{2}+𝑏(2)^{2}(−1)^{2} & =−24 \\ 12+4𝑏 & =−24 \\ 4𝑏 & =−36 \\ 𝑏 & =−9\end{aligned}


$$

Finally,

$$


\begin{aligned}3𝑎 & =2𝑏 \\ 3𝑎 & =2(−9) \\ 3𝑎 & =−18 \\ 𝑎 & =−6.\end{aligned}


$$

Therefore, $a=-6$ and $b=-9.$

### Example: Identifying Possible Pairs of First-Order Partial Derivatives

#### Question

Suppose that the function $f(x,y)$ and all of its first and second-order partial derivatives are continuous on an open set $U.$ Which of the following pairs could represent the first-order partial derivatives of $f(x,y)?$

1. $f_x(x,y)=x+2y$ and $f_y(x,y)=2y-x$

2. $f_x(x,y)=5(x+y)^4$ and $f_y(x,y)=5(x+y)^4$

3. $f_x(x,y)=-\sin{x}\sin{y}$ and $f_y(x,y)=\cos{x}\cos{y}$

#### Explanation

Since the function and its first and second-order partial derivatives are continuous on an open set $U,$ the mixed partial derivatives must be equal, that is,

$$


f_{xy}(x,y)=f_{yx}(x,y).


$$

Let's check if this condition is true for each of our pairs of first-order partial derivatives.

- For the first pair, the mixed partial derivatives are Since $f_{xy}(x,y) \neq f_{yx}(x,y),$ the first pair could ** represent the first-order partial derivatives of $f(x,y).$

- For the second pair, the mixed partial derivatives are Since $f_{xy}(x,y) = f_{yx}(x,y),$ the second pair ** represent the first-order partial derivatives of $f(x,y).$

- For the third pair, the mixed partial derivatives are Since $f_{xy}(x,y)=f_{yx}(x,y),$ the third pair ** represent the first-order partial derivatives of $f(x,y).$

Therefore, the correct answer is "II and III only."

### Equality of Higher-Order Partial Derivatives

If $f(x,y)$ is a function whose first-order and second-order mixed partial derivatives are continuous on an open set $U,$ then the second-order mixed partial derivatives are equal everywhere on $U.$

$$


\dfrac{\partial^2 f}{\partial x\, \partial y} =\dfrac{\partial^2 f}{\partial y\, \partial x}


$$

This result also extends to higher-order partial derivatives. For example, if the third-order partial derivatives of $f(x,y)$ are also continuous everywhere on $U,$ then the third-order mixed partial derivatives are independent of the order in which the differentiation is performed.

For example,

$$


\dfrac{\partial^3 f}{\color{blue}\partial x\, \partial x\, \partial y} =\dfrac{\partial^3 f}{\color{red}\partial y\, \partial x \, \partial x}.


$$

In this case, we can think of $\color{blue}\partial x\, \partial x\, \partial y$ and $\color{red}\partial y\, \partial x \, \partial x$ as distinct permutations of the symbols $\partial x,\partial x,$ and $\partial y.$ Any permutation of these symbols gives the same result. For example,

$$


\dfrac{\partial^3 f}{\color{blue}\partial x\, \partial x\, \partial y} = \dfrac{\partial^3 f}{\color{purple}\partial x\, \partial y\, \partial x}.


$$

**Watch out!** This does **not** mean that *all* third partial derivatives are equal! For example, it is generally true that

$$


\dfrac{\partial^3 f}{\color{blue}\partial x\, \partial x\, \partial y} \neq \dfrac{\partial^3 f}{\partial x\, \partial y\, \partial y}.


$$

These are not equal because $\partial x\, \partial y\, \partial y$ (in the right-hand side denominator) is a permutation of the symbols $\partial x, \partial y, \partial y,$ not $\partial x, \partial x, \partial y.$

### Example: Evaluating Expressions of Partial Derivatives at a Point

#### Question

Consider the function $f(x,y,z).$ Given that all of its higher-order partial derivatives are continuous on an open set $U,$ and that

$$


\dfrac{\partial^2 f}{\partial z\partial x} = -e^xy\sin{(yz)},


$$

evaluate the following expression at the point $(1,\pi,1)\mathbin{:}$

$$


\dfrac{\partial^3 f}{\partial z\partial x\partial z}+ \dfrac{\partial^3 f }{\partial x \partial z \partial y}


$$

#### Explanation

Since the higher-order partial derivatives are continuous on an open set $U,$ the mixed partial derivatives must be equal.

So, we have

$$


\begin{aligned}\frac{𝜕^{3}𝑓}{𝜕𝑧𝜕𝑥𝜕𝑧} & =\frac{𝜕^{3}𝑓}{𝜕𝑧𝜕𝑧𝜕𝑥} \\ & =\frac{𝜕}{𝜕𝑧}(\frac{𝜕^{2}𝑓}{𝜕𝑧𝜕𝑥}) \\ & =\frac{𝜕}{𝜕𝑧}(−𝑒^{𝑥}𝑦sin⁡(𝑦𝑧)) \\ & =−𝑒^{𝑥}𝑦^{2}cos⁡(𝑦𝑧).\end{aligned}


$$

In addition, we have

$$


\begin{aligned}\frac{𝜕^{3}𝑓}{𝜕𝑥𝜕𝑧𝜕𝑦} & =\frac{𝜕}{𝜕𝑦}(\frac{𝜕^{2}𝑓}{𝜕𝑧𝜕𝑥}) \\ & =\frac{𝜕}{𝜕𝑦}(−𝑒^{𝑥}𝑦sin⁡(𝑦𝑧)) \\ & =−𝑒^{𝑥}sin⁡(𝑦𝑧)−𝑒^{𝑥}𝑦𝑧cos⁡(𝑦𝑧) \\ & =−𝑒^{𝑥}(sin⁡(𝑦𝑧)+𝑦𝑧cos⁡(𝑦𝑧)).\end{aligned}


$$

Now, we evaluate both partial derivatives at the point $(1,\pi,1)\mathbin{:}$

$$


\begin{aligned}\frac{𝜕^{3}𝑓}{𝜕𝑧𝜕𝑥𝜕𝑧}_{(1,𝜋,1)} & =−𝑒^{(1)}(𝜋)^{2}cos⁡(𝜋⋅1)=𝑒𝜋^{2} \\ \frac{𝜕^{3}𝑓}{𝜕𝑥𝜕𝑧𝜕𝑦}_{(1,𝜋,1)} & =−𝑒^{(1)}(sin⁡(𝜋⋅1)+(𝜋)(1)cos⁡(𝜋⋅1))=𝑒𝜋\end{aligned}


$$

Finally, we get

$$


\begin{aligned}\frac{𝜕^{3}𝑓}{𝜕𝑧𝜕𝑥𝜕𝑧}_{(1,𝜋,1)}+\frac{𝜕^{3}𝑓}{𝜕𝑥𝜕𝑧𝜕𝑦}_{(1,𝜋,1)} & =𝑒𝜋^{2}+𝑒𝜋=𝑒𝜋(𝜋+1).\end{aligned}


$$
