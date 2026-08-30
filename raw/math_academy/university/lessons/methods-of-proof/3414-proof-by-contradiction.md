# Proof by Contradiction

Source: https://www.mathacademy.com/topics/3414?courseId=76
Topic ID: 3414

## Prerequisites

- [Tautologies and Contradictions](./249-tautologies-and-contradictions.md)
- [Direct Proof](./2801-direct-proof.md)
- [Negating Statements With Nested Quantifiers](./4258-negating-statements-with-nested-quantifiers.md)

## Lesson

### Introduction

One type of **indirect proof** is the so-called **proof by contradiction.**

The method of proof by contradiction is based on the fact that a statement $P$ is logically equivalent to the implication

$$


\lnot P \Rightarrow \mathbf{c},


$$

where $\mathbf{c}$ is a contradiction.

To see why this is equivalent to $P,$ note that since $A\Rightarrow B\equiv \lnot A\lor B,$ we have

$$


\begin{aligned}¬𝑃⇒𝐜 & ≡¬(¬𝑃)∨𝐜 \\ & ≡𝑃∨𝐜 \\ & ≡𝑃.\end{aligned}


$$

So, instead of directly proving a statement $P,$ we can assume that $\lnot P$ is true and show that this leads to a contradiction.

The outline of a typical proof by contradiction is as follows:

**Statement.** *$P$*

*Proof.*

We'll prove that $\lnot P$ leads to a contradiction.

**Assumption:** *Suppose $\lnot P.$*

*Explanation of what $\lnot P$ means using axioms, definitions, or other results.*

*Algebraic techniques, logic, and further definitions or axioms are used to demonstrate a contradiction through a series of inferences.*

**Conclusion:** *So, we got a contradiction, which means our assumption $\lnot P$ is false. Therefore, $P$ is true.*

In many cases, proving that the negation of a statement leads to a contradiction is easier than proving the original statement. In this lesson, we'll learn how to prove various statements using the contradiction.

### Proving a Statement by Contradiction

Let's prove the following proposition by contradiction:

$10x+4y \neq 1$ for all $x,y \in \mathbb{Z}.$

First, let's write down the formal statement $P$ that we wish to prove:

$$


\phantom{\lnot}P: \quad \forall x, y\in\mathbb Z,\, 10x+4y \neq 1


$$

To prove that $P$ is true, we assume that $\lnot P$ is true and show this leads to a contradiction.

$$


\lnot P: \quad \exists x, y\in\mathbb Z,\, 10x+4y = 1


$$

We begin our proof as follows:

*Assume, for a contradiction, that there exists $x,y \in \mathbb{Z}$ such that $10x+4y = 1.$*

The idea is to divide both sides by a specific number and show that the left-hand side is an integer while the right-hand side is not.

Since $10$ and $4$ have a common factor of $2,$ we can divide the left-hand side by this factor without introducing fractional coefficients.

*Dividing both sides by $2$ gives*

$$


\begin{aligned}10𝑥+4𝑦 & =1 \\ \frac{10𝑥+4𝑦}{2} & =\frac{1}{2} \\ \frac{10𝑥}{2}+\frac{4𝑦}{2} & =\frac{1}{2} \\ 5𝑥+2𝑦 & =\frac{1}{2}.\end{aligned}


$$

Finally, we show that we've reached a contradiction.

*Since $x$ and $y$ are integers, we have that $5x+2y$ is an integer.*

*But this is a contradiction since $\dfrac12$ is not an integer.*

Since we have a contradiction, our assumption that $\lnot P$ is true is incorrect. Hence, $P$ is true, and we write our conclusion as follows:

*Therefore, $10x+4y \neq 1$ for any $x,y \in \mathbb{Z}.$*

Now that we've figured out the details, let's state the full proof.

### Stating the Full Proof

Proposition:

$10x+4y \neq 1$ for all $x,y \in \mathbb{Z}.$

Proof:

*Assume, for a contradiction, that there exists $x,y \in \mathbb{Z}$ such that $10x+4y = 1.$*

*Dividing both sides by $2$ gives*

$$


\begin{aligned}10𝑥+4𝑦 & =1 \\ \frac{10𝑥+4𝑦}{2} & =\frac{1}{2} \\ \frac{10𝑥}{2}+\frac{4𝑦}{2} & =\frac{1}{2} \\ 5𝑥+2𝑦 & =\frac{1}{2}.\end{aligned}


$$

*Since $x$ and $y$ are integers, we have that $5x+2y$ is an integer.*

*But this is a contradiction since $\dfrac12$ is not an integer.*

*Therefore, $10x+4y \neq 1$ for any $x,y \in \mathbb{Z}.$*

### Example: Proving Statements About Combinations of Integers

#### Question

Prove by contradiction that $6x-9y \neq 2$ for any $x,y \in \mathbb{Z}.$

#### Explanation

Let's write down the formal statement $P$ that we wish to prove:

$$


P: \quad \forall x, y\in\mathbb Z,\, 6x-9y \neq 2


$$

To prove that $P$ is true, we assume that $\lnot P$ is true and show this leads to a contradiction.

$$


\lnot P: \quad \exists x, y\in\mathbb Z,\, 6x-9y = 2


$$

We begin our proof as follows:

Assume, for a contradiction, that there exists $x,y \in \mathbb{Z}$ such that $6x-9y = 2.$

The idea is to divide both sides by a specific number and show that the left-hand side is an integer while the right-hand side is not.

Since $6$ and $9$ have a common factor of $3,$ we can divide the left-hand side by this factor without introducing fractional coefficients.

Dividing both sides by $3$ gives

$$


\begin{aligned}6𝑥−9𝑦 & =2 \\ \frac{6𝑥−9𝑦}{3} & =\frac{2}{3} \\ \frac{6𝑥}{3}−\frac{9𝑦}{3} & =\frac{2}{3} \\ 2𝑥−3𝑦 & =\frac{2}{3}.\end{aligned}


$$

Finally, we show that we've reached a contradiction.

Since $x$ and $y$ are integers, we have that $2x - 3y$ is an integer.

But this is a contradiction since $\dfrac23$ is not an integer.

Since we have a contradiction, our assumption that $\lnot P$ is true is incorrect. Hence, $P$ is true, and we write our conclusion as follows:

Therefore, $6x-9y \neq 2$ for any $x,y \in \mathbb{Z}.$

### Proof Using Divisibility Arguments

Contradictions come in many different forms, and, in general, *any* contradiction we find when attempting a proof by contradiction will suffice!

Earlier, we considered the following true statement.

$$


\phantom{\lnot}P: \quad \forall x, y\in\mathbb Z,\, 10x+4y \neq 1


$$

To construct a proof by contradiction, we must first assume that $\lnot P$ is true:

$$


\lnot P: \quad \exists x, y\in\mathbb Z,\, 10x+4y = 1


$$

Another way of forming a contradiction in this case is to compare the divisibility of both sides by a particular number.

For example, for the statement

$$


10x+4y = 1


$$

the left-hand side is divisible by $2,$ while the right-hand side is not. Thus, we have a contradiction, which proves $P$ is true.

Let's see a concrete example of constructing this kind of argument.

### Example: Proving Statements About Combinations of Integers Using Divisibility

#### Question

Prove by contradiction that $45x+27y \neq 1$ for any $x,y \in \mathbb{Z}.$

#### Explanation

Let's write down the formal statement $P$ that we wish to prove:

$$


P: \quad \forall x, y\in\mathbb Z,\, 45x+27y \neq 1


$$

To prove that $P$ is true, we assume that $\lnot P$ is true and show this leads to a contradiction.

$$


\lnot P: \quad \exists x, y\in\mathbb Z,\,45x+27y = 1


$$

We begin our proof as follows:

Assume, for a contradiction, that there exists $x,y \in \mathbb{Z}$ such that $45x+27y = 1.$

The idea is to factor the expression on the left-hand side and consider the product as factors of the integer on the right-hand side.

Factoring the expression on the left-hand side gives

$$


\begin{aligned}45𝑥+27𝑦 & =1 \\ 9\underset{𝑎}{\underset{}{(5𝑥+3𝑦)}} & =1.\end{aligned}


$$

Now, if we define another integer $a=5x+3y$ (highlighted above), we have $9a=1,$ which, by the definition of divisibility, means $9 \:\mid\: 1.$

Let $a =5x+3y.$ Since $x$ and $y$ are integers, we have that $a$ is an integer.

Hence, we have

$$


\begin{aligned}9\underset{𝑎}{\underset{}{(5𝑥+3𝑦)}} & =1 \\ 9𝑎 & =1,\end{aligned}


$$

which means $9 \:\mid\: 1.$ But this is a contradiction since $9 \:\nmid\: 1.$

Since we have a contradiction, our assumption that $\lnot P$ is true is incorrect. Hence, $P$ is true, and we write our conclusion as follows:

Therefore, $45x+27y \neq 1$ for any $x,y \in \mathbb{Z}.$

### Proving Implications Using a Contradiction

Suppose we wish to prove that the following conditional statement is true by contradiction:

$$


P \Rightarrow Q


$$

If this statement is true, then its negation is false. We can negate our conditional statement as follows:

$$


\begin{aligned}¬(𝑃⇒𝑄) & =¬(¬𝑃∨𝑄) \\ & =¬(¬𝑃)∧¬𝑄 \\ & =𝑃∧¬𝑄\end{aligned}


$$

Note that we made use of the equivalences $A\Rightarrow B \equiv \lnot A \lor B$ and $\lnot (A\lor B)\equiv \lnot A\land \lnot B.$

Therefore, to prove an implication is true by contradiction, we assume that $P$ is true and $Q$ is *false* and show this leads to a contradiction.

Let's see some examples.

### Example: Template: Proving Parity Statements

#### Question

Suppose we wish to construct a proof by contradiction of the following statement:

$3n+1$ is even implies that $n$ is odd

What are the missing entries in the proof template below?

Assume for a contradiction that $3n+1$ is $\boxed{\phantom{even}}$ and $n$ is $\boxed{\phantom{even}}$.

Then $n=$ $\boxed{\phantom{2a+1}}$ for some integer $a.$

Substituting $n=$ $\boxed{\phantom{even}}$ into the expression $3n+1$ implies that $3n+1$ is odd. But this is a $\boxed{\phantom{contradiction}}$ since $3n+1$ is $\boxed{\phantom{even}}$ by assumption.

Therefore, we conclude that if $3n+1$ is even, then $n$ is $\boxed{\phantom{even}}$.

#### Explanation

Let's write down the formal statement that we wish to prove:

$$


\underbrace{3n+1\text{ is even}}_{P}\quad\Rightarrow\quad \underbrace{n\text{ is odd}}_{Q}


$$

To prove that $P\Rightarrow Q$ is true, we assume $P$ and $\lnot Q$ are both true and show that this leads to a contradiction.

We start by assuming that $3n+1$ is even and $n$ is even.

Assume for a contradiction that $3n+1$ is $\boxed{\color{blue}\text{even}}$ and $n$ is $\boxed{\color{blue}\text{even}}.$

Then, $n=\boxed{\color{blue}2a}$ for some integer $a.$

The idea is to substitute $n=2a$ into the expression $3n+1$ and show that this implies $3n+1$ is odd.

Substituting $n=\boxed{\color{blue}2a}$ into the expression $3n+1$ implies that $3n+1$ is odd.

This gives our contradiction.

But this is a $\boxed{\color{blue}\text{contradiction}}$ since $3n+1$ is $\boxed{\color{blue}\text{even}}$ by assumption.

Therefore, the assumption that $\lnot Q$ is true was incorrect, which means that $Q$ is true.

Therefore, we conclude that if $3n+1$ is even, then $n$ is is $\boxed{\color{blue}\text{odd}}.$

### Example: Proving Parity Statements

#### Question

Let $n$ be an integer. Prove by contradiction that if $n^4-1$ is even, then $n$ is odd.

#### Explanation

Let's write down the formal statement that we wish to prove:

$$


\underbrace{n^4-1\text{ is even}}_{P}\quad\Rightarrow\quad \underbrace{n\text{ is odd}}_{Q}


$$

To prove that $P\Rightarrow Q$ is true, we assume $P$ and $\lnot Q$ are both true and show that this leads to a contradiction.

We begin our proof as follows:

Assume, for a contradiction, that $n^4-1$ is even and $n$ is even. Then $n = 2a$ for some integer $a.$

The idea is to substitute $n=2a$ into the expression $n^4-1$ and obtain a contradiction.

As a result,

$$


\begin{aligned}𝑛^{4}−1 & =(2𝑎)^{4}−1 \\ & =16𝑎^{4}−1 \\ & =(16𝑎^{4}−2)+1 \\ & =2\underset{𝑏}{\underset{}{(8𝑎^{4}−1)}}+1.\end{aligned}


$$

If we define another integer $b=8a^4-1$ (highlighted above), we have that $n^4-1 = 2b+1,$ which shows that $n^4-1$ is one more than a multiple of $2.$ But since $n^4-1$ is even, we've reached a contradiction.

Let $b=8a^4-1.$ Since $a$ is an integer, we have that $b$ is an integer.

So, we have

$$


\begin{aligned}𝑛^{4}−1 & =2\underset{𝑏}{\underset{}{(8𝑎^{4}−1)}}+1 \\ & =2𝑏+1,\end{aligned}


$$

which is one larger than a multiple of $2.$ But this is a contradiction since $n^4-1$ is even.

Since we have a contradiction, our assumption that $\lnot Q$ is true is incorrect. Hence, $Q$ is true, and we write our conclusion as follows:

Therefore, $n$ is odd.
