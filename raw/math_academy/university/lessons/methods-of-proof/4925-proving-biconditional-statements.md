# Proving Biconditional Statements

Source: https://www.mathacademy.com/topics/4925?courseId=76
Topic ID: 4925

## Prerequisites

- [Equivalence Relations](./2622-equivalence-relations.md)
- [Proving Congruence by Contrapositive](./2799-proving-congruence-by-contrapositive.md)
- [Proving Divisibility Using Congruence](./4435-proving-divisibility-using-congruence.md)

## Lesson

### Introduction

Recall that the biconditional statement $P\Leftrightarrow Q$ is true if and only if $P$ and $Q$ have the same truth value.

The relation "$\Leftrightarrow$" between two statements is an *equivalence relation* because it's reflexive, symmetric, and transitive:

- $P\Leftrightarrow P$ is always true because $P$ has the same truth value as itself.

- If $P\Leftrightarrow Q$ is true, then $Q\Leftrightarrow P$ is also true. If $P$ and $Q$ have the same truth value, then $Q$ and $P$ also have the same truth value.

- If $P\Leftrightarrow Q$ and $Q\Leftrightarrow R$ are both true, then $P\Leftrightarrow R$ is also true.

Suppose have the following chain of equivalent statements:

$$


P \quad \Leftrightarrow\quad Q \quad \Leftrightarrow\quad R


$$

There are only two ways in which this chain of equivalences is true:

- $P,Q,$ and $R$ are *all* true

- $P,Q,$ and $R$ are *all* false

Consider the following predicate for $x\in\mathbb Z.$

$$


P(x): \quad 2x-3 = 5


$$

This is *equivalent* to the statement $x=4,$ and this can be proved using a *chain of equivalent statements* as follows:

$$


\begin{aligned}\underset{𝑃(𝑥)}{\underset{}{2𝑥−3=5}}\,⇔\,\underset{𝑄(𝑥)}{\underset{}{2𝑥=8}}\,⇔\,\underset{𝑅(𝑥)}{\underset{}{𝑥=4}}\end{aligned}


$$

Note that substituting ${\color{blue}{x}}={\color{blue}{4}}$ into $P,Q,$ and $R$ gives a truth value of "true" $(\text{T})$ in each case:

$$


\begin{aligned}\underset{T}{\underset{}{2⋅4−3=5}}\,⇔\,\underset{T}{\underset{}{2⋅4=8}}\,⇔\,\underset{T}{\underset{}{4=4}}\end{aligned}


$$

However, substituting ${\color{red}{x}}={\color{red}{3}}$ into $P,Q,$ and $R$ gives a truth value of "false" $(\text{F})$ in each case:

$$


\begin{aligned}\underset{F}{\underset{}{2⋅3−3=5}}\,⇔\,\underset{F}{\underset{}{2⋅3=8}}\,⇔\,\underset{F}{\underset{}{3=4}}\end{aligned}


$$

In general, we can prove a biconditional $P\Leftrightarrow Q$ by finding a set of statements $R_1, R_2, \ldots, R_n$ and using them to form a chain of equivalent statements connecting $P$ and $Q{:}$

$$


P \quad \Leftrightarrow\quad R_1 \quad \Leftrightarrow\quad R_2 \quad \Leftrightarrow\quad \cdots \quad \Leftrightarrow\quad R_n \quad \Leftrightarrow\quad Q


$$

In fact, you've been implicitly using this type of argument throughout your mathematical career! Solving linear equations is just one example.

### Proving an Implication and Its Converse

Another way to prove the statement $P\Leftrightarrow Q$ is to recall that it is equivalent to the conjunction of two implications:

$$


P\Leftrightarrow Q \equiv (P\Rightarrow Q) \land (Q\Rightarrow P)


$$

So, to prove that $P\Leftrightarrow Q$ is true, we can proceed as follows:

- First, prove the statement $P\Rightarrow Q.$

- Then, prove the converse statement $Q\Rightarrow P.$

A valid proof of both $P\Rightarrow Q$ *and* $Q\Rightarrow P$ is equivalent to proving $P\Leftrightarrow Q.$

We can use completely different arguments for proving $P\Rightarrow Q$ and $Q\Rightarrow P.$ For instance, the first proof might be direct, and the second could use the contrapositive.

Let's see an example.

### A Worked Example

Let's prove the following biconditional statement:

*Suppose $n$ is an integer. Then, $15 \mid n$ if and only if $3 \mid n$ and $5 \mid n.$*

The connector "if and only if" means we must prove an equivalence.

$$


P \Leftrightarrow Q


$$

However, instead of proving an equivalence directly, we can prove two conditional statements.

$$


P\Leftrightarrow Q \equiv (P\Rightarrow Q) \land (Q\Rightarrow P)


$$

So, we start our proof as follows:

*We need to show the following:*

$$


15∣𝑛


$$

*This is the same as proving two implications.*

First, we consider the "left to right" implication.

****** *We need to show that*

$$


15∣𝑛


$$

*If $15 \mid n,$ then $n =15k$ for some integer $k.$ We can rewrite this equation as*

$$


n = 3\big( 5k \big),


$$

*which means that $3 \mid n.$ Also, we can write*

$$


n = 5\big( 3k \big),


$$

*which means that $5 \mid n.$ Therefore, $3 \mid n$ and $5 \mid n.$*

Next, we consider the "right to left" implication.

****** *We need to show that*

$$


3∣𝑛


$$

*Since $3 \mid n,$ then $n=3s$ for some integer $s,$ and since $5 \mid n,$ then $n=5t$ for some integer $t.$*

Notice that the divisibility of $n$ by $3$ and $5$ are independent. So, in general, we should use different letters ($s$ and $t$) in the reasoning above.

Next, we'll use the fact that our divisors are coprime, meaning $\text{gcd}(3,5) = 1.$ Then, by applying the extended Euclidian algorithm, we can write

$$


3 \cdot 2 + 5 \cdot (-1) = 1.


$$

We continue with this part of the proof as follows:

*The integers $3$ and $5$ are coprime and $3 \cdot 2 + 5 \cdot (-1) = 1.$ So, multiplying this equation by $n,$ we get*

$$


3 \cdot 2n + 5 \cdot ( -n ) = n.


$$

*Now, substituting $n=5t$ into the first term on the left-hand side and $n=3s$ into the second term, we get*

$$


\begin{aligned}3⋅2(5𝑡)+5⋅(−(3𝑠))=𝑛 \\ 15⋅(2𝑡)+15⋅(−𝑠)=𝑛 \\ 15⋅(2𝑡−𝑠)=𝑛,\end{aligned}


$$

*which means that $15 \mid n.$ So, the second implication is proved.*

Finally, we write down the conclusion:

*Therefore, $15 \mid n$ if and only if $3 \mid n$ and $5 \mid n.$*

Let's state the full proof.

### Stating the Full Proof

Proposition.

*Suppose $n$ is an integer. Then, $15 \mid n$ if and only if $3 \mid n$ and $5 \mid n.$*

Proof:

*We need to show the following:*

$$


15∣𝑛


$$

*This is the same as proving two implications.*

****** *We need to show that*

$$


15∣𝑛


$$

*If $15 \mid n,$ then $n =15k$ for some integer $k.$ We can rewrite this equation as*

$$


n = 3\big( 5k \big),


$$

*which means that $3 \mid n.$ Also, we can write*

$$


n = 5\big( 3k \big),


$$

*which means that $5 \mid n.$ Therefore, $3 \mid n$ and $5 \mid n.$*

****** *We need to show that*

$$


3∣𝑛


$$

*Since $3 \mid n,$ then $n=3s$ for some integer $s,$ and since $5 \mid n,$ then $n=5t$ for some integer $t.$*

*The integers $3$ and $5$ are coprime and $3 \cdot 2 + 5 \cdot (-1) = 1.$ So, multiplying this equation by $n,$ we get*

$$


3 \cdot 2n + 5 \cdot \big( -n \big) = n.


$$

*Now, substituting $n=5t$ into the first term on the left-hand side and $n=3s$ into the second term, we get*

$$


\begin{aligned}3⋅2(5𝑡)+5⋅(−(3𝑠))=𝑛 \\ 15⋅(2𝑡)+15⋅(−𝑠)=𝑛 \\ 15⋅(2𝑡−𝑠)=𝑛,\end{aligned}


$$

*which means that $15 \mid n.$ So, the second implication is proved.*

*Therefore, $15 \mid n$ if and only if $3 \mid n$ and $5 \mid n.$*

### Example: Proving an Equivalence Involving Divisibility and Congruences

#### Question

Let $n$ be an integer. Prove that $a \equiv b \: (\text{mod} \: 24)$ if and only if $a \equiv b \: (\text{mod} \: 3)$ and $a \equiv b \: (\text{mod} \: 8).$

**

$$


3 \cdot 3 + 8 \cdot (-1) = \text{gcd}(3,8)=1


$$

#### Explanation

The connector "if and only if" means we must prove an equivalence.

$$


P \Leftrightarrow Q


$$

However, instead of proving an equivalence directly, we can instead prove two conditional statements.

$$


P\Leftrightarrow Q \equiv (P\Rightarrow Q) \land (Q\Rightarrow P)


$$

So, we start our proof as follows:

We need to show the following:

$$


𝑎≡𝑏\,(mod\,24)


$$

This is the same as proving two implications.

First, we consider the "left to right" implication.

**** We need to show that

$$


𝑎≡𝑏\,(mod\,24)


$$

To do that, we first write the statement in terms of divisibility.

Or, in terms of divisibility,

$$


24 \mid a-b \quad \Rightarrow \quad \big( 3 \mid a-b \quad \land \quad 8 \mid a-b \big).


$$

Then, we write $n=a-b$ to simplify the notation.

Let's denote $n=a-b.$

So, we now need to prove that

$$


24 \mid n \quad \Rightarrow \quad \big( 3 \mid n \quad \land \quad 8 \mid n \big).


$$

We proceed as follows:

If $24 \mid n,$ then $n =24k$ for some integer $k.$ We can rewrite this equation as

$$


n = 3\big( 8k \big),


$$

which means that $3 \mid n.$ Also, we can write

$$


n = 8\big( 3k \big),


$$

which means that $8 \mid n.$ Therefore, $3 \mid n$ and $8 \mid n.$

Next, we consider the "right to left" implication.

**** We need to show that

$$


𝑎≡𝑏\,(mod\,3)


$$

Or, in terms of divisibility,

$$


\big( 3 \mid a-b \quad \land \quad 8 \mid a-b \big) \quad \Rightarrow \quad 24 \mid a-b.


$$

Again, we simplify the notation by introducing $n=a-b.$

Let's again denote $n=a-b.$

So now, we need to prove

$$


\big( 3 \mid n \quad \land \quad 8 \mid n \big) \quad \Rightarrow \quad 24 \mid n.


$$

Next, we use the definition of divisibility.

Since $3 \mid n,$ then $n=3s$ for some integer $s,$ and since $8 \mid n,$ then $n=8t$ for some integer $t.$

Notice that the divisibility of $n$ by $3$ and $8$ are independent. So, in general, we should use different letters ($s$ and $t$) in the reasoning above.

Next, we'll use the fact that our divisors are coprime.

The integers $3$ and $8$ are coprime and $3 \cdot 3 + 8 \cdot (-1) = 1.$ So, multiplying this equation by $n,$ we get

$$


3 \cdot 3n + 8 \cdot \big(-n \big) = n.


$$

Now, substituting $n=8t$ into the first term on the left-hand side and $n=3s$ into the second term, we get

$$


\begin{aligned}3⋅3(8𝑡)+8⋅(−(3𝑠))=𝑛 \\ 24⋅(3𝑡)+24⋅(−𝑠)=𝑛 \\ 24⋅(3𝑡−𝑠)=𝑛,\end{aligned}


$$

which means that $24 \mid n.$ So, the second implication is proved.

Finally, we write down the conclusion:

Therefore, $a \equiv b \: (\text{mod} \: 24)$ if and only if $a \equiv b \: (\text{mod} \: 3)$ and $a \equiv b \: (\text{mod} \: 8).$

### Example: Proving Parity Using Congruences and the Contrapositive

#### Question

Let $n$ be an integer. Prove that $n$ is even if and only if $n^2$ is even.

#### Explanation

The connector "if and only if" means we need to prove an equivalence.

$$


P\Leftrightarrow Q


$$

However, instead of proving an equivalence directly, we can instead prove two conditional statements.

$$


P\Leftrightarrow Q \equiv (P\Rightarrow Q) \land (Q\Rightarrow P)


$$

So, we start our proof as follows:

We need to show the following:

$$


𝑛


$$

This is the same as proving two implications.

First, we consider the "left to right" implication.

**** We need to show that

$$


𝑛


$$

If $n$ is even, then $n \equiv 0 \: (\text{mod}\:2).$ Therefore,

$$


\begin{aligned}𝑛^{2} & ≡0^{2} & (mod\,2) \\ 𝑛^{2} & ≡0 & (mod\,2)\end{aligned}


$$

which means that $n^2$ is even. So, the first implication is proved.

Next, we consider the "right to left" implication.

**** We need to show that

$$


𝑛^{2}


$$

Or, in terms of congruences,

$$


n^2 \equiv 0 \:\: (\text{mod}\:2) \quad\Rightarrow\quad n \equiv 0 \:\: (\text{mod}\:2).


$$

Now, the final statement can be re-written using negations as follows:

Since we're working modulo $2$ (where the only remainders are $0$ and $1$), this statement is equivalent to

$$


n^2 \not\equiv 1 \:\: (\text{mod}\:2) \quad\Rightarrow\quad n \not\equiv 1 \:\: (\text{mod}\:2).


$$

Proving the negation statement can be a difficult task, but we can avoid that by using the contrapositive:

The contrapositive of the last statement is

$$


n \equiv 1 \:\: (\text{mod}\:2) \quad\Rightarrow\quad n^2 \equiv 1 \:\: (\text{mod}\:2).


$$

Next, we'll prove the contrapositive, as shown below.

Now, if $n \equiv 1 \: (\text{mod}\:2),$ then

$$


\begin{aligned}𝑛^{2} & ≡1^{2} & (mod\,2) \\ & ≡1 & (mod\,2)\end{aligned}


$$

as required. So, the second implication is proved.

Finally, we write down the conclusion:

Therefore, $n$ is even if and only if $n^2$ is even.

### Example: Proving Equivalences Over the Real Numbers

#### Question

Let $x$ and $y$ be real numbers. Prove that $(x+y)^2 =x^2+y^2$ if and only if $x=0$ or $y=0.$

#### Explanation

The connector "if and only if" means we must prove an equivalence.

$$


P \Leftrightarrow Q


$$

However, instead of proving an equivalence directly, we can instead prove two conditional statements.

$$


P\Leftrightarrow Q \equiv (P\Rightarrow Q) \land (Q\Rightarrow P)


$$

So, we start our proof as follows:

We need to prove the following:

$$


(x+y)^2 =x^2+y^2 \quad \Leftrightarrow \quad \big( x=0 \quad \lor \quad y=0 \big)


$$

This is the same as proving two implications.

First, we consider the "left to right" implication.

**** We need to show that

$$


(x+y)^2 =x^2+y^2 \quad \Rightarrow \quad \big( x=0 \quad \lor \quad y=0 \big).


$$

By expanding the left-hand side and simplifying, we obtain

$$


\begin{aligned}𝑥^{2}+2𝑥𝑦+𝑦^{2} & =𝑥^{2}+𝑦^{2} \\ 2𝑥𝑦 & =0 \\ 𝑥⋅𝑦 & =0.\end{aligned}


$$

The product on the left-hand side equals zero if $x=0$ or $y=0.$

Next, we consider the "right to left" implication.

**** We need to show that

$$


\big(x=0 \quad \lor \quad y=0 \big) \quad \Rightarrow \quad (x+y)^2= x^2+y^2.


$$

Here, consider the two cases separately.

We have two subcases:

**** Let $x=0.$ Then, substituting this into our equation, we obtain

$$


\begin{aligned}(𝑥+𝑦)^{2} & =𝑥^{2}+𝑦^{2} \\ (0+𝑦)^{2} & =0^{2}+𝑦^{2} \\ 𝑦^{2} & =𝑦^{2},\end{aligned}


$$

which is always true.

And the second case.

**** Let $y=0.$ Then, substituting this into our equation, we obtain

$$


\begin{aligned}(𝑥+𝑦)^{2} & =𝑥^{2}+𝑦^{2} \\ (𝑥+0)^{2} & =𝑥^{2}+0^{2} \\ 𝑥^{2} & =𝑥^{2},\end{aligned}


$$

which is always true.

Hence, if $x=0$ or $y=0$ then $(x+y)^2=x^2+y^2.$

Finally, we write down the conclusion:

Therefore, $(x+y)^2=x^2+y^2$ if and only if $x=0$ or $y=0.$
