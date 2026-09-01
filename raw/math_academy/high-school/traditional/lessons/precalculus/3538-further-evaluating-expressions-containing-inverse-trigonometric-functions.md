# Further Evaluating Expressions Containing Inverse Trigonometric Functions

Source: https://www.mathacademy.com/topics/3538?courseId=43
Topic ID: 3538

## Prerequisites

- [Evaluating Expressions Containing Inverse Trigonometric Functions](./209-evaluating-expressions-containing-inverse-trigonometric-functions.md)

## Lesson

### Introduction

To evaluate a trigonometric function whose argument is the corresponding inverse function, we can just "cancel out" the two functions, provided that the input $x$ is in the domain of the inverse function.

For example, notice that

$$



\cos \left( \arccos \left( \dfrac{\sqrt 3}{2} \right) \right) = \cos \left( \dfrac{\pi}{6} \right) = \dfrac{\sqrt 3}{2}.



$$

It's as though the $\cos$ and the $\arccos$ cancel out!

In general, we have the following results:

- $\sin(\arcsin(x)) = x$ for $-1 \leq x \leq 1$

- $\cos(\arccos(x)) = x$ for $-1 \leq x \leq 1$

- $\tan(\arctan(x)) = x$ for $-\infty < x < \infty$

More precisely, for every trigonometric function $f(\theta),$ we have that $f(f^{-1}(x)) = x$ for all $x$ in the range of the function $f(x).$

### Example: Evaluating a Trigonometric Function with the Corresponding Inverse Function as Input

#### Question

Find the value of $\sin\left(\arcsin\left(\dfrac{1}{2}\right)\right).$

#### Explanation

The range of $y = \sin x$ is $y\in [-1,1],$ which coincides with the domain of its inverse. So, for any value of $x,$ we have

$$



\sin(\arcsin x) = x.



$$

Therefore,

$$



\sin\left(\arcsin\left(\dfrac{1}{2}\right)\right) = \dfrac{1}{2}.



$$

### Evaluating an Inverse Trigonometric Function Whose Argument is its Corresponding Function

To evaluate an inverse trigonometric function whose argument is its corresponding function, we need to take extra care.

It's possible to "cancel out" the two functions, but we need to make sure that the input $\theta$ is in the range of the inverse function. In particular, we have the following results:

- $\arcsin(\sin(\theta)) = \theta$ provided that $-\dfrac{\pi}{2} \leq \theta \leq \dfrac{\pi}{2}$

- $\arccos(\cos(\theta)) = \theta$ provided that $0\leq \theta \leq \pi$

- $\arctan(\tan(\theta)) = \theta$ provided that $-\dfrac{\pi}{2} < \theta < \dfrac{\pi}{2}$

For example, suppose we want to evaluate

$$



\arccos\left(\cos\left(\dfrac{\pi}{6}\right)\right).



$$

Since our angle $\dfrac{\pi}{6}$ lies within the range of the $\arccos$ function, i.e., $0\leq \dfrac{\pi}{6}\leq \pi,$ we can write down the answer immediately, giving

$$



\arccos\left(\cos\left(\dfrac{\pi}{6}\right)\right) = \dfrac{\pi}{6}.



$$

### The Case When the Angle Is Not in the Range of the Inverse Function

On the other hand, if $\theta$ is not in the range of the inverse function, then we cannot "cancel out" the function and its inverse. For example, suppose we want to calculate

$$



\arccos\left(\cos\left(-\dfrac{\pi}{6}\right)\right).



$$

Our angle $-\dfrac{\pi}{6}$ does *not* lie within the range of the $\arccos$ function! Therefore,

$$



\arccos\left(\cos\left(-\dfrac{\pi}{6}\right)\right)\neq -\dfrac{\pi}{6}.



$$

To find the correct value, we first compute $\cos\left(-\dfrac{\pi}{6}\right).$ This gives

$$



\cos\left(-\dfrac{\pi}{6}\right) = \dfrac{\sqrt 3}{2}.



$$

Finally, we compute $\arccos\left(\dfrac{\sqrt 3}{2}\right).$ This gives

$$



\arccos\left(\dfrac{\sqrt 3}{2}\right) = \dfrac{\pi}{6}.



$$

Therefore,

$$



\arccos\left(\cos\left(-\dfrac{\pi}{6}\right)\right) = \arccos\left(\dfrac{\sqrt 3}{2}\right) = \dfrac{\pi}{6}.



$$

### Example: Evaluating an Inverse Trigonometric Function with the Corresponding Trigonometric Function as Input

#### Question

Find the value of $\arcsin\left(\sin\left(\dfrac{5\pi}{6}\right)\right).$

#### Explanation

First, note that the range of $\theta = \arcsin x$ is given by

$$



-\dfrac\pi 2 \le \theta \le \dfrac\pi2.



$$

Since $\dfrac{5\pi}{6}$ does **** lie within the range of $\theta,$ the answer might not be $\dfrac{5\pi}{6}.$

To find the correct value, we first compute $\sin\left(\dfrac{5\pi}{6}\right){:}$

$$



\sin\left(\dfrac{5\pi}{6}\right) = \dfrac 1 2



$$

Now, we find $\arcsin\left(\dfrac 1 2\right)\mathbin{:}$

$$



\arcsin\left(\dfrac 1 2\right) = \dfrac\pi 6



$$

Therefore, we conclude that

$$



\arcsin\left(\sin\left(\dfrac{5\pi}{6}\right)\right) = \arcsin\left(\dfrac 1 2\right) = \dfrac{\pi}{6}.



$$

### Example: Evaluating a Trigonometric Function with an Inverse Trigonometric Function as Input

#### Question

Find the value of $\cos\left(\arcsin\left(\dfrac{\sqrt{3}}{2}\right)\right).$

#### Explanation

The range of $\theta = \arcsin x$ is given by

$$



-90^\circ \le \theta \le 90^\circ.



$$

Note that the angle $\theta$ spans the first and fourth quadrants.

Since $\dfrac{\sqrt{3}}{2}$ is positive, $\arcsin\left(\dfrac{\sqrt{3}}{2}\right)$ is an angle that lies in the first quadrant, where sine is positive.

![Instructional graphic](../../../../lesson-assets/precalculus/topic-3538/54b8ff713218eaeb.png)

From the first quadrant, we see that

$$



\arcsin\left(\dfrac{\sqrt{3}}{2}\right) = 60^\circ.



$$

Finally then,

$$



\cos\left(\arcsin\left(\dfrac{1}{2}\right)\right) = \cos\left(60^\circ\right) = \dfrac {1} 2.



$$
