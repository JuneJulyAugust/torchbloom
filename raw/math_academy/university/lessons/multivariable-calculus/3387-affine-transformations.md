# Affine Transformations

Source: https://www.mathacademy.com/topics/3387?courseId=54
Topic ID: 3387

## Prerequisites

- [The Standard Matrix of a Linear Transformation](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/1959-the-standard-matrix-of-a-linear-transformation.md)
- [Sets and Functions](../linear-algebra/3334-sets-and-functions.md)

## Lesson

### Introduction

An **affine transformation** $\mathbf T:\mathbb R^2\rightarrow\mathbb R^2$ is a function that can be expressed in the form

$$


\mathbf x = A \mathbf u + \mathbf b,


$$

where $\mathbf x, \mathbf u,$ and $\mathbf b$ are column vectors in $\mathbb R^2,$ and $A$ is a $2\times 2$ matrix.

Under this notation,

- $[\begin{aligned}𝑢 \\ 𝑣\end{aligned}]$ represents vectors belonging to the input space, and

- $[\begin{aligned}𝑥 \\ 𝑦\end{aligned}]$ represents vectors belonging to the output space.

For example,

$$


[\begin{aligned}𝑢 \\ 𝑣\end{aligned}]


$$

is an affine transformation because it can be expressed in the form $\mathbf x = A\mathbf u + \mathbf b,$ as follows:

$$


\begin{aligned}[\begin{matrix}𝑥 \\ 𝑦\end{matrix}] & =[\begin{matrix}𝑢−𝑣+1 \\ 2𝑢+𝑣−3\end{matrix}] \\ & =[\begin{matrix}𝑢−𝑣 \\ 2𝑢+𝑣\end{matrix}]+[\begin{matrix}1 \\ −3\end{matrix}] \\ & =\underset{𝐴}{\underset{}{[\begin{matrix}1 & −1 \\ 2 & 1\end{matrix}]}}⋅\underset{𝐮}{\underset{}{[\begin{matrix}𝑢 \\ 𝑣\end{matrix}]}}+\underset{𝐛}{\underset{}{[\begin{matrix}1 \\ −3\end{matrix}]}}\end{aligned}


$$

However, the transformation

$$


[\begin{aligned}𝑢 \\ 𝑣\end{aligned}]


$$

is not affine since it contains the quadratic term $uv.$

Finally, note the following relationships between affine and linear transformations:

- A linear transformation $\mathbf x = A \mathbf u$ is a special case of an affine transformation with $\mathbf b = \mathbf 0.$

- For an affine transformation $\mathbf T$ given by $\mathbf x = A\mathbf u + \mathbf b,$ we say that $A$ is *the matrix representation of the linear transformation associated with* $\mathbf T.$

### Example: Identifying Affine Transformations

#### Question

Which of the following are affine transformations?

1. $[\begin{aligned}𝑢 \\ 𝑣\end{aligned}]$

2. $[\begin{aligned}𝑢 \\ 𝑣\end{aligned}]$

3. $[\begin{aligned}𝑢 \\ 𝑣\end{aligned}]$

#### Explanation

An affine transformation $\mathbf T:\mathbb R^2\rightarrow\mathbb R^2$ is a function of the form

$$


\mathbf x = A \mathbf u + \mathbf b,


$$

where $\mathbf x, \mathbf u,$ and $\mathbf b$ are column vectors in $\mathbb R^2,$ and $A$ is a $2\times 2$ matrix.

With this in mind, let's look at each transformation in turn.

- Transformation $\mathbf{T}_1$ is affine. Notice that $\mathbf{T}_1$ can be expressed as

- Transformation $\mathbf{T}_2$ is affine. Notice that $\mathbf{T}_2$ can be expressed as In fact, the transformation $\mathbf{T}_2$ is a linear transformation.

- Transformation $\mathbf{T}_3$ is not affine since it contains the quadratic term $v^2.$

Therefore, the correct answer is "$\mathbf{T}_1$ and $\mathbf{T}_2$ only."

### Example: Finding the Parametric Representation of an Affine Transformation Given its Matrix Form

#### Question

The matrix form of the affine transformation

$$


x = 3u-v + \boxed{a}, \qquad y = u + \boxed{b}v + \boxed{c}


$$

is shown below. What is the value of $a+b+c?$

$$


[\begin{aligned}𝑥 \\ 𝑦\end{aligned}]


$$

#### Explanation

An affine transformation $\mathbf T:\mathbb R^2\rightarrow\mathbb R^2$ is a function of the form

$$


\mathbf x = A \mathbf u + \mathbf b,


$$

where $\mathbf x, \mathbf u,$ and $\mathbf b$ are column vectors in $\mathbb R^2,$ and $A$ is a $2\times 2$ matrix.

We can carry out the matrix operations using the matrix form, as follows:

$$


\begin{aligned}[\begin{matrix}𝑥 \\ 𝑦\end{matrix}] & =\overset{[\begin{matrix}3 & −1 \\ 1 & −5\end{matrix}]}{}}{𝐴}⋅\overset{[\begin{matrix}𝑢 \\ 𝑣\end{matrix}]}{}}{𝐮}+\overset{[\begin{matrix}1 \\ 0\end{matrix}]}{}}{𝐛} \\ & =[\begin{matrix}3𝑢−𝑣 \\ 𝑢−5𝑣\end{matrix}]+[\begin{matrix}1 \\ 0\end{matrix}] \\ & =[\begin{matrix}3𝑢−𝑣+1 \\ 𝑢−5𝑣\end{matrix}]\end{aligned}


$$

Equating the corresponding elements, we obtain

$$


x = 3u - v + \boxed{1}, \qquad y = u + (\boxed{-5})v + \boxed{0} \, .


$$

Therefore, we have

$$


a+b+c = 1+(-5)+0 = -4.


$$

### Example: Finding the Matrix Representation of an Affine Transformation Given its Parametric Form

#### Question

The matrix form of the affine transformation

$$


x = 5u + v - 6, \qquad y = 2u + 4v


$$

is shown below. What is the value of $a+b+c?$

$$


[\begin{aligned}𝑥 \\ 𝑦\end{aligned}]


$$

#### Explanation

An affine transformation $\mathbf T:\mathbb R^2\rightarrow\mathbb R^2$ is a function of the form

$$


\mathbf x = A \mathbf u + \mathbf b,


$$

where $\mathbf x, \mathbf u,$ and $\mathbf b$ are column vectors in $\mathbb R^2,$ and $A$ is a $2\times 2$ matrix.

First, notice that we can express the given transformation as

$$


[\begin{aligned}𝑥 \\ 𝑦\end{aligned}]


$$

Separating the constants and expressing the linear part as a product, we get

$$


\begin{aligned}[\begin{matrix}𝑥 \\ 𝑦\end{matrix}] & =[\begin{matrix}5𝑢+𝑣−6 \\ 2𝑢+4𝑣\end{matrix}] \\ & =[\begin{matrix}5𝑢+𝑣 \\ 2𝑢+4𝑣\end{matrix}]+[\begin{matrix}−6 \\ 0\end{matrix}] \\ & =\underset{𝐴}{\underset{}{[\begin{matrix}5 & 1 \\ 2 & 4\end{matrix}]}}⋅\underset{𝐮}{\underset{}{[\begin{matrix}𝑢 \\ 𝑣\end{matrix}]}}+\underset{𝐛}{\underset{}{[\begin{matrix}−6 \\ 0\end{matrix}]}}.\end{aligned}


$$

Therefore, we have

$$


a+b+c = 1+2+0 = 3.


$$
