# Defining Abstract Vector Spaces

Source: https://www.mathacademy.com/topics/3835?courseId=154
Topic ID: 3835

## Prerequisites

- [Introduction to Abstract Vector Spaces](./1906-introduction-to-abstract-vector-spaces.md)

## Lesson

### Introduction

In previous lessons, we've seen how some sets equipped with addition and scalar multiplication operations exhibit properties similar to $\mathbb R^n.$

In this lesson, we will formally define what we mean by a **vector space.**

First, let $V$ be a set equipped with the following two operations:

Vector addition:

For any two elements $\mathbf{x}, \mathbf{y} \in V,$ there is a unique element $\mathbf{x}+\mathbf{y}$ that also lies in $V.$ We say that $V$ is **closed under vector addition.**

Scalar multiplication:

For any element $\mathbf{x} \in V$ and any number $\alpha \in \mathbb{R},$ there is a unique element $\alpha \mathbf{x}$ that also lies in $V.$ We say that $V$ is **closed under scalar multiplication.**

A set $V$ equipped with vector addition and scalar multiplication forms a **vector space** if it satisfies the following **vector space axioms**.

#### Axioms of Vector Addition ($+$)

- $\color{black}\text{[A1]}$: $\color{blue}\mathbf{x}+\mathbf{y} = \mathbf{y}+\mathbf{x}$ for any $\mathbf{x}, \mathbf{y} \in V$; vector addition is **commutative**.

- $\color{black}\text{[A2]}$: $\color{blue}(\mathbf{x}+\mathbf{y})+\mathbf{z} = \mathbf{x}+(\mathbf{y}+\mathbf{z})$ for any $\mathbf{x}, \mathbf{y}, \mathbf{z} \in V$; vectors addition is **associative**.

- $\color{black}\text{[A3]}$: There exists a **zero-vector** $\mathbf{0}$ such that $\color{blue}\mathbf{x} + \mathbf{0} = \mathbf{x}$.

- $\color{black}\text{[A4]}$: For every $\mathbf{x} \in V,$ there exists $-\mathbf{x} \in V$ such that $\color{blue}\mathbf{x} + (-\mathbf{x}) = \mathbf{0}$; $-\mathbf{x}$ is called the **negative** of $\mathbf{x}$.

#### Axioms of Scalar Multiplication ($\cdot$)

- $\color{black}\text{[A5]}$: $\color{blue}1 \cdot \mathbf{x} = \mathbf{x}$ for any $\mathbf{x} \in V$; multiplying by $1$ does not change a vector.

- $\color{black}\text{[A6]}$: $\color{blue}\alpha (\beta \mathbf{x}) = (\alpha\beta) \mathbf{x}$ for any numbers $\alpha,\beta \in \mathbb{R}$ and any vector $\mathbf{x} \in V$.

#### Axioms Connecting Vector Addition and Scalar Multiplication (the Distributive Laws)

- $\color{black}\text{[A7]}$: $\color{blue}(\alpha + \beta)\mathbf{x} = \alpha \mathbf{x} + \beta \mathbf{x}$ for any numbers $\alpha,\beta \in \mathbb{R}$ and any vector $\mathbf{x} \in V$.

- $\color{black}\text{[A8]}$: $\color{blue}\alpha (\mathbf{x} + \mathbf{y}) = \alpha \mathbf{x} + \alpha \mathbf{y}$ for any number $\alpha \in \mathbb{R}$ and any vectors $\mathbf{x}, \mathbf{y} \in V$.

So, a vector space is simply a collective term for all kinds of sets equipped with addition and scalar multiplication, where these operations satisfy this particular list of axioms (which are similar to the properties of these operations in $\mathbb{R}^n$).

The elements of any vector space are called **vectors**.

### Important Vector Spaces

There are many different vector spaces. Some of the most important are listed below.

- $\mathbb{R}^n$, the set of all column vectors of height $n$ with elements from $\mathbb{R}$

- $\text{M}_n(\mathbb{R})$, the set of all $n \times n$ matrices with elements from $\mathbb{R}$

- $\mathbb{R}[t]$, the set of all polynomials in the variable $t$ and with coefficients from $\mathbb{R}$

- $\mathbb{R}_n[t]$, the set of all polynomials of degree less than or equal to $n$ in the variable $t$ and with coefficients from $\mathbb{R}$

- The set of all real-valued functions of one variable.

### Example: Identifying Sets That Are Not Vector Spaces

#### Question

Let $V$ be the set of all real polynomials of degree exactly $3$, equipped with the usual addition and scalar multiplication operations. Complete the following sentence:

**

1. the sum of two polynomials of degree $3$ may not be a polynomial of degree $3$

2. $V$ does not contain the polynomial $-p(x)$ for every $p(x) \in V$

3. addition of polynomials is not commutative

#### Explanation

The correct answer is as follows:

**

For instance, if $p(x) = 1 +x^3$ and $q(x) = 1-x^3$, then $p(x)$ and $q(x)$ are in $V.$ However

$$


\begin{aligned}𝑝(𝑥)+𝑞(𝑥) & =(1+𝑥^{3})+(1−𝑥^{3}) \\ & =2∉𝑉.\end{aligned}


$$

On the other hand:

- Addition of polynomials is commutative.

- For any polynomial $p(x)$ of degree $3$, the corresponding negative polynomial $-p(x)$ also has degree $3.$

### Example: Proving Statements Using the Vector Space Axioms

#### Question

From top to bottom, fill in the blanks and hence complete the proof of the following statement using the axioms $[\textrm A1] - [\textrm A8]$ given below.

**

**

**

$$


\begin{aligned}𝐰+𝐰 & =𝐰 & & [\,given\,] \\ (𝐰+𝐰)+(−𝐰) & =𝐰+(−𝐰) & & [\,add -\mathbf{w} to both sides\,] \\ 𝐰+(𝐰+(−𝐰)) & =𝐰+(−𝐰) & & [\,axiom \underline{\hspace{3em}}\,\,] \\ 𝐰+𝟎 & =𝟎 & & [\,axiom A4\,] \\ 𝐰 & =𝟎 & & [\,axiom \underline{\hspace{3em}}\,\,]\end{aligned}


$$

The axioms:

$$


\begin{aligned}[A1]:𝐱+𝐲=𝐲+𝐱 & [A5]:1⋅𝐱=𝐱 \\ [A2]:(𝐱+𝐲)+𝐳=𝐱+(𝐲+𝐳) & [A6]:𝛼(𝛽𝐱)=(𝛼𝛽)𝐱 \\ [A3]:𝐱+𝟎=𝐱 & [A7]:(𝛼+𝛽)𝐱=𝛼𝐱+𝛽𝐱 \\ [A4]:𝐱+(−𝐱)=𝟎 & [A8]:𝛼(𝐱+𝐲)=𝛼𝐱+𝛼𝐲\end{aligned}


$$

#### Explanation

Using the axioms of a vector space, we obtain the following:

$$


\begin{aligned}𝐰+𝐰 & =𝐰 & & [\,given\,] \\ (𝐰+𝐰)+(−𝐰) & =𝐰+(−𝐰) & & [\,add -\mathbf{w} to both sides\,] \\ 𝐰+(𝐰+(−𝐰)) & =𝐰+(−𝐰) & & [\,axiom {\color{blue}\text{A2}}\,] \\ 𝐰+𝟎 & =𝟎 & & [\,axiom A4\,] \\ 𝐰 & =𝟎 & & [\,axiom {\color{blue}\text{A3}}\,]\end{aligned}


$$
