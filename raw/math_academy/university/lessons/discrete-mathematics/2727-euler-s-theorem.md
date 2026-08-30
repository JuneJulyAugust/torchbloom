# Euler's Theorem

Source: https://www.mathacademy.com/topics/2727?courseId=109
Topic ID: 2727

## Prerequisites

- [Euler's Totient Function](./2654-euler-s-totient-function.md)
- [Fermat's Little Theorem](./2726-fermat-s-little-theorem.md)

## Lesson

### Introduction

If $a$ and $n$ are coprime, then **Euler's theorem** states that

$$



a^{\phi(n)} \equiv 1 \quad (\text{mod}\:n),



$$

where $\phi$ is Euler's totient function (which returns the number of positive integers that are less than $n$ and are coprime to $n$).

Using Euler's theorem, we can reduce a calculation containing large exponents to one containing smaller exponents. For example, suppose that we want to compute the following:

$$



2^{91} \: \text{mod} \: 15



$$

First, notice that $\text{gcd}(2,15)=1$ and

$$



\begin{aligned}𝜙(15) & =𝜙(3)⋅𝜙(5) \\ & =(3−1)⋅(5−1) \\ & =8.\end{aligned}



$$

So, we can apply Euler's theorem, which gives

$$



2^{\phi(15)} \equiv {\color{blue}2^{8}} \equiv {\color{blue}1} \quad (\text{mod}\:15)\,.



$$

Now, rewriting the given exponent, we obtain the following:

$$



\begin{aligned}2^{91} & ≡2^{8⋅11+3} & & (mod\,15) \\ & ≡(2^{8})^{11}⋅2^{3} & & (mod\,15) \\ & ≡(1)^{11}⋅8 & & (mod\,15) \\ & ≡8 & & (mod\,15)\end{aligned}



$$

### Example: Identifying When Euler's Theorem Is Applicable

#### Question

Consider the following congruence, which is either true or false:

$$



5^{24} \equiv 1 \quad (\text{mod}\:39)



$$

Which of the following statements are true?

1. $\text{gcd}(5,39)=1$

2. $\phi(39) = 24$

3. The congruence is true by Euler's theorem

#### Explanation

Euler's theorem states that if $a$ and $n$ are coprime, then

$$



a^{\phi(n)} \equiv 1 \quad (\text{mod}\:n),



$$

where $\phi$ is Euler's totient function.

With that in mind, let's examine each of the given statements.

- Statement I is true. Indeed, $\text{gcd}(5,39)=1.$

- Statement II is true. First, notice that where $3$ and $13$ are distinct prime numbers. As a result,

- Statement III is true. By Euler's theorem, we get the following:

Therefore, the correct answer is "I, II, and III."

### Example: Computing Modular Residues of Single Exponents Using Euler's Theorem

#### Question

Evaluate $7^{122} \: \text{mod} \: 33.$

#### Explanation

Euler's theorem states that if $a$ and $n$ are coprime, then

$$



a^{\phi(n)} \equiv 1 \quad (\text{mod}\:n),



$$

where $\phi$ is Euler's totient function.

First, notice that $\text{gcd}(7,33)=1$ and

$$



\begin{aligned}𝜙(33) & =𝜙(3)⋅𝜙(11) \\ & =(3−1)⋅(11−1) \\ & =20.\end{aligned}



$$

So, we can apply Euler's theorem:

$$



7^{\phi(33)} \equiv {\color{blue}7^{20}} \equiv {\color{blue}1} \quad (\text{mod}\:33)



$$

Now, rewriting the given exponent, we obtain the following:

$$



\begin{aligned}7^{122} & ≡7^{20⋅6+2} & & (mod\,33) \\ & ≡(7^{20})^{6}⋅7^{2} & & (mod\,33) \\ & ≡(1)^{6}⋅49 & & (mod\,33) \\ & ≡16 & & (mod\,33)\end{aligned}



$$

### Example: Computing Modular Residues of Nested Exponents Using Euler's Theorem

#### Question

Evaluate $4^{\large 5^{220}} \: \text{mod} \: 21.$

#### Explanation

Euler's theorem states that if $a$ and $n$ are coprime, then

$$



a^{\phi(n)} \equiv 1 \quad (\text{mod}\:n),



$$

where $\phi$ is Euler's totient function.

First, notice that $\text{gcd}(4,21)=1$ and

$$



\begin{aligned}𝜙(21) & =𝜙(3)⋅𝜙(7) \\ & =(3−1)⋅(7−1) \\ & =12.\end{aligned}



$$

So, we can apply Euler's theorem:

$$



4^{\phi(21)} \equiv 4^{\color{blue}12} \equiv 1 \quad (\text{mod}\:21)



$$

Let's now find $5^{220}$ modulo ${\color{blue}12}.$ First, notice that $\text{gcd}(5,12)=1$ and

$$



\begin{aligned}𝜙(12) & =𝜙(2^{2})⋅𝜙(3) \\ & =(4−2)⋅(3−1) \\ & =4.\end{aligned}



$$

So, we can apply Euler's theorem:

$$



5^{\phi(12)} \equiv 5^{\color{red}4} \equiv 1 \quad (\text{mod}\:12)



$$

Now, re-writing $5^{220},$ we obtain the following:

$$



\begin{aligned}5^{220} & ≡5^{4⋅55} & & (mod\,12) \\ & ≡(5^{4})^{55} & & (mod\,12) \\ & ≡1 & & (mod\,12)\end{aligned}



$$

This means that

$$



5^{220} = 12k + 1



$$

for some integer $k.$

Finally, re-writing the given exponent, we obtain the following:

$$



\begin{aligned}4^{5^{220}} & ≡4^{12𝑘+1} & & (mod\,21) \\ & ≡(4^{12})^{𝑘}⋅4^{1} & & (mod\,21) \\ & ≡(1)^{𝑘}⋅4 & & (mod\,21) \\ & ≡4 & & (mod\,21)\end{aligned}



$$
