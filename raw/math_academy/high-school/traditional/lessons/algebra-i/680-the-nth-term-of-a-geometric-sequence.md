# The Nth Term of a Geometric Sequence

Source: https://www.mathacademy.com/topics/680?courseId=44
Topic ID: 680

## Prerequisites

- [The Product Rule for Exponents](../../../../middle-school/lessons/prealgebra/267-the-product-rule-for-exponents.md)
- [The Recursive Formula for a Geometric Sequence](./1818-the-recursive-formula-for-a-geometric-sequence.md)

## Lesson

### Introduction

The general formula for the $n$th term of a geometric sequence is

$$


a_n = a_1 \cdot r^{n-1},


$$

where $a_1$ is the first term and $r$ is the common ratio.

To illustrate how this works, suppose we want to find the $10$th term of the following geometric sequence:

$$


3, \: 6, \: 12, \: \ldots


$$

The first term is $a_1=3,$ and the common ratio is $r=2,$ so we can write the formula for the $n$th term of the sequence:

$$


\begin{aligned}𝑎_{𝑛} & =𝑎_{1}⋅𝑟^{𝑛−1} \\ & =3⋅2^{𝑛−1}\end{aligned}


$$

To find the $10$th term, we can use this formula with $n={\color{blue}10}\mathbin{:}$

$$


\begin{aligned}𝑎_{𝑛} & =3⋅2^{𝑛−1} \\ 𝑎_{10} & =3⋅2^{10−1} \\ & =3⋅2^{9} \\ & =3⋅512 \\ & =1\,536\end{aligned}


$$

Therefore, the $10$th term is $a_{10}=1\,536.$ Using the formula was much quicker than writing out all $10$ terms of the sequence!

### Example: Finding a Particular Term of a Geometric Sequence Given the First Term and Common Ratio

#### Question

The first term of a geometric sequence is $2$, and the common ratio is $3.$ What is the $9$th term?

#### Explanation

The first term is $a_1=2,$ and the common ratio is $r=3,$ so we can write the formula for the $n$th term of the sequence:

$$


\begin{aligned}𝑎_{𝑛} & =𝑎_{1}⋅𝑟^{𝑛−1} \\ & =2⋅3^{𝑛−1}\end{aligned}


$$

To find the $9$th term, we can use this formula with $n={\color{blue}9}\mathbin{:}$

$$


\begin{aligned}𝑎_{𝑛} & =2⋅3^{𝑛−1} \\ 𝑎_{9} & =2⋅3^{9−1} \\ & =2⋅3^{8} \\ & =2⋅6561 \\ & =13\,122\end{aligned}


$$

Therefore, the $9$th term is $a_{9}=13\,122.$

### Example: Finding a Formula for the Nth Term of a Geometric Sequence

#### Question

Find the formula for the $n$th term of a sequence if the $6$th term is $80$ and the common ratio is $-2.$

#### Explanation

The common ratio is $r=-2,$ so we can start writing the formula for the $n$th term of the sequence:

$$


\begin{aligned}𝑎_{𝑛} & =𝑎_{1}⋅𝑟^{𝑛−1} \\ & =𝑎_{1}⋅(−2)^{𝑛−1}\end{aligned}


$$

However, we still need to figure out the first term $a_1.$ We know that the $6$th term is $a_6=80,$ so we can solve for the first term as follows:

$$


\begin{aligned}𝑎_{6} & =𝑎_{1}⋅(−2)^{6−1} \\ 80 & =𝑎_{1}⋅(−2)^{5} \\ 80 & =𝑎_{1}⋅(−32) \\ −\frac{80}{32} & =𝑎_{1} \\ −\frac{5}{2} & =𝑎_{1}\end{aligned}


$$

Now that we know the first term is $a_1=-\dfrac{5}{2},$ we can complete the formula for the $n$th term of the sequence:

$$


\begin{aligned}𝑎_{𝑛} & =𝑎_{1}⋅(−2)^{𝑛−1} \\ & =−\frac{5}{2}⋅(−2)^{𝑛−1}\end{aligned}


$$

We can simplify a bit further by manipulating the exponents, as follows:

$$


\begin{aligned}𝑎_{𝑛} & =−\frac{5}{2}(−2)^{𝑛−1} \\ & =5⋅(−\frac{1}{2})⋅(−2)^{𝑛−1} \\ & =5⋅(−2)^{−1}⋅(−2)^{𝑛−1} \\ & =5⋅(−2)^{𝑛−2}\end{aligned}


$$

### Example: Finding a Particular Term of a Geometric Sequence Given a Term and the Common Ratio

#### Question

Given that the $5$th term of a geometric sequence is $9$, and the common ratio is $3,$ find the second term.

#### Explanation

The common ratio is $r=3,$ so we can start writing the formula for the $n$th term of the sequence:

$$


\begin{aligned}𝑎_{𝑛} & =𝑎_{1}⋅𝑟^{𝑛−1} \\ & =𝑎_{1}⋅3^{𝑛−1}\end{aligned}


$$

However, we still need to figure out the first term $a_1.$ We know that the $5$th term is $a_5=9,$ so we can solve for the first term as follows:

$$


\begin{aligned}𝑎_{5} & =𝑎_{1}⋅3^{5−1} \\ 9 & =𝑎_{1}⋅3^{4} \\ 9 & =𝑎_{1}⋅81 \\ \frac{9}{81} & =𝑎_{1} \\ \frac{1}{9} & =𝑎_{1}\end{aligned}


$$

Now that we know the first term is $a_1=\dfrac{1}{9},$ we can complete the formula for the $n$th term of the sequence:

$$


\begin{aligned}𝑎_{𝑛} & =𝑎_{1}⋅3^{𝑛−1} \\ & =\frac{1}{9}⋅3^{𝑛−1}\end{aligned}


$$

Then, we can use this formula to compute the second term:

$$


\begin{aligned}𝑎_{2} & =\frac{1}{9}⋅3^{2−1} \\ & =\frac{1}{9}⋅3 \\ & =\frac{1}{3}\end{aligned}


$$

Therefore, the second term is $a_2 = \dfrac{1}{3}.$
