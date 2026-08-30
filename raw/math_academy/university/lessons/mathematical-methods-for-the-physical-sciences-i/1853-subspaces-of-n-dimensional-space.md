# Subspaces of N-Dimensional Space

Source: https://www.mathacademy.com/topics/1853?courseId=154
Topic ID: 1853

## Prerequisites

- [The Cartesian Equation of a Plane](./1807-the-cartesian-equation-of-a-plane.md)
- [Linear Combinations of Vectors in N-Dimensional Euclidean Space](./1851-linear-combinations-of-vectors-in-n-dimensional-euclidean-space.md)
- [Describing Planar Regions Using Set-Builder Notation](./4392-describing-planar-regions-using-set-builder-notation.md)

## Lesson

### Introduction

A **subspace** of $\mathbb{R}^n$ is a subset of $\mathbb R^n$ that is closed under vector addition and scalar multiplication. In other words:

$H\subseteq \mathbb R^n$ is a subspace of $\mathbb{R}^n$ if and only if it satisfies the following properties:

- *Closure under vector addition:* $\qquad$ If $\mathbf{u}$ and $\mathbf{v}$ are in $H,$ then their sum $\mathbf{u}+\mathbf{v}$ is also in $H.$

- *Closure under scalar multiplication:* $\qquad$ If $\mathbf{u}$ is in $H,$ then $c\cdot \mathbf{u}$ is also in $H$ for any scalar number $c.$

For example, consider the line $L$ with equation $y=3x$ in $\mathbb{R}^2.$ Is $L$ a subspace of $\mathbb{R}^2?$

First, notice that we can express the points on $L$ as the following set:

$$


[\begin{aligned}𝑥 \\ 𝑦\end{aligned}]


$$

In other words, $L$ contains all vectors of the form $[\begin{aligned}𝑥 \\ 3𝑥\end{aligned}]$ where $x$ is a real number.

To determine whether $L$ is a subspace of $\mathbb R^2,$ we need to check the two conditions above.

- Let's pick two arbitrary vectors in $L,$ namely, $[\begin{aligned}𝑢_{1} \\ 3𝑢_{1}\end{aligned}]$ and $[\begin{aligned}𝑣_{1} \\ 3𝑣_{1}\end{aligned}]$ If we compute their sum, we get which satisfies the condition $y=3x.$ Therefore, $\mathbf{u}+\mathbf{v} \in L. \quad {\color{green}\checkmark}$

- Let's pick an arbitrary vector in $L,$ namely, $[\begin{aligned}𝑢_{1} \\ 3𝑢_{1}\end{aligned}]$ Then, for any scalar $c$ we have which satisfies the condition $y=3x.$ Therefore, $c\cdot \mathbf{u}\in L. \quad {\color{green}\checkmark}$

The set $L$ satisfies both conditions. So, we can conclude that it is a subspace of $\mathbb{R}^2.$

**Note:** Since the second condition must be satisfied for any $c,$ including $c=0,$ we can conclude that every subspace must contain the zero vector $\mathbf{0}.$ So, if a set does not contain $\mathbf{0}$ then it is *not* a subspace of $\mathbb{R}^n.$

For instance, the set

$$


[\begin{aligned}𝑥 \\ 𝑦\end{aligned}]


$$

does *not* contain the zero vector (since $0 \neq 0 + 1$), and consequently it is *not* a subspace of $\mathbb{R}^2.$

### Example: Determining Whether a Line Is a Subspace of Two-Dimensional Space

#### Question

Let $L$ be the line with equation $y=5+3x$ in $\mathbb{R}^2.$ Which of the following statements are true?

1. $L$ contains the zero-vector

2. $L$ is closed under vector addition

3. $L$ is closed under scalar multiplication

4. $L$ is **** a subspace of $\mathbb{R}^2$

#### Explanation

Recall the following two facts about subspaces:

- A set of vectors in a vector space is a ** if it is closed under vector addition and scalar multiplication.

- If a non-empty set is closed under scalar multiplication, then this set must contain the zero-vector (because $0 \cdot \mathbf{v} = \mathbf{0}$ for any vector $\mathbf{v}$). So, if a set does not contain the zero vector, then this set is not closed under scalar multiplication.

Notice that $L$ contains vectors of the form

$$


[\begin{aligned}𝑥 \\ 𝑦\end{aligned}]


$$

With that in mind, let's examine our statements.

- Statement I is false. The coordinates of the zero-vector do not satisfy the equation $y=5+3x{:}$

- Statement II is false. Let, for example, $[\begin{aligned}0 \\ 5\end{aligned}]$ and $[\begin{aligned}−1 \\ 2\end{aligned}]$ from $L.$ Then, However, $[\begin{aligned}−1 \\ 7\end{aligned}]$ since substituting the coordinates into the equation $y=5+3x$ gives the following:

- Statement III is false. Since $\mathbf{0} \not\in L,$ this set is not closed under scalar multiplication.

- Statement IV is true. Since statements II and III are false, $L$ is ** a subspace of $\mathbb{R}^2.$

Therefore, the correct answer is "IV only."

### Lines as Subspaces of Three-Dimensional Space

Recall that $H$ is a subspace of $\mathbb{R}^n$ if and only if it satisfies the following properties:

*Closure under vector addition:*

$\qquad$ If $\mathbf{u}$ and $\mathbf{v}$ are in $H,$ then their sum $\mathbf{u}+\mathbf{v}$ is also in $H.$

*Closure under scalar multiplication:*

$\qquad$ If $\mathbf{u}$ is in $H,$ then $c\cdot \mathbf{u}$ is also in $H$ for any scalar number $c.$

Let $L$ be the line in $\mathbb{R}^3$ that passes through the points $(0,0,0)$ and $(4,1,-2).$ Is $L$ a subspace of $\mathbb{R}^3?$

First, note that the direction vector of the line $L$ is

$$


\begin{aligned}4 \\ 1 \\ −2\end{aligned}


$$

This means that the vector equation of the line is

$$


\begin{aligned}𝐫 & =\begin{matrix}0 \\ 0 \\ 0\end{matrix}+𝑡\begin{matrix}4 \\ 1 \\ −2\end{matrix}=\begin{matrix}4𝑡 \\ 𝑡 \\ −2𝑡\end{matrix}\end{aligned}


$$

for $t\in\mathbb R,$ and the corresponding Cartesian equation is

$$


\dfrac x4=y=\dfrac z{-2}.


$$

To determine whether $L$ is a subspace, we need to check the two conditions above:

- Let's pick two arbitrary vectors in $L,$ namely, $\begin{aligned}4𝑢_{1} \\ 𝑢_{1} \\ −2𝑢_{1}\end{aligned}$ and $\begin{aligned}4𝑣_{1} \\ 𝑣_{1} \\ −2𝑣_{1}\end{aligned}$ If we compute their sum, we get which satisfies the condition $\dfrac x4=y=\dfrac z{-2}.$ Therefore, $\mathbf{u}+\mathbf{v}\in L. \quad {\color{green}\checkmark}$

- Let's pick an arbitrary vector in $L,$ namely, $\begin{aligned}4𝑢_{1} \\ 𝑢_{1} \\ −2𝑢_{1}\end{aligned}$ Then, for any scalar $c,$ we have which satisfies the condition $\dfrac x4=y=\dfrac z{-2}.$ Therefore, $c\cdot \mathbf{u}\in L. \quad {\color{green}\checkmark}$

The set $L$ satisfies both conditions. So, we can conclude that it is a subspace of $\mathbb{R}^3.$

### Example: Determining Whether a Line Is a Subspace of Three-Dimensional Space

#### Question

Let $L$ be the line in $\mathbb{R}^3$ that passes through the points $(1,2,2)$ and $(2,1,1).$ Which of the following statements are true?

1. $L$ contains the zero-vector

2. $L$ is closed under vector addition

3. $L$ is closed under scalar multiplication

4. $L$ is **** a subspace of $\mathbb{R}^3$

#### Explanation

Recall the following two facts about subspaces:

- A set of vectors in a vector space is a ** if it is closed under vector addition and scalar multiplication.

- If a non-empty set is closed under scalar multiplication, then this set must contain the zero-vector (because $0 \cdot \mathbf{v} = \mathbf{0}$ for any vector $\mathbf{v}$). So, if a set does not contain the zero vector, then this set is not closed under scalar multiplication.

With that in mind, let's examine our statements.

- Statement I is false. The direction vector of the line $L$ is This means that the vector equation of the line is for $t\in\mathbb R,$ and the corresponding Cartesian equation is But this line does not pass through the origin since

- Statement II is false. Let's consider the vectors $\begin{aligned}1 \\ 2 \\ 2\end{aligned}$ and $\begin{aligned}2 \\ 1 \\ 1\end{aligned}$ from $L$ (the position vectors of the given points). Then, However, the point $(3,3,3)$ does not belong to $L$ since

- Statement III is false. Since $\mathbf{0} \not\in L,$ this set is not closed under scalar multiplication.

- Statement IV is true. Since statements II and III are false, $L$ is ** a subspace of $\mathbb{R}^3.$

Therefore, the correct answer is "IV only."

### Planes as Subspace of Three-Dimensional Space

Again, recall that $H$ is a subspace of $\mathbb{R}^n$ if and only if it satisfies the following properties:

- *Closure under vector addition:* $\qquad$ If $\mathbf{u}$ and $\mathbf{v}$ are in $H,$ then their sum $\mathbf{u}+\mathbf{v}$ is also in $H.$

- *Closure under scalar multiplication:* $\qquad$ If $\mathbf{u}$ is in $H,$ then $c\cdot \mathbf{u}$ is also in $H$ for any scalar number $c.$

Consider the plane $\Pi$ with equation $z=4x-2y$ in $\mathbb{R}^3.$

Notice that $\Pi$ contains vectors of the form

$$


\begin{aligned}𝑥 \\ 𝑦 \\ 𝑧\end{aligned}


$$

Is $\Pi$ a subspace of $\mathbb{R}^3?$ To find out, we need to check the two conditions above.

- Let's pick two arbitrary vectors in $\Pi,$ namely, $\begin{aligned}𝑢_{1} \\ 𝑢_{2} \\ 4𝑢_{1}−2𝑢_{2}\end{aligned}$ and $\begin{aligned}𝑣_{1} \\ 𝑣_{2} \\ 4𝑣_{1}−2𝑣_{2}\end{aligned}$ If we compute their sum, we get which satisfies the condition $z=4x-2y.$ Therefore, $\mathbf{u}+\mathbf{v}\in \Pi. \quad {\color{green}\checkmark}$

- Let's pick an arbitrary vector in $\Pi,$ say, $\begin{aligned}𝑢_{1} \\ 𝑢_{2} \\ 4𝑢_{1}−2𝑢_{2}\end{aligned}$ Then, for any scalar $c$ we have which satisfies the condition $z=4x-2y.$ Therefore, $c\cdot \mathbf{u}\in \Pi. \quad {\color{green}\checkmark}$

The set $\Pi$ satisfies both conditions. So, we can conclude that it is a subspace of $\mathbb{R}^3.$

### Example: Determining Whether a Plane Is a Subspace of Three-Dimensional Space

#### Question

Let $\Pi$ be the plane with equation $x+4y-3z=2$ in $\mathbb{R}^3.$ Which of the following statements are true?

1. $\Pi$ contains the zero-vector

2. $\Pi$ is closed under vector addition

3. $\Pi$ is closed under scalar multiplication

4. $\Pi$ is **** a subspace of $\mathbb{R}^3$

#### Explanation

Recall the following two facts about subspaces:

- A set of vectors in a vector space is a ** if it is closed under vector addition and scalar multiplication.

- If a non-empty set is closed under scalar multiplication, then this set must contain the zero-vector (because $0 \cdot \mathbf{v} = \mathbf{0}$ for any vector $\mathbf{v}$). So, if a set does not contain the zero vector, then this set is not closed under scalar multiplication.

Notice that $\Pi$ contains vectors of the form

$$


\begin{aligned}𝑥 \\ 𝑦 \\ 𝑧\end{aligned}


$$

With that in mind, let's examine our statements.

- Statement I is false. The plane does not pass through the origin since

- Statement II is false. Let's consider $\begin{aligned}2 \\ 0 \\ 0\end{aligned}$ and $\begin{aligned}1 \\ 1 \\ 1\end{aligned}$ Then However, $\begin{aligned}3 \\ 1 \\ 1\end{aligned}$ does not belong to $\Pi$ since

- Statement III is false. Since $\mathbf{0} \not\in \Pi,$ this set is not closed under scalar multiplication.

- Statement IV is true. Since statements II and III are false, $\Pi$ is ** a subspace of $\mathbb{R}^3.$

Therefore, the correct answer is "IV only."
