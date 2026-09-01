# Orthogonal Sets in Inner Product Spaces

Source: https://www.mathacademy.com/topics/2104?courseId=55
Topic ID: 2104

## Prerequisites

- [Orthogonal Vectors in Inner Product Spaces](./2100-orthogonal-vectors-in-inner-product-spaces.md)
- [Orthogonal Sets in Euclidean Spaces](./2103-orthogonal-sets-in-euclidean-spaces.md)

## Lesson

### Introduction

Let's consider an inner product space $V$ equipped with the inner product $\langle \cdot, \cdot \rangle.$ A set of vectors

$$


{U}=\{ \mathbf{u}_1, \cdots, \mathbf{u}_p \}


$$

is called an **orthogonal set with respect to the given inner product** if all vectors in the set are mutually orthogonal.

For example, let's consider the set

$$


\begin{aligned}1 \\ 1 \\ 1\end{aligned}


$$

and the inner product on $\mathbb{R}^3$ defined as

$$


\langle \mathbf{x},\mathbf{y} \rangle = x_1 y_1 + 3x_2 y_2 + 2x_3 y_3.


$$

If we denote the vectors in our set ${V}$ as $\{\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3 \},$ we can check that ${V}$ is orthogonal by showing that

$$


\begin{aligned}⟨𝐯_{1},𝐯_{2}⟩=0 \\ ⟨𝐯_{1},𝐯_{3}⟩=0 \\ ⟨𝐯_{2},𝐯_{3}⟩=0.\end{aligned}


$$

Let's compute each inner product:

$$


\begin{aligned}⟨𝐯_{1},𝐯_{2}⟩ & =(1)(2)+3(1)(2)+2(1)(−4)=2+6−8=0 & ✓ \\ ⟨𝐯_{1},𝐯_{3}⟩ & =(1)(−3)+3(1)(1)+2(1)(0)=−3+3+0=0 & ✓ \\ ⟨𝐯_{2},𝐯_{3}⟩ & =(2)(−3)+3(2)(1)+2(−4)(0)=−6+6+0=0 & ✓\end{aligned}


$$

So indeed, ${V}$ is an orthogonal set.

### Example: Determining Whether a Set of Vectors Is Orthogonal With Respect to a Given Inner Product

#### Question

$$


\begin{aligned}2 \\ 2 \\ 1\end{aligned}


$$

Consider the vectors shown above. Given that the inner product in the vector space $\mathbb{R}^3$ is defined as

$$


\langle \mathbf{x},\mathbf{y} \rangle = 3x_1 y_1 + x_2 y_2 + 2x_3 y_3,


$$

which of the following statements are true?

1. $\mathbf{v}_1 \perp \mathbf{v}_2$ with respect to the given inner product

2. $\mathbf{v}_1 \perp \mathbf{v}_3$ with respect to the given inner product

3. $S=\{\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3 \}$ is an orthogonal set with respect to the given inner product

#### Explanation

Recall that a set of vectors in an inner product space is orthogonal if all vectors in the set are mutually orthogonal with respect to the given inner product.

With that in mind, let's examine our statements in turn.

- Statement I is true. Indeed, we have which means that $\mathbf{v}_1 \perp \mathbf{v}_2$ with respect to the given inner product.

- Statement II is false since which means that $\mathbf{v}_1 \not\perp \mathbf{v}_3$ with respect to the given inner product.

- Statement III is false. Since $\mathbf{v}_1 \not\perp \mathbf{v}_3,$ the set $S$ is ** orthogonal.

Therefore, the correct answer is "I only."

### Example: Determining Whether a Set of Polynomials is Orthogonal With Respect to a Given Inner Product

#### Question

Consider the following set of polynomials:

$$


p_1(t)=t+1, \qquad p_2(t)=t, \qquad p_3(t)=t-1.


$$

Given that the inner product in the vector space $\mathbb{R}_1[t]$ of polynomials of degree $1$ or less in the variable $t$ is defined as

$$


\langle p(t),q(t) \rangle =p(-1)q(-1)+p(1)q(1),


$$

which of the following statements are true?

1. $p_1(t) \perp p_3(t)$ with respect to the given inner product

2. $p_2(t) \perp p_3(t)$ with respect to the given inner product

3. $S=\{p_1(t), p_2(t), p_3(t) \}$ is an orthogonal set with respect to the given inner product

#### Explanation

Recall that a set of vectors in an inner product space is orthogonal if all vectors in the set are mutually orthogonal with respect to the given inner product.

With that in mind, let's examine our statements in turn.

- Statement I is true. Indeed, we have which means that $p_1(t) \perp p_3(t)$ with respect to the given inner product.

- Statement II is false since which means that $p_2(t) \not\perp p_3(t)$ with respect to the given inner product.

- Statement III is false. Since $p_2(t) \not\perp p_3(t),$ the set $S$ is ** orthogonal.

Therefore, the correct answer is "I only."

### Example: Determining Whether a Set of Functions is Orthogonal With Respect to a Given Inner Product

#### Question

Consider the following set of functions:

$$


f_1(t)=1, \qquad f_2(t)=t, \qquad f_3(t)=2t+1


$$

Given that the inner product in the vector space $\mathcal{C}[-1,1]$ of continuous functions over $[-1,1]$ is defined as

$$


\langle f(t),g(t) \rangle = \int_{-1}^{1} f(t)g(t) \: \text{d}t,


$$

which of the following statements are true?

1. $f_1(t) \perp f_3(t)$ with respect to the given inner product

2. $f_2(t) \perp f_3(t)$ with respect to the given inner product

3. $S=\{f_1(t), f_2(t), f_3(t) \}$ is an orthogonal set with respect to the given inner product

#### Explanation

Recall that a set of vectors in an inner product space is called orthogonal if all vectors in the set are mutually orthogonal with respect to the given inner product.

With that in mind, let's examine our statements in turn.

- Statement I is false. We have This means that $f_1(t) \not\perp f_2(t)$ with respect to the given inner product.

- Statement II is false. We have This means that $f_2(t) \not\perp f_3(t)$ with respect to the given inner product.

- Statement III is false. Since $f_1(t) \not\perp f_2(t),$ the set $S$ is ** orthogonal.

Therefore, the correct answer is "None of the statements are true."
