# The Linear Correlation Coefficient

Source: https://www.mathacademy.com/topics/1056?courseId=73
Topic ID: 1056

## Prerequisites

- [Linear Correlation](../../../high-school/traditional/lessons/algebra-i/734-linear-correlation.md)
- [Sums of Squares](../../../high-school/integrated-math-honors/lessons/integrated-math-ii-honors/5204-sums-of-squares.md)

## Lesson

### Introduction

The **linear correlation coefficient**, also called the **Pearson correlation coefficient**, measures the strength of the linear relationship between two variables. It is often denoted by $\rho$ for a population and by $r$ for a sample. In this lesson, we'll concern ourselves with population data only.

The linear correlation coefficient satisfies the following constraint:

$$


-1 \leq \rho \leq 1


$$

We interpret the endpoints of this interval as follows:

- $\rho = 1$ means that there is a perfect *positive* correlation between the data points.

- $\rho = -1$ means that there is a perfect *negative* correlation between the data points.

Moreover, $\rho = 0$ means there is no *linear* correlation between the data points.

In addition, we have the following rule of thumb:

- If $|\rho| \gt 0.7,$ the correlation is **strong,** and the data points closely follow a straight line.

- If $0.3\leq |\rho| \leq 0.7,$ the correlation is **weak.** The data points follow a straight line, but many are far from the line.

- If $|\rho| \lt 0.3,$ then the correlation is **negligible.** There is no (linear) correlation.

### Calculating the Correlation Coefficient

To calculate $\rho,$ we use the following formula:

$$


\begin{aligned}𝜌(𝑥,𝑦) & =\frac{Cov(𝑥,𝑦)}{𝜎_{𝑥}⋅𝜎_{𝑦}},\end{aligned}


$$

where

- $\text{Cov}(x,y)$ is the covariance between $x$ and $y,$ and

- $\sigma_x$ and $\sigma_y$ are the standard deviations of $x$ and $y,$ respectively.

For example, consider data sets $x$ and $y$ such that

$$


\text{Cov}(x,y)=-9, \qquad \sigma_x=6, \qquad \sigma_y=2.


$$

Substituting our numbers into the formula above, we get

$$


\begin{aligned}𝜌(𝑥,𝑦) & =\frac{(−9)}{(6)⋅(2)} \\ & =\frac{(−9)}{12} \\ & =−0.75.\end{aligned}


$$

Since $|\rho| \gt 0.7,$ the correlation is strong. Also, since $\rho$ is negative, the correlation is negative.

Therefore, there is a strong negative correlation between $x$ and $y.$

### Example: Computing the Correlation Coefficient Using Covariance and Standard Deviations

#### Question

Consider the following data sets:

$$


x = \big\{ 6, \: 3, \: -1, \: 0 \big\},\qquad y = \big\{ 5, \: 7, \: -2, \: 6 \big\}


$$

You're given that $\overline{x}=2,$ $\overline{y}=4,$ $\sigma_x \approx 2.739,$ and $\sigma_y \approx 3.536.$ Calculate the corresponding linear correlation coefficient. Round your answer to $2$ decimal places.

#### Explanation

The (population) linear correlation coefficient of the data sets $x=\big\{x_1,x_2, \ldots, x_n \big\}$ and $y=\big\{y_1,y_2, \ldots, y_n \big\}$ is given by

$$


\rho(x,y) = \dfrac{\text{Cov}(x,y)}{\sigma_x \cdot \sigma_y}


$$

where $\text{Cov}(x,y)$ is the covariance, and $\sigma_x$ and $\sigma_y$ are the standard deviations of the data sets.

First, we need to compute the covariance:

$$


\begin{aligned}Cov(𝑥,𝑦) & =\frac{1}{𝑛}\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}(𝑥_{𝑖}−\overset{𝑥}{})(𝑦_{𝑖}−\overset{𝑦}{–}) \\ & =\frac{1}{4}[(6−2)(5−4)+(3−2)(7−4)+(−1−2)(−2−4)+(0−2)(6−4)] \\ & =\frac{1}{4}[(4)(1)+(1)(3)+(−3)(−6)+(−2)(2)] \\ & =\frac{1}{4}[4+3+18−4] \\ & =\frac{1}{4}⋅21 \\ & =5.25\end{aligned}


$$

Finally, we use the formula. This gives

$$


\begin{aligned}𝜌(𝑥,𝑦) & =\frac{Cov(𝑥,𝑦)}{𝜎_{𝑥}⋅𝜎_{𝑦}} \\ & ≈\frac{5.25}{2.739⋅3.536} \\ & ≈0.54\end{aligned}


$$

rounded to $2$ decimal places.

### The Linear Correlation Coefficient in Sigma Notation

Suppose we have data sets $x=\big\{x_1,x_2, \ldots, x_n \big\}$ and $y=\big\{y_1,y_2, \ldots, y_n \big\}$ of the same size.

Let's now introduce the following notation:

$$


S_{xx} = \sum\limits_{i=1}^n (x_i-\overline{x})^2, \qquad S_{yy} = \sum\limits_{i=1}^n (y_i-\overline{y})^2, \qquad S_{xy} = \sum\limits_{i=1}^n (x_i-\overline{x})(y_i-\overline{y})


$$

Notice that $S_{xx}, S_{yy},$ and $S_{xy}$ are the sums of square deviations found in the formulas for the variance of $x,$ the variance of $y,$ and covariance of $x$ and $y,$ respectively.

Using the previous definition, we can show that the correlation coefficient can be calculated as follows:

$$


\rho = \dfrac{S_{xy}}{\sqrt{S_{xx} \cdot S_{yy}}}\,.


$$

### Example: Computing the Linear Correlation Coefficient Using the Expanded Formula

#### Question

Consider the following data sets:

$$


x = \big\{ 13, \: 10, \: 9, \: 12 \big\},\qquad y = \big\{ -1, \: 3, \: 2, \: 4 \big\}


$$

You are given that $\overline{x}=11$ and $\overline{y}=2.$ Calculate the corresponding linear correlation coefficient. Round your answer to $2$ decimal places.

#### Explanation

The linear correlation coefficient $\rho$ of the data sets $x=\big\{x_1,x_2, \ldots, x_n \big\}$ and $y=\big\{y_1,y_2, \ldots, y_n \big\}$ is given by

$$


\rho(x,y) = \dfrac{\text{Cov}(x,y)}{\sigma_x \cdot \sigma_y} = \dfrac{S_{xy}}{\sqrt{S_{xx} \cdot S_{yy}}}.


$$

First, we compute the sum in the numerator:

$$


\begin{aligned}𝑆_{𝑥𝑦} & =\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}(𝑥_{𝑖}−\overset{𝑥}{})(𝑦_{𝑖}−\overset{𝑦}{–}) \\ & =(13−11)(−1−2)+(10−11)(3−2) \\ & =+(9−11)(2−2)+(12−11)(4−2) \\ & =(2)(−3)+(−1)(1)+(−2)(0)+(1)(2) \\ & =−6−1+0+2 \\ & =−5\end{aligned}


$$

Second, we compute the sums in the denominator:

$$


\begin{aligned}𝑆_{𝑥𝑥} & =\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}(𝑥_{𝑖}−\overset{𝑥}{})^{2} \\ & =(13−11)^{2}+(10−11)^{2}+(9−11)^{2}+(12−11)^{2} \\ & =4+1+4+1 \\ & =10 \\ 𝑆_{𝑦𝑦} & =\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}(𝑦_{𝑖}−\overset{𝑦}{–})^{2} \\ & =(−1−2)^{2}+(3−2)^{2}+(2−2)^{2}+(4−2)^{2} \\ & =9+1+0+4 \\ & =14\end{aligned}


$$

Finally, we use the formula:

$$


\begin{aligned}𝜌(𝑥,𝑦) & =\frac{(−5)}{\sqrt{10}⋅\sqrt{14}} \\ & ≈−\frac{5}{3.162\,278⋅3.741\,657} \\ & ≈−0.42\end{aligned}


$$

rounded to $2$ decimal places.

### Example: Interpreting Linear Correlation Coefficients in Context

#### Question

A stall selling lemonade is set up at a special four-day summer festival. The stall owner wants to check the strength of the linear correlation between $x,$ the temperature at $12\,\text{p.m},$ and $y,$ the number of cups of lemonade sold that day. The data is shown below.

You are given that the means are $\overline{x}=24$ and $\overline{y}=107.$ Which of the following statements are true?

1. $\rho\approx 0.54$

2. There is a strong positive correlation between $x$ and $y.$

3. There is a weak positive correlation between $x$ and $y.$

**

#### Explanation

The linear correlation coefficient $\rho$ of the data sets $x=\big\{x_1,x_2, \ldots, x_n \big\}$ and $y=\big\{y_1,y_2, \ldots, y_n \big\}$ is given by

$$


\rho(x,y) = \dfrac{\text{Cov}(x,y)}{\sigma_x \cdot \sigma_y} = \dfrac{S_{xy}}{\sqrt{S_{xx} \cdot S_{yy}}}.


$$

In addition, we have the following rule of thumb:

- if $|\rho| \gt 0.7,$ the correlation is **

- if $0.3\leq |\rho| \leq 0.7,$ the correlation is **

- if $|\rho| \lt 0.3,$ then the correlation is **

Let's now examine our statements in turn:

- Statement I is true. To calculate $\rho,$ we first compute the sum in the numerator: Second, we compute the sums in the denominator: Finally, we use the formula: rounded to $2$ decimal places.

- Statement II is false, while statement III is true. Since $0.3\leq |\rho| \leq 0.7$ the correlation is weak. Also, since $\rho$ is positive, the correlation is positive.

Therefore, the correct answer is "I and III only."

### Proving the Formula for Rho in Terms of Squared Deviations

Let's derive the following result:

$$


\rho = \dfrac{S_{xy}}{\sqrt{S_{xx} \cdot S_{yy}}}


$$

We start with the definition of the correlation coefficient $\rho\mathbin{:}$

$$


\begin{aligned}𝜌 & =\frac{Cov(𝑥,𝑦)}{𝜎_{𝑥}⋅𝜎_{𝑦}}\end{aligned}


$$

We have

$$


\text{Cov}(x,y) = \dfrac1n \sum\limits_{i=1}^n (x_i-\overline{x})(y_i-\overline{y}) = \dfrac{S_{xy}}{n}.


$$

Similarly,

$$


\begin{aligned}𝜎_{𝑥} & =\sqrt{\frac{1}{𝑛}\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}(𝑥_{𝑖}−\overset{𝑥}{})^{2}}=\sqrt{\frac{𝑆_{𝑥𝑥}}{𝑛}} \\ 𝜎_{𝑦} & =\sqrt{\frac{1}{𝑛}\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}(𝑦_{𝑖}−\overset{𝑦}{–})^{2}}=\sqrt{\frac{𝑆_{𝑦𝑦}}{𝑛}}.\end{aligned}


$$

Substituting this into our definition for $\rho,$ we get

$$


\begin{aligned}𝜌 & =\frac{Cov(𝑥,𝑦)}{𝜎_{𝑥}⋅𝜎_{𝑦}} \\ & =\frac{(\frac{𝑆_{𝑥𝑦}}{𝑛})}{𝑛} \\ & =\frac{(\frac{𝑆_{𝑥𝑦}}{𝑛})}{𝑛} \\ & =\frac{(\frac{𝑆_{𝑥𝑦}}{𝑛})}{𝑛} \\ & =\frac{(\frac{𝑆_{𝑥𝑦}}{𝑛})}{𝑛} \\ & =\frac{𝑆_{𝑥𝑦}}{\sqrt{𝑆_{𝑥𝑥}⋅𝑆_{𝑦𝑦}}}.\end{aligned}


$$
