# Proving Divisibility Using Induction

Source: https://www.mathacademy.com/topics/646?courseId=76
Topic ID: 646

## Prerequisites

- [Mathematical Induction](./642-mathematical-induction.md)
- [Expanding Binomials Using Pascal's Triangle](../../../high-school/traditional/lessons/algebra-i/1157-expanding-binomials-using-pascal-s-triangle.md)

## Lesson

### Introduction

Recall that the **principle of induction** states the following:

*Suppose we have a sequence of mathematical statements $P(1), \, P(2), \, P(3), \, \ldots,$ where*

- *$P(1)$ is true, and*

- *$P(k)\Rightarrow P(k+1)$ for every $k\in\mathbb N.$*

*Then, $P(n)$ is true for every $n\in\mathbb N.$*

Let's recall our general strategy for proving results using induction:

- **Step 1**: Base Case

- **Step 2**: Inductive Hypothesis

- **Step 3**: Inductive Step

- **Step 4**: Conclusion

In this lesson, we'll learn how induction can be used to prove divisibility statements.

### A Worked Example

Let's prove that the following statement is true using mathematical induction:

$n^2+5n$ is even for all $n \in \mathbb{N}$

In this case, the general statement $P(n)$ we're required to prove is the following:

$P(n): \quad 2\,\mid\, n^2+5n$ for all $n \in \mathbb{N}$

We start by proving the base case, $P(1).$ To do this, we substitute $n=1$ into the expression and show it is divisible by $2{:}$

**Base Case**: We first prove our statement is true for the base case $n=1.$ Substituting $n=1$ into the expression $n^2+5n,$ we have

$$


P(1): \quad 1^2+5(1) = 6,\quad\text{and}\quad 2\,\mid\,6.


$$

Thus, our statement is true for $n=1.$

Next, we state our inductive hypothesis. Here, we assume that the given statement is true for some $n = k \geq 1.$

**Inductive Hypothesis**: We assume that for some $n = k \geq 1,$ we have that

$$


P(k): \quad 2\,\mid\,k^2+5k.


$$

We must show that $P(k) \Rightarrow P(k+1).$ Let's start by writing down $P(k+1).$ This is the first part of the **inductive step**.

**Inductive Step**: We're required to prove that

$$


P(k+1): \quad \quad 2\,\mid\, (k+1)^2 +5(k+1)\qquad\qquad (\ast)


$$

The idea is to rewrite the expression $(k+1)^2 +5(k+1)$ as $k^2+5k$ (from the inductive hypothesis) plus a multiple of $2.$ We do this as follows:

We write

$$


\begin{aligned}(𝑘+1)^{2}+5(𝑘+1) & =𝑘^{2}+2𝑘+1+5𝑘+5 \\ & =𝑘^{2}+5𝑘+2𝑘+6 \\ & =𝑘^{2}+5𝑘+2(𝑘+3).\end{aligned}


$$

Now, since $2\,\mid\,(k^2+5k)$ by the inductive hypothesis, and $2(k+3)$ is clearly divisible by $2,$ their sum is also divisible by $2,$ as required.

Since we have shown that the expression in $(\ast)$ is divisible by $2,$ our proof is complete. So, let's write down our conclusion.

Therefore, by the principle of induction, $2\,\mid\, n^2+5n$ for all $n \in \mathbb{N}.$

### Example: Completing a Proof Template

#### Question

Suppose we wish to prove the following statement using mathematical induction:

$5 \,\mid\, 6^n +4$ for all $n \in \mathbb{N}$

What are the missing entries in the proof template outlined below?

****: We first prove that our statement is true for the base case $n=1.$

$$


0000


$$

****: We assume that for some $000$ we have that

$$


000000


$$

****: We're required to prove that

$$


000000


$$

****: Therefore, $5 \,\mid\, 6^n +4$ for all $n\in \mathbb{N}.$

#### Explanation

To prove a statement using induction, we use the following framework:

- ****: Base Case

- ****: Inductive Hypothesis

- ****: Inductive Step

- ****: Conclusion

In this case, the general statement $P(n)$ we're required to prove is the following:

$$


5 \,\mid\, 6^n +4


$$

We start by proving the ****, $P(1).$ To do this, we substitute $n=1$ into the expression.

In our case, this gives the following:

****: We first prove that our statement is true for the base case $n=1.$

$$


\boxed{\color{blue}6^1 +4}= \boxed{\color{blue}10},\quad \text{and}\quad \boxed{\color{blue}5\,\mid \,10}


$$

Next, we write down our ****. We assume that $P(k)$ is true for some $n = k \geq 1.$ To do this, we simply replace $n$ with $k$ in our original statement.

In our case, this gives the following:

****: We assume that for some $n = \boxed{\color{blue}k \geq 1},$ we have that

$$


\boxed{\color{blue}5 \,\mid\, 6^k +4}.


$$

Then, we move onto the ****: We must show that $P(k) \Rightarrow P(k+1).$ We start by writing down $P(k+1).$

****: We're required to prove that

$$


\boxed{\color{blue}5 \,\mid\, 6^{k+1} +4}.


$$

The inductive step is where most of the work lies. The idea is to rewrite the expression using the inductive hypothesis and apply algebraic techniques to show that this is a multiple of $5.$

Once we've shown that $P(k) \Rightarrow P(k+1),$ the proof is complete, and we state our ****.

****: Therefore, $5 \,\mid\, 6^n +4$ for all $n \in \mathbb{N}.$

### Example: Proving Polynomial Divisibility

#### Question

Use mathematical induction to prove that $n^3-n$ is divisible by $3$ for all $n \in \mathbb{N}.$

#### Explanation

The principle of induction states the following: Suppose we have a sequence of mathematical statements $P(1), P(2), P(3), \ldots,$ where

- $P(1)$ is true, and

- $P(k) \Rightarrow P(k+1)$ for every $k \in \mathbb{N}.$

Then, $P(n)$ is true for every $n \in \mathbb{N}.$

In this case, the general statement $P(n)$ we're required to prove is the following:

$P(n): \quad 3\,\mid\, n^3-n$ for all $n \in \mathbb{N}$

We start by proving the base case, $P(1).$ To do this, we substitute $n=1$ into the expression and show it is divisible by $3{:}$

We proceed using induction on $n.$

****: We first prove that our statement is true for the base case $n=1.$ Substituting $n=1$ into the expression $n^3-n,$ we have

$$


P(1): \quad 1^3-1 = 0, \quad\text{and}\quad 3 \,\mid\, 0


$$

Thus, our statement is true for $n=1.$

Next, we state our inductive hypothesis. Here, we assume that the given statement is true for some $n = k \geq 1.$

****: We assume that for some $n = k \geq 1,$ we have that

$$


P(k): \quad 3\,\mid\, k^3-k.


$$

We must show that $P(k) \Rightarrow P(k+1).$ Let's start by writing down $P(k+1).$ This is the first part of the ****.

****: We're required to prove that

$$


P(k+1): \quad 3\,\mid\, (k+1)^3-(k+1). \qquad\qquad (\ast)


$$

The idea is to rewrite the expression $(k+1)^3-(k+1)$ as $k^3-k$ (from the inductive hypothesis) plus a multiple of $3.$ We do this as follows:

We write

$$


\begin{aligned}(𝑘+1)^{3}−(𝑘+1) & =𝑘^{3}+3𝑘^{2}+3𝑘+1−𝑘−1 \\ & =𝑘^{3}+3𝑘^{2}+2𝑘 \\ & =(𝑘^{3}−𝑘)+3(𝑘^{2}+𝑘).\end{aligned}


$$

Now, since $3\,\mid\,(k^3-k)$ by the inductive hypothesis, and $3(k^2+k)$ is clearly divisible by $3,$ their sum is also divisible by $3,$ as required.

Since we have shown that the expression in $(\ast)$ is divisible by $3,$ our proof is complete. So, let's write down our conclusion.

Therefore, by the principle of induction, $3 \,\mid\, n^3-n$ for all $n \in \mathbb{N}.$

### Example: Proving Divisibility of Exponential Expressions

#### Question

Use mathematical induction to prove that $10^{n}+2$ is divisible by $3$ for all $n \in \mathbb{N}.$

#### Explanation

The principle of induction states the following: Suppose we have a sequence of mathematical statements $P(1), P(2), P(3), \ldots,$ where

- $P(1)$ is true, and

- $P(k) \Rightarrow P(k+1)$ for every $k \in \mathbb{N}.$

Then, $P(n)$ is true for every $n \in \mathbb{N}.$

In this case, the general statement $P(n)$ we're required to prove is the following:

$P(n):\quad3\,\mid\, 10^{n}+2$ for all $n \in \mathbb{N}$

We start by proving the base case, $P(1).$ To do this, we substitute $n=1$ into the expression and show it is divisible by $3{:}$

We proceed using induction on $n.$

****: We first prove that our statement is true for the base case $n=1.$ Substituting $n=1$ into the expression $10^{n}+2,$ we have

$$


10^{1}+2 = 12, \quad\text{and}\quad 3\,\mid\, 12.


$$

Thus, our statement is true for $n=1.$

Next, we state our inductive hypothesis. Here, we assume that the given statement is true for some $n = k \geq 1.$

****: We assume that for some $n = k \geq 1,$ we have that

$$


P(k):\quad 3\,\mid\, 10^{k}+2.


$$

We must show that $P(k) \Rightarrow P(k+1).$ Let's start by writing down $P(k+1).$ This is the first part of the ****.

****: We're required to prove that

$$


P(k):\quad3\,\mid\, 10^{k+1}+2. \qquad\qquad (\ast)


$$

The idea is to rewrite the expression $10^{k+1}+2$ as $10^{k}+2$ (from the inductive hypothesis) plus a multiple of $3.$ We do this as follows:

We write

$$


\begin{aligned}10^{𝑘+1}+2 & =10^{𝑘}⋅10+2 \\ & =10(10^{𝑘})+2 \\ & =9(10^{𝑘})+10^{𝑘}+2 \\ & =9(10^{𝑘})+(10^{𝑘}+2).\end{aligned}


$$

Now, since $3 \,\mid\, (10^{k} +2)$ by the inductive hypothesis, and $9(10^{k}) = 3 \cdot 3(10^{k})$ is clearly divisible by $3,$ their sum is also divisible by $3,$ as required.

Since we have shown that the expression in $(\ast)$ is divisible by $3,$ our proof is complete. So let's write down our conclusion.

Therefore, by the principle of induction, $3 \,\mid\, 10^{n}+2$ for all $n \in \mathbb{N}.$
