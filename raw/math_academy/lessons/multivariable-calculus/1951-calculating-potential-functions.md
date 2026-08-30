# Calculating Potential Functions

Source: https://www.mathacademy.com/topics/1951?courseId=54
Topic ID: 1951

## Prerequisites

- [Solving First-Order ODEs Using Direct Integration](../ap-calculus-ab/1061-solving-first-order-odes-using-direct-integration.md)
- [Equality of Mixed Partial Derivatives](./1957-equality-of-mixed-partial-derivatives.md)
- [Conservative Vector Fields in the Cartesian Plane](./3149-conservative-vector-fields-in-the-cartesian-plane.md)

## Lesson

### Introduction

Suppose we know that the gradient of a function $f(x,y)$ is

$$


\nabla f(x,y) = (2xy-3x^2) \ \mathbf i + (x^2-2y) \ \mathbf j.


$$

How can we reconstruct the function $f(x,y)$ knowing only its gradient?

Since the components of $\nabla f$ must be the first-order partial derivatives of $f$ with respect to $x$ and $y$ respectively, we know that

$$


\begin{aligned} \dfrac {\partial f}{\partial x} = 2xy-3x^2, \qquad \dfrac {\partial f}{\partial y}=x^2-2y.\end{aligned}


$$

Integrating $\dfrac {\partial f}{\partial x}$ with respect to $x,$ treating $y$ as a constant, we get

$$


f(x,y) = \int \left(2xy-3x^2\right) \textrm d x = x^2y -x^3 +g(y),


$$

where $g(y)$ is an arbitrary function of $y.$ Intuitively, $g(y)$ contains all the terms that would vanish when differentiated with respect to $x.$

Now, differentiating the above with respect to $y$ gives

$$


\dfrac {\partial f}{\partial y} = x^2 + g'(y).


$$

So, equating the two expressions for $\dfrac {\partial f}{\partial y}$ yields

$$


\begin{aligned} x^2 + g'(y) &= x^2-2y\\g'(y) & = -2y. \end{aligned}


$$

Therefore, $\displaystyle g(y)=\int(-2y) \ \textrm d y = -y^2 +C.$

This means that

$$


f(x,y)=x^2y -x^3-y^2 +C .


$$

Note that the above procedure is symmetric with respect to $x$ and $y.$ We could have started by integrating $\dfrac {\partial f}{\partial y}$ with respect to $y$ and then differentiating with respect to $x.$ The final result would have been the same.

### Example: Reconstructing a Two-Variable Function From Its Gradient

#### Question

Find $f(x,y)$ such that $\nabla f = \mathbf{F},$ where $\mathbf F(x,y) = 2xy\ \mathbf i + (x^2 - 3)\ \mathbf j.$

#### Explanation

The gradient of the function $f(x,y)$ is defined as

$$


\nabla f(x,y) = \dfrac{\partial{f}}{\partial{x}}\,\textbf{i} + \dfrac{\partial{f}}{\partial{y}}\,\textbf{j}.


$$

Since $\nabla f(x,y) = \mathbf F(x,y),$ the function $f(x,y)$ must satisfy the following system:

$$


\dfrac{\partial{f}}{\partial{x}} = 2xy, \qquad \dfrac{\partial{f}}{\partial{y}} = x^2-3.


$$

First, we integrate $\dfrac{\partial{f}}{\partial{x}}$ with respect to $x.$ Note that the solution should contain an arbitrary function of $y\mathbin{:}$

$$


\begin{aligned}𝑓(𝑥,𝑦) & =∫\frac{𝜕𝑓}{𝜕𝑥}\,d𝑥 \\ & =∫2𝑥𝑦\,d𝑥 \\ & =𝑥^{2}𝑦+𝑔(𝑦)\end{aligned}


$$

Now, differentiating the above expression with respect to $y,$ we obtain

$$


\dfrac{\partial{f}}{\partial{y}} = x^2 + g'(y).


$$

Taking $\dfrac{\partial{f}}{\partial{y}} = x^2 -3$ into account, we obtain

$$


\begin{aligned}𝑥^{2}+𝑔^{′}(𝑦) & =𝑥^{2}−3 \\ 𝑔^{′}(𝑦) & =−3 \\ 𝑔(𝑦) & =−3𝑦+𝐶,\end{aligned}


$$

where $C$ is a constant.

Finally, substituting $g(y)=-3y +C$ into our expression for $f(x,y),$ we get

$$


f(x,y) = x^2y -3y + C.


$$

### Example: Reconstructing a Three-Variable Function From Its Gradient

#### Question

Find $f(x,y,z)$ such that $\nabla f(x,y,z) = \mathbf{F}(x,y,z),$ where $\mathbf{F}(x,y,z) = yz\,\mathbf{i} + (xz + 4z^2)\,\mathbf{j} + (xy+8yz)\,\mathbf{k}.$

#### Explanation

The gradient of the function $f(x,y,z)$ is defined as

$$


\nabla f(x,y,z) = \dfrac{\partial{f}}{\partial{x}} \, \mathbf{i} + \dfrac{\partial{f}}{\partial{y}} \, \mathbf{j} + \dfrac{\partial{f}}{\partial{z}} \, \mathbf{k}.


$$

Since $\nabla f(x,y,z) = \mathbf{F}(x,y,z),$ the function $f(x,y,z)$ must satisfy the following system:

$$


\dfrac{\partial{f}}{\partial{x}} = yz, \qquad \dfrac{\partial{f}}{\partial{y}} = xz + 4z^2, \qquad \dfrac{\partial{f}}{\partial{z}} = xy+8yz.


$$

First, we integrate $\dfrac{\partial{f}}{\partial{x}}$ with respect to $x.$ Note that the solution should contain an arbitrary function of $y$ and $z \mathbin{:}$

$$


\begin{aligned}𝑓(𝑥,𝑦,𝑧) & =∫\frac{𝜕𝑓}{𝜕𝑥}\,d𝑥 \\ & =∫𝑦𝑧\,d𝑥 \\ & =𝑥𝑦𝑧+𝑔(𝑦,𝑧)\end{aligned}


$$

Now, differentiating the above expression with respect to $y,$ we obtain

$$


\dfrac{\partial{f}}{\partial{y}} = xz + \dfrac{\partial{g}}{\partial{y}}.


$$

Taking $\dfrac{\partial{f}}{\partial{y}} = xz + 4z^2$ into account, we obtain

$$


\begin{aligned}𝑥𝑧+\frac{𝜕𝑔}{𝜕𝑦} & =𝑥𝑧+4𝑧^{2} \\ \frac{𝜕𝑔}{𝜕𝑦} & =4𝑧^{2}.\end{aligned}


$$

Now, we integrate $\dfrac{\partial{g}}{\partial{y}}$ with respect to $y.$ Note that the solution should contain an arbitrary function of $z \mathbin{:}$

$$


\begin{aligned}𝑔(𝑦,𝑧) & =∫\frac{𝜕𝑔}{𝜕𝑦}\,d𝑦 \\ & =∫4𝑧^{2}\,d𝑦 \\ & =4𝑦𝑧^{2}+ℎ(𝑧)\end{aligned}


$$

Substituting $g(y,z) = 4yz^2 + h(z)$ in the expression for $f(x, y,z),$ we get

$$


f(x,y,z) = xyz + 4yz^2 + h(z).


$$

To determine the function $h(z),$ we differentiate $f(x,y,z)$ with respect to $z.$ This gives

$$


\dfrac{\partial{f}}{\partial{z}} = xy + 8yz + h'(z).


$$

Taking $\dfrac{\partial{f}}{\partial{z}} = xy+8yz$ into account, we obtain

$$


\begin{aligned}𝑥𝑦+8𝑦𝑧 & =𝑥𝑦+8𝑦𝑧+ℎ^{′}(𝑧) \\ ℎ^{′}(𝑧) & =0 \\ ℎ(𝑧) & =𝐶,\end{aligned}


$$

where $C$ is a constant.

Consequently,

$$


f(x,y,z) = xyz + 4yz^2 + C.


$$
