# Continuously Compounded Interest

Source: https://www.mathacademy.com/topics/237?courseId=128
Topic ID: 237

## Prerequisites

- [Solving Equations Containing the Exponential Function](../algebra-ii/870-solving-equations-containing-the-exponential-function.md)
- [Modeling With Compound Interest](../algebra-ii/1481-modeling-with-compound-interest.md)

## Lesson

### Introduction

Suppose that some money $P_0$ is deposited into a bank account. We know the bank balance $P$ after $t$ years is given by the formula

$$


\begin{aligned} P &= P_0\left(1 + \dfrac r n \right)^{nt}, \end{aligned}


$$

where $r$ is the annual interest rate, and $n$ is the number of times payments are compounded per year.

Now suppose that we increase the number of compounding periods per year so that compounding occurs *at every instant.* We call this **continuous compounding.** When continuous compounding occurs, we can determine the balance $P$ at time $t$ using the **continuously compounded growth equation**, given by

$$


\begin{aligned} P &= P_0e^{rt}, \end{aligned}


$$

where $e\approx 2.718$ is Euler's number. We'll go into a little more detail regarding where this formula comes from at the end of the lesson.

For example, suppose that a company has $450\,000$ in the bank and that the balance grows at an annual rate of $4.5\%,$ continuously compounded. Then, to calculate the bank balance $5$ years from now, we can use the continuously compounded growth equation.

In this situation, we have an initial balance $P_0= 450\,000,$ a growth rate of $r= 4.5\% = 0.045,$ and $t=5$ years. Substituting these values into the formula, we obtain

$$


\begin{aligned} P &= P_0e^{rt} \\[3pt] &= (450\,000)e^{(0.045)(5)} \\[3pt] &= (450\,000)e^{0.225} \\[3pt] &= (450\,000)(1.252\,322\,716) \\[3pt] &\approx 563\,545. \end{aligned}


$$

So, the balance in $5$ years will be approximately $563\,545.$

The rate $r$ in the continuously compounded growth equation does not have to be an annual rate. It can be over any amount of time. The time $t$ inherits its unit from the rate.

### Example: Calculating a Final Amount After Continuous Compounding Is Applied

#### Question

An asset has been depreciating in value for the past $10$ years at an annual, continuously-compounded rate of $6\%.$ If that asset was initially worth $13\,500,$ what is it worth now? Round your answer to the nearest dollar.

#### Explanation

The continuously compounded growth equation is

$$


\begin{aligned} P &= P_0e^{rt}. \end{aligned}


$$

We have an initial amount of $P_0=13\,500,$ a rate of $r=-0.06,$ and a time duration of $t=10$ years. Substituting these values into the formula, we get

$$


\begin{aligned} P &= P_0e^{rt} \\&= 13\,500e^{(-0.06)(10)} \\[3pt] &= 13\,500e^{-0.6} \\[3pt] &= 13\,500(0.548\,81...) \\[3pt] &\approx 7\,409. \end{aligned}


$$

Therefore, after $10$ years, the value of the asset has decreased to $7\,409.$

### Example: Calculating an Initial Amount

#### Question

In a lab, a certain type of bacteria grows at a continuous rate of $5.2\%$ per day. If, after $2$ weeks, the number of bacteria is $20\,500,$ what was the initial number of bacteria $2$ weeks ago? Round your answer to the nearest whole number.

#### Explanation

The continuously compounded growth equation is

$$


\begin{aligned} P &= P_0e^{rt}. \end{aligned}


$$

We have a final amount of $P=20\,500,$ a rate of $r=0.052,$ and a time duration of $t=14$ days. Substituting these values into the formula and solving for $P_0,$ we get

$$


\begin{aligned}𝑃 & =𝑃_{0}𝑒^{𝑟𝑡} \\ 20\,500 & =𝑃_{0}𝑒^{(0.052)(14)} \\ 20\,500 & =𝑃_{0}𝑒^{0.728} \\ 20\,500 & =𝑃_{0}(2.070\,93...) \\ 𝑃_{0} & =\frac{20\,500}{2.070\,93...} \\ 𝑃_{0} & ≈9\,899.\end{aligned}


$$

Therefore, there were $9\,899$ bacteria initially.

### Example: Calculating a Rate or Time Duration

#### Question

Nine years ago, an organization had $4\,350$ members. Today it has $7\,210$ members. What was its continuously compounded rate of growth during this nine-year period? Round your answer to $1$ decimal place.

#### Explanation

The continuously compounded growth equation is

$$


P = P_0e^{rt}.


$$

We have an initial amount of $P_0=4\,350,$ a final amount of $P=7\,210,$ and a time duration of $t=9$ years. Substituting these values into the formula and solving for $r,$ we get

$$


\begin{aligned}𝑃 & =𝑃_{0}𝑒^{𝑟𝑡} \\ 7\,210 & =(4\,350)𝑒^{𝑟(9)} \\ 𝑒^{9𝑟} & =\frac{7\,210}{4\,350} \\ 𝑒^{9𝑟} & =1.657\,47... \\ ln⁡(𝑒^{9𝑟}) & =ln⁡(1.657\,47...) \\ 9𝑟 & =0.505\,29... \\ 𝑟 & =0.056\,14...≈5.6\%.\end{aligned}


$$

Therefore, continuously compounded rate of growth is $5.6\%.$

### The Relationship Between Continuous Compounding and the Compound Interest Equation

The formula for continuously compounded growth, given by

$$


P=P_0 e^{rt}


$$

is actually equal to the compound interest equation

$$


\begin{aligned} P &= P_0 \left(1 + \dfrac r n \right)^{nt}, \end{aligned}


$$

for extremely large $n$ (in other words, as $n \rightarrow \infty$).

To demonstrate, let's take the case of $P_0=1,$ $r=1,$ and $t=1.$ Then the formula for continuously compounded growth gives

$$


\begin{aligned}𝑃 & =𝑃_{0}𝑒^{1⋅1} \\ & =1𝑒^{1⋅1} \\ & =𝑒 \\ & =2.7182818…\end{aligned}


$$

and the compound interest equation is

$$


\begin{aligned}𝑃 & =𝑃_{0}(1+\frac{𝑟}{𝑛})^{𝑛𝑡} \\ & =1(1+\frac{1}{𝑛})^{𝑛⋅1} \\ & =(1+\frac{1}{𝑛})^{𝑛}.\end{aligned}


$$

If we substitute a large value of $n,$ say $n=1\,000\,000,$ then we get

$$


\begin{aligned}𝑃 & =(1+\frac{1}{1\,000\,000})^{1\,000\,000} \\ & =(1.000001)^{1\,000\,000} \\ & ≈2.718280 \\ & ≈𝑒.\end{aligned}


$$

This result matches up nicely with our result from the formula for continuously compounded growth!

Here, we demonstrated that the result holds for the special case where $P_0=r=t=1.$ However, it is possible to show that the formula is always true.
