# The Gamma Function

Source: https://www.mathacademy.com/topics/3289?courseId=73
Topic ID: 3289

## Prerequisites

- [Introduction to Integration by Parts](../../../ap-courses/lessons/ap-calculus-bc/317-introduction-to-integration-by-parts.md)
- [Complex Numbers](../../../high-school/traditional/lessons/algebra-ii/735-complex-numbers.md)
- [Improper Integrals](../../../ap-courses/lessons/ap-calculus-bc/758-improper-integrals.md)
- [Factorials](../../../high-school/traditional/lessons/geometry/774-factorials.md)
- [Recursive Sequences](../../../high-school/traditional/lessons/algebra-i/1226-recursive-sequences.md)

## Lesson

### Introduction

The **gamma function** $\Gamma(z)$ extends the factorial function to positive real numbers and parts of the complex plane.

In particular, for any natural number $n \geq 1,$ we have

$$


\Gamma(n) = (n-1)!


$$

If the complex number $z$ satisfies $\text{Re}(z) > 0,$ then the gamma function can be defined as the improper integral

$$


\Gamma(z) = \int_0^\infty t^{z-1} e^{-t} \, \textrm dt.


$$

In this lesson, we will only consider cases where $z$ is a positive real number.

### Example: Defining the Gamma Function

#### Question

Which of the following integrals are equivalent to $\Gamma(z)$ for $\text{Re}(z) > 0?$

1. $\displaystyle \int_0^1 t^{z-1} e^{-t} \, \textrm dt$

2. $\displaystyle \int_0^\infty \dfrac{t^{z}}{te^t} \, \textrm dt$

3. $\displaystyle \int_0^\infty \dfrac{e^t}{t^{1-z}} \, \textrm dt$

#### Explanation

First, let's recall the definition of the gamma function:

$$


\Gamma(z) = \int_0^\infty t^{z-1} e^{-t} \, \textrm dt, \qquad \text{Re}(z) > 0.


$$

With this definition in mind, let's consider each of the given integrals.

- Integral I does ** match the definition. The upper bound of integration does not match that given in the definition.

- Integral II matches the definition:

- Integral III does ** match the definition. The integrand $\dfrac{e^t}{t^{1-z}}$ is not equivalent to that shown in the definition.

Therefore, the correct answer is "II only."

### Example: Evaluating the Gamma Function for a Positive Integer

#### Question

Evaluate $\Gamma(7).$

#### Explanation

For any natural number $n \geq 1,$ we have

$$


\Gamma(n) = (n-1)!.


$$

Therefore,

$$


\Gamma(7) = 6! = 720.


$$

### The Recursive Formula and the Value of the Gamma Function at One-Half

To evaluate the gamma function at positive integer multiples of one-half, we use the following recursive formula:

$$


\Gamma(z+1) = z \Gamma(z), \qquad \Gamma \left( \dfrac{1}{2} \right) = \sqrt{\pi}


$$

We'll prove these results at the end of the lesson.

### Example: Evaluating the Gamma Function at a Multiple of One-Half

#### Question

Calculate $\Gamma \left(\dfrac{5}{2} \right).$

#### Explanation

To evaluate the gamma function at multiples of one-half, we use the following recursive formula:

$$


\Gamma(z+1) = z \Gamma(z), \qquad \Gamma \left( \dfrac{1}{2} \right) = \sqrt{\pi}


$$

So, we have the following:

$$


\begin{aligned}Γ(\frac{5}{2}) & =\frac{3}{2}Γ(\frac{3}{2}) \\ & =\frac{3}{2}⋅\frac{1}{2}Γ(\frac{1}{2}) \\ & =\frac{3}{2}⋅\frac{1}{2}\sqrt{𝜋} \\ & =\frac{3}{4}\sqrt{𝜋}\end{aligned}


$$

### Proof of the Recursive Formula

Here, we'll prove the recursive formula for the gamma function:

$$


\Gamma(z+1) = z \Gamma(z)


$$

The formula comes from applying integration by parts to the integral in the definition of the gamma function. By definition,

$$


\Gamma(z) = \int_0^\infty t^{z-1} e^{-t} \, \textrm dt, \qquad\text{Re}(z) > 0.


$$

Therefore,

$$


\begin{aligned}Γ(𝑧+1) & =∫_{∞0}𝑡^{𝑧}𝑒^{−𝑡}\,d𝑡 \\ & =−𝑡^{𝑧}𝑒^{−𝑡}_{∞0}−∫_{∞0}−𝑧𝑡^{𝑧−1}𝑒^{−𝑡}\,d𝑡 \\ & =\underset{𝑡→∞}{lim}(−\frac{𝑡^{𝑧}}{𝑒^{𝑡}})−(−\frac{𝑡^{𝑧}}{𝑒^{𝑡}})_{𝑡=0}+∫_{∞0}𝑧𝑡^{𝑧−1}𝑒^{−𝑡}\,d𝑡 \\ & =0−0+𝑧\underset{Γ(𝑧)}{\underset{}{∫_{∞0}𝑡^{𝑧−1}𝑒^{−𝑡}\,d𝑡}} \\ & =𝑧Γ(𝑧)\end{aligned}


$$

### Proving the Relationship Between the Gamma Function and the Factorial

Previously, we used the following relationship between the gamma function and the factorial:

$$


\Gamma(n) = (n-1)!


$$

This relationship holds for any natural number $n \geq 1.$ Now, let's prove it.

First, we start with the following identity, which we proved earlier:

$$


\Gamma(z+1) = z \Gamma(z)


$$

For any natural number $n \geq 1,$ the above identity states the following:

$$


\Gamma(n+1) = n \Gamma(n)


$$

Now, let's repeatedly expand out the right-hand side, noticing that most of the terms can be grouped into a factorial:

$$


\begin{aligned}Γ(𝑛+1) & =𝑛Γ(𝑛) \\ & =𝑛⋅\overset{(𝑛−1)⋅Γ(𝑛−1)}{Γ(𝑛)} \\ & =𝑛⋅(𝑛−1)⋅\overset{(𝑛−2)⋅Γ(𝑛−2)}{Γ(𝑛−1)} \\ & =… \\ & =\underset{𝑛!}{\underset{}{𝑛⋅(𝑛−1)⋅(𝑛−2)⋅…⋅1}}⋅Γ(1)\end{aligned}


$$

So, we have

$$


\Gamma(n+1) = n! \cdot \Gamma(1).


$$

To evaluate $\Gamma(1),$ we can use the definition of the gamma function:

$$


\Gamma(1) = \int_0^\infty e^{-t} \, \textrm dt = 1


$$

Therefore,

$$


\Gamma(n+1) = n!


$$

### Evaluating the Gamma Function at One-Half

Previously, we used the fact that $\Gamma \left(\dfrac{1}{2} \right) = \sqrt{\pi}.$ To prove this, we can directly compute the value of $\Gamma \left(\dfrac{1}{2} \right)$ using the definition of the gamma function:

$$


\Gamma\left(\dfrac{1}{2}\right) = \int_0^\infty t^{-1/2} e^{-t} \, \text{d}t


$$

We simplify this integral using the substitution $t = u^2,$ which implies $\text{d}t = 2u \, \text{d}u.$ Also, note that $u \to 0^+$ as $t \to 0^+$ and $u \to \infty$ as $t \to \infty.$ So, we have

$$


t^{-1/2} e^{-t} \, \text{d}t = (u^2)^{-1/2} e^{-u^2} \cdot 2u \, \text{d}u = e^{-u^2} \cdot 2 \, \text{d}u.


$$

Thus, we get

$$


\Gamma\left(\dfrac{1}{2}\right) = \int_0^\infty t^{-1/2} e^{-t} \, \text{d}t = 2 \int_0^\infty e^{-u^2} \, \text{d}u.


$$

This is directly related to the well-known **Gaussian integral**:

$$


\int_{-\infty}^\infty e^{-u^2} \, \text{d}u = \sqrt{\pi}


$$

Since the integrand $e^{-u^2}$ is even (i.e., symmetric about the $y$-axis), we have

$$


\int_0^\infty e^{-u^2} \, \text{d}u = \dfrac{1}{2} \int_{-\infty}^\infty e^{-u^2} \, \text{d}u = \dfrac{1}{2} \sqrt{\pi}.


$$

Substituting this result back into our expression for the Gamma function, we obtain

$$


\Gamma\left(\dfrac{1}{2}\right) = 2 \cdot \dfrac{1}{2} \sqrt{\pi} = \sqrt{\pi}.


$$
