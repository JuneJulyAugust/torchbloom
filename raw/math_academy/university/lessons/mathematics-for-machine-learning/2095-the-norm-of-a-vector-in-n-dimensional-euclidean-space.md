# The Norm of a Vector in N-Dimensional Euclidean Space

Source: https://www.mathacademy.com/topics/2095?courseId=145
Topic ID: 2095

## Prerequisites

- [The Dot Product in N-Dimensional Euclidean Space](./2094-the-dot-product-in-n-dimensional-euclidean-space.md)

## Lesson

### Introduction

The vector space $\mathbb{R}^n,$ paired with the dot product, is called a **Euclidean space**.

For a vector $\begin{aligned}𝑥_{1} \\ 𝑥_{2} \\ ⋮ \\ 𝑥_{𝑛}\end{aligned}$ in $\mathbb{R}^n,$ the **norm** (or **length**) is given by

$$


\Vert \mathbf{x} \Vert = \sqrt{\mathbf{x} \cdot \mathbf{x}} = \sqrt{x_1^2+x_2^2+\ldots+x_n^2}.


$$

For example, consider the vector $[\begin{aligned}−5 \\ 12\end{aligned}]$ The norm of this vector is calculated as

$$


\begin{aligned}‖𝐱‖ & =\sqrt{𝑥_{21}+𝑥_{22}} \\ & =\sqrt{(−5)^{2}+(12)^{2}} \\ & =\sqrt{25+144} \\ & =\sqrt{169} \\ & =13.\end{aligned}


$$

Note that the dot product of a vector with itself is always non-negative, $\mathbf{x}\cdot\mathbf{x}\geq 0,$ so it's always possible to take the square root $\sqrt{\mathbf{x}\cdot\mathbf{x}}.$

### Example: Calculating the Norm of a Vector

#### Question

Given $\begin{aligned}3 \\ −4 \\ −5\end{aligned}$ find $\|\mathbf{x}\|.$

#### Explanation

Using the formula for the norm, we have

$$


\begin{aligned}‖𝐱‖ & =\sqrt{𝑥_{21}+𝑥_{22}+𝑥_{23}} \\ & =\sqrt{3^{2}+(−4)^{2}+(−5)^{2}} \\ & =\sqrt{9+16+25} \\ & =\sqrt{50} \\ & =5\sqrt{2}.\end{aligned}


$$

### The Distance Between Two Vectors

In a Euclidean space, the **distance** between the vectors $\mathbf{x}$ and $\mathbf{y}$ is the norm of the difference $\mathbf{x}-\mathbf{y},$ that is

$$


\text{d}(\mathbf{x}, \mathbf{y}) = \Vert \mathbf{x} - \mathbf{y} \Vert.


$$

To create a formula for the distance, we write the vectors in component form:

$$


\begin{aligned}𝑥_{1} \\ 𝑥_{2} \\ ⋮ \\ 𝑥_{𝑛}\end{aligned}


$$

Now, we can express the norm in terms of the components:

$$


\begin{aligned}d(𝐱,𝐲) & =‖𝐱−𝐲‖ \\ & =\sqrt{(𝑥_{1}−𝑦_{1})^{2}+(𝑥_{2}−𝑦_{2})^{2}+⋯+(𝑥_{𝑛}−𝑦_{𝑛})^{2}}\end{aligned}


$$

For example, we can use the formula to find the distance between the vectors $[\begin{aligned}1 \\ 4\end{aligned}]$ and $[\begin{aligned}−5 \\ 1\end{aligned}]$ as follows:

$$


\begin{aligned}d(𝐱,𝐲) & =‖𝐱−𝐲‖ \\ & =\sqrt{(𝑥_{1}−𝑦_{1})^{2}+(𝑥_{2}−𝑦_{2})^{2}} \\ & =\sqrt{(1−(−5))^{2}+(4−1)^{2}} \\ & =\sqrt{6^{2}+3^{2}} \\ & =\sqrt{45} \\ & =3\sqrt{5}\end{aligned}


$$

### Example: Finding the Distance Between Two Vectors

#### Question

Given the vectors $\begin{aligned}−1 \\ 2 \\ 3\end{aligned}$ and $\begin{aligned}2 \\ 0 \\ −1\end{aligned}$ find the distance $\text{d}(\mathbf{x}, \mathbf{y}).$

#### Explanation

Using the formula for the distance, we have

$$


\begin{aligned}d(𝐱,𝐲) & =‖𝐱−𝐲‖ \\ & =\sqrt{(𝑥_{1}−𝑦_{1})^{2}+(𝑥_{2}−𝑦_{2})^{2}+(𝑥_{3}−𝑦_{3})^{2}} \\ & =\sqrt{(−1−2)^{2}+(2−0)^{2}+(3−(−1))^{2}} \\ & =\sqrt{(−3)^{2}+2^{2}+4^{2}} \\ & =\sqrt{9+4+16} \\ & =\sqrt{29}.\end{aligned}


$$

### Factoring a Constant Out of the Norm

We can factor a constant out of the norm, provided that we take the absolute value of the constant:

$$


\Vert k \mathbf{x} \Vert= \vert k \vert \cdot \Vert \mathbf{x} \Vert


$$

For example, consider the vector $[\begin{aligned}3 \\ 4\end{aligned}]$ To compute the norm of a multiple of $\mathbf{x},$ say ${\color{blue}-2}\mathbf{x},$ we can factor the absolute value $|{\color{blue}-2}|$ out of the norm as follows:

$$


\begin{aligned}‖−2𝐱‖ & =|−2|⋅‖𝐱‖ \\ & =2⋅\sqrt{𝑥_{21}+𝑥_{22}} \\ & =2⋅\sqrt{3^{2}+4^{2}} \\ & =2⋅\sqrt{9+16} \\ & =2⋅\sqrt{25} \\ & =2⋅5 \\ & =10.\end{aligned}


$$

**Note:** We can verify that we'd get the same result if we multiplied the $\color{blue}-2$ first, before computing the norm. Multiplying by ${\color{blue}-2},$ we have

$$


[\begin{aligned}3 \\ 4\end{aligned}]


$$

Then, computing the norm, we get

$$


\begin{aligned}‖−2𝐱‖ & =\sqrt{𝑥_{21}+𝑥_{22}} \\ & =\sqrt{(−6)^{2}+(−8)^{2}} \\ & =\sqrt{36+64} \\ & =\sqrt{100} \\ & =10.\,✓\end{aligned}


$$

### Example: Factoring a Constant Out of the Norm

#### Question

If $\left\Vert {- \dfrac{\mathbf{x}}{2}} \right\Vert = 5,$ find $\Vert 3 \mathbf{x} \Vert.$

#### Explanation

Remember that we can factor a constant out of the norm, provided that we take the absolute value of the constant:

$$


\Vert k \mathbf{x} \Vert= \vert k \vert \cdot \Vert \mathbf{x} \Vert


$$

Using this fact, we can solve for the norm $\Vert x \Vert$ as follows:

$$


\begin{aligned}−\frac{𝐱}{2} & =5 \\ −\frac{1}{2}𝐱 & =5 \\ −\frac{1}{2}⋅‖𝐱‖ & =5 \\ \frac{1}{2}⋅‖𝐱‖ & =5 \\ ‖𝐱‖ & =10\end{aligned}


$$

Now, we can evaluate $\Vert 3 \mathbf{x} \Vert \mathbin{:}$

$$


\begin{aligned}‖3𝐱‖ & =3⋅‖𝐱‖ \\ & =3⋅10 \\ & =30\end{aligned}


$$

### Normalizing a Vector

A **unit vector** is a vector whose length is equal to $1.$ If we divide a *non-zero* vector $\mathbf{x}$ by its norm $\Vert \mathbf{x} \Vert,$ we obtain a unit vector $\mathbf{v}=\dfrac{\mathbf{x}}{\Vert\mathbf{x}\Vert},$ since

$$


\Vert \mathbf{v} \Vert =\left\Vert \dfrac{\mathbf{x}}{\Vert \mathbf{x} \Vert} \right\Vert = \dfrac{1}{\Vert \mathbf{x} \Vert}\cdot\Vert \mathbf{x} \Vert = 1.


$$

The process of dividing a vector $\mathbf{x}$ by its norm $\Vert \mathbf{x} \Vert$ is called **normalizing the vector $\mathbf{x}.$** We say that the unit vector $\mathbf{v}=\dfrac{\mathbf{x}}{\Vert\mathbf{x}\Vert}$ is *in the same direction* as $\mathbf{x}.$

### Example: Normalizing a Vector

#### Question

Normalize the vector $[\begin{aligned}−8 \\ 6\end{aligned}]$

#### Explanation

To normalize a vector $\mathbf{x},$ we have to divide the vector by its norm: $\dfrac{\mathbf{x}}{\|\mathbf{x}\|}.$ Therefore, to normalize $\mathbf{x},$ we first calculate $\|\mathbf{x}\|$ as follows:

$$


\begin{aligned}‖𝐱‖ & =\sqrt{𝑥_{21}+𝑥_{22}} \\ & =\sqrt{(−8)^{2}+6^{2}} \\ & =\sqrt{64+36} \\ & =\sqrt{100} \\ & =10\end{aligned}


$$

Then, we divide $\mathbf{x}$ by its length:

$$


\begin{aligned}\frac{𝐱}{‖𝐱‖} & =\frac{𝐱}{10} \\ & =\frac{1}{10}𝐱 \\ & =\frac{1}{10}[\begin{matrix}−8 \\ 6\end{matrix}] \\ & =\begin{matrix}\frac{−8}{10} \\ \frac{6}{10}\end{matrix} \\ & =\begin{matrix}−\frac{4}{5} \\ \frac{3}{5}\end{matrix}\end{aligned}


$$
