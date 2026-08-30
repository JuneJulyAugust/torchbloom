# Finding the Sum of an Arithmetic Series

Source: https://www.mathacademy.com/topics/675?courseId=128
Topic ID: 675

## Prerequisites

- [Expressing an Arithmetic Series in Sigma Notation](./779-expressing-an-arithmetic-series-in-sigma-notation.md)

## Lesson

### Introduction

Suppose we want to calculate the sum of the following arithmetic series:

$$


S_{10} = \sum_{n=1}^{10} \big( 2n \big) = 2 + 4 + 6 + \cdots 16 + 18 + 20


$$

One way is to add up the terms individually, but that would take a long time.

There is an easier way. If we have an arithmetic series $\displaystyle{S_N = \sum_{n=1}^N a_n},$ then we can calculate $S_N$ using the formula

$$


S_N = \frac{N}{2}(a_1+a_N),


$$

where $a_1$ is the first term, $a_N$ is the last term, and $N$ is the total number of terms.

For our series, we have $a_1=2,$ $a_N= 20,$ and $N=10.$ Substituting these values into the formula for $S_N,$ we obtain

$$


\begin{aligned}𝑆_{10} & =\frac{𝑁}{2}(𝑎_{1}+𝑎_{𝑁}) \\ & =\frac{10}{2}(2+20) \\ & =5⋅22 \\ & =110.\end{aligned}


$$

**Note:** To see where the formula comes from, notice that we have $5$ pairs that add up to $22\mathbin{:}$

$$


\begin{aligned}𝑎_{1}+𝑎_{10} & =2+20=22 \\ 𝑎_{2}+𝑎_{9} & =4+18=22 \\ 𝑎_{3}+𝑎_{8} & =6+16=22 \\ 𝑎_{4}+𝑎_{7} & =8+14=22 \\ 𝑎_{5}+𝑎_{6} & =10+12=22\end{aligned}


$$

So, the sum is $5 \cdot 22 = 110.$ In general, the number of pairs is $\dfrac{N}{2},$ and they all add up to the value of $(a_1 + a_N).$

### Example: Finding the Sum of an Arithmetic Series Given the First and Last Terms

#### Question

Find the sum of the following arithmetic series:

$$


1+6+11+16+21+\cdots+101


$$

#### Explanation

To calculate the sum of an arithmetic series, we use the formula

$$


S_N = \frac{N}{2}(a_1+a_N),


$$

where $a_1$ is the first term, $a_N$ is the last term, and $N$ is the total number of terms.

For our series, we have $a_1=1,$ and the common difference is

$$


\begin{aligned}𝑑 & =𝑎_{2}−𝑎_{1} \\ & =6−1 \\ & =5.\end{aligned}


$$

So, the formula for the $n$th term is

$$


\begin{aligned}𝑎_{𝑛} & =𝑎_{1}+(𝑛−1)𝑑 \\ & =1+(𝑛−1)(5) \\ & =1+5𝑛−5 \\ & =5𝑛−4.\end{aligned}


$$

As we know, the last term is $a_N=101.$ Putting this value in the formula for the $n$th term obtained above, we get

$$


\begin{aligned}𝑎_{𝑁} & =5𝑁−4 \\ 101 & =5𝑁−4 \\ 105 & =5𝑁 \\ 𝑁 & =21.\end{aligned}


$$

Finally, substituting $a_1=1,$ $a_N = 101,$ and $N=21$ into the formula for $S_N,$ we obtain

$$


\begin{aligned} S_{21}&= \dfrac{21}{2}(1+101)\\[3pt] &= \dfrac{21}{2}\cdot 102 \\\[5pt] &= 21\cdot 51 \\\[5pt] &= 1\,071. \end{aligned}


$$

### Example: Finding the Sum of an Arithmetic Series Given in Sigma Notation

#### Question

What is the sum of the arithmetic series $\displaystyle{\sum_{n=1}^{25} (2n + 1)}?$

#### Explanation

To calculate the sum of an arithmetic series, we use the formula

$$


S_N = \frac{N}{2}(a_1+a_N),


$$

where $a_1$ is the first term, $a_N$ is the last term, and $N$ is the total number of terms.

Given the series $\displaystyle\sum_{n=1}^{25} (2n+1)$ in sigma notation, we note that

- the total number of terms is $N=25,$

- the first term is $a_1 = 2 \cdot 1 + 1= 3,$ and

- the last term is $a_{25}= 2 \cdot 25 + 1 = 51.$

Substituting these values into the formula for the sum of an arithmetic series, we obtain

$$


\begin{aligned}𝑆_{25} & =\frac{25}{2}(3+51) \\ & =\frac{25}{2}(54) \\ & =25⋅27 \\ & =675.\end{aligned}


$$

### The Alternative Formula for the Sum of an Arithmetic Series

So far, to calculate the sum of the first $N$ terms of an arithmetic series we have used the formula

$$


S_N = \frac{N}{2}(a_1 + a_N),


$$

where $a_1$ is the first term, $a_N$ is the last term, and $N$ is the number of terms.

Using the formula for the $n$th term $\displaystyle{a_n = a_1 + (n-1)d},$ we can express the last term $a_N$ as

$$


a_N = a_1 + (N-1)d,


$$

where $d$ is the common difference.

If we substitute this into our formula for $S_N,$ we get

$$


\begin{aligned}𝑆_{𝑁} & =\frac{𝑁}{2}(𝑎_{1}+𝑎_{𝑁}) \\ & =\frac{𝑁}{2}(𝑎_{1}+(𝑎_{1}+(𝑁−1)𝑑)) \\ & =\frac{𝑁}{2}(𝑎_{1}+𝑎_{1}+(𝑁−1)𝑑) \\ & =\frac{𝑁}{2}(2𝑎_{1}+(𝑁−1)𝑑).\end{aligned}


$$

This is a new formula for the sum. So, we can also calculate $S_N$ for an arithmetic series using the formula

$$


S_N = \frac{N}{2}\big( 2a_1+(N-1)d \big).


$$

With this formula, we can find the value of the sum without knowing the last term.

### Example: Finding the Sum of an Arithmetic Series Given the First Term and the Total Number of Terms

#### Question

Calculate the sum of the first $20$ terms of the following arithmetic series:

$$


5+11+17+23+\cdots


$$

#### Explanation

To calculate the sum of an arithmetic series, we use the formula

$$


S_N = \frac{N}{2}\big( 2a_1+(N-1)d \big)


$$

where $a_1$ is the first term, $d$ is the common difference, and $N$ is the number of terms.

We are given that the total number of terms $N=20$ and the first term is $a_1=5.$ Now, the common difference $d$ can be found as follows:

$$


\begin{aligned}𝑑 & =𝑎_{2}−𝑎_{1} \\ & =11−5 \\ & =6\end{aligned}


$$

Substituting $a_1=5,$ $d=6,$ and $N=20$ into the above formula for $S_N,$ we obtain

$$


\begin{aligned}𝑆_{20} & =\frac{𝑁}{2}(2𝑎_{1}+(𝑁−1)𝑑) \\ & =\frac{20}{2}(2⋅5+(20−1)⋅6) \\ & =10⋅(10+114) \\ & =10⋅124 \\ & =1\,240.\end{aligned}


$$

### Example: Finding the Sum of an Arithmetic Series Given Two Terms

#### Question

An arithmetic series has $a_3=7$ and $a_{8}=17,$ where $a_3$ and $a_{8}$ are the third and eighth terms of the series, respectively. Find the sum of the first $7$ terms of the series.

#### Explanation

To calculate the sum of an arithmetic series, we use the formula

$$


S_N = \frac{N}{2}\big( 2a_1+(N-1)d \big),


$$

where $a_1$ is the first term, $d$ is the common difference, and $N$ is the number of terms.

Since we know two terms of the arithmetic series, we can find its common difference as follows:

$$


\begin{aligned}𝑑 & =\frac{𝑎_{8}−𝑎_{3}}{8−3} \\ & =\frac{17−7}{8−3} \\ & =\frac{10}{5} \\ & =2\end{aligned}


$$

We know that $a_{3}=7,$ so we can use the formula for the $n$th term to compute $a_1,$ as follows:

$$


\begin{aligned}𝑎_{𝑛} & =𝑎_{1}+(𝑛−1)𝑑 \\ 𝑎_{3} & =𝑎_{1}+(3−1)⋅2 \\ 7 & =𝑎_{1}+4 \\ 𝑎_{1} & =3\end{aligned}


$$

Substituting $a_1=3,$ $d=2,$ and $N=7$ into the above formula for $S_N,$ we obtain

$$


\begin{aligned}𝑆_{7} & =\frac{𝑁}{2}(2𝑎_{1}+(𝑁−1)𝑑) \\ & =\frac{7}{2}(2⋅3+(7−1)⋅2) \\ & =\frac{7}{2}⋅(6+12) \\ & =\frac{7}{2}⋅18 \\ & =7⋅9 \\ & =63.\end{aligned}


$$

### Proof of the Sum Formula

The sum of the first $N$ terms of an arithmetic series with the initial term $a_1$ and the common difference $d$ can be found as

$$


S_N = \frac{N}{2}\big( 2a_1+(N-1)d \big).


$$

We'll now prove this result.

First, we recall that the $n$th term of the series is given by $a_n = a_1 + (n-1)d.$

Let's write down the sum by placing the indices $n=1,2,3,\ldots, N$ in ascending order:

$$


\begin{aligned}𝑆_{𝑁} & =𝑎_{1}+𝑎_{2}+⋯+𝑎_{𝑁−1}+𝑎_{𝑁} \\ & =𝑎_{1}+\underset{𝑎_{2}}{\underset{}{(𝑎_{1}+𝑑)}}+⋯+\underset{𝑎_{𝑁−1}}{\underset{}{(𝑎_{1}+(𝑁−2)𝑑)}}+\underset{𝑎_{𝑁}}{\underset{}{(𝑎_{1}+(𝑁−1)𝑑)}}\end{aligned}


$$

Now, let's write down the same sum but place the indices in descending order:

$$


\begin{aligned}𝑆_{𝑁} & =𝑎_{𝑁}+𝑎_{𝑁−1}+⋯+𝑎_{2}+𝑎_{1} \\ & =\underset{𝑎_{𝑁}}{\underset{}{(𝑎_{1}+(𝑁−1)𝑑)}}+\underset{𝑎_{𝑁−1}}{\underset{}{(𝑎_{1}+(𝑁−2)𝑑)}}+⋯+\underset{𝑎_{2}}{\underset{}{(𝑎_{1}+𝑑)}}+𝑎_{1}\end{aligned}


$$

By adding the two expressions, we get the following:

$$


\begin{aligned}𝑆_{𝑁} & = & 𝑎_{1} & + & (𝑎_{1}+𝑑) & + & ⋯ & + & (𝑎_{1}+(𝑁−1)𝑑) \\ 𝑆_{𝑁} & = & (𝑎_{1}+(𝑁−1)𝑑) & + & (𝑎_{1}+(𝑁−2)𝑑) & + & ⋯ & + & 𝑎_{1} \\ 2𝑆_{𝑁} & = & (2𝑎_{1}+(𝑁−1)𝑑) & + & (2𝑎_{1}+(𝑁−1)𝑑) & + & ⋯ & + & (2𝑎_{1}+(𝑁−1)𝑑)\end{aligned}


$$

The expression on the right contains $N$ copies of $2a_1+(N-1)d.$ Therefore,

$$


\begin{aligned}2𝑆_{𝑁}=𝑁⋅(2𝑎_{1}+(𝑁−1)𝑑)\,⟹\,𝑆_{𝑁}=\frac{𝑁}{2}(2𝑎_{1}+(𝑁−1)𝑑).\end{aligned}


$$
