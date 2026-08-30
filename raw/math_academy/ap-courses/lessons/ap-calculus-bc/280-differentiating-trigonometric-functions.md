# Differentiating Trigonometric Functions

Source: https://www.mathacademy.com/topics/280?courseId=21
Topic ID: 280

## Prerequisites

- [Finding Trigonometric Ratios of Special Angles Using the Unit Circle](../../../high-school/traditional/lessons/algebra-ii/268-finding-trigonometric-ratios-of-special-angles-using-the-unit-circle.md)
- [Calculating the Equation of a Tangent Line Using Differentiation](../ap-calculus-ab/986-calculating-the-equation-of-a-tangent-line-using-differentiation.md)

## Lesson

### Introduction

The derivatives of sine, cosine, and tangent are shown in the table below:

Now that we know the derivatives of the standard trigonometric functions, we can differentiate any combination of them by using the properties of differentiation.

For example, let's find the derivative of $y = \cos x + \sin x.$

Here, we can use the fact that the derivative of the sum is equal to the sum of the derivatives, and get

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =\frac{d}{d𝑥}(cos⁡𝑥+sin⁡𝑥) \\ & =\frac{d}{d𝑥}(cos⁡𝑥)+\frac{d}{d𝑥}(sin⁡𝑥) \\ & =−sin⁡𝑥+cos⁡𝑥.\end{aligned}


$$

**Note:** We'll derive the derivatives shown in the table at the end of this lesson.

### Example: Finding the Derivative of an Expression With Sine or Cosine Trigonometric Functions

#### Question

Find the derivative of $y = 3\cos x + 4\sin x + 2x^3.$

#### Explanation

We know that $\dfrac{\text{d}}{\text{d}x} (\sin x) = \cos x,$ and that $\dfrac{\text{d}}{\text{d}x} (\cos x) = -\sin x.$ Applying these formulas, we have

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =\frac{d}{d𝑥}(3cos⁡𝑥+4sin⁡𝑥+2𝑥^{3}) \\ & =3\frac{d}{d𝑥}(cos⁡𝑥)+4\frac{d}{d𝑥}(sin⁡𝑥)+2\frac{d}{d𝑥}(𝑥^{3}) \\ & =−3sin⁡𝑥+4cos⁡𝑥+2(3)𝑥^{2} \\ & =−3sin⁡𝑥+4cos⁡𝑥+6𝑥^{2}.\end{aligned}


$$

### Example: Finding the Derivative of an Expression With the Tangent Trigonometric Function

#### Question

Find the slope of $y = 4\tan x + 5x$ at $x = 0.$

#### Explanation

The slope at $x=0$ is given by the value of the derivative $y'$ at $x=0.$

First, we compute the derivative, using the fact that $\dfrac{\text{d}}{\text{d}x} (\tan x) = \sec^2 x.$ We get

$$


\begin{aligned}𝑦^{′}(𝑥) & =\frac{d}{d𝑥}(4tan⁡𝑥+5𝑥) \\ & =4sec^{2}⁡𝑥+5.\end{aligned}


$$

Evaluating at $x=0,$ we get

$$


\begin{aligned}𝑦^{′}(0) & =4sec^{2}⁡0+5 \\ & =4⋅1+5 \\ & =9.\end{aligned}


$$

Therefore, the slope is $9.$

### Justifying the Formula for the Derivative of Sine

To understand why the derivative of sine is cosine, we need to use the definition of the derivative:

$$


\dfrac {\text{d}} {\text{d}x} (\sin x) = \lim_{h\rightarrow 0}\dfrac{\sin(x+h) - \sin x}{h}


$$

Now, the so-called **addition formula for sine** states that

$$


\sin(x+h) = \sin(x)\cos(h)+\cos (x) \sin(h).


$$

By using the addition formula for sine, we can rewrite our expression for the derivative as follows:

$$


\begin{aligned}\frac{d}{d𝑥}(sin⁡𝑥) & =\underset{ℎ→0}{lim}\frac{sin⁡(𝑥)cos⁡(ℎ)+sin⁡(ℎ)cos⁡(𝑥)−sin⁡(𝑥)}{ℎ} \\ & =\underset{ℎ→0}{lim}\frac{sin⁡(𝑥)(cos⁡(ℎ)−1)+cos⁡(𝑥)sin⁡(ℎ)}{ℎ} \\ & =\underset{ℎ→0}{lim}(sin⁡(𝑥)\frac{(cos⁡(ℎ)−1)}{ℎ}+cos⁡(𝑥)\frac{sin⁡(ℎ)}{ℎ}) \\ & =sin⁡(𝑥)\underset{0}{\underset{}{\underset{ℎ→0}{lim}\frac{(cos⁡(ℎ)−1)}{ℎ}}}+cos⁡(𝑥)\underset{1}{\underset{}{\underset{ℎ→0}{lim}\frac{sin⁡(ℎ)}{ℎ}}} \\ & =cos⁡(𝑥)\end{aligned}


$$

In the last step, we used two important results for trigonometric limits:

$$


\lim_{h\rightarrow 0} \dfrac{1 - \cos(h)}{h}=0 \qquad \text{and} \qquad \lim_{h\rightarrow 0} \dfrac{\sin(h)}{h}=1.


$$

Deriving these results requires separate discussions, which we'll leave to future topics.

### Justifying the Formula for the Derivative of Cosine

We can follow the same method for the cosine and use the definition of the derivative to show that $(\cos x)'=-\sin x.$ First, we start with the definition of the derivative:

$$


\dfrac {\text{d}} {\text{d}x} (\cos x) = \lim_{h\rightarrow 0}\dfrac{\cos(x+h) - \cos x}{h}


$$

Now, the so-called **addition formula for cosine** states that

$$


\cos(x+h) = \cos(x)\cos(h)- \sin(x)\sin(h).


$$

Using the addition formula for cosine, we can rewrite our expression for the derivative as follows:

$$


\begin{aligned}\frac{d}{d𝑥}(cos⁡𝑥) & =\underset{ℎ→0}{lim}\frac{cos⁡(𝑥)cos⁡(ℎ)−sin⁡(𝑥)sin⁡(ℎ)−cos⁡(𝑥)}{ℎ} \\ & =\underset{ℎ→0}{lim}\frac{cos⁡(𝑥)(cos⁡(ℎ)−1)−sin⁡(𝑥)sin⁡(ℎ)}{ℎ} \\ & =cos⁡(𝑥)\underset{0}{\underset{}{\underset{ℎ→0}{lim}\frac{cos⁡(ℎ)−1}{ℎ}}}−sin⁡(𝑥)\underset{1}{\underset{}{\underset{ℎ→0}{lim}\frac{sin⁡(ℎ)}{ℎ}}} \\ & =−sin⁡(𝑥)\end{aligned}


$$

Once again, in the last step, we used the special limits for sine and cosine.

### Justifying the Formula for the Derivative of Tangent

We can also prove that $(\tan x)'= \sec^2 x$ using limits, though it's a bit cumbersome.

A faster way is to use a rule of differentiation known as the **quotient rule**.

You'll learn about the quotient rule very soon!
