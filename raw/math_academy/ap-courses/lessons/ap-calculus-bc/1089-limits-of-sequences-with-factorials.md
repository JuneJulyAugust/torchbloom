# Limits of Sequences With Factorials

Source: https://www.mathacademy.com/topics/1089?courseId=21
Topic ID: 1089

## Prerequisites

- [Limits of Sequences](./1087-limits-of-sequences.md)
- [Factorials in Variable Expressions](../../../high-school/traditional/lessons/geometry/3710-factorials-in-variable-expressions.md)

## Lesson

### Introduction

Sequences involving factorials often occur in advanced math. For that reason, we need to know how to analyze them.

Let's consider the sequence $a_n$ given below.

$$


a_n = \dfrac {n!}{(n + 1)!},\qquad n\geq 1


$$

Does this sequence converge or diverge? If it converges, what is its limit?

To evaluate the limit, note the following:

- The trick is to simplify $a_n$ by writing the *larger* factorial in terms of the smaller one.

- In this case, $(n+1)!$ is the larger factorial, and $n!$ is the smaller.

- So, we need to write $(n+1)!$ in terms of $n!$

Let's remind ourselves of the definition of the factorial function:

$$


{n!} = {\color{blue}{1\cdot 2\cdot 3\cdots (n-1)\cdot n}}


$$

Using the same definition, we can write $(n+1)!$ as

$$


(n+1)! = \underbrace{{\color{blue}{1\cdot 2\cdot 3\cdots (n-1)\cdot n}}}_{n!} \cdot (n+1).


$$

Replacing ${\color{blue}{1\cdot 2\cdot 3\cdots (n-1)\cdot n}}$ with $n!$ in the above expression, we have

$$


(n+1)! = n!\cdot (n+1).


$$

We can now use our expression for $(n+1)!$ in terms of $n!$ to simplify our expression for $a_n,$ as follows:

$$


\begin{aligned}𝑎_{𝑛} & =\frac{𝑛!}{(𝑛+1)!} \\ & =\frac{𝑛!}{𝑛!⋅(𝑛+1)} \\ & =\frac{𝑛!}{𝑛!⋅(𝑛+1)} \\ & =\frac{1}{𝑛+1}\end{aligned}


$$

From here, we see that $a_n\to 0$ as $n\to\infty$ because the numerator is constant, yet the denominator is a linear polynomial. So, we have

$$


\lim\limits_{n \to \infty} a_n = \lim\limits_{n \to \infty} \left(\dfrac{1}{n+1}\right) = 0.


$$

Therefore, we conclude that $a_n$ is convergent, and it converges to $0.$

### Example: Sequences Where N! is the Smallest Factorial

#### Question

Determine whether the sequence

$$


a_n = \dfrac{3(n+2)!}{2n!}, \qquad n \geq 1


$$

converges or diverges. If it converges, find its limit.

#### Explanation

To evaluate the limit, note the following:

- We need to write the larger factorial in terms of the smaller one.

- In this case, $(n+2)!$ is the larger factorial, and $n!$ is the smaller.

- So, we need to write $(n+2)!$ in terms of $n!$

Now, notice the following:

$$


(n+2)! = n! \cdot (n+1) \cdot (n+2)


$$

We use this to cancel the $n!$ that occurs in both the numerator and denominator in our expression for $a_n{:}$

$$


\begin{aligned}𝑎_{𝑛} & =\frac{3(𝑛+2)!}{2𝑛!} \\ & =\frac{3⋅𝑛!⋅(𝑛+1)⋅(𝑛+2)}{2⋅𝑛!} \\ & =\frac{3⋅𝑛!⋅(𝑛+1)⋅(𝑛+2)}{2⋅𝑛!} \\ & =\frac{3}{2}⋅(𝑛+1)⋅(𝑛+2)\end{aligned}


$$

We see that $a_n$ grows without bound as $n \to \infty$ because it's a quadratic polynomial. So, we have that

$$


\lim\limits_{n \to \infty} a_n = \lim\limits_{n \to \infty} \dfrac32 \cdot (n+1) \cdot (n+2) = \infty.


$$

We conclude that the sequence is divergent.

### Example: Sequences Where N! is the Largest Factorial

#### Question

Determine whether the sequence

$$


a_n = \dfrac{(n - 2)!}{n!}, \qquad n \geq 1


$$

converges or diverges. If it converges, find its limit.

#### Explanation

To evaluate the limit, note the following:

- We need to write the larger factorial in terms of the smaller one.

- In this case, $n!$ is the larger factorial, and $(n-2)!$ is the smaller.

- So, we need to write $n!$ in terms of $(n-2)!$

Now, notice the following:

$$


n! = (n-2)! \cdot (n-1)\cdot n


$$

We use this to cancel the $(n-1)!$ that occurs in both the numerator and denominator in our expression for $a_n{:}$

$$


\begin{aligned}𝑎_{𝑛} & =\frac{(𝑛−2)!}{𝑛!} \\ & =\frac{(𝑛−2)!}{(𝑛−2)!⋅(𝑛−1)⋅𝑛} \\ & =\frac{(𝑛−2)!}{(𝑛−2)!⋅(𝑛−1)⋅𝑛} \\ & =\frac{1}{(𝑛−1)⋅𝑛}\end{aligned}


$$

We see that $a_n$ shrinks to zero as $n \to \infty$ because the numerator is constant, yet the denominator is a quadratic polynomial. So, we have that

$$


\lim_{n \to \infty} a_n = \lim_{n \to \infty} \dfrac{1}{(n-1) \cdot n} = 0.


$$

We conclude that the sequence is convergent, and its limit is zero.

### Example: Sequences Containing Ratios of Shifted Factorials

#### Question

Determine whether the sequence

$$


a_n = \dfrac{2(n-1)!}{(n+1)!}


$$

converges or diverges. If it converges, determine its limit.

#### Explanation

To evaluate the limit, note the following:

- We need to write the larger factorial in terms of the smaller one.

- In this case, $(n+1)!$ is the larger factorial, and $(n-1)!$ is the smaller.

- So, we need to write $(n+1)!$ in terms of $(n-1)!$

Now, notice the following:

$$


(n+1)! = (n-1)!\cdot n \cdot (n+1)


$$

We use this to cancel the $(n-1)!$ that occurs in both the numerator and denominator in our expression for $a_n{:}$

$$


\begin{aligned}𝑎_{𝑛} & =\frac{2(𝑛−1)!}{(𝑛+1)!} \\ & =\frac{2⋅(𝑛−1)!}{(𝑛−1)!⋅𝑛⋅(𝑛+1)} \\ & =\frac{2⋅(𝑛−1)!}{(𝑛−1)!⋅𝑛⋅(𝑛+1)} \\ & =\frac{2}{𝑛⋅(𝑛+1)}\end{aligned}


$$

We see that $a_n$ shrinks to zero as $n\to\infty$ because the numerator is constant, yet the denominator is a quadratic polynomial. So, we have that

$$


\lim\limits_{n \to \infty} a_n = \lim\limits_{n \to \infty} \dfrac{2}{n\cdot (n+1)} = 0.


$$

We conclude that the sequence is convergent, and its limit is zero.
