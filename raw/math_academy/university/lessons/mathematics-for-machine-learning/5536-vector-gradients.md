# Vector Gradients

Source: https://www.mathacademy.com/topics/5536?courseId=145
Topic ID: 5536

## Prerequisites

- [Euclidean, Manhattan, and Minkowski Distance](./2915-euclidean-manhattan-and-minkowski-distance.md)
- [Gradients With Respect to a Variable Subset](./5527-gradients-with-respect-to-a-variable-subset.md)
- [The Chain Rule for Total Derivatives](./5868-the-chain-rule-for-total-derivatives.md)

## Lesson

### Introduction

In this lesson, we'll extend our knowledge of gradients of scalar-valued functions.

Recall that, for a function $f: \mathbb{R}^n \to \mathbb{R}$ that maps a vector $\mathbf{x} \in \mathbb{R}^n$ to a scalar value $f(\mathbf{x})$, the *gradient* of $f$ with respect to $\mathbf{x}$ is defined as the column vector of partial derivatives:

$$


\begin{aligned}\frac{𝜕𝑓}{𝜕𝑥_{1}} \\ \frac{𝜕𝑓}{𝜕𝑥_{2}} \\ ⋮ \\ \frac{𝜕𝑓}{𝜕𝑥_{𝑛}}\end{aligned}


$$

**Note:** Some resources use $\dfrac{\partial f}{\partial \mathbf x}$ to denote the gradient. We shall avoid this notation.

Recall that the *total derivative* of a scalar function $f: \mathbb{R}^n \to \mathbb{R}$ with respect to a vector $\mathbf{x} \in \mathbb{R}^n$ is the row vector

$$


[\begin{aligned}\frac{𝜕𝑓}{𝜕𝑥_{1}} & \frac{𝜕𝑓}{𝜕𝑥_{2}} & ⋯ & \frac{𝜕𝑓}{𝜕𝑥_{𝑛}}\end{aligned}]


$$

Hence, the gradient is simply the transpose of the total derivative:

$$


\nabla f(\mathbf{x}) = \left( \frac{\text{d} f}{\text{d} \mathbf{x}} \right)^T


$$

We'll now discuss some important results related to gradients widely used in machine learning applications.

Let's see an example.

### Gradient of a Linear Form With Respect to a Vector

Let’s derive a general rule for the gradient of a linear function.

Suppose $\mathbf{x} \in \mathbb{R}^n,$ and the scalar function $f$ is given by

$$


f(\mathbf{x}) = \mathbf{b}^T \mathbf{x},


$$

where $\mathbf{b} \in \mathbb{R}^n$ is a fixed vector.

We wish to find an expression for the gradient of $f.$

$$


\nabla_{\mathbf{x}} f = \nabla_{\mathbf{x}} (\mathbf{b}^T \mathbf{x})


$$

To do this, let's write our vectors $\mathbf b$ and $\mathbf x$ explicitly:

$$


\begin{aligned}𝑏_{1} \\ 𝑏_{2} \\ ⋮ \\ 𝑏_{𝑛}\end{aligned}


$$

Then, $\mathbf b^T \mathbf x$ is the scalar function

$$


\begin{aligned}𝐛^{𝑇}𝐱 & =[\begin{matrix}𝑏_{1} & 𝑏_{2} & … & 𝑏_{𝑛}\end{matrix}]\begin{matrix}𝑥_{1} \\ 𝑥_{2} \\ ⋮ \\ 𝑥_{𝑛}\end{matrix}\end{aligned}


$$

which simplifies as

$$


\mathbf b^T \mathbf x =b_1x_1+ b_2x_2 + \cdots + b_nx_n.


$$

The partial derivative of $\mathbf b^T \mathbf x$ with respect to $x_i$ is $b_i,$ since all the other terms will vanish.

$$


\dfrac{\partial}{\partial x_i}\left(\mathbf b^T\mathbf x\right) = \dfrac{\partial}{\partial x_i}\left(b_1x_1+ b_2x_2 + \cdots + b_i x_i + \cdots + b_nx_n\right) = b_i


$$

Since this is true for all $1\leq i\leq n,$ we have

$$


\nabla_{\mathbf x} \left(\mathbf b^T \mathbf x\right) = \mathbf b


$$

as required.

This is the multivariable analog of the familiar rule from single-variable calculus:

$$


\frac{\textrm d}{\textrm dx}(a x) = a


$$

### Example: Computing Gradients of Linear Forms

#### Question

Compute the gradient of the function $f: \mathbb{R}^4 \rightarrow \mathbb{R}$ defined by

$$


[\begin{aligned}0 & 1 & 0 & −1\end{aligned}]


$$

with respect to $\mathbf{x}$ at $\begin{aligned}1 \\ 0 \\ 1 \\ 0\end{aligned}$

#### Explanation

Writing $\begin{aligned}0 \\ 1 \\ 0 \\ −1\end{aligned}$, we have

$$


f(\mathbf{x})= \mathbf{b}^T\mathbf{x}.


$$

The gradient of a function $f(x) = \mathbf{b}^T\mathbf{x}$ with respect to $\mathbf{x} \in \mathbb{R}^n$ is

$$


\nabla_{\mathbf{x}} f(\mathbf{x}) = \mathbf{b}.


$$

Therefore, we get

$$


\begin{aligned}0 \\ 1 \\ 0 \\ −1\end{aligned}


$$

### The Gradient of a Squared Norm

We have the following result:

$$


\nabla_{\mathbf w} \left(\mathbf w^T \mathbf w\right) = 2\mathbf w


$$

This result is analogous to the following result from single-variable calculus:

$$


\dfrac{\textrm d}{\textrm d w}(w^2) = 2w


$$

To see why this is true, let $\mathbf w \in\mathbb R^n$ be given by

$$


\begin{aligned}𝑤_{1} \\ 𝑤_{2} \\ ⋮ \\ 𝑤_{𝑛}\end{aligned}


$$

Then, $\mathbf w^T \mathbf w$ is the *scalar* function

$$


\begin{aligned}𝐰^{𝑇}𝐰 & =[\begin{matrix}𝑤_{1} & 𝑤_{2} & … & 𝑤_{𝑛}\end{matrix}]\begin{matrix}𝑤_{1} \\ 𝑤_{2} \\ ⋮ \\ 𝑤_{𝑛}\end{matrix}\end{aligned}


$$

which can be written as

$$


\mathbf w^T \mathbf w =w_1^2+ w_2^2 + \cdots + w_n^2.


$$

The partial derivative of $\mathbf w^T \mathbf w$ with respect to $w_i$ is $2w_i,$ since all the other terms will vanish. Since this is true for all $1\leq i\leq n,$ we have

$$


\nabla_{\mathbf w} \left(\mathbf w^T \mathbf w\right) = 2\mathbf w


$$

as required.

Finally, note that since

$$


\mathbf w^T \mathbf w = ||\mathbf w ||^2


$$

we have the following equivalent result:

$$


\nabla_{\mathbf w}(||\mathbf w ||^2) = 2\mathbf w


$$

### Example: Computing Gradients Including Squared Norms

#### Question

Given the function

$$


f(\mathbf{x}, \mathbf{w}) = -7\mathbf{w}^T\mathbf{x} + 3\|\mathbf{w}\|^2 - 2


$$

that maps two vectors to a scalar, find $\nabla_{\mathbf w} f.$

#### Explanation

Using the results

$$


\nabla_{\mathbf w}(\mathbf{w}^T\mathbf{x}) = \mathbf{x}, \qquad \nabla_{\mathbf w} (\mathbf{w}^T\mathbf{w}) = 2\mathbf{w},


$$

we have

$$


\begin{aligned}∇_{𝐰}𝑓 & =∇_{𝐰}(−7𝐰^{𝑇}𝐱+3‖𝐰‖^{2}−2) \\ & =−7⋅∇_{𝐰}(𝐰^{𝑇}𝐱)+3⋅∇_{𝐰}(‖𝐰‖^{2})−∇_{𝐰}(2) \\ & =−7⋅∇_{𝐰}(𝐰^{𝑇}𝐱)+3⋅∇_{𝐰}(𝐰^{𝑇}𝐰)−∇_{𝐰}(2) \\ & =−7⋅𝐱+3⋅2𝐰−𝟎 \\ & =−7𝐱+6𝐰.\end{aligned}


$$

### The Gradient of the L1 Norm

Consider the $\text{L}_1$ (Manhattan) norm of a vector $\mathbf{x} \in \mathbb{R}^n$, defined as

$$


\|\mathbf{x}\|_1 = \sum_{i=1}^n |x_i|.


$$

We want to compute the gradient of this function with respect to $\mathbf{x}$. To do that, let’s focus on finding the partial derivative with respect to a single component $x_k{:}$

$$


\begin{aligned}\frac{𝜕‖𝐱‖_{1}}{𝜕𝑥_{𝑘}} & =\frac{𝜕}{𝜕𝑥_{𝑘}}\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}|𝑥_{𝑖}| \\ & =\frac{𝜕}{𝜕𝑥_{𝑘}}(|𝑥_{1}|+|𝑥_{2}|+⋯+|𝑥_{𝑘}|+⋯+|𝑥_{𝑛}|) \\ & =\frac{𝜕|𝑥_{1}|}{𝜕𝑥_{𝑘}}+\frac{𝜕|𝑥_{2}|}{𝜕𝑥_{𝑘}}+⋯+\frac{𝜕|𝑥_{𝑘}|}{𝜕𝑥_{𝑘}}+⋯+\frac{𝜕|𝑥_{𝑛}|}{𝜕𝑥_{𝑘}} \\ & =\frac{𝜕|𝑥_{𝑘}|}{𝜕𝑥_{𝑘}} \\ & =sign(𝑥_{𝑘}),\end{aligned}


$$

where $\text{sign}(x_k)$ is defined as

$$


\begin{aligned}−1, & \,𝑥_{𝑘}>0, \\ −1, & \,𝑥_{𝑘}<0.\end{aligned}


$$

So, the full gradient of the $\text{L}_1$ norm is simply

$$


\nabla_{\mathbf{x}} \|\mathbf{x}\|_1 = \text{sign}(\mathbf{x}),


$$

which is a vector whose $k$th component is $\text{sign}(x_k)$.

The gradient of $\|\mathbf x\|_1$ is not defined at points where any component of $\mathbf x$ equals zero. This is because the absolute value function has a sharp corner at zero and is therefore not differentiable there. Various methods are available to overcome this difficulty when the derivative of the $\textrm L1$ norm is used in practice, and we'll discuss these in future lessons.

### Chain Rule to Vector Gradients

In many machine learning models, a scalar function depends on a vector that itself depends on another vector.

Suppose $f:\mathbb{R}^m \to \mathbb{R}$ and $\mathbf g:\mathbb{R}^n \to \mathbb{R}^m,$ and define

$$


h(\mathbf x)=f(\mathbf g(\mathbf x)).


$$

Then the **chain rule for gradients** states:

$$


\nabla_{\mathbf x} h(\mathbf x) = J_{\mathbf g}(\mathbf x)^T \,\nabla_{\mathbf u} f(\mathbf u)\Big|_{\mathbf u=\mathbf g(\mathbf x)},


$$

where $J_{\mathbf g}(\mathbf x)$ is the Jacobian of $\mathbf g.$

In other words, we have

$$


\bigg(\substack{\Large \text{Gradient of} \\[3pt] \Large\text{composition}}\bigg) = \bigg(\substack{\Large \text{Jacobian of} \\[3pt] \Large\text{the inner function}}\bigg)^T \cdot \:\: \bigg(\substack{\Large \text{Gradient of} \\[3pt] \Large\text{the outer function}}\bigg).


$$

Let’s see this in action.

### Example: Computing Gradients of Functions Containing L1 Norms

#### Question

Given the function

$$


f(\mathbf{x}, \mathbf{w}) = -3\left(\|\mathbf{w}\|_1\right)^3 - 5\mathbf x^T\mathbf w


$$

that maps a vector to a scalar, find $\nabla_{\mathbf w}f.$ You may assume that $\mathbf w$ has no zero components.

#### Explanation

Using the results

$$


\nabla_{\mathbf w} (\|\mathbf{w}\|_1) = \text{sign}(\mathbf{w}), \qquad \nabla_{\mathbf w}\left(\mathbf x^T\mathbf w\right) = \mathbf x,


$$

we have

$$


\begin{aligned}∇_{𝐰}𝑓 & =∇_{𝐰}(−3(‖𝐰‖_{1})^{3}−5𝐱^{𝑇}𝐰) \\ & =∇_{𝐰}(−3(‖𝐰‖_{1})^{3})−∇_{𝐰}(5𝐱^{𝑇}𝐰) \\ & =−3⋅∇_{𝐰}((‖𝐰‖_{1})^{3})−5⋅∇_{𝐰}(𝐱^{𝑇}𝐰) \\ & =−3⋅3(‖𝐰‖_{1})^{2}⋅∇_{𝐰}(‖𝐰‖_{1})−5⋅𝐱 \\ & =−3⋅3(‖𝐰‖_{1})^{2}⋅sign(𝐰)−5⋅𝐱 \\ & =−9(‖𝐰‖_{1})^{2}⋅sign(𝐰)−5𝐱.\end{aligned}


$$
