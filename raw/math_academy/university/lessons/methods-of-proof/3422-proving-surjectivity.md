# Proving Surjectivity

Source: https://www.mathacademy.com/topics/3422?courseId=76
Topic ID: 3422

## Prerequisites

- [Direct Proof](./2801-direct-proof.md)
- [Into Functions](./3027-into-functions.md)
- [Negating Statements With Nested Quantifiers](./4258-negating-statements-with-nested-quantifiers.md)
- [Consistency and Dependency in Linear Systems](../../../high-school/traditional/lessons/algebra-i/4638-consistency-and-dependency-in-linear-systems.md)

## Lesson

### Introduction

Consider the function $f: \mathbb{R} \to \mathbb{R}$ defined by $f(x)=3x+1.$ Let's prove that this function is surjective.

First, recall the definition of a surjection:

*A function $f: X\rightarrow Y$ is a surjection if, for every element $y$ in $Y,$ there is at least one element in $X$ that maps to $y{:}$*

$$


\forall \, y \in Y, \, \exists \, x \in X, \: f(x)=y


$$

Therefore, in this case, the surjectivity of $f$ means the following:

*For all $y \in \mathbb{R}$ there exists $x \in \mathbb{R}$ such that $3x+1=y.$*

To prove this, we need to take an arbitrary $y \in Y$ and show that we can always find at least one value of $x\in X$ that is mapped to $y$ under $f.$

*So, let $y \in \mathbb{R}.$ Then, we have the following:*

$$


\begin{aligned}𝑓(𝑥) & =𝑦 \\ 3𝑥+1 & =𝑦 \\ 3𝑥 & =𝑦−1 \\ 𝑥 & =\frac{𝑦−1}{3}\end{aligned}


$$

So, if we wish to map to $y\in\mathbb R,$ we simply select $x = \dfrac{y-1}{3}\in\mathbb R.$ Note that

$$


f\left(\dfrac{y-1}{3}\right) = 3\cdot \left(\dfrac{y-1}{3}\right) + 1 = y.


$$

We continue our proof as follows:

*So, for every $y\in \mathbb R,$ we have*

$$


f\left(\dfrac{y-1}{3}\right) = y.


$$

Finally, we state the conclusion:

*Therefore, $f$ is a surjection.*

For clarity, let's restate our proposition and its proof.

### Restating the Full Proof

*Proposition:*

*The function $f: \mathbb{R} \to \mathbb{R},$ defined by $f(x)=3x+1,$ is surjective.*

*Proof:*

*A function $f: X\rightarrow Y$ is a surjection if, for every element $y$ in $Y,$ there is at least one element in $X$ that maps to $y{:}$*

$$


\forall \, y \in Y, \, \exists \, x \in X, \: f(x)=y


$$

*For all $y \in \mathbb{R}$ there exists $x \in \mathbb{R}$ such that $3x+1=y.$*

*So, let $y \in \mathbb{R}.$ Then, we have the following:*

$$


\begin{aligned}𝑓(𝑥) & =𝑦 \\ 3𝑥+1 & =𝑦 \\ 3𝑥 & =𝑦−1 \\ 𝑥 & =\frac{𝑦−1}{3}\end{aligned}


$$

*So, for every $y\in \mathbb R,$ we have*

$$


f\left(\dfrac{y-1}{3}\right) = y.


$$

*Therefore, $f$ is a surjection.*

### Example: Understanding the Definition of Surjectivity

#### Question

You're given that the function $f: \mathbb{N} \to \mathbb{N}$ defined by $f(x)=4x^2$ is **** surjective. Complete the reasoning in the statement below.

Since $f$ is not surjective, $\boxed{\phantom{\textrm{there exists} n \in \mathbb{N} \textrm{such that} \textrm{for all} m \in \mathbb{N}}}$ $\boxed{\phantom{4x^2 \neq n}}.$

#### Explanation

A function $f: X\rightarrow Y$ is a surjection if, for every element $y$ in $Y,$ there is at least one element in $X$ that maps to $y{:}$

$$


\forall \, y \in Y, \, \exists \, x \in X, \: f(x)=y


$$

The negation of this statement is

$$


\exists \, y \in Y, \, \forall \, x \in X, \: f(x) \neq y.


$$

Therefore, the correct statement in our case is as follows:

Since $f$ is not surjective, $\boxed{\color{blue}\textrm{there exists} y \in \mathbb{N} \textrm{such that} \textrm{for all} x \in \mathbb{N},}$ $\boxed{\color{blue}4x^2 \neq y}.$

### Example: Proving a Function is Surjective

#### Question

Prove that the function $f: \mathbb{R} \times \mathbb{R} \to \mathbb{R}$ defined by $f(x_1,x_2)=3x_1 + 2x_2$ is surjective.

#### Explanation

First, recall the definition of a surjection:

A function $f: X\rightarrow Y$ is a surjection if, for every element $y$ in $Y,$ there exists an element in $X$ that maps to $y{:}$

$$


\forall \, y \in Y, \, \exists \, x \in X, \: f(x)=y


$$

The idea is to take an arbitrary $y \in Y$ and show that we can always find at least one value of $x$ that is mapped to $y$ under $f{:}$

So, let $y \in \mathbb{R}.$ Then, we have the following:

$$


\begin{aligned}𝑓(𝑥_{1},𝑥_{2}) & =𝑦 \\ 3𝑥_{1}+2𝑥_{2} & =𝑦\end{aligned}


$$

For example, if we take $x_1=\dfrac{y}{3}$ and $x_2=0,$ then $f$ maps $(x_1,x_2)$ to $y.$

Finally, we state the conclusion:

Therefore, $f$ is a surjection.

### Example: Proving a Function is Not Surjective

#### Question

Prove that the function $f: \mathbb{Z} \to \mathbb{Z} \times \mathbb{Z}$ defined by $f(m)=(m, 3m-1)$ is **** surjective.

#### Explanation

First, recall the definition of a surjection:

A function $f: X\rightarrow Y$ is a surjection if, for every element $y$ in $Y,$ there exists an element in $X$ that maps to $y{:}$

$$


\forall \, y \in Y, \, \exists \, x \in X, \: f(x)=y


$$

The negation of this statement is

$$


\exists \, y \in Y, \, \forall \, x \in X, \: f(x) \neq y.


$$

So, we get the following:

To disprove a universal statement, it's sufficient to find a counterexample.

In other words, we need to show that there exists $y$ such that

$$


f(x) \neq y


$$

for any possible $x.$

We simply need to find a value $y$ that does not have a preimage.

As a counterexample, let's take $y=(1,0).$ Notice that

$$


\begin{aligned}𝑓(𝑚) & =𝑦 \\ (𝑚,3𝑚−1) & =(1,0)\end{aligned}


$$

Since two pairs are equal if and only if their respective components are equal, we obtain the system

$$


\begin{aligned}𝑚=1 \\ 3𝑚−1=0\end{aligned}


$$

which has no solution.

Finally, we state the conclusion:

Hence, the pair $(1,0)$ has no preimage in $\mathbb{Z}.$ Therefore, $f$ isn't a surjection.
