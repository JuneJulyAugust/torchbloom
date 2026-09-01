# Properties of Roots of Unity

Source: https://www.mathacademy.com/topics/4050?courseId=43
Topic ID: 4050

## Prerequisites

- [The Sum of a Finite Geometric Series](./1016-the-sum-of-a-finite-geometric-series.md)
- [The Power of Product Rule for Exponents](../../../../middle-school/lessons/grade-8/2012-the-power-of-product-rule-for-exponents.md)
- [The Roots of Unity](./3400-the-roots-of-unity.md)

## Lesson

### Introduction

Recall that the $n$th roots of unity are the solutions to the equation

$$



z^n = 1.



$$

In general, the $n$th roots of unity can be expressed as

$$



z_k = e^{2\pi k\textrm i /n }, \qquad k=0,1,2,\ldots,n-1.



$$

Also, recall that the root corresponding to $k=1$ is the *principal $n$th root of unity.*

We have the following theorem:

*Any $n$th root of unity is an integer power of the principal $n$th root.*

Let's see an example.

### Example: Expressing a Root of Unity Using Its Principal Root

#### Question

The $12$th root of unity $e^{2\pi \text{i}/3}$ can be written as

$$



e^{2\pi \text{i}/3} = z^p,



$$

where $z$ is the principal $12$th root of unity. What is the value of $p?$

#### Explanation

Recall that the $12$th roots of unity can be written in the form

$$



e^{2 k\pi \text{i} / 12}



$$

where $k=0,1,\ldots,11.$

We obtain the ** $12$th root of unity by substituting $k=1{:}$

$$



z= e^{2 \cdot 1 \cdot \pi \text{i} / 12} = {\color{blue}e^{\pi \text{i} / 6}}



$$

We can write the given root of unity as a power of the principal root as follows:

$$



\begin{aligned}𝑒^{2𝜋i/3} & =𝑒^{(2⋅2𝜋)i/(2⋅3)} \\ & =𝑒^{4𝜋i/6} \\ & =𝑒^{4⋅𝜋i/6} \\ & =(𝑒^{𝜋i/6})^{4}\end{aligned}



$$

Therefore, $p={\color{red}4}.$

### Product and Quotient Properties

The th roots of unity have other interesting properties, which we list below, along with a proof of each result.

When proving the results, assume that and are th roots of unity, and therefore

- *A product of two th roots of unity is an th root of unity.* To prove this, note that which means that is also an th root of unity.

- *The reciprocal of an th root of unity is an th root of unity.* To prove this, note that which means that is an th root of unity too.

- *The quotient of two th roots of unity is an th root of unity.* To prove this, note that which means that is an th root of unity.

- *Any integer power of an th root of unity is an th root of unity.* To prove this, note that which means that is an th root of unity.

### Example: Identifying True Statements Regarding Product and Quotient Properties

#### Question

Let $z$ be a $7$th root of unity. Which of the following statements are true?

1. $z^7 = 1$

2. $(z+z)^7 = 1$

3. $z+z=2z$ is a $7$th root of unity

#### Explanation

Let's examine our statements in turn.

- Statement I is true. If $z$ is a $7$th root of unity, then (by definition), we have that

- Statement II is false. We have

- Statement III is false. From statement II, we have that $(z+z)^7 \neq 1,$ which means that $z+z=2z$ is ** a $7$th root of unity. In general, the sum of two $n$th roots of unity is ** an $n$th root of unity.

Therefore, the correct answer is "I only."

### Sums of Roots of Unity

The sum of all $n$th roots of unity equals zero.

To see why, recall that

- the principal $n$th root of unity is $z=e^{2\pi\text{i}/n}\neq1,$ and

- any $n$th root of unity is of the form $z^k$ for $k=0,1,...,n-1.$

So, the sum of all $n$ roots can be calculated as the sum of the following geometric series:

$$



\begin{aligned}1+𝑧+𝑧^{2}+⋯+𝑧^{𝑛−1} & =\frac{1−𝑧^{𝑛}}{1−𝑧} \\ & =\frac{1−1}{1−𝑧} \\ & =0.\end{aligned}



$$

### Products of Roots of Unity

The product of all $n$th roots of unity equals $1$ if $n$ is odd and equals $-1$ if $n$ is even.

As an example, the principal fourth root of unity is

$$



z=e^{2\pi\text{i}/4}=e^{\pi\text{i}/2}.



$$

Any fourth root of unity is of the form $z^k$ for $k=0,1,2,3.$ Also, we have $z^4=1.$

Therefore, the product of all four roots of unity is

$$



\begin{aligned}𝑧^{0}⋅𝑧^{1}⋅𝑧^{2}⋅𝑧^{3} & =𝑧^{0\,+\,1\,+2\,+3} \\ & =𝑧^{6} \\ & =𝑧^{4}⋅𝑧^{2} \\ & =1⋅(𝑒^{𝜋i/2})^{2} \\ & =𝑒^{𝜋i} \\ & =−1.\end{aligned}



$$

Let's see an example of this multiplicative property for odd powers.

### Example: Identifying True Statements Regarding Sums and Products

#### Question

Find the product of all three cube roots of unity.

#### Explanation

Recall that the principal cube root of unity is

$$



z=e^{2\pi\text{i}/3},



$$

and that any cube root of unity is of the form $z^k$ for $k=0,1,2.$ Also, we have $z^3=1.$

Therefore, the product of all three roots is

$$



\begin{aligned}𝑧^{0}⋅𝑧^{1}⋅𝑧^{2} & =𝑧^{0\,+\,1\,+\,2} \\ & =𝑧^{3} \\ & =1.\end{aligned}



$$
