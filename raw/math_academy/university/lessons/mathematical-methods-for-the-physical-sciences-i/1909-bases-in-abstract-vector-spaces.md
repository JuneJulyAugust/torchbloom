# Bases in Abstract Vector Spaces

Source: https://www.mathacademy.com/topics/1909?courseId=154
Topic ID: 1909

## Prerequisites

- [Finding a Basis of a Span](./1855-finding-a-basis-of-a-span.md)
- [Linear Independence in Abstract Vector Spaces](./1908-linear-independence-in-abstract-vector-spaces.md)

## Lesson

### Introduction

A set of vectors

$$


\mathcal{B}=\{ \mathbf{b}_1,\mathbf{b}_2, \ldots, \mathbf{b}_n \}


$$

is called a **basis** of an abstract vector space $V$ if the following two conditions hold:

- $\mathcal{B}$ is linearly independent, and

- $\mathcal{B}$ spans $V.$

For example, let's consider the vector space $\mathbb{R}_2[t]$ of all polynomials in the variable $t$ over $\mathbb R$ with degree at most $2,$ and its subset

$$


\mathcal{B} = \left\{ {\color{blue}{1}}, {\color{blue}{t}}, {\color{blue}{t^2}} \right\}.


$$

Is $\mathcal{B}$ a basis for $\mathbb{R}_2[t]?$ Let's check our two conditions.

- First, we check for linear independence. Notice that the equation is true for all $t$ if and only if Therefore, the set $\mathcal{B}$ is linearly independent in $\mathbb{R}_2[t].$

- Next, we check that $\mathcal B$ spans $\mathbb{R}_2[t].$ Notice that we can write any polynomial $at^2+bt+c\in\mathbb{R}_2[t]$ as a linear combination of vectors from $\mathcal{B} \mathbin{:}$ Therefore, $\mathcal B$ spans $\mathbb{R}_2[t].$

Since both conditions hold, we conclude that $\mathcal{B} = \{{1}, {t}, {t^2} \}$ is a basis of $\mathbb{R}_2[t]$.

### Example: Identifying True Statements About Sets of Vectors in a Polynomial Vector Space

#### Question

Consider the vector space $\mathbb{R}_2[t]$ of all polynomials in the variable $t$ over $\mathbb R$ with degrees at most $2.$

Which of the following statements are true?

1. $\big\{0,t^2 \big\}$ is a linearly independent set in $\mathbb{R}_2[t]$

2. $-5t^2$ can be expressed as a linear combination of $\big\{0, t^2 \big\}$

3. $\big\{0, t^2 \big\}$ is a basis of $\mathbb{R}_2[t]$

#### Explanation

Let's examine each of the statements in turn.

- Statement I is false. Notice that where the first coefficient is nonzero, so the set is linearly dependent. In general, any set that contains a zero-vector is linearly dependent.

- Statement II is true. Indeed,

- Statement III is false. Since the set is not linearly independent, it can't form a basis.

Therefore, the correct answer is "II only."

### Example: Identifying True Statements About Sets of Vectors in a Matrix Vector Space

#### Question

Consider the vector space $\text{M}_2(\mathbb{R})$ of all $2 \times 2$ matrices over $\mathbb{R}.$

Which of the following statements are true?

1. $[\begin{aligned}0 & −1 \\ 0 & 0\end{aligned}]$ is a linearly independent set in $\text{M}_2(\mathbb{R})$

2. $[\begin{aligned}0 & −2 \\ 0 & 4\end{aligned}]$ can be expressed as a linear combination of $[\begin{aligned}0 & −1 \\ 0 & 0\end{aligned}]$

3. $[\begin{aligned}0 & −1 \\ 0 & 0\end{aligned}]$ is a basis of $\text{M}_2(\mathbb{R})$

#### Explanation

Let's examine each of the statements in turn.

- Statement I is true. Indeed, the equation is true if and only if $x_1=x_2=0.$ So, the set is linearly independent.

- Statement II is true. Indeed,

- Statement III is false. For example, the matrix $[\begin{aligned}1 & −1 \\ 0 & 5\end{aligned}]$ can't be written as a linear combination of since all these linear combinations result in matrices with the entry $a_{11} = 0\mathbin{:}$

Therefore, the correct answer is "I and II only."

### An Alternative Definition

A set of vectors $\mathcal{B}=\{\mathbf{b}_1,\mathbf{b}_2, \ldots, \mathbf{b}_n \}$ is a basis of a vector space $V$ if $\mathcal{B}$ is a **maximally linearly independent set in $V$**. In other words, $\mathcal{B}$ is linearly independent and for any vector ${\color{blue}\mathbf{w}} \in V,$ the set

$$


\mathcal{B} \cup \{ {\color{blue}\mathbf{w}} \} = \{ \mathbf{b}_1,\mathbf{b}_2, \ldots, \mathbf{b}_n, {\color{blue}\mathbf{w}} \}


$$

is linearly dependent.

### Example: Identifying True Statements About Bases of Abstract Vector Spaces

#### Question

Let $\mathcal{B}= \left\{\mathbf{b_1}, \mathbf{b_2}, \mathbf{b_3} \right\}$ be a basis of a vector space $V.$

Which of the following statements are true?

1. $\left\{\mathbf{b_2},- \mathbf{b_1}, \mathbf{b_3}+\mathbf{b_1} \right\}$ is a basis of $V$

2. $\left\{\mathbf{b_2}, \mathbf{b_3}, \mathbf{0} \right\}$ spans $V$

3. $\left\{-\mathbf{b_2}, 3\mathbf{b_1}\right\}$ is linearly dependent

#### Explanation

Since $\mathcal{B}$ is a basis, the following properties must hold:

- $\mathcal{B}$ is a maximally linearly independent set of vectors in $V,$ and

- $\mathcal{B}$ spans $V.$

With that in mind, let's examine our statements.

- Statement I is true. Indeed, the equation is equivalent to which, since $\left\{\mathbf{b_1}, \mathbf{b_2}, \mathbf{b_3} \right\}$ is linearly independent, gives Also, $\left\{\mathbf{b_2},- \mathbf{b_1}, \mathbf{b_3}+\mathbf{b_1} \right\}$ spans $V$ since any linear combination of vectors from $\mathcal{B}$ can be expressed as a linear combination of $\left\{\mathbf{b_2},- \mathbf{b_1}, \mathbf{b_3}+\mathbf{b_1} \right\}\mathbin{:}$

- Statement II is false. In order for $\left\{\mathbf{b_2}, \mathbf{b_3}, \mathbf{0} \right\}$ to span $V,$ every element of $\mathcal{B}$ must be able to be expressed as a linear combination of elements of $\left\{\mathbf{b_2}, \mathbf{b_3}, \mathbf{0} \right\}.$ But the vector $\mathbf{b}_1 \in \mathcal{B}$ can't be written as a linear combination of the elements of $\left\{\mathbf{b_2}, \mathbf{b_3}, \mathbf{0} \right\}.$

- Statement III is false. If $\left\{-\mathbf{b_2}, 3\mathbf{b_1}\right\}$ is linearly dependent then there exist $x_1$ and $x_2$ not both zero such that Then, we would have But this would mean that $\mathcal{B} = \left\{\mathbf{b_1}, \mathbf{b_2}, \mathbf{b_3} \right\}$ is linearly dependent, which contradicts the fact that $\mathcal{B}$ is a basis of $V.$

Therefore, the correct answer is "I only."

### Some Important Standard Bases

Let $\mathbb{R}_n[t]$ denote the vector space of all polynomials in the variable $t$ over $\mathbb{R}$ that have degree at most $n.$ Also, let $\text{M}_2(\mathbb{R})$ be the vector space of all $2 \times 2$ matrices over $\mathbb{R}.$ Then, we have the following important standard bases.

- The standard basis of $\mathbb{R}_1[t]$ is $\{1, \: t \}.$

- The standard basis of $\mathbb{R}_2[t]$ is $\{1, \: t, \: t^2 \}.$

- The standard basis of $\mathbb{R}_n[t]$ is $\{1, \: t, \: \ldots, \: t^n \}.$

- The standard basis of $\text{M}_2(\mathbb{R})$ is
