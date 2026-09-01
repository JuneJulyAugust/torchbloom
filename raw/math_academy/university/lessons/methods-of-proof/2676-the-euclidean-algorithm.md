# The Euclidean Algorithm

Source: https://www.mathacademy.com/topics/2676?courseId=76
Topic ID: 2676

## Prerequisites

- [The Division Algorithm](./2689-the-division-algorithm.md)

## Lesson

### Introduction

The **greatest common divisor** (or $\text{gcd}$) of two integers is the largest positive integer that divides both of the integers. For example,

$$


\text{gcd}(48,18) = 6


$$

because $6$ is the largest integer that divides both $48$ and $18.$

We often wish to compute the greatest common divisor of two large numbers. Doing this by inspection is hard. Another method is to use prime factorization, but this is also difficult and inefficient for large numbers.

Another method, known as the **Euclidian algorithm** is very efficient, despite being over $2\,000$ years old.

Let's demonstrate how to compute $\text{gcd}(48,18)$ using the Euclidian algorithm. The first step is to apply the division algorithm and write down $48 = 18q + r.$ When we do, we get

$$


48 = {\color{blue}{18}}(2) + {\color{red}12}.


$$

We ignore the quotient $2$ for now and focus on the ${\color{blue}{18}}$ (the smaller of our two numbers) and the remainder ${\color{red}12}.$ We apply the division algorithm again to these two numbers, and this gives

$$


18 = {\color{blue}{12}}(1) + {\color{red}6}.


$$

Applying the division algorithm to the number ${\color{blue}{12}}$ and the remainder ${\color{red}6}$ gives

$$


12 = {\color{blue}{6}}(2) + {\color{red}0}.


$$

We have now reached a remainder of ${\color{red}0},$ which means that we are done.

In practice, we normally write the steps underneath one another, like so.

$$


\begin{aligned}\begin{matrix}48 & = & 18(2) & + & 12 \\ & ↙ & & ↙ & \\ 18 & = & 12(1) & + & 6 \\ & ↙ & & ↙ & \\ 12 & = & 6(2) & + & 0\end{matrix}\end{aligned}


$$

The last positive remainder is ${\color{red}6}.$ The Euclidean algorithm states that this is the greatest common divisor that we seek. Therefore, we conclude that $\text{gcd}(48,18) = {\color{red}6}.$

Finally, we note that two integers $a$ and $b$ are **coprime** if $\gcd(a,b) = 1.$

### Example: Computing the Greatest Common Divisor of Two Three-Digit Numbers

#### Question

Find the greatest common divisor of $713$ and $322.$

#### Explanation

We use the Euclidean algorithm, as follows:

$$


\begin{aligned}\begin{matrix}713 & = & 322(2) & + & 69 \\ & ↙ & & ↙ & \\ 322 & = & 69(4) & + & 46 \\ & ↙ & & ↙ & \\ 69 & = & 46(1) & + & 23 \\ & ↙ & & ↙ & \\ 46 & = & 23(2) & + & 0\end{matrix}\end{aligned}


$$

The last positive remainder is ${\color{red}23}.$ Therefore, we conclude that the greatest common divisor of $713$ and $322$ is $23.$ Symbolically, we write

$$


\text{gcd}(713, 322) = 23.


$$

### Why Does the Euclidean Algorithm Work?

We now return to the question of why the Euclidean algorithm works. To help us to understand, let's consider once more how to compute $\text{gcd}(48,18).$ Using the algorithm, we get the following:

$$


\begin{aligned}\begin{matrix}48 & = & 18(2) & + & 12 \\ & ↙ & & ↙ & \\ 18 & = & 12(1) & + & 6 \\ & ↙ & & ↙ & \\ 12 & = & 6(2) & + & 0\end{matrix}\end{aligned}


$$

Carrying out the process gives the following pairs of integers:

$$


48,18\quad \longrightarrow\quad 18,12 \quad \longrightarrow \quad 12,6


$$

We claim that $\text{gcd}(48,18)$ must be the same as $\text{gcd}(18,12).$ To see why, notice that we used the division algorithm to write

$$


48 = 18(2) + 12.


$$

If $48$ and $18$ are divisible by some integer $n,$ then $n$ must also divide $18(2).$ This means that $n$ must divide $48-18(2),$ i.e., $n$ must divide $12.$ So any number $n$ that divides both $48$ and $18$ must also divide both $18$ and $12.$

Repeating the same argument, we are able to conclude that $\text{gcd}(18,12) = \text{gcd}(12,6).$ Since $\text{gcd}(12,6) = 6,$ we conclude that

$$


\text{gcd}(48,18) = \text{gcd}(18,12) = \text{gcd}(12,6) = 6.


$$

In this example, the algorithm concluded in three steps, but the argument can be extended to many steps.

### Example: Computing the Greatest Common Divisor of Larger Numbers

#### Question

Find the greatest common divisor of $1\,036$ and $555.$

#### Explanation

We use the Euclidean algorithm, as follows:

$$


\begin{aligned}\begin{matrix}1036 & = & 555(1) & + & 481 \\ & ↙ & & ↙ & \\ 555 & = & 481(1) & + & 74 \\ & ↙ & & ↙ & \\ 481 & = & 74(6) & + & 37 \\ & ↙ & & ↙ & \\ 74 & = & 37(2) & + & 0\end{matrix}\end{aligned}


$$

The last positive remainder is ${\color{red}37}.$ Therefore, we conclude that the greatest common divisor of $1\,036$ and $555$ is $37.$ Symbolically, we write

$$


\text{gcd}(1\,036, 555) = 37.


$$

### Example: Determining Whether Two Integers are Coprime

#### Question

Which of the following statements are true?

1. $\text{gcd}(651, 574) = 7$

2. $\text{gcd}(651, 574) = 1$

3. $651$ and $574$ are coprime

#### Explanation

Recall that two integers are coprime if their greatest common divisor is $1.$

With that in mind, let's examine our statements in turn.

- Statement I is true, while statement II is false. Indeed, let's use the Euclidean algorithm, as follows: The last positive remainder is ${\color{blue}7}.$ So, the greatest common divisor of $651$ and $574$ is $7\mathbin{:}$

- Statement III is false. Since $\text{gcd}(651, 574) > 1,$ the numbers are not coprime.

Therefore, the correct answer is "I only."
