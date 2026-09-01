# Variance of Sums of Independent Random Variables

Source: https://www.mathacademy.com/topics/3062?courseId=73
Topic ID: 3062

## Prerequisites

- [Properties of Variance for Discrete Random Variables](./3028-properties-of-variance-for-discrete-random-variables.md)
- [Independence of Discrete Random Variables](./3048-independence-of-discrete-random-variables.md)

## Lesson

### Introduction

If $X$ and $Y$ are *independent* random variables, then

$$


\text{Var}{[X+Y]} = \text{Var}[X]+ \text{Var}[Y] ,


$$

and

$$


\text{Var}{[X-Y]} = \text{Var}[X] + \text{Var}[Y] .


$$

**Watch out!** When computing the variance of a *difference* of independent random variables, we *add* the variances!

### Example: Calculating the Variance of a Sum or Difference of Independent Random Variables

#### Question

For two independent random variables $X$ and $Y,$ we have $\text{Var}[X]=3$ and $\text{Var}[Y]=7.$ Find $\text{Var}[X-Y].$

#### Explanation

Recall that if $X$ and $Y$ are independent random variables, then

$$


\text{Var}[X\pm Y]=\text{Var}[X]+\text{Var}[Y].


$$

Substituting the given data into the formula above, we obtain

$$


\text{Var}[X-Y]= 3 + 7 = 10.


$$

### The Variance of a Sum of Scaled Random Variables

We have been using the fact that if $X$ and $Y$ are independent, then

$$


\text{Var}{[X+Y]} = \text{Var}[X]+ \text{Var}[Y] .


$$

Using the property that $\text{Var}[aX] = a^2\text{Var}[X],$ we can show that if $X$ and $Y$ are independent, then

$$


\text{Var}{[aX+bY]} = a^2\text{Var}[X]+ b^2\text{Var}[Y] ,


$$

where $a$ and $b$ are constants.

For example, for two independent random variables $X$ and $Y$, we have

$$


\begin{aligned}Var[4𝑋+3𝑌] & =4^{2}Var[𝑋]+3^{2}Var[𝑌] \\ & =16Var[𝑋]+9Var[𝑌]\end{aligned}


$$

Once again, we need to show caution when considering a difference. For example,

$$


\begin{aligned}Var[4𝑋−3𝑌] & =Var[4𝑋+(−3)𝑌] \\ & =4^{2}Var[𝑋]+(−3)^{2}Var[𝑌] \\ & =16Var[𝑋]+9Var[𝑌].\end{aligned}


$$

More generally, if the random variables $X_1, X_2,\ldots, X_n,$ are *mutually independent*, then

$$


\text{Var}\left[\sum_{i=1}^n a_i X_i\right] = \sum_{i=1}^n a_i^2\text{Var}[X_i].


$$

### Example: Calculating the Variance of a Sum of Scaled Random Variables

#### Question

For two independent random variables $X$ and $Y,$ we have $\text{Var}[X]=10$ and $\text{Var}[Y]=12.$ Find $\text{Var}\left[X-2Y\right].$

#### Explanation

Recall that if $X$ and $Y$ are independent variables, and $a$ and $b$ are constants, then

$$


\text{Var}[aX+bY]=a^2\text{Var}[X]+b^2\text{Var}[Y].


$$

Substituting the given data into the formula above, we obtain

$$


\text{Var}\left[X-2Y\right]=\left(1\right)^2\cdot 10+\left(-2\right)^2\cdot 12 =58.


$$

### Example: Calculating a Combined Variance Given Some Raw Moments

#### Question

Consider two independent random variables $X$ and $Y$ with expectations $\textrm E[X]=5,$ $\textrm E[Y]=4$ and second raw moments $\textrm E[X^2]=30$ and $\textrm E[Y^2]=18.$ Find the variance of $12X-11Y.$

#### Explanation

Recall that if $X$ and $Y$ are independent random variables and $a$ and $b$ are constants, then

$$


\text{Var}[aX+bY]=a^2\text{Var}[X]+b^2\text{Var}[Y].


$$

Also, the variance of a random variable $X$ is determined by the formula

$$


\textrm {Var}[X]=\textrm E[X^2]-\textrm E[X]^2.


$$

First, let's find $\text{Var}[X]\mathbin{:}$

$$


\begin{aligned}Var[𝑋] & =E[𝑋^{2}]−E[𝑋]^{2} \\ & =30−5^{2} \\ & =5.\end{aligned}


$$

Similarly,

$$


\begin{aligned}Var[𝑌] & =E[𝑌^{2}]−E[𝑌]^{2} \\ & =18−4^{2} \\ & =2.\end{aligned}


$$

Therefore,

$$


\begin{aligned}Var[12𝑋−11𝑌] & =12^{2}Var[𝑋]+(−11)^{2}Var[𝑌] \\ & =144(5)+121(2) \\ & =962.\end{aligned}


$$
