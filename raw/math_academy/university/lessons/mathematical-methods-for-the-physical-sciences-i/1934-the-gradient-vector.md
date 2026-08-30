# The Gradient Vector

Source: https://www.mathacademy.com/topics/1934?courseId=154
Topic ID: 1934

## Prerequisites

- [Continuity and Differentiability of Functions](../../../ap-courses/lessons/ap-calculus-ab/1691-continuity-and-differentiability-of-functions.md)
- [Partial Differentiability of Multivariable Functions](./1932-partial-differentiability-of-multivariable-functions.md)
- [Geometric Interpretations of Partial Derivatives](./1955-geometric-interpretations-of-partial-derivatives.md)

## Lesson

### Introduction

The **gradient** of a multivariable function is analogous to the derivative of a single-variable function.

For a function $f(x,y)$ whose partial derivatives exist at a point $(x,y),$ the **gradient vector** is denoted $\nabla f(x,y)$ and can be found by computing the vector of partial derivatives:

$$


\begin{aligned} \nabla f (x,y) = \dfrac{\partial f}{\partial x} \mathbf i + \dfrac{\partial f}{\partial y} \mathbf j \end{aligned}


$$

### Example: Calculating the Gradient of a Function of Two Variables

#### Question

Find $\nabla f(x,y)$ at the point $(1,\pi)$ given that $f(x,y) = (x - y)\cos y.$

#### Explanation

First, we find the partial derivatives:

$$


\begin{aligned}𝑓_{𝑥}(𝑥,𝑦) & =\frac{𝜕}{𝜕𝑥}((𝑥−𝑦)cos⁡𝑦) \\ & =cos⁡𝑦 \\ 𝑓_{𝑦}(𝑥,𝑦) & =\frac{𝜕}{𝜕𝑦}((𝑥−𝑦)cos⁡𝑦) \\ & =−cos⁡𝑦−(𝑥−𝑦)sin⁡𝑦\end{aligned}


$$

So, the gradient is

$$


\begin{aligned}∇\,𝑓(𝑥,𝑦) & =𝑓_{𝑥}(𝑥,𝑦) 𝐢+𝑓_{𝑦}(𝑥,𝑦) 𝐣 \\ & =cos⁡𝑦 𝐢−(cos⁡𝑦+(𝑥−𝑦)sin⁡𝑦) 𝐣.\end{aligned}


$$

Finally, to find the gradient at the specified point, we substitute $(x,y)= (1,\pi)$ into the above, which gives

$$


\begin{aligned}∇\,𝑓(1,𝜋) & =𝑓_{𝑥}(1,𝜋) 𝐢+𝑓_{𝑦}(1,𝜋) 𝐣 \\ & =cos⁡𝜋 𝐢−(cos⁡𝜋+(1−𝜋)sin⁡𝜋) 𝐣 \\ & =−𝐢+𝐣.\end{aligned}


$$

### The Gradient of a Function of More Than Two Variables

For a function of three variables $f(x,y,z)$, the gradient of $f$ is given by the vector

$$


\begin{aligned} \nabla \! f (x,y,z) &= f_x(x,y,z)\\\mathbf i + f_y (x,y,z)\\\mathbf j + f_z (x,y,z)\\\mathbf k. \end{aligned}


$$

For a function $f(x_1, x_2, \ldots, x_n)$ of $n$ variables, its gradient is usually given as a column vector:

$$


\begin{aligned}𝑓_{𝑥_{1}} \\ 𝑓_{𝑥_{2}} \\ ⋮ \\ 𝑓_{𝑥_{𝑛}}\end{aligned}


$$

### Example: Calculating the Gradient of a Function of Three Variables

#### Question

Evaluate $\nabla g(x,y,z)$ at $(2,-1,3)$ if $g(x,y,z) = x^2 + xyz.$

#### Explanation

First, we find the partial derivatives:

$$


\begin{aligned}𝑔_{𝑥}(𝑥,𝑦,𝑧) & =\frac{𝜕}{𝜕𝑥}(𝑥^{2}+𝑥𝑦𝑧) \\ & =2𝑥+𝑦𝑧 \\ 𝑔_{𝑦}(𝑥,𝑦,𝑧) & =\frac{𝜕}{𝜕𝑦}(𝑥^{2}+𝑥𝑦𝑧) \\ & =0+𝑥𝑧 \\ & =𝑥𝑧 \\ 𝑔_{𝑧}(𝑥,𝑦,𝑧) & =\frac{𝜕}{𝜕𝑧}(𝑥^{2}+𝑥𝑦𝑧) \\ & =0+𝑥𝑦 \\ & =𝑥𝑦\end{aligned}


$$

Therefore, the gradient is

$$


\begin{aligned}∇𝑔(𝑥,𝑦,𝑧) & =𝑔_{𝑥}(𝑥,𝑦,𝑧) 𝐢+𝑔_{𝑦}(𝑥,𝑦,𝑧) 𝐣+𝑔_{𝑧}(𝑥,𝑦,𝑧) 𝐤 \\ & =(2𝑥+𝑦𝑧) 𝐢+(𝑥𝑧) 𝐣+(𝑥𝑦) 𝐤 \\ ∇𝑔(2,−1,3) & =(2(2)+(−1)(3)) 𝐢+2(3) 𝐣+2(−1) 𝐤 \\ & =1 𝐢+6 𝐣−2 𝐤 \\ & =𝐢+6 𝐣−2 𝐤.\end{aligned}


$$

### Example: Finding the Points Where a Gradient Vanishes

#### Question

Given that $f(x,y)= (y-4)\ln (x-2),$ find the points $(x, y)$ where $\nabla f(x,y) = \mathbf 0.$

#### Explanation

First, we find the partial derivatives:

$$


\begin{aligned}\frac{𝜕𝑓}{𝜕𝑥} & =\frac{𝜕}{𝜕𝑥}((𝑦−4)ln⁡(𝑥−2)) \\ & =\frac{𝑦−4}{𝑥−2} \\ \frac{𝜕𝑓}{𝜕𝑦} & =\frac{𝜕}{𝜕𝑦}((𝑦−4)ln⁡(𝑥−2)) \\ & =ln⁡(𝑥−2)\end{aligned}


$$

So, we have

$$


\nabla f(x,y) = \dfrac {y-4}{x-2} \, \mathbf i + \ln(x-2) \, \mathbf j.


$$

Now, we solve $\nabla f(x,y) = \mathbf 0\mathbin{:}$

$$


\dfrac {y-4}{x-2} \, \mathbf i + \ln(x-2) \, \mathbf j = 0 \ \mathbf i + 0\ \mathbf j


$$

By equating the coefficients of $\mathbf{i}$ on both sides of the equation (and similarly with $\mathbf{j}$), we obtain

$$


\begin{aligned}\frac{𝑦−4}{𝑥−2}=0 \\ ln⁡(𝑥−2)=0.\end{aligned}


$$

From the first equation, we get $y-4=0,$ which means $y=4.$ From the second equation, we obtain $\ln(x-2)=0,$ which means that $x=3.$

Therefore, $\nabla f(x,y) =\mathbf 0$ at the point $(3,4).$

### Properties of the Gradient

Since the gradient of a function of several variables is made up of partial derivatives, we can expect it to have properties that are similar to partial derivatives.

Assume that $f$ and $g$ are functions whose first-order partial derivatives exist and are continuous on some open domain, and that $a,b,$ and $c$ are real constants. Then, the gradient has the following properties:

- Constant rule: $\nabla c = \mathbf 0$

- Linearity: $\nabla (af + bg) = a \nabla\! f + b\nabla\! g$

- Product Rule: $\nabla(fg) = g \nabla\! f + f \nabla\! g$

- Quotient Rule: $\nabla \left(\dfrac{f}{g}\right) = \dfrac{g \nabla\! f - f \nabla\! g}{g^2}$

### Example: Calculating the Gradient Using the Properties of the Gradient

#### Question

Find the gradient of the product $f(x,y) g(x,y)$ given that

$$


\begin{aligned}𝑓(𝑥,𝑦) & =𝑥𝑦,\, & & ∇𝑓(𝑥,𝑦)=𝑦 𝐢+𝑥 𝐣, & & \\ 𝑔(𝑥,𝑦) & =\sqrt{√𝑥𝑦},\, & & ∇𝑔(𝑥,𝑦)=\frac{\sqrt{√𝑥𝑦}}{2𝑥} 𝐢+\frac{\sqrt{√𝑥𝑦}}{2𝑦} 𝐣. & & \end{aligned}


$$

#### Explanation

The gradient of the product of two functions $f(x,y)$ and $g(x,y)$ is given by

$$


\nabla [fg] = g \, \nabla\! f + f \, \nabla\! g.


$$

Using the product rule shown above, we obtain

$$


\begin{aligned}∇[𝑓(𝑥,𝑦)𝑔(𝑥,𝑦)] & =𝑔(𝑥,𝑦)∇𝑓(𝑥,𝑦)+𝑓(𝑥,𝑦)∇𝑔(𝑥,𝑦) \\ & =\sqrt{√𝑥𝑦}(𝑦 𝐢+𝑥 𝐣)+𝑥𝑦(\frac{\sqrt{√𝑥𝑦}}{2𝑥} 𝐢+\frac{\sqrt{√𝑥𝑦}}{2𝑦} 𝐣) \\ & =\sqrt{√𝑥𝑦}(𝑦 𝐢+𝑥 𝐣)+\frac{\sqrt{√𝑥𝑦}}{2}(𝑦 𝐢+𝑥 𝐣) \\ & =\frac{3\sqrt{√𝑥𝑦}}{2}(𝑦 𝐢+𝑥 𝐣).\end{aligned}


$$

### Continuous Partial Derivatives Imply Continuity

For a multivariable function, the existence of the gradient implies continuity.

A sufficient condition for the gradient to exist is that the partial derivatives and both exist in a neighborhood of and are continuous at.

Therefore, if and both exist in a neighborhood of and are continuous at, then is continuous at

**Watch out!** The continuity of the partial derivatives is crucial. The existence of the partial derivatives alone does not imply that a function is continuous at a point.
