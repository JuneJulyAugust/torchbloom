# Simplifying Expressions Using the Secant-Tangent Identity

Source: https://www.mathacademy.com/topics/1454?courseId=101
Topic ID: 1454

## Prerequisites

- [Alternate Forms of the Pythagorean Identity](./205-alternate-forms-of-the-pythagorean-identity.md)

## Lesson

### Introduction

Let's recall the Pythagorean identity:

$$


\begin{aligned}cos^{2}⁡𝑥+sin^{2}⁡𝑥=1\end{aligned}


$$

If we divide both sides of this identity by ${\color{black}\cos^2 x},$ we get the equation

$$


\dfrac {\cos^2 x} {\color{black}\cos^2 x} + \dfrac {\sin^2 x}{\color{black}\cos^2 x} = \dfrac 1 {\color{black}\cos^2 x}


$$

which can be written as follows:

$$


1+ \left(\dfrac {\sin x}{\cos x}\right)^2 = \left(\dfrac 1 {\cos x}\right)^2 \qquad (\ast)


$$

Now, recall the following identities:

$$


\tan x = \dfrac{\sin x}{\cos x}, \qquad \sec x = \dfrac{1}{\cos x}


$$

Substituting the above identities into $(\ast)$, we get

$$


\begin{aligned}1+(\frac{sin⁡𝑥}{cos⁡𝑥})^{2} & =(\frac{1}{cos⁡𝑥})^{2} \\ 1+(tan⁡𝑥)^{2} & =(sec⁡𝑥)^{2}\end{aligned}


$$

$$


1 + \tan^2 x = \sec^2 x.


$$

The final identity is called the **secant-tangent identity**. We often use it to simplify trigonometric expressions containing both tangent and secant functions.

### Example: Simplifying an Expression Using the Secant-Tangent Identity: Replacing a Squared Tangent

#### Question

Simplify the expression $\dfrac{2\sec^2 \theta}{1+\tan^2 \theta}.$

#### Explanation

First, let's recall the secant-tangent identity:

$$


1+\tan^2 \theta = \sec^2{\theta}


$$

We rewrite the given expression using the secant-tangent identity as follows:

$$


\dfrac{2\sec^2 \theta}{\color{blue}1+\tan^2 \theta} = \dfrac{2\sec^2 \theta}{\color{blue}\sec^2 \theta}


$$

We now cancel the common factor of $\sec^2 \theta$ in the numerator and denominator and simplify the fraction:

$$


\begin{aligned}\frac{2sec^{2}⁡𝜃}{sec^{2}⁡𝜃} & =\frac{2sec^{2}⁡𝜃}{sec^{2}⁡𝜃} \\ & =\frac{2⋅1}{1} \\ & =2\end{aligned}


$$

Therefore, we conclude that

$$


\dfrac{2\sec^2 \theta}{1+\tan^2 \theta} = 2.


$$

### Example: Simplifying an Expression Using the Secant-Tangent Identity: Replacing a Squared Secant

#### Question

Express $(1-\sec x)(1+\sec x)$ in terms of $\tan x$ only.

#### Explanation

First, let's recall the secant-tangent identity:

$$


1+\tan^2 x = \sec^2{x}


$$

First, we expand the parentheses using the difference of squares formula:

$$


(1-\sec x )(1+\sec x ) = 1 - \sec^2x


$$

Then, we rewrite the expression using the secant-tangent identity as follows:

$$


\begin{aligned}1−sec^{2}⁡𝑥 & =1−(1+tan^{2}⁡𝑥) \\ & =1−1−tan^{2}⁡𝑥 \\ & =−tan^{2}⁡𝑥\end{aligned}


$$

Therefore, we conclude that

$$


(1-\sec x )(1+\sec x )= -\tan^2 x.


$$

### Example: Simplifying an Expression Using the Secant-Tangent and Other Identities

#### Question

Express $2\tan x\cdot(\cot x+\tan{x})$ in terms of $\sec x$ only.

#### Explanation

First, let's recall the secant-tangent identity:

$$


1+\tan^2 x = \sec^2{x}


$$

Also, recall the following identity:

$$


\cot x = \dfrac{1}{\tan x}\quad\Longrightarrow\quad \tan x\cdot \cot x = 1


$$

Using the above identities, we can simplify our expression as follows:

$$


\begin{aligned}2tan⁡𝑥⋅(cot⁡𝑥+tan⁡𝑥) & =2tan⁡𝑥⋅cot⁡𝑥+2tan^{2}⁡𝑥 \\ & =2⋅1+2tan^{2}⁡𝑥 \\ & =2 \,(1+tan^{2}⁡𝑥) \\ & =2\,sec^{2}⁡𝑥\end{aligned}


$$

Therefore, we conclude that

$$


2\tan x\cdot(\cot x+\tan{x})= 2\sec^2x.


$$
