# Strong Induction and Recurrence Relations

Source: https://www.mathacademy.com/topics/712?courseId=76
Topic ID: 712

## Prerequisites

- [Mathematical Induction](./642-mathematical-induction.md)

## Lesson

### Introduction

Suppose we have an arithmetic sequence with first term $a_1 = 3$ and common difference $d = 2.$ This arithmetic sequence can be expressed recursively as follows:

$$


a_{n+1} = a_n + 2, \qquad a_1 = 3, \qquad n\in\mathbb N


$$

This recursive formula generates the arithmetic sequence $3,5,7,9,\ldots.$

Note the following:

- The recursive formula for a sequence is often called a **recurrence relation.**

- This example is a **first-order recurrence relation** since we require only one previous term to calculate the next term.

- We can use our knowledge of arithmetic sequences to express the $n$th term of this sequence explicitly as follows:

We can also prove that this explicit formula for $a_n$ is true using mathematical induction. First, let's recall the principle of induction.

### The Principle of Induction

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

Let's use the principle of induction to prove the result from the previous example.

### A Worked Example

Earlier, we saw that the first-order recurrence relation:

$$


a_{n+1} = a_n+2, \qquad a_1 = 3, \qquad n\in\mathbb N


$$

has the explicit formula given by

$$


a_n = 2n+1, \qquad n \in \mathbb{N}.


$$

Let's prove this result using mathematical induction.

In this case, the general statement $P(n)$ we're required to prove is the following:

$$


P(n): \quad a_n = 2n+1, \qquad n\in\mathbb N


$$

We start by proving the base case. To do this, we substitute $n=1$ into both the left-hand side and right-hand side.

**Base Case**: We first prove our statement is true for the base case $n=1.$ For the left-hand side, we have

$$


a_1 = 3,


$$

and for the right-hand side, we have

$$


2(1)+1 = 3.


$$

Thus, our statement is true for $n=1.$

Next, we state our inductive hypothesis. Here, we assume that the given statement is true for some $n=k \geq 1.$

**Inductive Hypothesis**: We assume that for some $n=k\geq1,$ we have

$$


a_k = 2k+1.


$$

We must show that $P(k) \Rightarrow P(k+1).$ Let's start by writing down $P(k+1).$ This is the first part of the inductive step.

**Inductive Step**: We're required to prove that

$$


\begin{aligned}𝑎_{𝑘+1} & =2(𝑘+1)+1 \\ & =2𝑘+3.\,\,(∗)\end{aligned}


$$

The idea is to rewrite the left-hand side of $(\ast)$ using the recurrence relation and inductive hypothesis to show that this equals the right-hand side. We do this as follows:

Using the recurrence relation, we have

$$


\begin{aligned}𝑎_{𝑘+1} & =𝑎_{𝑘}+2.\end{aligned}


$$

By the inductive hypothesis

$$


\begin{aligned}𝑎_{𝑘}+2 & =(2𝑘+1)+2 \\ & =2𝑘+3,\end{aligned}


$$

as required.

Since we've shown that the left-hand side of $(\ast)$ equals the right-hand side, our proof is complete. So, let's write down our conclusion.

**Conclusion**: Therefore, by the principle of induction, $a_n = 2n+1$ is true for all $n \in\mathbb{N}.$

### Example: Completing a Proof Template

#### Question

Consider the recurrence relation

$$


a_{n+1} = a_n + 4, \qquad a_1 = 2, \quad n \in\mathbb{N}.


$$

Suppose we wish to prove the following statement using mathematical induction:

$$


a_n = 4n - 2


$$

A proof template is outlined below. Fill in the missing statements.

****: We first prove that our statement is true for the base case $n=1{:}$

$$


\begin{aligned}𝑎_{1} & =4(1)−2\end{aligned}


$$

****: We assume that for some $n= \boxed{\phantom{k\geq 1}},$ we have

$$


a_k = \boxed{\phantom{4k -2}}.


$$

****: We're required to prove that

$$


a_{k+1} = \boxed{\phantom{4k +2}}.


$$

****: Therefore, $a_n = 4n -2$ for all $n\in \mathbb{N}.$

#### Explanation

To prove a statement using induction, we use the following framework:

- ****: Base Case

- ****: Inductive Hypothesis

- ****: Inductive Step

- ****: Conclusion

In this case, the general statement $P(n)$ we're required to prove is the following:

$$


a_n =4n-2


$$

We start by proving the base case. To do this, we substitute $n=1$ into both the left-hand side and right-hand side.

****: We first prove our statement is true for the base case $n=1.$

$$


\begin{aligned}𝑃(1):\,𝑎_{1} & =4(1)−2\end{aligned}


$$

Proving that the base case is true is usually straightforward. We simply calculate the right-hand side and show that it equals the left-hand side.

Next, we write down our ****. We assume that $P(k)$ is true for some $n=k\geq 1.$ To do this, we simply replace $n$ with $k$ in our original statement $P(n).$

****: We assume that for some $n=k\geq 1,$ we have

$$


a_k = 4k - 2.


$$

Then, we move onto the ****: We must show that $P(k)\Rightarrow P(k+1).$ We start by writing down $P(k+1).$

****: We're required to prove that

$$


\begin{aligned}𝑎_{𝑘+1} & =4(𝑘+1)−2 \\ & =4𝑘+2.\end{aligned}


$$

The inductive step is where most of the work lies. The idea is to rewrite the left-hand side of this equation using the recurrence relation and inductive hypothesis to show that this equals the right-hand side.

Once we've shown that $P(k)\Rightarrow P(k+1),$ the proof is complete, and we state our ****.

****: Therefore, $a_n = 4n -2$ for all $n\in \mathbb{N}.$

### Example: Proving Explicit Formulas for First-Order Recurrence Relations

#### Question

Given the recurrence relation

$$


a_{n+1} = 2a_n-3, \qquad a_1 =5,\quad n\in\mathbb N,


$$

use mathematical induction to prove the following statement:

$$


a_n = 2^n +3, \quad n \in \mathbb{N}


$$

#### Explanation

The principle of induction states the following: Suppose we have a sequence of mathematical statements $P(1),$ $P(2),$ $P(3), \ldots,$ where

- $P(1)$ is true, and

- $P(k) \Rightarrow P(k+1)$ for every $k \in \mathbb{N}.$

Then, $P(n)$ is true for every $n \in \mathbb{N}.$

In this case, the general statement $P(n)$ we're required to prove is the following:

$$


P(n): \quad a_n = 2^n + 3


$$

We start by proving the base case. To do this, we substitute $n=1$ into both the left-hand side and right-hand side.

****: We first prove our statement is true for the base case $n=1.$ For the left-hand side, we have

$$


a_1 = 5,


$$

and for the right-hand side, we have

$$


2^1 + 3 = 5.


$$

Thus, our statement is true for $n=1.$

Next, we state our inductive hypothesis. Here, we assume that the given statement is true for some $n=k \geq 1.$

****: We assume that for some $n=k\geq1,$ we have

$$


a_k = 2^k + 3.


$$

We must show that $P(k) \Rightarrow P(k+1).$ Let's start by writing down $P(k+1).$ This is the first part of the inductive step.

****: We're required to prove that

$$


a_{k+1} = 2^{k+1} + 3. \qquad\qquad (\ast)


$$

The idea is to rewrite the left-hand side of $(\ast)$ using the recurrence relation and inductive hypothesis to show that this equals the right-hand side. We do this as follows:

Using the recurrence relation, we have

$$


\begin{aligned}𝑎_{𝑘+1} & =2𝑎_{𝑘}−3.\end{aligned}


$$

By the inductive hypothesis

$$


\begin{aligned}2𝑎_{𝑘}−3 & =2(2^{𝑘}+3)−3 \\ & =2⋅2^{𝑘}+6−3 \\ & =2^{𝑘+1}+3,\end{aligned}


$$

as required.

Since we've shown that the left-hand side of $(\ast)$ equals the right-hand side, our proof is complete. So, let's write down our conclusion.

****: Therefore, by the principle of induction, $a_n = 2^n+3$ is true for all $n \in\mathbb{N}.$

### Second-Order Recurrence Relations

Now, consider the following recurrence relation:

$$


a_{n+2} = a_{n+1} + a_n, \quad a_1 = 1,\quad a_2 = 1, \qquad n\in\mathbb N


$$

This recurrence relation generates the Fibonacci sequence $1,1,2,3,5,8,13,\ldots.$

Note the following:

- This is an example of a **second-order recurrence relation** since we require *two* previous terms to calculate the next term.

- Deriving the explicit formula for the $n$th term is trickier here. However, it can be shown that

We can prove that our formula for $a_n$ is true using mathematical induction. However, this case differs from what we've seen previously because finding the next term in the sequence using the recursive formula requires knowledge of the previous *two* terms!

Therefore, we need to employ a modified form of induction, known as **strong induction,** to prove that the explicit formula for a second-order recurrence relation is true. We discuss this next.

### Strong Induction

The principle of **strong mathematical induction** states the following:

*Suppose we have a sequence of mathematical statements $P(1),$ $P(2),$ $P(3), \ldots,$ where*

- *$P(1)$ is true (as well as $P(2), P(3),P(4),\ldots,$ if required), and*

- *$(P(1)\land P(2)\land \ldots\land P(k)) \Rightarrow P(k+1)$ for every $k \in \mathbb{N}.$*

*Then, $P(n)$ is true for every $n \in \mathbb{N}.$*

The principle of strong induction is equivalent to the principle of induction.

Strong induction is useful when it's difficult to show that $P(k)\Rightarrow P(k+1)$ because $P(k)$ alone does not give enough information to imply that $P(k+1)$ must be true.

In such cases, we can assume that *all* of the statements $P(1), P(2), \ldots, P(k-1), P(k)$ are true, and then use *this* assumption to prove that $P(k+1)$ is true.

Let's see how to prove the explicit formula for the $n$th term of a second-order recurrence relation using strong induction.

### A Worked Example

Given the recurrence relation

$$


a_{n+1} = 2a_{n} - a_{n -1}, \qquad a_1 = 2, \qquad a_2 = 3, \qquad n\in\mathbb N, \qquad n \geq 2


$$

let's use strong induction to prove the following statement:

$$


a_n = n+1, \qquad \forall n\in\mathbb N


$$

The principle of strong induction states the following: Suppose we have a sequence of mathematical statements $P(1),$ $P(2),$ $P(3), \ldots,$ where

- $P(1)$ is true (as well as $P(2), P(3),P(4),\ldots,$ if required), and

- $P(1), P(2), \ldots, P(k) \Rightarrow P(k+1)$ for every $k \in \mathbb{N}.$

Then, $P(n)$ is true for every $n \in \mathbb{N}.$

In this case, the general statement $P(n)$ we're required to prove is the following:

$$


P(n): \quad a_n = n+1


$$

We start by proving the base cases. Since the first application of the recurrence formula $a_{n+1} = 2a_{n}-a_{n-1}$ does not apply until $a_3,$ we must check the base cases $P(1)$ and $P(2).$

**Base Cases**: We first prove our statement is true for the base cases $n=1,2.$ For $n=1,$ for the left-hand side, we have

$$


a_1 = 2,


$$

and for the right-hand side, we have

$$


(1)+1= 2.


$$

Similarly, for $n=2,$ for the left-hand side, we have

$$


a_2 = 3,


$$

and for the right-hand side, we have

$$


(2)+1= 3.


$$

Thus, our statement is true for $n=1$ and $n=2.$

Next, we write down our (strong) **inductive hypothesis,** which is to assume that $P(n)$ is true *for all* $n\leq k,$ where $k\geq 2.$

**Inductive Hypothesis**: We assume that $a_n=n+1$ for all $n\leq k$ for some $k \geq 2.$ In particular, we have the following:

$$


\begin{aligned}𝑎_{𝑘} & =𝑘+1 \\ 𝑎_{𝑘−1} & =𝑘\end{aligned}


$$

We must show that $P(1),P(2),\ldots, P(k) \Rightarrow P(k+1).$ Let's start by writing down $P(k+1).$ This is the first part of the inductive step.

**Inductive Step**: We're required to prove that

$$


a_{k+1} = k+2 . \qquad\qquad (\ast)


$$

The idea is to rewrite the left-hand side of $(\ast)$ using the recurrence relation and inductive hypothesis to show that this equals the right-hand side. We do this as follows:

Using the recurrence relation, we have

$$


\begin{aligned}𝑎_{𝑘+1} & =2𝑎_{𝑘}−𝑎_{𝑘−1}.\end{aligned}


$$

By the inductive hypothesis

$$


\begin{aligned}2𝑎_{𝑘}−𝑎_{𝑘−1} & =2(𝑘+1)−(𝑘) \\ & =2𝑘+2−𝑘 \\ & =𝑘+2,\end{aligned}


$$

as required.

Since we've shown that the left-hand side of $(\ast)$ equals the right-hand side, our proof is complete. So, let's write down our conclusion.

**Conclusion**: Therefore, by the principle of strong induction, $a_n = n+1$ is true for all $n \in\mathbb{N}.$

### Example: Completing a Proof Template

#### Question

Consider the recurrence relation

$$


a_{n+1} = 11a_{n} - 10a_{n-1}, \quad a_1 = 5, \quad a_2 = 95, \quad n \in\mathbb{N}, \quad n\geq 2.


$$

Suppose we wish to prove the following statement using strong induction:

$$


a_n = 10^n - 5, \quad \forall n\in\mathbb N


$$

A proof template is outlined below. Fill in the missing statements.

****: We first prove that our statement is true for the base cases $n=1$ and $n=2.$

$$


\begin{aligned}𝑎_{1} & =10^{1}−5 \\ 𝑎_{2} & =10^{3}−5\end{aligned}


$$

****: We assume that $a_n = 10^n-5$ is true for all $\boxed{\phantom{n\leq k}}.$ In particular, we have the following:

$$


\begin{aligned}𝑎_{𝑘}=10^{𝑘−1} \\ 𝑎_{𝑘−1}=10^{𝑘−1}\end{aligned}


$$

****: We're required to prove that

$$


a_{k+1} = \boxed{\phantom{10^{k-1}}}


$$

****: Therefore, $a_n = 10^n - 5$ for all $n\in \mathbb{N}.$

#### Explanation

To prove a statement using strong induction, we use the following framework:

- ****: Base Case

- ****: Inductive Hypothesis

- ****: Inductive Step

- ****: Conclusion

In this case, the general statement $P(n)$ we're required to prove is the following:

$$


a_n = 10^n - 5


$$

We start by proving the base cases. Since the first application of the recurrence formula $a_{n+1} = 11a_{n} - 10a_{n-1}$ does not apply until $a_3,$ we must check the base cases $P(1)$ and $P(2).$

****: We first prove our statement is true for the base cases $n=1$ and $n=2.$

$$


\begin{aligned}𝑎_{1} & =10^{1}−5 \\ 𝑎_{2} & =10^{2}−5\end{aligned}


$$

Proving that the base cases are true is usually straightforward. We simply calculate the right-hand side and show that it equals the left-hand side in both cases.

Next, we write down our (strong) **** which is to assume that $P(n)$ is true ** $n\leq k,$ where $k\geq 2.$

****: We assume that $a_n = 10^n - 5$ is true for all $n\leq k$ for $k \geq 2.$ In particular, we have the following:

$$


\begin{aligned}𝑎_{𝑘} & =10^{𝑘}−5 \\ 𝑎_{𝑘−1} & =10^{𝑘−1}−5\end{aligned}


$$

Then, we move onto the ****: We must show that $P(1),P(2),\ldots, P(k) \Rightarrow P(k+1).$ We start by writing down $P(k+1).$

****: We're required to prove that

$$


a_{k+1} = 10^{k+1} - 5.


$$

The inductive step is where most of the work lies. The idea is to rewrite the left-hand side of this equation using the recurrence relation and inductive hypothesis to show that this equals the right-hand side.

Once we've shown that $P(1),P(2),\ldots, P(k) \Rightarrow P(k+1),$ the proof is complete, and we state our ****.

****: Therefore, $a_n = 10^n - 5$ for all $n\in \mathbb{N}.$

### Example: Proving Explicit Formulas for Second-Order Recurrence Relations

#### Question

Given the recurrence relation

$$


a_{n+1} = 4a_{n} - 3a_{n -1}, \quad a_1 = 2,\quad a_2 = 8,\quad n\in\mathbb N, \quad n \geq 2


$$

use strong induction to prove the following statement:

$$


a_n = 3^n - 1, \quad \forall n\in\mathbb N


$$

#### Explanation

The principle of strong induction states the following: Suppose we have a sequence of mathematical statements $P(1),$ $P(2),$ $P(3), \ldots,$ where

- $P(1)$ is true (as well as $P(2), P(3),P(4),\ldots,$ if required), and

- $P(1), P(2), \ldots, P(k) \Rightarrow P(k+1)$ for every $k \in \mathbb{N}.$

Then, $P(n)$ is true for every $n \in \mathbb{N}.$

In this case, the general statement $P(n)$ we're required to prove is the following:

$$


P(n): \quad a_n = 3^n - 1


$$

We start by proving the base cases. Since the first application of the recurrence formula $a_{n+1} = 4a_{n} - 3a_{n-1}$ does not apply until $a_3,$ we must check the base cases $P(1)$ and $P(2).$

****: We first prove our statement is true for the base cases $n=1,2.$ For $n=1,$ for the left-hand side, we have

$$


a_1 = 2,


$$

and for the right-hand side, we have

$$


3^1 - 1 = 2.


$$

Similarly, for $n=2,$ for the left-hand side, we have

$$


a_2 = 8,


$$

and for the right-hand side, we have

$$


3^2 - 1 = 8.


$$

Thus, our statement is true for $n=1$ and $n=2.$

Next, we write down our (strong) **** which is to assume that $P(n)$ is true ** $n\leq k,$ where $k\geq 2.$

****: We assume that $a_n=3^n - 1$ for all $n\leq k$ for some $k \geq 2.$ In particular, we have the following:

$$


\begin{aligned}𝑎_{𝑘} & =3^{𝑘}−1 \\ 𝑎_{𝑘−1} & =3^{𝑘−1}−1\end{aligned}


$$

We must show that $P(1),P(2),\ldots, P(k) \Rightarrow P(k+1).$ Let's start by writing down $P(k+1).$ This is the first part of the inductive step.

****: We're required to prove that

$$


a_{k+1} = 3^{k+1} - 1. \qquad\qquad (\ast)


$$

The idea is to rewrite the left-hand side of $(\ast)$ using the recurrence relation and inductive hypothesis to show that this equals the right-hand side. We do this as follows:

Using the recurrence relation, we have

$$


\begin{aligned}𝑎_{𝑘+1} & =4𝑎_{𝑘}−3𝑎_{𝑘−1}.\end{aligned}


$$

By the inductive hypothesis

$$


\begin{aligned}4𝑎_{𝑘}−3𝑎_{𝑘−1} & =4(3^{𝑘}−1)−3(3^{𝑘−1}−1) \\ & =4(3^{𝑘})−4(1)−3(3^{𝑘−1})+3(1) \\ & =4(3^{𝑘})−4−3^{𝑘}+3 \\ & =3(3^{𝑘})−1 \\ & =3^{𝑘+1}−1,\end{aligned}


$$

as required.

Since we've shown that the left-hand side of $(\ast)$ equals the right-hand side, our proof is complete. So, let's write down our conclusion.

****: Therefore, by the principle of strong induction, $a_n = 3^n - 1$ is true for all $n \in\mathbb{N}.$
