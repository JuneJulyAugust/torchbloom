# Solving Linear Congruences

Source: https://www.mathacademy.com/topics/4839?courseId=76
Topic ID: 4839

## Prerequisites

- [Multiplicative Inverses Modulo N](./4818-multiplicative-inverses-modulo-n.md)

## Lesson

### Introduction

Suppose we want to solve the following linear congruence:

$$


4x \equiv 2 \quad (\text{mod}\:5)


$$

Since the modulus $n=5$ is fairly small, we can solve the congruence by trial and error.

Substituting the trial solutions $x = 0,1,2,3,4$ into the equation, we obtain the following:

$$


\begin{aligned}4⋅0 & ≡0≢2 & & (mod\,5) & & × \\ 4⋅1 & ≡4≢2 & & (mod\,5) & & × \\ 4⋅2 & ≡8≡5+3≡3≢2 & & (mod\,5) & & × \\ 4⋅3 & ≡12≡2⋅5+2≡2 & & (mod\,5) & & ✓ \\ 4⋅4 & ≡16≡3⋅5+1≡1≢2 & & (mod\,5) & & ×\end{aligned}


$$

Therefore, the solution is $x \equiv {\color{blue}{3}} \:(\text{mod}\:5).$

**Note**: Any number congruent to $3$ modulo $5$ is a solution. For example, note that $8 \equiv 3,$ and this also satisfies our congruence:

$$


\begin{aligned}4𝑥 & ≡4⋅8\, & & (mod\,5) \\ & ≡32\, & & (mod\,5) \\ & ≡6⋅5+2\, & & (mod\,5) \\ & ≡0+2\, & & (mod\,5) \\ & ≡2\,\,✓\, & & (mod\,5)\end{aligned}


$$

### Example: Solving Linear Congruences by Trial and Error

#### Question

Solve the linear congruence $2x \equiv 1 \:(\text{mod}\:5)$ using trial and error.

#### Explanation

Since the modulus $n=5$ is fairly small, we can solve the congruence by trial and error.

Substituting $x = 0,1,2,3,4$ into the equation, we obtain the following:

$$


\begin{aligned}2⋅0 & ≡0≢1 & & (mod\,5) & & × \\ 2⋅1 & ≡2≢1 & & (mod\,5) & & × \\ 2⋅2 & ≡4≢1 & & (mod\,5) & & × \\ 2⋅3 & ≡6≡5+1≡1 & & (mod\,5) & & ✓ \\ 2⋅4 & ≡8≡5+3≡3≢1 & & (mod\,5) & & ×\end{aligned}


$$

Therefore, the solution is is $x\equiv {\color{blue}{3}} \:(\text{mod}\:5).$

****: Any number congruent to $3$ modulo $5$ is a solution. For example, note that $8\equiv 3,$ and this also satisfies our congruence:

$$


\begin{aligned}2𝑥 & ≡2⋅8\, & & (mod\,5) \\ & ≡16\, & & (mod\,5) \\ & ≡3⋅5+1\, & & (mod\,5) \\ & ≡0+1\, & & (mod\,5) \\ & ≡1\,\,✓\, & & (mod\,5)\end{aligned}


$$

### Using the Multiplicative Inverse

Now, let's consider the following linear congruence:

$$


4x \equiv 5 \qquad (\text{mod}\:21)


$$

We can solve this congruence by multiplying both sides by the *multiplicative inverse* of $4$ modulo $21.$

In this case, we can find the multiplicative inverse by raising $4$ to positive integer exponents until we get an answer of $1{:}$

$$


\begin{aligned}4^{2} & ≡16 & & (mod\,21) \\ 4^{3} & ≡4⋅16≡64≡3⋅21+1≡3⋅0+1≡1 & & (mod\,21)\end{aligned}


$$

So, $4 \cdot {\color{blue}{16}} \equiv 1 \:(\textrm{mod}\:21),$ which means that $16$ is the multiplicative inverse of $4$ (modulo $21$).

Now, multiplying both sides of our congruence by $16,$ we get the following:

$$


\begin{aligned}4𝑥 & ≡5 & & (mod\,21) \\ 16⋅4𝑥 & ≡16⋅5 & & (mod\,21) \\ (16⋅4)𝑥 & ≡80 & & (mod\,21) \\ 1⋅𝑥 & ≡3⋅21+17 & & (mod\,21) \\ 𝑥 & ≡17 & & (mod\,21)\end{aligned}


$$

Therefore, the solution is $x \equiv 17 \: (\text{mod}\:21).$

### Uniqueness of Solutions

Not every linear congruence has a unique solution!

To determine whether a linear congruence has a single unique solution, we can use the following rule:

*A linear congruence $ax \equiv b \:(\text{mod}\:n)$ has a unique solution modulo $n$ if and only if $\text{gcd}(a,n)=1.$*

We'll prove this theorem at the end of the lesson.

So, whenever we solve a linear congruence, we should first use the above rule to check that there is a unique solution. In the linear congruence $4x \equiv 5 \:(\text{mod}\:21),$ we had $a=4$ and $n=21.$ Therefore,

$$


\text{gcd}(a,n)=\text{gcd}(4,21)=1,


$$

which means that our congruence does indeed have a unique solution.

In a future lesson, we'll discuss cases where linear congruences have multiple or no solutions.

### Example: Solving Congruences Using Multiplicative Inverses

#### Question

Solve the modular equation $7x \equiv 3 \:(\text{mod}\:15).$

**

#### Explanation

Recall that a linear congruence $ax \equiv b \:(\text{mod}\:n)$ has a unique solution modulo $n$ if and only if $\text{gcd}(a,n)=1.$

In the given congruence, we have $a=7$ and $n=15,$ so

$$


\text{gcd}(a,n)=\text{gcd}(7,15)=1.


$$

This means our congruence does indeed have a unique solution.

To find the solution, we need to multiply both sides of the equation by the multiplicative inverse of $7\,(\textrm{mod}\:15).$ To find the inverse of $7\,(\textrm{mod}\:15)$, we compute the exponents of $7\,(\textrm{mod}\:15)$ until we get a result of $1 \,(\textrm{mod}\:15)\mathbin{:}$

$$


\begin{aligned}7^{2} & ≡49≡3⋅15+4≡4 & & (mod\,15) \\ 7^{3} & ≡4⋅7≡28≡15+13≡13 & & (mod\,15) \\ 7^{4} & ≡13⋅7≡91≡6⋅15+1≡1 & & (mod\,15)\end{aligned}


$$

So, $13 \cdot 7 \equiv 1 \:(\textrm{mod}\:15),$ which means that $13$ is the multiplicative inverse of $7$ (modulo $15$).

Now, multiplying both sides of our congruence by $13,$ we get the following:

$$


\begin{aligned}7𝑥 & ≡3 & & (mod\,15) \\ 13⋅7𝑥 & ≡13⋅3 & & (mod\,15) \\ (13⋅7)𝑥 & ≡39 & & (mod\,15) \\ 1⋅𝑥 & ≡2⋅15+9 & & (mod\,15) \\ 𝑥 & ≡9 & & (mod\,15)\end{aligned}


$$

Therefore, the solution is $x\equiv 9 \: (\text{mod}\:15).$

### Example: Solving Congruences Using Additive and Multiplicative Inverses

#### Question

Solve the following congruence:

$$


7x - 11 \equiv 29 \quad (\text{mod}\:19)


$$

**

#### Explanation

First, we reduce our congruence to a congruence of the form $ax\equiv b,$ as follows:

$$


\begin{aligned}7𝑥−11 & ≡29\, & (mod\,19) \\ 7𝑥−11+11 & ≡29+11\, & (mod\,19) \\ 7𝑥 & ≡40\, & (mod\,19) \\ 7𝑥 & ≡38+2\, & (mod\,19) \\ 7𝑥 & ≡2⋅19+2\, & (mod\,19) \\ 7𝑥 & ≡2\, & (mod\,19)\end{aligned}


$$

Recall that a linear congruence $ax \equiv b \:(\text{mod}\:n)$ has a unique solution modulo $n$ if and only if $\text{gcd}(a,n)=1.$

In the given congruence, we have $a=7$ and $n=19$, and

$$


\text{gcd}(a,n)=\text{gcd}(7,19)=1.


$$

So, our congruence does indeed have a unique solution.

To find the solution, we need to multiply both sides of the equation by the multiplicative inverse of $7\,(\textrm{mod}\:19).$ To find the inverse of $7\,(\textrm{mod}\:19)$, we compute the exponents of $7\,(\textrm{mod}\:19)$ until we get a result of $1 \,(\textrm{mod}\:19)\mathbin{:}$

$$


\begin{aligned}7^{2} & ≡49≡2⋅19+11≡11 & & (mod\,19) \\ 7^{3} & ≡11⋅7≡77≡4⋅19+1≡1 & & (mod\,19)\end{aligned}


$$

So, $11 \cdot 7 \equiv 1 \:(\textrm{mod}\:19),$ which means that $11$ is the multiplicative inverse of $7$ (modulo $19$).

Now, multiplying both sides of our congruence by $11,$ we get the following:

$$


\begin{aligned}7𝑥 & ≡2 & & (mod\,19) \\ 11⋅7𝑥 & ≡11⋅2 & & (mod\,19) \\ (11⋅7)𝑥 & ≡22 & & (mod\,19) \\ 1⋅𝑥 & ≡19+3 & & (mod\,19) \\ 𝑥 & ≡3 & & (mod\,19)\end{aligned}


$$

Therefore, the solution is $x \equiv 3 \: (\text{mod}\:19).$

### Example: Solving Congruences Using the Extended Euclidean Algorithm

#### Question

Solve the congruence $15x \equiv 17 \:(\text{mod}\:44).$

#### Explanation

Recall that a linear congruence $ax \equiv b \:(\text{mod}\:n)$ has a unique solution modulo $n$ if and only if $\text{gcd}(a,n)=1.$

In the given congruence, we have $a=15$ and $n=44,$ where

$$


\text{gcd}(a,n)=\text{gcd}(15,44)=1.


$$

So, our congruence does indeed have a unique solution.

To find the solution, we need to multiply both sides of the equation by the multiplicative inverse of $15\,(\textrm{mod}\:44).$ To find the inverse of $15\,(\textrm{mod}\:44),$ we use the extended Euclidean algorithm.

First, we apply the forward reduction:

$$


\begin{aligned}\begin{aligned}44 & = & 15⋅2 & + & 14 \\ & ↙ & & ↙ & \\ 15 & = & 14⋅1 & + & 1\end{aligned}\end{aligned}


$$

Solving for the rightmost terms in the equations above, we get

$$


\begin{aligned}14 & =44−15⋅2 \\ 1 & =15−14\end{aligned}


$$

Then, we back-substitute:

$$


\begin{aligned}1 & =15−14 \\ & =15−(44−15⋅2) \\ & =15⋅3−44\end{aligned}


$$

We can write this result in modulo $44,$ as follows:

$$


\begin{aligned}15⋅3−44 & ≡1 & & (mod\,44) \\ 15⋅3 & ≡1 & & (mod\,44)\end{aligned}


$$

So, $15 \cdot 3 \equiv 1 \:(\textrm{mod}\:44),$ which means that $3$ is the multiplicative inverse of $15$ (modulo $44$).

Now, multiplying both sides of our original congruence by $3,$ we get the following:

$$


\begin{aligned}15𝑥 & ≡17 & & (mod\,44) \\ 3⋅15𝑥 & ≡3⋅17 & & (mod\,44) \\ (3⋅15)𝑥 & ≡51 & & (mod\,44) \\ 1⋅𝑥 & ≡44+7 & & (mod\,44) \\ 𝑥 & ≡7 & & (mod\,44)\end{aligned}


$$

Therefore, the solution is $x \equiv 7 \: (\text{mod}\:44).$

### Proof of the Theorem

Let's prove the following theorem:

*Let $a$, $b,$ and $n$ integers. If $\text{gcd}(a,n)=1$, then the linear congruence $ax \equiv b \:(\text{mod}\:n)$ has a unique solution.*

**Proof**.

To prove this theorem, we must show that a solution exists and that it is unique.

First, we prove that a solution exists:

- If $\text{gcd}(a,n)=1$, then by Bézout's identity, there exist integers $u$ and $v$ such that We can write this result in modulo $n$ as follows: This means that $u$ is the multiplicative inverse of $a$ (modulo $n$). So, multiplying both sides of the original congruence $ax \equiv b \:(\text{mod}\:n)$ by $u,$ we get Therefore, $x \equiv ub \: (\text{mod}\:n)$ is a solution.

Next, we prove the solution is unique:

- To prove uniqueness, we show that two solutions $x_1$ and $x_2$ to our congruence must be congruent. Suppose $x_1$ and $x_2$ are two solutions to the congruence, i.e., $ax_1 \equiv b\: (\textrm{mod}\,{n})$ and $ax_2 \equiv b\: (\textrm{mod}\,{n})$. We want to show that $x_1 \equiv x_2$. Since $ax_1 \equiv b\: (\textrm{mod}\,{n})$ and $ax_2 \equiv b\: (\textrm{mod}\,{n})$, we have Now, since $\text{gcd}(a,n) = 1$, we can multiply both sides by the modular inverse of $a$ modulo $n,$ which we previously denoted $u.$ Since $a$ and $n$ are relatively prime, $u$ exists. Therefore, $u \cdot a \equiv 1\:(\textrm{mod}\,{n})$, and we have as required.

Thus, we have shown both the existence and uniqueness of the solution to the congruence $ax \equiv b \pmod{n}$ when $\text{gcd}(a,n) = 1$.
