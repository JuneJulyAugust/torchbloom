# Introduction to Linear Transformations

Source: https://www.mathacademy.com/topics/865?courseId=101
Topic ID: 865

## Prerequisites

- [Addition and Scalar Multiplication of Cartesian Vectors in 3D](./175-addition-and-scalar-multiplication-of-cartesian-vectors-in-3d.md)
- [The Power of Product Rule With Algebraic Expressions](../../../traditional/lessons/algebra-i/1331-the-power-of-product-rule-with-algebraic-expressions.md)

## Lesson

### Introduction

Consider the function $f(x),$ defined as

$$


f(x) = 2x+1.


$$

This function $f$ takes a real number $x$ as input, and it outputs a real number. We can describe this fact using the following notation:

$$


f: x \longrightarrow 2x+1


$$

Similarly, we can define a function $\mathbf T,$ also called a **transformation** or a **map**, that takes a 2D-vector (or 3D-vector) as input and outputs a new 2D-vector (or, respectively, 3D-vector).

For example, let's consider the following transformation:

$$


[\begin{aligned}𝑥 \\ 𝑦\end{aligned}]


$$

This means that for any 2D-vector $[\begin{aligned}𝑥 \\ 𝑦\end{aligned}]$ the corresponding image $[\begin{aligned}𝑥 \\ 𝑦\end{aligned}]$ under the action of $\mathbf{T}$ can be found as follows:

$$


[\begin{aligned}𝑥 \\ 𝑦\end{aligned}]


$$

We can evaluate this transformation just like we would with any other function. For example, applying the transformation $\mathbf{T}$ to the input vector $[\begin{aligned}𝑥 \\ 𝑦\end{aligned}]$ we get

$$


\begin{aligned}𝐓[\begin{aligned}−1 \\ 3\end{aligned}]=[\begin{aligned}−1+3 \\ 2⋅3\end{aligned}]=[\begin{aligned}2 \\ 6\end{aligned}].\end{aligned}


$$

We say that the transformation $\mathbf T$ *maps* the input vector $[\begin{aligned}−1 \\ 3\end{aligned}]$ to the output vector $[\begin{aligned}2 \\ 6\end{aligned}]$

### Linear Transformations

A transformation $\mathbf{T}$ is called a **linear transformation** (or **linear map**) if the following two properties are satisfied:

1. $\mathbf{T}(k\mathbf{v})=k\mathbf{T}(\mathbf{v})$ for any vector $\mathbf{v}$ and any scalar $k$

2. $\mathbf{T}(\mathbf{v}_1+\mathbf{v}_2)=\mathbf{T}(\mathbf{v}_1)+\mathbf{T}(\mathbf{v}_2)$ for any vectors $\mathbf{v}_1$ and $\mathbf{v}_2$

If we let $[\begin{aligned}𝑥 \\ 𝑦\end{aligned}]$ $[\begin{aligned}𝑥_{1} \\ 𝑦_{1}\end{aligned}]$ $[\begin{aligned}𝑥_{2} \\ 𝑦_{2}\end{aligned}]$ then the conditions above can be written as follows:

1. $[\begin{aligned}𝑘𝑥 \\ 𝑘𝑦\end{aligned}]$

2. $[\begin{aligned}𝑥_{1}+𝑥_{2} \\ 𝑦_{1}+𝑦_{2}\end{aligned}]$

We can determine whether the transformation $[\begin{aligned}𝑥 \\ 𝑦\end{aligned}]$ is linear by checking if these two conditions are true.

- Checking the first condition, we have

- Checking the second condition, we have

Both conditions are satisfied, so this transformation is linear.

### Example: Determining the Image of a Vector Under a Map Using the Scalar Multiplication Property

#### Question

If $\mathbf{T}$ is a linear transformation and $[\begin{aligned}12 \\ 24\end{aligned}]$ then find $[\begin{aligned}2 \\ 4\end{aligned}]$

#### Explanation

Since $\mathbf{T}$ is a linear transformation, it must satisfy $\mathbf{T}(k\mathbf{v})=k\mathbf{T}(\mathbf{v}).$ Noting that $[\begin{aligned}12 \\ 24\end{aligned}]$ we have

$$


\begin{aligned}𝐓([\begin{aligned}12 \\ 24\end{aligned}]) & =𝐓(6[\begin{aligned}2 \\ 4\end{aligned}])=6𝐓([\begin{aligned}2 \\ 4\end{aligned}]).\end{aligned}


$$

Now, since we're told that

$$


[\begin{aligned}12 \\ 24\end{aligned}]


$$

we must have

$$


\begin{aligned}6𝐓([\begin{aligned}2 \\ 4\end{aligned}]) & =[\begin{aligned}18 \\ −30\end{aligned}] \\ 𝐓([\begin{aligned}2 \\ 4\end{aligned}]) & =\frac{1}{6}[\begin{aligned}18 \\ −30\end{aligned}] \\ 𝐓([\begin{aligned}2 \\ 4\end{aligned}]) & =[\begin{aligned}3 \\ −5\end{aligned}].\end{aligned}


$$

### Example: Determining the Image of a Vector Under a Map Using Vector Addition and Scalar Multiplication

#### Question

Consider a linear transformation $\mathbf{T}.$ If $[\begin{aligned}−18 \\ 24\end{aligned}]$ and $[\begin{aligned}14 \\ −12\end{aligned}]$ then find $\mathbf{T}(\mathbf{v}_1).$

#### Explanation

Since $\mathbf{T}$ is a linear transformation, we have that

$$


\begin{aligned}𝐓(𝑘𝐯+𝐰)=𝐓(𝑘𝐯)+𝐓(𝐰)=𝑘𝐓(𝐯)+𝐓(𝐰)\end{aligned}


$$

for any vectors $\mathbf{v}$ and $\mathbf{w}.$ Therefore,

$$


\begin{aligned}𝐓(4𝐯_{1}+𝐯_{2}) & =4𝐓(𝐯_{1})+𝐓(𝐯_{2}) \\ [\begin{aligned}−18 \\ 24\end{aligned}] & =4𝐓(𝐯_{1})+[\begin{aligned}14 \\ −12\end{aligned}] \\ 4𝐓(𝐯_{1}) & =[\begin{aligned}−18 \\ 24\end{aligned}]−[\begin{aligned}14 \\ −12\end{aligned}] \\ 4𝐓(𝐯_{1}) & =[\begin{aligned}−32 \\ 36\end{aligned}] \\ 𝐓(𝐯_{1}) & =\frac{1}{4}[\begin{aligned}−32 \\ 36\end{aligned}] \\ 𝐓(𝐯_{1}) & =[\begin{aligned}−8 \\ 9\end{aligned}].\end{aligned}


$$

### Example: Determining the Image of a Vector Sum Under a Map Using Vector Addition and Scalar Multiplication

#### Question

Consider a linear transformation $\mathbf{T}.$ If $\mathbf{v}_1 + \mathbf{v}_2=\mathbf{0}$ and $\begin{aligned}9 \\ −12 \\ 8\end{aligned}$ then find $\mathbf{T}(17\mathbf{v}_1+12\mathbf{v}_2).$

#### Explanation

First, since $\mathbf{v}_1 + \mathbf{v}_2=\mathbf{0},$ we have that

$$


\begin{aligned}17𝐯_{1}+12𝐯_{2} & =5𝐯_{1}+12𝐯_{1}+12𝐯_{2} \\ & =5𝐯_{1}+12(𝐯_{1}+𝐯_{2}) \\ & =5𝐯_{1}+12(𝟎) \\ & =5𝐯_{1}.\end{aligned}


$$

Therefore, we have

$$


\mathbf{T}(17\mathbf{v}_1+12\mathbf{v}_2)=\mathbf{T}(5\mathbf{v}_1).


$$

Now, since $\mathbf{T}$ is a linear transformation, we have that $\mathbf{T}(k\mathbf{v})=k\mathbf{T}(\mathbf{v}).$ So

$$


\begin{aligned}𝐓(5𝐯_{1}) & =5𝐓(𝐯_{1}) \\ & =5\begin{aligned}9 \\ −12 \\ 8\end{aligned} \\ & =\begin{aligned}45 \\ −60 \\ 40\end{aligned}.\end{aligned}


$$

In conclusion, $\begin{aligned}45 \\ −60 \\ 40\end{aligned}$

### Example: Identifying Linear Transformations

#### Question

Are the following transformations linear?

$$


[\begin{aligned}𝑥 \\ 𝑦\end{aligned}]


$$

#### Explanation

A linear transformation $\mathbf{T}$ satisfies two properties:

$$


\begin{aligned} & 𝐓[\begin{aligned}𝑘𝑥 \\ 𝑘𝑦\end{aligned}]=𝑘𝐓[\begin{aligned}𝑥 \\ 𝑦\end{aligned}], \\ & 𝐓[\begin{aligned}𝑥_{1}+𝑥_{2} \\ 𝑦_{1}+𝑦_{2}\end{aligned}]=𝐓[\begin{aligned}𝑥_{1} \\ 𝑦_{1}\end{aligned}]+𝐓[\begin{aligned}𝑥_{2} \\ 𝑦_{2}\end{aligned}].\end{aligned}


$$

First, let's consider $\mathbf{T}_1.$ Checking the first condition, we have

$$


\begin{aligned}𝐓_{1}[\begin{aligned}𝑘𝑥 \\ 𝑘𝑦\end{aligned}] & =[\begin{aligned}(𝑘𝑥)^{2} \\ (𝑘𝑥)(𝑘𝑦)\end{aligned}] \\ & =[\begin{aligned}𝑘^{2}𝑥^{2} \\ 𝑘^{2}𝑥𝑦\end{aligned}] \\ & =𝑘[\begin{aligned}𝑘𝑥^{2} \\ 𝑘𝑥𝑦\end{aligned}] \\ & ≠𝑘𝐓_{1}[\begin{aligned}𝑥 \\ 𝑦\end{aligned}].\,×\end{aligned}


$$

Therefore, $\textbf{T}_1$ is not a linear transformation.

Now, let's consider $\mathbf{T}_2.$

- Checking the first condition, we have

- Checking the second condition, we have

Therefore, $\textbf{T}_2$ is a linear transformation.
