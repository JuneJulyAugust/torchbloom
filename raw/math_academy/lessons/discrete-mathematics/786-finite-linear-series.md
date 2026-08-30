# Finite Linear Series

Source: https://www.mathacademy.com/topics/786?courseId=109
Topic ID: 786

## Prerequisites

- [Properties of Finite Series](../integrated-math-ii-honors/3958-properties-of-finite-series.md)

## Lesson

### Introduction

If we wish to sum the first $N$ integers, an easy way is to use the following formula:

$$



\begin{aligned}\underset{\underset{𝑛=1}{∑}}{\overset{}{𝑁}}𝑛 & =1+2+3+⋯+(𝑁−1)+𝑁 \\ & =\frac{1}{2}𝑁(𝑁+1)\end{aligned}



$$

As we will see, we can use this simple formula to evaluate any series of the form $\displaystyle{\sum_{n=1}^N (an+b)}.$

### Example: Calculating the Sum of the First N Integers

#### Question

Calculate $\displaystyle\sum_{n=1}^{100} n.$

#### Explanation

Using the formula

$$



\begin{aligned}\underset{\underset{𝑛=1}{∑}}{\overset{}{𝑁}}𝑛 & =\frac{1}{2}𝑁(𝑁+1)\end{aligned}



$$

with $N=100,$ we get

$$



\begin{aligned}\underset{\underset{𝑛=1}{∑}}{\overset{}{100}}𝑛 & =\frac{1}{2}⋅100⋅(100+1) \\ & =\frac{1}{2}⋅100⋅101 \\ & =5\,050.\end{aligned}



$$

### Example: Calculating the Sum of a Finite Linear Series with a Constant Factor

#### Question

Calculate $\displaystyle\sum_{n=1}^{100} 4n.$

#### Explanation

First, we take the factor $4$ outside the summation:

$$



\sum_{n=1}^{100} 4n = 4\sum_{n=1}^{100} n



$$

Now, using the formula

$$



\begin{aligned}\underset{\underset{𝑛=1}{∑}}{\overset{}{𝑁}}𝑛 & =\frac{1}{2}𝑁(𝑁+1)\end{aligned}



$$

with $N=100,$ we get

$$



\begin{aligned}4\underset{\underset{𝑛=1}{∑}}{\overset{}{100}}𝑛 & =4(\frac{1}{2}⋅100⋅101) \\ & =4⋅5\,050 \\ & =20\,200.\end{aligned}



$$

### Example: Calculating the Sum of a Finite Linear Series with a Constant Term

#### Question

Calculate $\displaystyle\sum_{n=1}^{200} (3n+2).$

#### Explanation

We can write the summation as follows:

$$



\begin{aligned}\underset{\underset{𝑛=1}{∑}}{\overset{}{200}}(3𝑛+2) & =\underset{\underset{𝑛=1}{∑}}{\overset{}{200}}3𝑛+\underset{\underset{𝑛=1}{∑}}{\overset{}{200}}2 \\ & =3\underset{\underset{𝑛=1}{∑}}{\overset{}{200}}𝑛+2\underset{\underset{𝑛=1}{∑}}{\overset{}{200}}1\end{aligned}



$$

Let's consider the two series separately.

- For the first series, we use the formula with $N=200,$ and we get

- In the second series, $\displaystyle{\sum_{n=1}^{200} 1}$ is just $1$ added together $200$ times, which is $200 \cdot 1 = 200.$ So, we have

Finally, we have

$$



\sum_{n=1}^{200} (3n+2) = 60\,300 + 400 = 60\,700.



$$

### Derivation of the Formula

Here, we'll derive the formula

$$



\sum_{n=1}^N n = \dfrac 1 2 N (N+1).



$$

First, let's represent the sum with the letter $S.$ This way, it will be easier to manipulate the sum algebraically.

$$



S = \sum_{n=1}^N n



$$

Next, let's write out $S$ twice. The first time, we'll write the numbers in ascending order, and the second time in descending order:

$$



\begin{aligned}𝑆=1 & +2+⋯+(𝑁−1)+𝑁 \\ 𝑆=𝑁 & +(𝑁−1)+⋯+2+1\end{aligned}



$$

Now, if we add the two sums above, we get the following:

$$



\begin{aligned}2𝑆 & =(𝑁+1)+(2+𝑁−1)+⋯+(𝑁−1+2)+(𝑁+1) \\ & =\underset{𝑁 times}{\underset{}{(𝑁+1)+(𝑁+1)+⋯+(𝑁+1)+(𝑁+1)}} \\ & =𝑁(𝑁+1)\end{aligned}



$$

Finally, solving for $S$, we reach the desired result:

$$



S = \dfrac 1 2 N (N+1)



$$
