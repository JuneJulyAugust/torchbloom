# Proving Divisibility by Contradiction

Source: https://www.mathacademy.com/topics/3526?courseId=76
Topic ID: 3526

## Prerequisites

- [Proof by Contradiction](./3414-proof-by-contradiction.md)
- [Proving Divisibility Using Congruence](./4435-proving-divisibility-using-congruence.md)

## Lesson

### Introduction

We can use proof by contradiction to demonstrate the non-divisibility of certain expressions.

For example, let's prove that for any $n\in\mathbb Z,$

$$


6 \not\mid (3n+1).


$$

First, we write down the formal statement $P$ that we wish to prove:

$$


\phantom{\lnot}P: \quad \forall n\in \mathbb Z,\: 6 \not\mid (3n+1)


$$

To prove that $P$ is true by contradiction, we assume that $\lnot P$ is true and show this leads to a contradiction.

$$


\lnot P: \quad \exists n\in \mathbb Z,\: 6 \mid (3n+1)


$$

We begin our proof as follows:

*Assume, for a contradiction, that $6 \mid (3n+1).$ Then, $3n+1=6k,$ where $k$ is an integer.*

Since the problem relates to divisibility by $6,$ let's write the equation $3n+1=6k$ in terms of congruence modulo $6.$

*Therefore, we have the following chain of equivalences:*

$$


\begin{aligned}3𝑛+1=6𝑘\, & ⇔\,3𝑛=6𝑘−1 & & \\ \, & ⇔\,3𝑛≡6𝑘−1\, & & (mod 6) \\ \, & ⇔\,3𝑛≡0⋅𝑘−1\, & & (mod 6) \\ \, & ⇔\,3𝑛≡−1\, & & (mod 6) \\ \, & ⇔\,3𝑛≡−1+6\, & & (mod 6) \\ \, & ⇔\,3𝑛≡5\, & & (mod 6)\end{aligned}


$$

This gives us the residue of $3n$ modulo $6{:}$

*Hence, we have that $3n \text{mod} 6 = 5.$*

Now, let's calculate all possible residues of $3n$ modulo $6.$ To do that, we substitute $n=0,1,\ldots,5$ into $3n$ and compute the residues:

$$


\begin{aligned}3⋅0 mod 6 & =0 \\ 3⋅1 mod 6 & =3 \\ 3⋅2 mod 6 & =0 \\ 3⋅3 mod 6 & =3 \\ 3⋅4 mod 6 & =0 \\ 3⋅5 mod 6 & =3\end{aligned}


$$

Notice that there are only two residues possible. So, we proceed as follows:

*However, substituting $n=0,1,\ldots,5$ into the expression $3n,$ we obtain that*

$$


3n \text{ mod } 6 \in \{ 0, 3\}.


$$

*But this is a contradiction since $3n \text{mod} 6 = 5$ by assumption.*

Since we have a contradiction, our original assumption must be incorrect. Hence, we write our conclusion as follows:

*Therefore, we conclude that $6 \not\mid (3n+1).$*

Now that we've figured out the details, let's state the full proof.

### Stating the Full Proof

**Proposition**

*$6 \not\mid (3n+1)$ for any $n\in\mathbb Z$*

**Proof**

*Assume, for a contradiction, that $6 \mid (3n+1).$ Then, $3n+1=6k,$ where $k$ is an integer.*

*Therefore, we have the following chain of equivalences:*

$$


\begin{aligned}3𝑛+1=6𝑘\, & ⇔\,3𝑛=6𝑘−1 & & \\ \, & ⇔\,3𝑛≡−1\, & & (mod 6) \\ \, & ⇔\,3𝑛≡5\, & & (mod 6)\end{aligned}


$$

*Hence, we have that $3n \text{mod} 6 = 5.$*

*However, substituting $n=0,1,\ldots,5$ into the expression $3n,$ we obtain that*

$$


3n \text{ mod } 6 \in \{ 0, 3\}.


$$

*But this is a contradiction since $3n \text{mod} 6 = 5$ by assumption.*

*Therefore, we conclude that $6 \not\mid (3n+1).$*

### Example: Proving Non-Divisibility of Linear Expressions

#### Question

Prove by contradiction that $60 \not\mid (45n-19)$ for any $n\in\mathbb Z.$

You may assume without proof that $45n \text{mod} 60 \in \{0,15,30,45\}$ for all $n.$

#### Explanation

Let's write down the formal statement $P$ that we wish to prove:

$$


\phantom{\lnot}P: \quad \forall n\in \mathbb Z,\: 60 \not\mid (45n-19)


$$

To prove that $P$ is true, we assume that $\lnot P$ is true and show this leads to a contradiction.

$$


\lnot P: \quad \exists n\in \mathbb Z,\: 60\mid (45n-19)


$$

We begin our proof as follows:

Assume, for a contradiction, that $60 \mid (45n-19).$ Then, $45n-19=60k,$ where $k$ is an integer.

Since the problem relates to divisibility by $60,$ let's write the equation $45n-19=60k$ in terms of congruence modulo $60.$

Therefore, we have the following chain of equivalences:

$$


\begin{aligned}45𝑛−19=60𝑘\, & ⇔\,45𝑛=60𝑘+19 & & \\ \, & ⇔\,45𝑛≡60𝑘+19\, & & (mod 60) \\ \, & ⇔\,45𝑛≡19\, & & (mod 60)\end{aligned}


$$

This gives us the residue of $45n$ modulo $60{:}$

Hence, we have that $45n \text{mod} 60=19.$

We're given the set of all possible residues for $45n$ modulo $60.$ Let's call this set $R.$

We're given that

$$


45n \text{ mod } 60 \in R = \big\{ 0,15,30,45 \big\}.


$$

However, notice that our residue $(19)$ is not an element of $R,$ which gives us our contradiction.

Therefore, we have a contradiction since $19\notin R.$

Since we have a contradiction, our original assumption must be incorrect. Hence, we write our conclusion as follows:

Therefore, we conclude that $60 \not\mid (45n-19).$

### Example: Proving Non-Divisibility of Linear Expressions: Residues Not Given

#### Question

Prove by contradiction that $4 \not\mid (14n+1)$ for any $n\in\mathbb Z.$

#### Explanation

Let's write down the formal statement $P$ that we wish to prove:

$$


\phantom{\lnot}P: \quad \forall n\in \mathbb Z,\: 4 \not\mid (14n+1)


$$

To prove that $P$ is true, we assume that $\lnot P$ is true and show this leads to a contradiction.

$$


\lnot P: \quad \exists n\in \mathbb Z,\: 4 \mid (14n+1)


$$

We begin our proof as follows:

Assume, for a contradiction, that $4 \mid (14n+1).$ Then, $14n+1=4k,$ where $k$ is an integer.

Since the problem relates to divisibility by $4,$ let's write the equation $14n+1=4k$ in terms of congruence modulo $4.$

Therefore, we have the following chain of equivalences:

$$


\begin{aligned}14𝑛+1=4𝑘\, & ⇔\,14𝑛=4𝑘−1 & & \\ \, & ⇔\,14𝑛≡4𝑘−1\, & & (mod 4) \\ \, & ⇔\,14𝑛≡−1\, & & (mod 4) \\ \, & ⇔\,14𝑛≡−1+4\, & & (mod 4) \\ \, & ⇔\,14𝑛≡3\, & & (mod 4)\end{aligned}


$$

This gives us the residue of $14n$ modulo $4{:}$

Hence, we have that $14n \text{mod} 4 = 3.$

Now, let's calculate all possible residues of $14n$ modulo $4.$ To do that, we substitute $n=0,1,2,3$ into $14n$ and compute the residues:

$$


\begin{aligned}14⋅0 mod 4 & =0 \\ 14⋅1 mod 4 & =2 \\ 14⋅2 mod 4 & =0 \\ 14⋅3 mod 4 & =2\end{aligned}


$$

Notice that there are only two residues possible. So, we proceed as follows:

However, substituting $n=0,1,2,3$ into the expression $14n,$ we obtain that

$$


14n \text{ mod } 4 \in \{ 0,2\}.


$$

But this is a contradiction since $14n \text{mod} 4 = 3$ by assumption.

Since we have a contradiction, our original assumption must be incorrect. Hence, we write our conclusion as follows:

Therefore, we conclude that $4 \not\mid (14n+1).$

### Example: Proving Non-Divisibility of Nonlinear Expressions

#### Question

Prove by contradiction that $4 \not\mid (n^4 - 11)$ for any $n \in \mathbb Z.$

#### Explanation

Let's write down the formal statement $P$ that we wish to prove:

$$


\phantom{\lnot}P: \quad \forall n \in \mathbb Z,\: 4 \not\mid (n^4 - 11)


$$

To prove that $P$ is true, we assume that $\lnot P$ is true and show this leads to a contradiction.

$$


\lnot P: \quad \exists n\in \mathbb Z,\: 4 \mid (n^4 - 11)


$$

We begin our proof as follows:

Assume, for a contradiction, that $4 \mid (n^4 - 11).$ Then, $n^4 - 11 = 4k,$ where $k$ is an integer.

Since the problem relates to divisibility by $4,$ let's write the equation $n^4 - 11 = 4k$ in terms of congruence modulo $4.$

Therefore, we have the following chain of equivalences:

$$


\begin{aligned}𝑛^{4}−11=4𝑘\, & ⇔\,𝑛^{4}=4𝑘+11 & & \\ \, & ⇔\,𝑛^{4}≡4𝑘+11\, & & (mod 4) \\ \, & ⇔\,𝑛^{4}≡11\, & & (mod 4) \\ \, & ⇔\,𝑛^{4}≡11−4⋅2\, & & (mod 4) \\ \, & ⇔\,𝑛^{4}≡3\, & & (mod 4)\end{aligned}


$$

This gives us the residue of $n^4$ modulo $4{:}$

Hence, we have that $n^4 \text{mod} 4 = 3.$

Now, let's calculate all possible residues of $n^4$ modulo $4.$ To do that, we substitute $n=0,1,2,3$ into $n^4$ and compute the residues:

$$


\begin{aligned}0^{4} mod 4 & =0 \\ 1^{4} mod 4 & =1 \\ 2^{4} mod 4 & =0 \\ 3^{4} mod 4 & =1\end{aligned}


$$

Notice that there are only two residues possible. So, we proceed as follows:

However, substituting $n = 0,1,2,3$ into the expression $n^4,$ we obtain that

$$


n^4 \text{ mod } 4 \in R = \{ 0,1\}.


$$

But this is a contradiction since $n^4 \text{mod} 3 = 3$ by assumption.

Since we have a contradiction, our original assumption must be incorrect. Hence, we write our conclusion as follows:

Therefore, we conclude that $4 \not\mid (n^4 - 11).$
