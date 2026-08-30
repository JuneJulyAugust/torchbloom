# Properties of the Divergence Operator

Source: https://www.mathacademy.com/topics/3701?courseId=154
Topic ID: 3701

## Prerequisites

- [The Divergence of a Vector Field](./2131-the-divergence-of-a-vector-field.md)
- [Gradient Vector Fields](./3692-gradient-vector-fields.md)

## Lesson

### Introduction

Recall that if $\mathbf F = P\,\mathbf i + Q\,\mathbf j + R\,\mathbf k$ is a vector field on $\mathbb R^3,$ then the divergence of $\mathbf F$ is given by

$$


\textrm{div}\,\mathbf F = \nabla\cdot \mathbf F = \dfrac{\partial P}{\partial x} + \dfrac{\partial Q}{\partial y} + \dfrac{\partial R}{\partial z}.


$$

Since divergence is computed using derivatives, it's unsurprising that it shares similar properties with derivatives.

For example, if $\mathbf F$ and $\mathbf H$ are vector fields and $k$ is a scalar constant, then we have the following linearity properties:

$$


\begin{aligned} & ∇⋅(𝑘\,𝐅)=𝑘\,(∇⋅𝐅) \\ & ∇⋅(𝐅+𝐇)=∇⋅𝐅+∇⋅𝐇\end{aligned}


$$

Applying these rules can often help us to save time when computing divergence. Let's see some examples.

### Example: Finding the Divergence of a Vector Field Using Linearity Properties

#### Question

Calculate $\nabla \cdot (\mathbf{F}-3\mathbf{G})$ for the vector fields $\mathbf F$ and $\mathbf G,$ where

$$


\mathbf{F}=\left(x^2+y\right)\,\mathbf{i}+ \left(xy-y^2\right)\,\mathbf{j}, \quad \nabla \cdot \mathbf{G}=x+y.


$$

#### Explanation

If $\mathbf F$ and $\mathbf G$ are vector fields and $k$ is a constant, then we have the following linearity properties for divergence:

- $\nabla \cdot (k \mathbf F) = k \nabla \cdot \mathbf F$

- $\nabla \cdot (\mathbf F + \mathbf G) = \nabla \cdot \mathbf F + \nabla \cdot \mathbf G$

In our case, we have

$$


\begin{aligned}∇⋅(𝐅−3𝐆) & =∇⋅(𝐅)+∇⋅(−3𝐆) \\ & =∇⋅𝐅−3∇⋅𝐆.\end{aligned}


$$

First, we need to calculate $\nabla \cdot \mathbf{F}.$ In doing so, we get

$$


\begin{aligned}∇⋅𝐅 & =\frac{𝜕}{𝜕𝑥}(𝑥^{2}+𝑦)+\frac{𝜕}{𝜕𝑦}(𝑥𝑦−𝑦^{2}) \\ & =2𝑥+𝑥−2𝑦 \\ & =3𝑥−2𝑦.\end{aligned}


$$

Applying the linearity properties, we get

$$


\begin{aligned}∇⋅(𝐅−3𝐆) & =∇⋅𝐅−3∇⋅𝐆 \\ & =(3𝑥−2𝑦)−3⋅(𝑥+𝑦) \\ & =−5𝑦.\end{aligned}


$$

### The Product Rule for Divergence

Recall that for functions $f(x)$ and $g(x),$ the product rule for differentiation is given by

$$


\dfrac{\textrm d }{\textrm d x}(f\cdot g) = f\dfrac{\textrm d }{\textrm d x}(g) + g\dfrac{\textrm d }{\textrm d x}(f).


$$

There is an analogous rule for computing the divergence of the product of a vector field and a scalar field.

Suppose that $\mathbf F$ is a vector field and $f$ is a scalar field. Then, we have the following identity:

$$


\nabla \cdot (f\,\mathbf F) = f\, \nabla \cdot \mathbf {F}+ \mathbf F \cdot \nabla \! f


$$

where $\nabla f$ is the gradient of $f.$

Notice that the del operator $\nabla$ acts on the terms in the same way as the $\dfrac{\textrm d}{\textrm d x}$ operator in the product rule for differentiation!

There are a few other tips that we can use to remember this rule:

- The term $\nabla \cdot (f\,\mathbf F)$ on the left-hand side must be a scalar field because it's a divergence. So, the two terms on the right-hand side must be scalar fields, too.

- The term $f\, \nabla \cdot \mathbf {F}$ on the right-hand side is a scalar field because both $f$ and $\nabla \cdot \mathbf F$ are scalar fields, and the product of two scalar fields is a scalar field. Note that this "product" is just regular multiplication.

- The term $\mathbf F \cdot \nabla \! f$ on the right-hand side is a scalar field because both $\mathbf F$ and $\nabla f$ are *vector* fields, and the *dot product* of two vector fields is a scalar field.

### Example: Finding the Divergence of a Vector Field Using the Product Rule

#### Question

Given that $\mathbf F(x,y) = \left\langle \dfrac 1x, xy \right \rangle$ and $f(x,y) = \dfrac 1{x},$ calculate $\nabla \cdot (f\,\mathbf F).$

#### Explanation

We will use the following identity:

$$


\nabla \cdot (f\,\mathbf F) = f\, \nabla \cdot \mathbf {F}+ \mathbf F \cdot \nabla f


$$

First, we compute $\nabla \cdot \mathbf {F}$ and $\nabla f.$ We get

$$


\begin{aligned}∇𝑓 & =⟨−\frac{1}{𝑥^{2}},0⟩, \\ ∇⋅𝐅 & =\frac{𝜕}{𝜕𝑥}(\frac{1}{𝑥})+\frac{𝜕}{𝜕𝑦}(𝑥𝑦)=−\frac{1}{𝑥^{2}}+𝑥.\end{aligned}


$$

Therefore, we have

$$


\begin{aligned}∇⋅(𝑓\,𝐅) & =𝑓\,∇⋅𝐅+𝐅⋅∇𝑓 \\ & =\frac{1}{𝑥}(−\frac{1}{𝑥^{2}}+𝑥)+⟨\frac{1}{𝑥},𝑥𝑦⟩⋅⟨−\frac{1}{𝑥^{2}},0⟩ \\ & =−\frac{1}{𝑥^{3}}+1−\frac{1}{𝑥^{3}} \\ & =1−\frac{2}{𝑥^{3}}.\end{aligned}


$$
