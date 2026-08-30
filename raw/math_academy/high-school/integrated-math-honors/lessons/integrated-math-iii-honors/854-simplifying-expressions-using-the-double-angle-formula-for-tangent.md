# Simplifying Expressions Using the Double-Angle Formula for Tangent

Source: https://www.mathacademy.com/topics/854?courseId=101
Topic ID: 854

## Prerequisites

- [The Sum and Difference Formulas for Tangent](./273-the-sum-and-difference-formulas-for-tangent.md)
- [Alternate Forms of the Secant-Tangent Identity](./3857-alternate-forms-of-the-secant-tangent-identity.md)

## Lesson

### Introduction

Let's recall the sum formula for tangent:

$$


\tan{\left(x+y\right)}= \dfrac{\tan{x}+\tan{y}}{1-\tan{x}\tan{y}}


$$

Substituting $y = x$ into the above gives

$$


\tan{\left(x+x\right)} = \dfrac{\tan{x}+\tan x}{1-\tan{x}\tan x}


$$

which simplifies to

$$


\tan 2x = \dfrac{2\tan{x}}{1-\tan^2{x}}.


$$

This identity is called the **double-angle formula for tangent**.

We can use this formula to simplify complex trigonometric expressions. Let's see how.

### Example: Using the Double-Angle Formula to Simplify Expressions

#### Question

Express $\dfrac{2\tan \left(\dfrac{\pi}{5}\right)}{\tan^2\left(\dfrac{\pi}{5}\right) - 1}$ as a single trigonometric ratio.

#### Explanation

First, we multiply the numerator and denominator of the given expression by $(-1)$ and rewrite it, as follows:

$$


\begin{aligned}\frac{2tan⁡(\frac{𝜋}{5})}{5} & =\frac{−2tan⁡(\frac{𝜋}{5})}{5} \\ & =−\frac{2tan⁡(\frac{𝜋}{5})}{5}\end{aligned}


$$

Now, let's recall the double-angle formula for tangent:

$$


\tan 2x = \dfrac{2\tan x}{1-\tan^2 x }


$$

Substituting $x=\dfrac{\pi}{5}$ into the above, we get

$$


\tan\left(\dfrac{2\pi}{5}\right) = \dfrac{2\tan \left(\dfrac{\pi}{5}\right)}{1 - \tan^2 \left(\dfrac{\pi}{5}\right) } .


$$

Therefore,

$$


-\dfrac{2\tan \left(\dfrac{\pi}{5}\right)}{1-\tan^2 \left(\dfrac{\pi}{5}\right)} = -\tan \left( \dfrac{2\pi}{5} \right).


$$

### Example: Finding the Tangent of a Double Angle Given the Tangent of an Angle

#### Question

Find the value of $\tan{2x}$ given that $\tan{x}=-\sqrt{2}.$

#### Explanation

First, let's recall the double-angle formula for tangent:

$$


\tan{2x} = \dfrac{ 2\tan x } {1 - \tan^2 x }


$$

Substituting $\tan x = -\sqrt{2}$ into the above, we get

$$


\begin{aligned}tan⁡2𝑥 & =\frac{2\,tan⁡𝑥}{1−(tan⁡𝑥)^{2}} \\ & =\frac{2⋅(−\sqrt{2})}{1−(−\sqrt{2})^{2}} \\ & =\frac{−2\sqrt{2}}{−1} \\ & =2\sqrt{2}.\end{aligned}


$$

### Example: Finding Exact Values of Trigonometric Expressions Using the Double-Angle Formula

#### Question

Find the exact value of $\dfrac{5\tan 15^\circ}{1-\tan^2{15^\circ}}.$

#### Explanation

First, let's recall the double-angle formula for tangent:

$$


\dfrac{2\tan x}{1-\tan^2 x } = \tan 2x


$$

Substituting $x=15^\circ$ into the above, we get

$$


\begin{aligned}\frac{2tan⁡15^{∘}}{1−tan^{2}⁡15^{∘}} & =tan⁡(2⋅15^{∘}) \\ & =tan⁡30^{∘} \\ & =\frac{\sqrt{3}}{3}.\end{aligned}


$$

So, we have

$$


\dfrac{2\tan{15^\circ}}{1-\tan^2{15^\circ}} = \dfrac{\sqrt 3}{3}.


$$

Finally, multiplying both sides of the above equation by $\dfrac{5}{2}$ gives

$$


\dfrac{5\tan{15^\circ}}{1-\tan^2{15^\circ}} =\dfrac{5\sqrt 3}{6}.


$$

### Example: Finding Exact Values of Advanced Trigonometric Expressions Using the Double-Angle Formula

#### Question

Simplify $\dfrac {3\tan 35^\circ}{2 - \sec^2 35^\circ}.$

#### Explanation

First, we simplify the given expression using the identity $\sec^2 x = 1 + \tan^2 x \mathbin{:}$

$$


\begin{aligned}\frac{3tan⁡35^{∘}}{2−sec^{2}⁡35^{∘}} & =\frac{3tan⁡35^{∘}}{2−(1+tan^{2}⁡35^{∘})} \\ & =\frac{3tan⁡35^{∘}}{1−tan^{2}⁡35^{∘}}\end{aligned}


$$

Now, let's recall the double-angle formula for tangent:

$$


\dfrac {2\tan x}{1 - \tan^2 x} = \tan 2x


$$

Substituting $x=35^\circ$ in the above, we get

$$


\begin{aligned}\frac{2tan⁡35^{∘}}{1−tan^{2}⁡35^{∘}} & =tan⁡(2⋅35^{∘})=tan⁡70^{∘}.\end{aligned}


$$

Finally, we have

$$


\begin{aligned}\frac{3tan⁡35^{∘}}{1−tan^{2}⁡35^{∘}} & =\frac{3}{2}⋅\underset{tan⁡70^{∘}}{\underset{}{[\frac{2tan⁡35^{∘}}{1−tan^{2}⁡35^{∘}}]}}=\frac{3}{2}tan⁡70^{∘}.\end{aligned}


$$
