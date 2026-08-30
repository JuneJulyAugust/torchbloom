# The Standard Matrix of a Linear Transformation

Source: https://www.mathacademy.com/topics/1959?courseId=101
Topic ID: 1959

## Prerequisites

- [Introduction to Linear Transformations](./865-introduction-to-linear-transformations.md)
- [Multiplying a Matrix by a Column Vector](./1195-multiplying-a-matrix-by-a-column-vector.md)

## Lesson

### Introduction

Every linear transformation $\mathbf{T}$ that acts on 2D-vectors has a $2 \times 2$ matrix $T$ associated with it. The matrix is called the **standard matrix** of the linear transformation. For any vector $\mathbf{v},$ the standard matrix $T$ of a linear transformation $\mathbf{T}$ must have the property

$$


\mathbf{T}(\mathbf{v}) = T \cdot \mathbf{v}


$$

where $T \cdot \mathbf{v}$ is the matrix product of the standard matrix $T$ and the vector $\mathbf{v}.$

To illustrate, consider the following linear transformation:

$$


[\begin{aligned}𝑥 \\ 𝑦\end{aligned}]


$$

The standard matrix for the linear transformation $\mathbf{S}$ is $[\begin{aligned}−3 & 7 \\ 1 & −5\end{aligned}]$ since it has the following property:

$$


\begin{aligned}\overset{\overset{[\begin{aligned}−3 & 7 \\ 1 & −5\end{aligned}]}{}}{𝑆}⋅[\begin{aligned}𝑥 \\ 𝑦\end{aligned}] & =[\begin{aligned}−3⋅𝑥+7⋅𝑦 \\ 1⋅𝑥+(−5)⋅𝑦\end{aligned}] \\ & =[\begin{aligned}−3𝑥+7𝑦 \\ 𝑥−5𝑦\end{aligned}] \\ & =𝐒[\begin{aligned}𝑥 \\ 𝑦\end{aligned}].\end{aligned}


$$

Notice here that $\mathbf{S}$ (using a **bold** letter) denotes the transformation (function) itself, while $S$ (big *italic* letter) is a $2 \times 2$ matrix that corresponds to the linear transformation.

In general, the standard matrix of the linear transformation $[\begin{aligned}𝑥 \\ 𝑦\end{aligned}]$ is

$$


[\begin{aligned}𝑎 & 𝑏 \\ 𝑐 & 𝑑\end{aligned}]


$$

We can learn a lot about linear transformations by looking at their standard matrices.

### Example: Identifying the Standard Matrix of a Linear Transformation

#### Question

Find the standard matrix that represents the linear transformation $\mathbf{T},$ where

$$


[\begin{aligned}𝑥 \\ 𝑦\end{aligned}]


$$

#### Explanation

We require a $2\times 2$ matrix ${T}$ such that

$$


[\begin{aligned}𝑥 \\ 𝑦\end{aligned}]


$$

Notice that

$$


[\begin{aligned}1 & 3 \\ 2 & −1\end{aligned}]


$$

Therefore, the matrix which represents the linear transformation $\mathbf{T}$ is

$$


[\begin{aligned}1 & 3 \\ 2 & −1\end{aligned}]


$$

### Example: Determining a Linear Transformation Given its Standard Matrix

#### Question

What is the linear transformation $\mathbf{T}$ whose standard matrix is $[\begin{aligned}8 & −1 \\ −5 & −2\end{aligned}]$

#### Explanation

Consider a general vector $[\begin{aligned}𝑥 \\ 𝑦\end{aligned}]$ Multiplying by the matrix $T,$ we have

$$


\begin{aligned}𝑇⋅[\begin{aligned}𝑥 \\ 𝑦\end{aligned}] & =[\begin{aligned}8 & −1 \\ −5 & −2\end{aligned}]⋅[\begin{aligned}𝑥 \\ 𝑦\end{aligned}] \\ & =[\begin{aligned}8𝑥−𝑦 \\ −5𝑥−2𝑦\end{aligned}].\end{aligned}


$$

Therefore, the linear transformation $\,\mathbf{T}\,$ is given by

$$


[\begin{aligned}𝑥 \\ 𝑦\end{aligned}]


$$

### Example: Finding the Image of a Vector Under a Linear Transformation Given its Standard Matrix

#### Question

Consider the matrix $T$ and the vector $\mathbf{v}$ given below. If $T$ is the standard matrix of the linear transformation $\mathbf{T},$ find $\mathbf{T}(\mathbf{v}).$

$$


[\begin{aligned}4 & 7 \\ −6 & −2\end{aligned}]


$$

#### Explanation

Using the fact that $\,\mathbf{T}(\mathbf{v})=T\cdot \mathbf{v},$ we get

$$


\begin{aligned}𝐓(𝐯) & =𝑇⋅𝐯 \\ & =[\begin{aligned}4 & 7 \\ −6 & −2\end{aligned}]⋅[\begin{aligned}−2 \\ 5\end{aligned}] \\ & =[\begin{aligned}27 \\ 2\end{aligned}].\end{aligned}


$$

### Example: Identifying the Standard Matrix of a Linear Transformation With Rearranging

#### Question

Find the standard matrix that represents the linear transformation $\mathbf{T},$ where

$$


[\begin{aligned}𝑥 \\ 𝑦\end{aligned}]


$$

#### Explanation

First, rewrite the order of the variables in the usual way:

$$


[\begin{aligned}𝑥 \\ 𝑦\end{aligned}]


$$

We require a $2\times 2$ matrix ${T}$ such that

$$


[\begin{aligned}𝑥 \\ 𝑦\end{aligned}]


$$

Notice that

$$


[\begin{aligned}−5 & 4 \\ 3 & 1\end{aligned}]


$$

Therefore, the matrix which represents the linear transformation $\mathbf{T}$ is

$$


[\begin{aligned}−5 & 4 \\ 3 & 1\end{aligned}]


$$
