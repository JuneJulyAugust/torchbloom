# Integration Using the Double-Angle Formulas

Source: https://www.mathacademy.com/topics/1038?courseId=21
Topic ID: 1038

## Prerequisites

- [The Double-Angle Formula for Sine](../../../high-school/traditional/lessons/precalculus/271-the-double-angle-formula-for-sine.md)
- [The Double-Angle Formula for Cosine](../../../high-school/traditional/lessons/precalculus/831-the-double-angle-formula-for-cosine.md)
- [Integration Using the Pythagorean Identities](../ap-calculus-ab/1037-integration-using-the-pythagorean-identities.md)

## Lesson

### Introduction

How can we calculate $\displaystyle{\int} \sin x \cos x \, \textrm{d}x?$

Notice that we have the product of sine and cosine with the same argument $(x).$ In such cases, we can use the double-angle formula for sine to solve the integral.

Let's recall the double-angle formula for sine, which is

$$


\sin {2x}=2\sin x \cos x.


$$

We can rearrange the above formula as

$$


\sin x \cos x = \dfrac{1}{2} \sin {2x}.


$$

Plugging this into our integral, we get

$$


\begin{aligned} \int \sin x \cos x \, \textrm{d}x&=\int \dfrac{1}{2}\sin {2x} \, \textrm{d}x\\\[5pt] &=\dfrac{1}{2} \int \sin {2x} \, \textrm{d}x\\\[5pt] &=\dfrac{1}{2} \left( -\dfrac{1}{2} \cos {2x}\right )+C \\\[5pt] &=-\dfrac{1}{4} \cos {2x}+C. \end{aligned}


$$

In general, we can use the double-angle formula for sine to solve any integral that's of the form

$$


\int \sin\left(ax+b\right)\cos(ax+b)\,\textrm{d}x.


$$

Let's take a look at another example.

### Example: Integrating Expressions Using the Double-Angle Formula for Sine

#### Question

Calculate $\displaystyle{{\int}} \sin \left(\dfrac{x}{2} \right)\cos \left(\dfrac{x}{2}\right)\, \textrm{d}x.$

#### Explanation

In this case, we use the double-angle formula for sine:

$$


\sin {2\theta} =2\sin \theta \cos \theta\quad\Rightarrow\quad \dfrac{1}{2}\sin(2\theta) = \sin{\theta}\cos{\theta}.


$$

Letting $\theta= \dfrac{x}{2},$ we get

$$


\begin{aligned} \dfrac{1}{2} \sin \left(2\cdot \dfrac{x}{2} \right) &= \sin \left(\dfrac{x}{2} \right)\cos\left( \dfrac{x}{2}\right)\\\[5pt] \dfrac{1}{2}\sin x &= \sin \left( \dfrac{x}{2}\right) \cos \left(\dfrac{x}{2}\right). \end{aligned}


$$

Therefore,

$$


\begin{aligned} \int \sin \left(\dfrac{x}{2}\right) \cos \left(\dfrac{x}{2}\right) \, \textrm{d}x&=\int \dfrac{1}{2}\sin {x} \, \textrm{d}x\\\[5pt] &=\dfrac{1}{2} \int \sin {x} \, \textrm{d}x\\\[5pt] &=\dfrac{1}{2} \left( - \cos {x}\right )+C \\\[5pt] &=-\dfrac{1}{2} \cos {x}+C. \end{aligned}


$$

### Using the Double-Angle Formulas for Cosine

Let's recall the three double-angle formulas for cosine:

$$


\begin{aligned}cos⁡(2𝑥) & =cos^{2}⁡𝑥−sin^{2}⁡𝑥 \\ & =2cos^{2}⁡𝑥−1 \\ & =1−2sin^{2}⁡𝑥.\end{aligned}


$$

We can use the double-angle formulas for cosine to integrate $\sin^2{x}$ and $\cos^2{x}.$ Let's take a look at some examples.

### Example: Integrating Expressions Using the Double-Angle Formula for Cosine

#### Question

Calculate $\displaystyle{\int} \left(\cos^2 3x - \sin^2 3x\right) \, \textrm{d}x.$

#### Explanation

We can use the double-angle formula for cosine:

$$


\cos^2\theta -\sin^2\theta=\cos 2\theta.


$$

Letting $\theta = 3x$ gives

$$


\cos^2 3x - \sin^2 3x = \cos 6x,


$$

and therefore,

$$


\begin{aligned} {\int} \left(\cos^2 3x - \sin^2 3x\right ) \, \textrm{d}x&=\int \cos 6x\, \textrm{d}x\\&=\dfrac{1}{6}\sin6x+ C.\\\end{aligned}


$$

### Example: Integrating Using the Squared Cosine Variant of the Cosine Double-Angle Formula

#### Question

Calculate $\displaystyle{\int} \cos^2 x \, \textrm{d}x.$

#### Explanation

Here, we use the double-angle formula for cosine that involves the $\cos^2{x}$ term, given by

$$


\cos{2x} =2\cos^2 x -1.


$$

Rearranging, we have

$$


\cos^2 x = \dfrac{1}{2} \left(\cos 2x +1 \right).


$$

Substituting this into our integral, we get

$$


\begin{aligned} \int \cos^2 x \, \textrm{d}x&=\int \dfrac{1}{2} \left(\cos 2x +1 \right) \, \textrm{d}x\\\[5pt] &=\dfrac{1}{2}\int ( \cos {2x} +1) \textrm{d}x\\\[5pt] &= \dfrac{1}{2}\left(\dfrac{1}{2}\sin {2x} +x\right) + C\\\[5pt] &= \dfrac{1}{4}\sin {2x} +\dfrac{1}{2}x + C. \end{aligned}


$$

### Example: Integrating Using the Squared Sine Variant of the Cosine Double-Angle Formula

#### Question

Calculate $\displaystyle{\int} \sin^2(3x) \, \textrm{d}x.$

#### Explanation

Let's recall the double-angle formula for cosine that involves the $\sin^2$ term:

$$


\cos {2\theta}=1-2\sin^2\theta.


$$

We can rearrange the above formula as

$$


\dfrac{1}{2}\left(1-\cos {2\theta} \right )=\sin^2\theta.


$$

Letting $\theta = 3x$, we have

$$


\dfrac{1}{2}\left(1-\cos {6x} \right )=\sin^2(3x).


$$

We can now integrate as follows:

$$


\begin{aligned}∫sin^{2}⁡(3𝑥)\,d𝑥 & =∫\frac{1}{2}(1−cos⁡6𝑥)\,d𝑥 \\ & =\frac{1}{2}∫(1−cos⁡6𝑥)\,d𝑥 \\ & =\frac{1}{2}(𝑥−\frac{1}{6}sin⁡6𝑥)+𝐶 \\ & =\frac{1}{2}𝑥−\frac{1}{12}sin⁡6𝑥+𝐶.\end{aligned}


$$
