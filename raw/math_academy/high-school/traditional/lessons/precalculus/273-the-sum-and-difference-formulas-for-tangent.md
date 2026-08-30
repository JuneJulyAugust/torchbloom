# The Sum and Difference Formulas for Tangent

Source: https://www.mathacademy.com/topics/273?courseId=43
Topic ID: 273

## Prerequisites

- [Evaluating Trigonometric Expressions](../algebra-ii/3766-evaluating-trigonometric-expressions.md)
- [Further Rationalizing Denominators of Algebraic Expressions](../algebra-i/6185-further-rationalizing-denominators-of-algebraic-expressions.md)

## Lesson

### Introduction

The following two identities are known as the **sum and difference formulas for tangent**:

$$



\begin{aligned}tan⁡(𝑥+𝑦) & =\frac{tan⁡𝑥+tan⁡𝑦}{1−tan⁡𝑥tan⁡𝑦} \\ tan⁡(𝑥−𝑦) & =\frac{tan⁡𝑥−tan⁡𝑦}{1+tan⁡𝑥tan⁡𝑦}\end{aligned}



$$

We can use the sum and difference rules to find the exact values of some trigonometric ratios. For example, let's use the sum rule to find the value of

$$



\tan(75^\circ).



$$

We start by writing $75^\circ$ as a sum of special angles:

$$



75^\circ = {\color{blue}45^\circ} + {\color{red}30^\circ}



$$

We now apply the sum formula for tangent as follows:

$$



\begin{aligned}tan⁡(75^{∘}) & =tan⁡(30^{∘}+45^{∘}) \\ & =\frac{tan⁡30^{∘}+tan⁡45^{∘}}{1−tan⁡30^{∘}tan⁡45^{∘}} \\ & =\frac{(\frac{\sqrt{3}}{3}+1)}{3} \\ & =\frac{(\frac{\sqrt{3}}{3}+1)}{3}\end{aligned}



$$

We can simplify this fraction by multiplying the numerator and denominator by $3\mathbin{:}$

$$



\begin{aligned}tan⁡(75^{∘}) & =\frac{(\frac{\sqrt{3}}{3}+1)}{3} \\ & =\frac{3⋅(\frac{\sqrt{3}}{3}+1)}{3} \\ & =\frac{\sqrt{3}+3}{3−\sqrt{3}} \\ & =\frac{3+\sqrt{3}}{3−\sqrt{3}}\end{aligned}



$$

Finally, we rationalize the denominator:

$$



\begin{aligned}tan⁡(75^{∘}) & =\frac{3+\sqrt{3}}{3−\sqrt{3}} \\ & =\frac{3+\sqrt{3}}{3−\sqrt{3}}⋅\frac{3+\sqrt{3}}{3+\sqrt{3}} \\ & =\frac{3^{2}+6\sqrt{3}+(\sqrt{3})^{2}}{3^{2}−(\sqrt{3})^{2}} \\ & =\frac{9+6\sqrt{3}+3}{9−3} \\ & =\frac{12+6\sqrt{3}}{6} \\ & =2+\sqrt{3}\end{aligned}



$$

Therefore, we conclude that

$$



\tan (75^\circ) = 2+\sqrt 3.



$$

### Example: Finding an Exact Value Using the Sum and Difference Formulas for Tangent

#### Question

Find the exact value of $\tan \left(\dfrac{\pi}{12} \right).$

**

#### Explanation

Recall the difference formula for tangent:

$$



\tan(x-y) = \dfrac{\tan{x}-\tan{y}}{1+\tan{x}\tan{y}}



$$

Applying the difference formula for tangent with $x = \dfrac{\pi}{3}$ and $y = \dfrac{\pi}{4},$ we obtain

$$



\begin{aligned}tan⁡(\frac{𝜋}{12}) & =tan⁡(\frac{𝜋}{3}−\frac{𝜋}{4}) \\ & =\frac{tan⁡(\frac{𝜋}{3})−tan⁡(\frac{𝜋}{4})}{3} \\ & =\frac{\sqrt{3}−1}{1+\sqrt{3}⋅1} \\ & =\frac{\sqrt{3}−1}{\sqrt{3}+1}.\end{aligned}



$$

Finally, we rationalize the denominator:

$$



\begin{aligned}tan⁡(\frac{𝜋}{12}) & =\frac{\sqrt{3}−1}{\sqrt{3}+1} \\ & =\frac{\sqrt{3}−1}{\sqrt{3}+1}⋅\frac{\sqrt{3}−1}{\sqrt{3}−1} \\ & =\frac{(\sqrt{3})^{2}−2\sqrt{3}+(−1)^{2}}{(\sqrt{3})^{2}−1^{2}} \\ & =\frac{3−2\sqrt{3}+1}{3−1} \\ & =\frac{4−2\sqrt{3}}{2} \\ & =2−\sqrt{3}\end{aligned}



$$

### Example: Simplifying an Expression Using the Sum and Difference Formulas: Degrees

#### Question

If $\tan x = -\dfrac {4\sqrt 3} 3$, then find the value of $\tan (x -30^\circ).$

#### Explanation

First, we recall the difference formula for tangent:

$$



\tan(u-v) = \dfrac{\tan{u}-\tan{v}}{1+\tan{u}\tan{v}}



$$

Applying the sum formula for tangent with $u=x$ and $v=30^{\circ},$ we obtain

$$



\begin{aligned} \tan(x -30^\circ) &= \dfrac{\tan x - \tan 30^\circ}{1 + \tan x \tan 30^\circ} \\[5pt] &= \dfrac{\left(-\dfrac{4 \sqrt 3}3 -\dfrac{1} {\sqrt 3}\right)}{\left(1+\left(-\dfrac{4 \sqrt 3}3\right) \cdot \left(\dfrac{1}{\sqrt{3}}\right)\right)} \\[5pt] &= \dfrac{\left(-\dfrac {4\sqrt 3} 3 - \dfrac{1}{\sqrt 3}\cdot \dfrac{\sqrt 3} { \sqrt 3}\right)} {\left(1-\dfrac 43\right)} \\[5pt] &= \dfrac{\left(-\dfrac {4\sqrt 3} 3 - \dfrac{\sqrt 3} { 3}\right)} {\left(-\dfrac 13\right)} \\[5pt] & = \dfrac {\left(- \dfrac{5\sqrt 3}{3}\right)} {\left( -\dfrac 1 3 \right)}\\[3pt] & = 5\sqrt{3}. \end{aligned}



$$

### Example: Simplifying an Expression Using the Sum and Difference Formulas: Radians

#### Question

Write $\tan\left(x-\dfrac{\pi}{4}\right)$ as an expression containing $\tan{x}.$

#### Explanation

First, we recall the difference formula for tangent:

$$



\tan(u-v) = \dfrac{\tan{u}-\tan{v}}{1+\tan{u}\tan{v}}



$$

Applying the difference formula for tangent with $u=x$ and $v=\dfrac{\pi}{4},$ we obtain

$$



\begin{aligned}tan⁡(𝑥−\frac{𝜋}{4}) & =\frac{tan⁡𝑥−tan⁡(\frac{𝜋}{4})}{4} \\ & =\frac{tan⁡𝑥−1}{1+tan⁡𝑥⋅1} \\ & =\frac{tan⁡𝑥−1}{tan⁡𝑥+1}.\end{aligned}



$$

### Deriving the Sum and Difference Formulas for Tangent

We've practiced using the sum and difference formulas for tangent. But where do they come from?

To derive the sum formula for tangent, we start off by recalling the sum and difference formulas for sine and cosine:

$$



\begin{aligned}sin⁡(𝑥+𝑦) & =sin⁡𝑥cos⁡𝑦+cos⁡𝑥sin⁡𝑦 \\ cos⁡(𝑥+𝑦) & =cos⁡𝑥cos⁡𝑦−sin⁡𝑥sin⁡𝑦\end{aligned}



$$

Now, using the identity $\tan\theta = \dfrac{\sin\theta}{\cos\theta},$ we can divide $\sin(x+ y)$ by $\cos(x+ y)$ to get $\tan(x+ y).$ Dividing, we have

$$



\dfrac{\sin(x+ y)}{\cos(x+ y)} = \dfrac{\sin x\cos y + \cos x\sin y}{\cos x\cos y - \sin x\sin y},



$$

and simplifying, we reach

$$



\tan(x+y) = \dfrac{\sin x\cos y + \cos x\sin y}{\cos x\cos y - \sin x\sin y}.



$$

To write the right-hand side in terms of tangent only, we divide the numerator and denominator by $\cos x\cos y.$ This gives

$$



\begin{aligned}tan⁡(𝑥+𝑦) & =\frac{sin⁡𝑥cos⁡𝑦+cos⁡𝑥sin⁡𝑦}{cos⁡𝑥cos⁡𝑦−sin⁡𝑥sin⁡𝑦} \\ & =\frac{(\frac{sin⁡𝑥cos⁡𝑦}{cos⁡𝑥cos⁡𝑦}+\frac{cos⁡𝑥sin⁡𝑦}{cos⁡𝑥cos⁡𝑦})}{cos⁡𝑥cos⁡𝑦} \\ & =\frac{(\frac{sin⁡𝑥cos⁡𝑦}{cos⁡𝑥cos⁡𝑦}+\frac{cos⁡𝑥sin⁡𝑦}{cos⁡𝑥cos⁡𝑦})}{cos⁡𝑥cos⁡𝑦} \\ & =\frac{(\frac{sin⁡𝑥}{cos⁡𝑥}+\frac{sin⁡𝑦}{cos⁡𝑦})}{cos⁡𝑥} \\ & =\frac{tan⁡𝑥+tan⁡𝑦}{1−tan⁡𝑥tan⁡𝑦}.\end{aligned}



$$

We can derive the difference formula for tangent in a similar way.
