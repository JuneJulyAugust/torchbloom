# Calculating Limits of Radical Functions Using Conjugate Multiplication

Source: https://www.mathacademy.com/topics/604?courseId=24
Topic ID: 604

## Prerequisites

- [The Power and Root Rules for Limits](./37-the-power-and-root-rules-for-limits.md)
- [Calculating Limits of Rational Functions by Factoring](./1813-calculating-limits-of-rational-functions-by-factoring.md)
- [Adding and Subtracting Radical Expressions](../../../high-school/traditional/lessons/algebra-i/3756-adding-and-subtracting-radical-expressions.md)
- [Further Rationalizing Denominators of Algebraic Expressions](../../../high-school/traditional/lessons/algebra-i/6185-further-rationalizing-denominators-of-algebraic-expressions.md)

## Lesson

### Introduction

Suppose that we want to calculate the following limit:

$$


\lim_{x \to 1} \frac{\sqrt{x} - 1}{x - 1}


$$

If we try to evaluate the limit by directly substituting $x=1,$ we get an indeterminate form:

$$


\begin{aligned}\underset{𝑥→1}{lim}\frac{\sqrt{𝑥}−1}{𝑥−1} & =\frac{\sqrt{1}−1}{1−1}=\frac{0}{0}\end{aligned}


$$

However, if we simplify the fraction before evaluating the limit, we obtain a more clear result. To simplify the fraction, we can multiply the numerator and the denominator of the function by the **conjugate** of the numerator.

To obtain the conjugate of $\sqrt{x}-1,$ we simply switch the sign between the two terms to get $\sqrt{x}+ 1.$

$$


\begin{aligned}  \lim_{x\to 1} \frac{\sqrt{x} - 1} {x - 1} &= \lim_{x\to 1} \frac{\sqrt{x} - 1} {x - 1} \cdot\dfrac{\sqrt{x} + 1}{\sqrt{x} + 1} \\&=\lim_{x\to 1} \dfrac{(\sqrt{x} - 1)(\sqrt{x} +1)} {(x-1)(\sqrt{x} + 1)}\\&=\lim_{x\to 1} \dfrac{\left(\sqrt{x}\right)^2 - 1^2} {(x-1)(\sqrt{x} + 1)}\\&=\lim_{x\to 1} \dfrac{x-1} {(x-1)(\sqrt{x} + 1)}\\&=\lim_{x\to 1} \dfrac{x-1} {(x-1)(\sqrt{x} + 1)}\\&=\lim_{x\to 1} \dfrac1{\sqrt{x} + 1}\\&=\dfrac{1}{\sqrt{1} +1}\\&=\dfrac{1}{2} \end{aligned}


$$

### Example: Calculating the Limit of a Rational Function with a Radical in the Numerator

#### Question

Evaluate $\displaystyle{\lim_{x \to 4^+} \dfrac {x - 2\sqrt{x}} {x - 4}}.$

#### Explanation

If we attempt to evaluate the limit, we get an indeterminate form:

$$


\begin{aligned}\underset{𝑥→4^{+}}{lim}\frac{𝑥−2\sqrt{𝑥}}{𝑥−4} & =\frac{4−2\sqrt{4}}{4−4}=\frac{0}{0},\end{aligned}


$$

So, we need to first simplify the limit. Since the radical is in the numerator, we can multiply the numerator and the denominator by the conjugate of the numerator. We get

$$


\begin{aligned} \lim_{x \to 4^+} \dfrac {x - 2\sqrt{x}} {x - 4} &= \lim_{x \to 4^+} \dfrac {(x -2 \sqrt{x})(x+2\sqrt x)} {(x - 4)(x+2\sqrt x)} \\&= \lim_{x \to 4^+} \dfrac {x^2-\left(2\sqrt{x}\right)^2} {(x - 4)(x+2\sqrt x)} \\&= \lim_{x \to 4^+} \dfrac {x^2-4x} {(x - 4)(x+2\sqrt x)} \\&= \lim_{x \to 4^+} \dfrac {x(x-4)} {(x - 4)(x+2\sqrt x)} \\&= \lim_{x \to 4^+} \dfrac {x} {x+2\sqrt x} \\&= \lim_{x \to 4^+} \dfrac {4} {4+2\sqrt4} \\&=\dfrac 1 2. \end{aligned}


$$

### Example: Calculating the Limit of a Rational Function with a Radical in the Denominator

#### Question

Calculate $\displaystyle{\lim_{x \to 0} \dfrac {3x} {\sqrt{x +1} -1}}.$

#### Explanation

If we attempt to evaluate the limit by simply evaluating the function at $x=0$, we get an indeterminate form:

$$


\begin{aligned}\underset{𝑥→0}{lim}\frac{3𝑥}{\sqrt{𝑥+1}−1} & =\frac{3⋅0}{\sqrt{0+1}−1}=\frac{0}{0}\end{aligned}


$$

So, we need to first simplify the limit. Since the radical is in the denominator, we can multiply the numerator and the denominator by the conjugate of the denominator. We get

$$


\begin{aligned} \lim_{x \to 0} \dfrac {3x} {\sqrt{x + 1} - 1} &=\lim_{x\to 0}\frac{(3x)(\sqrt{x+1}+1)}{(\sqrt{x + 1} - 1)(\sqrt{x+1}+1)}\\&=\lim_{x\to 0}\frac{3x(\sqrt{x+1}+1)}{\left(\sqrt{x+1}\right)^2-1^2}\\&=\lim_{x\to 0}\frac{3x(\sqrt{x+1}+1)}{x+1-1}\\&=\lim_{x\to 0}\frac{3x(\sqrt{x+1}+1)}{x}\\&=\lim_{x\to 0}3(\sqrt{x+1}+1)\\&=3(\sqrt{0+1}+1)\\&=6. \end{aligned}


$$
