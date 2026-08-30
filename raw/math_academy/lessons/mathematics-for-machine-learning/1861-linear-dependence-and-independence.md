# Linear Dependence and Independence

Source: https://www.mathacademy.com/topics/1861?courseId=145
Topic ID: 1861

## Prerequisites

- [Linear Span of Vectors in N-Dimensional Euclidean Space](./1852-linear-span-of-vectors-in-n-dimensional-euclidean-space.md)

## Lesson

### Introduction

We say that two vectors $\mathbf{v}_1$ and $\mathbf{v}_2$ are **linearly independent** if the only solution to the equation

$$


x_1 \mathbf{v}_1 + x_2 \mathbf{v}_2 = \mathbf{0}


$$

is $x_1 = x_2 = 0.$ Otherwise, if there exists any solution other than $x_1 = x_2 = 0,$ then we say that the two vectors $\mathbf{v}_1$ and $\mathbf{v}_2$ are **linearly dependent**.

To illustrate, let's consider two sets of vectors in $\mathbb{R}^2\mathbin{:}$

$$


[\begin{aligned}1 \\ 0\end{aligned}]


$$

- For the first set ${\color{blue}(\textrm{I})},$ we have The above equation is true only if $x_1=x_2=0.$ So, the set $\color{blue}(\textrm{I})$ is *linearly independent*.

- On the other hand, for the second set ${\color{red}(\textrm{II})},$ we have The above equation has solutions other than $x_1=x_2=0.$ For example, $x_1=2$ and $x_2=1$ gives Therefore, the set $\color{red}(\textrm{II})$ is *not* linearly independent. Rather, it is *linearly dependent*.

**Note:** You may notice that the vectors in the set $\color{red}(\textrm{II})$ were parallel (i.e. multiples of one another), while the vectors in set $\color{blue}(\textrm{I})$ were not. This trend holds in general, for all sets of two vectors:

- a set of two vectors is *linearly dependent* if and only if the two vectors are parallel, while

- a set of two vectors is *linearly independent* if and only if the two vectors are not parallel.

### Sets of Two Vectors Containing the Zero Vector

Any set of two vectors that contains the zero vector $\mathbf{0}$ must be linearly dependent. To see this, consider the set $\left\{\mathbf{v}, \mathbf{0} \right\}.$ We can realize that this set is linearly dependent using either of the following two methods.

**Method 1**

Notice that

$$


0 \cdot \mathbf{v} + 1 \cdot \mathbf{0} = \mathbf{0}.


$$

Therefore, the equation

$$


x_1 \mathbf{v} + x_2 \cdot \mathbf{0} = \mathbf{0}


$$

has a solution $x_1=0$ and $x_2=1,$ which is different from $x_1=x_2=0.$ So, the set is linearly dependent.

**Method 2**

Alternatively, recall that a set of two vectors is linearly dependent if and only if the two vectors are parallel. That is, the two vectors are multiples of each other.

The zero vector $\mathbf{0}$ is parallel to every other vector because it is a multiple of any other vector. For any vector $\mathbf{v},$ we have

$$


\mathbf{0} = 0 \cdot \mathbf{v} \qquad \Longrightarrow \qquad \mathbf{0} \parallel \mathbf{v}.


$$

So, because $\mathbf{0}$ is parallel to $\mathbf{v},$ the set $\left\{\mathbf{v}, \mathbf{0} \right\}$ is linearly dependent.

### Example: Finding a Vector That Makes a Set Linearly Dependent

#### Question

The set $\{\mathbf{a_1},\mathbf{a_2} \}$ is linearly dependent. Which of the following vectors could be $\mathbf{a}_2$ if $\begin{aligned}12 \\ 3 \\ 21\end{aligned}$

$$


\begin{aligned}4 \\ 1 \\ 7\end{aligned}


$$

#### Explanation

We say that two vectors $\mathbf{v}_1$ and $\mathbf{v}_2$ are ** if the only solution to the equation

$$


x_1 \mathbf{v}_1 + x_2 \mathbf{v}_2 = \mathbf{0}


$$

is $x_1 = x_2 = 0.$ Otherwise, the vectors are **.

A set containing ** vectors is linearly ** if and only if the two vectors are parallel.

From the given options, the correct answer is

$$


\begin{aligned}4 \\ 1 \\ 7\end{aligned}


$$

To see why, notice that

$$


\begin{aligned}4 \\ 1 \\ 7\end{aligned}


$$

In other words, the vectors $\mathbf a_1$ and $\mathbf a_2$ are parallel.

To see why this means that $\mathbf a_1$ and $\mathbf a_2$ are linearly dependent, notice that

$$


\begin{aligned}\frac{1}{3}𝐚_{1}−𝐚_{2} & =𝟎.\end{aligned}


$$

So, the equation

$$


x_1 \mathbf{a}_1 +x_2 \mathbf{a}_2 = \mathbf{0}


$$

has the solution $x_1=\dfrac 1 3$ and $x_2=-1,$ which is different from $x_1=x_2=0.$ Therefore, the set is linearly dependent.

### Linear Dependence and Independence for a General Set of Vectors

So far, we've discussed linear dependence and linear independence for sets of two vectors. However, these concepts can be extended to sets of any number of vectors.

A set of $n$ vectors $\left\{\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n \right\}$ is called **linearly independent** if the only solution to the equation

$$


x_1 \mathbf{v}_1 + x_2 \mathbf{v}_2 + \ldots + x_n \mathbf{v}_n = \mathbf{0}


$$

is $x_1=x_2=\ldots=x_n=0.$ Otherwise, if there exists any solution other than $x_1 = x_2 = \ldots = x_n = 0,$ then we say that the set $\left\{\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n \right\}$ is **linearly dependent**.

Similar to sets containing two vectors, a general set of $n$ vectors is dependent if *any* two vectors in the set are parallel.

**But be careful!** When working with sets containing more than two vectors, having a linearly dependent set is possible even if *none* of the vectors are parallel!

For example, consider the following set of vectors:

$$


[\begin{aligned}1 \\ 0\end{aligned}]


$$

None of the vectors in this set are parallel. However, we have

$$


[\begin{aligned}1 \\ 0\end{aligned}]


$$

So, the equation

$$


[\begin{aligned}1 \\ 0\end{aligned}]


$$

has a solution $x_1 = 1,$ $x_2 = 1,$ and $x_3 = -1,$ which is different from $x_1 = x_2 = x_3 = 0.$ Therefore, we conclude that the vectors are linearly dependent.

### General Sets of Vectors Containing the Zero Vector

As with sets containing only two vectors, any set of vectors that contains the zero vector $\mathbf{0}$ must be linearly dependent.

To see this, consider the set

$$


\left\{ \mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_{n-1}, \mathbf{0} \right\}.


$$

Notice that

$$


0 \cdot \mathbf{v}_1 + 0 \cdot \mathbf{v}_2 + \ldots + 0 \cdot \mathbf{v}_{n-1} + 1 \cdot \mathbf{0} = \mathbf{0}.


$$

So, the equation

$$


x_1 \mathbf{v}_1 + x_2 \mathbf{v}_2 + \ldots + x_{n-1} \mathbf{v}_{n-1} + x_n \cdot \mathbf{0} = \mathbf{0}


$$

has the solution $x_1=x_2=\ldots = x_{n-1}=0$ and $x_n=1,$ which is different from $x_1=x_2=\ldots = x_n=0.$ Therefore, the set is linearly dependent.

### Example: Identifying Linearly Independent Sets by Inspection

#### Question

Consider the following vectors:

$$


\begin{aligned}4 \\ −1 \\ 0\end{aligned}


$$

Which of the following statements are true?

1. $\mathbf{a}_1 - \mathbf{a}_2 -2 \mathbf{a}_3 = \mathbf{0}.$

2. $x_1\mathbf{a}_1 + x_2\mathbf{a}_2 + x_3\mathbf{a}_3 = \mathbf{0}$ only if $x_1=x_2=x_3 = 0.$

3. The set $\{\mathbf{a}_1, \mathbf{a}_2, \mathbf{a}_3\}$ is linearly independent.

#### Explanation

We say that three vectors $\mathbf{v}_1, \mathbf{v}_2$ and $\mathbf{v}_3$ are ** if the only solution to the equation

$$


x_1 \mathbf{v}_1 + x_2 \mathbf{v}_2 + x_3\mathbf{v}_3= \mathbf{0}


$$

is $x_1 = x_2 = x_3 = 0.$ Otherwise, the vectors are **.

With that in mind, let's look at each statement in turn.

- Statement I is false. Indeed:

- Statement II is true. The equation $x_1\mathbf{a}_1 + x_2\mathbf{a}_2 + x_3\mathbf{a}_3 = \mathbf{0}$ corresponds to the system Notice that we can reorder the equations in this system as follows: Solving this system using back substitution, we find that the solution is $x_1 = x_2 = x_3 = 0.$

- Statement III is true. Since statement II is true, the set $\{\mathbf{a}_1, \mathbf{a}_2, \mathbf{a}_3 \}$ is linearly independent.

Therefore, the correct answer is "II and III only."

### Example: Identifying Linearly Independent and Dependent Sets Using Row Reduction

#### Question

Consider the following vectors:

$$


\begin{aligned}2 \\ 4 \\ 0\end{aligned}


$$

Assume that $x_1,x_2,$ and $x_3$ are real numbers. Which of the following statements are true?

1. The equation $x_1\mathbf{a}_1+x_2\mathbf{a}_2+x_3\mathbf{a}_3=\mathbf{0}$ has an infinite number of nonzero solutions.

2. The vectors $\mathbf{a}_1,\mathbf{a}_2,$ and $\mathbf{a}_3$ are linearly independent.

3. The vectors $\mathbf{a}_1,\mathbf{a}_2,$ and $\mathbf{a}_3$ are linearly dependent.

#### Explanation

We say that three vectors $\mathbf{v}_1, \mathbf{v}_2,$ and $\mathbf{v}_3$ are ** if the only solution to the equation

$$


x_1 \mathbf{v}_1 + x_2 \mathbf{v}_2 + x_3 \mathbf{v}_3 = \mathbf{0}


$$

is $x_1 = x_2 = x_3 = 0.$ Otherwise, the vectors are **.

With that in mind, let's examine our statements.

The equation $x_1\mathbf{a}_1+x_2\mathbf{a}_2+x_3\mathbf{a}_3=\mathbf{0}$ corresponds to the system

$$


\begin{aligned}2𝑥_{1}−𝑥_{2}+2𝑥_{3}=0 \\ 4𝑥_{1}+4𝑥_{2}+5𝑥_{3}=0 \\ 6𝑥_{2}+𝑥_{3}=0.\end{aligned}


$$

To solve the system, we create its augmented matrix and reduce it using Gaussian elimination:

$$


\begin{aligned}𝑀 & =\begin{aligned}2 & −1 & 2 & 0 \\ 4 & 4 & 5 & 0 \\ 0 & 6 & 1 & 0\end{aligned} & 𝑅_{2}:=𝑅_{2}+(−2)𝑅_{1} \\ & ∼\begin{aligned}2 & −1 & 2 & 0 \\ 0 & 6 & 1 & 0 \\ 0 & 6 & 1 & 0\end{aligned} & 𝑅_{3}:=𝑅_{3}+(−1)𝑅_{2} \\ & ∼\begin{aligned}2 & −1 & 2 & 0 \\ 0 & 6 & 1 & 0 \\ 0 & 0 & 0 & 0\end{aligned} & \end{aligned}


$$

From the matrix above, we conclude that the basic variables are $x_1$ and $x_2,$ while $x_3$ is the free variable.

Since there is one free variable, the equation $x_1\mathbf{a}_1+x_2\mathbf{a}_2+x_3\mathbf{a}_3=\mathbf{0}$ has an infinite number of nonzero solutions, which means that the vectors are linearly dependent.

Therefore, statements II is false, while statements I and III are true.
