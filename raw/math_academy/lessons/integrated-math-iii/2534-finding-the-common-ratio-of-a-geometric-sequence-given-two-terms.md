# Finding the Common Ratio of a Geometric Sequence Given Two Terms

Source: https://www.mathacademy.com/topics/2534?courseId=134
Topic ID: 2534

## Prerequisites

- [The Quotient Rule for Exponents With Algebraic Expressions](../algebra-i/374-the-quotient-rule-for-exponents-with-algebraic-expressions.md)
- [Solving Exponential Equations](../algebra-i/391-solving-exponential-equations.md)
- [The Nth Term of a Geometric Sequence](../algebra-i/680-the-nth-term-of-a-geometric-sequence.md)
- [Solving Equations With Even Exponents Using the Nth Root Method](../algebra-i/1587-solving-equations-with-even-exponents-using-the-nth-root-method.md)
- [Solving Equations With Odd Exponents Using the Nth Root Method](../algebra-i/3748-solving-equations-with-odd-exponents-using-the-nth-root-method.md)

## Lesson

### Introduction

Suppose that we have a *positive* geometric sequence where the second term is $4$ and the fourth term is $64.$ How do we find the common ratio $r?$

This is a little trickier than before because we're not given two consecutive terms, but let's try to figure it out. First, let's denote

$$


a_2 = 4, \qquad a_4 = 64.


$$

The $n$th term of a geometric sequence is given by:

$$


a_n = a_1r^{n-1}


$$

Applying this formula with $n=2$ and $n=4$ gives:

$$


\begin{aligned}𝑎_{2} & =𝑎_{1}𝑟^{2−1}=𝑎_{1}𝑟 \\ 𝑎_{4} & =𝑎_{1}𝑟^{4−1}=𝑎_{1}𝑟^{3}\end{aligned}


$$

Using that $a_2 = 4$ and $a_4 = 64$, we obtain:

$$


\begin{aligned}𝑎_{1}𝑟 & =4 \\ 𝑎_{1}𝑟^{3} & =64\end{aligned}


$$

So now, we have a system of equations to solve. To solve this system, we *divide* the *second* equation above by the *first* equation:

$$


\begin{aligned}\frac{𝑎_{1}𝑟^{3}}{𝑎_{1}𝑟} & =\frac{64}{4} \\ \frac{𝑎_{1}𝑟^{3}}{𝑎_{1}𝑟} & =\frac{64}{4} \\ \frac{𝑟^{3}}{𝑟} & =16 \\ 𝑟^{2} & =16\end{aligned}


$$

Finally, we solve the above equation for $r.$ Note that $16 = 4^2,$ and so we can solve the equation as follows:

$$


\begin{aligned}𝑟^{2} & =16 \\ 𝑟^{2} & =4^{2} \\ 𝑟 & =4\end{aligned}


$$

We disregard the negative solution since our sequence must be positive.

Therefore, the common ratio $r=4.$

### Example: Finding an Equation for the Common Ratio

#### Question

Find the equation for the common ratio of the geometric sequence whose $4$th term is $6$ and whose $9$th term is $192.$

#### Explanation

The formula for the $n$th term of a geometric sequence is given by

$$


a_n = a_1r^{n-1}.


$$

Applying this formula with $n=4$ and $n=9,$ respectively, we have

$$


\begin{aligned}𝑎_{4} & =𝑎_{1}𝑟^{4−1}=𝑎_{1}𝑟^{3}, \\ 𝑎_{9} & =𝑎_{1}𝑟^{9−1}=𝑎_{1}𝑟^{8}.\end{aligned}


$$

Given that $a_4 = 6$ and $a_9 = 192,$ we obtain the following system of equations:

$$


\begin{aligned}𝑎_{1}𝑟^{3}=6 \\ 𝑎_{1}𝑟^{8}=192\end{aligned}


$$

Finally, by dividing the second equation by the first, we get

$$


\begin{aligned}\frac{𝑎_{1}𝑟^{8}}{𝑎_{1}𝑟^{3}} & =\frac{192}{6} \\ \frac{\,𝑎_{1}\,𝑟^{8}}{\,𝑎_{1}\,𝑟^{3}} & =\frac{192}{6} \\ \frac{𝑟^{8}}{𝑟^{3}} & =32 \\ 𝑟^{5} & =32.\end{aligned}


$$

Therefore, the common ratio satisfies $r^5 = 32.$

### Finding the Common Ratio Using a Formula

Finding the common ratio by solving a system of equations is quite a lot of work. Is there an easier way?

Indeed there is. Given two terms of a geometric sequence $a_n$ and $a_m,$ the formula for $r$ is as follows:

$$


r^{n-m} = \dfrac{a_n}{a_m}


$$

Let's demonstrate how this works. Suppose that we have a geometric sequence whose second term is $3$ and whose fifth term is $192.$ What is the common ratio?

Here, we're given $a_5 = 192$ and $a_2 = 3.$ Substituting $n=5$ and $m=2$ into the formula, we get:

$$


\begin{aligned}𝑟^{5−2} & =\frac{𝑎_{5}}{𝑎_{2}} \\ 𝑟^{3} & =\frac{192}{3} \\ 𝑟^{3} & =64\end{aligned}


$$

Finally, we solve the above equation for $r$ by noting that $64 = 4^3\mathbin{:}$

$$


\begin{aligned}𝑟^{3} & =64 \\ 𝑟^{3} & =4^{3} \\ 𝑟 & =4\end{aligned}


$$

So the common ratio is $r=4.$

When dealing with an equation that is **cubic** in $r$ (i.e., contains an $r^3$), then there is only one possible answer, unlike the squared case ($r^2$) where we have to pick from either positive or negative.

### Example: Finding the Common Ratio Using a Formula Given Two Non-Consecutive Terms

#### Question

Find the common ratio of the geometric sequence whose fourth term is $2$ and whose seventh term is $-686.$

#### Explanation

To find the common ratio $r$ of a geometric sequence given two terms $a_m$ and $a_n,$ we use the formula

$$


r^{n-m} = \dfrac{a_n}{a_m}.


$$

In this case, we're given $a_7 = -686$ and $a_4 = 2.$ Substituting $n=7$ and $m=4$ into the formula, we have

$$


\begin{aligned}𝑟^{7−4} & =\frac{𝑎_{7}}{𝑎_{4}} \\ 𝑟^{3} & =\frac{−686}{2} \\ 𝑟^{3} & =−343.\end{aligned}


$$

Finally, by solving the equation for $r,$ we get

$$


\begin{aligned}𝑟^{3} & =−343 \\ 𝑟^{3} & =(−7)^{3} \\ 𝑟 & =−7.\end{aligned}


$$

### Example: Finding the Common Ratio Given Some Additional Information About the Geometric Sequence

#### Question

The third term of a geometric sequence is $80$ and its fifth term is $20.$ Find the common ratio $r$ of this sequence given that $r$ is positive.

#### Explanation

To find the common ratio $r$ of a geometric sequence given two terms $a_m$ and $a_n,$ we use the formula

$$


r^{n-m} = \dfrac{a_n}{a_m}.


$$

In this case, we're given $a_5 = 20$ and $a_3 = 80.$ Substituting $n=5$ and $m=3$ into the formula, we have

$$


\begin{aligned}𝑟^{5−3} & =\frac{𝑎_{5}}{𝑎_{3}} \\ 𝑟^{2} & =\frac{20}{80} \\ 𝑟^{2} & =\frac{1}{4}.\end{aligned}


$$

Finally, solving the equation for $r$ and considering that $r$ is positive, we get

$$


\begin{aligned}𝑟^{2} & =\frac{1}{4} \\ 𝑟^{2} & =(\frac{1}{2})^{2} \\ 𝑟 & =\frac{1}{2}.\end{aligned}


$$
