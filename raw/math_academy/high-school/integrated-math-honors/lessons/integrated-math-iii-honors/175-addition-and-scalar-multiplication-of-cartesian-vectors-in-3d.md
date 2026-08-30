# Addition and Scalar Multiplication of Cartesian Vectors in 3D

Source: https://www.mathacademy.com/topics/175?courseId=101
Topic ID: 175

## Prerequisites

- [Addition and Scalar Multiplication of Cartesian Vectors in 2D](./244-addition-and-scalar-multiplication-of-cartesian-vectors-in-2d.md)
- [Three-Dimensional Vectors in Component Form](./1166-three-dimensional-vectors-in-component-form.md)

## Lesson

### Introduction

Suppose we are given two vectors $\mathbf{a}$ and $\mathbf{b},$ where

$$


\begin{aligned} & 𝐚=7𝐢+3𝐣+5𝐤,\, & 𝐛=−2𝐢+5𝐣+3𝐤.\end{aligned}


$$

How do we compute the vectors $\mathbf{a} + \mathbf{b}$ and $3\mathbf{a}?$

To add the vectors together, we add their components:

$$


\begin{aligned}𝐚+𝐛 & =(7𝐢+3𝐣+5𝐤)+(−2𝐢+5𝐣+3𝐤) \\ & =(7+(−2))𝐢+(3+5)𝐣+(5+3)𝐤 \\ & =5𝐢+8𝐣+8𝐤\end{aligned}


$$

Similarly, to compute $3\cdot\mathbf{a},$ we multiply each component of $\mathbf{a}$ by $3\mathbin{:}$

$$


\begin{aligned}3⋅𝐚 & =3⋅(7𝐢+3𝐣+5𝐤) \\ & =(3⋅7)𝐢+(3⋅3)𝐣+(3⋅5)𝐤 \\ & =21\,𝐢+9\,𝐣+15\,𝐤\end{aligned}


$$

### Sums and Scalar Multiplication of Vectors in Angle Bracket or Column Vector Form

To add or subtract vectors given in angle bracket or column vector form, we just need to add or subtract each component separately.

For example, in angle bracket notation, we have

$$


\begin{aligned}⟨7,\,3,\,5⟩+⟨−2,\,5,\,3⟩ & = \\ ⟨7+(−2),\,3+5,\,5+3⟩ & = \\ ⟨5,\,8,\,8⟩, & \end{aligned}


$$

and in column vector notation, we have

$$


\begin{aligned}\begin{matrix}7 \\ 3 \\ 5\end{matrix}+\begin{matrix}−2 \\ 5 \\ 3\end{matrix}=\begin{matrix}7+(−2) \\ 3+5 \\ 5+3\end{matrix}=\begin{matrix}5 \\ 8 \\ 8\end{matrix}.\end{aligned}


$$

Likewise, to multiply a vector given in angle bracket or column vector form, we just need to multiply each component separately.

For example, in angle bracket notation, we have

$$


\begin{aligned}3⋅⟨7, 3, 5⟩ & = \\ ⟨3⋅7, 3⋅3, 3⋅5⟩ & = \\ ⟨21, 9, 15⟩ & ,\end{aligned}


$$

and in column vector notation, we have

$$


\begin{aligned}3⋅\begin{matrix}7 \\ 3 \\ 5\end{matrix}=\begin{matrix}3⋅7 \\ 3⋅3 \\ 3⋅5\end{matrix}=\begin{matrix}21 \\ 9 \\ 15\end{matrix}.\end{aligned}


$$

### Example: Calculating Sums and Differences of Vectors

#### Question

Let $\mathbf{a}=\langle 2, -5, 1 \rangle$ and $\mathbf{b}=\langle 2, 0, -4 \rangle.$ Find $\mathbf{a}-\mathbf{b}.$

#### Explanation

To compute the difference, we just subtract each component individually:

$$


\begin{aligned}𝐚−𝐛 & =⟨2,−5,1⟩−⟨2,0,−4⟩ \\ & =⟨2−2,−5−0,1−(−4)⟩ \\ & =⟨0,−5,5⟩\end{aligned}


$$

### Example: Calculating Scalar Multiplication of Vectors

#### Question

Given that $\mathbf{a}=\langle -3, 2, 1 \rangle$, find $-2\mathbf{a}.$

#### Explanation

To compute the product, we just multiply each component individually:

$$


\begin{aligned}−2𝐚 & =−2⋅⟨−3,2,1⟩ \\ & =⟨−2⋅(−3),−2⋅2,−2⋅1⟩ \\ & =⟨6,−4,−2⟩\end{aligned}


$$

### Example: Calculating Sums and Scalar Multiplication of Vectors

#### Question

Let $\mathbf{a}=\langle -4, 5, 1 \rangle$ and $\mathbf{b}=\langle 4, 1, -3 \rangle$. Find $3\mathbf{a}+2\mathbf{b}$.

#### Explanation

To compute $3\mathbf{a}+2\mathbf{b},$ we just need to perform the required operations with each component separately:

$$


\begin{aligned}3𝐚+2𝐛 & =3⋅⟨−4,5,1⟩+2⋅⟨4,1,−3⟩ \\ & =⟨−12,15,3⟩+⟨8,2,−6⟩ \\ & =⟨−4,17,−3⟩\end{aligned}


$$

### Example: Calculating Sums and Scalar Multiplication of More Than Two Vectors

#### Question

Let $\begin{aligned}3 \\ 1 \\ −2\end{aligned}$ $\begin{aligned}1 \\ 1 \\ −1\end{aligned}$ and $\begin{aligned}−1 \\ 2 \\ 4\end{aligned}$ Find $\mathbf{a}-(\mathbf{b}-\mathbf{c}).$

#### Explanation

To compute $\mathbf{a}-(\mathbf{b}-\mathbf{c}),$ we just need to perform the required operations with each component separately:

$$


\begin{aligned}𝐚−(𝐛−𝐜) & =\begin{matrix}3 \\ 1 \\ −2\end{matrix}−\begin{matrix}1 \\ 1 \\ −1\end{matrix}−\begin{matrix}−1 \\ 2 \\ 4\end{matrix} \\ & =\begin{matrix}3 \\ 1 \\ −2\end{matrix}−\begin{matrix}2 \\ −1 \\ −5\end{matrix} \\ & =\begin{matrix}1 \\ 2 \\ 3\end{matrix}\end{aligned}


$$
