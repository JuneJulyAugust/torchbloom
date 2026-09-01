# The Chain Rule for Total Derivatives

Source: https://www.mathacademy.com/topics/5868?courseId=145
Topic ID: 5868

## Prerequisites

- [The Multivariable Chain Rule](./3173-the-multivariable-chain-rule.md)
- [Total and Tensor Derivatives](./5845-total-and-tensor-derivatives.md)

## Lesson

### Introduction

Consider the multivariable function $f:\mathbb R^n \to\mathbb R,$ defined by

$$


f(\mathbf y) = f(y_1,y_2, \ldots, y_n)


$$

with $n$ independent variables, and $\mathbf{y}: \mathbb R \to \mathbb R^n,$ defined by

$$


\begin{aligned}𝑦_{1}(𝑥) \\ 𝑦_{2}(𝑥) \\ ⋮ \\ 𝑦_{𝑛}(𝑥)\end{aligned}


$$

which is a vector-valued function of a variable $x.$

In a previous lesson, we saw that the derivative of $f(\mathbf{y}(x))$ with respect to $x$ is given by the multivariable chain rule.

$$


\dfrac{\text{d} f}{\text{d}x}= \dfrac{\partial f}{\partial y_1} \cdot \dfrac{\partial y_1}{\partial x} + \dfrac{\partial f}{\partial y_2} \cdot \dfrac{\partial y_2}{\partial x} + \dots + \dfrac{\partial f}{\partial y_n} \cdot \dfrac{\partial y_n}{\partial x}


$$

This can be written as a product of matrices as follows:

$$


[\begin{aligned}\frac{𝜕𝑓}{𝜕𝑦_{1}} & \frac{𝜕𝑓}{𝜕𝑦_{2}} & ⋯ & \frac{𝜕𝑓}{𝜕𝑦_{𝑛}}\end{aligned}]


$$

Now, notice that this can be written as

$$


\dfrac{\text{d} f}{\text{d}x} = \underbrace{\dfrac{\text{d}f}{\text{d}\mathbf y}}_{1\times n} \cdot \underbrace{\dfrac{\text{d}\mathbf y}{\text{d}x}}_{n\times 1}


$$

where

- $\dfrac{\text{d}f}{\text{d}\mathbf y}$ is the *total derivative* of $f$ with respect to $\mathbf y$, which is a row vector of size $1\times n$, and

- $\dfrac{\text{d}\mathbf y}{\text{d}x}$ is the *total derivative* of $\mathbf y$ with respect to $x$, which is a column vector of size $n\times 1.$

In the next slides, we will apply this matrix formulation to a concrete example.

### The Chain Rule for Total Derivatives

Let $\mathbf{y}: \mathbb{R}^n \to \mathbb{R}^q$ and $\mathbf{f}: \mathbb{R}^q \to \mathbb{R}^m$ be two differentiable vector-valued functions. We want to compute the derivative of the composition $\mathbf{f}(\mathbf{y}(\mathbf{x}))$ with respect to $\mathbf{x} \in \mathbb{R}^n.$

The **chain rule for total derivatives** tells us that

$$


\underbrace{\dfrac{\text{d}\mathbf{f}}{\text{d} \mathbf{x}}}_{m \times n} = \underbrace{\dfrac{\text{d}\mathbf{f}}{\text{d} \mathbf{y}}}_{m \times q} \cdot \underbrace{\dfrac{\text{d}\mathbf{y}}{\text{d} \mathbf{x}}}_{q \times n}.


$$

Here, the dot denotes matrix multiplication. The inner matrix dimensions match, so this is a valid matrix product.

**Watch Out!** When applying the chain rule for total derivatives, the *order of multiplication matters!* For example, if we swap the order of the matrix products, we'd get an incorrect result:

$$


\dfrac{\text{d}\mathbf{f}}{\text{d} \mathbf{x}} = \underbrace{\dfrac{\text{d}\mathbf{y}}{\text{d} \mathbf{x}}}_{q \times n} \cdot \underbrace{\dfrac{\text{d}\mathbf{f}}{\text{d} \mathbf{y}}}_{m \times q} \qquad \text{(WRONG!)}


$$

This is incorrect because the inner matrix dimensions do not agree, making it an invalid matrix product.

Let's take a look at a concrete example.

### A Concrete Example

Suppose we define

$$


[\begin{aligned}𝑦_{1}+𝑦_{2} \\ 𝑦_{1}−2𝑦_{2}\end{aligned}]


$$

Then, we have $\mathbf{f}: \mathbb{R}^2 \to \mathbb{R}^2$ and $\mathbf{y}: \mathbb{R}^2 \to \mathbb{R}^2.$

Let's see how to compute the derivative for the composition $\mathbf{f}(\mathbf{y}(\mathbf{x})).$

The chain rule states that

$$


\dfrac{\text{d} \mathbf{f}}{\text{d} \mathbf{x}} = \dfrac{\text{d}\mathbf{f}}{\text{d} \mathbf{y}} \cdot \dfrac{\text{d}\mathbf{y}}{\text{d} \mathbf{x}}.


$$

Let's consider each of the factors in turn.

- The function $\mathbf{f}$ acts on a vector $\mathbf{y} \in \mathbb{R}^2$ and outputs a vector $\mathbf{f}(\mathbf{y}) \in \mathbb{R}^2.$ Thus, the total derivative of $\mathbf{f}$ with respect to $\mathbf{y}$ is a $2\times 2$ matrix.

- The function $\mathbf{y}$ acts on a vector $\mathbf{x} \in \mathbb{R}^2$ and outputs a vector $\mathbf{y}(\mathbf{x}) \in \mathbb{R}^2.$ Thus, the total derivative of $\mathbf{y}$ with respect to $\mathbf{x}$ is also a $2\times 2$ matrix.

Computing our derivatives, we get

$$


[\begin{aligned}1 & 1 \\ 1 & −2\end{aligned}]


$$

Then, by the chain rule, we have

$$


\begin{aligned}\frac{d𝐟}{d𝐱} & =\frac{d𝐟}{d𝐲}⋅\frac{d𝐲}{d𝐱} \\ & =[\begin{matrix}1 & 1 \\ 1 & −2\end{matrix}]⋅[\begin{matrix}2𝑥_{1} & 0 \\ 0 & 2𝑥_{2}\end{matrix}] \\ & =[\begin{matrix}2𝑥_{1} & 2𝑥_{2} \\ 2𝑥_{1} & −4𝑥_{2}\end{matrix}].\end{aligned}


$$

This matrix gives us the total derivative of $\mathbf f$ with respect to $\mathbf x.$

### Verifying the Chain Rule Example

Let's *verify* that our result from the previous slide is correct by computing the derivative directly.

Recall that

$$


[\begin{aligned}𝑦_{1}+𝑦_{2} \\ 𝑦_{1}−2𝑦_{2}\end{aligned}]


$$

First, we substitute $\mathbf{y}$ into $\mathbf{f}$ to write $\mathbf{f}$ explicitly in terms of $\mathbf{x}{:}$

$$


[\begin{aligned}𝑥_{21}+𝑥_{22} \\ 𝑥_{21}−2𝑥_{22}\end{aligned}]


$$

Now, we compute the derivative of $\mathbf f$ with respect to $\mathbf x{:}$

$$


\begin{aligned}\frac{d𝐟}{d𝐱} & =\begin{matrix}\frac{𝜕𝑓_{1}}{𝜕𝑥_{1}} & \frac{𝜕𝑓_{1}}{𝜕𝑥_{2}} \\ \frac{𝜕𝑓_{2}}{𝜕𝑥_{1}} & \frac{𝜕𝑓_{2}}{𝜕𝑥_{2}}\end{matrix} \\ & =[\begin{matrix}2𝑥_{1} & 2𝑥_{2} \\ 2𝑥_{1} & −4𝑥_{2}\end{matrix}].\end{aligned}


$$

This agrees with the result we obtained using the chain rule.

### Example: Identifying the Dimensions of a Derivative

#### Question

Consider the functions $\mathbf y: \mathbb R^3\to \mathbb R^2$ and $\mathbf f: \mathbb R^2\to \mathbb R^2,$ defined by

$$


[\begin{aligned}𝑥_{2} \\ 𝑥_{1}+𝑥_{3}\end{aligned}]


$$

Determine the dimensions of the matrix representing the derivative

$$


\dfrac{\textrm d}{\textrm d \mathbf x} \mathbf{f}(\mathbf{y}(\mathbf x)) .


$$

#### Explanation

Using the chain rule, we have

$$


\dfrac{\textrm d}{\textrm d \mathbf x} \mathbf{f}(\mathbf{y}(\mathbf x)) = \dfrac{\textrm d\mathbf f}{\textrm d \mathbf y} \cdot \dfrac{\textrm d\mathbf y}{\textrm d \mathbf x}.


$$

Let's consider each of the factors in turn.

- The function $\mathbf{f}$ acts on a vector $\mathbf{y} \in \mathbb{R}^2$ and outputs a vector $\mathbf{f}(\mathbf{y}) \in \mathbb{R}^2.$ Thus, the total derivative of $\mathbf{f}$ with respect to $\mathbf{y}$ is a $2\times 2$ matrix.

- The function $\mathbf{y}$ acts on a vector $\mathbf{x} \in \mathbb{R}^3$ and outputs a vector $\mathbf{y}(\mathbf{x}) \in \mathbb{R}^2.$ Thus, the total derivative of $\mathbf{y}$ with respect to $\mathbf{x}$ is a $2\times 3$ matrix.

Therefore, the product

$$


\dfrac{\textrm d\mathbf f}{\textrm d \mathbf x}= \dfrac{\textrm d\mathbf f}{\textrm d \mathbf y} \cdot \dfrac{\textrm d\mathbf y}{\textrm d \mathbf x}


$$

of a $2\times 2$ matrix with a $2\times 3$ matrix is a $2\times 3$ matrix.

### Example: Differentiating the Composition of Vector-Valued Functions

#### Question

Consider the functions $\mathbf y: \mathbb R^3\to \mathbb R^2$ and $\mathbf f: \mathbb R^2\to \mathbb R^2,$ defined by

$$


[\begin{aligned}𝑥_{1}−𝑥_{2}𝑥_{3} \\ 𝑥_{1}+𝑥_{2}𝑥_{3}\end{aligned}]


$$

What is $\dfrac{\textrm d}{\textrm d \mathbf x} \mathbf{f}(\mathbf{y}(\mathbf x))$ evaluated at $\begin{aligned}0 \\ 1 \\ −1\end{aligned}$

#### Explanation

Using the chain rule, we have

$$


\dfrac{\textrm d}{\textrm d \mathbf x} \mathbf{f}(\mathbf{y}(\mathbf x)) = \dfrac{\textrm d\mathbf f}{\textrm d \mathbf y} \cdot \dfrac{\textrm d\mathbf y}{\textrm d \mathbf x}.


$$

Let's consider each of the factors in turn.

- The function $\mathbf{f}$ acts on a vector $\mathbf{y} \in \mathbb{R}^2$ and outputs a vector $\mathbf{f}(\mathbf{y}) \in \mathbb{R}^2.$ Thus, the total derivative of $\mathbf{f}$ with respect to $\mathbf{y}$ is a $2\times 2$ matrix Evaluating at $[\begin{aligned}0−1⋅(−1) \\ 0+1⋅(−1)\end{aligned}]$ we get

- The function $\mathbf{y}$ acts on a vector $\mathbf{x} \in \mathbb{R}^3$ and outputs a vector $\mathbf{y}(\mathbf{x}) \in \mathbb{R}^2.$ Thus, the total derivative of $\mathbf{y}$ with respect to $\mathbf{x}$ is a $2\times 3$ matrix Evaluating at $\begin{aligned}0 \\ 1 \\ −1\end{aligned}$ we get

Therefore, we have

$$


\begin{aligned}\frac{d}{d𝐱}𝐟(𝐲(𝐱))_{𝐱_{0}} & =\frac{d𝐟}{d𝐲}_{𝐲_{0}}⋅\frac{d𝐲}{d𝐱}_{𝐱_{0}} \\ & =[\begin{matrix}1 & 1 \\ 1 & −1\end{matrix}]⋅[\begin{matrix}1 & 1 & −1 \\ 1 & −1 & 1\end{matrix}] \\ & =[\begin{matrix}2 & 0 & 0 \\ 0 & 2 & −2\end{matrix}].\end{aligned}


$$

### The Chain Rule for Functions Defined Using Matrices

We can use the chain rule for functions that use matrices in their definition.

For example, consider the functions $\mathbf{y}(\mathbf{x}) = \mathbf{A}\mathbf{x}$ and $\mathbf{f}(\mathbf{y}) = \mathbf{B}\mathbf{y},$ where $\mathbf x\in \mathbb R^3, \mathbf y\in\mathbb R^2,$ and the matrices $\mathbf{A}$ and $\mathbf{B}$ are given by

$$


[\begin{aligned}1 & 0 & 2 \\ −1 & 3 & 4\end{aligned}]


$$

What is $\dfrac{\textrm d}{\textrm d \mathbf x} \mathbf{f}(\mathbf{y}(\mathbf x))$ evaluated at $\mathbf{x}_0 = [2, \, 0, \, -1]^T?$

Using the chain rule, we have

$$


\dfrac{\textrm d}{\textrm d \mathbf x} \mathbf{f}(\mathbf{y}(\mathbf x)) = \dfrac{\textrm d\mathbf f}{\textrm d \mathbf y} \cdot \dfrac{\textrm d\mathbf y}{\textrm d \mathbf x}.


$$

Let's consider each of the factors in turn.

- The function $\mathbf{f}$ acts on a vector $\mathbf{y} \in \mathbb{R}^2$ by multiplying it by $\mathbf{B}$ and outputs a vector $\mathbf{f}(\mathbf{y}) \in \mathbb{R}^2.$ Thus,

- The function $\mathbf{y}$ acts on a vector $\mathbf{x} \in \mathbb{R}^3$ by multiplying it by $\mathbf{A}$ and outputs a vector $\mathbf{y}(\mathbf{x}) \in \mathbb{R}^2.$ Thus,

Since these derivatives are constant matrices, the value at $\mathbf{x}_0$ is simply their product. Therefore, we have

$$


\begin{aligned}\frac{d}{d𝐱}𝐟(𝐲(𝐱)) & =\frac{d𝐟}{d𝐲}⋅\frac{d𝐲}{d𝐱} \\ & =𝐁𝐀 \\ & =[\begin{matrix}3 & 2 \\ 1 & −1\end{matrix}][\begin{matrix}1 & 0 & 2 \\ −1 & 3 & 4\end{matrix}] \\ & =[\begin{matrix}1 & 6 & 14 \\ 2 & −3 & −2\end{matrix}].\end{aligned}


$$

### Example: Differentiating Functions Defined Using Matrices

#### Question

Consider the functions $\mathbf{y}(\mathbf{x}) = \mathbf{A}\mathbf{x}$ and $\mathbf{f}(\mathbf{y}) = \mathbf{B}\mathbf{y},$ where $\mathbf x\in \mathbb R^3, \mathbf y\in\mathbb R^2,$ and the matrices $\mathbf{A}$ and $\mathbf{B}$ are given by

$$


[\begin{aligned}2 & 1 & 0 \\ 4 & −3 & 1\end{aligned}]


$$

What is $\dfrac{\textrm d}{\textrm d \mathbf x} \mathbf{f}(\mathbf{y}(\mathbf x))$ evaluated at $\mathbf{x}_0 = [1, \, 0, \, -2]^T?$

#### Explanation

Using the chain rule, we have

$$


\dfrac{\textrm d}{\textrm d \mathbf x} \mathbf{f}(\mathbf{y}(\mathbf x)) = \dfrac{\textrm d\mathbf f}{\textrm d \mathbf y} \cdot \dfrac{\textrm d\mathbf y}{\textrm d \mathbf x}.


$$

Let's consider each of the factors in turn.

- The function $\mathbf{f}$ acts on a vector $\mathbf{y} \in \mathbb{R}^2$ by multiplying it by $\mathbf{B}$ and outputs a vector $\mathbf{f}(\mathbf{y}) \in \mathbb{R}^3.$ Thus,

- The function $\mathbf{y}$ acts on a vector $\mathbf{x} \in \mathbb{R}^3$ by multiplying it by $\mathbf{A}$ and outputs a vector $\mathbf{y}(\mathbf{x}) \in \mathbb{R}^2.$ Thus,

Therefore, we have

$$


\begin{aligned}\frac{d}{d𝐱}𝐟(𝐲(𝐱)) & =\frac{d𝐟}{d𝐲}⋅\frac{d𝐲}{d𝐱} \\ & =𝐁𝐀 \\ & =\begin{matrix}−1 & 0 \\ −3 & 1 \\ 2 & 4\end{matrix}[\begin{matrix}2 & 1 & 0 \\ 4 & −3 & 1\end{matrix}] \\ & =\begin{matrix}−2 & −1 & 0 \\ −2 & −6 & 1 \\ 20 & −10 & 4\end{matrix}.\end{aligned}


$$

### Extending the Chain Rule

Suppose we have the following differentiable functions:

$$


\mathbf{y}: \mathbb{R}^n \to \mathbb{R}^p, \qquad \mathbf{z}: \mathbb{R}^p \to \mathbb{R}^q, \qquad \mathbf{f}: \mathbb{R}^q \to \mathbb{R}^m


$$

The chain rule can be extended in the natural way as follows:

$$


\dfrac{\textrm d}{\textrm d \mathbf x} \mathbf{f}(\mathbf{z}(\mathbf{y}(\mathbf x))) = \underbrace{\dfrac{\textrm d\mathbf f}{\textrm d \mathbf z}}_{m\times q} \cdot \underbrace{\dfrac{\textrm d\mathbf z}{\textrm d \mathbf y}}_{q\times p} \cdot \underbrace{\dfrac{\textrm d\mathbf y}{\textrm d \mathbf x}}_{p\times n}


$$

Let's see an example.

### Example: Differentiating the Composition of Three Functions

#### Question

For $\mathbf x, \mathbf y, \mathbf z\in\mathbb R^2,$ consider the following functions:

$$


\begin{aligned} & 𝐲(𝐱)=𝐀𝐱\,where\,𝐀=[\begin{matrix}−1 & 1 \\ 0 & −1\end{matrix}] \\ & 𝐳(𝐲)=[\begin{matrix}𝑦_{1}−𝑦_{2} \\ 𝑦_{1}𝑦_{2}\end{matrix}] \\ & 𝐟(𝐳)=𝐂𝐳\,where\,𝐂=[\begin{matrix}2 & −1 \\ −1 & 2\end{matrix}]\end{aligned}


$$

What is $\dfrac{\textrm d}{\textrm d \mathbf x} \mathbf{f}(\mathbf{z}(\mathbf{y}(\mathbf x)))$ evaluated at $[\begin{aligned}−1 \\ 1\end{aligned}]$

#### Explanation

Using the chain rule, we have

$$


\dfrac{\textrm d}{\textrm d \mathbf x} \mathbf{f}(\mathbf{z}(\mathbf{y}(\mathbf x))) = \dfrac{\textrm d\mathbf f}{\textrm d \mathbf z} \cdot \dfrac{\textrm d\mathbf z}{\textrm d \mathbf y} \cdot \dfrac{\textrm d\mathbf y}{\textrm d \mathbf x}.


$$

Let's consider each of the factors in turn.

- The function $\mathbf{f}$ acts on a vector $\mathbf{z} \in \mathbb{R}^2$ by multiplying it by $\mathbf{C}$ and outputs a vector $\mathbf{f}(\mathbf{z}) \in \mathbb{R}^2.$ Thus,

- The function $\mathbf{z}$ acts on a vector $\mathbf{y} \in \mathbb{R}^2$ and outputs a vector $\mathbf{z}(\mathbf{y}) \in \mathbb{R}^2.$ Thus, Evaluating at $[\begin{aligned}−1 & 1 \\ 0 & −1\end{aligned}]$ we get

- The function $\mathbf{y}$ acts on a vector $\mathbf{x} \in \mathbb{R}^2$ by multiplying it by $\mathbf{A}$ and outputs a vector $\mathbf{y}(\mathbf{x}) \in \mathbb{R}^2.$ Thus,

Therefore, we have

$$


\begin{aligned}\frac{d}{d𝐱}𝐟(𝐳(𝐲(𝐱)))_{𝐱_{0}} & =\frac{d𝐟}{d𝐳}_{𝐳_{0}}⋅\frac{d𝐳}{d𝐲}_{𝐲_{0}}⋅\frac{d𝐲}{d𝐱}_{𝐱_{0}} \\ & =[\begin{matrix}2 & −1 \\ −1 & 2\end{matrix}]⋅[\begin{matrix}1 & −1 \\ −1 & 2\end{matrix}]⋅[\begin{matrix}−1 & 1 \\ 0 & −1\end{matrix}] \\ & =[\begin{matrix}3 & −4 \\ −3 & 5\end{matrix}]⋅[\begin{matrix}−1 & 1 \\ 0 & −1\end{matrix}] \\ & =[\begin{matrix}−3 & 7 \\ 3 & −8\end{matrix}].\end{aligned}


$$
