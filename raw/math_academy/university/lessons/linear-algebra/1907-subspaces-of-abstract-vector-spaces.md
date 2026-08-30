# Subspaces of Abstract Vector Spaces

Source: https://www.mathacademy.com/topics/1907?courseId=55
Topic ID: 1907

## Prerequisites

- [Continuity Over an Interval](../../../ap-courses/lessons/ap-calculus-ab/612-continuity-over-an-interval.md)
- [Defining Abstract Vector Spaces](./3835-defining-abstract-vector-spaces.md)
- [Subspaces of N-Dimensional Space: Geometric Interpretation](./4077-subspaces-of-n-dimensional-space-geometric-interpretation.md)

## Lesson

### Introduction

Given a vector space $V$, any subset $H$ of $V,$ which is itself a vector space, is called a **subspace** of $V$.

Fortunately, we do not need to check all vector space axioms to determine whether a subset of some vector space is a subspace. Instead, we only need to check the **subspace criterion**, which states the following:

*A subset $H$ of a vector space $V$ is a subspace of $V$ if and only if $H$ is closed under vector addition and scalar multiplication. That is to say, both of the following conditions hold:*

- *If $\mathbf{u}$ and $\mathbf{v}$ lie in $H$, then their sum $\mathbf{u}+\mathbf{v}$ also lies in $H$. Formally,*

- *If $\mathbf{u}$ lies in $H$, then $k \cdot \mathbf{u}$ also lies in $H$ for any scalar $k$. Formally,*

For example, consider the vector space $\mathbb{R}_3[t]$ containing all polynomials of degree at most $3,$ along with the subset

$$


A = \{ at^2 \:|\: a \in \mathbb{R} \}.


$$

Is $A$ a subspace? Let's check the two subspace criterion conditions:

- Suppose $p_1(t)=a_1 t^2$ and $p_2(t)=a_2 t^2$ are two polynomials from $A$. Summing the two polynomials, we get Thus, $p_1(t)+p_2(t)$ is a polynomial of the form $at^2,$ which belongs to $A$.

- If $p_1(t)=a_1 t^2 \in A$ and $k \in \mathbb{R},$ then Thus, $kp_1(t)$ is a polynomial of the form $at^2,$ which belongs to $A$.

Since both conditions hold, we conclude that $A$ is a subspace $\mathbb{R}_3[t].$

### Example of a Subset That Is Not a Subspace

Let's now look at an example of a subset of a vector space that is not a subspace.

Consider the vector space $\mathbb R_2[t]$ of all polynomials in the variable $t$ of degree at most $2,$ and its subset

$$


B = \big\{ at+b \: | \: a,b \in\mathbb{Z} \big\}.


$$

Recall that a subset of a vector space is a subspace if it's closed under addition and scalar multiplication.

- $B$ is closed under polynomial addition. Indeed, suppose that $f(t)=a_1t+b_1$ and $g(t)=a_2t+b_2$ are two polynomials from $B.$ Then, which is a polynomial from $B$ since $a_1+a_2$ and $b_1+b_2$ are in $\Bbb Z.$

- $B$ is *not* closed under scalar multiplication. As a counterexample, consider $f(t)=t$ and $k=0.5,$ then which is *not* a polynomial from $B,$ because $0.5 \notin \Bbb Z.$

Therefore, $B$ is not a subspace of $\mathbb R_2[t].$

### Example: Identifying Subspaces of Polynomial Vector Spaces

#### Question

Consider the vector space $\mathbb R_3[t]$ of all polynomials in the variable $t$ of degree at most $3,$ and its subset $A = \big\{at^3-bt \: | \: a,b \in\mathbb{R} \big\}.$

Which of the following statements are true?

1. $A$ is closed under polynomial addition

2. $A$ is closed under scalar multiplication

3. $A$ is a subspace of $\mathbb R_3[t]$

4. $A$ is **** a subspace of $\mathbb R_3[t]$

#### Explanation

Recall that a subset of a vector space is a subspace if it's closed under addition and scalar multiplication.

With that in mind, let's examine each statement in turn.

- Statement I is true. If $f(t)=a_1t^3-b_1t$ and $g(t)=a_2t^3-b_2t$ are two polynomials from $A,$ then which is a polynomial from $A.$ So, $A$ is closed under addition.

- Statement II is true. If $f(t)=at^3-bt \in A$ and $k \in \mathbb{R},$ then which is a polynomial from $A.$ So, $A$ is closed under scalar multiplication.

- Statement III is true. $A$ is a subspace because it's closed under addition and scalar multiplication.

Therefore, the correct answer is "I, II, and III only."

### Example: Identifying Subspaces of Matrix Vector Spaces

#### Question

Consider the vector space $\text{M}_2(\mathbb{R})$ of all $2\times 2$ matrices over $\mathbb{R},$ and its subset $N$ containing all $2\times 2$ matrices such that the sum of the elements on the main diagonal is greater or equal to $0.$

Which of the following statements are true?

1. $N$ is closed under matrix addition

2. $N$ is closed under scalar multiplication

3. $N$ is a subspace of $\text{M}_2(\mathbb{R})$

4. $N$ is **** a subspace of $\text{M}_2(\mathbb{R})$

#### Explanation

Recall that a subset of a vector space is a subspace if it's closed under addition and scalar multiplication.

With that in mind, let's examine each statement in turn.

- Statement I is true. If $A_1$ and $A_2$ are two matrices from $N,$ then the sum of the elements on the main diagonal for each matrix is greater or equal to $0.$ Therefore, $A_1+A_2$ is a matrix where the sum of the elements on the main diagonal is greater or equal to $0.$ This matrix belongs to $N,$ and so $N$ is closed under addition.

- Statement II is false. If $A$ is an element of $N,$ then the sum of the elements on the main diagonal is greater than or equal to $0.$ If we let $k=-1 \in \mathbb{R},$ then $kA$ is a matrix where the sum of the elements on the main diagonal is less than or equal to $0.$ This matrix does not belong to $N,$ and so $N$ is ** closed under scalar multiplication.

- Statement III is false, while statement IV is true. $N$ is a ** subspace because it's not closed under scalar multiplication.

Therefore, the correct answer is "I and IV only."

### Example: Identifying Subspaces of Function Vector Spaces

#### Question

Consider the vector space $\mathcal{C}[-1,3]$ of all continuous functions $f:[-1,3] \to \mathbb{R}$ and its subset $A = \big\{f \in \mathcal{C}[-1,3] \: | \: f(0)=-f(2) \big\}.$

Which of the following statements are true?

1. $A$ is closed under function addition

2. $A$ is closed under scalar multiplication

3. $A$ is a subspace of $\mathcal{C}[-1,3]$

4. $A$ is **** a subspace of $\mathcal{C}[-1,3]$

#### Explanation

Recall that a subset of a vector space is a subspace if it's closed under addition and scalar multiplication.

With that in mind, let's examine each statement in turn.

- Statement I is true. If $f(x),g(x) \in A,$ then which means $f+g \in A.$ So, $A$ is closed under addition.

- Statement II is true. If $f(x) \in A$ and $k \in \mathbb{R},$ then which means $kf \in A.$ So, $A$ is closed under scalar multiplication.

- Statement III is true. $A$ is a subspace because it's closed under addition and scalar multiplication.

Therefore, the correct answer is "I, II, and III only."
