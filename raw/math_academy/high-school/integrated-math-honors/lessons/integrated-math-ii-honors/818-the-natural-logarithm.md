# The Natural Logarithm

Source: https://www.mathacademy.com/topics/818?courseId=128
Topic ID: 818

## Prerequisites

- [Evaluating Logarithms](../../../traditional/lessons/algebra-ii/378-evaluating-logarithms.md)
- [Degrees of Accuracy](../../../traditional/lessons/algebra-i/2234-degrees-of-accuracy.md)
- [Rational Numbers as Finite or Repeating Decimals](../../../../middle-school/lessons/grade-7/7011-rational-numbers-as-finite-or-repeating-decimals.md)

## Lesson

### Introduction

**Euler’s number**, denoted $e,$ is one of the most important constants in mathematics. It's an irrational number, and its numerical value is approximately

$$


e\approx2.718\,281\,828.


$$

The **natural logarithm**, denoted $\ln,$ is a special logarithm whose base is equal to Euler's number:

$$


\ln a = \log_e a


$$

In other words, the natural logarithm of $a$ is defined as follows:

$\ln{a} = x$ is equivalent to $a = e^x$

Everything we've done with logarithms can be applied to the natural logarithm.

For instance, we can express $e^3 \approx 20.086$ in logarithmic form. If we compare $e^{3} \approx 20.086$ with $a = e^x,$ we get $a = 20.086$ and $x = 3.$ Therefore,

$$


e^3\approx 20.086\quad \text{is equivalent to}\quad \ln(20.086) \approx 3.


$$

Note:

- Scientific calculators usually have a special key that allows $\ln a$ to be computed for specific values of $a.$

- Euler's number shows up in many different areas, including compound interest, population growth, and calculus. For now, it’s enough to know that $e$ is a natural base for logarithms and exponentials. We’ll meet this number often in future lessons, where its deeper significance will become clear.

### Example: Converting Between Exponential and Logarithmic Form With Natural Logarithms

#### Question

Convert the expression $\ln{3} \approx 1.1$ to its equivalent exponential form.

#### Explanation

The natural logarithm of $a$ is defined as follows:

$\ln{a} = x$ is equivalent to $a = e^x$

If we compare $\ln{3} \approx 1.1$ with $\ln{a} = x,$ we get $a = 3$ and $x = 1.1.$

Therefore, the approximation $\ln{3} \approx 1.1$ is equivalent to

$$


e^{1.1} \approx 3 .


$$

### Example: Evaluating Natural Logarithms

#### Question

Evaluate $\ln\left(e^{6}\right).$

#### Explanation

The natural logarithm of a power of $e$ is the power itself:

$$


\ln(e^x) = x


$$

In our case, we have $x = 6.$ Therefore,

$$


\ln\left( e^{6}\right) = 6.


$$

### Example: Evaluating Natural Logarithms of Fractions and Roots

#### Question

Evaluate $\ln\left(\dfrac{1}{e^{3}}\right).$

#### Explanation

First, we rewrite $\dfrac{1}{e^3}$ as a power of $e$ (the base of the natural logarithm) as follows:

$$


\dfrac{1}{e^3} = e^{-3}


$$

Therefore, we have

$$


\ln\left( \dfrac{1}{e^3} \right) = \ln \left( e^{-3} \right).


$$

The natural logarithm of a power of $e$ is the power itself:

$$


\ln(e^x) = x


$$

In our case, we have $x = -3.$ Therefore,

$$


\ln\left( e^{-3}\right) = - 3.


$$

### Example: Evaluating Expressions Containing Natural Logarithms Using a Calculator

#### Question

Rounded to $2$ decimal places, what is the value of $\dfrac{4}{\ln(2)}?$

#### Explanation

We compute the required expression to $2$ decimal places using a calculator, rounding the intermediate steps to $5$ decimal places to avoid rounding error. This gives

$$


\begin{aligned}\frac{4}{ln⁡(2)} & ≈\frac{4}{0.693\,15} \\ & ≈5.770\,76 \\ & ≈5.77.\end{aligned}


$$
