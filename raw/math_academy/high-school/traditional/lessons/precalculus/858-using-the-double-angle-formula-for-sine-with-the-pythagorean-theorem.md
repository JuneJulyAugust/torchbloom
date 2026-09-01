# Using the Double-Angle Formula for Sine With the Pythagorean Theorem

Source: https://www.mathacademy.com/topics/858?courseId=43
Topic ID: 858

## Prerequisites

- [The Double-Angle Formula for Sine](./271-the-double-angle-formula-for-sine.md)
- [Extending the Pythagorean Identity to All Quadrants](../algebra-ii/2021-extending-the-pythagorean-identity-to-all-quadrants.md)

## Lesson

### Introduction

Suppose we know that $\sin{\theta}=\dfrac{3}{5}$ for some angle $\theta$ that lies in the first quadrant. Can we find the exact value of $\sin2\theta$ without using a calculator?

Recall that the double-angle formula for sine states that

$$



\sin{2\theta}=2\sin{\theta}\cos{\theta}.



$$

We already know the value of $\sin{\theta}.$ To calculate $\cos\theta,$ we use the Pythagorean identity:

$$



\sin^2{\theta}+\cos^2{\theta}=1\qquad\Rightarrow\qquad \cos{\theta}=\pm \sqrt{1-\sin^2{\theta}}



$$

Since $\theta$ lies in the first quadrant, we know that $\cos{\theta}>0,$ and so we choose the positive square root. Let's now proceed to compute $\cos\theta\mathbin{:}$

$$



\begin{aligned}cos⁡𝜃 & =\sqrt{1−sin^{2}⁡𝜃} \\ & =\sqrt{1−(\frac{3}{5})^{2}} \\ & =\sqrt{1−\frac{9}{25}} \\ & =\sqrt{\frac{16}{25}} \\ & =\frac{4}{5}\end{aligned}



$$

Therefore, we have

$$



\begin{aligned}sin⁡2𝜃 & =2sin⁡𝜃cos⁡𝜃 \\ & =2⋅\frac{3}{5}⋅\frac{4}{5} \\ & =\frac{24}{25}.\end{aligned}



$$

Therefore, we conclude that $\sin{2\theta}=\dfrac{24}{25}$.

### Example: Finding the Exact Value of the Sine of a Double Angle in the First Quadrant Given Its Sine or Cosine

#### Question

Given that $\cos{\theta} = \dfrac{1}{3}$ and $0^\circ < \theta < 90^{\circ},$ what is the value of $\sin{2\theta}?$

#### Explanation

To find the value of $\sin2\theta,$ we use the double-angle formula for sine:

$$



\sin2\theta = 2\sin\theta\cos\theta



$$

First, we need to find the value of $\sin{\theta}.$ From the Pythagorean identity, we have

$$



\sin \theta = \pm \sqrt{1 - \cos^2 \theta}.



$$

Substituting $\cos{\theta} = \dfrac{1}{3}$ into the above, we get

$$



\begin{aligned}sin⁡𝜃 & =±\sqrt{1−(\frac{1}{3})^{2}} \\ & =±\sqrt{1−\frac{1}{9}} \\ & =±\sqrt{\frac{8}{9}} \\ & =±\frac{2\sqrt{2}}{3}.\end{aligned}



$$

We're given that $\theta$ lies in the first quadrant. Therefore, $\sin\theta > 0,$ and we take the ** square root in the above expression. Hence,

$$



\sin\theta = \dfrac{2\sqrt{2}}{3}.



$$

Finally, substituting our values for sine and cosine into the double-angle formula for sine, we get

$$



\begin{aligned}sin⁡2𝜃 & =2sin⁡𝜃cos⁡𝜃 \\ & =2⋅(\frac{2\sqrt{2}}{3})⋅(\frac{1}{3}) \\ & =\frac{4\sqrt{2}}{9}.\end{aligned}



$$

### Example: Finding the Exact Value of the Sine of a Double Angle Given Its Sine or Cosine

#### Question

Given that $\sin{\theta}=\dfrac{\sqrt 2}{2}$ and $\dfrac{\pi}{2}< \theta < \pi$, what is the value of $\sin2\theta?$

#### Explanation

To find the value of $\sin2\theta,$ we use the double-angle formula for sine:

$$



\sin2\theta = 2\sin\theta\cos\theta



$$

First, we need to find the value of $\cos{\theta}.$ From the Pythagorean identity, we have

$$



\cos \theta = \pm \sqrt{1 - \sin^2 \theta}.



$$

Substituting $\sin{\theta} = \dfrac{\sqrt{2}}{2}$ into the above, we get

$$



\begin{aligned}cos⁡𝜃 & =±\sqrt{1−(−\frac{\sqrt{2}}{2})^{2}} \\ & =±\sqrt{1−\frac{2}{4}} \\ & =±\sqrt{1−\frac{1}{2}} \\ & =±\sqrt{\frac{1}{2}} \\ & =±\frac{1}{\sqrt{2}} \\ & =±\frac{\sqrt{2}}{2}.\end{aligned}



$$

We're given that $\theta$ lies in the second quadrant. Therefore, $\cos\theta \lt 0,$ and we take the ** square root in the above expression. Hence,

$$



\cos x = -\dfrac{\sqrt{2}}{2}.



$$

Finally, substituting our values for sine and cosine into the double-angle formula for sine, we get

$$



\begin{aligned}sin⁡2𝜃 & =2sin⁡𝜃cos⁡𝜃 \\ & =2⋅(\frac{\sqrt{2}}{2})⋅(−\frac{\sqrt{2}}{2}) \\ & =−\frac{2⋅\sqrt{2}⋅\sqrt{2}}{2⋅2} \\ & =−\frac{2⋅2}{2⋅2} \\ & =−1.\end{aligned}



$$

### Example: Finding the Exact Value of the Sine of a Double Angle Given Its Secant or Cosecant

#### Question

Given that $\csc \theta = 2$ and $\theta$ lies in the first quadrant, what is the value of $\sin 2\theta?$

#### Explanation

To find the value of $\sin2\theta,$ we use the double-angle formula for sine:

$$



\sin2\theta = 2\sin\theta\cos\theta



$$

First, recall that $\sin{\theta} = \dfrac{1}{\csc{\theta}}.$ Therefore,

$$



\sin \theta = \dfrac{1}{\csc \theta} = \dfrac{1}{2}.



$$

Now, we need to find the value of $\cos{\theta}.$ From the Pythagorean identity, we have

$$



\cos \theta = \pm \sqrt{1 - \sin^2 \theta}.



$$

Substituting $\sin\theta = \dfrac12$ into the above, we get

$$



\begin{aligned}cos⁡𝜃 & =±\sqrt{1−sin^{2}⁡𝜃} \\ & =±\sqrt{1−(\frac{1}{2})^{2}} \\ & =±\sqrt{1−\frac{1}{4}} \\ & =±\sqrt{\frac{3}{4}} \\ & =±\frac{\sqrt{3}}{2}.\end{aligned}



$$

We're given that $\theta$ lies in the first quadrant. Therefore, $\cos\theta \gt 0,$ and we take the ** square root in the above expression. Hence,

$$



\cos{\theta} = \dfrac{\sqrt{3}}{2}.



$$

Finally, substituting our values for sine and cosine into the double-angle formula for sine, we get

$$



\begin{aligned}sin⁡2𝜃 & =2sin⁡𝜃cos⁡𝜃 \\ & =2⋅(\frac{1}{2})⋅(\frac{\sqrt{3}}{2}) \\ & =\frac{\sqrt{3}}{2}.\end{aligned}



$$

### Example: Finding the Exact Value of the Cosecant of a Double Angle Given Its Sine or Cosine

#### Question

Find the exact value of $\csc{2\theta}$ if $\cos{\theta}=\dfrac{\sqrt{3}}{3}$ and $\theta$ lies in the fourth quadrant.

#### Explanation

Recall that $\csc{2\theta} = \dfrac{1}{\sin{2\theta}}.$ So, we need to find the value of $\sin{2\theta}$ and then compute its reciprocal.

To find the value of $\sin2\theta,$ we use the double-angle formula for sine:

$$



\sin2\theta = 2\sin\theta\cos\theta



$$

First, let's find the value of $\sin{\theta}.$ From the Pythagorean identity, we have

$$



\sin \theta = \pm \sqrt{1 - \cos^2 \theta}.



$$

Substituting $\cos \theta = \dfrac{\sqrt{3}}{3}$ into the above, we get

$$



\begin{aligned}sin⁡𝜃 & =±\sqrt{1−cos^{2}⁡𝜃} \\ & =±\sqrt{1−(\frac{\sqrt{3}}{3})^{2}} \\ & =±\sqrt{1−\frac{1}{3}} \\ & =±\sqrt{\frac{2}{3}} \\ & =±\frac{\sqrt{2}}{\sqrt{3}}.\end{aligned}



$$

We're given that $\theta$ lies in the fourth quadrant. Therefore, $\sin\theta \lt 0,$ and we take the ** root in the above expression. Hence,

$$



\sin{\theta} = -\dfrac{\sqrt{2}}{\sqrt 3}.



$$

Now, substituting our values for sine and cosine into the double-angle formula for sine, we have

$$



\begin{aligned}sin⁡2𝜃 & =2sin⁡𝜃cos⁡𝜃 \\ & =2⋅(−\frac{\sqrt{2}}{\sqrt{3}})⋅(\frac{\sqrt{3}}{3}) \\ & =−\frac{2\sqrt{2}}{3}.\end{aligned}



$$

Finally,

$$



\begin{aligned}csc⁡2𝜃 & =\frac{1}{sin⁡2𝜃}=\frac{1}{(−\frac{2\sqrt{2}}{3})}=−\frac{3}{2\sqrt{2}}=−\frac{3\sqrt{2}}{4}.\end{aligned}



$$
