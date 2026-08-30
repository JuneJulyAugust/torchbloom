# The Dimension of a Span

Source: https://www.mathacademy.com/topics/1866?courseId=55
Topic ID: 1866

## Prerequisites

- [Finding a Basis of a Span](./1855-finding-a-basis-of-a-span.md)

## Lesson

### Introduction

There is something interesting about the bases of a vector space, summarized in the theorem below:

If the vector space $V$ has a basis with $n$ vectors, then any basis of $V$ has exactly $n$ vectors.

The number $n$ of vectors in any basis of $V$ is called the **dimension of the space** $V$ and is denoted $\text{dim}(V).$

For example, consider the linear span below:

$$


[\begin{aligned}3 \\ −1\end{aligned}]


$$

We know that, in order to find a basis of the span, we start by creating a matrix whose columns are made up of our vectors, and then we reduce the matrix to row echelon form:

$$


\begin{aligned}𝑀 & =\,\,[\begin{matrix}3 & −3 & −6 \\ −1 & 1 & 5\end{matrix}] & 𝑅_{2} & :=𝑅_{2}+\frac{1}{3}𝑅_{1} \\ & ∼[\begin{matrix}3 & −3 & −6 \\ 0 & 0 & 3\end{matrix}] & & \end{aligned}


$$

We see that the matrix above has two pivot columns: the $1$st and the $3$rd columns. This tells us that $\mathcal{B}=\{\mathbf{v}_1,\mathbf{v}_3 \}$ is a basis of $H.$

Since $\mathcal{B}$ consists of two vectors, *any basis* of $H$ will also have *exactly* two vectors. So, we have $\text{dim}(H)=2.$

### Finite and Infinite-Dimensional Vector Spaces

As defined earlier, the dimension of a vector space $V$ is the number of vectors in any basis of $V$.

However, note that the definition above is only applicable if a vector space has at least one basis with a finite number of elements.

- If a vector space has a basis with a finite number of vectors, then it is called **finite-dimensional**.

- Otherwise, if there is no finite basis, the vector space is called **infinite-dimensional**.

In linear algebra, we mostly consider finite-dimensional vector spaces.

### Example: Finding the Dimension of a Span by Inspection

#### Question

Determine the dimension of

$$


\begin{aligned}1 \\ 0 \\ 0\end{aligned}


$$

#### Explanation

We start by creating a matrix whose columns are made up of our vectors, and then we reduce the matrix to row echelon form:

$$


\begin{aligned}\begin{matrix}1 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 0\end{matrix}\end{aligned}


$$

In this case, our matrix is already in a row echelon form. We see that the matrix above has two pivot columns: the $1$st and the $2$nd columns. This tells us that $\mathcal{B}=\{\mathbf{v}_1,\mathbf{v}_2 \}$ forms a basis for our span.

Since $\mathcal{B}$ consists of two vectors, any basis of our span will also have ** two vectors. Therefore, the dimension of the span is $2\mathbin{:}$

$$


\begin{aligned}1 \\ 0 \\ 0\end{aligned}


$$

### Example: Finding the Dimension of a Span Using Row Reduction

#### Question

Determine the dimension of

$$


\begin{aligned}2 \\ −6 \\ 4\end{aligned}


$$

#### Explanation

We start by creating a matrix whose columns are made up of our vectors, and then we reduce the matrix to row echelon form:

$$


\begin{aligned}𝑀 & =\,\,\begin{matrix}2 & −1 & 5 \\ −6 & 3 & −15 \\ 4 & −2 & 10\end{matrix} & 𝑅_{2} & :=𝑅_{2}+3𝑅_{1} \\ & ∼\begin{matrix}2 & −1 & 5 \\ 0 & 0 & 0 \\ 4 & −2 & 10\end{matrix} & 𝑅_{3} & :=𝑅_{3}+(−2)𝑅_{1} \\ & ∼\begin{matrix}2 & −1 & 5 \\ 0 & 0 & 0 \\ 0 & 0 & 0\end{matrix} & & \end{aligned}


$$

We see that the matrix above has one pivot columns: the $1$st column. This tells us that $\mathcal{B}=\{\mathbf{v}_1 \}$ forms a basis for our span.

Since $\mathcal{B}$ consists of one vector, any basis of our span will also have ** one vector. Therefore, the dimension of the span is $1\mathbin{:}$

$$


\begin{aligned}2 \\ −6 \\ 4\end{aligned}


$$

### Geometric Intuition for Finite-Dimensional Vector Spaces

We can build some geometric intuition for finite-dimensional vector spaces. To illustrate, let's find the dimensions of $\{\mathbf{0}\},$ $\mathbb{R},$ $\mathbb{R}^2,$ and $\mathbb{R}^3.$

First, note that $\{\mathbf{0}\}$ can be written as $\mathbb{R}^0,$ and $\mathbb{R}$ can be written as $\mathbb{R}^1.$ We have the following standard bases:

$$


[\begin{aligned}1\end{aligned}]


$$

Consequently, we have the following dimensions:

$$


\begin{aligned}dim(ℝ^{0})=0,\,dim(ℝ^{1})=1,\,dim(ℝ^{2})=2,\,dim(ℝ^{3})=3.\end{aligned}


$$

Now, let's build some geometric intuition. We can represent the standard bases in the following diagram:

![Instructional graphic](../../../lesson-assets/linear-algebra/topic-1866/61c0229945ae61c4.png)

So, the sequence $\mathbb{R}^0,$ $\mathbb{R}^1,$ $\mathbb{R}^2,$ $\mathbb{R}^3,$ $\ldots$ can be visualized as follows:

![Instructional graphic](../../../lesson-assets/linear-algebra/topic-1866/23585b1be9a2f9c4.png)

Notice the following:

- The basis for $\mathbb{R}^0$ is represented geometrically as a $0$-dimensional point.

- The basis for $\mathbb{R}^1$ is represented geometrically as a $1$-dimensional line segment.

- The basis for $\mathbb{R}^2$ is represented geometrically as a $2$-dimensional square.

- The basis for $\mathbb{R}^3$ is represented geometrically as a $3$-dimensional cube.

Unfortunately, we can't visualize dimensions greater than $3,$ but we know that $\mathbb{R}^n$ has the following standard basis consisting of $n$ vectors:

$$


\begin{aligned}1 \\ 0 \\ 0 \\ ⋮ \\ 0\end{aligned}


$$

Therefore,

$$


\text{dim}(\mathbb{R}^n) = n.


$$
