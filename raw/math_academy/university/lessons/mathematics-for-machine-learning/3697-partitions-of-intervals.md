# Partitions of Intervals

Source: https://www.mathacademy.com/topics/3697?courseId=145
Topic ID: 3697

## Prerequisites

- [Sets](../../../high-school/traditional/lessons/geometry/45-sets.md)
- [The Difference of Squares Formula](../../../high-school/traditional/lessons/algebra-i/2275-the-difference-of-squares-formula.md)
- [Properties of Finite Series](../../../high-school/integrated-math-honors/lessons/integrated-math-ii-honors/3958-properties-of-finite-series.md)

## Lesson

### Introduction

A partition $P$ of a closed interval $[a,b]$ is a finite sequence of real numbers taken from $[a,b]$ such that

$$


a = x_0 < x_1< x_2 < \ldots < x_n = b\,.


$$

For example, given the interval $[0,6],$ one possible partition is

$$


0 < 2 < 5 < 6.


$$

We can express this partition using set notation as

$$


P=\{0,2,5,6\}.


$$

Note that this partition breaks up the interval $[0,6]$ into the union of the following subintervals:

$$


[0,2] \cup [2,5] \cup [5,6]


$$

### Example: Identifying Partitions of the Real Line

#### Question

Which of the following are partitions of the real interval $[1,9]?$

1. $\{1, 4, 5, 8\}$

2. $\{1, 3, 4, 9\}$

3. $1 < 2 < 9$

#### Explanation

A partition $P$ of a closed interval $[a,b]$ is a finite sequence of real numbers taken from $[a,b]$ such that

$$


a = x_0 < x_1< x_2 < \ldots < x_n = b\,.


$$

We can express $P$ using set notation as

$$


P=\{x_0,x_1,\ldots,x_n\}.


$$

With that in mind, let's consider each statement:

- Statement I is not a partition of $[1,9]$ since it does not include the right endpoint $b=9.$

- Statement II is a partition of $[1,9].$

- Statement III is a partition of $[1,9].$

Therefore, the correct answer is "II and III only."

### Sums Over Partitions

Suppose we have the partition $P=\{0,2,5,6\}$ of the interval $[a,b]=[0,6].$ Then, we have

$$


a=\underbrace{0}_{\large x_0} < \underbrace{2}_{\large x_1} < \underbrace{5}_{\large x_2} < \underbrace{6}_{\large x_3} =b.


$$

This partition breaks up the interval $[0,6]$ into the union of the following subintervals:

$$


[0,2] \cup [2,5] \cup [5,6]


$$

The length of the $i$th subinterval, denoted $\Delta x_i,$ is simply the difference of the endpoints:

- The length of the first interval $[0,2],$ denoted $\Delta x_1,$ is

- The length of the second interval $[2,5],$ denoted $\Delta x_2,$ is

- The length of the third interval $[5,6],$ denoted $\Delta x_3,$ is

Therefore,

$$


\begin{aligned}\underset{\underset{𝑖=1}{∑}}{\overset{}{3}}Δ𝑥_{𝑖} & =Δ𝑥_{1}+Δ𝑥_{2}+Δ𝑥_{3} \\ & =2+3+1 \\ & =6,\end{aligned}


$$

which is just the length of the interval $[0, 6].$

**Note:** In general, for any partition $P=\{x_0,x_1,\ldots,x_m\}$ of an interval $[a,b],$ the sum

$$


\displaystyle \sum_{i=1}^m\Delta x_i


$$

is just the length of the interval $[a, b],$ because

$$


\begin{aligned}\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑚}}Δ𝑥_{𝑖} & =Δ𝑥_{1}+Δ𝑥_{2}+Δ𝑥_{3}+⋯+Δ𝑥_{𝑚} \\ & =(𝑥_{1}−𝑥_{0})+(𝑥_{2}−𝑥_{1})+(𝑥_{3}−𝑥_{2})+⋯+(𝑥_{𝑚}−𝑥_{𝑚−1}) \\ & =(𝑥_{1}−𝑥_{0})+(𝑥_{2}−𝑥_{1})+(𝑥_{3}−𝑥_{2})+⋯+(𝑥_{𝑚}−𝑥_{𝑚−1}) \\ & =−𝑥_{0}+𝑥_{𝑚} \\ & =𝑥_{𝑚}−𝑥_{0} \\ & =𝑏−𝑎.\end{aligned}


$$

### Example: Computing Simple Sums Over Partitions of the Real Line

#### Question

Let $P= \left\{y_0, y_1, \ldots, y_n\right\}$ be a partition of the interval $[-3, 5].$ If $\Delta y_j = y_j - y_{j-1},$ calculate $\displaystyle \sum_{j=1}^n {3}\Delta y_j.$

#### Explanation

First, we take the factor $3$ outside the summation:

$$


\begin{aligned}\underset{\underset{𝑗=1}{∑}}{\overset{}{𝑛}}3Δ𝑦_{𝑗}=3\underset{\underset{𝑗=1}{∑}}{\overset{}{𝑛}}Δ𝑦_{𝑗}\end{aligned}


$$

Note that $\displaystyle \sum_{j=1}^n \Delta y_j$ is just the length of the interval $[-3, 5],$ because

$$


\begin{aligned}\underset{\underset{𝑗=1}{∑}}{\overset{}{𝑛}}Δ𝑦_{𝑗} & =Δ𝑦_{1}+Δ𝑦_{2}+Δ𝑦_{3}+⋯+Δ𝑦_{𝑛} \\ & =(𝑦_{1}−𝑦_{0})+(𝑦_{2}−𝑦_{1})+(𝑦_{3}−𝑦_{2})+⋯+(𝑦_{𝑛}−𝑦_{𝑛−1}) \\ & =(𝑦_{1}−𝑦_{0})+(𝑦_{2}−𝑦_{1})+(𝑦_{3}−𝑦_{2})+⋯+(𝑦_{𝑛}−𝑦_{𝑛−1}) \\ & =−𝑦_{0}+𝑦_{𝑛} \\ & =𝑦_{𝑛}−𝑦_{0} \\ & =5−(−3) \\ & =5+3 \\ & =8.\end{aligned}


$$

Therefore,

$$


{3}\sum_{j=1}^n \Delta y_j = 3 \cdot 8 = 24.


$$

### Example: Computing Sums Over Partitions of the Real Line

#### Question

Let $P = \left\{x_0, x_1, \ldots, x_m\right\}$ be a partition of the interval $[-3, 4].$ If $\Delta x_i = x_i - x_{i-1},$ calculate $\displaystyle\sum_{i=1}^m (x_i + x_{i-1})\Delta x_i.$

#### Explanation

We can simplify the given summation as follows:

$$


\begin{aligned}\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑚}}(𝑥_{𝑖}+𝑥_{𝑖−1})Δ𝑥_{𝑖} & =(𝑥_{1}+𝑥_{0})Δ𝑥_{1}+(𝑥_{2}+𝑥_{1})Δ𝑥_{2}+⋯+(𝑥_{𝑚}+𝑥_{𝑚−1})Δ𝑥_{𝑚} \\ & =(𝑥_{1}+𝑥_{0})(𝑥_{1}−𝑥_{0})+(𝑥_{2}+𝑥_{1})(𝑥_{2}−𝑥_{1})+⋯+(𝑥_{𝑚}+𝑥_{𝑚−1})(𝑥_{𝑚}−𝑥_{𝑚−1}) \\ & =(𝑥_{21}^{}−𝑥_{20}^{})+(𝑥_{22}^{}−𝑥_{21}^{})+⋯+(𝑥_{2𝑚}^{}−𝑥_{2𝑚−1}^{}) \\ & =(𝑥_{21}^{}−𝑥_{20}^{})+(𝑥_{22}^{}−𝑥_{21}^{})+⋯+(𝑥_{2𝑚}^{}−𝑥_{2𝑚−1}^{}) \\ & =−𝑥_{20}^{}+𝑥_{2𝑚}^{} \\ & =𝑥_{2𝑚}^{}−𝑥_{20}^{}\end{aligned}


$$

Now, since $x_0 = -3$ and $x_m = 4$ are the endpoints of our partition, we have

$$


\begin{aligned}\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑚}}(𝑥_{𝑖}+𝑥_{𝑖−1})Δ𝑥_{𝑖} & =𝑥_{2𝑚}^{}−𝑥_{20}^{} \\ & =4^{2}−(−3)^{2} \\ & =7.\end{aligned}


$$
