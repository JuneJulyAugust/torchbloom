# Verifying Trigonometric Identities Using the Double-Angle Formulas for Cosine

Source: https://www.mathacademy.com/topics/832?courseId=43
Topic ID: 832

## Prerequisites

- [The Double-Angle Formula for Cosine](./831-the-double-angle-formula-for-cosine.md)

## Lesson

### Introduction

Let's try to simplify the following expression:

$$



\dfrac{\cos{2x}+\sin^2{x}}{\cos{x}}



$$

Since the expression contains $\cos{2x},$ we should immediately think of using the double-angle formula for cosine. The question is, which double-angle formula should we use?

The formula

$$



\cos{2x}=\cos^2{x}-\sin^2{x}



$$

seems like the natural choice because we can see that one of the terms will cancel with the $\sin^2{x}$ term in the numerator. So let's substitute this into our expression and simplify:

$$



\begin{aligned}\frac{cos⁡2𝑥+sin^{2}⁡𝑥}{cos⁡𝑥} & =\frac{(cos^{2}⁡𝑥−sin^{2}⁡𝑥)+sin^{2}⁡𝑥}{cos⁡𝑥} \\ & =\frac{(cos^{2}⁡𝑥−sin^{2}⁡𝑥)+sin^{2}⁡𝑥}{cos⁡𝑥} \\ & =\frac{cos^{2}⁡𝑥}{cos⁡𝑥} \\ & =\frac{cos⁡𝑥⋅cos⁡𝑥}{cos⁡𝑥} \\ & =\frac{cos⁡𝑥⋅cos⁡𝑥}{cos⁡𝑥} \\ & =cos⁡𝑥\end{aligned}



$$

So, the expression $\dfrac{\cos{2x}+\sin^2{x}}{\cos{x}}$ is equivalent to $\cos{x},$ and we write

$$



\dfrac{\cos{2x}+\sin^2{x}}{\cos{x}} = \cos x.



$$

**Note:** In general, depending on the particular expression we're trying to simplify, we may want to use any one of the following double-angle formulas for cosine:

$$



\begin{aligned}cos⁡2𝑥 & =cos^{2}⁡𝑥−sin^{2}⁡𝑥 \\ cos⁡2𝑥 & =2cos^{2}⁡𝑥−1 \\ cos⁡2𝑥 & =1−2sin^{2}⁡𝑥\end{aligned}



$$

### Example: Simplifying Expressions Using the Basic Form of the Double-Angle Formula for Cosine

#### Question

Which expression is equivalent to $\dfrac{\cos{2x}}{\cos{x}+\sin{x}}?$

#### Explanation

First, we recall the double-angle formula for cosine:

$$



\cos{2x}= \cos^2{x}-\sin^2{x}



$$

Using the double angle formula for cosine, we simplify the given expression, as follows:

$$



\begin{aligned}\frac{cos⁡2𝑥}{cos⁡𝑥+sin⁡𝑥} & =\frac{cos^{2}⁡𝑥−sin^{2}⁡𝑥}{cos⁡𝑥+sin⁡𝑥} \\ & =\frac{(cos⁡𝑥−sin⁡𝑥)(cos⁡𝑥+sin⁡𝑥)}{cos⁡𝑥+sin⁡𝑥} \\ & =\frac{(cos⁡𝑥−sin⁡𝑥)(cos⁡𝑥+sin⁡𝑥)}{cos⁡𝑥+sin⁡𝑥} \\ & =cos⁡𝑥−sin⁡𝑥\end{aligned}



$$

### Example: Simplifying Expressions Using the Cosine Form of the Double-Angle Formula

#### Question

Simplify $\dfrac {(2\cos x - 1) (2\cos x + 1) - 1}{\sin 2 x}.$

#### Explanation

First, we expand the parentheses in the numerator and then simplify, as follows:

$$



\begin{aligned}\frac{(2cos⁡𝑥−1)(2cos⁡𝑥+1)−1}{sin⁡2𝑥} & =\frac{(4cos^{2}⁡𝑥−1)−1}{sin⁡2𝑥} \\ & =\frac{4cos^{2}⁡𝑥−2}{sin⁡2𝑥} \\ & =\frac{2(2cos^{2}⁡𝑥−1)}{sin⁡2𝑥}\end{aligned}



$$

Then, we recall the double-angle formula for cosine:

$$



\cos{2x} = 2\cos^2{x}-1



$$

Substituting this into our expression above, we get

$$



\begin{aligned}\frac{2(2cos^{2}⁡𝑥−1)}{sin⁡2𝑥} & =\frac{2\,cos⁡2𝑥}{sin⁡2𝑥} \\ & =2cot⁡2𝑥.\end{aligned}



$$

### Example: Simplifying Expressions Using the Sine Form of the Double-Angle Formula

#### Question

Simplify $\dfrac {\cos 2 \theta}{\sin^2 \theta}.$

#### Explanation

First, we recall the double-angle formula for cosine:

$$



\cos{2\theta}=1-2\sin^2{\theta}



$$

Substituting the double-angle formula into the numerator of our expression, we get

$$



\begin{aligned}\frac{cos⁡2𝜃}{sin^{2}⁡𝜃} & =\frac{1−2sin^{2}⁡𝜃}{sin^{2}⁡𝜃} \\ & =\frac{1}{sin^{2}⁡𝜃}−\frac{2sin^{2}⁡𝜃}{sin^{2}⁡𝜃} \\ & =\frac{1}{sin^{2}⁡𝜃}−\frac{2sin^{2}⁡𝜃}{sin^{2}⁡𝜃} \\ & =csc^{2}⁡𝜃−2.\end{aligned}



$$
