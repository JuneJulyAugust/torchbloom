# Properties of the Curl Operator

Source: https://www.mathacademy.com/topics/3700?courseId=154
Topic ID: 3700

## Prerequisites

- [The Curl of a Vector Field](./2132-the-curl-of-a-vector-field.md)
- [Gradient Vector Fields](./3692-gradient-vector-fields.md)

## Lesson

### Introduction

Recall that if $\mathbf F = P\,\mathbf i + Q\,\mathbf j + R\,\mathbf k$ is a vector field on $\mathbb R^3,$ then the curl of $\mathbf F$ is given by

$$


\begin{aligned}𝐢 & 𝐣 & 𝐤 \\ \frac{𝜕}{𝜕𝑥} & \frac{𝜕}{𝜕𝑦} & \frac{𝜕}{𝜕𝑧} \\ 𝑃 & 𝑄 & 𝑅\end{aligned}


$$

The curl is a quantity that's made up of derivatives, so we would expect it to have similar properties to derivatives.

For example, if $\mathbf F$ and $\mathbf H$ are vector fields and $k$ is a scalar constant, then we have the following linearity properties:

$$


\begin{aligned} & ∇×(𝑘𝐅)=𝑘\,∇×𝐅 \\ & ∇×(𝐅+𝐆)=∇×𝐅+∇×𝐆\end{aligned}


$$

Applying these rules can often help us to save time when computing curl. Let's see some examples.

### Example: Finding the Curl of a Vector Field Using Linearity Properties

#### Question

Calculate $\nabla\times(3\mathbf{F} + \mathbf{G})$ at the point $(-1,1,0)$ for the vector fields $\mathbf F$ and $\mathbf G,$ where

$$


\mathbf{F}(x,y,z) = 3x\,\mathbf{i} + y^2z\,\mathbf{j} + 2\,\mathbf{k}, \quad (\nabla\times\mathbf{G})(x,y,z) = 3y^2\,\mathbf{i} + 4z\,\mathbf{j} + \mathbf{k}.


$$

#### Explanation

If $\mathbf F$ and $\mathbf G$ are vector fields and $k$ is a constant, then we have the following linearity properties for curl:

- $\nabla \times (k \mathbf F) = k \nabla \times \mathbf F$

- $\nabla \times (\mathbf F + \mathbf G) = \nabla \times \mathbf F + \nabla \times \mathbf G$

In our case, we have

$$


\begin{aligned}∇×(3𝐅+𝐆) & =∇×(3𝐅)+∇×𝐆 \\ & =3∇×𝐅+∇×𝐆.\end{aligned}


$$

First, we need to calculate $\nabla \times \mathbf{F}.$ In doing so, we get

$$


\begin{aligned}∇×𝐅 & =\begin{aligned}𝐢 & 𝐣 & 𝐤 \\ \frac{𝜕}{𝜕𝑥} & \frac{𝜕}{𝜕𝑦} & \frac{𝜕}{𝜕𝑧} \\ 3𝑥 & 𝑦^{2}𝑧 & 2\end{aligned} \\ & =[\frac{𝜕}{𝜕𝑦}(2)−\frac{𝜕}{𝜕𝑧}(𝑦^{2}𝑧)]𝐢−[\frac{𝜕}{𝜕𝑥}(2)−\frac{𝜕}{𝜕𝑧}(3𝑥)]𝐣+[\frac{𝜕}{𝜕𝑥}(𝑦^{2}𝑧)−\frac{𝜕}{𝜕𝑦}(3𝑥)]𝐤 \\ & =(0−𝑦^{2})𝐢−(0−0)𝐣+(0−0)𝐤 \\ & =−𝑦^{2}\,𝐢.\end{aligned}


$$

Applying the linearity properties, we get

$$


\begin{aligned}∇×(3𝐅+𝐆) & =3∇×𝐅+∇×𝐆 \\ & =3[−𝑦^{2}\,𝐢]+[3𝑦^{2}\,𝐢+4𝑧\,𝐣+𝐤] \\ & =−3𝑦^{2}\,𝐢+3𝑦^{2}\,𝐢+4𝑧\,𝐣+𝐤 \\ & =(3𝑦^{2}−3𝑦^{2})\,𝐢+4𝑧\,𝐣+𝐤 \\ & =4𝑧\,𝐣+𝐤.\end{aligned}


$$

Finally, evaluating at the point $(-1,1,0),$ we get

$$


\begin{aligned}(∇×(𝐅−𝐆))(−1,1,0) & =4(0)\,𝐣+𝐤=𝐤.\end{aligned}


$$

### The Product Rule for Curl

Recall that for functions $f(x)$ and $g(x),$ the product rule for differentiation is given by

$$


\dfrac{\textrm d }{\textrm d x}(f\cdot g) = f\dfrac{\textrm d }{\textrm d x}(g) + g\dfrac{\textrm d }{\textrm d x}(f).


$$

There is an analogous rule for computing the curl of the product of a vector field and a scalar field.

Suppose that $\mathbf F$ is a vector field and $f$ is a scalar field. Then, we have the following identity:

$$


\nabla\times(f\,\mathbf F) = f \, \nabla \times \mathbf {F}+ \nabla \! f \times \mathbf F


$$

where $\nabla f$ is the gradient of $f.$

Notice that the del operator $\nabla$ acts on the terms in the same way as the $\dfrac{\textrm d}{\textrm d x}$ operator in the product rule for differentiation!

There are a few other tips that we can use to remember this rule:

- The term $\nabla\times(f\,\mathbf F)$ on the left-hand side must be a vector field because it's a curl. So, the two terms on the right-hand side must be vector fields, too.

- The term $f \, \nabla \times \mathbf {F}$ on the right-hand side is a vector field because $f$ is a scalar field, $\nabla \times \mathbf F$ is a vector field, and the product of a scalar and a vector field is a vector field. Note that this "product" is just regular multiplication.

- The term $\nabla \! f \times \mathbf F$ on the right-hand side is a vector field because both $\nabla f$ and $\mathbf F$ are vector fields, and the *cross-product* of two vector fields is a vector field.

### Example: Finding the Curl of a Vector Field Using the Product Rule

#### Question

Consider the vector field $\mathbf F(x,y,z) = \langle 0, y-z, x-y\rangle$ and the scalar field $f(x,y,z) = x+y.$ Given that

$$


\nabla\times \mathbf F = \langle 0,\,-1,\,0\rangle, \quad \nabla f = \langle 1,\, 1,\, 0\rangle,


$$

calculate $\nabla\times(f\,\mathbf F)$ at the point $(-1,1,3).$

#### Explanation

We shall use the following identity:

$$


\nabla\times(f\,\mathbf F) = f \nabla \times \mathbf {F}+ \nabla f \times \mathbf F


$$

First, we compute $\nabla f \times \mathbf F.$ We get

$$


\begin{aligned}∇𝑓×𝐅 & =\begin{aligned}𝐢 & 𝐣 & 𝐤 \\ 1 & 1 & 0 \\ 0 & 𝑦−𝑧 & 𝑥−𝑦\end{aligned} \\ & =[1⋅(𝑥−𝑦)−0⋅(𝑦−𝑧)]\,𝐢−[1⋅(𝑥−𝑦)−0⋅(0)]\,𝐣+[1⋅(𝑦−𝑧)−1⋅(0)]\,𝐤 \\ & =(𝑥−𝑦)\,𝐢+(𝑦−𝑥)\,𝐣+(𝑦−𝑧)\,𝐤 \\ & =⟨𝑥−𝑦,\,𝑦−𝑥,\,𝑦−𝑧⟩.\end{aligned}


$$

Therefore, we have

$$


\begin{aligned}∇×(𝑓\,𝐅) & =𝑓∇×𝐅+∇𝑓×𝐅 \\ & =(𝑥+𝑦)⟨0,−1,0⟩+⟨𝑥−𝑦,\,𝑦−𝑥,\,𝑦−𝑧⟩ \\ & =⟨0,−(𝑥+𝑦),0⟩+⟨𝑥−𝑦,\,𝑦−𝑥,\,𝑦−𝑧⟩ \\ & =⟨𝑥−𝑦,\,−2𝑥,\,𝑦−𝑧⟩.\end{aligned}


$$

Finally,

$$


\begin{aligned}∇×(𝑓\,𝐅)(−1,1,3) & =⟨(−1)−1,\,−2(−1),\,1−3⟩ \\ & =⟨−2,\,2,\,−2⟩.\end{aligned}


$$
