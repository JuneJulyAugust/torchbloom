# The Double-Angle Formula for Sine

Source: https://www.mathacademy.com/topics/271?courseId=43
Topic ID: 271

## Prerequisites

- [The Sum and Difference Formulas for Sine](./270-the-sum-and-difference-formulas-for-sine.md)

## Lesson

### Introduction

Recall the sum formula for sine:

$$


\sin (x+y) = \sin x \cos y + \cos x \sin y


$$

Substituting $y= {\color{blue}x}$ into the above gives

$$


\begin{aligned}sin⁡(𝑥+𝑥) & =sin⁡𝑥cos⁡𝑥+cos⁡𝑥sin⁡𝑥 \\ sin⁡2𝑥 & =sin⁡𝑥cos⁡𝑥+sin⁡𝑥cos⁡𝑥 \\ sin⁡2𝑥 & =2sin⁡𝑥cos⁡𝑥.\end{aligned}


$$

The last equation above is called the **double-angle formula for sine**:

$$


\sin 2x = 2 \sin x \cos x


$$

As we will see, this formula has many applications. For instance, it allows us to simplify some trigonometric expressions and find the exact value of sine for some non-special angles.

It's important to realize that this is an identity, *not* an equation, which means that it is true for *all* values of $x.$

### Example: Using the Double-Angle Formula to Simplify Products

#### Question

Write $2\sin{15^\circ} \cos{15^\circ}$ as a single trigonometric ratio.

#### Explanation

First, let's recall the double-angle formula for sine:

$$


2\sin{x}\cos{x} = \sin 2x


$$

Substituting $x=15^\circ$ into the above, we get

$$


\begin{aligned}2sin⁡15^{∘}cos⁡15^{∘} & =sin⁡(2⋅15^{∘})=sin⁡30^{∘}.\end{aligned}


$$

### Example: Using the Double-Angle Formula to Simplify Ratios

#### Question

Simplify the expression $\dfrac{\sin 25^\circ}{\sin 50^\circ}.$

#### Explanation

First, let's recall the double-angle formula for sine:

$$


\sin{2x} = 2\sin{x}\cos{x}


$$

Substituting $x=25^\circ$ into the above, we get

$$


\sin\left(2\cdot 25^\circ\right) = 2\sin 25^\circ \cos 25^\circ


$$

which simplifies to

$$


\sin 50^\circ = 2\sin 25^\circ \cos 25^\circ.


$$

Therefore, we can simplify the given expression by rewriting the ${\color{blue} \sin 50^\circ}$ in the denominator as follows:

$$


\begin{aligned}\frac{sin⁡25^{∘}}{sin⁡50^{∘}} & =\frac{sin⁡25^{∘}}{2sin⁡25^{∘}cos⁡25^{∘}} \\ & =\frac{sin⁡25^{∘}}{2sin⁡25^{∘}cos⁡25^{∘}} \\ & =\frac{1}{2cos⁡25^{∘}} \\ & =\frac{1}{2}sec⁡25^{∘}\end{aligned}


$$

### Example: Finding Exact Value of a Trigonometric Expression Using the Double-Angle Formula

#### Question

Without using a calculator, find the exact value of $3\sin{\left(\dfrac{\pi}{8}\right)}\cos{\left(\dfrac{\pi}{8}\right)}.$

#### Explanation

First, let's recall the double-angle formula for sine:

$$


2\sin{x}\cos{x} = \sin 2x


$$

Substituting $x=\dfrac {\pi}{8}$ into the above, we get

$$


\begin{aligned}2sin⁡(\frac{𝜋}{8})cos⁡(\frac{𝜋}{8}) & =sin⁡(2⋅\frac{𝜋}{8}) \\ & =sin⁡(\frac{𝜋}{4}) \\ & =\frac{\sqrt{√2}}{2}.\end{aligned}


$$

So, we have

$$


2\sin \left(\dfrac {\pi} {8} \right) \cos \left(\dfrac {\pi} {8} \right) = \dfrac{\sqrt{2}}{2}.


$$

Multiplying both sides of the above by $\dfrac 1 2$ gives

$$


\begin{aligned}\frac{1}{2}⋅2sin⁡(\frac{𝜋}{8})cos⁡(\frac{𝜋}{8}) & =\frac{1}{2}⋅\frac{\sqrt{√2}}{2} \\ sin⁡(\frac{𝜋}{8})cos⁡(\frac{𝜋}{8}) & =\frac{\sqrt{√2}}{4}.\end{aligned}


$$

Therefore, we conclude that

$$


3 \, {\color{black}\sin{\left(\dfrac{\pi}{8}\right)}\cos{\left(\dfrac{\pi}{8}\right)} } = 3 \left( \color{black} \dfrac{\sqrt{2}}{4} \right) = \dfrac{3\sqrt{2}}{4}.


$$

### Example: Using the Double-Angle Formula Multiple Times

#### Question

Without using a calculator, find the exact value of $\sin{\left(\dfrac{\pi}{24}\right)}\cos{\left(\dfrac{\pi}{24}\right)}\cos{\left(\dfrac{\pi}{12}\right)}.$

#### Explanation

First, let's recall the double-angle formula for sine:

$$


2\sin{x}\cos{x} = \sin{2x}


$$

Substituting $x=\dfrac{\pi}{24}$ into the above, we get

$$


2\sin\left(\dfrac{\pi}{24}\right)\cos\left(\dfrac{\pi}{24}\right) = \sin\left(2\cdot \dfrac{\pi}{24}\right)


$$

which simplifies as

$$


2\sin\left(\dfrac{\pi}{24}\right)\cos\left(\dfrac{\pi}{24}\right) = \sin\left(\dfrac{\pi}{12}\right) .


$$

Now, we can rewrite the given expression using the above, as follows:

$$


\begin{aligned}sin⁡(\frac{𝜋}{24})cos⁡(\frac{𝜋}{24})cos⁡(\frac{𝜋}{12}) & =\frac{1}{2}[2sin⁡(\frac{𝜋}{24})cos⁡(\frac{𝜋}{24})]cos⁡(\frac{𝜋}{12}) \\ & =\frac{1}{2}sin⁡(\frac{𝜋}{12})cos⁡(\frac{𝜋}{12})\end{aligned}


$$

Finally, using the double-angle formula once more with $x=\dfrac{\pi}{12},$ we can further simplify the above expression:

$$


\begin{aligned}\frac{1}{2}sin⁡(\frac{𝜋}{12})cos⁡(\frac{𝜋}{12}) & =\frac{1}{2}⋅\frac{1}{2}[2sin⁡(\frac{𝜋}{12})cos⁡(\frac{𝜋}{12})] \\ & =\frac{1}{4}[sin⁡(2⋅\frac{𝜋}{12})] \\ & =\frac{1}{4}sin⁡(\frac{𝜋}{6}) \\ & =\frac{1}{4}⋅\frac{1}{2} \\ & =\frac{1}{8}\end{aligned}


$$

Therefore,

$$


\sin{\left(\dfrac{\pi}{24}\right)}\cos{\left(\dfrac{\pi}{24}\right)}\cos{\left(\dfrac{\pi}{12}\right)} = \dfrac{1}{8}.


$$
