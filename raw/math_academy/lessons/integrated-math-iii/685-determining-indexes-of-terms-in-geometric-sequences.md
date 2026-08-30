# Determining Indexes of Terms in Geometric Sequences

Source: https://www.mathacademy.com/topics/685?courseId=134
Topic ID: 685

## Prerequisites

- [Translating Between Explicit and Recursive Formulas for Geometric Sequences](../algebra-i/2215-translating-between-explicit-and-recursive-formulas-for-geometric-sequences.md)
- [Finding the Common Ratio of a Geometric Sequence Given Two Terms](../algebra-i/2534-finding-the-common-ratio-of-a-geometric-sequence-given-two-terms.md)

## Lesson

### Introduction

In addition to using the formula

$$


\begin{aligned}𝑎_{𝑛} & =𝑎_{1}⋅𝑟^{𝑛−1}\end{aligned}


$$

to compute the terms of a geometric sequence, we can also use it to compute the index of a desired term in a geometric sequence.

To illustrate, suppose we're given the geometric sequence

$$


3, \: 6, \: 12, \: \ldots, \:96, \ldots


$$

that has the first term $a_1=3$ and the common ratio $r=2$. What index gives the term $96?$ In other words, what value of $n$ gives $a_n=96?$

We can construct the formula for the $n$th term, as follows:

$$


\begin{aligned}𝑎_{𝑛} & =𝑎_{1}⋅𝑟^{𝑛−1} \\ & =3⋅2^{𝑛−1}\end{aligned}


$$

Now, to find the value of $n$ that gives $a_n=96$, we can use the formula for the $n$th term, as follows:

$$


\begin{aligned}𝑎_{𝑛} & =3⋅2^{𝑛−1} \\ 96 & =3⋅2^{𝑛−1} \\ 32 & =2^{𝑛−1} \\ 2^{5} & =2^{𝑛−1}\end{aligned}


$$

Equating the exponents gives:

$$


5 = n - 1\quad \Longrightarrow \quad n = 6


$$

Therefore, $96$ is the $6$th term of the sequence.

### Example: Finding the Index of a Term Given the First Term and the Common Ratio

#### Question

Given that a geometric sequence has the first term $a_1 = 5$, the common ratio $r = 2$, and the $n$th term $a_n = 640$, what is the value of $n?$

#### Explanation

To find the index, we substitute our known values of $a_1$, $r$ and $a_n$ into the formula for the $n$th term:

$$


\begin{aligned}𝑎_{𝑛} & =𝑎_{1}⋅𝑟^{𝑛−1} \\ 640 & =5⋅2^{𝑛−1} \\ \frac{640}{5} & =2^{𝑛−1} \\ 128 & =2^{𝑛−1} \\ 2^{7} & =2^{𝑛−1}\end{aligned}


$$

Equating the exponents gives:

$$


7 = n - 1\quad \Longrightarrow \quad n = 8


$$

We can check this result by substituting $n = 8$ into the formula for the $n$th term:

$$


\begin{aligned}𝑎_{𝑛} & =𝑎_{1}⋅𝑟^{𝑛−1} \\ & =5⋅2^{8−1} \\ & =5⋅2^{7} \\ & =5⋅128 \\ & =640\,✓\end{aligned}


$$

### Example: Finding the Index of a Term Given the First Term and Another Term

#### Question

Given that a geometric sequence has the first term $a_1 = 1$ and the $4$th term $a_4 = 8$, what is the index of the term $32?$

#### Explanation

Since we are given that $a_4=8$, we can use the formula for the $n$th term to solve for $r$, as follows:

$$


\begin{aligned}𝑎_{𝑛} & =𝑎_{1}⋅𝑟^{𝑛−1} \\ 8 & =1⋅𝑟^{4−1} \\ 8 & =𝑟^{3} \\ 2^{3} & =𝑟^{3} \\ 2 & =𝑟\end{aligned}


$$

Therefore, the formula for the $n$th term is

$$


\begin{aligned}𝑎_{𝑛}=1⋅2^{𝑛−1}.\end{aligned}


$$

Now, we solve for the value of $n$ that gives $a_n=32,$ as follows:

$$


\begin{aligned}𝑎_{𝑛} & =1⋅2^{𝑛−1} \\ 32 & =2^{𝑛−1} \\ 2^{5} & =2^{𝑛−1} \\ 5 & =𝑛−1 \\ 6 & =𝑛\end{aligned}


$$

Therefore, $n=6.$

### Example: Finding the Index of a Term Given the Recursive Formula

#### Question

What is the index of the term $16$ for the geometric sequence below?

$$


a_{n+1} = 2 a_n \quad a_1 = \dfrac{1}{4},\quad n\geq 1


$$

#### Explanation

This geometric sequence is given as a recurrence relation, i.e.,

$$


a_{n+1} = {\color{blue}r} \cdot a_n.


$$

Therefore,

$$


a_1 = \dfrac{1}{4}, \quad {\color{blue}r}=2.


$$

We're interested in finding $n$ such that $a_n = 16.$ Using the formula for the $n$th term, we get:

$$


\begin{aligned}𝑎_{𝑛} & =𝑎_{1}⋅𝑟^{𝑛−1} \\ 16 & =\frac{1}{4}⋅2^{𝑛−1} \\ 2^{4} & =\frac{1}{2^{2}}⋅2^{𝑛−1} \\ 2^{6} & =2^{𝑛−1}\end{aligned}


$$

Equating the exponents gives:

$$


6 = n - 1\quad \Longrightarrow \quad n = 7


$$

Therefore, $16$ is the $7$th term of the sequence.

### Example: Finding the Index of a Particular Term When the First Term is Unknown

#### Question

Given that a geometric sequence has $a_2 = 24$, $a_5 = 3$ and $a_k = 12$, what is the value of $k?$

#### Explanation

First, we need to find the common ratio. We are told that $a_2=24$ and $a_5=3,$ so we can find the common ratio using a formula, as follows:

$$


\begin{aligned}𝑟^{𝑛−𝑚} & =\frac{𝑎_{𝑛}}{𝑎_{𝑚}} \\ 𝑟^{5−2} & =\frac{𝑎_{5}}{𝑎_{2}} \\ 𝑟^{5−2} & =\frac{3}{24} \\ 𝑟^{3} & =\frac{1}{8} \\ 𝑟^{3} & =(\frac{1}{2})^{3} \\ 𝑟 & =\frac{1}{2}\end{aligned}


$$

Now that we know the common ratio is $r=\dfrac{1}{2}$, we can use the same formula to solve for the value of $k$ such that $a_k=12\mathbin{:}$

$$


\begin{aligned}𝑟^{𝑛−𝑚} & =\frac{𝑎_{𝑛}}{𝑎_{𝑚}} \\ 𝑟^{𝑘−2} & =\frac{𝑎_{𝑘}}{𝑎_{2}} \\ (\frac{1}{2})^{𝑘−2} & =\frac{12}{24} \\ (\frac{1}{2})^{𝑘−2} & =\frac{1}{2} \\ (\frac{1}{2})^{𝑘−2} & =(\frac{1}{2})^{1} \\ 𝑘−2 & =1 \\ 𝑘 & =3\end{aligned}


$$
