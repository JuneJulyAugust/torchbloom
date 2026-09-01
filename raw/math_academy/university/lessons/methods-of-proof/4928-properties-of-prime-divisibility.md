# Properties of Prime Divisibility

Source: https://www.mathacademy.com/topics/4928?courseId=76
Topic ID: 4928

## Prerequisites

- [Properties of Integer Divisibility](./4433-properties-of-integer-divisibility.md)

## Lesson

### Introduction

In this lesson, we'll focus on understanding and applying divisibility properties with prime numbers.

Let's state our first property:

**Theorem**

*For any positive integers $m$ and $n$ and any prime numbers $p$ and $q,$ we have that*

$\qquad$ *$p^m \mid q^n \quad\text{or}\quad q^n \mid p^m \qquad\Longrightarrow\qquad p = q.$*

We can prove this property using proof by contradiction.

**Proof**

*We need to show that*

- *if $p^m \mid q^n$ then $p = q,$ and*

- *if $q^n \mid p^m$ then $p = q.$*

*Let's suppose $p^m \mid q^n.$ For a contradiction, let's assume $p \neq q.$ Then, $\text{gcd}(p,q) = 1,$ and there exist integers $r$ and $s$ such that*

$$


pr + qs = 1.


$$

*Since $p \mid p^m$ and $p^m \mid q^n,$ by the transitivity of division, $p \mid q^n.$ Now, multiplying the above equation by $q^{n-1},$ we get*

$$


prq^{n-1} + q^n s = q^{n-1}


$$

*Looking at the left-hand side of this equation, we have that*

- *$p \mid prq^{n-1}$ (since it has a factor $p$), and*

- *$p \mid q^n s$ (since $p \mid q^n,$ as we deduced earlier).*

*Hence, $p \mid q^{n-1}.$*

*Repeating the same argument several times, we obtain that*

$$


p \mid q^{n}, \quad p \mid q^{n-1}, \quad p \mid q^{n-2}, \quad p \mid q^{n-3}, \quad \ldots,


$$

*and, eventually, $p \mid q.$ But this is a contradiction because $p$ and $q$ are distinct primes.*

*Therefore, our assumption that $p \neq q$ was wrong. Therefore, $p=q.$*

Note that the case $q^n \mid p^m\Rightarrow q\mid p$ is proved in the same way.

### Example: Identifying True Statements Concerning Prime Divisibility

#### Question

Let $q$ be a prime number. Which of the following statements are true?

1. If $9\: | \ q^5$ then $q = 3$

2. If $q^2 \: | \: 2^3$ then $q = 8$

3. If $q^2 \: | \: 8$ then $q = 2$

#### Explanation

For any integers $m$ and $n$ and any prime numbers $p$ and $q,$ we have that

$p^m \mid q^n \quad\text{or}\quad q^n \mid p^m \qquad\Longrightarrow\qquad p = q.$

With that in mind, let's examine each of the statements.

- Statement I is true. Since $9=3^2$ and $9 \: | \: q^5,$ then $3^2 \: | \: q^5.$ As $3$ and $q$ are prime numbers, $2$ and $5$ are integers, and $3^2\: | \ q^5,$ we must have $q = 3.$

- Statement II is false. As a counterexample, let ${\color{blue}{q}}={\color{blue}{2}}.$ Then, ${\color{blue}{2}}^2\mid 2^3$ but ${\color{blue}{2}}\neq 8.$

- Statement III is true. Since $8=2^3$ and $q^2 \: | \: 8,$ then $q^2 \: | \: 2^3.$ As $q$ and $2$ are prime numbers, $2$ and $3$ are integers, and $q^2\: | \ 2^3,$ we must have $q = 2.$

Therefore, the correct answer is "I and III only."

### Euclid's Lemma

Let's state our next property, often called **Euclid's lemma**.

**Theorem (Euclid's Lemma)**

*For any integers $a$ and $b,$ and any prime $p,$*

$\qquad$ *$p \:|\: ab$ $\qquad\Longrightarrow\qquad$ $p \:|\: a \quad$ or $\quad p \:|\: b.$*

So, if $p$ divides a product of two factors, then $p$ divides at least one of the factors.

**Proof**

*Suppose that $p$ does not divide $a.$ We must show that $p$ divides $b.$*

*If the prime $p$ does not divide $a,$ then $p$ is not a factor in the prime decomposition of $a.$ Therefore, $a$ and $p$ must be coprime. This means there exist integers $r$ and $s$ such that*

$$


pr + as = \text{gcd}(a,p)=1.


$$

*On the other hand, given that $p\: | \: ab,$ there exists an integer $k$ such that*

$$


ab=pk.


$$

*Multiplying both sides of the first equation by $b$ and substituting $ab=pk,$ we obtain the following:*

$$


\begin{aligned}𝑝𝑟+𝑎𝑠 & =1 \\ (𝑝𝑟+𝑎𝑠)𝑏 & =𝑏 \\ 𝑝𝑟𝑏+(𝑎𝑏)𝑠 & =𝑏 \\ 𝑝𝑟𝑏+(𝑝𝑘)𝑠 & =𝑏 \\ 𝑝(𝑟𝑏+𝑘𝑠) & =𝑏.\end{aligned}


$$

*Since $r,b,k,$ and $s$ are integers, then $rb + ks$ is an integer too. Hence,*

$$


p\: | \: b.


$$

*Similarly, if we assume that $p$ does not divide $b,$ we get that $p \: | \: a.$*

### Example: Identifying True Statements Concerning Euclid's Lemma

#### Question

Which of the following statements are true?

1. If $5 \: | \: 14a$ then $5 \: | \: a$

2. If $7 \: | \: 14a$ then $7 \: | \: a$

3. If $12 \: | \: 8a$ then $12 \: | \: a$

#### Explanation

For any integers $a$ and $b,$ and any prime $p,$

$p \:|\: ab$ $\qquad\Longrightarrow\qquad$ $p \:|\: a \quad$ or $\quad p \:|\: b.$

With that in mind, let's examine each of the statements.

- Statement I is true. As $5$ is prime and $5 \: | \: 14a,$ we must have $5 \: | \: 14$ or $5 \: | \: a.$ Since $14$ is not divisible by $5,$ we obtain that $a$ must be divisible by $5.$

- Statement II is false. As a counterexample, let ${\color{blue}{a}}={\color{blue}{1}}.$ Then, $7\mid 14\cdot {\color{blue}{1}}$ but $7\not\mid {\color{blue}{1}}.$

- Statement III is false. As a counterexample, let ${\color{blue}{a}}={\color{blue}{3}}.$ Then, $12\mid 8\cdot {\color{blue}{3}}$ but $12\not\mid {\color{blue}{3}}.$

Therefore, the correct answer is "I only."

### Example: Identifying True Statements Combining Divisibility Properties

#### Question

Given that $p$ and $q$ are primes, $\text{gcd}(r,p)=1$ and $p^3 \: | \: rq^7.$ Which of the following equalities holds?

1. $p=r$

2. $p=q$

3. $r=q$

#### Explanation

Recall that for any integers $a,$ $b,$ and $c,$

$c \:|\: ab \quad$ and $\quad \text{gcd}(a,c)=1$ $\qquad\Longrightarrow\qquad$ $\quad c \:|\: b.$

Also, given that $p$ and $q$ are primes, we get

$p^m \:|\: q^n$ $\qquad\Longrightarrow\qquad$ $p = q,$

where $m$ and $n$ are positive integers.

With that in mind, we proceed as follows:

- Since $\text{gcd}(r,p)=1$ implies $\text{gcd}(r,p^3)=1,$ and $p^3 \: | \: rq^7,$ we must obtain that

- Since $p$ and $q$ are primes and $p^3 \: | \: q^7,$ we get

Therefore, the correct answer is "II only."
