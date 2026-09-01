# Sums of Finite Geometric Series Given in Sigma Notation

Source: https://www.mathacademy.com/topics/690?courseId=43
Topic ID: 690

## Prerequisites

- [The Sum of a Finite Geometric Series](./1016-the-sum-of-a-finite-geometric-series.md)
- [Writing Geometric Series in Sigma Notation](./1017-writing-geometric-series-in-sigma-notation.md)

## Lesson

### Introduction

Suppose we want to calculate the sum

$$



S_N = \displaystyle\sum_{n=1}^{5} 3 (4)^{n-1}.



$$

Notice that this series is in the form $\displaystyle{\sum_{n=1}^N a_1 r^{n-1}},$ which represents a geometric series.

To determine the sum, we can use the formula for the sum $S_N$ of a geometric series:

$$



S_N = a_1\dfrac{(1-r^N)}{1-r}



$$

In this case, $a_1 = 3,$ $r = 4,$ and $N = 5.$ If we substitute these values into the formula for $S_N,$ we obtain the following:

$$



\begin{aligned}\underset{\underset{𝑛=1}{∑}}{\overset{}{5}}3(4)^{𝑛−1} & =3⋅(\frac{1−4^{5}}{1−4}) \\ & =3⋅(\frac{−1023}{−3}) \\ & =1023\end{aligned}



$$

### Example: Finding the Sum of a Geometric Series Given in Sigma Notation

#### Question

Evaluate the series $\displaystyle\sum_{n=1}^{8} 3 (2)^{n-1}.$

#### Explanation

Since the given series is in the form $\displaystyle{\sum_{n=1}^N a_1 r^{n-1}},$ it is a geometric series.

To determine the sum, we use the formula for the sum $S_N$ of a geometric series:

$$



S_N = a_1\dfrac{(1-r^N)}{1-r}



$$

In this case, $a_1 = 3,$ $r = 2,$ and $N = 8.$ If we substitute these values into the formula for $S_N,$ we obtain the following:

$$



\begin{aligned}\underset{\underset{𝑛=1}{∑}}{\overset{}{8}}3(2)^{𝑛−1} & =3⋅(\frac{1−2^{8}}{1−2}) \\ & =3⋅(\frac{−255}{−1}) \\ & =765\end{aligned}



$$

### Example: Finding the Sum of a Simplified Geometric Series Given in Sigma Notation

#### Question

Evaluate the geometric series $\displaystyle \sum_{n=1}^{5} 3 (4)^{n}.$

#### Explanation

Since the given series is in the form $\displaystyle{\sum_{n=1}^N a r^{n}},$ it is a geometric series.

To determine the sum, we use the formula for the sum $S_N$ of a geometric series:

$$



S_N = a_1\dfrac{(1-r^N)}{1-r}



$$

In this case, $r = 4$ and $N = 5.$ We need to figure out the value of $a_1.$

The formula for the $n$th term of the series is

$$



a_n = 3(4)^n,



$$

and therefore we can calculate the first term $a_1$ as follows:

$$



\begin{aligned}𝑎_{1} & =3(4)^{1} \\ & =12\end{aligned}



$$

If we substitute $a_1 = 12,$ $r = 4,$ and $N = 5$ into the formula for $S_N,$ we obtain the following:

$$



\begin{aligned}\underset{\underset{𝑛=1}{∑}}{\overset{}{5}}3(4)^{𝑛} & =12⋅\frac{(1−4^{5})}{1−4} \\ & =−\frac{12}{3}(−1\,023) \\ & =4\,092\end{aligned}



$$

### Example: Finding the Sum of a Geometric Series by Determining the Common Ratio

#### Question

Evaluate the geometric series $\displaystyle \sum_{n = 1}^{5} \dfrac{8}{2^{n-1}}\,.$

#### Explanation

Notice that we can rewrite the series as follows:

$$



\sum_{n = 1}^{5} \dfrac{8}{2^{n-1}} = \sum_{n = 1}^{5} 8 \left( \dfrac{1}{2} \right)^{n-1}



$$

Since the above series is in the form $\displaystyle{\sum_{n=1}^N a_1 r^{n-1}},$ it is a geometric series.

To determine the sum, we use the formula for the sum $S_N$ of a geometric series:

$$



S_N = a_1\dfrac{(1-r^N)}{1-r}



$$

In this case, $a_1 =8,$ $r = \dfrac{1}{2},$ and $N = 5.$ If we substitute these values into the above formula, we obtain the following:

$$



\begin{aligned}\underset{\underset{𝑛=1}{∑}}{\overset{}{5}}\frac{8}{2^{𝑛−1}} & =8⋅\frac{[1−(\frac{1}{2})^{5}]}{2} \\ & =8⋅\frac{(\frac{31}{32})}{32} \\ & =8⋅\frac{31}{16} \\ & =\frac{31}{2}\end{aligned}



$$

### The Sum of a Geometric Series With a Zero Starting Index

We know that for a geometric series

$$



\displaystyle \sum_{n=1}^{N} a_1 r^{n-1},



$$

the sum of the first $N$ terms is given by

$$



S_N = a_1\dfrac{(1-r^N)}{1-r}.



$$

In the sum formula above, $a_1$ is the first term of the series because the series starts with the index $n=1.$

However, if a series starts with the index $n=0,$ then the first term of the series is actually $a_0.$ So, for a series in the form

$$



\displaystyle \sum_{n=0}^{N-1} a_1 r^{n-1},



$$

the sum is given by

$$



S_N = a_0 \dfrac{(1-r^N)}{1-r}.



$$

Let's see an example of this.

### Example: Finding the Sum of a Geometric Series Given With a Zero Starting Index

#### Question

Evaluate the geometric series $\displaystyle \sum_{n=0}^{4} 3\left(2\right)^{n-1}.$

#### Explanation

Since the given series is in the form $\displaystyle\sum{a_1 r^{n-1}},$ it is a geometric series. Notice that the index starts from $n=0$ instead of $n=1.$

To determine the sum, we use the formula for the sum $S_N$ of a geometric series:

$$



S_N = a_0\dfrac{(1-r^N)}{1-r}



$$

Note that we use $a_0$ in the sum formula because $a_0$ is the first term of the series.

In this case, $r =2.$ Also, note that $N=5,$ since there are $5$ terms in total: $a_0,$ $a_1,$ $a_2,$ $a_3,$ $a_4.$

The formula for the $n$th term of the series is

$$



a_n = 3\left( 2\right)^{n-1},



$$

so the first term $a_0$ is given by

$$



\begin{aligned}𝑎_{0} & =3(2)^{0−1} \\ & =3(2)^{−1} \\ & =3⋅\frac{1}{2} \\ & =\frac{3}{2}.\end{aligned}



$$

If we substitute $a_0 =\dfrac{3}{2},$ $r=2,$ and $N=5$ into the formula for $S_N,$ we obtain the following:

$$



\begin{aligned}𝑆_{5} & =\frac{3}{2}⋅\frac{(1−2^{5})}{(1−2)} \\ & =\frac{3}{2}⋅\frac{(−31)}{(−1)} \\ & =\frac{93}{2}\end{aligned}



$$
