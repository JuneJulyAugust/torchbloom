# Median, Quartiles and Percentiles of Continuous Random Variables

Source: https://www.mathacademy.com/topics/3024?courseId=73
Topic ID: 3024

## Prerequisites

- [Cumulative Distribution Functions for Continuous Random Variables](./2163-cumulative-distribution-functions-for-continuous-random-variables.md)
- [Range, Quartiles, and IQR](../grade-6/2480-range-quartiles-and-iqr.md)

## Lesson

### Introduction

If $X$ is a continuous random variable and $0 \leq p \leq 1,$ then the $100p$th **percentile** is a number $x_p$ such that

$$


P(X \leq x_p) = p.


$$

- In terms of CDF, the *cumulative distribution function* $F(x)$ of $X,$ the $100p$th percentile $x_p$ is a number on the $x$-axis such that

$$


F(x_p) = p.


$$

- In terms of PDF, the *probability density function* $f(x)$ of $X,$ the $100p$th percentile $x_p$ is a number on the $x$-axis such that the area under the graph of $y=f(x)$ to the left of $x$ is equal to $p \mathbin{:}$

$$


\int_{-\infty}^{x_p} f(x) \, \text{d}x = p.


$$

For example, let's find the $4$th percentile of the random variable $X$ if the probability density function of $X$ is given by

$$


\begin{aligned}\frac{1}{2}𝑥,\, & 0≤𝑥≤2, \\ 0,\, & otherwise.\end{aligned}


$$

The $4$th percentile corresponds to the decimal $p={\color{red}0.04}$ since $100 \cdot 0.04 = 4.$ So, we have

$$


\begin{aligned}𝑃(𝑋≤𝑥_{0.04}) & =∫_{𝑥_{0.04}0}^{}\frac{1}{2}𝑥\,d𝑥 \\ & =\frac{𝑥^{2}}{4}_{𝑥_{0.04}0}^{} \\ & =\frac{𝑥_{0.04}^{2}}{4}.\end{aligned}


$$

Therefore, the $4$th percentile is given by

$$


\begin{aligned}\frac{𝑥_{0.04}^{2}}{4} & =0.04 \\ 𝑥_{0.04}^{2} & =0.16 \\ 𝑥_{0.04} & =0.4.\end{aligned}


$$

Note that we took the positive root because $0 \leq x_{0.04} \leq 2.$

There are a few special percentiles:

- the $25$th percentile is called the **lower quartile**. This is the number $q_1$ such that

- the $50$th percentile is called the **median**. This is the number $m$ such that

- the $75$th percentile is called the **upper quartile**. This is the number $q_3$ such that

- the **interquartile range** is the difference between the upper and lower quartiles, that is,

### Example: Finding the Median Given the CDF a Continuous Random Variable

#### Question

Find the median of the random variable $X$ if the cumulative distribution function of $X$ is given by

$$


\begin{aligned}0, & 𝑥<1, \\ 1−\frac{1}{𝑥^{4}}, & 𝑥≥1.\end{aligned}


$$

#### Explanation

The median of a random variable $X$ is the number $m$ such that

$$


P(X \leq m) = \dfrac{1}{2}.


$$

In our case, we have

$$


P(X \leq m) = F(m) = 1-\dfrac{1}{m^4} , \quad m \geq 1.


$$

Therefore, the median is given by

$$


1-\dfrac{1}{m^4} = \dfrac{1}{2}\quad \Rightarrow \quad m = \sqrt[4]2.


$$

Note that we took the positive root because $m \geq 1.$

### Example: Finding the Median Given the PDF a Continuous Random Variable

#### Question

Find the median of the random variable $X$ if the probability density function of $X$ is given by

$$


\begin{aligned}0,\, & 𝑥<1, \\ \frac{2}{𝑥^{3}},\, & 𝑥≥1.\end{aligned}


$$

#### Explanation

The median of a random variable $X$ is the number $m$ such that

$$


P(X \leq m) = \dfrac{1}{2}.


$$

In our case, we have

$$


\begin{aligned}𝑃(𝑋≤𝑚) & =∫_{𝑚1}^{}\frac{2}{𝑥^{3}}\,d𝑥 \\ & =−\frac{1}{𝑥^{2}}_{𝑚1}^{} \\ & =−\frac{1}{𝑚^{2}}+1\end{aligned}


$$

Therefore, the median is given by

$$


\begin{aligned}−\frac{1}{𝑚^{2}}+1 & =\frac{1}{2} \\ \frac{1}{𝑚^{2}} & =\frac{1}{2} \\ 𝑚 & =\sqrt{√2}.\end{aligned}


$$

Note that we took the positive root because $m \geq 1.$

### Example: Finding a Quartile of a Continuous Random Variable

#### Question

Find, to three decimal places, the interquartile range of the random variable $X$ if the cumulative distribution function of $X$ is given by

$$


\begin{aligned}0, & 𝑥<0, \\ \frac{𝑥^{2}}{25}, & 0≤𝑥≤5, \\ 1, & 𝑥>5.\end{aligned}


$$

#### Explanation

To find the interquartile range, we first need to find the lower quartile and the upper quartile.

The lower quartile of a random variable $X$ is the number $q_1$ such that

$$


P(X \leq q_1) = \dfrac{1}{4},


$$

and the upper quartile is the number $q_3$ such that

$$


P(X \leq q_3) = \dfrac{3}{4}.


$$

First, we find the lower quartile:

$$


\begin{aligned}𝑃(𝑋≤𝑞_{1}) & =\frac{1}{4} \\ 𝐹(𝑞_{1}) & =\frac{1}{4} \\ \frac{1}{25}𝑞_{21}^{} & =\frac{1}{4} \\ 𝑞_{21}^{} & =\frac{25}{4} \\ 𝑞_{1} & =\frac{5}{2}\end{aligned}


$$

Then, we find the upper quartile:

$$


\begin{aligned}𝑃(𝑋≤𝑞_{3}) & =\frac{3}{4} \\ 𝐹(𝑞_{3}) & =\frac{3}{4} \\ \frac{1}{25}𝑞_{23}^{} & =\frac{3}{4} \\ 𝑞_{23}^{} & =\frac{75}{4} \\ 𝑞_{3} & =\frac{5\sqrt{√3}}{2}\end{aligned}


$$

Therefore, the interquartile range is

$$


IQR = q_3 - q_1 =\dfrac{5\sqrt3}{2} - \dfrac{5}{2}\approx 1.830


$$

rounded to three decimal places.

### Example: Finding a Percentile of a Continuous Random Variable

#### Question

Find the $27$th percentile of the random variable $X$ if the probability distribution function of $X$ is given by

$$


\begin{aligned}\frac{2}{75}𝑥,\, & 5≤𝑥≤10, \\ 0,\, & otherwise.\end{aligned}


$$

#### Explanation

The $100p$th percentile of a random variable $X$ is the number $x_p$ such that

$$


P(X \leq x_p) = p.


$$

In our case, we want to find the $27$th percentile, which corresponds to the decimal $p=0.27.$ We have

$$


\begin{aligned}𝑃(𝑋≤𝑥_{0.27}) & =∫_{𝑥_{0.27}5}^{}\frac{2}{75}𝑥\,d𝑥 \\ & =\frac{𝑥^{2}}{75}_{𝑥_{0.27}5}^{} \\ & =\frac{𝑥_{20.27}^{}}{75}−\frac{1}{3}.\end{aligned}


$$

Therefore, the $27$th percentile is given by

$$


\begin{aligned}\frac{𝑥_{20.27}^{}}{75}−\frac{1}{3} & =0.27 \\ 𝑥_{20.27}^{} & =75(\frac{27}{100}+\frac{1}{3}) \\ 𝑥_{0.27} & =6.727\end{aligned}


$$

rounded to three decimal places.
