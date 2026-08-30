# Fermat's Little Theorem

Source: https://www.mathacademy.com/topics/2726?courseId=109
Topic ID: 2726

## Prerequisites

- [The Division Properties of Modular Arithmetic](../methods-of-proof/2675-the-division-properties-of-modular-arithmetic.md)

## Lesson

### Introduction

**Fermat's little theorem** states the following:

*If $p$ is a prime number, then $a^{p} \equiv a \: (\text{mod}\:p)$ for any integer $a$.*

We also have the following special case of the theorem:

*$a^{p-1} \equiv 1 \: (\text{mod}\:p)$ for any prime $p$ and any integer $a$ that is coprime with $p,$ i.e. $\text{gcd}(a,p)=1.$*

Fermat's little theorem is useful because it allows us to quickly compute powers of integers modulo a prime number $p.$

For example, let's compute $5^{32} \: \text{mod} \: 7$ using the special case of Fermat's little theorem. First, notice that since $7$ is prime and $\text{gcd}(5,7)=1,$ we can indeed apply the theorem. So, we get

$$



5^{7-1} \equiv {\color{blue}5^{6}} \equiv {\color{blue}1} \quad (\text{mod}\:7) .



$$

So, to compute $5^{32} \: \text{mod} \: 7,$ we rewrite the exponent $32$ and then manipulate it using the laws of exponents, as follows:

$$



\begin{aligned}5^{32} & ≡5^{6⋅5+2} & & (mod\,7) \\ & ≡(5^{6})^{5}⋅5^{2} & & (mod\,7) \\ & ≡(1)^{5}⋅25 & & (mod\,7) \\ & ≡1⋅25 & & (mod\,7) \\ & ≡25 & & (mod\,7) \\ & ≡4 & & (mod\,7)\end{aligned}



$$

**Note:** A justification of the special case of Fermat's little theorem will be given at the end of this lesson. But first, let's get some practice using Fermat's little theorem and its special case.

### Example: Identifying When Fermat's Little Theorem Is Applicable

#### Question

Which of the following statements are true according to Fermat's little theorem?

1. $3^{22} \equiv 1 \: (\text{mod}\:23)$

2. $4^{17} \equiv 1 \: (\text{mod}\:17)$

3. $7^{14} \equiv 7 \: (\text{mod}\:15)$

#### Explanation

Fermat's little theorem states the following:

$a^{p} \equiv a \: (\text{mod}\:p)$ for any prime $p$ and any integer $a.$

Additionally, Fermat's little theorem has the following special case:

$a^{p-1} \equiv 1 \: (\text{mod}\:p)$ for any prime $p$ and any integer $a$ that is coprime with $p.$

With that in mind, let's examine each of the given statements.

- Statement I is true. Indeed, $23$ is prime, and $\text{gcd}(3,23)=1.$ So, according to the special case of Fermat's little theorem, we have

- Statement II false. $17$ is prime, and $\text{gcd}(4,17)=1$. So, according to Fermat's little theorem, we have

- Statement III is false. The modulus $15$ is ** prime. So, Fermat's little theorem can't be applied.

Therefore, the correct answer is "I only."

### Example: Computing Modular Residues of Single Exponents Using Fermat's Little Theorem

#### Question

Calculate the value of $4^{80} \: \text{mod} \: 7.$

#### Explanation

The special case of Fermat's little theorem states the following:

$a^{p-1} \equiv 1 \: (\text{mod}\:p)$ for any prime $p$ and any integer $a$ that is coprime with $p.$

First, notice that $7$ is prime and $\text{gcd}(4,7)=1.$ So, we can apply the special case of Fermat's little theorem:

$$



4^{7-1} \equiv {\color{blue}4^{6}} \equiv {\color{blue}1} \quad (\text{mod}\:7)



$$

Now, re-writing the given exponent, we obtain the following:

$$



\begin{aligned}4^{80} & ≡4^{13⋅6+2} & & (mod\,7) \\ & ≡(4^{6})^{13}⋅4^{2} & & (mod\,7) \\ & ≡(1)^{13}⋅16 & & (mod\,7) \\ & ≡2 & & (mod\,7)\end{aligned}



$$

### Example: Computing Modular Residues of Nested Exponents Using Fermat's Little Theorem

#### Question

Calculate the value of $4^{\large 7^{100}} \: \text{mod} \: 13?$

#### Explanation

The special case of Fermat's little theorem states the following:

$a^{p-1} \equiv 1 \: (\text{mod}\:p)$ for any prime $p$ and any integer $a$ that is coprime with $p.$

First, notice that $13$ is prime and $\text{gcd}(4,13)=1.$ So, we can apply the special case of Fermat's little theorem:

$$



4^{13-1} \equiv 4^{\color{blue}12} \equiv 1 \quad (\text{mod}\:13)



$$

Let's now find $7^{100}$ modulo ${\color{blue}12}.$ Notice that

$$



\begin{aligned}7^{1} & ≡7 & & (mod\,12) \\ 7^{2} & ≡1 & & (mod\,12) \\ 7^{3} & ≡7 & & (mod\,12) \\ 7^{4} & ≡1 & & (mod\,12) \\ \,⋮ & & & \end{aligned}



$$

This pattern will continue. So, $7$ to the power of any even integer (like $100$) will give us $1$ modulo $12,$ and we can write

$$



7^{100} = 12k+1



$$

for some integer $k.$

Now, re-writing the given exponent, we obtain the following:

$$



\begin{aligned}4^{7^{100}} & ≡4^{12𝑘+1} & & (mod\,13) \\ & ≡(4^{12})^{𝑘}⋅4^{1} & & (mod\,13) \\ & ≡(1)^{𝑘}⋅4 & & (mod\,13) \\ & ≡4 & & (mod\,13)\end{aligned}



$$

### A Justification of the Special Case

Recall the special case of Fermat's little theorem:

$a^{p-1} \equiv 1 \: (\text{mod}\:p)$ for any prime $p$ and any integer $a$ that is coprime with $p.$

Let's justify its validity by considering the case of $5^6 \: \text{mod} \: 7.$

First, let's consider the set $\mathbb Z_7^*= \{1,2,3,4,5,6\}.$ Notice that by multiplying each element of $\mathbb Z_7^*$ by $a = 5$ we get

$$



\{5\cdot 1,\, 5\cdot 2,\, 5\cdot 3,\, 5\cdot 4,\, 5\cdot 5,\, 5\cdot 6\} = \{5, 3,1,6, 4, 2 \}= \mathbb Z_7^* \quad (\text{mod}\:7).



$$

So, we obtained $\mathbb Z_7^*$ once again. Now, let's multiply each of the elements in both lists together and equate them.

$$



\begin{aligned}(5⋅1)⋅(5⋅2)⋅(5⋅3)⋅(5⋅4)⋅(5⋅5)⋅(5⋅6) & ≡5⋅3⋅1⋅6⋅4⋅2 & & (mod\,7) \\ 5^{6}⋅(1⋅2⋅3⋅4⋅5⋅6) & ≡(1⋅2⋅3⋅4⋅5⋅6) & & (mod\,7) \\ 5^{6}⋅(1⋅2⋅3⋅4⋅5⋅6) & ≡(1⋅2⋅3⋅4⋅5⋅6) & & (mod\,7) \\ 5^{6} & ≡1 & & (mod\,7)\end{aligned}



$$

So, we have managed to show that $5^6 \equiv 1\,(\text{mod}\, 7).$ Note that we used the division property of modular arithmetic to cancel the large factor from both sides of the congruence.

Note the following:

- It shouldn't be too difficult to convince yourself that the same trick will work for any prime $p$ and any integer $a$ that is coprime with $p.$

- The trick of multiplying $\mathbb Z^*_p$ by $a$ to permute the elements of $\mathbb Z_p^*$ will only work if $p$ is prime and $a$ is coprime with $p.$ As a counterexample, suppose that $p=4$ and $a=2$. Then $\mathrm{gcd}(2,4)=2>1$ and we have $\mathbb{Z}_4^*= \{1,2,3\},$ but

### Deriving the General Form Using the Special Case

Finally, using the special case of Fermat's little theorem, let's prove the following result:

$a^{p} \equiv a \: (\text{mod}\:p)$ for any prime $p$ and any integer $a.$

We have two cases:

- If $p$ divides $a$ then both sides are congruent to zero, so the result holds true.

- If $p$ doesn't divide $a,$ then $a$ is coprime with $p,$ which means we can use the special case: Multiplying both sides of the congruence above, we reach the desired result:
