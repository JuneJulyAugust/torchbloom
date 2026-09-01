# Calculating Trigonometric Ratios Using the Sum Formula for Sine

Source: https://www.mathacademy.com/topics/3837?courseId=101
Topic ID: 3837

## Prerequisites

- [The Sum and Difference Formulas for Sine](./270-the-sum-and-difference-formulas-for-sine.md)
- [Combining the Rules of Exponents](../../../../middle-school/lessons/grade-8/1457-combining-the-rules-of-exponents.md)
- [Extending the Pythagorean Identity to All Quadrants](../../../traditional/lessons/algebra-ii/2021-extending-the-pythagorean-identity-to-all-quadrants.md)

## Lesson

### Introduction

We can compute trigonometric ratios using the sum and difference formulas for sine together with the Pythagorean identity.

Let's suppose that for the angles $u$ and $v,$ we have

$$


\sin v = \dfrac{3}{5}, \qquad \cos v = \dfrac{4}{5}, \qquad \sin u = -\dfrac{12}{13}.


$$

How can we find the value of $\sin\left(u - v\right)$ given that $u$ lies in the third quadrant?

First, recall the difference formula for sine:

$$


\sin(u-v) = \sin u \cos v- \cos u \sin v


$$

We know the values of $\sin{v}$, $\cos{v}$, and $\sin{u}.$ To find the missing value of $\cos{u}$, we can use the Pythagorean identity:

$$


\sin^2 u + \cos^2 u= 1 \qquad\Longrightarrow\qquad \cos^2 u = 1- \sin^2 u


$$

Substituting our values into the Pythagorean identity, we get

$$


\begin{aligned}cos^{2}⁡𝑢 & =1−sin^{2}⁡𝑢 \\ & =1−(−\frac{12}{13})^{2} \\ & =1−(\frac{12}{13})^{2} \\ & =1−\frac{12^{2}}{13^{2}} \\ & =1−\frac{144}{169} \\ & =\frac{169}{169}−\frac{144}{169} \\ & =\frac{25}{169}.\end{aligned}


$$

Therefore,

$$


\begin{aligned}cos⁡𝑢 & =±\sqrt{\frac{25}{169}} \\ & =±\frac{5}{13}.\end{aligned}


$$

We're given that $u$ lies in the third quadrant, where cosine is negative. So, we disregard the positive value, and we have

$$


\cos u= -\dfrac{5}{13}.


$$

We can now apply the difference formula as follows:

$$


\begin{aligned}sin⁡(𝑢−𝑣) & =sin⁡𝑢cos⁡𝑣−cos⁡𝑢sin⁡𝑣 \\ & =(−\frac{12}{13})(\frac{4}{5})−(−\frac{5}{13})(\frac{3}{5}) \\ & =−\frac{48}{65}+\frac{15}{65} \\ & =−\frac{33}{65}.\end{aligned}


$$

### Example: Computing the Sine of a Composite Angle Using Angles in the First Quadrant

#### Question

Suppose that for the angles $u$ and $v,$ we have

$$


\sin u = \dfrac{3}{4}, \qquad \cos u = -\dfrac{\sqrt{7}}{4}, \qquad \cos v = \dfrac{4}{5}.


$$

Given that $v$ lies in the first quadrant, and

$$


\sin\left(u + v\right) = \dfrac{a- b\sqrt 7}{20},


$$

calculate the value of $a+b.$

#### Explanation

First, recall the sum formula for sine:

$$


\sin(u+v) = \sin u \cos v+ \cos u \sin v


$$

We know the values of $\sin{u},$ $\cos{u},$ and $\cos{v}.$ To find the missing value of $\sin{v},$ we can use the Pythagorean identity:

$$


\sin^2 v + \cos^2 v= 1 \qquad\Longrightarrow\qquad \sin^2 v = 1- \cos^2 v


$$

Substituting our values into the Pythagorean identity, we get

$$


\begin{aligned}sin^{2}⁡𝑣 & =1−cos^{2}⁡𝑣 \\ & =1−(\frac{4}{5})^{2} \\ & =1−\frac{4^{2}}{5^{2}} \\ & =1−\frac{16}{25} \\ & =\frac{25}{25}−\frac{16}{25} \\ & =\frac{25−16}{25} \\ & =\frac{9}{25}.\end{aligned}


$$

Therefore,

$$


\begin{aligned}sin⁡𝑣 & =±\sqrt{\frac{9}{25}} \\ & =±\frac{3}{5}.\end{aligned}


$$

We're given that $v$ lies in the first quadrant, where sine is positive. So, we disregard the negative value, and we have

$$


\sin v= \dfrac{3}{5}.


$$

We can now apply the sum formula, as follows:

$$


\begin{aligned}sin⁡(𝑢+𝑣) & =sin⁡𝑢cos⁡𝑣+cos⁡𝑢sin⁡𝑣 \\ & =(\frac{3}{4})(\frac{4}{5})+(−\frac{\sqrt{7}}{4})(\frac{3}{5}) \\ & =\frac{12}{20}−\frac{3\sqrt{7}}{20} \\ & =\frac{12−3\sqrt{7}}{20}\end{aligned}


$$

Finally, $a=12, b=3,$ and $a+b = 15.$

### Example: Computing the Sine of a Composite Angle Using Angles in the Second, Third, or Fourth Quadrants

#### Question

Suppose that for the angles $u$ and $v,$ we have

$$


\cos u = \dfrac{7}{25}, \qquad \sin v = \dfrac{4}{5}, \qquad \cos v = \dfrac {3} {5}.


$$

Given that $u$ lies in the fourth quadrant, find the value of $\sin(u-v).$

#### Explanation

First, recall the difference formula for sine:

$$


\sin(u-v) = \sin u \cos v- \cos u \sin v


$$

We know the values of $\cos{u}$, $\sin{v}$, and $\cos{v}.$ To find the missing value of $\sin{u}$, we can use the Pythagorean identity:

$$


\sin^2 u + \cos^2 u= 1 \qquad\Longrightarrow\qquad \sin^2 u = 1- \cos^2 u


$$

Substituting our values into the Pythagorean identity, we get

$$


\begin{aligned}sin^{2}⁡𝑢 & =1−cos^{2}⁡𝑢 \\ & =1−(\frac{7}{25})^{2} \\ & =1−\frac{7^{2}}{25^{2}} \\ & =1−\frac{49}{625} \\ & =\frac{625}{625}−\frac{49}{625} \\ & =\frac{576}{625}.\end{aligned}


$$

Therefore,

$$


\begin{aligned}sin⁡𝑢 & =±\sqrt{\frac{576}{625}} \\ & =±\frac{24}{25}.\end{aligned}


$$

We're given that $u$ lies in the fourth quadrant, where sine is negative. So, we disregard the positive value, and we have

$$


\sin u= -\dfrac{24}{25}.


$$

We can now apply the difference formula, as follows:

$$


\begin{aligned} \sin(u - v) &= \sin u \cos v - \cos u \sin v \\[5pt] &= \left( -\dfrac {24}{25} \right)\left(\dfrac {3} {5}\right) - \left(\dfrac {7}{25}\right) \left( \dfrac {4} {5}\right) \\[5pt] &= -\dfrac {72} {125} - \dfrac {28} {125} \\[5pt] &= -\dfrac {100} {125}\\[5pt] &= -\dfrac {4} {5}. \end{aligned}


$$
