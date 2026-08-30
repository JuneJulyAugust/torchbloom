# Converting Between Exponents

Source: https://www.mathacademy.com/topics/2047?courseId=134
Topic ID: 2047

## Prerequisites

- [The Power Rule for Exponents With Algebraic Expressions](../algebra-i/362-the-power-rule-for-exponents-with-algebraic-expressions.md)
- [Modeling With Compound Interest](../algebra-ii/1481-modeling-with-compound-interest.md)

## Lesson

### Introduction

One way of representing the fact that exponential and logarithmic functions are inverses is via the formula

$$


a = b^{\log_b{a}},


$$

where $a$ and $b$ are positive real numbers and $b\neq 1.$

One interesting application is to estimate the size of large numbers defined using powers.

For example, suppose we want to find an approximation of the following number:

$$


4^{60}


$$

It's hard to know how large this number is off the bat. However, we can get a better idea by writing this number as a power of $10\mathbin{:}$

$$


10^{\log(4^{60})}


$$

Applying the power rule to the argument of the logarithm and using the fact that $\log 4\approx 0.602,$ we get

$$


\begin{aligned}4^{60} & =10^{log⁡(4^{60})} \\ & =10^{60\,⋅\,log⁡4} \\ & ≈10^{60\,⋅\,0.602} \\ & ≈10^{36}.\end{aligned}


$$

From here, we can see that $4^{60}$ has around $37$ digits.

### Example: Estimating Large Numbers

#### Question

Estimate $2^{60}$ to the nearest integer power of $10.$

#### Explanation

Recall that $a = b^{\log_b{a}}$ since logarithms and exponential functions are inverses.

Therefore, we have

$$


\begin{aligned}2^{60} & =10^{log⁡(2^{60})} \\ & =10^{60\,⋅\,log⁡2} \\ & ≈10^{60\,⋅\,0.301} \\ & ≈10^{18}.\end{aligned}


$$

### Example: Transforming Exponential Functions

#### Question

Write $10^t \cdot 4^t$ as an approximate power of $10.$

#### Explanation

Recall that $a = b^{\log_b{a}}$ since logarithms and exponential functions are inverses.

Therefore, we have

$$


\begin{aligned}10^{𝑡}⋅4^{𝑡} & =10^{𝑡}⋅10^{log⁡(4^{𝑡})} \\ & =10^{𝑡}⋅10^{𝑡\,⋅\,log⁡4} \\ & ≈10^{𝑡}⋅10^{0.602𝑡} \\ & =10^{𝑡+0.602𝑡} \\ & =10^{(1+0.602)𝑡} \\ & =10^{1.602𝑡}.\end{aligned}


$$

### Equivalent Interest Rates

We can manipulate exponential functions to find equivalent interest rates.

Suppose that a particular investment offers an annual interest rate of $24 \%,$ compounded monthly. What is the equivalent interest rate for this investment if the interest were compounded yearly?

The first thing to realize is that the higher the compounding frequency, the greater the return (all other things being equal). Therefore, an interest rate for an investment compounded yearly should be *greater than* an equivalent rate compounded monthly. In other words, we expect our final answer to be greater than $24\%.$

Using the compound interest equation, if the initial deposit is $P_0,$ the total amount in the account after $t$ years will be equal to

$$


P = P_0 \cdot \left(1+\dfrac{0.24}{12}\right)^{12t} = P_0 \cdot (1.02)^{12t}.


$$

To determine the equivalent annual interest rate when compounding yearly, we transform the equation above using the power rule for exponents, as follows:

$$


\begin{aligned}𝑃 & =𝑃_{0}⋅(1.02)^{12𝑡} \\ & =𝑃_{0}⋅((1.02)^{12})^{𝑡} \\ & ≈𝑃_{0}⋅(1.268)^{𝑡} \\ & =𝑃_{0}⋅(1+\frac{0.268}{1})^{1⋅𝑡}\end{aligned}


$$

This represents the annual interest rate of ${\color{blue}0.268} = 26.8\%,$ compounding yearly.

### Example: Determining Equivalent Interest Rates

#### Question

A bank account pays $10 \%$ annual interest, compounded yearly. Find the equivalent annual interest rate when compounding monthly. Round your answer to the nearest tenth of a percent.

#### Explanation

If the initial deposit is $P_0,$ using the compound interest equation, the total amount on the account after $t$ years will be equal to

$$


P = P_0 \cdot \left(1+\dfrac{0.1}{1}\right)^t = P_0 \cdot (1.1)^t.


$$

To determine the equivalent annual interest rate when compounding monthly, we transform the equation above as follows:

$$


\begin{aligned}𝑃 & =𝑃_{0}⋅(1.1)^{𝑡} \\ & =𝑃_{0}⋅((1.1)^{1/12})^{12𝑡} \\ & ≈𝑃_{0}⋅(1.007\,974\,…)^{12𝑡} \\ & =𝑃_{0}⋅(1+0.007\,974\,…)^{12𝑡} \\ & =𝑃_{0}⋅(1+\frac{12⋅0.007\,974\,…}{12})^{12𝑡} \\ & ≈𝑃_{0}⋅(1+\frac{0.095\,689\,…}{12})^{12𝑡}.\end{aligned}


$$

This represents the annual interest rate of

$$


{\color{blue}0.095\,689\,\ldots} \approx 9.6\%


$$

when compounding monthly (${\color{red}12}$ times per year).
