# Inverse Laplace Transforms

Source: https://www.mathacademy.com/topics/2530?courseId=155
Topic ID: 2530

## Prerequisites

- [Expressing Rational Functions with Repeated Factors as Sums of Partial Fractions](../../../ap-courses/lessons/ap-calculus-bc/1062-expressing-rational-functions-with-repeated-factors-as-sums-of-partial-fractions.md)
- [The Smoothness Property of Laplace Transforms](./6402-the-smoothness-property-of-laplace-transforms.md)

## Lesson

### Introduction

The **inverse Laplace transform** of a function $F(s)$ is denoted $\mathcal{L}^{-1} \left\{F(s) \right\}.$

To find the inverse Laplace transform, we first find the function $f(t)$ whose Laplace transform is $F(s)\mathbin{:}$

$$


F(s) = \mathcal{L} \left\{ f(t) \right\}


$$

Then, we have

$$


\mathcal{L}^{-1} \left\{ F(s) \right\} = \mathcal{L}^{-1} \left\{ \mathcal{L} \left\{ f(t) \right\} \right\} = f(t).


$$

Note that the addition and scalar multiplication properties also hold for the inverse Laplace transform:

- The addition property:

- The scalar multiplication property:

Next, we will look at an example of calculating an inverse Laplace transform.

### Example: Finding the Inverse Laplace Transform of a Function Using Known Laplace Transforms

#### Question

Find the inverse Laplace transform for $F(s) = \dfrac{3}{s^2 + 9}.$

#### Explanation

From the table of Laplace transforms, we have

$$


\begin{aligned}L{sin⁡3𝑡} & =\frac{3}{𝑠^{2}+3^{2}}=\frac{3}{𝑠^{2}+9},\,𝑠>0.\end{aligned}


$$

Therefore, we have

$$


\begin{aligned}L^{−1}{\frac{3}{𝑠^{2}+9}} & =L^{−1}{L{sin⁡3𝑡}} \\ & =sin⁡3𝑡.\end{aligned}


$$

### Example: Finding the Inverse Laplace Transform of a Function Using the Addition Property

#### Question

Find $\mathcal{L}^{-1}\left\{F(s)\right\}$ for $F(s)=\dfrac{4e^{-s}-2}{s}.$

#### Explanation

First, we decompose the fraction into a sum of partial fractions:

$$


\dfrac{4e^{-s}-2}{s} =\dfrac{4e^{-s}}{s} - \dfrac{2}{s}


$$

From the table of Laplace transforms, we have

$$


\begin{aligned}L{𝑢_{1}(𝑡)} & =\frac{𝑒^{−𝑠}}{𝑠},\,𝑠>0, \\ L{1} & =\frac{1}{𝑠},\,𝑠>0,\end{aligned}


$$

where $u_1(t)=u(t-1)$ is the unit step function.

Therefore, using the addition and scalar multiplication properties of the inverse Laplace transform, we get

$$


\begin{aligned}L^{−1}{\frac{4𝑒^{−𝑠}}{𝑠}−\frac{2}{𝑠}} & =4L^{−1}{\frac{𝑒^{−𝑠}}{𝑠}}−2L^{−1}{\frac{1}{𝑠}} \\ & =4𝑢_{1}(𝑡)−2.\end{aligned}


$$

So the inverse Laplace transform of $F(s)=\dfrac{4e^{-s}-2}{s}$ is

$$


\mathcal{L}^{-1}\left\{F(s)\right\} = f(t)= 4 u_1(t) - 2.


$$

### Example: Finding the Inverse Laplace Transform of a Function Using the Scalar Multiplication Property

#### Question

Compute $\mathcal{L}^{-1}\left\{\dfrac{7}{s - 9}\right\}.$

#### Explanation

From the table of Laplace transforms, we have

$$


\begin{aligned}L{𝑒^{9𝑡}} & =\frac{1}{𝑠−9},\,𝑠>9.\end{aligned}


$$

Therefore, by applying the inverse Laplace transform to the above result, we have

$$


\begin{aligned}L{𝑒^{9𝑡}} & =\frac{1}{𝑠−9} \\ L^{−1}{L{𝑒^{9𝑡}}} & =L^{−1}{\frac{1}{𝑠−9}} \\ 𝑒^{9𝑡} & =L^{−1}{\frac{1}{𝑠−9}} \\ L^{−1}{\frac{1}{𝑠−9}} & =𝑒^{9𝑡}.\end{aligned}


$$

Using the multiplicative property of the inverse Laplace transform, we get

$$


\begin{aligned}7⋅L^{−1}{\frac{1}{𝑠−9}}=7⋅𝑒^{9𝑡} \\ L^{−1}{\frac{7}{𝑠−9}}=7𝑒^{9𝑡}.\end{aligned}


$$

### Example: Finding the Inverse Laplace Transform Using Partial Fractions

#### Question

Find the inverse Laplace transform for $F(s)=\dfrac{3s}{(s-4)(s+2)}.$

#### Explanation

First, we write $F(s)$ as a sum of partial fractions:

$$


\dfrac{3s}{(s-4)(s+2)} = \dfrac{2}{s-4} + \dfrac{1}{s+2}


$$

From the table of Laplace transforms, we have

$$


\begin{aligned}L{𝑒^{4𝑡}} & =\frac{1}{𝑠−4},\,𝑠>4, \\ L{𝑒^{−2𝑡}} & =\frac{1}{𝑠+2},\,𝑠>−2.\end{aligned}


$$

Therefore, using the addition and scalar multiplication properties of the inverse Laplace transform, we get

$$


\begin{aligned}L^{−1}{\frac{2}{𝑠−4}+\frac{1}{𝑠+2}} & =2L^{−1}{\frac{1}{𝑠−4}}+L^{−1}{\frac{1}{𝑠+2}} \\ & =2𝑒^{4𝑡}+𝑒^{−2𝑡}.\end{aligned}


$$

So the inverse Laplace transform of $F(s)=\dfrac{3s}{(s-4)(s+2)}$ is

$$


\mathcal{L}^{-1}\left\{ F(s) \right\} = f(t)=2e^{4t} + e^{-2t}.


$$
