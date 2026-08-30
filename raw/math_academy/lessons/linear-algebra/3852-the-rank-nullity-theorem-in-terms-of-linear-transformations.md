# The Rank-Nullity Theorem in Terms of Linear Transformations

Source: https://www.mathacademy.com/topics/3852?courseId=55
Topic ID: 3852

## Prerequisites

- [The Invertible Matrix Theorem in Terms of Linear Transformations](./1962-the-invertible-matrix-theorem-in-terms-of-linear-transformations.md)
- [The Rank-Nullity Theorem](./3836-the-rank-nullity-theorem.md)

## Lesson

### Introduction

The **rank-nullity theorem in terms of linear transformations** states the following:

*If $\mathbf{T}:\mathbb{R}^n \to \mathbb{R}^n$ is a linear transformation, then*

$$


\textrm{dim(Im}(\mathbf{T})) + \textrm{dim(Ker}(\mathbf{T})) = \textrm{dim}(\mathbb{R}^n),


$$

*or equivalently,*

$$


\textrm{rank}(\mathbf{T}) + \textrm{nullity}(\mathbf{T}) = n.


$$

For example, suppose that $\mathbf{T}:\mathbb{R}^3\to\mathbb{R}^3$ is a linear transformation such that

$$


\textrm{Im}(\mathbf{T})=\{ [ x, y, z ]^T \, : \, y+2z=0\}.


$$

Let's use the rank-nullity theorem to compute $\textrm{rank}(\mathbf{T})$ and $\text{nullity}(\mathbf{T}).$

First, solving $y+2z=0$ for $y,$ we get $y = -2z.$ Therefore, any vector from $\textrm{Im}(\mathbf{T})$ can be written as

$$


\begin{aligned}\begin{aligned}𝑥 \\ −2𝑧 \\ 𝑧\end{aligned}=𝑥\underset{𝐯_{1}}{\underset{}\begin{aligned}1 \\ 0 \\ 0\end{aligned}}}+𝑧\underset{𝐯_{2}}{\underset{}\begin{aligned}0 \\ −2 \\ 1\end{aligned}}}.\end{aligned}


$$

This means that $\textrm{Im}(\mathbf{T})=\textrm{Span}\{\mathbf{v}_1,\mathbf{v}_2\}.$ And since $\mathbf v_1$ and $\mathbf v_2$ are linearly independent, we have $\textrm{rank}(\mathbf{T})=2.$

Finally, using the rank-nullity theorem, we obtain

$$


\begin{aligned}nullity(𝐓) & =3−rank(𝐓) \\ & =3−2 \\ & =1.\end{aligned}


$$

### Example: Finding the Rank or Nullity of a Linear Transformation Using the Rank-Nullity Theorem

#### Question

Consider a linear transformation $\mathbf{T}:\mathbb{R}^3 \to \mathbb{R}^3.$ If $\textrm{nullity}(\mathbf{T})=1,$ then what is $\textrm{rank}(\mathbf{T})?$

#### Explanation

According to the rank-nullity theorem, if $\mathbf{T}:\mathbb{R}^n \to \mathbb{R}^n,$ then

$$


\textrm{rank}(\mathbf{T}) + \textrm{nullity}(\mathbf{T}) = n.


$$

For the given transformation, we have $n=3.$ Therefore,

$$


\begin{aligned}rank(𝐓)+nullity(𝐓) & =𝑛 \\ rank(𝐓)+1 & =3 \\ rank(𝐓) & =3−1 \\ & =2.\end{aligned}


$$

### Example: Finding the Rank or Nullity of a Linear Transformation Given a Description of the Image or Kernel

#### Question

Find $\text{nullity}(\mathbf{T})$ given that $\mathbf{T}:\mathbb{R}^3\to\mathbb{R}^3$ and $\textrm{Im}(\mathbf{T})=\{[x, y, z]^T \,: \, x=y=z\}.$

#### Explanation

Any vector from $\textrm{Im}(\mathbf{T})$ can be written as

$$


\begin{aligned}\begin{aligned}𝑥 \\ 𝑥 \\ 𝑥\end{aligned}=𝑥\underset{𝐯_{1}}{\underset{}\begin{aligned}1 \\ 1 \\ 1\end{aligned}}}.\end{aligned}


$$

This means that $\textrm{Im}(\mathbf{T})=\textrm{Span}\{\mathbf{v}_1\}.$ Therefore, $\textrm{rank}(\mathbf{T})=1.$

Finally, according the rank-nullity theorem, we obtain

$$


\begin{aligned}nullity(𝐓) & =3−rank(𝐓) \\ & =3−1 \\ & =2.\end{aligned}


$$

### Example: Identifying True Statements Using the Rank-Nullity Theorem

#### Question

Let $\mathbf{T}: \mathbb{R}^4 \rightarrow \mathbb{R}^4$ be a linear transformation whose standard matrix is $T,$ and let $\{\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3 \}$ be a set of linearly independent vectors in $\mathbb{R}^4.$ Consider the following statement:

**

Which of the following can be placed into the blank space to make a true statement?

1. $\textrm{rank}(T)=3$

2. $\textrm{nullity}(\mathbf{T})=3$

3. $\mathbf{T}$ is a bijection

#### Explanation

Since $\mathbf{T}$ is a linear transformation from $\mathbb{R}^4$ into $\mathbb{R}^4,$ the invertible matrix theorem states the following:

$\mathbf{T}$ is a bijection (an invertible transformation) $\begin{aligned} & Im(𝐓)=ℝ^{4} \\ & rank(𝐓)=4 \\ & Ker(𝐓)={𝟎} \\ & nullity(𝐓)=0\end{aligned}$

Also, according to the rank-nullity theorem,

$$


\textrm{rank}(\mathbf{T}) + \textrm{nullity}(\mathbf{T}) = 4.


$$

With that in mind, let's examine each statement in turn.

- Statement I is true. Since $\textrm{Im}(\mathbf{T})=\textrm{Span}\{\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3\}$ and the set $\{\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3 \}$ is linearly independent, we get that $\textrm{rank}(T)=\textrm{rank}(\mathbf{T})=3.$

- Statement II is false. According to the rank-nullity theorem, we obtain

- Statement III is false. Since $\textrm{rank}(\mathbf{T}) \neq 4$ (or since $\textrm{nullity}(\mathbf{T}) \neq 0$), the linear transformation $\mathbf{T}$ cannot be a bijection according to the invertible matrix theorem.

Therefore, the correct option is "I only."
