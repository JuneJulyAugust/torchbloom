# The Derivative of a Multivariable Function

Source: https://www.mathacademy.com/topics/4169?courseId=54
Topic ID: 4169

## Prerequisites

- [Linearization of Multivariable Functions](./1937-linearization-of-multivariable-functions.md)
- [The Jacobian of a Three-Dimensional Transformation](./2058-the-jacobian-of-a-three-dimensional-transformation.md)

## Lesson

### Introduction

We've spent some time studying so-called **plane transformations** of the form

$$


\mathbf T: \mathbb R^2\to\mathbb R^2.


$$

In this lesson, we'll generalize our understanding of derivatives to transformations (or functions) of the form

$$


\boldsymbol f:\mathbb R^n\to\mathbb R^m.


$$

To motivate the discussion, we start by considering functions of one variable.

Recall that a function $f: \mathbb{R} \to \mathbb{R}$ is **differentiable** at a point $x = a$ if there exists a number $f'(a)$, called the **derivative** of $f$ at $a$, such that

$$


f'(a) = \lim_{x \to a} \frac{f(x) - f(a)}{x - a}.


$$

We can restate this definition by applying basic algebraic properties of limits.

Since the left-hand side, $f'(a)$, is just a constant, we can rewrite the equation as

$$


\lim_{x \to a} f'(a) = \lim_{x \to a} \frac{f(x) - f(a)}{x - a},


$$

using the fact that the limit of a constant is the constant itself.

Bringing all terms to one side, we obtain

$$


\lim_{x \to a} \left( \frac{f(x) - f(a)}{x - a} - f'(a) \right) = 0,


$$

which can be rearranged as

$$


\lim_{x \to a} \left( \frac{f(x) - f(a) - f'(a)(x - a)}{x - a} \right) = 0.


$$

This final expression tells us that the difference between $f(x)$ and its *linear approximation* $f(a) + f'(a)(x - a)$ becomes negligible relative to $x - a$ as $x$ approaches $a$.

In other words, not only does $f(x)$ become close to $f(a) + f'(a)(x-a)$ near $a$, but the error between them shrinks *faster than* the distance $|x - a|$ itself.

Let's see how we can generalize this definition to vector-valued functions.

### Defining the Total Derivative

Suppose that a transformation (or function) $\boldsymbol f:\mathbb R^n\to\mathbb R^m$ is defined by

$$


\begin{aligned}𝑥_{1} \\ 𝑥_{2} \\ ⋮ \\ 𝑥_{𝑛}\end{aligned}


$$

where $f_1,f_2,\ldots,f_m$ are scalar functions of $n$ variables. We say that $\boldsymbol{f}$ is **differentiable** at a point $\mathbf{x} = \mathbf{a} \in \mathbb{R}^n$ if there exists an $m \times n$ matrix $\boldsymbol{f}'(\mathbf{a})$, called the **total derivative** of $\boldsymbol{f}$ at $\mathbf{a}$, such that

$$


\lim_{\mathbf{x} \to \mathbf{a}} \frac{ \boldsymbol{f}(\mathbf{x}) - \boldsymbol{f}(\mathbf{a}) - \boldsymbol{f}'(\mathbf{a})(\mathbf{x} - \mathbf{a}) }{ ||\mathbf{x} - \mathbf{a}|| } = \mathbf{0}.


$$

In other words, near $\mathbf{a}$, the function $\boldsymbol{f}$ is well-approximated by the linear map

$$


\boldsymbol{f}(\mathbf{a}) + \boldsymbol{f}'(\mathbf{a})(\mathbf{x} - \mathbf{a}),


$$

and the error between $\boldsymbol{f}(\mathbf{x})$ and this linear approximation becomes negligible compared to the distance $\|\mathbf{x} - \mathbf{a}\|$ as $\mathbf{x}$ approaches $\mathbf{a}$.

If $\boldsymbol{f}$ is differentiable at $\mathbf{x},$ then the total derivative of $\boldsymbol f$ is given by the matrix

$$


\begin{aligned}\frac{𝜕𝑓_{1}}{𝜕𝑥_{1}} & \frac{𝜕𝑓_{1}}{𝜕𝑥_{2}} & ⋯ & \frac{𝜕𝑓_{1}}{𝜕𝑥_{𝑛}} \\ \frac{𝜕𝑓_{2}}{𝜕𝑥_{1}} & \frac{𝜕𝑓_{2}}{𝜕𝑥_{2}} & ⋯ & \frac{𝜕𝑓_{2}}{𝜕𝑥_{𝑛}} \\ ⋮ & ⋮ & ⋮ & ⋮ \\ \frac{𝜕𝑓_{𝑚}}{𝜕𝑥_{1}} & \frac{𝜕𝑓_{𝑚}}{𝜕𝑥_{2}} & ⋯ & \frac{𝜕𝑓_{𝑚}}{𝜕𝑥_{𝑛}}\end{aligned}


$$

Note the following:

- We sometimes refer to $\boldsymbol f'(\mathbf x)$ simply as **the derivative** of $\boldsymbol f(\mathbf x).$

- For scalar-valued functions of the form $f: \mathbb R^n\to\mathbb R,$ the total derivative is the *transpose* of the gradient vector:

- For vector-valued functions $\boldsymbol f: \mathbb R\to\mathbb R^n$ of a single parameter $t,$ the total derivative at $t=a$ is the usual column vector containing the partial derivatives of the components of $f{:}$

- For functions of the form $\boldsymbol f: \mathbb R^2\to\mathbb R^2,$ the *determinant* of this matrix is the corresponding Jacobian: Similarly, for functions of the form $\boldsymbol f: \mathbb R^3\to\mathbb R^3,$ the *determinant* of this matrix is the corresponding Jacobian:

### Example: Finding the Derivative of a Scalar Function

#### Question

For the transformation $f:\mathbb R^2\to\mathbb R,$ defined as

$$


[\begin{aligned}𝑥 \\ 𝑦\end{aligned}]


$$

calculate $\boldsymbol f'$ at $[\begin{aligned}1 \\ −1\end{aligned}]$

#### Explanation

Suppose a transformation $\boldsymbol{f}:\mathbb R^n\to\mathbb R^m$ is defined by

$$


\begin{aligned}𝑥_{1} \\ 𝑥_{2} \\ ⋮ \\ 𝑥_{𝑛}\end{aligned}


$$

where $f_1,f_2,\ldots,f_m$ are scalar functions with $n$ variables. If $\boldsymbol f$ is differentiable at $\mathbf{x},$ then the total derivative of $\boldsymbol f$ at $\mathbf{x},$ denoted $\boldsymbol{f}'(\mathbf{x}),$ is given by the $m \times n$ matrix

$$


\begin{aligned}\frac{𝜕𝑓_{1}}{𝜕𝑥_{1}} & \frac{𝜕𝑓_{1}}{𝜕𝑥_{2}} & ⋯ & \frac{𝜕𝑓_{1}}{𝜕𝑥_{𝑛}} \\ \frac{𝜕𝑓_{2}}{𝜕𝑥_{1}} & \frac{𝜕𝑓_{2}}{𝜕𝑥_{2}} & ⋯ & \frac{𝜕𝑓_{2}}{𝜕𝑥_{𝑛}} \\ ⋮ & ⋮ & ⋮ & ⋮ \\ \frac{𝜕𝑓_{𝑚}}{𝜕𝑥_{1}} & \frac{𝜕𝑓_{𝑚}}{𝜕𝑥_{2}} & ⋯ & \frac{𝜕𝑓_{𝑚}}{𝜕𝑥_{𝑛}}\end{aligned}


$$

In our case, we have the following:

$$


[\begin{aligned}\frac{𝜕𝑓}{𝜕𝑥} & \frac{𝜕𝑓}{𝜕𝑦}\end{aligned}]


$$

First, we compute the partial derivatives:

$$


\begin{aligned}\frac{𝜕𝑓}{𝜕𝑥} & =\frac{𝜕}{𝜕𝑥}(𝑥^{2}𝑦)=2𝑥𝑦, & \,\frac{𝜕𝑓}{𝜕𝑦} & =\frac{𝜕}{𝜕𝑦}(𝑥^{2}𝑦)=𝑥^{2}\end{aligned}


$$

Therefore, we have

$$


[\begin{aligned}2𝑥𝑦 & 𝑥^{2}\end{aligned}]


$$

and $\boldsymbol{f}'$ at $[\begin{aligned}1 \\ −1\end{aligned}]$ is

$$


[\begin{aligned}2(1)(−1) & 1^{2}\end{aligned}]


$$

### Example: Finding the Derivative of a Vector Function

#### Question

For the transformation $\boldsymbol{f}:\mathbb R^2\to\mathbb R^3,$ defined as

$$


\begin{aligned}𝑥𝑦 \\ 𝑦^{2} \\ 𝑦ln⁡𝑥\end{aligned}


$$

the total derivative $\boldsymbol f'$ is given by

$$


\begin{aligned}𝐴𝐴 & 𝑥 \\ 𝐴𝐴 & 2𝑦 \\ \frac{𝑦}{𝑥} & 𝐴𝐴\end{aligned}


$$

From top to bottom, what are the missing entries?

#### Explanation

Suppose a transformation $\boldsymbol{f}:\mathbb R^n\to\mathbb R^m$ is defined by

$$


\begin{aligned}𝑥_{1} \\ 𝑥_{2} \\ ⋮ \\ 𝑥_{𝑛}\end{aligned}


$$

where $f_1,f_2,\ldots,f_m$ are scalar functions with $n$ variables. If $\boldsymbol{f}$ is differentiable at $\mathbf{x},$ then the total derivative of $\boldsymbol{f}$ at $\mathbf{x},$ denoted $\boldsymbol{f}'(\mathbf{x}),$ is given by the $m \times n$ matrix

$$


\begin{aligned}\frac{𝜕𝑓_{1}}{𝜕𝑥_{1}} & \frac{𝜕𝑓_{1}}{𝜕𝑥_{2}} & ⋯ & \frac{𝜕𝑓_{1}}{𝜕𝑥_{𝑛}} \\ \frac{𝜕𝑓_{2}}{𝜕𝑥_{1}} & \frac{𝜕𝑓_{2}}{𝜕𝑥_{2}} & ⋯ & \frac{𝜕𝑓_{2}}{𝜕𝑥_{𝑛}} \\ ⋮ & ⋮ & ⋮ & ⋮ \\ \frac{𝜕𝑓_{𝑚}}{𝜕𝑥_{1}} & \frac{𝜕𝑓_{𝑚}}{𝜕𝑥_{2}} & ⋯ & \frac{𝜕𝑓_{𝑚}}{𝜕𝑥_{𝑛}}\end{aligned}


$$

In our case, we have the following:

$$


\begin{aligned}\frac{𝜕𝑓_{1}}{𝜕𝑥} & \frac{𝜕𝑓_{1}}{𝜕𝑦} \\ \frac{𝜕𝑓_{2}}{𝜕𝑥} & \frac{𝜕𝑓_{2}}{𝜕𝑦} \\ \frac{𝜕𝑓_{3}}{𝜕𝑥} & \frac{𝜕𝑓_{3}}{𝜕𝑦}\end{aligned}


$$

First, we compute the partial derivatives:

$$


\begin{aligned}\frac{𝜕𝑓_{1}}{𝜕𝑥} & =\frac{𝜕}{𝜕𝑥}(𝑥𝑦)=𝑦,\, & \frac{𝜕𝑓_{1}}{𝜕𝑦} & =\frac{𝜕}{𝜕𝑦}(𝑥𝑦)=𝑥, \\ \frac{𝜕𝑓_{2}}{𝜕𝑥} & =\frac{𝜕}{𝜕𝑥}(𝑦^{2})=0,\, & \frac{𝜕𝑓_{2}}{𝜕𝑦} & =\frac{𝜕}{𝜕𝑦}(𝑦^{2})=2𝑦, \\ \frac{𝜕𝑓_{3}}{𝜕𝑥} & =\frac{𝜕}{𝜕𝑥}(𝑦ln⁡𝑥)=\frac{𝑦}{𝑥},\, & \frac{𝜕𝑓_{3}}{𝜕𝑦} & =\frac{𝜕}{𝜕𝑦}(𝑦ln⁡𝑥)=ln⁡𝑥\end{aligned}


$$

Therefore, we have

$$


\begin{aligned}𝑦 & 𝑥 \\ 0 & 2𝑦 \\ \frac{𝑦}{𝑥} & ln⁡𝑥\end{aligned}


$$

Thus, the missing entries are $y,\:$ $0,\:$ and $\ln{x}.$

### The Tangent Plane to the Graph of a Scalar Function

The equation of the tangent plane to a surface $z=f(x,y)$ at the point $(x_0,y_0,z_0),$ where $z_0=f(x_0,y_0),$ is given by

$$


z - z_0 = (x-x_0) \cdot \dfrac{\partial f}{\partial x}(x_0,y_0) + (y-y_0) \cdot \dfrac{\partial f}{\partial y}(x_0,y_0).


$$

Let's express this equation in terms of the total derivative.

Writing our multivariable function $f:\mathbb R^2 \to \mathbb R$ as $f\left(\mathbf x \right),$ where $[\begin{aligned}𝑥 \\ 𝑦\end{aligned}]$ the total derivative of $f$ is given by

$$


[\begin{aligned}\frac{𝜕𝑓}{𝜕𝑥} & \frac{𝜕𝑓}{𝜕𝑦}\end{aligned}]


$$

Let $[\begin{aligned}𝑥_{0} \\ 𝑦_{0}\end{aligned}]$ Then, we can re-write the equation of the tangent plane as a matrix equation as follows:

$$


\begin{aligned}𝑧−𝑧_{0} & =(𝑥−𝑥_{0})⋅\frac{𝜕𝑓}{𝜕𝑥}(𝑥_{0},𝑦_{0})+(𝑦−𝑦_{0})⋅\frac{𝜕𝑓}{𝜕𝑦}(𝑥_{0},𝑦_{0}) \\ 𝑧−𝑧_{0} & =[\begin{matrix}\frac{𝜕𝑓}{𝜕𝑥}(𝑥_{0},𝑦_{0}) & \frac{𝜕𝑓}{𝜕𝑦}(𝑥_{0},𝑦_{0})\end{matrix}]⋅[\begin{matrix}𝑥−𝑥_{0} \\ 𝑦−𝑦_{0}\end{matrix}] \\ 𝑧−𝑓(𝑥_{0},𝑦_{0}) & =[\begin{matrix}\frac{𝜕𝑓}{𝜕𝑥}(𝑥_{0},𝑦_{0}) & \frac{𝜕𝑓}{𝜕𝑦}(𝑥_{0},𝑦_{0})\end{matrix}]⋅([\begin{matrix}𝑥 \\ 𝑦\end{matrix}]−[\begin{matrix}𝑥_{0} \\ 𝑦_{0}\end{matrix}]) \\ 𝑧−𝑓(𝐚) & =[\begin{matrix}\frac{𝜕𝑓}{𝜕𝑥}(𝐚) & \frac{𝜕𝑓}{𝜕𝑦}(𝐚)\end{matrix}]⋅(𝐱−𝐚) \\ 𝑧−𝑓(𝐚) & =𝒇^{′}(𝐚)(𝐱−𝐚)\end{aligned}


$$

Therefore, the tangent plane to $f:\mathbb R^2\to\mathbb R$ at $\mathbf x = \mathbf{a},$ in matrix form, is given by

$$


z - f(\mathbf a) = \boldsymbol{f}'(\mathbf a)(\mathbf x - \mathbf a).


$$

### Example: Finding the Tangent Plane to the Graph of a Scalar Function in Matrix Form

#### Question

Consider the function $f:\mathbb R^2\to\mathbb R,$ defined as

$$


[\begin{aligned}𝑥 \\ 𝑦\end{aligned}]


$$

If the tangent to $f$ at $[\begin{aligned}1 \\ 2\end{aligned}]$ is given by

$$


[\begin{aligned}∗ & ∗\end{aligned}]


$$

find the missing values.

#### Explanation

Suppose a transformation $\boldsymbol{f}:\mathbb R^n\to\mathbb R^m$ is defined by

$$


\begin{aligned}𝑥_{1} \\ 𝑥_{2} \\ ⋮ \\ 𝑥_{𝑛}\end{aligned}


$$

where $f_1,f_2,\ldots,f_m$ are scalar functions with $n$ variables. If $\boldsymbol{f}$ is differentiable at $\mathbf{x},$ then the total derivative of $\boldsymbol{f}$ at $\mathbf{x},$ denoted $\boldsymbol{f}'(\mathbf{x}),$ is given by the $m \times n$ matrix

$$


\begin{aligned}\frac{𝜕𝑓_{1}}{𝜕𝑥_{1}} & \frac{𝜕𝑓_{1}}{𝜕𝑥_{2}} & ⋯ & \frac{𝜕𝑓_{1}}{𝜕𝑥_{𝑛}} \\ \frac{𝜕𝑓_{2}}{𝜕𝑥_{1}} & \frac{𝜕𝑓_{2}}{𝜕𝑥_{2}} & ⋯ & \frac{𝜕𝑓_{2}}{𝜕𝑥_{𝑛}} \\ ⋮ & ⋮ & ⋮ & ⋮ \\ \frac{𝜕𝑓_{𝑚}}{𝜕𝑥_{1}} & \frac{𝜕𝑓_{𝑚}}{𝜕𝑥_{2}} & ⋯ & \frac{𝜕𝑓_{𝑚}}{𝜕𝑥_{𝑛}}\end{aligned}


$$

In our case, we have the following:

$$


[\begin{aligned}\frac{𝜕𝑓}{𝜕𝑥} & \frac{𝜕𝑓}{𝜕𝑦}\end{aligned}]


$$

First, we compute the partial derivatives:

$$


\begin{aligned}\frac{𝜕𝑓}{𝜕𝑥} & =\frac{𝜕}{𝜕𝑥}(𝑥^{3}+𝑒^{𝑦})=3𝑥^{2},\, & \frac{𝜕𝑓}{𝜕𝑦} & =\frac{𝜕}{𝜕𝑦}(𝑥^{3}+𝑒^{𝑦})=𝑒^{𝑦}\end{aligned}


$$

Therefore, we have

$$


[\begin{aligned}3𝑥^{2} & 𝑒^{𝑦}\end{aligned}]


$$

Evaluating $f$ and its derivative at $[\begin{aligned}1 \\ 2\end{aligned}]$ we have

$$


[\begin{aligned}3 & 𝑒^{2}\end{aligned}]


$$

The tangent to $f$ at $\mathbf x = \mathbf a$ is given by

$$


z - f(\mathbf a) = \boldsymbol{f}'(\mathbf a)(\mathbf x - \mathbf a).


$$

Substituting $f(\mathbf a),$ $\boldsymbol{f}'(\mathbf a),$ and $\mathbf a$ in the equation above, we obtain

$$


[\begin{aligned}3 & 𝑒^{2}\end{aligned}]


$$

### Affine Approximations of Vector Functions

If $f:\mathbb R \to \mathbb R$ is differentiable at $x=a,$ then for points close to $x=a,$ we have the linear approximation

$$


f(x) \approx f(a) + f'(a)(x-a).


$$

We have a similar result for transformations of the form $\boldsymbol{f}:\mathbb R^n\to\mathbb R^m.$

If $\boldsymbol f:\mathbb R^n \to \mathbb R^m$ is differentiable at $\mathbf x=\mathbf a,$ then for points close to $\mathbf x=\mathbf a,$ we have the linear approximation

$$


\boldsymbol{f}(\mathbf x) \approx \boldsymbol{f}(\mathbf a) + \boldsymbol{f}'(\mathbf a)(\mathbf x - \mathbf a).


$$

Notice that this approximation for $\boldsymbol f$ is affine. Thus, if a function is differentiable at a point $\mathbf x = \mathbf a,$ it is **locally affine** in a neighborhood of $\mathbf x = \mathbf a.$

Let's see some examples.

### Example: Finding an Affine Approximation of a Vector Function

#### Question

Consider the transformation $\boldsymbol{f}:\mathbb R^2\to\mathbb R^2,$ defined as

$$


[\begin{aligned}𝑥_{2}sin⁡𝑥_{1} \\ sin⁡𝑥_{2}\end{aligned}]


$$

If the linear approximation of $\boldsymbol f$ at $[\begin{aligned}𝜋 \\ 0\end{aligned}]$ is given by

$$


[\begin{aligned}∗ \\ 0\end{aligned}]


$$

what are the missing values?

#### Explanation

Suppose a transformation $\boldsymbol{f}:\mathbb R^n\to\mathbb R^m$ is defined by

$$


\begin{aligned}𝑥_{1} \\ 𝑥_{2} \\ ⋮ \\ 𝑥_{𝑛}\end{aligned}


$$

where $f_1,f_2,\ldots,f_m$ are scalar functions with $n$ variables. If $\boldsymbol{f}$ is differentiable at $\mathbf{x},$ then the total derivative of $\boldsymbol{f}$ at $\mathbf{x},$ denoted $\boldsymbol{f}'(\mathbf{x}),$ is given by the $m \times n$ matrix

$$


\begin{aligned}\frac{𝜕𝑓_{1}}{𝜕𝑥_{1}} & \frac{𝜕𝑓_{1}}{𝜕𝑥_{2}} & ⋯ & \frac{𝜕𝑓_{1}}{𝜕𝑥_{𝑛}} \\ \frac{𝜕𝑓_{2}}{𝜕𝑥_{1}} & \frac{𝜕𝑓_{2}}{𝜕𝑥_{2}} & ⋯ & \frac{𝜕𝑓_{2}}{𝜕𝑥_{𝑛}} \\ ⋮ & ⋮ & ⋮ & ⋮ \\ \frac{𝜕𝑓_{𝑚}}{𝜕𝑥_{1}} & \frac{𝜕𝑓_{𝑚}}{𝜕𝑥_{2}} & ⋯ & \frac{𝜕𝑓_{𝑚}}{𝜕𝑥_{𝑛}}\end{aligned}


$$

In our case, we have the following:

$$


\begin{aligned}\frac{𝜕𝑓_{1}}{𝜕𝑥_{1}} & \frac{𝜕𝑓_{1}}{𝜕𝑥_{2}} \\ \frac{𝜕𝑓_{2}}{𝜕𝑥_{1}} & \frac{𝜕𝑓_{2}}{𝜕𝑥_{2}}\end{aligned}


$$

First, we compute the partial derivatives:

$$


\begin{aligned}\frac{𝜕𝑓_{1}}{𝜕𝑥_{1}} & =\frac{𝜕}{𝜕𝑥_{1}}(𝑥_{2}sin⁡𝑥_{1})=𝑥_{2}cos⁡𝑥_{1},\, & \frac{𝜕𝑓_{1}}{𝜕𝑥_{2}} & =\frac{𝜕}{𝜕𝑥_{2}}(𝑥_{2}sin⁡𝑥_{1})=sin⁡𝑥_{1} \\ \frac{𝜕𝑓_{2}}{𝜕𝑥_{1}} & =\frac{𝜕}{𝜕𝑥_{1}}(sin⁡𝑥_{2})=0,\, & \frac{𝜕𝑓_{2}}{𝜕𝑥_{2}} & =\frac{𝜕}{𝜕𝑥_{2}}(sin⁡𝑥_{2})=cos⁡𝑥_{2}\end{aligned}


$$

Therefore, we have

$$


[\begin{aligned}𝑥_{2}cos⁡𝑥_{1} & sin⁡𝑥_{1} \\ 0 & cos⁡𝑥_{2}\end{aligned}]


$$

Evaluating $\boldsymbol{f}$ and its derivative at $[\begin{aligned}𝜋 \\ 0\end{aligned}]$ we have

$$


[\begin{aligned}0 \\ 0\end{aligned}]


$$

The linear approximation of $\boldsymbol{f}$ at $\mathbf x = \mathbf a$ is given by

$$


\boldsymbol{f}\left(\mathbf x \right) \approx \boldsymbol{f}(\mathbf a) + \boldsymbol{f}'(\mathbf a)(\mathbf x - \mathbf a).


$$

Substituting $\boldsymbol{f}(\mathbf a),$ $\boldsymbol{f}'(\mathbf a),$ and $\mathbf a$ in the equation above, we obtain

$$


[\begin{aligned}0 \\ 0\end{aligned}]


$$
