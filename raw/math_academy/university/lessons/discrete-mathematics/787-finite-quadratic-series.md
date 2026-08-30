# Finite Quadratic Series

Source: https://www.mathacademy.com/topics/787?courseId=109
Topic ID: 787

## Prerequisites

- [Finite Linear Series](./786-finite-linear-series.md)

## Lesson

### Introduction

If we wish to sum the squares of the first $N$ integers, an easy way is to use the following formula:

$$



\begin{aligned}\underset{\underset{𝑛=1}{∑}}{\overset{}{𝑁}}𝑛^{2} & =1^{2}+2^{2}+3^{2}+⋯+(𝑁−1)^{2}+𝑁^{2} \\ & =1+4+9+⋯+(𝑁−1)^{2}+𝑁^{2} \\ & =\frac{1}{6}𝑁(𝑁+1)(2𝑁+1)\end{aligned}



$$

Since we also know that

$$



\begin{aligned}\underset{\underset{𝑛=1}{∑}}{\overset{}{𝑁}}𝑛 & =1+2+3+⋯+(𝑁−1)+𝑁 \\ & =\frac{1}{2}𝑁(𝑁+1),\end{aligned}



$$

we can use these formulas to evaluate any series of the form

$$



\displaystyle{\sum_{n=1}^N (an^2+bn+c)}.



$$

### Example: Calculating the Sum of the First N Square Numbers

#### Question

Calculate $\displaystyle\sum_{n=1}^{100} n^2.$

#### Explanation

Using the formula

$$



\sum_{n=1}^N n^2 = \frac{1}{6}N(N+1)(2N+1)



$$

with $N=100,$ we get

$$



\begin{aligned}\underset{\underset{𝑛=1}{∑}}{\overset{}{100}}𝑛^{2} & =\frac{1}{6}⋅100(100+1)(2⋅100+1) \\ & =\frac{1}{6}⋅100⋅101⋅201 \\ & =338\,350.\end{aligned}



$$

### Example: Calculating the Sum of a Finite Quadratic Series with a Constant Factor

#### Question

Calculate $\displaystyle \sum_{n=1}^{100} 4n^2.$

#### Explanation

First, we take the factor $4$ outside the summation:

$$



\sum_{n=1}^{100} 4n^2 = 4\sum_{n=1}^{100} n^2



$$

Now, using the formula

$$



\sum_{n=1}^N n^2 = \frac{1}{6}N(N+1)(2N+1)



$$

with $N=100,$ we get

$$



\begin{aligned}4\underset{\underset{𝑛=1}{∑}}{\overset{}{100}}𝑛^{2} & =4(\frac{1}{6}⋅100(100+1)(2⋅100+1)) \\ & =4⋅\frac{1}{6}⋅100⋅101⋅201 \\ & =4⋅338\,350 \\ & =1\,353\,400.\end{aligned}



$$

### Example: Calculating the Sum of a Quadratic Series with a Linear or Constant Term

#### Question

Calculate $\displaystyle \sum_{n=1}^{50} (3n^2+2n).$

#### Explanation

Notice that we can write the given summation as follows:

$$



\begin{aligned}\underset{\underset{𝑛=1}{∑}}{\overset{}{50}}(3𝑛^{2}+2𝑛) & =\underset{\underset{𝑛=1}{∑}}{\overset{}{50}}3𝑛^{2}+\underset{\underset{𝑛=1}{∑}}{\overset{}{50}}2𝑛 \\ & =3\underset{\underset{𝑛=1}{∑}}{\overset{}{50}}𝑛^{2}+2\underset{\underset{𝑛=1}{∑}}{\overset{}{50}}𝑛\end{aligned}



$$

Now, let's evaluate the two series using our formulas.

- For the first series, we use the formula with $N=50,$ and we get

- For the second series, we use the formula with $N=50,$ and we get

Finally, we have

$$



\begin{aligned}\underset{\underset{𝑛=1}{∑}}{\overset{}{50}}(3𝑛^{2}+2𝑛) & =128\,775+2\,550 \\ & =131\,325.\end{aligned}



$$
