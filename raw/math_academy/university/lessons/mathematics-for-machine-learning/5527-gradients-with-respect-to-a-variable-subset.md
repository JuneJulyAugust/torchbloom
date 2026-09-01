# Gradients With Respect to a Variable Subset

Source: https://www.mathacademy.com/topics/5527?courseId=145
Topic ID: 5527

## Prerequisites

- [The Second Derivative of a Multivariable Function](./2824-the-second-derivative-of-a-multivariable-function.md)

## Lesson

### Introduction

Recall that the gradient of a function

$$


f : \mathbb{R}^n \to \mathbb{R}


$$

tells us how the function changes with respect to each of its input variables. It collects all the partial derivatives into a single vector:

$$


\begin{aligned}\frac{𝜕𝑓}{𝜕𝑥_{1}} \\ \frac{𝜕𝑓}{𝜕𝑥_{2}} \\ ⋮ \\ \frac{𝜕𝑓}{𝜕𝑥_{𝑛}}\end{aligned}


$$

This vector points in the direction of the *steepest increase* of the function, and its components describe how sensitive $f$ is to changes in each variable $x_1, x_2, \dots, x_n.$

In other words, $\nabla f$ gives us a complete picture of how $f$ behaves locally around a point, not just in one direction, but in every direction.

But sometimes, we’re not interested in how the function behaves in every direction. Maybe some variables are being held fixed, or we just care about how the function responds to changes in a few specific inputs. In that case, we don’t need the full gradient. We only need the derivatives with respect to the variables we care about.

This idea leads us to the concept of the **subset gradient**, which captures how a function changes with respect to only a chosen group of variables while treating the others as constant.

In this lesson, we will learn what subset gradients are, and how to compute them. Let's look at a concrete example in the next slide.

### The Subset Gradient

A **subset gradient** is the vector formed by taking only the partial derivatives of a function with respect to a chosen subset of variables.

Let’s look at an example to understand how a subset gradient works in practice.

Suppose we have the function

$$


f(x, y, z) = x^2 y + y z^2.


$$

This function depends on three variables, and its full gradient is

$$


\begin{aligned}\frac{𝜕𝑓}{𝜕𝑥} \\ \frac{𝜕𝑓}{𝜕𝑦} \\ \frac{𝜕𝑓}{𝜕𝑧}\end{aligned}


$$

The full gradient tells us how $f$ responds to changes in all three directions. But in some situations, we may only care about how $f$ changes when we vary a few of the variables, for example, just $x$ and $y.$

If that’s the case, we compute a subset gradient, which focuses only on the variables of interest. In this case, we compute

$$


\begin{aligned}\frac{𝜕𝑓}{𝜕𝑥} \\ \frac{𝜕𝑓}{𝜕𝑦}\end{aligned}


$$

Here, we are treating $z$ as a constant, as if it were fixed and not changing, while taking partial derivatives with respect to $x$ and $y$ only. This is the same idea that underlies partial derivatives more generally: we hold all other variables constant except the ones we are differentiating with respect to.

Subset gradients are especially useful in problems where only some variables are being updated. They allow us to focus on the directions that matter for a particular step or subproblem, without being distracted by variables we are not actively changing.

### Example: Computing Basic Subset Gradients

#### Question

Given the function $f(x,y,z,w) = xyzw,$ compute $\nabla_{x,w} \: f.$

#### Explanation

To compute $\nabla_{x,w} \: f$, we take partial derivatives with respect to $x$ and $w$ only.

$$


\begin{aligned}\frac{𝜕𝑓}{𝜕𝑥}=\frac{𝜕}{𝜕𝑥}(𝑥𝑦𝑧𝑤) & =𝑦𝑧𝑤 \\ \frac{𝜕𝑓}{𝜕𝑤}=\frac{𝜕}{𝜕𝑤}(𝑥𝑦𝑧𝑤) & =𝑥𝑦𝑧\end{aligned}


$$

Therefore, we obtain the following:

$$


\begin{aligned}∇_{𝑥,𝑤}\,𝑓 & =\begin{matrix}\frac{𝜕𝑓}{𝜕𝑥} \\ \frac{𝜕𝑓}{𝜕𝑤}\end{matrix} \\ & =[\begin{matrix}𝑦𝑧𝑤 \\ 𝑥𝑦𝑧\end{matrix}]\end{aligned}


$$

### Variable Groups

So far, we have looked at functions with a few individual variables like $x$, $y$, and $z$. But in many real-world problems, we work with vectors of inputs and parameters rather than just a few named variables.

Let’s return to a familiar example where we fit a straight line to some data.

Suppose our *linear model* is given by

$$


f(x; m, b) = mx + b,


$$

where

- $x$ is the input, and

- $m$ and $b$ are the *parameters* we are trying to learn.

If we want to understand how the output changes when we adjust $m$ and $b$, we compute the gradient with respect to these parameters, denoted $\nabla_{m,b} \, f$. This tells us how sensitive the function is to changes in the slope and intercept, assuming $x$ is held fixed.

The same idea applies in higher dimensions.

Now, suppose we have multiple input variables and define a model

$$


f(\mathbf{x}; \mathbf{w}) = w_1 x_1 + w_2 x_2 + \cdots + w_n x_n,


$$

where

- $\mathbf{x} = (x_1, x_2, \dots, x_n)$ is the **input vector**, and

- $\mathbf{w} = (w_1, w_2, \dots, w_n)$ is the **vector of parameters** (or weights).

To understand how $f$ depends on the parameters, we compute the *gradient* with respect to $\mathbf{w}{:}$

$$


\begin{aligned}\frac{𝜕𝑓}{𝜕𝑤_{1}} \\ \frac{𝜕𝑓}{𝜕𝑤_{2}} \\ ⋮ \\ \frac{𝜕𝑓}{𝜕𝑤_{𝑛}}\end{aligned}


$$

Each $x_j$ is treated as constant during this computation. Just like in the scalar case, we are asking how the output depends on each parameter while keeping the input fixed. This gradient gives exactly the information we need when updating model weights during training.

Next, we will apply this result to a specific numerical example.

### Example: Computing Parameter Subset Gradients

#### Question

Given the function, compute

#### Explanation

To compute, we take partial derivatives with respect to and.

Therefore, we obtain the following:

### Example: Computing Vector Subset Gradients

#### Question

Given the function $f(\mathbf{x}; \mathbf{w}) = w_1x_1^{3} + w_2x_2^{3},$ compute $\nabla_{\mathbf{w}} \: f$ with the input $[\begin{aligned}3,\,−2\end{aligned}]$

#### Explanation

To compute $\nabla_{\mathbf{w}} \: f$, we take partial derivatives with respect to each component of $\mathbf{w}.$

$$


\begin{aligned}\frac{𝜕𝑓}{𝜕𝑤_{1}} & =\frac{𝜕}{𝜕𝑤_{1}}(𝑤_{1}𝑥_{31}+𝑤_{2}𝑥_{32})=𝑥_{31} \\ \frac{𝜕𝑓}{𝜕𝑤_{2}} & =\frac{𝜕}{𝜕𝑤_{2}}(𝑤_{1}𝑥_{31}+𝑤_{2}𝑥_{32})=𝑥_{32}\end{aligned}


$$

Therefore, with $[\begin{aligned}3,\,−2\end{aligned}]$ we obtain the following:

$$


\begin{aligned}∇_{𝐰}\,𝑓 & =[\begin{matrix}𝑥_{31} \\ 𝑥_{32}\end{matrix}] \\ & =[\begin{matrix}27 \\ −8\end{matrix}]\end{aligned}


$$

### Second-Order Derivatives

Just as we can compute gradients with respect to a subset of variables, we can also take second derivatives while focusing on just the variables that matter for our problem.

When we write $\nabla_{\mathbf{w}}(\nabla_{\mathbf{w}} f)$, we are computing all second-order partial derivatives of the function $f$ with respect to the variables in $\mathbf{w}.$ The result is a square matrix where each entry describes how one component of the gradient changes when we vary one of the selected variables. This matrix is the **Hessian with respect to** $\mathbf{w}.$

To make this concrete, suppose we have a function $f(x, y, z)$ that depends on three variables. If we only care about second derivatives with respect to $x$ and $y$, we write $\nabla_{x,y}(\nabla_{x,y} f).$

This gives us a $2 \times 2$ matrix that contains the following second-order partial derivatives

$$


\begin{aligned}\frac{𝜕^{2}𝑓}{𝜕𝑥^{2}} & \frac{𝜕^{2}𝑓}{𝜕𝑥𝜕𝑦} \\ \frac{𝜕^{2}𝑓}{𝜕𝑦𝜕𝑥} & \frac{𝜕^{2}𝑓}{𝜕𝑦^{2}}\end{aligned}


$$

Even though $f$ depends on three variables, this matrix isolates the second-derivative behavior of $f$ in just the $x$ and $y$ directions. This allows us to analyze or optimize over part of the input space without involving every variable.

Let’s go through a concrete example.

Consider the function

$$


f(\mathbf{x}; \mathbf{w}) = w_1^2 x_2^2 - w_2 x_1,


$$

and suppose we want to compute the Hessian with respect to $\mathbf{w} = [w_1, \, w_2]^T.$

First, we compute the gradient:

$$


\begin{aligned}\frac{𝜕𝑓}{𝜕𝑤_{1}} & =\frac{𝜕}{𝜕𝑤_{1}}(𝑤_{21}𝑥_{22}−𝑤_{2}𝑥_{1})=2𝑤_{1}𝑥_{22} \\ \frac{𝜕𝑓}{𝜕𝑤_{2}} & =\frac{𝜕}{𝜕𝑤_{2}}(𝑤_{21}𝑥_{22}−𝑤_{2}𝑥_{1})=−𝑥_{1}\end{aligned}


$$

Next, we compute the second derivatives:

$$


\begin{aligned}\frac{𝜕^{2}𝑓}{𝜕𝑤_{21}} & =2𝑥_{22}, & \,\frac{𝜕^{2}𝑓}{𝜕𝑤_{1}𝜕𝑤_{2}} & =0 \\ \frac{𝜕^{2}𝑓}{𝜕𝑤_{2}𝜕𝑤_{1}} & =0 & \,\frac{𝜕^{2}𝑓}{𝜕𝑤_{22}} & =0\end{aligned}


$$

Putting everything into matrix form, we get the Hessian

$$


\begin{aligned}\frac{𝜕^{2}𝑓}{𝜕𝑤_{21}} & \frac{𝜕^{2}𝑓}{𝜕𝑤_{1}𝜕𝑤_{2}} \\ \frac{𝜕^{2}𝑓}{𝜕𝑤_{2}𝜕𝑤_{1}} & \frac{𝜕^{2}𝑓}{𝜕𝑤_{22}}\end{aligned}


$$

This is the Hessian with respect to the parameter vector $\mathbf{w}.$ It tells us how the gradient of the function (with respect to parameters) changes when we vary each parameter and reveals the local shape of the function near any given point.

### Example: Computing Second-Order Derivatives

#### Question

Given the function $f(\mathbf{x}; \mathbf{w}) = (w_1x_1 - w_2+x_2)^2,$ compute $\nabla_{\mathbf{w}}(\nabla_{\mathbf{w}} \: f).$

#### Explanation

First, we compute $\nabla_{\mathbf{w}} \: f$:

$$


\begin{aligned}\frac{𝜕𝑓}{𝜕𝑤_{1}} & =\frac{𝜕}{𝜕𝑤_{1}}(𝑤_{1}𝑥_{1}−𝑤_{2}+𝑥_{2})^{2}=2𝑥_{1}(𝑤_{1}𝑥_{1}−𝑤_{2}+𝑥_{2}) \\ \frac{𝜕𝑓}{𝜕𝑤_{2}} & =\frac{𝜕}{𝜕𝑤_{2}}(𝑤_{1}𝑥_{1}−𝑤_{2}+𝑥_{2})^{2}=−2(𝑤_{1}𝑥_{1}−𝑤_{2}+𝑥_{2})\end{aligned}


$$

Next, we compute the second derivatives:

$$


\begin{aligned} & \frac{𝜕^{2}𝑓}{𝜕𝑤_{21}}=2𝑥_{21}\,\, & & \frac{𝜕^{2}𝑓}{𝜕𝑤_{1}𝜕𝑤_{2}}=−2𝑥_{1} \\ & \frac{𝜕^{2}𝑓}{𝜕𝑤_{2}𝜕𝑤_{1}}=−2𝑥_{1}\,\, & & \frac{𝜕^{2}𝑓}{𝜕𝑤_{22}}=2\end{aligned}


$$

Therefore, we obtain the following:

$$


\begin{aligned}∇_{𝐰}(∇_{𝐰}\,𝑓) & =\begin{matrix}\frac{𝜕^{2}𝑓}{𝜕𝑤_{21}} & \frac{𝜕^{2}𝑓}{𝜕𝑤_{1}𝜕𝑤_{2}} \\ \frac{𝜕^{2}𝑓}{𝜕𝑤_{2}𝜕𝑤_{1}} & \frac{𝜕^{2}𝑓}{𝜕𝑤_{22}}\end{matrix} \\ & =[\begin{matrix}2𝑥_{21} & −2𝑥_{1} \\ −2𝑥_{1} & 2\end{matrix}]\end{aligned}


$$
