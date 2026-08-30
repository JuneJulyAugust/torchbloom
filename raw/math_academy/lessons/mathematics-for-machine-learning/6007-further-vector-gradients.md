# Further Vector Gradients

Source: https://www.mathacademy.com/topics/6007?courseId=145
Topic ID: 6007

## Prerequisites

- [Quadratic Forms](./3123-quadratic-forms.md)
- [Vector Gradients](./5536-vector-gradients.md)

## Lesson

### Introduction

In this lesson, we'll extend our knowledge of gradients of scalar functions to include quadratic functions, quadratic forms, and the chain rule.

Consider the (scalar) **quadratic function**

$$


f(\mathbf{x}) = \mathbf{x}^T \mathbf{A} \mathbf{x}


$$

where $\mathbf{A} \in \mathbb{R}^{n \times n}$ is a matrix, and $\mathbf x\in\mathbb R^n$ is a column vector. We wish to calculate the gradient of this function:

$$


\nabla_{\mathbf x} f = \nabla_{\mathbf x} \left(\mathbf{x}^T \mathbf{A} \mathbf{x}\right)


$$

We start by showing that $f$ can be written in the expanded form

$$


f(\mathbf{x}) = \sum_{i=1}^n \sum_{j=1}^n a_{ij} x_i x_j.


$$

To understand why this is the same as $\mathbf x^T \mathbf{A} \mathbf x,$ let's first write

$$


\begin{aligned}𝑥_{1} \\ 𝑥_{2} \\ ⋮ \\ 𝑥_{𝑛}\end{aligned}


$$

Now, we compute $\mathbf{x}^T \mathbf{A} \mathbf{x}$ by working step by step.

First, we compute the product $\mathbf{A} \mathbf{x}$, which gives us an $n\times 1$ column vector:

$$


\begin{aligned}𝐀𝐱 & =\begin{aligned}𝑎_{11} & 𝑎_{12} & ⋯ & 𝑎_{1𝑛} \\ 𝑎_{21} & 𝑎_{22} & ⋯ & 𝑎_{2𝑛} \\ ⋮ & ⋮ & ⋱ & ⋮ \\ 𝑎_{𝑛1} & 𝑎_{𝑛2} & ⋯ & 𝑎_{𝑛𝑛}\end{aligned}⋅\begin{aligned}𝑥_{1} \\ 𝑥_{2} \\ ⋮ \\ 𝑥_{𝑛}\end{aligned} \\ & =\begin{aligned}𝑎_{11}𝑥_{1}+𝑎_{12}𝑥_{2}+⋯+𝑎_{1𝑛}𝑥_{𝑛} \\ 𝑎_{21}𝑥_{1}+𝑎_{22}𝑥_{2}+⋯+𝑎_{2𝑛}𝑥_{𝑛} \\ ⋮ \\ 𝑎_{𝑛1}𝑥_{1}+𝑎_{𝑛2}𝑥_{2}+⋯+𝑎_{𝑛𝑛}𝑥_{𝑛}\end{aligned} \\ & =\begin{aligned}\underset{\underset{𝑗=1}{∑}}{\overset{}{𝑛}}𝑎_{1𝑗}𝑥_{𝑗} \\ \underset{\underset{𝑗=1}{∑}}{\overset{}{𝑛}}𝑎_{2𝑗}𝑥_{𝑗} \\ ⋮ \\ \underset{\underset{𝑗=1}{∑}}{\overset{}{𝑛}}𝑎_{𝑛𝑗}𝑥_{𝑗}\end{aligned}.\end{aligned}


$$

Next, we multiply $\mathbf{x}^T$ by this result:

$$


[\begin{aligned}𝑥_{1} & 𝑥_{2} & ⋯ & 𝑥_{𝑛}\end{aligned}]


$$

Each term of this product looks like $x_i \cdot \displaystyle\sum_{j=1}^n a_{ij} x_j$, so the full expression becomes

$$


\mathbf{x}^T \mathbf{A} \mathbf{x} = \sum_{i=1}^n x_i \left( \sum_{j=1}^n a_{ij} x_j \right) = \sum_{i=1}^n \sum_{j=1}^n a_{ij} x_i x_j.


$$

So, we've shown that

$$


\boxed{\mathbf{x}^T \mathbf{A} \mathbf{x} = \sum_{i=1}^n \sum_{j=1}^n a_{ij} x_i x_j.}


$$

Let's now discuss how this helps us to compute the gradient of $f.$

### The Gradient of a Quadratic Function

We have the quadratic function

$$


f(\mathbf{x}) = \mathbf{x}^T A \mathbf{x}


$$

where $A \in \mathbb{R}^{n \times n}$ is a matrix, and $\mathbf x\in\mathbb R^n$ is a column vector. As we've seen, $f$ can be written in the expanded form

$$


f(\mathbf{x}) = \sum_{i=1}^n \sum_{j=1}^n A_{ij} x_i x_j.


$$

We'll use this form to compute the gradient of $f.$

To compute the gradient $\nabla_{\mathbf{x}} f$, we'll differentiate this expanded form with respect to $x_k.$ First, we express our expanded function as

$$


f(\mathbf x) = \sum_{i \neq k} \sum_{j \neq k} A_{ij} x_i x_j + \sum_{i \neq k} A_{ik} x_i x_k + \sum_{j \neq k} A_{kj} x_k x_j + A_{kk} x_k^2.


$$

The idea here is to break up the double summation by isolating all the terms that involve the variable $x_k$.

Notice that

- the first summation is *independent* of $x_k,$

- the second and third summations are *linear* in $x_k,$ and

- the final term is *quadratic* in $x_k.$

We can now compute our derivative term by term in a structured way. Differentiating with respect to $x_k,$ we get

$$


\begin{aligned}\frac{𝜕𝑓}{𝜕𝑥_{𝑘}} & =\frac{𝜕}{𝜕𝑥_{𝑘}}[\underset{𝑖≠𝑘}{∑}\underset{𝑗≠𝑘}{∑}𝐴_{𝑖𝑗}𝑥_{𝑖}𝑥_{𝑗}+\underset{𝑖≠𝑘}{∑}𝐴_{𝑖𝑘}𝑥_{𝑖}𝑥_{𝑘}+\underset{𝑗≠𝑘}{∑}𝐴_{𝑘𝑗}𝑥_{𝑘}𝑥_{𝑗}+𝐴_{𝑘𝑘}𝑥_{2𝑘}^{}] \\ & =\underset{𝑖≠𝑘}{∑}𝐴_{𝑖𝑘}𝑥_{𝑖}+\underset{𝑗≠𝑘}{∑}𝐴_{𝑘𝑗}𝑥_{𝑗}+2𝐴_{𝑘𝑘}𝑥_{𝑘} \\ & =(\underset{𝑖≠𝑘}{∑}𝐴_{𝑖𝑘}𝑥_{𝑖})+𝐴_{𝑘𝑘}𝑥_{𝑘}+(\underset{𝑗≠𝑘}{∑}𝐴_{𝑘𝑗}𝑥_{𝑗})+𝐴_{𝑘𝑘}𝑥_{𝑘} \\ & =\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}𝐴_{𝑖𝑘}𝑥_{𝑖}+\underset{\underset{𝑗=1}{∑}}{\overset{}{𝑛}}𝐴_{𝑘𝑗}𝑥_{𝑗} \\ & =(𝐴^{𝑇}𝐱)_{𝑘}+(𝐴𝐱)_{𝑘}.\end{aligned}


$$

Since this is true for all $1\leq k \leq n$, we get the result

$$


\nabla_{\mathbf{x}} (\mathbf{x}^T A \mathbf{x}) = A^T \mathbf{x} + A \mathbf{x} = (A^T + A)\mathbf x.


$$

From here, we have the following special cases:

- If $A$ is symmetric, then $A^T = A,$ $f(\mathbf x)$ is a quadratic form, and our result simplifies to

- Suppose that $A = I_n$ is the $n\times n$ identity matrix. Then, our result for symmetric matrices simplifies to which is a result we saw in a previous lesson.

### Example: Computing Gradient of a Quadratic Form

#### Question

Compute the gradient of the function $f: \mathbb{R}^3 \rightarrow \mathbb{R}$ defined by

$$


\begin{aligned}0 & 0 & −1 \\ 0 & −1 & 0 \\ −1 & 0 & 5\end{aligned}


$$

with respect to $\mathbf{x}$ at $\begin{aligned}1 \\ 1 \\ −1\end{aligned}$

#### Explanation

Writing $\begin{aligned}0 & 0 & −1 \\ 0 & −1 & 0 \\ −1 & 0 & 5\end{aligned}$, we have

$$


f(\mathbf{x})= \mathbf{x}^TA\mathbf{x}.


$$

For a symmetric matrix $A$, the gradient of the function $f(\mathbf{x}) = \mathbf{x}^TA\mathbf{x}$ with respect to $\mathbf{x} \in \mathbb{R}^n$ is

$$


\nabla_{\mathbf{x}} f(\mathbf{x}) = 2A\mathbf{x}.


$$

Therefore, since $A$ is symmetric, we get

$$


\begin{aligned}0 & 0 & −1 \\ 0 & −1 & 0 \\ −1 & 0 & 5\end{aligned}


$$

### Example: Computing Gradient of a Quadratic Function

#### Question

Compute the gradient of the function $f: \mathbb{R}^2 \rightarrow \mathbb{R}$ defined by

$$


[\begin{aligned}1 & −1 \\ 1 & 1\end{aligned}]


$$

with respect to $\mathbf{x}$ at $[\begin{aligned}−1 & −1\end{aligned}]$

#### Explanation

Defining the matrix $A$ as

$$


[\begin{aligned}1 & −1 \\ 1 & 1\end{aligned}]


$$

we have $f(\mathbf{x}) = \mathbf{x}^T A \mathbf{x}.$

Since $A$ is not symmetric, we use the more general formula for the gradient of a quadratic function:

$$


\nabla_{\mathbf{x}} f(\mathbf{x}) = (A^T + A)\mathbf{x}


$$

First, we compute

$$


[\begin{aligned}1 & 1 \\ −1 & 1\end{aligned}]


$$

which gives

$$


\begin{aligned}𝐴^{𝑇}+𝐴 & =[\begin{aligned}1 & 1 \\ −1 & 1\end{aligned}]+[\begin{aligned}1 & −1 \\ 1 & 1\end{aligned}] \\ & =[\begin{aligned}2 & 0 \\ 0 & 2\end{aligned}].\end{aligned}


$$

Now, compute the gradient at $[\begin{aligned}−1 \\ −1\end{aligned}]$

$$


\begin{aligned}∇_{𝐱}𝑓(𝐱) & =(𝐴^{𝑇}+𝐴)𝐱 \\ & =[\begin{aligned}2 & 0 \\ 0 & 2\end{aligned}][\begin{aligned}−1 \\ −1\end{aligned}] \\ & =[\begin{aligned}−2+0 \\ 0−2\end{aligned}] \\ & =[\begin{aligned}−2 \\ −2\end{aligned}]\end{aligned}


$$

### Computing Gradients With the Chain Rule

Now, let $\mathbf{y}: \mathbb{R}^n \to \mathbb{R}^q$ and $f: \mathbb{R}^q \to \mathbb{R}$. Suppose we want to compute the gradient

$$


\nabla_{\mathbf{x}} f(\mathbf{y}(\mathbf{x})).


$$

To do this, we need to apply the chain rule. The chain rule for total derivatives tells us that

$$


\underbrace{\frac{\textrm{d} f}{\textrm{d} \mathbf{x}}}_{1 \times n} = \underbrace{\frac{\textrm{d} f}{\textrm{d} \mathbf{y}}}_{1 \times q} \cdot \underbrace{\frac{\textrm{d} \mathbf{y}}{\textrm{d} \mathbf{x}}}_{q \times n}.


$$

Now, recall that the gradient of a scalar function is the transpose of the total derivative:

$$


\underbrace{\nabla_{\mathbf{x}} f}_{n \times 1} = \left( \frac{\textrm{d} f}{\textrm{d} \mathbf{x}} \right)^T


$$

To derive the chain rule in terms of gradients, we apply the identity $(AB)^T = B^T A^T$, which gives

$$


\begin{aligned}∇_{𝐱}𝑓 & =(\frac{d𝑓}{d𝐱})^{𝑇} \\ & =(\frac{d𝑓}{d𝐲}⋅\frac{d𝐲}{d𝐱})^{𝑇} \\ & =\underset{𝑛×𝑞}{\underset{}{(\frac{d𝐲}{d𝐱})^{𝑇}}}⋅\underset{𝑞×1}{\underset{}{(\frac{d𝑓}{d𝐲})^{𝑇}}}.\end{aligned}


$$

So, the gradient chain rule is

$$


\nabla_{\mathbf{x}} f = \left( \frac{\textrm{d} \mathbf{y}}{\textrm{d} \mathbf{x}} \right)^T \cdot \nabla_{\mathbf{y}} f.


$$

Note that the order matters; when expressed in the gradient form, the derivatives are applied *from right to left!*

### Example: Applying the Chain Rule to Gradients

#### Question

Consider the function $L: \mathbb{R}^{3} \rightarrow \mathbb{R}$ defined by $L(\mathbf{x}) = \dfrac{1}{2}(\mathbf{A}\mathbf{x} - \mathbf{b})^T(\mathbf{A}\mathbf{x} - \mathbf{b})$ where

$$


[\begin{aligned}3 & 1 & 2 \\ 0 & 5 & 4\end{aligned}]


$$

What is $\nabla_{\mathbf{x}} L(\mathbf{x})$ at $\begin{aligned}2 \\ 4 \\ 1\end{aligned}$

#### Explanation

We can solve this problem by applying the chain rule for gradients.

Let $\mathbf{y} = \mathbf{A}\mathbf{x} - \mathbf{b}.$ Then, $L(\mathbf{x}) = \dfrac{1}{2}\mathbf{y}^T\mathbf{y},$ and

$$


\nabla_{\mathbf{x}} L = \left(\dfrac{\textrm{d}L}{\textrm{d}\mathbf{x}}\right)^T = \left(\dfrac{\textrm{d}\mathbf{y}}{\textrm{d}\mathbf{x}}\right)^T \cdot \left(\dfrac{\textrm{d}L}{\textrm{d}\mathbf{y}}\right)^T.


$$

Now, since

$$


\dfrac{\textrm{d}}{\textrm{d}\mathbf{y}}\left(\dfrac{1}{2}\mathbf{y}^T\mathbf{y}\right) = \mathbf{y}^T \qquad\text{and}\qquad \dfrac{\textrm{d}\mathbf{y}}{\textrm{d}\mathbf{x}} = \dfrac{\textrm{d}}{\textrm{d}\mathbf{x}} (\mathbf{A}\mathbf{x} - \mathbf{b}) = \mathbf{A},


$$

we have that

$$


\begin{aligned}∇_{𝐱}𝐿 & =(\frac{d𝐲}{d𝐱})^{𝑇}⋅(\frac{d𝐿}{d𝐲})^{𝑇} \\ & =𝐀^{𝑇}⋅𝐲.\end{aligned}


$$

Evaluating at $\begin{aligned}2 \\ 4 \\ 1\end{aligned}$, we get

$$


\begin{aligned}∇_{𝐱}𝐿 & =𝐀^{𝑇}𝐲 \\ & =𝐀^{𝑇}(𝐀𝐱−𝐛) \\ & =[\begin{aligned}3 & 1 & 2 \\ 0 & 5 & 4\end{aligned}]^{𝑇}[\begin{aligned}3 & 1 & 2 \\ 0 & 5 & 4\end{aligned}]⋅\begin{aligned}2 \\ 4 \\ 1\end{aligned}−[\begin{aligned}6 \\ 9\end{aligned}] \\ & =\begin{aligned}3 & 0 \\ 1 & 5 \\ 2 & 4\end{aligned}([\begin{aligned}12 \\ 24\end{aligned}]−[\begin{aligned}6 \\ 9\end{aligned}]) \\ & =\begin{aligned}3 & 0 \\ 1 & 5 \\ 2 & 4\end{aligned}[\begin{aligned}6 \\ 15\end{aligned}] \\ & =\begin{aligned}18 \\ 81 \\ 72\end{aligned}.\end{aligned}


$$
