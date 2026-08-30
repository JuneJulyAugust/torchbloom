# Sums of Squares

Source: https://www.mathacademy.com/topics/5204?courseId=43
Topic ID: 5204

## Prerequisites

- [Covariance](./3591-covariance.md)

## Lesson

### Introduction

Given a data set $x_1, x_2, \ldots, x_n,$ we know that its variance, which we may denote as $\sigma_x^2,$ is given by

$$



\sigma_x^2 = \dfrac1n \sum_{i=1}^n (x_i - \overline x)^2



$$

where $\overline x$ is the mean of $x.$

The summation term

$$



S_{xx} = \sum_{i=1}^n (x_i - \overline x)^2



$$

is known as a **sum of squares** and is denoted $S_{xx}.$ As we'll see, this quantity often appears in statistical analysis, so giving it a separate notation is useful.

Similarly, if we have a data set $y_1, y_2, \ldots, y_n,$ then we define

$$



S_{yy} = \sum_{i=1}^n (y_i - \overline y)^2.



$$

Now, suppose we have the bivariate data set

$$



(x_1, y_1), \qquad (x_2, y_2),\qquad \ldots, \qquad (x_n, y_n).



$$

Then, the covariance is given by

$$



\text{Cov}(x,y) = \dfrac1n\sum_{i=1}^n (x_i - \overline x)(y_i - \overline y)



$$

and we may define $S_{xy}$ as

$$



S_{xy} = \sum_{i=1}^n (x_i - \overline{x})(y_i - \overline{y}).



$$

Finally, we can define the variance and covariance in terms of $S_{xx}, S_{yy},$ and $S_{xy}$ as follows:

$$



\begin{aligned}𝜎_{2𝑥} & =\frac{𝑆_{𝑥𝑥}}{𝑛},\,𝜎_{2𝑦}=\frac{𝑆_{𝑦𝑦}}{𝑛},\,Cov(𝑥,𝑦)=\frac{𝑆_{𝑥𝑦}}{𝑛}\end{aligned}



$$

### Example: Calculating Sums of Squares Given a Dataset or Summary Statistics

#### Question

Consider the two sets of $5$ paired observations shown in the table below.

Calculate $S_{xy}.$

#### Explanation

Given a set of $n$ paired observations $x_{1}, x_2, \ldots, x_{n}$ and $y_{1}, y_2, \ldots, y_{n},$ $S_{xy}$ is the sum of products of the deviations of $x_i$ and $y_i$ from their respective means, that is

$$



\begin{aligned}𝑆_{𝑥𝑦} & =\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}(𝑥_{𝑖}−\overset{𝑥}{})(𝑦_{𝑖}−\overset{𝑦}{–}).\end{aligned}



$$

First, we calculate the sample means $\overline{x}$ and $\overline{y}{:}$

$$



\overline{x} = \dfrac{15+12+13+16+19}{5} = 15



$$

$$



\overline{y} = \dfrac{8+13+6+15+13}{5} = 11



$$

Next, we calculate the differences between the $x_i$ and $\overline{x}$, $y_i$ and $\overline{y}$, and their product.

Therefore, $S_{xy}$ is

$$



S_{xy} = 0 + (-6) + 10 + 4 + 8 = 16.



$$

### Example: Calculating Variance and Covariance

#### Question

Consider two sets of $35$ paired observations $x_{1}, x_2, \ldots, x_{35},$ and $y_{1}, y_2, \ldots, y_{35}.$ You are given that

$$



\begin{aligned}𝑆_{𝑥𝑥}=35,\,𝑆_{𝑦𝑦}=133,\,𝑆_{𝑥𝑦}=105.\end{aligned}



$$

What is the value of $\mathrm{Cov}(x, y)?$

#### Explanation

Given a set of $n$ paired observations $x_{1}, x_2, \ldots, x_{n}$ and $y_{1}, y_2, \ldots, y_{n},$ their covariance can be calculated as follows:

$$



\begin{aligned}Cov(𝑥,𝑦) & =\frac{𝑆_{𝑥𝑦}}{𝑛},\end{aligned}



$$

where $S_{xy}$ is the sum of products of the deviations of $x_i$ and $y_i$ from their means.

We are given that $S_{xy} = 105.$ Substituting the given statistic in the above formula, we get

$$



\begin{aligned}Cov(𝑥,𝑦) & =\frac{105}{35} \\ & =3.\end{aligned}



$$

### Shortcut Formulas

Calculating $S_{xx}, S_{yy},$ and $S_{xy}$ using their definitions can be cumbersome. Thankfully, we have the following shortcut formulas:

$$



\begin{aligned}𝑆_{𝑥𝑥} & =\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}𝑥_{2𝑖}−\frac{1}{𝑛}(\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}𝑥_{𝑖})^{2} \\ 𝑆_{𝑦𝑦} & =\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}𝑦_{2𝑖}−\frac{1}{𝑛}(\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}𝑦_{𝑖})^{2} \\ 𝑆_{𝑥𝑦} & =\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}𝑥_{𝑖}𝑦_{𝑖}−\frac{1}{𝑛}(\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}𝑥_{𝑖})(\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}𝑦_{𝑖})\end{aligned}



$$

We'll prove these at the end of the lesson.

### Example: Calculating Sums of Squares Using the Shortcut Formula

#### Question

Consider the two sets of $5$ paired observations shown in the table below.

Given that $\displaystyle\sum_{i=1}^5 x_i^2 = 334,$ calculate $S_{xx}.$

#### Explanation

Given a set of $n$ paired observations $x_{1}, x_2, \ldots, x_{n}$ and $y_{1}, y_2, \ldots, y_{n},$ the sum of squared deviations from the mean for the data $x_i$ can be calculated as follows:

$$



\begin{aligned}𝑆_{𝑥𝑥} & =\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}(𝑥_{𝑖}−\overset{𝑥}{})^{2} \\ & =\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}𝑥_{2𝑖}−\frac{1}{𝑛}(\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}𝑥_{𝑖})^{2}.\end{aligned}



$$

First, we calculate the sum of the $x_i$ data:

$$



\sum_{i=1}^n x_i = 10 + 9 + 8 + 8 + 5 = 40.



$$

We are given that $\displaystyle\sum_{i=1}^5 x_i^2 = 334.$

Finally, by substituting into the above formula, we get

$$



S_{xx} =334 - \dfrac{1}{5}(40)^2 = 334- 320 = 14.



$$

### Example: Calculating S(x,y) Using the Shortcut Formula

#### Question

Consider two sets of $30$ paired observations $x_{1}, x_2, \ldots, x_{30},$ and $y_{1}, y_2, \ldots, y_{30}.$ You are given that

$$



\begin{aligned} & \underset{\underset{𝑖=1}{∑}}{\overset{}{30}}𝑥_{𝑖}=315, \\ & \underset{\underset{𝑖=1}{∑}}{\overset{}{30}}𝑦_{𝑖}=278, \\ & \underset{\underset{𝑖=1}{∑}}{\overset{}{30}}𝑥_{𝑖}𝑦_{𝑖}=2\,964.\end{aligned}



$$

Determine $S_{xy}.$

#### Explanation

Given a set of $n$ paired observations $x_{1}, x_2, \ldots, x_{n}$ and $y_{1}, y_2, \ldots, y_{n},$ the statistic $S_{xy}$ can be calculated as follows:

$$



\begin{aligned}𝑆_{𝑥𝑦} & =\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}(𝑥_{𝑖}−\overset{𝑥}{})(𝑦_{𝑖}−\overset{𝑦}{–}) \\ & =\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}𝑥_{𝑖}𝑦_{𝑖}−\frac{1}{𝑛}(\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}𝑥_{𝑖})(\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}𝑦_{𝑖}).\end{aligned}



$$

Substituting the given statistics in the above formula, we get

$$



\begin{aligned}𝑆_{𝑥𝑦} & =2\,964−\frac{1}{30}(315)(278) \\ & =2\,964−2\,919 \\ & =45.\end{aligned}



$$

### Proving the Shortcut Formulas

We wish to prove that

We start with the definition of

First, we expand the binomial:

Distributing the summation, we have

Now, since and are constants, we can write this as

Next, we use the following results:

This gives

as required.

The proofs for and are similar.
