# Linear Maps Between Two Different Vector Spaces

Source: https://www.mathacademy.com/topics/907?courseId=55
Topic ID: 907

## Prerequisites

- [The Standard Matrix of a Linear Transformation](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/1959-the-standard-matrix-of-a-linear-transformation.md)

## Lesson

### Introduction

Similar to transformations in a vector space, we can define a transformation between two *different* vector spaces. For instance, consider the transformation that maps the vector

$$


[\begin{aligned}𝑥 \\ 𝑦\end{aligned}]


$$

from $\mathbb{R}^2$ to the vector

$$


\begin{aligned}𝑥+𝑦 \\ 𝑥−𝑦 \\ 2𝑥+2𝑦\end{aligned}


$$

in $\mathbb{R}^3,$ which can be written as

$$


[\begin{aligned}𝑥 \\ 𝑦\end{aligned}]


$$

The *standard matrix* of this transformation is

$$


\begin{aligned}1 & 1 \\ 1 & −1 \\ 2 & 2\end{aligned}


$$

Recall that a transformation $\mathbf{T}: V \to W$ between two vector spaces $V$ and $W$ is *linear* if for any vectors $\mathbf{v}_1, \mathbf{v}_2\in V$ and any scalar $k\in\mathbb{R}$, the following conditions are satisfied:

- $\mathbf{T}(k\mathbf{v}_1) = k\mathbf{T}(\mathbf{v}_1)$

- $\mathbf{T}(\mathbf{v}_1+\mathbf{v}_2) = \mathbf{T}(\mathbf{v}_1)+\mathbf{T}(\mathbf{v}_2)$

It is easy to check that if a transformation can be represented as a matrix, then it is a linear transformation. Therefore, the transformation $\mathbf{S}$ is a linear transformation.

In general, if $V$ and $W$ are $n$-dimensional and $m$-dimensional vector spaces respectively, then the standard matrix of a linear transformation $\mathbf{T}\!: V \!\rightarrow W$ is an $m\times n$ matrix $T$.

### Example: Finding the Standard Matrix of a Linear Transformation

#### Question

Find the standard matrix that represents the linear transformation $\mathbf{T}:\mathbb{R}^3 \to \mathbb{R}^2,$ where $\begin{aligned}𝑥 \\ 𝑦 \\ 𝑧\end{aligned}$

#### Explanation

We require a $2\times 3$ matrix ${T}$ such that

$$


\begin{aligned}𝑥 \\ 𝑦 \\ 𝑧\end{aligned}


$$

Notice that

$$


[\begin{aligned}2 & −3 & 0 \\ 1 & 1 & −1\end{aligned}]


$$

Therefore, the matrix which represents the linear transformation $\mathbf{T}$ is

$$


[\begin{aligned}2 & −3 & 0 \\ 1 & 1 & −1\end{aligned}]


$$

### Example: Determining the Components of a Linear Map

#### Question

$$


\begin{aligned}−8 & −5 \\ −3 & −6 \\ −4 & 5\end{aligned}


$$

Consider the standard matrix $T$ of the linear transformation $\mathbf{T}:\mathbb{R}^2 \to \mathbb{R}^3$ shown above. What is the value of $a-b?$

#### Explanation

Given the vector $[\begin{aligned}𝑥 \\ 𝑦\end{aligned}]$ we have

$$


\begin{aligned}\begin{aligned}−8 & −5 \\ −3 & −6 \\ −4 & 5\end{aligned}⋅[\begin{aligned}𝑥 \\ 𝑦\end{aligned}] & =\begin{aligned}−8𝑥−5𝑦 \\ −3𝑥−6𝑦 \\ −4𝑥+5𝑦\end{aligned} \\ & =\begin{aligned}−5𝑦−8𝑥 \\ −3𝑥−6𝑦 \\ 5𝑦−4𝑥\end{aligned}.\end{aligned}


$$

Therefore, the linear transformation $\mathbf{T}$ is given by

$$


[\begin{aligned}𝑥 \\ 𝑦\end{aligned}]


$$

Finally, $a-b=(-5)-(-4)=-1.$

### Example: Finding the Image of a Vector Under a Linear Map

#### Question

Consider the matrix $T$ and the vector $\mathbf{v}$ given below. If $T$ is the standard matrix of the linear transformation $\mathbf{T}:\mathbb{R}^3 \to \mathbb{R}^2,$ find $\mathbf{T}(\mathbf{v}).$

$$


[\begin{aligned}1 & −1 & 2 \\ 3 & 0 & 1\end{aligned}]


$$

#### Explanation

Using the fact that $\,\mathbf{T}(\mathbf{v})=T\cdot \mathbf{v},$ we get

$$


\begin{aligned}𝐓(𝐯) & =𝑇⋅𝐯 \\ & =[\begin{aligned}1 & −1 & 2 \\ 3 & 0 & 1\end{aligned}]⋅\begin{aligned}2 \\ 3 \\ 1\end{aligned} \\ & =[\begin{aligned}1 \\ 7\end{aligned}].\end{aligned}


$$
