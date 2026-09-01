# Finite Cubic Series

Source: https://www.mathacademy.com/topics/789?courseId=109
Topic ID: 789

## Prerequisites

- [Finite Quadratic Series](./787-finite-quadratic-series.md)

## Lesson

### Introduction

If we wish to sum the cubes of the first $N$ integers, an easy way is to use the following formula:

$$



\begin{aligned}\underset{\underset{𝑛=1}{∑}}{\overset{}{𝑁}}𝑛^{3} & =1^{3}+2^{3}+3^{3}+⋯+(𝑁−1)^{3}+𝑁^{3} \\ & =\frac{1}{4}𝑁^{2}(𝑁+1)^{2}\end{aligned}



$$

Since we also know that

$$



\begin{aligned}\underset{\underset{𝑛=1}{∑}}{\overset{}{𝑁}}𝑛^{2} & =1^{2}+2^{2}+3^{2}+⋯+(𝑁−1)^{2}+𝑁^{2} \\ & =\frac{1}{6}𝑁(𝑁+1)(2𝑁+1)\end{aligned}



$$

and

$$



\begin{aligned}\underset{\underset{𝑛=1}{∑}}{\overset{}{𝑁}}𝑛 & =1+2+3+⋯+(𝑁−1)+𝑁 \\ & =\frac{1}{2}𝑁(𝑁+1),\end{aligned}



$$

we can use these formulae to evaluate any series of the form

$$



\displaystyle{\sum_{n=1}^N (an^3+bn^2+cn+d)}.



$$

Finally, it's worth noting that

$$



\sum_{n=1}^N n^3 = \frac{1}{4}N^2(N+1)^2 = \left(\frac{1}{2}N(N+1)\right)^2 = \left(\sum_{n=1}^N n\right)^2.



$$

In other words, the sum of the first $N$ cube numbers is equal to the square of the sum of the first $N$ natural numbers.

### Example: Calculating the Sum of the First N Cube Numbers

#### Question

Calculate $\displaystyle\sum_{n=1}^{100} n^3.$

#### Explanation

Using the formula

$$



\sum_{n=1}^N n^3 = \frac{1}{4}N^2(N+1)^2



$$

with $N=100,$ we get

$$



\begin{aligned}\underset{\underset{𝑛=1}{∑}}{\overset{}{100}}𝑛^{3} & =\frac{1}{4}⋅100^{2}(100+1)^{2} \\ & =\frac{1}{4}⋅100^{2}⋅101^{2} \\ & =\frac{1}{4}⋅10\,000⋅10\,201 \\ & =25\,502\,500.\end{aligned}



$$

### Example: Calculating the Sum of a Finite Cubic Series with a Constant Factor

#### Question

Calculate $\displaystyle \sum_{n=1}^{100} 4n^3.$

#### Explanation

First, we take the factor $4$ outside the summation:

$$



\sum_{n=1}^{100} 4n^3 = 4\sum_{n=1}^{100} n^3



$$

Now, using the formula

$$



\sum_{n=1}^N n^3 = \frac{1}{4}N^2(N+1)^2



$$

with $N=100,$ we get

$$



\begin{aligned}4\underset{\underset{𝑛=1}{∑}}{\overset{}{100}}𝑛^{3} & =4(\frac{1}{4}⋅100^{2}(100+1)^{2}) \\ & =4(\frac{1}{4}⋅100^{2}⋅101^{2}) \\ & =4(\frac{1}{4}⋅10\,000⋅10\,201) \\ & =4⋅25\,502\,500 \\ & =102\,010\,000.\end{aligned}



$$

### Example: Calculating the Sum of a Cubic Series with a Quadratic, Linear, or Constant Term

#### Question

Calculate $\displaystyle \sum_{n=1}^{50} (3n^3+2n).$

#### Explanation

Notice that we can write the given summation as follows:

$$



\begin{aligned}\underset{\underset{𝑛=1}{∑}}{\overset{}{50}}(3𝑛^{3}+2𝑛) & =\underset{\underset{𝑛=1}{∑}}{\overset{}{50}}3𝑛^{3}+\underset{\underset{𝑛=1}{∑}}{\overset{}{50}}2𝑛 \\ & =3\underset{\underset{𝑛=1}{∑}}{\overset{}{50}}𝑛^{3}+2\underset{\underset{𝑛=1}{∑}}{\overset{}{50}}𝑛\end{aligned}



$$

Now, let's evaluate the two series using our formulas.

- For the first series, we use the formula with $N=50,$ and we get

- For the second series, we use the formula with $N=50,$ and we get

Finally, we have

$$



\begin{aligned}\underset{\underset{𝑛=1}{∑}}{\overset{}{50}}(3𝑛^{3}+2𝑛) & =4\,876\,875+2\,550 \\ & =4\,879\,425.\end{aligned}



$$
