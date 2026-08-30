# The Special Case of the Binomial Theorem

Source: https://www.mathacademy.com/topics/3764?courseId=43
Topic ID: 3764

## Prerequisites

- [Expanding a Binomial Using Binomial Coefficients](./1156-expanding-a-binomial-using-binomial-coefficients.md)

## Lesson

### Introduction

Let's recall the binomial theorem for positive integer $n\mathbin{:}$

$$


{(a + b)^n} = {n \choose 0}{a^n}{b^0} + {n \choose 1}{a^{n - 1}}{b^1} + {n \choose 2}{a^{n - 2}}{b^2} + \cdots + {n \choose n}{a^0}{b^n}


$$

If we substitute $a=1$ and $b=x$ into the binomial theorem, we obtain (after some manipulations)

$$


{(1 + x)^n} = 1 + nx + \dfrac{{n(n - 1)}}{{2!}}{x^2} + \dfrac{{n(n - 1)(n - 2)}}{{3!}}{x^3} +\cdots + x^n.


$$

We'll derive this result at the end of the lesson.

It's often useful to use this version of the binomial formula whenever there is only one variable and the other term equals $1.$

### Example: Expanding a Binomial

#### Question

Find the first $3$ terms in ascending powers of $a$ of the binomial expansion of $(1+3a)^5.$

#### Explanation

The first $3$ terms of the binomial expansion for ${(1 + x)^n}$ are given by

$$


{(1 + x)^n} = 1 + nx + \frac{{n(n - 1)}}{{2!}}{x^2} + \cdots .


$$

By substituting $x=3a$ and $n=5$ into the above formula, we obtain

$$


\begin{aligned}(1+3𝑎)^{5} & =1+5(3𝑎)+\frac{5(5−1)}{2!}(3𝑎)^{2}+⋯ \\ & =1+5(3𝑎)+\frac{5(4)}{2}(9𝑎^{2})+⋯ \\ & =1+15𝑎+90𝑎^{2}+⋯.\end{aligned}


$$

### Example: Expanding a Binomial With Negative Coefficients

#### Question

Find the first $3$ terms in ascending powers of $m$ of the binomial expansion of $\left(1 - \dfrac{4m}{3}\right)^7.$

#### Explanation

The first $3$ terms of the binomial expansion for ${(1 + x)^n}$ are given by

$$


{(1 + x)}^n = 1 + nx + \frac{{n(n - 1)}}{{2!}}{x^2} + \cdots .


$$

By substituting $x=-\dfrac{4m}{3}$ and $n=7$ into the above formula, we obtain

$$


\begin{aligned}(1−\frac{4𝑚}{3})^{7} & =1+7(−\frac{4𝑚}{3})+\frac{7(7−1)}{2!}(−\frac{4𝑚}{3})^{2}+⋯ \\ & =1+7(−\frac{4𝑚}{3})+\frac{7(6)}{2}(−\frac{4𝑚}{3})^{2}+⋯ \\ & =1+7(−\frac{4𝑚}{3})+\frac{7(6)}{2}(\frac{16𝑚^{2}}{9})+⋯ \\ & =1−\frac{28𝑚}{3}+\frac{112𝑚^{2}}{3}+⋯.\end{aligned}


$$

### Example: Calculating a Coefficient of a Binomial Expansion

#### Question

Determine the coefficient of $r^3$ in the expansion of $\left(1 - 3r \right)^{10}.$

#### Explanation

The binomial expansion for $(1 + x)^n$ is given by

$$


(1 + x)^n = 1 + nx + \frac{n(n - 1)}{2!} x^2 + \cdots .


$$

In particular, the $x^3$ term is given by

$$


\dfrac{n(n-1)(n-2)}{3!} x^3.


$$

Replacing $x$ with $-3r$ and $n$ with $10$ in the above expression, we get

$$


\begin{aligned}\frac{10(10−1)(10−2)}{3!}(−3𝑟)^{3} & =\frac{10(9)(8)}{6}⋅(−3)^{3}⋅𝑟^{3} \\ & =\frac{10(9)(8)}{6}⋅(−27)𝑟^{3} \\ & =−3\,240𝑟^{3}.\end{aligned}


$$

Therefore, the coefficient of $r^3$ is $-3\,240.$

### Deriving the Special Case From the General Binomial Theorem

Let's derive our special case formula from the binomial theorem for positive integer $n\mathbin{:}$

$$


{(a + b)^n} = {n \choose 0}{a^n}{b^0} + {n \choose 1}{a^{n - 1}}{b^1} + {n \choose 2}{a^{n - 2}}{b^2} + {n \choose 3}{a^{n - 3}}{b^3} + \cdots + {n \choose n}{a^0}{b^n}


$$

Substituting $a=1$ and $b=x$ into the above, we get the following:

$$


\begin{aligned}(1+𝑥)^{𝑛} & =(\frac{𝑛}{0})⋅1^{𝑛}⋅𝑥^{0}+(\frac{𝑛}{1})⋅1^{𝑛−1}⋅𝑥^{1}+(\frac{𝑛}{2})⋅1^{𝑛−2}⋅𝑥^{2}+⋯+(\frac{𝑛}{𝑛})⋅1^{0}⋅𝑥^{𝑛} \\ & =(\frac{𝑛}{0})+(\frac{𝑛}{1})𝑥+(\frac{𝑛}{2})𝑥^{2}+(\frac{𝑛}{3})𝑥^{3}+⋯+(\frac{𝑛}{𝑛})𝑥^{𝑛}\end{aligned}


$$

Now, recall that

$$


{n \choose r} = \dfrac{n!}{(n-r)!\cdot r!}


$$

and the particular cases

$$


{n \choose 0} = 1, \qquad {n \choose 1} = n.


$$

We can now continue to simplify our binomial expansion as follows:

$$


\begin{aligned}(1+𝑥)^{𝑛} & =(\frac{𝑛}{0})+(\frac{𝑛}{1})𝑥+(\frac{𝑛}{2})𝑥^{2}+(\frac{𝑛}{3})𝑥^{3}+⋯+(\frac{𝑛}{𝑛})𝑥^{𝑛} \\ & =1+𝑛⋅𝑥+\frac{𝑛!}{(𝑛−2)!⋅2!}⋅𝑥^{2}+\frac{𝑛!}{(𝑛−3)!⋅3!}⋅𝑥^{3}+⋯+𝑥^{𝑛} \\ & =1+𝑛⋅𝑥+\frac{𝑛(𝑛−1)(𝑛−2)!}{(𝑛−2)!⋅2!}⋅𝑥^{2}+\frac{𝑛(𝑛−1)(𝑛−2)(𝑛−3)!}{(𝑛−3)!⋅3!}⋅𝑥^{3}+⋯+𝑥^{𝑛} \\ & =1+𝑛⋅𝑥+\frac{𝑛(𝑛−1)(𝑛−2)!}{(𝑛−2)!⋅2!}⋅𝑥^{2}+\frac{𝑛(𝑛−1)(𝑛−2)(𝑛−3)!}{(𝑛−3)!⋅3!}⋅𝑥^{3}+⋯+𝑥^{𝑛} \\ & =1+𝑛𝑥+\frac{𝑛(𝑛−1)}{2!}𝑥^{2}+\frac{𝑛(𝑛−1)(𝑛−2)}{3!}𝑥^{3}+⋯+𝑥^{𝑛},\end{aligned}


$$

which gives the desired result.
