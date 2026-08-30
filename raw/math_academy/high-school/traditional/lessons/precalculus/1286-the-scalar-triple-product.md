# The Scalar Triple Product

Source: https://www.mathacademy.com/topics/1286?courseId=43
Topic ID: 1286

## Prerequisites

- [Calculating the Cross Product Using Determinants](./245-calculating-the-cross-product-using-determinants.md)

## Lesson

### Introduction

The **scalar triple product** of three vectors $\mathbf{a},$ $\mathbf{b},$ and $\mathbf{c}$ is defined as $\mathbf{a} \cdot (\mathbf{b} \times \mathbf{c}).$

For example, suppose we have three vectors $\mathbf{a} = \langle -1,2,1 \rangle,$ $\mathbf{b} = \langle 1,1,-2 \rangle,$ and $\mathbf{c} = \langle 0,3,1 \rangle.$ Let's compute their scalar triple product, $\mathbf{a} \cdot (\mathbf{b} \times \mathbf{c}).$

First, we find the cross product:

$$



\begin{aligned}𝐛×𝐜 & =\begin{matrix}𝐢 & 𝐣 & 𝐤 \\ 𝑏_{1} & 𝑏_{2} & 𝑏_{3} \\ 𝑐_{1} & 𝑐_{2} & 𝑐_{3}\end{matrix} \\ & =\begin{matrix}𝐢 & 𝐣 & 𝐤 \\ 1 & 1 & −2 \\ 0 & 3 & 1\end{matrix} \\ & =\begin{matrix}1 & −2 \\ 3 & 1\end{matrix}𝐢−\begin{matrix}1 & −2 \\ 0 & 1\end{matrix}𝐣+\begin{matrix}1 & 1 \\ 0 & 3\end{matrix}𝐤 \\ & =(1⋅1−(−2)⋅3)𝐢−(1⋅1−(−2)⋅0)𝐣+(1⋅3−1⋅0)𝐤 \\ & =7𝐢−𝐣+3𝐤 \\ & =⟨7,−1,3⟩\end{aligned}



$$

Now, we can compute the scalar triple product:

$$



\begin{aligned}𝐚⋅(𝐛×𝐜) & =⟨−1,2,1⟩⋅⟨7,−1,3⟩ \\ & =(−1)⋅7+2⋅(−1)+1⋅3 \\ & =−6\end{aligned}



$$

**Note:** The scalar triple product takes its name from the fact that it multiplies three vectors together and always results in a scalar.

Later, we will learn some geometric intuition behind the scalar triple product. But for now, we will focus on computing the scalar triple product.

### Example: Calculating the Scalar Triple Product Using the Definition

#### Question

Let $\mathbf{a}=\langle 2,-3,2 \rangle,$ $\mathbf{b}=\langle -1,0,5 \rangle,$ and $\mathbf{c}=\langle 1,2,3 \rangle.$ Find $\mathbf{a} \cdot (\mathbf{b} \times \mathbf{c}).$

#### Explanation

First, we find the cross product:

$$



\begin{aligned}𝐛×𝐜 & =\begin{matrix}𝐢 & 𝐣 & 𝐤 \\ −1 & 0 & 5 \\ 1 & 2 & 3\end{matrix} \\ & =\begin{matrix}0 & 5 \\ 2 & 3\end{matrix}𝐢−\begin{matrix}−1 & 5 \\ 1 & 3\end{matrix}𝐣+\begin{matrix}−1 & 0 \\ 1 & 2\end{matrix}𝐤 \\ & =(0⋅3−5⋅2)𝐢−(−1⋅3−5⋅1)𝐣+(−1⋅2−0⋅2)𝐤 \\ & =−10𝐢+8𝐣−2𝐤 \\ & =⟨−10,8,−2⟩\end{aligned}



$$

Now, we can compute the scalar triple product:

$$



\begin{aligned}𝐚⋅(𝐛×𝐜) & =⟨2,−3,2⟩⋅⟨−10,8,−2⟩ \\ & =2⋅(−10)+(−3)⋅8+2⋅(−2) \\ & =−48\end{aligned}



$$

### The Definition of the Scalar Triple Product Via the Determinant

It turns out that the scalar triple product $\mathbf{a} \cdot (\mathbf{b} \times \mathbf{c})$ is just the determinant of the matrix whose rows are given by $\mathbf{a},$ $\mathbf{b},$ and $\mathbf{c}.$

That is to say, if $\mathbf{a} = \langle a_1,a_2,a_3 \rangle,$ $\mathbf{b} = \langle b_1,b_2,b_3 \rangle,$ and $\mathbf{c} = \langle c_1,c_2,c_3 \rangle,$ then

$$



\begin{aligned}𝐚⋅(𝐛×𝐜)=\begin{matrix}𝑎_{1} & 𝑎_{2} & 𝑎_{3} \\ 𝑏_{1} & 𝑏_{2} & 𝑏_{3} \\ 𝑐_{1} & 𝑐_{2} & 𝑐_{3}\end{matrix}.\end{aligned}



$$

A proof of this result will be given at the end of the lesson. But for now, let's focus on computing the scalar triple product using the determinant above.

### Example: Calculating the Scalar Triple Product Using a Determinant

#### Question

Let $\mathbf{a}=\langle 4,2,-1 \rangle,$ $\mathbf{b}=\langle 0,2,1 \rangle,$ and $\mathbf{c}=\langle -1,-1,2 \rangle.$ Find $\mathbf{a} \cdot (\mathbf{b} \times \mathbf{c}).$

#### Explanation

Remember that the scalar triple product $\mathbf{a} \cdot (\mathbf{b} \times \mathbf{c})$ is just the determinant of the matrix whose rows are given by $\mathbf{a},$ $\mathbf{b},$ and $\mathbf{c}.$

So, we have

$$



\begin{aligned}𝐚⋅(𝐛×𝐜) & =\begin{matrix}4 & 2 & −1 \\ 0 & 2 & 1 \\ −1 & −1 & 2\end{matrix} \\ & =4⋅\begin{matrix}2 & 1 \\ −1 & 2\end{matrix}−2⋅\begin{matrix}0 & 1 \\ −1 & 2\end{matrix}+(−1)⋅\begin{matrix}0 & 2 \\ −1 & −1\end{matrix} \\ & =4⋅(2⋅2−1⋅(−1))−2⋅(0⋅2−1⋅(−1))+(−1)⋅(0⋅(−1)−2⋅(−1)) \\ & =20−2−2 \\ & =16.\end{aligned}



$$

### Properties of the Scalar Triple Product

The scalar triple product has two important properties.

First, scalars can be factored out of the product. For example,

$$



({\color{red}2}\mathbf{a}) \cdot (\mathbf{b} \times \mathbf{c}) = \mathbf{a} \cdot ({\color{red}2}\mathbf{b} \times \mathbf{c}) = \mathbf{a} \cdot (\mathbf{b} \times {\color{red}2}\mathbf{c}) = {\color{red}2}\left[ \mathbf{a} \cdot (\mathbf{b} \times \mathbf{c})\right].



$$

Second, if we swap exactly two vectors in the scalar triple product, the result changes sign. For example, swapping $\mathbf{a}$ and $\mathbf{b},$ we have

$$



{\color{red}\mathbf{a}} \cdot ( {\color{blue}\mathbf{b}} \times \mathbf{c}) = - {\color{blue}\mathbf{b}} \cdot ( {\color{red}\mathbf{a}} \times \mathbf{c}).



$$

Note that if we swap twice, then the result remains the same, because the negatives cancel out. For example, swapping $\color{red}\mathbf{a}$ and $\color{blue}\mathbf{b}$ and then swapping $\color{red}\mathbf{a}$ and $\mathbf{c},$ we get

$$



\begin{aligned}𝐚⋅(𝐛×𝐜) & =−𝐛⋅(𝐚×𝐜) \\ & =−(−𝐛⋅(𝐜×𝐚)) \\ & =𝐛⋅(𝐜×𝐚).\end{aligned}



$$

These properties arise naturally from the fact that the scalar triple product can be computed as a determinant.

1. If we multiply a row of the matrix by a number, then the determinant is multiplied by that number:

2. If we swap two rows, then the determinant changes sign:

### Example: Calculating Scalar Triple Products Using Its Properties

#### Question

Find $\mathbf{c} \cdot (\mathbf{a} \times \mathbf{b}),$ if $2\mathbf{a} \cdot (\mathbf{b} \times 3\mathbf{c}) = 5.$

#### Explanation

First, we factor out the constants and get

$$



\begin{aligned}2𝐚⋅(𝐛×3𝐜) & =5 \\ 2⋅[𝐚⋅(𝐛×3𝐜)] & =5 \\ 2⋅3⋅[𝐚⋅(𝐛×𝐜)] & =5 \\ 𝐚⋅(𝐛×𝐜) & =\frac{5}{6}.\end{aligned}



$$

Then, we swap $\mathbf{a}$ and $\mathbf{c}$ to get

$$



\begin{aligned}𝐜⋅(𝐛×𝐚) & =−\frac{5}{6},\end{aligned}



$$

and again we swap $\mathbf{a}$ and $\mathbf{b}$ to get

$$



\begin{aligned}𝐜⋅(𝐚×𝐛) & =\frac{5}{6}.\end{aligned}



$$

### A Proof of the Formula for the Scalar Triple Product

We have been using the fact for three vectors $\mathbf{a} = \langle a_1,a_2,a_3 \rangle,$ $\mathbf{b} = \langle b_1,b_2,b_3 \rangle,$ and $\mathbf{c} = \langle c_1,c_2,c_3 \rangle,$ the scalar triple product can be computed as

$$



\begin{aligned}𝐚⋅(𝐛×𝐜)=\begin{matrix}𝑎_{1} & 𝑎_{2} & 𝑎_{3} \\ 𝑏_{1} & 𝑏_{2} & 𝑏_{3} \\ 𝑐_{1} & 𝑐_{2} & 𝑐_{3}\end{matrix}.\end{aligned}



$$

But why is this true? To understand where this result comes from, first notice that in the formula for the triple product, the cross product can be expressed as follows:

$$



\begin{aligned}𝐛×𝐜 & =\begin{matrix}𝐢 & 𝐣 & 𝐤 \\ 𝑏_{1} & 𝑏_{2} & 𝑏_{3} \\ 𝑐_{1} & 𝑐_{2} & 𝑐_{3}\end{matrix} \\ & =\begin{matrix}𝑏_{2} & 𝑏_{3} \\ 𝑐_{2} & 𝑐_{3}\end{matrix}𝐢−\begin{matrix}𝑏_{1} & 𝑏_{3} \\ 𝑐_{1} & 𝑐_{3}\end{matrix}𝐣+\begin{matrix}𝑏_{1} & 𝑏_{2} \\ 𝑐_{1} & 𝑐_{2}\end{matrix}𝐤\end{aligned}



$$

Now, when we take the dot product with $\mathbf{a},$ we get an expression that is just the cofactor expansion across the first row of the matrix:

$$



\begin{aligned}𝐚⋅(𝐛×𝐜) & =(𝑎_{1}𝐢+𝑎_{2}𝐣+𝑎_{3}𝐤)⋅(\begin{matrix}𝑏_{2} & 𝑏_{3} \\ 𝑐_{2} & 𝑐_{3}\end{matrix}𝐢−\begin{matrix}𝑏_{1} & 𝑏_{3} \\ 𝑐_{1} & 𝑐_{3}\end{matrix}𝐣+\begin{matrix}𝑏_{1} & 𝑏_{2} \\ 𝑐_{1} & 𝑐_{2}\end{matrix}𝐤) \\ & =𝑎_{1}\begin{matrix}𝑏_{2} & 𝑏_{3} \\ 𝑐_{2} & 𝑐_{3}\end{matrix}−𝑎_{2}\begin{matrix}𝑏_{1} & 𝑏_{3} \\ 𝑐_{1} & 𝑐_{3}\end{matrix}+𝑎_{3}\begin{matrix}𝑏_{1} & 𝑏_{2} \\ 𝑐_{1} & 𝑐_{2}\end{matrix} \\ & =\begin{matrix}𝑎_{1} & 𝑎_{2} & 𝑎_{3} \\ 𝑏_{1} & 𝑏_{2} & 𝑏_{3} \\ 𝑐_{1} & 𝑐_{2} & 𝑐_{3}\end{matrix}\end{aligned}



$$
