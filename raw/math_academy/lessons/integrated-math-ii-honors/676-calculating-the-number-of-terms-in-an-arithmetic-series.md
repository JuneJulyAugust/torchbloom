# Calculating the Number of Terms in an Arithmetic Series

Source: https://www.mathacademy.com/topics/676?courseId=128
Topic ID: 676

## Prerequisites

- [Solving Quadratic Equations Using a Difference of Squares](../algebra-i/394-solving-quadratic-equations-using-a-difference-of-squares.md)
- [The Quadratic Formula](../algebra-i/422-the-quadratic-formula.md)
- [Finding the First Term of an Arithmetic Series](./677-finding-the-first-term-of-an-arithmetic-series.md)
- [Solving Quadratic Equations with Leading Coefficients by Factoring](../algebra-i/1422-solving-quadratic-equations-with-leading-coefficients-by-factoring.md)

## Lesson

### Introduction

Suppose that we have an arithmetic sequence

$$


3, \: 9, \:15, \: 21, \: \ldots


$$

with the common difference $d=6,$ and we're told that the sum to $N$ its terms is

$$


𝑁


$$

To find the value of $N,$ the number of terms in the sequence we are summing, we can use the formula

$$


S_N = \dfrac{N}{2} \big(2a_1 + (N-1) d\big).


$$

So, we substitute $a_1=3,$ $d=6,$ and $S_N=192$ into the above and solve for $N,$ as follows:

$$


\begin{aligned}𝑆_{𝑁} & =\frac{𝑁}{2}(2𝑎_{1}+(𝑁−1)𝑑) \\ 192 & =\frac{𝑁}{2}(2⋅3+(𝑁−1)⋅6) \\ 192 & =\frac{𝑁}{2}(6+6𝑁−6) \\ 192 & =\frac{𝑁}{2}(6𝑁) \\ 192 & =3𝑁^{2} \\ 64 & =𝑁^{2} \\ 𝑁 & =±8\end{aligned}


$$

Notice that we must take the positive square root because $N$ can't be negative. So, we conclude that our series has $N=8$ terms.

### Example: Calculating the Number of Terms in an Arithmetic Series Using the Formula for the Sum

#### Question

The first term of an arithmetic series is $a_1=2,$ the common difference is $d=4,$ and the sum of the series is $S_N=200.$ Find the number of terms $N$ in the series.

#### Explanation

To find the number of terms, we can use the following formula:

$$


S_N = \dfrac N 2 \big(2a_1 + (N-1) d \big)


$$

We substitute $a_1=2,$ $d=4,$ and $S_N=200$ into the above and solve for $N,$ as follows:

$$


\begin{aligned}𝑆_{𝑁} & =\frac{𝑁}{2}(2𝑎_{1}+(𝑁−1)𝑑) \\ 200 & =\frac{𝑁}{2}(2⋅2+(𝑁−1)⋅4) \\ 200 & =\frac{𝑁}{2}(4+4𝑁−4) \\ 200 & =\frac{𝑁}{2}(4𝑁) \\ 200 & =2𝑁^{2} \\ 100 & =𝑁^{2} \\ 𝑁 & =10\end{aligned}


$$

Notice that we have taken the positive square root because $N$ can't be negative.

### Example: Calculating the Number of Terms in an Arithmetic Series Given the Pattern and the Sum

#### Question

Calculate the number of terms in the following arithmetic series:

$$


5+7+9+\cdots = 140


$$

#### Explanation

To solve this problem, we use the formula for the sum of an arithmetic series:

$$


S_{N} = \dfrac{N}{2} \big( 2a_1+(N-1)d \big)


$$

We are given the sum $S_N = 140,$ and the first term $a_1=5.$ Our goal is to find $N,$ the number of terms.

The common difference $d$ can be found as follows:

$$


\begin{aligned}𝑑 & =𝑎_{2}−𝑎_{1} \\ & =7−5 \\ & =2\end{aligned}


$$

Substituting these values into the formula for the sum of an arithmetic series, we have

$$


\begin{aligned}𝑆_{𝑁} & =\frac{𝑁}{2}(2𝑎_{1}+(𝑁−1)𝑑) \\ 140 & =\frac{𝑁}{2}(2(5)+(𝑁−1)(2)) \\ 140 & =\frac{𝑁}{2}(10+2𝑁−2) \\ 140 & =\frac{𝑁}{2}(2𝑁+8) \\ 140 & =𝑁^{2}+4𝑁 \\ 0 & =𝑁^{2}+4𝑁−140.\end{aligned}


$$

For the equation above, the quadratic formula gives

$$


\begin{aligned}𝑁 & =\frac{−4±\sqrt{√4^{2}−4⋅1⋅(−140)}}{2⋅1} \\ & =\frac{−4±\sqrt{√576}}{2} \\ & =\frac{−4±24}{2}.\end{aligned}


$$

So $N=10$ or $N=-14.$ We disregard the negative solution since $N$ must be positive.

Therefore, our series has $N=10$ terms.

### Example: Calculating the Number of Terms in an Arithmetic Series Given Two Terms and the Sum

#### Question

An arithmetic series has the $5$th term $a_{5}=14,$ the $7$th term $a_{7}=19,$ and the sum of the series is $S_N=850.$ Find the number of terms $N$ in the series.

#### Explanation

To solve this problem, we use the formula for the sum of an arithmetic series:

$$


S_N = \dfrac N 2 \big( 2a_1 + (N-1) d \big)


$$

Since we know two terms of the arithmetic series, we can find its common difference:

$$


\begin{aligned}𝑑 & =\frac{𝑎_{7}−𝑎_{5}}{7−5} \\ & =\frac{19−14}{7−5} \\ & =\frac{5}{2} \\ & =2.5\end{aligned}


$$

We know that $a_{5}=14.$ We can compute $a_1$ using the formula for the $n$th term, as follows:

$$


\begin{aligned}𝑎_{𝑛} & =𝑎_{1}+(𝑛−1)𝑑 \\ 𝑎_{5} & =𝑎_{1}+(5−1)⋅2.5 \\ 14 & =𝑎_{1}+4⋅2.5 \\ 14 & =𝑎_{1}+10 \\ 𝑎_{1} & =4\end{aligned}


$$

Now, substituting $a_1=4,$ $d=2.5,$ and $S_N=850$ into the formula for the sum of an arithmetic series, we have

$$


\begin{aligned}𝑆_{𝑁} & =\frac{𝑁}{2}(2𝑎_{1}+(𝑁−1)𝑑) \\ 850 & =\frac{𝑁}{2}(2(4)+(𝑁−1)(2.5)) \\ 850 & =\frac{𝑁}{2}(8+2.5𝑁−2.5) \\ 850⋅2 & =𝑁(5.5+2.5𝑁) \\ 1700 & =2.5𝑁^{2}+5.5𝑁 \\ 2.5𝑁^{2}+5.5𝑁−1\,700 & =0 \\ 5𝑁^{2}+11𝑁−3\,400 & =0.\end{aligned}


$$

For the equation above, the quadratic formula gives

$$


\begin{aligned}𝑁 & =\frac{−(11)±\sqrt{√(−11)^{2}−4⋅5⋅(−3400)}}{2⋅5} \\ & =\frac{−11±\sqrt{√68\,121}}{10} \\ & =\frac{−11±261}{10}.\end{aligned}


$$

So $N=25$ or $N=-27.2.$ We disregard the negative solution since $N$ must be a positive integer.

Therefore, our series has $N=25$ terms.
