# Variance and Standard Deviation

Source: https://www.mathacademy.com/topics/1632?courseId=134
Topic ID: 1632

## Prerequisites

- [Absolute Value Expressions](../../../traditional/lessons/algebra-i/96-absolute-value-expressions.md)
- [The Mean of a Data Set](./1634-the-mean-of-a-data-set.md)

## Lesson

### Introduction

When analyzing data, we often want to know how "spread out" the data is. One way to represent the spread of the data is to use the **variance** of the data.

If we have a data set that consists of the points $x_1, x_2, \ldots, x_n,$ then the variance, denoted by $\sigma^2,$ is defined as

$$


\sigma^2 = \dfrac{1}{n} \sum\limits_{i=1}^n (x_i - \overline{x})^2,


$$

where $\overline{x} = \dfrac{1}{n} \displaystyle \sum_{i=1}^n x_i$ is the mean of the data set.

There's some nice intuition behind the formula for the variance. The mean $\overline{x}$ can be interpreted as the "center" of the data set, and the squared difference $(x_i - \overline{x})^2$ represents the squared distance between $x_i$ and the center. So, the variance gives the average squared distance of the data points from the center.

In general,

- a data set that is *spread out* over many possible values will have a *high* variance, while

- a data set that is *concentrated* (or *clumped*) near a single value will have a *low* variance.

**Note**: The formula for the variance given here assumes that the points $x_1, x_2, \ldots, x_n$ include every member of the population we're interested in. There is a slightly different formula for variance when these points represent a sample drawn from a population. However, we won't worry about the difference for now.

### A Worked Example

The variance $\sigma^2$ of a data set is given by

$$


\sigma^2 = \dfrac{1}{n} \sum\limits_{i=1}^n (x_i - \overline{x})^2.


$$

To demonstrate how to use this formula, let's compute the variance of the data set below:

$$


1, \: 7, \: 3, \: 9


$$

First, we need to compute the mean:

$$


\begin{aligned}\overset{𝑥}{} & =\frac{1}{𝑛}\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}𝑥_{𝑖} \\ & =\frac{1}{4}⋅(1+7+3+9) \\ & =\frac{1}{4}⋅20 \\ & =5\end{aligned}


$$

Now, we can compute the variance:

$$


\begin{aligned}𝜎^{2} & =\frac{1}{𝑛}\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}(𝑥_{𝑖}−\overset{𝑥}{})^{2} \\ & =\frac{1}{4}[(1−5)^{2}+(7−5)^{2}+(3−5)^{2}+(9−5)^{2}] \\ & =\frac{1}{4}[16+4+4+16] \\ & =\frac{1}{4}[40] \\ & =10\end{aligned}


$$

Therefore, the variance is $\sigma^2 = 10.$

### Example: Computing the Variance of a Data Set Using the Definition

#### Question

What is the variance of the following data set?

#### Explanation

If we have a data set that consists of the points then the variance of the data set is given by where is the mean of the data set.

First, we need to compute the mean. There are points in our data set, so the mean is

Therefore, the variance is

### A Formula for Quickly Computing the Variance

There is an alternative formula that we can use to compute the variance of a data set $x_1, x_2, \ldots, x_n.$ This formula gives the same result as the usual formula, and it is often faster to use.

$$


\sigma^2 = \overline{x^2} - (\overline{x})^2


$$

Here, $\overline{x^2}$ refers to the mean of the squares of the points in the data set, that is,

$$


\overline{x^2} = \dfrac{1}{n} \sum\limits_{i=1}^n x_i^2.


$$

To demonstrate, let's again compute the variance of the data set below:

$$


1, \: 7, \: 3, \: 9


$$

Earlier, we found that $\overline{x} = 5.$ Now, let's compute $\overline{x^2}{:}$

$$


\begin{aligned}\overset{𝑥^{2}}{} & =\frac{1}{𝑛}\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}𝑥_{2𝑖}^{} \\ & =\frac{1}{4}⋅(1^{2}+7^{2}+3^{2}+9^{2}) \\ & =\frac{1}{4}⋅(1+49+9+81) \\ & =\frac{1}{4}⋅140 \\ & =35.\end{aligned}


$$

Then, we compute the variance as follows:

$$


\begin{aligned}𝜎^{2} & =\overset{𝑥^{2}}{}−(\overset{𝑥}{})^{2} \\ & =35−5^{2} \\ & =10\end{aligned}


$$

Indeed, we get the same answer as before!

### Example: Computing the Variance Given the Number, Sum, and Sum of Squares of the Data Points

#### Question

Compute the variance $\sigma^2$ of a data set $x_i$ consisting of $8$ data points, where

$$


\sum_{i=1}^{8} x_i = 40, \qquad \sum_{i=1}^{8} x_i^2 = 320.


$$

#### Explanation

If we have a data set that consists of the points $x_1, x_2, \ldots, x_n,$ then the variance of the data set is given by

$$


\sigma^2 = \overline{x^2} - (\overline{x})^2,


$$

where $\overline{x}$ is the mean of the data set and $\overline{x^2}$ is the mean of the squares of the points in the data set.

First, let's compute $\overline{x}.$ There are $n=8$ points in our data set, and we know that $\displaystyle \sum_{i=1}^{8} x_i = 40,$ so we get

$$


\begin{aligned}\overset{𝑥}{} & =\frac{1}{𝑛}\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}𝑥_{𝑖} \\ & =\frac{1}{8}\underset{\underset{𝑖=1}{∑}}{\overset{}{8}}𝑥_{𝑖} \\ & =\frac{1}{8}⋅40 \\ & =5.\end{aligned}


$$

Now, let's compute $\overline{x^2}.$ We know that $\displaystyle \sum_{i=1}^{8} x_i^2 = 320,$ so we get

$$


\begin{aligned}\overset{𝑥^{2}}{} & =\frac{1}{𝑛}\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}𝑥_{2𝑖}^{} \\ & =\frac{1}{8}\underset{\underset{𝑖=1}{∑}}{\overset{}{8}}𝑥_{2𝑖}^{} \\ & =\frac{1}{8}⋅320 \\ & =40.\end{aligned}


$$

So, the variance is

$$


\begin{aligned}𝜎^{2} & =\overset{𝑥^{2}}{}−(\overset{𝑥}{})^{2} \\ & =40−(5)^{2} \\ & =40−25 \\ & =15.\end{aligned}


$$

### Example: Computing the Variance of a Data Set Using the Formula

#### Question

What is the variance of the following data set?

$$


4, \: 5, \: 4, \: 7, \: 8, \: 11, \: 3


$$

#### Explanation

If we have a data set that consists of the points $x_1, x_2, \ldots, x_n,$ then the variance can be computed as

$$


\sigma^2 = \overline{x^2} - (\overline{x})^2,


$$

where $\overline{x}$ is the mean of the data set and $\overline{x^2}$ is the mean of the squares of the points in the data set.

First, let's compute $\overline{x}.$ There are $n=7$ points in our data set, so the mean is

$$


\begin{aligned}\overset{𝑥}{} & =\frac{1}{𝑛}\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}𝑥_{𝑖} \\ & =\frac{1}{7}⋅(4+5+4+7+8+11+3) \\ & =\frac{1}{7}⋅42 \\ & =6.\end{aligned}


$$

Now, let's compute $\overline{x^2}.$ Computing the mean of the squares of the points in the data set, we get

$$


\begin{aligned}\overset{𝑥^{2}}{} & =\frac{1}{𝑛}\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}𝑥_{2𝑖}^{} \\ & =\frac{1}{7}⋅(4^{2}+5^{2}+4^{2}+7^{2}+8^{2}+11^{2}+3^{2}) \\ & =\frac{1}{7}⋅(16+25+16+49+64+121+9) \\ & =\frac{1}{7}⋅300 \\ & =\frac{300}{7}.\end{aligned}


$$

So, the variance is

$$


\begin{aligned}𝜎^{2} & =\overset{𝑥^{2}}{}−(\overset{𝑥}{})^{2} \\ & =\frac{300}{7}−(6)^{2} \\ & =\frac{300}{7}−36 \\ & =\frac{300−252}{7} \\ & =\frac{48}{7}.\end{aligned}


$$

### Standard Deviation

The **standard deviation** of a data set $x_1, x_2, \ldots, x_n$ is defined as the square root of the variance:

$$


\sigma = \sqrt{ \sigma^2 } = \sqrt{ \dfrac{1}{n} \sum\limits_{i=1}^n (x_i - \overline{x})^2 } = \sqrt{ \,\,\, \vphantom{\sum\limits_{i=1}^n} \overline{x^2} - \left( \overline{x} \right)^2 }


$$

To demonstrate, let's again consider the data set below:

$$


1, \: 7, \: 3, \: 9


$$

Previously, we found that the variance of this data set was $\sigma^2 = 10.$ So, the standard deviation is given by

$$


\sigma = \sqrt{ 10 }.


$$

As we will see in the future, the standard deviation is often used in calculations where we want to quantify how "surprising" a particular observation is.

In those contexts, we often compute how many standard deviations the observed value was away from the mean: the further away, the more surprising the observation.

For now, though, let's get some practice computing the standard deviation.

### Example: Computing the Standard Deviation of a Data Set

#### Question

What is the standard deviation of the following data set?

$$


7, \: 5, \: 0, \: 2, \: 1, \: 3


$$

#### Explanation

The standard deviation of a data set $x_1, x_2, \ldots, x_n$ is the square root of the variance:

$$


\sigma = \sqrt{ \sigma^2 } = \sqrt{ \dfrac{1}{n} \sum\limits_{i=1}^n (x_i - \overline{x})^2 } = \sqrt{ \,\,\, \vphantom{\sum\limits_{i=1}^n} \overline{x^2} - \left( \overline{x} \right)^2 }


$$

First, let's compute $\overline{x}.$ There are $n=6$ points in our data set, so the mean is

$$


\begin{aligned}\overset{𝑥}{} & =\frac{1}{𝑛}\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}𝑥_{𝑖} \\ & =\frac{1}{6}⋅(7+5+0+2+1+3) \\ & =\frac{1}{6}⋅18 \\ & =3.\end{aligned}


$$

Now, let's compute $\overline{x^2}.$ Computing the mean of the squares of the points in the data set, we get

$$


\begin{aligned}\overset{𝑥^{2}}{} & =\frac{1}{𝑛}\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}𝑥_{2𝑖}^{} \\ & =\frac{1}{6}⋅(7^{2}+5^{2}+0^{2}+2^{2}+1^{2}+3^{2}) \\ & =\frac{1}{6}⋅(49+25+0+4+1+9) \\ & =\frac{88}{6} \\ & =\frac{44}{3}.\end{aligned}


$$

So, the variance is

$$


\begin{aligned}𝜎^{2} & =\overset{𝑥^{2}}{}−(\overset{𝑥}{})^{2} \\ & =\frac{44}{3}−(3)^{2} \\ & =\frac{44}{3}−9 \\ & =\frac{44−27}{3} \\ & =\frac{17}{3}.\end{aligned}


$$

Finally, the standard deviation is

$$


\sigma = \sqrt{ \sigma^2 } = \sqrt{ \dfrac{17}{3} }.


$$

### Why We Use the Squared Difference

Recall the definition of variance:

$$


\sigma^2 = \dfrac{1}{n} \sum\limits_{i=1}^n (x_i - \overline{x})^2


$$

You may wonder why the variance uses the *squared* difference, $(x_i - \overline{x})^2,$ instead of just using the non-squared difference $x_i - \overline{x}.$

It turns out that if we add up all the non-squared differences $x_i - \overline{x},$ then the negatives will cancel out the positives, and the result will always come out to zero no matter how spread out or concentrated the distribution is.

For example, consider the dataset

$$


-2, \: -2, \: 0, \: 2, \: 2.


$$

We have $\overline{x}=0,$ and if we compute $\displaystyle \dfrac{1}{n} \sum\limits_{i=1}^n (x_i - \overline{x}),$ we get a result of $0{:}$

$$


\begin{aligned}\frac{1}{𝑛}\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}(𝑥_{𝑖}−\overset{𝑥}{}) & =\frac{1}{5}[(−2−0)+(−2−0)+(0−0)+(2−0)+(2−0)] \\ & =\frac{1}{5}[−2−2+0+2+2] \\ & =\frac{1}{5}⋅0 \\ & =0\end{aligned}


$$

This will happen every time, because the quantity $\displaystyle \dfrac{1}{n} \sum\limits_{i=1}^n (x_i - \overline{x})$ always simplifies to $0{:}$

$$


\begin{aligned}\frac{1}{𝑛}\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}(𝑥_{𝑖}−\overset{𝑥}{}) & =\underset{\overset{𝑥}{}}{\underset{}{\frac{1}{𝑛}\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}𝑥_{𝑖}}}−\frac{1}{𝑛}\underset{𝑛\overset{𝑥}{}}{\underset{}{\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}\overset{𝑥}{}}} \\ & =\overset{𝑥}{}−\frac{1}{𝑛}⋅𝑛\overset{𝑥}{} \\ & =\overset{𝑥}{}−\overset{𝑥}{} \\ & =0\end{aligned}


$$

So we need to perform some operation to the distances $x_i - \overline{x}$ to make them non-negative. Squaring the distances, $(x_i - \overline{x})^2,$ will accomplish this.
