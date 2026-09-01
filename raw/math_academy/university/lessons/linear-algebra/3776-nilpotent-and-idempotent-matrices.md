# Nilpotent and Idempotent Matrices

Source: https://www.mathacademy.com/topics/3776?courseId=55
Topic ID: 3776

## Prerequisites

- [Powers of Matrices](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/1725-powers-of-matrices.md)

## Lesson

### Introduction

A matrix is said to be **nilpotent** if some positive power of the matrix is the zero matrix. For example, the matrix

$$


[\begin{aligned}0 & 1 \\ 0 & 0\end{aligned}]


$$

is nilpotent because its second power is the zero matrix:

$$


\begin{aligned}𝐵^{2} & =[\begin{matrix}0 & 1 \\ 0 & 0\end{matrix}][\begin{matrix}0 & 1 \\ 0 & 0\end{matrix}] \\ & =[\begin{matrix}0 & 0 \\ 0 & 0\end{matrix}] \\ & =𝑂\end{aligned}


$$

To state the definition more precisely: a matrix with the property $B^k=O$ for a number $k>0$ is known as a **nilpotent** matrix, and the lowest number $k$ such that $B^k=O$ is called the **index.**

Therefore, our matrix $B$ is a nilpotent matrix of index $2.$

### Example: Finding a Power of a Nilpotent Matrix

#### Question

Find $B^2$ given that $[\begin{aligned}3 & 9 \\ −1 & −3\end{aligned}]$

#### Explanation

Computing $B^2,$ we have

$$


\begin{aligned}𝐵^{2} & =𝐵⋅𝐵 \\ & =[\begin{matrix}3 & 9 \\ −1 & −3\end{matrix}]⋅[\begin{matrix}3 & 9 \\ −1 & −3\end{matrix}] \\ & =[\begin{matrix}0 & 0 \\ 0 & 0\end{matrix}] \\ & =𝑂.\end{aligned}


$$

Notice that, since $B^2=O,$ the matrix $B$ is a nilpotent matrix of index $2.$

### Idempotent Matrices

A matrix is said to be **idempotent**, when multiplied by itself, yields itself.

For example, the matrix

$$


[\begin{aligned}3 & −6 \\ 1 & −2\end{aligned}]


$$

is idempotent because $B^2 = B$:

$$


\begin{aligned}𝐵^{2} & =[\begin{matrix}3 & −6 \\ 1 & −2\end{matrix}][\begin{matrix}3 & −6 \\ 1 & −2\end{matrix}] \\ & =[\begin{matrix}3⋅3+(−6)⋅1 & 3⋅(−6)+(−6)⋅(−2) \\ 1⋅3+(−2)⋅1 & 1⋅(−6)+(−2)⋅(−2)\end{matrix}] \\ & =[\begin{matrix}3 & −6 \\ 1 & −2\end{matrix}] \\ & =𝐵\end{aligned}


$$

### Example: Finding a Power of an Idempotent Matrix

#### Question

Find $C^5$ given that $\begin{aligned}\frac{1}{2} & 0 & \frac{1}{2} \\ 0 & 1 & 0 \\ \frac{1}{2} & 0 & \frac{1}{2}\end{aligned}$

#### Explanation

First, we compute $C^2$ as follows:

$$


\begin{aligned}𝐶^{2} & =𝐶⋅𝐶 \\ & =\begin{matrix}\frac{1}{2} & 0 & \frac{1}{2} \\ 0 & 1 & 0 \\ \frac{1}{2} & 0 & \frac{1}{2}\end{matrix}⋅\begin{matrix}\frac{1}{2} & 0 & \frac{1}{2} \\ 0 & 1 & 0 \\ \frac{1}{2} & 0 & \frac{1}{2}\end{matrix} \\ & =\begin{matrix}\frac{1}{2} & 0 & \frac{1}{2} \\ 0 & 1 & 0 \\ \frac{1}{2} & 0 & \frac{1}{2}\end{matrix} \\ & =𝐶\end{aligned}


$$

Notice that $C^2=C,$ so $C$ is an idempotent matrix.

We can use this fact to compute $C^5$ quickly, as follows:

$$


\begin{aligned}𝐶^{5} & =𝐶^{2}⋅𝐶^{2}⋅𝐶 \\ & =𝐶⋅𝐶⋅𝐶 \\ & =𝐶^{2}⋅𝐶 \\ & =𝐶⋅𝐶 \\ & =𝐶^{2} \\ & =𝐶\end{aligned}


$$

Therefore,

$$


\begin{aligned}\frac{1}{2} & 0 & \frac{1}{2} \\ 0 & 1 & 0 \\ \frac{1}{2} & 0 & \frac{1}{2}\end{aligned}


$$
