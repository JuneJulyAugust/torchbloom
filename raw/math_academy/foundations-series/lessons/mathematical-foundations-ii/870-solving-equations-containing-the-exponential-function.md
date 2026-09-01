# Solving Equations Containing the Exponential Function

Source: https://www.mathacademy.com/topics/870?courseId=111
Topic ID: 870

## Prerequisites

- [Solving Exponential Equations Using Logarithms](./1482-solving-exponential-equations-using-logarithms.md)

## Lesson

### Introduction

Suppose we are given an equation containing an exponential function, such as

$$


e^{t}= 12.


$$

We can solve it in the same way that we usually solve exponential equations, by taking the log on both sides where the base of the logarithm is the base of the exponential.

Here, the base of the exponential is $e,$ so we take the *natural* logarithm of both sides, since

$$


\log_e{x} = \ln{x}.


$$

Taking the natural logarithm of both sides, we have that

$$


\begin{aligned}𝑒^{𝑡} & =12 \\ ln⁡(𝑒^{𝑡}) & =ln⁡(12).\end{aligned}


$$

Now, we use the fact that $\ln \left(e^a \right) = a$ to simplify the left-hand side. This gives

$$


t = \ln (12).


$$

This is the solution! We often present the solution of an exponential equation as an exact solution in logarithmic form.

### Example: Finding Exact Solutions to Exponential Equations Using the Natural Logarithm

#### Question

What is the value of $x$ if $e^{x - 3}=2^5?$

#### Explanation

First, we take the natural logarithm $\left(\ln\right)$ of both sides of the equation:

$$


\begin{aligned}𝑒^{𝑥−3} & =2^{5} \\ ln⁡(𝑒^{𝑥−3}) & =ln⁡(2^{5})\end{aligned}


$$

Now, we use the fact that $\ln \left(e^a \right) = a$ to simplify the left-hand side. This gives

$$


x-3 = \ln \left( 2^5 \right).


$$

Finally, we solve for $x$ and rewrite the right-hand side using the power law of logarithms, as follows:

$$


\begin{aligned}𝑥−3 & =ln⁡(2^{5}) \\ 𝑥 & =ln⁡(2^{5})+3 \\ 𝑥 & =5ln⁡(2)+3\end{aligned}


$$

Therefore, the solution is $x=5\ln (2) + 3.$

### Example: Finding Approximate Solutions to Exponential Equations Using the Natural Logarithm

#### Question

Find the solution to the equation $e^{2-4x} = 2$ rounded to $3$ decimal places.

#### Explanation

First, we take the natural logarithm $(\ln)$ of both sides of the equation and solve for $x\mathbin{:}$

$$


\begin{aligned}𝑒^{2−4𝑥} & =2 \\ ln⁡(𝑒^{2−4𝑥}) & =ln⁡(2) \\ 2−4𝑥 & =ln⁡(2) \\ −4𝑥 & =ln⁡(2)−2 \\ 𝑥 & =\frac{1}{2}−\frac{ln⁡(2)}{4}\end{aligned}


$$

Evaluating the above expression using a calculator gives

$$


x \approx 0.327


$$

rounded to $3$ decimal places.

### Example: Finding Solutions to Exponential Equations when Rearrangement is Required

#### Question

Given that $e^{x+1} + 1 = 3,$ what is the value of $x$?

#### Explanation

First, we isolate the exponential, as follows:

$$


\begin{aligned}𝑒^{𝑥+1}+1 & =3 \\ 𝑒^{𝑥+1} & =2\end{aligned}


$$

Then, we find the natural logarithm $\left(\ln\right)$ of both sides of the equation and solve for $x\mathbin{:}$

$$


\begin{aligned}𝑒^{𝑥+1} & =2 \\ ln⁡(𝑒^{𝑥+1}) & =ln⁡(2) \\ 𝑥+1 & =ln⁡(2) \\ 𝑥 & =ln⁡(2)−1\end{aligned}


$$

Therefore, the solution is $x =\ln\left(2\right) -1.$
