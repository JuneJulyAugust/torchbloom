# The Change of Base Formula for Logarithms

Source: https://www.mathacademy.com/topics/28?courseId=133
Topic ID: 28

## Prerequisites

- [The Common Logarithm](../../../traditional/lessons/algebra-ii/726-the-common-logarithm.md)
- [The Natural Logarithm](../../../traditional/lessons/algebra-ii/818-the-natural-logarithm.md)

## Lesson

### Introduction

Suppose we wish to evaluate $\log_{4}9,$ but our calculator only has a key for the common logarithm $\log$ (base $10$).

In such cases, we can use the **change of base formula**, which states that

$$


\log_a X = \dfrac {\log_b X} {\log_b a}.


$$

It effectively allows us to change a logarithm from one base, $a,$ to another, $b.$ Note that $X,$ $a,$ and $b$ have to be all greater than zero and that $a \ne 1,$ $b \ne 1.$

We usually choose the value of base $b$ that makes the problem easier. In particular, if we need to evaluate the expression using a calculator, we choose $b=10$ or $b=e$.

For example, to evaluate $\log_{4}9$ using this formula, we can rewrite the logarithm from base $a=4$ to base $b=10.$ This gives

$$


\begin{aligned}log_{4}⁡9 & =\frac{log⁡9}{log⁡4} \\ & ≈\frac{0.954\,242}{0.602\,059} \\ & =1.585\end{aligned}


$$

rounded to $3$ decimal places.

### Example: Rewriting a Logarithm Using the Change of Base Formula

#### Question

Which of the following is equivalent to $\log x?$

1. $\dfrac {\log_{2} x} {\log_{2} 10}$

2. $\dfrac {\log_{2} 10} {\log_{2} x}$

3. $\log_{2}\left(\dfrac{x}{10}\right)$

#### Explanation

The change of base formula for logarithms is

$$


\log_a X = \dfrac {\log_b X} {\log_b a}.


$$

The change of base formula works with any new base. In this example, the choices are written using base $2,$ so we rewrite $\log x$ in terms of $\log_2.$ This gives

$$


\begin{aligned}log⁡𝑥 & =log_{10}⁡𝑥 \\ & =\frac{log_{2}⁡𝑥}{log_{2}⁡10}.\end{aligned}


$$

So, the correct answer is "I only."

### Example: Evaluating a Logarithm With a Calculator Using the Change of Base Formula

#### Question

Use a calculator to evaluate $\log_3 (7)$ rounded to $2$ decimal places.

#### Explanation

Let's calculate $\log_3 (7)$ by changing the base $3$ to the common logarithm (base $10$).

We use the change of base formula:

$$


\log_a X = \dfrac {\log_b X} {\log_b a}


$$

In our case, we have $a=3,$ $X =7,$ and $b=10.$ So, we have

$$


\begin{aligned}log_{3}⁡(7) & =\frac{log_{10}⁡(7)}{log_{10}⁡(3)} \\ & =\frac{log⁡(7)}{log⁡(3)} \\ & ≈\frac{0.845\,10}{0.477\,12} \\ & ≈1.77.\end{aligned}


$$

### Example: Evaluating a Logarithm Without a Calculator Using the Change of Base Formula

#### Question

Calculate $\log_{16}(32)$ without using a calculator.

#### Explanation

We use the change of base formula:

$$


\log_a X = \dfrac {\log_b X} {\log_b a}


$$

In our case, we have $a=16$ and $X =32.$ Since both $a$ and $X$ are powers of $2,$ we set $b=2.$ So, we have

$$


\begin{aligned}log_{16}⁡(32) & =\frac{log_{2}⁡(32)}{log_{2}⁡(16)} \\ & =\frac{log_{2}⁡(2^{5})}{log_{2}⁡(2^{4})} \\ & =\frac{5}{4}.\end{aligned}


$$
