# Multiplicative Inverses Modulo N

Source: https://www.mathacademy.com/topics/4818?courseId=76
Topic ID: 4818

## Prerequisites

- [The Multiplication Properties of Modular Arithmetic](./2674-the-multiplication-properties-of-modular-arithmetic.md)
- [The Extended Euclidean Algorithm](./2677-the-extended-euclidean-algorithm.md)
- [Additive Inverses Modulo N](./2735-additive-inverses-modulo-n.md)

## Lesson

### Introduction

The multiplicative inverse of an integer $a$ modulo $n$ is the unique number $x$ such that

$$


a \cdot x \equiv 1 \quad (\text{mod}\:n).


$$

The word "unique" in the statement above means with respect to the inequality $0 \leq x < n.$

For example, $x={\color{red}{4}}$ is the multiplicative inverse of $a={\color{blue}{6}}$ modulo $23$ since

$$


\begin{aligned}6⋅4 & ≡24 & \,(mod\,23) & \\ & ≡23+1 & \,(mod\,23) & \\ & ≡0+1 & \,(mod\,23) & \\ & ≡1 & \,(mod\,23) & .\end{aligned}


$$

Note the following:

- We sometimes denote the multiplicative inverse of $a$ as $a^{-1}.$ So, ${\color{blue}{6}}^{-1} = {\color{red}{4}}$ in this example.

- Be careful not confuse the notation $a^{-1}$ with the reciprocal of $a.$ In this context, both $a$ and $a^{-1}$ are *integers.*

- The uniqueness of $a^{-1}$ is up to congruence modulo $n.$ For example, since ${\color{red}{27}}\equiv {\color{red}{4}}\:(\text{mod}23),$ we have

There are circumstances when a multiplicative inverse does not exist. To this end, we have the following theorem:

*An integer $a$ has a multiplicative inverse modulo $n$ if and only if $a$ and $n$ are coprime, i.e., $\text{gcd}(a,n)=1.$*

For example:

- We saw earlier that $6^{-1} = 4$ modulo $23.$ Indeed, $\text{gcd}(6,23) = 1.$ Moreover, since $n=23$ is prime, *every* integer $1 \leq x \leq 22$ modulo $23$ has a multiplicative inverse. More on that in future lessons.

- In contrast, the integer $a=2$ has no multiplicative inverse modulo $14$ since $\text{gcd}(2,14) = 2\neq 1.$ Intuitively, multiplying $a = 2$ by any integer $x$ modulo $14$ gives an even number, and taking the result modulo $14$ (also even) will never give us $1$ (an odd integer).

### Example: Determining the Existence of a Multiplicative Inverse

#### Question

Which of the following integers has a multiplicative inverse modulo $25?$

1. $7$

2. $10$

3. $12$

#### Explanation

An integer $a$ has a multiplicative inverse modulo $n$ if and only if $a$ and $n$ are coprime, i.e., $\text{gcd}(a,n)=1.$

With this in mind, let's examine the given options.

- $7$ has a multiplicative inverse modulo $25$ since $\text{gcd}(7,25)=1. \:\:{\color{darkgreen}\checkmark}$

- $10$ does ** have a multiplicative inverse modulo $25$ since $\text{gcd}(10,25)=5\neq1. \:\:{\color{red}\times}$

- $12$ has a multiplicative inverse modulo $25$ since $\text{gcd}(12,25)=1. \:\:{\color{darkgreen}\checkmark}$

Therefore, the correct answer is "I and III only."

### Finding a Multiplicative Inverse Using Trial and Error

Suppose we wish to calculate the multiplicative inverse of $3$ modulo $14.$ In other words, we want to find a number $x$ such that

$$


3 \cdot x \equiv 1 \quad (\text{mod}\:14).


$$

Firstly, we note that since $\text{gcd}(3,14) = 1,$ a unique multiplicative inverse exists.

Since the modulus $n=14$ is fairly small, one way to efficiently compute the inverse is to use trial and error. To do this, we compute powers of $3$ and take the residue modulo $14$ until we get a result of $1.$

$$


\begin{aligned}3^{2} & ≡3⋅3≡9 & & (mod\,14) \\ 3^{3} & ≡3⋅3^{2}≡3⋅9≡27≡1⋅14+13≡13 & & (mod\,14) \\ 3^{4} & ≡3⋅3^{3}≡3⋅13≡39≡2⋅14+11≡11 & & (mod\,14) \\ 3^{5} & ≡3⋅3^{4}≡3⋅11≡33≡2⋅14+5≡5 & & (mod\,14) \\ 3^{6} & ≡3⋅3^{5}≡3⋅5≡15≡1⋅14+1≡1 & & (mod\,14)\end{aligned}


$$

According to the last line, we have

$$


3 \cdot {\color{magenta}{5}} \equiv 1\qquad (\text{mod}\:14).


$$

Therefore, the multiplicative inverse of $3$ modulo $14$ is ${\color{magenta}{5}},$ and we can write

$$


3^{-1} = {\color{magenta}{5}}\qquad (\text{mod}\:14).


$$

**Note:** We could get the same result by substituting $x=1,2,\ldots, 13$ into

$$


3 \cdot x \equiv 1 \quad (\text{mod}\:14)


$$

until we get the correct congruence relation. However, the exponentiation method described above typically allows us to find the solution with fewer trials since the multiplicative inverse of $a$ (if exists) must appear among the powers of $a$ modulo $n.$

### Example: Computing Inverses Using Exponentiation

#### Question

Use trial and error to compute the multiplicative inverse of $8$ modulo $15.$

#### Explanation

The multiplicative inverse of $8$ modulo $15,$ denoted $8^{-1},$ is the number $x$ such that

$$


8 \cdot x \equiv 1 \quad (\text{mod}\:15).


$$

Note that since $\text{gcd}(8,15) = 1,$ an inverse element exists and is unique up to congruence modulo $15.$

Since the modulus $n=15$ is small, we can find the inverse $x$ by computing exponents of $8$ (modulo $15$) until we get a result of $1\mathbin{:}$

$$


\begin{aligned}8^{2} & ≡8⋅8≡64≡4⋅15+4≡4 & & (mod\,15) \\ 8^{3} & ≡8⋅4≡32≡2⋅15+2≡2 & & (mod\,15) \\ 8^{4} & ≡8⋅2≡16≡15+1≡1 & & (mod\,15)\end{aligned}


$$

So, $8 \cdot 2 \equiv 1 \, (\text{mod} \:15).$ Therefore, the multiplicative inverse of $8$ modulo $15$ is $\boxed{\color{blue}2}.$

### Using the Extended Euclidean Algorithm

Now, suppose we want to compute the multiplicative inverse of $23$ modulo $79.$

Since $\text{gcd}(23,79)=1,$ the inverse exists. However, the modulus $n=79$ is quite big, so finding the inverse by trial and error is inefficient. So, what do we do?

To answer this, recall that Bézout's identity states that there exist integers $u$ and $v$ such that

$$


23u + 79v = \text{gcd}(23,79).


$$

Now, since $\text{gcd}(23,79)=1,$ we have

$$


23u + 79v = 1.


$$

We can find the integers $u$ and $v$ using the extended Euclidian algorithm.

Applying the Euclidian algorithm (we'll skip over the details for now), we find that $u=-24, v = 7.$ Therefore,

$$


23 \cdot (-24) + 7 \cdot 79 = 1.


$$

To find the multiplicative inverse of $23,$ the key is to write this result modulo $79,$ as follows:

$$


\begin{aligned}23⋅(−24)+7⋅79 & ≡1 & & (mod\,79) \\ 23⋅(−24)+7⋅0 & ≡1 & & (mod\,79) \\ 23⋅(−24) & ≡1 & & (mod\,79) \\ 23⋅(0−24) & ≡1 & & (mod\,79) \\ 23⋅(79−24) & ≡1 & & (mod\,79) \\ 23⋅55 & ≡1 & & (mod\,79)\end{aligned}


$$

So, we have $23 \cdot 55 \equiv 1 \: (\text{mod}\:79).$ Therefore, $55$ is the multiplicative inverse of $23$ (modulo $79$).

Finally, we can express this result using the residue function as follows:

$$


23^{-1} \: \text{mod} \: 79 = 55


$$

### Example: Computing Inverses Using the Extended Euclidean Algorithm

#### Question

Use the extended Euclidean algorithm to compute the multiplicative inverse of $15$ modulo $86.$

#### Explanation

First of all, notice that $\text{gcd}(15,86)=1.$ So, the multiplicative inverse of $15$ modulo $86$ exists.

The multiplicative inverse of $15$ modulo $86$ is the number $x$ such that

$$


15\cdot x \equiv 1 \quad (\text{mod}\:86).


$$

To find the value of $x,$ we will use the extended Euclidean algorithm. First, we apply the forward reduction:

$$


\begin{aligned}\begin{matrix}86 & = & 15⋅5 & + & 11 \\ & ↙ & & ↙ & \\ 15 & = & 11⋅1 & + & 4 \\ & ↙ & & ↙ & \\ 11 & = & 4⋅2 & + & 3 \\ & ↙ & & ↙ & \\ 4 & = & 3⋅1 & + & 1\end{matrix}\end{aligned}


$$

Solving for the rightmost terms in the equations above, we get

$$


\begin{aligned}11 & =86−15⋅5 \\ 4 & =15−11 \\ 3 & =11−4⋅2 \\ 1 & =4−3.\end{aligned}


$$

Then, we back-substitute:

$$


\begin{aligned}1 & =4−3 \\ & =4−(11−4⋅2) \\ & =4⋅3−11 \\ & =(15−11)⋅3−11 \\ & =15⋅3−11⋅4 \\ & =15⋅3−(86−15⋅5)⋅4 \\ & =15⋅23−86⋅4 \\ & =15⋅23+86⋅(−4)\end{aligned}


$$

We can write this result modulo $86,$ as follows:

$$


\begin{aligned}15⋅23+86⋅(−4) & ≡1 & & (mod\,86) \\ 15⋅23 & ≡1 & & (mod\,86)\end{aligned}


$$

So, we have $15\cdot 23\equiv 1 \: (\text{mod}\:86),$ which means that $15^{-1} \: \text{mod} \: 86=\boxed{\color{blue}23}.$
