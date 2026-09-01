# The Multiplication Properties of Modular Arithmetic

Source: https://www.mathacademy.com/topics/2674?courseId=76
Topic ID: 2674

## Prerequisites

- [Modular Residues](./2786-modular-residues.md)

## Lesson

### Introduction

Let's consider the modular congruence

$$


a \equiv b \quad (\text{mod}\,n).


$$

One useful property of congruences is that we can *multiply* both sides by an *integer*, similar to regular equations.

For example, consider the true statement

$$


7\equiv 2 \quad (\text{mod}\,5).


$$

Multiplying both sides by (for example) $9$ gives

$$


\begin{aligned}9⋅7 & ≡9⋅2\, & (mod\,5) \\ 63 & ≡18\, & (mod\,5)\end{aligned}


$$

which is a true statement since $63$ and $18$ both have a remainder of $3$ when divided by $5.$

In general, the **scalar multiplication property** of congruences states that for $k\in\mathbb{Z},$

$$


a\equiv b \quad \Longrightarrow\quad ka \equiv kb \qquad (\text{mod}\,n).


$$

We also have

$$


a\equiv b \qquad (\text{mod}\,n) \quad \Longrightarrow\quad ka \equiv kb \qquad (\text{mod}\,kn).


$$

### Example: Using the Scalar Multiplication Property

#### Question

Which of the following is equivalent to $3x \equiv 1 \: (\text{mod}\,20)?$

1. $x \equiv 5 \quad (\text{mod}\,20)$

2. $x \equiv 7 \quad (\text{mod}\,20)$

3. $x \equiv 9 \quad (\text{mod}\,20)$

#### Explanation

The scalar multiplication properties of congruences state that for $k \in \mathbb{Z},$ we have the following:

- $a \equiv b \: (\text{mod}\,n) \quad \Longrightarrow\quad ka \equiv kb \:(\text{mod}\,n)$

- $a \equiv b \: (\text{mod}\,n) \quad \Longrightarrow\quad ka \equiv kb \:(\text{mod}\,kn)$

The modulus equals $20$ in all statements, which suggests we'll need to use the first property.

Notice that the coefficient of $x$ is $3,$ and $7\cdot 3 = 21$ is one larger than the modulus. Therefore, we can reduce the coefficient of $x$ to unity as follows:

$$


\begin{aligned}3𝑥 & ≡1\, & (mod\,20) \\ 7⋅3𝑥 & ≡7⋅1\, & (mod\,20) \\ 21𝑥 & ≡7\, & (mod\,20) \\ 𝑥+20𝑥 & ≡7\, & (mod\,20) \\ 𝑥+0𝑥 & ≡7\, & (mod\,20) \\ 𝑥 & ≡7\, & (mod\,20)\end{aligned}


$$

Therefore,

$$


3x \equiv 1 \quad \Longrightarrow \quad x \equiv 7\qquad (\text{mod}\,20)


$$

### The Multiplicative Property

Another useful property that stems from the multiplication property is as follows. Suppose that

$$


a\equiv b \quad \text{and}\quad c\equiv d \qquad (\text{mod}\,n),


$$

then, we have

$$


ac\equiv bd \qquad (\text{mod}\,n).


$$

Using this, we can compute the residue of a large product without finding the product explicitly. Let's see how.

### Example: Computing Residues of Products

#### Question

Use the multiplicative property of congruences to compute the residue of $76 \cdot 122 \text{mod} 6.$

#### Explanation

The multiplicative property of modular congruences states that if

$$


a\equiv b \quad \text{and}\quad c\equiv d \qquad (\text{mod}\,n),


$$

then, we have

$$


ac\equiv bd \qquad (\text{mod}\,n).


$$

First, we note the following:

$$


\begin{aligned}76 & ≡12⋅6+4\, & (mod\,6) \\ & ≡12⋅0+4\, & (mod\,6) \\ & ≡4\, & (mod\,6) \\ 122 & ≡20⋅6+2\, & (mod\,6) \\ & ≡20⋅0+2\, & (mod\,6) \\ & ≡2\, & (mod\,6)\end{aligned}


$$

Therefore, by the multiplicative property of congruences, we have the following:

$$


\begin{aligned}76⋅122 & ≡4⋅2\, & (mod\,6) \\ & ≡8\, & (mod\,6) \\ & ≡6+2\, & (mod\,6) \\ & ≡0+2\, & (mod\,6) \\ & ≡2\, & (mod\,6)\end{aligned}


$$

Therefore, we conclude that

$$


76 \cdot 122 \equiv 2 \qquad (\text{mod}\,6).


$$

### Example: Computing Residues of Exponents

#### Question

Use the multiplicative property of congruences to compute the residue of $5^{7} \text{mod} 8.$

#### Explanation

The multiplicative property of modular congruences states that if

$$


a\equiv b \quad \text{and}\quad c\equiv d \qquad (\text{mod}\,n),


$$

then, we have

$$


ac\equiv bd \qquad (\text{mod}\,n).


$$

First, we decompose the exponent into a product of smaller exponents. For example,

$$


5^{7} = 5^2\cdot 5^2 \cdot 5^3.


$$

Next, we note the following:

$$


\begin{aligned}5^{2} & ≡25\, & (mod\,8) \\ & ≡3⋅8+1\, & (mod\,8) \\ & ≡3⋅0+1\, & (mod\,8) \\ & ≡1\, & (mod\,8) \\ 5^{3} & ≡5⋅5^{2}\, & (mod\,8) \\ & ≡5⋅1\, & (mod\,8) \\ & ≡5\, & (mod\,8)\end{aligned}


$$

Therefore, by the multiplicative property of congruences, we have the following:

$$


\begin{aligned}5^{7} & ≡5^{2}⋅5^{2}⋅5^{3}\, & (mod\,8) \\ & ≡1⋅1⋅5\, & (mod\,8) \\ & ≡5\, & (mod\,8)\end{aligned}


$$

Therefore, we conclude that

$$


5^{7} \text{ mod } 8= 5.


$$

### The Exponentiation Property

The multiplicative property states that given $a \equiv b \: (\text{mod}\,n)$ and $c \equiv d \: (\text{mod}\,n),$ we obtain $ac \equiv bd \: (\text{mod}\,n).$ By taking the same congruence twice, we obtain

$$


a^2 \equiv b^2 \qquad (\text{mod}\,n).


$$

In general,

$$


a^k \equiv b^k \qquad (\text{mod}\,n)


$$

for any *positive* integer $k.$

### Example: Computing a Final Digit

#### Question

What is the last digit in the decimal expansion of $17^{13}?$

#### Explanation

If $a\equiv b\:(\text{mod}\,n)$ and $c\equiv d\:(\text{mod}\,n),$ then the following properties hold:

- $ac\equiv bd \: (\text{mod}\,n)$

- $a^k \equiv b^k \: (\text{mod}\,n)$ for any positive integer $k$

To find the last digit, we need to calculate the following residue:

$$


17^{13} \text{ mod } 10


$$

First, we note the following:

$$


\begin{aligned}17 & ≡10+7\, & (mod\,10) \\ & ≡0+7\, & (mod\,10) \\ & ≡7\, & (mod\,10)\end{aligned}


$$

Therefore, by the exponentiation property, we have the following:

$$


\begin{aligned}17^{2} & ≡7^{2}\, & (mod\,10) \\ & ≡49\, & (mod\,10) \\ & ≡4⋅10+9\, & (mod\,10) \\ & ≡4⋅0+9\, & (mod\,10) \\ & ≡9\, & (mod\,10) \\ 17^{4} & ≡9^{2}\, & (mod\,10) \\ & ≡81\, & (mod\,10) \\ & ≡8⋅10+1\, & (mod\,10) \\ & ≡8⋅0+1\, & (mod\,10) \\ & ≡1\, & (mod\,10)\end{aligned}


$$

Next, we decompose $17^{13}$ into a product of smaller exponents.

$$


17^{13} = \left(17^4\right)^3\cdot 17


$$

By applying the multiplicative and exponentiation properties, we have the following:

$$


\begin{aligned}17^{13} & ≡(17^{4})^{3}⋅17\, & (mod\,10) \\ & ≡(1)^{3}⋅7\, & (mod\,10) \\ & ≡1⋅7\, & (mod\,10) \\ & ≡7\, & (mod\,10)\end{aligned}


$$

Therefore, we conclude that

$$


17^{13} \text{ mod } 10 = 7


$$

which means that the last digit of $17^{13}$ is $7.$

### Proving the Scalar Multiplication Property

Throughout this lesson, we've made use of the following properties:

- $a \equiv b \: (\text{mod}\,n) \quad \Longrightarrow\quad ka \equiv kb \:(\text{mod}\,n)$

- $a \equiv b \: (\text{mod}\,n) \quad \Longrightarrow\quad ka \equiv kb \:(\text{mod}\,kn)$

Let's prove the first property. The proof of the second property is similar.

It's straightforward to prove the scalar multiplication property from the definition of congruence. First, note that we have the following chain of implications for $k, p\in\mathbb Z$:

$$


\begin{aligned}𝑎≡𝑏\,(mod\,𝑛)\, & ⟹\,𝑎−𝑏=𝑝𝑛 \\ & ⟹\,𝑘(𝑎−𝑏)=𝑘𝑝𝑛 \\ & ⟹\,𝑘𝑎−𝑘𝑏=(𝑘𝑝)𝑛\end{aligned}


$$

Now, let $kp = q\in\mathbb Z.$ Then, we have

$$


\begin{aligned}𝑘𝑎−𝑘𝑏=(𝑘𝑝)𝑛\, & ⟹\,𝑘𝑎−𝑘𝑏=𝑞𝑛 \\ & ⟹\,𝑘𝑎≡𝑘𝑏\,(mod\,𝑛).\end{aligned}


$$

Therefore, we conclude that

$$


a \equiv b \: (\text{mod}\,n) \quad \Longrightarrow\quad ka \equiv kb \:(\text{mod}\,n).


$$

Note the following:

- The proof of the second property is very similar.

- We'll prove the multiplicative and exponentiation properties in future lessons.
