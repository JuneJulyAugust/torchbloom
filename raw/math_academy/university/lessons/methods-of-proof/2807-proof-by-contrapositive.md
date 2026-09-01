# Proof by Contrapositive

Source: https://www.mathacademy.com/topics/2807?courseId=76
Topic ID: 2807

## Prerequisites

- [Direct Proof](./2801-direct-proof.md)

## Lesson

### Introduction

One type of **indirect proof** is the so-called **proof by contrapositive.** The method is based on the fact that the implication

$$


P \Rightarrow Q


$$

is logically equivalent to its contrapositive

$$


\lnot Q \Rightarrow \lnot P.


$$

So, instead of proving the statement directly, we can instead prove its contrapositive form.

The outline of a typical contrapositive proof is the following:

**Statement.** *If $P,$ then $Q.$*

*Proof.*

Since $P \Rightarrow Q \equiv \lnot Q \Rightarrow \lnot P,$ we'll prove the contrapositive $\lnot Q \Rightarrow \lnot P.$

**Assumption:** *Suppose $\lnot Q.$*

*Explanation of what $\lnot Q$ means using axioms, definitions, or other results.*

*Algebraic techniques, logic, and further definitions or axioms are used to demonstrate, through a series of inferences, that $\lnot Q$ implies $\lnot P.$*

**Conclusion:** *Therefore, $\lnot P.$* So, since $\lnot Q\Rightarrow \lnot P,$ by the contrapositive $P\Rightarrow Q.$

In many cases, proving the contrapositive form of a statement is easier than proving the original statement. In this lesson, we'll learn how to prove parity statements using the contrapositive.

### Proving Parity Statements by Contrapositive

Let's prove the following proposition using the contrapositive:

$$


\underbrace{3n+2 \text{ is odd}}_{P(n)} \quad\Rightarrow\quad \underbrace{n \text{ is odd}}_{Q(n)}


$$

To prove $P \Rightarrow Q,$ it suffices to prove the contrapositive $\neg Q \Rightarrow \neg P.$ So, let's write down the contrapositive of our statement.

*The contrapositive form of the given statement is as follows:*

$$


\underbrace{ n \text{ is even}}_{\lnot Q(n)} \quad\Rightarrow\quad \underbrace{3n+2 \text{ is even}}_{\lnot P(n)}


$$

We will prove this statement instead of the original one.

We start by using the fact that $n$ is even.

*If $n$ is even, then $n=2a$ for some integer $a.$*

The idea is to substitute $n=2a$ into the expression $3n+2$ and show it is even by writing it as a multiple of $2.$

*Therefore,*

$$


\begin{aligned}3𝑛+2 & =3(2𝑎)+2 \\ & =6𝑎+2 \\ & =2\underset{𝑏}{\underset{}{(3𝑎+1)}}.\end{aligned}


$$

Now, if we define another integer $b=3a+1$ (highlighted above), we have that $3n+2 = 2b,$ which shows that $3n+2$ is indeed a multiple of $2.$

*Let $b=3a+1.$ Since $a$ is an integer, we have that $b$ is an integer.*

*Hence, we have*

$$


\begin{aligned}3𝑛+2 & =2\underset{𝑏}{\underset{}{(3𝑎+1)}} \\ & =2𝑏,\end{aligned}


$$

*which is a multiple of $2.$*

Finally, we write our conclusion.

*Therefore, $3n+2$ is even.*

Now that we've figured out the details, let's state the full proof.

### Stating the Full Proof

Proposition:

$$


3n+2 \text{ is odd} \quad\Rightarrow\quad n \text{ is odd}


$$

Proof:

*The contrapositive form of the given statement is as follows:*

$$


n \text{ is even} \quad\Rightarrow\quad 3n+2 \text{ is even}


$$

*If $n$ is even, then $n=2a$ for some integer $a.$ Therefore,*

$$


\begin{aligned}3𝑛+2 & =6𝑎+2 \\ & =2(3𝑎+1).\end{aligned}


$$

*Let $b=3a+1.$ Since $a$ is an integer, we have that $b$ is an integer.*

*Hence, we have*

$$


\begin{aligned}3𝑛+2 & =2(3𝑎+1) \\ & =2𝑏,\end{aligned}


$$

*which is a multiple of $2.$*

*Therefore, $3n+2$ is even.*

### Example: Completing a Proof Schema

#### Question

Suppose we wish to construct a proof by contrapositive of the following statement:

Let $n$ be an integer. Then $4n^2+5n-1$ is odd only if $n$ is even.

What are the missing entries in the proof template below?

The contrapositive form of the statement is as follows:

$$


\boxed{\phantom{vvvxxxyyyzzz} } {\phantom{}} \, \quad\Rightarrow\quad \boxed{\phantom{vvvxxxyyyzzz} } {\phantom{}} \,


$$

If $n$ is $\boxed{\phantom{xxxyyy}}$, then $n=\boxed{\phantom{xxxyyy}}$, where $a$ is $\boxed{\phantom{vvvxxxyyyzzz}}.$

Substituting $\boxed{\phantom{xxxyyy}}$ into the expression $4n^2+5n-1,$ we can show that

$$


4n^2+5n-1 = \boxed{\phantom{xxxyyy} }, \text{ where } b \text{ is } \boxed{\phantom{xxxyyy} }.


$$

Therefore, since $4n^2+5n-1$ $\boxed{\phantom{xxxyyy}}$ a multiple of $2,$ we conclude that $4n^2+5n-1$ is $\boxed{\phantom{xxxyyy}}$.

#### Explanation

Recall the following:

- If an integer $n$ is even, then there exists an integer $p$ such that $n=2p.$

- If an integer $n$ is odd, then there exists an integer $q$ such that $n=2q+1.$

In this case, we need to prove the following:

$$


4n^2+5n-1 \text{ is odd} \quad\Rightarrow\quad n \text{ is even}


$$

To prove $P \Rightarrow Q,$ it suffices to prove the contrapositive $\neg Q \Rightarrow \neg P.$

The contrapositive form of the given statement is

$$


n \text{ is not even} \quad\Rightarrow\quad 4n^2+5n-1 \text{ is not odd}


$$

which is equivalent to

$$


\boxed{\color{blue}n \text{ is odd}} \quad\Rightarrow\quad \boxed{\color{blue}4n^2+5n-1 \text{ is even}}.


$$

We start by using the fact that $n$ is odd.

If $n$ is $\boxed{\color{blue}\text{odd}},$ then $n = \boxed{\color{blue}2a+1},$ where $a$ is $\boxed{\color{blue}\text{an integer}}.$

The idea is to substitute $n=2a+1$ into the expression $4n^2+5n-1$ and show it is even by writing it as a multiple of $2.$

Substituting $𝑛=2𝑎+1$ into the expression $4n^2+5n-1,$ we can show that $4n^2+5n-1 = \boxed{\color{blue}2b},$ where $b$ is $\boxed{\color{blue}\text{an integer}}.$

Once we've done this, the proof is complete, and we can state our conclusion.

Therefore, since $4n^2+5n-1$ $\boxed{\color{blue}\text{is}}$ a multiple of $2,$ we conclude that $4n^2+5n-1$ is $\boxed{\color{blue}\text{even}}.$

### Example: Proving the Parity of a Linear Expression

#### Question

Let $n$ be an integer. Using the contrapositive, prove that $n$ is odd whenever $3n-1$ is even.

#### Explanation

Recall the following:

- If an integer $n$ is even, then there exists an integer $p$ such that $n=2p.$

- If an integer $n$ is odd, then there exists an integer $q$ such that $n=2q+1.$

In this case, we need to prove the following:

$$


3n-1 \text{ is even} \quad\Rightarrow\quad n \text{ is odd}


$$

To prove $P \Rightarrow Q,$ it suffices to prove the contrapositive $\neg Q \Rightarrow \neg P.$ So, let's write down the contrapositive of our statement.

The contrapositive form of the given statement is as follows:

$$


n \text{ is even} \quad\Rightarrow\quad 3n-1 \text{ is odd}


$$

We'll prove this statement instead of the original one.

We start by using the fact that $n$ is even.

If $n$ is even, then $n=2a$ for some integer $a.$

The idea is to substitute $n=2a$ into the expression $3n-1$ and show it is odd by writing it as a multiple of $2,$ plus $1.$

Therefore,

$$


\begin{aligned}3𝑛−1 & =3(2𝑎)−1 \\ & =6𝑎−1 \\ & =(6𝑎−2)+1 \\ & =2\underset{𝑏}{\underset{}{(3𝑎−1)}}+1.\end{aligned}


$$

Now, if we define another integer $b=3a-1$ (highlighted above), we have that $3n-1 = 2b+1,$ which shows that $3n-1$ is indeed one more than a multiple of $2.$

Let $b=3a-1.$ Since $a$ is an integer, we have that $b$ is an integer.

Therefore, we have

$$


\begin{aligned}3𝑛−1 & =2\underset{𝑏}{\underset{}{(3𝑎−1)}}+1 \\ & =2𝑏+1,\end{aligned}


$$

which is one larger than a multiple of $2.$

Finally, we write our conclusion.

Therefore, $3n-1$ is odd.

### Example: Proving the Parity of a Nonlinear Expression

#### Question

Let $n$ be an integer. Prove that $n^3 + 1$ is even only if $n$ is odd.

#### Explanation

Recall the following:

- If an integer $n$ is even, then there exists an integer $a$ such that $n = 2a.$

- If an integer $n$ is odd, then there exists an integer $a$ such that $n = 2a+1.$

In this case, we need to prove the following:

$$


n^3 + 1 \text{ is even} \quad\Rightarrow\quad n \text{ is odd}


$$

To prove $P \Rightarrow Q,$ it suffices to prove the contrapositive $\neg Q \Rightarrow \neg P.$ So, let's write down the contrapositive of our statement.

The contrapositive form of the given statement is as follows:

$$


n \text{ is even} \quad\Rightarrow\quad n^3 + 1 \text{ is odd}


$$

We'll prove this statement instead of the original one.

We start by using the fact that $n$ is even.

If $n$ is even, then $n = 2a$ for some integer $a.$

The idea is to substitute $n = 2a$ into the expression $n^3 + 1$ and show it is odd by writing it as a multiple of $2,$ plus $1.$

Therefore,

$$


\begin{aligned}𝑛^{3}+1 & =(2𝑎)^{3}+1 \\ & =8𝑎^{3}+1 \\ & =2\underset{𝑏}{\underset{}{(4𝑎^{3})}}+1.\end{aligned}


$$

Now, if we define another integer $b = 4a^3$ (highlighted above), we have that $n^3+1 = 2b+1,$ which shows that $n^3+1$ is indeed one more than a multiple of $2.$

Let $b = 4a^3.$ Since $a$ is an integer, we have that $b$ is an integer.

Therefore, we have

$$


\begin{aligned}𝑛^{3}+1 & =2\underset{𝑏}{\underset{}{(4𝑎^{3})}}+1 \\ & =2𝑏+1,\end{aligned}


$$

which is one larger than a multiple of $2.$

Finally, we write our conclusion.

Therefore, $n^3+1$ is odd.
