# The Sum of a Finite Geometric Series

Source: https://www.mathacademy.com/topics/1016?courseId=43
Topic ID: 1016

## Prerequisites

- [Determining Indexes of Terms in Geometric Sequences](../algebra-i/685-determining-indexes-of-terms-in-geometric-sequences.md)

## Lesson

### Introduction

A **geometric series** is a sum of terms of a geometric sequence. For example, given the following seven terms of a geometric sequence,

$$


2, \: 6, \: 18, \: 54, \: 162, \: 486, \: 1\, 458


$$

the corresponding geometric series is

$$


S_7 = 2 + 6 +18 + 54 + 162 + 486 + 1\, 458.


$$

To compute the sum of the series, one way is to add up the terms individually. But that would take a long time.

Instead, we can use the formula for the sum of the first $N$ terms of a geometric series, given by

$$


S_N = a_1\dfrac{(1-r^N)}{1-r},


$$

where $a_1$ is the first term of the series and $r$ is the common ratio.

Let's apply this formula to find $S_7.$ First, we determine the common ratio $r\mathbin{:}$

$$


r = \dfrac {a_2}{a_1} = \dfrac 6 2 = 3


$$

Now, we can determine $S_7\mathbin{:}$

$$


\begin{aligned}𝑆_{7} & =𝑎_{1}\frac{(1−𝑟^{7})}{1−𝑟} \\ & =2\frac{(1−3^{7})}{1−3} \\ & =2\frac{(1−2\,187)}{−2} \\ & =2\,186\end{aligned}


$$

### Example: Calculating the Sum of a Geometric Series

#### Question

Compute the sum of the first $7$ terms of the geometric series $3+6+12+\cdots$

#### Explanation

Given a geometric series, the sum of the first $N$ terms is given by the formula

$$


S_N = a_1\dfrac{(1-r^N)}{1-r},


$$

where $a_1$ is the first term of the series and $r$ is the common ratio.

In our case, $a_1 = 3.$ To find the value of $r,$ we find the ratio of the first two terms in the series:

$$


r = \dfrac{a_2}{a_1} = \dfrac{6}{3} = 2


$$

If we substitute $a_1 = 3,$ $N = 7,$ and $r = 2$ into our formula, we obtain

$$


\begin{aligned}𝑆_{7} & =3⋅\frac{1−2^{7}}{1−2} \\ & =3⋅\frac{1−2^{7}}{−1} \\ & =−3(−127) \\ & =381.\end{aligned}


$$

### Example: Calculating the Sum of a Geometric Series With a Negative Common Ratio

#### Question

Compute the sum of the first $6$ terms of the geometric series $2 -8 + 32 - 128 + \cdots$

#### Explanation

Given a geometric series, the sum of the first $N$ terms is given by the formula

$$


S_N = a_1\dfrac{(1-r^N)}{1-r},


$$

where $a_1$ is the first term of the series and $r$ is the common ratio.

In our case, $a_1 = 2.$ To find the value of $r,$ we find the ratio of the first two terms in the series:

$$


r = \dfrac{a_2}{a_1} = \dfrac{-8}{2} = -4


$$

If we substitute $a_1 = 2$ and $r = -4$ in the formula, we obtain

$$


\begin{aligned}𝑆_{6} & =2⋅\frac{1−(−4)^{6}}{1−(−4)} \\ & =2⋅\frac{1−4^{6}}{1+4} \\ & =2⋅\frac{−4\,095}{5} \\ & =−1\,638.\end{aligned}


$$

### Example: Calculating the Sum of a Geometric Series Given the Last Term of the Series

#### Question

What is the sum of the geometric series $1 + 6 + 36 + \cdots + 46\,656?$

**

#### Explanation

The sum of the first $N$ terms of a geometric series is given by the formula

$$


S_N = a_1\dfrac{(1-r^N)}{1-r},


$$

where $a_1$ is the first term of this series, and $r$ is the common ratio. In our case, we have $a_1 = 1.$

To find $r,$ we find the ratio of the consecutive terms $a_1$ and $a_2 \mathbin{:}$

$$


r = \dfrac{a_2}{a_1} = \dfrac{6}{1} = 6


$$

Now we must determine $N$ (the index of the last term). To do this, we use the fact that

$$


a_N = a_1 \cdot r^{N-1} .


$$

Therefore, using the hint, we get

$$


\begin{aligned}46\,656 & =1⋅6^{𝑁−1} \\ 46\,656 & =6^{𝑁−1} \\ 6^{6} & =6^{𝑁−1} \\ 6 & =𝑁−1 \\ 𝑁 & =7.\end{aligned}


$$

Finally, if we substitute $a_1 = 1,$ $r = 6,$ and $N = 7$ in the formula for $S_N,$ we get

$$


\begin{aligned}𝑆_{7} & =1⋅\frac{1−6^{7}}{1−6} \\ & =\frac{6^{7}−1}{5} \\ & =\frac{279\,935}{5} \\ & =55\,987.\end{aligned}


$$

### Example: Calculating the Sum of a Geometric Series Given Two Consecutive Terms of the Series

#### Question

The second term of a geometric series is $20$ and the third term is $100.$ What is the sum of the first $6$ terms?

#### Explanation

The sum of the first $N$ terms of a geometric series is given by the formula

$$


S_N = a_1\dfrac{(1-r^N)}{1-r},


$$

where $a_1$ is the first term of the series, and $r$ is the common ratio.

To find $r,$ we find the ratio of the consecutive terms $a_2$ and $a_3 \mathbin{:}$

$$


r = \dfrac{a_3}{a_2} = \dfrac{100}{20} = 5


$$

Now we must determine the value of $a_1.$ To do this, we use the formula for the $n$th term, which states that

$$


a_n = a_1 \cdot r^{n-1}.


$$

For $n = 2,$ we get

$$


\begin{aligned}𝑎_{2} & =𝑎_{1}⋅5^{2−1} \\ 20 & =𝑎_{1}⋅5 \\ 𝑎_{1} & =4.\end{aligned}


$$

Finally, if we substitute $a_1 = 4,$ $N = 6,$ and $r = 5$ into the formula for $S_N,$ we obtain

$$


\begin{aligned}𝑆_{6} & =4⋅\frac{1−5^{6}}{1−5} \\ & =4⋅\frac{1−5^{6}}{−4} \\ & =5^{6}−1 \\ & =15\,624.\end{aligned}


$$

### Proof of the Formula for the Sum of a Geometric Series

Let's now prove the formula. We want to find the sum

$$


S_N = a_1 + a_2 + a_3 + \dots + a_N.


$$

The formula for the $n$th term is

$$


a_n = a_1 \cdot r^{n - 1}.


$$

Plugging this expression into $S_N,$ we get

$$


S_N = a_1 + a_1 \cdot r + a_1 \cdot r ^2 + \dots + a_1 \cdot r ^ {N - 1}.


$$

Now, let's write down $-r S_N$ underneath the expression for $S_N\mathbin{:}$

$$


\begin{aligned}𝑆_{𝑁} & =𝑎_{1}+𝑎_{1}⋅𝑟+𝑎_{1}⋅𝑟^{2}+𝑎_{1}⋅𝑟^{3}+⋯+𝑎_{1}⋅𝑟^{𝑁−1} \\ −𝑟⋅𝑆_{𝑁} & = −𝑎_{1}⋅𝑟−𝑎_{1}⋅𝑟^{2}−𝑎_{1}⋅𝑟^{3}−⋯−𝑎_{1}⋅𝑟^{𝑁−1}−𝑎_{1}⋅𝑟^{𝑁}.\end{aligned}


$$

Summing the two equations above, we get

$$


\begin{aligned}𝑆_{𝑁}−𝑟⋅𝑆_{𝑁} & =𝑎_{1}+(𝑎_{1}⋅𝑟−𝑎_{1}⋅𝑟)+(𝑎_{1}⋅𝑟^{2}−𝑎_{1}⋅𝑟^{2})+⋯ \\ & +(𝑎_{1}⋅𝑟^{𝑁−1}−𝑎_{1}⋅𝑟^{𝑁−1})−𝑎_{1}⋅𝑟^{𝑁}.\end{aligned}


$$

We see that all terms of $S_N$ are canceled but the first and the last. So we get

$$


\begin{aligned}𝑆_{𝑁}−𝑟⋅𝑆_{𝑁} & =𝑎_{1}−𝑎_{1}⋅𝑟^{𝑁} \\ 𝑆_{𝑁}(1−𝑟) & =𝑎_{1}(1−𝑟^{𝑁}) \\ 𝑆_{𝑁} & =𝑎_{1}\frac{(1−𝑟^{𝑁})}{1−𝑟}.\end{aligned}


$$
