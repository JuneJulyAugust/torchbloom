# Inner Product Spaces

Source: https://www.mathacademy.com/topics/2096?courseId=55
Topic ID: 2096

## Prerequisites

- [Introduction to Integration by Parts](../../../ap-courses/lessons/ap-calculus-bc/317-introduction-to-integration-by-parts.md)
- [Integration Using the Double-Angle Formulas](../../../ap-courses/lessons/ap-calculus-ab/1038-integration-using-the-double-angle-formulas.md)
- [The Dot Product in N-Dimensional Euclidean Space](./2094-the-dot-product-in-n-dimensional-euclidean-space.md)
- [Defining Abstract Vector Spaces](./3835-defining-abstract-vector-spaces.md)
- [Visualizing Cartesian Products](./4387-visualizing-cartesian-products.md)

## Lesson

### Introduction

Let $V$ be a vector space. Any function $f:V \times V \to \mathbb{R}$ that takes two vectors $\mathbf{a}, \mathbf{b} \in V$ and returns a real number is an **inner product** on $V,$ denoted $\langle \mathbf{a},\mathbf{b} \rangle,$ if the following axioms are satisfied:

- Linearity in the first argument:

- Symmetry:

- Positive definiteness:

The concept of an inner product is a generalization of the dot product. It allows us to apply the geometric ideas of length and angle to abstract vector spaces.

Notice that the standard dot product on $\mathbb{R}^n$ indeed satisfies these axioms. Recall that if $\mathbf u, \mathbf v \in \mathbb R^n,$ then

$$


\langle \mathbf u, \mathbf v\rangle = \mathbf{u}\cdot\mathbf{v} = u_1\cdot v_1 + u_2\cdot v_2 + \cdots + u_n\cdot v_n .


$$

Let $\mathbf u, \mathbf v, \mathbf w \in\mathbb R^n$ and $\alpha \in \mathbb R.$ Let's now check that our three axioms are satisfied.

- We first show that the dot product is linear in the first argument.

- Next, we show that the dot product is symmetric:

- Finally, we show that the dot product is positive definite: which is clearly positive for all $\mathbf u\neq\mathbf 0$ and is zero for $\mathbf u = \mathbf 0 \quad{\color{green}{\checkmark}}$

Since the dot product satisfies our three axioms, we conclude that it is an inner product.

Finally, note that since an inner product is both linear in the first argument and symmetric, then it is also linear in the second argument.

### The Weighted Dot Product

The first type of inner product that we will discuss is the **weighted dot product**.

Given a sequence of positive real numbers $d_1, d_2, \ldots d_n > 0,$ called "weights", the function

$$


\langle \mathbf{x}, \mathbf{y} \rangle = \sum_{i=1}^n d_i x_i y_i


$$

defines an inner product on $\mathbb{R}^n.$ This is similar to the dot product, except here, different components are given different weights.

### Example: Calculating the Inner Product of Two Vectors

#### Question

An inner product on $V = \mathbb{R}^3$ is given by $\langle \mathbf{x}, \mathbf{y} \rangle = 3 x_1 y_1 + x_2 y_2 + 7 x_3 y_3.$ Find $\langle \mathbf{x}, \mathbf{y} \rangle,$ if

$$


\begin{aligned}1 \\ −2 \\ 0\end{aligned}


$$

#### Explanation

Computing the inner product according to the definition, we get

$$


\begin{aligned}⟨𝐱,𝐲⟩ & =3𝑥_{1}𝑦_{1}+𝑥_{2}𝑦_{2}+7𝑥_{3}𝑦_{3} \\ & =3⋅1⋅(−3)+(−2)⋅1+7⋅0⋅5 \\ & =−9−2+0 \\ & =−11.\end{aligned}


$$

### An Inner Product of Polynomials in One Variable

The next inner product that we will discuss concerns inner products on polynomials.

Given a sequence of distinct real numbers the function defines an inner product on the vector space of polynomials of degree at most

Let's consider a few examples:

- The following function defines an inner product on

- The following function defines an inner product on

- The following function defines an inner product on

Notice that this inner product on requires summing terms. This is essential to ensure positive definiteness. For example, the function is *not* an inner product on since there exist nonzero polynomials such that which violates the condition

In general, a nonzero polynomial of degree at most can have at most distinct roots, so vanishing at distinct points forces the polynomial to be zero.

### Example: Calculating the Inner Product of Two Vectors in a Vector Space of Polynomials

#### Question

Let $V=\mathbb{R}_2[t]$ be the vector space of all polynomials of degree at most $2$, equipped with the inner product

$$


\langle {x}(t), {y}(t) \rangle = x(1)y(1) + x(2)y(2) + x(3)y(3).


$$

Find $\langle \mathbf{x}(t), \mathbf{y}(t) \rangle,$ if

$$


{x}(t) = 1-2t+3t^2, \quad {y}(t) = t-t^2.


$$

#### Explanation

Computing the inner product according to the definition, we get

$$


\begin{aligned}⟨𝑥(𝑡),𝑦(𝑡)⟩ & =𝑥(1)𝑦(1)+𝑥(2)𝑦(2)+𝑥(3)𝑦(3) \\ & =2⋅0+9⋅(−2)+22⋅(−6) \\ & =0−18−132 \\ & =−150.\end{aligned}


$$

### An Inner Product of Functions in One Variable

Our final inner product is a generalization of what we saw in the previous example. The function

$$


\langle x(t), y(t) \rangle = \displaystyle\int_{a}^{b} x(t) y(t) \, \text{d}t


$$

defines an inner product on $\mathcal{C}[a,b],$ the vector space of continuous functions on $[a,b].$

Here, instead of finding the product of the functions at some discrete points and summing them, we sum (integrate) the product of the functions over the whole interval $[a,b].$

### Example: Calculating the Inner Product of Two Vectors in a Vector Space of Continuous Functions

#### Question

Let $V=\mathcal{C}\left[0,2\pi\right],$ the vector space of all functions that are continuous on $\left[0,2\pi\right].$ Find $\langle \sin t, \cos t \rangle$ if the inner product on $V$ is defined as

$$


\langle x(t),y(t) \rangle = \displaystyle\int_{0}^{2\pi} x(t) y(t) \, \text{d}t.


$$

#### Explanation

We need to evaluate

$$


\langle \sin t, \cos t \rangle = \int_{0}^{2\pi}\sin{t} \cos{t} \,\text{d}t.


$$

We can evaluate this integral using the identity $\sin2t =2\sin t\cos t,$ as follows:

$$


\begin{aligned}∫_{2𝜋0}sin⁡𝑡cos⁡𝑡\,d𝑡 & =\frac{1}{2}∫_{2𝜋0}sin⁡2𝑡\,d𝑡 \\ & =−\frac{1}{4}cos⁡2𝑡_{2𝜋0} \\ & =−\frac{1}{4}(cos⁡4𝜋−cos⁡0) \\ & =−\frac{1}{4}(1−1) \\ & =0\end{aligned}


$$
