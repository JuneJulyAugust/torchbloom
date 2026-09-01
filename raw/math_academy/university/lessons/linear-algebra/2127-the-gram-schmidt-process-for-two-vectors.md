# The Gram-Schmidt Process for Two Vectors

Source: https://www.mathacademy.com/topics/2127?courseId=55
Topic ID: 2127

## Prerequisites

- [Orthogonal Sets in Euclidean Spaces](./2103-orthogonal-sets-in-euclidean-spaces.md)
- [Projecting Vectors Onto One-Dimensional Subspaces](./2122-projecting-vectors-onto-one-dimensional-subspaces.md)
- [Finding a Basis of the Column Space of a Matrix](./2623-finding-a-basis-of-the-column-space-of-a-matrix.md)

## Lesson

### Introduction

The **Gram-Schmidt process** is an algorithm that we can use to construct an *orthogonal* basis if we are given a non-orthogonal basis to start with.

For example, consider the basis $\{\mathbf{a}_1, \mathbf{a}_2 \}$ for the subspace $V=\text{Span} \{\mathbf{a}_1, \mathbf{a}_2 \},$ where

$$


[\begin{aligned}1 \\ −1\end{aligned}]


$$

We can use the above basis to construct an *orthogonal* basis for the given $2$-dimensional subspace. To do this, we use the Gram-Schmidt process, which involves $2$ steps:

- **Step 1:** Set ${\color{blue}\mathbf{v}_1}=\mathbf{a}_1.$

- **Step 2:** Find a vector $\color{blue}\mathbf{v}_2$ in $V$ that's orthogonal to $\color{blue}\mathbf{v}_1.$ This can be achieved by computing Notice that $\color{blue}\mathbf{v}_2$ is written as a linear combination of $\mathbf{a}_1(={\color{blue}\mathbf{v}_1})$ and $\mathbf{a}_2.$ So this means that ${\color{blue}\mathbf{v}_2} \in V,$ and also ${\color{blue}\mathbf{v}_2} \perp {\color{blue}\mathbf{v}_1}.$ Moreover,

After applying the Gram-Schmidt process, we get the set $\mathcal{B}=\{{\color{blue}\mathbf{v}_1}, {\color{blue}\mathbf{v}_2}\},$ which is an orthogonal basis for $V.$

So, in our example, we start by setting $[\begin{aligned}1 \\ −1\end{aligned}]$ Then, we find the vector $\mathbf{v}_2$ that's orthogonal to $\text{Span}\{\mathbf{v}_1\}$ as follows:

$$


\begin{aligned}𝐯_{2} & =𝐚_{2}−\frac{𝐚_{2}⋅𝐯_{1}}{𝐯_{1}⋅𝐯_{1}}𝐯_{1} \\ & =𝐚_{2}−\frac{4⋅1+6⋅(−1)}{1^{2}+(−1)^{2}}𝐯_{1} \\ & =[\begin{matrix}4 \\ 6\end{matrix}]−(−1)⋅[\begin{matrix}1 \\ −1\end{matrix}] \\ & =[\begin{matrix}5 \\ 5\end{matrix}]\end{aligned}


$$

Therefore, $[\begin{aligned}1 \\ −1\end{aligned}]$ is an orthogonal basis for $V.$

### Example: Finding an Orthogonal Basis For the Span of Two Vectors

#### Question

Consider the subspace $V$ and an orthogonal basis $\mathcal B$ of $V,$ given below. Given that $\mathcal B$ is derived from $V$ using the Gram-Schmidt process, what is the value of $\dfrac{a}{c}?$

$$


\begin{aligned}1 \\ −1 \\ 2\end{aligned}


$$

#### Explanation

First, let's denote

$$


\begin{aligned}1 \\ −1 \\ 2\end{aligned}


$$

We proceed to find an orthogonal basis using the Gram-Schmidt process, as follows.

- ****: We set $\begin{aligned}1 \\ −1 \\ 2\end{aligned}$

- ****: Next, we find $\mathbf{v}_2$, using the formula Applying the formula for $\mathbf v_2$ in our case gives

Therefore, $\begin{aligned}1 \\ −1 \\ 2\end{aligned}$ is an orthogonal basis for $V.$

Finally, $a=-\dfrac 7 3,$ $c=\dfrac{10}{3}$ and

$$


\dfrac{a}{c} = \dfrac{\left(-\dfrac{7}{3}\right)}{\left(\dfrac{10}{3}\right)} = -\dfrac{7}{10}.


$$

### Scaling the Vectors After the Gram-Schmidt Process

Sometimes it's helpful to "clean up" the result of a Gram-Schmidt process by scaling the resulting vectors.

For example, suppose that the set $\mathcal B,$ given by

$$


\begin{aligned}1 \\ −1 \\ 2\end{aligned}


$$

is an orthogonal basis for $\text{Span} \{\mathbf{v}_1, \mathbf{v}_2 \}.$

Since the vector $\mathbf{v}_2$ lies in $\text{Span} \{\mathbf{v}_1, \mathbf{v}_2 \}$ and $\mathbf{v}_1 \perp \mathbf{v}_2,$ the vector $3\mathbf{v}_2$ also lies in $\text{Span} \{\mathbf{v}_1, \mathbf{v}_2 \}$ and $\mathbf{v}_1 \perp 3\mathbf{v}_2.$ Therefore, taking

$$


\begin{aligned}−7 \\ 13 \\ 10\end{aligned}


$$

instead of $\mathbf{v}_2,$ we again obtain an orthogonal basis for $\text{Span} \{\mathbf{v}_1, \mathbf{v}_2 \}\mathbin{:}$

$$


\begin{aligned}1 \\ −1 \\ 2\end{aligned}


$$

But this time, the second vector in the basis looks slightly nicer and is probably easier to work with.

### Example: Finding an Orthogonal Basis For the Column Space of a Matrix

#### Question

Consider the subspace $\text{Col}(A)$ and an orthogonal basis $\mathcal B$ of $\text{Col}(A),$ where $A$ and $\mathcal B$ are given below. Given that $\mathcal B$ is derived from $\text{Col}(A)$ using the Gram-Schmidt process, what is the value of $\dfrac{c}{a}?$

$$


\begin{aligned}1 & −5 \\ −2 & −1 \\ 2 & −3\end{aligned}


$$

#### Explanation

Recall that $\text{Col}(A)$ is the span of the columns of $A.$

First, let's denote

$$


\begin{aligned}1 \\ −2 \\ 2\end{aligned}


$$

We proceed to find an orthogonal basis using the Gram-Schmidt process, as follows.

- ****: We set $\begin{aligned}1 \\ −2 \\ 2\end{aligned}$

- ****: Next, we find $\mathbf{v}_2$, by using the formula Applying the formula for $\mathbf v_2$ in our case gives

Therefore, $\begin{aligned}1 \\ −2 \\ 2\end{aligned}$ is an orthogonal basis for $\text{Col}(A).$

Finally, $a=-4,$ $c=-1,$ and

$$


\dfrac{c}{a} = \dfrac{-1}{-4} = \dfrac{1}{4}.


$$

### Using the Gram-Schmidt Process to Find an Orthonormal Basis

Given a basis $\{\mathbf{a}_1, \mathbf{a}_2\}$ for a subspace $V,$ we can use the Gram-Schmidt process to find an *orthonormal* basis of the subspace.

To do this, we simply execute the Gram-Schmidt process as before to obtain an orthogonal basis $\{\mathbf{v}_1, \mathbf{v}_2\},$ and then we normalize each vector in this basis to get the orthonormal basis $\{\mathbf{u}_1, \mathbf{u}_2\},$ where

$$


\mathbf{u}_1 = \dfrac{\mathbf{v}_1}{\Vert \mathbf{v}_1 \Vert}, \quad \mathbf{u}_2 = \dfrac{\mathbf{v}_2}{\Vert \mathbf{v}_2 \Vert}.


$$

### Example: Finding an Orthonormal Basis of a Vector Space

#### Question

Consider the subspace $V$ and an **** basis $\mathcal B$ of $V,$ given below. Given that $\mathcal B$ is derived from $V$ using the Gram-Schmidt process, what is the value of $|a|+|b|+|c|?$ '

$$


\begin{aligned}2 \\ 2 \\ −1\end{aligned}


$$

#### Explanation

First, let's denote

$$


\begin{aligned}2 \\ 2 \\ −1\end{aligned}


$$

We proceed to find an orthogonal basis using the Gram-Schmidt process, as follows.

- ****: We set $\begin{aligned}2 \\ 2 \\ −1\end{aligned}$

- ****: Next, we find $\mathbf{v}_2$, by using the formula Applying the formula for $\mathbf v_2$ in our case gives

Now, we normalize each vector to get an orthonormal basis:

- $\begin{aligned}2 \\ 2 \\ −1\end{aligned}$

- $\begin{aligned}4 \\ −2 \\ 4\end{aligned}$

Therefore, $\begin{aligned}\frac{2}{3} \\ \frac{2}{3} \\ −\frac{1}{3}\end{aligned}$ is an orthonormal basis for $V.$

Finally, $a=\dfrac{2}{3},$ $b=-\dfrac1 3,$ $c=\dfrac{2}{3},$ and

$$


|a|+|b|+|c| = \left| \dfrac{2}{3} \right| + \left|-\dfrac{1}{3}\right| + \left| \dfrac{2}{3} \right| = \dfrac 5 3.


$$
