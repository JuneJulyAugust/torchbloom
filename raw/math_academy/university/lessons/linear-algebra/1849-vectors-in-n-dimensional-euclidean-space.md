# Vectors in N-Dimensional Euclidean Space

Source: https://www.mathacademy.com/topics/1849?courseId=55
Topic ID: 1849

## Prerequisites

- [Special Sets](./47-special-sets.md)
- [Addition and Scalar Multiplication of Cartesian Vectors in 3D](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/175-addition-and-scalar-multiplication-of-cartesian-vectors-in-3d.md)
- [Calculating the Dot Product Using Components](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/177-calculating-the-dot-product-using-components.md)
- [Solving Quadratic Equations by Factoring](../../../high-school/traditional/lessons/algebra-i/375-solving-quadratic-equations-by-factoring.md)
- [The Quadratic Formula](../../../high-school/traditional/lessons/algebra-i/422-the-quadratic-formula.md)

## Lesson

### Introduction

The **real coordinate space** (of dimension $n$) is the set of all possible column vectors of height $n,$ whose components are real numbers. Symbolically, we represent the real coordinate space of dimension $n$ as $\mathbb{R}^n.$

For example, the following vectors are in $\mathbb{R}, \mathbb{R}^2,$ $\mathbb{R}^3,$ and $\mathbb{R}^5,$ respectively:

$$


[\begin{aligned}\sqrt{4} \\ 0\end{aligned}]


$$

We've already encountered several operations on vectors in $\mathbb{R}^2$ or $\mathbb{R}^3,$ namely, vector addition and subtraction, scalar multiplication, and the dot product. All of these operations work the same way in $\mathbb{R}^n.$

### Example: Calculating a Multiple of a Vector

#### Question

Let $\begin{aligned}−4 \\ 6 \\ 3 \\ 0\end{aligned}$ Find $\dfrac{1}{2} \mathbf{a}.$

#### Explanation

Multiplying each component of $\mathbf{a}$ by $\dfrac{1}{2},$ we get

$$


\begin{aligned}\frac{1}{2}𝐚 & =\frac{1}{2}\begin{matrix}−4 \\ 6 \\ 3 \\ 0\end{matrix} \\ & =\begin{matrix}\frac{1}{2}⋅(−4) \\ \frac{1}{2}⋅6 \\ \frac{1}{2}⋅3 \\ \frac{1}{2}⋅0\end{matrix} \\ & =\begin{matrix}−2 \\ 3 \\ \frac{3}{2} \\ 0\end{matrix}.\end{aligned}


$$

### Adding Two Vectors

To add two vectors in $\mathbb{R}^n,$ we just need to add their corresponding components. To illustrate, consider the vectors $\mathbf{a},\mathbf{b} \in \mathbb{R}^4,$ given by

$$


\begin{aligned}5 \\ 1 \\ −3 \\ 6\end{aligned}


$$

To compute $\mathbf{a} + \mathbf{b},$ all we have to do is to add each component of the vector $\mathbf{a}$ with the corresponding component of $\mathbf{b}.$ Doing this, we get

$$


\begin{aligned}𝐚+𝐛 & =\begin{matrix}5 \\ 1 \\ −3 \\ 6\end{matrix}+\begin{matrix}−5 \\ 3 \\ 1 \\ 0\end{matrix} \\ & =\begin{matrix}5+(−5) \\ 1+3 \\ −3+1 \\ 6+0\end{matrix} \\ & =\begin{matrix}0 \\ 4 \\ −2 \\ 6\end{matrix}.\end{aligned}


$$

We can only compute the sum, difference, or dot product of two vectors if both vectors have the same number of components. For example, we can't find the following sum, so we say it's *undefined*:

$$


\begin{aligned}1 \\ 2 \\ 3\end{aligned}


$$

### Example: Adding Multiples of Vectors

#### Question

Let $\begin{aligned}−3 \\ 6 \\ 12 \\ −9 \\ 3\end{aligned}$ and $\begin{aligned}−4 \\ −6 \\ 2 \\ −8 \\ 10\end{aligned}$ Find $\dfrac{1}{3}\mathbf{a}+\dfrac{1}{2}\mathbf{b}.$

#### Explanation

First, we multiply each component of $\mathbf{a}$ by $\dfrac{1}{3}$ and each component of $\mathbf{b}$ by $\dfrac{1}{2}.$ Then, we add the vectors:

$$


\begin{aligned}\frac{1}{3}𝐚+\frac{1}{2}𝐛 & =\frac{1}{3}⋅\begin{matrix}−3 \\ 6 \\ 12 \\ −9 \\ 3\end{matrix}+\frac{1}{2}⋅\begin{matrix}−4 \\ −6 \\ 2 \\ −8 \\ 10\end{matrix} \\ & =\begin{matrix}−1 \\ 2 \\ 4 \\ −3 \\ 1\end{matrix}+\begin{matrix}−2 \\ −3 \\ 1 \\ −4 \\ 5\end{matrix} \\ & =\begin{matrix}−1−2 \\ 2−3 \\ 4+1 \\ −3−4 \\ 1+5\end{matrix} \\ & =\begin{matrix}−3 \\ −1 \\ 5 \\ −7 \\ 6\end{matrix}\end{aligned}


$$

### General Rules

In general, if we have two vectors $\mathbf{u},\mathbf{v}\in\mathbb{R}^n$ and a scalar $\lambda\in\mathbb{R},$ then our vector operations are defined as follows:

1. The **sum/difference** of the two vectors is defined as

2. **Scalar multiplication** of a vector is defined as

3. The **dot product** of two vectors is defined as

### Example: Calculating the Dot Product of Two Vectors

#### Question

If $\begin{aligned}−1 \\ 4 \\ 3 \\ −5\end{aligned}$ and $\begin{aligned}−2 \\ 3 \\ −4 \\ 6\end{aligned}$ then what is $\mathbf{u} \cdot \mathbf{v}?$

#### Explanation

To compute the dot product, we add up the products of corresponding components:

$$


\begin{aligned}𝐮⋅𝐯 & =𝑢_{1}⋅𝑣_{1}+𝑢_{2}⋅𝑣_{2}+𝑢_{3}⋅𝑣_{3}+𝑢_{4}⋅𝑣_{4} \\ & =(−1)⋅(−2)+4⋅3+3⋅(−4)+(−5)⋅6 \\ & =2+12−12−30 \\ & =−28\end{aligned}


$$

### Example: Finding the Value of an Unknown Quantity in an Expression Involving the Dot Product

#### Question

Let be $\begin{aligned}10 \\ 𝑥 \\ 0 \\ 5\end{aligned}$ and $\begin{aligned}𝑥 \\ 𝑥 \\ 8 \\ 5\end{aligned}$ If $\mathbf{a}\cdot \mathbf{b}=0,$ find the value of $x.$

#### Explanation

Starting from the equation $\mathbf{a} \cdot \mathbf{b}=0,$ we compute the dot product in terms of $x$ and then solve for $x$ in the resulting equation:

$$


\begin{aligned}𝐚⋅𝐛 & =0 \\ 10⋅𝑥+𝑥⋅𝑥+0⋅8+5⋅5 & =0 \\ 10𝑥+𝑥^{2}+25 & =0 \\ 𝑥^{2}+10𝑥+25 & =0 \\ (𝑥+5)^{2} & =0 \\ 𝑥 & =−5\end{aligned}


$$

Therefore, we conclude that $x=-5.$
