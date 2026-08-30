# Proving Congruence by Contrapositive

Source: https://www.mathacademy.com/topics/2799?courseId=76
Topic ID: 2799

## Prerequisites

- [Proving Properties of Modular Congruence](./253-proving-properties-of-modular-congruence.md)
- [Proof by Contrapositive](./2807-proof-by-contrapositive.md)

## Lesson

### Introduction

Suppose we wish to prove the following statement:

$$


\underbrace{4a \not\equiv 4b \: (\textrm{mod} \: 9)}_{P} \quad\Rightarrow\quad \underbrace{a \not\equiv b \: (\textrm{mod} \: 9)}_{Q}


$$

How should we proceed?

Notice that this statement involves two negations $(\not\equiv).$ Also, the antecedent is a more complicated statement than the consequent. This suggests that a contrapositive proof might be fruitful.

First, recall that the contrapositive of $P \Rightarrow Q$ is $\neg Q \Rightarrow \neg P.$

So, the contrapositive form of our statement is

$$


\underbrace{\lnot \Big( a \not\equiv b \: (\textrm{mod} \: 9) \Big)}_{\lnot \, Q} \quad\Rightarrow\quad \underbrace{\lnot \Big( 4a \not\equiv 4b \: (\textrm{mod} \: 9) \Big)}_{\lnot \, P},


$$

which is equivalent to

$$


a \equiv b \: (\textrm{mod} \: 9) \quad\Rightarrow\quad 4a \equiv 4b \: (\textrm{mod} \: 9).


$$

Now, since the implication and its contrapositive are logically equivalent, instead of proving the original statement, we can prove its contrapositive form.

### Example: Templates for Proving Modular Congruence by Contrapositive

#### Question

Suppose we wish to construct a direct proof of the following statement using the contrapositive:

$7a \not\equiv 7b \: (\textrm{mod} \: 9)$ if $a \not\equiv b \: (\textrm{mod} \: 9).$

To do this, we need to prove the following equivalent proposition.

$$


\boxed{\phantom{fvvbbvvnn} } {\phantom{}} \: (\textrm{mod} \: 9) \quad\Rightarrow\quad \boxed{\phantom{vvbbvvnn} } {\phantom{}} \: (\textrm{mod} \: 9)


$$

What are the missing entries?

#### Explanation

The contrapositive of $P \Rightarrow Q$ is $\neg Q \Rightarrow \neg P.$

In this case, we have the statement

$$


\underbrace{a \not\equiv b \: (\textrm{mod} \: 9)}_{P} \quad\Rightarrow\quad \underbrace{7a \not\equiv 7b \: (\textrm{mod} \: 9)}_{Q}.


$$

The contrapositive form of this statement is

$$


\underbrace{\lnot \Big( 7a \not\equiv 7b \: (\textrm{mod} \: 9) \Big)}_{\lnot \, Q} \quad\Rightarrow\quad \underbrace{\lnot \Big( a \not\equiv b \: (\textrm{mod} \: 9) \Big)}_{\lnot \, P},


$$

which is equivalent to

$$


\boxed{\color{blue}7a \equiv 7b} \: (\textrm{mod} \: 9) \quad\Rightarrow\quad \boxed{\color{blue}a \equiv b} \: (\textrm{mod} \: 9).


$$

### Example: Proving the Addition and Subtraction Properties

#### Question

Let $a$ and $b$ be integers. Prove, using the contrapositive, that

if $a+7 \not\equiv b+7 \: (\textrm{mod} \: 10),$ then $a \not\equiv b \: (\textrm{mod} \: 10).$

#### Explanation

Sometimes, to prove $P \Rightarrow Q,$ it is easier to prove the contrapositive $\neg Q \Rightarrow \neg P$ that is equivalent to the initial implication.

In this case, we need to show that

$$


\underbrace{a+7 \not\equiv b+7 \: (\textrm{mod} \: 10)}_{P} \quad\Rightarrow\quad \underbrace{a \not\equiv b \: (\textrm{mod} \: 10)}_{Q}.


$$

The contrapositive of the statement is

$$


\underbrace{\lnot \Big( a \not\equiv b \: (\textrm{mod} \: 10) \Big)}_{\lnot \, Q} \quad\Rightarrow\quad \underbrace{\lnot \Big( a+7 \not\equiv b+7 \: (\textrm{mod} \: 10) \Big)}_{\lnot \, P},


$$

which is equivalent to

$$


a \equiv b \: (\textrm{mod} \: 10) \quad\Rightarrow\quad a+7 \equiv b+7 \: (\textrm{mod} \: 10).


$$

So, we proceed as follows:

The contrapositive of the statement is

$$


a \equiv b \: (\textrm{mod} \: 10) \quad\Rightarrow\quad a+7 \equiv b+7 \: (\textrm{mod} \: 10).


$$

We will prove this statement instead of the original one.

We start by using the definition of congruence modulo $n.$ Recall that

$$


a \equiv b \: (\textrm{mod} \: n) \quad\Leftrightarrow\quad n \mid (a-b) \quad\Leftrightarrow\quad a-b = nk


$$

for some integer $k.$ So, we can reason as follows:

Since $a \equiv b \: (\textrm{mod} \: 10),$ by the definition of modular congruence,

$$


10 \mid (a-b) \qquad\Leftrightarrow\qquad a-b = 10k


$$

for some integer $k.$

Now, we express the difference between $a+7$ and $b+7$ through the difference between $a$ and $b{:}$

Now, notice that

$$


\begin{aligned}(𝑎+7)−(𝑏+7) & =𝑎+7−𝑏−7 \\ & =𝑎−𝑏 \\ & =10𝑘.\end{aligned}


$$

Finally, we use the definition of modular congruence in reverse:

Therefore, according to the definition of modular congruence, we have

$$


a+7 \equiv b+7 \: (\textrm{mod} \: 10).


$$

By proving the contrapositive, we proved the initial statement, as required.

### Example: Proving the Multiplication and Division Properties

#### Question

Let $a$ and $b$ be integers. Prove that if $a \not\equiv b \: (\textrm{mod} \: 3),$ then $4a \not\equiv 4b \: (\textrm{mod} \: 12).$

#### Explanation

Recall that the conditional statement $P \Rightarrow Q$ and its contrapositive $\neg Q \Rightarrow \neg P$ are logically equivalent. Moreover, it's sometimes easier to prove the contrapositive.

In this case, we need to show that

$$


\underbrace{a \not\equiv b \: (\textrm{mod} \: 3)}_{P} \quad\Rightarrow\quad \underbrace{4a \not\equiv 4b \: (\textrm{mod} \: 12)}_{Q}.


$$

The contrapositive of the statement is

$$


\underbrace{\lnot \Big( 4a \not\equiv 4b \: (\textrm{mod} \: 12) \Big)}_{\lnot \, Q} \quad\Rightarrow\quad \underbrace{\lnot \Big( a \not\equiv b \: (\textrm{mod} \: 3) \Big)}_{\lnot \, P},


$$

which is equivalent to

$$


4a \equiv 4b \: (\textrm{mod} \: 12) \quad\Rightarrow\quad a \equiv b \: (\textrm{mod} \: 3).


$$

So, we proceed as follows:

The contrapositive of the given statement is

$$


4a \equiv 4b \: (\textrm{mod} \: 12) \quad\Rightarrow\quad a \equiv b \: (\textrm{mod} \: 3).


$$

We will prove this statement instead of the original one.

We start by using the definition of modular congruence. Recall that

$$


a \equiv b \: (\textrm{mod} \: n) \quad\Leftrightarrow\quad n \mid (a-b) \quad\Leftrightarrow\quad a-b = nk


$$

for some integer $k.$ So, we can reason as follows:

By the definition of modular congruence,

$$


\begin{aligned}4𝑎≡4𝑏\,(mod\,12) & \,⇔\,12∣(4𝑎−4𝑏) \\ & \,⇔\,12∣4(𝑎−𝑏)\end{aligned}


$$

Next, we use the definition of divisibility:

By the definition of divisibility in $\mathbb{Z},$ $12 \mid 4(a-b)$ means that there exists an integer $k$ such that

$$


4(a-b) = 12k.


$$

Now, we can cancel out the factor of $4{:}$

Dividing this equation by $4,$ we obtain

$$


a-b = 3k,


$$

which in turn implies

$$


3 \mid (a-b).


$$

Finally, we use the definition of modular congruence again:

Therefore, according to the definition of modular congruence, we have

$$


a \equiv b \: (\textrm{mod} \: 3).


$$

By proving the contrapositive, we proved the initial statement, as required.
