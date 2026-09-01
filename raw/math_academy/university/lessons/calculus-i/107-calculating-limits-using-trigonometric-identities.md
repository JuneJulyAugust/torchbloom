# Calculating Limits Using Trigonometric Identities

Source: https://www.mathacademy.com/topics/107?courseId=105
Topic ID: 107

## Prerequisites

- [The Double-Angle Formula for Sine](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/271-the-double-angle-formula-for-sine.md)
- [The Double-Angle Formula for Cosine](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/831-the-double-angle-formula-for-cosine.md)
- [Simplifying Trigonometric Expressions Using the Cotangent-Cosecant Identity](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/1455-simplifying-trigonometric-expressions-using-the-cotangent-cosecant-identity.md)
- [Calculating Limits of Rational Functions by Factoring](./1813-calculating-limits-of-rational-functions-by-factoring.md)
- [Limits of Reciprocal Trigonometric Functions](./1958-limits-of-reciprocal-trigonometric-functions.md)
- [Alternate Forms of the Secant-Tangent Identity](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/3857-alternate-forms-of-the-secant-tangent-identity.md)

## Lesson

### Introduction

Suppose that we want to calculate the following limit:

$$


\lim\limits_{x\to \pi/2}\dfrac{\sin{2x}}{2\cos{x}}


$$

If we attempt to evaluate this limit by directly substituting $x=\dfrac{\pi}{2},$ we get an indeterminate form:

$$


\begin{aligned}\underset{𝑥→𝜋/2}{lim}\frac{sin⁡2𝑥}{2cos⁡𝑥} & =\frac{sin⁡(2⋅\frac{𝜋}{2})}{2} \\ & =\frac{sin⁡(𝜋)}{2cos⁡(\frac{𝜋}{2})} \\ & =\frac{0}{0}\end{aligned}


$$

However, if we simplify the fraction before attempting to evaluate the limit, we obtain a more clear result.

To simplify the fraction in this particular case, the double angle formula for sine will be useful:

$$


\sin{2x}=2\sin{x}\cos{x}


$$

Using the double angle formula above, we have

$$


\begin{aligned}\underset{𝑥→𝜋/2}{lim}\frac{sin⁡2𝑥}{2cos⁡𝑥} & =\underset{𝑥→𝜋/2}{lim}\frac{2sin⁡𝑥cos⁡𝑥}{2cos⁡𝑥} \\ & =\underset{𝑥→𝜋/2}{lim}\frac{2sin⁡𝑥cos⁡𝑥}{2cos⁡𝑥} \\ & =\underset{𝑥→𝜋/2}{lim}sin⁡𝑥 \\ & =sin⁡(\frac{𝜋}{2}) \\ & =1.\end{aligned}


$$

In other cases, we may need to use a different trigonometric identity.

### Example: Calculating a Limit Using a Double Angle Formula

#### Question

$\lim\limits_{x\to \pi/4}\dfrac{\sin^2{x}-\cos^2{x}}{2\sin{x}\cos{2x}}=$

#### Explanation

If we attempt to evaluate this limit directly, we get an indeterminate form:

$$


\begin{aligned}\underset{𝑥→𝜋/4}{lim}\frac{sin^{2}⁡𝑥−cos^{2}⁡𝑥}{2sin⁡𝑥cos⁡2𝑥} & =\frac{sin^{2}⁡(\frac{𝜋}{4})−cos^{2}⁡(\frac{𝜋}{4})}{4} \\ & =\frac{1−1}{\sqrt{2}cos⁡(\frac{𝜋}{2})} \\ & =\frac{0}{0}\end{aligned}


$$

So we need to simplify the expression. The double angle formula for cosine will be useful in this case:

$$


\cos{2x}=\cos^2{x}-\sin^2{x}


$$

Using the double angle formula above, we have

$$


\begin{aligned}\underset{𝑥→𝜋/4}{lim}\frac{sin^{2}⁡𝑥−cos^{2}⁡𝑥}{2sin⁡𝑥cos⁡2𝑥} & =\underset{𝑥→𝜋/4}{lim}\frac{sin^{2}⁡𝑥−cos^{2}⁡𝑥}{2sin⁡𝑥(cos^{2}⁡𝑥−sin^{2}⁡𝑥)} \\ & =\underset{𝑥→𝜋/4}{lim}\frac{−(cos^{2}⁡𝑥−sin^{2}⁡𝑥)}{2sin⁡𝑥(cos^{2}⁡𝑥−sin^{2}⁡𝑥)} \\ & =\underset{𝑥→𝜋/4}{lim}(−\frac{1}{2sin⁡𝑥}) \\ & =−\frac{1}{\sqrt{2}} \\ & =−\frac{\sqrt{2}}{2}.\end{aligned}


$$

### Example: Calculating a Limit Using a Variation of a Double Angle Formula

#### Question

Evaluate $\lim\limits_{x\to 0}\dfrac{1-\cos x}{3\sin^2\left(\dfrac{x}{2}\right)}.$

#### Explanation

If we attempt to evaluate this limit directly, we get an indeterminate form:

$$


\begin{aligned}\underset{𝑥→0}{lim}\frac{1−cos⁡𝑥}{3sin^{2}⁡(\frac{𝑥}{2})} & =\frac{1−cos⁡(0)}{3sin^{2}⁡(0)} \\ & =\frac{1−1}{3⋅0} \\ & =\frac{0}{0}\end{aligned}


$$

So we need to simplify the expression. Again we will use the double angle formula for cosine, but in a different form:

$$


\cos{x}=1-2\sin^2\left(\dfrac{x}{2}\right)


$$

Substituting the above formula, we get

$$


\begin{aligned}\underset{𝑥→0}{lim}\frac{1−cos⁡𝑥}{3sin^{2}⁡(\frac{𝑥}{2})} & =\underset{𝑥→0}{lim}\frac{1−(1−2sin^{2}⁡(\frac{𝑥}{2}))}{2} \\ & =\underset{𝑥→0}{lim}\frac{2sin^{2}⁡(\frac{𝑥}{2})}{2} \\ & =\underset{𝑥→0}{lim}\frac{2}{3} \\ & =\frac{2}{3}.\end{aligned}


$$

### Example: Calculating a Limit Using the Pythagorean Identity

#### Question

$\lim\limits_{x\to (-\pi/2)}\dfrac{\cos^2x}{1+\sin x}=$

#### Explanation

If we attempt to evaluate this limit directly, we get an indeterminate form:

$$


\begin{aligned}\underset{𝑥→(−𝜋/2)}{lim}\frac{cos^{2}⁡𝑥}{1+sin⁡𝑥} & =\frac{cos^{2}⁡(−\frac{𝜋}{2})}{2} \\ & =\frac{0}{1−1} \\ & =\frac{0}{0}\end{aligned}


$$

So we need to simplify the expression. In particular, we will use the Pythagorean identity:

$$


\cos^2{x}=1-\sin^2{x}


$$

Substituting the above formula, we get

$$


\begin{aligned}\underset{𝑥→(−𝜋/2)}{lim}\frac{cos^{2}⁡𝑥}{1+sin⁡𝑥} & =\underset{𝑥→(−𝜋/2)}{lim}\frac{cos^{2}⁡𝑥}{1+sin⁡𝑥} \\ & =\underset{𝑥→(−𝜋/2)}{lim}\frac{1−sin^{2}⁡𝑥}{1+sin⁡𝑥} \\ & =\underset{𝑥→(−𝜋/2)}{lim}\frac{(1+sin⁡𝑥)(1−sin⁡𝑥)}{1+sin⁡𝑥} \\ & =\underset{𝑥→(−𝜋/2)}{lim}(1−sin⁡𝑥) \\ & =1−sin⁡(−\frac{𝜋}{2}) \\ & =1−(−1) \\ & =2.\end{aligned}


$$

### Example: Calculating a Limit Using Another Form of the Pythagorean Identity

#### Question

Evaluate $\lim\limits_{x\to 0}\dfrac{\sec x-1}{7\tan^2x}.$

#### Explanation

If we attempt to evaluate this limit directly, we get an indeterminate form:

$$


\begin{aligned}\underset{𝑥→0}{lim}\frac{sec⁡𝑥−1}{7tan^{2}⁡𝑥} & =\frac{sec⁡(0)−1}{7tan^{2}⁡(0)} \\ & =\frac{1−1}{7⋅0} \\ & =\frac{0}{0}\end{aligned}


$$

So we need to simplify the expression. In particular, we will use the Pythagorean identity for tangent and secant:

$$


\tan^2{x}=\sec^2{x}-1


$$

Substituting the above formula, we get

$$


\begin{aligned}\underset{𝑥→0}{lim}\frac{sec⁡𝑥−1}{7tan^{2}⁡𝑥} & =\underset{𝑥→0}{lim}\frac{sec⁡𝑥−1}{7(sec^{2}⁡𝑥−1)} \\ & =\underset{𝑥→0}{lim}\frac{sec⁡𝑥−1}{7(sec⁡𝑥−1)(sec⁡𝑥+1)} \\ & =\underset{𝑥→0}{lim}\frac{1}{7(sec⁡𝑥+1)} \\ & =\frac{1}{7(sec⁡(0)+1)} \\ & =\frac{1}{7(1+1)} \\ & =\frac{1}{14}.\end{aligned}


$$
