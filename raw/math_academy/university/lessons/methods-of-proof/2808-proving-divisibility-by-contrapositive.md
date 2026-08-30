# Proving Divisibility by Contrapositive

Source: https://www.mathacademy.com/topics/2808?courseId=76
Topic ID: 2808

## Prerequisites

- [Proving Divisibility](./2795-proving-divisibility.md)
- [Proof by Contrapositive](./2807-proof-by-contrapositive.md)
- [Simplifying Predicate Expressions Using De Morgan's Laws](./4302-simplifying-predicate-expressions-using-de-morgan-s-laws.md)

## Lesson

### Introduction

Recall that the conditional statement and its contrapositive are logically equivalent.

$$


P \Rightarrow Q \equiv \neg Q \Rightarrow \neg P


$$

We can use the contrapositive to prove statements about divisibility. To demonstrate, let's prove the following proposition using the contrapositive:

$$


\underbrace{d \not\mid 72}_{P} \quad\Rightarrow\quad \underbrace{d \not\mid 8}_{Q}.


$$

The contrapositive form of this statement is

$$


\underbrace{\lnot \Big( d \not\mid 8 \Big)}_{\lnot \, Q} \quad\Rightarrow\quad \underbrace{\lnot \Big( d \not\mid 72 \Big)}_{\lnot \, P},


$$

which is equivalent to

$$


d \mid 8 \quad\Rightarrow\quad d \mid 72.


$$

So, we proceed as follows:

*The contrapositive of the statement is*

$$


d \mid 8 \quad\Rightarrow\quad d \mid 72.


$$

*We will prove this statement instead of the original one.*

Recall that if an integer $a$ is divisible by $d,$ then there exists an integer $k$ such that $a = d \cdot k.$

Using this definition, we continue our proof as follows:

*By the definition of integer divisibility, we have*

$$


d \mid 8 \qquad\Leftrightarrow\qquad 8 = d \cdot k


$$

*for some integer $k.$*

Since we need to consider divisors of $72$ instead of $8,$ we multiply the last equation by $9{:}$

*Multiplying both sides of $8 = d k$ by $9,$ we obtain*

$$


\begin{aligned}9⋅8 & =9⋅𝑑𝑘 \\ 72 & =9𝑑𝑘 \\ 72 & =𝑑(9𝑘) \\ 72 & =𝑑𝑚\end{aligned}


$$

*where $m = 9k$ is an integer.*

Finally, we use the definition of integer divisibility once more:

*Therefore, by the definition of integer divisibility, $72 = dm$ means that $d \mid 72.$*

For clarity, let's restate the proposition and its proof.

### Restating the Full Proof

Proposition:

$$


\underbrace{d \not\mid 72}_{P} \quad\Rightarrow\quad \underbrace{d \not\mid 8}_{Q}.


$$

Proof:

*The contrapositive of the statement is*

$$


d \mid 8 \quad\Rightarrow\quad d \mid 72.


$$

*We will prove this statement instead of the original one.*

*By the definition of integer divisibility, we have*

$$


d \mid 8 \qquad\Leftrightarrow\qquad 8 = d \cdot k


$$

*for some integer $k.$*

*Multiplying both sides of $8 = d k$ by $9,$ we obtain*

$$


\begin{aligned}9⋅8 & =9⋅𝑑𝑘 \\ 72 & =9𝑑𝑘 \\ 72 & =𝑑(9𝑘) \\ 72 & =𝑑𝑚\end{aligned}


$$

*where $m = 9k$ is an integer.*

*Therefore, by the definition of integer divisibility, $72 = dm$ means that $d \mid 72.$*

### Example: Templates for Proving Divisibility by Contrapositive

#### Question

Consider the following statement:

If $7 \not\mid a,$ then $7 \not\mid 10a.$

What is the contrapositive form of this statement?

#### Explanation

The contrapositive of $P \Rightarrow Q$ is $\neg Q \Rightarrow \neg P.$

In this case, we have the statement

$$


\underbrace{7 \not\mid a}_{P} \quad\Rightarrow\quad \underbrace{7 \not\mid 10a}_{Q}.


$$

The contrapositive form of the statement is

$$


\underbrace{\lnot \Big(7 \not\mid 10a \Big)}_{\lnot \, Q} \quad\Rightarrow\quad \underbrace{\lnot \Big(7 \not\mid a \Big)}_{\lnot \, P},


$$

which is equivalent to

$$


7 \mid 10a \quad\Rightarrow\quad 7 \mid a.


$$

### Example: Proving Divisibility Using the Definition

#### Question

Let $a$ be an integer. Prove that $a$ is not divisible by $42$ whenever it is not divisible by $6.$

#### Explanation

Recall that the conditional statement $P \Rightarrow Q$ and its contrapositive $\neg Q \Rightarrow \neg P$ are logically equivalent. Moreover, it's sometimes easier to prove the contrapositive.

In this case, we need to show that

$$


𝑎


$$

The contrapositive form of this statement is

$$


𝑎


$$

which is equivalent to

$$


𝑎


$$

So, we proceed as follows:

The contrapositive of the statement is

$$


𝑎


$$

We will prove this statement instead of the original one.

Recall that if an integer $a$ is divisible by $d,$ then there exists an integer $k$ such that $a = d \cdot k.$

Using this definition, we continue the proof as follows:

By the definition of integer divisibility, if $a$ is divisible by $42,$ then

$$


a = 42k


$$

for some integer $k.$

Now, we'll rewrite our expression to explicitly show that $6$ is a factor of $a{:}$

Now, note that

$$


\begin{aligned}𝑎 & =42𝑘 \\ & =6⋅7⋅𝑘 \\ & =6(7𝑘) \\ & =6𝑚\end{aligned}


$$

where $m = 7k$ is an integer.

Finally, we use the definition of integer divisibility once more:

Therefore, by the definition of integer divisibility, since $a = 6m,$ we conclude that $a$ is divisible by $6.$

### Example: Proving a Divisor Given Two Other Divisors

#### Question

Let $a$ be an integer. Prove that if $36 \not\mid a,$ then $20 \not\mid a$ or $45 \not\mid a.$

#### Explanation

Recall that the conditional statement $P \Rightarrow Q$ and its contrapositive $\neg Q \Rightarrow \neg P$ are logically equivalent. Moreover, it's sometimes easier to prove the contrapositive.

In this case, we need to show that

$$


\underbrace{(36 \not\mid a)}_{P} \quad\Rightarrow\quad \underbrace{(20 \not\mid a) \:\lor\: (45 \not\mid a)}_{Q}.


$$

The contrapositive form of the statement is

$$


\underbrace{\lnot \Big( (20 \not\mid a) \:\lor\: (45 \not\mid a) \Big)}_{\lnot \, Q} \quad\Rightarrow\quad \underbrace{\lnot \Big( 36 \not\mid a \Big)}_{\lnot \, P},


$$

which is equivalent to

$$


(20 \mid a) \: \land\: (45 \mid a) \quad\Rightarrow\quad 36 \mid a.


$$

So, we proceed as follows:

The contrapositive of the statement is

$$


(20 \mid a) \: \land\: (45 \mid a) \quad\Rightarrow\quad 36 \mid a.


$$

We will prove this statement instead of the original one.

First, we recall the following fact:

$$


(d \mid a) \:\land\: (a \mid b) \quad\Rightarrow\quad d \mid b.


$$

Therefore, we start our proof as follows:

Because $4 \mid 20$ and $9 \mid 45,$ we have

$$


\begin{aligned}20∣𝑎 & \,⇒\,4∣𝑎, \\ 45∣𝑎 & \,⇒\,9∣𝑎.\end{aligned}


$$

Notice that $4$ and $9$ are coprime. As a result, their least common multiple equals the product of the numbers:

Since $4$ and $9$ are coprime, their least common multiple is given by

$$


\textrm{lcm}(4,9) = 36.


$$

We now make use of the division algorithm:

By the division algorithm, there exist integers $q$ and $r$ such that

$$


a = 36q + r, \qquad 0 \leq r \lt 36.


$$

We resort to the division algorithm because it closely resembles what we want, namely $a=36q.$ Our goal is to show that $r=0.$

The next step is to reason that $r$ (which we know should equal zero) is divisible by $4$ and $9.$ This is easier to see if we isolate $r,$ so let's do that.

Solving the left equation for $r,$ we get $r =a - 36q.$

Since both terms on the right-hand side are divisible by $4$ and $9,$ we can reason that $r$ is divisible by $4$ and $9{:}$

We have that $4 \mid a$ and $9 \mid a.$ Also, $36$ is divisible by both these numbers. So, $4 \mid r$ and $9 \mid r.$ This means $r$ is a common multiple of $4$ and $9.$

The realization that $r$ is a common multiple of $4$ and $9$ is the key to unlocking the proof.

To help us visualize the candidates for $r,$ let's write down a few common multiples of $4$ and $9{:}$

$$


\ldots,\qquad -72, \qquad -36, \qquad 0, \qquad 36, \qquad 72, \qquad \ldots


$$

The ** common multiple of $4$ and $9$ that satisfies $0 \leq r \lt 36$ is zero.

However, since $36$ is the least common multiple of $4$ and $9,$ and $0 \leq r \lt 36,$ we must have $r=0.$

Therefore, $a=36q+0=36q,$ and we make our conclusion using the definition of integer divisibility:

Therefore, since $a=36q,$ we have $36 \mid a.$
