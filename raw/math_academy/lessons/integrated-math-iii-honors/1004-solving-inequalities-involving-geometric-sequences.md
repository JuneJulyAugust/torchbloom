# Solving Inequalities Involving Geometric Sequences

Source: https://www.mathacademy.com/topics/1004?courseId=101
Topic ID: 1004

## Prerequisites

- [Determining Indexes of Terms in Geometric Sequences](../algebra-i/685-determining-indexes-of-terms-in-geometric-sequences.md)
- [Solving Inequalities Involving Exponential Functions](./2857-solving-inequalities-involving-exponential-functions.md)
- [Solving Logarithmic Equations by Combining the Laws of Logarithms](../algebra-ii/3832-solving-logarithmic-equations-by-combining-the-laws-of-logarithms.md)

## Lesson

### Introduction

Consider the following geometric sequence:

$$


3,\quad 6,\quad 12,\quad 24, \quad \ldots


$$

Suppose we want to find the first term that exceeds $3\,000\,000.$ We can do this by creating and solving an inequality.

First, let's construct a formula for the $n$th term of the sequence. The first term of the sequence is $a_1=3,$ and the common ratio is

$$


r = \dfrac 6 3 = 2.


$$

So, the $n$th term of the sequence can be written as

$$


\begin{aligned}𝑎_{𝑛} & =𝑎_{1}⋅𝑟^{𝑛−1} \\ & =3⋅2^{𝑛−1}.\end{aligned}


$$

We want the $n$th term to be greater than $3\,000\,000.$ So, we can set up and solve the corresponding inequality:

$$


\begin{aligned}𝑎_{𝑛} & >3\,000\,000 \\ 3⋅2^{𝑛−1} & >3\,000\,000 \\ 2^{𝑛−1} & >1\,000\,000 \\ log⁡(2^{𝑛−1}) & >log⁡(1\,000\,000) \\ (𝑛−1)log⁡(2) & >log⁡(1\,000\,000) \\ 𝑛−1 & >\frac{log⁡(1\,000\,000)}{log⁡(2)} \\ 𝑛 & >\frac{log⁡(1\,000\,000)}{log⁡(2)}+1\end{aligned}


$$

Estimating the right-hand side using a calculator, we get

$$


\dfrac {\log (1\,000\,000)} {\log (2)} + 1 \approx 20.932.


$$

Therefore, the $21$st term is the first term of the sequence that exceeds $3\,000\,000.$

To check our answer, we can easily verify that $a_{20} < 3\, 000\, 000$ and $a_{21} > 3\, 000\, 000\mathbin{:}$

$$


\begin{aligned}𝑎_{20} & =𝑎_{1}⋅𝑟^{20−1}=3⋅2^{19}=1\,572\,864<3\,000\,000 \\ 𝑎_{21} & =𝑎_{1}⋅𝑟^{21−1}=3⋅2^{20}=3\,145\,728>3\,000\,000\,✓\end{aligned}


$$

So, $a_{21}$ is indeed the first term that exceeds $3\,000\,000.$

### Example: Finding the First Term Exceeding a Given Value

#### Question

What is the first term that exceeds $2\,000\,000$ in the following geometric sequence?

$$


\dfrac 1 {32},\: \dfrac 1 4,\: 2,\: 16,\: \ldots


$$

#### Explanation

The first term of the sequence is $a_1=\dfrac{1}{32}$ and the common ratio is

$$


r = \dfrac {\left(\dfrac 1 {4}\right)} {\left(\dfrac 1 {32} \right)} = 8.


$$

So, the $n$th term of the sequence can be written as follows:

$$


\begin{aligned}𝑎_{𝑛} & =𝑎_{1}⋅𝑟^{𝑛−1} \\ & =\frac{1}{32}⋅8^{𝑛−1} \\ & =\frac{2}{64}⋅8^{𝑛−1} \\ & =\frac{2}{8^{2}}⋅8^{𝑛−1} \\ & =2⋅8^{−2}⋅8^{𝑛−1} \\ & =2⋅8^{𝑛−3}\end{aligned}


$$

We want the $n$th term to be greater than $2\,000\,000.$ So, we set up and solve the corresponding inequality:

$$


\begin{aligned}2⋅8^{𝑛−3} & >2\,000\,000 \\ 8^{𝑛−3} & >1\,000\,000 \\ log⁡(8^{𝑛−3}) & >log⁡(1\,000\,000) \\ (𝑛−3)log⁡(8) & >log⁡(1\,000\,000) \\ 𝑛−3 & >\frac{log⁡(1\,000\,000)}{log⁡(8)} \\ 𝑛 & >\frac{log⁡(1\,000\,000)}{log⁡(8)}+3\end{aligned}


$$

Estimating the right-hand side using a calculator, we get

$$


\dfrac {\log (1\,000\, 000)} {\log (8)} + 3 \approx 9.643.


$$

Therefore, the $10$th term is the first term of the sequence that exceeds $2\,000\,000.$

### Example: Finding the First Term Smaller Than a Given Value

#### Question

What is the first term that is less than $0. 000\,000\,1$ in the following geometric sequence?

$$


16,\: 8,\: 4,\: 2,\: \ldots


$$

#### Explanation

The first term of the sequence is $a_1=16,$ and the common ratio is

$$


r = \dfrac 8 {16} = \dfrac 1 2.


$$

So, the $n$th term of the sequence can be written as

$$


\begin{aligned}𝑎_{𝑛} & =𝑎_{1}⋅𝑟^{𝑛−1} \\ & =16⋅(\frac{1}{2})^{𝑛−1} \\ & =2^{4}⋅2^{1−𝑛} \\ & =2^{5−𝑛}.\end{aligned}


$$

We want the $n$th term to be less than $0.000\,000\,1.$ So, we set up and solve the corresponding inequality:

$$


\begin{aligned}2^{5−𝑛} & <0.000\,000\,1 \\ log⁡(2^{5−𝑛}) & <log⁡(0.000\,000\,1) \\ (5−𝑛)log⁡(2) & <log⁡(0.000\,000\,1) \\ 5−𝑛 & <\frac{log⁡(0.000\,000\,1)}{log⁡(2)} \\ −𝑛 & <\frac{log⁡(0.000\,000\,1)}{log⁡(2)}−5 \\ 𝑛 & >5−\frac{log⁡(0.000\,000\,1)}{log⁡(2)}\end{aligned}


$$

Estimating the right-hand side using a calculator, we get

$$


5 - \dfrac { \log (0.000\, 000\, 1)} {\log (2)} \approx 28.253.


$$

Therefore, the $29$th term is the first term of the sequence that is less than $0. 000\,000\,1.$

### Example: Cases Where the First Term Is Unknown

#### Question

The $4$th term of a geometric sequence is $54,$ and the common ratio is $3.$ What is the first term of this sequence to exceed $1\,000?$

#### Explanation

Since we are given that $a_{4}= 54$ and $r= 3,$ we can use the $n$th term formula to solve for $a_1,$ as follows:

$$


\begin{aligned}a_n&=a_1\cdot r^{n-1}\\[3pt] a_4&=a_1\cdot 3^{4-1}\\[3pt] 54&=a_1\cdot 3^3\\[3pt] 54&=27a_1\\[3pt] a_1&=2 \end{aligned}


$$

So, the $n$th term of the geometric sequence is

$$


\begin{aligned}𝑎_{𝑛} & =𝑎_{1}⋅𝑟^{𝑛−1} \\ & =2⋅3^{𝑛−1}.\end{aligned}


$$

We want the $n$th term to be greater than $1\,000.$ So, we set up and solve the corresponding inequality:

$$


\begin{aligned}2⋅3^{𝑛−1} & >1\,000 \\ 3^{𝑛−1} & >500 \\ log⁡(3)^{𝑛−1} & >log⁡(500) \\ (𝑛−1)log⁡(3) & >log⁡(500) \\ 𝑛−1 & >\frac{log⁡(500)}{log⁡(3)} \\ 𝑛 & >\frac{log⁡(500)}{log⁡(3)}+1\end{aligned}


$$

Estimating the right-hand side using a calculator, we get

$$


\dfrac {\log (500)} {\log (3)} + 1 \approx 6.657.


$$

Therefore, the $7$th term is the first term of the sequence that exceeds $1\,000.$
