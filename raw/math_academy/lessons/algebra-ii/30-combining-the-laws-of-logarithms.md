# Combining the Laws of Logarithms

Source: https://www.mathacademy.com/topics/30?courseId=51
Topic ID: 30

## Prerequisites

- [The Quotient Rule for Logarithms](./1474-the-quotient-rule-for-logarithms.md)
- [The Power Rule for Logarithms](./1475-the-power-rule-for-logarithms.md)

## Lesson

### Introduction

Recall that logarithms that share a common base $n$ obey the following three laws:

- **The Product Rule**

- **The Quotient Rule**

- **The Power Rule**

We can use these laws together to simplify a logarithmic expression.

For instance, we can write $3\log_2(x) + \dfrac 1 2 \log_2(y)$ as an expression containing a single term.

First, using the power rule, we can write

$$



\begin{aligned}
3\log_2(x) + \dfrac{1}{2}\log_2(y)
  &= \log_2\left(x^3\right) + \log_2\left(y^{1/2}\right) \\
  &= \log_2\left(x^3\right) + \log_2\left(\sqrt{y}\right).
\end{aligned}



$$

Now, using the product rule, we get

$$



\log_2\left(x^3\right) + \log_2 \left(\sqrt{y}\right) = \log_2 \left(x^3\sqrt{y}\right).



$$

Therefore,

$$



3\log_2(x) + \dfrac 1 2 \log_2(y) = \log_2 \left(x^3\sqrt{y}\right).



$$

### Example: Rewriting an Expression Using the Product and Quotient Rules of Logarithms

#### Question

Express $\ln(2)+\ln(x)-\ln(y)$ as a single logarithm.

#### Explanation

Using the product rule for natural logarithms, we can combine the first two terms of the given expression as follows:

$$



\begin{aligned}ln⁡(2)+ln⁡(𝑥)−ln⁡(𝑦)=ln⁡(2𝑥)−ln⁡(𝑦)\end{aligned}



$$

Now, using the quotient rule for natural logarithms, we get

$$



\ln(2x)-\ln(y) = \ln \left( \dfrac{2x}{y} \right).



$$

Therefore,

$$



\ln(2)+\ln(x)-\ln(y) = \ln\left(\dfrac{2x}{y}\right).



$$

### Example: Rewriting an Expression Using the Product and Power Rules of Logarithms

#### Question

Express $\log(3)+4\log(y)$ as a single logarithm.

#### Explanation

Using the power rule for logarithms, we can rewrite the second term to obtain

$$



\log(3)+4\log(y)=\log(3)+\log(y^4).



$$

Now, using the product rule for logarithms, we can combine the two terms to get

$$



\log(3)+\log(y^4)=\log\left(3y^4\right).



$$

Therefore,

$$



\log(3)+4\log(y)=\log\left(3y^4\right).



$$

### Example: Rewriting an Expression Using the Quotient and Power Rules of Logarithms

#### Question

Express $3\log(x) - 2\log(5)$ as a single logarithm.

#### Explanation

Using the power rule for logarithms, we can rewrite both terms of the expression as follows:

$$



\begin{aligned}3log⁡(𝑥)−2log⁡(5) & =log⁡(𝑥^{3})−log⁡(5^{2}) \\ & =log⁡(𝑥^{3})−log⁡(25)\end{aligned}



$$

Now, using the quotient rule for logarithms, we can combine the two terms to get

$$



\log\left(x^3\right) - \log(25) =\log\left( \dfrac{x^3}{25} \right).



$$

Therefore,

$$



3\log(x) - 2\log(5) = \log\left( \dfrac{x^3}{25} \right).



$$

### Example: Rewriting an Expression Using the Product, Quotient, and Power Rules of Logarithms

#### Question

Express $3\log(2)+\log(x)-\log(4)$ as a single logarithm.

#### Explanation

Using the power rule for logarithms, we can rewrite the first term of the given expression as follows:

$$



\begin{aligned}3log⁡(2)+log⁡(𝑥)−log⁡(4) & =log⁡(2^{3})+log⁡(𝑥)−log⁡(4) \\ & =log⁡(8)+log⁡(𝑥)−log⁡(4)\end{aligned}



$$

Now, using the product rule for logarithms, we can combine the first two terms to obtain

$$



\begin{aligned}log⁡(8)+log⁡(𝑥)−log⁡(4)=log⁡(8𝑥)−log⁡(4).\end{aligned}



$$

Finally, using the quotient rule for logarithms, we get

$$



\begin{aligned}log⁡(8𝑥)−log⁡(4) & =log⁡(\frac{8𝑥}{4}) \\ & =log⁡(2𝑥).\end{aligned}



$$

Therefore,

$$



3\log(2)+\log(x)-\log(4) = \log\left(2x\right).



$$
