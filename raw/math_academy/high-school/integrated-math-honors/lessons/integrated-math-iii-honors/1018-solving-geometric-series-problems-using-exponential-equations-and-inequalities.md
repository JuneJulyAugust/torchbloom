# Solving Geometric Series Problems Using Exponential Equations and Inequalities

Source: https://www.mathacademy.com/topics/1018?courseId=101
Topic ID: 1018

## Prerequisites

- [Sums of Finite Geometric Series Given in Sigma Notation](./690-sums-of-finite-geometric-series-given-in-sigma-notation.md)
- [The Sum of the First N Terms of a Geometric Series](./692-the-sum-of-the-first-n-terms-of-a-geometric-series.md)
- [Solving Inequalities Involving Exponential Functions](./2857-solving-inequalities-involving-exponential-functions.md)

## Lesson

### Introduction

Given the sum of a geometric series, we can find the number of terms in the sequence. Let's find the number of terms $N$ in the following geometric series:

$$


4+12+36+\cdots + a_N = 484


$$

First, we determine the common ratio $r$ for this geometric series:

$$


\begin{aligned}𝑟 & =\frac{𝑎_{2}}{𝑎_{1}}=\frac{12}{4}=3\end{aligned}


$$

The sum of the first $N$ terms of a geometric series can be determined by the formula

$$


S_N = \dfrac{a_1 (1-r^N) }{1-r}.


$$

In this case, $a_1= 4$ and $r = 3.$ Substituting our values into the above formula, we get the following:

$$


\begin{aligned}484 & =\frac{4(1−3^{𝑁})}{1−3} \\ 484 & =−2(1−3^{𝑁}) \\ 484 & =2(3^{𝑁}−1) \\ 242 & =3^{𝑁}−1 \\ 243 & =3^{𝑁}\end{aligned}


$$

Now, we rewrite $243$ as $3^{5},$ which gives

$$


\begin{aligned}3^{𝑁} & =3^{5}.\end{aligned}


$$

Finally, since both sides of the equation share the same base $(3),$ we equate the exponents:

$$


\begin{aligned}𝑁 & =5\end{aligned}


$$

Therefore, the series has $5$ terms.

### Example: Computing the Number of Terms in a Geometric Series

#### Question

Given that the sum of the geometric series $3+6+12+ \cdots + a_N$ is equal to $765,$ how many terms are there in the series?

#### Explanation

First, we determine the common ratio $r$ for this geometric series:

$$


\begin{aligned}𝑟 & =\frac{𝑎_{2}}{𝑎_{1}}=\frac{6}{3}=2\end{aligned}


$$

The sum of the first $N$ terms of a geometric series can be determined by the formula

$$


S_N = \dfrac{a_1 (1-r^N) }{1-r}.


$$

In this case, $a_1= 3$ and $r = 2.$ Substituting our values into the above formula, we get the following:

$$


\begin{aligned}765 & =\frac{3(1−2^{𝑁})}{1−2} \\ 765 & =−3(1−2^{𝑁}) \\ 765 & =3(2^{𝑁}−1) \\ 255 & =2^{𝑁}−1 \\ 256 & =2^{𝑁}\end{aligned}


$$

Now, we rewrite $256$ as $2^{8},$ which gives

$$


\begin{aligned}2^{𝑁} & =2^{8}.\end{aligned}


$$

Finally, since both sides of the equation share the same base $(2),$ we equate the exponents:

$$


\begin{aligned}𝑁 & =8\end{aligned}


$$

Therefore, the series has $8$ terms.

### Computing the Number of Terms Required to Bound a Geometric Series

Suppose now we have a geometric series

$$


2 + 4 + 8 + 16 + 32+ \dots,


$$

and we want to find the least value $N$ so that the sum of the first $N$ terms exceeds $620.$ That is, we want to find the least value of $N$ such that

$$


𝑁


$$

We can do this in a similar way to before, as if the sum were *equal to* $620,$ but using an inequality in place of an equals sign.

First, we determine the common ratio $r$ for this geometric series:

$$


\begin{aligned}𝑟 & =\frac{𝑎_{2}}{𝑎_{1}}=\frac{4}{2}=2\end{aligned}


$$

The sum of the first $N$ terms of a geometric series can be determined by the formula

$$


S_N = \dfrac{a_1 \left( 1-r^N\right) }{1-r}.


$$

Substituting $a_1= 2$ and $r =2,$ we get the following:

$$


\begin{aligned}𝑆_{𝑁} & =\frac{2(1−2^{𝑁})}{1−2} \\ & =2(2^{𝑁}−1)\end{aligned}


$$

If this is to exceed $620,$ then the following must be true:

$$


\begin{aligned}2(2^{𝑁}−1) & >620 \\ 2^{𝑁}−1 & >310 \\ 2^{𝑁} & >311\end{aligned}


$$

Now, we take $\log$ of both sides of the equation and use the power rule to solve for $N,$ as follows:

$$


\begin{aligned}log⁡(2^{𝑁}) & >log⁡(311) \\ 𝑁log⁡2 & >log⁡(311) \\ 𝑁 & >\frac{log⁡(311)}{log⁡2} \\ 𝑁 & >8.281…\end{aligned}


$$

Since $N$ must be an integer, we conclude that there need to be at least $9$ terms for the given sum to exceed $620.$

### Example: Computing the Number of Terms Required to Bound a Geometric Series From Below

#### Question

Find the least number of terms $N$ such that the sum $1+4+16+\cdots+a_N$ exceeds $240.$

#### Explanation

Note that $1+2+4+8+\cdots+a_N$ is the sum of a geometric series because the ratio of any two consecutive terms is always the same.

First, we determine the common ratio $r$ for this geometric series:

$$


\begin{aligned}𝑟 & =\frac{𝑎_{2}}{𝑎_{1}}=\frac{4}{1}=4\end{aligned}


$$

The sum of the first $N$ terms of a geometric series can be determined by the formula

$$


S_N = \dfrac{a_1 (1-r^N) }{1-r}.


$$

Substituting $a_1= 1$ and $r =4,$ we get the following:

$$


\begin{aligned}𝑆_{𝑁} & =1⋅\frac{1−4^{𝑁}}{1−4} \\ & =\frac{4^{𝑁}−1}{3}\end{aligned}


$$

If this is to exceed $240,$ then the following must be true:

$$


\begin{aligned}\frac{4^{𝑁}−1}{3} & >240 \\ 4^{𝑁}−1 & >720 \\ 4^{𝑁} & >721\end{aligned}


$$

Now, we take $\log$ of both sides of the equation and use the power rule to solve for $N,$ as follows:

$$


\begin{aligned}log⁡(4^{𝑁}) & >log⁡(721) \\ 𝑁log⁡4 & >log⁡(721) \\ 𝑁 & >\frac{log⁡(721)}{log⁡4} \\ 𝑁 & >4.746…\end{aligned}


$$

Since $N$ must be an integer, we conclude that there need to be at least $5$ terms for the given sum to exceed $240.$

### Example: Computing the Number of Terms Required to Bound a Geometric Series From Above

#### Question

Find the greatest number of terms $N$ such that the geometric series $2+4+8+\cdots+a_N$ does not exceed $1\,000.$

#### Explanation

Note that $2+4+8+\cdots+a_N$ is the sum of a geometric series since the ratio of any two consecutive terms is constant.

First, we determine the common ratio $r$ for this geometric series:

$$


\begin{aligned}𝑟 & =\frac{𝑎_{2}}{𝑎_{1}}=\frac{4}{2}=2\end{aligned}


$$

The sum of the first $N$ terms of a geometric series can be determined by the formula

$$


S_N = \dfrac{a_1 (1-r^N) }{1-r}.


$$

Substituting $a_1= 2$ and $r = 2$ into the above, we get the following:

$$


\begin{aligned}𝑆_{𝑁} & =2⋅\frac{1−2^{𝑁}}{1−2} \\ & =2⋅\frac{1−2^{𝑁}}{−1} \\ & =2(2^{𝑁}−1)\end{aligned}


$$

If this is to not exceed $1\,000,$ then the following must be true:

$$


\begin{aligned}2(2^{𝑁}−1) & <1\,000 \\ 2^{𝑁}−1 & <500 \\ 2^{𝑁} & <501\end{aligned}


$$

Now, we take $\log$ of both sides of the equation and use the power rule to solve for $N,$ as follows:

$$


\begin{aligned}log⁡(2^{𝑁}) & <log⁡(501) \\ 𝑁log⁡(2) & <log⁡(501) \\ 𝑁 & <\frac{log⁡(501)}{log⁡2} \\ 𝑁 & <8.968…\end{aligned}


$$

Since $N$ must be an integer, we conclude that there need to be at most $8$ terms for the given sum not to exceed $1\,000.$
