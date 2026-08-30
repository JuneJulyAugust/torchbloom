# Alternate Forms of the Pythagorean Identity

Source: https://www.mathacademy.com/topics/205?courseId=43
Topic ID: 205

## Prerequisites

- [Simplifying Expressions Using the Pythagorean Identity](./207-simplifying-expressions-using-the-pythagorean-identity.md)

## Lesson

### Introduction

Let's recall the Pythagorean identity:

$$



\cos^2\theta + \sin^2\theta = 1



$$

If we subtract $\sin^2\theta$ from both sides, we get another identity:

$$



\cos^2\theta = 1 - \sin^2\theta



$$

We call this an **alternate form** of the Pythagorean identity.

We can get a second alternate form if we start with $\cos^2\theta + \sin^2\theta = 1$ and subtract $\cos^2\theta$ from both sides. This gives

$$



\sin^2\theta = 1 - \cos^2\theta.



$$

The alternate forms can be used to rewrite $\cos^2\theta$ in terms of $\sin^2\theta$ and vice-versa. Let's see how this works in practice.

### Example: Simplifying Expression Using an Alternate Form of the Pythagorean Identity

#### Question

Simplify the expression $3\cos^2 x \left(\sec^2 x -1\right).$

#### Explanation

First, we expand the parentheses and simplify the resulting expression:

$$



3\cos^2 x \left(\sec^2 x -1\right) = 3\cos^2 x \sec^2 x - 3\cos^2 x



$$

Then, we use the identity $\sec x = \dfrac{1}{\cos x}$ to further simplify the expression:

$$



\begin{aligned}3cos^{2}⁡𝑥sec^{2}⁡𝑥−3cos^{2}⁡𝑥 & =3cos^{2}⁡𝑥⋅(\frac{1}{cos⁡𝑥})^{2}−3cos^{2}⁡𝑥 \\ & =3cos^{2}⁡𝑥⋅\frac{1}{cos^{2}⁡𝑥}−3cos^{2}⁡𝑥 \\ & =\frac{3cos^{2}⁡𝑥}{cos^{2}⁡𝑥}−3cos^{2}⁡𝑥 \\ & =\frac{3cos^{2}⁡𝑥}{cos^{2}⁡𝑥}−3cos^{2}⁡𝑥 \\ & =3−3cos^{2}⁡𝑥 \\ & =3(1−cos^{2}⁡𝑥)\end{aligned}



$$

Now, we can use the identity $\sin^2 x = 1-\cos^2 x$ to rewrite the expression in the parentheses, as follows:

$$



3(1-\cos^2 x) = 3\cdot \sin^2 x = 3\sin^2 x



$$

Therefore, we conclude that

$$



3\cos^2 x \left(\sec^2 x -1\right)= 3\sin^2 x.



$$

### Example: Simplifying Rational Expressions Using an Alternate Form of the Pythagorean Identity

#### Question

Simplify the trigonometric expression $\dfrac{\cos{x}}{1-\cos^2{x}}.$

#### Explanation

First, we rewrite the denominator using $1-\cos^2 x = \sin^2 x.$ This gives

$$



\dfrac{\cos{x}}{1-\cos^2{x}} = \dfrac{\cos{x}}{\sin^2{x}}.



$$

Next, we simplify the expression by separating out the factors, as follows:

$$



\begin{aligned}\frac{cos⁡𝑥}{sin^{2}⁡𝑥} & =\frac{cos⁡𝑥⋅1}{sin⁡𝑥⋅sin⁡𝑥} \\ & =\frac{cos⁡𝑥}{sin⁡𝑥}⋅\frac{1}{sin⁡𝑥} \\ & =cot⁡𝑥csc⁡𝑥\end{aligned}



$$

Therefore, we conclude that

$$



\dfrac{\cos{x}}{1-\cos^2{x}}=\cot{x}\csc{x}.



$$

### Example: Simplifying Expressions by Factoring an Alternate Form of the Pythagorean Identity

#### Question

Simplify the expression $\dfrac{\cos^2 x}{1-\sin x}.$

#### Explanation

First, we rewrite the numerator using $1-\sin^2 x = \cos^2 x,$ as follows:

$$



\dfrac{\cos^2 x}{1-\sin x} = \dfrac{1-\sin^2 x}{1-\sin x}



$$

Then, we factor the numerator as a difference of squares, and simplify:

$$



\begin{aligned}\frac{1−sin^{2}⁡𝑥}{1−sin⁡𝑥} & =\frac{(1−sin⁡𝑥)(1+sin⁡𝑥)}{1−sin⁡𝑥} \\ & =\frac{(1−sin⁡𝑥)(1+sin⁡𝑥)}{1−sin⁡𝑥} \\ & =\frac{1+sin⁡𝑥}{1} \\ & =1+sin⁡𝑥\end{aligned}



$$

Therefore, we conclude that

$$



\dfrac{\cos^2 x}{1-\sin x} = 1 + \sin x.



$$
