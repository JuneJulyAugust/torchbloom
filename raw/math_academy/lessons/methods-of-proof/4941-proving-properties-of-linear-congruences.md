# Proving Properties of Linear Congruences

Source: https://www.mathacademy.com/topics/4941?courseId=76
Topic ID: 4941

## Prerequisites

- [Proving Properties of Modular Congruence](./253-proving-properties-of-modular-congruence.md)
- [Solving Advanced Linear Congruences](./2737-solving-advanced-linear-congruences.md)
- [Proof by Contradiction](./3414-proof-by-contradiction.md)

## Lesson

### Introduction

In this lesson, we'll learn how to prove some important theorems regarding the existence and number of solutions to linear congruences.

The first theorem we'll consider is a statement about the existence of a solution to a linear congruence:

Let $a$ and $b$ be integers and $n$ be a positive integer. If $\text{gcd}(a,n)=1$, then the linear congruence $ax \equiv b \:(\text{mod}\:n)$ has a solution.

To prove the theorem, we'll construct the solution to our congruence.

We start by using the conditions given in the theorem. Since these conditions involve a statement about the greatest common divisor of $a$ and $n,$ we can use Bézout's identity.

Since $\text{gcd}(a,n)=1$, then by Bézout's identity, there exist integers $u$ and $v$ such that

$$


au+nv=1.


$$

Notice that if we write this equation modulo $n,$ the second term on the left-hand side reduces to zero.

We can write this result in modulo $n,$ as follows:

$$


\begin{aligned}𝑎𝑢+𝑛𝑣 & ≡1 & & (mod\,𝑛) \\ 𝑎𝑢+0⋅𝑣 & ≡1 & & (mod\,𝑛) \\ 𝑎𝑢 & ≡1 & & (mod\,𝑛)\end{aligned}


$$

Recall that the multiplicative inverse of $a$ modulo $n$ is the integer such that multiplying it by $a$ gives $1$ modulo $n.$ So, we see that $u$ fits this definition:

This means that $u$ is the multiplicative inverse of $a$ (modulo $n$).

Next, we can use the multiplicative inverse to eliminate the multiplier $a$ in our congruence, as shown below.

So, multiplying both sides of the original congruence $ax \equiv b \:(\text{mod}\:n)$ by $u,$ we get:

$$


\begin{aligned}𝑎𝑥 & ≡𝑏 & & (mod\,𝑛) \\ 𝑢⋅𝑎𝑥 & ≡𝑢⋅𝑏 & & (mod\,𝑛) \\ (𝑢⋅𝑎)𝑥 & ≡𝑢𝑏 & & (mod\,𝑛) \\ 1⋅𝑥 & ≡𝑢𝑏 & & (mod\,𝑛) \\ 𝑥 & ≡𝑢𝑏 & & (mod\,𝑛)\end{aligned}


$$

This shows that a solution to the congruence exists and is given by $x_1=ub.$

Finally, we write down the conclusion.

Therefore, the congruence has the solution $x_1 \equiv ub \: (\text{mod}\:n).$

Now that we have all of the details, let's restate the proof in full.

### Stating the Full Proof

Theorem:

Let $a$ and $b$ be integers and $n$ be a positive integer. If $\text{gcd}(a,n)=1$, then the linear congruence $ax \equiv b \:(\text{mod}\:n)$ has a solution.

Proof:

Since $\text{gcd}(a,n)=1$, then by Bézout's identity, there exist integers $u$ and $v$ such that

$$


au+nv=1.


$$

We can write this result in modulo $n,$ as follows:

$$


\begin{aligned}𝑎𝑢+𝑛𝑣 & ≡1 & & (mod\,𝑛) \\ 𝑎𝑢+0⋅𝑣 & ≡1 & & (mod\,𝑛) \\ 𝑎𝑢 & ≡1 & & (mod\,𝑛)\end{aligned}


$$

This means that $u$ is the multiplicative inverse of $a$ (modulo $n$).

So, multiplying both sides of the original congruence $ax \equiv b \:(\text{mod}\:n)$ by $u,$ we get:

$$


\begin{aligned}𝑎𝑥 & ≡𝑏 & & (mod\,𝑛) \\ 𝑢⋅𝑎𝑥 & ≡𝑢⋅𝑏 & & (mod\,𝑛) \\ (𝑢⋅𝑎)𝑥 & ≡𝑢𝑏 & & (mod\,𝑛) \\ 1⋅𝑥 & ≡𝑢𝑏 & & (mod\,𝑛) \\ 𝑥 & ≡𝑢𝑏 & & (mod\,𝑛)\end{aligned}


$$

Therefore, the congruence has the solution $x_1 \equiv ub \: (\text{mod}\:n).$

This theorem can be proved in many different ways. Let's take a look at another proof of this theorem.

### Example: Proving the Existence of a Solution to a Congruence

#### Question

Prove the following theorem:

Let $a$ and $b$ be integers and $n$ be a positive integer. If $\text{gcd}(a,n)=1$, then the linear congruence $ax \equiv b \:(\text{mod}\:n)$ has a solution.

#### Explanation

We start by considering the statement of the theorem in the particular case $b=0.$

Notice that if $b=0$, then the given linear congruence has a solution $x\equiv 0 \:(\text{mod}\:n).$ So, we need to prove that $ax \equiv b \:(\text{mod}\:n)$ has a solution in the case $b\neq 0.$

To prove the statement of the theorem in the case $b\neq 0,$ we use proof by contradiction.

Assume for the contradiction that the linear congruence $ax \equiv b \:(\text{mod}\:n)$ has no solutions for $b\neq 0.$

We now use the definition of modular congruence.

By the definition of congruence modulo $n$, this means that, for all $p, q \in \Bbb Z{:}$

$$


ap-b \neq nq \qquad (*)


$$

Let's apply the Bézout's identity:

On the other hand, since $\text{gcd}(a,n)= 1$, according to Bézout's identity there must exist integers $u$ and $v$ such that

$$


au+nv=1.


$$

This leads to a contradiction:

So, since inequality $(*)$ holds for ** integers $p$ and $q,$ we can set

$$


p=ub, \quad q= -vb,


$$

and substitute these values in $(*).$ Then, using the fact that $b\neq0,$ we get

$$


aub- b \neq -nvb \quad \Rightarrow \quad au+nv\neq 1,


$$

which contradicts the fact that $au+nv = 1.$

Finally, we state the conclusion:

Therefore, our assumption must be false, and we conclude that the linear congruence $ax \equiv b \:(\text{mod}\:n)$ has a solution.

### Proving Uniqueness

Let's once again consider the linear congruence

$$


ax\equiv b \quad (\textrm{mod } n)


$$

where $a, b\in\mathbb Z, n\in \mathbb N,$ and $\textrm{gcd}(a,n) = 1.$

We've proved that this congruence has a solution, and this solution is given by

$$


x_1 \equiv a^{-1}\cdot b \quad (\textrm{mod } n)


$$

where $a^{-1}$ is the multiplicative inverse of $a.$

Proving that a solution exists is only half the story. We know from previous lessons that this solution is *unique* up to congruence modulo $n.$ So, how do we prove this?

To prove that $x_1$ is the unique solution to the congruence, we can use proof by contradiction. The idea is to assume another solution $x_2$ exists, where $x_2\not\equiv x_1,$ and show that this leads to a contradiction.

Let's see an example.

### Example: Proving the Uniqueness of the Solution to a Congruence

#### Question

Prove the following theorem:

Let $a$ and $b$ be integers and $n$ be a positive integer with $\text{gcd}(a,n)=1.$ If $x_1$ denotes the solution to the congruence $ax \equiv b \:(\text{mod}\:n),$ then this solution is unique up to congruence modulo $n.$

#### Explanation

We'll prove this by contradiction, proceeding as follows:

Let's assume for a contradiction that the solution $x_1$ is not unique. This mean that there exists $x_2 \in \mathbb{Z}$ such that

$$


x_1 \not\equiv x_2 \: (\textrm{mod}\:n) \qquad\textrm{and}\qquad ax_2 \equiv b \: (\textrm{mod}\:n).


$$

Our goal is to reach a contradiction that shows $x_1$ and $x_2$ must be congruent modulo $n.$

Since $x_1$ and $x_2$ are both solutions, we have the following congruences:

$$


\begin{aligned}𝑎𝑥_{1}≡𝑏\,(mod\,𝑛) \\ 𝑎𝑥_{2}≡𝑏\,(mod\,𝑛)\end{aligned}


$$

If we subtract them using the subtraction property of congruences, we get:

$$


\begin{aligned}𝑎𝑥_{1}−𝑎𝑥_{2} & ≡𝑏−𝑏\, & & (mod\,𝑛) \\ 𝑎(𝑥_{1}−𝑥_{2}) & ≡0\, & & (mod\,𝑛)\end{aligned}


$$

Let's continue:

By subtracting the two congruences for $x_1$ and $x_2,$ we obtain

$$


a(x_1-x_2) \equiv 0 \: (\textrm{mod}\:n).


$$

Now, we use the fact that $a$ and $n$ are coprime to divide the congruence by $a{:}$

Since $\text{gcd}(a,n)=1,$ we can apply the division property of congruences to get

$$


x_1-x_2 \equiv 0 \: (\textrm{mod}\:n) \qquad\Leftrightarrow\qquad x_1 \equiv x_2 \: (\textrm{mod}\:n),


$$

which is a contradiction since $x_1\not\equiv x_2$ by assumption.

Since we have a contradiction, our proof is complete, and we can write down our conclusion.

Therefore, our assumption that $x_1\not\equiv x_2$ is false. Hence, $x_1\equiv x_2$ is true, which means $x_1$ is the unique solution of the linear congruence.

### Stating a Full Proof of Existence and Uniqueness

Let's combine our theorems about the existence and uniqueness of solutions to congruences into one **existence and uniqueness** theorem.

Theorem:

Let $a$ and $b$ be integers and $n$ be a positive integer. If $\text{gcd}(a,n)=1$, then the linear congruence $ax \equiv b \:(\text{mod}\:n)$ has a unique solution.

For existence and uniqueness proofs, it's normal to write the proof in two parts, as follows.

**Proof of existence:**

If $\text{gcd}(a,n)=1$, then by Bézout's identity, there exist integers $u$ and $v$ such that

$$


au+nv=1.


$$

We can write this result in modulo $n,$ as follows:

$$


\begin{aligned}𝑎𝑢+𝑛𝑣 & ≡1 & & (mod\,𝑛) \\ 𝑎𝑢 & ≡1 & & (mod\,𝑛)\end{aligned}


$$

This means that $u$ is the multiplicative inverse of $a$ (modulo $n$).

So, multiplying both sides of the original congruence $ax \equiv b \:(\text{mod}\:n)$ by $u,$ we get

$$


\begin{aligned}𝑎𝑥 & ≡𝑏 & & (mod\,𝑛) \\ 𝑢⋅𝑎𝑥 & ≡𝑢⋅𝑏 & & (mod\,𝑛) \\ (𝑢⋅𝑎)𝑥 & ≡𝑢𝑏 & & (mod\,𝑛) \\ 1⋅𝑥 & ≡𝑢𝑏 & & (mod\,𝑛) \\ 𝑥 & ≡𝑢𝑏 & & (mod\,𝑛)\end{aligned}


$$

Therefore, the congruence has the solution $x_1 \equiv ub \: (\text{mod}\:n).$

**Proof of uniqueness:**

Let's assume for a contradiction that the solution $x_1$ is not unique. This means that there exists $x_2 \in \mathbb{Z}$ such that

$$


x_1 \not\equiv x_2 \: (\textrm{mod}\:n) \qquad\textrm{and}\qquad ax_2 \equiv b \: (\textrm{mod}\:n).


$$

By subtracting the two congruences for $x_1$ and $x_2,$ we obtain

$$


a(x_1-x_2) \equiv 0 \: (\textrm{mod}\:n).


$$

Since $\text{gcd}(a,n)=1,$ we can apply the division property of congruences to get

$$


x_1-x_2 \equiv 0 \: (\textrm{mod}\:n) \qquad\Leftrightarrow\qquad x_1 \equiv x_2 \: (\textrm{mod}\:n),


$$

which is a contradiction since $x_1\not\equiv x_2$ by assumption.

Therefore, our assumption that $x_1\not\equiv x_2$ is false. Hence, $x_1\equiv x_2$ is true, which means $x_1$ is the unique solution of the linear congruence.

So far, we've only considered congruences with a unique solution. But we're also aware that some congruences have no solutions, and others have many solutions. We'll study these theorems next.

### Example: Proving That a Congruence Has No Solution

#### Question

Prove the following theorem:

Let $a,$ $b,$ and $n$ be integers. If $\text{gcd}(a,n)=k \gt 1$ and $k \not\mid b,$ then the linear congruence $ax \equiv b \:(\text{mod}\:n)$ has no solution.

#### Explanation

First, we expand the conditions of the theorem:

We assume $\gcd(a,n) = k > 1.$ Therefore, by Bézout's identity, there exist $u,v \in \mathbb{Z}$ such that

$$


au+nv=k.


$$

Moreover, any number of the form

$$


au'+nv',


$$

where $u'$ and $v'$ are integers, is a multiple of $k.$

Since we are trying to prove a negation (i.e., that a solution does ** exist), it's often easier to use proof by contradiction.

So, we proceed as follows:

Assume for a contradiction that $ax \equiv b \:(\text{mod}\:n)$ has a solution, which means that there exists $x_1 \in \mathbb{Z}$ such that

$$


ax_1 \equiv b \:(\text{mod}\:n).


$$

Now, by the definition of integer congruence, there exists $c \in \mathbb{Z}$ such that

$$


ax_1 - b = nc \qquad\Rightarrow\qquad ax_1 + (-nc) = b \qquad\Rightarrow\qquad ax_1 + n(-c) =b.


$$

Next, we use the results deduced from the conditions of the theorem.

Now, setting $x_1 = u'$ and $(-c) = v',$ we have that

$$


au'+nv' = b,


$$

which means $b$ must be a multiple of $k.$

This gives us our contradiction:

This is a contradiction to our assumption that $k \not\mid b.$

Finally, we write down the conclusion:

Therefore, the assumption that $ax \equiv b \:(\text{mod}\:n)$ has a solution is false, and we conclude that the congruence has no solution.

### Example: Proving the Number of Solutions to a Congruence

#### Question

Prove the following theorem:

Let $a$ and $b$ be integers and $n$ be a positive integer. If $\text{gcd}(a,n)=k \gt 1$ with $k \mid b,$ then the congruence $ax \equiv b \:(\text{mod}\:n)$ has exactly $k$ distinct solutions modulo $n.$

#### Explanation

We start by using the conditions given in the theorem:

First, we assume by hypothesis that $\text{gcd}(a,n)=k \gt 1$ and $k \mid b,$ meaning that there exist $a_1,n_1,b_1 \in \mathbb{Z}$ such that

$$


a=a_1k, \qquad n=n_1k, \qquad b=b_1 k.


$$

Since $k$ is the greatest common divisor of $a$ and $n$, the integers $a_1$ and $n_1$ must satisfy $\text{gcd}(a_1,n_1)=1.$

Now, we use Bézout's identity:

Therefore, by Bézout's identity, there exist integers $u$ and $v$ such that

$$


a_1u+n_1v = 1.


$$

We rewrite the above equation as a congruence and use the fact that $n_1 \equiv 0 \, \, (\text{mod}\:n_1){:}$

Since $n_1 \equiv 0 \, \, (\text{mod}\:n_1),$ we can re-write this equation as the following congruence:

$$


\begin{aligned}𝑎_{1}𝑢+𝑛_{1}𝑣 & ≡1 & & (mod\,𝑛_{1}) \\ 𝑎_{1}𝑢 & ≡1 & & (mod\,𝑛_{1}).\end{aligned}


$$

This means that $u$ is the multiplicative inverse of $a_1$ (modulo $n_1$).

Now, consider the congruence $a_1 \cdot x \equiv b_1\: (\text{mod}\:n_1).$ Since $\text{gcd}(a_1,n_1)=1,$ this congruence has the unique solution $x_1$ modulo $n_1.$ We can find this solution using the multiplicative inverse of $a_1$ found above.

So, multiplying both sides of the congruence $a_1x_1 \equiv b_1 \:(\text{mod}\:n_1)$ by $u,$ we get

$$


\begin{aligned}𝑎_{1}𝑥_{1} & ≡𝑏_{1} & & (mod\,𝑛_{1}) \\ 𝑢⋅𝑎_{1}𝑥_{1} & ≡𝑢⋅𝑏_{1} & & (mod\,𝑛_{1}) \\ (𝑢⋅𝑎_{1})𝑥_{1} & ≡𝑢𝑏_{1} & & (mod\,𝑛_{1}) \\ 1⋅𝑥_{1} & ≡𝑢𝑏_{1} & & (mod\,𝑛_{1}) \\ 𝑥_{1} & ≡𝑏_{1}𝑢 & & (mod\,𝑛_{1})\end{aligned}


$$

Consequently, $a_1 x_1 \equiv b_1 \:(\text{mod}\:n_1)$ has a unique solution $x_1=b_1u$ modulo $n_1,$ and $x_1$ is also a solution of the original linear congruence.

Given a solution $x_1$ of our congruence, we can construct the other solutions based on $x_1.$

Therefore, all the solutions of the original congruence must be congruent to $x_1$ modulo $n_1.$

Let us now consider for each $i \in \{1,\ldots, k \},$ the following expression:

$$


x_i = x_1 + (i-1)\cdot n_1


$$

Note that indexes larger than $k$ will lead to repeating solutions modulo $n=n_1k.$

Now, we show that these are solutions of the original congruence.

We will prove that $x_i$ is a solution of the original linear congruence for each $1 \leq i \leq k.$ Indeed,

$$


\begin{aligned}↔ & \,𝑎_{1}𝑥_{1} & & ≡𝑏_{1} & & & (mod\,𝑛_{1}) \\ ⇔ & \,𝑎_{1}(𝑥_{1}+(𝑖−1)𝑛_{1}) & & ≡𝑏_{1} & & & (mod\,𝑛_{1}) \\ ⇔ & \,𝑘𝑎_{1}(𝑥_{1}+(𝑖−1)𝑛_{1}) & & ≡𝑘𝑏_{1} & & & (mod\,𝑘𝑛_{1}) \\ ⇔ & \,𝑎(𝑥_{1}+(𝑖−1)𝑛_{1}) & & ≡𝑏 & & & (mod\,𝑛) \\ ⇔ & \,𝑎𝑥_{𝑖} & & ≡𝑏 & & & (mod\,𝑛)\end{aligned}


$$

Now, we need to show that the solutions found are all distinct:

These values form distinct solutions, meaning they are mutually non-congruent modulo $n.$ Indeed, if $i$ and $j$ are indices from $\{1,2,\ldots, k-1\}$ and $i \neq j,$ then, by assuming for a contradiction that $x_i \equiv x_j \: (\textrm{mod}\:n),$ we get the following:

$$


\begin{aligned}𝑥_{𝑖} & ≡𝑥_{𝑗} & & (mod\,𝑛) \\ 𝑥_{1}+(𝑖−1)𝑛_{1} & ≡𝑥_{1}+(𝑗−1)𝑛_{1} & & (mod\,𝑛) \\ (𝑖−1)𝑛_{1} & ≡(𝑗−1)𝑛_{1} & & (mod\,𝑛_{1}𝑘) \\ (𝑖−1) & ≡(𝑗−1) & & (mod\,𝑘) \\ 𝑖 & ≡𝑗 & & (mod\,𝑘)\end{aligned}


$$

Since both values are smaller than $k,$ the final congruence means that $i=j,$ which is a contradiction.

Finally, we write down the conclusion.

Therefore, our congruence has exactly $k$ distinct solutions modulo $n.$

The full proof is stated below:

First, we assume by hypothesis that $\text{gcd}(a,n)=k \gt 1$ and $k \mid b,$ meaning that there exist $a_1,n_1,b_1 \in \mathbb{Z}$ such that

$$


a=a_1k, \qquad n=n_1k, \qquad b=b_1 k.


$$

Since $k$ is the greatest common divisor of $a$ and $n$, the integers $a_1$ and $n_1$ must satisfy $\text{gcd}(a_1,n_1)=1.$

Therefore, by Bézout's identity, there exist integers $u$ and $v$ such that

$$


a_1u+n_1v = 1.


$$

Since $n_1 \equiv 0 \, \, (\text{mod}\:n_1),$ we can re-write this equation as the following congruence:

$$


\begin{aligned}𝑎_{1}𝑢+𝑛_{1}𝑣 & ≡1 & & (mod\,𝑛_{1}) \\ 𝑎_{1}𝑢 & ≡1 & & (mod\,𝑛_{1}).\end{aligned}


$$

This means that $u$ is the multiplicative inverse of $a_1$ (modulo $n_1$).

So, multiplying both sides of the congruence $a_1x_1 \equiv b_1 \:(\text{mod}\:n_1)$ by $u,$ we get

$$


\begin{aligned}𝑎_{1}𝑥_{1} & ≡𝑏_{1} & & (mod\,𝑛_{1}) \\ 𝑢⋅𝑎_{1}𝑥_{1} & ≡𝑢⋅𝑏_{1} & & (mod\,𝑛_{1}) \\ (𝑢⋅𝑎_{1})𝑥_{1} & ≡𝑢𝑏_{1} & & (mod\,𝑛_{1}) \\ 1⋅𝑥_{1} & ≡𝑢𝑏_{1} & & (mod\,𝑛_{1}) \\ 𝑥_{1} & ≡𝑏_{1}𝑢 & & (mod\,𝑛_{1})\end{aligned}


$$

Consequently, $a_1 x_1 \equiv b_1 \:(\text{mod}\:n_1)$ has a unique solution $x_1=b_1u$ modulo $n_1,$ and $x_1$ is also a solution of the original linear congruence.

Therefore, all the solutions of the original congruence must be congruent to $x_1$ modulo $n_1.$

Let us now consider for each $i \in \{1,\ldots, k \},$ the following expression:

$$


x_i = x_1 + (i-1)\cdot n_1


$$

Note that indexes larger than $k$ will lead to repeating solutions modulo $n=n_1k.$

We will prove that $x_i$ is a solution of the original linear congruence for each $1 \leq i \leq k.$ Indeed,

$$


\begin{aligned}↔ & \,𝑎_{1}𝑥_{1} & & ≡𝑏_{1} & & & (mod\,𝑛_{1}) \\ ⇔ & \,𝑎_{1}(𝑥_{1}+(𝑖−1)𝑛_{1}) & & ≡𝑏_{1} & & & (mod\,𝑛_{1}) \\ ⇔ & \,𝑘𝑎_{1}(𝑥_{1}+(𝑖−1)𝑛_{1}) & & ≡𝑘𝑏_{1} & & & (mod\,𝑘𝑛_{1}) \\ ⇔ & \,𝑎(𝑥_{1}+(𝑖−1)𝑛_{1}) & & ≡𝑏 & & & (mod\,𝑛) \\ ⇔ & \,𝑎𝑥_{𝑖} & & ≡𝑏 & & & (mod\,𝑛)\end{aligned}


$$

These values form distinct solutions, meaning they are mutually non-congruent modulo $n.$

Indeed, if $i$ and $j$ are indices from $\{1,2,\ldots, k-1\}$ and $i \neq j,$ then, by assuming for a contradiction that $x_i \equiv x_j \: (\textrm{mod}\:n),$ we get the following:

$$


\begin{aligned}𝑥_{𝑖} & ≡𝑥_{𝑗} & & (mod\,𝑛) \\ 𝑥_{1}+(𝑖−1)𝑛_{1} & ≡𝑥_{1}+(𝑗−1)𝑛_{1} & & (mod\,𝑛) \\ (𝑖−1)𝑛_{1} & ≡(𝑗−1)𝑛_{1} & & (mod\,𝑛_{1}𝑘) \\ (𝑖−1) & ≡(𝑗−1) & & (mod\,𝑘) \\ 𝑖 & ≡𝑗 & & (mod\,𝑘)\end{aligned}


$$

Since both values are smaller than $k,$ the final congruence means that $i=j,$ which is a contradiction.

Therefore, our congruence has exactly $k$ distinct solutions modulo $n.$
