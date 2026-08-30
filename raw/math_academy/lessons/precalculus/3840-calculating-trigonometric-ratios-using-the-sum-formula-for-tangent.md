# Calculating Trigonometric Ratios Using the Sum Formula for Tangent

Source: https://www.mathacademy.com/topics/3840?courseId=43
Topic ID: 3840

## Prerequisites

- [The Sum and Difference Formulas for Tangent](./273-the-sum-and-difference-formulas-for-tangent.md)
- [Combining the Rules of Exponents](../grade-8/1457-combining-the-rules-of-exponents.md)
- [Extending the Pythagorean Identity to All Quadrants](../algebra-ii/2021-extending-the-pythagorean-identity-to-all-quadrants.md)

## Lesson

### Introduction

We can compute trigonometric ratios using the sum and difference formulas for tangent together with the Pythagorean identity.

Suppose that for the angles $u$ and $v,$ we have

$$



\cos u = \dfrac {3}{5}, \qquad \tan v = 3.



$$

How can we find the value of $\tan(u+v)$ given that $u$ lies in the fourth quadrant?

First, we recall the sum formula for tangent:

$$



\tan(u+v) = \dfrac{\tan{u}+\tan{v}}{1-\tan{u}\tan{v}}



$$

We need to find the value of $\tan u.$ To do that, we first find the value of $\sin u$ using the Pythagorean identity:

$$



\sin^2 u + \cos^2 u= 1 \qquad\Longrightarrow\qquad \sin^2 u = 1- \cos^2 u



$$

Substituting our values into the Pythagorean identity, we get

$$



\begin{aligned}sin^{2}⁡𝑢 & =1−cos^{2}⁡𝑢 \\ & =1−(\frac{3}{5})^{2} \\ & =1−\frac{3^{2}}{5^{2}} \\ & =1−\frac{9}{25} \\ & =\frac{25}{25}−\frac{9}{25} \\ & =\frac{16}{25}.\end{aligned}



$$

Therefore,

$$



\begin{aligned}sin⁡𝑢 & =±\sqrt{√\frac{16}{25}} \\ & =±\frac{4}{5}.\end{aligned}



$$

We're given that $u$ lies in the fourth quadrant, where sine is negative. So, we disregard the positive value, and we have

$$



\sin u = -\dfrac{4}{5}.



$$

We can now compute $\tan u\mathbin{:}$

$$



\begin{aligned}tan⁡𝑢 & =\frac{sin⁡𝑢}{cos⁡𝑢}=\frac{(−\frac{4}{5})}{5}=−\frac{4}{3}\end{aligned}



$$

Finally, we use the sum formula for the tangent:

$$



\begin{aligned}tan⁡(𝑢+𝑣) & =\frac{tan⁡𝑢+tan⁡𝑣}{1−tan⁡𝑢tan⁡𝑣} \\ & =\frac{(−\frac{4}{3}+3)}{3} \\ & =\frac{(−\frac{4}{3}+\frac{9}{3})}{3} \\ & =\frac{(\frac{5}{3})}{3} \\ & =\frac{1}{3}\end{aligned}



$$

### Example: Computing the Tangent of a Composite Angle Using Angles in the First Quadrant

#### Question

Suppose that for the angles $u$ and $v,$ we have

$$



\sin u = \dfrac {4}{5} , \qquad \tan v = \dfrac{1}{2}.



$$

Given that $u$ lies in the first quadrant, find the value of $\tan\left(u + v\right).$

#### Explanation

First, we recall the sum formula for tangent:

$$



\tan(u+v) = \dfrac{\tan{u}+\tan{v}}{1-\tan{u}\tan{v}}



$$

We need to find the value of $\tan u.$ To do that, we first find the value of $\cos{u}$ using the Pythagorean identity:

$$



\sin^2 u + \cos^2 u= 1 \qquad\Longrightarrow\qquad \cos^2 u = 1- \sin^2 u



$$

Substituting our values into the Pythagorean identity, we get

$$



\begin{aligned}cos^{2}⁡𝑢 & =1−sin^{2}⁡𝑢 \\ & =1−(\frac{4}{5})^{2} \\ & =1−\frac{4^{2}}{5^{2}} \\ & =1−\frac{16}{25} \\ & =\frac{25}{25}−\frac{16}{25} \\ & =\frac{9}{25}.\end{aligned}



$$

Therefore,

$$



\begin{aligned}cos⁡𝑢 & =±\sqrt{√\frac{9}{25}} \\ & =±\frac{3}{5}.\end{aligned}



$$

We're given that $u$ lies in the first quadrant, where cosine is positive. So, we disregard the negative value, and we have

$$



\cos u= \dfrac{3}{5}.



$$

We can now compute $\tan u\mathbin{:}$

$$



\begin{aligned}tan⁡𝑢 & =\frac{sin⁡𝑢}{cos⁡𝑢}=\frac{(\frac{4}{5})}{5}=\frac{4}{3}\end{aligned}



$$

Finally, we use the sum formula for the tangent:

$$



\begin{aligned}tan⁡(𝑢+𝑣) & =\frac{tan⁡𝑢+tan⁡𝑣}{1−tan⁡𝑢tan⁡𝑣} \\ & =\frac{(\frac{4}{3}+\frac{1}{2})}{3} \\ & =\frac{(\frac{11}{6})}{6} \\ & =\frac{11}{2}.\end{aligned}



$$

### Example: Computing the Tangent of a Composite Angle Using Angles in the Second, Third, and Fourth Quadrants

#### Question

Suppose that for the angles $u$ and $v,$ we have

$$



\sin u = -\dfrac{2}{\sqrt{5}} , \qquad \tan v = 4.



$$

Given that $u$ lies in the third quadrant, find the value of $\tan\left(u - v\right).$

#### Explanation

First, we recall the difference formula for tangent:

$$



\tan(u-v) = \dfrac{\tan u - \tan v}{1+\tan u \tan v}



$$

We need to find the value of $\tan u.$ To do that, we first find the value of $\cos{u}$ using the Pythagorean identity:

$$



\sin^2 u + \cos^2 u= 1 \qquad\Longrightarrow\qquad \cos^2 u = 1- \sin^2 u



$$

Substituting our values into the Pythagorean identity, we get

$$



\begin{aligned}cos^{2}⁡𝑢 & =1−sin^{2}⁡𝑢 \\ & =1−(−\frac{2}{\sqrt{√5}})^{2} \\ & =1−(\frac{2}{\sqrt{√5}})^{2} \\ & =1−\frac{2^{2}}{(\sqrt{√5})^{2}} \\ & =1−\frac{4}{5} \\ & =\frac{5}{5}−\frac{4}{5} \\ & =\frac{1}{5}.\end{aligned}



$$

Therefore,

$$



\begin{aligned}cos⁡𝑢 & =±\sqrt{√\frac{1}{5}} \\ & =±\frac{1}{\sqrt{√5}}.\end{aligned}



$$

We're given that $u$ lies in the third quadrant, where cosine is negative. So, we disregard the positive value, and we have

$$



\cos u = -\dfrac{1}{\sqrt{5}}.



$$

We can now compute $\tan u\mathbin{:}$

$$



\begin{aligned}tan⁡𝑢 & =\frac{sin⁡𝑢}{cos⁡𝑢}=\frac{(−\frac{2}{\sqrt{√5}})}{\sqrt{√5}}=2\end{aligned}



$$

Finally, we use the difference formula for the tangent:

$$



\begin{aligned}tan⁡(𝑢−𝑣) & =\frac{tan⁡𝑢−tan⁡𝑣}{1+tan⁡𝑢tan⁡𝑣} \\ & =\frac{2−4}{1+2⋅4} \\ & =\frac{(−2)}{9} \\ & =−\frac{2}{9}\end{aligned}



$$
