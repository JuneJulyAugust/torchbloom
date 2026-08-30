# Proving Divisibility Using Congruence

Source: https://www.mathacademy.com/topics/4435?courseId=76
Topic ID: 4435

## Prerequisites

- [Proof by Cases](./4432-proof-by-cases.md)

## Lesson

### Introduction

We can use modular congruences to prove statements about divisibility. Congruences often provide a more straightforward way of establishing the truth of a divisibility statement compared to other methods.

For example, let's prove the following proposition:

*$5^n - 1$ is divisible by $4$ for any integer $n \geq 1.$*

In this case, we need to show the following:

$$


n \geq 1 \quad\Rightarrow\quad 4 \mid (5^n- 1)


$$

We start by checking that the statement makes sense in the given domain of $n{:}$

*Notice that the expression $5^n -1$ gives us an integer value when $n \geq 1.$*

Recall that $n \mid a$ is equivalent to $a \equiv 0 \: (\text{mod}\:n).$ So, instead of proving divisibility by $4,$ we can show that our expression is congruent to $0$ modulo $4{:}$

*According to the definition of modular congruence,*

$$


4 \mid (5^n-1) \quad\Leftrightarrow\quad 5^n -1 \equiv 0 \: (\text{mod}\:4).


$$

Now, we proceed as follows:

*Working in modulo $4,$ we have the following:*

$$


\begin{aligned}5^{𝑛}−1 & ≡(1)^{𝑛}−1 & (mod\,4) \\ & ≡1−1 & (mod\,4) \\ & ≡0 & (mod\,4)\end{aligned}


$$

Finally, we make our conclusion:

*Therefore, $4 \mid (5^n -1),$ as required.*

For clarity, let's restate the proposition and full proof.

### Stating the Full Proof

Proposition:

*$5^n - 1$ is divisible by $4$ for any integer $n \geq 1.$*

Proof:

*Notice that the expression $5^n -1$ gives us an integer value when $n \geq 1.$*

*According to the definition of modular congruence,*

$$


4 \mid (5^n-1) \quad\Leftrightarrow\quad 5^n -1 \equiv 0 \: (\text{mod}\:4).


$$

*Working in modulo $4,$ we have the following:*

$$


\begin{aligned}5^{𝑛}−1 & ≡(1)^{𝑛}−1 & (mod\,4) \\ & ≡1−1 & (mod\,4) \\ & ≡0 & (mod\,4)\end{aligned}


$$

*Therefore, $4 \mid (5^n -1),$ as required.*

### Example: Proving the Divisibility of an Expression

#### Question

Prove that $4^{2n-3}+ 5$ is divisible by $3$ for any integer $n \geq 2.$

#### Explanation

In this case, we need to show the following:

$$


n \geq 2 \quad\Rightarrow\quad 3 \mid (4^{2n-3}+ 5)


$$

We start by checking that the statement makes sense in the given domain of $n{:}$

Notice that the expression $4^{2n-3}+ 5$ gives us an integer value when $n \geq 2.$

Recall that $n \mid a$ is equivalent to $a \equiv 0 \: (\text{mod}\:n).$ So, instead of proving divisibility by $3,$ we can show that our expression is congruent to $0$ modulo $3{:}$

According to the definition of modular congruence,

$$


3 \mid (4^{2n-3}+ 5) \quad\Leftrightarrow\quad 4^{2n-3}+ 5 \equiv 0 \: (\text{mod}\:3).


$$

Now, we proceed as follows:

Working in modulo $3,$ we have the following:

$$


\begin{aligned}4^{2𝑛−3}+5 & ≡(1)^{2𝑛−3}+2 & (mod\,3) \\ & ≡1+2 & (mod\,3) \\ & ≡3 & (mod\,3) \\ & ≡0 & (mod\,3)\end{aligned}


$$

Finally, we make our conclusion:

Therefore, $3 \mid (4^{2n-3}+ 5),$ as required.

### Example: Proof by Cases

#### Question

Prove that $n^3-n$ is divisible by $3{:}$

#### Explanation

Recall that $n \mid a$ is equivalent to $a \equiv 0 \: (\text{mod}\:n).$ So, instead of proving divisibility by $3,$ we can show that our expression is congruent to $0$ modulo $3{:}$

According to the definition of modular congruence,

$$


3 \mid (n^3-n) \quad\Leftrightarrow\quad n^3-n \equiv 0 \: (\text{mod}\:3).


$$

An integer can have only $0,$ $1,$ or $2$ as a remainder when divided by $3.$ So, we'll prove our congruence using cases.

Now, we have the following cases for $n{:}$

First, we take $n \equiv 0$ in our expression:

**** Suppose $n \equiv 0 \: (\text{mod}\:3).$ Then:

$$


\begin{aligned}𝑛^{3}−𝑛 & ≡(0)^{3}−(0) & (mod\,3) \\ & ≡0 & (mod\,3)\end{aligned}


$$

Next, we take $n \equiv 1{:}$

**** Suppose $n \equiv 1 \: (\text{mod}\:3).$ Then:

$$


\begin{aligned}𝑛^{3}−𝑛 & ≡(1)^{3}−(1) & (mod\,3) \\ & ≡0 & (mod\,3)\end{aligned}


$$

Then, we take $n \equiv 2{:}$

**** Suppose $n \equiv 2 \: (\text{mod}\:3).$ Then:

$$


\begin{aligned}𝑛^{3}−𝑛 & ≡(2)^{3}−(2) & (mod\,3) \\ & ≡6 & (mod\,3) \\ & ≡0 & (mod\,3)\end{aligned}


$$

Finally, we make our conclusion:

In all these cases, we obtain

$$


n^3-n \equiv 0 \quad (\text{mod}\:3).


$$

Therefore, $n^3-n$ is divisible by $3,$ as required.

### Divisibility Tests

You will have learned certain *divisibility tests* early in your mathematical career. One such rule is determining whether a number is divisible by $3$.

*An integer is divisible $3$ if and only if the sum of the digits is divisible by $3.$*

For example, we can use this rule to check that $2\,387\,465\,652$ is divisible by $3.$ The sum of the digits is given by

$$


2+3+8+7+4+6+5+6+5+2 = 48


$$

and $48$ is divisible by $3.$ Therefore, $2\,387\,465\,652$ is divisible by $3.$

These rules may have seemed mysterious when you first studied them. However, we can prove them using the properties of modular congruence!

To demonstrate, let's prove the "is divisible by $3$" rule.

First, let $N$ be a positive integer. We'll express $N$ in expanded form as follows:

$$


N = 10^{n}a_{n} + \cdots + 10^{2}a_{2} + 10a_{1} + a_0


$$

Here, $a_{n}, \ldots, a_2, a_{1}, a_{0}$ are the digits of the number.

We wish to prove the following statement:

$$


3 \mid N \quad \Leftrightarrow \quad 3 \mid \big( a_{n} + \cdots + a_{2} + a_{1} + a_0 \big).


$$

First, we write the statement in terms of congruences:

*According to the definition of modular congruence,*

$$


3 \mid N \quad\Leftrightarrow\quad N \equiv 0 \quad (\text{mod}\:3).


$$

Now, let's expand the left-hand side:

*Expressing $N$ in expanded form, we get*

$$


\begin{aligned}10^{𝑛}𝑎_{𝑛}+⋯+10^{2}𝑎_{2}+10𝑎_{1}+𝑎_{0} & ≡0 & (mod\,3).\end{aligned}


$$

Next, we need to show that this implies

$$


\begin{aligned}𝑎_{𝑛}+⋯+𝑎_{2}+𝑎_{1}+𝑎_{0}≡0\, & (mod\,3).\end{aligned}


$$

To do this, recall the multiplication properties of modular arithmetic:

- For any $k\in \mathbb N,$ we have $a \equiv b \:\Leftrightarrow\: a^k\equiv b^k \quad (\text{mod}\: n).$

- For any $c\in \mathbb Z\setminus\{0\},$ we have $a \equiv b \:\Leftrightarrow\: ac \equiv bc \quad (\text{mod}\: n).$

With this in mind, note that

$$


10 \equiv 1 \quad\Leftrightarrow\quad 10^k a_k \equiv 1^k a_k \qquad (\text{mod}\: 3).


$$

So, we proceed as follows:

*Now, without changing the congruence, we can swap each occurrence of $10$ with $1$ on the left-hand side since they're congruent modulo $3{:}$*

$$


\begin{aligned}10^{𝑛}𝑎_{𝑛}+⋯+10^{2}𝑎_{2}+10𝑎_{1}+𝑎_{0} & ≡0 & (mod\,3) \\ (1)^{𝑛}𝑎_{𝑛}+⋯+(1)^{2}𝑎_{2}+(1)𝑎_{1}+𝑎_{0} & ≡0 & (mod\,3) \\ 𝑎_{𝑛}+⋯+𝑎_{2}+𝑎_{1}+𝑎_{0} & ≡0 & (mod\,3)\end{aligned}


$$

Finally, we can write down that conclusion.

*Therefore, according to the definition of modular congruence, the final equation means that*

$$


3 \mid \big( a_{n} + \cdots + a_{2} + a_{1} + a_0 \big).


$$

And we're done!

**Note:** All the transformations we performed above also work in reverse, which means that the right-to-left implication is also true.

We can also use modular congruence to prove slightly more complex divisibility rules. Let's see an example.

### Example: Proving the Divisibility Tests

#### Question

Let $N = 10^{n}a_{n} + \cdots + 10^{2}a_{2} + 10a_{1} + a_0$ be a positive integer, where $a_{n}, \ldots, a_2, a_{1}, a_{0}$ are the digits of the number. Prove that if $13 \mid N,$ then

$$


13 \mid \big( 10^{n-1}a_{n} + \cdots + 10a_{2} + a_{1} + 4a_0 \big).


$$

#### Explanation

We need to prove the implication

$$


13 \mid N \quad \Rightarrow \quad 13 \mid \big( 10^{n-1}a_{n} + \cdots + 10a_{2} + a_{1} + 4a_0 \big).


$$

First, we write the statement in terms of congruences:

According to the definition of modular congruence,

$$


13 \mid N \quad\Leftrightarrow\quad N \equiv 0 \quad (\text{mod}\:13).


$$

Now, let's expand the left-hand side:

Substituting the expression for $N$ into the congruence, we get

$$


\begin{aligned}10^{𝑛}𝑎_{𝑛}+⋯+10^{2}𝑎_{2}+10𝑎_{1}+𝑎_{0} & ≡0 & (mod\,13).\end{aligned}


$$

Now, we need to show that this implies

$$


\begin{aligned}10^{𝑛−1}𝑎_{𝑛}+⋯+10𝑎_{2}+𝑎_{1}+4𝑎_{0}≡0\, & (mod\,13).\end{aligned}


$$

The idea is as follows:

- We add $13ka_0$ for some integer $k$ to the left-hand side. This will give an expression that's also congruent to zero.

- The value of $k$ that we pick should give a multiple of $10a_0$ when combined with the existing $a_0$ term. This allows us to factor $10$ from the left-hand side.

With this in mind, note that

$$


a_0+3\cdot 13 a_0 = a_0+39 a_0 = 40a_0.


$$

So, we proceed as follows:

Now, without changing the congruence, we can add $39a_0$ to the left-hand side since it's congruent to $0$ modulo $13{:}$

$$


\begin{aligned}10^{𝑛}𝑎_{𝑛}+⋯+10^{2}𝑎_{2}+10𝑎_{1}+𝑎_{0}+39𝑎_{0} & ≡0 & (mod\,13) \\ 10^{𝑛}𝑎_{𝑛}+⋯+10^{2}𝑎_{2}+10𝑎_{1}+40𝑎_{0} & ≡0 & (mod\,13) \\ 10(10^{𝑛−1}𝑎_{𝑛}+⋯+10𝑎_{2}+𝑎_{1}+4𝑎_{0}) & ≡0 & (mod\,13)\end{aligned}


$$

Next, we cancel out the factor of $10.$

Since $10$ and $13$ are coprime, we can use a division rule for congruences and cancel out the factor of $10$ to get

$$


\begin{aligned}10^{𝑛−1}𝑎_{𝑛}+⋯+10𝑎_{2}+𝑎_{1}+4𝑎_{0} & ≡0 & (mod\,13).\end{aligned}


$$

Finally, we can write down that conclusion.

Therefore, according to the definition of modular congruence, the final equation means that

$$


13 \mid \big( 10^{n-1}a_{n} + \cdots + 10a_{2} + a_{1} + 4a_0 \big).


$$

**** All the transformations we performed above also work in reverse, which means that the right-to-left implication is also true.

The obtained equivalence statement is known in arithmetic as the rule of divisibility by $13{:}$

**
