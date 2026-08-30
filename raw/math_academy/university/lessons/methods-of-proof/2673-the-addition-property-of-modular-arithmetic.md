# The Addition Property of Modular Arithmetic

Source: https://www.mathacademy.com/topics/2673?courseId=76
Topic ID: 2673

## Prerequisites

- [Modular Congruence](./2641-modular-congruence.md)

## Lesson

### Introduction

Recall that two integers $a$ and $b$ are *congruent modulo* $n$ if they have the same remainder when divided by $n.$

Moreover, $a$ and $b$ are congruent modulo $n$ if and only if $n$ divides $a-b.$

$$


a \equiv b \quad (\text{mod}\,n) \qquad \Longleftrightarrow \qquad n \mid (a-b) \qquad \Longleftrightarrow \qquad a-b = kn,


$$

where $k\in\mathbb Z.$

A convenient property of congruences is that we can add and subtract on both sides, just as with regular equations.

Consider, for instance, the following true statement:

$$


22\equiv 10 \quad (\text{mod}\,12)


$$

The **addition property** allows us to add an integer to both sides. For example, adding $2$ to both sides gives

$$


\begin{aligned}22+2 & ≡10+2\, & (mod\,12) \\ 24 & ≡12\, & (mod\,12)\end{aligned}


$$

which is also a true statement since $24$ and $12$ both have a remainder of zero when divided by $12.$

Similarly, the **subtraction property** allows us to subtract an integer from both sides. For example, subtracting $9$ from both sides of our original statement gives

$$


\begin{aligned}22−9 & ≡10−9\, & (mod\,12) \\ 13 & ≡1\, & (mod\,12)\end{aligned}


$$

which is a true statement since $13$ and $1$ both have a remainder of $1$ when divided by $12.$

In general, the addition and subtraction properties state the following:

$$


\begin{aligned}𝑎≡𝑏\,⟺\,𝑎+𝑐≡𝑏+𝑐\,(mod\,𝑛) \\ 𝑎≡𝑏\,⟺\,𝑎−𝑐≡𝑏−𝑐\,(mod\,𝑛)\end{aligned}


$$

### Example: Using the Addition and Subtraction Properties

#### Question

If $x + 8 \equiv 11\: (\text{mod}\,15),$ find an equivalent statement where $x$ is isolated.

#### Explanation

The addition property of congruences states that

$$


a\equiv b \quad \Longleftrightarrow\quad a+c\equiv b+c \qquad (\text{mod}\,n).


$$

Similarly, the subtraction property states that

$$


a\equiv b \quad \Longleftrightarrow\quad a-c\equiv b-c \qquad (\text{mod}\,n).


$$

We use the subtraction property to subtract $8$ from both sides of the given congruence, as follows:

$$


\begin{aligned}𝑥+8 & ≡11\, & (mod\,15) \\ 𝑥+8−8 & ≡11−8\, & (mod\,15) \\ 𝑥 & ≡3\, & (mod\,15)\end{aligned}


$$

### Integers Congruent to Zero

According to the definition of modular congruence, we have that

$$


a \equiv b \quad (\text{mod}\,n) \qquad \Longleftrightarrow \qquad n \mid (a-b) \qquad \Longleftrightarrow \qquad a = b+ kn,


$$

where $k \in \mathbb{Z}.$ Substituting $b=0,$ we obtain

$$


a \equiv 0 \quad (\text{mod}\,n) \qquad \Longleftrightarrow \qquad n \mid a \qquad \Longleftrightarrow \qquad a = kn


$$

This gives rise to the following important fact:

*Any integer multiple of $n$ is congruent to $0$ modulo $n.$*

For example, the numbers $10,$ $-25,$ and $75$ are all are all multiples of ${\color{blue}5},$ so they are all congruent to $0$ modulo ${\color{blue}5}\mathbin{:}$

$$


\begin{aligned}10 & =2⋅5≡0 & \,(mod\,5) \\ −25 & =(−5)⋅5≡0 & \,(mod\,5) \\ 75 & =15⋅5≡0 & \,(mod\,5)\end{aligned}


$$

### Example: Identifying Integers That Are Congruent to Zero Modulo N

#### Question

Which of the following numbers is congruent to $0$ modulo $18?$

1. $-45$

2. $42$

3. $-54$

#### Explanation

First, recall that

$$


a \equiv 0 \quad (\text{mod}\,n) \qquad \Longleftrightarrow \qquad a = kn,


$$

where $k\in\mathbb Z.$ In other words, when $a$ is divided by $n,$ there is no remainder. This means that any integer multiple of $18$ is congruent to $0$ modulo $18.$

So, since $18\,|\,(-54),$ we obtain

$$


-54 \equiv (-3) \cdot {\color{blue}18} \equiv (-3)\cdot 0\equiv 0 \quad (\text{mod}\:{\color{blue}18}).


$$

None of the other options are multiples of $18.$

Therefore, the correct answer is "III only."

### Simplifying Congruences Using Integers Congruent to Zero

Let's try to simplify the right-hand side of the following congruence:

$$


x \equiv 102 \quad (\text{mod}\,5)


$$

By "simplify," we mean that we wish to transform the number on the right-hand side to be the smallest possible positive integer. In other words, we want to write

$$


x \equiv r \quad (\text{mod}\,5)\qquad\text{for}\qquad 0 \leq r < 5.


$$

When we add $0$ to both sides of a congruence modulo $n$, we can form an equivalent congruence by writing $0$ as an integer multiple of $n.$ This works because every integer multiple of $n$ is congruent to $0\:(\text{mod}\:{\color{black}n}).$

In our case, we add zero to both sides of the congruence and then use the fact that ${\color{blue}5} \cdot (-20) \equiv 0 \: (\text{mod}\:{\color{blue}5})$ to rewrite the right-hand side, as follows:

$$


\begin{aligned}𝑥 & ≡102\, & (mod\,5) \\ 𝑥+0 & ≡102+0\, & (mod\,5) \\ 𝑥 & ≡102+5⋅(−20)\, & (mod\,5) \\ 𝑥 & ≡102−100\, & (mod\,5) \\ 𝑥 & ≡2\, & (mod\,5)\end{aligned}


$$

We conclude that $x \equiv 102\, (\text{mod}\,5)$ is equivalent to $x \equiv 2\, (\text{mod}\,5).$

Our answer is correct because $102$ and $2$ both have a remainder of $2$ when divided by $5,$ and $0 \leq 2 < 5.$

**Note:** By the division algorithm, there is exactly one value of $r$ that satisfies

$$


x \equiv r \quad (\text{mod}\,n)\qquad\text{for}\qquad 0 \leq r < n.


$$

### Example: Simplifying Congruences

#### Question

Which of the following is equivalent to $x \equiv 23\: (\text{mod}\,6)?$

1. $x \equiv 2 \quad (\text{mod}\,6)$

2. $x \equiv 3 \quad (\text{mod}\,6)$

3. $x \equiv 5 \quad (\text{mod}\,6)$

#### Explanation

When we add zero to both sides of a congruence modulo $n$, we can form an equivalent congruence by writing zero as an integer multiple of $n.$ This works because every integer multiple of $n$ is congruent to zero modulo $n.$

In our case, we add zero to both sides of the congruence and then use the fact that ${\color{blue}6} \cdot (-3) \equiv 0 \: (\text{mod}\:{\color{blue}6})$ to rewrite the right-hand side, as follows:

$$


\begin{aligned}𝑥+0 & ≡23+0\, & (mod\,6) \\ 𝑥 & ≡23+0\, & (mod\,6) \\ & ≡23+6⋅(−3)\, & (mod\,6) \\ & ≡23−18\, & (mod\,6) \\ & ≡5\, & (mod\,6)\end{aligned}


$$

Therefore, the correct answer is "III only."

### Example: Date Problems

#### Question

The opening ceremony of the first modern Olympic Games was held on April 6th, 1896. Given that January 1st, 1896, was a Wednesday, use congruences to determine the day on which the Olympic Games opened.

**

#### Explanation

We can solve this problem using modular arithmetic.

First, we note the number of complete months between January 1st, 1896, and April 6th, 1896.

- There were $2$ months with $31$ days (January and March).

- There were $0$ months with $30$ days.

- There was $1$ month with $29$ days (February) since it was a leap year.

Therefore, the number of days $d$ between January 1st and April 6th is given by

$$


d = \overbrace{31(2) + 30(0) + 29(1)}^{\text{days to April 1st}} + 5.


$$

Now, note that

$$


31 \equiv 3, \qquad 30\equiv 2, \qquad 29\equiv 1 \qquad (\text{mod}\, 7).


$$

Therefore, writing the number $d$ modulo $7,$ we get the following:

$$


\begin{aligned}𝑑 & =2(31)+0(30)+1(29)+5 & \\ & ≡2(3)+0(2)+1(1)+5\, & (mod\,7) \\ & ≡6+0+1+5\, & (mod\,7) \\ & ≡12\, & (mod\,7) \\ & ≡5\, & (mod\,7)\end{aligned}


$$

Hence, the day of the week is the same as the date $5$ days after January 1st, 1896, namely Monday.

### Proof of the Addition and Subtraction Properties

In this lesson, we've been working with the so-called addition property of modular arithmetic.

$$


a\equiv b \quad \Longleftrightarrow\quad a+c\equiv b+c \qquad (\text{mod}\,n)


$$

It's straightforward to prove the addition property by writing $a\equiv b$ in terms of divisibility:

$$


\begin{aligned}𝑎≡𝑏\,(mod\,𝑛)\, & ⟺\,𝑎−𝑏=𝑘𝑛 \\ & ⟺\,(𝑎+𝑐)−(𝑏+𝑐)=𝑘𝑛 \\ & ⟺\,(𝑎+𝑐)≡(𝑏+𝑐)\,(mod\,𝑛)\end{aligned}


$$

The subtraction property is proved similarly:

$$


\begin{aligned}𝑎≡𝑏\,(mod\,𝑛)\, & ⟺\,𝑎−𝑏=𝑘𝑛 \\ & ⟺\,(𝑎−𝑐)−(𝑏−𝑐)=𝑘𝑛 \\ & ⟺\,(𝑎−𝑐)≡(𝑏−𝑐)\,(mod\,𝑛)\end{aligned}


$$
