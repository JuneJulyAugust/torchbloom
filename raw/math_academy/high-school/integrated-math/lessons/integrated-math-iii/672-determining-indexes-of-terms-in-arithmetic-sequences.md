# Determining Indexes of Terms in Arithmetic Sequences

Source: https://www.mathacademy.com/topics/672?courseId=134
Topic ID: 672

## Prerequisites

- [Finding the Nth Term of an Arithmetic Sequence Given Two Terms](../../../traditional/lessons/algebra-i/1346-finding-the-nth-term-of-an-arithmetic-sequence-given-two-terms.md)
- [Translating Between Explicit and Recursive Formulas for Arithmetic Sequences](../../../traditional/lessons/algebra-i/2214-translating-between-explicit-and-recursive-formulas-for-arithmetic-sequences.md)

## Lesson

### Introduction

In addition to using the formula

$$


\begin{aligned}𝑎_{𝑛} & =𝑎_{1}+(𝑛−1)𝑑\end{aligned}


$$

to compute the terms of an arithmetic sequence, we can also use it to compute the **index** of a particular term. The index of a term is simply the value of $n$ corresponding to that term.

To illustrate, suppose we're given the following arithmetic sequence:

$$


1, \: 4, \: 7, \: 10, \ \ldots, \: 28, \: \ldots


$$

If the first term is $1,$ the second term is $4,$ the third term is $7,$ and so on, then what term gives the value $28?$ In other words, what value of $n$ gives $a_n=28?$

Since $a_1=1$ and $d=3,$ we can construct the formula for the $n$th term as follows:

$$


\begin{aligned}𝑎_{𝑛} & =𝑎_{1}+(𝑛−1)𝑑 \\ & =1+(𝑛−1)(3) \\ & =1+3𝑛−3 \\ & =3𝑛−2\end{aligned}


$$

Now we can solve for the value of $n$ that gives $a_n=28,$ as follows:

$$


\begin{aligned}𝑎_{𝑛} & =3𝑛−2 \\ 28 & =3𝑛−2 \\ 30 & =3𝑛 \\ 10 & =𝑛\end{aligned}


$$

Therefore, $28$ is the $10$th term of the sequence.

### Example: Determining the Index of a Term in an Arithmetic Sequence

#### Question

What is the index of the term $42$ in the following arithmetic sequence?

$$


-10, \: -6, \: -2, \: \ldots


$$

#### Explanation

Since $a_1=-10$ and

$$


d=-6-(-10)=4,


$$

we can construct the formula for the $n$th term as follows:

$$


\begin{aligned}𝑎_{𝑛} & =𝑎_{1}+(𝑛−1)𝑑 \\ & =−10+(𝑛−1)(4) \\ & =−10+4𝑛−4 \\ & =4𝑛−14\end{aligned}


$$

Now, we solve for the value of $n$ that gives $a_n=42,$ as follows:

$$


\begin{aligned}𝑎_{𝑛} & =4𝑛−14 \\ 42 & =4𝑛−14 \\ 56 & =4𝑛 \\ 14 & =𝑛\end{aligned}


$$

Therefore, $42$ is the $14$th term of the sequence.

### Example: Determining the Index of a Term Given the Recursive Formula

#### Question

Given the arithmetic sequence

$$


a_{n+1} = a_n + 12, \quad a_1 = 3,\quad n\geq 1,


$$

what is the index of the term $255?$

#### Explanation

We will convert the recursive formula to an explicit formula and then solve for the value of $n$ such that $a_n=255.$

The recursive rule for an arithmetic sequence takes the form

$$


a_{n+1} = a_n +{\color{black}d}.


$$

In the given formula, we have $d={\color{black}12}.$ We are also told that $a_1={\color{black}3},$ so we can write the explicit formula as follows:

$$


\begin{aligned}𝑎_{𝑛} & =𝑎_{1}+(𝑛−1)𝑑 \\ & =3+(𝑛−1)(12) \\ & =3+12𝑛−12 \\ & =12𝑛−9\end{aligned}


$$

Now, we solve for the value of $n$ such that $a_n=255\mathbin{:}$

$$


\begin{aligned}𝑎_{𝑛} & =12𝑛−9 \\ 255 & =12𝑛−9 \\ 264 & =12𝑛 \\ \frac{264}{12} & =𝑛 \\ 22 & =𝑛\end{aligned}


$$

Therefore, $255$ is the $22$nd term of the sequence.

### Example: Determining the Index of a Term Given Another Term and the Common Difference

#### Question

Given an arithmetic sequence that has $a_4=5$ and common difference $d=3$, what is the index of the term $95?$

#### Explanation

Since $a_4=5$ is $3$ jumps after $a_1,$ we can determine the first term of the sequence:

$$


\begin{aligned}𝑎_{4} & =𝑎_{1}+3𝑑 \\ 5 & =𝑎_{1}+3(3) \\ 5 & =𝑎_{1}+9 \\ −4 & =𝑎_{1}\end{aligned}


$$

So, the formula for the $n$th term is:

$$


\begin{aligned}𝑎_{𝑛} & =𝑎_{1}+(𝑛−1)𝑑 \\ & =−4+(𝑛−1)(3) \\ & =−4+3𝑛−3 \\ & =3𝑛−7\end{aligned}


$$

Now, we solve for the value of $n$ that gives $a_n=95,$ as follows:

$$


\begin{aligned}𝑎_{𝑛} & =3𝑛−7 \\ 95 & =3𝑛−7 \\ 102 & =3𝑛 \\ \frac{102}{3} & =𝑛 \\ 34 & =𝑛\end{aligned}


$$

Therefore, $95$ is the $34$th term of the sequence.

### Example: Determining the Index of a Term Given Two Terms

#### Question

Given an arithmetic sequence that has $a_2=12$ and $a_{4} = 10$, what is the index of the term $-12?$

#### Explanation

To construct the formula for the sequence, we need to know the common difference $d$ and the first term $a_1.$

Since we are given $a_2=12$ and $a_4=10,$ we can find the common difference by dividing the total difference by the number of jumps:

$$


\begin{aligned}𝑑 & =\frac{𝑎_{4}−𝑎_{2}}{4−2} \\ & =\frac{10−12}{4−2} \\ & =\frac{−2}{2} \\ & =−1\end{aligned}


$$

Now, since $a_2=12$ is $1$ jump after $a_1,$ we can determine the first term of the sequence:

$$


\begin{aligned}𝑎_{2} & =𝑎_{1}+𝑑 \\ 12 & =𝑎_{1}−1 \\ 13 & =𝑎_{1}\end{aligned}


$$

So, the formula for the $n$th term is:

$$


\begin{aligned}𝑎_{𝑛} & =𝑎_{1}+(𝑛−1)𝑑 \\ & =13+(𝑛−1)(−1) \\ & =14−𝑛\end{aligned}


$$

Now we solve for the value of $n$ that gives $a_n=-12,$ as follows:

$$


\begin{aligned}𝑎_{𝑛} & =14−𝑛 \\ −12 & =14−𝑛 \\ −26 & =−𝑛 \\ 26 & =𝑛\end{aligned}


$$

Therefore, $-12$ is the $26$th term of the sequence.
