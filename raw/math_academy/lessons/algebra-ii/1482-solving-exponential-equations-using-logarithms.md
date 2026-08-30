# Solving Exponential Equations Using Logarithms

Source: https://www.mathacademy.com/topics/1482?courseId=51
Topic ID: 1482

## Prerequisites

- [The Change of Base Formula for Logarithms](./28-the-change-of-base-formula-for-logarithms.md)
- [Solving Exponential Equations](../algebra-i/391-solving-exponential-equations.md)
- [The Power Rule for Logarithms](./1475-the-power-rule-for-logarithms.md)

## Lesson

### Introduction

We can use logarithms to solve equations where the variable is in an exponent. For instance, suppose we are given the equation

$$



{\color{blue}2}^x=5.



$$

Notice that the base of the exponential is ${\color{blue}2}.$ So, if we take $\log_{\color{blue}2}$ of both sides of the equation, we have that

$$



\begin{aligned}log_{2}⁡(2^{𝑥}) & =log_{2}⁡(5).\end{aligned}



$$

Now, we can use the fact that $\log_{\color{blue}b} \left({\color{blue}b}^c \right) = c$ to simplify the left-hand side. This gives

$$



x = \log_{\color{blue}2} (5).



$$

This is the solution! We often present the solution of an exponential equation as an exact solution in logarithmic form.

Note that when taking the $\log_b$ of both sides of an exponential equation, we always use the base of the exponential as the base of the logarithm.

### Example: Finding Exact Solutions to Exponential Equations Using Logarithms

#### Question

Find the exact solution of the equation $2^{x+1}=3.$

#### Explanation

First, we take $\log_2$ of both sides of the equation:

$$



\begin{aligned}2^{𝑥+1} & =3 \\ log_{2}⁡(2^{𝑥+1}) & =log_{2}⁡(3)\end{aligned}



$$

Now, we use the fact that $\log_b \left(b^c \right) = c$ to simplify the left-hand side. This gives

$$



x+1 = \log_2 \left( 3 \right).



$$

Finally, we solve for $x,$ as follows:

$$



\begin{aligned}𝑥+1 & =log_{2}⁡(3) \\ 𝑥 & =log_{2}⁡(3)−1\end{aligned}



$$

Therefore, the solution is $x= \log_2 \left(3 \right) - 1.$

### Example: Finding Approximate Solutions to Exponential Equations Using Logarithms

#### Question

Given that $3^{2x+3}=5,$ find the value of $x$ rounded to $3$ decimal places.

#### Explanation

Taking $\log_3$ of both sides of the equation, we get

$$



\begin{aligned} 3^{2x+3} &= 5 \\[3pt] \log_3 \left(3^{2x+3}\right) &= \log_3 (5) \\[3pt] 2x+3 &= \log_3 (5) . \\[3pt] \end{aligned}



$$

Then, we rewrite the right-hand side using the change of base formula and solve for $x\mathbin{:}$

$$



\begin{aligned}2𝑥+3 & =\frac{log⁡(5)}{log⁡(3)} \\ 2𝑥 & =\frac{log⁡(5)}{log⁡(3)}−3 \\ 𝑥 & =\frac{log⁡(5)}{2log⁡(3)}−\frac{3}{2}\end{aligned}



$$

Evaluating the above expression using a calculator gives

$$



x \approx -0.768



$$

rounded to $3$ decimal places.

**** We used the change of base formula to rewrite the right-hand side, as many calculators can only compute base $10$ logarithms.

### Example: Finding Solutions to Exponential Equations when Rearrangement is Required

#### Question

Given that $3\cdot 6^{x} = 9,$ find the value of $x$ rounded to $3$ decimal places.

#### Explanation

First, we isolate the exponential on the left-hand side:

$$



\begin{aligned}3⋅6^{𝑥} & =9 \\ 6^{𝑥} & =3\end{aligned}



$$

Now, we take $\log_{6}$ of both sides of the equation:

$$



\begin{aligned} 6^x &= 3 \\[3pt] \log_6 \left(6^x\right) &= \log_6 (3) \\[3pt] x &= \log_6 (3)\\[3pt] \end{aligned}



$$

Next, we rewrite the right-hand side using the change of base formula:

$$



x = \dfrac{\log(3)}{\log(6)}



$$

Evaluating the above on a calculator gives

$$



x \approx 0.613



$$

rounded to $3$ decimal places.
