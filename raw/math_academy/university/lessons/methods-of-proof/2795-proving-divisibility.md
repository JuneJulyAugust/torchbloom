# Proving Divisibility

Source: https://www.mathacademy.com/topics/2795?courseId=76
Topic ID: 2795

## Prerequisites

- [Direct Proof](./2801-direct-proof.md)
- [Disjunctive Syllogism and Transitivity of Implication](./4305-disjunctive-syllogism-and-transitivity-of-implication.md)

## Lesson

### Introduction

In a previous lesson, we spent some time constructing direct proofs of parity statements like the one below:

$$


n\text{ is even} \quad\Rightarrow\quad n^2\text{ is even}


$$

The key to unlocking these proofs was to use the *definition* of evenness.

In this lesson, we'll learn how to construct direct proofs of divisibility statements. For that, we need a formal definition of divisibility:

*Let $a$ and $d$ be integers with $d\neq 0.$ We say that $\boldsymbol d$ **** $\boldsymbol a$ if there exists an integer $k$ such that $a=d\cdot k.$*

If $d$ divides $a,$ then we write $d\mid a.$

Correctly applying the definition of divisibility is an essential part of most proofs involving divisibility of integers.

### Proving a Divisibility Statement

Let's prove the following statement:

*If $d \mid 15,$ then $d \mid 60$*

We begin by writing this statement as an implication:

$$


\underbrace{d \mid 15}_{P(d)} \qquad\Rightarrow\qquad \underbrace{d \mid 60}_{Q(d)}


$$

It's clear from the context that the universal set of $P$ and $Q$ is given by $d\in \mathbb Z\setminus \{0\}.$ In other words, $d$ must be a nonzero integer.

According to our definition of divisibility, an integer $a$ is divisible by $d$ if there exists an integer $k$ such that $a = d \cdot k.$

We begin our proof by assuming that $P(d)$ is true and applying the definition of divisibility.

*Suppose $d\mid 15.$ By the definition of integer divisibility, we have*

$$


d \mid 15 \qquad\Leftrightarrow\qquad 15 = d \cdot k


$$

*for some integer $k.$*

Since we need to consider divisors of $60$ instead of $15,$ let's multiply the last equation by $4{:}$

*Multiplying both sides of the equation $15 = dk$ by $4,$ we obtain the following chain of implications:*

$$


\begin{aligned}15=𝑑𝑘\, & ⇒\,4⋅15=4⋅𝑑𝑘 \\ & ⇒\,60=4𝑑𝑘 \\ & ⇒\,60=𝑑⋅4𝑘\end{aligned}


$$

Now, we need to use the definition of divisibility once more to show that $d$ divides $60.$ To do this, we need to write $60=d\cdot m,$ where $m$ is an integer. So, we simply define a new integer $m = 4k$ and continue our proof.

$$


\begin{aligned}60=𝑑⋅4𝑘\,⇒\,60 & =𝑑𝑚\end{aligned}


$$

*where $m=4k$ is an integer.*

Finally, we state our conclusion.

*Therefore, by the definition of integer divisibility, since $60=dm,$ we have that $d \mid 60.$*

Let's now state the full proof.

### Stating the Full Proof

Proposition:

*If $d \mid 15,$ then $d \mid 60$*

Proof:

*Suppose $d\mid 15.$ By the definition of integer divisibility, we have*

$$


d \mid 15 \qquad\Leftrightarrow\qquad 15 = d \cdot k


$$

*for some integer $k.$*

*Multiplying both sides of the equation $15 = dk$ by $4,$ we obtain the following chain of implications:*

$$


\begin{aligned}15=𝑑𝑘\, & ⇒\,60=4𝑑𝑘 \\ & ⇒\,60=𝑑⋅4𝑘 \\ & ⇒\,60=𝑑𝑚\end{aligned}


$$

*where $m=4k$ is an integer.*

*Therefore, by the definition of integer divisibility, since $60=dm,$ we have that that $d \mid 60.$*

So, by transitivity of implication, we have shown that

$$


15 = dk \qquad \Rightarrow \qquad 60 = dm.


$$

In other words, $d \mid 15$ implies $d \mid 60.$

In this particular proof, we used an explicit chain of implications to show our result is true. We can also construct a proof where these implications are present but are more implicit. Let's see an example.

### Example: Proving Divisibility Using the Definition

#### Question

Let $a \in \mathbb Z.$ Prove that $a$ is divisible by $2$ if it is divisible by $10.$

#### Explanation

In this case, we need to show the following:

$$


𝑎


$$

Recall that if an integer $a$ is divisible by $d,$ then there exists an integer $k$ such that $a = d \cdot k.$

Using this definition, we begin our proof as follows:

By the definition of integer divisibility, if $a$ is divisible by $10,$ then

$$


a = 10k


$$

for some integer $k.$

Now, we'll rewrite our expression to explicitly show that $2$ is a factor of $a{:}$

Now, note that

$$


\begin{aligned}𝑎 & =10𝑘 \\ & =2⋅5⋅𝑘 \\ & =2(5𝑘) \\ & =2𝑚\end{aligned}


$$

where $m=5k$ is an integer.

Finally, we use the definition of integer divisibility once more:

Therefore, by the definition of integer divisibility, since $a=2m,$ we conclude that $a$ is divisible by $2.$

### Example: Proving a Divisor of a Factor Given a Divisor of a Product

#### Question

Let $a \in \mathbb{Z}.$ Prove that $5 \mid a$ if $5 \mid 9a.$

You may make use of the following result:

$$


5\cdot2-9\cdot1=1


$$

#### Explanation

In this case, we need to show the following:

$$


5 \mid 9a \quad\Rightarrow\quad 5 \mid a


$$

Recall that if an integer $a$ is divisible by $d,$ then there exists an integer $k$ such that $a = d \cdot k.$

Using this definition, we begin our proof as follows:

By the definition of divisibility of integers, we have

$$


5 \mid 9a \qquad\Leftrightarrow\qquad 9a = 5k


$$

for some integer $k.$

Now, we use the fact that $5\cdot2-9\cdot 1=1.$

We have the following result:

$$


5\cdot2-9 \cdot 1=1


$$

Multiplying both sides of this equation by $a,$ we get

$$


5\big(2a\big) - \big(9a\big) = a.


$$

Notice that the first term on the left-hand side is already divisible by $5.$ To show that the other term is also divisible by $5,$ we use the fact that $9a = 5k$ from the beginning of the proof:

Now, substituting $5k$ for $9a,$ we obtain

$$


\begin{aligned}5(2𝑎)−(5𝑘) & =𝑎 \\ 5(2𝑎−𝑘) & =𝑎 \\ 5𝑚 & =𝑎\end{aligned}


$$

where $m=2a - k$ is an integer.

Finally, we will use the definition of integer divisibility once more:

Therefore, according to the definition of integer divisibility, $5m=a$ means that $5 \mid a.$

### The Division Algorithm

Recall that the *division algorithm* states that if $a$ is an integer and $b$ is a positive integer, there exist integers $q$ (quotient) and $r$ (remainder) such that

$$


a = bq + r, \qquad 0 \leq r \lt b.


$$

One thing to note immediately is that if $b \mid a,$ then we must have $r=0.$ Therefore, one method of showing that $b \mid a$ is to write down the relationship between $a$ and $b$ given by the division algorithm and then construct an argument to show that $r=0.$

Let's see an example.

### Example: Proving a Divisor Given Two Other (Coprime) Divisors

#### Question

Let $a \in \mathbb{Z}.$ Prove that if $4 \mid a$ and $15 \mid a,$ then $60 \mid a.$

Since $4$ and $15$ are coprime, we have $\gcd(4,15)=$ $𝐴𝐴𝐴𝐴𝐴_{𝐴𝐴}$.

By Bézout's identity, there exist integers $u$ and $v$ such that

$$


𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴_{𝐴𝐴}


$$

Multiplying both sides by $a,$ we get

$$


4ua+15va=a.


$$

Since $4\mid a$ and $15\mid a,$ there exist integers $k$ and $m$ such that $𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴_{𝐴𝐴}$.

Substituting these for $a$ into the left-hand side of the expression above, we obtain

$$


𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴_{𝐴𝐴}


$$

Since $um+vk$ is $𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴_{𝐴𝐴}$, we conclude that $60\mid a.$

#### Explanation

In this case, we need to show the following:

$$


(4 \mid a) \: \land\: (15 \mid a) \quad\Rightarrow\quad 60 \mid a


$$

Notice that $4$ and $15$ are coprime, which means their greatest common divisor is $1{:}$

Since $4$ and $15$ are coprime, we have $\gcd(4, 15) = 1.$

We now use Bézout’s identity:

By Bézout’s identity, there exist integers $u$ and $v$ such that

$$


4u+15v = 1.


$$

Since we want to relate $a$ with $4$ and $15$, we multiply both sides by $a{:}$

Multiplying both sides by $a,$ we get

$$


4ua+15va = a.


$$

We use now the fact that $4\mid a$ and $15 \mid a,$ along with the definition of divisibility.

Since $4 \mid a$ and $15 \mid a,$ there exists integers $k$ and $m$ such that $a = 4k$ and $a = 15m.$

We use these expressions for $a$ to rewrite the left-hand side of the equality above, obtaining an expression relating $60$ and $a{:}$

Substituting these expressions for $a$ into the left-hand side of the expression above, we obtain

$$


\begin{aligned}𝑎 & =4𝑢𝑎+15𝑣𝑎 \\ & =4𝑢(15𝑚)+15𝑣(4𝑘) \\ & =60𝑢𝑚+60𝑣𝑘 \\ & =60(𝑢𝑚+𝑣𝑘).\end{aligned}


$$

By the definition of divisibility once more, we have that $60$ divides $a{:}$

Since $um+vk$ is an integer, we conclude that $60 \mid a.$

### Example: Proving a Divisor Given Two Other (Coprime) Divisors: Advanced Cases

#### Question

Let $a \in \mathbb{Z}.$ Prove that if $20 \mid a$ and $21 \mid a,$ then $35 \mid a.$

Because $5 \mid 20$ and $7 \mid 21,$ we have

$$


\begin{aligned}20∣𝑎 & \,⇒\,\phantom{AAAAAAA_A^A}∣𝑎, \\ 21∣𝑎 & \,⇒\,\phantom{AAAAAAA^A}∣𝑎.\end{aligned}


$$

Since $5$ and $7$ are coprime, we have $\gcd(5,7)=$ $𝐴𝐴𝐴𝐴𝐴𝐴𝐴^{𝐴}$.

By Bézout's identity, there exist integers $u$ and $v$ such that

$$


𝐴𝐴𝐴𝐴𝐴𝐴𝐴_{𝐴𝐴}


$$

Multiplying both sides by $a,$ we get

$$


5ua+7va=a.


$$

Since $5\mid a$ and $7\mid a,$ there exist integers $k$ and $m$ such that $𝐴𝐴𝐴𝐴𝐴𝐴𝐴_{𝐴𝐴}$.

Substituting these for $a$ into the left-hand side of the expression above, we obtain

$$


𝐴𝐴𝐴𝐴𝐴𝐴𝐴_{𝐴𝐴}


$$

Since $um+vk$ is $𝐴𝐴𝐴𝐴𝐴𝐴𝐴_{𝐴𝐴}$, we conclude that $35\mid a.$

#### Explanation

In this case, we need to show the following:

$$


(20 \mid a) \: \land\: (21 \mid a) \quad\Rightarrow\quad 35 \mid a


$$

First, we recall the following fact:

$$


(d \mid a) \:\land\: (b \mid d) \quad\Rightarrow\quad b \mid a


$$

Therefore, we start our proof as follows:

Because $5 \mid 20$ and $7 \mid 21,$ we have

$$


\begin{aligned}20∣𝑎 & \,⇒\,5∣𝑎, \\ 21∣𝑎 & \,⇒\,7∣𝑎.\end{aligned}


$$

Notice that $5$ and $7$ are coprime, which means their greatest common divisor is $1{:}$

Since $5$ and $7$ are coprime, we have $\gcd(5, 7) = 1.$

We now use Bézout’s identity:

By Bézout’s identity, there exist integers $u$ and $v$ such that

$$


5u+7v = 1.


$$

Since we want to relate $a$ with $5$ and $7$, we multiply both sides by $a{:}$

Multiplying both sides by $a,$ we get

$$


5ua+7va = a.


$$

We now use the fact that $5\mid a$ and $7 \mid a,$ along with the definition of divisibility.

Since $5 \mid a$ and $7 \mid a,$ there exist integers $k$ and $m$ such that $a = 5k$ and $a = 7m.$

We use these expressions for $a$ to rewrite the left-hand side of the equality above, obtaining an expression relating $35$ and $a{:}$

Substituting these for $a$ into the left-hand side of the expression above, we obtain

$$


\begin{aligned}𝑎 & =5𝑢𝑎+7𝑣𝑎 \\ & =5𝑢(7𝑚)+7𝑣(5𝑘) \\ & =35𝑢𝑚+35𝑣𝑘 \\ & =35(𝑢𝑚+𝑣𝑘).\end{aligned}


$$

By the definition of divisibility once more, we have that $35$ divides $a{:}$

Since $um+vk$ is an integer, we conclude that $35 \mid a.$
