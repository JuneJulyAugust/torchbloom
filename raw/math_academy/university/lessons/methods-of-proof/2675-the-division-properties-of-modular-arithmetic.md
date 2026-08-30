# The Division Properties of Modular Arithmetic

Source: https://www.mathacademy.com/topics/2675?courseId=76
Topic ID: 2675

## Prerequisites

- [The Multiplication Properties of Modular Arithmetic](./2674-the-multiplication-properties-of-modular-arithmetic.md)
- [The Euclidean Algorithm](./2676-the-euclidean-algorithm.md)

## Lesson

### Introduction

In a previous lesson, we saw that congruences obey the following scalar multiplication property:

$$


a\equiv b \qquad (\text{mod}\,n) \quad \Longrightarrow\quad ka \equiv kb \qquad (\text{mod}\,kn)


$$

It turns out that for $k\neq 0,$ we can perform this operation in reverse. That is,

$$


ka \equiv kb \quad(\text{mod}\,kn) \qquad \Longrightarrow \qquad a \equiv b \quad(\text{mod}\,n).


$$

Therefore, for $k\neq 0,$ we have the following **division property,** which we can write as an equivalence:

$$


ka \equiv kb \quad(\text{mod}\,kn) \qquad \Longleftrightarrow \qquad a \equiv b \quad(\text{mod}\,n).


$$

For example, consider the following true statement:

$$


12 \equiv 6 \quad (\text{mod}\:6)


$$

Note that all three numbers in our congruence have a common factor of ${\color{blue}3}.$

$$


{\color{blue}3} \cdot 4 \equiv {\color{blue}3} \cdot 2 \quad (\text{mod}\:{\color{blue}3} \cdot 2)


$$

Therefore, by the division property, we can cancel a factor of ${\color{blue}3}$ from both sides and the modulus.

$$


\begin{aligned}3⋅4≡3⋅2\, & (mod\,3⋅2) \\ 4≡2\, & (mod\,2)\end{aligned}


$$

It's important to note that the division property does not hold if $k=0.$ For example, consider the following counterexample.

$$


0\cdot 2 \equiv 0\cdot 1 \qquad \Longrightarrow\qquad 2\equiv 1 \qquad (\text{mod}\,2)


$$

The antecedent is true, the consequent is false, and hence the implication is *false*.

### Example: Using the First Division Property

#### Question

Given that $4a \equiv 4b \,(\text{mod}\,8),$ which of the following statements **** be true?

1. $a \equiv b \quad(\text{mod}\,4)$

2. $a \equiv b \quad(\text{mod}\,2)$

3. $a \equiv b \quad(\text{mod}\,8)$

#### Explanation

The division property of modular arithmetic states that for $k\neq 0,$ we have

$$


ka\equiv kb\quad(\text{mod} \,kn) \qquad \Longleftrightarrow\qquad a \equiv b \quad(\text{mod}\, n).


$$

We're asked to consider the following statement:

$$


4a \equiv 4b \quad(\text{mod}\,8)


$$

Notice that $\text{gcd}(4,8) =4.$

Applying the division property, we have the following:

$$


\begin{aligned}4𝑎 & ≡4𝑏 & & (mod\,8) \\ 4⋅𝑎 & ≡4⋅𝑏 & & (mod\,4⋅2) \\ 4⋅𝑎 & ≡4⋅𝑏 & & (mod\,4⋅2) \\ 𝑎 & ≡𝑏 & & (mod\,2)\end{aligned}


$$

Therefore, the correct answer is "II only".

### The Second Division Property

In a previous lesson, we saw that congruences obey another scalar multiplication property:

$$


a\equiv b \qquad (\text{mod}\,n) \quad \Longrightarrow\quad ka \equiv kb \qquad (\text{mod}\,n)


$$

The (second) **division property** of modular arithmetic tells us that

$$


ka\equiv kb\quad(\text{mod} \,n) \qquad \Longleftrightarrow\qquad a \equiv b \quad(\text{mod}\, n)


$$

*provided that $k$ and $n$ are coprime*. In other words, we require $\text{gcd}(k,n)=1.$

**Caution:** The condition that $k$ and $n$ are coprime is *very* important! The division property does *not* work when $k$ and $n$ are not coprime!

This might seem a little puzzling, so let's look at some concrete examples:

- Consider the following true statement: Notice that the two numbers in our congruence have a common factor of ${\color{blue}2}{:}$ Since $\text{gcd}({\color{blue}2},5)=1,$ we can cancel out ${\color{blue}2}$ from both sides, keeping the modulus unchanged.

- Next, consider the following true statement: Notice that the two numbers in our congruence, *and the modulus*, have a common factor of ${\color{red}3}{:}$ Because $\text{gcd}({\color{red}3},6) = 3 \neq 1,$ we *cannot* cancel out ${\color{red}3}$ from both sides. If we do, we get the following *false* statement! In such cases, we should use the first division property to simplify the congruence.

### Example: Using the Second Division Property

#### Question

If $ka \equiv kb \: (\text{mod} \,7)$ is equivalent to $\%\qquad\Longrightarrow\qquad a \equiv b \:(\text{mod} \,7),$ which of the following could be the value of $k?$

1. $k=-12$

2. $k=4$

3. $k=-14$

#### Explanation

The division property of modular arithmetic states that

$$


ka\equiv kb\quad(\text{mod} \,n) \qquad \Longleftrightarrow\qquad a \equiv b \quad(\text{mod}\, n)


$$

provided that $k$ and $n$ are coprime. In other words, we require $\text{gcd}(k,n)=1.$

In this case, the modulus $n=7.$ Let's consider each value of $k$ in turn.

- If $k=-12,$ then $\text{gcd}(k,n) = \text{gcd}(-12,7) = 1.$ Therefore, our equivalence is valid for $k=-12.$

- If $k=4,$ then $\text{gcd}(k,n) = \text{gcd}(4,7) = 1.$ Therefore, our equivalence is valid for $k=4.$

- If $k=-14,$ then $\text{gcd}(k,n) = \text{gcd}(-14,7) = 7\neq 1.$ Therefore, our equivalence is ** valid for $k=-14.$

Therefore, the correct answer is "I and II only".

### Example: Combining the Division Properties

#### Question

Given that $15a \equiv 15b \,(\text{mod}\,20),$ which of the following statements **** be true?

1. $a \equiv b \quad (\text{mod}\, 20)$

2. $a \equiv b \quad (\text{mod}\,4)$

3. $7a \equiv 7b \quad (\text{mod}\,4)$

#### Explanation

The division properties of modular arithmetic state the following:

- For $k\neq 0,$ we have

- For $\text{gcd}(k, n) = 1,$ we have

With that in mind, let's consider each statement.

- Statement I is false, while statement II is true. Applying the first property, we have the following: Since $\gcd(3,4)=1,$ by the second property, we have:

- Statement III is true. By statement II and the second property, we have:

Therefore, the correct answer is "II and III only."

### Proving the Division Properties

Let's see why the division properties work.

- The proof of the first property is straightforward:

- To prove the second division property, suppose that $\text{gcd}(k,n)=1$ and ${\color{blue}k}a\equiv {\color{blue}k}b \: (\text{mod} \,n).$ Then, according to the definition of congruent integers, we obtain Since $k$ and $n$ are coprime and $k(a - b)$ is divisible by $n,$ we have that $(a - b)$ must be divisible by $n.$ Now, using the definition again, we get
