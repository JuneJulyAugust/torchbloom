# Proving Inequalities Using Induction

Source: https://www.mathacademy.com/topics/927?courseId=76
Topic ID: 927

## Prerequisites

- [Mathematical Induction](./642-mathematical-induction.md)
- [Expanding Binomials Using Pascal's Triangle](../algebra-i/1157-expanding-binomials-using-pascal-s-triangle.md)
- [Factorials in Variable Expressions](../geometry/3710-factorials-in-variable-expressions.md)

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

In this lesson, we'll learn how induction is used to prove inequality statements. But first, let's discuss an important property of numbers often used in these proofs.

### Transitivity of Inequality

When proving inequalities using induction, we often use a property of integers known as **transitivity of inequality.**

In particular, if $a, b,$ and $c$ are integers, then the transitivity of inequality states the following:

- If $a > b$ and $b > c,$ then $a > c$

- If $a \geq b$ and $b \geq c,$ then $a \geq c$

- If $a < b$ and $b < c,$ then $a < c$

- If $a \leq b$ and $b \leq c,$ then $a \leq c$

For example:

- Since $3 > 2$ and $2 > 1,$ transitivity of inequality implies that $3 > 1.$

- Since $2 \leq 3$ and $3 \leq 5,$ then transitivity of inequality implies that $2 \leq 5.$

Let's now see how induction can be used to prove an inequality statement.

### A Worked Example

Let's prove that the following statement is true using mathematical induction:

$n^2+3n > 2n-1$ for all $n\in\mathbb N$

In this case, the general statement $P(n)$ we're required to prove is the following:

$P(n): \quad n^2+3n > 2n-1$ for all $n \in\mathbb N$

We start by proving the so-called base case. Since we are required to prove the statement for $n \geq 1,$ the base case is $P(1).$ So, we substitute $n=1$ into both the left-hand side and right-hand side and show that the left-hand side is greater than the right-hand side:

**Base Case**: We first prove our statement is true for the base case $n=1.$ For the left-hand side, we have

$$


\begin{aligned}1^{2}+3(1)=4,\end{aligned}


$$

and for the right-hand side, we have

$$


\begin{aligned}2(1)−1=1,\end{aligned}


$$

Thus, since $4 > 1,$ our statement is true for $n=1.$

Next, we state our inductive hypothesis. Here, we assume that the given statement is true for some $n=k\geq 1.$

**Inductive Hypothesis**: We assume that for some $n=k\geq 1,$ we have

$$


k^2+3k > 2k-1.


$$

We must show that $P(k)\Rightarrow P(k+1).$ Let's start by writing down $P(k+1).$ This is the first part of the so-called **inductive step**.

**Inductive Step**: We're required to prove that

$$


(k+1)^2+ 3(k+1) > 2(k+1)-1 = 2k+1 \qquad\qquad (\ast)


$$

The idea is to rewrite the left-hand side of $(\ast)$ *using the inductive hypothesis* and apply algebraic techniques to show that this is greater than the right-hand side. We do this as follows:

We write

$$


\begin{aligned}(𝑘+1)^{2}+3(𝑘+1) & =𝑘^{2}+2𝑘+1+3𝑘+3 \\ & =𝑘^{2}+3𝑘+2𝑘+4.\end{aligned}


$$

By the inductive hypothesis, we have

$$


\begin{aligned}𝑘^{2}+3𝑘+2𝑘+4 & =\underset{>2𝑘−1}{\underset{}{(𝑘^{2}+3𝑘)}}+2𝑘+4 \\ & >2𝑘−1+2𝑘+4 \\ & =(2𝑘+2)+(2𝑘+1) \\ & =\underset{>0}{\underset{}{2𝑘+2}}+2𝑘+1 \\ & >2𝑘+1,\end{aligned}


$$

as required.

Since we've shown that the left-hand side of $(\ast)$ is greater than the right-hand side, our proof is complete. So, let's write down our conclusion.

Therefore, by the principle of induction, $n^2+3n > 2n-1$ for all $n \in \mathbb N.$

### Example: Completing a Proof Template

#### Question

Suppose we wish to prove the following statement using mathematical induction:

$2^n > 2n$ for all $n \geq 3, n\in\mathbb N$

What are the missing entries in the proof template outlined below?

****: We first prove that our statement is true for the base case $000000$

$$


0000


$$

****: We assume that for some $000000$ We have

$$


000000


$$

****: We're required to prove that

$$


000000


$$

****: Therefore, $2^n > 2n$ for all $n \geq 3.$

#### Explanation

To prove a statement using induction, we use the following framework:

- ****: Base Case

- ****: Inductive Hypothesis

- ****: Inductive Step

- ****: Conclusion

In this case, the general statement $P(n)$ we're required to prove is the following:

$$


2^n > 2n


$$

We start by proving the so-called ****. Since we are required to prove the statement for $n \geq 3,$ the base case is $P(3).$ So, we substitute $n=3$ into both the left-hand side and right-hand side.

In our case, this gives the following:

****: We first prove that our statement is true for the base case $\boxed{\color{blue}n=3}.$

$$


\boxed{\color{blue}2^3} > \boxed{\color{blue}2(3)}


$$

Proving that the base case is true is usually straightforward. We simply calculate the left-hand and right-hand sides independently and show that the inequality holds.

Next, we write down our ****. We assume that $P(k)$ is true for some $n = k \geq 3.$ To do this, we simply replace $n$ with $k$ in our original statement $P(n).$

In our case, this gives the following:

****: We assume that for some $n = \boxed{\color{blue}k \geq 3},$ we have

$$


\boxed{\color{blue}2^k} > \boxed{\color{blue}2k}


$$

Then, we move on to the ****: We must show that $P(k) \Rightarrow P(k+1).$ We start by writing down $P(k+1).$

****: We're required to prove that

$$


\boxed{\color{blue}2^{k+1}} > \boxed{\color{blue}2(k+1)}.


$$

The inductive step is where most of the work lies. The idea is to rewrite the left-hand side of this inequality using the inductive hypothesis and apply algebraic techniques to show that this is greater than the right-hand side.

Once we've shown that $P(k) \Rightarrow P(k+1),$ the proof is complete, and we state our ****.

****: Therefore, $2^n > 2n$ for all $n \geq 3.$

### Example: Proving Polynomial Inequalities

#### Question

Use mathematical induction to prove that $n^2 > 2n+2$ for all $n \geq 3, n\in \mathbb N.$

#### Explanation

The principle of induction states the following: Suppose we have a sequence of mathematical statements $P(1), P(2), P(3),\ldots,$ where

- $P(1)$ is true, and

- $P(k)\Rightarrow P(k+1)$ for every $k\in\mathbb N.$

Then, $P(n)$ is true for every $n\in\mathbb N.$

In this case, the general statement $P(n)$ we're required to prove is the following:

$$


n^2 > 2n+2 \quad\text{for}\quad n \geq 3.


$$

We start by proving the so-called base case. Since we are required to prove the statement for $n \geq 3,$ the base case is $P(3).$ So, we substitute $n=3$ into both the left-hand side and right-hand side and show that the left-hand side is greater than the right-hand side:

We proceed using induction on $n.$

****: We first prove our statement is true for the base case $n=3.$ For the left-hand side, we have

$$


\begin{aligned}3^{2}=9,\end{aligned}


$$

and for the right-hand side, we have

$$


\begin{aligned}2(3)+2=8,\end{aligned}


$$

Thus, our statement is true for $n=3.$

Next, we state our inductive hypothesis. Here, we assume that the given statement is true for some $n=k\geq 3.$

****: We assume that for some $n=k\geq 3,$ we have

$$


k^2 > 2k+2.


$$

We must show that $P(k)\Rightarrow P(k+1).$ Let's start by writing down $P(k+1).$ This is the first part of the so-called ****.

****: We're required to prove that

$$


(k+1)^2 > 2(k+1)+2 . \qquad\qquad (\ast)


$$

The idea is to rewrite the left-hand side of $(\ast)$ ** and apply algebraic techniques to show that this is greater than the right-hand side. We do this as follows:

We write

$$


\begin{aligned}(𝑘+1)^{2} & =𝑘^{2}+2𝑘+1.\end{aligned}


$$

By the inductive hypothesis, we have

$$


\begin{aligned}𝑘^{2}+2𝑘+1 & =\underset{>2𝑘+2}{\underset{}{(𝑘^{2})}}+2𝑘+1 \\ & >2𝑘+2+2𝑘+1 \\ & =2𝑘+2+\underset{>1}{\underset{}{2𝑘}}+1 \\ & >2(𝑘+1)+2,\end{aligned}


$$

as required.

Since we've shown that the left-hand side of $(\ast)$ is greater than the right-hand side, our proof is complete. So, let's write down our conclusion.

Therefore, by the principle of induction, $n^2 > 2n+2$ for all $n \geq 3.$

### Example: Proving Other Inequalities

#### Question

Use mathematical induction to prove that $2^n +1 \leq 3^n$ for $n\in\mathbb N.$

#### Explanation

The principle of induction states the following: Suppose we have a sequence of mathematical statements $P(1), P(2), P(3), \ldots,$ where

- $P(1)$ is true, and

- $P(k) \Rightarrow P(k+1)$ for every $k \in \mathbb N.$

Then, $P(n)$ is true for every $n\in\mathbb N.$

In this case, the general statement $P(n)$ we're required to prove is the following:

$$


2^n +1 \leq 3^n \quad\text{for} \quad n \geq 1.


$$

We start by proving the so-called base case, $P(1).$ To do this, we substitute $n = 1$ into both the left-hand side and right-hand side and show that the left-hand side is less than or equal to the right-hand side:

We proceed using induction on $n.$

****: We first prove our statement is true for the base case $n = 1.$ For the left-hand side, we have

$$


\begin{aligned}2^{1}+1=3,\end{aligned}


$$

and for the right-hand side, we have

$$


\begin{aligned}3^{1}=3,\end{aligned}


$$

Thus, our statement is true for $n = 1.$

Next, we state our inductive hypothesis. Here, we assume that the given statement is true for some $n = k \geq 1.$

****: We assume that for some $n = k \geq 1,$ we have

$$


2^k +1 \leq 3^k.


$$

We must show that $P(k) \Rightarrow P(k+1).$ Let's start by writing down $P(k+1).$ This is the first part of the so-called ****.

****: We're required to prove that

$$


2^{k+1} + 1\leq 3^{k+1}. \qquad\qquad (\ast)


$$

The idea is to rewrite the left-hand side of $(\ast)$ ** and apply algebraic techniques to show that this is less than or equal to the right-hand side. We do this as follows:

We write

$$


\begin{aligned}2^{𝑘+1}+1 & =2^{𝑘}⋅2^{1}+1 \\ & =2(2^{𝑘})+1 \\ & =2^{𝑘}+2^{𝑘}+1.\end{aligned}


$$

By the inductive hypothesis, we have

$$


\begin{aligned}2^{𝑘}+\underset{≤3^{𝑘}}{\underset{}{2^{𝑘}+1}} & ≤2^{𝑘}+3^{𝑘} \\ & =\underset{<3^{𝑘}<2⋅3^{𝑘}}{\underset{}{2^{𝑘}}}+3^{𝑘} \\ & <2⋅3^{𝑘}+3^{𝑘} \\ & =3⋅3^{𝑘} \\ & =3^{𝑘+1},\end{aligned}


$$

as required.

Since we've shown that the left-hand side of $(\ast)$ is less than or equal to the right-hand side, our proof is complete. So, let's write down our conclusion.

Therefore, by the principle of induction, $2^n +1 \leq 3^n$ for all $n \geq 1.$
