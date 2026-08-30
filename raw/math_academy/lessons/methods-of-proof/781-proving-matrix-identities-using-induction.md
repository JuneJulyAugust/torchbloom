# Proving Matrix Identities Using Induction

Source: https://www.mathacademy.com/topics/781?courseId=76
Topic ID: 781

## Prerequisites

- [Mathematical Induction](./642-mathematical-induction.md)
- [Powers of Matrices](../integrated-math-iii-honors/1725-powers-of-matrices.md)

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

In this lesson, we'll learn how induction can be used to prove matrix identities.

### A Worked Example

Let's prove the following result using mathematical induction:

$[\begin{aligned}1 & 2 \\ 0 & 1\end{aligned}]$ for all $n \in \mathbb{N}$

In this case, the general statement $P(n)$ we're required to prove is the following:

$$


[\begin{aligned}1 & 2 \\ 0 & 1\end{aligned}]


$$

We start by proving the base case, $P(1).$ To do this, we substitute $n=1$ into both the left-hand side and right-hand side and show that they're equal:

**Base Case**: We first prove our statement is true for the base case $n=1.$ For the left-hand side, we have

$$


\begin{aligned}[\begin{aligned}1 & 2 \\ 0 & 1\end{aligned}]^{1}=[\begin{aligned}1 & 2 \\ 0 & 1\end{aligned}],\end{aligned}


$$

and for the right-hand side, we have

$$


\begin{aligned}[\begin{aligned}1 & 2(1) \\ 0 & 1\end{aligned}]=[\begin{aligned}1 & 2 \\ 0 & 1\end{aligned}].\end{aligned}


$$

Thus, our statement is true for $n=1.$

Next, we state our inductive hypothesis. Here, we assume that the given statement is true for some $n=k\geq 1.$

**Inductive Hypothesis**: We assume that for some $n=k\geq 1,$ we have

$$


[\begin{aligned}1 & 2 \\ 0 & 1\end{aligned}]


$$

We must show that $P(k)\Rightarrow P(k+1).$ Let's start by writing down $P(k+1).$ This is the first part of the **inductive step**.

**Inductive Step**: We're required to prove that

$$


[\begin{aligned}1 & 2 \\ 0 & 1\end{aligned}]


$$

The idea is to rewrite the left-hand side of $(\ast)$ *using the inductive hypothesis* and apply algebraic techniques to show that this equals the right-hand side.

When proving matrix identities using induction, the key to unlocking the proof is to factor out one instance of the matrix, as follows:

$$


[\begin{aligned}1 & 2 \\ 0 & 1\end{aligned}]


$$

Let's apply this technique in this case:

We write

$$


\begin{aligned}[\begin{aligned}1 & 2 \\ 0 & 1\end{aligned}]^{𝑘+1} & =[\begin{aligned}1 & 2 \\ 0 & 1\end{aligned}]^{𝑘}⋅[\begin{aligned}1 & 2 \\ 0 & 1\end{aligned}].\end{aligned}


$$

By the inductive hypothesis, we have

$$


\begin{aligned}[\begin{aligned}1 & 2 \\ 0 & 1\end{aligned}]^{𝑘}⋅[\begin{aligned}1 & 2 \\ 0 & 1\end{aligned}] & =[\begin{aligned}1 & 2𝑘 \\ 0 & 1\end{aligned}]⋅[\begin{aligned}1 & 2 \\ 0 & 1\end{aligned}] \\ & =[\begin{aligned}1 & 2+2𝑘 \\ 0 & 1\end{aligned}] \\ & =[\begin{aligned}1 & 2(𝑘+1) \\ 0 & 1\end{aligned}],\end{aligned}


$$

as required.

Since we've shown that the left-hand side of $(\ast)$ equals the right-hand side, our proof is complete. So, let's write down our conclusion.

Therefore, by the principle of induction, $[\begin{aligned}1 & 2 \\ 0 & 1\end{aligned}]$ is true for all $n \in \mathbb{N}.$

### Example: Completing a Proof Template

#### Question

Suppose we wish to prove the following statement using mathematical induction:

$$


[\begin{aligned}1 & 0 \\ 7 & 1\end{aligned}]


$$

What are the missing entries in the proof template below?

****: We first prove that our statement is true for the base case $n=1.$

$$


[\begin{aligned}1 & 5 \\ 0 & 1\end{aligned}]


$$

****: We assume that for some $000000$ we have

$$


[\begin{aligned}1 & 5 \\ 0 & 1\end{aligned}]


$$

****: We're required to prove that

$$


[\begin{aligned}1 & 5 \\ 0 & 1\end{aligned}]


$$

****: Therefore, $[\begin{aligned}1 & 0 \\ 7 & 1\end{aligned}]$ for all $n \in \mathbb{N}.$

#### Explanation

To prove a statement using induction, we use the following framework:

- ****: Base Case

- ****: Inductive Hypothesis

- ****: Inductive Step

- ****: Conclusion

In this case, the general statement $P(n)$ we're required to prove the following:

$$


[\begin{aligned}1 & 0 \\ 7 & 1\end{aligned}]


$$

We start by proving the ****, $P(1).$ To do this, we substitute $n=1$ into both the left-hand side and right-hand side.

In our case, this gives the following:

****: We first prove that our statement is true for the base case $n=1.$

$$


[\begin{aligned}1 & 0 \\ 7 & 1\end{aligned}]


$$

Proving that the base case is true is usually straightforward. We simply calculate the left-hand and right-hand sides independently and show they're equal.

Next, we write down our ****. We assume that $P(k)$ is true for some $n=k \geq 1.$ To do this, we simply replace $n$ with $k$ in our original statement $P(n).$

In our case, this gives the following:

****: We assume that for some $n = \boxed{\color{blue}k \geq 1},$ we have

$$


[\begin{aligned}1 & 0 \\ 7 & 1\end{aligned}]


$$

Then, we move onto the ****: We must show that $P(k) \Rightarrow P(k+1).$ We start by writing down $P(k+1).$

****: We're required to prove that

$$


[\begin{aligned}1 & 0 \\ 7 & 1\end{aligned}]


$$

The inductive step is where most of the work lies. The idea is to rewrite the left-hand side of this equation using the inductive hypothesis and apply algebraic techniques to show that this equals the right-hand side.

Once we're shown that $P(k) \Rightarrow P(k+1),$ the proof is complete, and we state our ****.

****: Therefore, $[\begin{aligned}1 & 0 \\ 7 & 1\end{aligned}]$ for all $n \in \mathbb{N}.$

### Example: Proving Matrix Identities

#### Question

Use mathematical induction to prove that $[\begin{aligned}1 & 0 \\ 3 & 4\end{aligned}]$ for all $n \in \mathbb{N}.$

#### Explanation

The principle of induction states the following: Suppose we have a sequence of mathematical statements $P(1), P(2), P(3), \ldots,$ where

- $P(1)$ is true, and

- $P(k)\Rightarrow P(k+1)$ for every $k\in\mathbb N.$

Then, $P(n)$ is true for every $n\in\mathbb N.$

In this case, the general statement $P(n)$ we're required to prove is the following:

$$


[\begin{aligned}1 & 0 \\ 3 & 4\end{aligned}]


$$

We start by proving the base case, $P(1).$ To do this, we substitute $n=1$ into both the left-hand side and right-hand side and show that they're equal:

We proceed using induction on $n.$

****: We first prove our statement is true for the base case $n=1.$ For the left-hand side, we have

$$


\begin{aligned}[\begin{aligned}1 & 0 \\ 3 & 4\end{aligned}]^{1}=[\begin{aligned}1 & 0 \\ 3 & 4\end{aligned}],\end{aligned}


$$

and for the right-hand side, we have

$$


\begin{aligned}[\begin{aligned}1 & 0 \\ 4^{1}−1 & 4^{1}\end{aligned}]=[\begin{aligned}1 & 0 \\ 3 & 4\end{aligned}].\end{aligned}


$$

Thus, our statement is true for $n=1.$

Next, we state our inductive hypothesis. Here, we assume that the given statement is true for some $n=k\geq 1.$

****: We assume that for some $n=k\geq 1,$ we have

$$


[\begin{aligned}1 & 0 \\ 3 & 4\end{aligned}]


$$

We must show that $P(k)\Rightarrow P(k+1).$ Let's start by writing down $P(k+1).$ This is the first part of the ****.

****: We're required to prove that

$$


[\begin{aligned}1 & 0 \\ 3 & 4\end{aligned}]


$$

The idea is to rewrite the left-hand side of $(\ast)$ ** and apply algebraic techniques to show that this equals the right-hand side.

When proving matrix identities using induction, the key to unlocking the proof is to factor out one instance of the matrix, as follows:

$$


[\begin{aligned}1 & 0 \\ 3 & 4\end{aligned}]


$$

Let's apply this technique in this case:

We write

$$


\begin{aligned}[\begin{aligned}1 & 0 \\ 3 & 4\end{aligned}]^{𝑘+1} & =[\begin{aligned}1 & 0 \\ 3 & 4\end{aligned}]^{𝑘}⋅[\begin{aligned}1 & 0 \\ 3 & 4\end{aligned}].\end{aligned}


$$

By the inductive hypothesis, we have

$$


\begin{aligned}[\begin{aligned}1 & 0 \\ 3 & 4\end{aligned}]^{𝑘}⋅[\begin{aligned}1 & 0 \\ 3 & 4\end{aligned}] & =[\begin{aligned}1 & 0 \\ 4^{𝑘}−1 & 4^{𝑘}\end{aligned}]⋅[\begin{aligned}1 & 0 \\ 3 & 4\end{aligned}] \\ & =[\begin{aligned}1 & 0 \\ 4^{𝑘}−1+3⋅4^{𝑘} & 4⋅4^{𝑘}\end{aligned}] \\ & =[\begin{aligned}1 & 0 \\ 4⋅4^{𝑘}−1 & 4⋅4^{𝑘}\end{aligned}] \\ & =[\begin{aligned}1 & 0 \\ 4^{𝑘+1}−1 & 4^{𝑘+1}\end{aligned}],\end{aligned}


$$

as required.

Since we've shown that the left-hand side of $(\ast)$ equals the right-hand side, our proof is complete. So let's write down our conclusion.

Therefore, by the principle of induction, $[\begin{aligned}1 & 0 \\ 3 & 4\end{aligned}]$ is true for all $n\geq 1.$
