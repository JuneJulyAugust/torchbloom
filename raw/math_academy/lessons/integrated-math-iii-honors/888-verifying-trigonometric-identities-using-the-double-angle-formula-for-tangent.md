# Verifying Trigonometric Identities Using the Double-Angle Formula for Tangent

Source: https://www.mathacademy.com/topics/888?courseId=101
Topic ID: 888

## Prerequisites

- [Simplifying Expressions Using the Double-Angle Formula for Tangent](./854-simplifying-expressions-using-the-double-angle-formula-for-tangent.md)

## Lesson

### Introduction

Recall that the double-angle formula for tangent is given by

$$


\tan 2x = \dfrac{2\tan{x}}{1-\tan^2{x}} .


$$

We can use the double-angle formula to simplify many different types of trigonometric expressions. Let's see how.

### Example: Using the Double-Angle Formula for Tangent

#### Question

Simplify $\dfrac{8\tan{2\theta}}{1-\tan^2{2\theta}}.$

#### Explanation

First, let's recall the double-angle formula for tangent:

$$


\tan 2x = \dfrac{2\tan x}{1-\tan^2 x }


$$

Substituting $x=2\theta$ into the above, we get

$$


\begin{aligned}tan⁡4𝜃=\frac{2tan⁡2𝜃}{1−tan^{2}⁡2𝜃}.\end{aligned}


$$

Writing our expression in terms of $\tan 2\theta,$ we have

$$


\begin{aligned}\frac{8tan⁡2𝜃}{1−tan^{2}⁡2𝜃} & =4⋅(\frac{2tan⁡2𝜃}{1−tan^{2}⁡2𝜃})=4\,tan⁡4𝜃.\end{aligned}


$$

Therefore,

$$


\dfrac{8\tan{2\theta}}{1-\tan^2{2\theta}} = 4\tan{4\theta} .


$$

### Example: Simplifying Trigonometric Expressions Using the Double-Angle Formula for Tangent

#### Question

Simplify the expression $\dfrac{5\tan{2x}}{\cot{x}-\tan{x}}.$

#### Explanation

Substituting $\cot{x}=\dfrac{1}{\tan{x}}$ into our expression and then simplifying, we get

$$


\begin{aligned}\frac{5tan⁡2𝑥}{cot⁡𝑥−tan⁡𝑥} & =\frac{5tan⁡2𝑥}{(\frac{1}{tan⁡𝑥}−tan⁡𝑥)} \\ & =\frac{5tan⁡2𝑥⋅tan⁡𝑥}{1−tan^{2}⁡𝑥} \\ & =5tan⁡2𝑥⋅(\frac{tan⁡𝑥}{1−tan^{2}⁡𝑥}).\end{aligned}


$$

Now, let's recall the double-angle formula for tangent:

$$


\tan {2x} = \dfrac {2\tan x}{1-\tan^2 x}


$$

Writing our expression in terms of $\tan2x,$ we have

$$


\begin{aligned}5tan⁡2𝑥⋅(\frac{tan⁡𝑥}{1−tan^{2}⁡𝑥}) & =\frac{5}{2}tan⁡2𝑥⋅(\frac{2tan⁡𝑥}{1−tan^{2}⁡𝑥}) \\ & =\frac{5}{2}tan⁡2𝑥⋅(tan⁡2𝑥) \\ & =\frac{5}{2}tan^{2}⁡2𝑥.\end{aligned}


$$

Therefore,

$$


\dfrac{5\tan{2x}}{\cot{x}-\tan{x}} = \dfrac{5}{2} \tan^2 {2x}.


$$

### Example: Simplifying Advanced Trigonometric Expressions Using the Double-Angle Formula for Tangent

#### Question

Simplify $\dfrac{4\tan^2{\theta}+\left(1-\tan^2{\theta}\right)^2}{1 - 2\tan^2{\theta} + \tan^4{\theta}}.$

#### Explanation

First, we write our expression as a perfect square:

$$


1 - 2\tan^2{\theta} + \tan^4{\theta} = \left( 1-\tan^2{\theta}\right)^2


$$

Rewriting the denominator of our expression using the above identity, we get

$$


\dfrac{4\tan^2{\theta}+\left( 1-\tan^2{\theta}\right)^2}{1 - 2\tan^2{\theta} + \tan^4{\theta}} = \dfrac{4\tan^2{\theta}+\left( 1-\tan^2{\theta}\right)^2}{ \left( 1-\tan^2{\theta}\right)^2}.


$$

Let's now recall the double-angle formula for tangent:

$$


\dfrac{2\tan{\theta}}{1-\tan^2{\theta}}=\tan{2\theta}


$$

Now, splitting the fraction, using the double-angle formula, and applying the tangent-secant formula, we obtain

$$


\begin{aligned}\frac{4tan^{2}⁡𝜃+(1−tan^{2}⁡𝜃)^{2}}{(1−tan^{2}⁡𝜃)^{2}} & =\frac{4tan^{2}⁡𝜃}{(1−tan^{2}⁡𝜃)^{2}}+\frac{(1−tan^{2}⁡𝜃)^{2}}{(1−tan^{2}⁡𝜃)^{2}} \\ & =\frac{4tan^{2}⁡𝜃}{(1−tan^{2}⁡𝜃)^{2}}+\frac{(1−tan^{2}⁡𝜃)^{2}}{(1−tan^{2}⁡𝜃)^{2}} \\ & =(\frac{2tan⁡𝜃}{1−tan^{2}⁡𝜃})^{2}+1 \\ & =tan^{2}⁡2𝜃+1 \\ & =sec^{2}⁡2𝜃.\end{aligned}


$$

Therefore,

$$


\dfrac{4\tan^2{\theta}+\left( 1-\tan^2{\theta}\right)^2}{1 - 2\tan^2{\theta} + \tan^4{\theta}} = \sec^2{2\theta}.


$$
