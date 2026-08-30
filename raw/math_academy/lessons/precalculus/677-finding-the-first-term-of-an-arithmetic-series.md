# Finding the First Term of an Arithmetic Series

Source: https://www.mathacademy.com/topics/677?courseId=43
Topic ID: 677

## Prerequisites

- [Finding the Sum of an Arithmetic Series](./675-finding-the-sum-of-an-arithmetic-series.md)
- [Solving Systems of Linear Equations Using Elimination: Two Transformations](../algebra-i/4236-solving-systems-of-linear-equations-using-elimination-two-transformations.md)

## Lesson

### Introduction

Suppose that, for an arithmetic series, we are only given

- the sum $S_N$ of the first $N$ terms, and

- the last term $a_N.$

If we want to find the value of the first term of the series, $a_1,$ we can use the following formula for the sum of an arithmetic series:

$$


S_N = \dfrac{N}{2}(a_1 +a_N).


$$

To demonstrate, suppose we have an arithmetic series where the sum of the first $N=20$ terms is $S_{20}=-320$ and the last term is $a_{20}=-35.$ To find the value of the first term, we can substitute these values into the formula above and solve for $a_1\mathbin{:}$

$$


\begin{aligned}−320 & =\frac{20}{2}(𝑎_{1}+(−35)) \\ −320 & =10(𝑎_{1}−35) \\ \frac{−320}{10} & =𝑎_{1}−35 \\ −32 & =𝑎_{1}−35 \\ 𝑎_{1} & =3\end{aligned}


$$

### Example: Finding the First Term of an Arithmetic Series Given the Last Term and the Sum

#### Question

If the sum of the first $20$ terms of an arithmetic series is $S_{20}=560,$ and the last term is $a_{20}=66,$ what is the first term of the series?

#### Explanation

We are given the last term of our series. So, to find the first term, we use the formula for the sum of an arithmetic series in the form

$$


S_N = \dfrac{N}{2}(a_1+a_N),


$$

where $a_1$ is the first term, $a_N$ is the last term, and $N$ is the number of terms.

Substituting $a_{20}=66,$ $N=20,$ and $S_N=560$ into the formula above and solving for $a_1,$ we get

$$


\begin{aligned}560 & =\frac{20}{2}(𝑎_{1}+66) \\ 560 & =10(𝑎_{1}+66) \\ \frac{560}{10} & =𝑎_{1}+66 \\ 56 & =𝑎_{1}+66 \\ 𝑎_{1} & =−10.\end{aligned}


$$

### Finding the First Term of an Arithmetic Series when the Last Term is Not Given

Now, suppose that, for an arithmetic series, we are only given

- the sum $S_N$ of the first $N$ terms, and

- the common difference $d.$

If we want to find the value of the first term of the series, $a_1,$ we can use the following formula for the sum of an arithmetic series:

$$


S_N = \dfrac{N}{2}\big( 2a_1+(N-1)d \big)


$$

For instance, suppose we have an arithmetic series where the sum of the first $N=10$ terms is $S_{10}=55,$ and the common difference is $d=3.$ To find the value of the first term, we can substitute these values into the formula above and solve for $a_1\mathbin{:}$

$$


\begin{aligned}55 & =\frac{10}{2}(2𝑎_{1}+(10−1)3) \\ 55 & =5(2𝑎_{1}+27) \\ 11 & =2𝑎_{1}+27 \\ −16 & =2𝑎_{1} \\ 𝑎_{1} & =−8\end{aligned}


$$

### Example: Finding the First Term of an Arithmetic Series Given the Common Difference and the Sum

#### Question

What is the first term of an arithmetic series if the common difference is $d=2,$ and the sum of the first $50$ terms is $S_{50}=2\,150?$

#### Explanation

We are given the common difference of the series. So, to find the first term, we use the formula for the sum of an arithmetic series in the form

$$


S_N = \dfrac{N}{2}\big( 2a_1+(N-1)d \big),


$$

where $a_1$ is the first term, $d$ is the common difference, and $N$ is the number of terms.

Substituting $N=50,$ $d=2,$ and $S_N=2\,150$ into the formula above and solving for $a_1,$ we have

$$


\begin{aligned}2\,150 & =\frac{50}{2}(2𝑎_{1}+(50−1)(2)) \\ 4\,300 & =50(2𝑎_{1}+98) \\ \frac{4\,300}{50} & =2𝑎_{1}+98 \\ 86 & =2𝑎_{1}+98 \\ −12 & =2𝑎_{1} \\ 𝑎_{1} & =−6.\end{aligned}


$$

### Example: Finding the First Term of an Arithmetic Series Given a Term and the Sum

#### Question

Find the first term of an arithmetic series if its $11$th term is $29$ and the sum of the first $16$ terms of the series is $384.$

#### Explanation

We are given one term of the series. So, to find the first term, we use the formula for the sum of an arithmetic series in the form

$$


S_N = \dfrac{N}{2}\left( 2a_1+(N-1)d \right),


$$

where $a_1$ is the first term, $d$ is the common difference, and $N$ is the number of terms.

Substituting $N = 16$ and $S_N = 384$ into the formula for the sum of an arithmetic series, we have

$$


\begin{aligned}𝑆_{𝑁} & =\frac{𝑁}{2}(2𝑎_{1}+(𝑁−1)𝑑) \\ 384 & =\frac{16}{2}(2𝑎_{1}+(16−1)𝑑) \\ 384 & =8(2𝑎_{1}+15𝑑) \\ \frac{384}{8} & =2𝑎_{1}+15𝑑 \\ 48 & =2𝑎_{1}+15𝑑.\end{aligned}


$$

Also, we can write an equation for the $11$th term of the arithmetic series and substitute in its known value:

$$


\begin{aligned}𝑎_{𝑛} & =𝑎_{1}+(𝑛−1)𝑑 \\ 𝑎_{11} & =𝑎_{1}+(11−1)𝑑 \\ 29 & =𝑎_{1}+10𝑑\end{aligned}


$$

As a result, we obtain the following system of equations:

$$


\begin{aligned}29=𝑎_{1}+10𝑑 \\ 48=2𝑎_{1}+15𝑑\end{aligned}


$$

To solve this system, we multiply the first equation by $-2$ and add the result to the second equation:

$$


\begin{aligned}−58 & =−2𝑎_{1}−20𝑑 \\ 48 & =2𝑎_{1}+15𝑑 \\ −10 & =−5𝑑 \\ 𝑑 & =2\end{aligned}


$$

Finally, substituting $d = 2$ into the first equation, we obtain

$$


\begin{aligned}29 & =𝑎_{1}+10(2) \\ 29 & =𝑎_{1}+20 \\ 𝑎_{1} & =9.\end{aligned}


$$
