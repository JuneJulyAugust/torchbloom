# Telescoping Series

Source: https://www.mathacademy.com/topics/1176?courseId=106
Topic ID: 1176

## Prerequisites

- [Convergent and Divergent Infinite Series](./982-convergent-and-divergent-infinite-series.md)
- [Expressing Rational Functions as Sums of Partial Fractions](./1060-expressing-rational-functions-as-sums-of-partial-fractions.md)

## Lesson

### Introduction

Let's see a trick that can be used to compute the sum of the following series:

$$


\sum_{n = 1}^\infty \dfrac 1 {n (n + 1)}


$$

First, we can use partial fractions to write

$$


\dfrac{1}{n(n+1)} = \dfrac{1}{n} - \dfrac{1}{n+1}.


$$

Then the sum is given by

$$


\sum_{n = 1}^\infty \dfrac 1 {n (n + 1)} = \sum_{n = 1}^\infty\left(\dfrac{1}{n} - \dfrac{1}{n+1}\right).


$$

Computing the first few partial sums, *without* simplifying, notice that many terms cancel:

$$



$$

\begin{aligned}𝑠_{1} & =(1\,−\,\frac{1}{2}) \\ 𝑠_{2} & =(1−\frac{1}{2})+(\frac{1}{2}\,−\,\frac{1}{3}) \\ 𝑠_{3} & =(1−\frac{1}{2})+(\frac{1}{2}−\frac{1}{3})+(\frac{1}{3}\,−\,\frac{1}{4}) \\ 𝑠_{4} & =(1−\frac{1}{2})+(\frac{1}{2}−\frac{1}{3})+(\frac{1}{3}−\frac{1}{4})+(\frac{1}{4}\,−\,\frac{1}{5}).\end{aligned}

$$


For each partial sum, we always end up canceling all terms except for the first and last terms. We say that this infinite series is a **telescoping series**, meaning that it consists of only a finite number of terms after canceling.

So, if $s_N$ is the $N$th partial sum of the series, we have


$$

s_N = {\color{blue}{1}} {\color{red}{\,-\, \dfrac 1 {N + 1}}} .

$$


Finally, we can determine the sum of the series by computing the limit of $s_N$ as $N\to\infty.$ We get


$$

\begin{aligned}\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}\frac{1}{𝑛(𝑛+1)} & =\underset{𝑁→∞}{lim}(1−\frac{1}{𝑁+1}) \\ & =1−0 \\ & =1.\end{aligned}

$$


### Example: Calculating the Sum of a Series Whose Denominator Is the Product of N and N+1

#### Question

Calculate $\displaystyle \sum\limits_{n = 4}^\infty {\dfrac{3}{{n(n + 1)}}}.$

#### Explanation

First, note that the series can be written as


$$

3\sum\limits_{n = 4}^\infty {\dfrac{1}{{n(n + 1)}}}.

$$


Using partial fractions, we can write the series as


$$

\displaystyle 3\sum\limits_{n = 4}^\infty \left(\dfrac 1 n - \dfrac 1 {n+1}\right).

$$


Computing the first few partial sums, starting with $n=4,$ gives


$$

$$


\begin{aligned}𝑠_{4} & =3[(\frac{1}{4}−\frac{1}{5})] \\ 𝑠_{5} & =3[(\frac{1}{4}−\frac{1}{5})+(\frac{1}{5}−\frac{1}{6})] \\ 𝑠_{6} & =3[(\frac{1}{4}−\frac{1}{5})+(\frac{1}{5}−\frac{1}{6})+(\frac{1}{6}−\frac{1}{7})] \\ 𝑠_{7} & =3[(\frac{1}{4}−\frac{1}{5})+(\frac{1}{5}−\frac{1}{6})+(\frac{1}{6}−\frac{1}{7})+(\frac{1}{7}−\frac{1}{8})].\end{aligned}


$$

Notice that in each partial sum, we always end up canceling all terms except for the first and last terms. Therefore, the $N$th partial sum is

$$


s_N = 3\left[\dfrac 1 4 - \dfrac{1}{N+1}\right].


$$

Finally, we can determine the sum of the series by taking the limit of $s_N\mathbin{:}$

$$


\begin{aligned}\underset{\underset{𝑛=4}{∑}}{\overset{}{∞}}\frac{3}{𝑛(𝑛+1)} & =\underset{𝑁→∞}{lim}𝑠_{𝑁} \\ & =\underset{𝑁→∞}{lim}3[\frac{1}{4}−\frac{1}{𝑁+1}] \\ & =3[\frac{1}{4}−0] \\ & =\frac{3}{4}\end{aligned}


$$

### Example: Calculating the Sum of a Series Whose Denominator Is the Product of Two Consecutive Expressions

#### Question

Calculate $\displaystyle \sum\limits_{n = 1}^\infty \dfrac{1}{(n+2)(n+3)}.$

#### Explanation

Using partial fractions, we have

$$


\dfrac{1}{(n+2)(n+3)} = \dfrac{1}{n+2} - \dfrac{1}{n+3}.


$$

So, our series can be written as

$$


\displaystyle \sum\limits_{n = 1}^\infty \left(\dfrac{1}{n+2} - \dfrac{1}{n+3}\right).


$$

Let's now compute the first few partial sums:

$$


\begin{aligned}𝑠_{1} & =(\frac{1}{3}−\frac{1}{4}) \\ 𝑠_{2} & =(\frac{1}{3}−\frac{1}{4})+(\frac{1}{4}−\frac{1}{5}) \\ 𝑠_{3} & =(\frac{1}{3}−\frac{1}{4})+(\frac{1}{4}−\frac{1}{5})+(\frac{1}{5}−\frac{1}{6}) \\ 𝑠_{4} & =(\frac{1}{3}−\frac{1}{4})+(\frac{1}{4}−\frac{1}{5})+(\frac{1}{5}−\frac{1}{6})+(\frac{1}{6}−\frac{1}{7})\end{aligned}


$$

Notice that in each partial sum, we always end up canceling all terms except for the first and last terms. Therefore, the $N$th partial sum is

$$


s_N = \dfrac{1}{3} - \dfrac{1}{N+3}.


$$

Finally, we can determine the sum of the series by taking the limit of $s_N\mathbin{:}$

$$


\begin{aligned}\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}\frac{1}{(𝑛+2)(𝑛+3)} & =\underset{𝑁→∞}{lim}𝑠_{𝑁} \\ & =\underset{𝑁→∞}{lim}(\frac{1}{3}−\frac{1}{𝑁+3}) \\ & =\frac{1}{3}−0 \\ & =\frac{1}{3}\end{aligned}


$$

### Example: Calculating the Sum of a Series Whose Denominator Is the Product of Two Non-Consecutive Expressions (x+a)(x+a+2)

#### Question

Calculate $\displaystyle \sum_{m = 1}^\infty \dfrac 1 {m(m +2)}.$

#### Explanation

We can use partial fractions to show that

$$


\dfrac{1}{m(m+2)} = \dfrac{1}{2}\left(\dfrac{1}{m} - \dfrac{1}{m+2}\right).


$$

So, our series can be written as

$$


\sum_{m = 1}^\infty \dfrac 1 2\left( \dfrac 1 m - \dfrac 1 {m + 2}\right) = \dfrac{1}{2} \sum_{m = 1}^\infty \left( \dfrac 1 m - \dfrac 1 {m + 2}\right).


$$

Let's compute the first few partial sums:

$$


\begin{aligned}𝑠_{1} & =\frac{1}{2}(\frac{1}{1}−\frac{1}{3}) \\ 𝑠_{2} & =\frac{1}{2}[(\frac{1}{1}−\frac{1}{3})+(\frac{1}{2}−\frac{1}{4})] \\ 𝑠_{3} & =\frac{1}{2}[(\frac{1}{1}−\frac{1}{3})+(\frac{1}{2}−\frac{1}{4})+(\frac{1}{3}−\frac{1}{5})] \\ 𝑠_{4} & =\frac{1}{2}[(\frac{1}{1}−\frac{1}{3})+(\frac{1}{2}−\frac{1}{4})+(\frac{1}{3}−\frac{1}{5})+(\frac{1}{4}−\frac{1}{6})] \\ 𝑠_{5} & =\frac{1}{2}[(\frac{1}{1}−\frac{1}{3})+(\frac{1}{2}−\frac{1}{4})+(\frac{1}{3}−\frac{1}{5})+(\frac{1}{4}−\frac{1}{6})+(\frac{1}{5}−\frac{1}{7})]\end{aligned}


$$

We notice that all of the terms cancel except the ${\color{blue}{\dfrac 1 1}}, {\color{blue}{\dfrac 1 2}},$ and the ${\color{red}{-\dfrac 1 {N+1}}}$ and ${\color{red}{-\dfrac 1 {N+2}}}$ terms. Therefore, the $N$th partial sum is

$$


s_N = \dfrac 1 2\left[{\color{blue}{\dfrac 1 1}} + {\color{blue}{\dfrac 1 2}} {\color{red}{-\dfrac 1 {N+1}}} {\color{red}{-\dfrac 1 {N+2}}}\right].


$$

Finally, we can determine the sum of the series by taking the limit of $s_N\mathbin{:}$

$$


\begin{aligned}\underset{𝑁→∞}{lim}𝑠_{𝑁} & =\underset{𝑁→∞}{lim}\frac{1}{2}[\frac{1}{1}+\frac{1}{2}−\frac{1}{𝑁+1}−\frac{1}{𝑁+2}] \\ & =\frac{1}{2}\underset{𝑁→∞}{lim}[\frac{1}{1}+\frac{1}{2}−\frac{1}{𝑁+1}−\frac{1}{𝑁+2}] \\ & =\frac{1}{2}[\frac{1}{1}+\frac{1}{2}−0−0] \\ & =\frac{1}{2}[\frac{1}{1}+\frac{1}{2}] \\ & =\frac{1}{2}⋅\frac{3}{2} \\ & =\frac{3}{4}.\end{aligned}


$$
