# Proving Parity

Source: https://www.mathacademy.com/topics/4429?courseId=76
Topic ID: 4429

## Prerequisites

- [Direct Proof](./2801-direct-proof.md)

## Lesson

### Introduction

Let's prove the following statement using a direct proof:

$$


\textrm{If } \underbrace{m \textrm{ is even and } n \textrm{ is odd,}}_{P(m,n)} \:\textrm{ then }\: \underbrace{m + 2n \textrm{ is even}.}_{Q(m,n)}


$$

To prove this result, we will use a framework similar to what we used for proving the parity of expressions of one variable:

- **Step 1:** Assume $P$ is true. In other words, we let $m$ and $n$ be integers, where $m$ is even and $n$ is odd.

- **Step 2:** Next, we use the *definition* of evenness to write $m=2a$ for some integer $a,$ and the definition of oddness to write $n=2b+1$ for some *other* integer $b.$

- **Step 3:** Then, we substitute $m=2a$ and $n=2b+1$ into the expression $m+2n$ and use algebraic techniques to show that the expression can be written as $2c,$ where $c$ is an integer.

- **Step 4:** Since $m+2n$ is a multiple of $2,$ we conclude that it's even (i.e., that $Q$ is true).

Note the following:

- Since the statement $P\Rightarrow Q$ is about evenness and oddness, it's clear from the context that $m\in \mathbb Z$ and $n\in \mathbb Z.$ In other words, the universal set of $P$ and $Q$ is given by $(m,n) \in \mathbb Z^2.$

- **Watch Out!** We *must* use two *different* integers to represent the evenness of $m$ and the oddness of $n.$ In this case, we used $a$ and $b.$ In general, we can use any letters we like, provided they are different. If we were to write $m=2a$ and $n=2a+1,$ this would lead to an *invalid proof* of the general statement since it follows from these assumptions that $n=m+1.$ This means our proof would only be valid for that special case.

### Example: Completing a Proof Schema

#### Question

Suppose we wish to construct a direct proof of the following statement:

$4-mn$ is even if $m$ is odd and $n$ is even.

A proof schema is outlined below. Fill in the missing entries.

Let $m$ be an $\boxed{\phantom{for any}} {\phantom{}} \,$ integer and let $n$ be an $\boxed{\phantom{for any}} {\phantom{}} \,$ integer. Then,

$$


m= \boxed{\phantom{for any} } {\phantom{}} \, \quad\text{and}\quad n= \boxed{\phantom{for any} } {\phantom{}} \,


$$

for some $\boxed{\phantom{integers a and b}} {\phantom{}} \,$

By substituting the above into $\boxed{\phantom{for any}},$ we can show that

$$


4-mn=\boxed{\phantom{for any} } {\phantom{}} \,


$$

where $c$ is $\boxed{\phantom{an integer}} {\phantom{}}.$

Therefore, since $4-mn$ $\boxed{\phantom{is 1 mm tt}} {\phantom{}} \,$ a multiple of $2,$ we conclude that $4-mn$ is $\boxed{\phantom{odd}} {\phantom{}}.$

#### Explanation

Recall the following:

- If an integer $n$ is even, then there exists an integer $p$ such that $n=2p.$

- If an integer $n$ is odd, then there exists an integer $q$ such that $n=2q+1.$

In this case, we need to show the following:

$$


m \text{ is odd and } n \text{ is even} \quad\Rightarrow\quad 4-mn \text{ is even}


$$

We start by using the fact that $m$ is odd and $n$ is even.

Let $m$ be an $\boxed{\color{blue}\text{odd}}$ integer and $n$ be an $\boxed{\color{blue}\text{even}}$ integer. Then,

$$


m=\boxed{\color{blue}2a+1} \quad\text{and}\quad n=\boxed{\color{blue}2b}


$$

for some $\boxed{\color{blue} \text{integers} a \text{and} b}.$

****! We must use two ** integers to represent the oddness of $m$ and evenness of $n.$ In this case, we use $a$ and $b.$

The idea is to substitute $m=2a+1$ and $n=2b$ into our expression $4-mn$ and show it is even by writing it as a multiple of $2.$

By substituting the above into $\boxed{\color{blue}4-mn},$ we can show that

$$


4-mn = \boxed{\color{blue}2c}


$$

where $c$ is $\boxed{\color{blue}\text{an integer}}.$

Once we've shown this, the proof is complete, and we can state our conclusion.

Therefore, since $4-mn$ $\boxed{\color{blue}\text{is}}$ a multiple of $2,$ we conclude that $4-mn$ is $\boxed{\color{blue}\text{even}}.$

### Constructing a Proof

We wish to prove the following statement:

$$


m \text{ is even and } n \text{ is odd} \quad\Rightarrow\quad m + 2n \text{ is even}


$$

Let's go through the proof step-by-step. We start by assuming that the antecedent is true:

**Step 1:** *Let $m$ and $n$ be integers, where $m$ is even and $n$ is odd.*

Now, we use the definitions of evenness and oddness.

**Step 2:** *Then, $m=2a$ and $n=2b+1$ for some integers $a$ and $b.$*

**Watch Out**! We must use two *different* integers to represent the evenness of $m$ and the oddness of $n.$ In this case, we use $a$ and $b.$

The idea is to substitute $m=2a$ and $n=2b+1$ into our expression $m + 2n$ and show it is even by writing it as a multiple of $2.$

**Step 3:** *Substituting $m=2a$ and $n=2b+1$ into the expression, we get*

$$


\begin{aligned}𝑚+2𝑛 & =(2𝑎)+2(2𝑏+1) \\ & =2𝑎+4𝑏+2 \\ & =2\underset{𝑐}{\underset{}{(𝑎+2𝑏+1)}}.\end{aligned}


$$

Now, if we define another integer $c=a + 2b + 1$ (highlighted above), we have that $m + 2n = 2c,$ which shows that $m + 2n$ is indeed a multiple of $2.$

*Let $c=a + 2b + 1.$ Since $a$ and $b$ are integers, $c$ is an integer. As a result, we have*

$$


\begin{aligned}𝑚+2𝑛 & =2\underset{𝑐}{\underset{}{(𝑎+2𝑏+1)}} \\ & =2𝑐\end{aligned}


$$

*which is a multiple of $2.$*

Finally, we write our conclusion:

**Step 4:** *Therefore, $m + 2n$ is even.*

Now that we've figured out all the details, let's write down the full proof.

### Stating a Full Proof

Proposition:

$$


m \text{ is even and } n \text{ is odd} \quad\Rightarrow\quad m + 2n \text{ is even}


$$

Proof:

*Let $m$ and $n$ be integers, where $m$ is even and $n$ is odd.*

*Then, $m=2a$ and $n=2b+1$ for some integers $a$ and $b.$*

*Substituting $m=2a$ and $n=2b+1$ into the expression, we get*

$$


\begin{aligned}𝑚+2𝑛 & =2𝑎+4𝑏+2 \\ & =2(𝑎+2𝑏+1) \\ & =2𝑐\end{aligned}


$$

*which is a multiple of $2.$*

*Therefore, $m + 2n$ is even.*

### Example: Proving an Expression Is Even

#### Question

Prove that if $m\in\mathbb Z$ is even and $n\in\mathbb Z$ is odd, then $mn$ is even.

#### Explanation

Recall the following:

- If an integer $n$ is even, then there exists an integer $p$ such that $n=2p.$

- If an integer $n$ is odd, then there exists an integer $q$ such that $n=2q+1.$

In this case, we need to show the following:

$$


m \text{ is even and } n \text{ is odd} \quad\Rightarrow\quad mn \text{ is even}


$$

We start by using the fact that $m$ is even and $n$ is odd.

Let $m$ and $n$ be integers, where $m$ is even and $n$ is odd. Then, $m=2a$ and $n=2b+1$ for some integers $a$ and $b.$

****! We must use two ** integers to represent the evenness of $m$ and the oddness of $n.$ In this case, we use $a$ and $b.$

The idea is to substitute $m=2a$ and $n=2b+1$ into our expression $mn$ and show it is even by writing it as a multiple of $2.$

Therefore, we have

$$


\begin{aligned}𝑚𝑛 & =(2𝑎)⋅(2𝑏+1) \\ & =4𝑎𝑏+2𝑎 \\ & =2\underset{𝑐}{\underset{}{(2𝑎𝑏+𝑎)}}.\end{aligned}


$$

Now, if we define another integer $c=2ab+a$ (highlighted above), we have that $mn = 2c,$ which shows that $mn$ is indeed a multiple of $2.$

Let $c=2ab+a.$ Since $a$ and $b$ are integers, $c$ is an integer.

Therefore,

$$


\begin{aligned}𝑚𝑛 & =2\underset{𝑐}{\underset{}{(2𝑎𝑏+𝑎)}} \\ & =2𝑐\end{aligned}


$$

which is a multiple of $2.$

Finally, we write our conclusion:

Therefore, we conclude that $mn$ is even.

### Example: Proving an Expression Is Odd

#### Question

Show that if $m\in\mathbb Z$ is odd and $n\in\mathbb Z$ is even, then $m - n$ is odd.

#### Explanation

Recall the following:

- If an integer $n$ is even, then there exists an integer $p$ such that $n=2p.$

- If an integer $n$ is odd, then there exists an integer $q$ such that $n=2q+1.$

In this case, we need to show the following:

$$


m \textrm{ is odd and } n \textrm{ is even } \Rightarrow m - n \textrm{ is odd}.


$$

We start by using the fact that $m$ is odd and $n$ is even.

Let $m$ and $n$ be integers, where $m$ is odd and $n$ is even. Then, $m=2a+1$ and $n=2b$ for some integers $a$ and $b.$

****! We must use two ** integers to represent the oddness of $m$ and the evenness of $n.$ In this case, we use $a$ and $b.$

The idea is to substitute $m=2a+1$ and $n=2b$ into our expression $m - n$ and show it is odd by writing it as a multiple of $2,$ plus $1.$

Therefore, we obtain

$$


\begin{aligned}𝑚−𝑛 & =(2𝑎+1)−(2𝑏) \\ & =2𝑎+1−2𝑏 \\ & =(2𝑎−2𝑏)+1 \\ & =2\underset{𝑐}{\underset{}{(𝑎−𝑏)}}+1.\end{aligned}


$$

Now, if we define another integer $c=a - b$ (highlighted above), we have that $m - n = 2c+1,$ which shows that $m - n$ is indeed one more than a multiple of $2.$

Let $c=a - b.$ Since $a$ and $b$ are integers, $c$ is an integer.

Therefore,

$$


\begin{aligned}𝑚−𝑛 & =2\underset{𝑐}{\underset{}{(𝑎−𝑏)}}+1 \\ & =2𝑐+1\end{aligned}


$$

which is one more than a multiple of $2.$

Finally, we write our conclusion:

Therefore, we conclude that $m - n$ is odd.
