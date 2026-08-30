# Finding the Nth Term of an Arithmetic Sequence Given Two Terms

Source: https://www.mathacademy.com/topics/1346?courseId=44
Topic ID: 1346

## Prerequisites

- [The Nth Term of an Arithmetic Sequence](./668-the-nth-term-of-an-arithmetic-sequence.md)
- [Finding the Common Difference of an Arithmetic Sequence](./669-finding-the-common-difference-of-an-arithmetic-sequence.md)

## Lesson

### Introduction

To find the $n$th term of an arithmetic sequence given two arbitrary terms, we must usually apply the following:

- The formula for the $n$th term of an arithmetic sequence is given by where $a_n$ is the $n$th term, $a_1$ is the first term, and $d$ is the common difference.

- We can find the common difference $d$ of an arithmetic sequence given two arbitrary terms using where $a_m$ is the $m$th term, and $a_k$ is the $k$th term.

Let's see some examples.

### Example: Finding the Nth Term Given the First Term and Another Term

#### Question

Find the formula for the $n$th term of an arithmetic sequence given that the first term is $-1$ and the eighth term is $13.$

#### Explanation

The formula for the $n$th term is given by

$$


a_n = a_1 + (n-1)d.


$$

We already know that the first term is $a_1=-1,$ so we just need to figure out the common difference $d.$

To find the common difference, we can find the total difference between the terms $a_1=-1$ and $a_8=13$ and divide it by the number of jumps, as follows:

$$


\begin{aligned}𝑑 & =\frac{𝑎_{8}−𝑎_{1}}{8−1} \\ & =\frac{13−(−1)}{8−1} \\ & =\frac{14}{7} \\ & =2\end{aligned}


$$

So the formula for the $n$th term of this arithmetic sequence is

$$


\begin{aligned} a_n&= a_{1}+(n-1)d \\[3pt] & = -1 + (n-1) (2) \\[3pt] & = -1 + 2n - 2 \\[3pt] & = 2n - 3. \end{aligned}


$$

### Example: Finding the Nth Term Given Two Consecutive Terms

#### Question

The fifth and sixth terms of an arithmetic sequence are $46$ and $50,$ respectively. Determine the formula for the $n$th term of the sequence.

#### Explanation

The formula for the $n$th term is given by

$$


a_n = a_1 + (n-1)d,


$$

so we need to figure out the first term $a_1$ and the common difference $d.$

Since the terms $a_5=46$ and $a_6=50$ are consecutive, we can subtract them to find the common difference:

$$


\begin{aligned}𝑑 & =𝑎_{6}−𝑎_{5} \\ & =50−46 \\ & =4\end{aligned}


$$

Now, we can use one of our known values, say, $a_5=46,$ to determine the first term of the sequence. Since $a_5$ is $4$ jumps after $a_1,$ we have

$$


\begin{aligned} a_5 &= a_1 + 4d \\[3pt] 46 &= a_1 + 4\cdot 4\\[3pt] 46 &= a_1 +16 \\[3pt] 46-16 &= a_1\\[3pt] a_1&= 30. \end{aligned}


$$

So the formula for the $n$th term of this arithmetic sequence is

$$


\begin{aligned} a_n&= a_{1}+(n-1)d \\[3pt] & = 30 + (n-1) \cdot 4 \\[3pt] & =30 + 4n -4 \\[3pt] & = 4n +26. \end{aligned}


$$

### Example: Finding the Nth Term Given Two Non-Consecutive Terms

#### Question

An arithmetic sequence has the $3$rd term $a_{3}=9$ and the $8$th term is $a_{8}=69.$ Find a formula for the $n$th term of the sequence.

#### Explanation

The formula for the $n$th term is given by

$$


a_n = a_1 + (n-1)d,


$$

so we need to figure out what the first term $a_1$ and the common difference $d$ are.

To find the common difference, we can find the total difference between the terms $a_{8}=69$ and $a_{3}=9$ and divide it by the number of jumps, as follows:

$$


\begin{aligned}𝑑 & =\frac{𝑎_{8}−𝑎_{3}}{8−3} \\ & =\frac{69−9}{8−3} \\ & =\frac{60}{5} \\ & =12\end{aligned}


$$

Now, we can use one of our known values, say, $a_{3}=9,$ to determine the first term of the sequence. Since $a_{3}$ is $2$ jumps after $a_1,$ we have

$$


\begin{aligned}𝑎_{3} & =𝑎_{1}+2𝑑 \\ 9 & =𝑎_{1}+2⋅12 \\ 9 & =𝑎_{1}+24 \\ 𝑎_{1} & =−15.\end{aligned}


$$

So, the formula for the $n$th term is

$$


\begin{aligned}𝑎_{𝑛} & =−15+(𝑛−1)⋅12 \\ & =−15+12𝑛−12 \\ & =12𝑛−27.\end{aligned}


$$
