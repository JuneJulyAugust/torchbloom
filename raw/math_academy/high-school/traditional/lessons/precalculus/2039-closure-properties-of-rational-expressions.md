# Closure Properties of Rational Expressions

Source: https://www.mathacademy.com/topics/2039?courseId=43
Topic ID: 2039

## Prerequisites

- [Dividing Rational Expressions](../algebra-ii/436-dividing-rational-expressions.md)
- [Adding and Subtracting Rational Expressions](../algebra-ii/437-adding-and-subtracting-rational-expressions.md)
- [The Trigonometric Ratios](../geometry/609-the-trigonometric-ratios.md)
- [The Natural Logarithm](../algebra-ii/818-the-natural-logarithm.md)
- [Closure Properties of Polynomials](./942-closure-properties-of-polynomials.md)
- [Sums and Products of Rational and Irrational Numbers](../algebra-ii/2034-sums-and-products-of-rational-and-irrational-numbers.md)

## Lesson

### Introduction

A **rational expression** is an expression of the form

$$



\dfrac{P(x)}{Q(x)},



$$

where both $P$ and $Q$ are polynomials.

For example, the expressions

$$



\dfrac{x^3-5x+1}{1-x}, \qquad \dfrac{1}{x^2}



$$

are both rational expressions.

Moreover, any polynomial $P(x)$ is a rational expression since it can be written as

$$



\dfrac{P(x)}{1},



$$

where the denominator $Q(x) = 1$ is a polynomial.

However, the expression

$$



\dfrac{x\boxed{\color{blue}\ln(x)}}{x+x^3}



$$

is *not* a rational expression because the numerator is *not* a polynomial (it contains a logarithm).

### Example: Identifying Rational Expressions

#### Question

Which of the following are rational expressions?

1. $x^5-x^3+8$

2. $\dfrac{x^2-3}{x+6}$

3. $\dfrac{\sin(x+2)}{4}$

#### Explanation

An expression is rational if it can be expressed as a ratio of two polynomials.

Let's examine our expressions in turn.

- I is a rational expression. Indeed, we can write it as where both the numerator $x^5-x^3+8$ and the denominator $1$ are polynomials.

- II is a rational expression. Both the numerator $x^2-3$ and the denominator $x+6$ are polynomials.

- III is ** a rational expression. Notice that the numerator contains $\sin(x+2),$ which is ** a polynomial.

Therefore, the correct answer is "I and II only."

### Closure Properties of Rational Expressions

Rational expressions are *closed* under the arithmetic operations of addition, subtraction, multiplication, and division.

So, we have that:

- The *sum* of two rational expressions is a rational expression:

- The *difference* between two rational expressions is a rational expression:

- The *product* of two rational expressions is a rational expression:

- The *quotient* of two rational expressions is a rational expression: provided that the denominator is nonzero.

In this sense, rational expressions and rational numbers have similar properties.

### Powers of Rational Expressions

Rational expressions are closed when raised to *integer* powers since these can be reduced to repeated multiplication.

For example, let $S$ be a rational expression. Then:

- $S^3 = S \cdot S \cdot S$ is a rational expression.

- $S^{-2} = \dfrac{1}{S^2} = \dfrac{1}{S \cdot S}$ is a rational expression provided $S$ is not identical to zero.

However, rational expressions are *not* closed when raised to *non-integer* powers.

For example,

$$



S^{1/2} = \sqrt{S}



$$

is *not* rational for all rational $S$ because it contains a square root. For example, if

$$



S = \dfrac1x



$$

then

$$



S^{1/2} = \dfrac{1}{\sqrt x}



$$

which is not rational.

It's worth noting that $S^{1/2}$ *is* rational for *some* choices of $S.$ For example, if we let

$$



S = \dfrac{1}{x^2}



$$

then

$$



S^{3/2} = \left(\dfrac{1}{x^2}\right)^{1/2} = \dfrac{1}{x}



$$

which *is* rational. However, since at least one rational expression exists such that $S^{1/2}$ is not rational, the rational expressions are *not* closed under the square root operation.

In general, applying exponential, logarithmic, and trigonometric operations to a rational expression does not result in a rational expression. Let's see an example.

### Example: Identifying True Statements About Rational Expressions

#### Question

Let $S$ and $T$ be nonzero rational expressions. Which of the following statements are true for all possible $S$ and $T?$

1. $T +\ln(S)$ is a rational expression

2. $S \cdot \sqrt{T-1}$ is a rational expression

3. $S^2$ is a rational expression

#### Explanation

An expression is rational if it can be expressed as a ratio of two polynomials.

Moreover, rational expressions are analogous to rational numbers in that they're closed under addition, subtraction, multiplication, and division.

With that in mind, let's examine our statements in turn.

- Statement I is false. This is ** a rational expression for all $S$ and $T$ since it contains a logarithmic function, namely, $\ln(S).$

- Statement II is false. This is ** a rational expression for all $S$ and $T$ since it contains a square root, namely, $\sqrt{T-1}.$

- Statement III is true. First, notice that Integer powers can be reduced to multiplication, and rational expressions are closed under multiplication.

Therefore, the correct answer is "III only."
