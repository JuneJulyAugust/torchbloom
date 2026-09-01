# The Sum and Difference Formulas for Sine

Source: https://www.mathacademy.com/topics/270?courseId=43
Topic ID: 270

## Prerequisites

- [Evaluating Trigonometric Expressions](../algebra-ii/3766-evaluating-trigonometric-expressions.md)

## Lesson

### Introduction

The following two identities are known as the **sum and difference formulas for sine**:

$$



\begin{aligned}sin⁡(𝑥+𝑦) & =sin⁡𝑥cos⁡𝑦+cos⁡𝑥sin⁡𝑦 \\ sin⁡(𝑥−𝑦) & =sin⁡𝑥cos⁡𝑦−cos⁡𝑥sin⁡𝑦\end{aligned}



$$

We'll prove these results at the end of the lesson.

These identities can be used to calculate the sine of an angle which is the sum or difference of two special angles.

For example, we can use the sum rule to find the exact value of $\sin(75^\circ).$ We start by writing $75^\circ$ as a sum of special angles:

$$



75^\circ = {\color{blue}45^\circ} + {\color{red}30^\circ}



$$

We can now apply the sum formula for sine as follows:

$$



\begin{aligned}sin⁡75^{∘} & =sin⁡(45^{∘}+30^{∘}) \\ & =sin⁡45^{∘}cos⁡30^{∘}+cos⁡45^{∘}sin⁡30^{∘} \\ & =\frac{\sqrt{2}}{2}⋅\frac{\sqrt{3}}{2}+\frac{\sqrt{2}}{2}⋅\frac{1}{2} \\ & =\frac{\sqrt{6}+\sqrt{2}}{4}\end{aligned}



$$

Therefore, we conclude that

$$



\sin 75^\circ = \dfrac {\sqrt{6} + \sqrt{2}} 4.



$$

Let's see another example.

### Example: Finding Exact Values Using the Sum and Difference Formulas

#### Question

Find the exact value of $\sin\left(\dfrac{\pi}{12}\right)$ without using a calculator.

**

#### Explanation

Recall the difference formula for sine:

$$



\sin(x-y) = \sin x\cos y - \cos x\sin y



$$

Applying the difference formula for sine with $x = \dfrac{\pi}{3}$ and $y = \dfrac{\pi}{4},$ we obtain

$$



\begin{aligned}sin⁡(\frac{𝜋}{12}) & =sin⁡(\frac{𝜋}{3}−\frac{𝜋}{4}) \\ & =sin⁡(\frac{𝜋}{3})cos⁡(\frac{𝜋}{4})−cos⁡(\frac{𝜋}{3})sin⁡(\frac{𝜋}{4}) \\ & =\frac{\sqrt{3}}{2}⋅\frac{\sqrt{2}}{2}−\frac{1}{2}⋅\frac{\sqrt{2}}{2} \\ & =\frac{\sqrt{6}−\sqrt{2}}{4}.\end{aligned}



$$

### Example: Simplifying Expressions in Degrees Using the Sum and Difference Formulas

#### Question

Express $\sin\left(x - 30^{\circ} \right)$ in terms of $\sin x$ and $\cos x.$

#### Explanation

Recall the difference formula for sine:

$$



\sin(u-v) = \sin u\cos v - \cos u\sin v



$$

Applying the difference formula for sine with $u=x$ and $v=30^{\circ},$ we get

$$



\begin{aligned}sin⁡(𝑥−30^{∘}) & =sin⁡𝑥cos⁡30^{∘}−cos⁡𝑥sin⁡30^{∘} \\ & =sin⁡𝑥⋅(\frac{\sqrt{3}}{2})−cos⁡𝑥⋅(\frac{1}{2}) \\ & =\frac{\sqrt{3}sin⁡𝑥}{2}−\frac{cos⁡𝑥}{2} \\ & =\frac{\sqrt{3}sin⁡𝑥−cos⁡𝑥}{2}.\end{aligned}



$$

### Example: Simplifying Expressions in Radians Using the Sum and Difference Formulas

#### Question

Express $\sin\left(x + \dfrac{\pi}{6} \right)$ in terms of $\sin x$ and $\cos x.$

#### Explanation

Recall the sum formula for sine:

$$



\sin(u+v) = \sin{u}\cos{v} + \cos{u}\sin{v}



$$

Applying the sum formula for sine with $u = x$ and $v = \dfrac{\pi}{6},$ we get

$$



\begin{aligned}sin⁡(𝑥+\frac{𝜋}{6}) & =sin⁡𝑥cos⁡(\frac{𝜋}{6})+cos⁡𝑥sin⁡(\frac{𝜋}{6}) \\ & =sin⁡𝑥⋅(\frac{\sqrt{3}}{2})+cos⁡𝑥⋅(\frac{1}{2}) \\ & =\frac{\sqrt{3}sin⁡𝑥}{2}+\frac{cos⁡𝑥}{2} \\ & =\frac{\sqrt{3}sin⁡𝑥+cos⁡𝑥}{2}.\end{aligned}



$$

### Proving the Sum Formula

Let's now prove the sum formula for sine:

$$



\sin(A+B) = \sin A\cos B + \cos A\sin B



$$

To start with, we need to use the *difference* formula for *cosine*:

$$



\cos(A-B) = \cos A\cos B + \sin A\sin B



$$

If you haven't seen this formula yet, don't worry. You'll learn more about it, including how it's proved using the unit circle, in a separate lesson.

Now, if we replace $A$ with $\left(\dfrac{\pi}{2} - A\right)$ in the difference formula for cosine, we get

$$



\cos\left(\dfrac\pi2 - A-B\right) = \cos \left(\dfrac\pi2 - A\right)\cos B + \sin\left(\dfrac\pi2 - A\right)\sin B



$$

i.e.

$$



\cos\left(\dfrac\pi2 - (A+B)\right) = \cos \left(\dfrac\pi2 - A\right)\cos B + \sin\left(\dfrac\pi2 - A\right)\sin B.



$$

Next, using the cofunction identities

$$



\begin{aligned}cos⁡(\frac{𝜋}{2}−(𝐴+𝐵)) & =sin⁡(𝐴+𝐵) \\ cos⁡(\frac{𝜋}{2}−𝐴) & =sin⁡𝐴 \\ sin⁡(\frac{𝜋}{2}−𝐴) & =cos⁡𝐴\end{aligned}



$$

the identity above reduces to

$$



\sin(A+B) = \sin A\cos B + \cos A\sin B



$$

as required.

### Proving the Difference Formula

We have shown how to derive the sum formula

$$



\sin(A+B) = \sin A\cos B + \cos A\sin B.



$$

We can derive the difference formula for sine by simply replacing $B$ with $-B,$ and using the evenness/oddness identities for cosine and sine, respectively:

$$



\cos(-B) = \cos B, \qquad \sin(-B) = -\sin B



$$

Substituting these into our sum formula, we get

$$



\begin{aligned}sin⁡(𝐴+(−𝐵))=sin⁡𝐴cos⁡(−𝐵)+cos⁡𝐴sin⁡(−𝐵)\end{aligned}



$$

which simplifies as

$$



\sin(A-B) = \sin A\cos B - \cos A\sin B



$$

as required.
