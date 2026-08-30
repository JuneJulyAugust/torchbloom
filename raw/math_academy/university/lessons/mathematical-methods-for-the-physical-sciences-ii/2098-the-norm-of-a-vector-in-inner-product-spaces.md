# The Norm of a Vector in Inner Product Spaces

Source: https://www.mathacademy.com/topics/2098?courseId=155
Topic ID: 2098

## Prerequisites

- [The Norm of a Vector in N-Dimensional Euclidean Space](./2095-the-norm-of-a-vector-in-n-dimensional-euclidean-space.md)
- [Inner Product Spaces](./2096-inner-product-spaces.md)

## Lesson

### Introduction

Any vector space $V$ combined with an inner product $\langle \cdot, \cdot \rangle$ on $V$ is called an **inner product space.**

When referring to inner product spaces, we often say that the vector space $V$ is *equipped* with the inner product $\langle \cdot, \cdot \rangle.$

The **norm** of a vector $\mathbf v\in V$ in an inner product space is defined as

$$


\begin{aligned}‖𝐯‖=\sqrt{⟨𝐯,𝐯⟩}.\end{aligned}


$$

This definition allows us to apply the geometric concept of length to vectors defined in abstract vector spaces. This is because the norm of a vector $\mathbf v$ in an inner product space is a generalization of the norm (or length) of a vector in Euclidean space. To see this, recall that for $\mathbf x\in\mathbb R^n,$ we have

$$


\Vert \mathbf{x} \Vert = \sqrt{\mathbf{x} \cdot \mathbf{x}},


$$

and we have already seen that the dot product is itself an inner product.

Let's consider an example. Suppose that an inner product on $V = \mathbb{R}^3$ defined as

$$


\langle \mathbf{x}, \mathbf{y} \rangle = 3x_1 y_1 + 2x_2 y_2 + 2x_3 y_3.


$$

Now consider the vector $\mathbf v\in V,$ given by

$$


\begin{aligned}1 \\ 2 \\ 1\end{aligned}


$$

Computing $\|\mathbf{v}\|$ using our definition, we get

$$


\begin{aligned}‖𝐯‖ & =\sqrt{⟨𝐯,𝐯⟩} \\ & =\sqrt{3⋅(1⋅1)+2⋅(2⋅2)+2⋅(1⋅1)} \\ & =\sqrt{3+8+2} \\ & =\sqrt{13}.\end{aligned}


$$

### Example: Calculating the Norm of a Vector With Respect to a Given Inner Product

#### Question

An inner product on $V = \mathbb{R}^3$ is defined as $\langle \mathbf{x}, \mathbf{y} \rangle = 2x_1 y_1 + x_2 y_2 + 3x_3 y_3.$ Calculate the norm of the vector $\begin{aligned}3 \\ 2 \\ 1\end{aligned}$ under this inner product.

#### Explanation

The norm of a vector $\mathbf v$ with respect to an inner product $\langle \cdot, \cdot \rangle$ is defined as

$$


\begin{aligned}‖𝐯‖=\sqrt{⟨𝐯,𝐯⟩}.\end{aligned}


$$

Computing $\|\mathbf{v}\|$ using our definition, we get

$$


\begin{aligned}‖𝐯‖ & =\sqrt{⟨𝐯,𝐯⟩} \\ & =\sqrt{2⋅(3⋅3)+2⋅2+3⋅(1⋅1)} \\ & =\sqrt{18+4+3} \\ & =\sqrt{25} \\ & =5.\end{aligned}


$$

### Example: Calculating the Norm of a Vector in an Inner Product Space of Polynomials

#### Question

Let $V=\mathbb{R}_2[t]$ be the vector space of all polynomials of degree at most $2,$ equipped with the inner product

$$


\langle {x}(t), {y}(t) \rangle = x(1)y(1) + x(2)y(2) + x(3)y(3).


$$

Calculate the norm of the vector $p(t) = 1 - t^2.$

#### Explanation

The norm of a vector $p(t)$ with respect to an inner product $\langle \cdot, \cdot \rangle$ is defined as

$$


\begin{aligned}‖𝑝(𝑡)‖=\sqrt{⟨𝑝(𝑡),𝑝(𝑡)⟩}.\end{aligned}


$$

Since ${p}(t) = 1-t^2,$ we obtain

$$


p(1)=0,\qquad p(2)= -3,\qquad p(3)=-8.


$$

Computing $\|p(t)\|$ using our definition, we get

$$


\begin{aligned}‖𝑝(𝑡)‖ & =\sqrt{⟨𝑝(𝑡),𝑝(𝑡)⟩} \\ & =\sqrt{𝑝(1)𝑝(1)+𝑝(2)𝑝(2)+𝑝(3)𝑝(3)} \\ & =\sqrt{[𝑝(1)]^{2}+[𝑝(2)]^{2}+[𝑝(3)]^{2}} \\ & =\sqrt{(0)^{2}+(−3)^{2}+(−8)^{2}} \\ & =\sqrt{0+9+64} \\ & =\sqrt{73}.\end{aligned}


$$

### Example: Calculating the Norm of a Vector in an Inner Product Space of Continuous Functions

#### Question

Let $V=\mathcal{C}\left[0,1\right]$ be the vector space of all functions that are continuous on $\left[0,1\right],$ equipped with the inner product

$$


\langle x(t),y(t) \rangle = \displaystyle\int_{0}^{1} x(t) y(t) \, \text{d}t.


$$

Calculate the norm of the vector $f(t)= 2t-1.$

#### Explanation

The norm of a vector $f(t)$ with respect to an inner product $\langle \cdot, \cdot \rangle$ is defined as

$$


\| f(t)\| = \sqrt{\langle f(t), f(t) \rangle}.


$$

Computing the inner product using our definition, we get

$$


\begin{aligned}⟨𝑓(𝑡),𝑓(𝑡)⟩ & =∫_{10}(𝑓(𝑡))^{2}\,d𝑡 \\ & =∫_{10}(2𝑡−1)^{2}\,d𝑡 \\ & =∫_{10}(4𝑡^{2}−4𝑡+1)\,d𝑡 \\ & =(\frac{4𝑡^{3}}{3}−2𝑡^{2}+𝑡)_{10} \\ & =\frac{4}{3}−2+1 \\ & =\frac{1}{3}\end{aligned}


$$

Therefore,

$$


\| f(t)\| = \sqrt{\dfrac{1}{3}} = \dfrac{\sqrt 3}{3}.


$$

### Normalizing a Vector in Inner Product Spaces

Recall that a unit vector is a vector whose length is equal to $1.$ If we divide a non-zero vector $\mathbf{x}\in\mathbb R^n$ by its norm $\Vert \mathbf{x} \Vert,$ we obtain a unit vector:

$$


\mathbf{u}=\dfrac{\mathbf{x}}{\Vert\mathbf{x}\Vert}


$$

The process of constructing a unit vector by dividing $\mathbf x$ by its norm is called **normalization.**

We normalize vectors in more general inner product spaces using the same method.

For example, consider an inner product on $V = \mathbb{R}^3$ defined as $\langle \mathbf{x}, \mathbf{y} \rangle = 2x_1 y_1 + 3x_2 y_2 + x_3 y_3.$ Let's normalize the following vector with respect to our inner product:

$$


\begin{aligned}2 \\ 1 \\ 2\end{aligned}


$$

The norm of a vector $\mathbf v$ with respect to an inner product $\langle \cdot, \cdot \rangle$ is defined as

$$


\begin{aligned}‖𝐯‖=\sqrt{⟨𝐯,𝐯⟩}.\end{aligned}


$$

Computing the inner product using our definition, we get

$$


\begin{aligned}⟨𝐯,𝐯⟩ & =2⋅(2⋅2)+3⋅(1⋅1)+2⋅2 \\ & =8+3+4 \\ & =15.\end{aligned}


$$

Therefore,

$$


\begin{aligned}‖𝐯‖ & =\sqrt{15}.\end{aligned}


$$

To normalize the vector $\mathbf v$, we divide $\mathbf v$ by its norm $\|\mathbf v\| \mathbin{:}$

$$


\begin{aligned}𝐮 & =\frac{𝐯}{‖𝐯‖} \\ & =\frac{1}{\sqrt{15}}\begin{matrix}2 \\ 1 \\ 2\end{matrix} \\ & =\frac{\sqrt{15}}{15}\begin{matrix}2 \\ 1 \\ 2\end{matrix}\end{aligned}


$$

### Example: Normalizing a Vector in an Inner Product Space

#### Question

Let $V=\mathcal{C}\left[0,\pi\right]$ be the vector space of all functions that are continuous on $\left[0,\pi\right],$ equipped with the inner product

$$


\langle x(t),y(t) \rangle = \displaystyle\int_{0}^{\pi} x(t) y(t) \, \text{d}t.


$$

Normalize the vector $f(t)= 3t.$

#### Explanation

The norm of a vector $f(t)$ with respect to an inner product $\langle \cdot, \cdot \rangle$ is defined as

$$


\| f(t)\| = \sqrt{\langle f(t), f(t) \rangle}.


$$

Computing the inner product using our definition, we get

$$


\begin{aligned}⟨𝑓(𝑡),𝑓(𝑡)⟩ & =∫_{𝜋0}(3𝑡)^{2}\,d𝑡 \\ & =∫_{𝜋0}9𝑡^{2}\,d𝑡 \\ & =3𝑡^{3}\,_{𝜋0} \\ & =3𝜋^{3}\end{aligned}


$$

Therefore,

$$


\| f(t) \| = \sqrt{3\pi^3} = \pi \sqrt{3\pi}.


$$

To normalize the vector $f(t),$ we divide $f(t)$ by its norm $\| f(t) \| \mathbin{:}$

$$


\begin{aligned}𝑢(𝑡) & =\frac{𝑓(𝑡)}{‖𝑓(𝑡)‖} \\ & =\frac{1}{𝜋\sqrt{3𝜋}}⋅3𝑡 \\ & =\frac{𝑡\sqrt{3}}{𝜋\sqrt{𝜋}}\end{aligned}


$$
