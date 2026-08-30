# Covariance

Source: https://www.mathacademy.com/topics/3591?courseId=128
Topic ID: 3591

## Prerequisites

- [Variance and Standard Deviation](./1632-variance-and-standard-deviation.md)
- [Scatter Plots](../../../traditional/lessons/algebra-i/2585-scatter-plots.md)

## Lesson

### Introduction

Given two finite data sets of equal length, say,

$$


x=\big\{ x_1,x_2, \ldots, x_n \big\}, \qquad y=\big\{ y_1,y_2, \ldots, y_n \big\},


$$

the **covariance** between $x$ and $y,$ denoted by $\textrm{Cov}(x,y),$ is a measure that evaluates the extent to which $x$ and $y$ change together.

- A positive covariance means that if $x$ increases, then $y$ is also likely to increase:

- A negative covariance means that if $x$ increases, then $y$ is likely to decrease:

- A covariance of zero (or close to zero) indicates that there is no *linear* relationship between $x$ and $y.$ **Watch Out!** A covariance of zero does *not* mean that $x$ and $y$ are not related. It simply means the relationship between them is not linear. To illustrate, consider the image below. The (nonlinear) relationship shown above is $y=x^2.$ However, it can be shown that $\textrm{Cov}(x,y) = 0$ for this data set.

To calculate $\textrm{Cov}(x,y),$ we use the following formula:

$$


\textrm{Cov}(x,y) = \dfrac{1}{n} \sum\limits_{i=1}^n (x_i - \overline{x})(y_i - \overline{y}),


$$

where $\overline{x}$ and $\overline{y}$ denote the means of $x$ and $y$ respectively.

**Note**: This formula for the covariance assumes that $x$ and $y$ are drawn from a *population*. There is a slightly different formula for covariance when $x$ and $y$ are sample data. However, we won't worry about the difference for now.

### Example: Computing Covariance

#### Question

Calculate $\textrm{Cov}(x,y)$ for the following data sets:

$$


x = \big\{ 6, \: -2, \: 7, \: 1 \big\},\qquad y = \big\{ 5, \: -1, \: 4, \: 0 \big\}


$$

#### Explanation

The (population) covariance of the data sets $x=\big\{x_1,x_2, \ldots, x_n \big\}$ and $y=\big\{y_1,y_2, \ldots, y_n \big\}$ is given by

$$


\textrm{Cov}(x,y) = \dfrac{1}{n} \sum\limits_{i=1}^n (x_i - \overline{x})(y_i - \overline{y}),


$$

where $\overline{x} = \dfrac{1}{n} \displaystyle \sum_{i=1}^n x_i$ and $\overline{y} = \dfrac{1}{n} \displaystyle \sum_{i=1}^n y_i$ are the means of the data sets.

First, we need to compute the means:

$$


\begin{aligned}\overset{𝑥}{} & =\frac{1}{𝑛}\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}𝑥_{𝑖} \\ & =\frac{1}{4}⋅(6+(−2)+7+1) \\ & =\frac{1}{4}⋅12 \\ & =3 \\ \overset{𝑦}{–} & =\frac{1}{𝑛}\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}𝑦_{𝑖} \\ & =\frac{1}{4}⋅(5+(−1)+4+0) \\ & =\frac{1}{4}⋅8 \\ & =2\end{aligned}


$$

Therefore, the covariance of our data sets is

$$


\begin{aligned}Cov(𝑥,𝑦) & =\frac{1}{𝑛}\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}(𝑥_{𝑖}−\overset{𝑥}{})(𝑦_{𝑖}−\overset{𝑦}{–}) \\ & =\frac{1}{4}[(6−3)(5−2)+(−2−3)(−1−2)+(7−3)(4−2)+(1−3)(0−2)] \\ & =\frac{1}{4}[(3)(3)+(−5)(−3)+(4)(2)+(−2)(−2)] \\ & =\frac{1}{4}[9+15+8+4] \\ & =\frac{1}{4}⋅36 \\ & =9.\end{aligned}


$$

### Example: Computing Covariance in Context

#### Question

A math teacher asked four of her students how many hours they had slept the night before an exam. The information she received is shown in the table above. Compute the covariance of the data sets given that the means are $\overline{x}=5$ and $\overline{y}=73.$

#### Explanation

The (population) covariance of the data sets $x=\big\{x_1,x_2, \ldots, x_n \big\}$ and $y=\big\{y_1,y_2, \ldots, y_n \big\}$ is given by

$$


\textrm{Cov}(x,y) = \dfrac{1}{n} \sum\limits_{i=1}^n (x_i - \overline{x})(y_i - \overline{y}),


$$

where $\overline{x} = \dfrac{1}{n} \displaystyle \sum_{i=1}^n x_i$ and $\overline{y} = \dfrac{1}{n} \displaystyle \sum_{i=1}^n y_i$ are the means of the data sets.

Therefore, the covariance of our data sets is

$$


\begin{aligned}Cov(𝑥,𝑦) & =\frac{1}{𝑛}\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}(𝑥_{𝑖}−\overset{𝑥}{})(𝑦_{𝑖}−\overset{𝑦}{–}) \\ & =\frac{1}{4}[(2−5)(54−73)+(4−5)(68−73)+(6−5)(80−73)+(8−5)(90−73)] \\ & =\frac{1}{4}[(−3)(−19)+(−1)(−5)+(1)(7)+(3)(17)] \\ & =\frac{1}{4}[57+5+7+51] \\ & =\frac{1}{4}⋅120 \\ & =30.\end{aligned}


$$

### The Connection Between Variance and Covariance

Variance measures the spread of a *single* data set $x$ around its mean value $\overline{x}.$ On the other hand, covariance measures the relationship between *two* data sets $x$ and $y.$

The (population) covariance of the data sets

$$


x=\big\{ x_1,x_2, \ldots, x_n \big\}, \qquad y=\big\{ y_1,y_2, \ldots, y_n \big\}


$$

is given by

$$


\textrm{Cov}(x,y) = \dfrac{1}{n} \sum\limits_{i=1}^n (x_i - \overline{x})(y_i - \overline{y}).


$$

If we compare a single data set, say $x$, against itself using our formula for covariance, we obtain

$$


\begin{aligned}Cov(𝑥,𝑥) & =\frac{1}{𝑛}\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}(𝑥_{𝑖}−\overset{𝑥}{})(𝑥_{𝑖}−\overset{𝑥}{}) \\ & =\frac{1}{𝑛}\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}(𝑥_{𝑖}−\overset{𝑥}{})^{2} \\ & =𝜎^{2},\end{aligned}


$$

where $\sigma^2$ denotes the variance of $x.$
