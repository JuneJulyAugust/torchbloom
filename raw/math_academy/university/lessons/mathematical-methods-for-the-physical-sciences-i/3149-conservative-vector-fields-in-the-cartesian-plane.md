# Conservative Vector Fields in the Cartesian Plane

Source: https://www.mathacademy.com/topics/3149?courseId=154
Topic ID: 3149

## Prerequisites

- [The Curl of a Vector Field](./2132-the-curl-of-a-vector-field.md)
- [Gradient Vector Fields](./3692-gradient-vector-fields.md)

## Lesson

### Introduction

A vector field $\mathbf F$ is **conservative** if there exists a scalar function $f$ such that

$$


\mathbf{F} = \nabla \! f.


$$

If such a function $f$ exists, it is called a **potential function** for $\mathbf F.$

For example, consider the vector field $\mathbf F,$ given by

$$


\mathbf F(x,y) = 2x\,\mathbf i + 2y\,\mathbf j.


$$

The function $f(x,y) = x^2 + y^2$ is a potential function for $\mathbf F$ because

$$


\begin{aligned}∇𝑓 & =\frac{𝜕𝑓}{𝜕𝑥}\,𝐢+\frac{𝜕𝑓}{𝜕𝑦}\,𝐣 \\ & =\frac{𝜕}{𝜕𝑥}(𝑥^{2}+𝑦^{2})\,𝐢+\frac{𝜕}{𝜕𝑦}(𝑥^{2}+𝑦^{2})\,𝐣 \\ & =2𝑥\,𝐢+2𝑦\,𝐣 \\ & =𝐅.\end{aligned}


$$

Not all vector fields are conservative. However, conservative vector fields have many interesting and useful properties, as we'll soon discover.

### Example: Identifying the Vector Field Corresponding to a Given Potential Function

#### Question

For which vector field is $f(x,y) = \sin(2x-y)$ a potential function?

#### Explanation

A vector field $\mathbf F$ is conservative if it is the gradient of a scalar function $f.$ That is, there exists a function $f$ such that $\mathbf F = \nabla f.$ The function $f$ is called a potential function for $\mathbf F.$

To compute the vector field associated with a potential function $f,$ we compute its gradient:

$$


\begin{aligned}∇𝑓 & =\frac{𝜕𝑓}{𝜕𝑥}\,𝐢+\frac{𝜕𝑓}{𝜕𝑦}\,𝐣 \\ & =\frac{𝜕}{𝜕𝑥}(sin⁡(2𝑥−𝑦))\,𝐢+\frac{𝜕}{𝜕𝑦}(sin⁡(2𝑥−𝑦))\,𝐣 \\ & =2cos⁡(2𝑥−𝑦)\,𝐢−cos⁡(2𝑥−𝑦)\,𝐣 \\ & =𝐅\end{aligned}


$$

Therefore, the vector field that has $f$ as a potential function is

$$


\mathbf F = 2\cos(2x-y)\,\mathbf i -\cos(2x-y) \, \mathbf j.


$$

### A Test to Determine Whether a Given Vector Field is Conservative

Let $\mathbf F(x,y) = P(x,y)\,\mathbf i+ Q(x,y)\,\mathbf j$ be a vector field with domain $D = \mathbb R^2,$ where $P$ and $Q$ have continuous first-order partial derivatives everywhere on $D.$ Then, we have the following theorem:

$\mathbf F$ *is conservative if and only if $\dfrac{\partial P}{\partial y} = \dfrac{\partial Q}{\partial x}$ everywhere on $D.$*

Note that this is equivalent to saying that the scalar curl is zero everywhere on $D,$ i.e.,

$$


\dfrac{\partial Q}{\partial x} - \dfrac{\partial P}{\partial y} = 0.


$$

If $D\neq\mathbb R^2,$ then the situation gets a little trickier. We'll consider this case in a separate lesson.

### Example: Finding a Parameter in a Given Conservative Vector Field

#### Question

Consider the vector field $\mathbf F = \dfrac{2ay}{1+9x^2} \, \mathbf i + \arctan{3x} \, \mathbf j$ on $\mathbb R^2$, where $a$ is a constant. Given that $\mathbf F$ is conservative, find the value of $a.$

#### Explanation

Let $\mathbf F(x,y) = P(x,y)\,\mathbf i+ Q(x,y)\,\mathbf j$ be a vector field with domain $D = \mathbb R^2,$ where $P$ and $Q$ have continuous first-order partial derivatives everywhere on $D.$ Then, we have the following theorem:

$\mathbf F$ **

For the vector field $\mathbf F,$ the domain $D = \mathbb R^2,$ and we have

$$


P = \dfrac{2ay}{1+9x^2}, \qquad Q = \arctan{3x}.


$$

Computing the partial derivatives, we get

$$


\dfrac{\partial P}{\partial y} = \dfrac{2a}{1 + 9x^2}, \qquad \dfrac{\partial Q}{\partial x} = \dfrac{3}{1 + 9x^2}.


$$

It's clear that the partial derivatives exist and are continuous on $\mathbb R^2.$ Equating the partial derivatives, we get

$$


\begin{aligned}\frac{2𝑎}{1+9𝑥^{2}} & =\frac{3}{1+9𝑥^{2}} \\ 2𝑎 & =3 \\ 𝑎 & =\frac{3}{2}.\end{aligned}


$$

Therefore, we conclude that $a = \dfrac{3}{2}.$

### Example: Identifying Conservative Vector Fields

#### Question

Which of the following vector fields are conservative on $\mathbb R^2?$

1. $\mathbf F = (e^{y^2} - 2xy) \, \mathbf i + (2xye^{y^2} - y) \,\mathbf j$

2. $\mathbf G = (3x^2 - y^2) \, \mathbf i + (4 - 2xy) \,\mathbf j$

3. $\mathbf H = (xy^2 + 1) \, \mathbf i + 2xy \,\mathbf j$

#### Explanation

Let $\mathbf F(x,y) = P(x,y)\,\mathbf i+ Q(x,y)\,\mathbf j$ be a vector field with domain $D = \mathbb R^2,$ where $P$ and $Q$ have continuous first-order partial derivatives everywhere on $D.$ Then, we have the following theorem:

$\mathbf F$ **

Note that for each of our functions, $D = \mathbb R^2.$ With this in mind, let's check each of the vector fields.

- For the vector field $\mathbf F,$ we have $P = e^{y^2} - 2xy$ and $Q = 2xye^{y^2} - y.$ Computing the partial derivatives, we get Since the partial derivatives are not equal, we conclude that $\mathbf F$ is not conservative on $\mathbb R^2.$

- For the vector field $\mathbf G,$ we have $P = 3x^2 - y^2$ and $Q = 4 - 2xy.$ Computing the partial derivatives, we get Since the partial derivatives are continuous and equal everywhere on $\mathbb R^2,$ we conclude that $\mathbf{G}$ is conservative on $\mathbb R^2.$

- For the vector field $\mathbf H,$ we have $P = xy^2 + 1$ and $Q = 2xy.$ Computing the partial derivatives, we get Since the partial derivatives are not equal, we conclude that $\mathbf{H}$ is not conservative on $\mathbb R^2.$

Therefore, the correct answer is "II only."
