# Proving Irrationality by Contradiction

Source: https://www.mathacademy.com/topics/4922?courseId=76
Topic ID: 4922

## Prerequisites

- [Proof by Contradiction](./3414-proof-by-contradiction.md)
- [Properties of Prime Divisibility](./4928-properties-of-prime-divisibility.md)

## Lesson

### Introduction

We can use proof by contradiction to prove that certain numbers are irrational.

For example, let's show that $\sqrt{2}$ is an irrational number. We begin by stating the formal statement $P$ that we wish to prove:

$$


\sqrt{√2}


$$

To prove that $P$ is true, we assume that $\lnot P$ is true and show this leads to a contradiction.

$$


\sqrt{√2}


$$

We begin our proof as follows:

*Assume, for a contradiction, that $\sqrt{2}$ is rational.*

If a number is rational, it can be written as a fraction in its lowest terms, i.e., where the numerator and denominator are coprime.

*Then,*

$$


\sqrt{2} = \dfrac{a}{b}


$$

*for some integers $a$ and $b,$ where $\gcd(a,b) = 1.$*

The contradiction we seek is that $a$ and $b$ are, in fact, *not* coprime under this assumption.

We start by squaring both sides of the equation:

*So, we have*

$$


\begin{aligned}\sqrt{√2} & =\frac{𝑎}{𝑏} \\ (\sqrt{√2})^{2} & =(\frac{𝑎}{𝑏})^{2} \\ 2 & =\frac{𝑎^{2}}{𝑏^{2}} \\ 2𝑏^{2} & =𝑎^{2},\end{aligned}


$$

*which, by the definition of divisibility, means that $2 \mid a^2.$*

Now, recall the following property of divisibility by a prime $p{:}$

$$


p \mid xy \quad\Rightarrow\quad (p \mid x) \lor (p \mid y)


$$

Applying this property with $p=2$ and $x=y=a,$ we have

$$


2 \mid a\cdot a = a^2 \quad\Rightarrow\quad (2 \mid a) \lor (2 \mid a).


$$

So, we have that $2 \mid a.$

*Since $2$ is prime, we have $2 \mid a,$ which means $a = 2c$ where $c$ is an integer.*

Now, we substitute $a=2c$ into the equation $2b^2 = a^2$ and show that $2$ is *also* a factor of $b.$

*Therefore,*

$$


\begin{aligned}2𝑏^{2} & =(2𝑐)^{2} \\ 2𝑏^{2} & =4𝑐^{2} \\ 𝑏^{2} & =2𝑐^{2}\end{aligned}


$$

*Hence, by the definition of divisibility, $2 \mid b^2,$ which means that $2 \mid b.$*

Finally, since $a$ and $b$ have a common factor of $2,$ their greatest common divisor is at least $2.$ This gives us our contradiction.

*Combining the results $2 \mid a$ and $2 \mid b,$ we conclude that $\gcd(a,b) \geq 2.$ But this contradicts the assumption that $\gcd(a,b) = 1.$*

Since we have a contradiction, our original assumption must be incorrect. Hence, we write our conclusion as follows:

*Therefore, $\sqrt{2}$ is irrational.*

Now that we've figured out the details, let's state the full proof.

### Stating the Full Proof

Proposition:

*$\sqrt{2}$ is irrational*

Proof:

*Assume, for a contradiction, that $\sqrt{2}$ is rational. Then,*

$$


\sqrt{2} = \dfrac{a}{b}


$$

*for some integers $a$ and $b,$ where $\gcd(a,b) = 1.$*

*So, we have*

$$


\begin{aligned}\sqrt{√2} & =\frac{𝑎}{𝑏} \\ (\sqrt{√2})^{2} & =(\frac{𝑎}{𝑏})^{2} \\ 2 & =\frac{𝑎^{2}}{𝑏^{2}} \\ 2𝑏^{2} & =𝑎^{2},\end{aligned}


$$

*which means that $2 \mid a^2.$*

*Since $2$ is prime, we have $2 \mid a,$ which means $a = 2c$ where $c$ is an integer.*

*Therefore,*

$$


\begin{aligned}2𝑏^{2} & =(2𝑐)^{2} \\ 2𝑏^{2} & =4𝑐^{2} \\ 𝑏^{2} & =2𝑐^{2}\end{aligned}


$$

*Hence, by the definition of divisibility, $2 \mid b^2,$ which means that $2 \mid b.$*

*Combining the results $2 \mid a$ and $2 \mid b,$ we conclude that $\gcd(a,b) \geq 2.$ But this contradicts the assumption that $\gcd(a,b) = 1.$*

*Therefore, $\sqrt{2}$ is irrational.*

### Example: Template: Proving the Irrationality of a Radical

#### Question

Suppose we wish to construct a proof by contradiction of the following statement:

$\sqrt{11}$ is irrational.

What are the missing entries in the proof template below?

Assume for a contradiction that $\sqrt{11}$ $\:\boxed{\phantom{XX}}\:$ rational.

Then, we have that

$$


\sqrt{11} = \boxed{\phantom{\dfrac{a}{b}\dfrac{a}{b}}}


$$

for some non-zero integers $a$ and $b,$ where $\gcd(a,b) = \boxed{\phantom{X}}.$

By squaring the above equation and applying some divisibility properties, we can show that $\textrm{gcd}(a,b) > 1.$

But this is a $\:\boxed{\phantom{contradiction}}\:$ since $\:\boxed{\phantom{contradiction}}\:$ by assumption.

Therefore, we conclude that $\sqrt{11}$ $\:\boxed{\phantom{XX}}\:$ rational.

#### Explanation

Let's write down the formal statement $P$ that we wish to prove:

$P: \quad \sqrt{11}$ is irrational

To prove that $P$ is true, we assume that $\lnot P$ is true and show this leads to a contradiction.

$\lnot P: \quad \sqrt{11}$ is rational

Since we're assuming $\sqrt{11}$ is rational, we can express it as the ratio of two integers.

Assume for a contradiction that $\sqrt{11}$ $\boxed{\color{blue}\textrm{is}}$ rational.

Then, we have that

$$


\sqrt{11} = \boxed{\color{blue}\dfrac{a}{b}}


$$

for some non-zero integers $a$ and $b,$ where $\gcd(a,b) = \boxed{\color{blue}1}.$

The idea is to remove the radical by squaring the equation. Then, we apply some divisibility arguments to show that $\textrm{gcd}(a,b) > 1.$

By squaring the above equation and applying some divisibility properties, we can show that $\text{gcd}(a,b) > 1.$

This gives us our contradiction.

But this is a $\boxed{\color{blue}\text{contradiction}}$ since $\boxed{\color{blue}\text{gcd}(a,b) = 1}$ by assumption.

Therefore, the assumption that $\lnot P$ is true was incorrect, which means that $P$ is true.

Therefore, we conclude that $\sqrt{11}$ $\boxed{\color{blue}\textrm{is not}}$ rational.

### Example: Proving Irrationality of Roots of Primes

#### Question

Prove by contradiction that $\sqrt[3]{5}$ is irrational.

#### Explanation

Let's write down the formal statement $P$ that we wish to prove:

$P: \quad \sqrt[3]{5}$ is irrational

To prove that $P$ is true, we assume that $\lnot P$ is true and show this leads to a contradiction.

$\lnot P: \quad \sqrt[3]{5}$ is rational

We begin our proof as follows:

Assume, for a contradiction, that $\sqrt[3]{5}$ is rational.

If a number is rational, it can be written as a fraction in its lowest terms, i.e., where the numerator and denominator are coprime.

Then,

$$


\sqrt[3]{5} = \dfrac{a}{b}


$$

for some non-zero integers $a$ and $b,$ where $\gcd(a,b) = 1.$

The idea is to cube both sides of the equation to find a factor of $a$ and a factor of $b.$

This implies that

$$


\begin{aligned}\sqrt[√5]{3} & =\frac{𝑎}{𝑏} \\ (\sqrt[√5]{3})^{3} & =(\frac{𝑎}{𝑏})^{3} \\ 5 & =\frac{𝑎^{3}}{𝑏^{3}} \\ 5𝑏^{3} & =𝑎^{3},\end{aligned}


$$

which means that $5 \mid a^3.$

Now, recall the following property of divisibility by a prime $p{:}$

$$


p \mid xyz \quad\Rightarrow\quad (p \mid x) \lor (p \mid y) \lor (p \mid z)


$$

Applying this property with $p = 5$ and $x = y = z = a,$ we have

$$


5 \mid a^3 \quad\Leftrightarrow\quad 5 \mid a \cdot a \cdot a \quad\Rightarrow\quad (5 \mid a) \lor (5 \mid a) \lor (5 \mid a).


$$

So, we have that $5 \mid a.$

Since $5$ is prime, we have $5 \mid a,$ which means $a = 5c$ where $c$ is an integer.

Now, we substitute $a = 5c$ into the equation $5b^3 = a^3$ and show that $5$ is also a factor of $b.$

Therefore, we have that

$$


\begin{aligned}5𝑏^{3} & =(5𝑐)^{3} \\ 5𝑏^{3} & =125𝑐^{3} \\ 𝑏^{3} & =25𝑐^{3} \\ 𝑏^{3} & =5⋅5𝑐^{3}.\end{aligned}


$$

Hence, by the definition of divisibility, $5 \mid b^3,$ which means that $5 \mid b.$

Finally, since $a$ and $b$ have a common factor of $5,$ their greatest common divisor is at least $5.$ This gives us our contradiction.

Combining the results $5 \mid a$ and $5 \mid b,$ we conclude that $\gcd(a,b) \geq 5.$ But this contradicts the assumption that $\gcd(a,b) = 1.$

Since we have a contradiction, our original assumption must be incorrect. Hence, we write our conclusion as follows:

Therefore, $\sqrt[3]{5}$ is irrational.

### Example: Proving Irrationality of Roots of Composite Numbers

#### Question

Prove by contradiction that $\sqrt[3]{15}$ is irrational.

**

$$


p \mid a^n \Rightarrow p \mid a


$$

**

#### Explanation

Let's write down the formal statement $P$ that we wish to prove:

$P: \quad \sqrt[3]{15}$ is irrational

To prove that $P$ is true, we assume that $\lnot P$ is true and show this leads to a contradiction.

$\lnot P: \quad \sqrt[3]{15}$ is rational

We begin our proof as follows:

Assume, for a contradiction, that $\sqrt[3]{15}$ is rational.

If a number is rational, it can be written as a fraction in its lowest terms, i.e., where the numerator and denominator are coprime.

Then,

$$


\sqrt[3]{15} = \dfrac{a}{b}


$$

for some non-zero integers $a$ and $b,$ where $\gcd(a,b) = 1.$

The idea is to cube both sides of the equation to find a factor of $a$ and a factor of $b.$

This implies that

$$


\begin{aligned}\sqrt[√15]{3} & =\frac{𝑎}{𝑏} \\ (\sqrt[√15]{3})^{3} & =(\frac{𝑎}{𝑏})^{3} \\ 15 & =\frac{𝑎^{3}}{𝑏^{3}} \\ 15𝑏^{3} & =𝑎^{3},\end{aligned}


$$

which means that $15 \mid a^3.$

We need to show that $15\mid a.$

Let's use this to show that $15\mid a.$

To do this, recall the following divisibility properties:

- Transitivity of divisibility:

- Divisibility of a power by a prime:

- Divisibility by a product:

Notice that $15=3\cdot 5$ is the product of two primes, which suggests we may want to use the third property.

Also, if $15$ divides $a^3,$ then $3$ and $5$ must divide $a^3$ by the first property.

We start by using the first property:

First, note that $15 = 3\cdot 5.$ By the transitivity of divisibility,

$$


\begin{aligned}(3∣15)∧(15∣𝑎^{3})\,⇒\,3∣𝑎^{3}.\end{aligned}


$$

Now, we use the second property:

Since $3$ is prime, this means that $3 \mid a.$

The argument to show that $5\mid a$ is identical, so we simply state that.

We also have $5 \mid a$ by a similar argument.

Since $3$ and $5$ are coprime, we can show that $15\mid a$ by the third property.

Since $3\mid a$ and $5\mid a,$ and $\textrm{gcd(3,5)} =1,$ we have that $15\mid a$ which means that $a=15c$ for some integer $c.$

Now, we substitute $a=15c$ into the equation $15b^3 = a^3$ and show that $15$ is also a factor of $b.$

Therefore, we have that

$$


\begin{aligned}15𝑏^{3} & =(15𝑐)^{3} \\ 15𝑏^{3} & =3,375𝑐^{3} \\ 𝑏^{3} & =225𝑐^{3}.\end{aligned}


$$

Then, we use the first property again:

Hence, by the definition of divisibility, $225 \mid b^3.$ By the transitivity of divisibility,

$$


\begin{aligned}(15∣225)∧(225∣𝑏^{3})\,⇒\,15∣𝑏^{3},\end{aligned}


$$

which means that $15 \mid b.$

Finally, since $a$ and $b$ have a common factor of $15,$ their greatest common divisor is at least $15.$ This gives us our contradiction.

Combining the results $15 \mid a$ and $15 \mid b,$ we conclude that $\gcd(a,b) \geq 15.$ But this contradicts the assumption that $\gcd(a,b) = 1.$

Since we have a contradiction, our original assumption must be incorrect. Hence, we write our conclusion as follows:

Therefore, $\sqrt[3]{15}$ is irrational.
