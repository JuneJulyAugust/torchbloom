# Proving Parity by Contrapositive

Source: https://www.mathacademy.com/topics/4437?courseId=76
Topic ID: 4437

## Prerequisites

- [Proof by Contrapositive](./2807-proof-by-contrapositive.md)
- [Simplifying Predicate Expressions Using De Morgan's Laws](./4302-simplifying-predicate-expressions-using-de-morgan-s-laws.md)
- [Proof by Cases](./4432-proof-by-cases.md)

## Lesson

### Introduction

Let's prove the following proposition.

$$


\underbrace{mn \text{ is even}}_{P(m,n)} \quad\Rightarrow\quad \underbrace{m \text{ is even or } n \text{ is even}}_{Q(m,n)}


$$

To prove $P \Rightarrow Q,$ it suffices to prove the contrapositive $\neg Q \Rightarrow \neg P.$

$$


\neg\left(m \text{ is even or } n \text{ is even}\right) \quad\Rightarrow\quad \neg\left(mn \text{ is even}\right)


$$

Negating the right-hand-side of our implication is straightforward:

$$


\neg\left(m \text{ is even or } n \text{ is even}\right) \quad\Rightarrow\quad mn \text{ is odd}


$$

To negate the statement "$m$ is even or $n$ is even," we use De Morgan's law for disjunctions.

$$


\begin{aligned}¬(𝑚 is even or 𝑛 is even)\, & ⇔\,¬(𝑚 is even∨𝑛 is even) \\ \, & ⇔\,¬(𝑚 is even)∧¬(𝑛 is even) \\ \, & ⇔\,𝑚 is odd∧𝑛 is odd \\ \, & ⇔\,𝑚 is odd and 𝑛 is odd\end{aligned}


$$

So, let's write down the contrapositive of our original statement.

*The contrapositive form of the given statement is as follows:*

$$


m \text{ is odd and } n \text{ is odd} \quad\Rightarrow\quad mn \text{ is odd}


$$

We start by using the fact that $m$ and $n$ are odd.

*If $m$ and $n$ are odd, then*

$$


m = 2a+1 \quad\text{and}\quad n = 2b+1,


$$

*where $a$ and $b$ are integers.*

We substitute $m=2a+1$ and $n=2b+1$ into the expression $mn$ and show it is odd by writing it as one larger than a multiple of $2.$

*Therefore,*

$$


\begin{aligned}𝑚𝑛 & =(2𝑎+1)(2𝑏+1) \\ & =4𝑎𝑏+2𝑎+2𝑏+1 \\ & =2\underset{𝑐}{\underset{}{(2𝑎𝑏+𝑎+𝑏)}}+1.\end{aligned}


$$

Now, if we define another integer $c=2ab+a+b$ (highlighted above), we have that $mn = 2c+1,$ which shows that $mn$ is indeed one larger than a multiple of $2.$

*Let $c=2ab+a+b.$ Since $a$ and $b$ are integers, we have that $c$ is an integer.*

*Hence, we have*

$$


\begin{aligned}𝑚𝑛 & =2\underset{𝑐}{\underset{}{(2𝑎𝑏+𝑎+𝑏)}}+1 \\ & =2𝑐+1,\end{aligned}


$$

*which is one larger than a multiple of $2.$*

Finally, we write our conclusion.

*Therefore, $mn$ is odd.*

For clarity, let's restate the proposition and its full proof.

### Stating the Full Proof

Proposition:

$$


mn \text{ is even} \quad\Rightarrow\quad m \text{ is even or } n \text{ is even}


$$

Proof:

*The contrapositive form of the given statement is as follows:*

$$


m \text{ is odd and } n \text{ is odd} \quad\Rightarrow\quad mn \text{ is odd}


$$

*If $m$ and $n$ are odd, then*

$$


m = 2a+1 \quad\text{and}\quad n = 2b+1,


$$

*where $a$ and $b$ are integers.*

*Therefore,*

$$


\begin{aligned}𝑚𝑛 & =(2𝑎+1)(2𝑏+1) \\ & =4𝑎𝑏+2𝑎+2𝑏+1 \\ & =2(2𝑎𝑏+𝑎+𝑏)+1.\end{aligned}


$$

*Let $c=2ab+a+b.$ Since $a$ and $b$ are integers, we have that $c$ is an integer.*

*Hence, we have*

$$


\begin{aligned}𝑚𝑛 & =2(2𝑎𝑏+𝑎+𝑏)+1 \\ & =2𝑐+1,\end{aligned}


$$

*which is one larger than a multiple of $2.$*

*Therefore, $mn$ is odd.*

### Example: Template: Proving Parity Statements

#### Question

Suppose we wish to construct a proof by contrapositive of the following statement:

Let $m$ and $n$ be integers. If $m +3n$ is odd, then $m$ is even or $n$ is even.

A proof schema is outlined below. Fill in the missing entries.

The contrapositive form of the given statement is as follows:

$$


m \, \, \boxed{\phantom{even } } {\phantom{}} \, \, \, \text{and} \, \, \, n \, \, \boxed{\phantom{even} } {\phantom{}} \, \quad\Rightarrow\quad m + 3n \, \, \boxed{\phantom{for any} } {\phantom{}} \,


$$

If $m$ and $n$ are $\boxed{\phantom{even}}$, then

$$


m = \boxed{\phantom{even } } \quad\text{and}\quad n = \boxed{\phantom{even } },


$$

where $a$ and $b$ are $\boxed{\phantom{integers}}.$

Substituting $m = \boxed{\phantom{even}} \, \, \, \text{and}\, \, \, n = \boxed{\phantom{even}}$ into the expression $m +3n,$ we can show that

$$


m +3n= \boxed{\phantom{even } },


$$

where $c$ is $\boxed{\phantom{even}}$

Therefore, since $m +3n$ $\boxed{\phantom{is one more}}$ a multiple of $2,$ we conclude that $m +3n$ is $\boxed{\phantom{even}}$.

#### Explanation

Recall the following:

- If an integer $n$ is even, then there exists an integer $p$ such that $n=2p.$

- If an integer $n$ is odd, then there exists an integer $q$ such that $n=2q+1.$

In this case, we need to prove the following:

$$


m +3n \text{ is odd} \quad\Rightarrow\quad m \text{ is even or } n \text{ is even}


$$

To prove $P \Rightarrow Q,$ it suffices to directly prove the contrapositive $\neg Q \Rightarrow \neg P.$

$$


\neg \left(m \text{ is even or } n \text{ is even}\right) \quad\Rightarrow\quad \neg \left(m +3n \text{ is odd}\right)


$$

Negating the right-hand-side of our implication is straightforward:

$$


\neg \left(m \text{ is even or } n \text{ is even}\right) \quad\Rightarrow\quad m +3n \text{ is even}


$$

To negate the statement "$m$ is even or $n$ is even", we use De Morgan's law for disjunctions.

$$


\begin{aligned}¬(𝑚 is even or 𝑛 is even)\, & ⇔\,¬(𝑚 is even∨𝑛 is even) \\ \, & ⇔\,¬(𝑚 is even)∧¬(𝑛 is even) \\ \, & ⇔\,𝑚 is odd∧𝑛 is odd \\ \, & ⇔\,𝑚 is odd and 𝑛 is odd\end{aligned}


$$

Therefore, we have the following statement:

The contrapositive form of the given statement is as follows:

$$


\color{blue} m\,\, \boxed{\text{is odd}} \text{ and } n\,\, \boxed{\text{is odd}} \quad\Rightarrow\quad m +3n\,\, \boxed{\color{blue}{\text{is even}}}.


$$

We start by assuming $m$ and $n$ are odd.

If $m$ and $n$ are $\boxed{\color{blue}\text{odd}},$ then

$$


m = \boxed{\color{blue}2a+1} \quad\text{and}\quad n = \boxed{\color{blue}2b+1}


$$

where $a$ and $b$ are $\boxed{\color{blue}\text{integers}}.$

The idea is to substitute $m=2a+1$ and $n=2b+1$ into the expression $m +3n$ and show it is even by writing it as a multiple of $2.$

Substituting $m=$ $\boxed{\color{blue}2a+1}$ and $n=$ $\boxed{\color{blue}2b+1}$ into the expression $m +3n,$ we can show that

$$


m +3n = \boxed{\color{blue}2c},


$$

where $c$ is $\boxed{\color{blue}\text{an integer}}.$

Once we've done this, the proof is complete, and we can state our conclusion.

Therefore, since $m +3n$ $\boxed{\color{blue}\text{is}}$ a multiple of $2,$ we conclude that $m +3n$ is $\boxed{\color{blue}\text{even}}.$

### Example: Proving Parity Statements

#### Question

Let $m$ and $n$ be integers. Prove that if $mn$ is odd, then $m$ is odd or $n$ is odd.

#### Explanation

Recall the following:

- If an integer $n$ is even, then there exists an integer $p$ such that $n=2p.$

- If an integer $n$ is odd, then there exists an integer $q$ such that $n=2q+1.$

In this case, we need to prove the following:

$$


mn \text{ is odd} \quad\Rightarrow\quad m \text{ is odd or } n \text{ is odd}


$$

To prove $P \Rightarrow Q,$ it suffices to prove the contrapositive $\neg Q \Rightarrow \neg P.$

$$


\neg\left(m \text{ is odd or } n \text{ is odd}\right) \quad\Rightarrow\quad \neg\left(mn \text{ is odd}\right)


$$

Negating the right-hand-side of our implication is straightforward:

$$


\neg\left(m \text{ is odd or } n \text{ is odd}\right) \quad\Rightarrow\quad mn\text{ is even}


$$

To negate the statement "$m$ is odd or $n$ is odd", we use De Morgan's law for disjunctions.

$$


\begin{aligned}¬(𝑚 is odd or 𝑛 is odd)\, & ⇔\,¬(𝑚 is odd∨𝑛 is odd) \\ \, & ⇔\,¬(𝑚 is odd)∧¬(𝑛 is odd) \\ \, & ⇔\,𝑚 is even∧𝑛 is even \\ \, & ⇔\,𝑚 is even and 𝑛 is even\end{aligned}


$$

So, let's write down the contrapositive of our original statement.

The contrapositive form of the given statement is as follows:

$$


m \text{ is even and } n \text{ is even} \quad\Rightarrow\quad mn \text{ is even}


$$

We'll prove this statement instead of the original one.

We start by using the fact that $m$ and $n$ are even.

If $m$ and $n$ are even, then

$$


m = 2a \quad\text{and}\quad n = 2b,


$$

where $a$ and $b$ are integers.

We substitute $m=2a$ and $n=2b$ into the expression $mn$ and show it is even by writing it as a multiple of $2.$

Therefore,

$$


\begin{aligned}𝑚𝑛 & =(2𝑎)(2𝑏) \\ & =4𝑎𝑏 \\ & =2\underset{𝑐}{\underset{}{(2𝑎𝑏)}}.\end{aligned}


$$

Now, if we define another integer $c=2ab$ (highlighted above), we have that $mn= 2c,$ which shows that $mn$ is indeed a multiple of $2.$

Let $c=2ab.$ Since $a$ and $b$ are integers, we have that $c$ is an integer.

Therefore, we have

$$


\begin{aligned}𝑚𝑛 & =2\underset{𝑐}{\underset{}{(2𝑎𝑏)}} \\ & =2𝑐,\end{aligned}


$$

which is a multiple of $2.$

Finally, we write our conclusion.

Therefore, $mn$ is even.

### Example: Template: Proving Parity Statements by Cases

#### Question

Construct a proof schema to prove the following statement:

Let $m$ and $n$ be integers. Then, $m+3n$ is even only if $m$ and $n$ have the same parity.

#### Explanation

Recall the following:

- If an integer $n$ is even, then there exists an integer $p$ such that $n=2p.$

- If an integer $n$ is odd, then there exists an integer $q$ such that $n=2q+1.$

In this case, we need to prove the following:

$$


m+3n \text{ is even} \quad\Rightarrow\quad m \text{ and } n \text{ have the same parity}


$$

To prove $P \Rightarrow Q,$ it suffices to directly prove the contrapositive $\neg Q \Rightarrow \neg P.$

The contrapositive form of the given statement is as follows:

$$


\boxed{\color{blue} m \text{ and } n \text{ have opposite parity}} \quad\Rightarrow\quad \boxed{\color{blue} m+3n \text{ is odd}}.


$$

Now, we have two cases: $m$ is even and $n$ is odd, or $m$ is odd and $n$ is even.

- First, we consider the case when $m$ is even.

****. If $m$ is even, then $n$ is $\boxed{\color{blue}\text{odd}}$ and we have

$$


m = {\boxed{\color{blue}2a}} \quad\text{and}\quad n = {\boxed{\color{blue}2b+1}},


$$

where $𝑎$

Substituting $𝑚=2𝑎$ and $𝑛=2𝑏+1$ into the expression $m+3n,$ we can show that $m+3n = \boxed{\color{blue}2c+1},$ where $c$ is $\boxed{\color{blue}\text{an integer}}.$

Hence, since $m+3n$ $\boxed{\color{blue}\text{is one larger than}}$ a multiple of $2,$ we conclude that $m+3n$ is $\boxed{\color{blue}\text{odd}}.$

- Now, we consider the case when $m$ is odd.

****. If $m$ is odd, then $n$ is $\boxed{\color{blue}\text{even}}$ and we have

$$


m = {\boxed{\color{blue}2a+1}} \quad\text{and}\quad n = {\boxed{\color{blue}2b}},


$$

where $𝑎$

Substituting $𝑚=2𝑎+1$ and $𝑛=2𝑏$ into the expression $m+3n,$ we can show that $m+3n = \boxed{\color{blue}2c+1},$ where $c$ is $\boxed{\color{blue}\text{an integer}}.$

Hence, since $m+n$ $\boxed{\color{blue}\text{is one larger than}}$ a multiple of $2,$ we conclude that $m+3n$ is $\boxed{\color{blue}\text{odd}}.$

Once we've done this, the proof is complete, and we can state our conclusion.

Finally, combining the cases above, we conclude that $m+3n$ is $\boxed{\color{blue}\text{even}}$ only if $m$ and $n$ have $\boxed{\color{blue}\text{the same}}$ parity.

### Example: Proving Parity Statements by Cases

#### Question

Let $m$ and $n$ be integers. Prove that $(m-1)n^2$ is odd only if $m$ is even and $n$ is odd.

#### Explanation

Recall the following:

- If an integer $n$ is even, then there exists an integer $p$ such that $n=2p.$

- If an integer $n$ is odd, then there exists an integer $q$ such that $n=2q+1.$

In this case, we need to prove the following:

$$


(m-1)n^2 \text{ is odd} \quad\Rightarrow\quad m \text{ is even and } n \text{ is odd}


$$

To prove $P \Rightarrow Q,$ it suffices to prove the contrapositive $\neg Q \Rightarrow \neg P.$

$$


\neg\left(m \text{ is even and } n \text{ is odd} \right) \Rightarrow \neg\left((m-1)n^2\text{ is odd}\right)


$$

Negating the right-hand-side of our implication is straightforward:

$$


\neg\left(m \text{ is even and } n \text{ is odd} \right) \Rightarrow (m-1)n^2 \text{ is even}


$$

To negate the statement "$m$ is even and $n$ is odd", we use De Morgan's law for conjunctions:

$$


\begin{aligned}¬(𝑚 is even and 𝑛 is odd) & =¬(𝑚 is even∧𝑛 is odd) \\ & =¬(𝑚 is even)∨¬(𝑛 is odd) \\ & =𝑚 is odd∨𝑛 is even \\ & =𝑚 is odd or 𝑛 is even\end{aligned}


$$

Now, let's write down the contrapositive of our statement.

The contrapositive form of the given statement is as follows:

$$


m \text{ is odd or } n \text{ is even} \quad\Rightarrow\quad (m-1)n^2 \text{ is even}


$$

We'll prove this statement instead of the original one.

Now, we have two cases: $m$ is odd, or $n$ is even.

- First, we consider the case when $m$ is odd.

****. If $m$ is odd, then $m=2a+1$ for some integer $a.$

As a result, we obtain

$$


\begin{aligned}(𝑚−1)𝑛^{2} & =(2𝑎+1−1)𝑛^{2} \\ & =2𝑎𝑛^{2} \\ & =2\underset{𝑏}{\underset{}{(𝑎𝑛^{2})}}.\end{aligned}


$$

Let $b=an^2.$ Since $a$ and $n$ are integers, we have that $b$ is an integer.

Therefore, we have

$$


\begin{aligned}(𝑚−1)𝑛^{2} & =2\underset{𝑏}{\underset{}{(𝑎𝑛^{2})}} \\ & =2𝑏,\end{aligned}


$$

which is a multiple of $2.$ Hence, $(m-1)n^2$ is even.

- Now, we consider the case when $n$ is even.

****. If $n$ is even, then $n=2a$ for some integer $a.$

As a result, we obtain

$$


\begin{aligned}(𝑚−1)𝑛^{2} & =(𝑚−1)(2𝑎)^{2} \\ & =4(𝑚−1)𝑎^{2} \\ & =2\underset{𝑏}{\underset{}{(2(𝑚−1)𝑎^{2})}}.\end{aligned}


$$

Let $b = 2(m-1)a^2.$ Since $a$ and $m$ are integers, we have that $b$ is an integer.

Therefore, we have

$$


\begin{aligned}(𝑚−1)𝑛^{2} & =2\underset{𝑏}{\underset{}{(2(𝑚−1)𝑎^{2})}} \\ & =2𝑏,\end{aligned}


$$

which is a multiple of $2.$ Hence, $(m-1)n^2$ is even.

Finally, we write our conclusion.

Therefore, combining the cases above, we conclude that $(m-1)n^2$ is odd only if $m$ is even and $n$ is odd.
