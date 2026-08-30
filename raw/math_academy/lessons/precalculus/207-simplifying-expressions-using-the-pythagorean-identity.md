# Simplifying Expressions Using the Pythagorean Identity

Source: https://www.mathacademy.com/topics/207?courseId=43
Topic ID: 207

## Prerequisites

- [Simplifying Expressions Using Basic Trigonometric Identities](./203-simplifying-expressions-using-basic-trigonometric-identities.md)
- [Using the Pythagorean Identity in the First Quadrant](../algebra-ii/1453-using-the-pythagorean-identity-in-the-first-quadrant.md)

## Lesson

### Introduction

The Pythagorean identity is

$$



\cos^2{\theta}+\sin^2{\theta}=1.



$$

We can use the Pythagorean identity to simplify trigonometric expressions. For example, let's try to simplify the following:

$$



2\sin \theta \left(\sin \theta + \dfrac {\cos^2 \theta} {\sin \theta}\right)



$$

We first expand the parentheses, and then simplify the resulting expression:

$$



\begin{aligned}2sin⁡𝜃(sin⁡𝜃+\frac{cos^{2}⁡𝜃}{sin⁡𝜃}) & =2sin^{2}⁡𝜃+2sin⁡𝜃⋅\frac{cos^{2}⁡𝜃}{sin⁡𝜃} \\ & =2sin^{2}⁡𝜃+2sin⁡𝜃⋅\frac{cos^{2}⁡𝜃}{sin⁡𝜃} \\ & =2sin^{2}⁡𝜃+2cos^{2}⁡𝜃 \\ & =2(sin^{2}⁡𝜃+cos^{2}⁡𝜃)\end{aligned}



$$

Now, we can use the Pythagorean identity to rewrite the expression in the parentheses, as follows:

$$



2(\sin^2\theta + \cos^2\theta) =2\cdot 1 = 2



$$

Therefore, we conclude that

$$



2\sin \theta \left(\sin \theta + \dfrac {\cos^2 \theta} {\sin \theta}\right) = 2.



$$

### Example: Simplifying an Expression by Expanding Parentheses and Using the Pythagorean Identity

#### Question

Simplify the expression $\sin x(2\cos x - \sin x) - \cos^2x.$

#### Explanation

First, we expand the parentheses:

$$



\begin{aligned}2sin⁡𝑥cos⁡𝑥−sin^{2}⁡𝑥−cos^{2}⁡𝑥\end{aligned}



$$

Next, we group the $\sin^2 x$ and $\cos^2 x$ terms.

$$



2\sin x\cos x -(\sin^2x + \cos^2 x)



$$

Then, we use $\sin^2{x} + \cos^2{x} = 1$ to simplify the expression in the parentheses:

$$



2\sin x\cos x - 1



$$

Therefore, we conclude that

$$



\sin x(2\cos x - \sin x) - \cos^2x = 2\sin x\cos x - 1.



$$

### Example: Simplifying an Expression by Factoring and Using the Pythagorean Identity

#### Question

Simplify the trigonometric expression $\sin^4{\theta}+\sin^2{\theta}\cos^2{\theta}.$

#### Explanation

First, we factor $\sin^2\theta$ from the expression:

$$



\sin^4{\theta}+\sin^2{\theta}\cos^2{\theta} = \sin^2{\theta}\cdot(\sin^2{\theta}+\cos^2{\theta})



$$

Then, we use $\cos^2\theta + \sin^2\theta = 1$ to simplify the expression in the parentheses:

$$



\begin{aligned}sin^{2}⁡𝜃⋅(sin^{2}⁡𝜃+cos^{2}) & =sin^{2}⁡𝜃⋅1=sin^{2}⁡𝜃\end{aligned}



$$

Therefore, we conclude that

$$



\sin^4{\theta}+\sin^2{\theta}\cos^2{\theta} = \sin^2\theta.



$$

### Example: Simplifying a Rational Expression Using the Pythagorean Identity

#### Question

Simplify the trigonometric expression $\dfrac {\cos \theta \sin^2 \theta + \cos^3 \theta}{\sin\theta}.$

#### Explanation

First, we factor the numerator:

$$



\dfrac {\cos \theta \sin^2 \theta + \cos^3 \theta} {\sin \theta} = \dfrac {\cos \theta \cdot (\sin^2 \theta + \cos^2 \theta)} {\sin \theta}



$$

Next, we use the Pythagorean identity to rewrite the expression in the parentheses, and then we simplify the resulting expression as much as possible.

$$



\begin{aligned}\frac{cos⁡𝜃⋅(sin^{2}⁡𝜃+cos^{2}⁡𝜃)}{sin⁡𝜃} & =\frac{cos⁡𝜃⋅(1)}{sin⁡𝜃} \\ & =\frac{cos⁡𝜃}{sin⁡𝜃} \\ & =cot⁡𝜃\end{aligned}



$$

Therefore, we conclude that:

$$



\dfrac {\cos \theta \sin^2 \theta + \cos^3 \theta} {\sin \theta} = \cot \theta.



$$

### Example: Simplifying a Trigonometric Expression Using a Common Denominator and the Pythagorean Identity

#### Question

Simplify the trigonometric expression $\dfrac{\sin{\theta}}{1+\cos{\theta}}+\cot{\theta}.$

#### Explanation

First, we rewrite the second term using the identity $\cot \theta = \dfrac{\cos\theta}{\sin\theta},$ as follows:

$$



\dfrac{\sin{\theta}}{1+\cos{\theta}}+\dfrac{\cos{\theta}}{\sin{\theta}}



$$

Next, we put both terms over a common denominator, and combine the two fractions:

$$



\begin{aligned}\frac{sin⁡𝜃⋅sin⁡𝜃}{sin⁡𝜃(1+cos⁡𝜃)}+\frac{cos⁡𝜃⋅(1+cos⁡𝜃)}{sin⁡𝜃(1+cos⁡𝜃)} & = \\ \frac{sin⁡𝜃⋅sin⁡𝜃+cos⁡𝜃⋅(1+cos⁡𝜃)}{sin⁡𝜃(1+cos⁡𝜃)} & \end{aligned}



$$

Finally, we simplify as follows:

$$



\begin{aligned}\frac{sin^{2}⁡𝜃+cos⁡𝜃+cos^{2}⁡𝜃}{sin⁡𝜃(1+cos⁡𝜃)} & = \\ \frac{(sin^{2}⁡𝜃+cos^{2}⁡𝜃)+cos⁡𝜃}{sin⁡𝜃(1+cos⁡𝜃)} & = \\ \frac{1+cos⁡𝜃}{sin⁡𝜃(1+cos⁡𝜃)} & = \\ \frac{1}{sin⁡𝜃} & = \\ csc⁡𝜃 & \end{aligned}



$$

Therefore, we conclude that

$$



\dfrac{\sin{\theta}}{1+\cos{\theta}}+\cot{\theta} = \csc\theta.



$$
