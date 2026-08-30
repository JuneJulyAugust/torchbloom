# Expressing an Arithmetic Series in Sigma Notation

Source: https://www.mathacademy.com/topics/779?courseId=43
Topic ID: 779

## Prerequisites

- [Determining Indexes of Terms in Arithmetic Sequences](../algebra-i/672-determining-indexes-of-terms-in-arithmetic-sequences.md)
- [Sigma Notation](./673-sigma-notation.md)

## Lesson

### Introduction

Suppose that we have the arithmetic sequence

$$


4, \: 7, \: 10, \: 13, \: 16, \: 19.


$$

The sum of all of the terms of an arithmetic sequence is known as an **arithmetic series**. Here, the arithmetic series for the arithmetic sequence above is

$$


S=4+7+10+13+16+19.


$$

We can write this sum more compactly using sigma notation. But first, we need to find a formula for the $n$th term in the series.

For our series above, the first term is $a_1=4$ and the common difference is

$$


\begin{aligned}𝑑 & =𝑎_{2}−𝑎_{1} \\ & =7−4 \\ & =3.\end{aligned}


$$

So, the formula for the $n$th term is

$$


\begin{aligned}𝑎_{𝑛} & =𝑎_{1}+(𝑛−1)𝑑 \\ & =4+(𝑛−1)(3) \\ & =4+3𝑛−3 \\ & =3𝑛+1.\end{aligned}


$$

There are $6$ terms in total, from $n={\color{black}1}$ to $n={\color{red}6}.$ So the sigma notation for the given series is:

$$


S = \sum_{n={\color{black}1}}^{\color{red}6} \left({\color{blue}3n+1}\right)


$$

If we expand the above series out term-by-term, we have

$$


\begin{aligned}𝑆 & =(3⋅1+1)+(3⋅2+1)+(3⋅3+1)+(3⋅4+1)+(3⋅5+1)+(3⋅6+1) \\ & =4+7+10+13+16+19,\end{aligned}


$$

which is our original sum.

**Watch out!** It's important to understand the difference between a *sequence* and a *series*. A sequence is a list of numbers (separated by commas). A series is what you get when you add all of the terms of a sequence together.

### Example: Writing an Arithmetic Series Using Sigma Notation when All Terms are Shown

#### Question

Write the arithmetic series $10+14+18+22+26+30+34$ in sigma notation.

#### Explanation

The first term is $a_1=10$ and the common difference is

$$


\begin{aligned}𝑑 & =𝑎_{2}−𝑎_{1} \\ & =14−10 \\ & =4.\end{aligned}


$$

So, the formula for the $n$th term is

$$


\begin{aligned}𝑎_{𝑛} & =𝑎_{1}+(𝑛−1)𝑑 \\ & =10+(𝑛−1)(4) \\ & =10+4𝑛−4 \\ & =4𝑛+6.\end{aligned}


$$

There are $7$ terms in total, from $n={\color{black}1}$ to $n={\color{red}7}.$ So, the sigma notation for the given sum is

$$


\sum_{n={\color{black}1}}^{\color{red}7} \left({\color{blue}4n+6}\right).


$$

### Example: Writing an Arithmetic Series Using Sigma Notation when Not All Terms are Shown

#### Question

Express the following arithmetic series using sigma notation:

$$


8+4+ \ldots -44 - 48


$$

#### Explanation

The first term is $a_1=8$ and the common difference is

$$


\begin{aligned}𝑑 & =𝑎_{2}−𝑎_{1} \\ & =4−8 \\ & =−4.\end{aligned}


$$

So, the formula for the $n$th term is

$$


\begin{aligned}𝑎_{𝑛} & =𝑎_{1}+(𝑛−1)𝑑 \\ & =8+(𝑛−1)(−4) \\ & =8−4𝑛+4 \\ & =−4𝑛+12.\end{aligned}


$$

We don't know the index of the last term, but we can find it using the formula for the $n$th term:

$$


\begin{aligned}𝑎_{𝑛} & =−48 \\ −4𝑛+12 & =−48 \\ 12+48 & =4𝑛 \\ 60 & =4𝑛 \\ 15 & =𝑛\end{aligned}


$$

There are $15$ terms in total, from $n={\color{black}1}$ to $n={\color{red}15}.$ So, the sigma notation for the given sum is

$$


\sum_{n={\color{black}1}}^{\color{red}15} ({\color{blue}- 4n+12}).


$$

### Example: Writing an Arithmetic Series Using Sigma Notation Given Two Terms of the Series

#### Question

An arithmetic series has $a_5=17$ and $a_{9}=7,$ where $a_5$ and $a_{9}$ are the fifth and ninth terms of the series, respectively. What is the sum of the first $11$ terms of the series, expressed using sigma notation?

#### Explanation

Since we know two terms of the arithmetic series, we can find its common difference:

$$


\begin{aligned}𝑑 & =\frac{𝑎_{9}−𝑎_{5}}{9−5} \\ & =\frac{7−17}{4} \\ & =\frac{−10}{4} \\ & =−\frac{5}{2}\end{aligned}


$$

Knowing that $a_{5}=17,$ we can use the formula for the $n$th term to compute $a_1,$ as follows:

$$


\begin{aligned}𝑎_{𝑛} & =𝑎_{1}+(𝑛−1)𝑑 \\ 17 & =𝑎_{1}+(5−1)(−\frac{5}{2}) \\ 17 & =𝑎_{1}−10 \\ 𝑎_{1} & =27\end{aligned}


$$

So we have $a_1 = 27$ and $d=-\dfrac 52.$ Therefore, the formula for the $n$th term is

$$


\begin{aligned}𝑎_{𝑛} & =27+(𝑛−1)(−\frac{5}{2}) \\ & =27−\frac{5}{2}𝑛+\frac{5}{2} \\ & =−\frac{5}{2}𝑛+\frac{59}{2}.\end{aligned}


$$

Finally, the sum of the first ${\color{red}11}$ terms can be written as

$$


\begin{aligned}\underset{\underset{𝑛=1}{∑}}{\overset{}{11}}(−\frac{5}{2}𝑛+\frac{59}{2}).\end{aligned}


$$
