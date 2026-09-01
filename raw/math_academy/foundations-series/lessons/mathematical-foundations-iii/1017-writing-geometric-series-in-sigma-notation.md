# Writing Geometric Series in Sigma Notation

Source: https://www.mathacademy.com/topics/1017?courseId=136
Topic ID: 1017

## Prerequisites

- [Sigma Notation](../../../high-school/integrated-math-honors/lessons/integrated-math-ii-honors/673-sigma-notation.md)
- [Determining Indexes of Terms in Geometric Sequences](../../../high-school/traditional/lessons/algebra-i/685-determining-indexes-of-terms-in-geometric-sequences.md)

## Lesson

### Introduction

We can write down a geometric series in a compact way using the sigma notation

$$


S = \displaystyle\sum_{n=1}^N a_1r^{n-1},


$$

where $a_1$ is the first term of the series, $r$ is the common ratio, and $N$ is the number of terms in the series.

For instance, suppose we wish to write the following geometric series in sigma notation:

$$


S= 2+4+8+16+32+64+128


$$

In this case, $a_1 = 2$ and $N = 7.$ To find $r,$ we calculate the ratio of the first two terms in the series:

$$


r = \dfrac{a_2}{a_1} = \dfrac{4}{2} = 2


$$

Therefore, expressing the geometric series given in sigma notation, we obtain

$$


2+4+8+16+32+64+128 = \sum_{n=1}^{7} 2\cdot 2^{n-1}.


$$

Finally, we can simplify the above series using the laws of exponents, as follows:

$$


\begin{aligned}\underset{\underset{𝑛=1}{∑}}{\overset{}{7}}2⋅2^{𝑛−1} & =\underset{\underset{𝑛=1}{∑}}{\overset{}{7}}2⋅2^{𝑛}⋅2^{−1} \\ & =\underset{\underset{𝑛=1}{∑}}{\overset{}{7}}2⋅2^{𝑛}⋅\frac{1}{2} \\ & =\underset{\underset{𝑛=1}{∑}}{\overset{}{7}}2⋅\frac{1}{2}⋅2^{𝑛} \\ & =\underset{\underset{𝑛=1}{∑}}{\overset{}{7}}2^{𝑛}\end{aligned}


$$

### Example: Writing a Geometric Series Using Sigma Notation

#### Question

Write the geometric series $4+ 12 + 36 +108+324$ using sigma notation.

#### Explanation

We must express the given series in the form

$$


\sum_{n=1}^{N}a_1 r^{n-1},


$$

where $a_1$ is the first term of the series, $r$ is the common ratio, and $N$ is the number of terms in the series. In this case, $a_1 = 4$ and $N = 5.$

To find $r,$ we calculate the ratio of the first two terms in the series:

$$


r = \dfrac{a_2}{a_1} = \dfrac{12}{4} = 3


$$

Therefore, expressing the geometric series given in sigma notation, we obtain

$$


\begin{aligned}4+12+36+108+324 & =\underset{\underset{𝑛=1}{∑}}{\overset{}{5}}4⋅3^{𝑛−1}.\end{aligned}


$$

### Example: Writing a Geometric Series Using Sigma Notation With Simplifications

#### Question

Express the geometric series $4+8+16+32+64$ using sigma notation.

#### Explanation

First, we must express the given series in the form

$$


\sum_{n=1}^{N}a_1 r^{n-1},


$$

where $a_1$ is the first term of the series, $r$ is the common ratio, and $N$ is the number of terms in the series. In this case, $a_1 =4$ and $N = 5.$

To find $r,$ we calculate the ratio of the first two terms in the series:

$$


r = \dfrac{a_2}{a_1} = \dfrac{8}{4} = 2


$$

Now, expressing the geometric series given in sigma notation, we obtain

$$


4+8+16+32+64 = \sum_{n=1}^{5}4 \cdot 2^{n - 1}.


$$

Finally, we can simplify the above series using the laws of exponents, as follows:

$$


\begin{aligned}\underset{\underset{𝑛=1}{∑}}{\overset{}{5}}4⋅2^{𝑛−1} & =\underset{\underset{𝑛=1}{∑}}{\overset{}{5}}4⋅2^{𝑛}⋅2^{−1} \\ & =\underset{\underset{𝑛=1}{∑}}{\overset{}{5}}4⋅2^{𝑛}⋅\frac{1}{2} \\ & =\underset{\underset{𝑛=1}{∑}}{\overset{}{5}}4⋅\frac{1}{2}⋅2^{𝑛} \\ & =\underset{\underset{𝑛=1}{∑}}{\overset{}{5}}2⋅2^{𝑛}\end{aligned}


$$

### Example: Writing a Geometric Series With a Negative Common Ratio Using Sigma Notation

#### Question

Write the geometric series $1 - 4 + 16 - 64 + 256$ using sigma notation.

#### Explanation

First, we must express the given series in the form

$$


\sum_{n=1}^{N}a_1 r^{n-1},


$$

where $a_1$ is the first term of the series, $r$ is the common ratio, and $N$ is the number of terms in the series. In this case, $a_1 = 1$ and $N = 5.$

To find $r,$ we calculate the ratio of the first two terms in the series:

$$


r = \dfrac{a_2}{a_1} = \dfrac{-4}{1} = -4


$$

So, expressing the geometric series given in sigma notation, we obtain

$$


1 - 4 + 16 - 64 + 256 = \sum_{n=1}^{5} 1 \cdot (-4)^{n - 1}.


$$

Finally, we can simplify the above using the laws of exponents, as follows:

$$


\begin{aligned}1−4+16−64+256 & =\underset{\underset{𝑛=1}{∑}}{\overset{}{5}}1⋅(−4)^{𝑛−1} \\ & =\underset{\underset{𝑛=1}{∑}}{\overset{}{5}}(−4)^{𝑛}(−4)^{−1} \\ & =\underset{\underset{𝑛=1}{∑}}{\overset{}{5}}(−4)^{𝑛}(−\frac{1}{4}) \\ & =\underset{\underset{𝑛=1}{∑}}{\overset{}{5}}(−\frac{1}{4})(−4)^{𝑛}\end{aligned}


$$

### Example: Writing a Geometric Series Using Sigma Notation by Calculating the Number of Terms

#### Question

Express the geometric series $1+ 3+ 9+ \cdots + 243$ using sigma notation.

#### Explanation

We must express the given series in the form

$$


\sum_{n=1}^{N}a_1 r^{n-1},


$$

where $a_1$ denotes the first term of the series, $r$ denotes the common ratio, and $N$ denotes the number of terms in the series. In this case, $a_1 = 1.$

To find $r,$ we find the ratio of the consecutive terms $a_1$ and $a_2 \mathbin{:}$

$$


r = \dfrac{a_2}{a_1} = \dfrac{3}{1} = 3


$$

Now we must determine $N$ (the index of the last term). To do this, we use the fact that

$$


a_N = a_1 \cdot r^{N - 1} .


$$

Therefore,

$$


\begin{aligned}𝑎_{𝑁} & =𝑎_{1}⋅𝑟^{𝑁−1} \\ 243 & =1⋅3^{𝑁−1} \\ 3^{5} & =3^{𝑁−1} \\ 5 & =𝑁−1 \\ 𝑁 & =6.\end{aligned}


$$

Expressing the geometric series in sigma notation, we obtain

$$


\begin{aligned}1+3+9+⋯+243 & =\underset{\underset{𝑛=1}{∑}}{\overset{}{6}}1⋅3^{𝑛−1} \\ & =\underset{\underset{𝑛=1}{∑}}{\overset{}{6}}3^{𝑛−1}.\end{aligned}


$$
