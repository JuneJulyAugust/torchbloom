# L'Hopital's Rule

Source: https://www.mathacademy.com/topics/463?courseId=21
Topic ID: 463

## Prerequisites

- [Second and Higher-Order Derivatives](../ap-calculus-ab/281-second-and-higher-order-derivatives.md)
- [Selecting Procedures for Calculating Derivatives](../ap-calculus-ab/1115-selecting-procedures-for-calculating-derivatives.md)
- [Limits of Logarithmic Functions](../ap-calculus-ab/1377-limits-of-logarithmic-functions.md)
- [Limits of Exponential Functions](../ap-calculus-ab/1717-limits-of-exponential-functions.md)
- [Limits of Reciprocal Functions](../ap-calculus-ab/1905-limits-of-reciprocal-functions.md)
- [Limits of Reciprocal Trigonometric Functions](../ap-calculus-ab/1958-limits-of-reciprocal-trigonometric-functions.md)
- [Limits of Radical Functions](../ap-calculus-ab/1986-limits-of-radical-functions.md)

## Lesson

### Introduction

Suppose that we want to find

$$


{\displaystyle \lim_{x\to 0} \frac {\sin x}{x} }.


$$

If we try to plug in $x=0,$ we get the indeterminate form $\dfrac{0}{0}.$ So what can we do?

Fortunately, we can find this limit using **L'Hopital's Rule**, which states that if $\displaystyle\lim_{x\rightarrow a}f(x) = 0$ and $\displaystyle\lim_{x\rightarrow a}g(x) = 0,$ then

$$


\ \lim_{x\to a} \dfrac {f(x)}{g(x)} = \lim_{x\to a} \frac {f'(x)}{g'(x)},


$$

provided that $f$ and $g$ are both differentiable at $x=a,$ and that $\displaystyle \lim_{x\to a} \dfrac {f'(x)}{g'(x)}$ exists.

So, by applying L'Hopital's rule to our limit, we get

$$


\begin{aligned} \lim_{x\to 0} \dfrac {\sin x}{x} &= \lim_{x\to0} \dfrac {[\sin x]'}{[x]'}\\\[5pt] &= \lim_{x\to 0} \dfrac {\cos x}{1}\\\[5pt] &= \cos 0\\\[5pt] &= 1. \end{aligned}


$$

### Example: Calculating a Limit Using L'Hopital's Rule

#### Question

Calculate $\displaystyle \lim_{x\rightarrow 3}\dfrac{x^3-27}{x-3}$.

#### Explanation

Note that plugging in $x=3$ gives the indeterminate form $\dfrac{0}{0}.$ However, we can use L'Hopital's rule to find this limit:

$$


\begin{aligned} \lim_{x\to 3} \dfrac {x^3-27}{x-3} &= \lim_{x\to3} \dfrac {[x^3-27]'}{[x-3]'}\\\[5pt] &= \lim_{x\to 3} \dfrac {3x^2}{1}\\\[5pt] &= 3(3)^2\\\[5pt] &= 27 \end{aligned}


$$

### Example: Calculating a Limit Using L'Hopital's Rule Twice

#### Question

Evaluate $\displaystyle \lim_{x\to 0} \, \frac {\sin^2 (2x)}{x^2}.$

#### Explanation

If we plug in $x=0$ we get the indeterminate form $\dfrac{0}{0},$ so we apply L'Hopital's rule to find the limit:

$$


\begin{aligned} \lim_{x\to0} \dfrac{\sin^2 (2x)}{x^2} &= \lim_{x\to 0} \dfrac {\left[\sin^2 (2x)\right]'}{[x^2]'}\\\[5pt] &= \lim_{x\to 0} \dfrac{2\cdot \sin (2x) \cdot\cos (2x)\cdot 2}{2x}\\\[5pt] &= \lim_{x\to 0}{2\cos (2x)} \cdot \lim_{x\to 0} \dfrac{\sin (2x)}{x}\\\[5pt] &= 2\cos(2\cdot 0)\lim_{x\to 0}\dfrac{\sin (2x)}{x}\\\[5pt] &= 2\lim_{x\to 0}\dfrac{\sin (2x)}{x} \end{aligned}


$$

This time, the resulting limit still gives the indeterminate form $\dfrac{0}{0}.$ But that's okay, because we can just apply L'Hopital's rule again! We get

$$


\begin{aligned} \lim_{x\to0} \dfrac{\sin^2 (2x)}{x^2} &= 2\lim_{x\to 0}\dfrac{\sin (2x)}{x}\\\[5pt] &= 2\lim_{x\to0} \dfrac {[\sin (2x)]'}{[x]'}\\\[5pt] &= 2\lim_{x\to0} \dfrac {2\cos (2x)}{1}\\\[5pt] &= 4\cos(2\cdot 0)\\&=4. \end{aligned}


$$

### L'Hopital's Rule for the Case of Infinity Divided by Infinity

We can also use L'Hopital's rule to deal with the indeterminate form $\dfrac{\infty}{\infty}$. In this case, L'Hopital's rule states that if $\displaystyle\lim_{x\rightarrow a}f(x) = \pm\infty$ and $\displaystyle\lim_{x\rightarrow a}g(x) = \pm\infty,$ then

$$


\lim_{x\to a} \dfrac {f(x)}{g(x)} = \lim_{x\to a} \frac {f'(x)}{g'(x)},


$$

provided that $f$ and $g$ are both differentiable at $x=a,$ and the limit $\displaystyle \lim_{x\to a} \frac {f'(x)}{g'(x)}$ exists.

### Example: Calculating an Indeterminate Limit of the Form Infinity Divided by Infinity Using L'Hopital's Rule

#### Question

Evaluate $\displaystyle \lim_{x\to 0} \dfrac{\ln\left(x^2\right)}{\left(\dfrac{2}{x^2}\right)}.$

#### Explanation

Here the limits of the numerator and denominator are $\displaystyle \lim_{x\to 0} \ln\left(x^2\right) = -\infty$ and $\displaystyle \lim_{x\to 0} \dfrac{2}{x^2} = \infty$ respectively, so we have the case $\dfrac{-\infty}{\infty}$.

Applying L'Hopital's rule, we obtain

$$


\begin{aligned} \lim_{x\to 0} \dfrac{\ln\left(x^2\right)}{\left(\dfrac{2}{x^2}\right)} &= \lim_{x\to 0} \dfrac{[\ln\left(x^2\right)]'}{\left(\dfrac{2}{x^2}\right)'}\\\[5pt] &= \lim_{x\to 0} \dfrac{\left(1/x^2\right)\cdot 2x}{-\left({4}/{x^3}\right)}\\\[5pt] &= \lim_{x\to 0} \dfrac{x^{-2} \cdot 2x}{-4x^{-3} }\\\[5pt] &= \lim_{x\to 0} \dfrac{2x^{-1}}{-4x^{-3} }\\\[5pt] &= -\dfrac{1}{2} \lim_{x\to 0} {x^2}\\\[5pt] &= -\dfrac{1}{2}\cdot 0\\\[5pt] &= 0. \end{aligned}


$$

### L'Hopital's Rule for Limits at Positive or Negative Infinity

L'Hopital's rule can be extended to the case in which the limit is taken as $x\rightarrow \pm\infty.$ In this case, L'Hopital's rule states that if either

- $\displaystyle\lim_{x\rightarrow \pm\infty}f(x) = \pm \infty$ and $\displaystyle\lim_{x\rightarrow \pm\infty}g(x) = \pm \infty,$ or

- $\displaystyle\lim_{x\rightarrow \pm\infty}f(x) = 0$ and $\displaystyle\lim_{x\rightarrow \pm\infty}g(x) = 0,$

then

$$


\ \lim_{x\to \pm\infty} \dfrac {f(x)}{g(x)} = \lim_{x\to \pm\infty} \frac {f'(x)}{g'(x)},


$$

provided that $f$ and $g$ are both differentiable for all sufficiently large $x,$ and the limit $\displaystyle\lim_{x\to \pm\infty} \frac {f'(x)}{g'(x)}$ exists.

### Example: Calculating a Limit at Positive or Negative Infinity Using L'Hopital's Rule

#### Question

Evaluate ${\displaystyle \lim_{x\to\infty} \frac {x^6}{5x^6-4}}.$

#### Explanation

In this case, we have an indeterminate form of type $\dfrac{\infty}{\infty},$ so applying L'Hopital's rule yields

$$


\begin{aligned} \lim_{x\to \infty} \dfrac {x^6}{5x^6-4} &= \lim_{x\to\infty} \dfrac {[x^6]'}{[5x^6-4]'}\\&= \lim_{x\to \infty} \dfrac {6x^5}{5(6x^5)-0}\\&= \lim_{x\to \infty} \dfrac {1}{5}\\&= \dfrac{1}{5}. \end{aligned}


$$

### The General Theorem

In this lesson, we started out with a special case of L'Hopital's rule (the case of $\dfrac{0}{0}$ as $x \to a$) and gradually introduced more cases. In closing, we will state the full version of L'Hopital's rule.

Suppose that

$$


\lim\limits_{x \to a} \dfrac{f(x)}{g(x)} = \dfrac{0}{0} \quad \textrm{or} \quad \lim\limits_{x \to a} \dfrac{f(x)}{g(x)} = \dfrac{\pm \infty}{\pm \infty},


$$

where $a$ is any real number, or $\pm \infty.$ Then we have

$$


\lim_{x\to a} \dfrac {f(x)}{g(x)} = \lim_{x\to a} \frac {f'(x)}{g'(x)},


$$

provided that the following conditions are met:

- If $a$ is a real number, and $f$ and $g$ are both differentiable at $x=a,$ then the limit $\displaystyle \lim_{x\to a} \frac {f'(x)}{g'(x)}$ exists.

- If $a$ is $\pm \infty,$ and $f$ and $g$ are both differentiable for all sufficiently large $x,$ then the limit $\displaystyle\lim_{x\to \pm\infty} \frac {f'(x)}{g'(x)}$ exists.

When working with familiar functions like polynomials, trigonometric functions, exponential functions, logarithmic functions, etc, it's safe to assume that these conditions are met.
