# Introduction to Abstract Vector Spaces

Source: https://www.mathacademy.com/topics/1906?courseId=145
Topic ID: 1906

## Prerequisites

- [Multiplying Complex Numbers](../algebra-ii/33-multiplying-complex-numbers.md)
- [The Arithmetic of Functions](../algebra-i/140-the-arithmetic-of-functions.md)
- [Scalar Multiplication of Matrices](../integrated-math-iii-honors/146-scalar-multiplication-of-matrices.md)
- [Closure Properties of Polynomials](../integrated-math-iii-honors/942-closure-properties-of-polynomials.md)
- [Linear Combinations of Vectors in N-Dimensional Euclidean Space](./1851-linear-combinations-of-vectors-in-n-dimensional-euclidean-space.md)
- [Sets and Functions](./3334-sets-and-functions.md)

## Lesson

### Introduction

The structure $\mathbb{R}^n$ is called a **vector space**. However, many other structures possess properties similar to $\mathbb{R}^n.$ These other structures can be called vector spaces too.

In this lesson, we'll learn about some important properties used to construct vector spaces. We begin by discussing what it means for a set to be **closed** under addition and scalar multiplication.

As an example, consider the set $\mathrm{M}_2(\mathbb{R})$ of all $2 \times 2$ matrices with real entries:

$$


[\begin{aligned}𝑎 & 𝑏 \\ 𝑐 & 𝑑\end{aligned}]


$$

For this set of matrices, we can define two operations:

- the addition of two matrices, and

- the multiplication of a matrix by a real number (called a scalar).

Now, notice the following:

- $\mathrm{M}_2(\mathbb{R})$ is **closed under addition**. This means that the sum of *any* two matrices from $\mathrm{M}_2(\mathbb{R})$ is also a matrix in $\mathrm{M}_2(\mathbb{R}).$

- $\mathrm{M}_2(\mathbb{R})$ is **closed under scalar multiplication**. This means that the product of *any* scalar and *any* matrix from $\mathrm{M}_2(\mathbb{R})$ is also a matrix in $\mathrm{M}_2(\mathbb{R}).$

Identifying that a set is closed under addition and scalar multiplication is an essential first step in determining whether a set can form a vector space.

### Sets That Are Not Closed

It's important to realize that not all sets are closed under addition and scalar multiplication. Sets not closed under addition and scalar multiplication *cannot* be vector spaces.

For instance, let $S$ be the set of all polynomials with real coefficients whose degree is greater than or equal to $5.$

We note that $S$ is not closed under addition. To see why this is the case, let's define the polynomials $p(x),q(x)\in S$ as

$$


p(x) = x^5, \qquad q(x) = 1-x^5.


$$

Adding the two polynomials using regular polynomial addition, we get

$$


p(x) + q(x) = x^5 + (1-x^5) = 1\notin S


$$

The sum $p(x) + q(x)$ is not in $S$ because it is a polynomial of degree zero, which is less than $5.$

Therefore, we conclude that our set $S$ is *not* closed under addition.

### Example: Identifying Sets Closed Under Addition and Scalar Multiplication

#### Question

Let $M$ be the set of all $2\times2$ real matrices whose entries are non-negative. Then, which of the following statements are true?

1. $I_2 \in M$

2. For any $A \in M$ and $\alpha \in \mathbb{R}$, we have $\alpha \cdot A \in M.$

3. The set is closed under scalar multiplication.

#### Explanation

Let's verify the statements one by one.

- Statement I is true. Indeed, $[\begin{aligned}1 & 0 \\ 0 & 1\end{aligned}]$ because all its entries are non-negative.

- Statement II is false. There exists a $2\times2$ real matrix in $M$ that has a scalar multiple not in $M.$ For example, let $[\begin{aligned}1 & 0 \\ 0 & 1\end{aligned}]$ and $\alpha=-1\in\mathbb{R}.$ Notice that $A$ belongs to $M$ since statement I is true. However, Since the entries on the main diagonal are negative, we conclude that $-1 \cdot A \notin M.$

- Statement III is false. Since statement II is false, the set is ** closed under scalar multiplication.

Therefore, the correct answer is "I only."

### Addition of Vectors

Let's now compare some properties of addition in $\mathbb{R}^2$ and $\text{M}_2(\mathbb{R}).$ It turns out that the addition of two matrices in $\mathrm{M}_2(\mathbb{R})$ is *very* similar to the addition of two vectors in $\mathbb{R}^n.$ See the table below.

And it's not just matrices that have additive properties similar to those of $\mathbb R^n.$ Many mathematical structures do. Let's see some more examples.

### Example: Verifying Properties Involving Vector Addition

#### Question

Let $L$ be the set of all polynomials with real coefficients whose degree is less than or equal to $2.$ Which of the following statements are true?

1. For any $p(x),q(x) \in L,$ we have $p(x)+q(x) = q(x)+p(x).$

2. For any $p(x),q(x),r(x) \in L,$ we have $[p(x)+q(x)]+r(x) = p(x)+[q(x)+r(x)].$

3. For each $p(x) \in L,$ we have $-p(x) \in L$ such that $p(x)+(-p(x))=0.$

#### Explanation

Let's examine our statements one at a time.

- Statement I is true. Indeed, for any polynomials $p(x), q(x) \in L,$ we obtain that since polynomial addition is commutative.

- Statement II is true. Indeed, for any polynomials $p(x),q(x),r(x) \in L,$ we obtain that since polynomial addition is associative.

- Statement III is true. Indeed, for any polynomial $p(x) \in L,$ there is a corresponding negative polynomial $-p(x)$ such that Notice that hence $-p(x) \in L.$

Therefore, the correct answer is "I, II, and III."

### Scalar Multiplication and the Distributive Laws

Let's also compare some properties of scalar multiplication in $\mathbb{R}^2$ and $\text{M}_2(\mathbb{R}).$ It turns out that the multiplication of a matrix in $\mathrm{M}_2(\mathbb{R})$ by a scalar is *very* similar to the multiplication of a vector in $\mathbb{R}^n$ by a real number. See the table below.

### Example: Verifying Properties Involving Scalar Multiplication and the Distributive Laws

#### Question

Let $P$ be the set of all $2\times 2$ real matrices $A= (a_{ij})$ such that $a_{11} + a_{22} > 0.$ Which of the following properties are true?

1. For any $A \in P,$ we have $1 \cdot A = A.$

2. For any $A \in P$ and $\alpha,\beta \in \mathbb{R},$ we have $\alpha(\beta A) = (\alpha\beta) A.$

3. For any $A \in P$ and $\alpha,\beta \in \mathbb{R},$ we have $(\alpha+\beta) A= \alpha A + \beta A.$

#### Explanation

Let's verify the statements one by one.

- Statement I is true. Indeed, for any $2\times 2$ matrix $A = (a_{ij}) \in P,$ the entries are just real numbers. Thus, we have and hence,

- Statements II is true. Indeed, for any $2\times 2$ matrix $A = (a_{ij}) \in P,$ the entries are just real numbers. Thus, for any $\alpha, \beta \in \mathbb{R},$ we obtain that and hence,

- Statements III is true. Indeed, for any $2\times 2$ matrix $A = (a_{ij}) \in P,$ the entries are just real numbers. Thus, for any $\alpha, \beta \in \mathbb{R},$ we obtain that and hence,

Therefore, the correct answer is "I, II, and III."

### A Summary of the Addition and Scalar Multiplication Properties of Euclidian Space

In this lesson, we discussed several properties exhibited by vectors in $\mathbb R^n$ and other sets. Let's consolidate these properties into a single list.

We'll meet these properties again in a future lesson, where we'll formally define what we mean by a vector space.
